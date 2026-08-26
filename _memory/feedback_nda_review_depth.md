---
name: NDA reviews — proportional, not deep
description: For inbound NDAs/MNDAs, Lawyer agent should do a light proportional review (red flags only), not a full clause-by-clause redline — but always extract cross-project learnings even on light reviews
type: feedback
originSessionId: 32a2d705-9dd9-4dc6-9f12-32d4723d9284
---
NDA reviews should be proportional to risk. NDAs are commodity contracts; full clause-by-clause redlines are overkill for standard mutual NDAs from warm counterparties.

**The rule:** Lawyer agent runs a *light* review on NDAs — verdict + real red flags only, not a deep redline. Skip cosmetic stuff. Focus on the handful of items that actually bite (mutuality, term, governing law, IP-leakage clauses sneaking in, non-solicit/non-compete masquerading as NDA terms, signing-entity correctness).

**Always extract learnings** even on light reviews. Robert explicitly wants `lawyer_learnings.md` updated with anything non-obvious found, so the agent gets sharper on NDAs over time even when individual reviews are quick.

**Why:** Most NDAs Robert sees are mutual, low-stakes, precursor to deck/finance sharing. Deep review burns Lawyer-agent cycles and slows the deal — counterparties expect NDA turnaround in days, not weeks. But the *meta-knowledge* (UK vs Swedish posture, what UK SMEs typically slip in, what common templates omit) compounds across deals, so harvest it.

**How to apply:**
- Default Lawyer dispatch for NDA = light proportional review prompt (verdict + real red flags + signing-entity check, ~250 words back).
- Always include "extract learnings worth saving" in the dispatch.
- Reserve full redline treatment for: contracts with payment/IP/exclusivity terms, anything over £/€50k commitment, anything where counterparty is a publisher or platform, or anything Robert explicitly flags as high-stakes.

**Source:** Robert's instruction during Formula Drone NDA review, 2026-05-06: *"for NDA the lawyer wouldnt have to be too thorough but great learnings."*
