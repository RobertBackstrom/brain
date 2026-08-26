# Legal Analysis - Erik Reynolds / Afrime into Aurora Punks (3 workstreams)

**Status:** DRAFT - internal legal analysis/strategy only. Nothing drafted for external send, nobody contacted, nothing filed.
**Date:** 2026-07-07
**Prepared by:** Lawyer agent
**For:** Robert, then external counsel (Marc Harris / Dangoor - corporate; Sifferrådet / Henrik Franzén - tax; US counsel - Afrime-side project stake)
**Grounding docs read:** `ap_ip_ownership_canonical.md`; `drafts/erik_reynolds_data_room_MASTER_DRAFT.md`; the 2023-06-29 Samarbetsavtal Runatyr-AP + 2025-03-28 tillägg (gdrive `19CaIVH9...`); `rlr-000-epic.md`; court decision K 4429-25 (APDS bevakning); Runatyr-CZP kvittning + momsdeklaration drafts; Henrik Franzén "Fodran på Runatyr" mail chain Mar-May 2025; company-structure reference; `wiki/legal/` KB.

---

## 0. Executive summary - read this first

**Top 5 risks (ranked):**

1. **The RLR ownership premise in the data room is wrong as drafted, and the fix is the single hardest legal problem in the deal.** RLR IP is **not** in AP and is **not "partly already in AP."** Per the 2023-06-29 Samarbetsavtal §1.1, **Runatyr AB owns the RLR IP** (and the Elric licence). AP never acquired Runatyr and holds only a **contractual 5M SEK loan claim** on Runatyr (tillägg 2025-03-28 §4.1-4.2), whose contemplated repayment mechanism is a **future sale of RLR+Elric from Runatyr to AP** (§4.3) that **has not happened.** Erik is being invited to value AP on a catalog whose flagship title AP does not yet own. **CRITICAL.**

2. **There is an unpaid ~1,000,000 SEK output-VAT liability sitting in Runatyr from a related-party paper transaction, and Robert is personally on the hook for it (företrädaransvar).** In Mar-May 2025 Runatyr invoiced APDS ("APDEV") **4,000,000 SEK + 25% moms** for "Robot Lord Rising samt Elric källkod och assets", "paid" same day by kvittning (Henrik/Frida Swan chain). That invoice created ~1M SEK output VAT in Runatyr. If it was not reported/paid (the pending "Momsrättelser Q2 2025" in run-006 strongly suggests it was not), Robert as **VD + firmatecknare of Runatyr** carries personal liability under **SFL 59 kap. 13 §**. **CRITICAL.**

3. **The 5M receivable and the RLR "sale" may sit in the bankrupt APDS estate, not in AP.** The tillägg is AP-Runatyr, but the accounting was booked in APDS ("Jag har nu lagt mottaget skadestånd i APDEV 5Mkr med fordran på Runatyr", Henrik 5 May 2025). APDS is in konkurs (K 4429-25, bevakningsdeadline **21 July 2026**). If the RLR-linked receivable is an APDS estate asset, the path to RLR runs through **trustee Nils Åberg (Carler)**, not through AP - and the canonical doc's "AP holds the 5M receivable" is then also wrong. This must be resolved before any RLR step. **CRITICAL / time-boxed to 21 Jul 2026.**

4. **A controlled Runatyr bankruptcy followed by AP buying RLR from the estate is a textbook återvinning + otillbörlighet target, because every party in the chain is närstående.** Runatyr is 50% CZP / 50% Yasin, Robert is CZP's 100% owner and Runatyr's VD/firmatecknare, and AP is CZP-affiliated. A related-party asset sale out of a VAT-owing estate, at anything below defensible market value, is challengeable **without any backward time limit** under KonkL 4:5 (närstående) and for two years under KonkL 4:10. **HIGH.**

5. **A raise/option-ladder toward Erik control is not Robert's to give - it triggers Behold's 32% block, pre-emption, and ABL 8:23 self-dealing on nearly every step Robert touches.** Negative equity (parent equity ~ -1.58M USD) plus ~1.2M SEK related-party owner loans also raises a live **kontrollbalansräkning** question (ABL 25:13). **HIGH.**

