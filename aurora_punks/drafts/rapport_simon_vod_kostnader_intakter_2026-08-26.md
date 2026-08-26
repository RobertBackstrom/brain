# Vessels of Decay — kostnader, intäkter och rev share-läge mot Neon Artery

**Internt underlag, inte utskickat.** Framtaget 2026-08-26 av CorpBot på Roberts begäran.
Motpart om och när det går ut: Simon Jakobsson, Neon Artery AB.
Kompletterar `vod_revenue_forecast_2026-07-15.md`, som gällde nedskrivningsfrågan i AP AB.

---

## 1. Kort svar

1. **Simon ligger på 30 procent, inte 50.** Option C, som är det som gäller, växlar upp honom
   till 50 procent först när AP recoupat sin investering. Den recoupen är inte i närheten av
   nådd. Det här är en **rättelse** mot det tidigare interna underlaget, som utgick från en rak
   30-procentsandel utan recouptrappa. Se avsnitt 3.
2. **Det som är intjänat till Simon under 2026 är cirka 3 000 kronor.** CZP har bokfört
   11 998,23 SEK i royalty från Headup och fått in 10 099,20 efter tysk källskatt. Trettio
   procent av det som faktiskt inflöt är **3 029,76 SEK**. Se avsnitt 5.
3. **Headup recoupar fortfarande.** Utvecklarsidan får 20 procent av Gross Revenue tills Headup
   fått tillbaka sina externa kostnader på cirka 156 000 EUR. Vid nuvarande takt sker det aldrig.
4. **APDS bokföring går inte att nå.** De 108 000 EUR i milstolpsfinansiering från Headup och de
   450 000 SEK som gick till Neon Artery ligger båda där. Fortnox kräver BankID för att visa
   APDS siffror. Se avsnitt 6.
5. **Samma avtalspartsproblem som på 1993.** Avtalet med Simon är tecknat av Aurora Punks,
   Headup-avtalet av APDS, och det är CZP som fakturerar och tar emot pengarna idag.

---

## 2. Avtalskedjan

```
Headup Games GmbH  --(License and Publishing Agreement)--  Aurora Punks Development Services AB
                                                                        |
                                                          Aurora Punks  --(Option C)--  Neon Artery AB
```

### 2.1 Uppströms: Headup mot APDS

Signerat "License and Publishing Agreement", Drive `LicAgr_Vessels_of_Decay_AP_signed_HUG.pdf`
och `LicAgr_Vessels_of_Decay_Headup_AP_projectinfo_rev1`. Annex 8:

| Term | Innehåll |
|---|---|
| Andel under recoup | Developer får **20 % av all Gross Revenue** |
| Andel efter recoup | **50 % av all Gross Revenue** |
| Gross Revenue | Alla pengar som inflyter på Headups konton kopplat till publiceringen, exkl. moms. I praktiken plattformsintäkt efter Steams och konsolernas avdrag |
| Recoup-pool | "Headup External Costs", cirka **156 000 EUR**, inklusive utvecklingsfinansieringen på 108 000 EUR |
| Tröskel för 50/50 | Cirka **195 000 EUR ackumulerad Gross Revenue** |
| Redovisning | Kvartalsvis, betalning inom 20 bankdagar efter giltig faktura |

Det finns **inget ytterligare kostnadsavdrag** på Developer-andelen. Det är en rak procent på
Gross Revenue.

### 2.2 Nedströms: Aurora Punks mot Neon Artery, Option C

Förhandlad av Andreea Chifu, skickad till Simon **2024-10-14** och bekräftad av Robert samma dag
med orden *"I confirm that these are the numbers we have agreed upon from Aurora Punks"*.
Formellt kontrakt signerades och bifogades till Headup 2024-10-18.

Ordagrant ur mailet:

> **Option C**
> Developers gets a license fee of 450k SEK
> Rev share 30% from net (after Headup cut) for developer until AP recouped their investment;
> change to 50% after recoup.

Netto definieras i samma förhandling, i Option A och B som Option C bygger vidare på:

> net revenue is calculated from net revenue received by Aurora Punks for the game (gross revenue
> for the game after deduction of platform fees, taxes, bank fees, publisher share)

Alltså: **plattformsavgifter, skatter, bankavgifter och förläggarandel dras av innan Simons
procent räknas.** Tysk källskatt och bankavgifter hör hemma i "taxes" och "bank fees".

Simon fick också, ur samma förhandling:

1. First right of refusal att utveckla uppföljare inom IP:t.
2. Om han avstår, rollen som Creative Advisor på framtida projekt i IP:t.
3. First right of refusal att köpa IP:t, med värdering som ska tas fram vid behov.

### 2.3 Vad som gäller före Option C

