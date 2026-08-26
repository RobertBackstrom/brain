---
title: Disposable Corps - high level plan (underlag till LUG och deras projektinvesterare)
project: dsc
status: draft
created: 2026-08-26
author: Assistant (bizdev + pm + game design), för Robert Bäckström
audience: internt underlag. Extern version ligger på pitch.aurorapunks.com/disposable-corps (gated)
---

# Disposable Corps: high level plan

Underlag för Magnus Lysell (LUG) att ta med till projektinvesterare på Gamescom, och för
Roberts eget beslut om vad AP ska erbjuda. Extern, nedskalad och scrubbadversion publiceras
som gated sida. **Det här dokumentet är internt och innehåller saker som inte ska ut**, se
sista sektionen.

## 1. Var projektet faktiskt står

Verifierat 2026-08-26 mot Steam, LUG:s kampanjsajt, mailhistoriken och Discord-loggen med Anthony Wong.

1. **Spelet är inte släppt.** Steam app 3579070, "Coming soon", inget releasedatum, noll recensioner. Demo (app 3617330) ute sedan 2025-05-16. Windows, engelska plus förenklad och traditionell kinesiska. Utvecklare Armoured Dudes 甲士, utgivare Light Up Games.
2. **Publik tystnad sedan 2026-01-10.** Sju månader utan en enda Steam-nyhet. Innan dess var kadensen tät: ChinaJoy juli 2025, demouppdatering till TPS Fest augusti 2025, playtest 1 i september, WEPLAY och BGM i november, playtest 2 "The Refactoring Update" 22 december, förlängd två gånger, sista inlägget 10 januari med "we will go dark to work on the next update". Sedan ingenting.
3. **De byggde om grunden i stället för att skeppa.** Playtest 2 beskrivs som en refaktorisering av rörelse, kamera, AI och pathfinding, plus nytt rekylsystem och nya vapenmodeller. Under playtestet: tank ammo racks, bandskador, pansardeformation, brittiska styrkor (ofärdiga), server region-filter, gräsrenderingsslider.
4. **Serverbilden.** De har redan en serverlista med värdregionsfilter, och Steam-sidan listar både LAN PvP och LAN Co-op. Det pekar på att spelet redan kan köras värdbaserat, vilket gör Magnus önskan om att slippa "massa servrar" till en betydligt mindre teknisk resa än den låter. Måste verifieras i fas 0.
5. **Teamet är fyra personer:** huvudprogrammerare, juniorprogrammerare, game designer som också är vd och producent, samt en artist (Anthony, 2026-06-18). Ingen UI/UX-kompetens.
6. **Roberts egen speltest 2026-06-11:** spelade single player-tutorialen, "pretty rough UX".

## 2. Vad som är fel med produkten

Anthonys egen lista (2026-06-12), det vill säga utgivarens bedömning, inte vår:

1. UI och UX är dåligt
2. Kartan är dåligt designad och för stor
3. Spelarna förstår inte vad de ska göra
4. PvP-upplevelsen är dålig, botarna dödar dig för snabbt
5. Botarnas pathing och att kommendera dem fungerar dåligt
6. Sammantaget inte särskilt roligt

Anthonys diagnos av orsaken: "lack of skill for sure, and they lack any sense of good game design".

Läs listan igen och notera vad den inte innehåller. Det står ingenting om att spelet saknar
innehåll, teknik eller produktionsvärde. Allt på listan är **designbeslut och läsbarhet**.
Det är precis den kompetens teamet saknar och precis den AP tillför. Det är också därför en
ren timresursförstärkning inte löser problemet: koden är inte flaskhalsen, produktägarskapet är det.

## 3. Designen: skär core loopen till det som bara det här spelet kan göra

Spelet är idag fyra spel i ett: en shooter, en RTS-lätt truppkommendering, en basbyggare och
en fordonssimulator, ovanpå en för stor karta utan tydligt mål. Det förklarar hela punktlistan ovan.

