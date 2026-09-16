---
project: house_siege
ticket: hsg-001
date: 2026-09-16
status: internt arbetsdokument, ej delat med grundarna
author: BizDev
---

# House Siege: marknadscomp, core loop, art direction och två scope

Internt underlag. Inget här har gått till Markus, Oscar eller Bibbi.

## TL;DR

1. **Konceptet sitter i rätt lane vid exakt rätt tidpunkt.** Friendslop är den mest
   kapitaleffektiva genren på Steam just nu, och House Siege har den enda egenskap som
   räknas i den lanen: en hook som funkar på ett stumt autoplay-klipp.
2. **Men spelet är felskalat.** 4v4/5v5 med full strukturfysik och sex hustyper är inte ett
   friendslop-spel, det är ett spel för 15 till 25 MSEK. Skalat till 3v3, ett hus,
   chunk-baserad förstörelse och sex minuters ronder landar det i lanen.
3. **Den stora designrisken är reparation.** Deras eget dokument ställer frågan rätt: är det
   lika roligt att bygga som att förstöra? Comparna svarar nej. Varje kommersiellt lyckat
   förstörelsespel är förstörelse-bara. Ingen har shippat en rolig reparationsloop.
   Mitt förslag nedan löser det genom att göra även försvararens verb destruktivt.
4. **Ingen direkt konkurrent finns.** Jag sökte igenom Steam på destruction, demolish,
   siege och raid. Närmast ligger singleplayer-sandlådor (Teardown, Brick Rigs) och
   asymmetrisk PvP utan förstörelse (Dead by Daylight). Ingen äger "försvara eller riv huset" i PvP.
5. **Två scope:** rekommenderad nivå efter kostnadspasset i avsnitt 10 är
   **600 000 SEK** för Steam-sida plus SoMe-ammunition (5,0 manmånader, 3 månader) och
   **2 130 000 SEK** för prototyp med P2P och bottar fram till Steam Beta
   (17,75 manmånader, 6 månader). Totalt 2 730 000 SEK, 70 procent cash och 30 procent
   deferred. Avsnitt 5 och 6 beskriver det ursprungliga, dyrare upplägget och står kvar
   som jämförelse.
6. **Go/no-go-porten mellan dem är 30 000 wishlists inom 60 dagar.** Det är Poldens egen
   signeringströskel, och den är den enda ärliga anledningen att spendera Scope B-pengarna.

---

## 1. Marknadscomp-pass

Alla siffror hämtade live från Steams API 2026-09-16, med `language=all` så det inte är
lokalfiltrerat (se [[bizdev_learnings]] 2026-08-26). Recensionsantal, inte
uppskattade försäljningssiffror.

### Nivå 1: friendslop-genombrotten. Det här är lanen vi siktar på.

| Titel | Recensioner | Betyg | Pris | Release |
|---|---|---|---|---|
| Lethal Company | 510 897 | 97 % Overwhelmingly Positive | $9.99 | okt 2023 |
| R.E.P.O. | 423 797 | 96 % Overwhelmingly Positive | $6.49 | feb 2025 |
| PEAK | 371 878 | 94 % Very Positive | $7.99 | jun 2025 |
| Schedule I | 316 126 | 98 % Overwhelmingly Positive | $19.99 | mar 2025 |
| Content Warning | 163 413 | 94 % Very Positive | $7.99 | apr 2024 |
| Meccha Chameleon | 88 828 | 88 % Very Positive | $5.99 | jun 2026 |

**Vad det säger:** prispunkten är $5.99 till $9.99, inte premium. Budgetarna ligger under
200 000 USD (Naavik), och Polden anger 150 000 USD som snittinvestering per spel.
Konverteringen från wishlist till köp är 21 till 38 procent på dag 7 och 38 till 64 procent
på dag 30, mot 3 till 6 procent för AAA. För ett spel som kostar 6 dollar är en wishlist i
praktiken ett köp som väntar.

### Nivå 2: förstörelse säljer, men utan multiplayer

| Titel | Recensioner | Betyg | Pris | Release |
|---|---|---|---|---|
| Teardown | 136 106 | 96 % Overwhelmingly Positive | $29.99 | apr 2022 |
| Brick Rigs | 59 630 | 95 % Very Positive | $19.99 | jul 2023 |
| Besiege | 53 252 | 95 % Overwhelmingly Positive | $14.99 | feb 2020 |
| Instruments of Destruction | 1 574 | 91 % Very Positive | $19.99 | maj 2024 |

