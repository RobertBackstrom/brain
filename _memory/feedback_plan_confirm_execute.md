---
name: Plan-Confirm-Execute hard gate
description: Hard gate for all non-trivial work — first output must be restated goal + 1–3 clarifying questions. No deep investigation or drafting until Robert confirms direction.
type: feedback
originSessionId: 80df2c40-7757-4026-974d-ce3d26268cd1
---
**Rule:** For any non-trivial task, the agent's FIRST output MUST be:

1. A 1–2 sentence restatement of the goal as understood (so Robert can spot a wrong frame)
2. 1–3 specific, answerable clarifying questions about scope, direction, audience, format, or key assumption
3. **STOP.** No deep investigation, drafting, code-writing, or multi-tool research until Robert confirms.

**Why:** Agents (and the main Assistant) currently default to: long internal thinking → long produced output → often in the wrong direction. The cost of one clarifying round-trip is far smaller than a 20-minute run that lands off-target. Robert flagged this as a pattern across every agent he's worked with so far (2026-05-06). The "ask first" gate inverts the failure mode without adding much friction.

**What counts as "non-trivial" (gate applies):**
- Expected work > ~5 min, or multi-step
- Produces external output (drafts, deliverables, social posts, emails, decks, contracts, designs)
- Has any ambiguity in scope, audience, format, tone, or success criteria
- Touches client-facing systems
- Multiple plausible approaches exist and the task brief doesn't pin one

**Exempt (proceed without gate):**
- Pure lookups ("what's X?", "where does Y live?") — answer directly
- Single-line edits or settings changes with an unambiguous instruction
- Continuation of a plan already confirmed earlier in the same session
- Read-only investigation that fits in 1–2 tool calls
- Tasks routed via cron / autonomous queue where the brief is already specific (those have their own brief at create-time)

**How to apply:**
1. **Wiki search first** (per [[feedback_search_wiki_first]]) — many "questions" are already answered. Don't ask what the wiki tells you.
2. After the search, if any *direction-level* uncertainty remains, surface it as a question. Even if the task seems clear, ask 1 question about the most ambiguous dimension — that single question catches most wrong-direction starts.
3. Questions must be **specific and answerable in one line each.** Prefer multiple-choice or yes/no over open-ended.
   - Good: "Audience for this deck — investors, partners, or internal team?"
   - Good: "Should I match the tone of last week's BSC post or go more formal?"
   - Bad: "How should I approach this?"
   - Bad: "What do you want me to do?"
4. After confirmation, execute without re-asking on resolved dimensions. The gate is one-shot, not a loop.
5. **Don't pad the question batch.** 1 sharp question beats 3 weak ones. If you genuinely have nothing to ask after wiki search, say so explicitly ("I'm clear on scope; proceeding") and proceed — but the bar for that is high.

**Interaction with other rules:**
- [[feedback_search_wiki_first]] runs *before* this gate. Wiki first, then ask only what the wiki couldn't answer.
- [[feedback_must_ask_escalation]] is the *mid-run* escalation protocol when an agent hits a MUST-ASK boundary after work has started. This rule is about *up-front* alignment before work starts. Both apply.
- [[feedback_critical_vs_mundane]] still governs publish/send approval — this gate is about *direction*, not *publication*.

**Where this rule is also enforced:**
- `CLAUDE.md` § "Plan-Confirm-Execute"
- Every agent definition in `agents/*.md`
- This memory entry (auto-loaded at session start)
