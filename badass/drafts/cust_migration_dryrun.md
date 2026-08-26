# CUST Migration — Dry-Run Plan (Phase 1 step e)

**Status:** EXECUTED 2026-05-22. Migration complete - 731 issues in CUST, 5 source projects archived (E12026/F1/BMS/PFL/OR). See §8 acceptance for the final state, and the action items in the closing log. SJ NOT archived - SJ-67 leftover pending decision.
**Prepared:** 2026-05-21. Decision: full migration ASAP (investor timeline is time-sensitive).

---

## 1. Goal

Consolidate all live customisation work into the CUST project so the Portfolio Board (plan 34) has clean, consistently-structured data to draw an investor-grade timeline from. This is the data-hygiene fix Nancy flagged.

## 2. Scope + volume

| Source project | Move | Issues | Then |
|---|---|---|---|
| E12026 (E1 Series) | **All** issues | 625 (271 open, 354 done, 314 sub-tasks) | Archive E12026 |
| SJ (Show Jumping) | Open only | 1 | Archive SJ |
| F1 (F1 VR) | Open only | 18 | Archive F1 |
| BMS (Blackbook) | Open only | 19 | Archive BMS |
| PFL | Nothing | — | Archive PFL (4 stale open, last touch Dec 2025) |
| OR (Ocean Race) | Nothing | — | Archive OR (0 open) |

**Total to move: 663 issues.** E12026 moves whole (history included — the investor timeline needs completed work visible). SJ/F1/BMS move open work only; their done history stays in the archived project.

## 3. Mechanism — why it's a UI operation

Jira's REST API has **no clean cross-project move** endpoint. The supported path is the **bulk-move wizard** (Issues → Bulk change → Move). It preserves history, comments, attachments, epic/sub-task links, and **re-keys** issues (E12026-542 → CUST-NNN).

**Disruption mitigation — the key reassurance:** Jira keeps the **old key as a permanent redirect**. Any existing link or bookmark to `E12026-542` will auto-resolve to the new CUST key after the move. So the team's existing links keep working — the move is far less disruptive than "every key changes" sounds.

**Who drives it:** Robert runs the wizard (locked 2026-05-21). It's UI-only. I prepare the issue lists + status map, and run the full post-move field/label pass via API.

## 4. Epic → CUST mapping (38 epics)

Every E12026 epic → Component **E1 Series** (client) + a Type component + Location + Fix Version. Children inherit their epic's Location/Type.

