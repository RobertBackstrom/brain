---
name: Death Board kanban — epic = column
description: After 2026-05-02 redesign the kanban is epic-organized, not status-organized; status is a section inside each column. Don't reason against the old 7-status-column model.
type: feedback
originSessionId: 68935ec3-c156-4f2a-888c-2dafb02d9c05
---
The Death Board kanban switched on 2026-05-02 (`db-098`) from a 7-status-column board to an **epic-as-column** board. Every `type: epic` ticket is one column; tickets inside are grouped into collapsible status sections (In Progress / Planned / Backlog / Icebox / Done / Closed) sorted by priority desc, due asc.

**Why:** The old model made it impossible to see "what's the state of K2C?" — answering required scanning all 7 columns mentally. The new model puts every project's state in one column, with status as a per-ticket attribute rendered as a section inside the column.

**How to apply:**
- When designing or modifying any DB-related code, default to "columns ARE epics; status is a section attribute." Don't add features that assume status-as-column.
- Tickets without a `parent:` auto-render under `<prefix>-000-epic` at render time — DON'T write a backfill that fills `parent:` into every orphan ticket; the auto-assignment is intentional.
- Drag-and-drop on the kanban is **reparenting**, not status change. New code that emits drop events should call `PUT /api/followups/:id/parent`, not `/status`.
- Canonical statuses are 6 now (`icebox, backlog, planned, in_progress, done, closed`) — `rnd` was dropped. Don't reintroduce `rnd` in tooling, prompts, or templates without a follow-up decision.
- The detail panel uses **structured `questions[]`** in YAML frontmatter, not a wall-of-text "needs input" section. Agents asking Robert mid-task should use `ipc-helper.js askQuestion()` (HTTP-backed) — that writes to `questions[]`, not to `.question` files.

Full feature spec: [[project_deathboard_features]] (Kanban redesign section). Source: `db-098`, output_log entry 2026-05-02.
