# GDPA + PS Partners-onboarding för CZP

**Skapad 2026-08-27. Reviderad 2026-08-28 (CorpBot, 4am-svep). Ärende `apb-057`. Gatar `apb-015`
(title transfer) helt.**
Bakgrund och transferplan: `ps_title_transfer_APDS_to_CZP_2026-07-24.md` avsnitt 12.

**Vad som ändrades 2026-08-28:** avsnitt 7 gick från en hänvisning till ett färdigt datapaket sedan
förra entitetsbytets ifyllda SIE-blankett hittades i Drive, avsnitt 9 rollfråga omformulerad från
Team Admin till Global Account Admin efter Sonys rolländring i augusti, två nya förberedande steg
med extern ledtid i avsnitt 8, och två nya bilagor. Ingenting skickat, ingenting registrerat.

---

## 1. Varför det här är ett eget ärende

Sonys `/api/v1/partners` returnerar exakt en partner: APDS. **CZP finns inte i Sonys system
alls.** Sony kan inte byta Concept Lead eller Publisher Store Name till en entitet som inte
existerar, och tremånadersledtiden på transfern börjar först när de kan agera. Onboardingen av CZP
är alltså inte ett förberedande steg vid sidan av transfern, den är transferns kritiska väg.

## 2. Var ansökan faktiskt ligger (verifierat 2026-08-27)

- **Ansökningsformuläret: `https://register.playstation.net/`** (nås via "Join Us Now" på
  partners.playstation.net). Första steget är en väljare: *"Where is your company or institution
  registered?"*. Välj **Sweden**.
- **Befintlig partnerinloggning: `https://partners.playstation.net/sign-in`.** Roberts session
  (`Robert@aurorapunks.com`) är redan autentiserad där, verifierat samma dag.
- Sony beskriver processen i två steg: **(1)** ansökan online plus företagsregistrering,
  **(2)** godkänna avtalet, alltså GDPA-klicket. Det finns inga uppläggningsavgifter.
- GDPA:n godkänns genom att klicka ACCEPT i portalen. Texten kräver att den som accepterar
  **är behörig att binda bolaget**. Se punkt 5 om signaturbehörigheten.

## 3. Den enda strategiska frågan, och den måste avgöras före inskickning

Går CZP in genom den generiska "Join Us Now"-tratten blir det **en ny, fristående partner utan
historik**. Konsekvenser: ny partnervetting, ingen koppling till APDS partnerId `10006419` /
SPID `UB1314`, och risk att ärendet hamnar hos fel regionsteam. Då har vi två orelaterade
partnerposter och transfern har inte flyttat en millimeter.

**Ansökan måste därför bära successionssignalen från början**, inte bara transferärendet. Konkret:
1. Skicka ansökan på `register.playstation.net`.
2. **Samma dag**, öppna ett Help Center-ärende som refererar ansökan OCH `CS0157316`, kategori
   `Partner accounts and app access` -> `Mergers and acquisitions`. Färdig text i avsnitt 10.
3. Ställ strukturfrågan explicit till Sony i stället för att gissa: **ska CZP bli ett eget nytt
   company, eller en ny organization under befintligt company `38001`?** Company 38001 rymmer idag
   WLBS (org 40816), APDS (org 44810) och Sir Whoppass (org 44823). En org under 38001 skulle ligga
   nära katalogen, men 38001 är två konkursbons company och vi har ingen bekräftad Team Admin där.
   Det här är Sonys beslut att fatta, inte vårt, och fel gissning kostar en omstart.

## 4. Datapaket för formuläret

Allt nedan är verifierat mot registreringsbeviset (Bolagsverket ärende 415999/2026, 2026-07-13)
respektive Steam-onboardingen. Fyll formuläret ur den här listan, hitta inte på fältvärden.

| Fält | Värde |
|---|---|
| Legal company name | **Creation Zero Point Holding AB** |
| Trading as / dba | Aurora Punks |
| Country of registration | Sweden |
| Company reg. no. | **559182-7471** |
| VAT | **SE559182747101** |
| Postadress | c/o Robert Bäckström, Bondegatan 31, 116 33 Stockholm, Sweden |
| Säte | Stockholms län, Stockholms kommun |
| Aktiekapital | 50 000 SEK / 500 aktier |
| Räkenskapsår | 0101-1231 |
| Revisor | Ingen |
| Primär kontakt | Robert Bäckström, robert@aurorapunks.com, +46 70 441 6979 |
| Roll | Styrelseledamot (ensam), tecknar firman som styrelsen |

