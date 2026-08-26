---
name: digital-signatures-self-hosted-opensign
description: Signing runs on self-hosted OpenSign (sign.runatyr.games → sign.aurorapunks.com); DocuSeal is a dormant paid fallback
metadata: 
  node_type: memory
  type: reference
  originSessionId: 745f5972-f904-487b-b194-f39b7cb21d94
---

Digital-signature flows run on a **self-hosted OpenSign** instance on the VPS (open-source, $0). Chosen 2026-06-05 because DocuSeal's free tier has no API and its paid API (~$20/mo) was never taken on, and Google Drive eSignature has no programmatic API. **OpenSign is the ONLY signing tool we use (confirmed 2026-07-06) — do NOT reach for Google Drive eSignature (no API, manual-click only) or DocuSeal (dormant).**

- **Auto-advance watcher (db-251, live 2026-07-06):** `assistant/opensign-watcher.js` + systemd timer (5-min) polls in-flight ordered docs and auto-emails the next signer when the prior one signs (OpenSign pushes no events, so it's a poller not a webhook). Includes a **5-day recurring nudge** to a stuck frontier signer (cap 6 nudges ~30 days), Discord-notifies Robert on nudge/completion, and sends a completion mail with the signed-PDF link. State in `assistant/state/opensign-watcher.json`. A new ordered doc created via `opensign.js` is picked up automatically; no manual chasing needed.

- **Live at:** `sign.runatyr.games` (interim) → flips to `sign.aurorapunks.com` once aurorapunks.com finishes its Wix→Cloudflare migration. Caddy on loopback `127.0.0.1:3782` behind the `deathboard` CF tunnel; org branded "Aurora Punks"; signature emails send from robert@aurorapunks.com via Gmail SMTP (app password).
- **API:** Parse Cloud Functions, session-token auth (`X-Parse-Application-Id: opensign`), NOT a REST `X-API-Token` API. Working send sequence (login → raw Parse file upload [the `savefile` fn is bugged] → `createdocumentfromapp` with Signers/Placeholders → `sendmailv3` with a self-built `/load/recipientSignPdf/...` link) is documented in `agents/memory/devops_learnings.md`. Build/extend the client at `assistant/opensign.js`. Produces standard electronic signatures (SES) — valid for Swedish B2B contracts under eIDAS; no QES needed.
- **Deploy/infra:** `/home/assistant/projects/opensign-app/` (docker-compose, pinned digests), `assistant/OPENSIGN_SELFHOST_SPEC.md`, systemd `opensign-app.service` (ExecStart sg-docker-wrapped), nightly volume backup. Tracked under db-046.
- **DocuSeal (dormant fallback):** `assistant/docuseal.js` + the `/webhook/docuseal` handler stay wired but the API needs a paid subscription (`docuseal.api` deferred — see secrets_registry). Don't reach for DocuSeal unless OpenSign is down and a paid sub has been activated.
