---
name: Status updates trail execution
description: Never mark a tracker/ticket/contract status forward of reality. Status fields only move AFTER the actual action has been executed.
type: feedback
originSessionId: 8e82d357-bdc6-452a-83df-239e573ffb25
---
Never change a status to a forward state until the actual task that produces that state has been executed.

**Why:** Surfaced 2026-05-18 on K2C subcontract tracker — entries said "Signed 2026-04-22" for the 5 main subs even though redrafts on 2026-05-06 reopened them and they were still in pre-sign. A forward-marked status hides truth from every other agent/process reading the tracker and from Robert at-a-glance. The misalignment cost a real read-cycle of "wait, are these actually signed or not?". Tracker fields are operational signals, not aspirational ones.

**How to apply:**
- Tracker / ticket / contract status only moves *after* the action that produces the new state has run. Examples:
  - "Sent for eSignature" — only after the Drive eSignature flow has actually been initiated and confirmed.
  - "Signed" — only after the signed PDF/Gdoc lands and is filed.
  - "Filed" — only after the file is in the correct GDrive folder.
- Updating *backwards* to reflect current truth (e.g., flipping a stale "Signed" back to "Unsigned" because a redraft reopened it) IS allowed — that's correcting the record to match reality, not promising future state.
- When unsure: write what is true *now*, not what is about to be true. If you're about to execute step X, don't pre-mark X done; mark it done when X returns success.
- Applies to: contract trackers, deal pipeline, ticket status, output_log entries, deliverables registers, any other state field a downstream agent might trust.
