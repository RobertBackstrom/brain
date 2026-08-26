---
name: Personal Listings (Lister project)
description: Robert's personal-economy 2nd-hand selling pipeline — Tradera + eBay automation via the Lister agent. NOT client work, NOT billable.
type: project
originSessionId: c9bb674f-5330-499b-b368-88fc0407c5b8
---
# Personal Listings — Lister project

## Scope
Robert's first **personal-economy** project (every other agent/project is client- or infra-facing). Long-term scope spans 4 phases:

1. **Step 1 — publish ads** to Tradera + eBay (current MVP, scaffolded 2026-04-30)
2. **Step 2 — Pokemon TCG**: scan owned cards, evaluate, list
3. **Step 3 — eBay arbitrage**: scrape trending cards at margin, propose buys
4. **Step 4 — pewter miniatures** (Citadel / GW)

MVP = Step 1 only. Auto-publish under per-category threshold; high-value or flagged categories go to drafts + ticket.

## Conventions
- **DB prefix:** `mkt`
- **Project folder:** `/home/assistant/projects/personal_listings/`
- **Agent owner:** Lister ([agents/lister.md](/home/assistant/projects/agents/lister.md))
- **Time tracking:** does NOT log to `time_log.csv` (personal income, not billable)
- **Threshold knob:** `personal_listings/category_thresholds.yml` (per-category auto-publish ceiling + `mandatory_review` flags)

## Architecture seams (don't break later)
- Pluggable intake: `WatchedPhotos` (Step 1), `CardScan` (Step 2), `EbayTrendingScraper` (Step 3), `MiniatureBox` (Step 4)
- Pluggable comp engine: `EbaySold`, `TraderaCompleted` for MVP; later `TCGPlayer`, `Cardmarket`, `eBayLive`, `StarCityGames`, `Trolltrader`
- Item-identity layer: SKU is opaque; `inventory.csv` reserves `tcg_set_code`, `tcg_card_number`, `mini_faction`, `mini_sculpt_id`
- Pipeline names use "publishers" (not "Tradera+eBay") — drop-in for new marketplaces

## Status
**Scaffolded 2026-04-30** — agent definition, learnings file, registry entry, project folder, threshold config, listing templates all in place. Plan file at `~/.claude/plans/the-assistant-lets-sleepy-spindle.md`.

**Pre-MVP DevOps blockers** (tickets pending Robert's approval to create):
- `mkt-001` — register eBay developer app + production keys (decide region: EBAY_DE recommended for EU shipping)
- `mkt-002` — apply for Tradera partner API + implement Playwright fallback (steamworks_scraper pattern)
- `mkt-003` — image hosting at `images.runatyr.games/listings/<sku>/<n>.jpg` via existing CF tunnel + nginx, signed URLs
- `mkt-004` — GDrive Lister Inbox → VPS `watched-photos/` cron sync
- `mkt-005` — extend `assistant/server.js` with HMAC-protected eBay Notifications + Tradera webhook receivers
- `mkt-006` — VPS user-cron jobs (lister-process-watched-photos 4×/day, lister-relist-stale 1×/day) with single-instance flock

## Next decisions to surface as Step 1 lands
- eBay region (`EBAY_DE` vs `EBAY_US`) — DevOps confirms during eBay app setup
- Initial threshold values per category — start with conservative defaults in `category_thresholds.yml`, refine after first 10 manual listings
- Pricing aggressiveness per category (`sell_factor` 0.85 sell-fast vs 1.05 sell-best)
- Photo drop UX confirmation (GDrive folder vs Telegram bot vs SFTP)

## Adjacent track: TCG Webshop (moved out of the MEMORY.md hook 2026-08-17)
Project folder `projects/tcg_webshop/`.
- **tcg-001** — webshop concept: **parked**.
- **tcg-002** — **Grading Tool, the live track.** iOS app in TestFlight, pre-grade API on `grade.aurorapunks.com`.
