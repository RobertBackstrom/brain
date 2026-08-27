---
title: Swedish Corporate Law (ABL)
owner: Lawyer agent
status: active
last_reviewed: 2026-08-05
last_updated: 2026-08-05
primary_source: aktiebolagslagen (2005:551), lagen.nu
---

# Swedish Corporate Law (ABL)

Reference. Not legal advice. Verify citations before relying.

## Board duties (ABL 8 kap.)

- **Firmateckning** — who can sign for the company; default styrelsen i förening unless bolagsordning/protokoll says otherwise. Verify per registreringsbevis: Bolagsverket via `https://www.allabolag.se/<orgnr>` for Swedish AB, Companies House via `https://find-and-update.company-information.service.gov.uk/company/<companyNumber>` for UK Ltd. **Practical rule for contract signature blocks:** the signatory's title under the signature line must match the firmateckning-bearing role on the registreringsbevis (VD / Styrelseledamot / Director), NOT the project role they hold ("Lead Designer", "Porting Lead" etc). The project role is fine in the body of the contract; it just shouldn't be in the binding signature. (K2C subcontract review, 2026-05-06)
- **Beslutsförhet** — quorum rules; jäv (conflict of interest) per `ABL 8 kap. 23 §`.
- **VD's mandate** — `ABL 8 kap. 29 §`; löpande förvaltning.

_Fill on first real task._

## Bolagsstämma

- Per capsulam vs digital vs fysisk — see admin agent learning 2026-04-29: Bolagsverket no longer accepts per capsulam for board/VD changes (2025+ practice change). Default to digital.
- Kallelseregler, beslutsmajoritet, protokollsformat.

## Aktieägaravtal (SHA)

- Drag-along / tag-along enforceability under Swedish law.
- Vesting + leaver provisions.
- ROFR vs ROFO.

## Bolagsordning

- Mandatory clauses per `ABL 3 kap. 1 §`.
- Hembudsklausul, samtyckesklausul, förköpsklausul.

## Bolagsverket filings — substance

(Mechanics owned by CorpBot. Lawyer judges *what is required* and *what risk* a filing creates.)

## Intercompany structures (paying-agent vs kommissionärsbolag vs sub-license)

When a Swedish AB group needs one entity to hold a contract while another fronts the billing — typical when the contracting AB has VAT/F-skatt registration pending — three Swedish frameworks apply:

**1. Paying-agent / disclosed agency (sw. *betalningsombud*).** Lightest form. Principal AB holds the contract end-to-end; agent AB is authorised by written agreement and a notice to the upstream counterparty to issue invoices, receive payments, and disburse subs on principal's behalf. Agent holds **no economic interest** in the contract (book inflows as IC payable, not revenue). No fee unless explicitly agreed (and any fee must be supported by ABL 17:1 business motivation). Default choice when the upstream contract permits invoicing through "affiliated companies or subcontractors."

**2. Kommissionärsförhållande (IL 36 kap. 1–4 §§).** Heavier statutory form. Kommissionärsbolag conducts business *in its own name* for kommittentens account; if the six conditions are met, kommissionärsbolag's profit is taxed at kommittent. Conditions: written agreement; both Swedish AB; principal is exclusive; profit transferred annually to principal; commission verksamhet is the kommissionärsbolag's main activity; same koncern for tax purposes. Reject when the agent AB has substantial non-commission activity (fails condition 5).

**3. Sub-license / sub-contract.** Two arm's-length contracts: principal AB licenses or sub-contracts the work to operating AB at a defined price. Creates a priced AP↔operating-AB transaction subject to ABL 17:1 (olovlig värdeöverföring) and IL 16:1 (avdragsrätt) scrutiny. Triggers an internprissättning surface even within Sweden — the price needs to be defensible. Heaviest of the three.

**Robert's position (K2C 2026-05-04 — k2c-003):** Default to paying-agent for short-duration registration-bridge cases. The AP↔CZP Paying-Agent Agreement template lives at `umbrella/k2c_sands_of_duat/Legal/K2C_AP_CZP_PayingAgent_Agreement_2026-05-04_DRAFT.md` (2-3 page intercompany doc, mirrors Section 2.4 paying-agent clauses already present in all five K2C sub drafts). The notice-letter template to upstream publisher lives in the same folder.

