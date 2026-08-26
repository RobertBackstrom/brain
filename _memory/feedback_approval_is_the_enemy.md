---
name: Approval prompts are the enemy, not tokens
description: When Robert says a tool shouldn't "sit behind ToolSearch" or similar, he means the approval prompt, not the schema-fetch step. Fix with permissions.allow, not ENABLE_TOOL_SEARCH.
type: feedback
originSessionId: d729c984-260e-4fff-a7ff-c7f28e1e6164
---
When Robert complains about a tool flow being slow, gated, or "in the way," the default assumption is he's talking about the **per-call approval prompt** that interrupts him — not token cost, not ToolSearch's schema-fetch, not subagent tool loading.

**Why:** Approval prompts yank him out of whatever he's doing. Tokens and latency don't. He's already said pre-approval is fine for Bash and for the main Assistant — the pattern is: silent execution on trusted tools, friction only at the two official gates (mid-session ticket creation + critical ship).

**How to apply:** Before reaching for `ENABLE_TOOL_SEARCH=false` or any preload mechanism, check whether the real fix is adding the tool(s) to `permissions.allow` — either user-level (`~/.claude/settings.json`) or project-level (`projects/.claude/settings.local.json`). Wildcards like `mcp__gmail__*` work and future-proof the entry. Two distinct knobs:

- **Schema loading** — `ENABLE_TOOL_SEARCH` env var. Affects tokens, not UX.
- **Per-call approval** — `permissions.allow` list. Affects UX, not tokens.

Don't conflate them. Default to the cheaper, UX-targeted one.