| Epic | Summary | Type Component | Location | Fix Version |
|---|---|---|---|---|
| E12026-1 | Agreed Deliverables | (none) | Jeddah | E1 2025 S2 |
| E12026-4 | Showcase Activation | (none) | Jeddah | E1 2025 S2 |
| E12026-102 | Environment Broadcast | Environment Production | Jeddah | E1 2025 S2 |
| E12026-103 | E12026-Livery | AR Live Broadcast | Jeddah | E1 2025 S2 |
| E12026-199 | AR Broadcast | AR Live Broadcast | Como | E1 2026 S3 |
| E12026-207 | VR Broadcast | VR Live Broadcast | Como | E1 2026 S3 |
| E12026-208 | Environment Broadcast | Environment Production | Como | E1 2026 S3 |
| E12026-209 | AR app V0.2.0 | AR App | Como | E1 2026 S3 |
| E12026-210 | AR app V0.3.0 | AR App | Como | E1 2026 S3 |
| E12026-211 | Arcade Game | Steam-Console | Como | E1 2026 S3 |
| E12026-212 | Live GP | AR Live Broadcast | Como | E1 2026 S3 |
| E12026-213 | Fortnite | UEFN | Como | E1 2026 S3 |
| E12026-259 | Graphics | AR Live Broadcast | Como | E1 2026 S3 |
| E12026-305 | Course Explainers | Course Explainers | Como | E1 2026 S3 |
| E12026-416 | E1 Production | (none) | Como | E1 2026 S3 |
| E12026-279 | AR app V0.2.1 | AR App | Dubrovnik | E1 2026 S3 |
| E12026-312 | AR app V0.3.0 (Dub) | AR App | Dubrovnik | E1 2026 S3 |
| E12026-324 | Vision Pro app V0.1.0 (Dub) | XR Headset | Dubrovnik | E1 2026 S3 |
| E12026-396 | Course Explainers | Course Explainers | Dubrovnik | E1 2026 S3 |
| E12026-542 | AR Broadcast Setup - Dubrovnik | AR Live Broadcast | Dubrovnik | E1 2026 S3 |
| E12026-657 | VR Broadcast - Dubrovnik | VR Live Broadcast | Dubrovnik | E1 2026 S3 |
| E12026-677 | Environment Dubrovnik | Environment Production | Dubrovnik | E1 2026 S3 |
| E12026-682 | Gaming Dubrovnik | Steam-Console | Dubrovnik | E1 2026 S3 |
| E12026-327 | AR app V0.2.2 | AR App | Monaco | E1 2026 S3 |
| E12026-332 | AR app V0.3.0 (Mon) | AR App | Monaco | E1 2026 S3 |
| E12026-335 | Vision Pro app V0.1.0 (Mon) | XR Headset | Monaco | E1 2026 S3 |
| E12026-337 | AR app V0.2.4 | AR App | Lagos | E1 2026 S3 |
| E12026-342 | Vision Pro app V0.1.0 (Lag) | XR Headset | Lagos | E1 2026 S3 |
| E12026-344 | AR app V0.2.3 | AR App | TBC | E1 2026 S3 |
| E12026-349 | AR app V0.3.0 (TBC) | AR App | TBC | E1 2026 S3 |
| E12026-351 | Vision Pro app V0.1.0 (TBC) | XR Headset | TBC | E1 2026 S3 |
| E12026-353 | AR App V0.2.4 | AR App | Miami | E1 2026 S3 |
| E12026-358 | Vision Pro app V0.1.0 (Mia) | XR Headset | Miami | E1 2026 S3 |
| E12026-361 | AR app V0.2.5 | AR App | Bahamas | E1 2026 S3 |
| E12026-185 | Draft 2 | Format Explainer | (none) | E1 2026 S3 |
| E12026-186 | Draft 1 | Format Explainer | (none) | E1 2026 S3 |
| E12026-421 | Draft 3 | Format Explainer | (none) | E1 2026 S3 |

SJ open work → Component **Show Jumping** · F1 open → **F1 VR** · BMS open → **BMS**. Location/Fix Version left blank for these (no E1 season).

**Three untyped epics - confirmed 2026-05-21.** E12026-1, -4 ("Agreed Deliverables" / "Showcase Activation") and -416 ("E1 Production") are Done coordination epics. Mapped to Component E1 Series only, no Type. Robert confirmed: keep as-is.

## 5. Label normalisation (during/after move)