**Bank, för payee-registreringen (eget SIE-ärende, se avsnitt 7):**
SEB · IBAN `SE9650000000052661032177` · BIC `ESSESESS`.

**E-postvalet, en sak att inte slarva med.** CZP:s registrerade e-post hos Bolagsverket är
`johanrobert.backstrom@gmail.com`, men Sony-identiteten och DevNet-inloggningen är
`Robert@aurorapunks.com`. **Använd `robert@aurorapunks.com` mot Sony** så kontinuiteten mot
befintlig access bevaras. Ska ett registerutdrag jämföras kommer adresserna att skilja sig, och det
är väntat, inte ett fel.

**Portfölj att ange**, alltså det CZP ska publicera, hämtat ur transferomfattningen:
Block'Em! (concept `10012216`), Chenso Club (`10005000`), 1993 Shenandoah (`10002510`, NP Title ID
`CUSA27230_00`). Exkluderad: "DO NOT USE" (`10006927`, suspended).

## 5. Signaturbehörighet, GDPA:ns egen spärr

GDPA:n: *"THE PERSON ACCEPTING THIS AGREEMENT ON DEVELOPER'S OR PUBLISHER'S BEHALF REPRESENTS THAT
HE OR SHE IS AUTHORIZED TO BIND DEVELOPER OR PUBLISHER."*

CZP:s firmateckning är **"Firman tecknas av styrelsen"**. Robert Bäckström (760209-0230) är
**ensam ordinarie ledamot**, Bo Ragnar Enmark (510818-1198) är suppleant. Det finns **ingen särskild
firmatecknare**. Robert tecknar alltså firman *i egenskap av styrelsen*, vilket uppfyller kravet.
**Skriv titeln som "styrelseledamot" / "Board Member", aldrig "Director" eller "authorised
signatory"**, eftersom en granskare som jämför mot registreringsbeviset annars hittar en titel som
inte finns där. Har Sony ett fält för styrkande av behörighet: bifoga registreringsbeviset.

## 6. Formulering, den enda meningen som får kosta

Bilaga 2 till rörelseöverlåtelseavtalet anger **AP AB** som IP-ägare till både Block'Em! och Chenso
Club. Skriv därför genomgående att CZP **förvärvat rörelsen med tillhörande publicerings- och
distributionsrättigheter**. Skriv aldrig att CZP äger IP:t. Sony ska flytta ett konto och en
publiceringsposition, och det är exakt vad handlingarna belägger. Påstår vi mer än handlingarna
bär, faller ärendet på beviskravet.

**Kedjan, som den ska återges:**

    White Lines Black Spaces AB
      -> Aurora Punks Development Services AB (559320-7466)
        -> Bright Gambit AB (559351-6536)
          -> Creation Zero Point Holding AB (559182-7471)

**Handlingar, skicka båda och i den ordningen:**
1. `Rörelseöverlåtelseavtal` APDS konkursbo -> Bright Gambit. Scrive `09222115557567493495`,
   2026-01-18, BankID Nils Åberg (förvaltare) + Tim Browne. Drive
   `10ZN-_9YckcvVJDBGV-5szGsAlaI_f-SQ`. **Bär titelnamnen** i bilaga 2.
2. `Asset_Transfer_Agreement_BrightGambit_CreationZeroPoint`. DocuSign, 2026-02-16, Andreea Chifu +
   Robert Bäckström. Drive `1nYJ_Vp7rnxcrJrWqMQ-43lHPKwLmpsBz`. **Bär CZP som part.**

Ingen av dem ensam uppfyller Sonys krav 1 (titlar + datum + båda parters underskrifter) för CZP.
Tillsammans gör de det.

## 7. Bankregistreringen körs parallellt, inte efter

Payee-bytet tas **uttryckligen inte** emot inuti transferärendet. Det är ett eget SIE-ärende och
har egen ledtid. Starta det samma vecka som ansökan, annars blir det den nya flaskhalsen när
transfern väl går igenom.

