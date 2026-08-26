---
name: feedback_drive_links_clickable
description: "Always present Drive/Gdoc references to Robert as full clickable https URLs, never bare file IDs"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 27e17108-1de2-481a-86b8-921da6f8626d
---

When reporting any Google Drive / Google Doc / Sheet / Slides / folder back to Robert, give the **full clickable `https://` URL** (markdown link), never a bare file ID. He reads agent output in the VS Code extension window, which only linkifies real URLs — a raw ID like `13Y0Moz…` is dead text he can't open.

Canonical forms: Doc `https://docs.google.com/document/d/<id>/edit`, Sheet `…/spreadsheets/d/<id>/edit`, Slides `…/presentation/d/<id>/edit`, generic file `https://drive.google.com/file/d/<id>/view`, folder `https://drive.google.com/drive/folders/<id>`. `gdrive-upload.js` prints the link on upload — relay it.

**Why:** bare IDs aren't clickable in the VS Code window; Robert had to hand-build URLs to open the K2C v3 contracts.
**How to apply:** keep bare IDs only in internal artifacts (trackers, memos, code); in any message/report to Robert, use the URL. See [[document_generation]].
