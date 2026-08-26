---
name: BADASS Studios XR Platform
description: XR platform project for Badass Studios — Robert does PM/roadmap/estimation, E1 racing is anchor client, UE5-based
type: project
originSessionId: 4d378e3d-428c-452b-9875-970bd26af171
---
## Overview
Badass Studios is building **BadassXR**, an Unreal Engine 5-based XR platform with modular architecture. Robert's role is product management — specifically roadmap scoping, task breakdown, and estimation for the Jira backlog.

**Why:** Rosemary (CEO) needs completed roadmap + cost estimates for investor pitches (Dell Capital) and budget planning. This has been urgent since Jan 2026.

**How to apply:** Robert's deliverable is backlog estimation in Jira. Focus on breaking vague tasks into proper user stories and providing man-month estimates.

**Update (2026-05):** the engagement has broadened well beyond backlog estimation — Robert now runs a full Jira restructure (the **CUST** project), P&L/staffing planning, and the AP/BADASS engagement contract. See the **Customisation Jira Restructure** and **Engagement Contract** sections below.

## Key People
- **Rosemary Lokhorst** — CEO, rosemary@badass-studios.com, +1 747-322-2210 (LA timezone, 9h behind CET)
- **Alex Sangwin-Skillen** — Co-Founder/Creative Director, alex@badass-studios.com, +447368200388
- **Sezar Kamleh** — Developer (boat physics, UI migration, C++ conversion, leaderboard), sezar@badass-studios.com
- **Jake Kay** — Artist (cockpit, format explainers, VR assets), jakekayart@gmail.com
- **Marco Tosoni** — Artist (environment/POI models, Como scene, exploring AI tools like Meshy)
- **John Liou** — Developer (VCam, camera tracks, Como integration)
- **Ben Jeffreys** — Developer (AR app, Blackbook, App Store, geoconversion)
- **Gaizka Pueyo** — Infrastructure/DevOps (low velocity, Robert questioning if work remains for him)
- **Nancy Imado / Herbert** — Chief of Staff (nancy@badass-studios.com); previously listed as part-time QA, role expanded as of May 2026; owns role descriptions, calendar/meeting ops, Jira board hygiene, internal comms
- **Adam Binns** — Marketing/social
- **Sheida Shaker** — Operations
- **Oskar** — Developer (Badass side)
- **Robin Hoffa** — Developer (Eternal Minds, hoffa@eternalminds.se)

## Team Composition (as of 2026-03-24)
- **3 Devs:** John, Sezar, Ben
- **2 Artists:** Jake, Marco
- **Lead/Arch/PM/Creative:** Alex (spread thin across all roles)
- **Infra:** Gaizka (status unclear)
- Average capacity: ~10 PM per person per year (blended)

