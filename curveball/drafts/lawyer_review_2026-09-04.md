# Juridisk genomgång: publishing-avtalet med The Gang Studio AB

**Dokument som granskats:** `publishing_agreement_thegang_2026-09-04.md` (engelsk text, svensk rätt, Stockholms tingsrätt)
**Underlag:** `publishing_agreement_notes_2026-09-01.md`, `term_sheet_2026-08-31.md`, `curveball/CLAUDE.md`, output_log
**Granskare:** Lawyer (intern rådgivare). **Jag är inte advokat.** Varje punkt är märkt `[Bedömning]` när jag står för den själv, och `[Advokat]` när den måste till extern advokat innan signering.
**Datum:** 2026-09-04
**Status på avtalet:** utkastet ligger hos motparten. Ändringar nedan ska därför inte skickas styckvis. Samla dem i en enda version 2 med ett kort följebrev, annars ser det ut som att vi öppnar avtalet på nytt varje dag.

---

## Sammanfattning

Avtalet är välskrivet, kort och gör det Robert bad om. Men det har **en konstruktionsmiss som gör punkt 12.5 verkningslös**, och ett antal ställen där AP investerar allt arbete och saknar den motprestation avtalet ser ut att ge. De tre allvarligaste är, i ordning:

1. **12.5 är tom.** Nettointäkt är definierad som pengar AP tar emot från Valve. Efter uppsägning har AP inte appen, alltså tar AP inte emot något och det finns ingen skyldighet för The Gang att rapportera eller betala. Den överlevande andelen är noll kronor.
2. **AP:s eget arbete lämnas ifrån sig gratis, både under och efter avtalet.** 10.2 ger The Gang rätt att när som helst få ut hela källkoden inklusive AP:s ändringar, utan någon begränsning i vad de får göra med den, och exklusiviteten i 2.1 gäller bara Steam.
3. **Ansvarsbegränsningen i 17.1 utesluter AP:s enda verkliga skada.** AP:s hela ersättning är framtida intäktsandel, alltså utebliven vinst, som 17.1 uttryckligen undantar.

Utöver det finns en fråga som inte är avtalsteknisk utan existentiell: **det är inte utrett att The Gang Studio AB äger spelet**.

---

# Del A. De fem punkter Robert beställde

## A1. Punkt 12.5, håller konstruktionen? (Fråga 1)

**Nej. Den håller inte, men felet ligger inte i undantagen, det ligger i definitionen.** `[Bedömning]`

1.3 definierar Net Revenue som *"the amounts actually received by the Publisher from Valve Corporation"*. 12.2 säger att Steam-appen går tillbaka till The Gang inom 30 dagar. Efter uppsägning tar alltså AP emot noll kronor från Valve, Net Revenue är noll, och 6.2 om 30 procent av noll ger noll. 12.5 säger att andelen "continues", men det finns inget kvar att fortsätta på.

Tre följdfel av samma sak:
1. Hela rapporterings- och betalningsapparaten i 8 pekar åt fel håll efter uppsägning. 8.1 lägger rapporterings- och betalningsplikten på **utgivaren**, alltså AP. Efter uppsägning är det The Gang som har intäkterna och som skulle behöva rapportera. 12.6 låter 8 överleva, men 8 säger då bara att AP ska rapportera pengar AP inte får.
2. Granskningsrätten i 8.4 pekar också mot AP, alltså mot fel part efter uppsägning.
3. 8.3 ger The Gang användaraccess till appen i AP:s konto. Efter uppsägning behöver AP det omvända, och det står ingenstans.

**Undantagens avgränsning mot 11.3 och 11.4, är den rätt?** Delvis. `[Bedömning]`

1. **Mot 11.4 (insolvens) är avgränsningen rätt och medvetet till AP:s fördel.** Om The Gang går i konkurs eller rekonstruktion behåller AP andelen. Att AP behåller andelen även om det är AP som blir insolvent kommer motparten att peka på. Det är en förhandlingspost, inte ett fel.
2. **Mot 11.3 är avgränsningen för vid, och det är farligt för AP.** 12.5 säger "the Publisher's uncured material breach" utan att begränsa vilken bestämmelse. 11.3 ger uppsägningsrätt vid varje väsentligt avtalsbrott som inte rättats inom 30 dagar. Resultatet är en stupkant: en utebliven kvartalsrapport som inte rättas i tid kan i teorin kosta AP hela den eviga andelen. Det är en förverkanderegel utan proportionalitet, och just den typen av klausul är den som angrips med `AvtL 36 §`. Här är den dessutom riktad mot oss.
3. **Ordet "material" gör inte jobbet.** Väsentlighet prövas i efterhand av en domstol. AP bör hellre räkna upp vilka brott som får ha den effekten.

### Föreslagen text

Ny definition i 1:

```
1.5 "Post-Termination Revenue" means the amounts actually received by the Developer,
or by any party publishing or distributing the Game with the Developer's authority,
from sales and other commercial exploitation of the Game on personal computers after
termination of this Agreement, after the storefront's share, refunds, chargebacks and
platform taxes.
```

Ersätt 12.5:

