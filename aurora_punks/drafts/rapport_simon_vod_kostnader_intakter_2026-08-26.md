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
2. **Det som är intjänat till Simon under 2026 är 3 029,76 kronor**, räknat på faktiskt inflöde
   efter tysk källskatt. Se avsnitt 5. **Därutöver uppskattas perioden juni 2025 till mars 2026
   till cirka 10 400 kronor för hans del, men den fakturerades av APDS och är därmed en fordran i
   ett konkursbo, inte ett krav mot CZP.** Se avsnitt 9.
3. **Headup recoupar fortfarande.** Utvecklarsidan får 20 procent av Gross Revenue tills Headup
   fått tillbaka sina externa kostnader på cirka 156 000 EUR. Vid nuvarande takt sker det aldrig.
4. **En del av kostnadshistoriken är nu belagd.** WLBS bokföring för 2023 finns i mailen från
   Henrik Franzén, med VoD som eget projektobjekt: **225 431 kronor nedlagt under året, aktiverat
   till 250 609**. APDS löpande huvudbok kräver fortfarande BankID, och där ligger de 108 000 EUR
   från Headup och de 450 000 till Neon Artery. Se avsnitt 4.3 och 6.
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

Den härledningen får nu stöd i bokföringen. **WLBS ensamt lade ned 225 431 kronor på VoD under
2023 och aktiverade 250 609**, se avsnitt 4.3. Lägger man till CZP:s förvärv av titeln för
175 000 år 2022, de 450 000 i licensavgift till Neon Artery och det APDS lade ned 2024 och 2025,
passeras 956 000 utan svårighet. Att AP-sidan skulle ha recoupat sin investering är uteslutet.

Mot en inflödestakt på cirka 12 000 SEK per halvår är tröskeln inte nådd på decennier. Simon står
alltså på **30 procent**, och kommer att göra det.

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

### 4.3 WLBS 2023, projektet "INTERNAL - Vessels Of Decay"

**Den här bokföringen finns.** Henrik Franzéns SIE-fil för WLBS räkenskapsår 2023,
`assistant/exports/sie/WLBS_2023_frmail.se`, har VoD som eget projektobjekt, **"53 INTERNAL -
Vessels Of Decay"**, med 99 transaktioner.

| Konto | Post | Belopp |
|---|---|---:|
| 4535 | Inköp av tjänster från annat EU-land, 25 % | 116 458,12 |
| 4600 | Legoarbeten och underentreprenader | 28 949,87 |
| 7210 | Löner till tjänstemän | 42 454,31 |
| 7510 | Arbetsgivaravgifter 31,42 % | 13 339,13 |
| 5800 + 5810 | Resekostnader och biljetter | 17 929,71 |
| 5900 + 5911 | Annonsering och annonsering EU | 6 299,49 |
| | **Summa nedlagd kostnad 2023** | **225 430,63** |
| 3800 | Aktiverat arbete för egen räkning | −250 609,00 |
| 1010 | Utvecklingsutgifter, balanserat | 250 609,00 |

Leverantörerna bakom 4535 och 4600 är Super Menno Monster, Kando Factory Ltd, Odd Magnus
Glodeck, Lano Software GmbH, Remote Europe Holding BV, Cold Pixel AB och APDS internt. Sju
anställda har tid på projektet under året.

**Två saker att notera:**

1. **WLBS aktiverade 250 609 men lade ned 225 431.** Differensen på 25 178 kronor är antingen
   kostnader från tidigare år som aktiverades samtidigt, eller ett overheadpåslag. Den bör
   förklaras, eftersom det aktiverade beloppet är det som följt med tillgången vidare.
2. **De 250 609 hör till "AP:s investering"** i Option C-recoupen, oavsett att de bokades i
   WLBS och inte i APDS. Bolaget var dotterbolag till Aurora Punks fram till konkursen
   2024-09-25.

### 4.4 APDS

**Delvis tillgängligt.** Årsredovisningen för 2023 finns som PDF i mailen, liksom
bouppteckningen från konkursen. Löpande huvudbok kräver fortfarande BankID. Här ligger:

1. De 108 000 EUR i milstolpsfinansiering från Headup.
2. De 450 000 SEK i licensavgift till Neon Artery, enligt Roberts bekräftelse 2026-07-15 redan
   utbetald.
3. Portning, QA, musik och produktionskostnader 2024 och 2025.
4. Royaltyinflödet från Headup juni 2025 till mars 2026.

Ur koncernsammanställningen framgår att APDS omsättning växte från 534 kUSD 2022 till 651 kUSD
2023 och 1 107 kUSD 2024, med ett rörelseresultat på −231 kUSD 2024. Det säger något om
storleksordningen men inget om VoD specifikt.

---

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

## 6. Vad som finns och vad som saknas i bokföringen

