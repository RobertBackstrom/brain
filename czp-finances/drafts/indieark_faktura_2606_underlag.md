# Underlag: kundfaktura Yaozuo Games Ltd (IndieArk), junirapporten 2026

**Framtagen:** 2026-08-13 · **Ägare:** CorpBot · **Status:** klar att mata in, väntar på Fortnox-access

## Vad som ska faktureras

Strike Force Heroes, 10 % av net sales på konsol, enligt rapport **IA-R-APD2026008**
(rapportdatum 2026-08-06, mottagen 2026-08-08).

| Rad | Beskrivning | USD |
|---|---|---|
| 1 | Nintendo Switch sales share (June 2026), 41 units, net sales 418,45 | 41,85 |
| 2 | Xbox sales share (June 2026), 173 units, net sales 2 652,82 | 265,28 |
| 3 | PlayStation sales share (June 2026), 48 units, net sales 756,12 (SIEJ 2 / SIEA 33 / SIEE 13) | 75,61 |
| | **Att fakturera** | **382,74** |

Rapport-PDF: `assistant/uploads/indieark_2606_report.pdf`

## Kund

Yaozuo Games Ltd (IndieArk), 4003 building A, Qianhai Horoy Center, Shenzhen, Kina.
Fakturamail: invoice@indieark.com. Kontakt: Kevin Ye, kevinye@indieark.com.

Rapporten är fortfarande ställd till **Aurora Punks Development Services AB**. Fakturan
går ändå från **CZP**, i linje med fakturorna 51, 52, 63, 73, 81 och 93 under 2026 som
alla ställts ut av CZP och betalats.

## Bokföring

Speglar faktura 93 (verifikat B 43):

- Intäkt: **3305 Försäljning tjänster till land utanför EU**, dimension objekt 6 = "7" Strikeforce Heroes
- Motkonto: 1510 Kundfordringar
- Ingen moms. Tjänst till beskattningsbar person utanför EU, omsättningsland utanför Sverige.
  Redovisas i **ruta 40** i momsdeklarationen.
- Valutakursdifferens vid betalning bokas på **7960**, som på faktura 93 (344,17 kr vid
  betalningen 15 juni).

## Två saker att hantera i samma veva

1. **Kontokorrigering.** Fakturorna 51, 52, 63 och 73 bokfördes på 3105, försäljning av
   varor utanför EU, vilket lägger dem i ruta 36 i stället för ruta 40. Faktura 81 och 93
   ligger rätt på 3305. Ingen skatteeffekt, men rutorna i lämnade momsdeklarationer är fel.
   Beslut behövs om det ska rättas eller lämnas.
2. **Fakturaservice tar inte USD.** Enligt Henrik (2026-02-17) klarar Fortnox
   fakturatjänster bara SEK och EUR. USD-fakturan ställs ut utan fakturaservice.

## Historik 2026

| Faktura | Bokförd | Registrerad | Rapport | Belopp SEK | Betald |
|---|---|---|---|---|---|
| 51 + 52 | 2026-02-06 | 2026-02-26 | 25.11 + 25.12 | 4 010,08 + 10 568,04 | ja |
| 63 | 2026-03-13 | 2026-03-31 | 26.01 | 9 257,28 | ja |
| 73 | 2026-04-24 | 2026-04-29 | 26.02 | 8 351,49 | ja |
| 81 | 2026-05-13 | 2026-05-22 | 26.03 | 3 926,32 | ja |
| 93 | 2026-06-10 | 2026-06-24 | 26.04 | 8 312,36 | ja, 15 juni |
| saknas | | | **26.05** | **USD 450,62** | ej utställd |
| saknas | | | **26.06** | **USD 382,74** | ej utställd |

**RÄTTAT 2026-08-18 mot Fortnox kundreskontra (auktoritativ källa):** båda fakturorna
**finns redan utställda**. Faktura **102**, 450,00 USD, fakturadatum 2026-07-06 (majrapporten)
och faktura **105**, 382,00 USD, fakturadatum 2026-08-18 (junirapporten). Båda är obetalda.

Mitt tidigare påstående att de saknades byggde på SIE-filen, som bara innehåller **bokförda**
verifikat. Faktura 102 är utställd men ännu inte bokförd, och syntes därför inte. Robert hade
rätt hela vägen. **Lärdom: kundreskontran, inte SIE-filen, är källan för vad som är fakturerat.**

Kvar att göra på den här posten: ingenting nytt ska ställas ut. Fakturorna 102 och 105 ska
bokföras och bevakas för betalning.

---

## Konteringsbeslut 2026-08-19 (Robert)

**Stående regel: intäktsdelning och samutveckling bokförs på 3305, försäljning tjänster till
land utanför EU, ruta 40.** Gäller Yaozuo framåt och Shosha från faktura 97. De gamla
fakturorna på 3105 lämnas orörda, vi slutar bara upprepa felet. Ingen kronaeffekt, skillnaden
är vilken ruta beloppet redovisas i.

För Yaozuo skedde bytet i praktiken redan vid **faktura 81** (2026-05-13), och faktura 93 ligger
också rätt. Det är bara 51, 52, 63 och 73 som ligger kvar på 3105.

### Obokförda Yaozuo-fakturor

| Faktura | Datum | Belopp | Kontering |
|---|---|---:|---|
| 102 | 2026-07-06 | 450,00 USD | 1510 debet / **3305** kredit, dimension 6 objekt **7** Strikeforce Heroes |
| 105 | 2026-08-18 | 382,00 USD | samma |

Ingen moms. Valutakursdifferens vid betalning på 3960 eller 7960, som på faktura 93 där
344,17 kr fördes till 7960. Låt Fortnox sätta USD-kursen ur fakturan, räkna inte fram den.