## Staffing Plan v3 (Structural Spec) — Delivered 2026-05-09
- **GDoc:** https://docs.google.com/document/d/11eqVAkuuhjvjzFYAiPbvc7mtF5tids0KWasUJ2_xt54/edit
- Location: BADASS Drive → Deliverables (`1hdEG5JhcjggvnsfThnOn_5sxfJW-vZzj`)
- Five-group structure: Mgmt / Marketing & Comms / Platform / Customisation Core (5 templates) / Shared Services
- Cost model formula: `Mgmt + M&C + Platform + Σ(active_projects × template_cost) + scaled_shared_services + sub_overflow`
- 50% threshold rule: >50% per project = Core, ≤50% = Shared Services
- Scaling: bigger project = more subs added to Core (not FTE inflation); concurrent = full Core duplication; surplus FTE hours flow upstream to Platform
- 5 templates: AR Live Broadcast / VR Live Broadcast / AR App / UEFN / Steam-Console Game; Digital Twin folds into Broadcast templates
- Marco/Jake/Ben held on Platform per Rosy's investor-optics direction (pending Alex discussion)
- Customisation Team Lead = AP-supplied PM role at 60% per template (Robert covers E1)
- Numbers / Staff Sheet build deferred until Dieter signs off on shape; will land in May 4 v2 P&L file
- Cloud/AI cost = placeholder lines, populated via badass-002 next week
- Live numerical source-of-truth: May 4 v2 P&L (https://drive.google.com/file/d/1QU1OrZmUrMfD8c5SNTD5Xs3w48Gr5Z1I/view)
- Drive hygiene: April 15 P&L moved to Archive folder (root-level Archive `1XBCUg_UQ9oHyaC-z-Cmbpiwznkv20dtb`)

## Backlog Estimation Report — Shared with Client 2026-03-24
- **Google Doc (canon):** https://docs.google.com/document/d/1iybWdSyKAthihOWVahetM6pqWfHZ7UEEk4YdyogIazE/edit
- **Google Sheet (backlog):** https://docs.google.com/spreadsheets/d/1h5K949tv3Qt6JFviUASdPzXm2aJ4fTlXX7dpTrGfTa0/edit
- **Local MD:** badass/backlog_estimation_report.md
- **Upload script:** badass_report_to_gdoc.py (MD → HTML → Google Doc via Robert's OAuth)
- Key findings: 1,673 Jira issues, 483 orphan tasks, 10/12 EPICs underbroken, PE/BX project duplication
- Current backlog: 47-87 PM; Expected (with padding): 62-117 PM across 2026-2028
- 2026 resource gap: 12 PM additional needed (team output 53 PM vs 65 PM adjusted demand)
- AP recommendation: 100-140 days/year (60-80 senior dev + 40-60 PM days)
- Robert edited the doc directly — removed individual names from exec summary, changed Gaizka velocity note, rewrote Como recommendation to ask about including in overall backlog, added note about devs reporting last-minute deadline push as biggest challenge

## Platform Modules
1. **Platform BadassXR** — Core/shared infrastructure
2. **Module: AR Broadcasting** — Live AR overlays for broadcast
3. **Module: VR Broadcasting** — VR experience
4. **Module: Steam Game** — Racing game on Steam
5. **Module: Fortnite Game** — UEFN/Fortnite integration (pipeline exists, 15 days per instance)
6. **Module: AR App** — Mobile AR app (Blackbook)

## Anchor Client: E1 Series
UIM E1 Championship (electric powerboat racing). Badass provides:
- Digital twin environments (Como, Jeddah tracks)
- Live broadcast AR/graphics
- Fan-facing racing game
- AR app for spectators
- 2026 race calendar: 8 venues, Como next (Apr 24-25)

## Daily Standup Routine
Robert attends the BADASS daily standup (Tue-Fri, 17:30 CET). Before each standup, Claude should prep a briefing:
1. Pull the latest Read AI pre-read/summary from Gmail (from Alex via Read AI)
2. Check Dev Squad Teams notifications in Gmail for anything shared
3. Check recent Jira activity (last 3 days, all projects: BX, PE, E12026)
4. Check the Rosemary/Alex email threads for anything pending or needing response
5. Compile into a standup brief with: yesterday's topics, Jira movement, open threads, suggested talking points

**Why:** Robert is ramping up PM involvement (proposed 30h/month PM role). Attending standup daily with prep means he can add value immediately and stay on top of team velocity.

**How to apply:** When Robert says "standup prep" or "daily standup" for BADASS, run this routine automatically.

## Active Threads (as of 2026-03-27)
- **AP Proposal on the table:** 80h/month (30h PM Robert + 50h dev Petter Andersson) or scale to 160h/month. Rosy positive, wants Monday call with Alex to discuss. Need to confirm time (she suggested 6am PAR / 5:30am PST).
- **Role breakdown sent:** Added Role column to backlog sheet, sent demand-by-role summary to Rosy for business plan.
- **Alex's E1 Roadmap PDF:** "BADASS_E1 Roadmap (2026-02-18)_AlexUpdate.pdf" received Mar 23 — review status unclear.
- **Como race:** Apr 24-25. John deep in VR broadcast camera/track/buoyancy work. 4 weeks out.

## Tools & Systems
- **Jira**: badass-studios.atlassian.net (12 projects). Customisation work is consolidating into the new **CUST** project — see below. API access via the `badass.atlassian-api-token` (secrets_registry) for REST + the Rovo connector for issue-level work.
- **Teams**: Daily standups + team chat; Robert added to Dev Squad group (Mar 24)
- **Google Drive**: BADASS folder = `czp_projects/BADASS/` on the CZP Shared Drive (Deliverables / Financials / Legal / Archive subfolders)
- **Read AI**: Meeting summaries via alex@badass-studios.com — pre-reads arrive ~2h before standup

## Customisation Jira Restructure — CUST (since 2026-05)
- **CUST** ("BADASS Customisation") — new company-managed Jira project (id 10672) consolidating six per-client projects into one. Boards: CUST-All (954), Per-Client (955), Templates (957), default "CUST board" (953). (Per-Location board 956 deleted 2026-06-14 — it was a redundant duplicate of CUST-All; venue slicing now via labels + saved filters/Plan views.)
- Structure: **Component = Client** (E1 Series, Show Jumping, F1 VR, Blackbook, BMS) + **Component = Type** (AR Live Broadcast, VR Live Broadcast, AR App, Environment Production, Course Explainers, UEFN, Steam-Console, Format Explainer, XR Headset). **Location** = controlled-list custom field. **Fix Version** = season. **T-shirt Size** field for effort.
- 9 template Epics under a TEMPLATES component; a location-spawn engine clones a template's stories into a new Location Epic. **Template depth varies — clone is only as rich as the template:** AR Live Broadcast 20 / VR Live Broadcast 17 / AR App 5 / XR Headset, Env Prod, Course Explainers 4 each / UEFN 2 / Steam-Console now 13 (built out 2026-06-17, CUST-879..890) / **Format Explainer still 0 (empty — next user to spawn it hits a one-task clone)**. 2026-06-17: Nancy spawned Steam-Console Monaco (CUST-877) and it cloned only 1 story because the template was a stub; fixed by authoring the gaming build set into CUST-60 and backfilling Monaco (CUST-891..902). Both now 13 stories. Two interchangeable engines: the script `badass/drafts/cust_spawn_location.py` (PM-run), and the **native Jira Automation "Flow" — LIVE since 2026-06-14** ("CUST: Spawn template Stories on new Location Epic", project CUST). Self-serve: create an Epic + set 5 fields (Client, Type, Location, Fix Version, Template Source) + save → checklist clones in ~30s, label-tagged. Build steps + the two silent-fail gotchas (unquoted lookup JQL; "changed since last execution" box) in CUST Admin User Guide §6.
- **Migration complete (2026-05-22):** 665 issues (E12026 + open SJ/F1/BMS) bulk-moved into CUST; old source projects archived. Location tagging is DUAL — Location field AND a matching label (the label is what boards/filters sort on).
- **Portfolio Board** (Jira plan 34) is the existing cross-project timeline; once CUST holds clean data it becomes the investor-facing timeline Nancy needs. BADASS already has Plans — no Premium upgrade required.
- Full running detail lives in `badass/activity_log.md`.

## Engagement Contract (2026-05)
- The original Outsourcing Agreement was with **Aurora Punks Development Services AB (APDS, 559320-7466)** — now **bankrupt** (konkurs; estate handled by Advokatfirman Carler). It covered the UEFN dev work (done + invoiced).
- Robert's PM work runs under a **new** standalone agreement: **Creation Zero Point Holding AB (559182-7471) ↔ BADASS Studios Limited** — PM Services, GBP 65/hr, drafted and filed in `czp_projects/BADASS/Legal/`, signing flow pending. GBP 2,600 fixed for the first 40h (to 2026-05-20) invoiced; hourly thereafter. Note: CZP Holding's verksamhetsföremål is holding-company-only — mismatch flagged, Robert accepted as-is.

## Alex's Jira Agent / `BADASS-Studios/Jira` repo (since 2026-05-29)
- Alex built an **AGENTS.md** — explicit rules the team must follow when creating Jira Issues (what tasks go where, templates, structure). Tested it by creating **CUST-743** (E1 Miami) with tasks/sub-tasks via Copilot.
- He wants a **lightweight GitHub repo `BADASS-Studios/Jira`** (https://github.com/BADASS-Studios/Jira) so every team member uses **GitHub Copilot** to create/update Jira tasks, kept current with agent skills + templates + docs on task routing. Offered Robert collaborator access (invite sent to robert@aurorapunks.com 2026-05-29).
- May 29 standup: this "JIRA-integrated tool replaces the prior copilot, enforces clearer roles + prompts for task entry"; "tasks auto-assign to creator unless admin"; open Qs: does the plugin work in JetBrains Rider; can users edit others' tasks.
- **Strategic angle:** Alex's agent is the "how to create issues correctly" layer on top of Robert's CUST taxonomy (components=client/type, location, templates, spawn automation). Complementary, not competing — Robert's CUST Admin Guide IS the documentation that agent should encode. Opportunity to co-own the task-routing rules (deepens engagement); risk is drift if the repo diverges from CUST conventions.
- **Access RESOLVED (2026-06-17):** the VPS `gh` CLI (`RobertBackstrom`) is now an active member of `BADASS-Studios` and reads `BADASS-Studios/Jira` fine — the prior 404 is gone. Repo contents: `AGENTS.md` (the rules), `.github/agents/jira-manager.agent.md` (Copilot custom-agent def), `Copilot_MCP_Setup.md`, `README.md`, `.vscode/mcp.json`. Clone with `gh repo clone BADASS-Studios/Jira`. (Earlier 2026-06-01 note: repo was private + invite invisible to the gh handle — no longer true.) The demo video `JiraAgentTest.mp4` is still on Alex's SharePoint/OneDrive (Microsoft-auth gated, db-189).
- **Jira VS Code Agent — audit 2026-06-17:** It's a GitHub Copilot custom agent ("Jira Manager") run inside VS Code/Rider via Copilot + Atlassian Rovo MCP + `vscode_askQuestions`; the orchestrating session can't drive it (no `vscode_askQuestions` tool, interactive IDE flow — only Robert can run the live test). Audited the rule set vs live CUST. Findings: (1) **Epic-parenting VERIFIED WORKING** — AGENTS.md sets `customfield_10014` (legacy Epic Link); CUST is company-managed (`simplified:false`) where the modern field is `parent`. Empirical test 2026-06-17 (created TEST Task CUST-903 with Epic-Link-only, then deleted): setting `customfield_10014` alone auto-populated `parent`, so the issue nests correctly under the epic. Jira mirrors Epic Link → parent on this instance; the agent's parenting is fine. (Could still recommend switching to `parent` for forward-proofing since Epic Link is deprecated, but it's not broken.) (2) **Component table gaps** — Game Client + Mobile AR App both marked "(confirm in Jira)"; real components are `Steam-Console` (10156) and `AR App`. (3) Epic-list is filtered strictly by Location (`customfield_10231`) — works because venue + feature epics are location-tagged (verified Monaco epics + CUST-743 Dubrovnik), but a platform/cross-cutting epic with no Location wouldn't surface. (4) Anti-Epic-creation rules are strong (explicit refusal + anti-bypass clause + pre-submission check) — by spec it will NOT create Epics; the realistic "asks about an Epic" case is a brand-new venue with no matching epic → it dead-ends the user to "ask an admin."

## Rosy roadmap check-in (open, 2026-06-01)
- Rosy (Teams): wants a quick call to check in on the **roadmap** (liked the Excel + Word work); flagged "may be some follow-up with the roadmap" and "make sure we have the most up-to-date doc there." She's at **Nordic Game** this week, **back Friday** — proposed Friday, maybe a short slot before but events make focus hard.
- Action for Robert: confirm Friday (or offer a short pre-NGC slot); have the latest roadmap Excel/Word ready to share before the call.
