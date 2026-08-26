---
name: feedback_check_downloads_desktop_first
description: "When Robert references a pasted/attached file, check ~/Downloads and ~/Desktop on the VPS first; pasted images don't persist to disk."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 523a46f5-e275-4733-a122-0a4c90edbe7a
---

When Robert says "use this image/logo/file" with a paste or attachment, the bytes do **not** land on the VPS filesystem — the harness passes them to the model as image/content only, so there is no path to serve from. Robert's standing instruction: **"Always look in the Downloads folder or Desktop to start with."**

**Why:** The VPS is the runtime ([[feedback_vps_operating_environment]]); Robert's laptop Downloads/Desktop are not reachable from the VPS. He drops files into the VPS via VS Code (drag into the workspace) and expects them in a predictable spot.

**How to apply:**
1. On any "use this file" request, first `ls -lat ~/Downloads ~/Desktop` on the VPS, then search recent files (`find ... -newermt today`) and the relevant project folder.
2. `~/Downloads` and `~/Desktop` did not exist on the VPS by default — created them 2026-06-16 as the canonical drop zones.
3. If the file genuinely isn't on disk, don't stall: stage everything that doesn't need the bytes (layout, CSS, markup referencing the expected path), then ask Robert to save it to a concrete VPS path (e.g. the project's drafts/ folder or ~/Downloads/) and finish on drop.
4. Logos/art often arrive on a **solid white background** — for dark pages, default to knocking white out to transparent (PIL alpha threshold) unless edges are dirty, then fall back to a dark plate behind the mark.
