---
name: Always suggest long-term solutions
description: When an integration requires per-session auth, manual setup, or any repeated friction, proactively suggest promoting it to a persistent VPS service and hand the work to DevOps
type: feedback
originSessionId: d4cc9839-cdbc-428e-959c-d7d145f95ec4
---
Per-session OAuth flows, manual tool setup, and one-off integrations are all signals to propose a durable VPS-hosted version. Robert prefers long-term infrastructure over per-session workarounds.

**Why:** Robert said (2026-04-14) "always suggest long-term solutions" after I only offered the interactive OAuth dance for Gmail MCP. Repeating auth every session burns time, blocks 4am autonomous runs, and means scheduled agents (Analytics, Content Editor scheduled mode, DB email scanner) can't touch those integrations at all.

**How to apply:**
1. When any integration needs session-time OAuth, manual config, or a browser step, pause and ask: "Should this be a persistent VPS service?" Default to yes for anything Robert uses across projects.
2. Self-host with stored refresh tokens (precedent: Fortnox MCP — OAuth token in VPS env, runs headless).
3. Targets that should all be VPS-persistent: Gmail, Google Drive, Google Calendar, Atlassian (Jira/Confluence), LinkedIn, Instagram, WhatsApp, Miro, Slack, Discord, and any new integration Robert relies on cross-project.
4. Secrets go in `/home/assistant/projects/secrets_registry.md` by `<domain>.<purpose>` ID, values in VPS `.env` + LastPass (per existing secrets_registry feedback).
5. Hand the setup work to the DevOps agent — don't do MCP wiring in-session yourself. Create a DB follow-up tagged for DevOps, or invoke the agent.
6. Surface the long-term recommendation even when the user hasn't asked, especially the first time friction appears in a session.
