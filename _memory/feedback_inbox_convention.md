---
name: Inbox = unacted upon
description: Emails in Gmail inbox are considered not acted upon; archive after acting. Triage = `in:inbox`. Info lookup = no scope. 2026-05-18 added auto-archive filter spec for high-volume noise.
type: feedback
originSessionId: 356fd578-f80d-48e9-b2d6-8217031810b5
---
If an email is in the inbox, it has NOT been acted upon. Once acted upon (replied, forwarded, ticket created), it gets archived.

**Why:** Robert needs a clean, reliable signal for what still needs attention. Read/unread is unreliable. Inbox presence is binary and trustworthy.

**How to apply:**
- **Triage scan** ("what needs Robert's attention"): `in:inbox`
- **Info retrieval** ("did we discuss X with Y"): omit `in:inbox` - search all mail. Auto-archived ≠ deleted; archived items are findable.
- After creating a draft reply or DB ticket, archive it (remove INBOX label). Daily briefing lists "Ready to Archive" for trigger-acted emails.

**2026-05-18 inbox slimming (inbox: 3000+ → 808):** Filter spec at `assistant/gmail-filters-spec.json` covers 16 durable filters. DevOps applies via API after re-auth (see db-154). Buckets:

- **Skip-inbox (keep labeled/findable):** PlayStation `noreply@publish`, PS5/PS4 DevNet, Azure Daily Title Reports, Atlassian digests + invites, Aurora Punks Google Groups digests (hello/catchall/finance/qa/arkisland), CurseForge/Lurkit/Trello/GitHub notifications
- **Trash-on-arrival:** ONSEC iGaming, Pinterest, FB friendupdates, Lenovo CX; Swedish retail marketing (Elite/Adlibris/Office Depot/Swappie/Gofrendly/Studiefrämjandet); newsletters (MS Learn/Google Cloud/Konvoy/Liftoff/IndieGameBusiness/IGDA/AdMob/Kochava); event drips (Tandem/Hivemind/Eventbrite/Courage/DevGAMM/gamescom marketing/PG Connects/Nordic Game marketing); SaaS onboarding (DocHub/n8n/Voyage/Eqvista/Notion); Swedish finance cold outreach (Eurofinans/Creddo/Kompar); Meta consumer marketing
- **KEEP in inbox (Robert's call):** Nintendo Developer Portal sales reports, Sony PO/statements (`NO-REPLY-BI@sony.com`), Gemini/Read AI/Otter/Fyxer meeting summaries, Apple Developer admin + Microsoft Royalties

**PlayStation promo special:** auto-archived BUT new ones trigger Plane issue creation via watcher (db-154).

**Don't propose archiving** messages that match a Track B auto-archive filter - they're handled.

**2026-05-29 overhaul (db-186) - the rules now ENFORCE themselves.** The May filters were never applied as native Gmail filters (blocked on `gmail.settings.basic` re-auth, db-154), so the inbox crept back to 1179. New architecture, single source of truth at `assistant/triage-policy.json`, drives three consumers:
- `gmail-sweep.js` - archives/trashes noise buckets continuously via the `gmail.modify` scope (no re-auth needed). Run daily by `cron/daily-inbox-triage.sh` at 06:30 UTC.
- `gmail-newsletter-digest.js` - Substack + HTMAG-post newsletters (digest:true) are read, summarized with links, mailed to Robert as ONE digest, then archived. Not silently archived.
- `server.js checkEmails()` - reads `routine_ignore_senders` / `routine_skip_subjects` from the policy; scans `in:inbox` only.

**Corrections baked into the policy (don't undo):** `info@gamesindustry.network` = Nordic Game/MeetToMatch matchmaking, NOT a newsletter -> keep_in_inbox. Luma + MeetToMatch kept in inbox (own-event RSVPs). HTMAG digest excludes `subject:"festival alert"` (those are evt tickets). Gemini meeting notes actually arrive from `gemini-notes@google.com`. To change what's noise, edit triage-policy.json (one place), never re-hard-code in server.js.
