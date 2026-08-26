---
name: Gmail drafts auto-dedup on thread
description: gmail_create_draft auto-deletes prior drafts on the same threadId; opt out with allowDuplicate=true
type: feedback
originSessionId: 7cb55151-a650-4ab7-9cc9-91d2063e90dc
---
`gmail_create_draft` (assistant/mcp-gmail.js) automatically deletes any existing drafts on the same `threadId` before creating the new one. The response includes `replacedDraftIds` listing what was deleted.

**Why:** Robert flagged duplicate drafts piling up on the same thread (Paddy / Dungeon Skater had a May 14 holding reply + May 15 substantive reply both sitting in drafts, neither sent). Multi-day autonomous queues kept drafting onto the same thread without checking for prior drafts. Built 2026-05-19 as the durable fix (option 2 of three: rule / wrapper / hybrid; he picked wrapper).

**How to apply:**
- Default behavior is correct: when replying to a thread, always pass `threadId`. Old draft gets superseded, new one stands alone.
- If you genuinely need to keep multiple drafts on the same thread (rare — usually only if Robert is mid-edit on one manually), pass `allowDuplicate: true`.
- The companion tools `gmail_list_drafts` (filter by threadId) and `gmail_delete_draft` (by draftId) exist for explicit cleanup paths.
- Caveat: if Robert hand-typed a draft on a thread and an agent then drafts on the same thread, his draft will be silently replaced. If a user-edited draft is suspected, list_drafts first and inspect snippet/Date before calling create_draft.
- Caveat: stdio MCP server is spawned at session start, so behavior change applies to new sessions; in-flight session keeps old behavior until reconnect.
