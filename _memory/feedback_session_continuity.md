---
name: session-continuity-workflow
description: Connect every session to a DB ticket; sweep inbox/outgoing mail and update memory at both session boundaries (open + close) so context never stays trapped in conversation history
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0510e4d6-9262-4120-b007-7aad4de9fe5e
---

Every session connects to a DB ticket, and every session boundary — open and close — includes a mail sweep and a memory update. Context must never stay trapped in conversation history.

### 1. Session start — orient before working
- Check whether the work relates to an existing DB ticket. If Robert doesn't reference a ticket ID, search the DB for related tickets and suggest them; if none fits, offer to create one. Never silently work without a ticket connection — the DB is the hub.
- **Sweep mail before starting a project session:** check the inbox and Sent/outgoing mail relevant to the project. Send/reply/awaiting-reply statuses move outside Claude's sessions — never trust stale session memory for mail state. See [[feedback_verify_draft_sent]].
- Read the ticket's activity log and the relevant project memory for prior context.

### 2. Session end — write back before closing
- Write a short session summary to the ticket's activity log: what was done, key decisions, where things stand, open questions.
- **Sweep mail again and update memory before closing:** re-check inbox/Sent for anything that moved during the session, reconcile trackers / the deal wiki against live mail state, and write any durable new facts to memory. Don't close with mail state or learnings unrecorded.

### 3. Cross-session awareness
- When starting on a ticket, read its activity log first. If Robert mentions overlapping sessions, read both logs, consolidate into one, mark the other merged.

**Why:** Sessions become silos when context stays trapped in conversation history. The ticket activity log, memory, and live mail state are the persistent layers that bridge sessions. Robert's instruction (2026-05-21): "check inbox/outgoing mail and update memory before closing or when opening a project session" — added after Claude reported a draft as unsent that Robert had already sent.
**How to apply:** Steps 1-2 are mandatory, not optional. The mail sweep + memory update at both boundaries is how the system stays coherent.