```
12.5 Where this Agreement is terminated other than under section 11.2 or for the
Publisher's uncured material breach of section 3.1, 3.2 or 8, the Publisher's revenue
share continues after termination. From termination the Developer shall pay the
Publisher thirty (30) per cent of Post-Termination Revenue, and any part of the amount
in section 6.1 that the Publisher has not yet retained shall first be paid to the
Publisher out of Post-Termination Revenue. Sections 8.1, 8.2 and 8.4 then apply with
the Parties reversed, so that the Developer reports and pays and the Publisher may
audit, and the Developer shall give the Publisher user access to the Steam App for
that purpose.
```

Justera 12.6 så att det står "section 8 survives termination and applies as set out in section 12.5".

## A2. Evig intäktsandel utan bortre gräns och utan utköp (Fråga 2)

**Grundfrågan: håller en evig andel?** `[Bedömning, med en advokatflagga]`

1. **Eviga avtal är i sig giltiga i svensk rätt.** `NJA 2004 s. 167` upprätthöll ett benefikt evighetsavtal om jakträtt. Utgångspunkten är alltså inte ogiltighet.
2. **Men huvudregeln för avtal utan bestämd avtalstid är att de kan sägas upp med skälig uppsägningstid.** `NJA 2009 s. 672` (Malmbergsbagarn, tre månader, med "avtalstidens längd samt den uppsagda partens investeringar och omställningskostnader" som bedömningsfaktorer) och `NJA 2018 s. 19` (Traktoråterförsäljaren, sex månader efter 22 år). Verifierat mot avtalslagen2020.se avsnitt 10.1, hämtat 2026-09-04.
3. **Skillnaden som räddar oss, om den skrivs ut:** de rättsfallen gäller avtal om **löpande prestationer** i en pågående relation. Vår andel är inte betalning för en löpande tjänst, den är **uppskjuten köpeskilling för en investering AP redan gjort**. Det står bara inte i avtalet. Som texten ser ut nu läser en domstol 6.2 som en del av ett utgivningsförhållande, alltså precis den avtalstyp som är uppsägningsbar.
4. **Åtgärd: skriv in karaktären, inte bara varaktigheten.** En rad som säger vad andelen är betalning för flyttar avtalet ur uppsägningspresumtionen. Det kostar ingenting och är den billigaste riskreduktionen i hela dokumentet.
5. `AvtL 36 §`-risken finns kvar men är låg mellan två näringsidkare med jämförbar förhandlingsstyrka på ett avtal om 30 procent. Den blir högre om intäkten en dag är stor och AP:s insats framstår som liten i förhållande. Även här hjälper punkt 3 ovan.

**Överlåtelse av bolaget eller av IP:t, räcker 18.2?** `[Bedömning]`

**Nej.** 18.2 reglerar överlåtelse av **avtalet**, inte av tillgången.

1. **Aktieöverlåtelse (bolaget säljs).** 18.2 biter inte, och det behöver den inte. Bolaget är fortfarande part och fortfarande bundet. AP har dock ingen underrättelserätt och får veta det sist.
2. **Inkråmsöverlåtelse (IP:t säljs).** Här finns hålet. The Gang säljer spelet och Steam-appen till Köparen. Avtalet binder inte Köparen, för ett avtal kan inte belasta tredje man. The Gang är kvar som avtalspart men har inte längre några intäkter, och 12.5 i min föreslagna lydelse träffar bara "the Developer, or any party publishing with the Developer's authority". En köpare som publicerar med **egen** rätt faller utanför. AP:s enda kvarvarande anspråk blir skadestånd mot ett tömt bolag.
3. **Konkurs.** Om The Gang går i konkurs efter en överlåtelse är fordran mot bolaget i praktiken värdelös.
4. **Utköpsklausul.** Att den saknas är Roberts medvetna val och jag ändrar inte det. Men den är i praktiken **AP:s vän**, inte motpartens: utan den kommer en framtida köpare i stället att pressa fram en omförhandling under tidspress, eller strunta i andelen och låta AP processa. En formelbaserad utköpsrätt sätter ett golv på vad andelen är värd vid en exit.

### Föreslagen text

```
6.5 The revenue share in section 6.2 is deferred consideration for the Publisher's
investment of work in completing and publishing the Game. It is not consideration for
continuing services, it is not terminable by notice, and it continues regardless of the
term of this Agreement, subject only to section 12.5.
```

```
18.9 Successors. The Developer shall not sell, assign, transfer or exclusively licence
the Game, the Steam App or the intellectual property rights in the Game unless the
transferee first undertakes in writing to the Publisher to be bound by sections 6, 8
and 12.5 as if it were the Developer. The Developer remains liable for the performance
of those sections if it does not obtain that undertaking. The Developer shall notify
the Publisher in writing of any change of control of the Developer within ten (10)
business days.
```

Frivillig, tas fram bara om The Gang begär utköpsrätt (siffrorna är platshållare, Robert sätter dem):

```
6.6 The Developer may buy out the revenue share in section 6.2 by paying the Publisher
an amount equal to three (3) times the total amounts retained by or paid to the
Publisher under section 6 during the twenty-four (24) months before the notice, and not
less than [750,000] SEK.
```

