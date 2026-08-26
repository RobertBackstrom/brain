---
name: briefing-dedup-recurring-vendor
description: "Daily briefing's thread-ID ticket dedup misses recurring vendor reminders that land on a new Gmail thread each send — check by subject/invoice number too, and honor prior close_reason"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: df3f13ab-13ac-483c-a3c3-52baeaf1ec01
---

The daily briefing's Gate 2 dedup (`grep email_thread_id: <threadId> assistant/followups/`) only catches a duplicate ticket if the follow-up email replies on the same Gmail thread. Recurring vendor notices (e.g. Websupport unpaid-invoice reminders) often arrive as a brand-new thread each time rather than a reply, so the thread-ID check misses them even though it's the same underlying invoice/issue.

**Why:** On 2026-08-18 the briefing created czp-025 for Websupport invoice 62600008098149 — the exact invoice already ticketed as czp-024 on 2026-08-17, which Robert had explicitly dismissed as `not_relevant` via Discord. The reminder email came in on a new threadId, so the dedup grep found nothing. Re-raising a ticket Robert already closed as not worth his time is the same trust cost as re-raising an already-answered email thread ([[feedback_gmail_read_full_threads]] documents the parallel failure mode for Gate 1).

**How to apply:**
- Before creating a ticket from an automated/vendor email (invoices, renewal notices, verification digests), also grep `assistant/followups/` for a distinctive token from the subject/body (invoice number, order ID, domain name) — not just the threadId.
- If a match is found and its `status: closed` with `close_reason: not_relevant` (or similar dismissal), do not recreate it — note the existing ticket ID under FYI instead, and mention the prior dismissal so Robert isn't asked to re-decide something he already decided.
- If a match is found and still open, use the existing ticket ID rather than creating a new one, same as thread-ID dedup.
