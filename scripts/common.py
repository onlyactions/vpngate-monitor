"""Shared constants and helpers for the VPN Gate monitor pipeline.

Pipeline layout:

  fetch.py     -- stage 1-5: fetch the VPN Gate CSV API, log, clean, dedupe, archive
  test_vpns.py -- stage 6:  open a REAL OpenVPN tunnel to every listed server,
                            verify traffic egress, geo and throughput
  report.py    -- stage 7:  render README.md (the living report), badges, history

This module intentionally uses the Python standard library only, so that
test_vpns.py can run as root (required to create tun devices) with the system
interpreter and no pip packages.
"""
from __future__ import annotations

import base64
import csv
import gzip
import io
import json
import os
import re
import socket
from datetime import datetime, timedelta, timezone

# ----------------------------------------------------------------- constants

API_URL = "https://www.vpngate.net/api/iphone/"

# Ordered endpoint candidates. VPN Gate sometimes answers datacenter IP ranges
# with an empty HTML placeholder page instead of the CSV; every response is
# therefore validated and we fall through to the next candidate.
ENDPOINTS = [
    "https://www.vpngate.net/api/iphone/",
    "http://www.vpngate.net/api/iphone/",
    "http://api.vpngate.jp/api/iphone/",
]

USER_AGENT = (
    "Mozilla/5.0 (compatible; vpngate-monitor/1.0; "
    "+https://github.com/g1010yzd10/vpngate-monitor) automated-6-hourly-check"
)

CSV_FIELDS = [
    "HostName", "IP", "Score", "Ping", "Speed", "CountryLong", "CountryShort",
    "NumVpnSessions", "Uptime", "TotalUsers", "TotalTraffic", "LogType",
    "Operator", "Message", "OpenVPN_ConfigData_Base64",
]
INT_FIELDS = {
    "Score", "Ping", "Speed", "NumVpnSessions", "Uptime",
    "TotalUsers", "TotalTraffic",
}
PUBLIC_FIELDS = [f for f in CSV_FIELDS if f != "OpenVPN_ConfigData_Base64"]
# extra derived columns written into servers_clean.csv
EXT_PUBLIC_FIELDS = PUBLIC_FIELDS + ["Proto", "Port"]

DEFAULTS = {
    "connect_timeout": 25,     # s: wait for "Initialization Sequence Completed"
    "trace_timeout": 10,       # s: exit-IP verification request
    "speed_bytes": 5_000_000,  # bytes pulled through the tunnel for throughput
    "speed_timeout": 22,       # s: throughput budget
    "workers": 48,             # parallel isolated tunnels
    "keep_archive": 360,       # csv.gz snapshots kept in archive/
    "min_rows": 50,            # refuse to replace good data with anything smaller
    "history_cap": 2000,       # max lines kept in data/history.jsonl
    "recall_days": 30,         # keep re-testing servers seen in the API within N days
    "registry_cap": 3000,      # hard cap on remembered servers
}

UPLOAD_BYTES = 524_288       # 512 KB pushed through the tunnel (upload test)

# ---------------------------------------------------------------------- time


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def now_iso() -> str:
    return utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def stamp() -> str:
    return utcnow().strftime("%Y%m%d_%H%M%S")


def iso_to_human(iso: str) -> str:
    return (iso or "").replace("T", " ").replace("Z", " UTC")


# ------------------------------------------------------------------- parsing


def parse_vpngate_csv(text: str):
    """Parse the VPN Gate "iphone" CSV format.

    The payload looks like::

        *vpn_servers
        #HostName,IP,Score,Ping,Speed,...,OpenVPN_ConfigData_Base64
        public-vpn-108,219.100.37.98,3037443,...
        *

    Returns (header, rows, malformed_count). Marker lines (``*vpn_servers``
    and the trailing ``*``) and the ``#``-prefixed header line are handled.
    """
    header, rows, malformed = None, [], 0
    for r in csv.reader(io.StringIO(text)):
        if not r:
            continue
        first = (r[0] or "").strip()
        if first.startswith("*"):
            continue
        if first.startswith("#") or first.lower().startswith("hostname"):
            if header is None:
                header = [c.strip().lstrip("#").strip() for c in r]
            continue
        if len(r) == len(CSV_FIELDS):
            rows.append([c.strip() for c in r])
        else:
            malformed += 1
    if header is None:
        header = list(CSV_FIELDS)
    return header, rows, malformed


