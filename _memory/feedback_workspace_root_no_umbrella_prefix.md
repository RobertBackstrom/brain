---
name: feedback_workspace_root_no_umbrella_prefix
description: "Clickable file links must be relative to Robert's VS Code workspace root (umbrella/) - never prefix \"umbrella/\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bfd4134c-822a-4411-a330-3eef9d8a78c3
---

Robert's VS Code SSH workspace is rooted at **`/home/assistant/projects/umbrella/`** (the project `CLAUDE.md` at `projects/` is a symlink into `umbrella/CLAUDE.md`). So clickable markdown file links, which the VS Code extension resolves **relative to the user's workspace root**, must NOT carry an `umbrella/` prefix - that makes them broken "half links" that resolve to nothing from his root.

**Do:** `[CHECKLISTA.md](aurora_punks/legal/apds_bevakning_underlag/CHECKLISTA.md)`
**Don't:** `[CHECKLISTA.md](umbrella/aurora_punks/legal/...)`

Files still physically live under `/home/assistant/projects/umbrella/...` (that is where Read/Write/Bash operate), and when quoting a full absolute path for shell use, include `umbrella/`. The rule is only about the **clickable link path shown to Robert** - strip the leading `umbrella/` so it is relative to his workspace root.

**Why:** Robert flagged (2026-07-13) that "det finns inget umbrella på VPSen" from his workspace view - the links didn't work for him. His root IS umbrella, so `aurora_punks/...` is already correct.

**How to apply:** In any user-facing markdown link, drop a leading `umbrella/` segment; keep the rest of the path. Applies to the main Assistant and every spawned agent that reports file paths back to Robert. Note: there is also a separate `projects/aurora_punks/` sibling folder outside the umbrella workspace - the working AP tree Robert sees is `umbrella/aurora_punks/` (= `aurora_punks/` from his root).
