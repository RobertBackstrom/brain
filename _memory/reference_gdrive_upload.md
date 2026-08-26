---
name: Google Drive upload script
description: Node script at assistant/gdrive-upload.js for uploading local files to Google Drive. Use this whenever a file needs to go to Drive instead of asking Robert to do it manually.
type: reference
---

Upload local files to Google Drive using `node assistant/gdrive-upload.js <file> [folder-name-or-id]`.

Supports: pdf, md, txt, html, json, png, jpg, csv, tsv. PPTX also works (Google auto-converts to Slides).

Auth: uses `~/.claude/.gdrive-server-credentials.json` with drive.file scope. Run `--auth` to re-authorize if needed.

**Scope:** Now uses full `drive` scope (not `drive.file`), so it can write to any folder including Shared Drives. Shared Drive support enabled via `supportsAllDrives=true`.

**How to apply:** Whenever creating a deliverable (proposals, reports, presentations, exports) that Robert needs in Drive, upload it directly instead of just saving locally. Robert is a Google Workspace user — files should end up in Drive, not on disk.

**Reading docs:** The GDrive MCP tool uses a service account (service-account@claude-code-mcp-489713.iam.gserviceaccount.com) that has access to the full CZP shared drive. Use the MCP gdrive tools to read Google Docs/Sheets. If the MCP tool returns 404, fall back to the Docs API via the OAuth creds at `~/.claude/.gdrive-server-credentials.json`.
