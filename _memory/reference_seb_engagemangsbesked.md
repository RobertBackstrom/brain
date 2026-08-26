---
name: reference_seb_engagemangsbesked
description: "Var man beställer engagemangsbesked hos SEB, vad det kostar, hur SEB levererar det och varför filen inte går att öppna"
metadata: 
  node_type: memory
  type: reference
  originSessionId: d03f4a88-fd56-434d-9b6c-99e4b57c0e79
  modified: 2026-08-16T18:39:08.091Z
---

Engagemangsbesked (bankens sammanställning av bolagets tillgångar, skulder och säkerheter) begärs av
revisorn vid varje bokslut. Gäller alla Roberts SEB-bolag: AP, CZP, Runatyr.

**Beställs i Business Arena**, SEB:s företagsinternetbank. **200 kr per besked.** I beställningen
väljer man mottagare: en själv, revisorn direkt, eller båda, per post eller mail. Bekräftat av SEB:s
Anna Eklund 2024-06-10 och av seb.se 2026-08.

**Ange alltid revisorn som mottagare redan i beställningen.** AP:s besked per 2025-12-31 beställdes
utan det, gick bara till robert@aurorapunks.com och blev liggande medan revisorn tre gånger
efterlyste det. Det kostade två månader i revisionen 2026.

**SEB levererar det som "Audit Statement"**, inte som "engagemangsbesked". Avsändare
`SEBAuditStatements@seb.se`, ämnesrad `SEB Audit Statement for <BOLAG> per <datum> | Case ID <nnnnnnnn>`.
Sök alltså på **Audit Statement** eller Case ID i mailen, inte på "engagemangsbesked", annars ser det
ut att saknas.

**Filen går inte att öppna utan Microsoft-inloggning, och aldrig på VPS:en.** Bilagan
`<CaseID>_Email.pdf` är AIP-krypterad mot SEB:s egen RMS-tenant. Omslaget är en tom platshållarsida,
det riktiga dokumentet ligger inbäddat och krypterat. Innehållsnyckeln finns inte i filen och
rättighetslistan är själv krypterad, så det går inte ens att avgöra vem som får öppna den. Varje
läsare måste autentisera mot SEB:s RMS och hämta en use license. Microsofts läsare finns bara för
Windows, Mac, iOS och Android, **inte Linux**. Möjliga vägar för en mottagare: Edge 83+ inloggad med
arbetskonto, eller Microsofts gratis "RMS for individuals" om adressen saknar Entra ID (aurorapunks.com
ligger på Google Workspace och har ingen).

**Regeln:** lägg ingen tid på att knäcka filen. Beställ om med revisorn som mottagare, eller svara
`SEBAuditStatements@seb.se` med Case ID och be dem skicka om. Robert valde ombeställning 2026-08-16.

**Utfall, bekräftat 2026-08-25:** ombeställningen fungerade. SEB skickade Audit Statement för AP per
2025-12-31 (Case ID 100034432) till redovisningskonsulten `amer@book-it.se` 2026-08-17 08:46, han
vidarebefordrade samma dag till revisorn Christine Lef, som kvitterade samma kväll: "Det fungerar bra."
Tiden från ombeställning till kvitto var alltså en dag. Regeln står sig: ange mottagaren i beställningen,
och om det missas, beställ om i stället för att brottas med krypteringen. Det räcker att mottagaren har
Windows/Mac/Edge, vilket revisions- och redovisningsbyråer har.

Se [[reference_entity_accountants]] för vem som är revisor respektive redovisningskonsult per bolag,
och [[project_aurora_punks]] för AP:s bokslutsmapp.