`[Advokat]` Håller 18.9 mot en köpare som är i god tro, och kan man förstärka andelen sakrättsligt (pant i fordran, anteckning, eller ett separat säkerhetsupplägg) i stället för att bara ha en obligationsrättslig utfästelse? Det är den enda frågan i hela paketet där jag inte kan ge ett säkert svar.

## A3. Indemnity i 16 och ansvarsbegränsning i 17 (Fråga 3)

**Nedkortningen har tappat fyra saker, och en av dem är allvarlig.** `[Bedömning]`

1. **17.1 utesluter AP:s enda verkliga skada. Detta är det allvarligaste enskilda felet i avtalet efter 12.5.** AP får ingen kontant ersättning. AP:s hela vederlag är framtida intäktsandel. Om The Gang bryter mot avtalet, exempelvis vägrar flytta appen eller om spelet visar sig göra intrång och måste dras, är AP:s skada **utebliven vinst**, som 17.1 uttryckligen undantar. Med nuvarande lydelse har AP alltså ett avtal där motpartens avtalsbrott i praktiken inte är sanktionerat.
2. **Det saknas ansvarstak helt.** Det är inte i sig fel, men det är ovanligt och det innebär att AP har obegränsat direktansvar för till exempel ett publiceringsmisstag. Ett ömsesidigt tak är normalt bättre för den part som har minst kassa, alltså här AP.
3. **Om ett tak införs måste The Gangs IP-garanti ligga utanför det.** Ett IP-anspråk mot spelet är den enda händelse som kan radera hela AP:s investering. Ett tak på 16.2 vore att kapa den ena garantin som faktiskt skyddar oss.
4. **Indemnityn i 16.4 saknar försvarsplikt.** Den täcker "documented loss" i efterhand. Vad AP behöver är att The Gang **försvarar** ett tredjemansanspråk om intrång på egen bekostnad, och att AP får stoppa distributionen medan det pågår utan att det räknas som avtalsbrott eller äter av tolvmånadersfristen.
5. **Korsvis skydd finns formellt (16.4 är ömsesidig) men är obalanserat i sak**, eftersom 16.2 lägger hela IP-risken hos The Gang medan 16.3 bara ålägger AP att arbeta professionellt. Det är rätt fördelning, den ska bara inte urholkas av ett tak.

### Föreslagen text

```
16.4 Each Party shall indemnify the other for documented loss arising from a breach of
its warranties in this section, including reasonable legal costs. Where a third party
claims that the Game infringes its rights, the Developer shall at its own cost defend
the claim and shall indemnify the Publisher for damages, settlements and reasonable
legal costs. The indemnified Party shall notify the other without delay and shall not
settle a claim without the other Party's written consent, which shall not be
unreasonably withheld. The Publisher may suspend distribution of the Game while such a
claim is pending. Such suspension is not a breach of this Agreement and does not count
towards the period in section 11.2.
```

```
17.3 Amounts payable under section 6 or section 12.5 are direct loss for the purposes
of this Agreement, and section 17.1 does not exclude a claim for them.

17.4 Each Party's aggregate liability under this Agreement is limited to the greater of
[500,000] SEK and the total amounts paid or payable under section 6 during the twelve
(12) months before the claim. This limit does not apply to liability under sections
16.2 and 16.4, to a breach of section 15, or to the cases in section 17.2.
```

`[Advokat]` Taknivån och om 17.3 håller vid en domstolsprövning av gränsdragningen direkt/indirekt skada. Svensk rätt saknar en fast definition av "indirekt skada" utanför köplagen, och att avtala om att en post **är** direkt skada är vanligt men inte prövat i det här sammanhanget.

## A4. Behöver exklusiviteten i 2.1 kompletteras? (Fråga 4)

**Ja, och problemet är större än noteringsfilen antog.** `[Bedömning]`

Noteringen resonerade att exklusiviteten är praktiskt självgående eftersom appen flyttar till AP. Det stämmer **för Steam**. Men:

1. **1.4 definierar Platform som "PC through the Steam store".** 2.2 säger att upplåtelsen är begränsad till Platform och att inget annat är upplåtet. The Gang behåller alltså PC-rättigheterna på **Epic Games Store, GOG, itch, Humble och varje annan PC-butik**, fullt ut och utan att bryta mot avtalet.
2. **Kombinerat med 10.2 är det ett verkligt läckage.** 10.2 ger The Gang rätt att när som helst under löptiden få ut hela den aktuella källkoden inklusive AP:s ändringar, gratis och inom tio arbetsdagar, **utan en enda begränsning i vad de får göra med den**. The Gang kan alltså begära AP:s färdiga P2P-bygge på tisdagen och sälja det på Epic på fredagen, helt lagligt enligt avtalets ordalydelse, medan AP recouper sina 100 000 kronor på Steam.
3. **Samma sak på konsol och mobil.** 13.1 lägger dem utanför avtalet och 13.2 ger AP 60 dagars förhandlingsföreträde. Men inget hindrar The Gang från att ta AP:s färdigställda kod enligt 10.2 och porta den. Förhandlingsföreträdet gäller vem som ger ut, inte vem som får använda AP:s arbete.
4. **Det saknas också en varumärkeslicens.** 2.1 ger rätt att publicera och marknadsföra spelet, men ingenstans står att AP får använda namnet Curveball och spelets logotyp. Det är förmodligen underförstått, men det är gratis att skriva ut.