Self-dealing safeguard (ABL 8:23): when same person signs for both Principal and Agent AB, principal-side signature must be by other directors (not the dual-role person), and the dual-role person abstains from voting on the IC arrangement on the principal-side board. K2C convention: AP signed by Mattias Wiking + Andreea Chifu; CZP signed by Robert.

## Personal guarantees by directors of subsidiaries — recourse limits

When the same person serves as VD/firmatecknare for a subsidiary AB *and* is principal of a holding AB (or has a separate consulting AB) that hires them out, **personal guarantees signed for the operating subsidiary's credits do not automatically pass through to the consulting/holding entity** if the operating sub goes bankrupt.

Standard CZP-style consulting agreement (mall: WLBS 2022-06-01) carries D&O / E&O insurance obligation but **no indemnification clause** for personal guarantees. Routes that fail:

- **Sysslomansregress (`HB 18 kap. 4 §`)** — agent's reimbursement right runs against the *huvudman* (the entity for whose benefit the outlay was made). Personal guarantee for sub's credit = sub is huvudman; recourse already exists as bankruptcy claim. Holding/consulting AB cannot be inserted as "intermediate principal."
- **Skadeståndslagen 3:1 (principalansvar)** — covers employer liability for harm employee causes *third parties*, not employee's own voluntary financial commitments.
- **Frivillig betalning från konsult/holding-AB till individen** — classified as **olovlig värdeöverföring** (`ABL 17 kap. 1 §`) absent business motivation; omclassified to **förtäckt utdelning or lön** for 3:12 and beskattas hos individen oavsett benämning. ABL 17:6 återbäring + 17:7 bristtäckningsansvar för styrelse.
- **Cession of bankruptcy claim from individual to own holding-AB** — at market price gives no benefit (same kapitalförlustavdrag realiseras antingen via försäljning eller via slutlig utdelning, IL 54:6); above market triggers ABL 17:1 + förtäckt utdelning.

**Clean route for individual borgensman:** retain claim, pursue konkursutdelning, claim **kapitalförlust på fordran** under `IL 54 kap. 6 §` (70 % avdragsgill mot kapital) for the unrecovered portion.

**Exception (when recourse may exist):** Express indemnification clause in consulting/employment agreement, **or** documented holding-AB board resolution authorising VD to sign guarantee "for holding-AB's account" — must pre-date the bankruptcy. Verify by reading the actual agreement and minute book before relying.

**Practical fix going forward:** Either (a) add indemnification clause to consulting agreements between holding/consulting AB and operating subs, (b) price a borgensavgift (guarantee fee) to the individual as risk compensation, or (c) use non-personal security (företagshypotek, factoring).

Memo: `umbrella/aurora_punks/legal/apds_borgen_recourse/memo_2026-05-04_borgen_recourse.md`.

## Bolagsverket-föreläggande om ny styrelse när bolaget redan är i konkurs

Ett automatiskt Bolagsverket-brev "Anmäl styrelse" / "saknar behörig styrelse" med hot om tvångslikvidation (`ABL 25 kap. 11 §`) + särskild avgift (3 900 kr) **behöver inte åtgärdas när bolaget redan är försatt i konkurs**:

- **Konkurs och likvidation är ömsesidigt uteslutande.** Tvångslikvidation enligt 25:11 gäller bolag i drift, inte ett bolag vars tillgångar förvaltas av en konkursförvaltare. Brevet är typiskt ett registerutskick som inte korsats mot pågående konkurs.
- **Bolaget upplöses ändå via konkursen** — avslutas konkursen **utan överskott** är bolaget automatiskt upplöst när konkursen avslutas, utan likvidation (`ABL 25 kap. 50 §` motsatsvis). Domstolsbeslutad likvidation efter konkurs inträffar bara om konkursen avslutas **med** överskott (25:50 direkt).
- **Ingen personlig risk från just föreläggandet.** Den särskilda avgiften påförs bolaget (oprioriterad fordran mot tomt bo). Personligt betalningsansvar för styrelse hänger på kapitalbrist/kontrollbalansräkning (`ABL 25 kap. 18 §`), inte på utebliven styrelseregistrering.
- **Enda åtgärd:** vidarebefordra brevet till konkursförvaltaren för bekräftelse. Registrera inte ny styrelse, betala inget.
- **Varför "saknar behörig styrelse" triggas:** om en av två ledamöter avgått står den kvarvarande som ensam ledamot utan suppleant = inte behörig styrelse enligt `ABL 8 kap. 3 §`. Styrelsen som organ upplöses dock inte av konkursen.

