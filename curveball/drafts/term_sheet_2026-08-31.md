# Curveball: term sheet

| | |
|---|---|
| **Parter** | Aurora Punks AB (559256-9718), nedan AP, och The Gang Studio AB, nedan The Gang |
| **Datum** | 2026-08-31 |
| **Status** | Icke-bindande sammanfattning av kommersiella villkor. Bindande verkan uppstår först genom ett undertecknat avtal, med undantag för punkt 12 om sekretess |

## 1. Bakgrund

The Gang äger Curveball. Spelet är färdigutvecklat men aldrig lanserat, och den backend det byggdes mot är avvecklad. AP har byggt om projektet från källkod, versionshanterar det och har verifierat att det går att spela.

Det här dokumentet beskriver hur parterna tar spelet till marknad. Det finns i två varianter, en utan extern finansiär och en med Light Up Games, nedan LUG.

## 2. AP:s åtagande

1. Färdigställa bygget för PC. Det omfattar att ersätta de dedikerade servrarna med spelarhostad multiplayer, flytta de serverauktoritativa LootLocker-anropen till en tjänst AP driver, samt den polering som krävs för lansering.
2. Publicera spelet på Steam och sköta butikssida, uppdateringar och lanseringsplan.
3. Ta fram och driva en plan för community traction.
4. AP står för sina egna kostnader. **Ingen köpt marknadsföring ingår**, och ingen part åtar sig en mediabudget. Vill någon part lägga betald media krävs skriftlig överenskommelse om vem som betalar och hur det behandlas.

Arbetet utförs av AP. Anlitar AP underleverantör svarar AP för den fullt ut.

## 3. The Gangs åtagande

1. Upplåta de rättigheter till Curveball som krävs för att AP ska kunna utföra punkt 2, för PC världen över, under avtalets löptid.
2. Ge AP användaraccess till Steam-app 2805120 samt en Steam Web API publisher key.
3. Ge AP admin- eller serveraccess till LootLocker-spelet `a86igukp`.
4. Svara på tekniska frågor om koden i rimlig omfattning. Något löpande utvecklingsåtagande ingår inte.

The Gang behåller äganderätten till Curveball och allt underliggande material. AP får ingen äganderätt till spelet.

## 4. Utgivning och pengaflöde

Spelet säljs på The Gangs befintliga Steam-app **2805120**, som redan bär butikssida, önskelistor och historiken från demot och NextFest. Valve betalar därmed till The Gang.

Nettointäkt definieras som vad The Gang faktiskt får från Valve för Curveball, alltså efter Valves andel, återbetalningar, chargebacks och plattformsskatter. Varken The Gangs eller AP:s interna kostnader dras av innan delning, med undantag för det som anges i alternativ 2 nedan.

## 5. Intäktsdelning, utan LUG

Två alternativ. **AP föredrar alternativ 1.** Det ger båda sidor samma incitament under hela spelets livslängd och tar bort all administration kring recoup-redovisning.

### Alternativ 1: rak delning

| | |
|---|---|
| Recoup | Ingen |
| Delning av nettointäkt | **50 % AP, 50 % The Gang, från första kronan och därefter i perpetuitet** |

The Gang får betalt från dag ett och har ingen kostnad, ingen risk och inget belopp att räkna av först.

### Alternativ 2: recoup före delning

| | |
|---|---|
| Recoup | AP återtar **100 000 SEK** ur nettointäkten innan delning påbörjas |
| Delning därefter | **30 % AP, 70 % The Gang, i perpetuitet** |

Det här är den struktur parterna diskuterade den 30 juni, då med LUG i bilden. Beloppet 100 000 SEK är samma siffra som kommunicerades då.

### Vad skillnaden faktiskt betyder

Med nettointäkt R gäller att The Gang får 0,50 × R i alternativ 1 och 0,70 × (R minus 100 000) i alternativ 2. Alternativen är lika stora vid **R = 350 000 SEK**.

Under 350 000 SEK i nettointäkt tjänar The Gang mer på alternativ 1. Över den nivån tjänar The Gang mer på alternativ 2. För AP gäller exakt det omvända, med samma brytpunkt. Valet är alltså ett rent riskbyte och inte en fråga om vem som får mest.