def valid_ipv4(s: str) -> bool:
    try:
        socket.inet_aton(s)
        parts = s.split(".")
        return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
    except (OSError, ValueError):
        return False


def clean_row(row):
    """Type-check and normalise one CSV row. Returns a dict or None."""
    if len(row) != len(CSV_FIELDS):
        return None
    d = dict(zip(CSV_FIELDS, row))
    host = (d.get("HostName") or "").strip()
    ip = (d.get("IP") or "").strip()
    if not host or not valid_ipv4(ip):
        return None
    try:
        for f in INT_FIELDS:
            d[f] = int(d.get(f) or 0)
    except ValueError:
        return None
    for f in ("CountryLong", "CountryShort", "LogType", "Operator", "Message"):
        d[f] = (d.get(f) or "").strip().strip('"').strip()
    b64 = re.sub(r"\s+", "", d.get("OpenVPN_ConfigData_Base64") or "")
    try:
        ok = bool(base64.b64decode(b64, validate=False)) if b64 else False
    except Exception:
        ok = False
    d["OpenVPN_ConfigData_Base64"] = b64
    d["_config_ok"] = ok
    return d


def dedupe(servers):
    """Remove duplicates: identical (HostName, IP) pairs first, then any other
    row sharing the same IP (keeping the highest-scored entry).

    Returns (kept, removed_exact, removed_same_ip).
    """
    seen_pair, seen_ip, kept = set(), set(), []
    exact = same_ip = 0
    for s in sorted(servers, key=lambda x: (-x.get("Score", 0), x["HostName"], x["IP"])):
        pair = (s["HostName"], s["IP"])
        if pair in seen_pair:
            exact += 1
            continue
        if s["IP"] in seen_ip:
            same_ip += 1
            continue
        seen_pair.add(pair)
        seen_ip.add(s["IP"])
        kept.append(s)
    return kept, exact, same_ip


# ------------------------------------------------------------------- io


def atomic_write(path: str, data: bytes):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)


