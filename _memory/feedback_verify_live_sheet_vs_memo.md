---
name: Re-verify live sheet state before executing a planned cell push from a memo
description: Hand-off memos that say "push cell X to value Y" can be obsolete by the time you action them. Always read live state first and reconcile.
type: feedback
originSessionId: 8e82d357-bdc6-452a-83df-239e573ffb25
---
When a hand-off memo (or prior session's plan doc) says "push cell X to value Y via gsheets_update_cell", do NOT execute blindly. Read the live sheet state first and reconcile.

**Why:** 2026-05-18 K2C P&L push. The May-6 handoff said "push K2C P&L row 14 cells + AP P&L M7 = 39,626 (Dec)". By 2026-05-18 the live K2C P&L had already been updated (Lost Hive tightened from 337,500 forward-looking to 270,000 signed-contract → K2C profit 1,019,626 → 1,093,876, +74,250) and the AP P&L row 7 had been restructured from quarterly batches (Jul/Oct/Dec) to monthly K2C-IC values that auto-track the K2C P&L. Executing the memo's push would have OVERWRITTEN the more current state with stale numbers — exactly the opposite of the intent.

**How to apply:**
- Before any `gsheets_update_cell` push driven by a prior memo, read the target cell + the upstream input cells + downstream formulas (or eyeball the totals row) and compare to the memo's expected state.
- If live = memo: push as planned.
- If live ≠ memo because live is MORE current (newer numbers, more accurate scope): the memo is obsolete. Do not push. Update the memo / activity log with the new live state. Tell Robert what you found.
- If live ≠ memo because live is wrong (someone fat-fingered, or a CSV-replace flattened formulas): push the corrected value, but call out the divergence and what you think caused it.
- Same principle applies to "the local CSV is the source of truth, push to live" patterns — verify both before touching cells.
- Generalises beyond sheets: tracker rows, ticket statuses, registry entries. Any state field a memo claims should be X — verify against current reality before mutating.
