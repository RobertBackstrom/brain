---
name: GCP OAuth project (gws-oauth-aurora)
description: Shared Google Cloud project hosting the OAuth client used by gmail/gdrive/calendar helpers on the VPS
type: reference
originSessionId: 887b0c3c-8fec-4f3d-952a-4856f0d91cf8
---
- Project ID: **446018956587** (name: gws-oauth-aurora)
- OAuth client lives here; same `client_id` is reused across scope profiles in `assistant/oauth-helper.js` (gmail, gdrive, calendar, ...)
- Enabled APIs (confirmed 2026-04-23): Gmail, Drive, Sheets, Calendar
- Billing: active (began 2026-04-10)
- When adding a new scope profile that touches a new Google API, the API must be enabled in the console: `https://console.developers.google.com/apis/api/<api-name>.googleapis.com/overview?project=446018956587`
- Credentials keys file: `~/.claude/gcp-oauth.keys.json` (loaded by oauth-helper.js)
