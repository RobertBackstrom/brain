---
name: feedback-backlog-is-parked
description: "backlog = parked (no auto-processing); only planned + in_progress are eligible for 4am sweeps, checkout dispatch, and agent execution"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1459ec94-bba9-4188-820e-b70f468fd2dd
---

The 5 canonical ticket statuses are: `backlog`, `planned`, `in_progress`, `done`, `closed`. No others exist.

`backlog` means parked - no autonomous agent will touch it. Only `planned` and `in_progress` are eligible for 4am sweeps, checkout dispatch, stale scans, overdue alerts, and ops queue.

`icebox` and `rnd` were removed (db-170, 2026-05-21; full cleanup 2026-06-01). All former icebox tickets were migrated to `backlog`.

**Why:** Plane's bidirectional sync maps multiple DB statuses to one state group. Making `backlog` = parked gives a clean round-trip (Plane backlog = DB backlog = parked) without a lossy collapse on write-back. Five statuses keeps the model clean across server, kanban, dashboard, Hive, and Plane bridge.

**How to apply:** When creating tickets, set `planned` if agents should pick them up, `backlog` if they should wait for Robert's active decision. When filtering for actionable work, only include `planned` + `in_progress`. Related: [[feedback_kanban_epic_column_model]].
