# Apple Developer: rätta entitetsunderlaget (ärende 102345613725)

**Datum:** 2026-08-03 · **Projekt:** apb / run-010 · **Konto:** Team ID `SCALFR6L25`, `qa@aurorapunks.com`
**Underlag:** `_legals/Registreringsbevis_AP_AB_559256-9718_2026-04-21.pdf` (hämtat från Bolagsverket-mailet 2026-04-21)

---

## Problemet i en mening

Apple-kontot heter **Aurora Punks AB** men det bolagsbevis som ligger hos Apple som identitetsunderlag
är **APDS:s** (559320-7466), bolaget som gick i konkurs 2025-12-12, och uppladdningen slutfördes
dessutom aldrig.

## Vad Apple har idag kontra verkligheten

| Fält | Apple har | Bolagsverket 2026-04-21 |
|---|---|---|
| Organisation | Aurora Punks AB | Aurora Punks AB (rätt) |
| Orgnr i inlämnat underlag | 559320-7466 (**APDS, i konkurs**) | 559256-9718 |
| Adress | Timmermansgatan 43, 118 55 Stockholm (privatadress) | c/o Bäckström, Bondegatan 31, 116 33 Stockholm |
| Ärendestatus | 102345613725 öppet sedan 2024-07, underlag avvisat 2024-11-01 | — |

Adressen Robert uppgav till Apple i juli 2024 är alltså inaktuell numera också: postadressen ändrades
hos Bolagsverket 2026-04-21 (ärende 232595/2026) till Bondegatan 31.

## Sekvensering: förläng FÖRST, rätta sedan

Öppna inte ett company-information-ärende medan medlemskapet ligger nere. En
company-information-ändring kan trigga en legal-authority-granskning hos Apple, och den granskningen
skulle då blockera en förlängning som tre produkter väntar på (graderingsappen, K2C, Hooja).

1. Förläng medlemskapet (999 kr, rutinärende).
2. När kontot är aktivt igen, rätta entitetsunderlaget enligt nedan.

## Firmateckningen är en fälla att känna till i förväg

Registreringsbeviset visar att **Robert inte ensam kan teckna AP AB:s firma**:

- Styrelse: Andreea-Mariana Chifu (ledamot + **VD**), Mattias Wiking (**ordförande**),
  Alexander Bergendahl, **Robert Bäckström**, Magnus Troedsson.
- Firmateckning: *firman tecknas av styrelsen; firman tecknas två i förening av ledamöterna;
  dessutom har verkställande direktören rätt att teckna firman beträffande löpande
  förvaltningsåtgärder.*

Robert är alltså styrelseledamot men varken VD eller ensam firmatecknare. En förlängning på 999 kr är
utan tvekan en löpande förvaltningsåtgärd och är oproblematisk. Men om Apple kör en **legal authority
review** i samband med entitetsrättelsen kan de fråga efter bevis på behörighet att binda bolaget, och
då räcker inte Roberts underskrift ensam. Ha en andra ledamot eller VD Chifu beredd att medsignera.

## Utkast till svar på ärende 102345613725

Skickas till `eurodev@apple.com` med ärendenumret i ämnesraden. PDF:en laddas upp separat via
`developer.apple.com/contact/file-upload/?teamId=SCALFR6L25` (Apple kan inte öppna Google Drive-länkar,
det var därför förra försöket avvisades 2024-11-01).

---

Hello,

Following up on case 102345613725 regarding the company information update for Team ID SCALFR6L25.

I have uploaded the certificate of registration through the file upload tool. Two corrections to my
earlier submission:

1. The document I sent in October 2024 was for the wrong entity. The correct legal entity for this
   developer account is **Aurora Punks AB, company registration number 559256-9718**. The document
   previously attached belonged to a different company in the group.

2. The registered address has since changed. The current registered address is:

   Aurora Punks AB
   c/o Bäckström, Bondegatan 31
   116 33 Stockholm
   Sweden

The attached certificate of registration from the Swedish Companies Registration Office (Bolagsverket),
issued 21 April 2026, confirms both the company registration number and the address.

Please let me know if you need anything further to complete the update.

Best regards,
Robert Bäckström
Aurora Punks AB

---

## Efter rättelsen

Uppdatera även D&B-posten så att D-U-N-S-registret matchar. Apple erbjöd det uttryckligen som
alternativ väg och kontrollerar mot D&B vid framtida verifieringar. Ingång:
`support.dnb.com/?CUST=APPLEDEV`. Tar ungefär två arbetsdagar innan Apple ser ändringen.

---

## 2026-08-06: D-U-N-S-frågan är LÖST ur mailarkivet (4am-körning, CorpBot)

Ticketens steg 1 ("vilket D-U-N-S ligger på teamet?") gick att besvara utan portalinloggning.
Hela kedjan ligger i tråden `17f8cea36fbbfd79` (2022-03-15):

1. **AP AB har ett eget D-U-N-S: `35-342-0335` (353420335)**, utfärdat av Bisnode/D&B
   2022-03-15 kl 10:30 för orgnr **559256-9718**, beställt av Robert samma morgon uttryckligen
   "för att sätta upp ett Apple Dev-konto". Apples enrollment-bekräftelse ("Dear Aurora Punks")
   kom samma dag kl 13:50. Teamet är alltså med största sannolikhet ankrat på 353420335, inte på
   något APDS-nummer. APDS-kopplingen var bara det felaktiga registreringsbeviset 2024, som
   dessutom avvisades.
2. **Fälla: `35-068-5539` (350685539) är WLBS:s D-U-N-S** (White Lines Black Spaces AB,
   559217-4196, i konkurs sedan 2024, K 16834-24). Henrik nämner det numret i samma tråd, vilket
   gör det lätt att ta fel. Rör aldrig den posten, den tillhör konkursboet.
3. Tredjepartsdata (Prospeo, CB Insights) visar fortfarande Timmermansgatan 43 som AP:s adress,
   konsistent med att D&B-posten är inaktuell.

### D&B-uppdateringen, klar att köra (MUST-ASK: extern registerändring, väntar på Roberts go)

| Fält | Värde |
|---|---|
| Portal | `https://support.dnb.com/?CUST=APPLEDEV` |
| D-U-N-S | 353420335 (sök på orgnr 559256-9718 om numret inte hittas direkt) |
| Legal name | Aurora Punks AB |
| Ny adress | c/o Bäckström, Bondegatan 31, 116 33 Stockholm, Sweden |
| Underlag vid behov | `_legals/Registreringsbevis_AP_AB_559256-9718_2026-04-21.pdf` |
| Ledtid | D&B bekräftar per mail; Apple ser ändringen efter ~2 arbetsdagar |

### Uppdaterad sekvens

1. Robert (eller CorpBot efter go): submitta adressändringen hos D&B enligt tabellen ovan.
2. Invänta D&B:s bekräftelsemail.
3. Skicka Gmail-utkastet `r4239276101451352352` på tråden "Re: [102345613725] Company
   information update". **Utkastet är omskrivet 2026-08-06** till D&B-varianten (det gamla
   utkastet påstod felaktigt att filuppladdningen var gjord) och är formulerat för att skickas
   FÖRST EFTER D&B:s bekräftelse. Är ärendet stängt: öppna nytt via "Update your information"
   på Membership details eller `developer.apple.com/contact`.