**Det som är unikt och som ingen annan gör i det här formatet:** du gräver skyttegraven, du
slåss i graven du grävde, och den sprängs sönder under dig. Plus namnet, som redan är designen:
*Disposable Corps*. Du är en officer som skickar utbytbara män över kanten, och du är själv
bara ännu en kropp.

### Föreslagen loop, en match om 20 till 25 minuter i tre ronder med sidbyte

1. **Förberedelse, 90 sekunder.** Försvararen befäster en **avgränsad sektor**, inte hela kartan: fasta grävpunkter, barrikader, kulsprutenästen. Angriparen väljer anfallsväg och understöd.
2. **Anfall, 5 till 7 minuter.** Ett enda mål i taget, en skyttegravslinje, tydligt utmärkt, synlig klocka. Varje spelare för befäl över en liten AI-tropp om fyra till sex man, så 5v5 känns som sextio man på fronten.
3. **Kollaps och konsolidering, 60 sekunder.** Faller linjen flyttas fronten till nästa sektor och loopen börjar om. Tre sektorer per karta är en match.

Det är samma "dynamiskt skiftande front" de redan säljer på butikssidan, men gjord läsbar.

### Hur det mappar mot felen

| Problem | Åtgärd i loopen |
|---|---|
| Kartan för stor | Endast en sektor är aktiv i taget, resten är stängd. Kartan behöver inte byggas om, den grindas. |
| Vet inte vad man ska göra | Ett mål åt gången, en tydlig frontlinje i HUD, en ordervy |
| Botar dödar för snabbt | Botarna blir din tillgång, inte hotet. Sänkt AI-precision, suppression i stället för dödlighet. Spelare dödar spelare, botar ger massa och kaos |
| Bot-pathing och kommendering | Tre order på en radialmeny: framåt till markör, håll, gräv här. Begränsade order på en sektorsavgränsad navmesh är ett lösbart problem, öppen truppsimulering är det inte |
| Inte roligt | Ronden byggs mot ett ögonblick: visselpipan, alla över kanten samtidigt, artillerield. Var femte minut |

### Skärlista

Bort eller parkerat till efter Early Access: ekonomisystemet med pengar och fabriker som
producerar stridsvagnar (ett RTS-lager ovanpå en shooter och en huvudorsak till förvirringen),
nationsroster utöver två fraktioner, den djupa pansarsimuleringen med ammunitionsställ,
bandskador och deformationströsklar, kuriosabyggnader, PvE-co-op som marknadsfört läge,
LAN som säljargument, tutorialen som separat nivå (ersätts av guidning i första ronden).

### Serverfrågan

Värdbaserad listen server plus Steams relänät, ovanpå serverlistan och regionfiltret som redan
finns. Dedikerade servrar blir valfria för communityn i stället för en fast månadskostnad per
region. Det är det Magnus menar med att slippa massa servrar, och det ser ut att vara halvvägs
byggt redan. Verifieras i fas 0.

## 4. Faser och tidslinje

Early Access-release i **månad 10**, inom Magnus fönster på sex till tolv månader.

| Fas | Tid | Innehåll | Utfall |
|---|---|---|---|
| **0. Genomlysning** | 4 till 6 veckor | Byggd- och kodgenomgång, engineversion, serverarkitektur, designteardown, backlog, skär- och fixlista, låst scope | Beslutsunderlag plus **fast pris på fas 1** |
| **1. Core loop-lås** | månad 2 till 5 | Omskärningen körd, en karta med tre sektorer, truppkommando v2, bot-tuning, UX-pass med ny HUD och onboarding, serverbytet | **Stängd playtest med mätbar retention.** Investerarnas riktiga go/no-go |
| **2. EA-innehåll** | månad 6 till 9 | Tre kartor, två fraktioner, lätt progression, telemetri, ny butikssida och trailer, lokalisering, prestanda | EA-kandidat |
| **3. Launch och 90 dagar live** | månad 10 till 12 | EA-släpp, patchkadens, community, första innehållsdroppen | Släppt spel med livedrift |

