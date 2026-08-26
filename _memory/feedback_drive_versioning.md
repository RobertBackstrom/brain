---
name: feedback_drive_versioning
description: One current version per Drive folder; move previous versions to an _archive folder. Applies to every agent working with Drive docs.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 27e17108-1de2-481a-86b8-921da6f8626d
---

Standing housekeeping rule for Drive docs (Robert 2026-05-29, applies everywhere and to every agent): **keep only one current version of a document in a folder.** When you supersede/re-upload a doc, move the previous version into an **`_archive`** subfolder in the same pass so the working folder shows only the current version.

Sharing of `_archive`: default Robert-only, but inherited team/board access is acceptable when the folder already carries it and Robert is fine with it — he confirmed **AP-board access is fine** for the K2C legals folder. Strip only *extra* direct shares beyond what the folder grants.

**Shared-Drive caveat:** you cannot make a child more private than its parent; an `_archive` under a board-shared Shared Drive folder inherits that sharing and inherited permissions can't be deleted (403). If true privacy is ever required, the archive must live outside the shared tree. Full detail + the permission-checking commands in [[drive_versioning]].

**Why:** avoids multiple versions of the same contract sitting side by side in the legals folder (confusing for signatories/reviewers).
