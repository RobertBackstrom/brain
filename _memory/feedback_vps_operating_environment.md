---
name: Operating environment is the VPS
description: All scheduling, authoring, API/MCP tools, health checks, and LLM usage operate within the VPS context — laptop is never the runtime
type: feedback
originSessionId: 9bd244aa-4744-46ba-87df-18495c1c67d6
---
The Assistant and every agent operating under it (PM, Content Editor, Analytics, BizDev, GameDev, DevOps, UIbot, CorpBot, Index) run within the VPS context. The Hetzner VPS (`board.runatyr.games`, user `assistant`) is the runtime — Robert's laptop is just a thin SSH client.

**Why:** Robert built this system specifically to remove Windows/laptop dependency. If anything depends on his local machine being awake, the system fails when he's asleep, traveling, or just not at his desk. He restated this 2026-04-29: "all our work with the Assistant, its agents, the Wikis and the masterbrain needs to take this into consideration." This is the foundational architecture, not a guideline.

**How to apply (the five layers):**
- **Scheduling** → systemd user timers, the VPS crontab, or the Death Board internal scheduler (`server.js` Routine + 4am sweep + weekly reflection). Before any automation: "Where does this run when Robert is asleep?" → must be "the VPS." **`/schedule` is *not* VPS-native** — Anthropic's `/schedule` routines run in Anthropic's cloud sandbox and have no native VPS file or process access. Use `/schedule` only for tasks that live entirely in claude.ai connectors (Gmail, Calendar, Atlassian, Slack, Miro) plus WebSearch/WebFetch. The moment a routine needs to read VPS files, write to the masterbrain, hit Stack-A creds, or call non-public Death Board APIs, it belongs in cron. Cloud→VPS bridges are possible (HMAC-protected endpoint behind a Cloudflare Access bypass, mirroring `/webhook/atlassian` or `/webhook/docuseal`) but expand the public attack surface — ask whether a VPS cron job is the cleaner answer first. Lesson: the original `daily-morning-briefing` cloud routine had been silently failing on VPS-bound POSTs since 2026-04-23 because nothing distinguished "scheduled on the VPS" from "scheduled in Anthropic's cloud, dispatching toward the VPS." Don't conflate.
- **Authoring** → write directly to `/home/assistant/projects/`. Skills, memory, agent learnings, follow-ups, project folders, drafts, wiki content, masterbrain — all live here. No local-then-sync.
- **API / MCP / tools** → install on the VPS with stored refresh tokens. claude.ai-hosted connectors that need per-session OAuth are anti-pattern; promote to durable VPS service ([[project_the_assistant]], `db-020`, [[feedback_long_term_solutions]]).
- **Health checks & monitoring** → run from the VPS, target VPS services or external endpoints.
- **LLM usage** → Anthropic API from the VPS, Opus default, governed by `server.js` + `config.json` `agent_governance`.

**Path conventions:** Linux paths anchored at `/home/assistant/projects/`. No `%USERPROFILE%`, no `C:\`, no Windows-style paths anywhere — including in scripts, configs, docs, and ticket bodies.

Codified in CLAUDE.md "Operating Environment" section so all spawned agents inherit it.
