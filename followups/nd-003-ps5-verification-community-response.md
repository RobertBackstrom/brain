---
project: nd
status: open
priority: high
updated: 2026-09-10
created: 2026-09-07
type: task
owner: Robert
---

## PS5 verification + community response

Container ticket for the Necrotic Dominion PS5 workstream: getting Robert onto a retail PS5 as a
CurseForge tester, shipping the fix, and answering the backlog of players who reported the crash.
Detailed history lives in `umbrella/necrotic_dominion/output_log.md`; defect tracking is Jira `ND`.

**State: PS5 fix SHIPPED 2026-09-04. Community response in progress.**

### Open

- **Linkdu47 was answered 2026-09-10** (see Activity), but with the Group A answer. He runs rented
  dedicated servers, so the 09-04 update does not cover him and ND-12 was not addressed. Expect a
  reply saying it still crashes; a follow-up is queued behind the ND-13/ND-14 date.
- **Elias owns 11 players** plus Package Thief's obelisk question. Handover doc:
  https://docs.google.com/document/d/1ZREgLq2zzS8JzsjUiuo6oaLE63NCeaNmNl2X6J2a4Cs/edit
- **Dedicated-server PS5 (ND-13/ND-14) still has no date, and now has a reason.** Elias, Discord
  2026-09-10 16:36: *"Kollat en del idag pa server problemet men inte hittat nagot ska se om jag kan
  fa crash logs fran dem som forsokt."* He is looking and has found nothing, so there is no date to
  give Group B yet. **He is asking for crash logs from the affected players** — those people are the
  three in Group B of the reply list, and one of them carries an untried lead (see Activity).
- **ND-12** (spells deal damage and play sound but render no visuals on PS5) — unknown whether the
  09-04 optimization pass touched it. Not covered in the 09-10 reply to Linkdu47, who raised it himself.
- **CurseForge Issues tab has never been read by anyone.** Separate player-facing tracker from
  comments, not reachable from the VPS. Robert now has author access.
- **db-342** — `nd-discord-read.js` returns a silent exit-0 empty result on bad args.

### Activity
- [2026-09-10] **PM/Claude**: Elias reported on Discord that he has spent the day on the
  dedicated-server problem without finding anything, wants crash logs from affected players, and is
  building to test the cave-spawner fixes. **The crash-log sources he is asking for are already
  compiled:** Group B of the reply list is exactly the three people who ran ND on a dedicated server
  — Linkdu47, UNASHAMED and miah1607 — each with Discord permalinks. **Untried lead worth surfacing
  before more blind investigation:** miah1607 is not on Nitrado but the ASA Server Creation Tool, the
  server dies about three quarters through boot while 15 other servers run fine, and the ASCT
  developers looked at it and suggested **an authentication problem because the server runs
  anonymous**. That is a concrete hypothesis for ND-14 that costs nothing to test. Also relevant:
  JayGrym's Xbox-works datapoint is what narrowed ND-11.

- [2026-09-10] **Robert**: Answered **Linkdu47** in #ark-bugs 07:36, as a reply on his 2025-08-04
  message, and synced with Elias separately. Closes the last name Robert was holding; all 17
  reporters have now had a reply. **Caveat to watch:** the text given was the solo/memory-crash
  answer — *"We had some memory crashes on the PS5 which was sorted in the update last weekend.
  Please have a go to see if it works."* Linkdu47 is Group B (PS5 to rented dedicated server), which
  the 09-04 update does not fix, and ND-12 was not mentioned. He will most likely test and come back
  saying it still crashes. The honest follow-up still needs the **ND-13/ND-14 dedicated-server date**
  that Elias has not delivered (mail thread `1a07c02e221f2fea`, no reply since 09-07).
- [2026-09-09] **Elias**: Answered four in #ark-bugs (fire_peacock_15979, tsonag, bones9711,
  ioniconi) plus the obelisk question in #ark-general on 09-08, and thanked JayGrym by name.

- [2026-09-07] **PM/Claude**: Session covering the whole PS5 path end to end. **Access resolved:** the
  three-week "does Robert have CurseForge access" thread was a false negative — the 2026-08-12 audit
  read an empty view on `console.curseforge.com` (CurseForge for Studios, where publishers register
  *games*), not the mod-author dashboard, which is **`authors.curseforge.com`**. `AuroraPunksBoss` was
  Owner with Cross Platform Testing already ticked the whole time. Amichai Marmor's "you both have full
  permissions" screenshot showed `davidkruse` + `DevElias` and did not render the owner row, which sent
  me down a wrong path too. **PSN link:** done via CurseForge Connected Accounts as an OAuth grant to
  `FatsharkAlouatta`; the two accounts do **not** need matching email addresses and Robert correctly did
  not change his PSN address. Robert then tested `1117983-dev` on the retail kit (confirmed working
  2026-09-04) and Elias shipped the update, announced in `#ark-announcements` 2026-09-04.
  **Community sweep:** 400 days of Discord across four ARK channels plus CurseForge comments via
  notification mail. **17 players** had reported the PS5 problem; grouped by whether the shipped fix
  actually covers them (solo = fixed, dedicated server = not). Robert answered five plus two
  update-timing questions, keeps Linkdu47, and Elias has eleven. Handover Doc created, shared writer
  with Elias, and the mail **was sent** 2026-09-07 15:28 (thread `1a07c02e221f2fea`, no reply yet).
  **Also filed:** db-342; ND-11 updated with the 2026-09-02 customer report plus four corroborating
  Discord reporters and the finding that this is PS5-specific (JayGrym had the same build running on
  Xbox); ND-28 updated and now closeable.
  **Watch:** Elias was onboarded as a Starbreeze contractor on Irons 2 in late August, which competes
  with the 45 h/mån ND commitment on top of school.