**Single most important sequencing recommendation:**
> **Do the Runatyr VAT and RLR-title cleanup FIRST, and do it under the new företrädaransvar "rådrum" regime that took effect 1 July 2026 - before any controlled bankruptcy, before the APDS bevakning deadline (21 Jul 2026), and before RLR is presented to Erik as an AP asset.** The order is: (1) quantify + regularise the Runatyr VAT and apply for rådrum (SFL, new rules in force 2026-07-01); (2) establish where the 5M receivable and any RLR "sale" actually sit (AP vs APDS estate) and file AP's bevakning in APDS by 21 Jul if AP is the true creditor; (3) only then design the cleanest RLR-into-AP route - which may be a **direct arm's-length purchase from a solvent Runatyr financed by the loan set-off, avoiding bankruptcy entirely**, rather than the "controlled bankruptcy then buy from estate" plan. Solvent transfer is materially cleaner than the bankruptcy route on both återvinning and företrädaransvar. Everything Erik-facing (issue, options, IP contribution) sits downstream of this cleanup.

**Correction to canonical / data room:** `ap_ip_ownership_canonical.md` line 20 ("RLR ... possibly already partly in AP" / "Investigate whether RLR is already legally in AP") and the master draft §5 should be updated: **RLR is legally in Runatyr; AP holds a contractual claim only; the contemplated vehicle is a Runatyr->AP IP sale, per the signed 2025-03-28 tillägg §4.3.**

---

## Workstream 1 - RLR recovery and the Runatyr VAT / bankruptcy question (HIGHEST sensitivity)

### 1.1 What the documents actually establish

1. **2023-06-29 Samarbetsavtal (Runatyr / AP), signed Robert for Runatyr, Mattias Wiking for AP:**
   - §1.1 "Runatyr äger de immateriella rättigheterna (IP) till Robot Lord Rising och spel-licensen för Elric of Melniboné." **Runatyr owns RLR.**
   - §1.2-2.2 AP intended to buy a **majority of Runatyr's shares** (not the IP), and to fund development pending that share deal.
   - §3.1 If no majority-share transaction by **2025-02-01**, AP gets a **5M SEK skadestånd** as compensation for its development costs, as a **fordran on Runatyr** (§3.2).
2. **2025-03-28 tillägg (same signatories):**
   - §4.1 Confirms AP did not become majority owner -> 5M SEK claim arises; actual worked-up costs stated at **6,790,780 SEK**.
   - §4.2 The claim is booked as an **interest-free loan**.
   - §4.3 "Återbetalning av lånet ska ske genom **försäljning av IP:n Robot Lord Rising och Elric of Melniboné från Runatyr AB till Aurora Punks AB** enligt separata överenskomna villkor." **The intended exit is a sale of the IP into AP - not yet executed.**
3. **Parallel accounting construction (Henrik Franzén / Frida Swan chain, 31 Mar - 5 May 2025):** Runatyr invoiced **APDS ("APDEV") 4,000,000 SEK + 25% moms** for "Robot Lord Rising samt Elric källkod och assets", dated 2025-03-28, "paid" same day by **kvittning**; APDS booked "mottaget skadestånd 5Mkr med fordran på Runatyr", split 2.5M/2.5M RLR/Elric.
4. **Runatyr ownership + status:** 50% Yasin Hillborg / 50% CZP (AP-funded but share transfer unexecuted); Robert is VD + firmatecknare; Runatyr was already at bankruptcy's edge in Oct 2024 over an 11.5K SEK shortfall; pending momsrättelser for Q4 2024 + Q2 2025 (run-006). Yasin has asked for a documented Runatyr->RLR licence and his 25,000 SEK back to exit (Jul 2025 mail).

**Legal conclusion on "is RLR already in AP":** No. AP holds a **loan receivable**. Title sits in Runatyr. The 2025-03-28 tillägg is an agreement to sell in future, on terms "to be separately agreed" - i.e. an unperfected obligation, not a conveyance. There is also an **unresolved conflict** over whether the RLR "sale" and the 5M receivable live in **AP** (per the tillägg) or in **APDS** (per the booking). This conflict is the first thing to nail down.

### 1.2 Risk rating: **CRITICAL**

Three independent exposures stack here: (a) personal företrädaransvar for Runatyr VAT; (b) återvinning/otillbörlighet on a related-party RLR extraction; (c) reviving Yasin's leverage (ABL 29:1 damages claim, jäv-klander of the IP dealings) exactly when he is a 50% owner of a failing company - the pattern already flagged in lawyer_learnings 2026-05-03.

### 1.3 Företrädaransvar for the unpaid VAT - and does filing/controlled konkurs trigger or mitigate it?

**Rule:** Under **SFL 59 kap. 12-13 §§**, a representative (VD/firmatecknare) who **intentionally or through gross negligence** fails to pay the company's tax or VAT is **personally jointly liable**. Relief where, **by the original due date (förfallodagen)**, the representative has taken **verksamma åtgärder** for an orderly, creditor-collective wind-down (konkursansökan or företagsrekonstruktion). (Skatteverket rättslig vägledning; HFD 2018:4.)

