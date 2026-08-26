# Xbox / Microsoft Partner Center - entitetsflytt till CZP

**Datum:** 2026-08-26
**Ärende:** apb-051 (rättighetskedjan) · syskon: apb-026 (Steam, klar), apb-015 (PlayStation), Nintendo (utkast skickat till granskning)
**Master:** `umbrella/aurora_punks/legal/apds_entity_transfer_master_2026-08-26.md`
**Status:** kartlagt, inte påbörjat. Robert satte ordningen Nintendo -> PlayStation -> Xbox 2026-08-26.

---

## 1. Xbox är inte samma problem som Steam och PlayStation, och antagandet måste rättas först

Mitt första utkast i mastern skrev att "APDS har en egen Microsoft-tenant" och att produktlistan
låg under APDS. **Det är inte belagt, och sannolikt fel.** Det som faktiskt finns i materialet:

1. **Ett Partner Center-konto som heter "Aurora Punks"**, med Owner-MSA
   `andreassonhektor@gmail.com` (Hektor Andreasson) och `finance@aurorapunks.com` som Manager.
   Robert har återfått access på Manager-kontot. `robert@aurorapunks.com` är Developer och kan
   inte tilldela roller.
2. **Kontot innehåller flera AP-titlar utöver Sir Whoopass.** Det är precis vad som sänkte
   MSA Transfer-spåret i `swa-002`: en hel-kontoöverlåtelse hade dragit med allt.
3. **Azure-appregistreringarna för WLBS och APDS** i `IndieBI app.txt` är API-credentials för
   säljdata, inte bevis på vem som äger Partner Center-kontot. Jag blandade ihop dem.
4. **Mailet från `idsetup@xbox.com` 2022-04-12 säger att båda kontona bar
   "White Lines Black Spaces AB as the legal entity name".** WLBS gick i konkurs 2024-09-25.
   Om den strängen aldrig uppdaterades står Partner Center-kontot i ett konkursat bolags namn,
   två konkurser bakåt i kedjan.

**Fråga 1, och den avgör hela spåret: vilket bolagsnamn står det på kontot idag?** WLBS, APDS,
Aurora Punks AB eller CZP. Allt annat följer av svaret, och den läses på tio minuter i Partner
Center under Account settings.

## 2. Varför Xbox sannolikt ska lösas tvärtom mot Steam

Steam-frågan var "företagsuppdatering på samma konto, eller flytt app för app till ett nytt
konto", och det blev flytt app för app. **På Xbox lutar allt åt motsatt svar.**

- **Per-produkt-reparenting är fryst.** MSA V2-produkter, alltså allt skapat efter mars 2022, kan
  inte flyttas mellan Partner Center-konton. Microsoft engineering har frusit funktionen utan ETA.
  Bekräftat via Reed Hunt i `swa-002`, och det höll i sig från juni till augusti 2026.
- **Alla titlarna på kontot tillhör samma förvärvade rörelse.** Det som gjorde
  hel-kontoöverlåtelsen olämplig för Sir Whoopass var att SW skulle bort medan resten stannade.
  Här är läget det omvända: hela kontot ska följa med till CZP.

Slutsatsen: **be Microsoft ändra den juridiska personen på det befintliga kontot till CZP, i
stället för att flytta produkter.** Det kringgår V2-frysningen helt, eftersom ingenting reparentas.
Det är också det enda spåret som är förenligt med att Sir Whoopass ligger kvar under kontot som en
scoped invite till Atomic Elbow, en workaround som förutsätter att kontot inte rivs isär.

**Konsekvens att ta höjd för:** en ändring av juridisk person drar med sig Sir Whoopass, som redan
är sålt till Atomic Elbow via TLA med verkan 2026-02-01. AE:s access är en inbjudan scopad till
SW-produktgruppen, inte ett ägande. Det tål en entitetsändring, men Reed och Niklas bör informeras
innan den görs, inte efter.

## 3. Ordningen

1. **Läs Partner Center.** Logga in som `finance@aurorapunks.com` (Manager). Ta ut: juridiskt
   bolagsnamn och org.nr på kontot, full produktlista, MSA V1 eller V2 per produkt, payee- och
   bankuppgifter, samt vilka tenants som är associerade. Utan detta är allt nedanför gissningar.
2. **Kontrollera payee.** Samma fråga som på Nintendo och Steam: går pengarna till ett konkursat
   bolag? Det är den enda posten här som kan blöda pengar just nu.
3. **Kontakta Reed Hunt** (`v-reedhunt@microsoft.com`, ID@Xbox / Hanson Consulting) i en **ny
   tråd**, inte i Sir Whoopass-tråden `19ddfcc812e25c3a`. Fråga rakt: vilken process gäller när
   den juridiska personen bakom ett Partner Center-konto har förvärvats, och kan bolagsnamnet
   och bankuppgifterna på kontot ändras utan att produkterna reparentas. Reed har varit rak och
   hjälpsam genom hela SW-ärendet och är rätt ingång.
4. **Bifoga kedjan** när Microsoft frågar: `Rörelseöverlåtelseavtal` APDS konkursbo till Bright
   Gambit (Drive `10ZN-_9YckcvVJDBGV-5szGsAlaI_f-SQ`) plus
   `Asset_Transfer_Agreement_BrightGambit_CreationZeroPoint` (Drive
   `1nYJ_Vp7rnxcrJrWqMQ-43lHPKwLmpsBz`).
5. **Informera Niklas Karlsson på Atomic Elbow** innan en entitetsändring genomförs, av samma skäl
   som i avsnitt 2.

## 4. Blockerare

- **Creds saknas i `assistant/.env`.** Ingenting för Microsoft, och `finance@aurorapunks.com` bär
  MFA via Authenticator efter att SMS blockerats av Microsofts telefonrenommé-spärr (err 399287).
  Playwright finns på Nitro och fungerar, men en MFA-inloggning kan inte automatiseras utan att
  TOTP-secreten finns. **DevOps: promota Microsoft-creds plus TOTP till env**, annars måste steg 1
  köras manuellt av Robert.
- **Sir Whoopass-workarounden är inte stängd.** `swa-002` väntar fortfarande på att Atomic Elbow
  bekräftar att de ser SW och inte AP:s övriga titlar. Rör inte kontostrukturen förrän det är
  bekräftat, annars blandas två felsökningar ihop.

## 5. Formulering

Bilaga 2 anger AP AB som IP-ägare till flera av titlarna. Skriv därför att CZP förvärvat rörelsen
med tillhörande publicerings- och distributionsrättigheter, inte att CZP äger IP:t. Se mastern
avsnitt 2.
