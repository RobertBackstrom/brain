# BADASS Customisation Jira, Structural Proposal v1

**From:** Robert (Aurora Punks PM), Nancy Imado (Chief of Staff / Project Manager (PM))
**To:** Rosemary Lokhorst, Alex Sangwin-Skillen
**Status:** DRAFT, structural review only, awaiting sign-off before execution
**Related:** April 2026 BX platform overhaul; PM Jira help call 2026-05-06

---

## TL;DR

Two phases, sequenced.

**Phase 1, Customisation Jira Restructure (next 2 weeks).** Six per-client Jira projects (E12026, SJ, F1, OR, PFL, BMS) collapse into one new `CUST` project. E12026 is the only project with activity in the last 60 days; SJ and F1 each carry a handful of open tickets that may reactivate; PFL, BMS, OR look fully dormant. Client becomes a *Component*, season a *Fix Version*, race/event an *Epic*. Recurring deliverables (AR Broadcast, VR Broadcast, AR App, Course Explainers) become **template Epics** that auto-clone tasks into each new location via Jira Automation. **The PM's job becomes one click**: pick client + location + template, 20+ tasks land pre-populated and pre-sized. T-shirt sizing (XS=0.5d to XL=20d) baked into templates so year over year we get real per-venue cost data.

**Phase 2, Standup to Jira Auto-Update (~1.5 days of AP work, then 2 weeks of light tuning).** Read AI already records the daily Teams standup and emails the summary. Today nothing happens to Jira after. Phase 2 closes that loop: Aurora's existing post-meeting-sweep pipeline (running for another project since April) gets pointed at the BADASS standup, PM agent maps action items to Epics, transitions tickets based on standup language ("I finished X" to Done, "blocked on Y" to blocker), posts a daily digest to Teams. **Recommendation: keep Read AI** (already deployed; AP pipeline is notetaker-agnostic so switching later is free). Backup option: Fireflies.ai.

**Migration timing** sits in the cover email, not this doc. High-level: Phase 1 quick-fix already done. Phase 1 execution next week. Phase 2 wires up the week after, fully autonomous ahead of Dubrovnik race week 12-13 June.

---

## Why the current setup hurts

### Example
E12026-542 "AR Broadcast Setup, Dubrovnik" is an Epic in E12026. Alex created 20 child tasks under it. None showed on the Dubrovnik board.

**Root cause:** the "Dubrovnik board" is filtered by `labels = "Dubrovinik"` (the team has been spelling it `Dubrovinik` for months, the label was typoed when first created and propagated as people copy-pasted). The new epic and children had **no labels at all**, so they fell outside the filter.

This is one symptom of three structural problems:

### Problem 1, Labels are the only thing scoping a location
Labels are free-text. Three observed variants: `Dubrovinik` (typo, dominant), `Dubrovnik` (correct, minority), `dubrovnik` (lowercase). New team members copy whatever they see. Boards filtered by label miss anything mislabeled or unlabeled.

### Problem 2, Recurring activities are re-built by hand every location
Every venue needs: AR Broadcast Setup, VR Broadcast, AR App (V0.2.x / V0.3.x), Vision Pro App, Course Explainers, Environment Production, optionally Live GP / Fortnite / Arcade Game. That's the same 8-10 epics × 8 venues = ~70 epics per season, all hand-typed with inconsistent naming ("AR app V0.2.0" vs "AR app V0.2.x" vs "AR App V0.2.4"). Sub-tasks vary by who happened to write them up.

### Problem 3, Six projects for one team's work
The customisation team is one team. They rotate across clients (E1 today, Show Jumping if it reactivates, F1 VR placeholder, etc.). Six Jira projects = six boards, six permission schemes, six dashboards, six naming conventions, six places for things to fall through the cracks. The PM has to flip between them to know what's happening.

---

## Proposed structure

### One project: `CUST`, Customisation

| Layer | Mechanism | Example |
|---|---|---|
| **Project** | Jira project | `CUST`, "BADASS Customisation" |
| **Client** | Component (single-select, controlled list) | E1 Series · Show Jumping · F1 VR · Ocean Race · PFL · Blackbook · *(new client)* |
| **Season** | Fix Version | "E1 2026 S3" · "E1 2027 S4" · "PJL 2026" |
| **Project type** | Component or custom field (controlled list) | AR Live Broadcast · VR Live Broadcast · AR App · UEFN · Steam-Console Game |
| **Location / event** | **Epic** with a `Location` custom field (single-select, controlled list) | Epic: "Dubrovnik 2026" · Epic: "Como 2026" · Epic: "Monaco 2026" |
| **Recurring deliverable** | **Story** under the Location Epic, auto-cloned from a Template | "AR Broadcast Setup", "AR App V0.2.x", "Course Explainers" |
| **Atomic work** | Sub-task under the Story, auto-cloned with template defaults | "Configure StreamDeck", "Mo-Sys Lens Tweaking", etc. |

