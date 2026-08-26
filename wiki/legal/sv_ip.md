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

## Robert's positions

- **2026-05-03 (RLR/Scen & Film):** Försökte hävda att Yasin Hillborg "inte kan hävda upphovsrätt på IP:t" — vilket missförstod vad propån yrkade (ideell rätt, ej ekonomisk). Justerades efter genomgång — strategi blev efterlevnad inom scope, inte stridsläge. Tar rak återkoppling när den är lagrum-baserad.

## Open questions

- Hur ser konkursförvaltarens (Carler/Mattsson) bedömning av IP-kedjan Runatyr→APDS→AP ut i APDS-konkursen?
- Är 2023-IP-Avtalet Runatyr→AP klanderbart givet att Yasin (50% delägare i Runatyr) inte godkände det?
