# Teef — Bottom-Up Cost Estimate (internal working doc)

**Scope basis:** Android-only soft-launch build of *Teef*, Missions 1–6, per the Co-Dev Brief §3.
**Budget envelope (Robert, 2026-06-18):** 4–5 devs for **6 weeks top**. Rate **€80/h** confirmed. End-Q4 2026 is the *launch* target; the *build* is a tight 6-week effort delivered well ahead of it, leaving TXG runway for balancing + soft-launch ops.

**Status:** sized to the 6-week envelope. Scope-vs-time is aggressive by design — leans hard on the existing browser prototype, the finished GDD, and concentrating polish on the CPI/D3-critical surface.

---

## 1. Team and effort (6-week build) — CANONICAL (Robert, 2026-06-19)

Rate: €80/h × 40 h/week = **€3,200 per dev-week**.

Team restructured to **4.0 FTE** for Option A; Option B adds the environment artist from 50% to 100% (= 4.5 FTE). **No separate QA seat** — device matrix + Play submission covered inside the team. **AI-assisted production** carries the environment + character volume (public-facing use OK per Robert, 2026-06-18; tools chosen to fit the client art style).

| Role | Person | Scope | Option A | Option B |
|---|---|---|---|---|
| Tech Lead (Unity) | Oskar Hansen | Architecture, core loop, Phase 1/2, Wanted/chase, geo→3D map, transparency/fade. Carries design capacity (Tom = authority). QA/device-matrix oversight | 100% | 100% |
| Gameplay programmer | Fredrik Laurent | Missions 1–6, economy, save/autosave, remote config (Sheet→Firebase), Magnetic SDK, crash reporting | 100% | 100% |
| Concept/art direction + tech/character artist (AI) | Hasan Chenari | Concept + art direction; ~35 characters (heavy NPC reuse), full animation set, supporting art | 100% | 100% |
| Environment artist (AI) | Prateek Karajgikar | geo→3D London map, ~9 locations, UI, app icon. **Street-accurate Soho/Mayfair = the Option B delta** | 50% | 100% |
| Production · audio · design (shared ½ seat) | Robert (prod) · Tim Browne (design adv.) · Carolina (SFX) | Oversight, client cadence, weekly demos, sign-off; advisory design; SFX/audio | 50% | 50% |
| **Build team total (FTE)** | | | **4.0** | **4.5** |

---

## 2. Cost

Labour at €3,200/dev-week × 6 weeks:

| Variant | Build (post-trim) | + QA (Northify) | + 10% contingency | **Total quoted** |
|---|---|---|---|---|
| **Option A — Reads-as-London** | €92,000 | €8,000 | €10,000 | **€110,000** |
| **Option B — Street-accurate** | €102,000 | €8,000 | €11,000 | **€121,000** |

**Pricing logic (Robert 2026-06-21):** build trimmed ~€4k each (€96k→€92k A, €106k→€102k B) — removing the A/B creative test frees Hassan to go straight to in-game representation, so less environment-artist load in the pre-prod fortnight. Soft, but a responsive price gesture to the client (CONFIRM the €4k with Robert). Option B's +€10k over A is still the env-artist 50%→100%. **QA €8k** (Northify) + **10% contingency** on (build+QA) folded into each total. **Unity engine license fees paid by client.** Totals land clean at €110k / €121k.

### (superseded) prior 5-dev / 4-dev envelope
| Variant | Dev-weeks | Build cost @ €3,200/dev-wk | + EP (1.5 dw) | Build total |
|---|---|---|---|---|
| **5-dev (ceiling)** | 30 | €96,000 | €4,800 | **~€100,800** |
| **4-dev (lean)** | 24 | €76,800 | €4,800 | **~€81,600** |

**Pass-through / third-party costs (on top, at cost):**
- Geo data — OpenStreetMap (ODbL) / Ordnance Survey OpenData for footprints+heights; open-licensed, ~zero cost. Mapbox kept only as a reference/fallback, not a runtime dependency, so no per-load cost.
- AI tooling — image/asset generation subscription(s) for the tech-art pipeline (modest monthly cost; tools picked to fit the client art style).
- Music licensing — 4 cheap licensed tracks (brief wants licensed, not composed).
- QA device matrix hardware — Android min-spec (Android 9+, 4GB RAM) up to current.
- **Functional + compliance QA — specialist partner (Northify):** separate budgeted line, **~€8k** for the slice (CONFIRM figure w/ Robert), scoped at kickoff. In-team dev QA is already in the build price. Brief puts QA plan + execution on the agency (§3, §7), so this is warranted.
- Google Play Console fee. Store copy/screens/trailer are TXG's (out of scope).
- Magnetic SDK — credentials from TXG, assume no license cost to AP.

**Headline to quote (dual, Robert 2026-06-21):** **€110k** (Option A, reads-as-London, recommended) / **€121k** (Option B, street-accurate). Each = trimmed build (€92k/€102k) + QA €8k + 10% contingency. Builds trimmed ~€4k each (less pre-prod env art, no A/B). Six-week build, €80/h. Pass-through at cost. Production oversight included. Client pays Unity engine license fees.

