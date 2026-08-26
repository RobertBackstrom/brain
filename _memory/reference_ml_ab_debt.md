---
name: reference_ml_ab_debt
description: "CZP:s skuld till Magnus Liljedahl AB - ursprung, saldo, kvittningsmekanik (Ha Bra Liv), ränta och Magnus 9 CZP-aktier. Underlag för skuldavstämning + ev. kvittningsemission."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 0833de4c-f544-4f81-b947-d4e43dbe7c1b
  modified: 2026-07-24T15:16:18.042Z
---

CZP Holding AB:s skuld till **Magnus Liljedahl AB** (org **559207-3968**, kontakt Magnus "Mank Flannery" bombardemagnus@gmail.com):

- **Ursprung:** revers feb 2020 på **1 300 000** (signerad PDF i gmail-personal thread `17036365493d19ca` "Lånerevers"; själva PDF:en ej maskinläst - **bekräfta exakt räntesats där**; Robert säger **4 %/år**, Henrik refererar "avtalade räntan" + fakturerade räntan månadsvis via Billogram). Lånet växte via fler utbetalningar.
- **Henriks avstämning per 2024-11-18** (gmail `1933f8a7c5d20ef1`): **3 Mkr grundlån utan amorteringskrav + 565 tkr med amorteringskrav + 67 497 kr ränta t.o.m. 2023-12-31** (de två sista som fakturor, delbetalbara).
- **Bokförd skuld (konto 2890):** IB 2025 −3 000 000 → UB 2025 −3 259 855 → **UB per 2026-06-22 = −3 139 455** (balansrapport 30/4-2026 visade −3 172 855). OBS: 2890 **VÄXTE** 2025 (reklass E17 −557 497 av 565k+ränta-delen + A322 −345 000 studsad betalning återförd), trots amorteringar.
- **Magnus egen syn (mail 2026-01-08 `19b9dceb30282769` "Skulddokumentation", ChatGPT-mall):** skuld **4 000 000 total, ~500 000 amorterat → ~3 500 000 kvar**. Han vill att Robert skriver under ett **erkännande av skuld**. OBS: detta var ett GROVT utkast, INTE avstämt.
- **HENRIKS AVSTÄMNING per 2025-12-31 (mail 2026-01-13, den auktoritativa siffran):** **Liljedahl fordran 3 302 801 kr (ev ränta oklart)** vs **CZ bokförd skuld 3 284 855 kr** → **gap endast 17 946 kr "oklart"**. Skulden är alltså i praktiken avstämd; flygbiljetten är redan inräknad. **RÄTTELSE: mitt tidigare påstående om ett ~360k-gap drivet av obokförd ränta var FEL** - byggt på Magnus grova utkast, inte Henriks avstämning. Kvarvarande oklarheter: (a) 17 946-gapet, (b) ränteläget ("ev ränta oklart" - om 4 % faktiskt fakturerats via Billogram eller inte), (c) SIE-böckerna visar UB 2025 = 3 259 855, dvs 25k lägre än Henriks 3 284 855 (årsskiftes-timing). Ränta bokförs INTE löpande på 2890.
- **4 %-räntan gäller PER DELUTBETALNING från insättningsdatum** (lånet kom i omgångar 2020-2023). 2024 SIE behövs INTE - Henriks 2025-12-31-avstämning är ankaret. Aktuellt saldo per 22/6-2026 ≈ 3,14-3,16M (3 284 855 minus 2026 amort 100k Åter Lån + 20,4k Ha Bra Liv).
- **Kvittningsmekanik:** CZP:s inköp från **Ha Bra Liv Stockholm AB** (Robert kallar det "Ett Gott Liv") bokförs **direkt mot 2890** = Magnus är kopplad till Ha Bra Liv, inköpen kvittar skulden. Ha Bra Liv-kvittning: **2025 ≈ 56 642**, **2026 YTD ≈ 20 400**. Robert nämner även **en flygbiljett** som ska kvittas (ej lokaliserad i böckerna - be Robert peka ut).
- **ÄGANDE: Robert äger CZP 100 % (500/500 aktier, bekräftat i hans egen K10 2024). Magnus Liljedahl AB har INGET ägande i CZP** (Robert 2026-07-16). Ett Henrik-mail 2022-10-20 (`183f45da...`) noterade "Magnus bolag äger 9 aktier i CZ" - det **materialiserades aldrig / återgick**; lita på K10:an, inte det mailet.
- **KVITTNINGSEMISSION-IDÉN ÄR SKROTAD** (2026-07-16): eftersom Magnus aldrig fick ägande och Robert vill behålla 100 %, blir det ingen skuld→aktie-konvertering. **Nytt upplägg: hela skulden INKL upplupen 4 %-ränta räknas fram → nytt "erkännande av skuld" → Lawyer bygger avtalet.** Ränta ska tillkomma (Robert: "vi utgår från att räntan ska tillkomma"), dvs 4 % ackumuleras och läggs på skulden.

