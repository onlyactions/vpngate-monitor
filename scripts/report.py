#!/usr/bin/env python3
"""Stage 7 -- render README.md (the living report), badges, history.

Reads (under --data-dir):
  last_fetch.json   stage 1-5 metadata (required for a full report)
  results.json      stage 6 real VPN test output (optional -> "pending" mode)
  history.jsonl     append-only per-run summary

Writes:
  README.md                       the full auto-generated report
  badges/*.json                   shields.io endpoint badges
  data/latest.json                merged dataset (cleaned fields + test results)
  data/summary.json               compact run summary incl. error breakdown
  data/history.jsonl              updated (idempotent per fetch)

Standard library only.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

REPO_DEFAULT = "onlyactions/vpngate-monitor"


def plog(msg):
    print(f"[report] {msg}", flush=True)


def esc(v):
    """Escape a value for a markdown table cell."""
    return str(v if v is not None else "").replace("|", "\\|").replace("\n", " ").strip()


def trunc(v, n=42):
    v = str(v or "")
    return v if len(v) <= n else v[: n - 1] + "…"


def read_json(path):
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        plog(f"WARN could not read {path}: {e}")
        return None


def read_servers_csv(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            for k in common.INT_FIELDS:
                try:
                    row[k] = int(row.get(k) or 0)
                except (TypeError, ValueError):
                    row[k] = 0
            out.append(row)
    return out


def median(vals):
    v = sorted(vals)
    return v[len(v) // 2] if v else None


def speed_color(mbps):
    if mbps is None:
        return "lightgrey"
    if mbps >= 100:
        return "brightgreen"
    if mbps >= 30:
        return "green"
    if mbps >= 10:
        return "yellowgreen"
    if mbps >= 3:
        return "orange"
    return "red"


def alive_color(pct):
    if pct is None:
        return "lightgrey"
    if pct >= 60:
        return "brightgreen"
    if pct >= 40:
        return "green"
    if pct >= 20:
        return "yellow"
    return "red"


# ------------------------------------------------------------------ renderer


def render(readme_path, repo, meta, results_doc, servers, registry, history):
    env = os.environ
    run_no = env.get("GH_RUN_NUMBER", "—")
    run_url = env.get("GH_RUN_URL", "")
    event = env.get("GH_EVENT", "local")
    repo_url = f"https://github.com/{repo}"
    raw_base = f"https://raw.githubusercontent.com/{repo}/main"

    tests = (results_doc or {}).get("results", [])
    tmeta = results_doc or {}
    by_key = {(t.get("HostName"), t.get("IP")): t for t in tests}

    # current API servers (fresh fields) + historical-only servers (registry)
    merged = []
    for s in servers:
        entry = {f: s.get(f, "") for f in common.PUBLIC_FIELDS}
        entry["in_current_list"] = True
        merged.append(entry)
    seen = {(e["HostName"], e["IP"]) for e in merged}
    for key, e in registry.items():
        host, ip = key.split("|", 1)
        if (host, ip) in seen or not e.get("proto") or not e.get("port"):
            continue
        entry = {f: e.get(f, "") for f in common.PUBLIC_FIELDS}
        entry["in_current_list"] = False
        merged.append(entry)
    for entry in merged:
        t = by_key.get((entry["HostName"], entry["IP"]))
        entry["test"] = ({k: t.get(k) for k in (
            "alive", "connect_ms", "via", "proto", "exit_ip", "exit_country",
            "geo_match", "http_s", "download_mbps", "upload_mbps",
            "downloaded_bytes", "speed_capped", "error",
            "exit_isp", "exit_org", "exit_as", "exit_city",
            "exit_mobile", "exit_proxy", "exit_hosting")}
         if t else None)
        if entry["test"] and entry["test"].get("alive"):
            entry["display_name"] = common.display_name(entry)

    current = [e for e in merged if e["in_current_list"]]
    tested = [e for e in merged if e["test"]]
    alive = [e for e in tested if e["test"].get("alive")]
    alive_cur = [e for e in alive if e["in_current_list"]]
    revived = [e for e in alive if not e["in_current_list"]]
    dead = [e for e in tested if not e["test"].get("alive")]
    untested = len(merged) - len(tested)
    fetched = meta.get("unique_servers", len(current)) if meta else len(current)
    hist_known = len(merged) - len(current)
    alive_pct = (100.0 * len(alive) / len(tested)) if tested else None
    usability = (100.0 * len(alive_cur) / fetched) if fetched else None
    speeds = [e["test"]["download_mbps"] for e in alive
              if e["test"].get("download_mbps")]
    avg_sp = sum(speeds) / len(speeds) if speeds else None
    med_sp = median(speeds) if speeds else None
    max_sp = max(speeds) if speeds else None
    ups = [e["test"]["upload_mbps"] for e in alive
           if e["test"].get("upload_mbps")]
    avg_up = sum(ups) / len(ups) if ups else None
    max_up = max(ups) if ups else None
    clean_n = sum(1 for e in alive if e["test"].get("exit_proxy") is False)
    res_n = sum(1 for e in alive if e["test"].get("exit_hosting") is False)
    mob_n = sum(1 for e in alive if e["test"].get("exit_mobile") is True)
    mismatches = [e for e in alive if e["test"].get("geo_match") is False]
    conns = [e["test"]["connect_ms"] for e in alive if e["test"].get("connect_ms")]

    fastest = sorted(alive, key=lambda e: (-(e["test"].get("download_mbps") or 0),
                                           -e.get("Score", 0)))[:10]
    topscore = sorted(alive, key=lambda e: (-e.get("Score", 0),
                                            -(e["test"].get("download_mbps") or 0)))[:10]

    # countries ------------------------------------------------------------
    countries = defaultdict(lambda: {"n": 0, "alive": 0, "best": 0.0, "best_host": ""})
    for e in merged:
        c = countries[(e.get("CountryShort") or "??",
                       e.get("CountryLong") or "Unknown")]
        c["n"] += 1
        if e["test"] and e["test"].get("alive"):
            c["alive"] += 1
            mb = e["test"].get("download_mbps") or 0
            if mb > c["best"]:
                c["best"], c["best_host"] = mb, e.get("HostName", "")
    country_rows = sorted(countries.items(), key=lambda kv: (-kv[1]["n"], kv[0][0]))

    # honesty ----------------------------------------------------------------
    def claimed_mbps(e):
        return (e.get("Speed") or 0) / 1_000_000.0

    honest = [e for e in alive
              if e["test"].get("download_mbps") and claimed_mbps(e) > 0]
    honest.sort(key=lambda e: (e["test"]["download_mbps"] / claimed_mbps(e)))

    # failure breakdown -------------------------------------------------------
    fails = Counter(((e["test"].get("error") or "unknown").split(":")[0])
                    for e in dead)

    # badges -------------------------------------------------------------------
    def badge(label, message, color):
        return {"schemaVersion": 1, "label": label, "message": str(message),
                "color": color}

    badges = {
        "servers": badge("servers tracked", f"{fetched:,}", "blue"),
        "alive": badge("verified alive",
                       (f"{len(alive):,}/{len(tested):,} tested ({alive_pct:.0f}%)"
                        if tested else "pending"),
                       alive_color(alive_pct if tested else None)),
        "speed": badge("avg measured ↓",
                       (f"{avg_sp:.1f} Mbps" if avg_sp is not None else "pending"),
                       speed_color(avg_sp)),
        "up-speed": badge("avg measured ↑",
                          (f"{avg_up:.1f} Mbps" if avg_up is not None else "pending"),
                          speed_color(avg_up)),
        "clean": badge("clean exits",
                       (f"{clean_n:,} unflagged" if tested else "pending"),
                       "green" if clean_n else "lightgrey"),
        "updated": badge("last run",
                         common.iso_to_human(meta.get("fetched_at")) if meta
                         else "pending",
                         "informational"),
    }

    # ---------------------------------------------------------------- markdown
    L = []
    ap = L.append

    ap("# 🛡️ VPN Gate Monitor")
    ap("")
    ap("> **Daily** this repo fetches the complete public "
       "[VPN Gate](https://www.vpngate.net/en/) server list, **cleans, "
       "deduplicates and archives** it — and then does the part that matters: "
       "it **opens a real OpenVPN tunnel to every single listed server**, "
       "verifies that traffic genuinely exits through it, checks *where* it "
       "exits and **who operates that exit** (ISP, AS, IP reputation), and "
       "measures real download **and upload** throughput.")
    ap(">")
    ap("> **Everything below this line is the auto-generated living report. "
       "No hand-edited numbers.**")
    ap("")
    wl = f"{repo}/actions/workflows/vpngate.yml"
    ap(f"[![pipeline](https://github.com/{wl}/badge.svg)]"
       f"(https://github.com/{wl})")
    for name in ("servers", "alive", "speed", "up-speed", "clean", "updated"):
        b = badges[name]
        url = quote(f"{raw_base}/badges/{name}.json", safe="")
        ap(f"[![{b['label']}](https://img.shields.io/endpoint?url={url})"
           f"]({raw_base}/badges/{name}.json)")
    ap("")

    # latest results ----------------------------------------------------------
    ap("## 📊 Latest results")
    ap("")
    if meta is None and not servers:
        ap("⏳ **No run has completed yet.** The first automated run is "
           "scheduled right after this repo was pushed — this report will "
           "fill itself in automatically.")
        ap("")
    else:
        run_line = f"#{run_no}"
        if run_url:
            run_line = f"[#{run_no} · view run]({run_url})"
        ap("| | |")
        ap("|---|---|")
        ap(f"| **Run** | {run_line} · "
           f"{common.iso_to_human(meta.get('fetched_at')) if meta else '—'}"
           f" · trigger: `{event}` |")
        ap(f"| **Servers fetched (unique)** | **{fetched:,}** |")
        if meta:
            ap(f"| **Duplicates removed** | "
               f"{meta.get('removed_exact_duplicates', 0):,} exact + "
               f"{meta.get('removed_same_ip_duplicates', 0):,} same-IP |")
        ap(f"| **Servers tested** | **{len(tested):,} of {len(merged):,}** — "
           f"all {fetched:,} current + {hist_known:,} historical "
           f"(every server seen in the API within "
           f"{(meta or {}).get('recall_days', 30)} days) |" if tested else
           f"| **Servers tested** | ⏳ pending first test run |")
        if tested:
            ap(f"| **✅ Verified alive** (tunnel up + egress proven) | "
               f"**{len(alive):,}** — {len(alive_cur):,} from the current "
               f"list + {len(revived):,} historical ♻️ |")
            ap(f"| **❌ Dead / unusable** | {len(dead):,} |")
            if usability is not None:
                ap(f"| **Usability** | **{usability:.1f}%** of everything "
                   f"VPN Gate lists right now actually works |")
            if avg_sp is not None:
                ap(f"| **⚡ Measured download (avg / median / max)** | "
                   f"**{avg_sp:.1f} / {med_sp:.1f} / {max_sp:.1f} Mbps** |")
            if avg_up is not None:
                ap(f"| **⚡ Measured upload (avg / max)** | "
                   f"**{avg_up:.1f} / {max_up:.1f} Mbps** |")
            ap(f"| **🧼 Exit IP reputation** | **{clean_n:,}** unflagged "
               f"('clean') · **{res_n:,}** residential · **{mob_n:,}** mobile · "
               f"rest datacenter/flagged |")
            if fastest:
                f0 = fastest[0]
                ap(f"| **🚀 Fastest verified** | **{esc(f0.get('HostName'))}** · "
                   f"{common.country_flag(f0.get('CountryShort'))} "
                   f"{esc(f0.get('CountryLong'))} · "
                   f"**{f0['test']['download_mbps']:.1f} Mbps** |")
            ap(f"| **🧭 Exit-country mismatches** | {len(mismatches):,} "
               f"(server exits somewhere else than it claims) |")
            if conns:
                ap(f"| **🤝 Handshake time (alive, avg)** | "
                   f"{sum(conns) / len(conns) / 1000:.1f} s |")
        if untested:
            ap(f"| **Untested** | {untested:,} |")
        ap("")

    # fastest -----------------------------------------------------------------
    ap("## 🚀 Fastest verified servers")
    ap("")
    if fastest:
        ap("Each row is fully described by its display name (see "
           "[How to read the names](#-how-to-read-the-names) below): country, "
           "ISP + AS of the **verified exit IP**, measured download/upload "
           "speed, the exit IP itself and its reputation.")
        ap("")
        ap("```text")
        for i, e in enumerate(fastest, 1):
            ap(f"{i}. {e.get('display_name', common.display_name(e))}  "
               f"({esc(e.get('HostName'))})")
        ap("```")
        ap("")
        ap("| # | Server | Country | Endpoint | Exit IP (verified) | "
           "ISP · AS · rep | Measured ↓ | Measured ↑ | Claimed ↓ | Score |")
        ap("|---:|---|---|---|---|---|---:|---:|---:|---:|")
        for i, e in enumerate(fastest, 1):
            t = e["test"]
            up = f"{t.get('upload_mbps'):.1f} Mbps" if t.get("upload_mbps") \
                else "-"
            ap(f"| {i} | `{esc(e.get('HostName'))}` | "
               f"{common.country_flag(e.get('CountryShort'))} "
               f"{esc(e.get('CountryShort'))} | "
               f"`{esc(t.get('via') or e.get('IP'))}`"
               f"{'/' + esc(t.get('proto')) if t.get('proto') else ''} | "
               f"`{esc(t.get('exit_ip'))}` | "
               f"{esc(common.short_isp(t.get('exit_isp') or t.get('exit_org')))} "
               f"{common.as_num(t.get('exit_as'))} "
               f"{common.quality_tag(t.get('exit_mobile'), t.get('exit_hosting'), t.get('exit_proxy'))} | "
               f"**{t.get('download_mbps') or 0:.1f} Mbps** | "
               f"{up} | "
               f"{common.mbps(e.get('Speed'))} Mbps | {e.get('Score', 0):,} |")
        ap("")
        ap("*Measured = 5 MB download + 512 KB upload through the live tunnel "
           "to speed.cloudflare.com. Claimed = the server's self-reported line "
           "speed in the VPN Gate API. Exit IP/ISP/reputation are looked up "
           "from ip-api after the tunnels close. 'Historical' servers are no "
           "longer in the API's current top list but still answered our "
           "tunnel — we keep re-testing everything we have ever seen.*")
    else:
        ap("⏳ No verified-alive servers yet — waiting for the first "
           "completed test run.")
    ap("")

    # how to read the names ------------------------------------------------
    ap("## 🏷️ How to read the names")
    ap("")
    ap("Every verified server gets a display name that tells you everything "
       "about **what you would actually connect to**:")
    ap("")
    ap("```text")
    ap("\U0001F1E9\U0001F1EA DE | Contabo AS141995 | ↓12.0 ↑1.2Mbps | 84.247.155.196 | DC·Clean")
    ap("```")
    ap("")
    ap("| part | meaning |")
    ap("|------|---------|")
    ap("| `\U0001F1E9\U0001F1EA DE` | country of the **verified exit** (not what "
       "the server claims) |")
    ap("| `Contabo AS141995` | ISP / organization operating the exit IP and its "
       "autonomous system |")
    ap("| `↓12.0 ↑1.2Mbps` | download / upload measured through the live "
       "tunnel (`?` = test failed) |")
    ap("| `84.247.155.196` | the verified exit IP — your egress address |")
    ap("| `DC` | datacenter / hosting IP (most VPN Gate servers) |")
    ap("| `RES` | residential IP — usually the best bet against bot/VPN "
       "blocks |")
    ap("| `MOB` | mobile / carrier IP (CGNAT) |")
    ap("| `Clean` | exit not listed in ip-api's proxy/VPN/Tor database |")
    ap("| `Flag` | exit listed as proxy/VPN — expect streaming blocks |")
    ap("")

    # top score -----------------------------------------------------------------
    ap("## ⭐ Top-scored & verified alive")
    ap("")
    if topscore:
        ap("| # | Server | Country | Score | Claimed ↓ | Measured ↓ | "
           "Measured ↑ | Sessions | Uptime | Log policy |")
        ap("|---:|---|---|---:|---:|---:|---:|---:|---:|---|")
        for i, e in enumerate(topscore, 1):
            t = e["test"]
            up = f"{t.get('upload_mbps'):.1f}" if t.get("upload_mbps") else "-"
            ap(f"| {i} | `{esc(e.get('HostName'))}` | "
               f"{common.country_flag(e.get('CountryShort'))} "
               f"{esc(e.get('CountryShort'))} | {e.get('Score', 0):,} | "
               f"{common.mbps(e.get('Speed'))} Mbps | "
               f"{t.get('download_mbps') or 0:.1f} Mbps | "
               f"{up} Mbps | "
               f"{e.get('NumVpnSessions', 0):,} | "
               f"{common.fmt_uptime(e.get('Uptime'))} | "
               f"{esc(e.get('LogType'))} |")
    else:
        ap("⏳ Pending first completed test run.")
    ap("")

    # countries -----------------------------------------------------------------
    ap("## 🌍 Countries")
    ap("")
    if country_rows:
        ap("| Country | Servers | Verified alive | Best measured ↓ | "
           "Fastest server |")
        ap("|---|---:|---:|---:|---|")
        for (short, long_), c in country_rows[:40]:
            ap(f"| {common.country_flag(short)} {esc(long_)} ({esc(short)}) | "
               f"{c['n']:,} | {c['alive']:,} | "
               f"{c['best']:.1f} Mbps | `{esc(c['best_host'])}` |")
        if len(country_rows) > 40:
            ap(f"| … | +{len(country_rows) - 40} more countries | | | |")
    else:
        ap("⏳ Pending data.")
    ap("")

    # honesty --------------------------------------------------------------------
    ap("## 🕵️ Claim vs. reality")
    ap("")
    if honest:
        ap("The VPN Gate `Speed` field is whatever the server *claims*. "
           "Here is the truth, measured through a live tunnel — the hall of "
           "shame (claimed ≫ delivered):")
        ap("")
        ap("| Server | Country | Claims | Delivers | Reality ratio |")
        ap("|---|---|---:|---:|---:|")
        for e in honest[:10]:
            t = e["test"]
            ratio = t["download_mbps"] / claimed_mbps(e)
            ap(f"| `{esc(e.get('HostName'))}` | "
               f"{common.country_flag(e.get('CountryShort'))} "
               f"{esc(e.get('CountryShort'))} | "
               f"{claimed_mbps(e):,.0f} Mbps | {t['download_mbps']:.1f} Mbps | "
               f"{ratio * 100:.0f}% |")
        ap("")
        best = honest[-5:]
        if best:
            names = ", ".join(f"`{esc(e.get('HostName'))}` "
                              f"({e['test']['download_mbps']:.0f} Mbps)"
                              for e in reversed(best))
            ap(f"Most honest of this round: {names}.")
    else:
        ap("⏳ Pending first completed test run.")
    ap("")

    # geo mismatches ----------------------------------------------------------------
    ap("## 🧭 Exit-country mismatches")
    ap("")
    if mismatches:
        ap("These servers are listed under one country but your traffic "
           "**actually exits somewhere else** (verified via Cloudflare's "
           "geo view of the exit IP) — useful to know before you trust one:")
        ap("")
        ap("| Server | Claims | Actually exits via | Exit IP | Measured ↓ |")
        ap("|---|---|---|---|---:|")
        for e in mismatches[:15]:
            t = e["test"]
            ap(f"| `{esc(e.get('HostName'))}` | "
               f"{common.country_flag(e.get('CountryShort'))} "
               f"{esc(e.get('CountryShort'))} | "
               f"{common.country_flag(t.get('exit_country'))} "
               f"{esc(t.get('exit_country'))} | `{esc(t.get('exit_ip'))}` | "
               f"{t.get('download_mbps') or 0:.1f} Mbps |")
    else:
        ap("None detected in the latest run"
           + ("." if tested else " — pending first test run.") if not tested
           else ". ✅ Every verified server exits where it claims.")
    ap("")

    # history ------------------------------------------------------------------------
    ap("## 📈 History")
    ap("")
    if len(history) > 1:
        alive_series = [h.get("alive_pct") for h in history]
        speed_series = [h.get("avg_mbps") for h in history]
        ap(f"Alive % trend (last {len(history)} runs): "
           f"`{common.spark(alive_series)}`")
        ap("")
        ap(f"Avg measured speed (Mbps): `{common.spark(speed_series)}`")
        ap("")
        ap("| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Avg ↑ | "
           "Mismatches |")
        ap("|---|---:|---:|---:|---:|---:|---:|---:|")
        for h in reversed(history[-15:]):
            ap(f"| {common.iso_to_human(h.get('time'))} | "
               f"{h.get('fetched', 0):,} | {h.get('alive', 0):,} | "
               f"{h.get('alive_pct', 0):.0f}% | "
               f"{h.get('avg_mbps') or 0:.1f} | {h.get('max_mbps') or 0:.1f} | "
               f"{h.get('avg_up_mbps') or 0:.1f} | "
               f"{h.get('mismatches', 0)} |")
    else:
        ap("History builds up here run by run "
           f"(currently {len(history)} entr{'y' if len(history) == 1 else 'ies'}).")
    ap("")

    # pipeline --------------------------------------------------------------------------
    ap("## ⚙️ How the pipeline works")
    ap("")
    ap("```mermaid")
    ap("flowchart LR")
    ap("    C[\"cron: daily 03:23 UTC\"] --> F[\"fetch vpngate.net CSV API\"]")
    ap("    F --> L[\"log raw + meta\"]")
    ap("    L --> CL[\"clean + type-check\"]")
    ap("    CL --> D[\"dedupe hostname + IP\"]")
    ap("    D --> A[\"archive .csv.gz snapshot\"]")
    ap("    D --> T[\"REAL test: OpenVPN tunnel per server<br/>egress + geo + throughput\"]")
    ap("    T --> R[\"report: README + badges + history\"]")
    ap("    R --> P[\"commit and push\"]")
    ap("```")
    ap("")
    ap("1. **Fetch** — `GET /api/iphone/` with retries and endpoint "
       "fallback; responses are validated (the API sometimes serves an empty "
       "placeholder page to datacenter IPs) and the raw bytes are logged and "
       "hashed (sha256).")
    ap("2. **Clean** — parse the special CSV (`*vpn_servers` marker, "
       "`#`-prefixed header), type-check every numeric field, validate IPs, "
       "drop broken rows, strip noise.")
    ap("3. **Dedupe** — remove exact `(HostName, IP)` duplicates, then "
       "same-IP entries keeping the highest-scoring one.")
    ap("4. **Archive** — every run writes an immutable gzipped snapshot to "
       "`archive/` (auto-pruned to the newest 360 ≈ 90 days).")
    ap("5. **Test — the real deal.** For **every** server, every run — not "
       "just the API's current list, but **the union of every server that has "
       "ever appeared** within the 30-day recall window (kept in "
       "`data/known_servers.json`): decode the shared VPN Gate OpenVPN "
       "template (all servers ship the same CA + dummy client cert — verified), "
       "rebuild each server's config with its remembered `(proto, port)`, "
       "force it onto a per-worker `tun` device, disable pushed routes, pin "
       "two /32 routes through the tunnel to per-worker Cloudflare anycast "
       "IPs, wait for *Initialization Sequence Completed*, then verify egress "
       "(`cdn-cgi/trace` through the tunnel must return a foreign exit IP + "
       "real exit country), measure a 5 MB download and a 512 KB upload "
       "through the same tunnel, and — once all tunnels are down — batch-"
       "lookup every verified exit IP at ip-api to add the ISP, AS and IP-"
       "reputation flags (datacenter / residential / mobile / proxy-DB) "
       "that you see in the display names. Up to 48 isolated tunnels run in "
       "parallel; a server that never completes the handshake is hard-killed "
       "after 25 s.")
    ap("6. **Report** — this README, six live badges, `latest.json`, "
       "`summary.json` and the `history.jsonl` log are regenerated and "
       "committed by `github-actions[bot]`.")
    ap("")

    # data files ---------------------------------------------------------------------------
    ap("## 📁 Data files & programmatic use")
    ap("")
    ap(f"All results are in this repo — hotlink them straight from "
       f"`{repo_url}`:")
    ap("")
    ap(f"- [`data/latest.json`]({raw_base}/data/latest.json) — the merged "
       f"dataset: every cleaned server + its latest real test result")
    ap(f"- [`data/servers_clean.csv`]({raw_base}/data/servers_clean.csv) — "
       f"cleaned, deduplicated server list (no bulky config blobs)")
    ap(f"- [`data/summary.json`]({raw_base}/data/summary.json) — compact "
       f"run summary with failure breakdown")
    ap(f"- [`data/history.jsonl`]({raw_base}/data/history.jsonl) — one JSON "
       f"line per run, append-only")
    ap(f"- [`archive/`]({repo_url}/tree/main/archive) — immutable gzipped "
       f"snapshots of every run")
    ap("- full logs, raw API response and per-server error details are "
       "attached to each [Actions run]("
       f"https://github.com/{repo}/actions) as artifacts (30-day retention)")
    ap("")
    ap("Grab a working VPN right now:")
    ap("")
    ap("```bash")
    ap(f"curl -s {raw_base}/data/latest.json \\")
    ap("  | python3 -c \"import json,sys;[print(s['IP'],s['CountryShort'],"
       "s['test']['download_mbps'],'Mbps') for s in json.load(sys.stdin) "
       "if s['test'] and s['test']['alive']]\" \\")
    ap("  | sort -k3 -nr | head")
    ap("```")
    ap("")
    ap("Field units: `Score` points · `Ping` ms · `Speed` bit/s (self-"
       "reported) · `Uptime` ms · `TotalUsers` count · `TotalTraffic` bytes "
       "· `download_mbps` / `upload_mbps` Mbps (measured through the "
       "tunnel) · `exit_*` = ISP/AS/city/reputation of the verified exit "
       "IP · `display_name` = the full-descriptor name.")
    ap("")

    # methodology -----------------------------------------------------------------------------
    ap("## 🔬 Methodology & caveats")
    ap("")
    ap("- **Real tunnels, not CSV checks.** A server only counts as alive if "
       "OpenVPN completed its handshake *and* an HTTPS request bound to the "
       "tunnel egressed with a foreign IP. A server whose tunnel silently "
       "black-holes traffic fails the egress step and is reported dead.")
    ap("- **No DNS through the VPN.** Test destinations are pinned with "
       "`curl --resolve` to per-worker Cloudflare anycast addresses, so a "
       "broken/hijacking VPN DNS can never fake a success.")
    ap("- **Throughput** is one 5 MB download plus one 512 KB upload to "
       "`speed.cloudflare.com` through the live tunnel — a sample, not a "
       "lab measurement.")
    ap("- **Vantage point**: GitHub Actions runners (Azure, usually US/EU). "
       "A server that is slow from there may be fast from your country, and "
       "vice versa.")
    ap("- **Fairness**: volunteer servers are shared — measured speeds dip "
       "when many clients are connected (`NumVpnSessions` is listed).")
    ap("- **Security**: test traffic is TLS to Cloudflare only; we never send "
       "anything sensitive through volunteer servers. Neither should you — "
       "assume the operator can see traffic metadata.")
    ap("")

    # disclaimer --------------------------------------------------------------------------------
    ap("## ⚠️ Disclaimer")
    ap("")
    ap("- [VPN Gate](https://www.vpngate.net/en/) is an academic experiment "
       "by the University of Tsukuba, Japan (Daiyuu Nobori & co). This "
       "project is an independent monitor of its public API and is **not "
       "affiliated** with it.")
    ap("- VPN servers are run by volunteers; some keep connection logs "
       "(see `LogType`). Use them legally and responsibly; do not route "
       "anything private or illegal through them.")
    ap("- Data is provided **as-is** for research/educational purposes.")
    ap("")
    ap("## 📄 License")
    ap("")
    ap("Code: MIT. Data: originates from VPN Gate's public API — respect "
       "their terms.")
    ap("")
    if run_url:
        ap("---")
        ap(f"*Auto-generated by [run #{run_no}]({run_url}) at "
           f"{common.now_iso().replace('T', ' ').replace('Z', ' UTC')}. "
           f"Next scheduled run: daily 03:23 UTC.*")
        ap("")

    return "\n".join(L).rstrip() + "\n", badges, merged, {
        "meta": meta, "fetched": fetched, "tested": len(tested),
        "alive": len(alive), "dead": len(dead), "untested": untested,
        "alive_pct": alive_pct, "usability": usability,
        "avg_mbps": avg_sp, "median_mbps": med_sp, "max_mbps": max_sp,
        "avg_up_mbps": (round(avg_up, 2) if avg_up is not None else None),
        "max_up_mbps": max_up,
        "clean_exits": clean_n, "residential_exits": res_n,
        "mobile_exits": mob_n,
        "mismatches": len(mismatches),
        "historical_known": hist_known,
        "revived": len(revived),
        "avg_connect_ms": (sum(conns) / len(conns)) if conns else None,
        "fastest": [{"HostName": e.get("HostName"), "IP": e.get("IP"),
                     "CountryShort": e.get("CountryShort"),
                     "in_current_list": e.get("in_current_list"),
                     "download_mbps": e["test"].get("download_mbps"),
                     "upload_mbps": e["test"].get("upload_mbps"),
                     "display_name": e.get("display_name")}
                    for e in fastest],
        "failure_breakdown": dict(fails.most_common(12)),
        "runner_ip": tmeta.get("runner_ip"),
        "run": {"number": run_no, "url": run_url, "event": event,
                "generated_at": common.now_iso()},
    }


# ------------------------------------------------------------------------ main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--badges-dir", default="badges")
    args = ap.parse_args()

    repo = os.environ.get("GH_REPO", REPO_DEFAULT)
    meta = read_json(os.path.join(args.data_dir, "last_fetch.json"))
    results_doc = read_json(os.path.join(args.data_dir, "results.json"))
    servers = read_servers_csv(os.path.join(args.data_dir, "servers_clean.csv"))
    registry = common.load_registry(os.path.join(args.data_dir, "known_servers.json"))
    hist_path = os.path.join(args.data_dir, "history.jsonl")
    history = common.read_history(hist_path, common.DEFAULTS["history_cap"])

    readme, badges, merged, s = render(args.readme, repo, meta, results_doc,
                                       servers, registry, history)

    common.atomic_write(args.readme, readme.encode("utf-8"))
    plog(f"wrote {args.readme} ({len(readme):,} bytes)")

    os.makedirs(args.badges_dir, exist_ok=True)
    for name, doc in badges.items():
        common.write_json(os.path.join(args.badges_dir, f"{name}.json"), doc)
    plog(f"wrote {len(badges)} badges -> {args.badges_dir}/")

    common.write_json(os.path.join(args.data_dir, "latest.json"), merged)
    plog(f"wrote {args.data_dir}/latest.json ({len(merged):,} servers)")

    # history (idempotent per fetch: re-rendering the same fetch replaces
    # its own line instead of duplicating it)
    if meta is not None:
        run_key = meta.get("fetched_at") or common.now_iso()
        entry = {
            "run_key": run_key,
            "time": meta.get("fetched_at") or common.now_iso(),
            "fetched": s["fetched"],
            "tested": s["tested"],
            "alive": s["alive"],
            "alive_pct": round(s["alive_pct"], 1) if s["alive_pct"] is not None else None,
            "avg_mbps": round(s["avg_mbps"], 2) if s["avg_mbps"] is not None else None,
            "max_mbps": s["max_mbps"],
            "avg_up_mbps": s.get("avg_up_mbps"),
            "clean_exits": s.get("clean_exits"),
            "mismatches": s["mismatches"],
            "revived": s.get("revived", 0),
            "run": s["run"],
        }
        if history and history[-1].get("run_key") == run_key:
            history[-1] = entry
        else:
            history.append(entry)
        common.write_history(hist_path, history)
        plog(f"history -> {hist_path} ({len(history)} entries)")

    # compact summary (also used by the commit step)
    common.write_json(os.path.join(args.data_dir, "summary.json"), s)
    plog(f"wrote {args.data_dir}/summary.json")

    # GitHub step summary, if running inside Actions
    gss = os.environ.get("GITHUB_STEP_SUMMARY")
    if gss and os.path.exists(os.path.dirname(gss) or "."):
        with open(gss, "a", encoding="utf-8") as f:
            f.write("\n### 🛡️ VPN Gate Monitor — run summary\n\n")
            f.write(f"- Fetched **{s['fetched']:,}** unique servers\n")
            if s["usability"] is not None:
                f.write(f"- Real-tested **{s['tested']:,}** — "
                        f"**{s['alive']:,} verified alive** "
                        f"({s['usability']:.0f}% usable)\n")
            else:
                f.write(f"- Real-tested {s['tested']:,}\n")
            if s["avg_mbps"] is not None:
                f.write(f"- Avg measured speed **{s['avg_mbps']:.1f} Mbps** "
                        f"down, max **{s['max_mbps']:.1f} Mbps**")
                if s.get("avg_up_mbps") is not None:
                    f.write(f"; avg upload **{s['avg_up_mbps']:.1f} Mbps**")
                f.write("\n")
            if s.get("clean_exits"):
                f.write(f"- Clean (unflagged) exits: **{s['clean_exits']:,}**, "
                        f"residential: **{s.get('residential_exits', 0):,}**, "
                        f"mobile: **{s.get('mobile_exits', 0):,}**\n")
            f.write(f"- Exit-country mismatches: {s['mismatches']}\n")
            if s["fastest"]:
                f0 = s["fastest"][0]
                f.write(f"- Fastest: `{f0['HostName']}` "
                        f"({f0['CountryShort']}) — "
                        f"{f0['download_mbps']:.1f} Mbps\n")
        plog("appended GitHub step summary")

    if s["usability"] is not None:
        plog(f"DONE: fetched={s['fetched']} tested={s['tested']} "
             f"alive={s['alive']} usability={s['usability']:.1f}%")
    else:
        plog(f"DONE: fetched={s['fetched']} tested={s['tested']} "
             f"alive={s['alive']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
