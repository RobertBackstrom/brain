---
name: Office hours prioritization
description: Prioritize input-needed tasks during Robert's office hours (08:00–18:00 Stockholm); push autonomous/no-input work into down time.
type: feedback
originSessionId: dc3e5bca-1e16-4bf0-8106-cb57de4e40d3
---
**Primary trigger:** Robert's **check-in / check-out via the Death Board Discord bot**. Check-in = office open; check-out = office closed. No wall-clock assumption.

**Fallback heuristic (when no check-in state is known):** 08:00–18:00 Stockholm, Mon–Fri. Weekends default to check-out mode.

**On days Robert never checks in:** treat as fully autonomous — run mundane queue through the day the same way overnight runs do.

Use the check-in state as the scheduling axis for agent work.

**During office hours (08–18 local):**
Prioritize tasks that need Robert's input — draft reviews, approval gates, decisions, anything blocked on his eyes or voice. When multiple tickets are ready, surface the input-needed ones first so his presence unblocks the pipeline. Autonomous tasks can wait.

**Outside office hours (18–08 local, weekends):**
Prioritize autonomous / no-input tasks — research, drafts, code implementations, data pulls, scraping, builds, anything that can land in a queue for his morning review. Avoid creating new input gates late in the evening if possible — save them for the next morning unless urgent.

**Why:** Robert's attention is the bottleneck; wall-clock alignment matters. Stacking input-needed work into the window when he's actually at the keyboard maximizes throughput. Running autonomous jobs overnight means he wakes up to results instead of a queue.

**How to apply:**
- Read check-in state from the Discord bot first, wall-clock second.
- Morning inbox (at check-in) surfaces three queues: plans-awaiting-approval, input-needed, completed-awaiting-review.
- Check-out triggers the mundane queue: unattended planning + approved-plan execution + mundane tasks (no approval). See [[feedback_critical_vs_mundane]].
- When a new input gate appears after check-out, queue for next check-in unless explicitly blocking (then use foreground takeover per [[feedback_must_ask_escalation]]).
- Days with no check-in at all = weekend-style autonomous mode all day.
