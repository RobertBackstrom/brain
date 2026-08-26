# Personal Listings — CLAUDE.md

## Engagement
- **Role:** Robert's personal-economy 2nd-hand selling pipeline. NOT client work, NOT billable.
- **DB prefix:** `mkt`
- **Status:** active (MVP = Step 1, scaffolded 2026-04-30)
- **Agent owner:** Lister ([../agents/lister.md](../agents/lister.md))

## Why
Robert wants to automate selling stuff he owns on Tradera + eBay (Step 1), then expand to Pokemon TCG card listing (Step 2), eBay arbitrage (Step 3), and pewter miniatures (Step 4). Goal is minimum manual effort — Lister handles intake, comps, drafts, and threshold-gated publish; Robert handles physical packaging and shipping.

## Time tracking
**Do NOT log to `projects/time_log.csv`.** This is personal income, not billable consultancy.

## Conventions

### File layout
```
personal_listings/
├── CLAUDE.md                    # this file
├── output_log.md                # delivery log (each publish/sale is an entry)
├── inventory.csv                # source of truth for items being sold
├── category_thresholds.yml      # auto-publish ceiling + mandatory_review flags
├── listing_templates/
│   ├── tradera-template.md
│   └── ebay-template.md
├── drafts/<sku>/                # one folder per item: tradera.md, ebay.md, photos/, comp_data.json
├── watched-photos/              # Robert drops new-item photos here (or via GDrive Lister Inbox sync)
│   └── _processed/              # archive after intake; folder named <sku>
├── sold/<yyyy>/<sku>/           # post-sale archive (Swedish bookkeeping = 7 yr; we keep forever)
└── cache/                       # comp lookup cache: ebay_sold_<cat>_<date>.json, tradera_completed_<cat>_<date>.json
```

### SKU format
`yyyymmdd-<3-char-cat>-<seq>` — example: `20260430-pcb-001` (PC build, item 1 today). Categories use 3-letter codes from `category_thresholds.yml`.

### Inventory states (`inventory.csv` `status` column)
`candidate` (Step 3 — proposed buy) → `bought` → `received` → `drafted` → `listed` → `sold` → `archived`. Step 1 items skip directly to `drafted`.

### Acquisition source
`owned` (Step 1 — already in Robert's possession) | `arbitrage_buy` (Step 3) | `tcg_owned` (Step 2) | `mini_owned` (Step 4)

## Threshold logic (the key MVP knob)
`category_thresholds.yml` defines per-category `auto_publish_ceiling_sek` and `mandatory_review` flags. Lister auto-publishes only when:
- `asking_price ≤ auto_publish_ceiling_sek` for the item's category, AND
- the category is not flagged `mandatory_review: true`.

Otherwise, drafts are saved and `mkt-NNN` ticket is opened with `needs_input=true`.

## Voice & copy
Listing copy is **condition-honest and factual**. No hype words. Swedish on Tradera, English on eBay. See [[writing_voice_robert]] but apply with the marketplace voice signature ("Smoke-free home, ships from Sweden").

## Hooks for Steps 2–4 (don't break later)
- **Pluggable intake** — `Source` abstraction: `WatchedPhotos` / `CardScan` / `EbayTrendingScraper` / `MiniatureBox`. Intake separated from publish.
- **Pluggable comp engine** — per-category routing: `EbaySold`, `TraderaCompleted`, later `TCGPlayer`, `Cardmarket`, `eBayLive`, `StarCityGames`, `Trolltrader`.
- **Item-identity layer** — SKU is opaque; `inventory.csv` has reserved fields for `tcg_set_code`, `tcg_card_number`, `mini_faction`, `mini_sculpt_id`.
- **Per-category kill-switches** — `mandatory_review: true` blocks future "auto-buy" (Step 3) or "auto-publish graded card" (Step 2).
- **Pipeline names use "publishers"** not "Tradera+eBay" — drop-in for new marketplaces later.

## Pre-MVP DevOps blockers
Tickets `mkt-001` through `mkt-006` cover the prerequisites (eBay developer app, Tradera API application + Playwright fallback, image hosting at `images.runatyr.games`, GDrive→VPS photo sync, sale webhooks, cron jobs). DevOps owns these before Lister can ship code-side MVP.

## Related
- Agent: [../agents/lister.md](../agents/lister.md), [../agents/memory/lister_learnings.md](../agents/memory/lister_learnings.md)
- Reusable patterns: [[steamworks_scraper]] (Playwright + session-persist), [[gdrive_workflow]] (GDrive Lister Inbox sync), `assistant/server.js` HMAC webhook pattern (sale notifications).
