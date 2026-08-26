---
name: keep-oauth-credentials-in-sync-across-all-dependents
description: "When updating Google OAuth credentials, find and update ALL files/configs that reference the same client_id; and after any Google password change, re-run the oauth-helper exchange for every scope key."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87be6b3b-6ee6-4e0b-88e4-f132dbaa50a8
  modified: 2026-08-15T16:33:06.656Z
---

## A Google password change revokes every OAuth grant, silently (2026-08-15)

Confirmed live: a password reset on the Google account killed the work Gmail refresh
token (`~/.claude/.gmail-archive-credentials.json`). Refresh returned
`invalid_grant: Token has been expired or revoked`. The mailbox was blind for **28
hours across 343 logged failures** before anyone noticed, because nothing alerts on it.

**How to apply:** after any Google password change, re-run the two-step exchange for
**every** affected scope key, not just the one you happened to notice:

```
node assistant/oauth-helper.js url <scope-key>
node assistant/oauth-helper.js exchange <scope-key> "<callback-url>"
```

Scope keys: `gmail`, `gmail-personal`, `gdrive`, `gdrive-personal`, `calendar`.

**Diagnosing which grants died:** test each refresh token directly rather than
guessing. Grants can survive selectively (in the 08-15 case personal Gmail and GDrive
both still refreshed fine while work Gmail was dead), so "one thing works" is not
evidence the others do. `journalctl --user -u deathboard | grep "expired or revoked"`
gives the exact break time and the blast radius.

**What goes dark when work Gmail dies:** the 15-minute `checkEmails`/`checkSentEmails`
scan, `[Events] HTMAG`, the 06:30 inbox sweep, **Gemini meeting-notes ingestion** (so
the PM daily routine loses its standup source), the RAG `gmail` index, and
`gmail-draft.js`. Backfill after re-auth with `post-meeting-sweep.js` and
`rag-external-indexer.js --gmail`.

---

## Client_id sync

When updating OAuth or credential files, always search the full codebase for all dependents using the same client_id/secret before finishing.

**Why:** Multiple scripts and configs share the same Google OAuth client (`446018956587`). If one gets updated and others don't, auth silently breaks in those other tools.

**How to apply:** Before updating any OAuth credential, run `grep -r` for the client_id across the project. Update every hit. Known locations for the Google Drive/Workspace OAuth:
- `~/.claude/gcp-oauth.keys.json` (used by `assistant/gdrive-upload.js`)
- `~/.claude/.gdrive-server-credentials.json` (stored token, delete to force re-auth)
- `.mcp.json` (gdrive MCP server env vars)
- `assistant/scan-reports.js` (hardcoded)
- `assistant/config.json` (client_id reference)
- `skills/followup_system.md` (env var export example)