### Föreslagen text

Alternativ A, om Robert vill ha hela PC-marknaden (min rekommendation, eftersom AP tar hela kostnaden):

```
1.4 "Platform" means personal computers (Windows, macOS and Linux) through any digital
storefront. "Territory" means worldwide.
```

Alternativ B, om Steam ska förbli avgränsningen, minimum:

```
2.4 During the term the Developer shall not itself publish, distribute, sell or
otherwise make the Game available on any storefront for personal computers, and shall
not licence or authorise any third party to do so. This applies whether or not the
version concerned includes the Publisher Contributions.

2.5 The Developer grants the Publisher a non-exclusive licence to use the name, logo
and other trade marks of the Game to the extent needed to publish and market the Game
under this Agreement.
```

Och i båda fallen, begränsning i 10.2:

```
10.2 The Developer may at any time request the complete current source code, including
the Publisher's changes. The Publisher shall deliver it free of charge within ten (10)
business days. Source code delivered under this section may be used by the Developer
for verification, security and continuity purposes only. While this Agreement is in
force the Developer shall not exploit it commercially on any platform, and shall not
authorise a third party to do so.
```

## A5. Formkravet vid undertecknandet och OpenSign-flödet (Fråga 5)

`[Bedömning]`

1. **AP:s sida är korrekt uppställd i utkastet.** AP AB tecknas två i förening av styrelseledamöterna (`reference_company_structure`, bekräftat mot registreringsbeviset). Rättsligt: styrelsen företräder bolaget och tecknar dess firma enligt `ABL 8 kap. 35 §`, och en registrerad firmateckning i förening innebär att **en ensam ledamots underskrift inte binder AP**. Robert kan alltså inte signera ensam, och signaturblockets två AP-rader är rätt konstruktion. Mattias Wiking som medtecknare är enligt Roberts beslut 2026-09-04.
2. **Elektronisk signatur räcker i sig.** Det finns inget formkrav på skriftlighet eller egenhändig namnteckning för ett publishingavtal. OpenSign producerar en enkel elektronisk signatur (SES), vilket är giltigt för svenska B2B-avtal under eIDAS. Ingen avancerad eller kvalificerad signatur behövs. (`reference_digital_signatures`.)
3. **Den verkliga risken ligger på motpartens sida, inte vår.** Enligt kontrollen 2026-09-04 är **Gustav Linde VD och styrelseordförande i The Gang Studio AB, inte Joel**. En VD har behörighet för den löpande förvaltningen enligt `ABL 8 kap. 29 §`. Ett avtal som upplåter exklusiva världsomspännande rättigheter till bolagets enda produkt och flyttar dess Steam-app till en annan part är inte löpande förvaltning. Undertecknar fel person binder avtalet **inte** The Gang (`ABL 8 kap. 42 §`), och AP:s enda motpart blir undertecknaren personligen enligt `AvtL 25 §`, vilket är värdelöst.
4. **Åtgärd före utskick till signering:** begär registreringsbevis för The Gang Studio AB, låt den eller de som står som firmatecknare där skriva under, och om Joel ska teckna i stället, begär ett styrelseprotokoll eller en fullmakt som bilaga till avtalet.
5. **OpenSign-flödet med tre undertecknare.** Ordnad signering, med de två AP-tecknarna först och The Gang sist, eller tvärtom. Två praktiska saker som är belagda tidigare (`devops_learnings`, `reference_digital_signatures`):
   1. Signaturblocket här har formen `Signature: ___` utan ankartexterna `For and on behalf of` eller namnrader på formen `<Namn>, Board Member`. Både `nda`- och `sub`-placeringen i `opensign.js` returnerar då `null` och faller tillbaka på `last`, som slänger fälten längst ned på sista sidan. **Använd `placement: 'manual'` med egna koordinater.**
   2. Lägg `<div style="page-break-before: always;"></div>` före signaturrubriken så att blocket inte straddlar en sidbrytning, och skriv understrecken escapade (`\_\_\_`) så att markdown inte gör om raden till `<hr>`.
6. **Ingångsdatum.** Ingressen säger "as of the date of last signature". Med tre undertecknare i ordnad signering är det den sista i kedjan som sätter datum, och det är också det datum tolvmånadersfristen i 11.2 räknas från. Det är korrekt men bör knytas till ett definierat begrepp, se F2 nedan.

---

# Del B. Övriga fynd, rangordnade efter allvar

## F1. Kedjan: äger The Gang Studio AB överhuvudtaget spelet? `[Advokat]`

**Detta är den enskilt största risken i affären, och den är inte avtalsteknisk.**