**New law in force 2026-07-01 (Prop. 2025/26:52, "nya regler om befrielse och rådrum") - directly on point for this deal window:**
1. **Rådrum:** the representative can **apply for a two-month rådrum** from the original due date; during it, the assessment of personal liability **moves from the original förfallodag to the end of the rådrum period**. This buys a legitimate, statutory window to arrange an orderly settlement without the liability crystallising.
2. **Befrielse:** relief is broadened to "**oskäligt**" (unreasonable to hold the representative liable), with enumerated factors, replacing the narrower prior standard.

**Application:**
1. Deliberately bankrupting a VAT-owing company **does not extinguish** already-accrued företrädaransvar. If the ~1M SEK VAT was already due and unpaid through grov oaktsamhet, konkurs now does not erase Robert's personal exposure for it - it is assessed as of the **due date**, not the konkurs date.
2. The mitigant is **timing and process, not the bankruptcy itself.** The clean posture is: quantify the VAT, get current filings/rättelser in, **apply for rådrum** for the amounts first falling due, and either pay or take verksamma åtgärder within the rådrum window. Doing this shifts the liability-assessment point and evidences good faith (defeating "grov oaktsamhet").
3. **Prefer solvent regularisation over "controlled bankruptcy."** A controlled bankruptcy of a VAT-owing near-insolvent company where the sole valuable asset is then sold to a related party is the **worst optics** for both företrädaransvar (looks like asset-stripping ahead of the fisc) and återvinning. If Runatyr can be kept solvent long enough to (a) regularise VAT and (b) sell RLR to AP at market with the 5M loan set off against price, the estate/trustee is never involved and the återvinning window never opens.

### 1.4 Återvinning (KonkL 4 kap) and otillbörlighet on a related-party RLR sale

**If a Runatyr bankruptcy does happen and AP buys RLR from the estate:**
1. **Närstående status.** Runatyr and CZP/AP/Robert are närstående within **KonkL 4 kap. 3 §** (common control / owner sphere). This is the decisive multiplier.
2. **KonkL 4 kap. 5 § (otillbörlig transaktion).** A transaction that improperly favours one creditor, withdraws property from creditors, or over-indebts the debtor is recoverable. For **närstående there is no backward time limit** (the five-year cap that applies to non-related parties does not bind related parties). A below-market RLR sale to AP, or set-off of AP's own loan against the price, is squarely inside this.
3. **KonkL 4 kap. 10 § (betalning/set-off of debt).** Using AP's 5M loan claim to "pay" for RLR is a recovery risk; for **närstående the look-back is two years** (vs three months). Set-off in konkurs is further constrained by **KonkL 5 kap. 15-16 §§** (set-off barred where the claim was acquired/arose in a recoverable manner or too close to konkurs).
4. **Skatteverket as VAT creditor** would be a motivated party pushing the trustee to challenge, given the VAT sits unpaid.
5. **Arm's-length pricing is mandatory and must be independent.** RLR must be valued by a **neutral third party** (not Robert's own cost figure of 6.79M), the price actually paid in cash or by defensible set-off, and the board of Runatyr (excluding Robert on jäv, **ABL 8 kap. 23 §**) plus the AP board (excluding Robert) must approve on documented minutes. Note Yasin as 50% Runatyr owner would need to be handled - his consent or a clean buy-out removes a klander risk.

### 1.5 Recommended structure (cleanest defensible path)

**Route A (preferred) - solvent Runatyr, direct IP purchase into AP, no bankruptcy:**
1. Regularise Runatyr VAT (file rättelser, apply rådrum, pay). Keep Runatyr solvent.
2. Resolve Yasin: buy out his 50% or obtain written consent to the IP sale, returning his 25,000 SEK; document a Runatyr->RLR chain-of-title note answering his "no outsourcing/assignment agreement existed" points (see lawyer_learnings 2026-05-03 - the intra-group IP transfer must be *documented*, not asserted).
3. Independent valuation of RLR + Elric.
4. Runatyr sells RLR (and Elric, if any residual value - canonical says Elric is dead, so likely RLR only) to AP at that value; consideration = **set-off against the 5M loan** to the extent defensible, cash for any balance, with output VAT correctly charged and paid by Runatyr (AP recovers input VAT).
5. Board approvals both sides with Robert recused (ABL 8:23); minutes disclosing the related-party nature.
6. Result: RLR is cleanly in AP with a documented, VAT-correct, arm's-length, board-approved title - **exactly what Erik's DD will test.**