**Vad det säger:** Teardown tar 30 dollar och har 136 000 recensioner utan att ha
multiplayer. Förstörelse bär ett premiumpris på egen hand. Men notera bredden i den här
nivån: Instruments of Destruction har 1 574 recensioner. Bra förstörelsetech garanterar
ingenting. Teardown vann på pusseldesign, inte på fysiken.

### Nivå 3: taket, och varningen

| Titel | Recensioner | Betyg | Pris | Release |
|---|---|---|---|---|
| Rainbow Six Siege | 1 552 974 | 82 % Very Positive | Free | dec 2015 |
| Dead by Daylight | 934 842 | 78 % Mostly Positive | $19.99 | jun 2016 |

**Vad det säger:** asymmetrisk PvP kan bli enormt. Båda är dock live services i tio år med
AAA-budget och permanent balansorganisation. Betygen (82 och 78 procent) är också de lägsta
i hela comp-setet. Asymmetrisk PvP gör spelare arga på ett sätt som co-op inte gör.

### Budgetslutsats

House Siege som det är skrivet i deras deck, med 4v4/5v5, full strukturfysik, sex
hustyper, progression, matchmaking, backend, cosmetics och console-roadmap, är inte ett
spel i friendslop-budget. Det är 15 till 25 MSEK och tre år. Ingen studio tar det på spec.

House Siege skalat till **3v3, ett hus, chunk-baserad förstörelse, sex minuters ronder och
bottar** är ett spel som går att bygga för 3 till 4 MSEK till en spelbar beta. Det är det
spelet de två scopen nedan bygger.

Att skala ner är inte att sänka ambitionen. Det är att flytta beviset framför pengarna.

---

## 2. Styrkor och svagheter

### Styrkor

1. **Hooken överlever ett stumt autoplay-klipp.** 35 procent av alla wishlists kommer från
   TikTok, Reels och Shorts (Poldens egen uppdelning). Ett hus som rasar behöver ingen
   förklaring, ingen ljudspår och ingen genrekunskap. Det är den mest värdefulla
   egenskapen ett spel kan ha i dagens discovery-regim, och den kan inte läggas till i efterhand.
2. **Målet är ett synligt tal på ett fysiskt föremål.** Ingen UI-läskunnighet krävs.
   En tittare förstår ställningen genom att titta på huset.
3. **Förlust är roligt.** Friendslop drivs av att misslyckas på ett delbart sätt.
   Ett strukturellt ras är den bästa förlustanimation som finns, och den är gratis: fysiken
   gör den åt dig, olika varje gång.
4. **Fysiken författar innehållet.** Billigaste tänkbara replayability. Sex hus behöver inte
   sex designade upplevelser, bara sex uppsättningar väggar.
5. **Ingen äger positionen.** Sökningen hittade ingen PvP-titel om att försvara eller riva
   ett hus. Närmast ligger Demolish or Die (49 recensioner) och Building Destruction
   (126 recensioner), båda för små för att vara konkurrenter och båda singleplayer.
6. **Asymmetri halverar innehållsbehovet.** Två fantasier ur en uppsättning system,
   ett hus, en karta.

### Svagheter

1. **Reparation är inte ett kul verb, och det är hela deras försvarssida.** Detta är den
   enskilt största risken. Teardown, Brick Rigs, Besiege och Instruments of Destruction är
   alla förstörelse-bara. Det finns ingen comp där bygga eller laga är den roliga halvan.
   Utan en lösning här är House Siege ett spel där hälften av spelarna har det tråkigt.
   Se avsnitt 3.
2. **Förstörelse plus multiplayer är den dyraste kombinationen i indie.** Teardown har
   ingen multiplayer, och det är inte en slump: att replikera förstörelsetillstånd
   deterministiskt över nätet är svårt. Samtliga friendslop-comps har trivial fysik
   jämfört med det här.
3. **PvP kräver samtidiga spelare, friendslop lever på två till fyra kompisar.** 4v4 kräver
   åtta personer för att ens starta. Det är kallstartsproblemet som dödar PvP-indies.
   Bottar är därför inte en feature, de är produkten. Det är rätt av Robert att lägga dem
   i Scope B.
4. **Asymmetrisk balans är en löpande kostnad, inte en lanseringskostnad.** R6 Siege har
   patchat balans i tio år. Ett litet team kan inte det. Designen måste vara robust mot
   obalans från början, vilket talar för färre verktyg och tydligare roller.
5. **Prislappen krockar med deras egen plan.** Decket säger "premium base game" med
   console-expansion. Friendslop säger $5.99 till $7.99. Det är två olika spel.
   Ett 30-dollarsspel kräver Teardown-nivå på techen.