1. Enligt kontrollen 2026-09-04 finns **två bolag på Slakthusplan 3**: The Gang Studio AB (559511-5568, registrerat 2024-12-17) och **The Gang Sweden AB (559224-9691, registrerat 2019, 158 anställda)**.
2. **Steam-appen 2805120 är äldre än The Gang Studio AB.** Spelet var på NextFest och har en butikssida, en demo och önskelistor från tiden före december 2024. Det talar starkt för att appen och sannolikt upphovsrätten ligger i The Gang Sweden AB, inte i den part vi skrivit avtalet med.
3. **Konsekvensen är nemo dat.** Upplåter Studio AB rättigheter det inte äger får AP ingenting. Bakgrund A i avtalet ("the Developer... owns, or holds the right to use, all intellectual property rights") och garantin i 16.2 är då AP:s enda skydd, och det skyddet är en fordran mot ett bolag registrerat 2024 vars tillgångar vi inte känner till.
4. **Praktiskt bevis som är billigt att skaffa:** Steamworks-kontot visar vilken juridisk person som äger appen (kontonamn, bank- och skatteuppgifter). Be Olle eller Gustav om en skärmbild av kontots företagsuppgifter, eller ställ frågan rakt ut. Överföringen enligt 5 kommer ändå att avslöja det, men då har vi redan skrivit på.
5. **Åtgärder, i fallande ordning:** (a) rätt bolag som part, (b) båda bolagen som parter, (c) en skriftlig bekräftelse och överlåtelse från The Gang Sweden AB till Studio AB som bilaga, (d) en moderbolagsgaranti. Alternativet, att bara lita på 16.2, rekommenderar jag inte.

### Föreslagen skärpning av 16.2 oavsett vilken väg som väljs

```
16.2 The Developer warrants that it is the sole owner of the Game and of the Steam App,
that no other company in the same group or otherwise holds any right in the Game or the
Steam App, that the Game does not infringe the rights of any third party, and that it
holds all third party engine, middleware, plugin and asset licences needed for the Game
to be developed, published and sold on the Platform, and that those licences permit the
Publisher to exercise the rights granted in section 2.
```

## F2. 5 plus 11.2 plus 12.2: AP kan förlora app, kod och andel utan ersättning `[Bedömning]`

Det här är den samverkan Robert bad mig titta särskilt på, och den är verklig.

1. **Kedjan:** appen flyttas till AP vid undertecknandet (5.1). AP lägger ned månaders arbete utan kontant ersättning. Lanseringen glider förbi tolv månader. The Gang säger upp enligt 11.2. Då inträffar **allt** samtidigt: appen går tillbaka (12.2), den kompletta källkoden inklusive AP:s ändringar lämnas över automatiskt och gratis (10.3), och AP:s intäktsandel upphör (12.5). AP står utan app, utan kod, utan andel och utan en krona.
2. **"Launched" är odefinierat.** Räknas Early Access? Räknas en release i en enda region? Räknas ett demo? Det är det ord som avgör om hela ovanstående inträffar, och det finns inte i definitionerna.
3. **Fristen löper utan tillägg för motpartens dröjsmål.** Om The Gang dröjer med appöverföringen (5), med LootLocker-accessen (4.3) eller med publisher key (4.2), äter det av AP:s tolv månader. Det är i praktiken en möjlighet för motparten att skapa den uppsägningsgrund den sedan åberopar. Detsamma gäller ett IP-anspråk enligt 16.2 som tvingar AP att pausa, och force majeure enligt 18.5, som i dag inte påverkar 11.2 alls.
4. **Uppsägningsrätten har ingen tidsgräns.** Om AP lanserar i månad tretton, kan The Gang då fortfarande säga upp med hänvisning till att lansering inte skedde inom tolv? Ordalydelsen säger ja. Det gör AP uppsägningsbart för alltid av en historisk händelse.
5. **Forfeituren av AP:s eget arbete saknar motvikt.** Att AP förlorar rätten att publicera är rimligt. Att The Gang samtidigt får AP:s färdiga P2P-implementation, den nya backendintegrationen och antifuskarbetet gratis är det inte.

### Föreslagen text

```
1.6 "Effective Date" means the date of the last signature to this Agreement.

1.7 "Launch" means the Game being made available for sale to the general public on the
Steam store, whether in early access or as a full release.
```

```
11.2 If the Publisher has not Launched the Game within twelve (12) months from the
Effective Date, the Developer may terminate this Agreement by written notice given
within thirty (30) days of the end of that period. The right lapses on Launch and on
the expiry of that notice period. The twelve month period is extended day for day by
(a) any delay caused by the Developer, including any delay in completing the transfer
under section 5 or in providing the access under sections 4.2 and 4.3, (b) any period
during which the Publisher has suspended work or distribution because of a third party
claim covered by section 16.2, and (c) any event of force majeure under section 18.5.
On termination under this section the Publisher's right to publish ends and the
Publisher retains no revenue share.
```

```
5.1 On signature of this Agreement the Steam App shall be transferred from the
Developer's Steamworks account to the Publisher's Steamworks account, using the app
transfer tool built into Steamworks. The transfer shall be initiated within five (5)
business days of the Effective Date and each Party shall complete the steps required of
it without delay. The Publisher becomes the publisher of record.
```

## F3. AP:s eget arbete: ingen äganderätt, ingen överlåtelse, ingen begränsning `[Bedömning + Advokat]`

