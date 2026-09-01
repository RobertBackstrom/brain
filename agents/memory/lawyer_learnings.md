# Lawyer Agent Learnings

<!-- ROTATION-NOTE -->
> **This file holds the most recent entries only** (rotated by `assistant/rotate-learnings.js`, ~100 KB budget).
> Older entries live in `archive/lawyer/` and are listed in the archive index at the bottom of this file.
> Nothing is deleted and everything stays searchable via `rag_search(query, source="agents")`.
>
> **Still append new learnings to the TOP of this file** — rotation moves the tail out on its own.

>

<!-- Append new learnings with: learning, source project, date, category, tags -->
<!-- Categories: swedish_corp | swedish_tax | swedish_employment | swedish_ip | gdpr | contract_review | process | tooling -->
<!-- If Robert corrected a substantive legal point: tag `correction` and write the corrected position prominently. -->

## 2026-08-27 — Samtycke är inte disposition: "räcker klausulen?"-frågor ska dekomponeras per rättshandling
**Projekt:** k2c (Simon Jakobsson CZP-anställning, k2c-051) · **Kategori:** swedish_ip + swedish_employment + process · **Taggar:** URL 28 §, LAS 6 c §, SemL 5/16b/30 §§, AvtL 36/38 §§, koncernintern överlåtelse, SÄVA, uttagsbeskattning

1. **Frågan "räcker §8.7 eller behövs ett separat koncerninternt avtal?" var fel ställd, och rätt
   svar var att visa varför: klausulen och avtalet gör olika saker.** En vidareöverlåtelseklausul i
   ett anställningsavtal är den anställdes SAMTYCKE (krävs pga `URL 28 §`: utan avtal får
   förvärvaren varken ändra verket eller överlåta rätten vidare, verifierad ordagrant 2026-08-27).
   Själva flytten mellan bolagen är en egen rättshandling som systerbolaget måste vara part i;
   det kan aldrig förvärva genom ett anställningsavtal det inte är part i. **Metod: när någon
   frågar "räcker klausul X eller behövs dokument Y", lista först vilka separata rättshandlingar
   kedjan kräver och vem som är part i varje. Ofta är svaret "både och" för att alternativen löser
   olika länkar.** Formen på det koncerninterna avtalet: automatisk överlåtelse i förvärvsögonblicket
   (bolaget blir ren genomgångsstation), retroaktiv verkan för redan utfört arbete, back-to-back-
   scope, och ett vederlag (självkostnadsrecharge av lönekostnaden; vederlagsfritt öppnar
   uttagsbeskattning `IL 22 kap.` när bolagen inte är i äkta koncern).
2. **LAS 6 c § gör "avtalet är inte utskickat än" till en löpande lagöverträdelse med datum.**
   Skriftlig information om väsentliga villkor ska lämnas senast SJUNDE kalenderdagen efter
   arbetsstart, och för särskild visstidsanställning ska visstidsinformationen lämnas i samband
   med att anställningen ingås (båda verifierade ordagrant 2026-08-27). En anställd som börjat
   jobba utan påskrivet avtal ger alltså följebrevet ett lagstadgat sista-datum (här 2026-08-31),
   inte bara processlogik. **Säg det i deadline-termer till klienten; det flyttar prioritet.**
3. **Inbakad semesterersättning ("lön inkl 12 %") håller bara därför att komponenterna är separat
   specificerade.** `SemL 5 §` (anställning högst tre månader: får avtalas att ledighet inte läggs
   ut, ersättning i stället) + `16 b §` (procentregeln 12 %) + `30 §` (utbetalning senast en månad
   efter anställningens slut). Transparensen (grundlön X + semesterersättning Y = brutto Z, i
   avtalet) är giltighetsvillkoret. **Varning till nästa avtalsbygge: när en klientversion "städas"
   får komponentspecifikationen inte redigeras bort, den är det som bär konstruktionen.**
4. **Kolla om det nya upplägget bryter en tidigare beslutad strukturprincip innan det byggs
   vidare.** Maj-memots princip var "CZP never holds IP" (alla sub-överlåtelser AP-direkt).
   Anställningen tvingade in CZP i kedjan; rätt reparation var minimal (konduit-design), inte att
   tyst ge upp principen. Och kontrollen avslöjade en större lucka: paying-agent-avtalet som alla
   refererar som "the existing agreement" var fortfarande OSIGNERAT enligt contracts-trackern.
   **Verifiera alltid signaturstatus på det "befintliga" avtal ett nytt dokument ska luta sig mot.**
5. **Tooling, Google Sheets-radinsättning utan formelhaveri:** läs arket med
   `valueRenderOption=FORMULA` först, sätt in raden INUTI sum-rangen (insertDimension med
   startIndex på näst sista konstituentraden) så expanderar `=SUM(F9:F16)` till `F9:F17` av sig
   själv, och korsflikreferenser (`=k2c_pnl_2026!F25`) autojusteras i samma arbetsbok. Verifiera
   efteråt genom att räkna delta på totalerna (här: exakt raden + 10 % contingency). Och läs
   A1-cellen innan skrivning: legacy-banners ("MIGRATED, EDIT THERE") pekar om målet; underlaget
   pekade på fel ark.

---

## 2026-08-27 - Räkna ut vad bevakningen faktiskt är värd innan du prissätter en förlikning, och kontrollera VEM som äger anspråket
**Projekt:** apb/czp (APDS K 4429-25, anmärkning aktbil 58 mot CZP:s bevakning, apb-053) · **Kategori:** swedish_corp + process · **Taggar:** KL 4:10, KL 4:19, KL 4:20, KL 9:6, ABL 25:18, ABL 17:7, ABL 29:1, SFL 59:13, bevakningsförfarande, förlikningssammanträde, återvinning

1. **Klienten var beredd att betala sig ur en process där han inte kunde förlora pengar.** Robert
   läste anmärkningen mot CZP:s bevakning som ett kontantkrav på 192 000 kr. Det var det inte.
   Förvaltaren hade valt anmärkningsvägen (`KL 4:19` 1 st p 2), som är fristlös men **defensiv**:
   utfallet är att bevakningen sätts ned, inte att borgenären åläggs betala. Hans egen skrivning
   avslöjade valet ordagrant, "ska avräknas från Borgenärens utdelningsfordran". Kontantkravet
   kräver stämning enligt `KL 4:20` 1 st, här med frist 2026-12-14. **Regel: läs alltid vilken av
   de tre vägarna i 4:19 förvaltaren valt, och citera hans egen yrkandeformulering som bevis.**
2. **Och bevakningen som skulle "försvaras" var värd noll.** Boet hade 301 765 kr mot 6 076 746 kr
   bevakat, konkurskostnaderna före. Utdelningsprocenten är den första siffran som ska räknas fram
   i varje bevakningstvist, före varje juridisk analys. Utan den rekommenderar man klienten att
   betala för att skydda något värdelöst och lämnar den riktiga risken, stämningsfristen, öppen.
   **Följd för uppgörelsetexten:** den ska skrivas som avstående från *återvinningsanspråket*, inte
   som återkallande av anmärkningen. Annars ger klienten upp bevakningen och behåller risken.
3. **Ägarfrågan avgör vad förvaltaren överhuvudtaget kan sälja.** Boet kan efterge `KL 4 kap.`,
   `ABL 17:6/17:7` och `ABL 29:1` för bolagets räkning. Boet kan **inte** efterge `ABL 25:18`
   (varje enskild borgenärs eget anspråk), `SFL 59:13` (statens) eller borgenärs egen `ABL 29:1`.
   Robert kom fram till detta själv innan jag hann svara, och han hade rätt. **Skriv aldrig in en
   "köp bort allt"-ambition i ett bud till en förvaltare som inte äger anspråken.** Ny KB-sektion i
   `wiki/legal/sv_corp_law.md`.
4. **Taktisk följd som är lätt att missa:** ta inte upp 25:18 med förvaltaren. Han kan ändå inte
   binda borgenärerna, och frågan signalerar bara att klienten ser exponeringen. Här låg den
   verkliga 25:18-risken hos två helt andra parter, Skatteverket (53 % av massan) och WLBS
   konkursbo.
5. **Förvaltarskrifter innehåller sakfel som är värda att leta efter.** Här: "fem betalningar" följt
   av sex uppräknade, och påståendet att underlag "inte påträffats" när de daterade lånemotposterna
   låg i den huvudbok förvaltaren själv lämnat ut. Faller de 107 000 kr som var låneåterbetalning
   bort understiger resterande 85 000 kr tioprocentsgränsen i `KL 4:10`, alltså brister
   avsevärdhetsrekvisitet. **Stäm alltid av förvaltarens beloppslista mot gäldenärens huvudbok per
   konto, inte bara mot datum och summa.**
7. **Två Robert-korrigeringar på samma dokumentpaket, båda värda att internalisera.**
   (a) **Avslöja inte för domstolen att en förlikning är på väg.** Utkastet till yttrande skrev att
   parterna nått en principöverenskommelse. Robert invände. Han hade rätt på tre punkter:
   föreläggandet efterfrågar **inställning**, inte förhandlingsstatus; uppgiften skadar om
   uppgörelsen spricker, eftersom akten då visar att klienten var villig att göra upp innan någon
   prövning börjat; och det är **inte borgenärens sak att ensidigt karakterisera förvaltarens
   ståndpunkt** inför rätten dagar innan han ska underteckna. Uppgörelsen anmäls **gemensamt när
   avtalet är påskrivet**. Ersättningstexten blev inställning plus fyra enradiga skäl och "avser att
   utveckla sin talan vid sammanträdet", vilket möter kallelsens krav på att bifoga det som styrker
   fordran utan att utveckla argumentationen.
   (b) **Docera inte juridik för motpartens advokat och erbjud dig inte att skriva avtalet åt
   honom.** Se `skills/voice/channel_mail.md`, avsnittet om mail till motpartens jurist. Lagrummen
   hör hemma i vårt interna underlag; i mailet räcker önskemålet om vad avtalet ska innehålla.
   **Generell regel: när mottagaren är en specialist i sitt eget fält, leverera kravet och utelämna
   motiveringen.**

7. **Ingivande till tingsrätt: e-tjänsten slår mejlad signerad PDF, och den signerar åt dig.**
   `https://digitalhandling.etjanst.domstol.se/digitalhandling` tar handlingar i **pågående mål**,
   kräver målnummer, och låter ingivaren **signera med BankID i tjänsten**. Endast PDF vid signering,
   max 18 MB; utan signering tas fler format. Det gör OpenSign- eller scanna-steget onödigt för
   domstolshandlingar och ger ett kvitto. **Detta kompletterar posten 2026-07-10 om att inlagor kan
   ges in som mejlad signerad PDF: det stämmer fortfarande, men e-tjänsten är förstahandsvalet.**
   Mejlvägen är kvar som fallback, och då till avdelningens adress ur kallelsen
   (`umea.tingsratt.allmanna@dom.se`), inte domstolens allmänna växeladress. Verifierat 2026-08-27.

7. **"Vi löser det med kvittning" är inte ett avslut, och det är den farligaste meningen i hela
   ärendet.** När klienten och förvaltaren blivit överens i god ton är frestelsen att skriva en kort
   uppgörelse som bara justerar bevakningen. Men förvaltarens "kvittning" är avräkning **inom**
   bevakningsförfarandet, och den lämnar `KL 4:20` 1 st-fristen för en riktig återvinningstalan
   orörd. **Regel: varje uppgörelse med ett konkursbo måste innehålla ett uttryckligt avstående från
   det bakomliggande anspråket, inte bara en reglering av det processuella momentet.** Skriv
   klausulen själv och var först med pennan. Lägg också in att avtalet inte innebär medgivande i
   sak, annars kan en uppgörelsetext i ett ärende användas mot klienten i ett annat (här:
   APDS-uppgörelsen mot kundförlustlinjen i Runatyrs moms). Och begränsa avtalet till rätt parter:
   en "samtliga mellanhavanden"-klausul mot ett bolag får inte svepa in klientens **privata**
   bevakning i samma konkurs.

7. **Underrättelsen till GÄLDENÄREN är den billigaste vägen att räkna alla anmärkningar i en
   konkurs.** Rätten skickar en underrättelse till konkursgäldenären om förlikningssammanträdet och
   bifogar **samtliga** anmärkningsskrifter, eftersom gäldenären har rätt att yttra sig över varje
   tvistig bevakning. Här bifogade aktbilaga 64 både 57 och 58, vilket bevisade att bara två
   borgenärer var anmärkta och att klientens *privata* bevakning stod oanmärkt. **Regel: när en
   klient är både borgenär och företrädare för gäldenären, läs gäldenärsexemplaret först. Det ger
   hela tvistebilden, borgenärskallelsen ger bara den egna.**
8. **Jämför förvaltarens anmärkningar mot varandra för att skilja standardtext från substans.**
   Aktbilaga 57 (mot ABEX) och 58 (mot CZP) hade identisk `KL 9:6`-öppning ord för ord, men 57 var
   *reservationsvis* och saknade andrahandsgrund. Slutsats: 9:6-grunden var förvaltarens rutinöppning
   mot flera borgenärer, och den verkliga exponeringen låg i `KL 4:10`. Utan jämförelsen hade
   klienten lagt förhandlingskrutet på fel grund.

6. **En begäran om tidredovisning besvaras med avtalskonstruktionen, inte med rekonstruerade
   tidsedlar.** Fast månadsarvode betyder att tidredovisning aldrig krävts och inte finns. Men
   "den finns inte" räcker inte som ensamt svar: det förvaltaren egentligen vill ha är bevis för
   utförd prestation, och det levereras med styrelsehandlingar, korrespondens, ingångna avtal och
   leveranser.