## AVSTÄMNING 2026-07-22 (den auktoritativa siffran - byggd på FULL SIE-historik 2020-2026)

Underlag: `czp-finances/drafts/ml_skuld_avstamning_2026-06-30.csv` + `ml_skuld_underlag_till_lawyer.md`,
uppladdade till CZP `_legals/_working/` (`1QqP291eZngSdQhfFunCuBziue3Ywc3B4`).

- **Utestående kapital per 2026-06-30 = 3 103 355 kr** (Ha Bra Liv räknat inkl moms per Roberts instruktion; +6 300 vs bokfört).
- **Tranchar:** 1 300 000 (2020-11-30) + 1 063 000 (2022-06-23) + 1 700 000 omföring från 2390 (2022-12-31) + 557 497 omklassad lev.faktura 622 (2025-02-17). Amort+kvittningar −1 517 142.
- **RÄNTA - VIKTIG RÄTTELSE:** ränta HAR fakturerats löpande och bokförts på **konto 8420**: 2021 = 90 331, 2022 = 60 000, 2023 = 185 994. **Från 2024 fakturerades ingen ränta alls.** Summa fakturerat 336 325. Mitt tidigare antagande att ränta aldrig bokförts var fel - kolla alltid 8420, inte bara 2890.
- Upplupen ränta 4 % actual/365 på faktiskt dagssaldo 2020-2026H1 = **588 802**. Fakturerat 336 325 → **obetalt 252 477**.
- Fakturerad ränta 2021-2023 (336 325) **överstiger** 4 %-beräkningen för samma period (270 705) med 65 620.
- **VALD POSITION (Robert 2026-07-24): 3 355 832 kr** = kapital 3 103 355 + obetald ränta 252 477. Rak 4 % över hela lånets liv, all fakturerad ränta avräknad. Överdebiteringen 65 620 tillgodoräknas CZP. Robert valde uttryckligen det alternativ som är mest fördelaktigt för CZP.
- **Fallback om Magnus invänder mot omräkning av 2021-2023:** 3 416 893 (4 % först från 2024-01-01). Skillnad 61 061 - får inte blockera själva erkännandet.
- **Öppna punkter före påskrift:** (1) faktura 622 (632 497, 2024-11-18) bokfördes mot 2970, inte 8420 - innehåller den ränta som redan är kapitaliserad? (2) 25k-gapet SIE vs Henrik + 17 946 vs Magnus, (3) ingående moms Ha Bra Liv 6 300 - återföras? (4) A322 2025-12-31 −345 000 "inget bet återfört" bekräftas mot bank.

FRODA-lån (2842, −65 568 i böckerna) - Robert säger **löst**, böckerna släpar. Svea Ekonomi (2843) ≈ −124 137 per juni-26.
Se [[reference_company_structure]], [[project_czp_finances]].
