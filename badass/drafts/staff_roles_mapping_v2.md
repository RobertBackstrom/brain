---
name: BADASS Staff Roles Mapping v2
description: Post-Apr 22 alignment of Dieter's P&L Staff sheet with Rosy's role descriptions and Robert's roadmap demand. Supersedes v1.
type: project
---

# BADASS — Staff Roles Mapping v2 (2026-04-22)

**Supersedes:** [staff_roles_mapping.md](staff_roles_mapping.md) (Apr 19 sweep)
**Source decisions:** Robert call Apr 22 + Rosy Dropbox role descriptions Apr 21 + Dieter P&L Apr 15

## Cost-center logic (Robert, Apr 22)

- **Platform Team** = builds and maintains the BadassXR core, the 1st-party game products (Race / Soccer / Concert templates), and runs platform CERT for Steam / consoles / mobile. Funded from runway / Dell Capital.
- **Customisation Team** = per-client implementations on top of the platform (E1 Como/Jeddah/Dubrovnik, Fortnite UEFN per-client, AR apps for client X, etc). Cost-recovered from client budgets.
- **Today's reality:** Marco and Jake are spending most of their time on customer-facing E1 Como work, so they belong in Customisation. Sezar and John are doing platform-shaped work (multiplayer, render-target perf, cameras) so they stay in Platform.

## Current staff — proposed cost-center placement

| Person | Title (per Rosy) | Dieter sheet today | Cost center (v2) | Change |
|---|---|---|---|---|
| Sezar Kemleh | UE Developer (Intermediate) | Platform UK row 8 ("Unreal Eng Developer Sezar") | **Platform UK** | Rename Rosy's "Senior UE Dev" doc → "UE Developer" (intermediate level) for him. No row move. |
| John Liou | Unreal Engine, XR & Real-Time Graphics Developer | Platform US row 22 ("Full Stack-/Unreal Developer Jon Liou") | **Platform US** | No move. Title align: rename to Rosy's wording in next sheet pass. |
| Jake Kay | Lead 3D Artist | Platform UK row 6 | **Customisation UK** | **MOVE** Platform UK → Customisation UK (need Rosy sign-off) |
| Marco Tosoni | 3D Artist | Platform UK row 7 ("Technical Artist Mario Tosoni", US) | **Customisation UK** | **MOVE** + title change (Tech Artist → 3D Artist) + first-name fix (Mario → Marco) + location fix (US → UK if applicable — confirm with Dieter) |
| Ben Jeffreys | Junior AR Designer & Developer | Platform UK row 9 | **Pending — Robert to call** | Currently Platform; AR App is a platform-level module per architecture but Ben's day-to-day is E1 customer work. |
| Alex Sangwin | CCO | GenMgmt row 78 | GenMgmt | Title: Dieter has "Creative Director from 2026 Alex Sangwin" — align to CCO |
| Rosy Lokhorst | CEO | GenMgmt row 83 | GenMgmt | Aligned |
| Ben Douglas | COO | GenMgmt row 82 | GenMgmt | Aligned |
| Dieter Launer | Finance Manager | GenMgmt row 80 | GenMgmt | Aligned (50%) |
| Peter van Manen | Head of Engineering | GenMgmt row 86 | GenMgmt | Aligned |
| Nancy Imado | Chief of Staff | GenMgmt row 87 | GenMgmt | Aligned |
| Adam Binns | eSports Community & Partner Manager (per Rosy) | GenMgmt row 85 ("Comms Manager Adam Binns") | GenMgmt or Comms? | Title change per Rosy. Note: Rocket League initiative not in current roadmap scope but use Rosy's wording. |
| Michiel Sala | BusDev Manager | Mkt&Sales row 98 | Mkt&Sales | Aligned |
| Ian (?) | Accounting & Pricing | GenMgmt row 81 ("Accounting & Pricing Ian"), Freelance row 175 | GenMgmt (?) | **Open question — Robert doesn't know Ian. Ask Dieter/Rosy.** |

## New hires — proposed cost-center placement

