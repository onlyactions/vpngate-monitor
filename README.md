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
| **Run** | [#23 · view run](https://github.com/onlyactions/vpngate-monitor/actions/runs/45755748436) · 2026-11-26 04:32:13 UTC · trigger: `schedule` |
| **Servers fetched (unique)** | **94** |
| **Duplicates removed** | 0 exact + 0 same-IP |
| **Servers tested** | **1,590 of 1,590** — all 94 current + 1,496 historical (every server seen in the API within 30 days) |
| **✅ Verified alive** (tunnel up + egress proven) | **533** — 52 from the current list + 481 historical ♻️ |
| **❌ Dead / unusable** | 1,057 |
| **Usability** | **55.3%** of everything VPN Gate lists right now actually works |
| **⚡ Measured download (avg / median / max)** | **12.9 / 14.2 / 63.8 Mbps** |
| **⚡ Measured upload (avg / max)** | **2.3 / 11.3 Mbps** |
| **🧼 Exit IP reputation** | **168** unflagged ('clean') · **532** residential · **5** mobile · rest datacenter/flagged |
| **🚀 Fastest verified** | **vpn932993769** · 🇺🇸 United States · **63.8 Mbps** |
| **🧭 Exit-country mismatches** | 0 (server exits somewhere else than it claims) |
| **🤝 Handshake time (alive, avg)** | 2.8 s |

## 🚀 Fastest verified servers

Each row is fully described by its display name (see [How to read the names](#-how-to-read-the-names) below): country, ISP + AS of the **verified exit IP**, measured download/upload speed, the exit IP itself and its reputation.

```text
1. 🇺🇸 US | Frontier AS5650 | ↓63.8 ↑9.9Mbps | 47.150.212.85 | RES·Clean  (vpn932993769)
2. 🇨🇦 CA | Shaw Communications AS6327 | ↓38.9 ↑9.1Mbps | 184.68.30.115 | MOB·Clean  (vpn491348575)
3. 🇺🇸 US | Isomedia AS18530 | ↓38.8 ↑6.9Mbps | 66.114.142.213 | RES·Flag  (vpn407625834)
4. 🇰🇷 KR | Korea Telecom AS4766 | ↓29.7 ↑3.9Mbps | 220.125.128.62 | RES·Flag  (vpn980553333)
5. 🇯🇵 JP | DION (KDDI AS2516 | ↓29.5 ↑3.9Mbps | 124.209.226.195 | RES·Flag  (vpn679218486)
6. 🇯🇵 JP | Sony Network AS2527 | ↓29.4 ↑3.9Mbps | 39.111.221.149 | RES·Flag  (vpn167234104)
7. 🇯🇵 JP | ASAHI Net AS4685 | ↓28.4 ↑3.8Mbps | 138.64.81.88 | RES·Flag  (vpn419460835)
8. 🇯🇵 JP | ARTERIA Networks AS2519 | ↓27.8 ↑3.2Mbps | 133.32.133.240 | RES·Flag  (vpn537511968)
9. 🇯🇵 JP | DION (KDDI AS2516 | ↓27.6 ↑3.8Mbps | 118.154.9.31 | RES·Clean  (vpn358380061)
10. 🇯🇵 JP | Sony Network AS2527 | ↓27.6 ↑3.8Mbps | 131.147.36.66 | RES·Flag  (vpn189019752)
```

| # | Server | Country | Endpoint | Exit IP (verified) | ISP · AS · rep | Measured ↓ | Measured ↑ | Claimed ↓ | Score |
|---:|---|---|---|---|---|---:|---:|---:|---:|
| 1 | `vpn932993769` | 🇺🇸 US | `47.150.212.85:1785`/tcp | `47.150.212.85` | Frontier AS5650 RES·Clean | **63.8 Mbps** | 9.9 Mbps | 167.9 Mbps | 1,992,640 |
| 2 | `vpn491348575` | 🇨🇦 CA | `184.68.30.116:1697`/tcp | `184.68.30.115` | Shaw Communications AS6327 MOB·Clean | **38.9 Mbps** | 9.1 Mbps | 17.4 Mbps | 1,154,690 |
| 3 | `vpn407625834` | 🇺🇸 US | `66.114.142.213:1357`/tcp | `66.114.142.213` | Isomedia AS18530 RES·Flag | **38.8 Mbps** | 6.9 Mbps | 180.7 Mbps | 1,958,117 |
| 4 | `vpn980553333` | 🇰🇷 KR | `220.125.128.62:1959`/udp | `220.125.128.62` | Korea Telecom AS4766 RES·Flag | **29.7 Mbps** | 3.9 Mbps | 99.9 Mbps | 667,111 |
| 5 | `vpn679218486` | 🇯🇵 JP | `124.209.226.195:1752`/udp | `124.209.226.195` | DION (KDDI AS2516 RES·Flag | **29.5 Mbps** | 3.9 Mbps | 462.5 Mbps | 662,622 |
| 6 | `vpn167234104` | 🇯🇵 JP | `39.111.221.149:1195`/udp | `39.111.221.149` | Sony Network AS2527 RES·Flag | **29.4 Mbps** | 3.9 Mbps | 715.4 Mbps | 618,855 |
| 7 | `vpn419460835` | 🇯🇵 JP | `138.64.81.88:55515`/udp | `138.64.81.88` | ASAHI Net AS4685 RES·Flag | **28.4 Mbps** | 3.8 Mbps | 30.6 Mbps | 1,029,210 |
| 8 | `vpn537511968` | 🇯🇵 JP | `133.32.133.240:7610`/udp | `133.32.133.240` | ARTERIA Networks AS2519 RES·Flag | **27.8 Mbps** | 3.2 Mbps | 529.5 Mbps | 618,402 |
| 9 | `vpn358380061` | 🇯🇵 JP | `118.154.9.31:1543`/udp | `118.154.9.31` | DION (KDDI AS2516 RES·Clean | **27.6 Mbps** | 3.8 Mbps | 817.6 Mbps | 715,842 |
| 10 | `vpn189019752` | 🇯🇵 JP | `131.147.36.66:1195`/udp | `131.147.36.66` | Sony Network AS2527 RES·Flag | **27.6 Mbps** | 3.8 Mbps | 932.1 Mbps | 610,142 |

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
| 1 | `public-vpn-261` | 🇯🇵 JP | 3,070,532 | 251.5 Mbps | 8.8 Mbps | 1.4 Mbps | 107 | 31.3 d | 2weeks |
| 2 | `public-vpn-253` | 🇯🇵 JP | 3,013,832 | 218.4 Mbps | 14.2 Mbps | 1.3 Mbps | 152 | 31.3 d | 2weeks |
| 3 | `public-vpn-100` | 🇯🇵 JP | 3,003,937 | 236.1 Mbps | 16.0 Mbps | 3.0 Mbps | 179 | 16.9 d | 2weeks |
| 4 | `public-vpn-229` | 🇯🇵 JP | 2,935,826 | 99.1 Mbps | 3.9 Mbps | 1.0 Mbps | 140 | 29.9 d | 2weeks |
| 5 | `public-vpn-126` | 🇯🇵 JP | 2,878,776 | 569.1 Mbps | 17.3 Mbps | 3.0 Mbps | 117 | 29.9 d | 2weeks |
| 6 | `public-vpn-202` | 🇯🇵 JP | 2,849,321 | 236.5 Mbps | 8.1 Mbps | 0.7 Mbps | 78 | 23.9 d | 2weeks |
| 7 | `public-vpn-71` | 🇯🇵 JP | 2,846,143 | 286.1 Mbps | 15.1 Mbps | 2.9 Mbps | 80 | 32.9 d | 2weeks |
| 8 | `public-vpn-160` | 🇯🇵 JP | 2,839,108 | 290.8 Mbps | 9.7 Mbps | 1.9 Mbps | 153 | 32.9 d | 2weeks |
| 9 | `public-vpn-185` | 🇯🇵 JP | 2,833,369 | 234.7 Mbps | 15.5 Mbps | 1.1 Mbps | 125 | 32.9 d | 2weeks |
| 10 | `public-vpn-206` | 🇯🇵 JP | 2,825,566 | 328.0 Mbps | 17.0 Mbps | 0.5 Mbps | 70 | 20.9 d | 2weeks |

## 🌍 Countries

| Country | Servers | Verified alive | Best measured ↓ | Fastest server |
|---|---:|---:|---:|---|
| 🇯🇵 Japan (JP) | 722 | 262 | 29.5 Mbps | `vpn679218486` |
| 🇰🇷 Korea Republic of (KR) | 529 | 229 | 29.7 Mbps | `vpn980553333` |
| 🇷🇺 Russian Federation (RU) | 129 | 12 | 18.4 Mbps | `vpn908098700` |
| 🇹🇭 Thailand (TH) | 65 | 5 | 18.3 Mbps | `vpn719752522` |
| 🇺🇸 United States (US) | 39 | 8 | 63.8 Mbps | `vpn932993769` |
| 🇻🇳 Viet Nam (VN) | 22 | 2 | 12.8 Mbps | `vpn182757269` |
| 🇦🇺 Australia (AU) | 9 | 2 | 14.3 Mbps | `vpn863521180` |
| 🇦🇷 Argentina (AR) | 5 | 0 | 0.0 Mbps | `` |
| 🇧🇷 Brazil (BR) | 5 | 0 | 0.0 Mbps | `` |
| 🇵🇪 Peru (PE) | 5 | 0 | 0.0 Mbps | `` |
| 🇨🇦 Canada (CA) | 4 | 2 | 38.9 Mbps | `vpn491348575` |
| 🇮🇩 Indonesia (ID) | 4 | 2 | 14.8 Mbps | `vpn104-cyberdewata` |
| 🇲🇽 Mexico (MX) | 4 | 2 | 27.1 Mbps | `vpn678204705` |
| 🇦🇪 United Arab Emirates (AE) | 3 | 0 | 0.0 Mbps | `` |
| 🇬🇧 United Kingdom (GB) | 3 | 0 | 0.0 Mbps | `` |
| 🇭🇷 Croatia (LOCAL Name: Hrvatska) (HR) | 3 | 0 | 0.0 Mbps | `` |
| 🇮🇳 India (IN) | 3 | 1 | 9.3 Mbps | `vpn359610091` |
| 🇲🇲 Myanmar (MM) | 3 | 1 | 14.2 Mbps | `vpn477566769` |
| 🇻🇪 Venezuela (VE) | 3 | 1 | 20.5 Mbps | `vpn589121690` |
| 🇧🇾 Belarus (BY) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇳 China (CN) | 2 | 0 | 0.0 Mbps | `` |
| 🇨🇴 Colombia (CO) | 2 | 0 | 0.0 Mbps | `` |
| 🇪🇨 Ecuador (EC) | 2 | 0 | 0.0 Mbps | `` |
| 🇭🇰 Hong Kong (HK) | 2 | 1 | 0.9 Mbps | `vpn942711940` |
| 🇲🇾 Malaysia (MY) | 2 | 0 | 0.0 Mbps | `` |
| 🇳🇿 New Zealand (NZ) | 2 | 0 | 0.0 Mbps | `` |
| 🇵🇦 Panama (PA) | 2 | 0 | 0.0 Mbps | `` |
| 🇵🇭 Philippines (PH) | 2 | 0 | 0.0 Mbps | `` |
| 🇹🇼 Taiwan (TW) | 2 | 1 | 0.9 Mbps | `vpn503500791` |
| 🇨🇭 Switzerland (CH) | 1 | 1 | 17.0 Mbps | `vpn783506990` |
| 🇩🇪 Germany (DE) | 1 | 0 | 0.0 Mbps | `` |
| 🇫🇷 France (FR) | 1 | 0 | 0.0 Mbps | `` |
| 🇬🇩 Grenada (GD) | 1 | 1 | 7.4 Mbps | `diamondgnd` |
| 🇮🇹 Italy (IT) | 1 | 0 | 0.0 Mbps | `` |
| 🇯🇴 Jordan (JO) | 1 | 0 | 0.0 Mbps | `` |
| 🇳🇱 Netherlands (NL) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇸 Palestinian Territory Occupied (PS) | 1 | 0 | 0.0 Mbps | `` |
| 🇵🇹 Portugal (PT) | 1 | 0 | 0.0 Mbps | `` |
| 🇷🇴 Romania (RO) | 1 | 0 | 0.0 Mbps | `` |

## 🕵️ Claim vs. reality

The VPN Gate `Speed` field is whatever the server *claims*. Here is the truth, measured through a live tunnel — the hall of shame (claimed ≫ delivered):

| Server | Country | Claims | Delivers | Reality ratio |
|---|---|---:|---:|---:|
| `vpn981288372` | 🇯🇵 JP | 237 Mbps | 0.1 Mbps | 0% |
| `vpn301434747` | 🇺🇸 US | 139 Mbps | 0.1 Mbps | 0% |
| `vpn107502003` | 🇯🇵 JP | 812 Mbps | 1.2 Mbps | 0% |
| `public-vpn-37` | 🇯🇵 JP | 1,394 Mbps | 2.2 Mbps | 0% |
| `vpn949825988` | 🇯🇵 JP | 260 Mbps | 0.5 Mbps | 0% |
| `vpn392875556` | 🇷🇺 RU | 165 Mbps | 0.3 Mbps | 0% |
| `vpn750706241` | 🇯🇵 JP | 332 Mbps | 1.0 Mbps | 0% |
| `vpn667739311` | 🇯🇵 JP | 112 Mbps | 0.3 Mbps | 0% |
| `vpn379858910` | 🇯🇵 JP | 365 Mbps | 1.1 Mbps | 0% |
| `vpn618946778` | 🇦🇺 AU | 493 Mbps | 1.7 Mbps | 0% |

Most honest of this round: `vpn491348575` (39 Mbps), `vpn244093263` (18 Mbps), `vpn799057875` (16 Mbps), `vpn151821463` (20 Mbps), `vpn890053288` (10 Mbps).

## 🧭 Exit-country mismatches

. ✅ Every verified server exits where it claims.

## 📈 History

Alive % trend (last 33 runs): `██▇▆▆▁▄▅▄▃▄█▄▄▄▄▄▄▃▃▃▃▃▂▃▂▂▂▂▁▂▂▂`

Avg measured speed (Mbps): `▄▅▁▅▁▆▅▄▁▃▁▄▃▄▄▅▅██▄▅█▃▇▄▂▅▅▆▅▆█▆`

| Run at | Fetched | Alive | Alive % | Avg ↓ | Max ↓ | Avg ↑ | Mismatches |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-11-25 04:34:32 UTC | 95 | 524 | 34% | 12.8 | 52.4 | 2.2 | 1 |
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
*Auto-generated by [run #23](https://github.com/onlyactions/vpngate-monitor/actions/runs/45755748436) at 2026-11-26 04:43:07 UTC. Next scheduled run: daily 03:23 UTC.*