## 6. Intäktsdelning, med LUG

Kommer LUG in som finansierings- och marknadsföringspartner gäller strukturen från den 30 juni:

1. AP och LUG återtar sina faktiska nedlagda kostnader till 100 % ur nettointäkten.
2. Därefter delas nettointäkten **70 % The Gang, 30 % AP och LUG**, i perpetuitet.
3. Fördelningen av de 30 procenten mellan AP och LUG regleras i separat avtal mellan AP och LUG och påverkar inte The Gangs andel.

LUG:s inträde förutsätter att alla tre parter skriver på. Sker det inte gäller punkt 5.

## 7. Källkod och rättigheter till arbetet

AP håller källkoden i ett privat versionshanterat repo. The Gangs leverans från 4 juni 2026 ligger orörd som baseline, så allt AP tillfört går att läsa ut som en avgränsad ändringsmängd.

The Gang har rätt att när som helst få ut hela den aktuella källkoden inklusive AP:s ändringar, utan kostnad och inom tio arbetsdagar. Vid avtalets upphörande sker överlämningen automatiskt.

AP behåller rätten till de generella verktyg och tjänster AP byggt och som inte är specifika för Curveball, exempelvis grant-tjänsten. The Gang får en fri och obegränsad licens att använda dem för Curveball.

## 8. Rapportering och betalning

1. The Gang rapporterar nettointäkten kvartalsvis och betalar AP:s andel inom 30 dagar från kvartalets slut.
2. AP har via sin Steamworks-access rätt att se försäljningsdata direkt och stämma av mot rapporten.
3. AP har rätt att en gång per år på egen bekostnad låta granska underlaget. Visar granskningen en avvikelse till AP:s nackdel över 5 % står The Gang för kostnaden.

## 9. Konsol och mobil

Det här avtalet gäller PC via Steam. Andra plattformar ingår inte. AP har rätt att först förhandla om dem, i 60 dagar från det att The Gang meddelar att en sådan version är aktuell.

## 10. Löptid och avslut

1. Avtalet gäller från undertecknande. Intäktsdelningen gäller i perpetuitet för de intäkter spelet genererar.
2. Har AP inte lanserat spelet inom **tolv månader** från undertecknande har The Gang rätt att säga upp avtalet skriftligt. Sker det upphör AP:s rätt att publicera, källkoden lämnas över enligt punkt 7, och AP har ingen kvarvarande intäktsandel.
3. Väsentligt avtalsbrott som inte rättas inom 30 dagar från skriftlig anmodan ger den andra parten rätt att säga upp avtalet.
4. Punkterna 7, 8 och 12 gäller även efter att avtalet upphört.

## 11. Kredd och marknadsföring

Spelet krediteras The Gang som utvecklare och AP som utgivare. Båda parter får använda spelet i sin egen marknadsföring och referenslista.

## 12. Övrigt

1. Vardera part står för sina egna kostnader fram till undertecknande.
2. Villkoren i det här dokumentet är konfidentiella och får inte delas utanför parterna, med undantag för rådgivare och potentiella finansiärer under sekretess.
3. Svensk rätt. Tvist avgörs av Stockholms tingsrätt.

---

## Att ta ställning till innan detta går ut

1. **Tolvmånadersfristen i punkt 10.2.** Den är satt av mig som en rimlig utgångspunkt, inte utifrån en tidplan. Vi har ingen estimering av färdigställandet som vilar på den lästa Blueprint-logiken än, så siffran bör stämmas av mot en verklig plan innan den blir bindande.
2. **Granskningsrätten i punkt 8.3** är standard men kan uppfattas som misstroende mot en motpart ni känner väl. Den är också AP:s enda skydd mot felrapportering, givet att pengarna landar hos dem först.
3. **Perpetuitet i båda alternativen.** Det är vad du bad om. Värt att veta är att en motpart som senare vill sälja bolaget eller IP:t ofta vill kunna köpa ut en evig intäktsandel. En utköpsklausul finns inte med här, och det är avsiktligt.
4. **Juridisk granskning.** Det här är ett term sheet, inte ett avtal. Fullavtalet bör gå via Lawyer och en riktig advokat innan signering.