Det ursprungliga co-dev-avtalet AP mot Neon Artery, Google Doc
`Co-Dev_AuroraPunks_NeonArtery_VoD_Agreement`, hade andra villkor och IP:t hos Neon Artery. I
februari 2024 sammanfattade Robert läget mot First Blood så här: AP hade cirka **85 000 USD**
investerat, med recoup på 30 % av Net Revenue och 20 % rev share, plus en buy-out på 85 000 USD
plus 15 % påslag alternativt 80 % av investerat belopp, 68 000 USD, plus 5 % rev share.

**Option C ersätter det.** Den äldre strukturen är bara relevant som historik och som en av
källorna till vad "AP:s investering" betyder i recouptrappan.

---

## 3. Recouptrappan, och varför den är oklar

Option C säger "until AP recouped their investment" utan att sätta ett belopp. Det är den enda
verkligt öppna punkten i hela beräkningen, eftersom den avgör om Simon står på 30 eller 50
procent.

Budgetunderlaget som Andreea gav Simon 2024-10-08 är den bästa skriftliga anknytningen:

| Post | SEK |
|---|---:|
| Redan spenderat och bokfört | 826 000 |
| Portning, alla plattformar | 500 000 |
| Musik | 40 000 |
| Produktion, design, programmering | 360 000 |
| Utveckling, Simon | 300 000 |
| Marknadsföringsassets | 50 000 |
| QA | 100 000 |
| **Total budget** | **2 176 000** |
| varav finansierat av Headup | ca 1 220 000 |
| **varav buret av Aurora Punks** | **ca 956 000** |

Option A och B i samma förhandling formulerade tröskeln som *"once Aurora Punks recouped AP
occurred costs outside the received publisher funding"*. Läser man Option C i ljuset av det blir
**AP:s investering cirka 956 000 SEK**, alltså budgeten minus förlagsfinansieringen, plus de
450 000 som sedan gick till Simon som licensavgift om den ska räknas in.

Mot en inflödestakt på cirka 12 000 SEK per halvår är den tröskeln inte nådd på decennier. Simon
står alltså på **30 procent**, och kommer att göra det.

**Att verifiera:** om det signerade kontraktet från oktober 2024 sätter en siffra på "AP's
investment" gäller den siffran, inte min härledning. Jag har termsheetet men inte det
undertecknade dokumentet. Se avsnitt 8.

---

## 4. Kostnader för IP:t, det jag kan belägga

### 4.1 CZP, förvärv och vidareförsäljning 2022

| Ver | Datum | Händelse | Belopp |
|---|---|---|---:|
| A 7 | 2022-02-08 | Förvärv av Vessels of Decay, betalt från 1930 till lager 1410 | **175 000,00** |
| A 84 | 2022-12-14 | "Säljer Vessels 2022, faktureras 2023". 1410 ut, 4910 kostnad in, 4910 försäljning ut mot 1896 | **439 301,00 exkl moms** |

CZP tog alltså in titeln för 175 000 och sålde den vidare för 439 301, en bokförd vinst på
264 301. I ett internt mail från samma period beskrivs affären som *"Neon Artery / Vessels of
Decay buys 100% ownership of IP for 489 301 SEK"*, med AP som återbetalar Roberts nedlagda
projektkostnader.

**Differensen 50 000 SEK mellan 489 301 och 439 301 är oförklarad** och bör redas ut, se
avsnitt 8.

### 4.2 CZP 2026, projekttagg 11 "Vessels of Decay"

| Ver | Datum | Post | Belopp |
|---|---|---|---:|
| D 14 | 2026-02-01 | Levfaktura PolyCrunch Games Limited (813), konto 4515, omvänd skattskyldighet | 7 936,50 |
| E 21 | 2026-03-03 | Betalning av samma, kursförlust 164,64 | 8 101,14 |

En andra PolyCrunch-faktura, **D 78 den 2026-06-07 på 8 150,63**, är bokförd på samma konto men
**saknar projekttagg**. Hör den till VoD blir 2026 års externa utvecklingskostnad **16 087,13**
i stället för 7 936,50. Det måste avgöras innan Simons netto räknas, eftersom
utvecklingskostnader inte är avdragsgilla mot hans andel enligt Option C. Det är bara
plattformsavgifter, skatter, bankavgifter och förläggarandel som får dras.

### 4.3 APDS

**Inte tillgängligt.** Här ligger de tunga posterna:

1. De 108 000 EUR i milstolpsfinansiering från Headup.
2. De 450 000 SEK i licensavgift till Neon Artery, som enligt Roberts bekräftelse 2026-07-15
   redan är utbetald.
3. Portning, QA, musik och produktionskostnader enligt budgeten i avsnitt 3.

---

## 5. Intäkter och vad Simon har rätt till

### 5.1 CZP 2026