**Uppdaterat 2026-08-28: instrumentet är identifierat och vi har ett ifyllt exemplar från förra
entitetsbytet.** Det här är inte ett formlöst supportärende, det är en namngiven blankett:

**`SIE Company Setup Form`** (SIE:s egen version 20210315). Tre avsnitt, där avsnitt 1 fylls av
SIE internt och avsnitt 2 och 3 av oss. Exemplaret från förra gången ligger i Drive som
`SIE_Company_Setup_Form_WLBS.pdf` (`1YX65RcmX2rZ2dBux7nrKeRaNTCQqhWa9`), DocuSign-signerat.
Blank mall: `SIE Company Setup Form-New.pdf` (`1sz4VeqL7cbC3SwsPpk3Ku1DTg9TLl3pk`).

**Det viktiga fyndet i det gamla exemplaret: blanketten har ett eget fält för att skilja avtalspart
från betalningsmottagare.** WLBS-formuläret angav `Company/Indiv. Name: White Lines Black Spaces AB`
men `Payee Name (if different from above): Aurora Punks Development Services AB`, med APDS eget
SEB-konto. Förra entitetsbytet på Sony gjordes alltså genom **Payee Name-fältet**, inte genom ett
nytt avtal och inte genom en kontoflytt. Det är den billiga vägen och den har redan gått igenom hos
dem en gång. Färdigt datapaket för CZP i **bilaga A**.

**Fyra saker är obligatoriska vid kontoändring, och en av dem har egen ledtid hos SEB:**

1. Telefonnummer till en ekonomikontakt som SIE ringer upp för att verifiera kontouppgifterna.
2. Nyligen signerad W-8BEN-E. Se **bilaga B**.
3. Uppdaterad Company Setup Form.
4. Utanför USA och Kanada: **kontobekräftelse på bankens brevpapper**. Det är en beställning hos
   SEB, inte något vi kan skriva själva, och det är den enda posten i hela avsnitt 7 med extern
   ledtid. **Beställ den först, inte sist.**

**Två villkor som styr planeringen:** SIE:s betalningsvillkor är **netto 60**, och **en blankett per
valuta**. WLBS körde USD. Kör CZP samma valuta så slipper vi två parallella uppsättningar.

**Namnmatchningen är den som tystar utbetalningar om den slarvas.** W-8BEN-E ska matcha Payee Name,
och Payee Name ska matcha kontohavaren hos SEB. Kontohavaren är verifierad som
`CREATION ZERO POINT HOLDING AB` (SEB Företagskonto 5266 10 321 77). Skriv därför **Creation Zero
Point Holding AB** som Payee Name, inte "Aurora Punks". Handelsnamnet hör hemma i DBA-fältet och
ingen annanstans. Det här är exakt den avvikelse som stoppade Microsofts royaltyutbetalningar i fem
månader utan en enda avvisningsnotis (`apb-055`), och den kostar ingenting att undvika i förväg.

## 8. Ordning, med ägare

| # | Steg | Vem | Blockerar |
|---|---|---|---|
| 0a | Beställ kontobekräftelse på SEB:s brevpapper för 5266 10 321 77 | Robert | 3 |
| 0b | Bestäm CZP:s chapter 4-status på W-8BEN-E, se bilaga B | Ameer / revisor | 3 |
| 1 | Ansökan på `register.playstation.net`, Sweden | Robert | allt nedan |
| 2 | Help Center-ärende med successionsframing + CS0157316 + strukturfrågan | Robert | 4 |
| 3 | SIE Company Setup Form + W-8BEN-E + kontobekräftelse, eget ärende | Robert | payee-bytet, ej 4 |
| 4 | GDPA-klicket när Sony öppnar det | Robert (som styrelsen) | apb-015 |
| 5 | Öppna om CS0157316, bifoga båda avtalen | Robert | transfern |

**Steg 0a och 0b är nya per 2026-08-28** och ligger före steg 3 därför att de är de enda posterna i
hela ärendet med ledtid hos någon annan än oss. De blockerar inte ansökan, så kör dem parallellt med
steg 1 och 2.

**Undvik två fönster i Content Pipeline:** planerat underhåll **1 september 12:00 PDT** och
**29 september 11:00 PDT**, upp till tre timmar vardera. Rör inget i `publish.playstation.net` då.

## 9. Öppet