Everything is one project. The team sees one backlog. The PM owns one board.

### Why Component for Client (not Project)
Per-client *projects* were the old shape, they create the duplication problem. **Component** is the Jira-native way to slice cross-cutting work without spawning project sprawl. Boards can filter by Component (e.g., "Show me only E1 work"). Reports group by Component for per-client P&L reconciliation.

### Why Fix Version for Season
Seasons rotate annually. Fix Version is Jira-native for "stuff shipping in this release window." Velocity reports work out of the box. When the 2026 season closes, you mark the version released and start 2027 S4, no project juggling.

### Why Epic per Location
Each race/event is the natural unit of delivery. Epic gives you:
- A single URL to share for the event's status ("here's everything Dubrovnik 2026")
- Progress rollup (X of N stories Done)
- A scope boundary for sprint planning ("can we get Dubrovnik to ready-for-broadcast by 9 June?")

The Location custom field is **mandatory on every Epic** so the data is always there for filtering, reporting, and the per-location cost tracking.

### Custom fields to add
1. **Location**, single-select, controlled list maintained by the PM. Mandatory on Epic. Optional on Story/Task (inherits from parent for reporting).
2. **T-shirt Size**, single-select: XS / S / M / L / XL. Default mapping in field description: `XS=0.5d, S=2d, M=5d, L=10d, XL=20d`. Optional on Epic (rollup), mandatory on Story.
3. **Template Source**, single-select: AR Live Broadcast · VR Live Broadcast · AR App · UEFN · Steam-Console Game. On Epic only. Used by the Automation rule to know which template to clone from.

---

## The Template Engine (what matters)

