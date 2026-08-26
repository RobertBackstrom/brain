---
name: BADASS Staff Sheet — Changeset for Dieter
description: Cell-level edits to apply to the Apr 15 Staff sheet (xlsm) to reflect the Apr 22 alignment
type: project
---

# BADASS — Staff Sheet Changeset

**Source file:** Badass P^LL update for Roadmap (2026-04-15).xlsm, sheet **Staff**
**Apply after:** Dieter back from leave Apr 27
**Why a changeset doc, not a re-saved xlsm:** the file is macro-enabled (.xlsm). Programmatic re-save risks the VBA layer. Dieter applies these in Excel directly.

---

## Section A — In-place text edits (low risk)

| Cell | Current value | New value | Reason |
|---|---|---|---|
| A7 | `Technical Artist Mario Tosoni` | `3D Artist Marco Tosoni` | Title per Rosy's role desc; first-name fix |
| E7 | `US` | **CONFIRM** — Marco is UK-based per Robert; was the `US` location intentional? | Likely typo |
| A8 | `Unreal Eng Developer Sezar` | `UE Developer (Intermediate) Sezar Kemleh` | Per Rosy "UE Developer" doc; Sezar is intermediate not senior |
| A22 | `Full Stack-/Unreal Developer Jon Liou` | `UE / XR / Real-Time Graphics Developer John Liou` | Per Rosy's role desc; first-name spelling |
| A78 | `Creative Director from 2026 Alex Sangwin` | `CCO Alex Sangwin-Skillen` | Per Rosy CCO doc |
| A85 | `Comms Manager Adam Binns` | `eSports Community & Partner Manager Adam Binns` | Per Rosy doc (Rocket League framing — note: not in current roadmap scope, but using Rosy's wording) |
| A98 | `Business Developement/PAM Michiel Sala` | `BusDev Manager Michiel Sala` | Per Rosy doc; spelling fix |
| A175 | `Ian Something` | **OPEN** — full name TBC | Need from Dieter |

---

## Section B — Cross-team move: Jake + Marco from Platform UK → Customisation UK

**Pending Rosy approval. Robert's read of their day-to-day is 80%+ customer-facing E1 work.**

### Step B1 — Zero out their employment in Platform UK
- Set **M6 = 0** (Jake employment %, currently 1) — and zero across all quarter columns N..AD..onwards
- Set **M7 = 0** (Marco employment %, currently 1) — and zero across all quarter columns

### Step B2 — Add two new rows at the bottom of "Customisation Team UK (Salaries)" section (insert above row 47 "Expenses")

| Col | Row 46a (Jake) | Row 46b (Marco) |
|---|---|---|
| A | `Lead 3D Artist Jake Kay` | `3D Artist Marco Tosoni` |
| B | `See Below` | `See Below` |
| E | `UK` | `UK` (confirm) |
| H | `400` | `400` |
| I | `400` | `400` |
| J | `40000` | `40000` |
| L | `n.a` | `n.a` |
| M | `1` | `1` |
| N..end | `1` for every quarter | `1` for every quarter |

**Update totals:**
- B40 (Customisation Team UK total salary) — recalculate to include Jake + Marco loaded cost
- B5 (Platform Dev Team UK total salary) — recalculate down by Jake + Marco
- Row 51, 19, 37 totals — formulas should auto-update if SUM ranges include the new rows

---

## Section C — New role rows to add

### C1 — UEFN Dev (Customisation, full-time per Robert)
**Where:** New row in "Customisation Team UK (Salaries)" section (or US — Dieter to choose).
- A: `Verse / UEFN Developer`
- B (salary): `60000` — placeholder, Dieter to validate band
- E: `UK`
- L: `n.a`
- M (Q2-2026 employment %): `0`
- **First quarter at 100%:** Q3-2026 (column P or earliest 2026 column = `1`)

### C2 — Senior AI Engineer (Platform, central tech, can be AP-covered)
**Where:** New row in "Platform Development Team UK (Salaries)" section.
- A: `Senior AI Engineer`
- B (salary): `90000` — placeholder
- L: `n.a`
- **First quarter at 100%:** Q4-2026
- **Note:** Dieter — flag this row as "or AP coverage" since Robert's view is this can be sourced via Aurora Punks contract instead of hire.

### C3 — Release Manager (50% Platform / 50% Customisation)
**Where:** Two half-FTE rows OR one full row split across cost-center sums (Dieter's preference).
- A (option 1, two rows): `Release Manager — Platform CERT (50%)` in Platform UK; `Release Manager — Client Markets (50%)` in Customisation UK
- B (salary): `75000` total — placeholder
- M (employment %): `0.5` each row
- **First quarter at 100% (combined):** Q4-2026
- **Internal QA Lead** is folded into this role per Robert — no separate row needed. External QA per client app sits in the relevant project budget (not this sheet).

### C4 — DevOps Engineer (Platform)
**Where:** New row in Platform UK (or US — depends on Gaizka continuity, see open Q).
- A: `DevOps Engineer`
- B (salary): `65000` — placeholder
- **First quarter at 100%:** Q4-2026

### C5 — PM / Project Manager (Platform, AP coverage interim)
**Where:** New row in Platform UK.
- A: `PM / Project Manager`
- B (salary): `70000` — placeholder
- M: `0` (AP covers from now until Q4-2026)
- **First quarter at 100% (internal hire):** Q4-2026 or Q1-2027 depending on AP retainer extension

### C6 — Technical Artist (Platform per Robert, Apr 22)
**Where:** New row in Platform UK.
- A: `Technical Artist`
- B (salary): `55000` — placeholder
- **First quarter at 100%:** Q3-2026

### C7 — Tech Artist VR Broadcast (Customisation)
**Where:** New row in Customisation UK.
- A: `Technical Artist — VR Broadcast`
- B (salary): `55000` — placeholder
- **First quarter at 100%:** Q3-2026

### C8 — Tech Producer AR/VR Broadcast (Customisation)
**Where:** New row in Customisation UK.
- A: `Technical Producer — AR/VR Broadcast`
- B (salary): `70000` — placeholder
- **First quarter at 100%:** Q3-2026

### C9 — Unity & Mobile XR Dev (Customisation)
**Where:** New row in Customisation UK.
- A: `Unity & Mobile XR Developer`
- B (salary): `55000` — placeholder
- **First quarter at 100%:** Q4-2026

### C10 — 2D Artist (Customisation)
**Where:** New row in Customisation UK (or repurpose existing artist rows).
- A: `2D Artist`
- B (salary): `45000` — placeholder
- **First quarter at 100%:** Q4-2026

---

## Section D — Existing open rows: set quarter flips

For each of these existing 0%-employment rows in Dieter's sheet, suggested first quarter at 100%:

| Sheet row | Role | Section | Suggested first Q at 100% |
|---|---|---|---|
| 10 | Producer/Technical Lead | Platform UK | Q4-2026 (or fold into Tech Producer broadcast hire) |
| 11 | Animator | Platform UK | Hold (no immediate roadmap demand) |
| 12 | Full Stack Developer | Platform UK | Q4-2026 |
| 13 | AR/XR Developer | Platform UK | Hold (covered by Sezar + Ben J for now) |
| 14 | 3D Artist | Platform UK | Hold (covered by Tech Artist hire) |
| 23 | Team Lead | Platform US | Q1-2027 (US team scale) |
| 24-29 | (US team open roles) | Platform US | Q2-2027 onwards (US scale-up) |
| 41-46 | Customisation Team UK open roles | Customisation UK | Q3-2026 onwards as customer pipeline lands |
| 54-59 | Customisation Team US | Customisation US | Q1-2027 onwards |
| 70 | QA Team Lead | QA section | Folded into Release Mgr (see C3) |
| 71 | QA | QA section | External per client (see C3 note) |

---

## Section E — All Groovy crew (rows 190-193)

**Booking model open question.** Robert's read: external broadcast crew, expense from per-project (Customisation) budget, not a salaried P&L line.

If Rosy confirms: leave rows 190-193 as-is in the "Current Additional Freelance Resources on call" section. Add a column note: `Booked per-event from client project budgets.`

---

## Verification checklist (post-edit)

Dieter to verify after applying:
- [ ] Total Platform Dev Team UK headcount drops by 2 (Jake + Marco out)
- [ ] Total Customisation Team UK headcount jumps by 2 (Jake + Marco in) plus any new hires whose first Q is in 2026
- [ ] All Section C new roles appear in 5-year P&L tab totals
- [ ] No formula breaks (flag any #REF! errors)
- [ ] Quarter-flip dates align with Robert's Apr 9 demand timeline