**Route B (only if Runatyr is already unavoidably insolvent) - konkurs then estate purchase:**
1. Robert takes verksamma åtgärder / rådrum on VAT **before** any konkurs to cap företrädaransvar.
2. Let the trustee run the estate; AP bids for RLR **at independent market value, in cash**, in open process - never a negotiated related-party set-off. A trustee-blessed, market-priced sale is the återvinning-proof version, but it is slower, gives the trustee/Skatteverket leverage over price, and risks a competing bidder for RLR.

**Route A is strongly preferred.** Route B's only advantage (a trustee "clean-hands" stamp) is outweighed by loss of price control, the företrädaransvar optics, and the possibility that RLR is dragged into the APDS estate question (1.6).

### 1.6 The APDS-estate ambiguity (must resolve by 21 Jul 2026)

1. Establish **in whose books the 5M receivable-on-Runatyr and the 4M RLR "sale" actually sit** - AP or APDS. Pull Runatyr's, AP's and APDS's 2025 ledgers and the actual invoice.
2. If the receivable is an **APDS estate asset**, then: (a) AP does *not* hold it, and (b) the RLR settlement path runs through **trustee Nils Åberg (Carler)** - AP would need to buy the receivable (or RLR itself) from the APDS estate. **File AP's bevakning in APDS by the 21 July 2026 deadline** (K 4429-25) to preserve any AP claim regardless; a protective bevakning costs little and missing it is fatal (claims after 21 Jul are excluded).
3. If the 4M invoice was a genuine sale of "RLR källkod och assets" to APDS in Mar 2025, the **source/assets may be APDS estate property** even though the trustee has (per rlr-000) signalled no IP claim - get that in **writing from the trustee** ("boet gör inte anspråk på RLR-IP") before relying on it, per the estate-property rule in `wiki/legal/sv_corp_law.md` (KonkL 3:1-2, 7 kap).

### 1.7 Lagrum - Workstream 1

- **SFL (2011:1244) 59 kap. 12-13 §§** - företrädaransvar; verksamma åtgärder by due date. **New befrielse + rådrum rules in force 2026-07-01 (Prop. 2025/26:52).**
- **KonkL (1987:672) 4 kap. 3 §** (närstående), **4 kap. 5 §** (otillbörlighet, unlimited look-back for närstående), **4 kap. 6 §** (gåva, 3 yr närstående), **4 kap. 10 §** (betalning, 2 yr närstående); **5 kap. 15-16 §** (kvittning i konkurs); **3 kap. 1-2 §, 7 kap.** (estate property/administration).
- **ABL 8 kap. 23 §** (jäv on the related-party sale), **ABL 29 kap. 1 §** (director damages exposure to Runatyr/Yasin).
- **ML / SFL** VAT accrual on invoice (the 25% moms became due when the 4M invoice was issued, kvittning notwithstanding).
- **URL** - RLR chain of title (Runatyr acquired economic rights from Yasin via employment; document it - lawyer_learnings 2026-05-03).

### 1.8 External counsel - Workstream 1

- **Insolvency/tax-litigation advokat** (not general corporate): företrädaransvar strategy + rådrum application, and the återvinning-proof structuring. This is the highest-stakes external need in the whole deal.
- **Sifferrådet / Henrik Franzén:** quantify the exact unpaid VAT, file rättelser (Q4 2024, Q2 2025), and confirm where the receivable/sale are booked.
- **Carler (Nils Åberg / Ulrika Mattsson):** written confirmation on APDS estate's non-claim to RLR + the bevakning filing.
- **URL specialist** only if Yasin escalates.

---

## Workstream 2 - Behold, pre-emption and the staged path-to-control

### 2.1 The core problem

Erik's "Tencent-style" ladder (20-30% now, options toward majority/full) cannot be delivered by Robert selling CZP's shares. Majority/full control of AP means **diluting or acquiring Behold's 32.26%** and every other holder. That requires either (a) new-issue dilution that all shareholders' pre-emption rights bite on, or (b) secondary purchases that any hembud/förköp in the aktieägaravtal governs. Robert controls only CZP's 30.14%.

### 2.2 Risk rating: **HIGH**

Behold (KM Troedsson sits on the AP board) is a professional VC with WISE instruments already converted; they will have negotiated pre-emption, anti-dilution triggers, information and possibly consent rights. **Action item: read the actual AA + WISE 1/WISE 2 agreements** - the data room notes "no anti-dilution / no liquidation preference in the base model" but flags these must be read from the actual instruments if triggered. Do not design the ladder until those are read.

### 2.3 New issue (nyemission) mechanics