(WLBS AB 559217-4196, konkurs sept 2024, förvaltare 7wise; lawyer 2026-07-08)

## Rådighet över konkursboets egendom - moderbolag får inte omorganisera dotterbolags handlingar/data

När ett helägt dotterbolag är i konkurs: moderbolaget äger **aktierna**, inte dotterbolagets tillgångar/handlingar/data. Vid konkursbeslutet förlorar gäldenärsbolaget rådigheten över egendom som hör till boet (`Konkurslagen (1987:672) 3 kap. 1 §`); rättshandlingar av gäldenären gäller inte mot boet (`KL 3 kap. 2 §`); boet förvaltas och företräds av konkursförvaltaren (`KL 7 kap.`); grunddefinitionen i `KL 1 kap. 1 §`.

- **Digital omorganisation räknas som förfogande.** Att flytta, döpa om, dela om eller radera filer/mappar/behörigheter/backend-poster som utgör boets egendom är att förfoga över boets egendom - får inte göras av moder utan förvaltarens skriftliga medgivande. "Bara städa i Drive" är inte neutralt: det kan förändra räkenskapsmaterial och se ut som inblandning i boet, särskilt om moder/koncernbolag själva är närstående borgenärer.
- **Presumtion:** allt dotterbolags-genererat innehåll presumeras vara boets egendom tills förvaltaren säger annat. Moderns trygga zon = moderns **egna** handlingar om konkursen (egna styrelseprotokoll, egna avtalskopior, egen borgenärsbevakning). Ett tomt, märkt Drive-skal för dotterbolaget är moderns egen metadata och är OK - estate-innehåll flyttas inte in.
- **Praxis-mönster (från AP:s egna konkurser):** förvaltare ber uttryckligen om bekräftelse att koncernen "inte gör anspråk på egendomen" innan boet säljer (Windswept, WSA jul 2024); flytt av backend-registreringar mellan koncernbolag kräver förvaltarens "ingen erinran" och boet förbehåller sig rätten att återkomma (WLBS→APDS Sir Whoopass, 7wise okt 2024). Fråga alltid, få skriftligt.
- **Bokföringsplikten ligger kvar hos gäldenärsbolaget, inte hos moder.** Moder har ingen statutär arkiveringsplikt för dotterbolagets böcker, men får inte förändra/förstöra dotterbolagets räkenskapsmaterial den råkar inneha - det är boets + potentiellt bevismaterial i bevaknings-/återvinningsprocessen (`BFL 7 kap. 2 §`, 7 års bevarande).

(AP-koncernens Drive-migrering, db-256; APDS 559320-7466 förvaltare Nils Åberg/Carler K 4429-25, WLBS 559217-4196 förvaltare Petter Vaeren/7wise K 16834-24; lawyer 2026-07-10)

## Ingen allmän plikt att ansöka om konkurs vid obestånd

Vanlig klientmissuppfattning: att en styrelseledamot *måste* ansöka om konkurs så snart bolaget är på obestånd. Sverige har **ingen sådan "duty to file"**. Ledamotens faktiska plikter är tre:

