# Konteringsunderlag: Shosha Games, Water Me & You, juli 2026

**Framtagen:** 2026-08-19 · **Ägare:** CorpBot · **Beslut:** Robert 2026-08-19
**Status:** klar att mata in i Fortnox
**Projektmärkning:** dimension 6, objekt **12 "Water, Me and You"** på samtliga rader

## Beslut som styr

1. **Nya fakturor bokförs på 3305** (försäljning tjänster till land utanför EU, ruta 40).
   Samutveckling är en tjänst. De fyra tidigare Shosha-fakturorna ligger på 3105 och lämnas
   orörda, vi slutar bara upprepa felet. Ingen kronaeffekt, skillnaden är ruta 36 mot ruta 40.
2. **Kreditfakturorna 100 och 101 krediterar faktura 79 och 87.**
3. **Betalningen 2026-07-24 matchas mot faktura 97.**

## Läget i reskontran

| Faktura | Datum | Belopp | Bokförd | Kommentar |
|---|---|---:|---|---|
| 79 | 2026-04-30 | 7 000 EUR | ja, B 35, 75 883,50 på 3105 | krediteras av 100 |
| 87 | 2026-05-31 | 7 000 EUR | ja, B 44, 75 404,00 på 3105 | krediteras av 101 |
| 97 | 2026-07-06 | 10 000 EUR | **nej** | betald 2026-07-24 |
| 98 | 2026-07-06 | 10 000 EUR | **nej** | förfaller 2026-08-07 |
| 99 | 2026-07-06 | 4 000 EUR | **nej** | förfaller 2026-08-28 |
| 100 | 2026-07-06 | −7 000 EUR | **nej** | kredit av 79 |
| 101 | 2026-07-06 | −7 000 EUR | **nej** | kredit av 101 |

Nettoeffekt: −14 000 EUR krediteras, +24 000 EUR faktureras. Shoshas skuld ökar med 10 000 EUR.

## Poster

### 1. Kundfaktura 97, 10 000 EUR, fakturadatum 2026-07-06

| Konto | Objekt | Debet | Kredit |
|---|---|---:|---:|
| 1510 Kundfordringar | 6/12 | *SEK enligt Fortnox kurs* | |
| 3305 Försäljning tjänster till land utanför EU | 6/12 | | *samma belopp* |

### 2. Kundfaktura 98, 10 000 EUR, samma datum

Identisk kontering som post 1.

### 3. Kundfaktura 99, 4 000 EUR, samma datum

Identisk kontering som post 1.

### 4. Kreditfaktura 100, krediterar faktura 79

| Konto | Objekt | Debet | Kredit |
|---|---|---:|---:|
| 3105 Försäljning varor till land utanför EU | 6/12 | 75 883,50 | |
| 1510 Kundfordringar | 6/12 | | 75 883,50 |

**Viktigt:** krediteringen ska vändas mot **3105 och det ursprungliga SEK-beloppet**, inte mot
3305 och dagskursen. Annars nollas inte faktura 79 på kundreskontran och en restpost blir kvar
på 1510. Kontrollera i Fortnox att faktura 79 går till saldo noll efter krediteringen. Gör den
inte det, för mellanskillnaden till 3960 eller 7960.

### 5. Kreditfaktura 101, krediterar faktura 87

| Konto | Objekt | Debet | Kredit |
|---|---|---:|---:|
| 3105 Försäljning varor till land utanför EU | 6/12 | 75 404,00 | |
| 1510 Kundfordringar | 6/12 | | 75 404,00 |

Samma kontroll som post 4.

### 6. Kundbetalning 2026-07-24, 109 717,24 SEK, mot faktura 97

| Konto | Objekt | Debet | Kredit |
|---|---|---:|---:|
| 1930 Företagskonto | 6/12 | 109 717,24 | |
| 1510 Kundfordringar | 6/12 | | *fakturans SEK-belopp* |
| 3960 Valutakursvinster / 7960 Valutakursförluster | 6/12 | *mellanskillnad* | *mellanskillnad* |

Följer mönstret från C 12 (vinst 113,10 på 3960) och C 24 (förlust 1 424,66 på 7960). Eftersom
EUR-kursen låg omkring 10,77 till 10,91 på de tidigare fakturorna och betalningen motsvarar
10,97, ligger en **kursvinst på 3960** närmast till hands. Räkna inte fram kursen för hand,
låt Fortnox sätta den ur fakturan.

## Efter inmatning

Bankdifferensen på 91 020,96 kr minskar med 109 717,24 när post 6 är bokförd. Kvar blir då de
fyra raderna: KORTFRIST LÅ 15 000 och ÄGARLÅN, KOR 10 000 den 6 juli, samt RUNATYR AB 2 000 och
H16548119566 4 303,72 den 16 juli.