1. **Company-law competence.** A nyemission is decided by **bolagsstämma** (ABL 13 kap. 1 §), or by the board under a **stämmobemyndigande** (ABL 13 kap. 35 §) or subject to stämma ratification (13 kap. 31 §). An issue large enough to move control needs stämma.
2. **Pre-emption / företrädesrätt.** Existing shareholders have statutory företrädesrätt to a cash issue pro rata (**ABL 13 kap. 1 §**). To let Erik in, either every shareholder waives (avstår) their företrädesrätt, or the stämma resolves a **riktad nyemission** (directed issue) disapplying företrädesrätt, which needs **9/10 majority** of votes and shares represented (**ABL 13 kap. 2 §**). With Behold at 32%, **a directed issue cannot pass over Behold's objection** - Behold's alignment is structurally required, not optional.
3. **Aktieägaravtal.** Separately from the ABL default, the AA likely contains pre-emption/hembud/förköp and possibly drag/tag. These are contractual and bind the parties even where ABL would allow the issue; a breach is a damages/■specific-performance matter between shareholders. Map the AA before any term sheet.

### 2.4 The option ladder - how to paper it enforceably under Swedish law

1. **Teckningsoptioner (warrants, ABL 14 kap.)** are the clean Swedish vehicle for "the right to subscribe more later": stämma issues teckningsoptioner (14 kap. 2 §, directed grant needs the same 9/10 as a directed issue, 14 kap. 2 § jfr 13 kap. 2 §), with fixed subscription price and window. This gives Erik a real, registered right to move from 20-30% upward without re-running a stämma each rung.
2. **Contractual call options over existing shares** (to reach majority/full from other holders) are enforceable as ordinary contracts, but **specific performance of a share transfer is weaker in Swedish law than in common-law**; back them with (a) pledged shares / aktiepant, (b) irrevocable powers, (c) liquidated-damages, and (d) alignment with any AA drag-along so a majority can compel the tail. Do **not** rely on a bare "option to buy Behold's shares" - Behold must be a signatory to whatever ladder touches its stake.
3. **Staged valuation.** Each rung's price/valuation must be fixed or formula-based up front (anti-sandbagging both ways). Cross-check against 3:12/förmånsbeskattning only to the extent any Swedish individuals receive options as comp (not the case for Erik, a US investor - but check if Robert/team get anything).
4. **Board vs stämma.** Grant of teckningsoptioner and any directed issue = **stämma** (with 9/10 for directed). Robert **cannot** grant these at board level, and on every step where CZP/Robert is on both sides (e.g. CZP also subscribing, or the IP contribution below), **ABL 8 kap. 23 § jäv** requires Robert to recuse and the independent directors (Mattias, Alexander, Andreea, KM) to carry the decision - mirroring the K2C AP-side convention (Mattias + Andreea sign, Robert abstains).

### 2.5 Sequenced actions - Workstream 2

1. Read AA + WISE 1/WISE 2 + bolagsordning (hembud/förköp/samtycke; anti-dilution; consent thresholds). Marc Harris holds the authoritative cap table and likely the instruments.
2. Get **Behold's in-principle alignment** before any Erik term sheet - a control ladder is dead without it. Frame it as recap + growth capital, not a squeeze.
3. Decide vehicle: **entry = directed nyemission (9/10 stämma)**; **upside = teckningsoptioner (ABL 14 kap.)**; **control tail = contractual call options + AA drag**, all in one shareholders'-level agreement Erik + Behold + CZP + material holders sign.
4. Calendar the stämma(s); prepare kallelse + majoritetskrav; pre-clear the 9/10 count.
5. ABL 8:23 governance memo for every step Robert is conflicted on (recusal + independent-director sign-off + minutes disclosing the related-party nature).

### 2.6 Lagrum - Workstream 2

- **ABL 13 kap. 1, 2, 31, 35 §§** (nyemission, företrädesrätt, directed-issue 9/10, bemyndigande).
- **ABL 14 kap. 2 §** (teckningsoptioner; directed grant majority).
- **ABL 4 kap.** (share classes/rights, equal-treatment likhetsprincipen 4 kap. 1 §).
- **ABL 8 kap. 23 §** (jäv), **7 kap.** (bolagsstämma), **8 kap. 34 §** (jäv styrelse for related-party).
- Aktieägaravtal (contractual pre-emption/hembud/drag - read the live instrument).

### 2.7 External counsel - Workstream 2

- **Marc Harris / Dangoor (corporate):** cap-table mechanics, the directed-issue + teckningsoptioner package, AA interplay, drafting the ladder. This is Marc's core lane.

---

## Workstream 3 - IP contribution, cross-border capital, project stake, and balance-sheet cleanup

### 3.1 Apportemission to move CZP catalog IP into AP (no cash)

**Risk rating: MEDIUM-HIGH** (mechanically doable, but valuation + kontrollbalans interact).

