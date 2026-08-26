# CUST scaffold — prep findings (2026-05-19)

Read-only audit of badass-studios.atlassian.net before mutating. Purpose: feed the Phase 1 scaffold + template seeding step.

---

## 1. Location label inventory (controlled-list candidates)

Live `labels` values on E12026 issues, with counts:

| Label | Count | Disposition |
|---|---|---|
| Dubrovnik | 99+ (likely more — query capped at 100) | Canonical — keep |
| como | 58 | Normalise to **Como** at migration |
| Jeddah | 15 | Keep (legacy S2, may apply to historical) |
| Monaco | 10 | Keep |
| TBC | 9 | Keep as special-case value |
| Miami | 7 | Keep |
| Lagos | 7 | Keep |
| Bahamas | 5 | Keep |
| racebird | 4 | NOT a location — leave as ad-hoc tag |
| Formatexplainer | 2 | NOT a location — leave as ad-hoc tag |
| dubrovnik | 1 | Typo — normalise to **Dubrovnik** at migration |

**Proposed `Location` custom field option list (single-select):**
Dubrovnik · Como · Monaco · Lagos · Miami · Bahamas · Jeddah · TBC

Two normalisations needed during migration: `como` → `Como` (58 items), `dubrovnik` → `Dubrovnik` (1 item). Free-text `racebird` and `Formatexplainer` stay as labels.

---

## 2. Template Epic seeds — confirmed visible & sized

| Template | Seed Epic | Children visible | Status | Notes |
|---|---|---|---|---|
| **AR Live Broadcast** | E12026-542 "AR Broadcast Setup — Dubrovnik" | 19 Tasks (To Do) | Mature, ready as canonical | Per May 12 audit had "20 children"; 1 likely hidden by issue-level security (range E12026-543/603 area) |
| **VR Live Broadcast** | E12026-657 "VR Broadcast — Dubrovnik" | 17 Stories/Tasks | Mostly To Do, 2 In Progress | John's tree, includes Stream Deck, camera tracks, buoy/track placement, hitbox data |
| **AR App V0.2.x** | E12026-279 | 4 children (1 In Progress) | Active | Ben's. Stories: Boat Viewer, UI update, Environment, E1-vision alignment |
| **AR App V0.3.x** | E12026-312 | 1 child | Skeleton | Ben's. Only Story so far: "Manipulation UI rework" |
| **Environment Production** | E12026-677 "Environment Dubrovnik" | 4 Stories | 1 Done + 3 To Do | Marco's. Pre-prod (Done), Production, AR Production, Optimization. NB: proposal references "E12026-514" but that's a child Story, not the Epic — parent Epic is E12026-677 |
| **Course Explainers** | E12026-396 | 4 Stories (all To Do) | Ready | Jake's. Boat pathing, cinematic enhancement, lighting, render output |
| **UEFN** | E12026-213 "Fortnite" (Como) | 2 Tasks To Do, several Done | Done — last touched 19 May | Sezar marked the Epic Done today. Children: "Publish island 5 days before event", "7 edits / 7 days rule" |
| **Steam-Console game** | E12026-682 "Gaming Dubrovnik" + E12026-211 "Arcade Game" | 682 new (3 stories/tasks), 211 with content | Mixed | Sezar. 682 is the most current — created today/yesterday. 211 has finished content from Como (logic cleanup, depot migration, Como integration tasks) |

Format Explainers (E12026-185/186/421) is a separate template not in the v2 proposal — likely should be added as a 6th customisation type, OR folded into a generic Marketing/Format Asset bucket. Flag for Robert.

---

## 3. Migration mapping — E12026 Epics → (Component, Location, Template Source)

All 37 Epics, grouped by source Component / season:

### Season 2 — Jeddah (4 Epics, all Done)
- E12026-1 Agreed Deliverables
- E12026-4 Showcase Activation
- E12026-102 Environment Broadcast
- E12026-103 E12026-Livery

