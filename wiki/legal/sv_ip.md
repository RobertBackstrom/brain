---
title: Swedish & EU IP Law
owner: Lawyer agent
status: skeleton
last_reviewed: 2026-08-26
primary_sources: upphovsrättslagen (1960:729), varumärkeslagen (2010:1877), patentlagen (1967:837), mönsterskyddslagen (1970:485), FHL (2018:558)
---

# Swedish & EU IP Law

Reference. Not legal advice. Real lawyer required for enforcement, infringement defense, or anything entering registration prosecution at PRV/EUIPO.

## Förvärv av IP ur ett konkursbo (rörelseöverlåtelse)

*Tillagt 2026-08-26 ur APDS-konkursen (K 4429-25 Umeå TR), APDS konkursbo -> Bright Gambit AB -> CZP. Se `umbrella/aurora_punks/legal/apds_entity_transfer_master_2026-08-26.md`.*

- **Boet kan inte överlåta mer än gäldenären ägde.** Självklart i teorin, lätt att missa i praktiken,
  eftersom överlåtelseklausulen brukar vara vid ("rätten till bolagets immateriella rättigheter,
  inklusive men inte begränsat till källkod och distributionsrättigheter") medan bilagan tyst
  redovisar att flera poster ägs av tredje man eller av ett systerbolag. **Läs ägarkolumnen i
  bilagan, inte rubriken i avtalet.** Det är bilagan som avgör vad köparen faktiskt kan hävda.
- **Vad som ändå överlåts för en titel vars upphovsrätt ligger hos någon annan:** gäldenärens
  *position*. Källkod, utvecklarrollen, distributions- och publiceringsrättigheter, avtalspositioner.
  Det räcker för att flytta ett plattformskonto, men det bär inte påståendet "vi äger IP:t".
  Sverige har ingen work-for-hire-doktrin (`URL 40 a §` täcker bara datorprogram i anställning), så
  äganderätten följer inte med automatiskt bara för att koden gör det.
- **Tillsynsmyndighetens godkännande är ett tillgång, inte en formalitet.** Enligt `KL 7 kap. 10 §`
  ska förvaltaren i viktigare frågor höra tillsynsmyndigheten och särskilt berörda borgenärer, och
  försäljning av en rörelse är uttryckligen en sådan fråga. Bär avtalet en klausul om att TSM
  godkänt, citera den: den föregriper den enklaste invändningen mot förvärvet.
- **Boet friskriver sig fullständigt, som standard.** Räkna med formuleringar i stil med
  "Säljaren lämnar inga garantier beträffande möjligheterna att överföra eller använda dessa
  rättigheter" och "Köparen är ensamt ansvarig för att kontrollera rättigheterna". Hela
  due diligence-bördan ligger på köparen, och det finns ingen att gå tillbaka till efteråt.
- **Äganderättsförbehåll är standard i boavtal.** Äganderätten övergår först när köpeskillingen
  är till fullo betald. Vid en förvärvskedja i flera led måste betalning beläggas i **varje** led,
  annars är kedjan formellt obruten bara på papperet. Begär betalningsbevis, inte bara avtalet.
- **Distributionsavtal med insolvensklausul överlåts inte.** Bär avtalet "explicit termination if
  insolvency, liquidation, or bankruptcy" upphörde det på konkursdagen, alltså före boets
  försäljning. Det fanns då ingenting kvar att överlåta. Kontrollera klausulen innan en sådan titel
  räknas in i förvärvet.
- **Moms.** Boet brukar behandla försäljningen som verksamhetsöverlåtelse och inte debitera moms.
  Säljs samma tillgångar vidare i nästa led måste momsfrågan ställas om från början: debiteras moms
  på något som också är en verksamhetsöverlåtelse är det felaktigt debiterad moms, och köparens
  avdrag kan nekas. Se [[sv_tax]].
- **Partsidentifiering.** Kontrollera org.nr mot bilagorna och mot tingsrättens målhandlingar. Ett
  fel nummer i ingressen med rätt bolagsnamn gör knappast avtalet ogiltigt, men det ger en motpart
  en gratis invändning och rättas billigast med en skriftlig bekräftelse från förvaltaren.

## Upphovsrätt (Copyright)

- **Verksbegrepp** — work threshold (`URL 1 §`); independent creation + minimum originality.
- **Skyddstid** — life + 70 years (`URL 43 §`).
- **Ekonomiska rättigheter** — exemplarframställning, tillgängliggörande för allmänheten.
- **Ideell rätt** (moral rights) per `URL 3 §` — namngivelse + respekträtt; **cannot be assigned**, only waived in scope/extent. This is the big trap in international assignment templates that assume US-style WFH.
- **No work-for-hire doctrine** in Sweden. IP created by employees in employment vests with employer only via:
  - `URL 40 a §` (computer programs — automatic transfer to employer)
  - Explicit contract assignment for everything else, OR
  - Implied license via the "verkställande tjänsteman"-doctrine — narrow, don't rely on it.
- **Contractor IP** — *no automatic transfer at all*. Contract MUST contain explicit assignment. AP AB Subcontracts master template handles this; verify partner drafts include equivalent.

## Varumärke (Trademark)

- **PRV** — Swedish national mark, classes per Nice agreement.
- **EUIPO** — EU mark covering all 27 member states.
- **WIPO Madrid** — international registration via PRV/EUIPO base.
- **Use requirement** — risk of cancellation after 5 years non-use (`VML 3 kap. 2 §`).
- **Game titles** — title alone often weak; combine with logo + stylized wordmark for stronger protection.

## Patent

- **PRV** — Swedish national; 20 years from filing.
- **EPO** — European Patent Convention; bundles into national validations or unitary patent.
- **PCT** — international filing route; 30/31-month national phase entries.
- **Software patents** — limited in Europe; "as such" exclusion under EPC Art. 52.

## Mönsterskydd (Design Rights)

- **Swedish national mönster** via PRV.
- **Registered Community Design (RCD)** — EUIPO; 25 years (5+5+5+5+5).
- **Unregistered Community Design (UCD)** — automatic on disclosure, 3 years protection.
- Useful for game asset look-and-feel, character designs, packaging.

## Trade secrets / FHL

- **FHL (2018:558)** — implements EU Trade Secrets Directive.
- Definition: information not generally known, has commercial value because of secrecy, reasonable steps taken to protect.
- Survives end of employment if specific (general skill/knowledge does not).

## Game-specific IP

### Engine licensing
- **Unity** — runtime fee history (rolled back 2024); per-seat Pro/Enterprise; revenue thresholds; source access via Source license.
- **Unreal** — 5% royalty after $1M lifetime per product (custom enterprise terms supersede).
- **Godot** — MIT, no royalty, no source restrictions. (Robert's strategic angle for IP retention.)

### Middleware
- Wwise, FMOD, Speedtree, Substance, Houdini Engine — each has its own licensing model. Check thresholds, indie tiers, attribution requirements.

### Asset stores
- Unity Asset Store / Unreal Marketplace EULAs vary per asset; some seat-restricted, some project-restricted, some workgroup-wide. Read each.

### Contractor IP for game studios
- AP AB Subcontracts master template handles assignment under Swedish URL — verify it covers:
  - Full economic rights assignment to AP AB / project SPV
  - Moral rights waived to maximum extent permissible
  - Carve-outs for contractor's pre-existing tools / general utilities (with license back to AP AB to use in deliverables)
  - Open-source disclosure obligation (so we know what's GPL/MPL/AGPL before it ships)

### Publisher IP terms
- Standard pub deals: pub gets exclusive distribution rights (license, not assignment), dev retains underlying IP.
- Watch for: derivative works rights, sequels/prequels rights, port/platform rights, marketing materials ownership, music separate licensing, voice-actor rights.
- "All rights reserved to publisher" clauses — push back, dev should retain unless the deal is explicitly an IP buyout (rare, usually 7-figure).

## Anställning på ett koncernbolag som INTE är uppströmsmotpart (kontrollerad 2026-08-26)

Konstruktionen dyker upp så fort ett holdingbolag är arbetsgivare men ett annat koncernbolag bär
leveransåtagandet mot kunden. Konkret fall: CZP anställer en pixelartist, medan **AP** är den som är
skyldig Raw Fury leveransen enligt utvecklingsavtalet. Två fällor, båda tysta.

**1. Anställningen i sig överlåter ingenting för bildkonst.** `URL 40 a §` täcker **endast
datorprogram**. Pixelart, sprites, miljökonst, UI-grafik och animationer är konstnärliga verk, så
rätten stannar hos upphovsmannen om avtalet inte innehåller en **uttrycklig överlåtelse**. Se
bulletlistan under "Upphovsrätt" ovan. Ett anställningsavtal som bara lutar sig mot anställningen,
eller som citerar 40 a § som om den vore generell, överlåter alltså inte konsten. Skriv en egen
klausul som överlåter vid skapandet, för hela skyddstiden, i alla världens länder och alla nuvarande
och framtida exploateringsformer, och **täck källfiler och arbetsfiler**, inte bara levererade assets.

**2. Överlåtelsen stannar hos arbetsgivaren om ingen vidareöverlåtelse skrivs in.** Arbetsgivaren blir
rättighetshavare, inte systerbolaget. Utan en uttrycklig vidareöverlåtelse når konsten aldrig den part
som är bunden mot utgivaren, och bristen syns inte förrän någon granskar rättighetskedjan, typiskt vid
due diligence eller när utgivaren begär garantier. **Avgjort 2026-08-27 (Simon-ärendet): de två
"alternativen" nedan är i själva verket två olika rättsfrågor, och båda behövs.**
- **Den anställdes samtycke** (klausul i anställningsavtalet där den anställde samtycker till, och i
  nödvändig mån medverkar till, arbetsgivarens vidareöverlåtelse till systerbolaget och vidare till
  utgivaren, på samma villkor som huvudöverlåtelsen; ska överleva anställningens upphörande). Krävs
  på grund av `URL 28 §` (verifierad ordagrant mot lagen.nu 2026-08-27): *"Om ej annat avtalats,
  äger den till vilken upphovsrätt överlåtits icke ändra verket samt ej heller överlåta rätten
  vidare."* Utan klausulen får arbetsgivaren inte överlåta vidare alls.
- **Själva dispositionen mellan bolagen**: ett koncerninternt IP-överlåtelseavtal. Samtyckesklausulen
  kan inte ersätta den, eftersom systerbolaget inte är part i anställningsavtalet och inte kan
  förvärva genom det. Bäst form: automatisk överlåtelse i samma ögonblick arbetsgivaren förvärvar
  rättigheterna, med retroaktiv verkan för redan utfört arbete, back-to-back-scope mot
  anställningsavtalets överlåtelseklausul, och vederlag (självkostnadsvidarefakturering av
  lönekostnaden räcker; vederlagsfritt öppnar uttagsbeskattning `IL 22 kap.` när bolagen inte är i
  äkta koncern). Notera att ett befintligt **paying agent-avtal inte duger** — det reglerar
  betalning, inte immaterialrätt. Mall: `k2c_sands_of_duat/Legal/K2C_CZP_AP_IP_Assignment_2026-08-27_DRAFT.md`.

**3. Ideell rätt följer inte med.** `URL 3 §` namngivelse- och respekträtt kan inte överlåtas, bara
efterges i angiven omfattning (se avsnittet nedan). Ta ett samtycke till normal bearbetning och
användning för titeln, och lova inte credits som koncernen inte själv har säkrat uppströms — se
"Credit / attribution in co-dev and outsourcing agreements".

**4. Lönen får inte villkoras av att utgivaren betalat.** Detta är arbetsrätt, inte immaterialrätt,
men det slår sönder just den här avtalsformen om man kopierar ett B2B-upplägg rakt av: en
pass-through-klausul som gör utbetalningen beroende av att kunden betalat flyttar affärs- och
kreditrisken till den anställde. Milstolpar får styra **intjänandet** (leverans plus godkännande),
aldrig betalningsvillkoret. Se `sv_employment.md`.

**Tillämpat i:** `k2c_sands_of_duat/contracts_2026_subcontractors/draft_12_simon_czp_employment.md`
(§8.2 uttrycklig överlåtelse, §8.3 40 a §-avgränsningen utskriven, §8.7 vidareöverlåtelse CZP → AP,
§6.2 arbetsrättsspärren) samt `k2c_sands_of_duat/Legal/K2C_CZP_AP_IP_Assignment_2026-08-27_DRAFT.md`
(den koncerninterna dispositionen) och `Legal/LEGAL_MEMO_K2C_Simon_IP_kedja_2026-08-27.md` (analysen).

**Bonusfynd i samma ärende (arbetsrätt, inte IP):** `LAS 6 c §` sätter en lagstadgad frist på att få
ut avtalet: skriftlig information om väsentliga villkor senast **sjunde kalenderdagen efter
arbetsstart**, och för särskild visstidsanställning ska visstidsinformationen lämnas **i samband med
att anställningen ingås** (verifierad ordagrant 2026-08-27). En anställd som redan börjat jobba utan
påskrivet avtal är alltså inte bara en processrisk utan en löpande 6 c §-överträdelse med
skadeståndsrisk (`LAS 38 §`).

## Ideell rätt — eftergift kan inte ske blankt (URL 3 § 3 st)

**Verifierat 2026-05-03 (RLR/Scen & Film-ärendet).**

URL 3 § 3 st: *"Med bindande verkan kan upphovsmannen eftergiva sin rätt enligt första eller andra stycket endast såvitt angår en till art och omfattning begränsad användning av verket."*

En bred IP-överlåtelseklausul i anställningsavtal (typ "alla rättigheter inklusive copyright är bolagets exklusiva egendom") överlåter giltigt **ekonomisk rätt** men kan **inte** generellt eftergiva ideell rätt. Eftergift måste vara *specifik till art och omfattning*. Praktisk konsekvens: anställd kvarhåller namngivelserätt även efter total ekonomisk-rätt-överlåtelse.

Det här är **inte** vad en internationell mall skriven mot US work-for-hire försöker åstadkomma. AP AB:s subkontraktsmall hanterar detta korrekt med språk om "*moral rights waived to maximum extent permissible*" — den förmuleringen är giltig (begränsar sig till "permissible").

## Yrkanden från fackförbund (Scen & Film, Författarförbundet, KLYS-medlemmar) baserade på ideell rätt

**Verifierat 2026-05-03.** Vanliga yrkanden:
- Bekräfta mottagande av brev
- Bekräfta korrekt namngivelse vid framtida exemplarframställning/tillgängliggörande
- Skicka fysiskt exemplar (för granskning)
- Förbehåll om skadeståndskrav (URL 54 § — skälig ersättning + ev "ytterligare skada" inkl ideell skada)

Strategi: **efterlev inom exakt scope.** Ideell rätt är inte stridsbar position på lagrum. Att slåss = exponera bredare ärenden. Säkra istället att svaret inte koncederar ekonomisk rätt eller bredare upphovsrätt.

## Credit / attribution in co-dev and outsourcing agreements

**Verifierat 2026-08-17 (K2C/Pharaoh Lands, AP↔Raw Fury LTC).**

Credit is **not** a default. A plain outsourcing/work-for-hire agreement with a full assignment clause gives the developer **no** right to be named, no in-game splash, no logo placement, and normally no right to talk about the work at all. If credit is not written in, it does not exist. Three fallback arguments and what each is actually worth:

1. **`URL 3 § 1 st` (namngivningsrätt), verbatim:** *"Då exemplar av ett verk framställes eller verket göres tillgängligt för allmänheten, skall upphovsmannen angivas i den omfattning och på det sätt god sed kräver."* Cannot be waived in blanket form (`URL 3 § 3 st`, see section above), so it survives even a total economic assignment. **But it belongs to the physical creators, not to the studio AB.** A studio is never *upphovsman*. It gets the individuals a line in the credits list per industry custom; it does not get the company a splash screen or a logo. Useful as background pressure, useless as a company-level claim.
2. **Referential trademark use, `VmL (2010:1877) 1 kap. 11 § p 3`, verbatim:** ensamrätten hindrar inte att någon annan, *"när det sker i enlighet med god affärssed, i näringsverksamhet använder ... varukännetecknet för att identifiera eller hänvisa till innehavarens varor eller tjänster."* A truthful factual statement ("we developed X for Y") is normally lawful referential use. It does **not** carry screenshots, key art, trailers or logos — those are the publisher's copyright and need permission.
3. **The contract's own confidentiality clause is usually the real blocker**, not the missing credit clause. Where the agreement deems "the Work" Confidential Information and bars publication to third parties without prior written approval, the developer is contractually silent until the publisher announces. The escape hatch is the standard public-domain carve-out ("becomes publicly known without breach"), which releases only what the publisher has actually made public, and only after it has done so.

**Practical rule:** the credit ask is cheap at contract time and near-impossible afterwards, because a complete-agreement clause means only a signed written amendment moves it. Put a Credit clause in every AP outsourcing/co-dev draft covering (a) credit wording and placement in the in-game credits, (b) whether a developer logo/splash appears and where, (c) the "developed by" line on storefront pages, (d) named permission to state the engagement publicly from a defined date, and (e) which marketing assets the developer may reuse in its own channels and portfolio.

**Back-to-back check:** never grant subcontractors portfolio/showreel rights (screenshots, video clips, credit references) that the studio does not hold upstream. Sub-licensing a publisher's copyright that was never licensed to you is the exposure, and it is easy to create by copy-pasting a standard §3.9 portfolio clause into six sub drafts.

## STIM-anslutning: vad en kompositör faktiskt kan ge bort

**Verifierat 2026-09-02** ordagrant mot [Allmänna villkor för anslutning till Stim](https://www.stim.se/om-oss/villkor-och-avtal/allmanna-villkor-for-anslutning-till-stim).

Återkommande fråga i varje spelmusikaffär med en svensk kompositör: "kan hon skriva under en
assigns-all-rights-klausul?" Svaret kräver att man delar upp rättigheterna i tre lager.

**Vad STIM faktiskt håller (och som därför INTE kan överlåtas till en publisher):**
- **3.2:** den Anslutne upplåter exklusivt "såväl existerande som framtida Musik" och "har [inte]
  rätt att till annan upplåta eller överlåta de Ekonomiska rättigheter som omfattas av detta Avtal".
- **3.5:** garanterar att rättigheterna inte upplåtits/överlåtits till annan.
- **9.2:** åtagande att "inte träffa överenskommelse som strider mot Avtalet".
- => En "assigns ALL rights"-underskrift sätter kompositören i garantibrott mot STIM. Reell risk.

**Kan man plocka enskilda verk ur STIM? NEJ.**
- **5.1, ordagrant:** *"En Ansluten har rätt att begränsa ett lämnat förvaltningsuppdrag genom att
  från Stims förvaltning återta en eller flera rättighetskategorier från det eller de territorier
  som den Anslutne önskar. **Ett återtagande kan aldrig ske på verksnivå.**"*
- **12.2:** 6 månaders uppsägningstid, även vid begränsning. **6.1:** utökning kan ske när som helst.
- **3.10:** ideella rätten (`URL 3 §`) stannar alltid hos upphovspersonen (jfr avsnittet ovan).
- **3.8:** förstaframföranderätten ligger kvar hos musikskaparen; licensen omfattar inte verk där den
  ännu inte utnyttjats. **3.9:** musikdramatiska verk omfattas inte.

**Vad som ligger UTANFÖR mandatet och alltså är kompositörens att ge direkt:**
1. **Synk av beställningsmusik.** STIM: *"Du får förhandla själv om synkroniseringsavgiften samtidigt
   som du förhandlar om din lön för beställningen... fri förhandling mellan dig och beställaren."*
   Musik komponerad på beställning till ett spel ÄR beställningsmusik → **direktlicensiering**.
2. **Masterinspelningarna.** STIM hanterar inte masterrätt. Kan överlåtas rakt av. (Utövande
   konstnärs närstående rättigheter → SAMI, separat fråga.)

**Kvar inom mandatet: framförande + mekanik.** I en spelaffär biter mekaniken på i praktiken ETT
ställe: publisherns **egen OST-release** (mångfaldigande, i Norden licensierat via NCB). Allt annat
(in-game, patchar, portar, trailers, marknadsföring) löses via direktlicensierad synk.

**STIM:s per-verk-instrument för spel (verifierat mot blanketten 2026-09-02).** Att förvaltnings-
uppdraget inte kan ÅTERTAS på verksnivå (5.1) betyder inte att verk inte kan frigöras. STIM har
blanketten **"Direct Licensing of (a) Certain Music Work(s) in a Video Game"**: per namngivet verk
(STIM Work Title + Work Number) och per namngivet spel avstår STIM sin licensiering och ger
kompositören "the sole and perpetual right to directly license or assign". Verken stannar i STIM för
all annan användning. Signeras av kompositören OCH STIM; kräver verkanmälda spår med verknummer plus
slutlig speltitel, alltså inte en samma-dag-sak. **Generell lärdom: fråga efter kollektivförvaltarens
blankettflora innan du svarar nej på en avgränsningsfråga.**

**Waiverns tre luckor.** "Video Game Use" = verken **som integrerad del av spelet**, sync i
marknadsföringsmaterial, och producentens **egna** plattformar. Täcker alltså INTE: (1) utgivarens
**fristående OST-release** (inte integrerad del → NCB eller utvidgad definition); (2) **tredjeparts
streamers**, eftersom "in relation to any other use ... the Affiliation Contract shall fully apply"
— waivern levererar INTE stream-safe; (3) **kommande titlar i serien**, eftersom den binds till ETT
namngivet spel. Bonus i utgivarens favör: STIM åtar sig att inte licensiera verken till något annat
spel. Textkopia: `umbrella/k2c_sands_of_duat/contracts_2026_subcontractors/_rf_music_templates/STIM_waiver_direct_licensing_video_game.md`.

**Stream-safe: utgivarens hårda krav (Robert 2026-09-02).** Ovanstående uppdelning får INTE säljas in
till kompositören som "du behåller hela STIM-intäkten". Varje spelutgivare kräver att musiken är
stream-safe, dvs att den inte kan trigga claim, strike, demonetisering eller takedown mot content
creators som streamar gameplay. Två mekanismer som måste hållas isär: **PRO-waivern** stoppar STIM:s
egen inkassering, medan **YouTube Content ID / Facebook Rights Manager / Twitch audio-recognition**
claimar oberoende av waivern och kräver ett separat åtagande (ingen registrering, whitelisting,
skyldighet att dra tillbaka claims). Den ärliga uppdelningen mot kompositören: **spelanvändning och
streamers avstås; musiken som musik (egen DSP-release, radio, live) behålls.** Skriv alltid in den
motvikten, annars läser klausulen som total avsägelse och kompositören vägrar.

**Fyra branschstandarder, rangordnade efter genomförbarhet mot en mall-publisher:**
1. Överlåtelse enligt publisherns mall + **STIM-carve-out i Special Conditions** (rekommenderas: mallen
   står orörd, Special Conditions finns till för att anpassas per kompositör).
2. **Master-buyout + evig exklusiv synklicens** på kompositionen. Vanligaste europeiska indie-standarden.
3. Publishern tar **förlagsandelen** och registreras som musikförlag i STIM. Verifiera tillåten andel
   mot STIM:s fördelningsregler innan siffra föreslås (EJ verifierad per 2026-09-02).
4. Ren licens, kompositören behåller allt. Svagast mot publisher.

**Tillämpning:** dekomponera alltid till synk / master / framförande+mekanik och peka ut vilket lager
som faktiskt är omtvistat. Det gör svaret till motparten "ni behöver inte ändra ert avtal" i stället
för "vi vill omförhandla". Se `umbrella/k2c_sands_of_duat/contracts_2026_subcontractors/memo_stim_music_rights_2026-09-02.md` (K2C/Carolina/Raw Fury).

## Robert's positions

- **2026-05-03 (RLR/Scen & Film):** Försökte hävda att Yasin Hillborg "inte kan hävda upphovsrätt på IP:t" — vilket missförstod vad propån yrkade (ideell rätt, ej ekonomisk). Justerades efter genomgång — strategi blev efterlevnad inom scope, inte stridsläge. Tar rak återkoppling när den är lagrum-baserad.

## Open questions

- Hur ser konkursförvaltarens (Carler/Mattsson) bedömning av IP-kedjan Runatyr→APDS→AP ut i APDS-konkursen?
- Är 2023-IP-Avtalet Runatyr→AP klanderbart givet att Yasin (50% delägare i Runatyr) inte godkände det?
