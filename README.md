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
| **Run** | [#3 · view run](https://github.com/onlyactions/vpngate-monitor/actions/runs/42446246272) · 2026-11-08 04:18:29 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **97** |
| **Duplicates removed** | 0 exact + 1 same-IP |
| **Servers tested** | **275 of 275** — all 97 current + 178 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **134** — 61 from the current list + 73 historical ♻️ |
| **❌ Dead / unusable** | 141 |
| **Usability** | **62.9%** of everything VPN Gate lists right now actually works |
| **⚡ Measured speed (avg / median / max)** | **11.5 / 13.3 / 47.3 Mbps** |
| **🚀 Fastest verified** | **vpn258000289** · 🇺🇸 United States · **47.3 Mbps** |
| **🧭 Exit-country mismatches** | 1 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 3.1 s |

## 🚀 Fastest verified servers

| # | Server | Country | List | Endpoint | Handshake | Measured ↓ | Claimed ↓ | Score |
|---:|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn258000289` | 🇺🇸 United States | ♻️ historical | `107.15.246.139:1917`/tcp | 2.0s | **47.3 Mbps** | 140.7 Mbps | 1,905,275 |
| 2 | `vpn725064175` | 🇦🇷 Argentina | 📋 current | `186.158.120.118:5199`/udp | 2.5s | **24.9 Mbps** | 182.4 Mbps | 685,040 |
| 3 | `vpn310756240` | 🇷🇺 Russian Federation | ♻️ historical | `90.154.70.206:10131`/udp | 2.5s | **23.4 Mbps** | 44.5 Mbps | 1,515,668 |
| 4 | `vpn105725304` | 🇯🇵 Japan | 📋 current | `138.64.254.248:17649`/udp | 2.8s | **23.2 Mbps** | 234.0 Mbps | 622,036 |
| 5 | `vpn178005109` | 🇯🇵 Japan | 📋 current | `114.184.115.158:1848`/udp | 2.5s | **21.4 Mbps** | 335.8 Mbps | 635,498 |
| 6 | `vpn370389678` | 🇯🇵 Japan | 📋 current | `133.207.167.224:5626`/udp | 2.5s | **21.4 Mbps** | 310.5 Mbps | 648,364 |
| 7 | `vpn526062445` | 🇯🇵 Japan | 📋 current | `60.143.120.123:1632`/udp | 2.5s | **20.2 Mbps** | 207.5 Mbps | 1,454,780 |
| 8 | `vpn630509601` | 🇯🇵 Japan | 📋 current | `118.240.3.52:1195`/udp | 2.8s | **19.5 Mbps** | 893.1 Mbps | 617,313 |
| 9 | `vpn399630262` | 🇧🇷 Brazil | ♻️ historical | `179.135.95.98:995`/tcp | 2.8s | **19.0 Mbps** | 115.0 Mbps | 829,089 |
| 10 | `vpn631309138` | 🇹🇭 Thailand | ♻️ historical | `49.48.220.228:1671`/udp | 2.8s | **15.9 Mbps** | 430.4 Mbps | 633,077 |

*Measured = 5 MB download through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-39` | 🇯🇵 JP | 2,787,871 | 228.2 Mbps | 13.6 Mbps | 137 | 14.9 d | 2weeks |
| 2 | `public-vpn-134` | 🇯🇵 JP | 2,748,495 | 241.4 Mbps | 11.8 Mbps | 56 | 14.9 d | 2weeks |
| 3 | `public-vpn-205` | 🇯🇵 JP | 2,714,062 | 171.1 Mbps | 9.0 Mbps | 92 | 14.9 d | 2weeks |
| 4 | `public-vpn-95` | 🇯🇵 JP | 2,705,979 | 1,030.7 Mbps | 14.5 Mbps | 210 | 14.9 d | 2weeks |
| 5 | `public-vpn-164` | 🇯🇵 JP | 2,633,438 | 401.5 Mbps | 13.9 Mbps | 74 | 13.9 d | 2weeks |
| 6 | `public-vpn-74` | 🇯🇵 JP | 2,630,986 | 231.8 Mbps | 13.7 Mbps | 46 | 14.9 d | 2weeks |
| 7 | `public-vpn-200` | 🇯🇵 JP | 2,590,636 | 196.4 Mbps | 7.4 Mbps | 50 | 13.9 d | 2weeks |
| 8 | `public-vpn-203` | 🇯🇵 JP | 2,312,010 | 258.5 Mbps | 4.0 Mbps | 52 | 14.9 d | 2weeks |
| 9 | `public-vpn-142` | 🇯🇵 JP | 2,259,009 | 509.6 Mbps | 14.8 Mbps | 75 | 13.1 d | 2weeks |
| 10 | `public-vpn-105` | 🇯🇵 JP | 2,234,067 | 353.9 Mbps | 14.3 Mbps | 61 | 14.9 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 142 | 80 | 23.2 Mbps | `vpn105725304` |
| 🇰🇷 Korea Republic of (KR) | 82 | 41 | 15.2 Mbps | `vpn428888787` |
| 🇷🇺 Russian Federation (RU) | 16 | 1 | 23.4 Mbps | `vpn310756240` |
| 🇹🇭 Thailand (TH) | 12 | 3 | 15.9 Mbps | `vpn631309138` |
| 🇻🇳 Viet Nam (VN) | 5 | 2 | 9.1 Mbps | `vpn925698769` |
| 🇺🇸 United States (US) | 4 | 1 | 47.3 Mbps | `vpn258000289` |
| 🇧🇾 Belarus (BY) | 2 | 0 | 0.0 Mbps | `` |
| 🇲🇲 Myanmar (MM) | 2 | 0 | 0.0 Mbps | `` |
| 🇲🇾 Malaysia (MY) | 2 | 0 | 0.0 Mbps | `` |
| 🇦🇷 Argentina (AR) | 1 | 1 | 24.9 Mbps | `vpn725064175` |
| 🇦🇺 Australia (AU) | 1 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 1 | 1 | 19.0 Mbps | `vpn399630262` |
| 🇬🇧 United Kingdom (GB) | 1 | 1 | 0.5 Mbps | `patito` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇲🇽 Mexico (MX) | 1 | 1 | 5.0 Mbps | `vpn678204705` |
| 🇵🇭 Philippines (PH) | 1 | 1 | 8.5 Mbps | `vpn269589023` |
| 🇷🇴 Romania (RO) | 1 | 1 | 0.5 Mbps | `opengw` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `opengw` | 🇷🇴 RO | 170 Mbps | 0.5 Mbps | 0% |
| `vpn409198720` | 🇯🇵 JP | 236 Mbps | 0.7 Mbps | 0% |
| `vpn434008438` | 🇯🇵 JP | 168 Mbps | 0.7 Mbps | 0% |
| `vpn750706241` | 🇯🇵 JP | 326 Mbps | 2.5 Mbps | 1% |
| `vpn933450169` | 🇯🇵 JP | 425 Mbps | 3.3 Mbps | 1% |
| `vpn143703231` | 🇯🇵 JP | 435 Mbps | 3.5 Mbps | 1% |
| `vpn379404050` | 🇯🇵 JP | 171 Mbps | 2.1 Mbps | 1% |
| `vpn933716554` | 🇯🇵 JP | 237 Mbps | 3.0 Mbps | 1% |
| `vpn449287030` | 🇯🇵 JP | 185 Mbps | 2.6 Mbps | 1% |
| `public-vpn-95` | 🇯🇵 JP | 1,031 Mbps | 14.5 Mbps | 1% |

Most honest of this round: `vpn501671840` (10 Mbps), `vpn701561709` (15 Mbps), `vpn793886241` (14 Mbps), `vpn757870457` (11 Mbps), `vpn466281884` (4 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `opengw` | 🇷🇴 RO | 🇯🇵 JP | `187.15.134.160` | 0.5 Mbps |

## 📈 History

Alive % trend (last 13 runs): `██▇▆▆▁▄▅▄▃▄█▄`

Avg measured speed (Mbps): `▆▇▁▇▁██▆▁▅▁▆▅`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|
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
*Auto-generated by [run #3](https://github.com/onlyactions/vpngate-monitor/actions/runs/42446246272) at 2026-11-08 04:20:07 UTC. Next scheduled run: daily at 03:23 UTC.*
