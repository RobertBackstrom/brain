# BADASS — Engagement Time Breakdown

**Engagement:** BADASS Studios — PM / roadmap / estimation / Jira restructure
**Rate:** GBP 65 / hour
**Fixed-price scope:** 40 hours = GBP 2,600
**Reconstructed:** 2026-05-20, from `badass/activity_log.md` (engagement work starts 2026-03-22)

> **How to read this.** Hours are reconstruction estimates from the activity log, not a live timer - treat them as a first pass to correct against your own recollection. Line items are grouped by dated deliverable. The 40-hour fixed-scope line is marked in the table. Everything below it is overage: report it, not charged.

---

## Line items

| # | Date | Work item | Category | Est. hrs | Cumulative |
|---|------|-----------|----------|---------|-----------|
| 1 | 2026-03-22 | Full Jira backlog audit - 1,673 issues across BX/PE/E12026; 350 mapped to architecture; 483 orphans + 7 junk tickets identified | strategy | 5.0 | 5.0 |
| 2 | 2026-03-24 | Backlog estimation report - draft, edit, share as Google Doc (name removal, Como rewrite, deadline note) | strategy | 4.0 | 9.0 |
| 3 | 2026-03-26 | Role-based breakdown + Option A engagement proposal; backlog sheet Role column (578 rows tagged) | strategy | 3.5 | 12.5 |
| 4 | 2026-04-01 | Backlog walkthrough call (Rosemary, Alex) + prep | meeting | 1.5 | 14.0 |
| 5 | 2026-04-09 | Module-by-module role breakdown (Platform / Gaming / AR-XR / Broadcast / Environment / E1); demand analysis 42-71.5 PM | strategy | 4.0 | 18.0 |
| 6 | 2026-04-15 | Roadmap / Financial call (Teams - Rosemary, Dieter, Alex) | meeting | 1.5 | 19.5 |
| 7 | 2026-04-19 | Staff sheet parse (197 rows) + Jira audit + `staff_roles_mapping.md` gap analysis | strategy | 2.5 | 22.0 |
| 8 | 2026-04-22 | Staff sheet changeset - alignment call + changeset draft | strategy | 2.5 | 24.5 |
| 9 | 2026-04-27 | P&L staff sheet changeset applied to xlsm (39 edits, Changes Log tab); Drive folders + deliverable uploads; reply draft; Cloud/AI cost scoping | strategy | 4.0 | 28.5 |
| 10 | 2026-05-05 | Dieter call (30 min) + v3 staffing direction capture + resequencing | meeting | 1.5 | 30.0 |
| 11 | 2026-05-09 | Staffing Plan v3 structural spec - 7-section walkthrough, GDoc delivered, Drive hygiene, email drafts | strategy | 5.0 | 35.0 |
| 12 | 2026-05-11 | Org chart v2 - cost-centre structure, HTML/PNG/PDF | strategy | 2.5 | 37.5 |
| 13 | 2026-05-12 | Jira customisation overhaul - Dubrovnik board unblock, 11-project audit, structural proposal v1 GDoc + review pass | strategy | 5.0 | 42.5 |
| — | — | **— 40-hour fixed-price scope consumed here (mid 2026-05-12) —** | | | **40.0** |
| 14 | 2026-05-13 | Label inheritance sweep (147 issues relabelled) + proposal cover + leadership send | dev | 3.0 | 45.5 |
| 15 | 2026-05-14 | Multi-stakeholder workshop prep pack | strategy | 2.0 | 47.5 |
| 16 | 2026-05-19 | CUST scaffold kickoff - prep audit, label/template inventory, BADASS API token setup | dev | 2.5 | 50.0 |
| 17 | 2026-05-20 | CUST scaffold executed - project, 14 components, 2 versions, 3 custom fields, 5 boards; 8 template Epics + 54 Stories seeded; spawn engine + automation spec; Nancy handoff | dev | 4.5 | 54.5 |

---

## Recurring — daily standups

BADASS standup is Tue-Fri 17:30 CET, ran ~early April to now (~7 weeks). ~24-26 standups
actually happened (a few cancelled, e.g. the Apr 16 Como-testing week). Each runs **20-30 min**
(midpoint 25 min = 0.42 hr). Robert attended a portion, not all.

| Attendance assumed | Hours @ 25 min avg |
|--------------------|--------------------|
| ~10 standups | 4.2 |
| ~15 standups | 6.3 |
| ~20 standups | 8.3 |

**Working estimate: ~15 attended = ~6.3 hrs** (adjust once you have a count). Standup prep is
Claude-generated, so negligible Robert-side time - not added separately.

---

## Summary

| | Hours | Value @ GBP 65 |
|---|------|---------------|
| **Within fixed-price scope** | 40.0 | **GBP 2,600** (invoiced) |
| Overage - itemised (items 13 part / 14-17) | 14.5 | GBP 942 (reported, not charged) |
| Overage - standups (~15 attended, working est.) | 6.3 | GBP 410 (reported, not charged) |
| **Total reconstructed effort** | **~60.8** | **GBP 3,952** |

**Takeaway:** the 40-hour fixed price covered the March-early-May work - backlog estimation, roadmap demand modelling, P&L staffing plan v3, org chart. The **entire Jira restructure (CUST project) from 2026-05-12 onward is overage** - roughly 14.5 itemised hours plus ~6 hrs of standups. That is the block to report as delivered-beyond-scope: ~21 hours, ~GBP 1,350 of value delivered above the fixed price.

---

## Open items for Robert to confirm

1. **Hour estimates** - these are reconstructed from activity-log density, not a timer. Adjust any that feel off.
2. **Standup hours** - how many BADASS standups did you actually attend, and are they in or out of the fixed-price scope? Drives the recurring line.
3. **Pre-2026-03-22 work** - the activity log starts at the backlog audit. If there was earlier scoping/intro work, it needs adding.
4. **Calls** - items 4/6/10 are estimated at call length + light prep. Correct if they ran longer.
5. Seeded into `projects/time_log.csv` (2026-05-20) - 17 itemised rows + 1 reconstructed standup row. That file is now the canonical tracker; this doc is the billing view on top of it.