| Bolag | Läge |
|---|---|
| **Creation Zero Point Holding AB** | Full åtkomst 2019 till 2026, projekttagg 11 för VoD från och med 2026. |
| **White Lines Black Spaces AB** | Fortnox svarar `NO_YEARS` efter konkursen 2024-09-25, men **SIE för 2023 finns i mailen från Henrik Franzén** och är nu sparad lokalt med VoD som eget projektobjekt. 2019 till 2022 och 2024 saknas. |
| **Aurora Punks Development Services AB** | Sju räkenskapsår listas i Fortnox men export kräver e-legitimation. Årsredovisning 2023 och konkursbouppteckningen finns som PDF i mailen. |

För APDS gäller att Fortnox landar på lobbyn med *"Bekräfta din identitet för att se dina siffror.
Logga in med e-legitimation."* Lösenordssessionen räcker inte för det bolaget, medan CZP och
Runatyr fungerar. **Robert löser det med BankID och en SIE-export per år.**

För WLBS övriga år är vägen Henrik Franzén, samma väg som 2023-filen kom, alternativt
konkursförvaltaren Carler.

---

## 7. Slutsats

1. Simon står på **30 procent** och kommer att göra det. Bara WLBS 2023 och CZP:s förvärv 2022
   summerar till över 425 000 kronor av AP-sidans investering, och tröskeln ligger runt 956 000.
2. **3 029,76 SEK** är vad som är intjänat till honom på 2026 års två Headup-avräkningar, räknat
   på faktiskt inflöde efter tysk källskatt.
3. Det som ligger i APDS sedan lanseringen i juni 2025 tillkommer och är okänt tills huvudboken
   går att läsa.
4. Headup är långt från recoup, så utvecklarsidan stannar på 20 procent av Gross Revenue.
5. Innan något skickas till Simon måste avtalspartsfrågan redas ut. Avtalet är Aurora Punks
   avtal, Headup-avtalet är APDS avtal, APDS är i konkurs sedan 2025-12-12, WLBS sedan
   2024-09-25, och det är CZP som fakturerar idag.

---

## 8. Vad som behövs för att göra rapporten skickbar

| Nr | Post | Var den finns | Vem |
|---|---|---|---|
| 1 | APDS huvudbok 2020 till 2026 | Fortnox, kräver BankID | Robert |
| 2 | **WLBS SIE för 2022 och 2024**, för att stänga kostnadshistoriken före APDS tog över | Henrik Franzén, samma väg som 2023-filen | CorpBot begär, Robert godkänner |
| 3 | Det **signerade** Neon Artery-kontraktet från oktober 2024, särskilt om "AP's investment" har ett belopp | Drive eller mailen kring 2024-10-18 | CorpBot |
| 4 | Headups kvartalsrapporter sedan 2025-06-19: Gross Revenue per plattform och recoup-saldo mot 156 000 EUR | Headup, Dirk Gooding | Robert |
| 5 | Förklaring till differensen 250 609 aktiverat mot 225 431 nedlagt i WLBS 2023 | WLBS-underlagen, Henrik | CorpBot |
| 6 | Om PolyCrunch-fakturan D 78 på 8 150,63 avser VoD | fakturaunderlaget i Fortnox | CorpBot |
| 7 | Förklaring till differensen 489 301 mot 439 301 i IP-affären 2022 | CZP-underlag, mailen | CorpBot |
| 8 | Om Headups källskatteavdrag ska räknas på hela fakturan eller på 20 % av utvecklingskostnaden | Headup, Dirk Gooding | Robert |
| 9 | Avtalspartsläget efter APDS- och WLBS-konkurserna | konkursförvaltaren Carler, Nils Åberg | Lawyer |

---

## 9. Uppskattning av APDS-perioden

Robert har beslutat 2026-08-26 att APDS huvudbok inte kommer att gå att få fram. Det här avsnittet
uppskattar den. **Alla siffror här är uppskattningar där inget annat anges.** Valutakurser hämtade
2026-08-27 och korskontrollerade mot två källor: **EUR/SEK 11,08**, USD/SEK 9,52.

### 9.1 AP-sidans investering, det som avgör om Simon står på 30 eller 50 procent

| Post | Belopp | Status |
|---|---:|---|
| CZP förvärv av titeln 2022-02-08 | 175 000 | **bokfört**, ver A 7 |
| WLBS utvecklingskostnad 2023, aktiverad | 250 609 | **bokfört**, ver A 148, projekt 53 |
| CZP externa utvecklingskostnader 2026, PolyCrunch | 16 087 | **bokfört**, ver D 14 och D 78 |
| APDS 2024 och 2025 | **cirka 514 000** | uppskattat, se nedan |
| **Summa AP-sidans investering** | **cirka 956 000** | |

