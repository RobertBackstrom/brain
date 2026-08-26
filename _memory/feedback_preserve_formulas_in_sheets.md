---
name: Preserve formulas in Sheets/Excel — never bulk-replace
description: Never overwrite a Google Sheet or Excel file via CSV-replace / file upload when it contains formulas. Always update cell-by-cell on input cells only. Applies to all agents.
type: feedback
originSessionId: e65977b1-d850-4955-9969-fd388ceb24ea
---
# Preserve formulas — never bulk-replace a live Sheet

When working in a Google Sheet or Excel file that contains formulas (SUM, cross-cell references, conditional logic, lookups, ARRAYFORMULA, etc.), you MUST update cell-by-cell on the **input cells only**. Never:

- Replace the file via Drive API media upload (e.g. `assistant/gdrive-replace-sheet.js` with a CSV)
- Overwrite the whole tab via `values.update` covering the full range
- Re-upload an XLSX over an existing Sheet
- Use `gdrive-upload.js --convert` to replace an existing native Sheet

All of these collapse formulas into static values. The formulas are gone, downstream cells stop reflecting upstream changes, and any human collaborator editing the Sheet thinks "I'll just change this input number" — which now does nothing because the totals are hard-coded.

## How to update a Sheet that has formulas

1. **Detect formulas first.** Read with `valueRenderOption=FORMULA` (Sheets API) or open the Sheet and inspect Total/Subtotal/computed-looking cells. If any cell starts with `=`, treat the whole Sheet as formula-bearing.
2. **Identify the input cells** — typically the leaf data rows (raw revenue/cost line items, monthly inputs). Totals, subtotals, accrued/cumulative rows, and the TOTAL column on the right are usually formulas, not inputs.
3. **Update input cells only**, one at a time, via `gsheets_update_cell` or batched `values.update` on a *narrow* range that excludes formula cells. The formulas recompute automatically.
4. **For row-structure changes** (adding a new line, e.g. "K2C intercompany transfer from CZP"): insert a row, copy the formula pattern from an adjacent row into the new row's TOTAL cell, then fill input cells.
5. **Verify after writing**: read with `valueRenderOption=FORMULA` and confirm formulas are still strings starting with `=`. If they read as numbers, you flattened them.

## Recovery if you already flattened it

- For Google Sheets: Drive keeps a 30-day revision history. Restore via UI (`File > Version history > See version history > Restore this version`) is the fastest recovery path. The Drive API does not expose native Sheets revisions for direct read, so a human restore through the UI is usually required.
- For Excel: depends on whether the file is in OneDrive/SharePoint (version history) or local (no recovery).

**Why:** Robert's P&L sheets, time-tracking sheets, and financial models are formula-heavy by design — the totals and accrued rows are derived, not entered. Replacing them with static values silently breaks the model and corrupts every downstream consumer (board members editing inputs, scheduled agents reading totals, manual recalculations).

**How to apply:** Before any write to a Sheet/Excel file that has been hand-built or maintained by a human, ASSUME it contains formulas. Read with formula rendering, identify input cells, and update only those. Bulk-replace is acceptable ONLY when the file was generated end-to-end by an agent run, never touched by a human, AND has no formulas. When in doubt, ask — or do per-cell.
