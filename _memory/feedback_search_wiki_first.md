---
name: Search the wiki before asking Robert
description: Default reflex — query the RAG wiki before escalating any non-trivial question to Robert. Top lever for reducing his interrupt load.
type: feedback
originSessionId: 164e468c-a421-49c5-932a-cfc6fcd7dadf
---
Before asking Robert any non-trivial question, query the RAG knowledge index.

**Why:** Robert built the wiki (Death Board, 2026-04-25/26) explicitly to reduce repeat questions. Skills, memory, agent learnings, followups, Gmail and GDrive are all indexed (Phase 3 shipped — `rag-external-indexer.js` runs on cron). Most "what's the convention for X" / "where does Y live" / "did we do Z before" questions are already answered in the corpus. Asking Robert for those answers wastes his time and signals that the agent didn't try.

**How to apply:**

1. **Before any question to Robert**, call `mcp__rag__rag_search` with `rerank=true` on the question phrasing (or the relevant keywords). HTTP fallback: `https://board.runatyr.games/api/wiki/search?q=...&rerank=1`.
2. Filter by `source` (skills/memory/agents/followups) or `project` (slug) when scope is obvious.
3. **Decision rule:**
   - Top hit relevance ≥ 0.7 *and* unambiguously answers → apply it without asking.
   - Empty results, contradictory results, or shallow snippets → ask Robert. After he answers, **write the answer back as a skill or feedback memory** so the next agent doesn't re-ask.
4. **Same flow before duplicating work** — search first to see if the work is already done or cached. The "tried X, didn't work because Z" pattern is exactly what the wiki is supposed to prevent rerunning.
5. **Don't blindly trust** — a memory that names a specific function/flag is a claim that it existed at write time. If recommending action, verify the file/flag still exists (per `Before recommending from memory` in the auto-memory contract).

**Where this rule is also enforced:**
- `CLAUDE.md` § "Search the wiki before asking Robert"
- Every agent definition in `agents/*.md` (admin, analytics, bizdev, content_editor, devops, gamedev, index, pm, ui)
- This memory entry (auto-loaded at session start)

**Compounding effect:** every learning written once becomes available to every future session indefinitely. Without the wiki, knowledge survived ~10-20 conversations. With it, year-old context is one query away.

**See also (domain-specific instances of "search first"):**
- [feedback_check_before_creating](feedback_check_before_creating.md) — search existing followups before creating a new one
- [feedback_check_czp_drive_first](feedback_check_czp_drive_first.md) — search CZP Drive for trackers/docs before asking where things live