1. **Vehicle.** A non-cash issue (**apportemission**) where CZP subscribes for new AP shares and pays with **apportegendom** = the catalog IP (BlockEm, Chenso Club, Ooglians, 1993, Beyond the Filter, plus RLR *once it is cleanly in CZP/AP per Workstream 1*). Decided by stämma (or board under bemyndigande), **ABL 13 kap. 1 §**, with the apport specified in the beslut.
2. **Revisorsyttrande (mandatory).** An apportemission requires an **auditor's statement** under **ABL 13 kap. 7-8 §** (jfr **2 kap. 19 §** at formation) confirming the apportegendom is (a) useful to the company and (b) **not valued above its real worth**. The IP must be **independently valued**; the auditor will not sign off on Robert's internal cost figures. Christine Lef (Parameter Revision) or the appointed revisor issues this.
3. **Chain of title first.** The auditor and Erik's DD both need each asset's **documented ownership** in CZP (ex-APDS-estate acquisitions: get the estate purchase docs; the WLBS->APDS->CZP chain; Meta agreement status on Beyond the Filter; Neon Artery buyout clause on Vessels of Decay). Per lawyer_learnings 2026-05-03, intra-group IP ownership must be **documented, not asserted** - acute here because the assets passed through two bankruptcies.
4. **Related-party.** CZP subscribing an apportemission in AP is a related-party transaction (Robert both sides): ABL 8:23 recusal + independent-director approval + disclosed minutes; likhetsprincipen (4:1) - other shareholders' pre-emption is displaced by a directed apportemission, so **9/10 majority** applies (13 kap. 2 §) -> Behold's alignment again required.
5. **Tax (CZP side).** Contributing IP to AP for shares is a **disposal (avyttring)** by CZP at market value for tax - potential capital gain in CZP if the IP's tax basis is below the apport value; but näringsbetingade andelar rules and the fact CZP receives shares (not cash) affect timing. **Sifferrådet must model the CZP-side tax** before the apport value is fixed - a high valuation helps Erik's AP story but can create a taxable gain in CZP.

### 3.2 Malformation 10% + 5 Fortress <10% at ">=1.5x ROI in AP shares" (apb-037)

**Risk rating: MEDIUM.** Same apportemission machinery (these are share-for-share swaps: CZP contributes the minority stakes, receives AP shares). Additional points:
1. The "**>=1.5x ROI in AP shares**" mechanic is a **valuation/ratio term**, not a legal structure - it must resolve to a fixed number of AP shares at a fixed AP valuation for the revisorsyttrande to be signable. "1.5x ROI" cannot appear in the emissionsbeslut; a share count can.
2. Each target company's **own hembud/förköp/samtycke** may bite on CZP transferring the stake into AP - read those bolagsordningar/AA (Malformation, 5 Fortress).
3. Keep these on the separate **CorpBot + BizDev + Lawyer** session (apb-037) as canonical directs - do not fold into the main raise timeline.

### 3.3 Kontrollbalansräkning duty (negative equity)