## 2026-08-26 — Plattformsentitetsflyttar: beviskravet är uppfyllt långt innan flytten kan börja
**Projekt:** apb (APDS -> CZP över Nintendo, PlayStation, Xbox) · **Kategori:** contract_review + process · **Taggar:** entitetsflytt, Sony Title Transfer, Nintendo NDP, Xbox MSA V2, payee, konkurs

1. **Två avtal i en kedja uppfyller tillsammans ett beviskrav som inget av dem klarar ensamt.**
   Sonys krav är titelnamn + datum + båda parters underskrifter. Boavtalet bär **titelnamnen** i
   bilagan men har inte CZP som part. Nästa avtal bär **CZP som part** men beskriver tillgångarna
   generiskt. Skicka alltid båda, i kronologisk ordning, och säg uttryckligen vilket som bär vad.
   **Kontrollera kravet fält för fält mot handlingarna innan något skickas**, i stället för att
   anta att "vi har avtalet" räcker.
2. **Att bevisningen äntligen finns betyder inte att spåret kan börja.** På PlayStation var den
   verkliga blockeraren hela tiden att den mottagande entiteten **inte existerar i motpartens
   system**. `/api/v1/partners` returnerade exakt en partner, den avlämnande. Sony kan inte flytta
   något till en icke-existerande part, och ledtiden startar inte förrän de kan agera.
   **Metod: fråga alltid först "finns mottagaren hos motparten?" innan man optimerar underlaget.**
   Onboarding av mottagaren har längre ledtid än själva flytten.
3. **En fryst funktion hos motparten kan vända rätt lösning helt.** Steam löstes app för app.
   På Xbox är per-produkt-reparenting fryst för MSA V2 utan ETA, samtidigt som alla titlar på
   kontot hör till samma förvärvade rörelse. Då är rätt drag att **ändra juridisk person på det
   befintliga kontot** i stället för att flytta produkter. Samma juridiska faktum, motsatt
   mekanik, för att motpartens verktyg skiljer sig. Läs motpartens begränsningar innan man
   kopierar en process som fungerat någon annanstans.
4. **En felande betalning kan vara ett entitetsbesked, inte ett fältfel.** Nintendos
   `RSN REGULATORY REASON` är en bankcompliance-avvisning mot en entitet i konkurs. Ingen
   payee-redigering kan någonsin laga den. **Ett ärende med fel rubrik hamnar hos fel avdelning:**
   en transferbegäran inne i en "your payment has failed"-tråd hanteras som ett bankärende. Öppna
   ny tråd och låt payee lösas som en konsekvens av flytten.
5. **Kontrollera vem som faktiskt står som juridisk person på plattformskontot, inte vem man tror.**
   Ett mail från 2022 visade att Xbox-kontot bar ett bolag som gick i konkurs 2024. Kedjan kan
   alltså vara en konkurs djupare än ärendet utgår från. Samma kontroll gäller varje plattform.
6. **Skilj API-credentials från kontoägarskap.** Jag drog slutsatsen "APDS har en egen
   Microsoft-tenant" ur ett dokument med Azure client-ID och tenant-ID. Det var säljdata-
   credentials, inte kontoägarskap. **En tenant-ID i en integrationsfil säger ingenting om vem som
   äger Partner Center-kontot.**
7. **När Robert avböjer advokatgenomlysning: notera beslutet, och omsätt de öppna frågorna till
   arbetsmoment i stället för att driva frågan igen.** Tre av fyra var administrativa och stängs
   med mail. Den fjärde, hur långt vi får gå i att beskriva oss som rättighetshavare, omsattes till
   en stående formuleringsregel i varje plattformsärende. Det är den formen en avböjd granskning
   ska ta: inte bortglömd, inte upprepad, utan inbyggd i hur arbetet utförs.

---

## 2026-08-26 — Bilagan, inte överlåtelseklausulen, avgör vad ett konkursboförvärv faktiskt bär
**Projekt:** apb/czp (APDS konkursbo -> Bright Gambit -> CZP, apb-051) · **Kategori:** swedish_ip + contract_review
> **Kanoniska fakta ur den här posten är promotade till [[project_apds_czp_rights_chain]]** (kedjan, bilaga 2:s ägarfördelning, formuleringsregeln). Läs det minnet för fakta, den här posten för metoden. · **Taggar:** KL 7:10, konkursbo, rörelseöverlåtelse, äganderättsförbehåll, nemo dat, verksamhetsöverlåtelse-moms, entitetsflytt, Scrive

1. **Läs ägarkolumnen i bilagan innan du läser överlåtelseklausulen.** Boavtalet överlät "rätten
   till bolagets immateriella rättigheter, inklusive men inte begränsat till källkod och
   distributionsrättigheter", vilket låter uttömmande. Bilaga 2:s egen kolumn "IP Ownership",
   ifylld av gäldenärens ställföreträdare, sa att bara **5 av 17** poster ägdes av konkursbolaget.
   Sju ägdes av systerbolaget och fem av tredje man. Ett bo kan inte överlåta mer än gäldenären
   ägde, så bilagan är den operativa handlingen och rubriken är marknadsföring. **Metod: bygg
   alltid en ägartabell ur bilagan först, och låt den styra vad som får påstås utåt.**
2. **Skilj på positionen och äganderätten, och säg det innan någon skriver till en motpart.**
   Det som ändå överläts för en titel vars upphovsrätt ligger hos ett systerbolag är gäldenärens
   *position*: källkod, utvecklarroll, distributions- och publiceringsrättigheter. Det räcker för
   att flytta ett plattformskonto, eftersom plattformen flyttar kontot och publiceringspositionen,
   inte upphovsrätten. Det bär däremot inte meningen "vi äger IP:t" i ett mail till Nintendo eller
   Sony. **Den distinktionen är den enda av mina fyra fynd som faktiskt kan bita**, för den handlar
   om vad vi skriver till en motpart och inte om vad vi tror internt.
3. **Tillsynsmyndighetens godkännande är ett svar, inte en formalitet.** `KL 7 kap. 10 §`: i
   viktigare frågor ska förvaltaren höra tillsynsmyndigheten och särskilt berörda borgenärer, och
   försäljning av rörelse är uttryckligen en sådan fråga (verifierat mot riksdagen.se 2026-08-26).
   Bär avtalet en klausul om att TSM godkänt, citera den i första stycket av varje ärende. Den
   föregriper den enklaste invändningen mot förvärvet.
4. **Äganderättsförbehåll måste beläggas i VARJE led i en förvärvskedja.** Här fanns förbehåll i
   båda leden och betalning obelagd i båda: 55 000 till boets klientmedelskonto (inget kvitto) och
   sista raten av 110 000 till BG (aldrig ens fakturerad). En kedja som ser komplett ut på papperet
   kan alltså vara formellt obruten bara till namnet. **Begär betalningsbevis, inte bara avtalet.**
   Nyansen som räddar oss: i led två har säljaren inte fakturerat, så köparen är inte i dröjsmål.
5. **Ett mellanled är bättre än en direktöverlåtelse till ägarens holdingbolag.** BG köpte för
   55k i eget namn från boet och sålde vidare för 110k. Det bryter den raka linjen konkursbo till
   närstående och gör återvinningsangreppet svårare, trots att prispåslaget ser ut att inbjuda till
   frågor. Notera det aktivt som en styrka när kedjan redovisas.
6. **Momsen ska ställas om från början i varje led.** Boet skrev "torde mervärdesskatt inte utgå"
   (verksamhetsöverlåtelse). Nästa led debiterade ändå moms. Är även det ledet en
   verksamhetsöverlåtelse är det felaktigt debiterad moms, och köparens avdrag kan nekas.
   Momsbehandlingen ärvs inte, den prövas per transaktion.
7. **Insolvensklausul = ingenting överläts.** Vessels of Decay stod i bilagan med "Explicit
   termination if insolvency, liquidation, or bankruptcy". Klausulen utlöstes på konkursdagen,
   alltså före boets försäljning. Kontrollera klausulen innan en sådan titel räknas in i förvärvet.
8. **Kontrollera org.nr mot bilagorna och mot tingsrättens målhandlingar.** Ingressen bar
   "559380-1938", bilaga 1 och hela mål K 4429-25 bär 559320-7466. Rätt bolagsnamn gör det knappast
   ogiltigt, men det är en gratis invändning och rättas billigast med en skriftlig bekräftelse från
   förvaltaren. **Grep-vana: dra alla org.nr ur en signerad handling och diffa mot det egna
   materialet innan handlingen åberopas.**
9. **Process, och den är återanvändbar:** när en saknad länk i en rättighetskedja dyker upp, gå
   inte direkt till det brådskande ärendet. Bygg först ett register över *alla* nedströms
   beroenden. Här var det tio plattformar och partners, varav fyra (Xbox, Epic/UEFN, Overwolf,
   HeadUp) aldrig ens hade påbörjats trots att två av dem har löpande intäkt till ett konkursbo.
   Registret hittade mer pengar än det brådskande ärendet gjorde.

---

## 2026-08-17 — Credit finns inte som default, och tystnadsklausulen är det som faktiskt binder
**Projekt:** k2c/apb (AP↔Raw Fury LTC, Pharaoh Lands) · **Kategori:** contract_review + swedish_ip · **Taggar:** URL 3 §, VmL 1 kap. 11 §, complete agreement, back-to-back, portfolio-klausul, credit

1. **Frågan "vad säger avtalet om credit" besvaras nästan alltid med ingenting, och det svaret måste levereras som ett fynd, inte som en axelryckning.** RF-LTC:t är 12 sidor, nio sektioner, Schedule A/B/C. Noll om credit, splash, logo, marknadsföring eller PR. Ett rent outsourcingavtal med full överlåtelse (§4.3) ger utvecklaren ingen namngivning och ingen rätt att prata om jobbet. **Metod: leta inte bara efter klausulen, leta efter var den *borde* ha suttit** (ownership, special conditions i schedulet, general) och säg uttryckligen att den saknas i alla tre. Grep-ord som fångar den när den finns: `credit|splash|logo|publicit|announce|press|marketing|attribution|portfolio`.
2. **Det som faktiskt hindrar klienten är sekretessklausulen, inte den saknade creditklausulen.** §5.1 gör "the Work and the Customer Properties" till Confidential Information och förbjuder att publicera till tredje part utan skriftligt förhandsgodkännande, med indemnity (§6.1) kopplad just till sektion 5-brott. Ventilen är standardkarveouten "becomes publicly known without breach" (§5.2 a), som släpper exakt det förlaget självt gjort publikt och först när det gjort det. **Svara alltid på "får vi berätta om det?" ur sekretessklausulen först, credit-frågan är sekundär.**
3. **Två svaga fallbacks som ska presenteras som svaga.** (a) `URL 3 § 1 st` namngivningsrätt, ordagrant verifierad mot lagen.nu 2026-08-17, kan inte eftergivas blankt (3 § 3 st) och överlever total ekonomisk överlåtelse **men tillhör de fysiska skaparna, aldrig bolaget** (ett AB är inte upphovsman). Den ger namn i creditlistan, aldrig en splash. (b) `VmL (2010:1877) 1 kap. 11 § p 3`, ordagrant verifierad: referenshänvisning till innehavarens varor/tjänster i enlighet med god affärssed är tillåten, så "vi utvecklade X åt Y" är normalt lagligt, men den bär **inte** skärmdumpar, key art eller trailers, som är förlagets upphovsrätt.
4. **Complete agreement-klausulen (§9.1) gör muntliga credit-löften värdelösa.** Här hade klienten planerat en tio veckors relansering (apb-040) mot ett *verbalt* besked från förlagets marknadsansvarige om annonsdatum och credit, uttryckligen "planerat som en garanti". Enda bindande vägen är signerat skriftligt tillägg eller nytt schedule. **Regel: när en plan hänger på ett credit-antagande, kolla avtalet innan planen får löpa, inte efter.**
5. **Back-to-back-hålet som är lätt att skapa själv:** AP hade gett samtliga sex underkonsulter en §3.9 portfolio/showreel-rätt inklusive skärmdumpar och videoklipp ur den släppta builden. Den rätten fanns inte uppströms och kan inte vidarelicensieras. Klausulen räddades av sin egen förbehållsformulering ("subject to any publicity rules notified by Client or the upstream publisher"), men huvudregeln står: **grepa alltid de egna underavtalen efter rättigheter som saknar uppströms motsvarighet innan man svarar på vad klienten får göra.**
6. **Miss värd att skriva ned: RAG hittade inte att frågan redan var ställd.** Klienten hade tagit upp creditfrågan med förlaget på RF-synken 4 aug ("Niclas noted it, to be settled with Pontus"). Det stod i projektminnet `project_k2c_sands_of_duat.md`, men fyra `rag_search` med rerank över gdrive/gmail/project lyfte det aldrig — de returnerade planen (apb-040) men inte raden. **Regel: när frågan är "har vi redan tagit upp det här med motparten", grep:a projektminnesfilen direkt (`grep -niE "<nyckelord>" memory/project_<slug>.md`) utöver rag_search.** Semantisk sökning rankar dokument, och en enda mening i ett långt dagboksminne drunknar. Kostar två sekunder och avgör om rådet ska vara "fråga dem" eller "du har redan frågat, de sitter på svaret".
7. **Kanonisk fakta hör hemma i projektminnet, inte bara i loggboken:** avtalsläget (ingen creditklausul, §5.1 styr, skriftligt OK från förlaget räcker som mekanism) är promotat till [[project_k2c_sands_of_duat]] 2026-08-17 och den fulla analysen till `wiki/legal/sv_ip.md` § "Credit / attribution in co-dev and outsourcing agreements".
8. **Tooling:** `assistant/gdrive-read.js <fileId> <out.pdf>` + `pdftotext -layout` läser en signerad DocuSign-PDF ur Drive utan att spränga kontexten (undviker base64-vägen i `gdrive_read_file`). Hela 12-sidorsavtalet blev 3 547 ord och kunde läsas i sin helhet, vilket är rätt ambitionsnivå: **citera aldrig ett avtal på grep-träffar när det är litet nog att läsa helt.** Schedule C var "see attachment" i den signerade PDF:en, så det inkorporerade dokumentet (proposal v2) måste hämtas separat, och det har företräde enligt §1.1.

