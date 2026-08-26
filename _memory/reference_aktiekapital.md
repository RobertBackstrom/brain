---
name: reference_aktiekapital
description: "Registrerat aktiekapital + org nr + antal aktier per bolag (AP, CZP, ...) - sätter KBR-tröskeln enligt ABL 25 kap. Verifierade värden med källa."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 659b483c-2dc4-4e2a-8b37-00cb4ed9d9aa
---

Registrerat aktiekapital per bolag. **Avgörande för KBR-tröskeln:** kontrollbalansräkning aktualiseras när EK < **hälften** av registrerat aktiekapital (ABL 25:13); för att undgå likvidationsplikt måste EK vara återställt till **hela** aktiekapitalet vid andra kontrollstämman (ABL 25:16).

| Bolag | Org nr | Aktiekapital | Antal aktier | Kvotvärde | KBR-tröskel (halva) | Läkningskrav (hela) |
|---|---|---|---|---|---|---|
| **Aurora Punks AB** | 559256-9718 | **198 086,50 kr** | 396 173 | 0,50 kr | **99 043,25 kr** | **198 086,50 kr** |
| **Creation Zero Point Holding AB** | 559182-7471 | **50 000 kr** | (ej noterat) | - | **25 000 kr** | **50 000 kr** |

**AP-källa:** Registreringsbevis Bolagsverket 2024-08-30, ärende 400338/2024 (Drive `1EPVEHQEEqZeXZ4Ghl7Am4ZH5XmbLYVCm`). Bolagsordningens gränser: lägst 125 821 kr, högst 503 284 kr - aktiekapitalet kan alltså **inte** sänkas till 25 000. Antal aktier 396 173 stämmer mot den aktuella cap tablen ([[project_aurora_punks]]), vilket indikerar att beviset fortfarande är aktuellt. Hämta färskt registerbevis före formella beslut.

**CZP-källa:** SIE-fil räkenskapsår 2025, konto 2081 (Drive `1Eyo40ygA-avpOTinYpENtaGd04n13BYP`, Fortnox-export 2026-05-13).

## Vanligt fel - läs detta

**25 000 kr är INTE AP:s aktiekapital.** 25 000 kr är det lagstadgade minimikapitalet för svenska AB sedan 2020 och en lätt förväxling. AP ligger långt över efter nyemissionerna 2020/2021/2024. Att räkna KBR-tröskeln på 25 000 i stället för 198 086,50 ger fel svar på om EK är läkt. (Roberts minnesbild 2026-07-16 var 25k; korrigerat mot registerbeviset.)

## Luckor - fyll på när värdena verifierats

- Runatyr Games - aktiekapital ej hämtat
- Zenland Games AB - aktiekapital ej hämtat
- Aurora Punks Development Services AB (559320-7466) - konkurs 12/12/2025, aktiekapital ej hämtat

Metod för att hämta: registerbevis från Bolagsverket/verksamt, eller konto **2081** i bolagets SIE-fil. Vid PDF: `pdftotext -layout` och sök "Sammanställning av aktiekapital" (utan `-layout` hamnar siffrorna i fel kolumn och tappas).

Related: [[project_ap_ek_2025_almi_agarlan]], [[project_aurora_punks]], [[reference_company_structure]], [[project_czp_finances]]
