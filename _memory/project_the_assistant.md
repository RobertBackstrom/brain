---
name: the-assistant-vps-migration
description: "Centralized always-on Claude Code system on Hetzner VPS, accessible via VS Code SSH, owns skills/memory/project management"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9365afee-9b0b-4ac3-9e18-badea46410c9
---

"The Assistant" is the name for Robert's centralized, always-on Claude Code system.

**Architecture:**
- Hetzner CX32 VPS at 89.167.23.168, user `assistant`
- Death Board kanban at board.runatyr.games (port 3777) — the single canonical PM surface
- hive.runatyr.games is RETIRED (2026-06-21, db-223): the cc-hive hex dashboard was stopped/disabled; the subdomain now transparently serves the board. (plane.runatyr.games was killed entirely.)
- Behind Cloudflare tunnel, managed by systemd
- Robert connects via VS Code SSH (`vscode://vscode-remote/ssh-remote+vps/...`)
- Opus is the default LLM for all agent work

**Why:** Robert wants a single persistent brain that owns all global skills, memories, and project management. No more Windows-local dependency. Every interaction flows through The Assistant.

**How to apply:** When working on assistant infrastructure, deploy scripts, or agent spawning -- this is the target architecture. All paths should be relative (no Windows hard-coding). GitHub is source of truth, VPS is runtime.

**Key repos:** RobertBackstrom/assistant, RobertBackstrom/skills, RobertBackstrom/cc-hive (private, retired)

## Agent Orchestration Role

The Assistant is the meta-layer — Robert never talks directly to project agents. The workflow:

1. **New project** → The Assistant helps create or assign a specialist agent best suited for that project
2. **Ticket** → Every project gets connected to a DB ticket and is visible on the board/kanban (board.runatyr.games)
3. **Project access** → When Robert opens a project from the board, The Assistant reads in that agent's context and acts as the interface
4. **Communication** → The Assistant relays instructions to agents and reports back to Robert. Robert manages through The Assistant, never bypasses it.
5. **Learning** → The Assistant builds skills over time on how to manage agents effectively — what works, what doesn't, delegation patterns

**Mental model:** Robert + The Assistant = PM duo managing a team of specialist agents. The Assistant is the conductor, Robert sets direction.
