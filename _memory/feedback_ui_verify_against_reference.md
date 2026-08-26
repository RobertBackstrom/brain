---
name: UI verification must compare against the reference, not the prior state
description: After any UI change made against a reference image Robert provided, compare the rendered screenshot to the reference — not to the previous iteration — using an explicit checklist of agreed traits before presenting. Save the reference image alongside screenshots.
type: feedback
originSessionId: 8dbd03cc-3ffa-4012-9b7a-b047b8e47930
---
After any UI change made against a reference image Robert provided, the verification step must compare the rendered output to **the reference**, not to the *previous iteration*. Use an explicit checklist of the traits agreed in the handshake.

**Why:** On db-017 phase 3 (2026-04-14), shipped hexes that were vertically stretched rhombuses because `preserveAspectRatio="none"` stretched a square-viewBox polygon into a 1:1.1547 container. Screenshot looked "better than phase 2" so it got reported as done — without side-by-side against Robert's reference, which would have made the distortion obvious in 5 seconds. Robert caught it and asked for the workflow fix.

**How to apply:**
1. When Robert sends a reference image, save it to `assistant/ui-review/<ticket-id>/reference.<ext>` before coding.
2. In the handshake message (before coding), write an explicit bullet list of traits to verify (e.g. "regular hex = equal sides", "solid fill", "rounded corners", "white iconography"). This is the verification checklist.
3. After implementing, screenshot the rendered state, pull up the reference, and tick each trait off against the rendered output — visually compare geometry, colors, spacing, hierarchy. If any trait fails, fix before presenting.
4. Present with the ticked checklist visible so Robert can spot-check what was verified.

Scope: any UI task where a reference image was provided. Skip for pure code changes or UI tweaks without a reference.
