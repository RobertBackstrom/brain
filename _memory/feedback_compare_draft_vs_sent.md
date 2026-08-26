---
name: Compare draft to sent — extract lessons
description: After Robert sends a mail you drafted, diff your draft against the sent version and capture lessons learned as memory updates.
type: feedback
originSessionId: 0574dc28-f6ee-495e-b57d-44797ca01f08
---
After creating a Gmail draft for Robert to review and send, the next time you have an opportunity, fetch the corresponding sent message and diff it against your original draft text. Capture any patterns from Robert's edits as memory updates (writing-voice tightening, tone shifts, structural reorganisations, deletions of specific framings).

**Why:** Robert reviews and edits drafts before sending. His edits encode preferences that aren't always articulated explicitly — what to keep, cut, soften, restructure. Treating each draft → sent diff as a free feedback signal accelerates voice/format/tone calibration without him having to spell out the rules.

**How to apply:**

1. **When you push a Gmail draft**, log the draftId + threadId + Drive-saved draft path in the session's activity log so it's recoverable next session.
2. **At the start of subsequent sessions** (or when explicitly asked, or before drafting another mail to the same correspondent), fetch the most recent sent message on the same thread via `mcp__gmail__gmail_thread` or `gmail_search`. Compare to your saved draft.
3. **Look for patterns**: cuts (what got removed and why), additions (what Robert added), rewrites (tone/voice/framing changes), structural moves (sections reordered, TL;DR added/changed, lists shortened), salutation/sign-off changes, recipient changes (cc/bcc adjustments).
4. **Write findings back to memory**: if the change is generalisable (applies to similar mails in future), add to `writing_voice_robert.md` or a new feedback memory. If it's contact-specific (e.g., how Robert addresses a particular CEO), add to `user_contact_relationships.md`. If it's project-specific framing, add to the project memory.
5. **Don't be precious about your draft** — Robert's edits are the signal, not noise.
6. **Skip** if Robert sent verbatim (no edits = current draft pattern works, no learning needed).

Source project: BADASS (2026-05-11). Trigger: drafted long merged-file delivery mail to Rosy Lokhorst; Robert agreed practice should apply going forward.
