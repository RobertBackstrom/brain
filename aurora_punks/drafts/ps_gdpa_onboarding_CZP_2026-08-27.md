# GDPA + PS Partners-onboarding för CZP

**Skapad 2026-08-27. Ärende `apb-057`. Gatar `apb-015` (title transfer) helt.**
Bakgrund och transferplan: `ps_title_transfer_APDS_to_CZP_2026-07-24.md` avsnitt 12.

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
transfern väl går igenom. Uppgifter i avsnitt 4.

## 8. Ordning, med ägare

| # | Steg | Vem | Blockerar |
|---|---|---|---|
| 1 | Ansökan på `register.playstation.net`, Sweden | Robert | allt nedan |
| 2 | Help Center-ärende med successionsframing + CS0157316 + strukturfrågan | Robert | 4 |
| 3 | Bankregistrering för CZP, eget ärende | Robert | payee-bytet, ej 4 |
| 4 | GDPA-klicket när Sony öppnar det | Robert (som styrelsen) | apb-015 |
| 5 | Öppna om CS0157316, bifoga båda avtalen | Robert | transfern |

## 9. Öppet

- **Team Admin på company 38001 är fortfarande oidentifierad.** Kandidater, obekräftade: Johannes
  Fornaeus, Hektor Andreasson. Blir svaret på strukturfrågan i avsnitt 3 "ny org under 38001"
  behövs den personen, och då är det den nya blockeraren.
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

Two things I would like your guidance on before anything is set up the wrong way round:

1. Should Creation Zero Point Holding AB be registered as its own company in your system, or as a
   new organization under the existing company 38001, which today holds White Lines Black Spaces AB
   (org 40816), Aurora Punks Development Services AB (org 44810) and Sir Whoppass (org 44823)?
   I would rather you tell me than guess, since undoing it later costs us both a cycle.

2. Once Creation Zero Point Holding AB exists as a partner, can it be added as a collaborating
   partner on the three concepts in scope, so the title transfer can proceed? Those are Block'Em!
   (concept 10012216), Chenso Club (10005000) and 1993 Shenandoah (10002510, NP Title ID
   CUSA27230_00). Concept 10006927 is out of scope and should stay where it is.

To be precise about what is being claimed: Creation Zero Point Holding AB acquired the business
with the associated publishing and distribution rights. It is not claiming ownership of the
underlying IP. What we are asking you to move is an account and a publishing position.

The bank details for the new entity go in as a separate case, as your guidelines require. I will
raise that in parallel rather than in this one.

Happy to take this on a call if that is quicker.

Best regards,
Robert Bäckström
Board Member, Creation Zero Point Holding AB
robert@aurorapunks.com
+46 70 441 6979

---
