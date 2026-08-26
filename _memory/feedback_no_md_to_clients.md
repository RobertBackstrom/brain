---
name: feedback_no_md_to_clients
description: "Never share .md with clients; client deliverables are Google Docs, and additions to an already-shared doc are updated IN PLACE"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8b3ec3d7-c39c-4783-acee-dc15b22d201d
---

Robert cannot share markdown (.md) files with clients. Client-facing deliverables must be Google Docs (or the appropriate native format), never a raw `.md`. He has corrected this more than once ("I have told you before and will tell you again"), so treat it as a hard rule.

When new content extends a document that is **already shared with the client**, do NOT create a new file (a new `.md` or even a new GDoc) - **update the existing shared doc IN PLACE**, keeping the same fileId and shareable link. Robert confirmed in-place update of an already-shared doc is allowed and expected (a new file causes link rot and re-share friction).

**Why:** clients receive Google Docs, not markdown; and a new file breaks the existing share + the link people already have.

**How to apply:**
- Author working content in `.md` locally if convenient, but the client artifact is always the GDoc.
- To add to a shared GDoc, fold the new section into the local source `.md`, then update the live doc in place with `node assistant/gdrive-update-doc.js <local.md> <fileId>` (PATCHes the existing Google Doc from markdown via Drive media update with `supportsAllDrives=true` - same fileId, same link). `md-to-html` handles tables.
- **CAVEAT - `gdrive-update-doc.js` expects MARKDOWN, not HTML.** It runs its input through `md-to-html` first, so feeding it an already-rendered/styled `.html` file (e.g. a UIbot-designed doc) re-processes the HTML as markdown and garbles the live doc. For a **pre-styled HTML** source, push with a **raw `text/html` media PATCH** instead: `PATCH https://www.googleapis.com/upload/drive/v3/files/<fileId>?uploadType=media&supportsAllDrives=true` with `Content-Type: text/html` and the HTML as the body (same OAuth token flow as gdrive-update-doc.js). Near-miss on the Blue Scarab Equinox estimate (2026-06-10): first push used the md tool by mistake; corrected with the raw PATCH. **Always verify any client-doc push by exporting it back** (`/export?mimeType=text/plain`) and confirming 0 literal `<table`/`<th` tags + key figures present.
- Example: BADASS "CUST - Admin User Guide" (fileId `1sgy8vFEgKghS5vTA-skSlPG8DhFDR-_eVglgvpcuKPA`) - the Portfolio Board views section was added here in place rather than as a separate file (2026-05-29).

Related: [[feedback_deliverables_to_project_folder]], [[feedback_deck_format_publish_web]], [[feedback_drive_versioning]].
