---
name: Read full Gmail threads before reporting status
description: When checking email state, fetch full thread bodies not just search snippets, and broaden subject filters beyond the obvious keywords
type: feedback
originSessionId: 703a6ef7-dbb3-475f-b1c8-85b3d7fd8636
---
When reporting status on anything that lives in email (contract state, client replies, outstanding asks), do not stop at `gmail_search` snippets. Pull the full thread via `gmail_thread` for every thread that looks relevant. Snippets truncate at ~150 chars and hide the latest reply, attachments, and CC'd parties.

Also broaden subject filters. Contract traffic often rides on threads with non-obvious subjects (e.g. the K2C RF master contract came on a thread titled "Small tweak to the payment schedule — new MS3"). If a narrow search returns nothing, widen to `newer_than:Nd` with counterparty domains and no subject filter before concluding "nothing came in."

**Why:** 2026-04-22 on K2C — Robert asked for a CorpBot status report. I reported Tim's draft as "unreplied" and RF master as "no word from Niclas in 8 days." Both were wrong: Robert's Apr 21 reply to Tim accepting 122,222 SEK was in the thread I had already seen, and the updated RF contract had been attached by Niclas on Apr 21 on a payment-schedule-titled thread. I stopped at snippets and a narrow subject filter. Robert called it out, rightly.

**How to apply:**
- Any status report that touches email: list the relevant threads from search, then `gmail_thread` each one and read the last two messages at minimum.
- Before declaring "no email from X in N days," re-run the search with just `from:<domain> newer_than:Nd` (no subject filter) to catch threads that ride on unrelated subjects.
- When attachments are referenced ("See attached"), note that gmail MCP does not surface attachments — flag this explicitly in the report rather than silently missing the attached document.
