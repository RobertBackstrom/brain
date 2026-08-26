---
name: Available MCP tools
description: Full inventory of MCP integrations Robert uses — proactively fetch schemas for these at session start
type: reference
originSessionId: a94f4e9e-72f7-447c-beb0-bf4ef8fb3be6
---
## MCP Tools Available

Two stacks live on the box. Don't conflate — see [feedback_vps_operating_environment](feedback_vps_operating_environment.md) for the broader principle.

### Native VPS MCPs (Stack A — `~/.claude/` creds, auto-refresh, run from any session including cron)
- **Gmail (native)** — `mcp__gmail__*` — `gmail_search`, `gmail_read`, `gmail_thread`, `gmail_create_draft`, `gmail_archive`, `gmail_label`, `gmail_list_labels`. Stack-A creds at `~/.claude/.gmail-archive-credentials.json` (gmail.modify scope; covers send too).
- **Google Drive / Sheets** — `mcp__gdrive__*` — local fork at `assistant/mcp-gdrive-fork/` with full Shared Drive support.
- **RAG wiki** — `mcp__rag__*` — `rag_search`, `rag_get_doc`, `rag_list_sources`. Indexes skills/memory/agents/followups/Gmail/GDrive.
- **Atlassian (Jira + Confluence)** — `mcp__atlassian-jira__*`, `mcp__atlassian-confluence__*` — issues/pages/comments/transitions.
- **LinkedIn (read)** — `mcp__linkedin-sd__*` (stickerdaniel) — `get_person_profile`, `get_company_profile`, `get_company_posts`, `search_people`, `search_jobs`, `get_job_details`, `get_inbox`, `get_conversation`, `search_conversations`, `get_sidebar_profiles`, `send_message`, `close_session`. Auth via cookie file at `~/.linkedin-mcp/cookies.json` (db-048). **It is already Patchright/Playwright under the hood** — "let's just use Playwright instead" is a non-fix: both failure modes below live on the auth/IP layer, so any browser driver inherits them identically, and a bespoke script would re-implement cookie import/validation and lose the MCP tool surface. **Two distinct down-signatures — don't conflate:** (1) `ERR_TOO_MANY_REDIRECTS` on auth-strict URLs (DMs, search, non-celebrity profiles; SEO/famous profiles still work) = data-center IP fingerprint block (Hetzner AS24940), structural, no re-export helps — see devops_learnings 2026-04-29 / db-112. (2) `"No valid LinkedIn session"` on `get_my_profile` = **dead cookie** (LinkedIn invalidates server-side; the client-side `expirationDate` is meaningless), fix = `node assistant/linkedin-restore-cookie.js --stdin` with li_at on line 1 + JSESSIONID on line 2 — **without JSESSIONID, write-actions (send_message, connect) fail even after reads recover**. No service restart needed; cookies.json is read on next call. **Probe live, don't read the trace** — `~/.linkedin-mcp/trace-runs/*/server.log` has been 0-byte since 2026-07-15, and `ps aux` showing processes up says nothing about session validity. Cookie rotates ~monthly (db-275 tracks a freshness probe). See devops_learnings 2026-07-16.
- **WhatsApp (native, db-086)** — `mcp__whatsapp__*` — `whatsapp_status`, `whatsapp_list_chats`, `whatsapp_search_chats`, `whatsapp_read_thread`, `whatsapp_send_message`, `whatsapp_get_qr`. Backed by a persistent whatsapp-web.js bridge at `assistant/whatsapp/bridge.js` (systemd user service `whatsapp-bridge.service`, listens 127.0.0.1:4501). LocalAuth pairing in `assistant/whatsapp/.wwebjs_auth/`; bearer token in `~/.claude/.whatsapp-bridge-credentials.json`. Send is critical-task-gated. If session expires, `qr_pending` state surfaces a fresh QR via `qr.txt`/`qr.png` in the bridge dir.
- **Slack (native, db-108 → multi-workspace db-116)** — 7 parallel MCP instances, distinct names: `mcp__slack-aurora__*`, `mcp__slack-rawfury__*`, `mcp__slack-dof__*`, `mcp__slack-upstream__*`, `mcp__slack-overwolf__*`, `mcp__slack-behold__*`, `mcp__slack-bright__*`. Read-only surface per workspace: `channels_list`, `conversations_history`, `conversations_replies`, `conversations_search_messages`, `conversations_unreads`, `conversations_mark`, `users_search`, `usergroups_list`/`_create`/`_update`/`_users_update`/`_me`. Cookie auth (xoxc + xoxd) via `korotovsky/slack-mcp-server` (npm `slack-mcp-server`, prebuilt linux-amd64 binary). Launcher: `assistant/scripts/mcp-slack-launcher.sh <workspace-key>` reads the entry for that key from a JSON array at `~/.claude/.slack-credentials.json`. Token rotation per workspace: `assistant/scripts/slack-cred-set.sh <key> <xoxc> <xoxd> [team_id]`. **Send-message tool intentionally NOT registered** in any of the 7 — upstream binary gates `conversations_add_message` behind `SLACK_MCP_ADD_MESSAGE_TOOL`; the launcher leaves it unset across all workspaces, so it doesn't appear in tools/list at all (stricter than WhatsApp's "review first" comment-gate). To enable posting in one workspace later, edit the launcher and add `export SLACK_MCP_ADD_MESSAGE_TOOL=true` after the cred load — separate ticket, per-workspace approval. **Picking the right workspace:** when scanning for a specific deal/project, use the workspace that the conversation lives in (e.g. K2C/Sands of Duat lives in `slack-rawfury`); when sweeping for unreads across all surfaces, hit `conversations_unreads` on each `slack-<key>__*` server. **Free-tier caveat:** any of these on Slack Free truncates history at 90 days; check `secrets_registry.md → slack.session-cookies → Active workspaces` for the per-workspace tier note.
- **Slack auth, db-322 (2026-08-24):** cookie auth is now the FALLBACK. Preferred per workspace is an `xoxp-` app user token (internal Slack app, read-only user scopes) written with `assistant/scripts/slack-xoxp-set.sh`; the launcher prefers it and ignores cookies when present. It is not session-bound, so it does not get kicked out. Walkthrough: `skills/slack_auth_setup.md`. Health: `assistant/slack-auth-probe.js` (cron 06:20, Discord alert on transition + weekly re-nag). Durability: `assistant/rag-slack-indexer.js` (cron every 4h) ingests channel history to RAG as `source='slack'`, so dead auth stops new material rather than erasing Slack knowledge, and free-tier 90-day truncation stops losing history. **Check registration before debugging creds** - in Aug 2026 all 7 `slack-*` servers had fallen out of `~/.claude.json` and the symptom looked identical to an auth failure. Status 2026-08-24: 6 workspaces on dead cookies, `upstream` never provisioned, blocked on Robert creating the apps (db-322).
- **Playwright** — `mcp__playwright__*` — headless browser automation.