1. **ABL 25:13-18 kontrollbalansräkning** — utlöses av *kapitalbrist* (EK < halva registrerade aktiekapitalet), inte obestånd som sådant. Genast KBR + revisorsgranskning + första kontrollstämma (25:15) + rådrum + andra kontrollstämma (25:16), annars likvidationsansökan (25:17). Försummelse -> **personligt medansvar** för förpliktelser under försummelsetiden (25:18). En bokförd skuld som slår EK under halva aktiekapitalet utlöser plikten även om kassan för stunden räcker.
2. **Borgenärsskydd vid insolvens** — inte ådra nya oförmögna skulder, inte gynna enskild borgenär (BrB 11 kap. oredlighet/otillbörlighet mot borgenärer; återvinning KonkL 4 kap.).
3. **SFL 59 företrädaransvar för skatt/moms** — här är konkurs-/rekonstruktionsansökan ("verksamma åtgärder senast på förfallodagen") ett sätt att *kapa* ansvaret, men rådrum (Prop. 2025/26:52, i kraft 1 juli 2026) är ett renare alternativ. Se `wiki/legal/sv_tax.md`.

**Praktisk konsekvens:** när en enda identifierbar skuld gör bolaget insolvent (t.ex. oredovisad moms) är förstahandsstrategin att attackera den skulden vid källan (legitim kreditering, eller ägartillskott/lån som finansierar bort den) i stället för konkurs. Konkurs raderar inte upplupet företrädaransvar (bedöms per förfallodagen) och öppnar närstående-återvinning (KonkL 4:3/4:5) — ofta klientens värsta utgång. (Runatyr, run-012, lawyer 2026-07-13.)

## Preskription/talefrister — styrelseansvar, värdeöverföringar, återvinning

(Lawyer 2026-07-17, APDS/WLBS-ärendena. Verifierade mot lagtext/sekundärkällor per samma datum; exakta NJA-nummer markerade som osäkra ska verifieras före åberopande.)

| Grund | Frist | Startpunkt | Vem väcker talan |
|---|---|---|---|
| **ABL 25:18** medansvar (underlåten KBR) | **3 år från förpliktelsens uppkomst**, dock får talan alltid väckas inom **1 år från den dag förpliktelsen senast skulle ha fullgjorts** (`ABL 25:20 a`, SFS 2013:762). Preklusionsfrist — kan inte avbrytas med krav; ansvaret upphör definitivt. Accessoriskt: preskriberas bolagets skuld faller medansvaret (HD-praxis dec 2019) | Per förpliktelse. Omfattar ENDAST förpliktelser som uppkommer under ansvarsperioden (underlåtenhetens inträde — KBR-plikt + kort upprättandetid, ofta 1–2 mån — till rättelse enligt `25:20` eller konkurs). Äldre skulder träffas aldrig | Varje **enskild borgenär** vars fordran uppkom i fönstret; inte konkursboet kollektivt |
| **ABL 29:1** skadestånd, talan **för bolagets räkning** | **5 år** från utgången av det räkenskapsår då beslutet/åtgärden vidtogs (`ABL 29:13`); ettårsfristen i `29:10` kopplas till framlagd ÅR + ansvarsfrihet; konkursbo får föra talan trots ansvarsfrihet (`29:12`); brottsgrundad talan undantagen | Räkenskapsårets utgång | Bolaget, minoritet (`29:7`), konkursboet |
| **ABL 29:1** borgenärs/tredje mans **egen** talan | Ingen ABL-frist (29:13 avser talan för bolagets räkning) → allmän preskription **10 år** (`PreskL 2 §`). Kräver överträdelse av ABL/ÅRL/bolagsordning + skada + kausalitet — hög tröskel. Gränsdragningen delvis doktrin | Skadegörande handlingen | Enskild borgenär/aktieägare |
| **ABL 17:6** återbäring + **17:7** bristtäckning | Ingen särskild frist i 17 kap → **10 år** (`PreskL 2 §`) | Värdeöverföringen | Bolaget/konkursboet |
| **KL 4:5** otillbörlighetsåtervinning | Materiellt: 5 år före fristdagen; mot **närstående ingen bakre tidsgräns** (`KL 4:5` 1 st sista ledet; närståendekrets `4:3`; kunskapspresumtion mot närstående `4:5` 2 st) | Fristdag = konkursansökans dag (`KL 4:2`) | Konkursboet; enskild borgenär om förvaltaren avstår (`4:19` 2 st) |
| **KL 4:10** betalning av skuld | 3 mån före fristdagen; mot **närstående 2 år** (om inte solvens visas). Försvar: sen betalning i pengar av förfallen skuld är varken förtida eller osedvanlig; ordinär betalning undantas | Fristdag | Samma |
| **Talefrist all återvinning** | **`KL 4:20` 1 st: talan inom 1 år från konkursbeslutet**, alt. 6 mån från det att anledningen blev känd för boet (specialfall fast egendom/bodelning). **`4:20` 2 st: INGEN frist** när återvinning görs gällande genom **anmärkning mot bevakning eller invändning** mot krav mot boet | Konkursbeslutet resp. kännedom | Konkursboet |