- **Rollfrågan är omformulerad per 2026-08-28: det vi behöver heta är Global Account Admin, inte
  Team Admin.** Sony ändrade rollmodellen under augusti och beskrev den i partnerutskicken 26 och
  27 augusti. **GAA är den överordnade rollen**, Team Admin är en delegerad roll som **en GAA
  konfigurerar**, och Team Admin kan numera provisionera appar och roller åt sina användare bara
  i den mån en GAA satt upp det. Konsekvensen för oss är tvådelad. Blir svaret på strukturfrågan
  "eget nytt company" behöver **CZP en egen GAA från dag ett**, och det ska vara Robert. Blir svaret
  "ny org under 38001" behöver vi **en GAA på 38001**, inte en Team Admin, och den personen är
  fortfarande oidentifierad. Kandidater, obekräftade: Johannes Fornaeus, Hektor Andreasson.
- **DevNet-användarhantering flyttade in i PlayStation Partners 26 augusti 2026.** Att skapa
  DevNet-användare, styra DevNet-siteåtkomst och sätta DevNet-roller görs nu från
  `partners.playstation.net/hub` och kräver GAA eller Team Admin med rätt behörighet. Kvar i DevNet
  ligger bara preferenser, krypteringsnycklar och site-specifika användarinställningar. Det träffar
  DevNet-halvan av själva transfern (`apb-015`), där mottagande partner ska läggas till som
  Collaborator med Owner-behörighet: den åtgärden går inte längre att göra som Company Admin i
  DevNet utan rätt roll i Partners. Värt att nämna i Help Center-ärendet så vi inte upptäcker det
  när transfern annars vore klar.
- **Org 44823 "Sir Whoppass"** ligger kvar under company 38001 trots att titeln gått till Atomic
  Elbow. Inte i vägen för det här ärendet, men bör städas i samma svep som transfern.
- NP Title ID för Block'Em! och Chenso Club är fortfarande inte utdragna. Sony tillåter uttryckligen
  komplettering efter att ärendet öppnats, så det blockerar inte ansökan.

## 10. Utkast: Help Center-ärendet som ska följa ansökan samma dag

Kategori `Partner accounts and app access` -> `Mergers and acquisitions`. Ämne: **"New partner
registration for successor entity - Creation Zero Point Holding AB, ref CS0157316"**.

---

Hi,

I have today submitted a partner registration for Creation Zero Point Holding AB through
register.playstation.net. I am raising this case at the same time so the application is not
processed as an unrelated new studio, because it is not one.

Creation Zero Point Holding AB is the successor to your existing partner Aurora Punks Development
Services AB (partner ID 10006419, SPID UB1314). Aurora Punks Development Services AB went into
bankruptcy on 12 December 2025. The business, together with the associated publishing and
distribution rights, was acquired out of the estate and now sits with Creation Zero Point Holding
AB, which trades as Aurora Punks.

Chain of title:

    White Lines Black Spaces AB
      -> Aurora Punks Development Services AB (559320-7466)
        -> Bright Gambit AB (559351-6536)
          -> Creation Zero Point Holding AB (559182-7471)

Two documents evidence it, and they work together rather than separately. The first, a business
transfer agreement between the Aurora Punks Development Services estate and Bright Gambit AB dated
18 January 2026, lists the titles in its schedule 2 and is signed by the appointed trustee and by
Bright Gambit. The second, an asset transfer agreement between Bright Gambit AB and Creation Zero
Point Holding AB dated 16 February 2026, brings the business to its current holder and is signed by
both parties. I will attach both as soon as you confirm where you want them.

This relates to case CS0157316, which was raised earlier on the same subject and auto-closed while
we were assembling this evidence.

Three things I would like your guidance on before anything is set up the wrong way round:

1. Should Creation Zero Point Holding AB be registered as its own company in your system, or as a
   new organization under the existing company 38001, which today holds White Lines Black Spaces AB
   (org 40816), Aurora Punks Development Services AB (org 44810) and Sir Whoppass (org 44823)?
   I would rather you tell me than guess, since undoing it later costs us both a cycle.

2. Whichever of those you choose, who ends up holding Global Account Admin for Creation Zero Point
   Holding AB, and what do you need from me to establish it? I ask because of the role changes you
   announced on 26 and 27 August: DevNet user management now runs through PlayStation Partners and
   needs GAA or a Team Admin that a GAA has configured. If the answer to question 1 is a new
   organization under company 38001, then this depends on a GAA on that company, and 38001 belongs
   to two bankruptcy estates. I would rather surface that now than when everything else is ready.