## 2026-08-07 — Domstolsarkivet är den snabbaste primärkällan som finns, och den används alltid för sent
**Projekt:** apb/czp/run (K 4429-25, T 3362-25) · **Kategori:** process + tooling · **Taggar:** dagboksblad, bevakningsförteckning, tredskodom, offentlighetsprincipen, securemail

1. **Tre mejl till tingsrättens arkiv gav mer på tolv timmar än veckor av intern analys.** Begäran skickad 23:52, svar 08:51 nästa morgon. Utfallet: dagboksblad i två mål, en tredskodom ingen kände till, och bevakningsförteckningen med samtliga borgenärer och belopp. Gratis, offentligt. **Regel: vid varje konkurs eller tvist, begär dagboksblad och bevakningsförteckning från domstolen INNAN du analyserar ur klientens eget material.** Adressmönster `arkiv.<domstol>@dom.se`. Ange målnummer och klientens relation till målet.
2. **Vad de tre handlingarna ger.** *Dagboksbladet* är hela processhistoriken med aktbilagenummer, ombudsbyten, delgivningar och avgöranden; här avslöjade det att ombuden frånträtt en månad före MUF och att TR ringt klienten personligen om delgivning. *Bevakningsförteckningen* är den enda handling som visar den verkliga borgenärsbilden; förvaltarberättelsens bouppteckning gjorde det inte (saknade en lönegarantipost om 1,77 Mkr och en slutlig dom om 3,49 Mkr). *Beslutet om bevakningsförfarande* innehåller rekvisitet ordagrant och är bevisning i sig.
3. **Tooling-gotcha som kostar en session om den missas.** Domstolarna svarar via `securemail.domstol.se`. Gmail-meddelandet innehåller **bara en logo.png**, så agenter kan inte läsa bilagorna, klienten måste öppna länken och ladda ned. Filerna raderas efter 30 dagar och man **måste** använda knappen "Logga ut"; stänger man bara webbläsaren dör engångslänken. Säg det i samma andetag som du ber om handlingarna.
4. **Stora PDF:er via `gdrive_read_file`** kommer base64-kodade och spränger kontextfönstret. Spara till fil, strippa allt utom base64-alfabetet, avkoda, kör `pdftotext -layout`. Fungerade på både 154 kB och 311 kB.

## 2026-08-07 — Verifiera att den namngivna motparten INTE existerar innan du hävdar att namnet är fel
**Projekt:** apb/czp (K 4429-25) · **Kategori:** process · **Taggar:** correction, misskontering, identitetsantagande, subagent-verifiering

1. **Två huvudfynd på ett dygn byggde båda på en identitet ingen kontrollerat, och båda föll.** (a) 400 000-krediten: kontot antogs vara klientens privatkonto utifrån en negativ arbetsanteckning ("EJ CZP"); det var gäldenärens sparkonto. (b) Acino-posten: en betalning bokförd mot "Levbet Acino AB" rubricerades som misskonterad närståendebetalning och som "materialets farligaste post". Acino AB visade sig ha partneravtal från 2023-12-22, åberopat i klientens **eget** svaromål i det parallella målet, och hade **själv bevakat 736 468 kr** i konkursen.
2. **Regeln:** innan en bokförd post kallas misskontering eller döljande, kontrollera om den utpekade motparten är en verklig avtalspart. Sök namnet i (i) bevakningsförteckningen, (ii) parternas inlagor i angränsande mål, (iii) klientens egen bevisning. Ett bolag som självt bevakar en miljonfordran är ingen bokföringsmässig täckmantel.
3. **Svag bevisning som lurade:** att ett verifikatnummer låg ur ordning (586 efter 588). Sekvensavvikelser i ett levbetflöde är brus, inte indicium.
4. **Meta, gäller allt frontier-modellarbete:** ett dyrare modelltier ger inte verifierade fynd. Slutsatser som vilar på "vems konto", "vems betalning", "vems bolag" ska spot-checkas mot primärkällan **innan** de går in i en advokatframställning. Kontrollen tog trettio sekunder i båda fallen.

## 2026-08-07 — Kundförlust: kvittningen är grunden, och botemedlet kan vara giftigare än sjukdomen
**Projekt:** run/apb (Runatyr → APDS, 4 Mkr + 1 Mkr moms) · **Kategori:** swedish_tax + swedish_corp · **Taggar:** ML 8:16, ML 16:23, kvittning, KonkL 9:1, ABL 25:13, Schmeink

1. **Kvittning är betalning och dödar kundförlusten.** ML 8:16 förutsätter en utestående fordran som inte går att driva in. Är fakturan reglerad genom kvittning finns ingen fordran kvar att förlora. Klientens invändning att "det påverkar inte momsen som ska rapporteras" är riktig men irrelevant: den påverkar inte redovisningsskyldigheten, den påverkar rätten till **nedsättning**.
2. **Pivotfrågan är säljarens egen huvudbok, inte gäldenärens.** Här hade gäldenärens redovisningskonsult bokfört kvittningen ensidigt medan säljaren aldrig behandlat fakturan som betald. Den asymmetrin räddade spåret: fordran lever hos säljaren och kvittningen behöver inte angripas frontalt. **Fråga alltid efter borgenärsbolagets balansräkning innan kundförlust rekommenderas eller avfärdas.**
3. **Varför det spelade roll att slippa angripa kvittningen:** att underkänna den hade raderat gäldenärens intäktsbokning om 5 Mkr, rivit EK-läkningen och öppnat ABL 25:18 bakåt ett helt år, där en slutlig tredskodom på 3,49 Mkr låg. Botemedlet var värt 1 Mkr, biverkningen 3,49 Mkr. **Räkna alltid effekten av åtgärden på klientens övriga exponering, inte bara på posten den ska lösa.**
4. **Kundförlust slår kreditering på Schmeink.** Ingen kreditnota krävs och köparen behöver inte justera sin ingående moms, så köparens avdrag får ligga kvar i det tomma boet. Avgörande när motparten är insolvent. Krediteringens dolda pris är dessutom bevismässigt: att kreditera en IP-faktura inbjuder frågan varför man fakturerade för rättigheter man sedan säger saknade värde.
5. **Beslutet om bevakningsförfarande är ett motargument mot kundförlust.** Lydelsen är "bevakningsförfarande ska äga rum **eftersom det kan antas att fordringar utan förmånsrätt erhåller utdelning**". Det är en judiciell bedömning som skär rakt mot rekvisitet "sannolikt att betalning inte kommer att fås", och den fattas normalt innan en enda bevakning kommit in. Motmedlet är aritmetik ur bevakningsförteckningen (här 302 tkr i tillgångar mot 6 077 tkr bevakat, konkurskostnader före) plus utdelningsförslaget när det kommer.
6. **Nedskrivningen kan starta en ny ansvarsklocka i borgenärsbolaget.** Skrivs en miljonfordran ned kan borgenärsbolaget självt hamna under halva aktiekapitalet och utlösa KBR-plikt enligt ABL 25:13, alltså ett andra ABL 25:18-fönster mot samma företrädare. **Gör aldrig nedskrivningen innan effekten på det egna kapitalet är räknad och en KBR förberedd.**

## 2026-08-05 — Blint-om-passet på APDS-komplexet: motpartsfältet ljuger, rådrum går inte bakåt, och "saknas i bokföringen" ska aldrig skrivas före en fyrvägsavstämning
**Projekt:** apb/czp/run (K 4429-25) · **Kategori:** swedish_corp + swedish_tax + process · **Taggar:** KonkL 4:10, 4:5, ABL 25:18, 25:20, 25:20a, NJA 2018 s. 602, NJA 2019 s. 941, NJA 2014 s. 948, SFL 59:15a, SFS 2026:561, ABL 21:2, delta-metod, felbokförd motpart

1. **En betalning som "saknas i bokföringen" kan vara bokförd på fel motpart.** 3 aug-passet sökte i APDS huvudbok 2440 efter CZP-referenser, hittade inget på 2025-11-03 och skrev "saknas i både 1675 och 2440". Fel: posten fanns som E 471 "Levbet Acino AB (586)" 25 000, samma dag och belopp som CZP:s bankinsättning. **Metod: vid bank-mot-bok-avstämning, sök på DATUM+BELOPP i hela huvudboken, aldrig bara på motpartsnamn.** Skillnaden är juridiskt kategorisk: "ospecificerad" är slarv, "fel motpart" är felbokföring (BrB 11:5-fragment, boets bästa 4:5-otillbörlighetsoptik) och den externa formuleringen "saknas i de konton boet lämnat ut" blir objektivt oriktig och motbevisbar av boet självt.
2. **SFL 59:15 a-rådrummet (SFS 2026:561, i kraft 2026-07-01, verifierad ordagrant) täcker bara betalningstidpunkter som INTE passerat** ("...som omfattas av ansökan och som först förfaller till betalning"). En rättelse av gammal period (Q1 2025 inlämnad 2026) kan aldrig räddas med rådrum; 59:13-bedömningen sitter kvar på ursprungliga förfallodagen (HFD 2018:4). Verktygen för gamla perioder: finansiering före/med rättelsen, nya 59:15-befrielsen (oskälighet, fyra uttryckliga faktorer varav proportionalitet och verksamma skadebegränsningsåtgärder), 59:19-överenskommelse. 3 aug-passet föreslog rådrum som fallback för Q1-rättelsen; det benet fanns inte.
3. **ABL 21:2-koncernundantaget kräver äkta koncern (ABL 1:11).** Ett holdingbolag med 30 % i moderbolaget är inte "samma koncern" som dotterbolaget; lån dotterbolag→holdingbolag ligger i förbjudna kretsen (21:1 p 1 och p 5) och bara det kommersiella undantaget kan rädda dem. Skriv aldrig "koncernundantaget täcker" utan att ha räknat ägarkedjan till majoritet i varje led.
4. **25:18-rättsfallspaketet att alltid dra i kapitalbristärenden** (alla verifierade mot lagen.nu 2026-08-05): NJA 2018 s. 602 (perioden slutar vid konkurs), NJA 2018 s. 1038 (inte vid rekonstruktion), NJA 2019 s. 941 (uppkomsttidpunkt lika för 18 § och 20 a §; förlikning skapar ingen ny förpliktelse), NJA 2014 s. 948 (borgenär med vetskap utan förbehåll förlorar kravet — dödar närstående borgenärers 25:18-hot), NJA 2014 s. 892 (avgången ledamot), NJA 2020 s. 526 (rättegångskostnader löpande). 25:20 kräver granskad KBR på HELA aktiekapitalet framlagd på stämma; 25:18 4 st friar bara läkning inom KBR-upprättandefristen. Faktisk läkning senare = oprövad fråga, körbar åt båda hållen.
5. **Delta-metoden fungerade men var nära att haverera på självförtroende:** jag skrev först delta-avsnittet utifrån learnings-postens sammanfattning av 3 aug-passet i stället för filerna själva, och fick skriva om det när de faktiska filerna visade sig ha fångat det mesta (inkl. 3/11-posten och accelerationsklausulen i Bergner-anteckningarna). **Delta får aldrig skrivas mot ett minne av dokumentet, bara mot dokumentet.** Och: ett "Haiku-pass" kan vara bra — läs innan du dömer.
6. **Verifiera draft-status före instruktioner om drafts:** "draften är inte skickad" i ett uppdrag kan vara sant samtidigt som en TIDIGARE version av samma mail redan är skickad i samma tråd (här: Bergner v1 skickad 2026-08-03 15:55, draften en nära identisk revision). Instruktionen "skicka draften" hade gett mottagaren dubblettmail. Kolla tråden, inte bara drafts-listan.
7. **lagen.nu via curl + strip är pålitligare än WebFetch för lagtext.** WebFetch-sammanfattningen hallucinerade paragrafinnehåll (gav 8:49-innehåll för 8:23, gåvoregeln för 4:10). Curl + tag-strip + frassökning ger ordagrann text med SFS-nummer för senaste ändring. Skatteverket/riksdagen 403-blockerar fortfarande.
8. ~~1675-skuldsaldot vilar på en overifierad 400k-kredit~~ **RÄTTAD 2026-08-05, slutsatsen var fel. Läs den som en metodlärdom om motsatsen.** Påståendet byggde på att 400 000 den 2025-06-24 gick från CZP till konto **53291070828**, antaget vara Roberts privatkonto utifrån gen-248-noteringen "53291070828 = EJ CZP (Robert)". **Den noteringen utesluter bara CZP som kontohavare, den utpekar ingen.** 53291070828 är **APDS sparkonto**, vilket avgjordes på 30 sekunder genom att stämma av samtliga fem CZP-överföringar till kontot mot APDS huvudbok 1675: alla fem matchar på datum och belopp (27 000 den 9/1, 13 000 den 16/1, 20 000 den 26/3, 13 000 den 9/5, 400 000 den 24/6). Skulden var verklig och 1675-betalningarna är äkta låneåterbetalningar.

   **Lärdomen:** ett okänt kontonummer identifieras genom att korsköra **alla** dess transaktioner mot motpartens huvudbok, inte genom att läsa en tidigare arbetsanteckning. En negativ notering ("EJ X") är inte en positiv identifiering, och att behandla den som en sådan producerade ett falskt huvudfynd som var på väg in i en advokatframställning. Kontrollen är billig, gör den först. Att banktexten saknar en lånebeteckning som andra poster bär ("LÅN APDS") är inget indicium när betalningen går till ett sparkonto som adresseras med kontonummer.