**Praktiska yttre gränser:** förvaltarens mandat dör när boet avslutas, men anspråk som väckts eller **överlåtits** före avslut drivs vidare av förvärvaren inom samma frister; boets återvinningstalerätt enligt 4:20 1 st förlängs inte av överlåtelse. Efterutdelning (`KL 11:19-21`) väcker liv i boet för nya tillgångar men skapar inga nya talefrister. 25:18- och borgenärs 29:1-anspråk tillhör borgenärerna och överlever boavslutet inom sina egna frister.

**Fallgropar:** (1) "KL 4:5 har ingen tidsgräns mot närstående" avser bara den materiella bakåträckvidden — utan stämning inom 4:20-fristen återstår bara den defensiva anmärkningsvägen. (2) 25:18 träffar aldrig fordringar som uppkom före ansvarsperioden — kontrollera alltid NÄR borgenärens fordran uppkom innan hot om personligt ansvar tas på allvar; rättegångskostnader uppkommer dock successivt under processen (NJA 2020 s. 526; uppkomstprincipen NJA 2019 s. 941, verifierad 2026-08-05). (3) 25:20 a är preklusion, inte preskription — inga avbrott.

Tillämpning på APDS/WLBS-ärendena: `aurora_punks/drafts/lawyer_preskription_och_czp_ap_2026-07-17.md`.

## Medansvarsperiodens början och slut (ABL 25:18-20 a) — verifierat mot lagtext + HD-praxis 2026-08-05

**Lagtext (lagen.nu, konsoliderad lydelse per 2026-08-05):**

1. **25:18 1 st:** solidariskt ansvar för styrelsen för "de förpliktelser som uppkommer för bolaget under den tid som underlåtenheten består" (underlåten KBR-upprättning/granskning, underlåten första kontrollstämma, eller underlåten likvidationsansökan). **3 st:** culpabefrielse för den som "visar att han eller hon inte har varit försumlig" — omvänd bevisbörda. **4 st:** vid 13 § 1-fall gäller ansvaret bara om EK verkligen understeg halva aktiekapitalet när KBR-plikten uppkom, och inte om EK steg över gränsen **innan KBR:n senast skulle vara upprättad** — dvs. snabb faktisk läkning (inom upprättandefristen, veckor till någon månad) friar, senare läkning gör det inte per lagtexten.
2. **25:20 (ansvarsperiodens slut), uttömmande lista:** (a) likvidationsansökan enligt 17 § 2 st, (b) **revisorsgranskad KBR som utvisar att EK uppgår till HELA det registrerade aktiekapitalet, framlagd på bolagsstämma**, eller (c) likvidationsbeslut av stämma/Bolagsverket/domstol.
3. **HD-praxis:** **NJA 2018 s. 602** — medansvarsperioden avslutas när bolaget försätts i konkurs. **NJA 2018 s. 1038** — företagsrekonstruktion avslutar den INTE. **NJA 2019 s. 941** — förpliktelsens uppkomsttidpunkt bestäms lika för 18 § (ansvarstiden) och 20 a § (preklusionen), efter de väsentliga faktiska omständigheterna; en förlikning som bara bekräftar en äldre förpliktelse skapar ingen ny. **NJA 2014 s. 948** — borgenär som hade **vetskap** om underlåtenheten och inte förbehöll sig medansvaret kan inte kräva ledamoten (viktigt mot närstående/informerade borgenärer). **NJA 2014 s. 892** — ledamot som avgår under perioden. **NJA 2020 s. 526** — rättegångskostnadsansvar uppkommer löpande.
4. **Öppen fråga utan HD-svar:** om en ansvarsperiod som börjat löpa bryts av **faktisk** EK-läkning ovanför gränsen (utan granskad KBR på stämma). Lagtexten talar emot (25:20 uttömmande; 25:18 4 st friar bara snabb läkning), men culpabefrielsen i 25:18 3 st ger ett reellt argument för förpliktelser som uppkom medan kapitalet faktiskt var återställt. Behandla som oprövat; advokatfråga i skarpt läge. (APDS: EK läkt feb 2025 genom intäktsfört skadestånd, ny brist juni/juli 2025, ingen KBR någonsin — bägge linjerna är körbara för en borgenär respektive för styrelsen.)
5. **Uppkomsttidpunkt för en ÅTERVINNINGSFORDRAN vid 25:18-tillämpning** (t.ex. konkursbos återvinningskrav mot ett annat koncernbolag): inte klarlagd i HD-praxis. Kandidater: rättshandlingarna, konkursbeslutet, eller domens konstitutiva verkan. Styr om fordran faller i ett ansvarsfönster. Oprövat; flagga alltid.

