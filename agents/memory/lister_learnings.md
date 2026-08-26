---
name: Lister Agent Learnings
description: Cross-project knowledge accumulated by the Lister agent — comps, marketplace quirks, photo intake gotchas, threshold calibration, voice/copy patterns
type: agent_memory
agent: lister
---

# Lister Agent Learnings

Personal-economy agent. Append to the right section after each completed task with `[<source>, <YYYY-MM-DD>, <tag>]`. Source = `Step 1 (publish ads)`, `Step 2 (TCG)`, `Step 3 (arbitrage)`, `Step 4 (miniatures)`, or a specific category. Tag = `comp`, `marketplace`, `photo`, `threshold`, `voice`, `process`, `feedback`.

## Pricing & Comps

_How comp lookups behave per category, time windows, currency/VAT handling, condition factor calibration._

(empty — populate as Step 1 ships and runs through real items)

## Marketplace Quirks

_Tradera and eBay specifics: category-tree gotchas, condition-code rules, image size/order rules, title length limits, fee structures, swedish-vs-english title conventions, shipping-rule pitfalls._

- **Tradera v4 REST API is open-registration** at api.tradera.com/register — no partner-application gate (assumption to the contrary will waste planning time). [Step 1, 2026-04-30, tooling]
- **Tradera ships an official Claude Code plugin** at https://github.com/tradera/ai-marketplace (`claude plugin install tradera-api@tradera-ai-marketplace`). It's slash-command/skill-based, not MCP (`mcp.json` is empty). Skills internally `curl https://api.tradera.com/v4/...` with X-App-Id / X-App-Key / X-User-Id / X-User-Token headers — reuse the curl recipes from SKILL.md files in Lister Node code at runtime, no slash-command dependency. [Step 1, 2026-04-30, tooling]
- **Tradera v4 has NO sold-listings filter** per llms-full.txt (search endpoints exist but don't expose ended-vs-active state). Tradera-native comps require either a Playwright scraper of "Avslutade auktioner" (mkt-007, deferred) or wait for upstream API to add it. For MVP, drive comps from eBay sold-listings × `tradera_regional_factor`. [Step 1, 2026-04-30, comp]
- **Tradera Push API uses AWS SQS, not inbound webhooks.** `OrderCreated` + `ItemClosed` events delivered to a queue we provision; consumer long-polls. Onboarding: email apiadmin@tradera.com with the queue ARN. Bundle this with the rate-limit raise email. [Step 1, 2026-04-30, marketplace]
- **Tradera v4 rate limit is 100 calls / 24 h baseline.** Email apiadmin@tradera.com to raise — cite the use case. Per-item cost: 1 publish + 1 end-listing on sale = ~2 calls. 50 items/day caps the baseline. Caching get-item (we already have local IDs from publish) saves zero calls — caching is for downstream item-detail re-checks only. [Step 1, 2026-04-30, marketplace]

## Photo Intake

_What shots are mandatory per category, lighting/angle issues, when to ask Robert for re-shoots, how vision misclassifies similar items._

(empty)

## Threshold Calibration

_When the auto-publish threshold misfired (too low → friction, too high → embarrassing publish). Per-category lessons → updates to `category_thresholds.yml`._

(empty)

## Voice & Copy

_Listing copy patterns Robert approved or rejected. Swedish-vs-English nuance per category. Title patterns that converted well._

(empty)

## Critical-vs-Mundane Calls

_Log of every borderline decision: did we auto-publish or ticket? What was the outcome? Use to refine the matrix in `lister.md`._

(empty)

## Step 2 — Pokemon TCG (placeholder)

_Card identification, set codes, grading impact on price, PSA/BGS, mandatory_review flagged for graded cards._

(empty)

## Step 3 — eBay Arbitrage (placeholder)

_Trending signals, "good value" definitions per category, margin floor after fees+shipping, candidate→bought→received→listed flow gotchas._

(empty)

## Step 4 — Miniatures (placeholder)

_Multi-item-per-photo intake, faction/sculpt identification, painted-vs-stripped pricing, OOP rarity premium, breakdown vs bundle decisions._

(empty)
