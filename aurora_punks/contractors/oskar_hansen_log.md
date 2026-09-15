---
project: aurora_punks
type: contractor_record
contractor: Oskar Hansen
entity: Skokloster Konsult AB (559331-8313)
role: Porting Lead / Platform Engineer
source: Discord DM, Robert <-> Oskar
period: 2024-11-01 .. 2026-09-11
created: 2026-09-15
sensitivity: internal
---

# Oskar Hansen (Skokloster Konsult AB) — kontraktörslogg

Underlag från Robert och Oskars Discord-DM. Klistrad in av Robert 2026-09-15 i samband
med gen-006. Personuppgifter och inloggningar är **utelyfta** ur den här filen, se
"Utelyft" längst ned.

## Vem

- **Oskar Hansen**, Porting Lead / Platform Engineer.
- Bolag: **Skokloster Konsult AB**, org nr 559331-8313, Skoklostervägen 40, Skokloster (Håbo).
- Kontaktuppgifter och betalningsuppgifter lämnade 2024-11-01. Ligger i `secrets_registry.md`
  respektive Fortnox, inte här.
- Aktiv på: K2C (Sands of Duat / Pharaoh Lands), WMAY, Sir Whoopass, Block'Em!, GFF,
  Blue Scarab (Equinox: Homecoming), Feign, Malformation, SoulWalker, Hunter Call of the Wild
  (Avalanche-portning, via Rift Gaming).

## Oskars önskemål om K2C-kontraktet (2026-08-27)

Det här är den punkt Robert flaggade som viktigast. Oskar skrev 2026-08-27 17:19:

1. **Lägg om kontraktet till samma form som de andra underleverantörerna har för aug–dec.**
2. **Flytta gärna 20 % från augusti** till en annan månad om det passar Robert bättre.
3. **Arbetet ska inte ta slut vid cert.** Nuvarande skrivning innebär att så fort cert är
   godkänt är uppdraget slut. Oskars invändning: mycket går igenom cert medan det fortfarande
   finns game-breaking buggar kvar, dels sådant man inte hann före cert, dels sådant som visar
   sig vid testning efteråt.
4. **Utrymme för efterarbete.** Kombinerat med eventuellt "gratis" arbete januari–april vill han
   kunna fixa buggar, playtesta, profilera, leta minnesläckor och få ned minnesåtgången ordentligt
   innan det blir problem efter release. Särskilt relevant om spelet går genom cert redan tidigt
   i december.
5. **Sjukdom och röda dagar ska inte dra ned ersättningen.** Han vill slippa tänka på att få
   mindre betalt de dagarna, dvs månadsfast i stället för ren timdebitering.

**Roberts svar 2026-08-27 21:27:** "Absolut, vi kan väl kika på det i nästa vecka."
Per 2026-09-15 är det inte gjort. Tre veckor har gått.

## Produktion och infrastruktur (urval ur loggen)

- **2024-11-18:** Robert bad om veckovis statusuppdatering i SFH-kanalen, i samma form som
  Neville gör på VoD. Oskars mall: dagens arbete, blockerare markerade [BLOCKED], väntande
  poster [WAITING], plus vad som kommer nästa arbetsdag.
- **2025-05-23:** Oskar levererade app-flow och estimat för **FastSpring-appen**
  (Firebase Authentication, signed JWT till webbserver, FastSpring-webhooks, URL-scheme
  tillbaka till spelet). Estimat totalt cirka 12 dagar: FastSpring API 3 d, Firebase 2 d,
  köpflöde/webb 2 d, prototyp 1 d, Firebase i Unity 2 d, test och buffert 2 d.
  Motivering för Firebase: realtidsdatabas med callback när en spelares inventory ändras,
  plus färdig Unity-SDK.
- **2025-07-01/02:** Konsolpatch för KK. Robert kollade kontraktet: AP har **inget krav** på
  att leverera patchar (han trodde först 45 dagars servicetid). Beslut: stötta ändå, men
  samla ihop alla fixar först. Oskars bedömning: mest av tiden är testning, byggtiden
  försvinner om man kör två datorer, spelet går att spela igenom på två konsoler på under en dag.
- **2025-07-02 (Block'Em!):** Estimat portning **fem veckor** plus tid för cert och fixar,
  crossplatform 1 vecka. PC local only under en vecka. Höjd estimering pga risk att
  nätverkslösningen måste bytas: EOS-transportern är fyra år gammal. Oskar bedömde att det
  rimligen borde varit minst två veckor till. Gustav hade slutestimaten från mötet.
- **2025-08-01/03:** Tidrapportering för UE-refresher bokförs under **Running Costs, kund
  Aurora Punks AB**.
- **2025-09-04:** Oskar skickade utkast till meddelande till **Kwale om Feign-projektet**.
  Nintendo hade svarat att det troligen inte blir några stora problem, men att vissa delar
  måste lösas i synk med dem pga den egna nätverkslösningen, vilket förlänger tidplanen.
  Robert godkände utan ändringar.
- **2026-08-25:** Switch-devkit. Oskar kör **remote viewer** och styr kitet från datorn.
  Byggen delas via Drive. Oskar bad om tillgång till **submissions-mappen på AP:s Drive**
  för att kunna bygga en riktig patch, remasterfilen för SFH saknades (han hade byggt ett
  vanligt PS5-paket). Robert skulle kolla på det.
- **2026-08-27:** Firmware-uppdatering på Nintendo Target Manager. Verktyget heter
  **SystemUpdateSdev**, ligger under
  `C:\nintendoSDK\Unity6000.3.6_LTS-NXAddon20.5.14-Unity6.3\NintendoSDK\Tools\CommandLineTools`.
  Det finns även en initialize med UI. Felsökning: efter firmware-uppdatering måste
  handkontrollen paras om, annars ger inputen ingen reaktion trots att startskärmen visas.
- **2026-08-27:** Switch-bygget saknade den nya loggan. Oskar misstänkte en merge-konflikt och
  la upp en Jira-ticket.
- **2026-08-31:** Behov av en Drive-mapp för art assets från artister som inte har GitHub eller
  ligger i projektet (Dubi). Skäl: en source of truth så inget hamnar mellan stolarna.
  Robert bekräftade att en Drive finns.
- **2026-09-02:** Oskar skulle möta **Rift Gamings kodare Chris** för att titta på koden och
  estimera **Avalanche-portningen av Hunter: Call of the Wild**. Blockerat på kodtillgång.
- **2026-09-11:** Mötet med Rift genomfördes på Österlånggatan 43 (Bandit Island).

## Utelyft ur den här filen

Följande fanns i den klistrade historiken och ska **inte** ligga i ett RAG-indexerat dokument:

1. Oskars **personnummer**, privatadress, privata mailadress, telefonnummer och
   **bankuppgifter** (Handelsbanken). Hör hemma i Fortnox och i leverantörsregistret.
2. **Perforce-credentials i klartext** för Equinox: Homecoming (Blue Scarab) samt ett
   admin-konto på ett internt 192.168-nät. Se `secrets_registry.md`. Båda lämnades i
   Discord-klartext 2026-09-04 och 2026-09-11 och **bör roteras**.