**Migration:** Component = E1 Series, Fix Version = "E1 2025 S2" (new), Location = Jeddah.

### Como (12 Epics — S3 first race, all Done)
- E12026-199 AR Broadcast (→ AR Live Broadcast template, Como)
- E12026-207 VR Broadcast (→ VR Live Broadcast, Como)
- E12026-208 Environment Broadcast (→ Environment Production, Como)
- E12026-209 AR app V0.2.0 (→ AR App, Como)
- E12026-210 AR app V0.3.0 (→ AR App, Como)
- E12026-211 Arcade Game (→ Steam-Console, Como)
- E12026-212 Live GP (→ ?? new template or one-off)
- E12026-213 Fortnite (→ UEFN, Como)
- E12026-259 Graphics (→ ?? new "Graphics" template or merge into AR Broadcast)
- E12026-305 Course Explainers (→ Course Explainers, Como)
- E12026-416 E1 Production (→ ?? coordination Epic, likely Live GP territory)

**Migration:** Component = E1 Series, Fix Version = "E1 2026 S3" (Como).

### Dubrovnik (8 Epics — S3 next race, 6 To Do, 2 To Do/In Progress)
- E12026-279 AR app V0.2.1 → AR App
- E12026-312 AR app V0.3.0 (Dub) → AR App
- E12026-324 Vision Pro app V0.1.0 (Dub) → AR App (Vision Pro variant — flag)
- E12026-396 Course Explainers → Course Explainers
- E12026-542 AR Broadcast Setup — Dubrovnik → AR Live Broadcast
- E12026-657 VR Broadcast — Dubrovnik → VR Live Broadcast
- E12026-677 Environment Dubrovnik → Environment Production
- E12026-682 Gaming Dubrovnik → Steam-Console

**Migration:** Component = E1 Series, Fix Version = "E1 2026 S3" (Dubrovnik), Location = Dubrovnik. All 8 are the template-engine pilot batch.

### Monaco (3 Epics — all To Do, future)
- E12026-327 AR app V0.2.2 → AR App
- E12026-332 AR app V0.3.0 (Mon) → AR App
- E12026-335 Vision Pro app V0.1.0 (Mon) → AR App (Vision Pro)

### Lagos (2), TBC (3), Miami (2), Bahamas (1) — all To Do
Pattern repeats: each location has 2-3 AR App Epics (V0.2.x + V0.3.x + Vision Pro). All migrate as Component = E1 Series with their Location field.

### Format Explainers / Race-Wide (3 Epics — Done)
- E12026-185 Draft 1
- E12026-186 Draft 2
- E12026-421 Draft 3

**Migration:** Component = E1 Series, no specific Location (or Location = "Race-wide"). New template "Format Explainer" — flag for Robert.

---

## 4. Dormant client projects — D1 decision check

D1 said: archive PFL/BMS/OR, migrate SJ + F1 open tickets. Current open-ticket reality:

| Project | Open items | Latest activity | D1 disposition | Audit note |
|---|---|---|---|---|
| **OR** (Ocean Race) | **0** | n/a | Archive | Confirmed safe — no open tickets |
| **PFL** (PFL MMA) | 4 (3 Epics To Do, 1 Sub-task In Progress) | PFL-35 last touched **2025-12-08** (5+ months stale) | Archive | Sub-task In Progress status is stale; treat as abandoned |
| **BMS** (Blackbook Motor Sports) | 19 (mostly Sub-tasks, 1 Story In Progress: BMS-94 Ben Jeffreys) | BMS-94 last touched **2026-05-04** (15 days ago) | ⚠️ **Reconsider** | Ben actually touched BMS in last 60 days. D1 assumed dormant — not true. Recommend migrate BMS as a Component (treat like SJ/F1) and ask Robert to confirm |
| **SJ** (Show Jumping / PJL) | 1 Epic (SJ-67 "3D AR Assets" To Do) | Stale | Migrate as Component | 1 Epic to absorb |
| **F1** (F1 VR) | 18 (2 Epics + tasks/sub-tasks, F1-20 In Progress) | Mixed | Migrate as Component | F1-25 "XR Project to push on Steam" may overlap with Steam-Console template — verify scope before migration |

