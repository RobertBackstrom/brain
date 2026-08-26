---
name: Re-verify ticket numbers after rename
description: When renaming a ticket to dodge a number collision, re-list the followups directory immediately before the rename — don't trust pre-rename "next free" math
type: feedback
originSessionId: 67489293-65af-41fb-b260-382cb916a362
---
After renaming a ticket to dodge a number collision, re-list the followups directory to confirm the new number is actually free. Don't trust "next free" math from before the rename.

**Why:** Multiple sessions create tickets simultaneously now (parallel Claude sessions, scheduled agents, the 4am sweep). The gap between "list next free" and "write file" is a race window where collisions get re-introduced. Hit during db-112 file-rename on 2026-05-06: the listing said next free was db-110, but db-110 (Bibbi/Wix) had been created in a parallel session, AND db-111 was also taken (BADASS Jira invite). Cost was one extra rename round-trip.

**How to apply:** `ls assistant/followups/ | grep '^db-1[0-9][0-9]' | sort -u | tail` immediately before each create or rename, not in the planning step. Same applies for any other prefix (gen-, eli-, sec-, etc.). When two collisions in a row happen, suspect a parallel session is also creating tickets and consider waiting / sanity-checking once more before the next attempt.
