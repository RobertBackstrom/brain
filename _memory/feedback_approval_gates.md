---
name: Two approval gates for session work
description: Only two human-in-the-loop checkpoints — ticket creation (mid-session) and critical ship actions. Everything else executes automatically.
type: feedback
originSessionId: dc3e5bca-1e16-4bf0-8106-cb57de4e40d3
---
Robert's session workflow has exactly two approval gates. Everything in between executes without asking.

**Gate 1 — Ticket creation (mid-session only):**
Before creating a DB/Jira ticket during an interactive session, show a lean proposal: title + one-line spec. Get thumbs up, then create. Keep it tight — no full spec draft up front.

**Gate 2 — Critical ship:**
Ask before the user-visible moment on critical surfaces:
- Any write to **client systems**: Jira boards, new docs in client-shared Drive folders
- Any **client communication**: email, WhatsApp, Discord DMs
- **Pushes to client git repos** (the push itself is critical, not the commit)
- **Public posts on Robert's personal social profiles**

Exception: content that was already approved in a content plan via the outreach/BizDev agent is cleared to post without re-asking.

Non-critical = no gate. Local commits, internal DB tickets, personal repo pushes, research notes, drafts in `drafts/` or `followups/`, file edits, test runs, **local harness/config changes** (settings.json, env vars, MCP registration, hooks) — all execute freely.

When a task needs implementation work and a matching agent exists (DevOps, PM, BizDev, etc.), activate the agent and execute. Don't turn it into an options menu for Robert — surface the trade-off in one line, make the call, ship. He'll correct if wrong.

**Autonomous 4am runs:**
- Gate 1: auto-create tickets (Option A). Robert reviews at standup.
- Gate 2: already enforced by the standing "never publish/send" rule — autonomous runs never cross it.

**Why:** Robert wants throughput on small stuff and a clean review surface for the things that matter. Two gates, not ten. Over-asking on commits or internal tickets wastes his attention; under-asking on client comms or public posts is a reputation/contract risk.

**How to apply:** Before any action, classify: is this a ticket being created mid-session, or a user-visible action on a client/public surface? If yes to either, ask first. If no, proceed. When unsure whether a surface is "client," err toward asking once and saving the answer.