6. **Det finns inget team, ingen tech, inget motorval och ingen prototyp.** Just nu finns
   noll bevis för att någon kopplad till projektet kan bygga det här.
7. **Grundarnas egna meriter i decket är obekräftade.** Se CLAUDE.md. Det spelar roll om
   materialet ska vidare till en tredje part.

---

## 3. Core loop: TEAR, BUILD, BREAK

Deras deck beskriver PREPARE, BREACH, ESCALATE, COLLAPSE OR SURVIVE. Det är en
matchtidslinje, inte en core loop. En core loop är vad en enskild spelare gör om och om
igen på tjugo sekunder.

### Problemet som måste lösas

Försvararen måste ha ett verb som är lika fysiskt och lika roligt som att förstöra.
"Håll inne E på väggen för att reparera" är det inte.

### Förslaget: huset är sitt eget byggmaterial

**Försvararna har inga byggresurser. De får material genom att slita sönder huset inifrån.**

Du behöver bräda ytterdörren. Det finns ingen brädhög. Det finns en trappa. Du river
trappan, släpar upp den och slänger den mot dörren.

Det ger tre saker på en gång:

1. **Försvararens verb blir också destruktivt.** Samma fysik, samma feel, samma komik som
   angriparnas. Ingen spelare sitter och håller inne en knapp.
2. **Varje försvar kostar något.** Möbler är gratis att riva. När möblerna tar slut börjar
   du äta bärande konstruktion, och då sjunker din egen House Integrity. Du gräver i din
   egen health bar för att överleva nästa minut.
3. **Kartan förändras av försvaret, inte bara av anfallet.** Du rev trappan, nu kommer du
   inte upp på övervåningen heller.

Signatursatsen: **det enda sättet att rädda huset är att äta upp det.**

### Loopen

Båda lagen kör samma fyra verb. Det är medvetet, och det är också ett scope-argument:
en interaktionsmodell i stället för två halverar prototypkostnaden.

```
   GRAB  ->  HAUL  ->  SLAM  ->  BREAK
    |                              |
    +------------ 15-25s ----------+
```

- **GRAB** - slit loss något. En dörr, ett badkar, ett kylskåp, en bärande balk.
- **HAUL** - bär det. Tungt, klumpigt, du blir långsam och du ser dum ut.
- **SLAM** - slå fast det. Försvarare bräddar en öppning. Angripare använder samma
  föremål som murbräcka eller ramp.
- **BREAK** - någon river det du just satte dit, och loopen börjar om.

### Matchramen

| Parameter | Deras deck | Mitt förslag | Varför |
|---|---|---|---|
| Lagstorlek | 4v4 eller 5v5 | **3v3** | Sex spelare är taket för bekväm P2P och golvet för kallstart. Friendslop-comps ligger på 2 till 4. |
| Rondlängd | 12 minuter | **6 minuter** | Kortare ronder ger fler klipp och lägre tröskel. En session blir best-of-3 på ~20 minuter. |
| Sidbyte | Nämns inte | **Byt sida efter varje rond** | Alla får förstöra. Löser halva "tråkig försvarare"-risken gratis. |
| Vinstvillkor | Integrity över 50 % | **Integrity över 50 % vid tidens slut, eller total kollaps direkt** | Behåll deras. Den är bra och läsbar. |
| Förstörelse | "Strukturell fysik" | **Chunk-baserad, förförfattade brottytor** | Voxel-förstörelse à la Teardown går inte att replikera över nät till rimlig kostnad. Chunks går. |

Det sista är det tekniskt viktigaste beslutet i hela projektet och det måste bevisas i
Scope B månad 1.

---

## 4. Art direction: "Flatpack"

Robert har rätt i instinkten, och det finns ett kommersiellt argument bakom den som är värt
att säga rakt ut:

**Konsten ska se ut som att en människa gjort den slarvigt, inte som att en maskin gjort den
perfekt.** Polerad AI-render signalerar "ingen studio är kopplad till det här". Ful men
sammanhängande low-poly signalerar "riktigt spel, riktiga människor, med på skämtet".
Köparen kan skilja på dem, och deras nuvarande key art signalerar fel sak.

### Referenser och vad vi tar från varje