def write_json(path: str, obj):
    atomic_write(path, (json.dumps(obj, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))


def _public_rows(servers):
    rows = []
    for s in servers:
        row = [str(s.get(f, "")) for f in PUBLIC_FIELDS]
        row.append(str(s.get("_proto") or s.get("proto") or ""))
        row.append(str(s.get("_port") or s.get("port") or ""))
        rows.append(row)
    return rows


def write_public_csv(path: str, servers):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(EXT_PUBLIC_FIELDS)
        w.writerows(_public_rows(servers))
    os.replace(tmp, path)


def write_public_csv_gz(path: str, servers):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".tmp"
    with gzip.open(tmp, "wt", newline="", encoding="utf-8", compresslevel=9) as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(EXT_PUBLIC_FIELDS)
        w.writerows(_public_rows(servers))
    os.replace(tmp, path)


def prune_archive(directory: str, keep: int) -> int:
    """Delete oldest snapshots beyond `keep`. Returns number removed."""
    if not os.path.isdir(directory):
        return 0
    files = sorted(f for f in os.listdir(directory)
                   if f.startswith("vpngate_") and f.endswith(".csv.gz"))
    removed = 0
    for f in files[: max(0, len(files) - keep)]:
        try:
            os.remove(os.path.join(directory, f))
            removed += 1
        except OSError:
            pass
    return removed


def read_history(path: str, cap: int):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return out[-cap:]


def write_history(path: str, entries):
    atomic_write(
        path,
        ("\n".join(json.dumps(e, ensure_ascii=False) for e in entries) + "\n").encode("utf-8"),
    )


# -------------------------------------------------------------- formatting


def mbps(bps):
    try:
        return f"{float(bps) / 1_000_000:,.1f}"
    except (TypeError, ValueError):
        return "?"


def fmt_bytes(n):
    n = float(n or 0)
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if n < 1000 or unit == "PB":
            return f"{n:,.0f} {unit}" if unit == "B" else f"{n:,.1f} {unit}"
        n /= 1000


def fmt_uptime(ms):
    ms = ms or 0
    days = ms / 86_400_000
    if days >= 1:
        return f"{days:,.1f} d"
    return f"{ms / 3_600_000:,.1f} h"


def country_flag(code: str) -> str:
    code = (code or "").strip().upper()
    if len(code) == 2 and code.isalpha() and code.isascii():
        return "".join(chr(0x1F1E6 + ord(c) - 65) for c in code)
    return "🏳"


# ---------------------------------------------------------------- naming ---
#
# Full-descriptor display name for a verified VPN Gate server, same template
# family as the proxy-scanner node names:
#
#   🇩🇪 DE | Contabo AS141995 | ↓12.0 ↑1.2Mbps | 84.247.155.196 | DC·Clean
#            ISP       AS       measured ↓/↑     verified exit   type·reputation

LEGAL_SUFFIX_RE = re.compile(
    r"(?i)[,\s]*(co\.,? ?ltd\.?|ltd[a-z]?\.?|llc|inc\.?|incorporated|gmbh|"
    r"s\.?a\.?r\.?l\.?|sarl|s\.?p\.?a?\.?|srl|s\.?a\.?s\.?|a/s|ab|as|oyj|plc|"
    r"pty\.?|pte\.?|b\.?v\.?|n\.?v\.?|s\.?a\.?|corp\.?|corporation|company|"
    r"holding|holdings|group|limited|partners|llp|kft|ooo|zrt|s\.?d\.?n\.?bhd)"
    r"[,\s]*\.?$")
AS_RE = re.compile(r"(A[Ss]\d{1,10})")


def short_isp(name, cap=22):
    """Compact ISP label: drop legal suffixes, cap length without cutting
    a word in half."""
    if not name:
        return ""
    s = re.sub(r"\s+", " ", str(name)).strip(" .,-")
    prev = None
    while prev != s:
        prev = s
        s = LEGAL_SUFFIX_RE.sub("", s).strip(" .,-")
    if len(s) > cap:
        s = s[:cap]
        if " " in s:
            s = s.rsplit(" ", 1)[0]
    return s


def as_num(as_field):
    """'AS141995 Contabo Asia Private Limited' -> 'AS141995'."""
    m = AS_RE.search(str(as_field or ""))
    return m.group(1) if m else ""


def ip_type_tag(mobile, hosting):
    if mobile is True:
        return "MOB"
    if hosting is True:
        return "DC"
    if hosting is False:
        return "RES"
    return "?"


def clean_tag(proxy_flag):
    if proxy_flag is True:
        return "Flag"
    if proxy_flag is False:
        return "Clean"
    return "?"


def quality_tag(mobile, hosting, proxy_flag):
    parts = [p for p in (ip_type_tag(mobile, hosting),
                         clean_tag(proxy_flag)) if p != "?"]
    return "·".join(parts) if parts else "?"


def _fmt_m(mbps_value):
    if mbps_value is None:
        return "?"
    try:
        return f"{float(mbps_value):.1f}"
    except (TypeError, ValueError):
        return "?"


def display_name(entry):
    """Build the full-descriptor name for a merged server entry (dict with
    CountryShort + nested 'test' dict as produced by report.render)."""
    t = entry.get("test") or {}
    cc = (t.get("exit_country") or entry.get("CountryShort") or "").upper()
    route = f"{country_flag(cc)} {cc}" if len(cc) == 2 else "🏳 ??"
    asn = as_num(t.get("exit_as"))
    as_field = str(t.get("exit_as") or "")
    org_from_as = as_field.split(" ", 1)[1].strip() if " " in as_field else ""
    if org_from_as == asn:
        org_from_as = ""
    isp = short_isp(t.get("exit_isp") or t.get("exit_org") or org_from_as)
    who = " ".join(x for x in (isp, asn) if x) or "??"
    speed = (f"↓{_fmt_m(t.get('download_mbps'))} "
             f"↑{_fmt_m(t.get('upload_mbps'))}Mbps")
    ip = str(t.get("exit_ip") or "").strip() or "??"
    quality = quality_tag(t.get("exit_mobile"), t.get("exit_hosting"),
                          t.get("exit_proxy"))
    return f"{route} | {who} | {speed} | {ip} | {quality}"


def spark(series):
    """Tiny unicode sparkline for a list of numbers."""
    blocks = "▁▂▃▄▅▆▇█"
    vals = [v for v in series if v is not None]
    if not vals:
        return ""
    lo, hi = min(vals), max(vals)
    if hi == lo:
        return "▄" * len(vals)
    return "".join(blocks[min(7, int(8 * (v - lo) / (hi - lo)))] for v in vals)


# ------------------------------------------------------------- openvpn cfg


def extract_proto_port(cfg_text):
    """Pull (proto, port) out of a decoded VPN Gate OpenVPN config."""
    p = re.search(r"(?mi)^\s*proto\s+(\S+)", cfg_text)
    r = re.search(r"(?mi)^\s*remote\s+(\S+)\s+(\d+)", cfg_text)
    proto = p.group(1).lower() if p else None
    port = int(r.group(2)) if r else None
    return proto, port


def extract_template(cfg_text):
    """Strip the server-specific remote/proto lines, keeping the shared
    skeleton. VPN Gate ships the SAME CA / dummy client cert & key in every
    config, so any server can be dialled with template + remote line."""
    t = re.sub(r"(?mi)^\s*remote\s+\S+\s+\d+\s*$", "", cfg_text)
    t = re.sub(r"(?mi)^\s*proto\s+\S+\s*$", "", t)
    return t.strip() + "\n"


def build_config_from_template(template, proto, ip, port):
    return f"proto {proto}\nremote {ip} {port}\n" + template


# ----------------------------------------------------------------- registry


def load_registry(path):
    """The registry remembers every server that ever appeared in the API."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            reg = json.load(f)
        return reg if isinstance(reg, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def save_registry(path, reg):
    write_json(path, reg)


def update_registry(reg, servers, now_iso):
    for s in servers:
        key = f"{s['HostName']}|{s['IP']}"
        e = reg.get(key)
        if e is None:
            e = {f: s.get(f, "") for f in PUBLIC_FIELDS}
            e["first_seen"] = now_iso
            e["occurrences"] = 0
            reg[key] = e
        for f in PUBLIC_FIELDS:
            e[f] = s.get(f, e.get(f, ""))
        if s.get("_proto"):
            e["proto"] = s["_proto"]
        if s.get("_port"):
            e["port"] = s["_port"]
        e["last_seen"] = now_iso
        e["occurrences"] = e.get("occurrences", 0) + 1


def prune_registry(reg, recall_days, cap=None):
    """Drop servers whose last API appearance is older than recall_days
    (and enforce a hard cap). Returns number of entries removed."""
    cap = cap or DEFAULTS["registry_cap"]
    cutoff = (utcnow() - timedelta(days=max(0, recall_days))).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    stale = [k for k, e in reg.items()
             if (e.get("last_seen") or "") < cutoff]
    for k in stale:
        del reg[k]
    removed = len(stale)
    if len(reg) > cap:
        for k in sorted(reg, key=lambda k: reg[k].get("last_seen") or "")[: len(reg) - cap]:
            del reg[k]
            removed += 1
    return removed


def build_test_plan(reg, current_servers):
    """Everything that must be REAL-tested this run: every current server
    plus every server remembered from the last recall_days days."""
    current_keys = {(s["HostName"], s["IP"]) for s in current_servers}
    plan = []
    for key, e in reg.items():
        host, ip = key.split("|", 1)
        if not e.get("proto") or not e.get("port"):
            continue  # never had a dialable endpoint
        plan.append({
            **{f: e.get(f, "") for f in PUBLIC_FIELDS},
            "HostName": host,
            "IP": ip,
            "proto": e["proto"],
            "port": e["port"],
            "in_current_list": (host, ip) in current_keys,
        })
    plan.sort(key=lambda p: (not p["in_current_list"], -int(p.get("Score") or 0)))
    return plan


# ------------------------------------------------------------- test infra


def worker_tun(w: int) -> str:
    """Deterministic tun device name for worker slot w (tun100..tun299)."""
    return f"tun{100 + w}"


def worker_cf_ips(w: int):
    """Two per-worker anycast Cloudflare destination IPs.

    We deliberately spread workers across *distinct* Cloudflare edge IPs in
    104.16.0.0/13 so that the /32 host routes of parallel tunnels never
    collide. Any address in that range terminates TLS for any
    Cloudflare-fronted hostname (routing happens by SNI), which lets us pin
    both the exit-IP trace and the throughput download to the same address
    without any DNS lookup through the VPN.
    """
    return (f"104.16.{w % 256}.{4 + w // 256}", f"104.17.{w % 256}.{4 + w // 256}")
