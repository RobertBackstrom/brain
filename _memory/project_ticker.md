---
name: project_ticker
description: "Ticker agent — market trends + trade ideas for SE/US gaming & tech equities, plus confirmation-gated execution of a small personal Saxo account"
metadata: 
  node_type: memory
  type: project
  originSessionId: f9dbf1ec-43bd-40b0-a6ae-11f8c0b07531
---

Ticker is a personal (not billable) market-trends agent + small managed trading account, created 2026-06-16.

**What it is:** A ~10K SEK personal risk-capital account Robert delegated to the agent. Robert sets goals ("double in a week", "park defensively"); Ticker researches, forms trade ideas, sizes them, and posts execution decisions. **Every order is gated on Robert's explicit in-channel confirmation** — never autonomous. His own money/account, not third-party financial advice.

**Config locked (2026-06-16):** active trade ideas · coverage = SE gaming + SE tech (broad) + US gaming + US big tech/space · horizon swing/position/long-term, NO intraday · data free-first (Yahoo) then EODHD (~$80/mo) · broker = **Saxo OpenAPI** · execution questions on a **dedicated Death Board lane** separate from daily catch-ups, Robert replies go/no-go + size (Ticker recommends size).

**Built:** agent at [agents/ticker.md], learnings, `/ticker` command, free-data CLI `assistant/ticker-data.js` (Yahoo EOD, no key, curl-based; covers US + Stockholm `.ST`). Project folder `ticker/` (CLAUDE.md, watchlist.json, execution_spec_saxo.md, output_log.md).

**Phase 2 pending (DevOps):** `assistant/saxo.js` (OAuth + order endpoint, SIM first) + dedicated Death Board "Trades" lane + confirm handler. Guardrails in `ticker/execution_spec_saxo.md`: SIM-first, limit-orders-only, per-order/daily caps, allowlist=watchlist, kill switch, full audit trail.

**Trigger lesson:** I claimed "SpaceX has no public stock" — it had IPO'd (SPCX, Nasdaq, 2026-06-12) past my cutoff. Always verify listing/price live before any market claim. See [[project_agent_registry]].
