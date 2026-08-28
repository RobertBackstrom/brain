# Mail till Olle + Joel (The Gang) - 2026-08-28

Tråd: Gmail `19e889144ac3e56a` ("Curveball"). Uppföljning på Olles svar 19 augusti.
Status: **utkast, väntar på Roberts godkännande innan det läggs som draft i Gmail.**

Syfte: rapportera att bygget är uppe och spelbart mot botar, konstatera att deras backend är borta,
och få ett beslut om vi laddar upp testbyggen på deras Steam-app eller ett eget hos oss.

---

Tja,

Kort läge: vi har fått igång bygget själva, det går att spela mot botar redan nu, och er backend
svarar inte längre. Det jag behöver från er är ett beslut om var vi lägger testbyggen.

**1. Bygget är uppe.**
Vi byggde UE 5.3 från källkod och kompilerade projektet, både editorn och speltargeten, utan att
något saknades. Zipen från 4 juni var alltså komplett, precis som du sa Olle. Vi har satt upp
versionshanteringen hos oss med er leverans som baseline, så allt vi gör framåt är en tydlig diff
mot exakt det ni skickade.

**2. Det går att spela nu, helt utan servrar.**
Startar man rakt in i en arena förbi menyn så streamas banan in, matchen rullar och botarna spawnar,
fem stycken i FFA. Bra läge för blast.tv-spåret: vi kan ge dem något att speltesta mot botar långt
innan multiplayern är på plats, om ni vill hålla den kontakten varm.

**3. LootLocker lever, er egen backend gör det inte.**
Kontodelen svarar fint, inloggning, valutor, inventory och kataloger fungerar. Men
`mlc-backend-dev.thegang.io` går inte ens att slå upp i DNS längre, så matchmaking, party och
inbjudningar är borta. Det är inget problem för oss, den delen ersätter vi ändå, men säg till om det
ligger något där som ni vill spara innan vi bygger om.

**4. Det jag behöver beslut om: var lägger vi testbyggen?**

Alternativ A, ert Steam-app. 2805120 har butikssidan och ni har redan playtest-branchen 2981120 och
demot 3371540. Ni lägger till oss som användare i ert Steamworks-konto och vi laddar upp på en egen
branch. Vi testar då mot rätt app-id och rätt depåer från början.

Alternativ B, ett eget app-id hos Aurora Punks. Går snabbare att komma igång och rör inte ert konto,
men blir en flytt senare om spelet ska säljas på er butikssida.

Jag lutar åt A. Går ni med på det behöver vi två saker: användaraccess till appen, och en Steam Web
API publisher key. Nyckeln är för att kunna verifiera spelarnas sessioner på serversidan när vi
byter ut den delen, annars får vi bygga en svagare lösning.

**5. En sak till på samma tema.**
Vi behöver också admin- eller serveraccess till LootLocker-spelet (`a86igukp`), för att kunna testa
att belöningar och inventory hamnar rätt när serverdelen byts ut. Den frågan ligger kvar sedan
förra mailet.

/Robert
