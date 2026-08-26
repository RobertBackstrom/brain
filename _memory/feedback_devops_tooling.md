---
name: DevOps handles agent tooling
description: MCP setup, tool wiring, permissions, and integration work goes to the DevOps agent. Claude should request DevOps activation rather than doing it inline.
type: feedback
originSessionId: 164e468c-a421-49c5-932a-cfc6fcd7dadf
---
MCP server setup, tool wiring, permission allowlists, settings.json edits, and any harness/integration work belongs to the DevOps agent. Don't do it inline from a session that was activated for something else.

**Why:** Robert built a named-agent pattern specifically so domain expertise compounds in one place. When the main session does ad-hoc DevOps work, the gotchas (vec0 PK type, Voyage rate limits, settings scope inheritance, etc.) end up scattered across project memories or lost entirely instead of accumulating in `agents/memory/devops_learnings.md` where the next DevOps task can find them. Demonstrated repeatedly: Gmail MCP pre-approval (db-049), GDrive allow-listing, Playwright wiring (db-032), Voyage RAG (this week).

**How to apply:**

- When a task touches `~/.claude/settings.json`, `~/.claude.json`, `assistant/server.js` agent-spawn paths, MCP server registration, or systemd timers — activate DevOps via `/devops` first if not already, then proceed.
- After completing the work, write the gotcha and the pattern to `agents/memory/devops_learnings.md` with date + project tag.
- For new MCP servers: register in `~/.claude.json` mcpServers block, add wildcard `mcp__<server>__*` to permissions.allow in **both** user (`~/.claude/settings.json`) and project (`.claude/settings.local.json`) scope so subagents inherit pre-approval.
- For new harness behaviors that should be automatic: that's a hook, not a memory rule — use the `update-config` skill.

**What this rule is NOT:**
- Not a blocker for trivial inline work (e.g. one-line config tweak Robert is watching). Use judgment.
- Not a permission gate — DevOps doesn't need approval to read or experiment, only to ship persistent changes that affect every future session.
