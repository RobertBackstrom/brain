# Rättelse och kontering: ägarlån CZP till Aurora Punks AB

**Framtagen:** 2026-08-19 · **Ägare:** CorpBot · **Beslut:** Robert 2026-08-19
**Status:** klar att bokföra, väntar på nytt konto

## Vad som gäller

Julireversen om **50 000 SEK** betalades ut i två delar:

| Datum | Banktext | Belopp | Nuläge i bokföringen |
|---|---|---:|---|
| 2026-07-03 | ÄGARLÅN UT | 40 000,00 | Bokförd, verifikat **A 204**, mot **2893** Skulder till närstående personer |
| 2026-07-06 | ÄGARLÅN, KOR | 10 000,00 | **Obokförd** |
| | **Summa** | **50 000,00** | |

Båda ska stå som **ägarlån från CZP till Aurora Punks AB**, alltså en fordran på AP, inte
som återbetalning av CZP:s skuld till Robert. Konteringen på A 204 är fel.

## Problem: kontot saknas

CZP:s kontoplan har ingen fordran på AP AB. Serien är upptagen enligt nedan, och **1714 avser
konkursbolaget APDS**, inte moderbolaget:

| Konto | Benämning |
|---|---|
| 1711 | Fordran på Cold Pixel AB |
| 1712 | Fordran på White Lines Black Spaces AB |
| 1713 | Fordran på Runatyr AB |
| 1714 | Fordran på Aurora Punks Development Services AB |
| 1715 | Fordran på Grey Tower AB |
| 1716 | Fordran på LOOT |
| 1717 | Dark Riviera AB |
| 1718 | Fordran på Monowo AB |
| **1719** | **ledigt — föreslås "Fordran på Aurora Punks AB"** |

**Kontroll som behövs:** verifikat **A 37, 2026-02-26**, texten "Aurora Punks AB / Ägarlån CZP"
om 25 000 bokfördes mot **1714**. Om det lånet gick till AP AB och inte till APDS ligger även
den posten på fel konto och bör flyttas till 1719 i samma veva.

## Bokföringsposter

### 1. Rättelse av A 204 (omföring 40 000)

| Konto | Debet | Kredit |
|---|---:|---:|
| 1719 Fordran på Aurora Punks AB | 40 000,00 | |
| 2893 Skulder till närstående personer | | 40 000,00 |

Text: `Rättelse A 204 — ägarlån CZP till AP AB enligt revers 2026-07-06, felaktigt bokfört mot 2893`

### 2. Bokföring av den obokförda utbetalningen 6 juli (10 000)

| Konto | Debet | Kredit |
|---|---:|---:|
| 1719 Fordran på Aurora Punks AB | 10 000,00 | |
| 1930 Företagskonto | | 10 000,00 |

Text: `Ägarlån CZP till AP AB, del 2 av revers 2026-07-06`

### 3. Utbetalningen 2026-08-19 (50 000, ny revers)

| Konto | Debet | Kredit |
|---|---:|---:|
| 1719 Fordran på Aurora Punks AB | 50 000,00 | |
| 1930 Företagskonto | | 50 000,00 |

Text: `Ägarlån CZP till AP AB enligt revers 2026-08-19`

**Utfall:** konto 1719 visar 100 000 SEK, vilket motsvarar de två reverserna. 2893 minskar med
40 000, vilket är riktigt eftersom den posten aldrig var en återbetalning till Robert.

## Kvar att klassificera

**2026-07-06, KORTFRIST LÅ, 15 000 SEK** är fortfarande obokförd och hör inte till reversen
(10 000 + 40 000 utgör hela de 50 000). Motpart behöver anges innan den kan konteras.

## Motsvarande post hos AP

AP bokför spegelvänt: 1930 debet mot en skuld till CZP på 2893 eller motsvarande
koncernskuldkonto. AP:s bokföring ligger hos Amer.
