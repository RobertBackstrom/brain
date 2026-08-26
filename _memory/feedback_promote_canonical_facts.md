---
name: feedback_promote_canonical_facts
description: "Canonical cross-agent facts (ownership, rev-share, Drive vault location, deal terms) belong in shared memory, not one agent's learnings."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c08d30a4-cbb2-44de-9772-ad5040f43147
---

When an agent (esp. CorpBot) learns a **canonical** fact — ownership splits, rev-share terms, where a project's master vault/files live on Drive, deal/contract terms, cap-table facts — that fact must live where **every** agent looks with authority: the project's memory file (project-scoped) or a `reference` memory (global). It must NOT stay buried in `agents/memory/<name>_learnings.md`, which is semantically that one agent's loggbok.

**Why:** RAG indexes agent learnings too, so a buried canonical fact is technically searchable — but it reads as "one agent's note," not a shared truth, and agents don't treat it as authoritative. The real lever is **placement**, not indexing.

**How to apply:**
1. Promote inline when you learn it — don't wait for `/close`. Project-scoped → project memory (+ MEMORY.md pointer). Global → a `reference` memory. Leave a `[[pointer]]` in the agent's learnings back to the canonical home.
2. **No manual RAG step.** `memory/`, `skills/`, `agents/` are live-watched (rag-config.js `WATCHED` → chokidar in `deathboard.service`, ~30s debounce), so anything written there is RAG-searchable by every agent within half a minute. Only `--backfill` if the watcher is confirmed down.
3. `/close` §3 now has a promotion sweep as the backstop for anything missed inline.

Related: [[feedback_memory_write_protocol]], [[feedback_search_wiki_first]].
