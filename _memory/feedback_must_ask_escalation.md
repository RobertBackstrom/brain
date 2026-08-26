---
name: MUST-ASK 3-tier escalation
description: When an agent hits a MUST-ASK mid-run, use this 3-tier escalation instead of always pinging or always queueing silently.
type: feedback
originSessionId: 82050791-0030-4319-adc0-4a0ea51cedfd
---
**Rule:** When an agent hits a MUST-ASK boundary mid-run, escalate along three tiers based on urgency and blocking state.

**Tier 1 — Ticket Q&A (default, quiet):**
- Agent writes the question as an `AskUserQuestion`-style widget on the ticket's Activity tab
- Sets `needs_input: true`
- Keeps working on other subtasks if any exist
- Robert sees it next inbox sweep
- Use when: agent has other work to do, question can wait, non-urgent

**Tier 2 — Discord ping (nudge):**
- Trigger: Tier 1 question has sat >15 min during Robert's check-in window (office hours)
- DB Discord bot DMs Robert with ticket link + question summary
- Robert replies in Discord OR opens the ticket
- Use when: office hours + unresolved question that's starting to block real work

**Tier 3 — Foreground takeover (demand):**
- The board flips into modal mode — full-screen takeover with the question widget + context snippet + answer options
- Robert can't do anything else on the board until answering or deferring
- Tab title flashes; Discord also pings
- Use when: agent is truly blocked with no other subtasks, answer takes 5 seconds, or task flagged `blocking: true`
- Also the default path when Crit/Mundane classification is unset and the agent needs Robert to choose

**Why:** One-size interrupt style is wrong. Background scrapers shouldn't hijack Robert; genuinely blocked agents shouldn't sit silent in the inbox. Three tiers match the real spectrum of urgency.

**How to apply:**
- Default every question to Tier 1
- The board escalates Tier 1 → Tier 2 after 15 min during office hours (automatic, not the agent's job)
- Agents only set Tier 3 explicitly when they're truly stuck with nothing else to do, or when the task type is unset

**Related:** [[feedback_critical_vs_mundane]], [[autonomous_decision_framework]]
