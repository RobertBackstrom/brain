---
name: Memory write protocol — inline-save default, /close audits
description: When to save memory/learnings inline vs draft-first; resolves the CLAUDE.md vs /close conflict
type: feedback
originSessionId: 7153d773-b18a-4e59-8c5f-3ebc94b63aa6
---
**Rule:** New memory and agent learnings save **inline** during the work that produced them. `/close` is an audit + sweep for *missed* learnings, not an approval gate on saved ones.

**Why:** Robert flagged a genuine protocol conflict on 2026-05-12. CLAUDE.md §Named Agents said "ALWAYS write new learnings back"; `.claude/commands/close.md` §3 said "draft and show first, don't auto-save." Both used strong language. Resolution went to Option A — inline-save wins — because: (1) context decays fast, drafting-then-approving at session-end loses nuance, (2) technical learnings like the Atlassian/MCP wrapper-script pattern (devops_learnings.md §"Multi-site Atlassian via wrapper-script MCPs") are hard to reconstruct after the work, (3) the friction of draft-first per learning discourages agents from logging anything, defeating the cross-project memory mechanism.

**How to apply:**
- **Date-stamp check (do this on EVERY dated write — learnings, logs, tickets, trackers):** the `[YYYY-MM-DD]` on any entry comes from the session **`currentDate`** context, full stop. Do NOT derive it from the shell `date` command (it has read wrong — sandbox clock skew put it 2 days off on 2026-07-03), from a file's mtime, or from the newest existing entry's date. If you're about to stamp a date, glance at `currentDate` first. This is the single most-missed step when agents append learnings — see [[feedback_anchor_on_currentdate]].
- **Inline-save (no approval gate):**
  - New agent learning that fits the protocol (surprising outcome, validated judgment call, tooling gotcha, client preference)
  - New user/feedback/project/reference memory per CLAUDE.md auto-memory section
  - Explicit "remember X" request from Robert
- **Approval gate still applies:**
  - **Modifying or deleting** existing memory entries (merge / supersede / remove) — `/close` §2 cleanup proposals still get reviewed
  - Anything that encodes a contested Robert preference or judgment call where the agent is uncertain — when in doubt, draft inline and ask before committing
- **`/close` §3 behavior:** List what got saved inline today (titles only), then sweep for misses. Draft only the missed ones. Don't re-litigate inline saves; if Robert wants one revised, that's handled as a memory-cleanup proposal under §2.
- **Cross-refs:** [[CLAUDE.md]] §Named Agents step 4, [.claude/commands/close.md](.claude/commands/close.md) §3.