| Old label | Action |
|---|---|
| `como` (58 items) | Becomes Location = **Como** |
| `dubrovnik` lowercase (1 item, E12026-657) | Becomes Location = **Dubrovnik** |
| `Dubrovnik`, `Monaco`, `Lagos`, `Miami`, `Bahamas`, `Jeddah`, `TBC` | Become the matching Location value |
| `Formatexplainer` | Drop — replaced by Component = Format Explainer |
| `racebird` (4 items) | Keep as a plain label (it's a boat-type tag, not a location) |

Location is a controlled field; labels stop being load-bearing after the move.

## 6. Execution sequence

1. **Pre-flight:** pilot test data CUST-63..67 deleted (done 2026-05-21). Post the team heads-up (§9). Confirm no one is mid-bulk-edit on E12026.
2. **Migrate E12026 → CUST** via bulk-move wizard. Move only - project + issue type (1:1) + status map (§7.4). No components set in the wizard; I stamp all components via API after. ~625 issues, wizard sub-batches by issue type.
3. **Migrate SJ / F1 / BMS open issues** → CUST, 3 small wizard runs (1 + 18 + 19), same move-only approach.
4. **Post-move API pass (me):** stamp Client component + per-epic Type component + Location + Fix Version across the moved trees; normalise labels; orphan sweep.
5. **Add CUST to Plan 34** ("Portfolio Board") as an issue source; remove the now-empty E12026 source.
6. **Archive** E12026, SJ, F1, BMS, PFL, OR (read-only; history preserved).
7. **Verify** (§8).

## 7. Risks + blockers

1. **Issue-level security** — E12026-403/404/405/406 (Course Explainers sub-tasks) returned 403/404 in the May sweep. They may resist the move. Nancy (admin) relaxes the security level or moves them manually. Verify at execution.
2. **Orphan issues** — top-level Tasks/Stories with no epic won't inherit a Location/Type. The post-move API pass includes an orphan sweep (JQL `project = CUST AND parent is EMPTY AND issuetype != Epic`) to tag them or flag for manual review.
3. **In-flight Dubrovnik work** — re-keying mid-prep. Mitigated by the old-key redirect (§3) + the team heads-up. Pick a low-activity window (evening / weekend).
4. **Status mapping** - resolved 2026-05-21 from live counts. E12026 has 7 statuses, only 5 carry issues: To Do (230), In Progress (37), In Review (2), Testing (2), Done (354). Blocked / Blocked by are empty. CUST workflow = To Do / In Progress / Done. Map: To Do→To Do, In Progress→In Progress, In Review→In Progress, Testing→In Progress, Done→Done. Only 4 issues change category, all correctly. No CUST workflow change needed.

## 8. Acceptance checks (post-migration)

- CUST issue count ≈ 663 moved + the pre-migration scaffold (~66 template + type-Epic issues, after the CUST-63..67 pilot deletion).
- E12026 issue count = 0; E12026/SJ/F1/BMS/PFL/OR archived.
- Spot-check 5 epics: correct Component(s), Location, Fix Version; children present; sub-task parentage intact.
- Old key E12026-542 redirects to its new CUST key.
- Plan 34 shows CUST as a source and renders the customisation work.
- The 3 CUST boards (All / Per-Client / Per-Location) populate.

## 9. Team heads-up (draft — Teams, post T-1 day)

> Quick heads-up: today, Fri 22 May, we're consolidating the customisation Jira projects into one new project, **CUST**. Your E12026 tickets will move there and get new keys (E12026-542 becomes CUST-something). Old links still work - Jira auto-redirects them - so nothing breaks, but the project you'll work in is now "BADASS Customisation" (CUST). Boards and filters are already set up. Ping me with anything that looks off afterwards.

## 10. Rollback

Bulk-move is reversible by moving issues back, but messy at 663-issue scale. Mitigation is prevention: the post-move verification (§8) runs immediately; any wrong field values are fixed forward via API (cheap). The move itself (project + keys) would only be reversed in a genuine disaster — not expected.

---

## Decisions locked (2026-05-21)

1. **Scope** - full migration. All 625 E12026 (incl. done history) + 38 open SJ/F1/BMS = 663.
2. **Driver** - Robert runs the wizard. PM preps the lists + status map and runs the post-move API pass.
3. **Timing** - migration runs **today, Fri 22 May** (Robert + Nancy brought it forward from the weekend, to leave the weekend free for fixes before Monday). Team heads-up was due T-1, Thu 21 May.
4. **Untyped epics + heads-up** - approved as drafted (§4, §9).
5. **Blocked status** - not added. Blocked is empty in E12026, nothing to migrate; status map (§7.4) is clean without it.

## Migration run sheet (Robert)

**Pre-flight:** the team heads-up (§9) was due Thu 21 May (T-1). If it has not gone out, post it in Teams now, before the wizard runs. Pilot data CUST-63..67 already deleted.

**Today, Fri 22 May - four wizard runs.** An evening run keeps overlap with active editing lowest. Each: Issue Navigator, paste the JQL, select all, ••• → Bulk change → Move.

| Run | JQL | Count | Target |
|---|---|---|---|
| 1 | `project = E12026` | 625 | CUST |
| 2 | `project = SJ AND statusCategory != Done` | 1 | CUST |
| 3 | `project = F1 AND statusCategory != Done` | 18 | CUST |
| 4 | `project = BMS AND statusCategory != Done` | 19 | CUST |

In every run:
- **Issue type:** map 1:1 (Epic→Epic, Story→Story, Task→Task, Sub-task→Sub-task, Bug→Bug).
- **Status:** To Do→To Do, In Progress→In Progress, In Review→In Progress, Testing→In Progress, Done→Done.
- **Components / fields:** leave blank. Don't set anything in the wizard - PM stamps all components, Location and Fix Version via API afterwards. If the wizard forces a required field, pick the lowest-impact value and tell PM.
- **Sub-tasks:** keep as sub-tasks; the wizard preserves parentage.

Run 1 is large - the wizard processes it in its own sub-batches by issue type, so allow time.

**After the four runs, hand back to PM:** API field-stamping pass (§6.4), add CUST to Plan 34, archive the six old projects, run the §8 verification.
