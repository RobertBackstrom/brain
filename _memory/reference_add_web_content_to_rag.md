---
name: reference_add_web_content_to_rag
description: "How to add an external web URL (article, LinkedIn post) into the RAG index — no generic web source exists."
metadata: 
  node_type: memory
  type: reference
  originSessionId: a04ac643-1edf-416f-b416-0a573fa0f327
---

The RAG indexer has **no generic web-URL source** (sources are skills/memory/agents/followups/wiki/project + Gmail/GDrive/Discord). To add an external article or post to RAG:

1. **WebFetch** the URL to extract full content as markdown (follow cross-host redirects — Substack `open.substack.com` → `<pub>.substack.com`; LinkedIn may 307 to a country mirror, e.g. `pl.linkedin.com`).
2. **Save as `wiki/references/<slug>.md`** with frontmatter matching the existing convention: `title`, `source` (substack/linkedin/…), `author`, `date` (original publish; use `retrieved:` if the real date isn't reliably exposed), `url`, `tags`, optional `repo`/`publication`. Body = the extracted content, not a summary.
3. **Index it:** `node assistant/rag-indexer.js --backfill` (scoped to wiki), or just let the wiki file-watcher pick it up.

Why `wiki/references/` and not `indexContent` with an ad-hoc source: it's a **real file in a watched source**, so it survives `--reset`/re-backfill. Gmail/GDrive-style `indexContent` docs get wiped on reset and only return if their external indexer re-pulls them.

Verify with `mcp__rag__rag_search(source="wiki", rerank=true)`. Note bare `node -e` scripts against `rag.db` can't count embeddings (the `vec0`/sqlite-vec extension isn't loaded) — use the MCP search to confirm retrieval instead. See [[reference_obsidian_vault]], [[feedback_dump_og_links]].
