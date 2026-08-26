---
name: reference_gsheets_tab_enumeration
description: "gdrive gsheets_read can't list tabs — needs exact tab name or numeric gid; gdrive_read_file returns only the first tab."
metadata: 
  node_type: memory
  type: reference
  originSessionId: b02b134f-4308-4af1-ab19-91cf2fa63d67
---

`mcp__gdrive__gsheets_read` cannot enumerate a spreadsheet's tabs. With no `sheetId`/`ranges` it returns only the **first** tab. To read a specific tab you must pass either the numeric `sheetId` (the `gid=` in the sheet URL) or an exact `ranges` value like `["TabName!A1:Z80"]` — a wrong/guessed tab name errors with "Unable to parse range". `mcp__gdrive__gdrive_read_file` on a Sheet also exports only the first tab.

**How to read a non-first tab:** grab the `gid=` from the share URL (that's the `sheetId`), or ask the user to read the tab names off the bottom of the sheet. There's no list-tabs call in the current fork. If this becomes a recurring need, it's a [[feedback_long_term_solutions]] candidate for DevOps (add a list-sheets method to `mcp-gdrive-fork/`).

**Faster path since 2026-07-21: RAG now indexes ALL tabs of every Google Sheet.** So for *reading content* out of a non-first tab, `mcp__rag__rag_search` is usually quicker than fighting `gsheets_read` for a gid - the tab text is already indexed (each tab appears as a `# Sheet: <name>` block). Use `gsheets_read` only when you need live/current cell values or are about to write. See [[reference_rag_content_coverage]].

**The fork fix is known.** The RAG indexer solves this by exporting the Sheet as **.xlsx** (`export?mimeType=...spreadsheetml.sheet`) and reading it with SheetJS, which enumerates every tab by name (`wb.SheetNames`). Same trick would give `mcp-gdrive-fork/` a real list-tabs/read-any-tab method - see `workbookBufferToText()` in `assistant/rag-external-indexer.js`.