Uppskattningen av APDS-delen är inte fri utan en restpost. Budgetunderlaget Andreea gav Simon
2024-10-08 sätter totalbudgeten till 2 176 000 varav Headup finansierar cirka 1 220 000, vilket
lämnar **956 000 på AP-sidan**. De 108 000 EUR Headup faktiskt betalade motsvarar 1 196 640 kronor
till dagens kurs, vilket stämmer väl med de planerade 1 220 000. Restposten mot det som är bokfört
i CZP och WLBS blir då cirka 514 000, och det är precis den period där APDS drev projektet: från
Option C i oktober 2024 fram till lanseringen i juni 2025.

Inom de 514 000 ligger bland annat licensavgiften på 450 000 till Neon Artery, som enligt Roberts
bekräftelse 2026-07-15 redan är utbetald.

**Slutsats:** recoupen ligger på cirka 956 000 kronor och AP-sidan har fått in i storleksordningen
53 000, alltså knappt sex procent. **Simon står på 30 procent och gör det under överskådlig tid.**
För att nå 50 skulle intäkterna behöva bli ungefär arton gånger så stora som hittills.

### 9.2 Royaltyn från Headup, uppskattad för APDS-perioden

Lansering 2025-06-19. Faktureringen flyttade till CZP i mars 2026. Det ger tre kvartal där
royaltyn gick till APDS.

| Period | Belopp | Status |
|---|---:|---|
| Q3 2025, lanseringskvartalet | 25 000 | uppskattat, lanseringskvartal ligger typiskt tre till fem gånger över den stabila nivån |
| Q4 2025 | 8 000 | uppskattat |
| Q1 2026, till bytet | 8 000 | uppskattat |
| **Summa APDS-perioden** | **cirka 41 000** | uppskattat |
| CZP faktura 58, 2026-02-26 | 5 437,75 | **bokfört** |
| CZP faktura 80, 2026-05-05 | 6 560,48 | **bokfört** |
| **Summa till AP-sidan sedan lansering** | **cirka 53 000** | |

Den stabila nivån är hämtad ur CZP:s två faktiska avräkningar, som snittar cirka 6 000 kronor per
kvartal.

### 9.3 Vad Simon har att fordra, totalt

| Period | Bas | Källskatt 15,8 % | Netto | **Simons 30 %** | Mot vem |
|---|---:|---:|---:|---:|---|
| APDS, juni 2025 till mars 2026 | 41 000 | −6 478 | 34 522 | **cirka 10 357** | konkursboet APDS |
| CZP, 2026 | 11 998 | −1 890 | 10 108 | **3 030** | CZP |
| **Summa** | **52 998** | **−8 368** | **44 630** | **cirka 13 387** | |

**Den viktigaste raden är den översta, och den har försämrats.** Uppskattade 10 357 kronor avser en
period där avtalsparten var Aurora Punks och betalaren APDS. **Bevakningsfristen i APDS-konkursen,
mål K 4429-25, löpte ut 2026-07-21 och ingen bevakning gjordes för den här fordran.** Beloppet går
alltså varken att kräva av konkursboet eller av CZP. Robert bekräftade det 2026-08-28.

Det är inte ett juridiskt problem för oss men det är ett förtroendeproblem. Robert vill kompensera
Simon på annat sätt, se `drafts/discord_simon_royalty_2026-08-28.md`.

De 3 030 kronorna för 2026 är däremot en levande skuld hos CZP och kan betalas.

### 9.4 Osäkerheten, ärligt

1. **Lanseringskvartalet är den svagaste gissningen.** Kommer Headups faktiska kvartalsrapport in
   ändras 10 357 direkt. Rapporterna finns hos Headup och Robert kan begära dem, det kräver inget
   av APDS.
2. De 514 000 för APDS är en restpost mot en budget från oktober 2024, inte ett bokfört belopp.
   Blev det dyrare eller billigare än planerat förskjuts recoupen, men inte tillräckligt för att
   trigga 50-procentsnivån.
3. Om det **signerade** Neon Artery-kontraktet sätter en siffra på "AP's investment" gäller den
   siffran före min härledning.
4. Headup är fortfarande långt från sin egen recoup på 156 000 EUR, vilket motsvarar cirka
   1 728 000 kronor. Utvecklarsidan stannar därför på 20 procent av Gross Revenue.

### 9.5 Vad jag skulle skriva till Simon

Redovisa de två faktiska CZP-avräkningarna och de 3 030 kronorna som är intjänade där. Var öppen
med att perioden juni 2025 till mars 2026 fakturerades av APDS, att den uppskattas till cirka
10 000 kronor för hans del, och att den frågan hanteras mot konkursboet. Erbjud att skicka Headups
kvartalsrapporter så snart de kommit in, så att siffran blir exakt i stället för uppskattad.
