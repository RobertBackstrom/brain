---
name: Check activity logs before declaring blocked
description: Always read ticket activity logs, parent epics, and related tickets before categorizing a ticket as blocked or needing Robert's input
type: feedback
originSessionId: c5c9d0d8-ec34-463a-a129-295d61877ace
modified: 2026-08-02T12:04:06.495Z
---
When scanning DB tickets for autonomous processing, always read the full ticket including activity log, check the parent epic, and check related tickets before declaring something "blocked" or "needs Robert."

**Why:** Robert caught that gen-158 had a staff sheet attachment in Rosemary's latest email, and the BADASS epic had full context. The agent scan declared it blocked without checking.

**How to apply:** During queue runs, for every ticket: (1) read the full ticket with activity, (2) read the parent epic if one exists, (3) check Gmail for recent related emails, (4) only then assess whether it's blocked or actionable. Don't rely on ticket summaries alone.

Sibling rule, one level up: [[feedback_verify_with_sibling_agents]] applies the same instinct across agents — if the fact belongs to another agent's domain (invoice state to CorpBot, infra to DevOps), query that domain rather than escalating to Robert.