### How it works for the PM
1. PM creates a new Epic: summary "Dubrovnik 2026", picks Component **E1 Series**, fixVersion **E1 2026 S3**, Location **Dubrovnik**, Template Source **AR Live Broadcast**.
2. Jira Automation fires: clones all Stories from the **Template Epic** for AR Live Broadcast (a hidden parent Epic in the project, never directly worked) into the new Epic, with T-shirt sizes pre-populated and sub-tasks pre-cloned with their default sizes.
3. PM adjusts (skip ones not relevant for this location, bump size if it's a bigger venue), assigns owners.
4. Team picks up the work. Their burden: tick boxes / move tickets, that's it.

### Template Epics (one per Project Type)
Hidden under a `TEMPLATES` Component, never worked directly. Each contains a canonical, sized Story tree:

**AR Live Broadcast** (template, ~20 Stories from E12026-542's existing tree):
- AR Broadcast Setup, Office prep · S
  - Configure StreamDeck for AR Broadcast · XS
  - Test AR Broadcast Actors with Simulated Data · S
  - TrackMapper Camera Pre-Positioning · XS
  - Visual Quality Assessment (Fake Video-In) · S
  - Blackmagic Card & SDI Output Test · XS
  - Import Artist Sub-Levels · XS
- AR Broadcast Setup, On-site hardware · M
  - Camera Rig & B20 Assembly · S
  - SDI & Video Format Verification (On-Site) · XS
  - Mo-Sys Lens Tweaking · S
  - Local Fibre Test · XS
  - LiveLink & Camera Tracking Setup · S
  - Al Kamel Data Feed & WebSocket Relay · S
- AR Calibration · M
  - SunTracker, Broadcast Room Config · S
  - SunTracker, Hoist Raised Setup (daily) · XS
  - Camera GPS Positioning · XS
  - AR Calibration, UE Component Setup · S
  - AR Calibration, Solve & Save · S
  - Import Sponsors Level & Final Spline Tweak · S
- Pre-Live Sign-Offs · S
- Live Broadcast Operations · L (multi-day)

**Other templates to seed** (Alex + PM fill in sub-tasks): VR Live Broadcast · AR App (V0.2.x and V0.3.x flavours) · UEFN · Steam-Console Game · Course Explainers · Environment Production. Start with AR Live Broadcast (already mature in E12026-542), others get fleshed out as locations need them.

### Why Jira Automation (not bulk-clone scripts)
- Native to Jira, no external infra.
- The PM can edit the rule if templates evolve, no developer involvement.
- The Automation log shows who triggered what, when, auditable.
- Free tier supports 100 rule executions/month; we're nowhere near that.

---

## Phase 1, Customisation Jira Restructure

### Step 1.0, Quick-fix (already done)
- 41 items now correctly labeled `Dubrovnik`; the `Dubrovinik` typo label is empty.
- E12026-542 + 20 children labeled so the existing Dubrovnik board picks them up.
- Duplicate Course Explainers Epic E12026-402 flagged with a comment to close.

### Step 1.1, Spec sign-off
- Stakeholders review this doc.
- Decisions locked (see below).
- Sign-off green-lights Step 1.2.

### Step 1.2, CUST scaffolding
- Create CUST project (team-managed, same template as BX).
- Create the controlled-list custom fields (Location, T-shirt Size, Template Source).
- Seed the **AR Live Broadcast** template Epic with sized Stories (mirror E12026-542's tree).
- Build the "New Location, clone template" Automation rule.
- Set up the standard boards: All Customisation (default), Per-Client (filtered by Component), Per-Location (filtered by Location field).

### Step 1.3, E12026 migration
- Bulk-move all E12026 issues to CUST, mapping:
  - existing per-venue Epics, new Location Epics with the `Location` custom field set
  - all labels normalised to controlled-list values (no more typos)
  - Component = E1 Series, Fix Version = E1 2026 S3
- Old E12026 archived read-only (history preserved, links don't break).
- Verify all in-flight work appears correctly on the new boards.

### Step 1.4, Dormant client triage
- **Archive** PFL, BMS, OR (no live work, history preserved, can be revived).
- **Migrate** open tickets for SJ + F1 into CUST as their own Components (small effort, keeps options open).
- Old projects archived after migration.

### Step 1.5, PM onboarding
- One-page "How to use CUST" guide:
  - "I'm starting a new location, here's the 4 fields to fill"
  - "I want to see only E1, click this saved filter"
  - "I want to know what's overdue, this Dashboard"
- 30-min walkthrough call.

---

## Phase 2, Standup Notetaker to Jira Auto-Update

### The problem this solves

BADASS runs daily standup on Microsoft Teams (Tue-Fri 17:30 CET). Today the team talks for 20 minutes, Read AI records and emails a summary, and **nothing happens to Jira**. Tickets remain stale, action items live in transcript bodies nobody re-reads, status doesn't update until the next sprint review.

The fix: feed the standup transcript through an agent that **updates Jira automatically**. Transitions tickets to match what the team just said, creates new sub-tasks for action items, comments on referenced tickets with the meeting context, and posts a daily digest back to Teams ("Yesterday: 3 to Done, 2 new In Progress, 1 blocker").

### What's already built (free for BADASS)

Aurora Punks already runs this exact pipeline for two other projects. The components live on the AP infrastructure (Hetzner VPS):

1. **Calendar watcher** detects when a flagged meeting ends.
2. **Notetaker-agnostic transcript ingest**, searches Gmail for the transcript by event title/calendar link. Already handles Read.ai, Fireflies, Otter, Fathom, Gemini, Microsoft Recap. New notetakers self-heal because we match on event reference, not sender.
3. **Death Board ticket** auto-created with the transcript + an agent prompt scoped to the project.
4. **PM agent** (Claude-powered) processes the ticket: maps action items to existing Epics, creates sub-tasks under the right one, transitions status based on standup language.
5. **Status-transition heuristics** already calibrated from another project's standup work:
   - "I finished X / done with X", transition to Done
   - "I'm working on X / starting X", In Progress, assignee = speaker
   - "blocked on Y / waiting for Z", adds blocker comment + label
   - "parked / next week", BACKLOG
   - "we decided X", comment on the relevant ticket

For BADASS, this means **Phase 2 is mostly configuration, not new code.** AP infrastructure exists, has been running for ~4 weeks elsewhere, and just needs to be pointed at the BADASS Teams standup + the new CUST project.

### Notetaker recommendation: keep Read AI, evaluate alternatives only if it underperforms

| Notetaker | Teams support | Jira integration | Cost | Status |
|---|---|---|---|---|
| **Read AI** (current) | ✓ Bot joins Teams calls | Via AP pipeline (already wired) | What BADASS pays today | ✅ **Recommended, already deployed** |
| Fireflies.ai | ✓ Native Teams app | Native Jira integration + AP pipeline | $10-19/user/month | Backup option |
| Otter.ai | ✓ Native Teams app | Via Zapier or AP pipeline | $10-20/user/month | Backup option |
| Microsoft Copilot Intelligent Recap | ✓ Native (no bot) | Via Power Automate (more setup) | Teams Premium ($10/user/month) + Copilot for M365 ($30/user/month if not already licensed) | Skip, too expensive for the marginal upside |
| Sembly AI | ✓ Teams bot | Native Jira integration | $10-29/user/month | Backup option |
| Fathom | ✓ Teams bot | Limited Jira (via Zapier) | Free tier exists | Skip, Jira side weak |

**Why Read AI stays:**
- Already deployed; team trained; Alex gets pre-reads 2h before standup (working signal).
- AP pipeline already recognises Read AI output and tags it accordingly.
- Switching costs (retrain team, change calendar invites, swap pre-read flow) outweigh marginal accuracy gains.
- The AP pipeline is notetaker-agnostic anyway, if we switch later, no code change needed.

**Evaluate alternatives only if** Read AI's transcript quality is materially worse than expected, OR Read AI's pricing changes meaningfully. If we ever switch, the lean would be **Fireflies.ai**, proven Jira integration, Teams-native, and already on AP's notetaker tag list.

### Implementation, Phase 2 steps

#### Step 2.0, Read AI sanity check
Before any work: confirm Read AI's post-meeting summary actually lands in a Gmail account the AP pipeline can scan (Robert's Gmail, since he's an attendee). One real standup transcript opened by hand to verify quality + format.

#### Step 2.1, Wire BADASS daily standup into the AP pipeline
- Add the BADASS Daily Standup recurring event to the AP calendar watcher's config.
- Point the meeting at `project: badass` and the new CUST project key.
- Tune the PM agent prompt to BADASS-specific patterns (customisation rotation across locations, not feature dev like the K2C-style configuration).
- Daily standup ends 17:30 CET, pipeline runs ~30 min after to catch the Read AI summary.

#### Step 2.2, Auto-update Jira
- Wire the PM agent's Jira-mutation path to CUST (after Phase 1 ships).
- Confirm status heuristics map cleanly to CUST workflows.
- Test against one or two recorded standups before going live.

#### Step 2.3, Daily digest back to Teams (optional)
- Post a one-line "Yesterday's standup to Jira: 3 to Done, 2 new In Progress, 1 blocker" message to a Teams channel.
- Options: Teams Incoming Webhook (simplest), Power Automate flow (more flexible), or a Teams bot (heaviest).
- **Lean:** Teams Incoming Webhook, 5 min to set up, no licensing required, posts as a "BADASS Bot" identity.

#### Step 2.4, Tune and watch (first 2 weeks of operation)
- Monitor: are the auto-updates right? Are sub-tasks landing under the correct Epic? Are status transitions matching team intent?
- PM reviews the next-morning Jira diff and flags anything wrong; the PM agent's prompt gets refined accordingly.
- After 2 weeks: should be running cleanly with minimal intervention.

### Effort + cost

| Step | Effort | Owner |
|---|---|---|
| 2.0 Read AI sanity | 1 h | Robert + AP |
| 2.1 Wire pipeline | 4 h | AP DevOps |
| 2.2 Auto-update Jira | 2 h | AP PM agent tuning |
| 2.3 Teams digest | 4 h | AP DevOps (optional) |
| 2.4 Tune (over 2 weeks) | ~30 min/day | PM + AP |
| **Total** | **~1.5 days of AP work + 2 weeks of light supervision** | |

**Incremental tooling cost: $0.** AP infrastructure absorbs the runtime (it's already running for other projects). Read AI cost stays whatever BADASS pays today.

### What BADASS gets in Phase 2

- **Standup talk to Jira state**, no more "the team said X but Jira still shows Y."
- **Action items live as tickets**, not transcript bullets nobody re-reads.
- **Daily digest to Teams**: everyone sees what moved without opening Jira.
- **Per-meeting audit trail**: every Jira comment carries the source standup date, easy to trace back the "why" of any change.
- **Year-1 velocity data**: actual time-to-done per task type accumulates, sharpening Phase 1's template T-shirt estimates.

### Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Read AI transcript quality is too sparse for action-item extraction | Medium | Medium | Step 2.0 sanity check before commitment. If Read AI is weak, evaluate Fireflies.ai (1-week trial cost). |
| Agent transitions a ticket wrongly during a live race week | Low | Medium | First 2 weeks of operation = "shadow mode", agent posts proposed changes as comments only, PM reviews and applies manually. After 2 weeks of clean diffs, switch to autonomous. |
| Team feels surveilled ("the bot is listening to me") | Low | Low | Already mitigated, Read AI is already in the room. Nothing new is being recorded; we're just *acting* on the existing recording. Surface this clearly in the Phase 2 kickoff note. |
| Teams Incoming Webhook gets deprecated (Microsoft is sunsetting in 2025/2026) | High over 12 months | Low | If/when it sunsets, switch to Power Automate flow, slight extra setup but well-supported. |

---

## Three decisions, locked

**Decision 1, Dormant client triage: ✅ Archive PFL / BMS / OR; migrate SJ + F1 open tickets.**
PFL, Blackbook Motor Sports, and Ocean Race have no live work and unlikely revival in the near horizon, archive as-is, history preserved, can be revived later. Show Jumping and F1 VR each have a handful of open tickets and could reactivate, migrate their open tickets into CUST as their own Component, archive the closed history in the old project.

**Decision 2, Template ownership: distributed by template, PM is operator.**
The cleanest pattern given the team shape:

| Template | Content owner (reviews/approves changes) | Why |
|---|---|---|
| AR Live Broadcast | **Alex Sangwin-Skillen** | Authored the E12026-542 checklist; deepest hands-on |
| VR Live Broadcast | **John Liou** | VR lead, Como VR work |
| AR App (V0.2.x + V0.3.x) | **Ben Jeffreys** | AR app developer + App Store ownership |
| Environment Production | **Marco Tosoni** | Environment artist, scenes lead |
| Course Explainers | **Jake Kay** | Course explainer artist |
| UEFN / Fortnite | TBD (Travis if engaged) | Pipeline owner |
| Steam-Console Game | **Sezar Kamleh** | Boat physics, gameplay code |

**PM = template administrator.** Has edit rights on all templates and runs the engine: after every race week, a 15-min retro with the relevant content owner ("what did we add / skip / resize this time?"), updates the template. Year 2 estimates get sharp from real velocity. The team's burden stays low because their input is conversational, not "fill in a Jira form."

Why this shape: Alex is spread thin (per the v3 staffing review, Lead/Architect/Creative + PM all on him). Making him single-owner of every template makes him the bottleneck. Distributing by who-owns-which-delivery puts each template's content with the person who actually knows that delivery. PM stays the operator who keeps the engine running and the cadence consistent.

**Decision 3, T-shirt size defaults: ✅ Baked into templates.**
Every cloned Story arrives pre-sized (XS/S/M/L/XL per template default). PM bumps the size at intake if this location is bigger/smaller than the template (e.g., "Como is a known harder venue, bump from S to M"). Gives a velocity baseline from day one. Year 1 data calibrates year 2 defaults.

---

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Team resists new structure ("we like our boards") | Medium | Medium | Keep old E12026 archived/visible read-only for 60 days. Old links still resolve. |
| Automation rule breaks during a live race week | Low | High | Don't migrate during a race week. Dubrovnik race is 12-13 June, migrate well before. |
| Template estimates are wildly wrong year 1 | High | Low | This is normal. Year 1 data is the baseline; year 2 templates get refined from real velocity. |
| PM adds a new client/template wrong | Low | Low | Lock the controlled lists to admin-edit only; PM submits new values to Robert, gets them added. |
| The team forgets to fill T-shirt size | High | Low | PM assigns at intake (PM's job, not theirs). If a Story shows up with size blank, board has a "needs sizing" filter to scan. |

---

## What BADASS gets

**From Phase 1:**
- **One board, one backlog** for the PM.
- **New location = one form, 4 fields, 20 tasks auto-created.** No copy-paste, no missed sub-tasks.
- **Per-location cost data** accumulates automatically (sum of T-shirt sizes per Epic). After 2-3 races we have real numbers for "how long does an AR Broadcast actually take in 2026."
- **No more typo'd labels.** Location is a controlled-list custom field, only valid values are pickable.
- **Cross-client reporting** (e.g., "show me all VR Broadcast work this quarter") via Component + Template Source filters.
- **Cross-link to Platform Epics** (BX) stays the same as today.

**From Phase 2:**
- **Standup talk to Jira state**, automatically. Tickets stop being stale.
- **Action items as tickets**, not transcript bullets nobody re-reads.
- **Daily digest to Teams**: everyone sees what moved without opening Jira.
- **Real velocity feedback** sharpening Phase 1's T-shirt templates over time.

---

## Next steps

1. Robert and Nancy send this doc to Rosy and Alex for review.
2. 30-min review call later this week to lock Phase 1 decisions + green-light Phase 2.
3. Robert + AP + PM execute Phase 1 next week. Phase 2 wires up the week after.
4. First real test: Dubrovnik race week (12-13 June). By then, CUST is the working board for E1 *and* standups are flowing automatically into it.

Robert + Nancy
