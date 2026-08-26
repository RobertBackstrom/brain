# Console Backend MCPs / APIs — Landscape Memo

**Date:** 2026-04-20
**Scope:** Partner/dev portals, store/commerce, consumer live services, and unofficial tooling across PlayStation, Xbox, Nintendo.
**TL;DR:** No one has built a real MCP for a console partner portal. Plenty of reverse-engineered consumer-API libraries exist (especially Xbox and PlayStation), and those would be quick to wrap. Partner-side automation today is scraping or Domo exports, not APIs.

---

## What exists, by platform

| Platform | Surface | Project | Status | Auth | Covers | License | Link |
|---|---|---|---|---|---|---|---|
| PlayStation | Consumer live | **psnawp** (Python) | Active (v2.1+, last updated Jun 2025) | NPSSO cookie | Users, trophies, friends, games, store queries | MIT | [github](https://github.com/isFakeAccount/psnawp) |
| PlayStation | Consumer live | **psn-api** (JS/TS) | Active | NPSSO cookie | Trophies, users, game data | MIT | [github](https://github.com/achievements-app/psn-api) |
| PlayStation | Consumer live | **mgp25/psn-api** (Python) | Stale | NPSSO cookie | Older/original PSN reverse-engineered lib | — | [github](https://github.com/mgp25/psn-api) |
| PlayStation | Loyalty | **andshrew/PlayStation-Stars** | Reference docs, active | PSN cookie | Undocumented PS Stars endpoints captured from PS App | — | [github](https://github.com/andshrew/PlayStation-Stars) |
| PlayStation | Store | **mrt1m/playstation-store-api** | Stale | None (public) | PS Store product lookup wrapper | MIT | [github](https://github.com/mrt1m/playstation-store-api) |
| PlayStation | Store | **Apify PS Store scrapers** | Active (hosted) | Apify token | Store listings, prices, promos | Commercial | [apify](https://apify.com/epctex/playstation-store-scraper/api) |
| PlayStation | Partners / sales | **PS Partners Analytics (Domo)** | Official, web/Domo only | Partner login | Official sales/royalty dashboards, no public REST | SIE portal | [analytics.playstation.net](https://analytics.playstation.net/) |
| Xbox | Consumer live | **OpenXBL / xbl.io** | Active (10M req/mo, 2026 copyright) | API key (free 150 req/hr; paid tiers) | Profiles, achievements, friends, presence, clips, Game Pass catalog, clubs | SaaS (hosted) | [xbl.io](https://xbl.io/) |
| Xbox | Community MCP | **dend/halo-infinite-mcp** | Active | Xbox Live auth | Halo Infinite player stats + matches via MCP | MIT | [github](https://github.com/dend/halo-infinite-mcp) |
| Xbox | Dev/GDK tooling | **XblDevAccount.exe, Xbox Manager** | Official, NDA-gated | Partner Center cred | Auth, console automation, sandbox publishing | NDA / MS GDK | [learn.microsoft.com](https://learn.microsoft.com/en-us/gaming/gdk/docs/tools/tools-services/live-dev-account-tool) |
| Xbox | Partner Center | Official API | **Does not exist publicly** | — | Store listings, submissions, sales are Partner Center web only (parts via MS Store submission API for UWP) | — | [Partner Center](https://partner.microsoft.com/dashboard) |
| Nintendo | Consumer live | **nxapi** (samuelthomas2774) | Active (Node CLI + Electron) | NSO session | NSO, Parental Controls, SplatNet 2, NookLink, presence | AGPL-ish | [gitlab](https://gitlab.com/samuelthomas2774/nxapi) |
| Nintendo | Store | **lmmfranco/nintendo-switch-eshop** | Active | None (public) | eShop game + pricing crawler | MIT | [github](https://github.com/lmmfranco/nintendo-switch-eshop) |
| Nintendo | Legacy live | **Pretendo Network (NEX)** | Active, reverse-eng | — | Replacement Nintendo Network for 3DS/WiiU; protocol docs | AGPL | [pretendo.network](https://pretendo.network/) |
| Nintendo | GameCube automation | **u1f992/mcp-gamecube-bridge** | Niche | — | GC input bridging via MCP (hardware/emulator) | — | [github](https://github.com/u1f992/mcp-gamecube-bridge) |
| Nintendo | Dev portal | Official API | **Does not exist publicly** | — | NDP self-publish is web-only; no automation surface | — | [developer.nintendo.com](https://developer.nintendo.com) |

**Cross-platform MCP note:** I checked TensorBlock's awesome-mcp-servers gaming list, wong2's awesome-mcp-servers, Microsoft's official MCP catalog, and FastMCP's directory. The *only* console-related MCPs currently published are the Halo Infinite one, the GameCube bridge, and general "installed games" discovery tools. Nothing targets partner/dev portals or commerce automation for any of the three platforms.

---

## Gaps (no one has built this)

1. **PS Partners / SIE Partners Analytics as an API.** Officially Domo-backed, only web UI + Domo exports. No public REST surface, no community wrapper. Only paths: (a) Domo's own export API if Sony exposes it to you, (b) Playwright scraping of `analytics.playstation.net` (ToS grey area), (c) manual CSV download + ingest.
2. **Xbox Partner Center / Microsoft Store submission automation** beyond the narrow old UWP submission API. Cert, sandbox pushes, marketing metadata, sales reports — all Partner Center web UI.
3. **Nintendo Developer Portal.** The hardest locked. No community tooling. Self-publish workflow is fully manual through the portal.
4. **Any MCP wrapper around psnawp / psn-api / OpenXBL / nxapi.** These libs exist, but nobody has wrapped them as MCP servers yet — even though the path would be short (a day each, maybe).

---

## Recommendation

**Short-term, high-leverage (order of effort, low to high):**

1. **Wrap OpenXBL as a DevOps MCP spike.** Free tier, already a clean REST API, supports exactly the kind of "pull me Xbox consumer-side data" work that's useful for community/content tracking. 4–8 hours of DevOps work.
2. **Wrap psnawp as an MCP.** More delicate because it uses your NPSSO cookie (account-ban risk if abused), but useful for trophy/store data pulls. Rate-limit at the library's built-in 300/15m and scope read-only.
3. **Wrap nxapi as an MCP** only if NSO/Splatoon/Animal Crossing data is ever load-bearing for your projects. Otherwise skip — it's consumer flavor, not publisher data.

**Partner-portal automation (the thing you actually asked about):**

None of this solves the "pull sales reports from PlayStation Partners / Xbox Partner Center / Nintendo NDP" problem that SalesInsights is built around. The honest answer is:

- **Status quo (manual export → GDrive → SalesInsights):** still the only ToS-safe path for all three partner portals.
- **Playwright scrapers** against the partner portals are technically possible for PS and Xbox (Nintendo has aggressive bot detection) but carry real risk: ToS violation, account flagging, and — worst case — revocation of partner status. Not recommended unless you get written OK.
- **Domo export API for PS Partners Analytics** is worth asking your SIE account manager about directly. Domo has scheduled CSV exports; if SIE whitelists programmatic access on your tenant, that's a legitimate automation path.
- **MS Store submission API (`manage.devcenter.microsoft.com`)** exists but is narrowly scoped to app/game submissions, not sales reports. Worth a second look if Xbox cert automation is ever on the table.

**Build-yourself vs. wait:** Don't build a partner-portal scraper. Do build the thin MCP wrappers above for the consumer-side libs if/when you need them. For partner-side, push SIE/MS reps for proper export access before you invest in fragile scraping.

---

## Risk notes

- **NPSSO cookie (PSN):** libraries authenticate with your personal PSN cookie. Using it at scale or for commercial purposes risks account suspension. OK for low-volume research, not production pipelines tied to a partner account.
- **OpenXBL:** SaaS (your data flows through a third party). Free tier is fine for exploration; check their ToS before using for client work.
- **Partner-portal scraping:** each of the three has anti-automation clauses in their dev agreements. Ban risk is real and expensive.
- **Nintendo specifically:** they are famously litigious about any unofficial tooling. Pretendo is tolerated because it targets dead platforms (3DS/WiiU). Don't touch anything that looks like it's automating live NDP access.

---

## Sources

- [psnawp](https://github.com/isFakeAccount/psnawp) · [psn-api JS](https://github.com/achievements-app/psn-api) · [mgp25/psn-api](https://github.com/mgp25/psn-api) · [PSNAWP docs](https://psnawp.readthedocs.io/en/latest/)
- [PlayStation Partners](https://partners.playstation.net/) · [PS Partners Analytics](https://analytics.playstation.net/) · [Domo at SIE writeup](https://diginomica.com/how-domo-powers-partner-analytics-sony-interactive-entertainment) · [PS Stars docs](https://github.com/andshrew/PlayStation-Stars)
- [OpenXBL](https://xbl.io/) · [OpenXBL GitHub](https://github.com/OpenXBL) · [halo-infinite-mcp](https://github.com/dend/halo-infinite-mcp) · [MS Tools & automation APIs](https://learn.microsoft.com/en-us/gaming/gdk/_content/gc/test-automation-publishing/test-automation-publishing-tools/tools-automation-apis/atoc-api-tools-dev-env) · [XblDevAccount](https://learn.microsoft.com/en-us/gaming/gdk/docs/tools/tools-services/live-dev-account-tool)
- [nxapi](https://gitlab.com/samuelthomas2774/nxapi) · [lmmfranco/nintendo-switch-eshop](https://github.com/lmmfranco/nintendo-switch-eshop) · [Pretendo Network](https://pretendo.network/) · [Nintendo Developer Portal](https://developer.nintendo.com) · [mcp-gamecube-bridge](https://github.com/u1f992/mcp-gamecube-bridge)
- [TensorBlock awesome-mcp-servers / gaming](https://github.com/TensorBlock/awesome-mcp-servers/blob/main/docs/gaming.md) · [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) · [Microsoft MCP catalog](https://github.com/microsoft/mcp)