1. **9.1 är juridiskt oriktigt så snart AP skrivit en rad kod.** Den säger att The Gang äger "the Game and all underlying material, including the source code". Svensk rätt känner inte work for hire. Upphovsrätten till det AP skapar uppkommer hos AP (`URL 1 §`) och övergår bara genom avtal (`URL 27 §`). Något överlåtelseavtal finns inte i dokumentet. 9.1 är alltså en beskrivning som inte stämmer, och 10.2/10.3 är enbart leveransplikter, inte licenser.
2. **Det skär åt båda hållen.** The Gang får koden men enligt `URL 28 §` får en förvärvare varken ändra verket eller överlåta rätten vidare utan avtal. Det gör The Gangs position efter en hand-back osäker, och det gör AP:s position oklar. Oklarhet i ett avtal om vem som äger vad är alltid dyrare än en tydlig fördelning, även när oklarheten tillfälligt gynnar oss.
3. **9.3 ger dessutom bort AP:s generella verktyg för evigt.** "The Developer receives a free, unlimited and perpetual licence to use those tools and services for the Game." Det gäller alltså även efter att avtalet upphört av vilket skäl som helst, gratis, för alltid. Grant-tjänsten är byggd av AP och är återanvändbar över projekt. Att licensen är evig ska matchas mot att AP:s andel kan vara det.

### Föreslagen text

```
9.5 The Publisher retains ownership of the copyright in the code, assets, tools and
documentation it creates under this Agreement (the "Publisher Contributions"). The
Publisher grants the Developer a licence to use the Publisher Contributions as part of
the Game for the term of this Agreement, and after termination on the terms of section
10.4. Section 9.1 is read subject to this section.
```

```
10.4 Where this Agreement is terminated other than under section 11.2 or for the
Publisher's uncured material breach, the licence in section 9.5 becomes perpetual and
irrevocable on termination. Where this Agreement is terminated under section 11.2 or
for the Publisher's uncured material breach, the Developer may use the Publisher
Contributions only against payment of the Publisher's documented development cost for
them, or, at the Developer's option, the Publisher shall deliver the source code
without the Publisher Contributions.
```

```
9.3 The Publisher retains ownership of the general tools and services it has built that
are not specific to the Game, for example its item grant service. The Developer
receives a licence to use those tools and services for the Game, free of charge for as
long as this Agreement is in force and for as long as the Publisher retains a revenue
share under section 12.5, and thereafter on the Publisher's then applicable commercial
terms.
```

`[Advokat]` Om Robert hellre vill hålla 9.1 som den är av förhandlingsskäl, låt advokaten bedöma vad AP faktiskt sitter på i ett hand-back-läge utan uttrycklig överlåtelse. Min bedömning är att oklarheten inte är värd den taktiska fördelen.

## F4. Tredjepartslicenser: Unreal-royaltyn, EAC, LootLocker, middleware `[Bedömning]`

1. **Unreal Engine 5.3 kostar 5 procent.** Epics standard-EULA tar ut fem procents royalty på världsomspännande bruttointäkt över de första 1 000 000 USD i livstidsintäkt per produkt (verifierat mot unrealengine.com/eula/unreal 2026-09-04). Vid en lansering som gör mer än en miljon dollar landar den kostnaden på **den som är säljande part**, alltså AP.
2. **1.3 tillåter ingen avräkning för den.** "No internal costs of either Party are deducted before the split." Motorroyaltyn är inte en intern kostnad, den är en avgift på försäljningen, men ordalydelsen fångar den inte och AP får då betala den ur sina 30 procent. Vid stor framgång kan de fem procenten av brutto vara en betydande del av AP:s trettio procent av netto.
3. **Licenshavarfrågan är separat och kan blockera lanseringen.** Epics EULA är knuten till licenstagaren. AP behöver egen Unreal-licens och egen royaltyrapportering för produkten. Detsamma gäller EAC och Epic Online Services, GameAnalytics, Tolgee och varje Marketplace- eller Fab-tillgång i projektet, av vilka många är per licenstagare och inte överlåtbara. Ingenting i avtalet ålägger The Gang att leverera den listan eller att se till att AP får utöva licenserna.
4. **Praktisk följd redan nu:** EAC måste ändå ersättas eller tas bort före lansering enligt B3-testet 2026-09-01. Ta med det i samma inventering.

### Föreslagen text

```
1.3 ... No internal costs of either Party are deducted before the split. Engine,
middleware and other third party royalties payable on revenue from the Game, including
the royalty under Epic Games' Unreal Engine licence, are deducted before the split.
```

```
4.5 The Developer shall provide a complete list of the third party engine, middleware,
plugin, asset and service licences used in the Game, and shall do what is needed for
the Publisher to exercise or take over those licences to the extent required to perform
section 3 and to publish the Game.
```

## F5. Nettointäktens mekanik: återbetalningar, nycklar, reserv `[Bedömning]`

