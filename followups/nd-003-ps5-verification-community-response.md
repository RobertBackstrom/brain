---
project: nd
status: open
priority: high
updated: 2026-09-07
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

- **Linkdu47** is Robert's to answer. Dedicated server, 13 months waiting, was personally promised a fix
  in June. **His problem is NOT fixed** by the 09-04 update, which covers single-player only.
- **Elias owns 11 players** plus Package Thief's obelisk question. Handover doc:
  https://docs.google.com/document/d/1ZREgLq2zzS8JzsjUiuo6oaLE63NCeaNmNl2X6J2a4Cs/edit
- **Dedicated-server PS5 (ND-13/ND-14) has no date.** Robert asked Elias for one; it is the honest
  answer Group B needs.
- **ND-12** (spells deal damage and play sound but render no visuals on PS5) — unknown whether the
  09-04 optimization pass touched it. Linkdu47 will ask.
- **CurseForge Issues tab has never been read by anyone.** Separate player-facing tracker from
  comments, not reachable from the VPS. Robert now has author access.
- **db-342** — `nd-discord-read.js` returns a silent exit-0 empty result on bad args.

### Activity

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