## 5. Teamet, båda sidor i samma budget

Ändrat 2026-08-26 efter Discord-gruppen *LUG <> AP Disposable Corps* (Anthony, Magnus, Robert).
**Det gamla teamet är borta.** Kvar är de två grundarna: Paul kodar, Hammer står för vision och
game design. Anthony om det tidigare teamet: juniort, och deras UI/UX var dålig. Den bedömningen
är intern och går aldrig i skrift utanför AP.

Anthony bad om att få med grundarna i planen och satte priset själv: **30 000 SEK i månaden för
båda två**. Paketet täcker därmed hela projektet, inte bara AP:s halva, vilket är vad LUG:s
finansiärer behöver se.

| Roll | Sida | Allokering | SEK/mån |
|---|---|---|---|
| Grundarna (Paul kod, Hammer vision och design) | Armoured Dudes | 2 personer | 30 000 |
| Lead programmer (Fredrik Laurent) | AP | 50 % | 45 000 |
| UI/UX-designer (ej tillsatt) | AP | 50 % | 40 000 |
| Artist (Prateek) | AP | 50 % | 40 000 |
| Producent och produktägare (Robert) | AP | 25 % | 25 000 |
| **Totalt** | | | **180 000** |

Kodarraden halverades för att Paul kodar löpande. AP tar hostingbytet, nätverkslagret, teknisk
riktning och kodgranskning. UX-raden halverades också, men behålls bemannad eftersom ingen på
deras sida täcker den och den ligger överst på fellistan.

## 6. Budget och incitament

AP:s kontantdel är taklagd på **1 500 000 SEK för hela tolvmånadersåtagandet**. Grundarnas
30 000 i månaden betalas kontant och ligger ovanpå taket. Uppskjutet recoupas **2,5x vid
spelsläpp**, därefter **15 procent revenue share** till AP.

| | Per månad | 12 månader |
|---|---|---|
| Armoured Dudes (grundarna) | 30 000 | 360 000 |
| AP:s scope | 150 000 | 1 800 000 |
| **Projektkostnad** | **180 000** | **2 160 000** |
| AP skjuter upp | 25 000 | 300 000 |
| **Kontantbehov** | **155 000** | **1 860 000** |

Åtaganden, kursen 11,07 SEK per euro (ECB 2026-08-25, korskontrollerad mot två källor):

| Åtagande | Månader | Total SEK | Kontant SEK | Kontant EUR |
|---|---|---|---|---|
| Genomlysning | 1 | 180 000 | 155 000 | 14 000 |
| Låst core loop plus playtest | 5 | 900 000 | 775 000 | 70 000 |
| Fram till EA-släpp | 10 | 1 800 000 | 1 550 000 | 140 000 |
| **Hela vägen inklusive 90 dagar live** | **12** | **2 160 000** | **1 860 000** | **167 900** |

AP skjuter upp **300 000 SEK** över löptiden, som recoupas till **2,5x = 750 000 SEK** vid släpp,
därefter 15 procent revenue share.

### Vad som blev bättre med den här versionen

**Rörelsekapitalrisken är i princip borta.** I den förra versionen sköt AP upp 1 320 000, vilket
förutsatte att Ark Island accepterade halva arvodet mot recoup, annars var det AP:s pengar. Nu är
uppskjutningen **300 000 över tolv månader, 25 000 i månaden**. Det är hanterbart även om
underleverantörerna vill ha fullt betalt kontant, och då bär AP det på egen bok utan att fråga
någon. Recoupen faller från 3,3 MSEK till 750 000, alltså grovt 7 500 sålda exemplar i stället
för 33 000 innan revshare börjar.

**Kontantbehovet ut mot finansiärerna är 1,86 MSEK för hela spelet**, inte bara för AP:s del.
Det är en enklare sak att paketera än två separata finansieringar.

## 7. Styrningen, i praktiken löst 2026-08-26