1. **Återbetalningar och chargebacks som kommer efter ett rapporterat kvartal** har ingen hantering. AP har redan betalat ut 70 procent på en intäkt som sedan går tillbaka. Det behövs en kvittningsrätt och en rimlig reserv.
2. **Intäkter som inte kommer "from Valve" faller utanför definitionen.** Steam-nycklar sålda via Humble, Fanatical eller ett bundle betalas av återförsäljaren, inte av Valve. Som 1.3 är skriven är sådan intäkt inte Net Revenue alls, alltså delas den inte. Det gynnar AP kortsiktigt men är ett hål The Gang kommer att peka på, och det är bättre att stänga det själv än att bli anklagad för att ha lagt det där.
3. **Första rapporteringsperioden** bör anges, liksom att en period utan intäkt rapporteras som noll i stället för inte alls.

### Föreslagen text

```
1.3 ... Net Revenue also includes amounts the Publisher receives for the Game from
other sources, including sales of Steam keys through resellers and bundle revenue.
```

```
8.6 If refunds or chargebacks are received after a quarter has been reported, the
Publisher may set the amount off against later quarters. The Publisher may retain a
reserve of up to ten (10) per cent of Net Revenue for a quarter against refunds and
chargebacks, to be released no later than in the second following quarter. A quarter
without revenue is reported as nil.
```

## F6. Momsen `[Revisor, inte advokat]`

1. Avtalet säger ingenting om moms. 8.2 säger bara att betalning sker mot The Gangs faktura.
2. **AP är inte momsregistrerat** enligt Skatteverkets svar 2026-08-27 (admin-learnings, apb-056). En intäktsandel till ett svenskt bolag är med största sannolikhet en momspliktig omsättning, alltså lägger The Gang 25 procent moms på sin faktura. Kan AP inte dra av den ingående momsen är det en **verklig kostnad på 25 procent av 70 procent av nettointäkten**, vilket förändrar affärens ekonomi väsentligt.
3. Det här är en fråga om pengar, inte om formulering, och den ska till revisorn **före signering**, inte efteråt. Två möjliga avtalslösningar beroende på vad revisorn säger:

```
8.7 All amounts in this Agreement are exclusive of value added tax, which is added
where applicable.
```

eller, om AP ska skyddas mot kostnaden:

```
8.7 The Developer's share under section 6.2 is inclusive of any value added tax
payable on it.
```

4. Notera också att AP som säljande part på Steam tar över Valves hantering av plattformsskatter, vilket redan är avräknat i 1.3.

## F7. Insolvens: licensen mot ett konkursbo `[Advokat]`

1. 11.4 ger AP rätt att säga upp vid The Gangs insolvens. Men AP vill sannolikt **inte** säga upp, AP vill fortsätta sälja spelet.
2. **Svensk rätt ger licenstagaren ett svagt skydd i licensgivarens konkurs.** Frågan om licensers sakrättsliga skydd är omdiskuterad och inte slutligt avgjord. Ett konkursbo kan välja att inträda i avtalet eller inte, och en licens som inte är sakrättsligt skyddad kan i värsta fall inte göras gällande mot boet eller mot en förvärvare av IP:t ur boet.
3. AP:s exponering är hela investeringen. Det här är en av två frågor i memot där jag inte kan ge ett svar som håller.
4. Möjliga grepp som advokaten får bedöma: en option för AP att förvärva spelet och Steam-appen vid The Gangs konkurs mot ett fastställt belopp (risk för återvinning), pant, eller ett escrow-upplägg. Notera att ett förvärvsvillkor som utlöses av konkursen i sig kan vara verkningslöst mot boet.

## F8. Spelardata och GDPR `[Bedömning]`

1. Avtalet reglerar appen, önskelistorna och följarna men inte **konton, progression och inventarier**. Efter LootLocker-utgången ligger ägandet i Steam Inventory Service, som följer appen, medan progressionen ligger i AP:s grant-tjänst, som inte gör det. Vid en hand-back får The Gang tillbaka en app vars spelare tappar sin progression.
2. Noteringsfilen flaggade detta 1 september och lät det medvetet vara. Jag tycker att det ska in nu. Det är en mening, och den gör hand-back-klausulen komplett i stället för att lämna en teknisk tvist till det ögonblick då parterna redan är osams.
3. **Det saknas också helt en dataskyddsklausul.** Steam-ID är personuppgift. AP driver en tjänst som behandlar spelardata, och 4.3 innebär att The Gang exporterar spelardata till AP. Två meningar räcker för att slippa frågan.

```
12.7 On termination the Publisher shall deliver the player progression and entitlement
data held in the Publisher's services in a documented, machine readable format within
thirty (30) days.
```

```
18.10 Each Party is a separate controller for the personal data it processes in
connection with the Game and is responsible for its own compliance with Regulation (EU)
2016/679. If either Party processes personal data on behalf of the other, the Parties
shall enter into a separate data processing agreement.
```

## F9. Mindre punkter, men värda att rätta i samma version `[Bedömning]`

1. **Bakgrund C beskriver arbete AP redan utfört på The Gangs upphovsrättsskyddade kod utan skriftlig licens.** Recitalet är i dag ett erkännande utan täckning. Lägg till ett ratificerande stycke:
   ```
   E. The Parties confirm that the work the Publisher carried out on the Game before the
   date of this Agreement was carried out with the Developer's consent and is covered by
   this Agreement.
   ```
