# Output Log — Personal Listings

Significant deliveries: scaffolding, listings published, sales completed, calibration changes. Newest first.

## 2026-04-30

### Tradera plan rewrite after discovering tradera/ai-marketplace plugin
- **What:** Rewrote the Tradera approach across mkt-002, mkt-005, secrets_registry, and lister.md after Robert surfaced the official Tradera Claude Code plugin at https://github.com/tradera/ai-marketplace.
- **Details:**
  - **Plugin reality**: slash-command/skill plugin (mcp.json is empty); skills internally `curl https://api.tradera.com/v4/...`. Lister reuses the curl recipes in Node code at runtime, no slash-command dependency in cron.
  - **API is open-registration** at api.tradera.com/register — no partner-application gate. Original mkt-002 framing (apply for partner API + wait weeks) was wrong.
  - **5 env vars** replace the old 3: `TRADERA_APP_ID` (int), `TRADERA_APP_KEY` (GUID), `TRADERA_PUBLIC_KEY` (GUID), `TRADERA_USER_ID` (int), `TRADERA_USER_TOKEN` (GUID). secrets_registry updated.
  - **Sold-listings gap**: Tradera v4 has search (`/v4/search`, `/v4/search/advanced`) but **no sold-listings filter** per llms-full.txt review. MVP comp pricing collapsed to **eBay sold-listings only**, with `tradera_regional_factor` (default 0.85) per category for Tradera asking-price. Tradera-native comps deferred to mkt-007 (icebox until MVP volume warrants).
  - **Sale events**: Tradera doesn't offer inbound HMAC webhooks. They have a Push API via AWS SQS (`OrderCreated`, `ItemClosed`). mkt-005 rewritten — Tradera path = SQS consumer (`assistant/lister-tradera-sqs-consumer.js`, systemd user service); eBay path unchanged. Added `aws.sqs-tradera-events` secret entry.
  - **Rate limit confirmed**: 100 calls / 24 h baseline. mkt-002 includes an email-to-apiadmin@tradera.com step bundling rate-limit raise + Push API onboarding.
  - **Files touched**: [mkt-002](../assistant/followups/mkt-002-tradera-api-application-and-playwright-fallback.md), [mkt-005](../assistant/followups/mkt-005-ebay-tradera-sale-webhook-receivers.md), [mkt-007](../assistant/followups/mkt-007-tradera-native-comp-engine-deferred.md) (new — icebox), [agents/lister.md](../agents/lister.md), [secrets_registry.md](../secrets_registry.md).
- **Why:** The plugin existed before our scaffold (Tradera repo last pushed 2026-04-16). Building on top of the official plugin is cleaner than partner-API + Playwright; finding it before code-side MVP work begins is exactly the right time. Net effect: smaller surface area, no Playwright path for MVP, +1 deferred ticket (mkt-007), -1 secrets entry (`tradera.session-cookies` removed).

### Scaffolded Lister agent + personal_listings project
- **What:** Created the Lister agent (Robert's first personal-economy agent), seeded its learnings file, and scaffolded `personal_listings/` with CLAUDE.md, output_log, inventory.csv, category_thresholds.yml, listing templates, and folder skeleton (drafts/, watched-photos/, sold/, cache/).
- **Details:**
  - [agents/lister.md](../agents/lister.md) — agent definition (tools, rules, workflows, critical-vs-mundane matrix)
  - [agents/memory/lister_learnings.md](../agents/memory/lister_learnings.md) — seeded with categories for Pricing & Comps, Marketplace Quirks, Photo Intake, Threshold Calibration, Voice & Copy, Critical-vs-Mundane Calls, plus placeholders for Steps 2–4
  - [agents/_registry.md](../agents/_registry.md) — added Lister row
  - [personal_listings/category_thresholds.yml](category_thresholds.yml) — seeded with conservative defaults for common categories (PC parts, electronics, board games, books)
  - Plan file at `~/.claude/plans/the-assistant-lets-sleepy-spindle.md`
- **Why:** Robert wants to automate Tradera + eBay listings (Step 1 of a 4-phase plan: publish ads → Pokemon TCG eval → eBay arbitrage → pewter miniatures). MVP = Step 1 only with auto-publish under per-category threshold. Steps 2–4 plug in later via pluggable intake/comp engine seams.

| Date | What | Where | Outcome |
|------|------|-------|---------|
| 2026-04-30 | Scaffold Lister agent + personal_listings/ project folder | agents/lister.md, agents/memory/lister_learnings.md, agents/_registry.md, personal_listings/* | Scaffold complete; awaiting DevOps prerequisite tickets (mkt-001..006) |
| 2026-04-30 | Tradera plan rewrite after plugin discovery | mkt-002, mkt-005, mkt-007 (new), agents/lister.md, secrets_registry.md | Open-API path replaces partner-API; eBay-only comps for MVP; SQS replaces webhook; mkt-007 ices Tradera-native comps |
