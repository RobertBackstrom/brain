---
name: gdrive MCP auth + fork
description: How the gdrive MCP authenticates and why we run a local fork (Shared Drive support). Replaces the earlier "service account" note — that was incorrect.
type: reference
originSessionId: 807db031-95b3-4c3b-96f0-944ab455d70c
updated: 2026-04-20
---

## Auth model — Robert's personal OAuth

The `mcp__gdrive__*` tools authenticate as **robert@aurorapunks.com** via OAuth, not a service account.

- OAuth client: `446018956587-phujr539bjihq7ikth78i5gjqfvi9a0u.apps.googleusercontent.com` (project `gws-oauth`, same as gws/gmail-archive)
- Credentials: `/home/assistant/.claude/.gdrive-server-credentials.json` (refresh token auto-rotates)
- Keys file: `/home/assistant/.claude/gcp-oauth.keys.json`
- Scopes: `auth/drive` + `auth/spreadsheets` (full)
- That means: **the MCP can see anything Robert can see** — personal Drive, any Shared Drive he's a member of, anything shared to him 1:1. No per-file sharing required.

If Robert can open a file in browser.google.com/drive → MCP can read it. Full stop.

## The fork

**Upstream `@isaacphi/mcp-gdrive@0.2.0`** has a bug: `files.get`, `files.export`, and `files.list` calls omit `supportsAllDrives: true` / `includeItemsFromAllDrives: true` / `corpora: 'allDrives'`. This causes silent 404s on **every file that lives inside a Shared Drive** (anything with a `driveId`) and makes search return only personal-Drive results.

We run a local patched fork at:

- `/home/assistant/projects/assistant/mcp-gdrive-fork/`
- Entry point: `dist/index.js` — registered in `~/.claude.json` as `mcpServers.gdrive`
- Version tag: `0.3.0-runatyr-1`
- Fix: every `drive.files.*` call gets `supportsAllDrives: true`; `files.list` also gets `includeItemsFromAllDrives: true` and `corpora: 'allDrives'`
- Bonus: `gdrive_search` now accepts raw Drive query strings (passes through verbatim if the query contains `contains`/`=`/`and`/`or`). Previously you were locked into "name contains X" only.

## If auth breaks

- Symptom: every call returns auth errors
- Fix: `gws auth logout && gws auth login` is a different OAuth client; use the standalone flow:
  ```
  node /home/assistant/.npm/_npx/085f14926c9c96cf/node_modules/@isaacphi/mcp-gdrive/dist/index.js
  ```
  will re-launch the browser consent flow and rewrite `.gdrive-server-credentials.json`. (The fork shares the same creds file.)

## Smoke test

- Script: `/home/assistant/projects/assistant/cron/gdrive-mcp-smoke.sh`
- Runs: `/home/assistant/projects/assistant/mcp-gdrive-fork/smoke-test.mjs` against 5 canary docs (CZP Shared Drive .docx, Brink PDF in personal Drive, AP Shared Drive Gdoc, CZP Shared Drive Gdoc, AP Admin Shared Drive PDF)
- Cron: `0 6 * * *` daily at 06:00 UTC
- Pass log: `assistant/logs/gdrive-mcp-smoke.log`
- Fail alert: `assistant/logs/gdrive-mcp-alert.log` (single-line entry per failure)

## Upstream tracking

isaacphi/mcp-gdrive PR-worthy. If upstream merges the fix we can delete the fork and go back to `npx -y @isaacphi/mcp-gdrive`. Until then, the fork is the supported path and `~/.claude.json` must point at it.
