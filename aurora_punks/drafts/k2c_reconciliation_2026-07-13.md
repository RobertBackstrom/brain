# K2C revenue reconciliation - Erik/Afrime data room

**Datum:** 2026-07-13 - **DRAFT** (CorpBot)
**Syfte:** Reconcile the three K2C figures that don't line up before the data room ships.
**Sources:** AP P&L 2026 (`1ml7Ba...`, tab `ap_pnl_2026`, K2C line = row 10), K2C sub-model (`1xlHrzO...` `k2c_pnl_2026` - now migrated as a tab into the AP workbook; standalone is LEGACY), K2C milestones (`1A_IzD...`), H1 board avstämning (`h1_2026_avstamning_board.md`).

## The three numbers - what each actually is

1. **~5.6M SEK (5 600 000)** = K2C / Raw Fury co-dev **gross contract envelope**, whole contract. Confirmed by the milestone sheet: MS1-MS7 = 15/15/10/10/15/20/15 % = 100 % = 5 600 000 SEK. This is gross RF milestone revenue, before any subcontractor cost.

2. **964 669 SEK** = the "K2C" line in the AP P&L (`ap_pnl_2026!O10`). This is **NOT AP revenue** - it is AP's **net margin** on K2C. In the consolidated AP P&L, K2C is booked as a single net intercompany contribution line (revenue minus all subcontractor cost), because the gross revenue and the subcontractor costs both live in the K2C sub-model / CZP books. So "K2C = 964 669" on the AP P&L is profit, not turnover.

3. **~1M SEK** = the **same thing as #2**, rounded. The standalone K2C sub-model computes net P&L = 993 131 SEK (row 24/25). The live AP workbook tab shows 964 669. The ~28k gap is a MS2/Jul sync drift between the legacy standalone (174 142) and the migrated live tab (145 679); the live AP workbook is source of truth (the standalone header flags itself as legacy). "~1M", "993 131" and "964 669" all describe one quantity: AP net margin.

**Bottom line: there are only TWO real numbers, not three.** 5.6M gross envelope, and ~0.96M net margin. The "third" number is the net margin rounded.

## The math (K2C sub-model, whole contract 2026)

| Line | SEK |
|---|--:|
| RF milestone revenue (gross, MS1-MS7) | 5 600 000 |
| Subcontractors (Tim/Bright Gambit, Fredrik/Ark Island, Oskar/Skokloster, Robert/CZP, Imi/Red Marmoset, Lost Hive, Carolina) | 4 188 062 |
| Contingency (10 %) | 418 806 |
| **Total cost** | **4 606 869** |
| **AP net margin (P&L)** | **993 131** (sub-model) / **964 669** (live AP workbook) |

Net margin as % of gross ≈ 17 %.

## Corrected figures to present

- **(a) K2C gross contract value:** **5 600 000 SEK** (Raw Fury co-dev, 7 milestones, one contract).
- **(b) AP net margin:** **~965 000 SEK** (964 669 live; ~993k in the sub-model), after ~4.61M subcontractor + contingency cost. ≈17 % net.
- **(c) 2026 portion vs total:** the **entire** contract executes in calendar 2026. MS0 signature 2026-04-15, MS7 Gold 2026-12-03; the Jan-27 column is 0. So 2026 portion = total: 5.6M gross / ~965k net, no spill into 2027.
- **(d) End date:** **MS7 - Release / Gold, target 2026-12-03** (RC MS6 2026-10-23; Content Complete MS5 2026-09-25).

## Data-room-ready note (K2C revenue)

> Aurora Punks holds a co-development contract with Raw Fury for the Sands of Duat / Pharaoh Lands DLC, gross value 5.6M SEK across seven milestones running April to December 2026 (Gold on 2026-12-03). AP subcontracts the bulk of the work (art, engineering, audio), so its retained net margin on the engagement is roughly 0.96M SEK (about 17 %). The 964 669 SEK figure that appears on the AP P&L is that net margin, not gross revenue - the full 5.6M is the top-line contract value.

## Watch-outs for the data room
1. Do not present 964 669 as "K2C revenue" - it is net margin. Label it clearly, and cite 5.6M as the contract value alongside.
2. The standalone K2C sheet (`1xlHrzO...`) is legacy - it self-flags as no longer source of truth. Use the `k2c_pnl_2026` tab inside the AP workbook (`1ml7Ba...`) for any live figure.
3. Minor ~28k reconciling item between legacy (993 131) and live (964 669) sits in the MS2/Jul month; harmless for the data room but worth a one-line note if a granular monthly split is shown.
