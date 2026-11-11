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
| **Run** | [#6 · view run](https://github.com/onlyactions/vpngate-monitor/actions/runs/42958804834) · 2026-11-11 04:22:55 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **97** |
| **Duplicates removed** | 0 exact + 0 same-IP |
| **Servers tested** | **517 of 517** — all 97 current + 420 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **234** — 59 from the current list + 175 historical ♻️ |
| **❌ Dead / unusable** | 283 |
| **Usability** | **60.8%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **12.0 / 13.6 / 28.2 Mbps** |
| **🚀 Fastest verified** | **vpn630509601** · 🇯🇵 Japan · **28.2 Mbps** |
| **🧭 Exit-country mismatches** | 0 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.3 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn630509601` | 🇯🇵 Japan | ♻️ historical | `118.240.3.52:1195`/udp | 2.3s | **28.2 Mbps** | 893.1 Mbps | 617,313 |
| 2 | `vpn135774294` | 🇯🇵 Japan | 📋 current | `60.141.30.170:1412`/udp | 2.5s | **26.8 Mbps** | 496.2 Mbps | 809,831 |
| 3 | `kobac333` | 🇯🇵 Japan | ♻️ historical | `217.178.142.124:26114`/udp | 2.5s | **26.7 Mbps** | 167.0 Mbps | 699,400 |
| 4 | `vpn367633262` | 🇯🇵 Japan | 📋 current | `138.64.87.141:39975`/udp | 2.5s | **26.6 Mbps** | 665.7 Mbps | 670,751 |
| 5 | `vpn244638209` | 🇯🇵 Japan | 📋 current | `58.189.70.202:1217`/udp | 2.3s | **26.1 Mbps** | 861.2 Mbps | 711,925 |
| 6 | `vpn679218486` | 🇯🇵 Japan | ♻️ historical | `124.209.226.195:1752`/udp | 2.5s | **25.9 Mbps** | 682.8 Mbps | 683,399 |
| 7 | `vpn909153861` | 🇯🇵 Japan | 📋 current | `138.64.96.118:14355`/udp | 2.5s | **25.8 Mbps** | 194.2 Mbps | 812,170 |
| 8 | `vpn201737691` | 🇯🇵 Japan | ♻️ historical | `59.85.16.253:1742`/udp | 2.5s | **25.2 Mbps** | 590.9 Mbps | 1,494,450 |
| 9 | `vpn391570092` | 🇯🇵 Japan | ♻️ historical | `59.130.14.121:1376`/udp | 2.8s | **23.9 Mbps** | 859.3 Mbps | 704,675 |
| 10 | `vpn370389678` | 🇯🇵 Japan | 📋 current | `133.207.167.224:5623`/udp | 2.5s | **21.7 Mbps** | 309.8 Mbps | 859,697 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-100` | 🇯🇵 JP | 3,003,937 | 236.1 Mbps | 16.6 Mbps | 179 | 16.9 d | 2weeks |
| 2 | `public-vpn-258` | 🇯🇵 JP | 2,927,383 | 194.9 Mbps | 5.3 Mbps | 64 | 16.9 d | 2weeks |
| 3 | `public-vpn-257` | 🇯🇵 JP | 2,848,604 | 513.6 Mbps | 8.8 Mbps | 108 | 16.9 d | 2weeks |
| 4 | `public-vpn-39` | 🇯🇵 JP | 2,787,871 | 228.2 Mbps | 16.7 Mbps | 137 | 14.9 d | 2weeks |
| 5 | `public-vpn-201` | 🇯🇵 JP | 2,718,064 | 163.6 Mbps | 5.4 Mbps | 93 | 14.9 d | 2weeks |
| 6 | `public-vpn-205` | 🇯🇵 JP | 2,714,062 | 171.1 Mbps | 6.8 Mbps | 92 | 14.9 d | 2weeks |
| 7 | `public-vpn-90` | 🇯🇵 JP | 2,710,460 | 264.5 Mbps | 15.2 Mbps | 173 | 16.9 d | 2weeks |
| 8 | `public-vpn-95` | 🇯🇵 JP | 2,705,979 | 1,030.7 Mbps | 14.1 Mbps | 210 | 14.9 d | 2weeks |
| 9 | `public-vpn-52` | 🇯🇵 JP | 2,695,814 | 415.8 Mbps | 11.0 Mbps | 148 | 16.9 d | 2weeks |
| 10 | `public-vpn-164` | 🇯🇵 JP | 2,633,438 | 401.5 Mbps | 16.7 Mbps | 74 | 13.9 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 247 | 129 | 28.2 Mbps | `vpn630509601` |
| 🇰🇷 Korea Republic of (KR) | 163 | 87 | 17.6 Mbps | `vpn990126810` |
| 🇷🇺 Russian Federation (RU) | 41 | 3 | 21.0 Mbps | `vpn310756240` |
| 🇹🇭 Thailand (TH) | 18 | 2 | 17.0 Mbps | `vpn241487766` |
| 🇺🇸 United States (US) | 15 | 8 | 6.0 Mbps | `vpn250207254` |
| 🇻🇳 Viet Nam (VN) | 6 | 2 | 9.7 Mbps | `vpn923730258` |
| 🇦🇷 Argentina (AR) | 3 | 0 | 0.0 Mbps | `` |
| 🇦🇺 Australia (AU) | 2 | 0 | 0.0 Mbps | `` |
| 🇧🇾 Belarus (BY) | 2 | 0 | 0.0 Mbps | `` |
| 🇬🇧 United Kingdom (GB) | 2 | 0 | 0.0 Mbps | `` |
| 🇮🇳 India (IN) | 2 | 1 | 10.6 Mbps | `vpn359610091` |
| 🇲🇲 Myanmar (MM) | 2 | 0 | 0.0 Mbps | `` |
| 🇲🇾 Malaysia (MY) | 2 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 1 | 0 | 0.0 Mbps | `` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 1 | 0 | 0.0 Mbps | `` |
| 🇮🇩 Indonesia (ID) | 1 | 0 | 0.0 Mbps | `` |
| 🇮🇹 Italy (IT) | 1 | 0 | 0.0 Mbps | `` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇲🇽 Mexico (MX) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 1 | 1 | 2.6 Mbps | `vpn269589023` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 1 | 1 | 15.8 Mbps | `sausage` |
| 🇻🇪 Venezuela (VE) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn986723868` | 🇯🇵 JP | 223 Mbps | 0.3 Mbps | 0% |
| `vpn175155645` | 🇯🇵 JP | 38 Mbps | 0.1 Mbps | 0% |
| `vpn306037816` | 🇯🇵 JP | 554 Mbps | 2.0 Mbps | 0% |
| `vpn309240574` | 🇺🇸 US | 240 Mbps | 1.0 Mbps | 0% |
| `public-vpn-197` | 🇯🇵 JP | 208 Mbps | 1.0 Mbps | 0% |
| `vpn802629635` | 🇰🇷 KR | 369 Mbps | 2.0 Mbps | 1% |
| `vpn290770797` | 🇯🇵 JP | 81 Mbps | 0.5 Mbps | 1% |
| `vpn177768996` | 🇯🇵 JP | 2,402 Mbps | 16.4 Mbps | 1% |
| `vpn332082897` | 🇯🇵 JP | 2,296 Mbps | 16.3 Mbps | 1% |
| `vpn750706241` | 🇯🇵 JP | 332 Mbps | 2.8 Mbps | 1% |

Most honest of this round: `vpn648203125` (16 Mbps), `vpn466281884` (15 Mbps), `vpn701561709` (16 Mbps), `vpn484776697` (15 Mbps), `vpn244093263` (15 Mbps).

## 🧭 Exit-country mismatches

. ✅ Every verified server exits where it claims.

## 📈 History

Alive % trend (last 16 runs): `██▇▆▆▁▄▅▄▃▄█▄▄▄▄`

Avg measured speed (Mbps): `▆▇▁▇▁██▆▁▅▁▆▅▆▆█`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
| 2026-11-10 04:16:47 UTC | 95 | 205 | 46% | 12.6 | 65.4 | 1 |
| 2026-11-09 04:26:43 UTC | 93 | 164 | 45% | 11.4 | 39.3 | 0 |
| 2026-11-08 04:18:29 UTC | 97 | 134 | 49% | 11.5 | 47.3 | 1 |
| 2026-11-07 04:14:58 UTC | 93 | 88 | 48% | 10.9 | 27.0 | 1 |
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
*Auto-generated by [run #6](https://github.com/onlyactions/vpngate-monitor/actions/runs/42958804834) at 2026-11-11 04:26:05 UTC. Next scheduled run: daily at 03:23 UTC.*