**Named team (canonical, Robert 2026-06-19):** Tech Lead Oskar Hansen; Gameplay programmer Fredrik Laurent; Concept/art-direction + tech/character artist (AI) Hasan Chenari (100%); Environment artist (AI) Prateek Karajgikar (50% A / 100% B); shared ½ seat = Robert (production) + Tim Browne (design advisory) + Carolina (SFX/audio). No separate QA seat — device matrix/Play submission inside the team. **Spelling: Hansen confirmed.**

---

## 3. Commercial model

- **Milestone-based fixed price** over the 6-week build. Fits the fixed launch date + mandatory weekly demo.
- **Payment schedule (6-week build):**
  - 30% deposit on signature
  - 40% at mid-build milestone (Soho / Missions 1–4 demo accepted)
  - 20% on content-complete (Missions 1–6, 30 fps on min spec)
  - 10% on store-live acceptance (live in Argentina Play Store), small retention released after support window
- **Post-launch support:** 30 days for critical bug fixes + store re-submissions, capped hours, then T&M.
- **Scope-change:** weekly demo is the change surface; written change orders for anything beyond §3 against the rate card.

---

## 4. Assumptions / open items for Robert
1. **AI-assisted production** carries the environment + character volume; output kept sensible and matched to the client art style. Specific tools chosen to fit that style (not auto-picked).
2. **Mapping** — recommended route is geo→3D reconstruction (OSM/OS footprints+heights → stylised, baked), not Mapbox-at-runtime. Mapbox = fallback/reference. Modelled on the geo-data-to-3D-environment ("track mapper") technique.
3. **No designer line** — Tom is the design resource; Tech Lead carries design capacity to drive calls.
4. **Scope vs 6 weeks** — leans on prototype + GDD being build-ready at kickoff, polish concentrated on M1/first-30s, NPC variants reused, M2–6 art lean. "Weekly demos to end-Q4" read as: build in 6 weeks, then TXG balancing/soft-launch tail.
5. **5-dev ceiling vs 4-dev lean** — which to quote (or the band). 5th seat is QA full vs part-time.
6. **Sourcing** — which roles in-house vs sub-studio under back-to-back NDA (cost, not client price).
7. **Contracting entity** — which AP entity signs (NOT APDS AB / konkurs).
8. **Kickoff date** — sets when the 6-week clock starts against end-Q4.

---

## 5. Reprice to updated brief (2026-07-03, round 8) — CURRENT

**Trigger:** Tom's 29 Jun updated brief (GDoc `1HKPJ-O0u8h_tuYEag3_EzE3UD26NTQUEVwaIxYD1Z1A`). Scope down: **6→4 missions, all Soho, no Mayfair map, ~90→~60 min.** Art A/B already removed (client tests style themselves). Brief adds spec (10 targets/20 portraits + named crew, UI = top production priority, AI-assisted encouraged). Mayfair gone ⇒ Option B (street-accurate Soho+Mayfair) mooted ⇒ **single quote.**

**New rate card applied** (canonical: `memory/reference_rate_card.md`, added this session). Bottom-up on the tighter scope, **5-week build**, mid-band rates:

| Role | Person | Band | SEK/h | Alloc (200h=1.0 FTE) | SEK |
|---|---|---|---|---|---|
| Tech Lead | Oskar Hansen | Senior | 775 | 1.0 (200h) | 155,000 |
| Gameplay prog | Fredrik Laurent | Senior | 775 | 1.0 (200h) | 155,000 |
| UI / systems prog | Petter | Interm. | 600 | 0.6 (120h) | 72,000 |
| Art dir / character | Hasan Chenari | Art Lead | 725 | 0.7 (140h) | 101,500 |
| Environment (Soho) | Prateek Karajgikar | Artist | 475 | 0.5 (100h) | 47,500 |
| Production / EP | Robert | EP | 1000 | 0.3 (60h) | 60,000 |
| Design advisory | Tim Browne | Senior | 775 | ~25h | 19,375 |
| SFX / audio | Carolina | Sound | 475 | 0.25 (50h) | 23,750 |
| **Build subtotal** | | | | ~4.5 FTE | **634,125 SEK** |

- Build ≈ **€55.6k** @ 11.4 EUR/SEK (blended ~€62/h vs old €80/h). + Northify QA €8k + 10% contingency ⇒ **card-derived floor ≈ €69k.**
- **Decision (Robert): hold margin, quote €85k single number.** Rationale: a clean ~23% cut off the accepted €110k passes the scope savings to the client (good faith in a shortlist round) while keeping ~€15k margin over the cost floor on a fixed-date job, and stays comfortably sub-€100k. Floor to not undercut was ~€75k.

**Client-facing decomposition (pitch page + one-pager):** **€85k = Build €69k + QA (Northify) €8k + 10% contingency.** Senior team, five-week build. Milestones 30 / 40 (M1 slice + Soho map) / 20 (content-complete, all four missions) / 10 (store-live). Unity license with client; full IP transfer on delivery; pass-through at cost.

**Delivered 2026-07-03:** pitch page + one-pager updated + PDF regenerated; Gmail draft r-2315103627119601564 (PDF attached) created on thread `19ebb4a5e69ab2ab`, **NOT sent** (Robert sends). See output_log round 8.
