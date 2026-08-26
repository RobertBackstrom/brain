---
name: feedback_read_ticket_activity_top
description: "Read a followup ticket's Activity from the TOP (newest-first), never via tail."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2696e915-aed2-4d9b-91bd-9c4365a7f6b5
---

Followup tickets prepend Activity newest-first, so reading them with `tail` returns the **stale bottom** of the file (old action plans, closed 4am-sweep notes) and hides the current state.

**Why:** on [[project_rlr_ip_dispute]]-adjacent work (apb-026, Steam APDS→CZP transfer) an agent read the ticket via `tail`, missed the 2026-07-14 entry documenting the zero-app onboarding gate and the 2026-07-15 SDA-verification entry, and spent an afternoon re-deriving both via live Playwright — the exact rediscovery the ticket exists to prevent.

**How to apply:** open the file properly or `sed -n '1,60p'`. If a ticket is long, search for the newest date (`grep -n "^- \[2026"`), don't tail. The Activity block directly under the frontmatter is authoritative; everything below it may be superseded. Applies to every agent on every followup.
