# 🛡️ VPN Gate Monitor

> **Daily** this repo fetches the complete public [VPN Gate](https://www.vpngate.net/en/) server list, **cleans, deduplicates and archives** it — and then does the part that matters: it **opens a real OpenVPN tunnel to every single listed server**, verifies that traffic genuinely exits through it, checks *where* it exits and **who operates that exit** (ISP, AS, IP reputation), and measures real download **and upload** throughput.
>
> **Everything below this line is the auto-generated living report. No hand-edited numbers.**

[![pipeline](https://github.com/onlyactions/vpngate-monitor/actions/workflows/vpngate.yml/badge.svg)](https://github.com/onlyactions/vpngate-monitor/actions/workflows/vpngate.yml)
[![servers tracked](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fservers.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/servers.json)
[![verified alive](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Falive.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/alive.json)
[![avg measured ↓](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fspeed.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/speed.json)
[![avg measured ↑](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fup-speed.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/up-speed.json)
[![clean exits](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fclean.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/clean.json)
[![last run](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fonlyactions%2Fvpngate-monitor%2Fmain%2Fbadges%2Fupdated.json)](https://raw.githubusercontent.com/onlyactions/vpngate-monitor/main/badges/updated.json)

## 📊 Latest results

| | |
|---|---|
| **Run** | [#22 · view run](https://github.com/onlyactions/vpngate-monitor/actions/runs/45547626346) · 2026-11-25 04:34:32 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **95** |
| **Duplicates removed** | 0 exact + 1 same-IP |
| **Servers tested** | **1,559 of 1,559** — all 95 current + 1,464 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **524** — 68 from the current list + 456 historical ♻️ |
| **❌ Dead / unusable** | 1,035 |
| **Usability** | **71.6%** of everything VPN Gate lists right now actually works |
| **⚡ Measured download (avg / median / max)** | **12.9 / 14.2 / 52.4 Mbps** |
| **⚡ Measured upload (avg / max)** | **2.2 / 6.9 Mbps** |
| **🧼 Exit IP reputation** | **172** unflagged ('clean') · **523** residential · **7** mobile · rest datacenter/flagged |
| **🚀 Fastest verified** | **vpn491348575** · 🇨🇦 Canada · **52.4 Mbps** |
| **🧭 Exit-country mismatches** | 1 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 2.8 s |

## 🚀 Fastest verified servers

Each row is fully described by its display name (see [How to read the names](#-how-to-read-the-names) below): country, ISP + AS of the **verified exit IP**, measured download/upload speed, the exit IP itself and its reputation.

```text
1. 🇨🇦 CA | Shaw Communications AS6327 | ↓52.4 ↑6.9Mbps | 184.68.30.115 | MOB·Clean  (vpn491348575)
2. 🇯🇵 JP | Sony Network AS2527 | ↓29.4 ↑3.9Mbps | 131.147.36.66 | RES·Flag  (vpn189019752)
3. 🇯🇵 JP | Sony Network AS2527 | ↓29.1 ↑3.1Mbps | 118.240.3.52 | RES·Flag  (vpn630509601)
4. 🇯🇵 JP | Sony Network AS2527 | ↓28.8 ↑3.8Mbps | 223.132.1.215 | RES·Flag  (vpn482888807)
5. 🇯🇵 JP | Sony Network AS2527 | ↓28.4 ↑3.8Mbps | 39.111.221.149 | RES·Flag  (vpn167234104)
6. 🇯🇵 JP | NTT Communications AS4713 | ↓28.0 ↑3.4Mbps | 180.43.107.71 | RES·Flag  (vpn459755685)
7. 🇯🇵 JP | ASAHI Net AS4685 | ↓27.3 ↑3.7Mbps | 138.64.83.11 | RES·Clean  (vpn939813472)
8. 🇯🇵 JP | Sony Network AS2527 | ↓27.2 ↑3.6Mbps | 147.192.140.77 | RES·Flag  (vpn831230332)
9. 🇯🇵 JP | ASAHI Net AS4685 | ↓26.7 ↑3.5Mbps | 138.64.96.118 | RES·Flag  (vpn909153861)
10. 🇯🇵 JP | Chubu AS18126 | ↓26.5 ↑3.5Mbps | 118.105.160.215 | RES·Flag  (vpn702119480)
```

| # | Server | Country | Endpoint | Exit IP (verified) | ISP · AS · rep | Measured ↓ | Measured ↑ | Claimed ↓ | Score |
|---:|---|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn491348575` | 🇨🇦 CA | `184.68.30.116:1697`/tcp | `184.68.30.115` | Shaw Communications AS6327 MOB·Clean | **52.4 Mbps** | 6.9 Mbps | 17.4 Mbps | 1,154,690 |
| 2 | `vpn189019752` | 🇯🇵 JP | `131.147.36.66:1195`/udp | `131.147.36.66` | Sony Network AS2527 RES·Flag | **29.4 Mbps** | 3.9 Mbps | 932.1 Mbps | 610,142 |
| 3 | `vpn630509601` | 🇯🇵 JP | `118.240.3.52:1195`/udp | `118.240.3.52` | Sony Network AS2527 RES·Flag | **29.1 Mbps** | 3.1 Mbps | 893.1 Mbps | 617,313 |
| 4 | `vpn482888807` | 🇯🇵 JP | `223.132.1.215:1195`/udp | `223.132.1.215` | Sony Network AS2527 RES·Flag | **28.8 Mbps** | 3.8 Mbps | 925.0 Mbps | 1,156,381 |
| 5 | `vpn167234104` | 🇯🇵 JP | `39.111.221.149:1195`/udp | `39.111.221.149` | Sony Network AS2527 RES·Flag | **28.4 Mbps** | 3.8 Mbps | 715.4 Mbps | 618,855 |
| 6 | `vpn459755685` | 🇯🇵 JP | `180.43.107.71:1563`/udp | `180.43.107.71` | NTT Communications AS4713 RES·Flag | **28.0 Mbps** | 3.4 Mbps | 93.3 Mbps | 720,658 |
| 7 | `vpn939813472` | 🇯🇵 JP | `138.64.83.11:23875`/udp | `138.64.83.11` | ASAHI Net AS4685 RES·Clean | **27.3 Mbps** | 3.7 Mbps | 598.6 Mbps | 579,285 |
| 8 | `vpn831230332` | 🇯🇵 JP | `147.192.140.77:1195`/udp | `147.192.140.77` | Sony Network AS2527 RES·Flag | **27.2 Mbps** | 3.6 Mbps | 957.6 Mbps | 702,065 |
| 9 | `vpn909153861` | 🇯🇵 JP | `138.64.96.118:14355`/udp | `138.64.96.118` | ASAHI Net AS4685 RES·Flag | **26.7 Mbps** | 3.5 Mbps | 185.0 Mbps | 663,610 |
| 10 | `vpn702119480` | 🇯🇵 JP | `118.105.160.215:1958`/udp | `118.105.160.215` | Chubu AS18126 RES·Flag | **26.5 Mbps** | 3.5 Mbps | 833.4 Mbps | 611,183 |

*Measured = 5 MB download + 512 KB upload through the live tunnel to speed.cloudflare.com. Claimed = the server's self-reported line speed in the VPN Gate API. Exit IP/ISP/reputation are looked up from ip-api after the tunnels close. 'Historical' servers are no longer in the API's current top list but still answered our tunnel — we keep re-testing everything we have ever seen.*

## 🏷️ How to read the names

Every verified server gets a display name that tells you everything about **what you would actually connect to**:

```text
🇩🇪 DE | Contabo AS141995 | ↓12.0 ↑1.2Mbps | 84.247.155.196 | DC·Clean
```

| part | meaning |
|------|---------|
| `🇩🇪 DE` | country of the **verified exit** (not what the server claims) |
| `Contabo AS141995` | ISP / organization operating the exit IP and its autonomous system |
| `↓12.0 ↑1.2Mbps` | download / upload measured through the live tunnel (`?` = test failed) |
| `84.247.155.196` | the verified exit IP — your egress address |
| `DC` | datacenter / hosting IP (most VPN Gate servers) |
| `RES` | residential IP — usually the best bet against bot/VPN blocks |
| `MOB` | mobile / carrier IP (CGNAT) |
| `Clean` | exit not listed in ip-api's proxy/VPN/Tor database |
| `Flag` | exit listed as proxy/VPN — expect streaming blocks |

## ⭐ Top-scored & verified alive

| # | Server | Country | Score | Claimed ↓ | Measured ↓ | Measured ↑ | Sessions | Uptime | Log policy |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | `public-vpn-261` | 🇯🇵 JP | 3,070,532 | 251.5 Mbps | 4.9 Mbps | 2.3 Mbps | 107 | 31.3 d | 2weeks |
| 2 | `public-vpn-253` | 🇯🇵 JP | 3,013,832 | 218.4 Mbps | 10.9 Mbps | 2.5 Mbps | 152 | 31.3 d | 2weeks |
| 3 | `public-vpn-258` | 🇯🇵 JP | 2,927,383 | 194.9 Mbps | 7.2 Mbps | 0.6 Mbps | 64 | 16.9 d | 2weeks |
| 4 | `public-vpn-0` | 🇯🇵 JP | 2,899,483 | 727.6 Mbps | 10.2 Mbps | 2.9 Mbps | 80 | 26.9 d | 2weeks |
| 5 | `public-vpn-126` | 🇯🇵 JP | 2,878,776 | 569.1 Mbps | 15.9 Mbps | 2.2 Mbps | 117 | 29.9 d | 2weeks |
| 6 | `public-vpn-78` | 🇯🇵 JP | 2,853,500 | 294.3 Mbps | 14.2 Mbps | 2.8 Mbps | 126 | 14.9 d | 2weeks |
| 7 | `public-vpn-202` | 🇯🇵 JP | 2,849,321 | 236.5 Mbps | 11.7 Mbps | 0.9 Mbps | 78 | 23.9 d | 2weeks |
| 8 | `public-vpn-185` | 🇯🇵 JP | 2,833,369 | 309.4 Mbps | 9.4 Mbps | 0.3 Mbps | 102 | 31.9 d | 2weeks |
| 9 | `public-vpn-206` | 🇯🇵 JP | 2,825,566 | 328.0 Mbps | 4.1 Mbps | 2.0 Mbps | 70 | 20.9 d | 2weeks |
| 10 | `public-vpn-95` | 🇯🇵 JP | 2,779,114 | 1,163.6 Mbps | 15.2 Mbps | 2.3 Mbps | 256 | 24.9 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 708 | 269 | 29.4 Mbps | `vpn189019752` |
| 🇰🇷 Korea Republic of (KR) | 522 | 214 | 23.7 Mbps | `vpn711923274` |
| 🇷🇺 Russian Federation (RU) | 125 | 9 | 14.1 Mbps | `vpn526802829` |
| 🇹🇭 Thailand (TH) | 62 | 7 | 18.8 Mbps | `vpn855688522` |
| 🇺🇸 United States (US) | 38 | 7 | 2.4 Mbps | `vpn519502227` |
| 🇻🇳 Viet Nam (VN) | 22 | 3 | 12.7 Mbps | `vpn182757269` |
| 🇦🇺 Australia (AU) | 9 | 2 | 14.7 Mbps | `vpn863521180` |
| 🇦🇷 Argentina (AR) | 5 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 5 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 5 | 0 | 0.0 Mbps | `` |
| 🇨🇦 Canada (CA) | 4 | 2 | 52.4 Mbps | `vpn491348575` |
| 🇮🇩 Indonesia (ID) | 4 | 2 | 14.4 Mbps | `vpn104-cyberdewata` |
| 🇲🇽 Mexico (MX) | 4 | 2 | 12.0 Mbps | `vpn156777673` |
| 🇦🇪 United Arab Emirates (AE) | 3 | 0 | 0.0 Mbps | `` |
| 🇬🇧 United Kingdom (GB) | 3 | 0 | 0.0 Mbps | `` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 3 | 0 | 0.0 Mbps | `` |
| 🇮🇳 India (IN) | 3 | 0 | 0.0 Mbps | `` |
| 🇲🇲 Myanmar (MM) | 3 | 1 | 13.8 Mbps | `vpn477566769` |
| 🇧🇾 Belarus (BY) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 2 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 2 | 0 | 0.0 Mbps | `` |
| 🇭🇰 Hong Kong (HK) | 2 | 1 | 0.8 Mbps | `vpn942711940` |
| 🇲🇾 Malaysia (MY) | 2 | 0 | 0.0 Mbps | `` |
| 🇳🇿 New Zealand (NZ) | 2 | 1 | 24.3 Mbps | `vpn640114063` |
| 🇵🇦 Panama (PA) | 2 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 2 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 2 | 1 | 0.9 Mbps | `vpn503500791` |
| 🇻🇪 Venezuela (VE) | 2 | 1 | 22.5 Mbps | `vpn589121690` |
| 🇨🇭 Switzerland (CH) | 1 | 1 | 2.4 Mbps | `vpn783506990` |
| 🇨🇴 Colombia (CO) | 1 | 0 | 0.0 Mbps | `` |
| 🇩🇪 Germany (DE) | 1 | 0 | 0.0 Mbps | `` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 0 | 0.0 Mbps | `` |
| 🇮🇹 Italy (IT) | 1 | 0 | 0.0 Mbps | `` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇳🇱 Netherlands (NL) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇸 Palestinian Territory Occupied (PS) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇹 Portugal (PT) | 1 | 0 | 0.0 Mbps | `` |
| 🇷🇴 Romania (RO) | 1 | 1 | 7.7 Mbps | `opengw` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn301434747` | 🇺🇸 US | 139 Mbps | 0.1 Mbps | 0% |
| `vpn517964018` | 🇰🇷 KR | 87 Mbps | 0.1 Mbps | 0% |
| `vpn949825988` | 🇯🇵 JP | 260 Mbps | 0.3 Mbps | 0% |
| `vpn406459834` | 🇰🇷 KR | 863 Mbps | 1.1 Mbps | 0% |
| `public-vpn-37` | 🇯🇵 JP | 1,394 Mbps | 2.0 Mbps | 0% |
| `vpn392875556` | 🇷🇺 RU | 165 Mbps | 0.3 Mbps | 0% |
| `vpn113368656` | 🇯🇵 JP | 257 Mbps | 0.6 Mbps | 0% |
| `vpn475858293` | 🇯🇵 JP | 249 Mbps | 0.6 Mbps | 0% |
| `vpn699620341` | 🇰🇷 KR | 334 Mbps | 0.8 Mbps | 0% |
| `vpn750706241` | 🇯🇵 JP | 332 Mbps | 1.0 Mbps | 0% |

Most honest of this round: `vpn501671840` (13 Mbps), `vpn491348575` (52 Mbps), `vpn244093263` (18 Mbps), `vpn890053288` (11 Mbps), `vpn151821463` (18 Mbps).

## 🧭 Exit-country mismatches

These servers are listed under one country but your traffic **actually exits somewhere else** (verified via Cloudflare's geo view of the exit IP) — useful to know before you trust one:

| Server | Claims | Actually exits via | Exit IP | Measured ↓ |
|---|---|---|---|---:|
| `opengw` | 🇷🇴 RO | 🇯🇵 JP | `187.15.135.101` | 7.7 Mbps |

## 📈 History

Alive % trend (last 32 runs): `██▇▆▆▁▄▅▄▃▄█▄▄▄▄▄▄▃▃▃▃▃▂▃▂▂▂▂▁▂▂`

Avg measured speed (Mbps): `▄▅▁▅▁▆▅▄▁▃▁▄▃▄▄▅▅██▄▅█▃▇▄▂▅▅▆▅▆█`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Avg ↑ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-11-24 14:41:04 UTC | 95 | 550 | 36% | 14.6 | 38.0 | 2.5 | 2 |
| 2026-11-24 14:29:24 UTC | 94 | 505 | 35% | 13.2 | 31.7 | 0.0 | 1 |
| 2026-11-24 04:29:47 UTC | 87 | 452 | 33% | 12.1 | 39.7 | 0.0 | 1 |
| 2026-11-23 04:37:36 UTC | 92 | 479 | 36% | 13.3 | 39.2 | 0.0 | 2 |
| 2026-11-22 04:22:09 UTC | 95 | 445 | 35% | 12.3 | 35.6 | 0.0 | 2 |
| 2026-11-21 04:18:18 UTC | 93 | 435 | 36% | 12.0 | 28.8 | 0.0 | 2 |
| 2026-11-20 04:21:47 UTC | 93 | 436 | 38% | 9.8 | 39.0 | 0.0 | 2 |
| 2026-11-19 04:25:57 UTC | 95 | 429 | 40% | 11.4 | 47.3 | 0.0 | 3 |
| 2026-11-18 04:22:25 UTC | 92 | 389 | 39% | 14.2 | 37.8 | 0.0 | 2 |
| 2026-11-17 04:21:05 UTC | 98 | 397 | 42% | 11.0 | 26.6 | 0.0 | 3 |
| 2026-11-16 04:58:07 UTC | 94 | 366 | 42% | 14.3 | 35.9 | 0.0 | 1 |
| 2026-11-15 04:20:41 UTC | 90 | 334 | 41% | 12.4 | 29.8 | 0.0 | 0 |
| 2026-11-14 04:17:29 UTC | 98 | 323 | 44% | 11.3 | 54.8 | 0.0 | 2 |
| 2026-11-13 04:22:35 UTC | 97 | 295 | 44% | 14.9 | 46.8 | 0.0 | 1 |
| 2026-11-12 04:23:10 UTC | 93 | 272 | 46% | 15.0 | 29.9 | 0.0 | 0 |

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
5. **Test — the real deal.** For **every** server, every run — not just the API's current list, but **the union of every server that has ever appeared** within the 30-day recall window (kept in `data/known_servers.json`): decode the shared VPN Gate OpenVPN template (all servers ship the same CA + dummy client cert — verified), rebuild each server's config with its remembered `(proto, port)`, force it onto a per-worker `tun` device, disable pushed routes, pin two /32 routes through the tunnel to per-worker Cloudflare anycast IPs, wait for *Initialization Sequence Completed*, then verify egress (`cdn-cgi/trace` through the tunnel must return a foreign exit IP + real exit country), measure a 5 MB download and a 512 KB upload through the same tunnel, and — once all tunnels are down — batch-lookup every verified exit IP at ip-api to add the ISP, AS and IP-reputation flags (datacenter / residential / mobile / proxy-DB) that you see in the display names. Up to 48 isolated tunnels run in parallel; a server that never completes the handshake is hard-killed after 25 s.
6. **Report** — this README, six live badges, `latest.json`, `summary.json` and the `history.jsonl` log are regenerated and committed by `github-actions[bot]`.

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

Field units: `Score` points · `Ping` ms · `Speed` bit/s (self-reported) · `Uptime` ms · `TotalUsers` count · `TotalTraffic` bytes · `download_mbps` / `upload_mbps` Mbps (measured through the tunnel) · `exit_*` = ISP/AS/city/reputation of the verified exit IP · `display_name` = the full-descriptor name.

## 🔬 Methodology & caveats

- **Real tunnels, not CSV checks.** A server only counts as alive if OpenVPN completed its handshake *and* an HTTPS request bound to the tunnel egressed with a foreign IP. A server whose tunnel silently black-holes traffic fails the egress step and is reported dead.
- **No DNS through the VPN.** Test destinations are pinned with `curl --resolve` to per-worker Cloudflare anycast addresses, so a broken/hijacking VPN DNS can never fake a success.
- **Throughput** is one 5 MB download plus one 512 KB upload to `speed.cloudflare.com` through the live tunnel — a sample, not a lab measurement.
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
*Auto-generated by [run #22](https://github.com/onlyactions/vpngate-monitor/actions/runs/45547626346) at 2026-11-25 04:45:14 UTC. Next scheduled run: daily 03:23 UTC.*