**Flag:** D1's archive list may be wrong on BMS. Recommend asking Robert before archiving BMS.

---

## 5. Other existing site projects — out-of-scope for migration

| Key | Name | Disposition |
|---|---|---|
| BX | BADASS XR Platform | Keep — platform tracking, not customisation |
| PE | Platform Enhancement | Keep — platform tracking |
| OPS | Badass Internal Ops | Keep — internal ops (Innovate UK, Dell, partnerships) |
| MO | Master Overview | Keep — product discovery |
| P4TEST | Perforce Test | Likely archivable; ask Nancy |

---

## 6. Pre-flight checklist before scaffold

Items to confirm with Robert before mutating:

1. **BMS disposition** — D1 said archive, but BMS-94 was touched 15 days ago. Migrate or archive?
2. **F1-25 / Steam-Console overlap** — F1-25 "XR Project to push on Steam" feels like the same scope the Steam-Console template will own. Migrate F1-25 into CUST as Component=F1 + Template Source=Steam-Console, or treat F1's Steam stuff as separate?
3. **Format Explainer template** — proposal v2 lists 5 templates (AR Live BC, VR Live BC, AR App, Course Explainer, UEFN, Steam-Console = actually 6). The 3 "Draft" Epics (185/186/421) for race-wide format videos don't fit any. Add as 7th template "Format Explainer", or treat as one-off Stories under a "Race-wide" Location?
4. **Graphics + Live GP** — E12026-212 "Live GP" and E12026-259 "Graphics" don't map cleanly to the 6 templates. New templates, or fold into AR Live Broadcast / Environment Production?
5. **Vision Pro variant of AR App** — every location has a "Vision Pro app V0.1.0" Epic alongside V0.2.x / V0.3.x. Treat as part of AR App template (Stories tagged "Vision Pro"), or split into its own template?
6. **Project type taxonomy as Component vs custom field** — proposal says either-or. Recommend Component (so the JQL `component = "AR Live Broadcast"` is canonical). Alternative is `customfield_Type` single-select for stricter validation.

---

## 7. Scaffold plan (step b) — proposed execution order

If Robert OKs the questions above, execution order:

1. Create CUST project (Company-managed Software, classic).
2. Create Components: E1 Series · Show Jumping · F1 VR · BMS (?) · Blackbook · TEMPLATES · AR Live Broadcast · VR Live Broadcast · AR App · Environment Production · Course Explainers · UEFN · Steam-Console — total 13 (or fewer if project-type is custom field).
3. Create Fix Versions: "E1 2025 S2" (legacy), "E1 2026 S3" (current). Pre-create Q4 2026 / 2027 placeholder once Rosy has the calendar.
4. Create custom fields:
   - `Location` (single-select): Dubrovnik · Como · Monaco · Lagos · Miami · Bahamas · Jeddah · TBC
   - `T-shirt Size` (single-select): XS · S · M · L · XL
   - `Template Source` (single-select): AR Live Broadcast · VR Live Broadcast · AR App · Environment Production · Course Explainers · UEFN · Steam-Console · Format Explainer
5. Set field-context to attach these custom fields to CUST screens (story + epic + task screens minimum).
6. Create 3 boards: "CUST — All", "CUST — Per-Client", "CUST — Per-Location".

Then pause for Robert sign-off before step (c) template Epic seeding.

---

## Sources
- Live queries against badass-studios.atlassian.net via Rovo OAuth, 2026-05-19.
- Cross-checked against `badass/drafts/cust_jira_proposal_v2.md` and `badass/activity_log.md` 2026-05-12/13 entries.