### claude.ai cloud connectors (cloud-side OAuth, work from VPS sessions but separate auth surface)
- **Gmail (cloud)** — `mcp__claude_ai_Gmail__*` — alternate cloud surface; native `mcp__gmail__*` is preferred per VPS-runtime principle.
- **Google Calendar** — `mcp__claude_ai_Google_Calendar__*` — events, free time, scheduling. Native equivalent for read-only ops: [`assistant/scan-meetings.js`](../../../projects/assistant/scan-meetings.js).
- **Atlassian Rovo** — `mcp__claude_ai_Atlassian_Rovo__*` — alternate cloud surface for Jira/Confluence.
- **Miro** — `mcp__claude_ai_Miro__*` — boards, diagrams, docs, tables. Cloud-only.

### Cloud-only via claude.ai (no VPS equivalent yet)
- **Instagram** — `mcp__social-channels__instagram_*` — profile, posts, insights, publish.
- **YouTube** — `mcp__social-channels__youtube_*` — channel info, video stats, search.
- **TikTok** — `mcp__social-channels__tiktok_*` — profile, video stats.
- **Steam (community)** — `mcp__social-channels__steam_*` — app details, reviews, news, player count.

### Other
- **LinkedIn (post)** — `mcp__linkedin-composio__*` (Composio) — post creation/deletion, comments, reactions, company pages, image/video upload, ad targeting. Auth via Composio OAuth (db-048). Per-session URL — regen via `assistant/scripts/generate_composio_mcp_url.py`.
- **Fortnox** — `mcp__fortnox__*` — accounting/invoicing.
- **fal-ai** — *not yet wired as MCP* (db-125 pending). Stop-gap: REST via `FAL_KEY` from `.env` (see `secrets_registry.md → fal.api-key`). Discuss tool choice with Robert first per [feedback_art_tool_discussion].
- **Stability AI / OpenAI Image** — not wired, no key in registry.

## Why this memory exists
Robert noticed that between sessions, Claude forgets which MCP tools are available and needs reminding. This list ensures proactive tool usage. When a task involves email, social media, project management, or docs — fetch the relevant schema via ToolSearch instead of asking Robert.

## Subagent note
When spawning agents, explicitly mention relevant MCP tools in the prompt so the agent knows to use them.