## Bevakningsförfarande enligt äldre KonkL-regler — fristkarta K 4429-25 (verifierad mot Umeå TR aktbilaga 19, 2026-06-16)

1. Övergångsregeln (SFS 2025:796, prop. 2024/25:135): har tingsrätten beslutat om bevakningsförfarande **före 2026-07-01** tillämpas äldre bestämmelser på förfarandet. K 4429-25: beslut 2026-06-16 → äldre regler, förlikningssammanträde finns kvar.
2. K 4429-25 (APDS): bevakning senast 2026-07-21; **anmärkning senast 2026-08-11** (gäller förvaltaren OCH borgenärer, och är boets fristlösa väg att göra återvinning gällande defensivt, KL 4:19-20); **förlikningssammanträde 2026-09-01 kl. 09.30** om anmärkningar framställts; beslutet ej överklagbart.
3. KL 4:20 1 st (lydelse per SFS 2025:796, verifierad 2026-08-05): återvinningstalan väcks inom **ett år från konkursbeslutet** (APDS: 2025-12-12 → 2026-12-12, helgdagsförskjutning till nästa vardag), alternativt sex månader från kännedom. Anmärknings-/invändningsvägen har ingen egen frist men styrs i praktiken av anmärkningsfristen i förfarandet.

## Vad ett konkursbo KAN och INTE KAN förlika bort (verifierat mot lagtext + KL 4:19-20, 2026-08-27)

Återkommande klientfråga vid varje uppgörelse med en förvaltare: "kan vi köpa oss fria från allt?"
Nej. Anspråken delar sig efter **vem som äger dem**, och förvaltaren kan bara efterge boets egna.

**Boets, alltså förhandlingsbart med förvaltaren:**

1. `KL 4 kap.` återvinning. Boet har exklusiv talerätt; enskild borgenär får väcka talan bara om
   förvaltaren avstår (`KL 4:19` 2 st).
2. `ABL 17:6` återbäring och `ABL 17:7` bristtäckning vid olovlig värdeöverföring. Bolagets anspråk,
   förvaltas av boet.
3. `ABL 29:1` skadestånd, **talan för bolagets räkning**. Boet får föra den även om ansvarsfrihet
   beviljats (`ABL 29:12`).

**Inte boets, alltså INTE förhandlingsbart oavsett vad klienten är beredd att betala:**

4. `ABL 25:18` medansvar vid underlåten KBR. Görs gällande av **varje enskild borgenär vars egen
   fordran uppkom i ansvarsfönstret**, inte av boet kollektivt. Överlever boavslutet inom `ABL 25:20 a`.
5. `SFL 59:13` företrädaransvar. Statens anspråk, drivs av Skatteverket i förvaltningsdomstol.
6. `ABL 29:1` borgenärs eller tredje mans **egen** talan för skada som drabbat denne direkt.

**Praktisk konsekvens för uppgörelsetext:** en slutuppgörelse med boet ska räkna upp `KL 4 kap.`,
`ABL 17 kap.` och `ABL 29 kap. för bolagets räkning` uttryckligen. Att bara skriva "anmärkningen
återkallas" eller "samtliga mellanhavanden regleras" lämnar återvinningstalan öppen. Och lova aldrig
klienten fred från 25:18 eller företrädaransvar via förvaltaren, hur generöst budet än är.