| Referens | Appid | Vad vi tar |
|---|---|---|
| **How to Fish** | 4001890 | Den medvetet amatörmässiga grovheten. Inget försöker imponera. |
| **R.E.P.O.** | 3241660 | Guldstandarden. Nästan otexturerade gråbruna miljöer, en stark läsbar silhuett, fysiken bär allt. |
| **Content Warning** | 2881650 | Flat shading och begränsad palett. Läsbart på 480p i en telefon. |
| **Brick Rigs** | 552100 | Modulariteten. Huset är synligt byggt av delar som klickar ihop. |
| **Human Fall Flat** | 477160 | Blanka degiga figurer, noll ansiktsanimation, all komik ur ragdoll. |
| **WEBFISHING** | 3146520 | Flat vertex colour i stället för texturer. |

### Riktningen

- **Huset är en byggsats.** Synligt modulärt, som ett möbelpaket. Det gör förstörelsen
  läsbar (man ser vilken bit som lossnade) och gör authoring billigt (ett kit, sex hus).
  Därav arbetsnamnet Flatpack.
- **Flat vertex colour. Inga PBR-material, inga normal maps, inga texturer.** Skär
  artkostnaden dramatiskt och är dessutom exakt hur lanen ser ut.
- **Skadetillstånd är färg, inte detalj.** En bit går från beige till sprucken till
  borta. Läsbart på en telefon i en scrollande feed.
- **Figurer är degiga blanka humanoider med en dräktslot.** Cosmetics-monetisering utan
  karaktärsartkostnad.
- **Mättade primärfärger på beige och grå hus.** Laget syns, skadan syns, resten är bakgrund.
- **Kameran är fast och vid.** Klippbarhet slår immersion. Man ska se hela huset falla.

### Två hårda regler

1. **Ingen AI-genererad key art.** Varje bild i butiken och i SoMe ska vara en riktig render
   ur den riktiga byggen, även när den är ful. En ful skärmdump ur ett verkligt bygge slår
   en vacker AI-bild, för den bevisar att spelet existerar.
2. **Ingen realism.** Så fort huset börjar se ut som ett riktigt hus börjar folk jämföra
   med Teardown och Battlefield, och den jämförelsen förlorar vi.

---

## 5. Scope A: Steam-sida och SoMe-ammunition

**Mål:** en live Steam-sida, en trailer som ser ut som gameplay, och cirka 30 vertikala klipp.
Utan att bygga spelet.

**Metod:** ett trailer-bygge. Riggad förstörelse i realtid, skriptade sekvenser, inga
nätverk, inga bottar, ingen matchlogik. En realtidscinematisk sandlåda som filmas.

### Tidplan, tre månader

| Månad | Milstolpe | Innehåll | Roller | FTE |
|---|---|---|---|---|
| **M1** | Art direction lock | Flatpack-kit v1, palett, figurdesign, chunk-förstörelse R&D, första testrender | Tech artist 1,0 · 3D-artist 1,0 · AD/designer 0,5 | **2,5** |
| **M2** | Hero house klart | Ett komplett hus, sex till åtta förstörelsesekvenser riggade, figur med dräkt, kameraarbete | Tech artist 1,0 · 3D-artist 1,0 · AD/designer 0,5 · Producent 0,25 | **2,75** |
| **M3** | Sidan live | Trailerinspelning och klipp, 30 vertikala klipp, capsules, sex skärmdumpar, butikstext, taggar, sidan publicerad | Tech artist 0,5 · 3D-artist 0,5 · AD/designer 0,5 · Producent 0,25 | **1,75** |

**Summa: 7,0 manmånader.**

### Budget Scope A

| Post | Belopp |
|---|---|
| 7,0 manmånader × 120 000 | **840 000 SEK** |
| Varav cash (70 %) | 588 000 SEK |
| Varav deferred (30 %) | 252 000 SEK |
| Cash per månad | 210 000 · 231 000 · 147 000 |

**Utanför ovanstående:** creator-kampanjen. Poldens modell bygger på betald spridning via
TikTok, Reels och Shorts. Räkna **150 000 till 300 000 SEK i mediabudget** ovanpå. Det är
inte vår kostnad och inte vår marginal, men det måste finnas, annars mäter testet ingenting.

### Vad de äger efteråt

Steam-sidan, trailern, klippen, hela Flatpack-kittet och figurerna. Om de inte går vidare
med oss kan de ta paketet till vem som helst. Det är avsiktligt och det är vårt starkaste
säljargument mot alternativet att pitcha ett förlag som tar rättigheter i utbyte.

---

## 6. Scope B: prototyp, P2P och bottar, fram till Steam Beta