## 2026-08-03 — Slutlig FVB APDS: räkna alltid om förvaltarens egen betalningslista mot huvudboken, och KL 6:2 är reaktiv
**Projekt:** apb/czp/run (K 4429-25) · **Kategori:** swedish_corp + process · **Taggar:** KonkL 4:5, 4:10, 4:20, 6:2, 6:2a, ABL 25:18, 25:20, SFL 59, ML 16:23, förvaltarberättelse, närstående, avräkningskonto

1. **Förvaltarens sammanställningar är inte facit.** Åbergs egen xlsx listade 6 betalningar/192 000 kr till CZP inom fristen; APDS huvudbok 2440 (som boet självt skickade ut) visar 8 st/282 000 kr — två poster (75 000 den 26/9, 15 000 den 30/9, båda ref 942 = faktura 33) saknades i hans lista trots samma fakturareferens som de han fann. Kontrollsumman som avslöjade det: FVB:ns "2 700 000 kvarstod obetalt" stämmer bara om 300 000 betalats, inte 215 000. **Metod: stäm alltid av förvaltarens belopp mot (a) huvudbokens rader och (b) FVB:ns egna restbelopp innan de accepteras som förhandlingsbas.**
2. **KL 6:2 verifierad mot SFS 2026-08-03: upplysningsplikten är reaktiv** ("de upplysningar ... **som de begär**"). Bouppteckningsbekräftelsen (6:2 a, straffansvar BrB 11:1) avser bouppteckningens tillgångar/skulder/räkenskapsmaterial — inte förvaltarens analysprodukter. Rådet som gavs: rätta inte förvaltarens räknefel självmant och isolerat, ljug aldrig om frågad, och lägg fram allt via ombud som del av en samlad förlikning (en förlikning som mörkar kända belopp är angripbar via AvtL 30/33 §§ och blir boets bästa 4:5-otillbörlighetsbevis där närståendes onda tro redan presumeras).
3. **Ett avräkningskonto skär åt båda hållen.** 1675-huvudboken friade betalningarna från "underlag saknas" (kontot var tvåvägs, CZP-tillgodohavande −106k drogs ned till +1k) men gjorde dem samtidigt till *återbetalning av ägarlån till närstående inom fristen* = närmast automatisk 4:10-förlust (107k). Det starka försvaret låg i stället i 2440-posterna: intjänat VD-arvode (5 mån à 125k inkl moms = 625k utfört) översteg betalt (300k) — "bolaget betalade mindre än intjänandetakten" är den bästa ordinär-invändningen för närstående-arvoden. Spegelboken (CZP:s SIE, konto 1714/1510) visade att BÅDA bolagen klassade posterna spretigt men fullständigt = bra mot otillbörlighet, dåligt för en enhetlig betalningsberättelse.
4. **En efterkonkurs-kreditfaktura (CZP #48, 2 187 500, tre dagar efter konkursdagen) är dubbeleggad:** den styrker periodiseringen (hjälper KBR-tidpunkt + obestånd) och att borgenären aldrig krävde mer än utfört arbete, men ger samtidigt boet argumentet att ursprungsfakturan aldrig motsvarade en verklig skuld vid utställandet. Kör EN linje: förskottsfakturering av löpande arvode, betalningar = intjänat.
5. **FVB-grafik är bevismaterial mot klienten:** grafen la första kapitalbristen i januari 2024 (helt 2024 utan KBR, bekräftat av revisorsanmärkning i bilagd ÅR). Utan formell rättelse enligt ABL 25:20 (granskad KBR2 framlagd) kan en fientlig borgenär hävda kontinuerlig ansvarsperiod från 2024 — vilket kan återuppliva ett 25:18-hot (här WLBS 3,49M) som tidigare avfärdats på omfångsrekvisitet med ett antaget fönster aug–dec 2025. **Ompröva omfångsslutsatser när nya obestånds-/EK-data landar; faktisk EK-läkning ≠ formell 25:20-rättelse.**
6. **Kreditering vs deklaration är ingen valfråga.** ML 16:23/Genius Holding + SKV-handläggarens skriftliga besked (rättelse i ursprungsperioden före kreditnota) betyder att debiterad moms ska deklareras OAVSETT kreditering; kreditnotan vänder den först i senare period och kräver att skattebortfallet undanröjs (Schmeink). Sekvens som gavs: advokat → ofarlig delrättelse → finansiering/rådrum → rättelse → först därefter kreditnota + omfakturering till rätt (solvent) motpart + boets skriftliga medverkan. En rättelse som fastställer skuld i ett tomt bolag utan samtidig finansiering = undertecknat eget företrädaransvar (HFD 2018:4, ursprunglig förfallodag).
7. **Två oförenliga försvarslinjer får inte blandas:** "böckerna gäller" (skadeståndet var APDS:s → EK läkt feb 2025 → kort 25:18-fönster, men boet får 5M-fordran mot Runatyr vid kreditering) vs "avtalet gäller" (skadeståndet var AP:s → kvittningen ogiltig, men EK-läkningen rivs → 25:18 från 2024). Klienten kan bara köra den första. Kartlägg alltid vilken linje som dödar vilken exponering INNAN någon av dem framförs externt.
8. **Fristkarta i äldre-regler-bevakningsförfarande är operativ juridik:** anmärkningsfrist (här 11 aug) och förlikningssammanträde (1 sep) är de facto-deadlines för att få ombud på plats — boets återvinning kan komma som anmärkning mot närståendes bevakning i stället för stämning, och den vägen saknar frist (KL 4:20-systematiken) medan stämningsvägen dör 1 år efter konkursbeslutet.

## 2026-07-21 — Kundförlust i moms + bevakning i konkurs: passivitet är inte neutralt
**Projekt:** run/rlr (Runatyr ↔ APDS, mål K 4429-25) · **Kategori:** `swedish_tax` + `process` · **Taggar:** ML 8:16, ML 7:43-47, KonkL 9 kap., prop. 2024/25:135, närstående, kundförlust

1. **ML-lagrum (2023:200), verifierat mot två oberoende källor men INTE mot lagtext:** kundförlust / minskning av beskattningsunderlaget = **8 kap. 16 §** (motsvarar gamla 7 kap. 6 § 4 st ML 1994:200). Redovisningstidpunkt = **7 kap. 43-47 §§**. Skatteverkets och riksdagens sidor blockerar WebFetch (403 "Request Rejected") — svenskforfattningssamling.se-PDF:en eller FAR Online är alternativa vägar nästa gång. Kontrollera mot lagtext före extern åberopan.
2. **Befarad ≠ konstaterad.** Endast **konstaterad** kundförlust ger momsnedsättning; befarad är ren redovisningsreservering utan momseffekt. **Ingen kreditnota krävs** vid kundförlust (till skillnad från prisnedsättning i efterhand) — och **köparen behöver inte justera sin ingående moms**. Följd: Schmeink & Cofreth-invändningen (skattebortfall hos tomt bo) biter mycket svagare på kundförlustvägen än på krediteringsvägen. Det är ett självständigt argument för kundförlust framför kreditnota när motparten är insolvent.
3. **SKV:s eftergiftsposition är den farliga analogin vid passivitet.** Ställningstagandet 2019-12-05 (kundförluster + prisnedsättningar i efterhand) säger att en borgenär som **avstår från kvittning** i konkurs inte gjort en kundförlust utan **frivilligt avstått från betalning**. Underlåten bevakning i ett bevakningsförfarande ligger nära nog för att SKV ska kunna använda analogin. Ingen praxis hittad på underlåten bevakning specifikt — flagga som analogi, inte regel.
4. **Bevakningsförfarandets existens är ett moms-motargument.** Ett bevakningsförfarande beslutas normalt bara när utdelning till oprioriterade förväntas. Det skär rakt mot rekvisitet "sannolikt att betalning inte kommer att fås" och gör kundförlusten svårare att få igenom just i de konkurser där bevakning krävs. Dubbeleggat: samma faktum gör bevakningen värd att göra och kundförlusten svårare.
5. **Dokumentkravet vid konkurs:** SKV kräver **handling från konkursförvaltaren** som visar att borgenären inte kan förvänta sig betalt av boet, plus att fordran är **oprioriterad**. Fallande styrka: utdelningsförslag (KonkL 11 kap.) med 0 till oprioriterade > förvaltarberättelse (KonkL 7:15) > skriftligt e-postbesked. Får utdelning ändå ut ska avdraget **återföras proportionellt**. Färdig begäran-mall finns i `umbrella/aurora_punks/legal/run012_kundforlust_bevakning_2026-07-21.md` §2.4 — återanvänd den.
6. **Närstående:** SKV ställer uttryckligen **"höga krav på den bevisning som säljaren ska prestera"** vid intressegemenskap. Det är en artikulerad bevisbörderegel, inte allmän misstänksamhet. Bästa motbevisning är handlingar klienten inte kontrollerar ensam: motpartens egen bokföring, avtal signerade av utomstående, och att fordran faktiskt drivs mot boet som vilken borgenär som helst.

**NYTT KONKURSFÖRFARANDE 1 JULI 2026 (prop. 2024/25:135) — övergångsregeln är lätt att missa:**
7. Nya reglerna gäller **även konkurser beslutade före ikraftträdandet** — men har tingsrätten **före 1 juli 2026 beslutat att inleda bevakningsförfarande, tillämpas äldre bestämmelser på förfarandet**. Har frågan kommit in före 1 juli utan beslut, gäller nya reglerna. Kolla alltid **datum för beslutet om bevakningsförfarande**, inte konkursdatumet.
8. I nya ordningen: **förlikningssammanträdet avskaffas**, förvaltaren (inte tingsrätten) beslutar om och genomför bevakningsförfarandet, anmärkning får återkallas av den som gjort den. Ser man ett utsatt förlikningssammanträde i ett pågående mål är det ett tecken på att **gamla regler gäller**.
9. **Efterbevakning (gamla KonkL 9:20):** avgift **3 % av prisbasbeloppet ≈ 1 776 kr (2026)**, betalas i förskott, annars vidtar rätten ingen åtgärd. Hård bortre gräns: **innan förvaltaren upprättat utdelningsförslag** — en tidpunkt borgenären inte kontrollerar. Billig men aldrig ett planerat alternativ; den läker inte det bevismässiga intrycket av att fristen missades.

**How to apply:** När klient med närståendefordran överväger att låta en bevakningsfrist gå ut: säg GO på bevakning även när fordran är omtvistad eller klienten själv tidigare sagt att fakturan var fel. Att inte bevaka är inte passivitet utan ett aktivt val som (a) förlorar utdelningsrätten, (b) ger SKV en eftergiftsinvändning mot momsnedsättningen, och (c) — allvarligast — utgör bevisning för att fordran aldrig var kommersiellt verklig. Bevakningen är dessutom ofta den enda **nya samtida handling** klienten kan skapa till stöd för fordrans äkthet mitt under en pågående granskning.

**Positionsbyte inför samma mottagare:** när klienten tidigare sagt motsatsen till samma publik (här: förvaltare + SKV, jan 2026 "fakturan borde krediteras") — **föregrip motsägelsen i egen inlaga, dölj den aldrig**. Renaste framställningen är "positionen ändrades för att bevisningen ändrades" och den kräver att bevisningen faktiskt daterar **efter** det tidigare uttalandet (här: det signerade Samarbetsavtalet återfunnet 2026-07-18 vs uttalandet i jan 2026). Att motparten själv gräver fram motsägelsen är alltid värre. Och: **en linje, konsekvent, till alla mottagare** — argumentera aldrig samtidigt att fakturan är felaktig och att den ska bevakas till fullt belopp.

## 2026-07-21 — KORRIGERING av dagens tidigare post + två lärdomar om karaktäriseringsval
*(Runatyr/APDS, run-012)*

### Korrigering först

Posten "Kundförlust i moms + bevakning i konkurs" ovan säger att det signerade Samarbetsavtalet
**återfanns 2026-07-18** och bygger sitt råd om positionsbyte på att bevisningen daterade efter det
tidigare uttalandet. **Det är fel.** Avtalet låg bifogat klientens eget mail till revisorn
**2025-12-10**, och samma mail innehöll klientens egen formulering av linjen ("Kan Runatyr ifrågasätta
upplägget med att kvitta betalningen mot skulden och istället hävda att den inte är betald?") — två
dagar före motpartens konkurs. Framställningen "positionen ändrades för att bevisningen ändrades" är
därmed motbevisad i just detta ärende. **GO-rekommendationen på bevakning drogs tillbaka och fristen
läts löpa ut.** Lärdomen om att föregripa motsägelser står kvar; lärdomen är att **verifiera
dateringen av den påstått nya bevisningen mot klientens egen mailhistorik innan den bär en framställning.**

### Lärdom 1: testa fordringskaraktäriseringen mot MOTPARTENS obeståndsdatum

**Learning:** Att välja "fakturan är giltig men obetald" mot ett konkursbo är inte enbart ett
momsställningstagande. Det påstår att gäldenären hade en obetald skuld från fakturadatum, vilket
**flyttar gäldenärens obeståndsdatum bakåt** och på ett högre belopp. Satt klienten i den styrelsen
öppnar det ABL 25 kap. 18 § medansvar för förpliktelser under hela underlåtenhetsperioden, SFL 59:12-13
för gäldenärsbolagets skatter, och BrB 11:5 om böckerna visar en kvittning utan verkan. Här: nio
månaders fortsatt drift, klienten ensam styrelseledamot.

**Why:** Momsbeloppet var 1 Mkr och avgränsat. Obeståndsansvaret var öppet och obegränsat. Vi
optimerade först på momsfrågan och missade att den var den mindre av de två.

**How to apply:** När klienten suttit på båda sidor av transaktionen: räkna alltid igenom vad varje
karaktäriseringsalternativ gör med **motpartens** solvens vid transaktionstidpunkten, innan du
rekommenderar linje. Ställ frågan explicit: "vem satt i den styrelsen, och vad påstår vi om vad de
visste?" Kreditering (fakturan felriktad) begränsar ofta exponeringen till momsen; giltig-men-obetald
öppnar hela obeståndskedjan.

### Lärdom 2: för svag att bevaka = för svag att bära en kundförlust

**Learning:** En närståendefordran som klienten inte anser sig kunna driva i konkursen kan inte
samtidigt bära ett kundförlustavdrag. Det är samma bevisfråga — fordrans kommersiella verklighet — i
två skepnader. Klienten kan inte ha en fordran som är verklig nog att skriva av men inte verklig nog
att kräva in.

**How to apply:** Använd det som beslutsregel när klienten vacklar: kan han inte tänka sig att bevaka,
ska han inte heller planera för momsnedsättning, utan för att momsen blir kvar. Det gör valet konkret
och stänger önsketänkandet. Omvänt: håller fordran för bevakning håller den normalt också för
kundförlust, och då är bevakningen dessutom det bästa beviset (se posten ovan).

**Tags:** karaktäriseringsval, obeståndsdatum, ABL-25:18, närståendefordran, kundförlust, run-012

## 2026-07-17 — Preskription i konkurs-/ansvarsmål: materiell räckvidd ≠ talefrist, och omfångsrekvisitet slår frist (apb/czp)

**Källa:** PM preskription + CZP↔AP-struktur, `aurora_punks/drafts/lawyer_preskription_och_czp_ap_2026-07-17.md`. WLBS/APDS-komplexet.
**Kategori:** swedish_corp + insolvens + process
**Taggar:** KL 4:5, KL 4:10, KL 4:20, ABL 25:18, ABL 25:20a, ABL 29:13, ABL 17:6-7, preskription, återvinning, närstående, medansvar

**Learning (den felkälla som nästan vände hela riskbilden): "ingen bakre tidsgräns mot närstående" i KL 4:5 är MATERIELL räckvidd - den säger ingenting om hur länge talan får väckas.** Processuellt styr **KL 4:20 1 st**: återvinningstalan väcks inom **ett år från konkursbeslutet**, alternativt sex månader från det att grunden blev känd för boet. Ett tidigare memo (2026-06-09) angav bara den obegränsade bakre gränsen, vilket lästes som "ingen deadline alls" och skapade fel oro *och* fel lugn samtidigt. Rätt bild för APDS: Åbergs offensiva talan mot CZP måste väckas **senast ca 2026-12-12**. Läs alltid 4:5/4:10 tillsammans med 4:20 - annars blir svaret på "hur länge kan de driva det?" fel i båda riktningarna.

**Learning (undantaget som lever för evigt): KL 4:20 2 st - återvinning som görs gällande genom ANMÄRKNING mot bevakning eller INVÄNDNING mot krav mot boet har ingen tidsfrist.** Förvaltaren behöver alltså inte stämma för att få effekt: han kan vänta tills motpartens egen bevakning ska prövas och då kvitta bort utdelningen. Praktisk konsekvens: den som har en stor bevakning i boet (här CZP:s 3 MSEK-fordran) sitter kvar i återvinningsrisk så länge konkursen pågår, även efter att ettårsfristen stängt. Offensiv väg dör; defensiv väg gör det inte.

**Learning (kolla omfångsrekvisitet FÖRE fristen i ABL 25:18-ärenden).** 25:18 träffar **bara förpliktelser som uppkommer under ansvarsperioden** (underlåtenhet att upprätta KBR → konkurs/rättelse). En borgenär vars fordran uppkom *före* fönstret kan inte använda 25:18 alls, hur hotfullt kravbrevet än är formulerat. I WLBS/APDS-fallet: Vaerens hot om "17 samt 25 kap" mot styrelsen avsåg en fordran uppkommen före WLBS-konkursen sept 2024, dvs. långt före ansvarsfönstret aug-dec 2025 → hotet faller på omfånget, inte på fristen. Fristen (ABL 25:20 a) är dessutom en **preklusionsfrist**: tre år från förpliktelsens uppkomst, alltid minst ett år från förfallodagen; ansvaret dör definitivt och kan inte hållas vid liv med kravbrev som vanlig preskription. Medansvaret är accessoriskt - preskriberas bolagets skuld faller medansvaret med den. Kolla också vem som satt i styrelsen *under fönstret*: ledamöter registrerade efter konkursen delar inte ansvaret.

**Learning (fristkartan att återanvända):** ABL 29:1 talan för bolagets räkning = **5 år från utgången av det räkenskapsår** åtgärden vidtogs (ABL 29:13); boet får föra talan trots ansvarsfrihet (29:12); brottsgrundad talan undantagen. Borgenärs **egen** 29:1-talan saknar ABL-frist → allmän tioårspreskription (PreskL 2 §), men kräver normöverträdelse + egen skada + kausalitet (hög tröskel). ABL 17:6-7 saknar egen frist → tio år. Fristdag i KL:s mening = **dagen konkursansökan kom in** (KL 4:2), inte konkursbeslutet - hämta den ur tingsrättens akt, den flyttar 4:10-fönstret.

**Learning (process): kontrollera vad klienten redan representerat skriftligt innan du bygger hans position.** Roberts "clean slate - ingen legal historik ger AP rätt till projekten" kollapsade inte på juridiken i första hand utan på hans eget mail till revisorn 2026-05-12, med hela styrelsen i kopia, där han skrev att uppdragen ägs på AP-nivå - plus paying-agent-memot 2026-05-04 som dokumenterar motsatt struktur. Sök alltid `in:sent` + tidigare memon efter motstridiga representationer **före** du utvecklar ett argument; annars bygger du något som motparten fäller med klientens egen skrivning.

**Learning (två vinklar som inte var i briefen men bör vara standard vid närstående-fee):** (1) **Corporate opportunity / lojalitetsplikt** - att förhandla affärer i moderbolagets namn och i efterhand styra värdet till ett helägt bolag är mönstret för en 29:1-talan driven av minoriteten (29:7), oavsett hur fee:n prissätts. Framåtriktad öppet beslutad fee undviker det; retroaktiv omdirigering gör det inte. (2) **Räkna fee:ns KBR-effekt innan nivån föreslås** - i ett bolag vars kontrollbalans läks med ca 60 tkr marginal kan en närstående-fee ensam välta läkningen och återuppväcka likvidationsplikten. Beloppsspärren (ABL 17:3 1 st) medger noll utrymme vid negativt EK, och **borgenärsskyddet i 17:3 kan inte samtyckas bort ens av samtliga aktieägare** (till skillnad från jävs- och minoritetssidan, som SAS-samtycke läker).

**Tags:** wlbs, apds, czp, aurora-punks, preskription, återvinning, medansvar, ABL-25, ABL-29, ABL-17, KL-4, närstående, corporate-opportunity, KBR

## 2026-07-17 — "Konkurs för att slippa bokföringsbrott" är bakvänt: brottet sitter i böckerna, konkursen tillkallar åklagaren

**Källa:** Runatyr moms/RLR (run-012), SIE-avstämningen 2026-07-17
**Kategori:** swedish_corp + swedish_tax + insolvens
**Taggar:** correction, BrB 11:5, KonkL 7:15, KonkL 7:16, SFL 59:13, HFD 2018:4, SkBL 12, SFL 49:10, bokföringsbrott, frivillig rättelse, konkurs, moms

Klientresonemanget var: "om momsen inte rättas begår jag bokföringsbrott, alltså KBR → konkurs, hellre tar jag ~1,4M personligen än begår ett brott." Tre fel i ett:

1. **Bokföringsbrott (BrB 11:5) botas i bokföringen, inte i tingsrätten.** Rekvisitet sitter i räkenskapernas skick (huvudsakskriteriet). Rätt åtgärd är att komplettera böckerna med de utelämnade affärshändelserna + rättade deklarationer/ÅR, rådgivarlett. Varken konkurs eller privat betalning påverkar den historiska gärningen - men konkurs GARANTERAR granskning: förvaltaren måste redovisa obeståndstidpunkt/KBR-efterlevnad (KonkL 7:15) och omedelbart anmäla misstänkt BrB 11-brott till åklagare (KonkL 7:16). Solvent bolag + rättade böcker + samarbete = låg åtalsrisk; konkurs = institutionaliserad brottsanmälan.
2. **Konkurs skyddar inte mot företrädaransvar** (SFL 59:12-13; HFD 2018:4 - bedöms per ursprunglig förfallodag; "verksamma åtgärder" hjälper bara SENAST på förfallodagen). En konkursansökan ett år efter förfallodagarna är verkningslös som skydd. Det som sänker exponeringen: skatten påförs aldrig (materiell invändning), betalning vid påförande, rådrum (Prop. 2025/26:52, i kraft 2026-07-01) för framtida förfall, befrielse ("oskäligt") för upplupet, och uppsåtsmotbevisning.
3. **Beloppet var en härledning, inte en skuld.** Böckerna (lästa i SIE-original) visade momsFORDRAN + positivt EK - ingen bokförd momsskuld alls; exponeringen uppstår först genom SKV-beslut i en öppen granskning. Regel: KBR:a/konkursa/betala aldrig på härledda belopp - läs SIE-filerna först (`iconv -f CP437 -t UTF-8 fil.se`, kolla 261x-transaktioner, 1650/2650-saldon, EK-konton 208x-209x).

**Frivillig rättelse-nyansen (SkBL 12 §, SFL 49:10):** ett riktat föreläggande släcker frivilligheten för de FÖRELAGDA perioderna - men inte automatiskt för angränsande, ännu inte förelagda perioder (här: 2024 medan granskningen avsåg 2025). Det fönstret är memots mest tidskritiska fynd och stänger när granskningen vidgas → agera i dagar, inte veckor, och låt advokat dra frivillighetsgränsen.

**"Koncernen nettar till noll" är ingen momsinvändning** (moms är subjekt- och transaktionsbaserad; momsgrupp bara finans/försäkring) - men den är ett bra billighets-/befrielse- och uppsåtsargument. Sortera argumenten i rätt låda: materiellt vs befrielse/mens rea. Klientens öppna, frågande SKV-korrespondens ("har vi tänkt rätt?") är guld mot uppsåt - lås in den vinsten genom att stoppa fortsatt fritext-mailande till handläggaren när läget blivit skarpt (allt är processmaterial).

**How to apply:** När klient föreslår konkurs som "det ansvarsfulla" svaret på en redovisnings-/skattemiss: (a) skilj de tre spåren - böckernas skick (BrB 11:5), skattebeslutet (SFL/ML), personansvaret (SFL 59) - och visa att konkurs inte hjälper i något av dem när förfallodagarna passerat; (b) verifiera att den fruktade skulden ens finns bokförd/beslutad; (c) kolla om frivillig rättelse ännu lever för icke-förelagda perioder. Jäv-check: en förvaltare i ett närstående bo (här Carler/APDS) kan aldrig vara, eller rekommendera utan konfliktkontroll, klientens obeståndsombud.

---

## 2026-07-15 — Ark Island co-publishing draft: two competing structures on file (aurora_punks)
**Category:** contract_review / swedish_ip · **Tags:** Ark Island, Aurora Punks, co-publishing, ToA, Knives & Gutters, related-party ABL 8:23

Drafted a **Co-Publishing Agreement AP AB ↔ Ark Island** for Tears of Adria + Knives & Gutters (`aurora_punks/drafts/ArkIsland_CoPublishing_Agreement_DRAFT_2026-07-13.md` + `.docx`). Key learnings:

1. **Ark Island owns the IP on both titles; AP is publishing help only** (`ap_ip_ownership_canonical.md` §B). Robert holds ~5% personal equity in Ark Island → related-party; disclose per **ABL 8:23 (jäv)** awareness, but parties contract at arm's length as AP AB (559256-9718) and Ark Island. Contracting entity is AP AB, NOT bankrupt APDS.
2. **Two structures exist and must not be silently merged.** (a) Robert's newer explicit steer (2026-07-07): a **sub-10% publishing rev-share** for publishing services. (b) A real existing agreement on file — **`CoDev_AP_ArkIsland`** (GDrive, RAG source=gdrive) — runs **AP 60% of revenue on all platforms until a recoupable amount ×2 is repaid**, plus a monthly service fee with a 40%-of-service-fee signature tranche (160k SEK example) and billables deferred to recoup at launch. That's a co-dev+co-pub shape and only fits if AP is *funding/building*. Draft defaults to (a), flags (b) as the alternative in the rev-share section, and adds an "entire agreement" TO CONFIRM asking whether the new deal supersedes or sits alongside CoDev_AP_ArkIsland (they can't both bind the same titles).
3. **Insolvency-termination caveat:** AP-side immediate termination on Ark Island konkurs/rekonstruktion/likvidation is a required term per the tracker, BUT ipso-facto/insolvency-termination clauses have limited enforceability under Swedish insolvency law (LUS/rekonstruktionslagen) — always flag for the real lawyer rather than presenting as watertight.
4. **Assignability to an AP "Designee"** (affiliate/successor) without counterparty consent is a required term (supports AP group restructuring) — mirrors the CoDev agreement.
5. **Scope reality per title:** K&G = Campaigns + Community (festival/showcase pipeline, Steam events); ToA = post-release GTM relaunch, self-published with Robert on Steamworks. Publishing-services deal (marketing-only shape, dev keeps IP + high share) is the correct legal frame, per `game_publishing_deals` skill.

**Process:** `czp_legal/templates/{MNDA,Subcontracts}/` and `assistant/legal_templates/` are currently EMPTY — no renderable master to instantiate from; drafted from clause patterns + `game_publishing_deals` skill. `md-to-docx.sh` pipeline works for styling the draft.

## 2026-07-13 — EUIPO SME Fund Voucher 2 (varumärken) tar slut mitt i året — voucher-först-sekvensen är absolut

**Källa:** Aurora Punks EU-varumärkesplan (apb-039)
**Kategori:** swedish_ip + process
**Taggar:** EUTM, EUIPO, SME Fund, varumärke, Nice-klasser, art 7 EUTMR, art 8 EUTMR, Fast Track, Madridprotokollet

Planeringsläror för att EU-varumärkesskydda ett ord-/företagsmärke för en svensk spel-SME:

1. **EUIPO SME Fund Voucher 2 (varumärken+design) förbrukas ofta MITT i året.** 2026 löpte fonden 2 feb–4 dec men Voucher 2 var slut/tillfälligt stängd redan sommaren. **Voucher-först-sekvensen är ovillkorlig:** ansök om vouchern → få beslut → betala EUTM-avgiften EFTERÅT. Betalning före beslut = förlorad återbetalning. Oanvända medel kan omfördela/återöppna Voucher 2 senare på året — bevaka SME Fund-sidan. Konsekvens: gör klareringssökning + klassval NU (gratis), men vänta med att betala tills vouchern är beviljad, om inte tidpunkten är kritisk.
2. **Voucher 2 = 75 % återbetalning av EU-avgifter** (ansökan + tilläggsklass + gransknings-/registrerings-/publiceringsavgift), 75 % även nationellt/regionalt (PRV), **50 % för icke-EU-designeringar** (Madrid UK/US). **Tak 1 000 EUR per SME.** Täcker BARA myndighetsavgifter, inte ombudsarvode.
3. **EUIPO-avgifter 2026 (online):** grund 850 EUR (1 klass), +50 EUR för 2:a klassen, +150 EUR/klass från 3:e. Ordmärke för spel/publishing = klass **9 (nedladdningsbar spelmjukvara) + 41 (underhållning/spelutgivning)**; klass 42 (SaaS/mjukvaruutveckling) bara om co-dev-tjänster marknadsförs under märket. Netto för 9+41 med bidrag ~225 EUR.
4. **Registrerbarhet:** ett arbiträrt tvåordsmärke (typ "Aurora Punks") för spel/mjukvara passerar art. 7 EUTMR (inga absoluta hinder). Reell risk = relativa hinder (art. 8, äldre liknande märken) — **måste köras i EUIPO eSearch plus + TMview**. OBS: EUIPO-domänen (euipo.europa.eu) och eSearch/TMview **blockerar maskinell WebFetch (HTTP 403)** — klareringssökningen kan inte automatiseras härifrån, måste köras manuellt/av ombud. Verifiera SME Fund-siffror via sekundära IP-byråkällor.
5. **Process:** EU-domicilierad sökande behöver **inget ombud** inför EUIPO; DIY-ingivande OK för rent ordmärke med HDB-termer (Fast Track). **UK-ombud kan efter Brexit INTE företräda EU-sökande inför EUIPO.** Oppositionsfönster = **3 mån** från publicering (fast, kan ej kortas). Registrering ~4–6 mån vid ren ansökan.
6. **Geografi:** EUTM täcker Sverige — nationell PRV-ansökan redundant. UK kräver **separat UKIPO-filing** post-Brexit. Effektivast för UK+US: använd EUTM som bas för **internationell registrering via Madridprotokollet** och designera. SME Fund täcker 50 % av icke-EU-designeringsavgifterna.

**Faktakontroll-lärdom:** US-registreringsnummer förväxlas lätt med EUTM i tickets. Här var "EUTM cert 7647268 klass 9" i själva verket en **US-registrering 7647268 i klass 9+41** (Sheridans-mail). Verifiera märkes-/registreringsnummer mot mailhistoriken innan man bygger vidare.

## 2026-07-13 — Sverige har INGEN allmän plikt att ansöka om konkurs vid obestånd — vanlig klientmissuppfattning

**Källa:** Runatyr moms/RLR (run-012)
**Kategori:** swedish_corp
**Taggar:** correction, obestånd, konkurs, ABL 25:13-18, kontrollbalansräkning, SFL 59, BrB 11 kap, verksamma åtgärder

Robert (och många företagsledare) tror att en styrelseledamot har en *plikt att ansöka om konkurs* så snart bolaget är på obestånd. **Fel.** Sverige har ingen "duty to file". De faktiska plikterna är tre, och ingen är att springa till tingsrätten:

1. **ABL 25:13-18 kontrollbalansräkning** — utlöses av *kapitalbrist* (EK < halva aktiekapitalet), inte obestånd som sådant. Vid trigger: upprätta KBR *genast*, revisorsgranskning, första kontrollstämma (25:15), rådrum, andra kontrollstämma (25:16), annars likvidationsansökan (25:17). Försummelse -> personligt medansvar för förpliktelser under försummelsetiden (25:18). En bokförd skuld som slår EK under halva aktiekapitalet utlöser plikten även om kassan för stunden räcker.
2. **Borgenärsskyddet vid insolvens** — får inte ådra nya skulder som inte kan betalas, inte gynna enskild borgenär (BrB 11 kap. oredlighet/otillbörlighet mot borgenärer; återvinning KonkL 4).
3. **SFL 59 företrädaransvar för skatt/moms** — HÄR, och bara här, är konkurs-/rekonstruktionsansökan ("verksamma åtgärder senast på förfallodagen") ett sätt att *kapa* ansvaret. Men nya rådrums-regeln (Prop. 2025/26:52, i kraft 1 juli 2026) ger ett renare alternativ än att rusa till konkurs.

**How to apply:** När klient säger "jag måste ansöka om konkurs för bolaget är insolvent" — rätta genast. Fråga: (a) är kapitalbristtröskeln (ABL 25:13) passerad? Då är KBR-plikten den reella, sannolikt redan aktiva. (b) Vilken skuld gör bolaget insolvent? Om det är EN skuld (här: oredovisad moms), attackera den vid källan (kreditering om leveransen kan reverseras, eller ägartillskott/lån som finansierar bort den) i stället för att konkursa. Konkurs raderar inte upplupet företrädaransvar (bedöms per förfallodagen) och öppnar närstående-återvinning — ofta klientens värsta utgång.

## 2026-07-13 — Kreditfaktura kan återföra utgående moms VID KÄLLAN — men bara om leveransen faktiskt reverseras, inte som skatteanpassning

**Källa:** Runatyr moms/RLR (run-012) — Runatyr fakturerade APDEV 4M+moms för RLR/Elric mar 2025, "betalt" via kvittning, moms ej redovisad
**Kategori:** swedish_tax
**Taggar:** moms, kreditfaktura, kreditnota, ML nedsättning, verksamhetsövergång, företrädaransvar, kvittning, konkursbo

När en oredovisad utgående moms sitter på en faktura vars underliggande transaktion är ifrågasatt, är en **kreditfaktura** potentiellt den renaste fixen: den återför den utgående momsen vid källan (ML medger nedsättning när underlaget för omsättningen bortfaller), vilket kan lösa både momsskulden OCH företrädaransvaret utan konkurs eller rådrum.

**Men två motstående linjer måste vägas, och krediteringen får INTE utfärdas reflexmässigt:**
- **För:** inget skriftligt överlåtelseavtal fullbordades (faktura ≠ överlåtelse); kan vara verksamhetsövergång; transaktionen fullbordades aldrig.
- **Mot:** om tillgångarna *levererades och monetiserades* (här: Elric-källkod i en publicerad mod, RLR exploaterat) kan Skatteverket hävda att en leverans *skedde* och att momsen står kvar. En kreditering ~1 år senare, av en faktura till ett numera konkursat närståendebolag, med effekten att momsskulden försvinner precis när företrädaransvar hotar, har dålig optik och kan bli bevis för uppsåt.

**Estate-fälla:** om fakturan "betalades" genom kvittning mot en fordran i ett bolag som sedan gått i konkurs, river krediteringen kvittningen och återuppväcker den kvittade fordran (här: APDEV:s 5M skadeståndsfordran på Runatyr) OCH tar bort en tillgång ur konkursboet (den immateriella tillgången). Krediteringen måste därför samordnas med förvaltaren + obeståndsadvokat, inte göras isolerat av bokföraren.

**How to apply:** Föreslå kreditfaktura som förstahandsprövning när oredovisad utgående moms sitter på en icke-fullbordad transaktion — men skicka den ALLTID via både momskonsult (mekanik/period) och obeståndsadvokat (estate-effekt) före utfärdande. Verifiera att leveransen faktiskt kan sägas inte ha skett; om assets levererats och monetiserats, förvänta motstånd från Skatteverket.

## 2026-07-13 — Läs den faktiska bokföringskedjan innan du lokaliserar en fordran — papper (avtal) och böcker kan peka åt olika håll

**Källa:** Runatyr/APDS 5M (run-012) — 07-07-memot antog AP<->Runatyr, böckerna sa APDEV<->Runatyr
**Kategori:** process + swedish_tax
**Taggar:** correction, intercompany, bevakning, konkursbo, fordran-lokalisering, due-diligence

07-07-memot antog att AP höll en 5M-fordran på Runatyr (per tillägget 2025-03-28 §4). Den faktiska Sifferråds-bokföringen (gmail-kedjan mar-maj 2025) visade något annat: skadeståndet bokfördes i **APDEV** ("lagt mottaget skadestånd i APDEV 5Mkr med fordran på Runatyr"), RLR/Elric som **APDS immateriell tillgång**, och APDEV<->Runatyr-fordringarna kvittades till netto noll. Konsekvens: AP hade ingen ren bevakningsbar fordran mot APDS-boet (5M var en APDEV-*tillgång*, inte en skuld *till* AP), och RLR-titeln satt per böckerna i konkursboet — inte i den solventa Runatyr man planerade sälja från.

**How to apply:** Vid varje fordrans-/tillgångslokalisering i en koncern med konkursinslag — läs den faktiska verifikationskedjan (mail till/från bokföringskonsulten, huvudboken), inte bara avtalet. Avtalet säger vad parterna avsåg; böckerna säger var posten faktiskt hamnade. I konkurs är det böckerna förvaltaren utgår från. Skillnaden avgör vem som ska bevaka vad och varifrån en tillgång kan säljas.

## 2026-07-13 — Att kreditera fakturamoms mot ett tomt konkursbo kan FLYTTA skulden från bolag till dig personligen (Genius Holding + Schmeink & Cofreth)

**Källa:** Runatyr/APDS 4M-faktura (run-012), Fable-advokatsimulering
**Kategori:** swedish_tax
**Taggar:** correction, felaktigt debiterad moms, kreditnota, Genius Holding C-342/87, Schmeink & Cofreth C-454/98, Stadeco C-566/07, företrädaransvar, konkursbo, skattebortfall, ML 2023:200 16:23

Den intuitiva fixen "kreditera den felaktiga fakturan så försvinner momsen" har en giftig baksida när motparten är ett tomt konkursbo som redan dragit den ingående momsen:

1. **Felaktigt debiterad moms är betalningsskyldig tills en GILTIG kreditnota utfärdats** (ML 2023:200 16 kap. 23 §, tidigare ML 1994:200 1:1 3 st / 1:2e; EU: Genius Holding C-342/87). Att bara vilja kreditera räcker inte — momsen sitter kvar hos utställaren till dess.
2. **Rättelse/återföring medges bara om utställaren "i god tid undanröjt risken för skattebortfall"** (Schmeink & Cofreth C-454/98; Stadeco C-566/07). Om mottagaren redan dragit den ingående momsen och är i konkurs med tomt bo är den risken inte undanröjd — den är realiserad. Skatteverket kan då VÄGRA återföring hos säljaren tills statens belopp säkrats på köparsidan.
3. **Den giftiga baksidan:** krediteringen tvingar konkursboet att återföra den ingående momsen -> SKV får en fordran i det tomma boet -> utan medel i boet driver SKV beloppet som **företrädaransvar (SFL 59:12-13) mot boets företrädare**. Är klienten företrädare för BÅDE säljar- och köparbolaget (som Robert för Runatyr och APDS) byter en oskickligt genomförd kreditering en *bolagsskuld* i säljarbolaget mot ett *personligt* krav via köparbolaget.

**How to apply:** Innan du föreslår kreditering av fakturamoms — kolla (a) drog mottagaren den ingående momsen, (b) är mottagaren solvent nog att återföra den. Är svaret drog+insolvent, utfärda ALDRIG kreditnotan innan en obeståndsadvokat kört skattebortfalls- och massafordringsanalysen och samordnat redovisningen med förvaltaren. Rätt sekvens: pinna perioder/belopp -> skattebortfallsanalys -> samordna med bo -> sedan ev. kreditnota. Fel sekvens = personligt ansvar.

## 2026-07-13 — Ingen work-for-hire: "vi betalade och publicerade" ger aldrig titel; att äga bolaget ger inte heller upphovsrätten

**Källa:** RLR-äganderätt (run-012), Fable-simulering + evidence-dossier
**Kategori:** swedish_ip
**Taggar:** URL 1, URL 27, URL 40a, URL 6, work-for-hire, fragmenterad äganderätt, confirmatory assignment, avtalsbundenhet

Klientens intuition "AP betalade allt, publicerade under sitt namn, anställde alla kreatörer, alltså äger AP IP:t" håller inte. Två fel:
1. **Upphovsrätt uppstår hos den fysiska skaparen (URL 1 §) och flyttar bara genom uttrycklig överlåtelse (URL 27 §)** — inte genom betalning, publicering eller bokföring. Enda automatiska övergången är **datorprogram i anställning (URL 40 a §)** — gäller bara koden, inte grafik/berättelse/design/musik.
2. **Att äga bolaget flyttar inte skaparens upphovsrätt in i bolaget.** "Runatyr äger via ägaren Yasin" är ingen rättsgrund. Bolaget håller bara det som förvärvats via anställningsklausul eller avtal.

Resultatet när inga signerade överlåtelser finns (bara ett osignerat avtal + muntliga påståenden) = **fragmenterad äganderätt** över de olika bidragen (kod hos ett bolag via 40a, koncept hos ett annat om anställning bevisas, externa kreatörers bidrag löst hängande), plus **ideell rätt hos varje individ** oavsett (URL 3 § 3 st, kan aldrig överlåtas blankt). Enda rationella slutet är förlikning + **confirmatory assignments** (retroaktiva bekräftelseavtal, giltiga och standardverktyg för trasiga kedjor) — vilket kräver att nyckelskaparen (här Yasin) görs upp med FÖRST.

**Extra fälla:** en klient som skrivit flera oförenliga äganderättsversioner (signerat avtal säger ett, mail till en part säger ett annat, inlaga till förvaltare ett tredje) förstör sin egen trovärdighet i äganderättsfrågan — motpartens första bilaga i varje process. Rätta INTE detta genom att välja den mest aggressiva versionen; välj den som (a) stämmer med signerade urkunder och (b) inte öppnar onödiga fronter (här: "överlåtelsen fullbordades aldrig" > "Runatyr ägde aldrig").

**How to apply:** Vid IP-äganderättsfrågor i studio-/koncernmiljö — börja med kedjeanalysen per namngiven skapare (vem, vilket bolag, vilken klausul, vilket datum), inte med bolagets balansräkning. Räkna med att titeln är fragmenterad tills motsatsen bevisas, och att confirmatory assignments (inkl. uppgörelse med den kvarvarande delägaren/skaparen) är vägen till ren titel.

## 2026-07-10 — Konkurs freeze-scope for a Drive migration: presume estate property, name the right förvaltare, and never touch during a live bevakning

**Källa:** db-256 AP/CZP/Runatyr Drive-omstrukturering — freeze-scope legal-memo (`umbrella/aurora_punks/legal/freeze_scope_legal_memo_2026-07-10.md`)
**Kategori:** swedish_corp + gdpr
**Taggar:** konkurs, KL 3:1, KL 7 kap, boets egendom, rådighet, bokföringslagen 7:2, GDPR art 5/6/17, de_facto_controller, APDS, WLBS, förvaltare, bevakningsförfarande

When a parent company wants to "tidy up" Google Drive and part of the corpus belongs to bankrupt subsidiaries, the whole exercise is a rådighets-question, not an IT-question.

1. **Parent owns the shares, not the records.** At konkurs the debtor loses rådighet over estate property (`KL 3:1`), the estate is run by the förvaltare (`KL 7 kap.`), and the parent (former 100% owner) has no claim on the sub's files/data/IP/räkenskaper. Presume everything the sub generated is boets egendom until the förvaltare says otherwise.
2. **Digital moves = förfogande.** Moving/renaming/re-sharing/deleting estate files counts as disposing of estate property. "Just reorganizing in Drive" is not neutral — it can alter räkenskapsmaterial and read as a related-party creditor interfering with the estate.
3. **An empty labelled shell is fine; estate content is not.** A parent can create a Drive unit named after the bankrupt sub and hold its OWN material (own board minutes, own contract copies, own creditor-claim prep) there. It must not move estate content in. This reconciles "sub is its own unit in the structure" with "sub's estate content is frozen."
4. **deletedUsersData is GDPR, not archiving.** Default = delete, not migrate (storage limitation `art. 5.1 e`, purpose spent `art. 17.1 a`, no lawful basis for a leftover copy). Only the bokföring-linked subset is retained (`art. 6.1 c` + `art. 17.3 b` overriding erasure, via `BFL 7 kap. 2 §` 7-year rule). The sharp risk: when the sub is dissolved it can no longer be controller, so a parent holding the copy risks becoming **de facto personuppgiftsansvarig** for orphaned data — copying it into a nicer structure is exactly what triggers that.
5. **Name the right förvaltare, per entity.** AP's two bankrupt subs have DIFFERENT trustees: **APDS** (559320-7466, K 4429-25 Umeå TR) = Advokat Nils Åberg, Advokatfirman Carler; **WLBS** (559217-4196, K 16834-24 Sthlm TR) = Advokat Petter Vaeren, 7wise (Rebecca Näslund). Don't send an APDS question to the WLBS trustee.
6. **A live bevakning freezes the hands hardest.** APDS was in an active claims-verification with an absolute bevakningsfrist (21 July 2026). Touching APDS records mid-bevakning, while AP/CZP are themselves related-party creditors, is pure downside. Rule: during an active konkurs process, don't reorganize the debtor's records at all.

**Verdict shape for a 6-item freeze set:** 0 clean MAY MIGRATE without a check, 3 FREEZE/NEEDS TRUSTEE (trustee-hardware, APDS estate, WLBS estate), 1 MUST DELETE with a preserve-carve-out (deletedUsersData), 2 NEEDS CONTENT TRIAGE (a "Konkurs" working folder + generic "ARCHIVE"). The go/no-go box is ticked by the meaning "nothing in the freeze set migrates this run; empty shells may be built."

**How to apply:** For any migration/cleanup that brushes a bankrupt group entity, produce a per-item FREEZE / MAY MIGRATE / MUST PRESERVE / MUST DELETE / NEEDS TRUSTEE table, presume estate property, split GDPR data from bokföring data, map each entity to its own förvaltare, and hard-stop on anything with a live konkurs deadline. Advisory only — FREEZE/NEEDS TRUSTEE items need the förvaltare's written no-objection before anything moves; sammanflätat parent+estate material goes to an independent obeståndsadvokat (not the estate's own trustee — conflict).

## 2026-07-10 — Bevakning i konkurs går till TINGSRÄTTEN, inte förvaltaren; och en närstående borgenär som är återvinningsmål ska inte bevaka utan advokat

**Källa:** APDS-konkursen (K 4429-25, Umeå TR), bevakning-action-brief `umbrella/aurora_punks/legal/apds_bevakning_2026-07-10.md` (rlr-011)
**Kategori:** swedish_corp
**Taggar:** konkurs, bevakning, bevakningsförfarande, KL 9 kap, KL 9:5, återvinning KL 4:5, kvittningsförbud KL 5:15, regressfordran, borgen, närstående, förmånsrätt, FRL 18, APDS

1. **Rätt mottagare för bevakning = rätten, inte konkursförvaltaren.** I ett bevakningsförfarande (`KL 9 kap.`) lämnas bevakningsinlagan skriftligen till **tingsrätten**, inte till förvaltaren. Robert gjorde precis det vanliga felet - mejlade Carler (boets ombud) och ville "anmäla fordran" - och blev hänvisad vidare: både förvaltaren och handläggaren svarade "till tingsrätten, med angivna belopp, styrkt med underlag". Detta kostade tid som en frist inte alltid har. När en klient säger "jag har anmält min fordran till förvaltaren" - verifiera att det gått till **rätten**; annars är fordran inte bevakad.
2. **Bevakningsinlagans innehåll (`KL 9 kap.`, innehållet ca 9:5):** belopp (+ ränteyrkande), grund, yrkad förmånsrätt, och styrkande underlag bifogat; praxis två exemplar (rätt + förvaltare). Oprioriterade fordringar: ange uttryckligen "ingen förmånsrätt, oprioriterad" (`FRL (1970:979) 18 §`). Följ alltid domstolens eget utskick/kungörelse för exakt formkrav.
3. **Efterbevakning finns men kostar.** Missad bevakningsfrist är inte absolut fatal - efterbevakning är möjlig fram till utdelningsförslag, men den som efterbevakar står normalt för den extra handläggningskostnaden. Behandla fristen som skarp ändå.
4. **Infriad personlig borgen -> regressfordran = ren oprioriterad konkursfordran.** Bevakas mot boet (`9 § skuldebrevslagen` + regressregler). Nyanser: (a) ej fullt infriad kredit bevakas som **villkorad** regressfordran; (b) undvik **dubbelbevakning** - i den mån borgensmannen betalat träder han in i kreditgivarens ställe (subrogation), så samma kapital ska inte bevakas två gånger; (c) kolla att alla krediter är med - i APDS föll den ena borgen (CapitalBox) ur bouppteckningen och måste bevakas explicit.
5. **"Återvinningsbeloppet" är inte borgenärens fordran - det skär åt andra hållet.** APDS 857k till CZP under obeståndsperioden = **återvinningsexponering mot CZP** (`KL 4:5`), inte en CZP-fordran. CZP:s faktiska fordran mot boet är den obetalda konsultfakturan. En närstående borgenär som samtidigt är återvinningsmål ska bevaka (annars förloras fordran genom passivitet) men **belopp + framställning styrs av obeståndsadvokat**: återvunnet belopp ger en motsvarande fordran (`KL 4:15`), men kvittning är förbjuden för närstående/obeståndsperioduppkomna mellanhavanden (`KL 5 kap. 15-16 §`), och en närståendefordran möts sannolikt av anmärkning.
6. **Jäv/flera stolar:** en person kan samtidigt vara gäldenärsbolagets ställföreträdare (har intygat bouppteckning under straffansvar), privat borgenär OCH ägare av ett borgenärs-/återvinningsbolag. Bevakning är tillåten men gäldenärskanalen får inte blandas med borgenärsbevakningen; koppla in oberoende obeståndsadvokat (inte boets förvaltare - jäv).

**How to apply:** När en klient har fordringar i en närståendes/dotterbolags konkurs: (1) verifiera om bevakning faktiskt gått till rätten, inte bara till förvaltaren; (2) separera rena fordringar (privat borgen -> bevaka direkt, hinner klienten själv) från entanglade närståendefordringar (advokatfråga pga återvinning/kvittning/anmärkning); (3) skriv skelett-bevakningsinlaga med belopp+grund+förmånsrätt+underlag och håll den till frist; (4) korrigera aktivt om klienten tror att ett återvinningsbelopp är "hans fordran".

## 2026-07-10 — Pin a related-party konkursfordran from the accountant's latest reskontra, not the stale nominal invoice; bevakning is independent of återvinning

**Källa:** APDS-konkursen (K 4429-25), CZP bevakningsinlaga finalisering (rlr-011)
**Kategori:** swedish_corp + swedish_tax
**Taggar:** konkurs, bevakning, kreditfaktura, kundreskontra, moms kundförlust, KL 4:5, KL 4:15, närstående, related_party

1. **The nominal invoice figure is almost always wrong by filing time.** CZP's claim looked like 2 700 000 kr (3 MSEK invoice minus 300k paid, per the 30 Oct 2025 reskontra). But two things moved it: (a) a **kreditfaktura** of 2 375 000 kr was issued when the VD engagement ended 31 Oct 2025 (only 5 months June-Oct were actually performed = 625 000 kr inkl moms), and (b) the accountant's later reskontra (Henrik/Sifferrådet, 26 Feb 2026) booked the net CZP kundfordran on APDS at **ca 500 000 kr**. The defensible bevakad belopp is the accountant's most recent reskontra total, not the stale nominal. Always chase the latest reskontra statement (often buried in a personal-account mail thread with the bookkeeper) before setting the amount, and account for any credit note.
2. **Do not over-bevaka a related-party claim.** A närståendefordran is scrutinised and an over-claim draws an anmärkning. Dropping from 2,7M to ~500k (reflecting the kreditering) is the correct conservative move, not a weakness.
3. **Bevakning and återvinning are separate processes - don't gate one on the other.** A related-party creditor that is also a KL 4:5 återvinningsmål should still bevaka its claim now (missing the frist forfeits utdelning). The återvinning is adjudicated separately/later; if a payment is clawed back it restores an equivalent claim (KL 4:15). Kvittningsförbud for närstående/obeståndsperiod mellanhavanden (KL 5:15-16) is context for the återvinning track, not a reason to hold the bevakning.
4. **Moms on the claim:** bevaka the gross amount inkl moms. The creditor cannot reclaim the moms (kundförlust) until the fordran is **konstaterad** in the konkurs - so bevaka-ing is itself the step that eventually unlocks the moms recovery. (Henrik, årsmoms-tråden.)

**How to apply:** For a related-party consulting/IC claim into a group entity's konkurs: (1) pull the bookkeeper's latest kundreskontra for the exact net figure, not the invoice nominal; (2) check for credit notes that reduced the invoice; (3) bevaka the gross incl. moms at that net figure; (4) file independently of any parallel återvinning; (5) keep the underlying work-substantiation ready for the anmärkning/förlikning stage.

## 2026-07-10 — Inlagor to a Swedish tingsrätt can be filed by emailed signed PDF; the binding "how" is in the court's beslut PDF (attachment), not the cover email

**Källa:** APDS-konkursen (K 4429-25, Umeå TR), bevakning filing-method verification (rlr-011)
**Kategori:** swedish_corp + process
**Taggar:** konkurs, bevakning, ingivning, e-post, tingsrätt, gmail-attachments, KL 9 kap, in_duplo

1. **Email is fine.** A signed, scanned PDF emailed to the court's official avdelnings-address (here `umea.tingsratt.allmanna@dom.se`) satisfies filing of an inlaga. Sveriges Domstolar accepts handlingar by email; a wet-ink paper original is generally not required to follow for a bevakning. Confirm receipt with one phone call to the kansli - that closes the form question.
2. **KL 9 kap "in duplo" is handled internally.** Historic practice is bevakning in two copies (one for the court, one for the förvaltare). When you email one PDF, the court prints/forwards the förvaltare copy itself - the sender does not have to post two paper copies. Don't let the "två exemplar" wording scare a client into posting paper.
3. **The binding filing instruction is in the court's BESLUT/utskick PDF, which the cover email does not quote.** The Sveriges Domstolar cover email is boilerplate ("bifogat finns viktig information, läs dokumenten"). The actual beslut (here Aktbilaga 19, 2026-06-16: bevakningsförfarande ska äga rum, bevakning senast 21 juli, anmärkning 11 aug, förlikning 1 sep, bevakningshandlingar hålls på kansliet) is in the attached PDF. `mcp__gmail__gmail_thread` returns text body only - pull the attachment with `node assistant/gmail-attachments.js list/download <msgId>` then read it via the pdf-parse PDFParse path. The beslut here set the frist but did NOT mandate paper or a copy count - so email is clean.
4. **Side-benefit:** a court beslut PDF also carries the parties' registered addresses (personnummer/folkbokförd adress of the ställföreträdare, gäldenärens säte) - useful for filling borgenär/party fields you otherwise lack.

**How to apply:** For any "how do I file X with the tingsrätt" question, extract and read the court's own beslut/kallelse PDF first (via gmail-attachments.js), quote it, and default the recommendation to emailed signed PDF + confirming phone call unless the beslut says otherwise.

---

## 2026-07-08 — Bolagsverket "anmäl styrelse"-föreläggande mot bolag i konkurs = ignorera, vidarebefordra till förvaltaren

**Källa:** WLBS AB (559217-4196, AP-helägt, konkurs sept 2024, förvaltare 7wise / Petter Vaeren + Rebecca Näslund)
**Kategori:** swedish_corp
**Taggar:** konkurs, tvångslikvidation, ABL 25:11, ABL 25:50, ABL 8:3, ABL 25:18, behörig styrelse, Bolagsverket, upplöst

Robert fick ett automatiskt Bolagsverket-brev: "saknar behörig styrelse", anmäl ny styrelse senast visst datum annars föreläggande om likvidation + 3 900 kr särskild avgift. Bolaget var redan i konkurs. Rätt svar: **inget att åtgärda.**

- Konkurs och tvångslikvidation är ömsesidigt uteslutande. 25:11-processen gäller bolag i drift, inte konkursbo.
- Bolag i konkurs som avslutas **utan överskott** upplöses automatiskt vid konkursens slut, utan likvidation (`ABL 25:50` motsatsvis). Likvidation efter konkurs bara vid **överskott**.
- Särskild avgift 3 900 kr påförs bolaget = oprioriterad fordran mot tomt bo, ingen personlig kostnad. Föreläggandet triggar inget personligt betalningsansvar (det hänger på kapitalbrist, `ABL 25:18`, inte styrelseregistrering).
- Trigger för "saknar behörig styrelse": en av två ledamöter avgången → ensam ledamot utan suppleant = inte behörig enligt `ABL 8:3`.

**How to apply:** När klienten får ett Bolagsverket-registerbrev (styrelse, revisor, delgivningsmottagare, tvångslikvidation) för ett bolag som redan är i konkurs — verifiera konkursstatusen (RAG "gmail" + gdrive på orgnr), bekräfta att brevet är automatiskt och rekommendera enda åtgärden: vidarebefordra till konkursförvaltaren, registrera inget, betala inget. Enda undantaget som ändrar bilden: förvaltaren räknar med att konkursen avslutas med överskott (då blir 25:50 direkt tillämplig och domstol förordnar likvidator). Wiki uppdaterad: [[sv_corp_law]].

## 2026-07-07 — "Agreement to sell IP later on terms to be agreed" is a receivable, not a conveyance — verify title before valuing a catalog

**Källa:** Erik Reynolds / Afrime into Aurora Punks — RLR ownership analysis (`aurora_punks/drafts/erik_afrime_lawyer_analysis.md`)
**Kategori:** swedish_ip + swedish_corp + contract_review
**Taggar:** RLR, Runatyr, apport, konvertering, chain_of_title, apportemission, due_diligence, IP_transfer

The AP data room + canonical IP doc asserted RLR was "possibly already partly in AP." The signed documents say the opposite. The 2023-06-29 Runatyr↔AP Samarbetsavtal §1.1 states **Runatyr owns the RLR IP**; AP only ever intended to buy a majority of Runatyr's *shares* (never did). The 2025-03-28 tillägg §4.1-4.3 converts AP's 5M SEK compensation claim into an **interest-free loan** whose repayment is "**genom försäljning av IP:n … från Runatyr AB till Aurora Punks AB enligt separata överenskomna villkor**" — an agreement to sell in future on terms to be agreed. That is an **unperfected obligation, not a transfer.** RLR is legally in Runatyr; AP holds a receivable.

**How to apply:** When a client says an asset is "in" a company or "basically ours," find the **conveyance instrument** (assignment/överlåtelseavtal, executed, with consideration), not a background agreement, MoU, or "agreement to agree." A clause that says "repayment will occur *through a future sale* on *separately agreed terms*" is a promise to transact, not a transfer — the asset is still with the counterparty and the client holds a contract claim. This is decisive before any apportemission (the revisor won't certify apport of an asset the contributor doesn't own) or before presenting a catalog to an investor whose DD will pull the chain of title. Restated the swedish_ip principle: intra-group IP ownership must be **documented, not asserted** (already logged 2026-05-03) — here it wasn't even asserted correctly.

## 2026-07-07 — New SFL företrädaransvar regime (rådrum + oskälighet) in force 2026-07-01 — Prop. 2025/26:52

**Källa:** Erik/Afrime analysis — Runatyr unpaid VAT / företrädaransvar workstream
**Kategori:** swedish_tax + swedish_corp
**Taggar:** företrädaransvar, SFL 59:12-13, rådrum, befrielse, oskälighet, konkurs, verksamma_åtgärder, moms, Prop_2025/26:52

Verified live (WebSearch 2026-07-07): a new law amending the skatterättsliga företrädaransvaret took effect **1 July 2026** (Prop. 2025/26:52, "nya regler om befrielse och rådrum"):
1. **Rådrum:** a representative who may become personally liable can **apply for a two-month rådrum** from the tax's original due date; the assessment of personal liability then **shifts from the original förfallodag to the end of the rådrum** — a statutory breathing space to arrange an orderly settlement without liability crystallising.
2. **Befrielse broadened to "oskäligt":** relief (whole/partial) where it is *unreasonable* to hold the representative liable, with enumerated factors — wider than the prior narrow standard.

The base rule is unchanged: **SFL 59 kap. 12-13 §§** — VD/firmatecknare personally liable for the entity's unpaid tax/VAT on uppsåt/grov oaktsamhet; classic relief = verksamma åtgärder (konkurs-/rekonstruktionsansökan) **by the due date** (HFD 2018:4). Konkurs does NOT erase already-accrued företrädaransvar — it's assessed as of the due date, not the konkurs date.

**How to apply:** When a client's AB has unpaid VAT/tax and the client is a representative, the first move is not "let it go bankrupt" — it's (1) quantify, (2) file rättelser/current returns, (3) **apply for rådrum** on the amounts first falling due (new since 2026-07-01), and (4) pay or take verksamma åtgärder within the window. This shifts the assessment point and evidences good faith (defeats grov oaktsamhet). Wiki `sv_tax.md` updated.

## 2026-07-07 — Controlled bankruptcy of a related-party, VAT-owing AB to extract its main asset is the worst-case on BOTH företrädaransvar and återvinning — prefer a solvent transfer

**Källa:** Erik/Afrime analysis — "controlled Runatyr bankruptcy → AP buys RLR from estate" plan
**Kategori:** swedish_corp + swedish_tax
**Taggar:** återvinning, KL 4:3, KL 4:5, KL 4:10, KL 5:15, närstående, företrädaransvar, kvittning, arm's_length, controlled_bankruptcy

The proposed plan — deliberately bankrupt Runatyr (unpaid ~1M SEK VAT), then have related-party AP buy the flagship IP (RLR) from the estate, partly by setting off AP's own 5M loan — stacks maximum risk:
1. **Återvinning is time-unbounded for närstående.** All parties are närstående (`KL 4:3`): Runatyr 50% CZP / 50% Yasin, Robert = CZP 100% + Runatyr VD/firmatecknare, AP CZP-affiliated. `KL 4:5` (otillbörlighet) has **no backward time limit** for related parties (the 5-year cap binds only non-related parties); `KL 4:10` (payment/set-off of debt) look-back is **2 years** for närstående (vs 3 months); set-off in konkurs is separately barred under `KL 5 kap. 15-16 §`. A below-market or set-off RLR extraction is squarely recoverable.
2. **Skatteverket as unpaid-VAT creditor** is a motivated party pushing the trustee to challenge.
3. **Företrädaransvar** for the VAT is assessed at the due date; bankrupting the company now doesn't erase it and the asset-strip optics make grov oaktsamhet easier to argue.

**Cleaner route: keep the company solvent, regularise the VAT (rådrum), get an independent valuation, and sell the IP directly to the acquirer at market with the loan set off against price, board-approved with the conflicted director recused (`ABL 8:23`).** A solvent arm's-length transfer never opens the återvinning window and never involves a trustee. The only thing the bankruptcy route buys — a trustee "clean-hands" stamp on the sale — is outweighed by loss of price control, the företrädaransvar optics, and the chance the asset gets pulled into a *different* estate's claims.

**How to apply:** Whenever a client proposes "let entity X go under, then buy its best asset into entity Y," and X and Y are related and X owes tax — reframe hard toward a **solvent transfer first**. The bankruptcy-then-repurchase route is a återvinning + företrädaransvar magnet. Always: independent valuation (never the client's own cost figure), real consideration, jäv-clean board approvals, and tax regularised before the asset moves.

## 2026-07-07 — A 32%+ blockholder can veto any control move: directed issue / directed warrant grant / directed apport all need 9/10 (ABL 13:2, 14:2)

**Källa:** Erik/Afrime analysis — staged path-to-control over AP, Behold 32.26%
**Kategori:** swedish_corp
**Taggar:** ABL 13:1, ABL 13:2, ABL 14:2, ABL 13:41, företrädesrätt, riktad_nyemission, teckningsoptioner, apportemission, kvittningsemission, blockholder, pre-emption

A "Tencent-style" ladder to majority/full ownership of a Swedish AB cannot be delivered by the founder's own stake when a VC block exists. Existing shareholders have statutory **företrädesrätt** to a cash issue pro rata (`ABL 13 kap. 1 §`); to bring a new investor in over that, you either get every holder to waive, or the stämma resolves a **riktad (directed) nyemission** disapplying företrädesrätt — which needs **9/10 of votes AND shares represented** (`ABL 13 kap. 2 §`). The same 9/10 governs a **directed teckningsoptioner grant** (`14 kap. 2 §`), a **directed apportemission**, and a **directed kvittningsemission** (`13 kap. 41 §`). **Consequence: any holder above 10% (here Behold at 32%) can block every directed step.** The control ladder is structurally impossible without the blockholder's alignment — surface that before any term sheet, not after.

Swedish vehicles for the ladder: **teckningsoptioner (ABL 14 kap.)** for "right to subscribe more later" (registered, enforceable); **contractual call options** over existing shares for the control tail (but specific performance of a share transfer is weaker in Swedish law — back with aktiepant, irrevocable proxies, liquidated damages, and AA drag-along; the blockholder must be a signatory to anything touching its stake). Entry = directed nyemission; upside = warrants; tail = call options + drag.

**How to apply:** First question on any change-of-control into a Swedish AB with outside holders — "what's the largest single block, and is it above 10%?" If yes, that holder has a veto on every directed issue/warrant/apport/kvittning. Read the aktieägaravtal (hembud/förköp/samtycke/drag/anti-dilution) before designing anything; the AA can bind even where the ABL default would allow the move.

## <!-- ARCHIVE-INDEX -->Archived learnings index

8 older entries were rotated into `archive/lawyer/` to keep this file loadable in one pass.
Nothing was deleted. They are still indexed by RAG — `rag_search(query, source="agents")` finds them,
or open the archive file below (each has its own Contents block, so you can offset-read a single entry).

### 2026-Q3 — 1 entries → [`2026-Q3.md`](archive/lawyer/2026-Q3.md)

- 2026-07-07 — Negative equity + kapitalskydd-blocked loan repayment is affirmative evidence a…

### 2026-Q2 — 7 entries → [`2026-Q2.md`](archive/lawyer/2026-Q2.md)

- 2026-06-24 — "For clarity" carve-outs must anchor to a defined date, not a borrowed "Effecti…
- 2026-06-22 — PIVOT 5: decoupling the music-licensing leg from a composer's employment contra…
- 2026-06-18 — Contractor counter-redline on back-to-back subs: gating termination-for-conveni…
- 2026-06-18 — Swedish bankruptcy claims verification (bevakningsförfarande): strict absolute…
- 2026-06-17 — Employer-employee + direct composer↔publisher music licence: the URL no-WFH "bu…
- 2026-06-17 — Game-audio IP can route either composer→publisher direct OR composer→employer→p…
- 2026-06-17 — Splitting the employer from the IP-assignee in a group: assign work-product dir…