3. Once Creation Zero Point Holding AB exists as a partner, can it be added as a collaborating
   partner on the three concepts in scope, so the title transfer can proceed? Those are Block'Em!
   (concept 10012216), Chenso Club (10005000) and 1993 Shenandoah (10002510, NP Title ID
   CUSA27230_00). Concept 10006927 is out of scope and should stay where it is.

To be precise about what is being claimed: Creation Zero Point Holding AB acquired the business
with the associated publishing and distribution rights. It is not claiming ownership of the
underlying IP. What we are asking you to move is an account and a publishing position.

The financial setup for the new entity goes in as a separate case, as your guidelines require. I am
raising that in parallel rather than in this one, with a completed SIE Company Setup Form, a signed
W-8BEN-E and bank instructions on our bank's letterhead, so it does not become the bottleneck once
this side is agreed.

Happy to take this on a call if that is quicker.

Best regards,
Robert Bäckström
Board Member, Creation Zero Point Holding AB
robert@aurorapunks.com
+46 70 441 6979

---

## Bilaga A. SIE Company Setup Form, färdigt datapaket för CZP

Mall: `SIE Company Setup Form-New.pdf`, Drive `1sz4VeqL7cbC3SwsPpk3Ku1DTg9TLl3pk`.
Förlaga: `SIE_Company_Setup_Form_WLBS.pdf`, Drive `1YX65RcmX2rZ2dBux7nrKeRaNTCQqhWa9`.
Avsnitt 1 fyller SIE. Vi fyller avsnitt 2 och 3.

**Avsnitt 2, Company Information**

| Fält | Värde | Not |
|---|---|---|
| Company Is | New | |
| Company/Indiv. Name | Creation Zero Point Holding AB | juridiskt namn, exakt |
| DBA (doing business as) | Aurora Punks | handelsnamnet hör hemma här och ingen annanstans |
| Address | c/o Robert Bäckström, Bondegatan 31 | |
| City / Postal Code / Country | Stockholm / 116 33 / Sweden | |
| State/Province/Country of Incorporation | Sweden | |
| Company Website | https://www.aurorapunks.com/ | samma som förra gången |
| No. of W-2 Employees | 0 | |
| Main company contact | Robert Bäckström | |
| Phone | +46 70 441 6979 | |
| Email | robert@aurorapunks.com | |

**Avsnitt 3, Financial Information**

| Fält | Värde | Not |
|---|---|---|
| Type of Business | Foreign Corporation | som WLBS |
| Tax ID Number | SE559182747101 | **momsnumret, inte org.nr**. WLBS angav sitt momsnummer i det här fältet |
| Is 1099/1042 Required? | Not required | som WLBS |
| Services to be Performed | Outside U.S. | |
| Payee Name | Creation Zero Point Holding AB | måste matcha W-8BEN-E och kontohavaren hos SEB |
| Payee Address | c/o Robert Bäckström, Bondegatan 31, 116 33 Stockholm, Sweden | |
| Email for Invoice Inquiries | robert@aurorapunks.com | `finance@aurorapunks.com` användes förra gången, kontrollera att den lådan fortfarande bevakas innan den anges |
| Email for Purchase Orders | samma som ovan | |
| Payment Method | Wire Transfer (non-U.S.) | |
| Currency | USD | en blankett per valuta, kör samma som WLBS |
| Bank Name / Address | SEB, 106 40 Stockholm, Sweden | |
| SWIFT Code | ESSESESS | |
| Beneficiary Name (Account Name) | Creation Zero Point Holding AB | verifierat som kontohavare på 5266 10 321 77 |
| Account No. | 5266 10 321 77 | |
| IBAN | SE9650000000052661032177 | |

**Electronic Payments, signaturraden.** Robert Bäckström, och titeln ska stå som **Board Member**.
WLBS-blanketten signerades "CEO", vilket var korrekt då. CZP har ingen VD, firman tecknas av
styrelsen och Robert är ensam ordinarie ledamot. Skriv aldrig CEO eller Director här, av samma skäl
som i avsnitt 5.