**Risk rating: HIGH and possibly already live.**
1. **Trigger.** Under **ABL 25 kap. 13 §**, the board must **genast** prepare a **kontrollbalansräkning (KBR)** when there is reason to believe the company's equity is **below half the registered share capital** (or when enforcement under UB 4 kap. shows insufficiency). AP's parent equity is materially negative (~ -1.58M USD per the consolidated line) and the data room itself notes ABL kapitalskydd **blocked** repayment of the owner loans until Jul 2026 - that is direct evidence the board already had reason to suspect kapitalbrist.
2. **Consequence chain.** KBR -> if kapitalbrist confirmed, **first kontrollstämma** (25:15); 8-month rådrum to restore equity to full registered capital, then **second kontrollstämma** (25:16); failure -> board must file for likvidation (25:17), and **personligt medansvar** for board (and others acting) attaches for obligations incurred during a period of neglect (**25:18**). Robert as de facto deputy VD + director is in scope.
3. **Cure.** The Erik raise + the owner-loan-to-equity conversion + the apport IP are precisely what **restores equity** and cures the KBR exposure - but the **KBR must be prepared now on a proper going-concern/övervärde basis** (KBR permits booking assets at real value incl. justerat eget kapital, so the catalog IP's true value and any övervärden can be brought in), not deferred until the raise closes. **This is time-sensitive: do the KBR before, not after.**
4. Confirm with Sifferrådet + revisor whether a KBR was already triggered by the 2025 accounts; if so, the clock/medansvar analysis needs a real lawyer immediately.

### 3.4 Converting related-party owner loans to equity

**Risk rating: MEDIUM.**
1. The ~1.2M SEK owner loans (Byberg, Loot Spawn, Alexander, Mattias, CZP, Deko Du, WLBS tail) can be converted by a **kvittningsemission** (set-off issue): creditors subscribe new AP shares and pay by setting off their loan claims (**ABL 13 kap. 41 §** - the beslut states the set-off right; requires a **revisorsyttrande** on the claims' existence and value, 13 kap. 42 §).
2. This both **removes debt** and **lifts equity** - a double benefit for the KBR cure and Erik's clean-cap story.
3. Related-party (several creditors are shareholders/board): ABL 8:23, and directed -> 9/10. The **Deko Du overdue** (since 2023-10-20) and the **WLBS 500K tail with 10% guarantee** need individual treatment - the WLBS tail especially (it "fell due at WLBS wind-down") may not be a clean AP obligation; verify it is AP's debt before converting.
4. Watch **förtäckt värdeöverföring / 3:12** only if any conversion is at off-market share price to an insider - convert at the same price Erik pays (or a defensible KBR-based price) to avoid recharacterisation.

### 3.5 Cross-border: US capital into a Swedish AB

**Risk rating: MEDIUM (flag-heavy, Sifferrådet-owned).**
1. **Equity vs convertible.**
   - *Direct equity subscription:* Erik's USD buys newly issued AP shares. **No Swedish withholding on a share subscription** (it is capital in, not income out). Simplest.
   - *Convertible (konvertibel, ABL 15 kap.):* debt that converts; interest paid to a US holder can attract Swedish tax considerations, but Sweden generally does **not** levy withholding on interest to non-residents (no räntekällskatt) - still, confirm treaty/anti-abuse. Convertibles help bridge valuation disputes and can be cleaner pre-KBR.
2. **Kupongskatt (withholding on dividends).** **Kupongskattelagen (1970:624)** imposes **30% withholding on dividends** paid by a Swedish AB to a non-resident, **reduced by the Sweden-US tax treaty** (typically to 15%, or 5% for >=10% corporate holders, 0% in some pension cases). This bites only on **future dividends** to Erik, not on his investment in - but model it now so the return expectations are set correctly. If Erik invests via a **US corporation** (Afrime/Strategic Entertainment) holding >=10%, treaty 5% may apply; via an individual, 15%.
3. **Permanent establishment (fast driftställe).** Erik/Afrime **investing** in AP does not itself create a Swedish PE. But if the "co-develop Unyverse" work means **Afrime personnel operating in/through AP in the US**, or AP staff operating in the US for Unyverse, watch for a **US PE for AP** and a **Swedish PE for Afrime** - fact-driven, flag to both Sifferrådet and US counsel. Model treaty Art. 5/7.
4. **Source-of-funds / KYC.** The brief notes Erik's $1-5M source is **unverified** (Afrime itself has only ~$400K raised and is seeking seed). Before AP issues shares against his money, run **source-of-funds diligence** - AP taking unverified foreign capital into its cap table is an AML/reputational risk, and a failed tranche mid-ladder would leave AP mis-capitalised. Make funding **tranched and condition-gated**, with each teckningsoption/rung only exercisable on actual funds received.
5. **W-8BEN-E / FATCA:** AP will need Erik's entity's US tax forms; not blocking, but Sifferrådet/revisor should have them on file.

### 3.6 AP's project stake in Afrime's games (US-law rev-share / co-ownership)

**Risk rating: MEDIUM - needs US counsel; Swedish-side asks below.**
1. **This is US-law-governed and must be drafted/reviewed by US counsel.** AP taking a "project stake" (rev-share or co-ownership) in Unyverse and future Afrime titles is a US IP/commercial contract. Do **not** let it be papered under Swedish law by default.
2. **Swedish-side asks to hand US counsel:**
   - **Characterise the stake:** is it a **revenue interest** (contractual % of net revenue - simplest, no IP co-ownership) or **co-ownership of the IP** (joint work, needing a co-ownership/exploitation agreement)? Canonical/BizDev read is rev-share, not equity in Afrime - keep it a **contractual revenue interest** to avoid AP being dragged into Afrime's cap-table/insolvency risk.
   - **Security for AP:** since Afrime is pre-seed and thinly funded, AP's rev-share should be secured - e.g. a **first charge on Unyverse net revenues**, escrow/collection-account mechanics, step-in rights, and a source-code/asset escrow so AP can complete/exploit if Afrime fails.
   - **Waterfall + audit rights:** define "net revenue", platform fees, recoupment order (AP's co-dev funding recoups first), and AP's audit rights.
   - **Change-of-control / IP-follows-the-money:** if Erik is simultaneously acquiring AP *and* AP is funding Afrime's game, map the **circularity** - AP money funds Unyverse, AP takes a stake in Unyverse, Erik takes a stake in AP. Ensure no double-counting and no related-party leakage (Erik on both sides of the Unyverse economics).
3. **Swedish tax on inbound rev-share:** AP receiving US-source royalty/rev-share may face **US withholding**; the Sweden-US treaty (royalties generally 0% under the treaty) should eliminate it with a W-8BEN-E from AP - Sifferrådet to confirm and file.

### 3.7 Sequenced actions - Workstream 3

1. **KBR now** (Sifferrådet + revisor) - do not wait for the raise. Establish whether medansvar has already begun to run.
2. Document chain of title for every catalog asset (estate docs, Meta, Neon Artery) - gates the revisorsyttrande and Erik DD.
3. Independent IP valuation (whole catalog + RLR post-Workstream-1) -> fixes the apport value.
4. Structure the recap as one coordinated set of stämmobeslut: (a) **apportemission** CZP catalog IP; (b) **kvittningsemission** owner loans -> equity; (c) **directed cash nyemission** to Erik; (d) **teckningsoptioner** ladder. Sequence so equity is restored (KBR cured) at or before Erik's cash rung.
5. Sifferrådet: CZP-side apport tax, kupongskatt modelling on Erik's future dividends, PE analysis, treaty forms.
6. US counsel: the Unyverse project-stake agreement, secured and escrowed; source-of-funds/KYC on Erik before any share issue.
7. Keep Malformation/5 Fortress on apb-037.

### 3.8 Lagrum - Workstream 3

- **ABL 2 kap. 6, 19 §** (apportegendom, revisorsyttrande at formation), **13 kap. 1, 2, 7-8, 41-42 §§** (apportemission, directed-issue 9/10, revisorsyttrande, kvittningsemission), **14 kap.** (teckningsoptioner), **15 kap.** (konvertibler).
- **ABL 25 kap. 13-18 §§** (kontrollbalansräkning, kontrollstämmor, medansvar).
- **ABL 17 kap. 1 §** (olovlig värdeöverföring - off-market conversions), **8 kap. 23 §** (jäv), **4 kap. 1 §** (likhetsprincipen).
- **Kupongskattelagen (1970:624)** + Sweden-US tax treaty (dividends Art. 10, royalties Art. 12, PE Art. 5/7).
- **IL** näringsbetingade andelar / avyttring rules for the CZP-side apport disposal (Sifferrådet).

### 3.9 External counsel - Workstream 3

- **Sifferrådet / Henrik Franzén:** KBR, CZP apport tax, kupongskatt, PE, treaty forms, VAT on inter-entity IP moves.
- **Revisor (Christine Lef / Parameter Revision):** revisorsyttrande for apport + kvittningsemission; KBR sign-off.
- **Marc Harris / Dangoor:** the emission package + governance.
- **US counsel:** the Unyverse project-stake agreement + Erik source-of-funds/KYC.

---

## Consolidated "real lawyer must review" list

1. **Insolvency/tax-litigation advokat** - Runatyr företrädaransvar + rådrum + återvinning-proof RLR route (Workstream 1). Highest priority.
2. **Marc Harris / Dangoor (corporate)** - the emission + option-ladder package, AA/pre-emption, Behold, ABL 8:23 governance (Workstreams 2 + 3).
3. **Sifferrådet / Henrik Franzén (tax)** - VAT quantification, KBR, CZP apport tax, kupongskatt, PE (Workstreams 1 + 3).
4. **Revisor (Parameter/Christine Lef)** - revisorsyttrande + KBR (Workstream 3).
5. **US counsel** - Unyverse project stake + Erik KYC/source-of-funds (Workstream 3.6).
6. **Carler (Nils Åberg)** - APDS estate non-claim on RLR + AP bevakning by 21 Jul 2026 (Workstream 1.6).

**I am not a licensed advokat. This is a first-read internal analysis to focus the external hours, not legal sign-off. Every structural step above (especially the Runatyr VAT/bankruptcy handling, the kontrollbalansräkning timing, and the directed-issue majorities) must be confirmed by the named counsel before execution.**

---

## Time-critical dates

1. **21 July 2026** - APDS bevakningsdeadline (K 4429-25). File AP's protective claim if AP is a true APDS creditor. Non-extendable.
2. **2026-07-01 onward** - new SFL företrädaransvar befrielse + rådrum regime is live; use it for Runatyr VAT.
3. **30 July 2026** - AP owner-loan amortisation starts (35,200 SEK/mo); interacts with KBR/kapitalskydd - decide conversion-to-equity before cash goes out.
