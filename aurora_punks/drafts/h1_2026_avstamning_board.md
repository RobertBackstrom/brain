# H1 2026 - Avstämning CZP Fortnox ↔ K2C/AP P&L (board-underlag)

**Datum:** 2026-06-22 (inför styrelsemöte 2026-06-23)
**Bolag:** Konsoliderat AP + CZP (operativt). **AP saknar räkenskapsår 2026 i Fortnox** → all AP-verksamhet bokförs via CZP. CZP-böckerna = den operativa sanningen.
**Utfall:** CZP Fortnox SIE4, räkenskapsår 2026, bokfört t.o.m. ~2026-06-22 (draget via Playwright 2026-06-22). Drive: CZP/Bokföring, id `1YYVS7Qi...`.
**Budget:** AP P&L (`1ml7Ba…`) + K2C P&L (`1xlHrzO…`). Tröskel: **5 % OCH 5 000 SEK**.

## 1. AP:s andel av intäkterna (dina 5 strömmar)
CZP-böckerna är bredare än AP. Endast dessa motparter är AP:s:
| AP-intäkt H1 | Belopp | Motsvarar AP P&L-rad |
|---|--:|---|
| Raw Fury AB (K2C) | 840 000 | K2C (MS1) |
| Netlight Consulting | 594 193 | Netlight (Gustav) |
| Shosha Games | 217 657 | WMAY/Shosha |
| Malformation AB | 135 174 | (ej i AP P&L idag) |
| Oddiko AB | 28 000 | (ej i AP P&L idag) |
| **AP-intäkt totalt H1** | **1 815 024** | |

**CZP-only intäkter (EJ AP):** Epoch 230 033, House of Elias 84 000, Beep Japan 76 109, Ark Island 42 150, BADASS 32 632, Yaozuo 32 187, Eternal Minds 14 500 netto, Reactional 3 200. → CZP totalt H1 ~2 353 000; AP-andel ~1 815 000 (77 %).

## 2. Hardware - överdraget är verkligt, men utspritt (inte på 5410)
| Komponent | Belopp | Var bokfört | Status |
|---|--:|---|---|
| Bright Gambit konkursbo (2 fakt à 36 000) | 72 000 | **konto 6991** (ej hardware-konto) | bokfört; avtal 110K → ~38K återstår att boka |
| Pleo (hardware-del) | 30 000 | **konto 1731** (Pleo-clearing) | EJ kostnadsfört än |
| Retail (Nintendo/Webhallen/Elgiganten) | ~3 400 | 5410 | bokfört |
| **Hardware totalt (hittills)** | **~105 000** | utspritt | **mot 85 000 budget → ÖVER, växer till ~140K** |

**Obs konto 5410 (33 388) är mest FELKLASSAT:** "Utlägg Robert Q1" 25 787 (innehåll ej itemiserat) + AI-prenumerationer (OpenAI/Claude/Anthropic/Cloudflare/Voyage ~3 900, borde vara programvara) + retail-hardware ~3 400. → Riktig hardware på 5410 är bara ~3 400; resten är fel konto.

## 3. Subkonsulter - bokfört utfall, mappat
| Konsult | Bokfört H1 | Konto | K2C? |
|---|--:|---|:--:|
| Skokloster (Oskar) | 275 182 | 4600 (223 620) + 6540 (51 562) | K2C/WMAY |
| Red Marmoset (Imi) | 110 553 | 4531 | K2C |
| Ark Island (Fredrik) | 87 480 | 4600 | K2C |
| Lost Hive | 13 500 | 4600 | K2C |
| Nethash | 80 000 | 4600 | EJ K2C (CZP) |
| Eternal Minds | 29 043 | 4600 | EJ K2C (CZP) |

**Tim/Bright Gambit design** syns inte som subkonsult-kostnad H1 (BG-fakturorna avser konkursboet, inte Tims arbete) - ofakturerat eller annan väg. **Flagga.**

## 4. Felklassificeringar att korrigera med Amer (påverkar AP-mappning)
1. **6540 IT-tjänster 51 562 = Skokloster/Oskar** (konsult), inte IT. Flytta till 4600/underkonsult.
2. **5410 hardware 33 388:** flytta AI-prenumerationer (~3 900) → 5420 programvara; bryt ut "Utlägg Robert Q1" 25 787 per innehåll.
3. **6991 72 000 = Bright Gambit konkursbo** - aktivera som hardware/inventarie (1220) snarare än kostnad om det är en tillgång.

## 5. Avvikelse mot budget (de poster som kan mappas till AP/K2C)
| Post | Budget H1 | Utfall H1 | Avvikelse | Flagga |
|---|--:|--:|--:|:--:|
| Hardware (konsoliderat) | 42 500 (85k FY prorata) | ~105 000 | +62 500 | 🔴 **ÖVER** |
| Redovisning (6530) | 6 000 | 22 636 | +16 636 | 🔴 över (bokslut 2025?) |
| Programvara (5420-22 + AI på 5410) | ~12 600 | ~17 000 | +4 400 | 🟡 |
| Imi/Red Marmoset (4531) | K2C-rad Imi H1 ~387k | 110 553 | under | 🟢 (periodisering) |
| Fredrik/Ark Island | K2C-rad H1 ~185k | 87 480 | under | 🟢 |
| Oskar/Skokloster | K2C-rad H1 ~41k | 275 182 | +234k | 🔴 **utred (WMAY+K2C blandat?)** |
| Lokalhyra (5010) | ej i AP P&L | 112 393 | n/a | 🟡 CZP-only? |

## Öppna frågor till Robert
1. Pleo 30K hardware ligger i 1731 (ej kostnadsfört) - boka som hardware/inventarie?
2. "Utlägg Robert Q1" 25 787 på 5410 - vad innehåller den (hardware/övrigt)?
3. Skokloster 275k - hur splittas K2C vs WMAY vs övrigt?
4. Tim/Bright Gambit design - var är den kostnaden?
5. Ska Malformation + Oddiko in som rader i AP P&L (de är AP-intäkt men saknas där)?
6. Lokalhyra 112k + Nethash/Eternal Minds 109k - CZP-only (utanför AP-scope)?

## Changes Log
| Datum | Vad | Av |
|---|---|---|
| 2026-06-22 | Kassabasis-underlag | CorpBot |
| 2026-06-22 | Ersatt med bokfört Fortnox 2026 (SIE via Playwright); huvudboksgrävning per konto/motpart; AP-intäkt isolerad (5 strömmar); hardware-överdrag spårat (BG konkursbo + Pleo) | CorpBot |
