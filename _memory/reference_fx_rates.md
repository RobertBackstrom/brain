---
name: fx-rates-for-contract-and-p-l-numbers
description: Fetch EUR/SEK and USD/SEK live and cross-check two sources for any contract or P&L figure; .fx_cache.json can hold a months-old seeded fallback.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 87be6b3b-6ee6-4e0b-88e4-f132dbaa50a8
  modified: 2026-08-16T18:25:51.328Z
---

**For any number that lands in a contract, an invoice, or a P&L cell, fetch the rate live and cross-check two sources.** Do not read it out of `assistant/.fx_cache.json`.

**Why:** the cache is fine for dashboards and rough sizing, but it silently persists stale values. On 2026-08-16 it held an EUR rate fetched **2026-06-17**, two months old, tagged `"EURSEK=X (seeded, Yahoo 429 fallback)"` — a hardcoded seed written when Yahoo rate-limited, not a real quote. It read 11.05 against a live 11.00. Small here, but it is a *silent* wrongness with no staleness check and no error, and it was only caught because the number was going into a subcontractor cost.

**How to apply:**

```bash
curl -sL "https://api.frankfurter.dev/v1/latest?base=EUR&symbols=SEK"
curl -sL "https://open.er-api.com/v6/latest/EUR"     # cross-check
```

Note `api.frankfurter.app` 301-redirects, so use `api.frankfurter.dev` or pass `curl -L`. Two sources agreeing to within ~0.2% is the confirmation; if they diverge more than that, something is wrong with one of them and neither should be used unexamined.

**State the rate and its date in the deliverable.** k2c precedent: the April 2026 contract set held EUR/SEK **11.40**, `_budget_breakdown.md` records that assumption explicitly, and the 2026-08-15 fourth-artist booking recorded **11.00** in the P&L row label itself. Anyone re-reading the sheet can then tell a rate change from an error. See [[project_k2c_sands_of_duat]] and [[feedback_verify_live_sheet_vs_memo]].

**Rule of thumb:** an FX assumption that is not written down next to the number it produced is an untraceable number.
