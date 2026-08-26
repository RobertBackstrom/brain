---
name: feedback-stale-review-include-links
description: "When reviewing stale tickets that reference an original post/URL, always include that link in the stale review message so Robert can check it himself"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 880f743b-74d3-4232-a401-de94a277cb29
---

When a stale Death Board ticket references an original post, article, or external URL, always include that link in the stale review verdict/message.

**Why:** Robert wants to quickly glance at the source material to decide relevance himself, rather than needing to open the ticket separately.

**How to apply:** During stale ticket reviews, check for any URLs in the ticket body (LinkedIn posts, articles, etc.) and embed them in the `reason` field of the JSON verdict. Applies to all stale review passes.
