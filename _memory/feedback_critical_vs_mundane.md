---
name: Critical vs Mundane task classification
description: Task-level autonomy flag that decides whether Robert is in the approval loop. Replaces agent-level scheduling. Applies to every ticket and every agent.
type: feedback
originSessionId: 82050791-0030-4319-adc0-4a0ea51cedfd
---
**Rule:** Every ticket carries a `taskType` flag — `critical` or `mundane`. That flag, not the agent, decides whether Robert is in the approval loop.

**Mundane (agent executes without approval):**
- Drafts (emails to Gmail drafts, social posts, outreach copy, reply suggestions)
- Scraping / monitoring (forums, KPIs, inboxes, calendars, community channels)
- Research, enrichment, ticket hygiene, skill maintenance
- Meeting-note pulls from Gemini/AI with buffer before asking Robert
- Agents run on check-out and through off-hours

**Critical (agent plans → Robert approves → agent executes → Robert reviews → close):**
- Publishing / transmitting anything outward-facing (social posts, emails sent, forum replies, DMs)
- Writes to client-facing systems (Jira, storefronts, Steam forums, web pages)
- Spending, contracts, anything legal/financial/binding
- Creation of drafts is mundane; **publication of those drafts is critical**

**Key rule:** Agents CAN create critical tickets autonomously. They just can't execute them. (e.g. community bot finds a Discord thread, drafts a reply, creates a critical ticket — Robert posts.)

**Who sets the flag:**
- Agent proposes at ticket creation using the rubric above
- Robert confirms on edge cases only; most are set by agent
- Default when agent is unsure: foreground-takeover question (see [[feedback_must_ask_escalation]]) — don't guess, ask

**Floor:** The CAN-DO / MUST-ASK matrix in [[autonomous_decision_framework]] still applies. Mundane never means "allowed to publish without approval." Crit/Mundane is routing; the floor is absolute.

**Why:** Robert wants maximum autonomous throughput but zero risk of unapproved external actions. Task-level flagging scales cleaner than agent-level ("Analytics is scheduled, BizDev is on-demand") — every agent can be autonomous for the right tasks.

**How to apply:**
- When creating a ticket, always propose a `taskType`
- On check-out, run the mundane queue without asking
- On check-in, surface the three review queues: plans-awaiting-approval, input-needed, completed-awaiting-review
- If a mundane task escalates mid-run (finds something that needs judgment), flip to critical and queue for Robert