Anthony frågade i gruppen hur upplägget skulle fungera med Paul och Hammer kvar. Roberts svar,
som Anthony accepterade och som Magnus såg:

> "I will be the annoying partner who asks for fixes and make sure they understand its needed,
> then we discuss solutions and if Paul says he wanna do it we set a deadline for it."

Det är en annan och bättre modell än "AP tar över". AP äger **produktbesluten och tidplanen**,
Paul behåller **implementationen**. Den tekniska medgrundaren blir inte fråntagen sin kod, han
får en motpart som driver fixlistan och sätter deadlines. Det var precis den invändning som
blockerade i juli ("the only way this can work is if the technical support only listens to him"),
och den här formuleringen går runt den utan att AP ger upp något som behövs för leveransen.

Risk kvar: modellen bygger på att Paul faktiskt levererar mot överenskomna deadlines. Det finns
ingen sanktion i upplägget om han inte gör det. Genomlysningsmånaden är rätt ställe att testa
det i liten skala innan tolv månader binds upp.

## 8. Risker och antaganden

1. **Nedgraderad 2026-08-26.** Mandatfrågan är löst i princip genom "annoying partner"-modellen, se sektion 7. Kvar är att den bygger på Pauls efterlevnad av deadlines utan sanktion.
2. Ingen repo- eller kodåtkomst än, ingen genomgång gjord. Alla siffror är intervall tills fas 0 är körd.
3. Engine och version okänd. Påverkar nätverksarbetet direkt.
4. Två parallella kapitalspår, Hammer och Pauls egen roadmap mot LUG:s investerare. Risk att AP:s plan används som förhandlingsbricka.
5. Sju månaders tystnad. Wishlist-kurvan svalnar och vi har inte siffran, LUG har den.
6. Inget NDA direkt med Armoured Dudes. 2025-avtalet var med LUG.
7. Kinesiskt team, tidszon plus begränsad engelska enligt Anthony. Lägg på producentoverhead, den är inbakad i 50 procent producent.
8. **Inaktuell 2026-08-26.** Budgeten täcker nu båda sidor: grundarna ligger inne på 30 000 i månaden, satt av Anthony. Det gamla antagandet om separat finansiering av deras team gäller inte.
9. Teamet på deras sida är **två personer**, inte fyra. Det tidigare teamet är borta. Tolv månader till EA vilar på att Paul ensam orkar den löpande kodproduktionen med AP:s senior på halvfart bredvid.
10. Underlaget går vidare till **LUG:s finanspartners**. Siffrorna blir svårare att ändra när de väl är paketerade.

## 9. Beslut, tagna 2026-08-26

Robert satte hela den kommersiella modellen: låst team om 2,5 personer, UX-raden på 80 000,
Prateek på 40 000 vid halvfart, producenten på 25 procent av K2C-lönen, uppskjutning över
60 000 per resurs (40 000 för Prateek), 2,5x recoup vid släpp och 15 procent revenue share.
Den gamla nettodelningen 50/25/25 är **struken**, revenue share ersätter den.

Robert satte därefter (samma dag) **kontanttaket till 1,5 MSEK för hela tolvmånadersåtagandet**,
vilket ersätter tröskelmodellen och höjer AP:s uppskjutna del från 600 000 till 1 320 000.

Kvar att bestämma: om Ark Island accepterar halva arvodet mot recoup (se sektion 6), om månad 1
säljs som ett eget åtagande eller bara som första månaden av tolv, och om AP kräver ett tak på
hur länge det uppskjutna får ligga innan det förfaller.

## 10. Får inte lämna det här dokumentet

- Anthonys formulering om att teamet saknar skill och game design-känsla. Aldrig i skrift till någon utanför AP.
- Att den tekniska medgrundaren pekas ut som blockeraren. Den externa sidan talar om mandat och arbetssätt, inte om personer.
- Interna kostnads- och marginalresonemang. Externa sidan visar pris, inte rate card.