2. **5.4 påstår att "No third party approval is required".** Det är i praktiken en garanti från båda parter om hur Valve beter sig. Mjuka upp: `The transfer is made through Valve's own tool and requires no approval other than Valve's processing of the request.`
3. **3.1 och 3.3 är öppna åtaganden som kan åberopas som väsentligt avtalsbrott.** "the polish required for launch" och "shall run community work" har ingen måttstock. Lägg in `as the Publisher reasonably determines` i 3.1 och `use reasonable efforts to` i 3.3. Detta hänger ihop med stupkanten i 12.5: varje vagt åtagande är en potentiell förverkandegrund.
4. **3.2 bör säga vem som bestämmer.** Lägg till: `The Publisher decides the release date, the release form, pricing and discounting for the Game.` Det var hela skälet till att appen flyttar.
5. **12.1 "within a reasonable time" bör knytas till 12.2.** `The Publisher shall stop selling the Game no later than on completion of the transfer under section 12.2.`
6. **18.7 anger bara e-postadresser, och för The Gang en personlig adress.** Lägg till bolagens registrerade adresser och kräv att uppsägning enligt 11 även skickas till den registrerade adressen. En uppsägning som bara går till en privat mailadress hos någon som slutat är en tvist som väntar på att hända.
7. **8.3 innebär att en extern person får användarbehörighet i AP:s Steamworks-konto.** Behörigheter i Steamworks sätts per app, men kontrollera att The Gangs användare inte ser AP:s övriga titlar innan accessen ges. Praktiskt, inte juridiskt.
8. **15.3 löper tre år efter upphörande medan intäktsandelen är evig.** Sekretessen bör täcka betalningsuppgifter så länge betalningar pågår.
9. **13.2 "If the Developer decides that a console or mobile version is relevant" är ett villkor motparten själv styr över.** Lägg till att förhandlingsföreträdet gäller `if the Developer decides to develop, publish or licence a console or mobile version, or receives an offer to do so`.
10. **18.4 släcker term sheetet, inklusive LUG-varianten.** Det är avsiktligt, men om LUG kommer in senare måste den strukturen in i ett eget avtal mellan AP och LUG. Sektion 7 räcker för att AP ska få göra det utan The Gangs samtycke.

---

# Del C. Vad jag bedömer själv och vad som måste till extern advokat

**Jag är intern rådgivare, inte advokat.** Ingenting i det här memot är en slutlig juridisk bedömning, och avtalet bör inte signeras förrän en advokat sett åtminstone punkterna nedan.

## Måste till extern advokat före signering

1. **Rättighetskedjan (F1).** Vilket bolag som äger spelet och Steam-appen, och hur avtalet ska konstrueras om det är The Gang Sweden AB. Detta är den enda punkt jag skulle stoppa signeringen på oavsett vad övrigt kostar.
2. **Den eviga andelens hållbarhet och skydd mot en inkråmsöverlåtelse (A2).** Håller 18.9 mot en godtroende förvärvare, och går andelen att förstärka sakrättsligt?
3. **Licensen i motpartens konkurs (F7).**
4. **Ansvarstaket och gränsdragningen direkt/indirekt skada (A3), särskilt om 17.3 håller.**
5. **Förverkanderegeln i 12.5 mot `AvtL 36 §`**, i den lydelse den slutligen får.

## Frågor som inte är advokatfrågor

1. **Momsen (F6)** går till revisorn, inte till advokaten, och den ska besvaras före signering eftersom den påverkar affärens ekonomi.
2. **Unreal-royaltyn och tredjepartslicenserna (F4)** är en teknisk och kommersiell inventering som GameDev kan göra ur repot, inte en juridisk fråga förrän listan finns.
3. **Firmateckningen och OpenSign-flödet (A5)** är process. Enda juridiska momentet är att kontrollera motpartens registreringsbevis, vilket vi gör själva.

## Mina egna bedömningar, som Robert kan agera på direkt

Allt märkt `[Bedömning]` ovan. Kort sagt: F2, F3, F5, F8, F9 och A1, A4 och A5 är sådant jag skulle ändra i version 2 utan att vänta på advokat, eftersom de antingen är rena drafting-fel eller kostnadsfria förtydliganden.

---

# Del D. Vad jag skulle göra härnäst, i ordning

1. **Ställ ägarfrågan till The Gang innan något annat.** Den är redan formulerad i mailutkastet 2026-09-04. Utan svaret vet vi inte vem som ska stå som part.
2. **Begär registreringsbevis** för det bolag som ska teckna, samtidigt.
3. **Skicka F6 (momsen) till revisorn** som en egen fråga, den har längst ledtid.
4. **Bygg version 2** med ändringarna i A1, A4, F2, F3, F5, F8 och F9 samlade, och skicka den som en version, inte som lösa kommentarer.
5. **Låt advokaten se version 2** med Del C som frågelista, i stället för att låta honom läsa hela avtalet fritt. Det halverar timmarna.
6. **Först därefter OpenSign**, med manuell fältplacering och ordnad signering i tre steg.