| Role | Cost center | Rationale | First Q at 100% (proposed) |
|---|---|---|---|
| **UEFN Developer (Verse)** | **Customisation** (full-time per Robert) | Epic owns UEFN platform — Badass only does client customs. Asset library carries between clients. | Q3-2026 (need by May for Fortnite Monaco) |
| **Senior AI Engineer** | **Platform** (central tech resource per Robert) | Attached to AI-heavy backlog epics. Can also be covered by Aurora Punks (so this row may stay open / part-time / contract). | Q4-2026 (or AP coverage from Q3-2026) |
| **Release Manager** | **50% Customisation + 50% Platform** | Platform side: CERT for Badass-owned games on Steam/consoles/mobile. Customisation side: client app/game store onboarding. | Q4-2026 (post-Como, before first product cert push) |
| **Internal QA Lead** | **wrapped into Release Manager** | Per Robert: internal QA is part of the 100% Release Mgr position, not a separate hire. | Same as Release Mgr |
| **External QA teams** | **per-client (Customisation, pass-through)** | Billed to client as part of their app/game budget. Not a fixed P&L line. | N/A (project-based) |
| **Technical Artist** | **Platform** (per Robert, Apr 22) | New hire to bridge art ↔ engine on the platform side. Owns shaders/optimisation/pipeline systems. | Q3-2026 |
| **Tech Artist VR Broadcast** | **Customisation** | Per-event broadcast deliverables for E1 / future broadcast clients. | Q3-2026 (broadcast crunch) |
| **Tech Producer AR/VR Broadcast** | **Customisation** | Per-event production for E1 / clients. | Q3-2026 |
| **Unity & Mobile XR Dev** | **Customisation** | Per-client AR apps (Blackbook-style). | Q4-2026 |
| **Senior UE Dev** | Platform | Senior gap for platform engineering depth. | Q4-2026 |
| **DevOps Engineer** | **Platform** | Missing from Dieter's sheet. Gaizka's role status unclear. | Q4-2026 |
| **PM** | Platform (or AP coverage) | From my Apr 9 gap list. AP can cover in interim. | Q3-2026 (AP from now) |
| **2D Artist** | Customisation | E1 customer needs (UI/HUD/branding overlays). | Q4-2026 |
| **All Groovy crew** (Olivia, Jeroen, Xander, Daniela) | **Customisation pass-through** (per Robert's read) | External broadcast crew, per-event expense from project budget. **Confirm booking model with Rosy.** | N/A (event-based) |

## Open questions for Dieter / Rosy

1. **Marco + Jake move.** Are you (Rosy) OK with us moving them from Platform to Customisation in the P&L? Robert's read is that 80%+ of their current work is customer-facing E1 delivery.
2. **Ian.** Who is he? What's his role (beyond "Accounting & Pricing")? Engagement model (employee / contractor / All Groovy crew)?
3. **All Groovy.** Confirm: this is an external company, broadcast crew (Olivia, Jeroen, Xander, Daniela) booked per-event from client project budgets — yes?
4. **Marco's first name** in the sheet says "Mario Tosoni." Confirm "Marco Tosoni" is correct.
5. **Marco's location** in the sheet is set to US. Is this correct, or should it be UK?
6. **QA standalone role description** (separate from Release Mgr) — Rosy, you flagged QA on Apr 18 — keep as separate doc, or fold entirely into the Release Mgr write-up?
7. **Ben Jeffreys cost-center** — Platform (AR App is a platform module) or Customisation (his day-to-day is on E1)?

## Roles in Dieter's sheet with NO Rosy description yet (low-priority backlog)

Most of these can wait, but flagging for completeness:
- Legal (£115K line, no hire)
- Team Assistant (£35K)
- Account Manager (£85K)
- Brand/Marketing Manager (£75K)
- Marketing Assistant (£33K)
- Evangelist/Futurologist (£40K)
- Web Developer (£30K)
- Dev IT Support (£26K)
- Customer Support (£26K)
- PR Manager (£25K)
- Producer / Animator / Character Artist (multiple sections)
- Customisation Team Lead UK (£80K) and US ($175K)

## Quarter-flip rationale (links to roadmap demand)

From Robert's Apr 9 module-by-module breakdown:
- **Verse/UEFN Dev by May** (Fortnite Monaco) → start Q3-2026 at 100%
- **3D Artist by June** (Dubrovnik venue art) → already covered by Marco move; if additional, start Q3-2026
- **PM ASAP** → AP coverage from now, possible internal hire Q4-2026
- **DevOps** → start Q4-2026 (Gaizka's continuity question first)
- **Senior AI Engineer** → start Q4-2026 (AI-heavy epics ramp from Q3 onwards)
- **Release Mgr** → start Q4-2026 (first 1st-party cert push lines up with Steam release planning post-Como)
- **Tech Artist (Platform)** → Q3-2026 (Como wrap-up creates immediate optimisation demand)
- **Tech Artist VR Broadcast / Tech Producer AR/VR Broadcast** → Q3-2026 (broadcast crunch on E1 calendar from June onwards)
- **Unity & Mobile XR Dev** → Q4-2026 (post-Como AR App roadmap)
- **2D Artist** → Q4-2026

All quarters subject to Dieter's validation against runway and Dell Capital cadence.
