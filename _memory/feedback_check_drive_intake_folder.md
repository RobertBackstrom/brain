---
name: feedback_check_drive_intake_folder
description: "Robert's phone-upload Drive intake folder (Kvitton_Inbox) is the drop point for ALL uploaded documents, not just receipts - every agent should check here when a file is \"uploaded\"."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a461e6fe-0862-4c43-ae3c-9ba21e6f8caa
  modified: 2026-07-27T14:42:06.744Z
---

When Robert says he "uploaded" a document (a passport, a scan, any file) and doesn't give a path,
check the Drive intake folder **first**: `Kvitton_Inbox` = folder id
`1xPRfNjgz9wQHEkdxWzpOwlREn4LJFYbJ` in his My Drive
(https://drive.google.com/drive/folders/1xPRfNjgz9wQHEkdxWzpOwlREn4LJFYbJ). Scanned files land
there named like `Skannad {27 juli 2026 16:24:36}.pdf`. Robert stated (2026-07-27) it is
important that **the Assistant and every agent** check here for uploaded documents - treat it as
the default upload inbox, above Downloads/Desktop/`assistant/uploads`.

**Why:** it started as the kvitto-intake pipeline ([[project_receipt_intake]], db-279) but Robert
now uses it as the general document dropbox. Agents that only look in local upload dirs miss files
he actually put in Drive.

**How to apply:** search it with `gdrive_search("'1xPRfNjgz9wQHEkdxWzpOwlREn4LJFYbJ' in parents")`.
It syncs into RAG automatically via `assistant/rag-external-indexer.js --gdrive` (My Drive changes
feed), so uploaded docs also become searchable by filename shortly after upload. To rename/move a
Drive file (no MCP write tool exists) use `drive-lib.js` `api('PATCH', .../files/<id>?..., {name})`
or `moveOne()`.

**Caveat / open wiring (DevOps, in progress 2026-07-27):** the **receipt-router auto-classifies
files dropped in the ROOT** of this folder and sweeps non-receipts to `_needs_review/` with a
Discord ping. A non-receipt (e.g. a passport) left in the root can get grabbed by that classifier.
Robert has asked DevOps to extend the wiring so general documents are handled, not just receipts -
until that lands, be aware a document in the root may be moved by the receipt pipeline. Related:
[[feedback_check_downloads_desktop_first]].