**Mål:** bevisa att core loopen är rolig, att förstörelse kan replikeras P2P, och att
bottar gör spelet spelbart utan sex samtidiga människor. Slutläge: en Steam Beta som går
att bygga community kring.

Startar efter Scope A och återanvänder allt artmaterial därifrån.

### Tidplan, sex månader

| Månad | Milstolpe | Vad som bevisas | Roller | FTE |
|---|---|---|---|---|
| **M1** | **Prototype** | GRAB, HAUL, SLAM, BREAK i grålåda. Chunk-förstörelse på en vägg. Bara lokalt. Frågan som besvaras: känns det bra att slita loss saker? | Senior gameplay/network 1,0 · Gameplay 1,0 · Designer 0,5 · Producent 0,25 | **2,75** |
| **M2** | **First Playable** | Hela loopen i ett hus. Integrity-mätaren. Kannibaliseringsmekaniken. Lokal 3v3 mot dumma bottar. Frågan: är försvar lika kul som anfall? | + Tech artist 0,5 · 3D 0,5 | **3,75** |
| **M3** | **Netcode Alpha** | P2P listen server, replikering av förstörelsetillstånd, sex spelare över internet. Den tekniskt farligaste månaden. | Samma | **3,75** |
| **M4** | **Bots & Balance** | Bottar som både kan anfalla och försvara. Host migration. Återanslutning. Första balanspasset med sidbyte. | Samma | **3,75** |
| **M5** | **Beta Candidate** | Steam-lobbies, inbjudningsflöde, progression-stub, telemetri, krasch- och prestandapass. | Samma | **3,75** |
| **M6** | **Steam Beta** | Stängd beta till wishlist-listan, sedan öppen. Community-kanal, patchkadens, live-mätning. | Samma, producent upp till 0,5 | **3,75** |

**Summa: 21,5 manmånader.**

### Budget Scope B

| Post | Belopp |
|---|---|
| 21,5 manmånader × 120 000 | **2 580 000 SEK** |
| Varav cash (70 %) | 1 806 000 SEK |
| Varav deferred (30 %) | 774 000 SEK |
| Cash per månad, snitt | ~301 000 SEK |

### Risker i Scope B, rangordnade

1. **M3 är projektet.** Om förstörelsereplikering över P2P inte håller är hela spelet ett
   annat spel. Bygg M1 så att M3-frågan kan ställas tidigt, och lägg en teknisk spike på
   replikering redan i M1 i stället för att vänta.
2. **M2 avgör om designen håller.** Om kannibaliseringsmekaniken inte gör försvar roligt
   ska projektet stoppas där, inte i M5.
3. **Bottar är svårare än de låter.** En bott som ska riva ett hus intelligent är ett
   riktigt AI-problem. Budgeterat, men det är den post som oftast spricker.

---

## 7. Kommersiell modell

Mönstret är hämtat från Disposable Corps och anpassat.

| Villkor | Nivå |
|---|---|
| Kostnad per manmånad | 120 000 SEK |
| Cash | 70 % |
| Deferred | 30 % |
| Recoup på deferred | 2,5x vid release |
| Rev-share efter recoup | 15 % |
| IP-position | Ingen. De äger allt. |

### Totalen om båda scopen körs

| Post | Belopp |
|---|---|
| 28,5 manmånader × 120 000 | **3 420 000 SEK** |
| Cash över nio månader | 2 394 000 SEK |
| Deferred | 1 026 000 SEK |
| Deferred recoupat till 2,5x vid release | 2 565 000 SEK |
| Därefter | 15 % rev-share |

### Vad det betyder i sålda exemplar

Vid $6.99, efter Steams 30 procent och ett realistiskt avdrag på ~25 procent för
regionsprissättning och rabatter, landar netto runt $3.67 per exemplar.

- Täcka vår cash: **cirka 69 000 exemplar**
- Täcka cash plus hela recoupen: **cirka 142 000 exemplar**

Sätt det mot comparna: Content Warning har 163 000 recensioner, Meccha Chameleon 88 000.
Vid en konservativ recension-till-försäljning på 30:1 betyder det miljoner exemplar. Även
ett blygsamt utfall i den här lanen ligger långt över 142 000.

**Slutsatsen är att modellen inte kräver en hit för att gå ihop.** Den kräver att spelet
blir klart och att det inte floppar helt. Det är ett bra argument i rummet, och det är sant.

*Not: USD-omräkningen är ungefärlig. Hämta live FX innan någon siffra går in i ett avtal,
se [[reference_fx_rates]].*

---

## 8. KPI-porten mellan Scope A och Scope B