**Bifoga:** signerad W-8BEN-E enligt bilaga B, och kontobekräftelse på SEB:s brevpapper.

---

## Bilaga B. W-8BEN-E, vad APDS angav och vad som ändras för CZP

Förlaga: `Form W8BENE v Oct 2021_APDS-signed.pdf`, Drive `1H9_qrn7L7w1no0Gtwnzp0Kam3uFHzx4N`,
signerad av Robert 2025-07-17. Blanketten är i allt väsentligt en transkribering, med ett undantag
som ska avgöras av revisorn.

| Rad | APDS angav | CZP ska ange |
|---|---|---|
| 1, Name of organization | Aurora Punks Development Services AB | Creation Zero Point Holding AB |
| 2, Country of incorporation | Sweden | Sweden |
| 4, Chapter 3 Status | **Corporation** | Corporation |
| 5, Chapter 4 Status (FATCA) | se nedan | **öppen fråga, se nedan** |
| 6, Permanent residence address | Timmermansgatan 43, 118 55 Stockholm, Sweden | c/o Robert Bäckström, Bondegatan 31, 116 33 Stockholm, Sweden |
| 9b, Foreign TIN | SE559320746601 | **SE559182747101** |
| 14a, resident of | Sweden | Sweden |
| 14b, LOB-grund | Company that meets the **ownership and base erosion test** | samma |
| 15, Special rates | Article **12 §1**, **0 %**, på **Royalties** | samma |
| Part XXX | Robert Bäckström, 2025-07-17 | Robert Bäckström, som styrelseledamot |

**Noll procent är rätt och det är värt att veta varför.** Skatteavtalet mellan USA och Sverige ger
0 % källskatt på royalty enligt artikel 12. LOB-grunden "ownership and base erosion test" håller för
CZP av samma skäl som för APDS, bolaget ägs till 100 % av en svensk skattskyldig person. Notera att
AP en gång fyllde i 30 % källskatt mot Robot Cache och fick det påpekat av motparten innan det
rättades. Fyll inte i något annat än 0 utan att veta varför.

**Den enda posten jag inte fyller i åt dig: chapter 4-statusen på rad 5.** För ett verksamhetsdrivande
spelbolag är **Active NFFE** (Part XXV) normalsvaret. CZP är ett **holdingbolag**, och om merparten
av intäkterna klassas som passiva blir svaret i stället **Passive NFFE** (Part XXVI), som dessutom
kräver ett aktivt ställningstagande i 40b eller 40c om substantiella amerikanska ägare. Skillnaden
är materiell och den ska Ameer eller revisorn avgöra, inte jag och inte Sony. Läs samtidigt av
APDS-blankettens faktiska kryss i original innan du transkriberar: den extraherade texten placerar
en markering i trakten av Part XIX och XX, vilket inte kan stämma för APDS och sannolikt är ett
extraheringsfel, men det ska bekräftas mot PDF:en och inte gissas.

---

## Bilaga C. Länkar som sparar en sökning

- Ansökan: `https://register.playstation.net/`
- Partnerinloggning: `https://partners.playstation.net/sign-in`
- Partners-hub, numera även DevNet-användarhantering: `https://partners.playstation.net/hub`
- Skapa Help Center-ärende, direktlänk:
  `https://help.playstation.net/csm?id=create_ticket&sys_id=4a2e1ee987555a10ea33a6c73cbb35a8`
- Ny dokumentationssajt, lanserad 27 augusti 2026: `https://docs.playstation.net/`
- Onboardingsidan där Sony själva samlar registrering, finansiell och skattemässig uppsättning,
  hårdvarubeställning och supportvägar:
  `https://docs.playstation.net/r/en-us/playstation-partners-onboarding/partner_onboarding`
- Rollbeskrivningarna GAA och Team Admin:
  `https://docs.playstation.net/r/en-us/playstation-partners-getting-started/accounts_adminroles`

Dokumentationssajten ligger bakom samma Okta-inloggning som portalen. Den gick inte att läsa
obevakat den 28 augusti, se ärendeloggen. **Läs onboardingsidan innan du fyller i ansökan** och
stäm av den mot avsnitt 4 och bilaga A. Den publicerades efter att den här planen skrevs och är
Sonys egen beskrivning av samma sekvens vi har rekonstruerat.
