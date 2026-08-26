---
name: Always check for existing tickets before creating
description: Never create new DB followup tickets without first checking if similar ones already exist
type: feedback
originSessionId: b64e1c43-3a25-48e8-bd61-d7c2c26493b9
---
Always search existing followups before creating new ones. Duplicates waste time and create confusion.

**Why:** Robert flagged this when Claude created DB feature tickets without checking first. Tickets may already exist from prior sessions or from queue processing.

**How to apply:** Before creating any new followup in assistant/followups/, grep/search existing files for similar titles, contexts, or topics. Merge activity into existing tickets rather than creating new ones.

**See also:** [feedback_search_wiki_first](feedback_search_wiki_first.md) — meta-rule; this is the followup-store instance of it.
