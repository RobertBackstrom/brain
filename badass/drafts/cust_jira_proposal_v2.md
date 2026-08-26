# BADASS Customisation Jira, Structural Proposal v2

**From:** Robert (Aurora Punks PM), Nancy Imado (Chief of Staff / PM)
**To:** Rosemary Lokhorst, Alex Sangwin-Skillen
**Status:** DRAFT, design review
**AP effort:** under 10 hours total across both phases.

---

## TL;DR

Two phases.

**Phase 1, Customisation Jira Restructure.** Six per-client Jira projects (E12026, SJ, F1, OR, PFL, BMS) collapse into one new `CUST` project. Client becomes a Component, season a Fix Version, race/event an Epic, location a controlled-list custom field. Recurring deliverables (AR Broadcast, VR Broadcast, AR App, Course Explainers) become template Epics that auto-clone into each new location via Jira Automation. T-shirt sizes (XS-XL) baked into templates so we get real per-venue cost data over time.

**Phase 2, Standup to Jira Auto-Update.** Aurora Punks' existing post-meeting pipeline gets pointed at the BADASS daily standup. Read AI stays. Pipeline maps action items to Epics, transitions tickets based on standup language, posts a daily digest to Teams. Live before Dubrovnik race 12-13 June.

---

## The problem

Six Jira projects for one rotating customisation team. Per-venue scope is held in free-text labels, which means every typo and case variant breaks a board filter (current example: `Dubrovinik` vs `Dubrovnik`). The same 20-task delivery checklist gets hand-typed per venue with inconsistent naming. Sub-tasks don't inherit their parent Epic's location label, so they fall outside every per-location board. Today these are 5-minute symptoms; structurally they are guaranteed to recur.

---

## Proposed structure

| Layer | Mechanism | Example |
|---|---|---|
| Project | Jira project | `CUST`, "BADASS Customisation" |
| Client | Component (controlled list) | E1 Series, Show Jumping, F1 VR, Ocean Race, PFL, Blackbook |
| Season | Fix Version | "E1 2026 S3", "PJL 2026" |
| Project type | Component or custom field | AR Live Broadcast, VR Live Broadcast, AR App, UEFN, Steam-Console |
| Location / event | Epic with `Location` controlled-list field | "Dubrovnik 2026", "Como 2026" |
| Recurring deliverable | Story under the Location Epic, auto-cloned from template | "AR Broadcast Setup", "AR App V0.2.x" |
| Atomic work | Sub-task under the Story, auto-cloned with template defaults | "Configure StreamDeck", "Mo-Sys Lens Tweaking" |

### Custom fields

1. **Location**: single-select, controlled list, mandatory on Epic, optional on Story/Task (inherits for reporting).
2. **T-shirt Size**: XS / S / M / L / XL with default mapping `XS=0.5d, S=2d, M=5d, L=10d, XL=20d`. Mandatory on Story, optional on Epic (rollup).
3. **Template Source**: single-select per project type. On Epic only. Used by the Automation rule to know which template to clone.

---

## Template engine

**PM workflow:** create a new Epic, set Component + Fix Version + Location + Template Source. Jira Automation clones all Stories from the matching Template Epic into the new Epic, with T-shirt sizes pre-populated and sub-tasks pre-cloned. PM adjusts where this venue differs and assigns owners. That is the entire intake.

**Template Epics:** one per project type, hidden under a `TEMPLATES` Component, never worked directly. Seed list:

- **AR Live Broadcast**: ~20 sized Stories, mirrored from E12026-542 (already mature).
- **VR Live Broadcast**: seeded from John's Como VR work.
- **AR App (V0.2.x and V0.3.x)**: seeded from Ben's E12026-279 + E12026-312 trees.
- **Environment Production**: seeded from Marco's E12026-514.
- **Course Explainers**: seeded from Jake's E12026-396 / E12026-402.
- **UEFN, Steam-Console Game**: seeded as patterns surface.

Content owner per template (reviews quarterly, owns updates):

| Template | Owner |
|---|---|
| AR Live Broadcast | Alex |
| VR Live Broadcast | John |
| AR App | Ben |
| Environment Production | Marco |
| Course Explainers | Jake |
| UEFN | TBD |
| Steam-Console | Sezar |

PM is template administrator and runs the engine. After each race week, 15-min retro with the relevant content owner: what was added, skipped, resized.

---

## Phase 1 steps

1. **Spec sign-off.** Decisions below locked.
2. **CUST scaffolding.** Create project, custom fields, AR Live Broadcast template Epic, Automation rule, standard boards (All / Per-Client / Per-Location).
3. **E12026 migration.** Bulk-move all E12026 issues to CUST. Existing per-venue Epics become Location Epics with `Location` field set. Labels normalised to controlled values. Component = E1 Series, Fix Version = E1 2026 S3. Old E12026 archived read-only.
4. **Dormant client triage.** Archive PFL, BMS, OR (no live work). Migrate SJ + F1 open tickets into CUST as their own Components. Archive old projects.
5. **PM onboarding.** One-page "How to use CUST" guide + 30-min walkthrough.

---

## Phase 2 steps

The pipeline already runs for two other AP-managed projects on the same VPS infrastructure. Notetaker-agnostic (recognises Read AI, Fireflies, Otter, Fathom, Gemini, Microsoft Recap), so Read AI stays. No new licensing.

1. **Read AI sanity check.** Confirm the post-meeting summary lands in a Gmail account the AP pipeline can scan.
2. **Wire BADASS standup into the pipeline.** Add the recurring event to the calendar watcher, point at `project: badass` and the new CUST project key, tune the PM agent prompt to BADASS patterns.
3. **Auto-update Jira.** Wire the Jira-mutation path to CUST. Status heuristics: "I finished X" to Done, "I'm working on X" to In Progress + assignee, "blocked on Y" adds blocker comment + label, "parked" to Backlog.
4. **Daily digest to Teams.** One-line summary posted via Teams Incoming Webhook ("Yesterday's standup to Jira: 3 to Done, 2 new In Progress, 1 blocker").
5. **Tune (first 2 weeks).** Shadow mode to start: agent posts proposed changes as comments, PM reviews and applies manually. After 2 clean weeks, switch to autonomous. Live before Dubrovnik 12-13 June.

---

## Decisions to lock

1. **Dormant client triage.** Archive PFL / BMS / OR; migrate SJ + F1 open tickets into CUST as their own Components.
2. **Template ownership.** Distributed by template (table above). PM is operator, not content owner.
3. **T-shirt sizes baked into templates.** Every cloned Story arrives pre-sized. PM bumps at intake if the venue differs from the default.

---

## Next steps

Robert and Nancy share this doc with Rosy and Alex. 30-min call later this week to confirm decisions and green-light Phase 1. Execution starts the following week.

Robert + Nancy