Robert bad mig kolla Poldens modell för att avgöra om KPI:erna ligger rätt. Här är vad de
faktiskt gör.

### Poldens modell

Tre steg: pitch och svar inom två veckor, sedan ett **marknadstest** som de själva
finansierar (Steam-sida, trailer, creator-kampanj, dashboards öppna för utvecklaren), sedan
signering med full finansiering. De anger **150 000 USD i snittinvestering per spel, med
marknadsföring ovanpå som aldrig recoupas**. Publicerat: 10 spel, 600 000 sålda exemplar,
3 miljoner wishlists i portföljen, över 1 miljon wishlists genererade före
produktionsbeslut. Cartel Pilots Wanted 400 000 wishlists, Totally Secure Airport 450 000.

**Deras signeringströskel: 30 000 wishlists från testet.**

Deras egen uppdelning av var wishlists kommer ifrån: TikTok, Reels och Shorts 35 procent,
Steam internt 25 procent, vänner 25 procent, Twitch och YouTube 10 procent, eget innehåll
5 procent. Alltså kommer **70 procent utifrån Steam**. Det är därför mediabudgeten i
Scope A inte är valfri.

### Vår KPI-stege

Scope A:s enda syfte är att producera en siffra som gör Scope B till ett enkelt beslut.

| Utfall, 60 dagar efter att sidan gått live | Tolkning | Åtgärd |
|---|---|---|
| Under 10 000 wishlists | Hooken bär inte i den här formen | Stoppa. Materialet är deras, de har förlorat 840k, inte 3,4M. |
| 10 000 till 30 000 | Tvetydigt | Iterera trailer och kapsel, kör om kampanjen en gång innan beslut. |
| **30 000 eller mer** | **Poldens egen signeringsbar är passerad** | Kör Scope B. |
| 100 000 eller mer | Oreshkins nivå för "stor hit" i genren | Kör Scope B och höj ambitionen på console och lokalisering. |

**En viktig nyansering som måste sägas i rummet:** 30 000 wishlists är en *signeringströskel*,
inte en lönsamhetströskel. Vid 38 procents 30-dagarskonvertering ger 30 000 wishlists cirka
11 400 exemplar. Det betalar ingenting. Trettiotusen betyder "konceptet bär, fortsätt
investera", inte "vi är hemma". För att budgeten ovan ska gå ihop vill vi se
**150 000 wishlists vid lansering**, vilket är helt normalt i den här lanen om Scope B
levererar en beta som folk klippar.

### Det ärliga förbehållet

Polden finansierar sitt marknadstest själva, i ungefär den storleksordning vi offererar
840 000 SEK för. Grundarna har alltså i teorin ett alternativ: pitcha ett förlag som gör
testet gratis mot rättigheter.

Det bör vi säga först, inte bli påkomna med. Motargumenten är starka och sanna:
Polden signerar co-op, inte asymmetrisk PvP med tung förstörelsetech, så träffytan är
osäker. Ett förlag tar rättigheter och kontroll. Vårt upplägg lämnar dem med
allt material i handen och IP:t obelastat. Och de får tekniskt besked om huruvida spelet
går att bygga, vilket ett marknadstest aldrig ger dem.

---

## 10. Kostnadsreduktion: vad som faktiskt går att skära

Tillagt 2026-09-16 efter Roberts fråga om lägre grafisk ambition, AI och Unity Asset Store.

Kort svar: ja, 20 till 35 procent. Men besparingen ligger inte i att göra grafiken fulare.
Den ligger i att **inte bygga teknik vi inte behöver** och i att **köpa allt som inte syns
i hjältebilden**.

### Lever 1: Scope A behöver ingen förstörelsetech alls

Det här är den största enskilda posten och den var dold i originalscopet.

En trailer behöver inte realtidsförstörelse. Den behöver **bakade simuleringar**: cell
fracture och rigid body i Blender, uppspelat som animation. Ingen runtime, inget system,
ingen R&D. Det tar bort hela "chunk-förstörelse R&D"-raden ur M1, alltså exakt den post
som var dyrast och mest osäker.

Konsekvensen är att Scope A:s teknik är slit-och-släng. Det är rätt, eftersom Scope A:s
leverans är **footage och en Steam-sida, inte kod**.

### Lever 2: köp huset i stället för att bygga det

Unity Asset Store har färdiga, förfrakturerade modulära husbyggsatser:

| Paket | Vad det ger |
|---|---|
| Modular Destroyed Buildings (Hivemind) | 300+ meshes, väggar, golv, tak, färdiga hus med gåbara interiörer |
| Destructible Buildings (Raw Formula) | 24 till 34 frakturbitar per byggelement, byggt för fysik och explosioner |
| Destroyed Building Kit (Loknar) | hela spannet från intakt till ruin |
| Synty POLYGON | prenumeration 30 USD per månad för hela biblioteket, packs 20 till 350 USD |

Det tar bort större delen av 3D-artistens last i M1 och M2.

### Lever 3: AI där den är gratis, inte där den kostar

Steam skrev om sin AI-deklaration i **januari 2026**. Den nya gränsdragningen är
användbar för oss:

- **Kräver inte deklaration:** AI-verktyg i utvecklingsledet. Konceptbilder, moodboards,
  kodassistans, planering. Explicit undantaget.
- **Kräver deklaration:** allt spelaren faktiskt ser eller hör i spelet, **och
  marknadsföringsmaterial och butikssidan**.

Praktiskt för oss:

- **Konceptning, moodboards, shot planning, kodassistans:** använd fullt ut. Gratis, syns inte,
  deklareras inte.
- **Breakable props:** AI-genererad 3D duger. Rodin beskrivs som produktionsklar utan
  efterarbete, Tripo gör låg-poly snabbt. För flatskuggad sönderslagbar möbelrekvisita i
  bakgrunden är kvaliteten mer än tillräcklig, och det är åttio föremål vi slipper modellera.
- **Capsule, key art, butiksbilder: nej.** De är marknadsföringsmaterial och triggar
  deklarationsplikt. Ungefär vart femte spel på Steam bär numera etiketten, så det är
  inte skamligt, men i just den här genren är publiken den mest AI-fientliga som finns och
  kapseln är den enskilt mest avgörande bilden i hela projektet. Där sparar vi inte pengar.

### Lever 4: Scope B ska inte replikera fysik

Standardlösningen, och den är dokumenterad: **replikera skadehändelser, inte fysiktillstånd.**
Auktoritativt tillstånd blir "vilka chunks är borta" plus House Integrity, alltså i praktiken
en bitmask och ett tal. Flygande spillror är klientsides kosmetik och får divergera mellan
spelare.

Det avdramatiserar M3, som jag pekade ut som projektets farligaste månad, och det är därför
Scope B kan tappa en tech artist och ändå leverera.

### Motorval, som följer av det här

**Unity, för båda scopen.** Friendslop-lanen är nästan uteslutande Unity, byggt av team på
två till fyra personer, valt just för tillgången på assets och tutorials. Utvecklarna är
billigare och fler. Alla förstörelsepaket ovan är Unity. Unreals Chaos är bättre
förstörelsetech, men replikeringen är ett känt elände och lanen finns inte där.

### Det jag inte skulle skära

Scope A:s hela produkt är ett klipp som stoppar scrollen. Om huset är ett igenkännbart
Asset Store-hus ser klippet ut som hundra andra spel, och wishlist-siffran kommer in låg.
Då har vi spenderat en halv miljon på att inte lära oss någonting, vilket är dyrare än att
spendera 840 000 på att lära oss något.

Kritiken finns och den är namngiven i communityn: köpta Synty-assets ger "serious asset flip
vibes", och spelare känner igen dem tvärs över titlar.

**Regeln blir: köp allt som inte är i hjältebilden, författa det som är.** Konkret betyder
det en egen flat shader, en låst palett och en egen figursilhuett. Det är ungefär tre veckor
tech artist, och det är den enda raden jag inte skulle röra. Det är den som gör att köpta
assets slutar se köpta ut.

**Och ett specifikt argument för just den här kunden:** deras eget deck ser redan
AI-tillverkat ut. Om vår första leverans också ser köpt och hopsatt ut förstärker vi exakt
det intryck som sänker projektet hos en riktig studio eller ett förlag senare.

### Omräknade scope

**Scope A**

| Variant | Manmånader | Totalt | Cash (70 %) | Deferred (30 %) | Vad som ändras |
|---|---|---|---|---|---|
| A0, originalet | 7,0 | 840 000 | 588 000 | 252 000 | Allt författat |
| **A1, rekommenderad** | **5,0** | **600 000** | **420 000** | **180 000** | Köpt husbyggsats, bakad förstörelse, AI-props, ett eget look dev-pass |
| A2, golvet | 4,0 | 480 000 | 336 000 | 144 000 | Som A1 men två månader, kortare trailer, färre klipp |

