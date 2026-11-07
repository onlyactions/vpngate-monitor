# 🛡️ VPN Gate Monitor

> **Once a day** this repo fetches the complete public [VPN Gate](https://www.vpngate.net/en/) server list, **cleans, deduplicates and archives** it — and then does the part that matters: it **opens a real OpenVPN tunnel to every single listed server**, verifies that traffic genuinely exits through it, checks *where* it exits, and measures real download throughput.
>
> **Everything below this line is the auto-generated living report. No hand-edited numbers.**

[![pipeline](https://github.com/onlyactions/vpngate-monitor/actions/workflows/vpngate.yml/badge.svg)](https://github.com/onlyactions/vpngate-monitor/actions/workflows/vpngate.yml)
[![servers tracked](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fservers.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/servers.json)
[![verified alive](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Falive.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/alive.json)
[![avg measured speed](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fspeed.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/speed.json)
[![last run](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fupdated.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/updated.json)

## 📊 Latest results

| | |
|---|---|
| **Run** | [#2 · view run](https://github.com/onlyactions/vpngate-monitor/actions/runs/42337563970) · 2026-11-07 04:14:58 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **93** |
| **Duplicates removed** | 0 exact + 0 same-IP |
| **Servers tested** | **184 of 184** — all 93 current + 91 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **88** — 50 from the current list + 38 historical ♻️ |
| **❌ Dead / unusable** | 96 |
| **Usability** | **53.8%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **10.9 / 12.8 / 27.0 Mbps** |
| **🚀 Fastest verified** | **vpn395594089** · 🇧🇾 Belarus · **27.0 Mbps** |
| **🧭 Exit-country mismatches** | 1 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.4 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn395594089` | 🇧🇾 Belarus | 📋 current | `46.53.252.187:6638`/udp | 2.5s | **27.0 Mbps** | 57.0 Mbps | 637,148 |
| 2 | `vpn310756240` | 🇷🇺 Russian Federation | ♻️ historical | `90.154.70.206:10131`/udp | 2.5s | **26.2 Mbps** | 44.5 Mbps | 1,515,668 |
| 3 | `vpn201737691` | 🇯🇵 Japan | 📋 current | `59.85.16.253:1742`/udp | 2.8s | **23.9 Mbps** | 590.9 Mbps | 1,494,450 |
| 4 | `vpn399630262` | 🇧🇷 Brazil | ♻️ historical | `179.135.95.98:995`/tcp | 2.5s | **20.0 Mbps** | 115.0 Mbps | 829,089 |
| 5 | `vpn761307546` | 🇷🇺 Russian Federation | ♻️ historical | `193.233.121.97:1292`/udp | 2.5s | **18.8 Mbps** | 39.3 Mbps | 472,194 |
| 6 | `vpn629209184` | 🇷🇺 Russian Federation | ♻️ historical | `212.164.64.254:16903`/udp | 2.8s | **18.0 Mbps** | 198.1 Mbps | 526,052 |
| 7 | `vpn579347997` | 🇯🇵 Japan | 📋 current | `118.240.129.23:1606`/tcp | 2.8s | **17.8 Mbps** | 897.8 Mbps | 903,212 |
| 8 | `vpn500270442` | 🇯🇵 Japan | 📋 current | `121.109.224.163:1361`/tcp | 3.0s | **16.3 Mbps** | 545.6 Mbps | 783,585 |
| 9 | `vpn631309138` | 🇹🇭 Thailand | ♻️ historical | `49.48.220.228:1671`/udp | 3.0s | **15.8 Mbps** | 430.4 Mbps | 633,077 |
| 10 | `vpn989314839` | 🇯🇵 Japan | ♻️ historical | `211.10.52.110:1729`/tcp | 2.8s | **15.6 Mbps** | 959.3 Mbps | 649,259 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-45` | 🇯🇵 JP | 2,442,498 | 203.9 Mbps | 13.4 Mbps | 104 | 13.1 d | 2weeks |
| 2 | `public-vpn-142` | 🇯🇵 JP | 2,259,009 | 509.6 Mbps | 13.8 Mbps | 75 | 13.1 d | 2weeks |
| 3 | `public-vpn-49` | 🇯🇵 JP | 2,144,481 | 213.9 Mbps | 13.3 Mbps | 63 | 13.9 d | 2weeks |
| 4 | `public-vpn-138` | 🇯🇵 JP | 1,905,828 | 246.3 Mbps | 10.2 Mbps | 117 | 13.9 d | 2weeks |
| 5 | `public-vpn-67` | 🇯🇵 JP | 1,785,011 | 226.6 Mbps | 14.3 Mbps | 63 | 13.1 d | 2weeks |
| 6 | `public-vpn-119` | 🇯🇵 JP | 1,755,421 | 752.4 Mbps | 13.9 Mbps | 135 | 13.1 d | 2weeks |
| 7 | `public-vpn-102` | 🇯🇵 JP | 1,726,252 | 257.7 Mbps | 13.6 Mbps | 59 | 13.9 d | 2weeks |
| 8 | `vpn250920860` | 🇯🇵 JP | 1,520,209 | 369.4 Mbps | 13.9 Mbps | 97 | 27.7 d | 2weeks |
| 9 | `vpn310756240` | 🇷🇺 RU | 1,515,668 | 44.5 Mbps | 26.2 Mbps | 26 | 8.8 d | 2weeks |
| 10 | `vpn201737691` | 🇯🇵 JP | 1,494,450 | 590.9 Mbps | 23.9 Mbps | 69 | 20.4 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 81 | 44 | 23.9 Mbps | `vpn201737691` |
| 🇰🇷 Korea Republic of (KR) | 61 | 28 | 14.0 Mbps | `vpn446015046` |
| 🇷🇺 Russian Federation (RU) | 13 | 4 | 26.2 Mbps | `vpn310756240` |
| 🇹🇭 Thailand (TH) | 10 | 5 | 15.8 Mbps | `vpn631309138` |
| 🇻🇳 Viet Nam (VN) | 4 | 1 | 9.3 Mbps | `vpn925698769` |
| 🇺🇸 United States (US) | 3 | 0 | 0.0 Mbps | `` |
| 🇧🇾 Belarus (BY) | 2 | 1 | 27.0 Mbps | `vpn395594089` |
| 🇲🇲 Myanmar (MM) | 2 | 0 | 0.0 Mbps | `` |
| 🇲🇾 Malaysia (MY) | 2 | 1 | 8.4 Mbps | `vpn375420108` |
| 🇧🇷 Brazil (BR) | 1 | 1 | 20.0 Mbps | `vpn399630262` |
| 🇬🇧 United Kingdom (GB) | 1 | 1 | 0.7 Mbps | `patito` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇲🇽 Mexico (MX) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 1 | 1 | 6.2 Mbps | `vpn269589023` |
| 🇷🇴 Romania (RO) | 1 | 1 | 4.6 Mbps | `opengw` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `public-vpn-198` | 🇯🇵 JP | 556 Mbps | 1.0 Mbps | 0% |
| `vpn434008438` | 🇯🇵 JP | 168 Mbps | 0.4 Mbps | 0% |
| `vpn855299844` | 🇰🇷 KR | 450 Mbps | 1.1 Mbps | 0% |
| `vpn466639974` | 🇯🇵 JP | 287 Mbps | 1.6 Mbps | 1% |
| `vpn933450169` | 🇯🇵 JP | 425 Mbps | 3.2 Mbps | 1% |
| `vpn750706241` | 🇯🇵 JP | 326 Mbps | 2.5 Mbps | 1% |
| `vpn267521680` | 🇯🇵 JP | 152 Mbps | 1.3 Mbps | 1% |
| `vpn300065743` | 🇹🇭 TH | 343 Mbps | 4.3 Mbps | 1% |
| `vpn449287030` | 🇯🇵 JP | 185 Mbps | 2.5 Mbps | 1% |
| `vpn647204175` | 🇯🇵 JP | 189 Mbps | 2.7 Mbps | 1% |

Most honest of this round: `vpn648203125` (13 Mbps), `vpn701561709` (14 Mbps), `vpn757870457` (8 Mbps), `vpn310756240` (26 Mbps), `vpn548061161` (14 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `opengw` | 🇷🇴 RO | 🇯🇵 JP | `187.15.135.234` | 4.6 Mbps |

## 📈 History

Alive % trend (last 12 runs): `██▇▆▆▁▄▅▄▃▄█`

Avg measured speed (Mbps): `▆▇▁▇▁██▆▁▅▁▆`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-11-06 09:50:11 UTC | 96 | 69 | 72% | 11.8 | 26.2 | 0 |
| 2026-10-05 14:10:31 UTC | 95 | 434 | 45% | 8.8 | 52.2 | 4 |
| 2026-10-05 05:01:08 UTC | 94 | 394 | 44% | 10.9 | 50.4 | 3 |
| 2026-10-03 16:01:20 UTC | 98 | 368 | 45% | 8.8 | 33.1 | 4 |
| 2026-10-03 11:25:01 UTC | 99 | 388 | 52% | 11.8 | 37.9 | 5 |
| 2026-10-03 04:45:33 UTC | 94 | 322 | 49% | 12.6 | 77.0 | 5 |
| 2026-10-02 22:01:53 UTC | 97 | 164 | 28% | 12.9 | 97.8 | 5 |
| 2026-10-02 05:01:43 UTC | 97 | 289 | 57% | 9.1 | 54.4 | 5 |
| 2026-10-01 05:13:27 UTC | 96 | 248 | 59% | 12.1 | 73.6 | 6 |
| 2026-09-30 04:59:45 UTC | 93 | 214 | 63% | 8.7 | 23.2 | 7 |
| 2026-09-29 04:50:31 UTC | 91 | 191 | 73% | 11.9 | 80.1 | 3 |
| 2026-09-29 04:45:58 UTC | 93 | 126 | 70% | 11.4 | 53.6 | 2 |

## ⚙️ How the pipeline works

```mermaid
flowchart LR
    C["cron: daily 03:23 UTC"] --> F["fetch vpngate.net CSV API"]
    F --> L["log raw + meta"]
    L --> CL["clean + type-check"]
    CL --> D["dedupe hostname + IP"]
    D --> A["archive .csv.gz snapshot"]
    D --> T["REAL test: OpenVPN tunnel per server<br/>egress + geo + throughput"]
    T --> R["report: README + badges + history"]
    R --> P["commit and push"]
```

1. **Fetch** — `GET /api/iphone/` with retries and endpoint fallback; responses are validated (the API sometimes serves an empty placeholder page to datacenter IPs) and the raw bytes are logged and hashed (sha256).
2. **Clean** — parse the special CSV (`*vpn_servers` marker, `#`-prefixed header), type-check every numeric field, validate IPs, drop broken rows, strip noise.
3. **Dedupe** — remove exact `(HostName, IP)` duplicates, then same-IP entries keeping the highest-scoring one.
4. **Archive** — every run writes an immutable gzipped snapshot to `archive/` (auto-pruned to the newest 360 ≈ 90 days).
5. **Test — the real deal.** For **every** server, every run — not just the API's current list, but **the union of every server that has ever appeared** within the 30-day recall window (kept in `data/known_servers.json`): decode the shared VPN Gate OpenVPN template (all servers ship the same CA + dummy client cert — verified), rebuild each server's config with its remembered `(proto, port)`, force it onto a per-worker `tun` device, disable pushed routes, pin two /32 routes through the tunnel to per-worker Cloudflare anycast IPs, wait for *Initialization Sequence Completed*, then verify egress (`cdn-cgi/trace` through the tunnel must return a foreign exit IP + real exit country) and measure a 5 MB download through the same tunnel. Up to 48 isolated tunnels run in parallel; a server that never completes the handshake is hard-killed after 25 s.
6. **Report** — this README, four live badges, `latest.json`, `summary.json` and the `history.jsonl` log are regenerated and committed by `github-actions[bot]`.

## 📁 Data files & programmatic use

All results are in this repo — hotlink them straight from `https://github.com/onlyactions/vpngate-monitor`:

- [`data/latest.json`](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/latest.json) — the merged dataset: every cleaned server + its latest real test result
- [`data/servers_clean.csv`](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/servers_clean.csv) — cleaned, deduplicated server list (no bulky config blobs)
- [`data/summary.json`](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/summary.json) — compact run summary with failure breakdown
- [`data/history.jsonl`](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/history.jsonl) — one JSON line per run, append-only
- [`archive/`](https://github.com/onlyactions/vpngate-monitor/tree/main/archive) — immutable gzipped snapshots of every run
- full logs, raw API response and per-server error details are attached to each [Actions run](https://github.com/onlyactions/vpngate-monitor/actions) as artifacts (30-day retention)

Grab a working VPN right now:

```bash
curl -s https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/data/latest.json \
  | python3 -c "import json,sys;[print(s['IP'],s['CountryShort'],s['test']['download_mbps'],'Mbps') for s in json.load(sys.stdin) if s['test'] and s['test']['alive']]" \
  | sort -k3 -nr | head
```

Field units: `Score` points · `Ping` ms · `Speed` bit/s (self-reported) · `Uptime` ms · `TotalUsers` count · `TotalTraffic` bytes · `download_mbps` Mbps (measured through the tunnel).

## 🔬 Methodology & caveats

- **Real tunnels, not CSV checks.** A server only counts as alive if OpenVPN completed its handshake *and* an HTTPS request bound to the tunnel egressed with a foreign IP. A server whose tunnel silently black-holes traffic fails the egress step and is reported dead.
- **No DNS through the VPN.** Test destinations are pinned with `curl --resolve` to per-worker Cloudflare anycast addresses, so a broken/hijacking VPN DNS can never fake a success.
- **Throughput** is one 5 MB download to `speed.cloudflare.com` through the live tunnel — a sample, not a lab measurement.
- **Vantage point**: GitHub Actions runners (Azure, usually US/EU). A server that is slow from there may be fast from your country, and vice versa.
- **Fairness**: volunteer servers are shared — measured speeds dip when many clients are connected (`NumVpnSessions` is listed).
- **Security**: test traffic is TLS to Cloudflare only; we never send anything sensitive through volunteer servers. Neither should you — assume the operator can see traffic metadata.

## ⚠️ Disclaimer

- [VPN Gate](https://www.vpngate.net/en/) is an academic experiment by the University of Tsukuba, Japan (Daiyuu Nobori & co). This project is an independent monitor of its public API and is **not affiliated** with it.
- VPN servers are run by volunteers; some keep connection logs (see `LogType`). Use them legally and responsibly; do not route anything private or illegal through them.
- Data is provided **as-is** for research/educational purposes.

## 📄 License

Code: MIT. Data: originates from VPN Gate's public API — respect their terms.

---
*Auto-generated by [run #2](https://github.com/onlyactions/vpngate-monitor/actions/runs/42337563970) at 2026-11-07 04:16:13 UTC. Next scheduled run: daily at 03:23 UTC.*
