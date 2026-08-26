# Index Agent — Cross-Project Learnings

Learnings accumulated across projects. Read this file when activating the Index agent.

---

## 2026-06-10 — Complete Drive folder registry build (60+ folder IDs mapped across all drives)

**Learned:** Built comprehensive Drive folder ID registry at `reference_drive_folders.md` mapping every key folder to its ID for instant RAG lookup. Discovered 7 Shared Drives (projects, CZP, legals, Runatyr, Aurora Punks ×3 variants), mapped complete _financials/_legals/_deliverables hierarchies for all major client projects (BADASS, Elias, K2C, Striden), identified corporate folders (AP Bokslut 2025 at `1TmSqmdwPY115LXwlFHNDyCniQkEzxGCh`).

**Key findings:**
1. **Migration incomplete:** Some legacy projects (water_me_and_you, sir_whoopass) still in My Drive, not yet moved to projects Shared Drive consolidation
2. **Standard structure consistent:** All projects in projects Shared Drive follow _financials/_legals/_deliverables with _working/_archive subfolders
3. **Discovery methodology:** Use `gdrive_search` to enumerate folders by name, cross-reference known documents (e.g., AP Bokslut 2025 doc) to verify correct parent folders, map parent-child relationships via file metadata

**Why:** Eliminates "where do I upload this?" search loops - agents can now look up exact folder ID from registry on first try

**How to apply:** When agents need to upload files, consult `reference_drive_folders.md` Quick Reference table or full hierarchy for exact folder ID. When new shared folders are created (accounting handovers, client deliverables, etc), append folder ID + sharing info to registry per maintenance protocol.

**Source:** gen-248 (APDS förvaltarberättelse), triggered by AP bank statement upload question
**Tags:** drive-folder-registry, gdrive, folder-mapping, index, rag, reference-memory, gen-248

## 2026-06-22 — Shared-Drive *root* IDs don't resolve via `'<id>' in parents` in gdrive_search
**Learned:** 2026-06-22 | **Project:** Aurora Punks (deck audit) | **Category:** gdrive, gdrive_search, shared-drive, query-syntax, gotcha

**Symptom:** Querying `'0ACOk67Zhg9zlUk9PVA' in parents and mimeType = '...'` against a Shared-Drive **root** ID (the `0A…` prefixed IDs) returned 0 files, even though the drive has plenty of content. Tried it on two AP Shared-Drive roots Robert linked — both 0.

**Why:** A Shared-Drive root is not addressable as a normal `parents` folder. Root-level enumeration needs `corpora=drive` + `driveId=<id>` (which this MCP's `gdrive_search` does not expose), not a `parents` filter.

**How to apply:** To find files in a Shared Drive, either (a) search by **name/mimeType** — `gdrive_search` already spans all drives, so a plain `mimeType = 'application/vnd.google-apps.presentation'` or name match works and returns the deck regardless of which drive it's in — or (b) target a real **subfolder** ID, not the `0A…` root. Don't waste a call on `'<0A-root>' in parents`; it silently returns nothing.

**Tags:** gdrive, gdrive_search, shared-drive-root, in-parents, corpora-driveId, query-gotcha, index, aurora-punks
