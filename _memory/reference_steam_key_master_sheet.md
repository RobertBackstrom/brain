---
name: reference_steam_key_master_sheet
description: "Master Steam/console key-tracking Google Sheet — ID, per-game tab convention, and how to add a new game tab"
metadata: 
  node_type: memory
  type: reference
  originSessionId: ec7889a7-b2e4-4238-9fed-9f04f5a3d003
---

The shared key-tracking Google Sheet (Steam + console keys across all AP/Runatyr titles) lives at spreadsheet ID `1WnhzKJhCV65vWbeLc8HezxBRjbrzyrf666wD4dt_WAM`. One tab ("arbetsblad") per game/platform — e.g. Innsmouth, Few Shall Return, SWA, Iron Evil, K2C (added 2026-06-16). Abbreviated tab names are fine (SWA, K2C precedent).

**Canonical per-game layout** (the `Template` tab, faithfully mirrored by `Few Shall Return`):
- `B2` = game title
- `B3:F3` headers = Key / Taken by who/Purpose / Platform/Version / Assigned to / Type of key
- `B4` = "Steam" (platform section header)
- `B5:F5` = legend row = KOD / taken / Steam / Publisher / Beta Key
- `B6` onward = one key per row in col B; col C = who took it (name, blank if unassigned)

**Tooling gotchas:**
- `mcp__gdrive__gsheets_read` with no `ranges` returns ONLY the first tab (Template). To list all tabs or read a specific game, use the Sheets API metadata call (`?fields=sheets(properties(sheetId,title,...))`) or pass explicit `ranges` like `["GameName!A1:G12"]`.
- The MCP has no "create tab" verb. To add a new game tab, call Sheets API `spreadsheets:batchUpdate` with an `addSheet` request, then `values:batchUpdate` (USER_ENTERED) to populate — reuse the OAuth pattern in [assistant/gsheet-set-cell.js](assistant/gsheet-set-cell.js).

Respects [[feedback_preserve_formulas_in_sheets]] — touch named cells only, never CSV-replace.