| Ver | Datum | Faktura | Intäkt 3308 | Tysk källskatt 6350 | Inflöde 1930 |
|---|---|---|---:|---:|---:|
| B 12 / C 13 / C 38 | 2026-02-26 | Headup 58 | 5 437,75 | 857,11 | 4 576,86 |
| B 30 / C 30 / C 39 | 2026-05-05 | Headup 80 | 6 560,48 | 1 032,90 | 5 522,34 |
| | | **Summa** | **11 998,23** | **1 890,01** | **10 099,20** |

Källskatten ligger på 15,7 till 15,8 procent av fakturabeloppet, vilket stämmer med Headups
besked från december 2024 om **15 procent källskatt plus 5,5 procent solidaritetstillägg på de
15**, alltså 15,825 procent effektivt.

**Att kontrollera:** Headup skrev att avdraget skulle appliceras på **20 procent av de totala
utvecklingskostnaderna**, inte på hela royaltyfakturan. Här dras det på hela beloppet. Antingen
har regeln ändrats eller så drar Headup för mycket. Värt en fråga till Dirk Gooding.

### 5.2 Simons andel

| Beräkningsgrund | Belopp | Simons 30 % |
|---|---:|---:|
| Bokförd bruttointäkt | 11 998,23 | 3 599,47 |
| **Faktiskt inflöde efter källskatt och växling** | **10 099,20** | **3 029,76** |

**Jag rekommenderar den nedre raden.** Option C säger "30% from net (after Headup cut)" och
nettodefinitionen i samma förhandling räknar uttryckligen bort *taxes* och *bank fees*. Tysk
källskatt och kursförlust hör dit.

Det finns ett motargument: källskatt är avräkningsbar mot svensk bolagsskatt, så bolaget förlorar
den inte slutligt, bara likviditetsmässigt. Vill man vara generös mot Simon lägger man tillbaka
den. Skillnaden är 570 kronor och inte värd en dispyt, men positionen bör vara medveten.

### 5.3 Historiken före 2026

Royaltyn fakturerades från APDS innan bytet till CZP i mars 2026. Enligt det tidigare underlaget
fakturerades löpande royalty till Headup så sent som mars 2026, alltså finns det inflöden i APDS
sedan lanseringen 19 juni 2025 som inte syns här. **Det beloppet är okänt tills APDS huvudbok
kan läsas**, och det påverkar Simons ackumulerade fordran direkt.

---

## 6. Varför APDS bokföring inte går att nå

Fortnox listar sju räkenskapsår för Aurora Punks Development Services AB, 2020 till 2026, men
varje exportförsök landar på lobbyn med meddelandet *"Bekräfta din identitet för att se dina
siffror. Logga in med e-legitimation."* Lösenordssessionen räcker inte för det bolaget.

**Robert löser det genom att logga in i APDS i Fortnox med BankID och köra en SIE-export per år.**
Då kan jag räkna färdigt utan schabloner.

---

## 7. Slutsats

1. Simon står på **30 procent** och kommer att göra det, eftersom AP:s investering på
   storleksordningen 956 000 SEK inte recoupas vid nuvarande intäktstakt.
2. **3 029,76 SEK** är vad som är intjänat till honom på 2026 års två Headup-avräkningar, räknat
   på faktiskt inflöde.
3. Det som ligger i APDS sedan lanseringen i juni 2025 tillkommer och är okänt.
4. Headup är långt från recoup, så utvecklarsidan stannar på 20 procent av Gross Revenue.
5. Innan något skickas till Simon måste avtalspartsfrågan redas ut. Avtalet är Aurora Punks
   avtal, Headup-avtalet är APDS avtal och APDS är i konkurs sedan 2025-12-12, och det är CZP som
   fakturerar idag.

---

## 8. Vad som behövs för att göra rapporten skickbar

| Nr | Post | Var den finns | Vem |
|---|---|---|---|
| 1 | APDS huvudbok 2020 till 2026 | Fortnox, kräver BankID | Robert |
| 2 | Det **signerade** Neon Artery-kontraktet från oktober 2024, särskilt om "AP's investment" har ett belopp | Drive eller mailen 2024-10-18 | CorpBot när sökvägen är känd |
| 3 | Headups kvartalsrapporter sedan 2025-06-19: Gross Revenue per plattform och aktuellt recoup-saldo mot 156 000 EUR | Headup, Dirk Gooding | Robert |
| 4 | Exakt sammansättning av "Headup External Costs" | Annex 8 och milstolpsunderlagen | CorpBot |
| 5 | Om PolyCrunch-fakturan D 78 på 8 150,63 avser VoD | fakturaunderlaget i Fortnox | CorpBot |
| 6 | Förklaring till differensen 489 301 mot 439 301 i IP-affären 2022 | CZP-underlag, mailen | CorpBot |
| 7 | Om Headups källskatteavdrag ska räknas på hela fakturan eller på 20 % av utvecklingskostnaden | Headup, Dirk Gooding | Robert |
| 8 | Avtalspartsläget efter APDS-konkursen | konkursförvaltaren | Lawyer |