A1 månad för månad: M1 tech artist 1,0 och AD 0,5 (shader, palett, kitbash) = 1,5.
M2 tech artist 1,0, 3D 0,5, AD 0,5, producent 0,25 (bakade ras, figur, set dressing) = 2,25.
M3 tech artist 0,5, AD 0,5, producent 0,25 (trailer, 30 klipp, capsules, butikstext) = 1,25.

**Scope B**

| Variant | Manmånader | Totalt | Cash (70 %) | Deferred (30 %) | Vad som ändras |
|---|---|---|---|---|---|
| B0, originalet | 21,5 | 2 580 000 | 1 806 000 | 774 000 | Egen art, fysikreplikering antagen |
| **B1, rekommenderad** | **17,75** | **2 130 000** | **1 491 000** | **639 000** | Händelsereplikering, återbruk av A-material, tech artist och 3D nästan bort |
| B2, golvet | 14,75 | 1 770 000 | 1 239 000 | 531 000 | Fem månader i stället för sex. Bottmånaden pressas, och bottarna är produkten. |

**Totalt**

| | Manmånader | Totalt | Cash | Deferred | Recoup 2,5x |
|---|---|---|---|---|---|
| A0 + B0 | 28,5 | 3 420 000 | 2 394 000 | 1 026 000 | 2 565 000 |
| **A1 + B1** | **22,75** | **2 730 000** | **1 911 000** | **819 000** | **2 047 500** |
| A2 + B2 | 18,75 | 2 250 000 | 1 575 000 | 675 000 | 1 687 500 |

A1 plus B1 sparar **690 000 SEK**, alltså 20 procent. Break-even flyttar från cirka 142 000
sålda exemplar till **cirka 114 000**.

Mediabudgeten för creator-kampanjen (150 000 till 300 000) ligger kvar oförändrad ovanpå.
Den går inte att skära, eftersom 70 procent av wishlisten kommer utifrån Steam.

### Licenshygien

Asset Store- och Synty-licenser tillåter kommersiell användning, men villkoren skiljer sig
mellan evig licens och prenumeration, och vidaredistribution av källfiler är normalt
förbjudet. Gå igenom licensen för varje paket **innan** det hamnar i ett bygge som ska
levereras till kunden, inte efteråt. Lägg licensförteckningen som bilaga till avtalet.

---

## 9. Vad jag skulle fråga dem innan något signeras

1. **Vem äger IP:t idag, och finns det ett bolag?** Decket säger "grundarna". Det räcker
   inte för ett avtal med recoup och rev-share.
2. **Vad är kassan?** 2,4 MSEK cash över nio månader är det faktiska åtagandet. Två
   fastighetsmän kan absolut bära det, men det är inte samma sak som att de vill.
3. **Är de beredda att släppa de andra två koncepten tills vidare?** Deras deck säger
   uttryckligen "samtliga tre". Fokus på ett är en förutsättning för att det här ska funka.
4. **Vem är den kreativa beslutsfattaren?** Samma mandatproblem som på Disposable Corps.
   Två grundare som vill ha "aktiv kreativ medverkan" utan speldesignbakgrund är
   precis den konfiguration som bränner tid. Reglera det i avtalet, inte i efterhand.
5. **Trailern visar riggad förstörelse, inte gameplay. Är de bekväma med det?** Det är
   standard i lanen och fullt legitimt, men det måste vara ett medvetet gemensamt beslut.

---

## Källor

Steam-data hämtad live 2026-09-16 via `appreviews` med `language=all` och `appdetails`.

- [Polden Publishing](https://polden.gg/) - modell, tre steg, 150 000 USD snittinvestering
- [GamesBeat: Blue Ocean Games partners with Polden Publishing](https://gamesbeat.com/vc-fund-blue-ocean-games-partners-with-polden-publishing-on-data-driven-market-validation/) - portföljsiffror
- [Kirill Oreshkin på LinkedIn: wishlist-källor](https://www.linkedin.com/posts/kiroreshkin_what-are-the-main-sources-of-wishlists-for-activity-7466381362317385729-tvDZ) - 35/25/25/10/5-uppdelningen
- [Alinea Analytics: Another friendslop challenger enters the Steam arena](https://alineaanalytics.substack.com/p/another-friendslop-challenger-enters) - konverteringstal, prisstrategi
- [Naavik: How Sub-$200K Games Win Discovery and the Steam Algorithm](https://naavik.co/podcast/how-sub-200k-games-win-discovery-and-the-steam-algorithm/) - budgetband
- Grundarnas eget material: `fastighetskillar`-mappen, se CLAUDE.md
