---
name: feedback_signed_files_to_legals
description: "After any eSignature completes, file the executed PDF in the project's _legals folder and move the source GDoc to _legals/_working"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8f7ae57d-a0a2-40f0-a88e-7a3f5c29338e
---

When a document finishes signing (OpenSign — see [[digital-signatures-self-hosted-opensign]]), always do two filing steps, every time, without being asked:

1. **Executed signed PDF → the project's `_legals` folder** (the final current version). Per the CZP project Drive layout in [[feedback_czp_project_structure]], each project has nested `_legals` / `_deliverables` / `_financials`, each with `_working` / `_archive`.
2. **Source GDoc → `_legals/_working`** (it's no longer the live artifact once executed; the signed PDF is).

**Why:** keeps one authoritative executed copy per agreement in `_legals`, with the editable source demoted to working files so nobody edits a doc that's already been signed.
**How to apply:** on signing completion, download the executed PDF from OpenSign's `signedUrl`, upload it to the project `_legals` folder, and move the working GDoc into `_legals/_working`. Report the executed PDF as a clickable Drive URL ([[feedback_drive_links_clickable]]). Standing rule confirmed by Robert 2026-06-05. Pair with [[feedback_proofread_round_before_esignature]] and [[feedback_drive_versioning]].
