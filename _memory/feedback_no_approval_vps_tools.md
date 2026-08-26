---
name: No per-call approval for trusted local tools
description: Don't ask approval before Bash or read-only VPS tools (Drive/Gmail/Jira/Calendar reads, CLI, file reads) — in the main session or any subagent. Just run them.
type: feedback
originSessionId: 94ec0c09-d62b-4722-9005-cbb2cd8bc45b
---
Don't ask Robert for per-call approval before running trusted local tools — neither in the main session nor in any spawned subagent. This covers two pre-approved classes:

- **Bash** — `ls`, `cat`, `node` scripts, `git status`, etc. Pre-approved everywhere.
- **Read-only VPS tools** — Drive reads, Gmail searches, Jira fetches, Calendar reads, WhatsApp reads, file-system reads. Just execute.

**Why:** Robert has repeatedly granted blanket approval for VPS-local work — he called it out on 2026-04-13 when I re-asked for approval on `gdrive_read_file` for a meeting-notes GDoc. Pausing on these prompts breaks the autonomous/office-hours workflow and every subagent's ability to operate independently. The permission is wired in `.claude/settings.local.json` (project) and `~/.claude/settings.json` (user), so it inherits across all sessions and subagents. The approval prompt — not tokens or latency — is the friction (see [[feedback_approval_is_the_enemy]]).

**How to apply:**
- Never preface a Bash or read-tool call with "this may need approval" or stop to ask.
- When spawning subagents (PM, CorpBot, GameDev, DevOps, UIbot, BizDev, Content, Analytics, Index, etc.), assume these tools are auto-allowed — don't remind the user about permissions.
- Extends the existing permission-free rules for Playwright (see [[feedback_ui_verify_against_reference]]) and allabolag.se WebSearch.
- Still confirm before: external writes (publishing social posts, sending emails, posting to Jira/Discord, DocuSeal, editing client systems), destructive ops, anything with blast radius outside our systems. The "Confirm before external changes" rule (CLAUDE.md) still holds — this just clarifies that *reads* and local Bash on authorized tools don't count as external changes.
- If a specific Bash command is actually denied at runtime, that's a real settings issue — investigate and fix settings, don't fall back to asking per-call.
