---
name: Check Gemini meeting notes before reporting status
description: Any agent on a project with recurring meetings — search Gmail + Drive for Gemini-generated summaries before reporting state. Local files lag behind.
type: feedback
originSessionId: d4cc9839-cdbc-428e-959c-d7d145f95ec4
---
On any project with recurring meetings (WMY, BADASS, K2C, Elias, etc.), the latest meeting state often lives in Gemini-generated summary emails sent to robert@aurorapunks.com after each call, and the matching Gemini-Notes Google Doc on Drive. Local `assistant/meetings/` and `assistant/followups/` folders may lag behind. Applies to any agent (PM, BizDev, etc.) producing a status briefing or action-item ingest.

**Why:** Robert pointed out (2026-04-14, WMY recap) that I claimed to have the latest meeting notes after only checking the local filesystem. Gemini emails the summary as soon as the call ends — that is the freshest source. Drive sync and local capture come later.

**How to apply:** Before producing any "where are we" / status / recap output for a project with a meeting cadence:
1. Search Gmail for `from:(meetings-noreply@google.com OR gemini) <project keywords>` covering at least the window since the last locally captured meeting note
2. Cross-reference what's in `assistant/meetings/<prefix>-*` and `assistant/followups/`
3. If new Gemini emails exist, pull them, summarize action items, and create/update follow-ups before reporting status
4. If Gmail isn't authenticated, surface that immediately rather than reporting based on stale local state
