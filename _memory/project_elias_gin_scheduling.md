---
name: elias-gin-scheduling-for-erik
description: "GIN matchmaking calendar — Robert's GIN account proxies Erik Brattlöf's NGC 2026 meeting scheduling"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8449b814-3d97-42ac-85e6-5c62877664c2
---

Robert uses his GIN account (Games Industry Network, `gamesindustry.network`, login `robert@aurorapunks.com`) to book NGC 2026 meetings **for Erik Brattlöf** (Elias Audio), via GIN + LinkedIn. GIN availability is therefore guided by **Erik's** calendar, not Robert's.

**Erik's NGC availability** (from his "Elias NGC" Google appointment-schedule page, 30-min slots, owner Erik Brattlöf):
- Wed May 27: 12:00-15:00
- Thu May 28: 09:00-15:00 and 17:00-19:00
- Mon 25 / Tue 26 / Fri 29: none

**Done 2026-05-21:** GIN `/my-calendar` blocked to mirror this — 11 blocked slots ("Erik unavailable") covering everything outside Erik's windows (Mon/Tue/Fri full days; Wed except 12-15; Thu except 09-15 & 17-19). GIN has no native calendar sync; see [[bizdev_learnings]] for the API + the reverse-chronological-order workaround for its overlap-check bug. GIN login tracked in `secrets_registry.md` as `gin.login`.

**VPS watcher first real run 2026-05-26 (NGC opens today):** `assistant/gin-erik-watcher.js` was already password-armed; ran `--once` against 4 confirmed GIN meetings. Booked Chris James (Wed 14:00) + Randall Ryan (Thu 10:00) successfully. Victor Hime (Wed 12:00) failed three attempts with HTTP 400 from Google's BookSlot API — rate-limit / anti-bot after the 2 rapid bookings; Robert to book manually from his own browser. Adam Ritchie (Wed 15:00) failed because the slot is outside Erik's published Wed window (page ends 14:30); needs GIN reschedule or Erik widening availability. Systemd timer (`gin-erik-watcher.timer`) is still **disabled** — activation recommended for the rest of NGC week (10-min cadence avoids the rate-limit burst). Auto-books + Discord-notifies; on failure, Discord-alerts only (no retry; clear state.json entry to re-arm). Activation runbook: `assistant/gin-erik-watcher.ACTIVATION.md`. See `umbrella/elias_bizdev/output_log.md` (2026-05-26 entry) for the per-meeting result, [[feedback_devops_tooling]], [[project_elias_ngc_mixer]].