## Anmärkningsvägen är fristlös men DEFENSIV (KL 4:19-20), och det avgör vad en uppgörelse är värd

(APDS K 4429-25, anmärkning aktbil 58 mot CZP:s bevakning; lawyer 2026-08-27)

1. `KL 4:19` 1 st räknar upp tre sätt att påkalla återvinning: **(1)** talan vid allmän domstol,
   **(2)** anmärkning mot bevakning eller bestridande vid utdelningsförfarandet, **(3)** invändning
   mot annat yrkande mot boet.
2. `KL 4:20` 1 st: **ettårsfristen från konkursbeslutet gäller bara väg (1)** och borgenärstalan
   enligt 19 § 2 st, som väcks genom stämning vid konkursdomstolen. Väg (2) och (3) är **fristlösa**
   (`4:20` 2 st). Därför framställs anmärkningar ofta på anmärkningsfristens sista dag: det är boets
   billiga, fristlösa väg in.
3. **Men väg (2) är defensiv.** Bevakningsförfarandets föremål är borgenärens rätt till utdelning.
   Utfallet är att bevakningen fastställs eller sätts ned, inte att borgenären åläggs betala. En
   förvaltare som vill ha kontanter tillbaka måste stämma inom `4:20` 1 st. Kontrollera alltid
   förvaltarens egen formulering: skriver han att återvinningsfordran "ska avräknas från
   utdelningsfordran" har han valt det defensiva spåret.
4. **Värderingskonsekvensen, som klienten nästan alltid missar.** Är boet insolvent i förhållande
   till bevakat belopp (konkurskostnader går före) är borgenärens bevakning värd noll. Då kostar
   anmärkningen ingenting att förlora, och den enda reella exponeringen är stämningsfristen. **Räkna
   ut boets faktiska utdelningsprocent innan du rekommenderar ett förlikningsbud**, annars betalar
   klienten för att skydda något värdelöst och lämnar det farliga öppet.
5. Följd för uppgörelsen: den ska formuleras som avstående från **återvinningsanspråket**, inte som
   återkallande av anmärkningen. Annars ger klienten upp bevakningen och står kvar med
   stämningsrisken till fristens utgång.

## ABL 21 kap. låneförbud — närståendekretsen i korsägda strukturer

`ABL 21:1` förbjuder penninglån till bl.a. (p 1) den som äger aktier i bolaget **eller i annat bolag i samma koncern**, och (p 5) juridisk person över vilken sådan person har bestämmande inflytande. Koncernundantaget i `21:2` kräver äkta koncern enligt `ABL 1:11` (majoritetskontroll i moder-dotter-kedja). **Ett holdingbolag med minoritetspost i moderbolaget (t.ex. 30 %) är INTE i samma koncern** — koncernundantaget är otillämpligt; kvar finns bara det kommersiella undantaget (lån för gäldenärens rörelse av affärsmässiga skäl). Sanktioner: ogiltighet/återbetalning + straff (`ABL 30:1`), åtalspreskription 2 år. (APDS→CZP-utlåningen 2025; lawyer 2026-08-05.)

## Robert's positions

- **Intercompany bridge structures:** prefer paying-agent over kommissionärsbolag or sub-license when the use case is a short-duration VAT/F-skatt registration gap. (k2c-003, 2026-05-04)
- **Self-dealing on AP↔CZP:** AP signs by Mattias + Andreea; CZP signs by Robert; Robert abstains on AP-side vote. (CorpBot 2026-04-22 + lawyer 2026-05-04)
- **Personal guarantees from VD-konsult role:** no automatic recourse against CZP; default to private kapitalförlustavdrag (IL 54:6) unless documented indemnification or board resolution exists. (APDS-konkursen, 2026-05-04)

## Open questions

- Confirm RF master section 3.1 "affiliated companies or subcontractors" wording exactly matches what the Apr 22 CorpBot read recorded — fetch live RF draft 1yFxHLrAlNQg_YjQGnIgrGqr7i0lwYS6W and grep when GDrive MCP is back in service. (k2c-003, 2026-05-04)
