# Följenotering till publishing-avtalet med The Gang

Gäller `publishing_agreement_thegang_2026-09-01.md`, skrivet 2026-09-01. Den här filen går
**inte** till motparten.

## 1. Vad som är lånat varifrån

| Del av avtalet | Källa |
|---|---|
| Övergripande struktur, partsblock, Background/Whereas, definitionsled, IP-sektionen, indemnity, liability, General Provisions | `Publishing_Agreement_Client_AuroraPunk_Template` (Distant Bloom-arvet, `1SCNUNc9jf…`) |
| Formuleringen om att part får anlita partner och underleverantörer efter eget val men ska notifiera motparten | Co-Publishing MASTER (Water Me & You, `1-MbTmYhBb…`), sektion "Agreements with 3rd party". Kraftigt omskriven, se punkt 3 nedan |
| Audit-klausulens mekanik (en gång per kalenderår, tio dagars varsel, auktoriserad revisor, kontorstid, 5 %-tröskeln) | Båda mallarna. Riktningen är omvänd, se punkt 3 |
| Recoupable expenses-apparaten, portingansvar, marknadsföringsåtaganden, Exhibit A och Exhibit B | **Medvetet inte lånat.** Se punkt 3 |
| Allt kommersiellt innehåll (100 000 SEK recoup, 30/70, Steam-appflytten, källkodsöverlämning, tolvmånadersfristen, konsol/mobil) | `term_sheet_2026-08-31.md` plus Roberts beslutslista 2026-09-01 |
| Teknisk leveransbeskrivning i 3.1 och LootLocker-accessen i 4.3 | `lootlocker_exit_2026-08-31.md` |

Distant Bloom-avtalet (`1Qz-T29UDpZ…`) hämtades inte separat. Mallen `1SCNUNc9jf…` är enligt
uppgift härledd ur samma dokument och innehåller dessutom signerad avtalstext ordagrant, så en
tredje läsning tillförde inget. **Nämn det för advokaten om han vill se den signerade förlagan.**

## 2. Fält som saknas och måste fyllas i innan utskick

1. **The Gang Studio AB org.nr.** Finns inte någonstans i masterbrainen. RAG-sökning på bolagsnamn,
   adress och Joel gav bara mailsignaturer. Hämtas från allabolag eller frågas Joel.
2. **Bolagsnamnets exakta lydelse.** Vi använder "The Gang Studio AB". Mailsignaturen skriver
   "The Gang Studio", domänen är `thegang.io`, LinkedIn-sidan heter "The Gang Sweden". Det är inte
   säkert att det juridiska namnet är någon av dem. Verifiera mot registreringsbeviset samtidigt
   som org.nr.
3. **The Gangs firmatecknare**, namn och titel, samt om firman tecknas ensam eller i förening.
4. **Notisadress för The Gang** i punkt 18.7.
5. **Andra AP-undertecknaren.** AP:s firma tecknas två i förening av ledamöterna
   ([[reference_company_structure]]). **Robert kan alltså inte signera det här ensam.** Signaturblocket
   är byggt för två AP-signaturer. Välj medtecknare bland Mattias, Alexander, Andreea eller KM.
6. **Datum för undertecknande.**

## 3. Vad som skiljer mot Distant Bloom och Water Me & You, och varför

1. **Riktningen på pengaflödet är omvänd.** I båda förlagorna är utvecklaren säljande part på PC
   och AP fakturerar dem. Här tar AP emot pengarna från Valve och rapporterar och betalar till
   utvecklaren. Följden är att rapporteringsplikten, betalningsplikten och **granskningsrätten
   pekar mot AP** i stället för mot motparten. Förlagornas dubbelriktade audit-klausul är ersatt av
   en enkelriktad, eftersom The Gang inte har något att rapportera.
2. **Ingen recoupable-expenses-apparat.** Förlagorna har QA-tak, lokaliseringstak, portingtak på
   50 000 USD och 15 procents påslag på marknadsföringskostnader. Här finns en enda siffra,
   100 000 SEK, och inga kostnader alls dras av före delning. Det är den enskilt största
   förenklingen och den är avsiktlig: Joel bad om något enkelt, och AP tar ingen köpt media.
3. **Co-publisher-klausulen är omvänd mot WMAY.** WMAY-mallen säger bara att part får anlita
   partner och ska notifiera motparten "om det kan påverka vinstdelningen". Vår version (sektion 7)
   säger uttryckligen att en co-publisher betalas **ur AP:s egen andel**, att The Gangs 70 procent
   inte påverkas, att recoup-beloppet inte höjs, och att ingen omförhandling krävs. Det är
   starkare för AP och samtidigt tydligare skydd för dem, vilket är själva poängen.
   LUG är inte namngiven någonstans i avtalet.
4. **Ingen porting, ingen marknadsföringsbilaga, ingen Exhibit A eller B.** Förlagorna hänger hela
   åtagandet på två bilagor. Här står åtagandena i sektion 3 och 4 i löpande text, fem punkter
   vardera. Avtalet blev fyra sidor i stället för tjugoåtta.
5. **Tvistlösning: Stockholms tingsrätt, inte SCC-skiljedom.** Båda förlagorna har
   skiljeförfarande hos Stockholms Handelskammare. Roberts beslut är allmän domstol. Det är
   billigare vid en liten tvist och rimligt givet storleken på affären, men det är också
   offentligt. Medvetet val, värt att nämna för advokaten.
6. **Löptiden är inte tio år.** Förlagorna löper tio år eller tills intäkterna understiger 100 USD
   i tre månader. Här gäller intäktsdelning i perpetuitet med en tolvmånaders lanseringsfrist som
   enda tidsgräns.
7. **Källkodsklausulen finns inte i någon förlaga.** Sektion 10 är ny och kommer ur att AP håller
   mainline. Vendor-baselinen från 4 juni nämns i avtalstexten, vilket är avsiktligt: den gör
   "AP:s ändringar" till något mätbart i stället för en tolkningsfråga.
8. **Steam-appflytten finns inte i någon förlaga.** Hela sektion 5 är ny.

## 4. Vad jag är osäker på, i fallande ordning

1. **Punkt 12.5, vad som händer med AP:s intäktsandel vid uppsägning som inte beror på utebliven
   lansering.** Term sheetet svarar inte på det. Jag har skrivit att andelen **överlever**
   uppsägning, utom när The Gang säger upp enligt 11.2 (ej lanserat inom tolv månader) eller på
   grund av AP:s icke rättade väsentliga avtalsbrott. Logiken är att AP:s investering är gjord i
   arbete och därför inte ska kunna nollställas av en uppsägning, men att AP inte ska belönas för
   eget avtalsbrott. **Detta är mitt förslag, inte Roberts beslut. Bekräfta innan utskick.**
2. **Perpetuitet utan utköpsklausul.** Samma flagga som i term sheetet. En motpart som senare vill
   sälja bolaget eller IP:t vill normalt kunna köpa ut en evig intäktsandel. Ingen sådan klausul
   finns, avsiktligt. Räkna med att The Gangs eventuella rådgivare tar upp det.
3. **Exklusiviteten i 2.1.** Term sheetet säger inte uttryckligen att utgivningsrätten är exklusiv.
   Jag har skrivit exklusiv, eftersom appen flyttar till AP och The Gang då rent praktiskt inte kan
   publicera parallellt. Om Robert vill hålla det öppnare stryks ordet "exclusive".
4. **Tolvmånadersfristen.** Oförändrad flagga från term sheetet: siffran är satt som rimlig
   utgångspunkt, inte mot en verklig tidplan.
5. **Vad som händer med spelarna vid hand-back.** Avtalet reglerar appen, önskelistorna och
   följarna, men inte konton, progression eller inventarier i den tjänst AP driver. Efter
   LootLocker-utgången ligger ägandet i Steam Inventory Service, som följer appen, och progressionen
   i AP:s grant-tjänst, som inte gör det. **Det saknas en mening om att AP vid upphörande lämnar ut
   progressionsdata i maskinläsbart format.** Jag har medvetet inte lagt in den för att inte öppna
   ett tekniskt spår i ett avtal som ska vara enkelt, men den bör in i nästa version.
6. **Momsen.** Ingenting sägs om moms på utbetalningarna till The Gang. Två svenska bolag,
   fakturaflöde, så det borde vara rakt, men AP är **inte momsregistrerat** enligt Skatteverkets
   svar 2026-08-27 (se admin-learnings, apb-056). Det är en riktig fråga för revisorn, inte för
   advokaten, och den påverkar hur betalningen i 8.2 faktiskt går till.
7. **Steam Web API publisher key i 4.2.** Den behövs för grant-tjänstens ticketverifiering och blir
   överflödig när appen väl flyttat. Formuleringen "fram till att överföringen är genomförd" täcker
   det, men om överföringen dröjer är nyckeln det enda som gör att AP kan jobba vidare.

## 5. Juridisk granskning, det jag vill att en advokat tittar på

1. Punkt 12.5 enligt ovan.
2. Att en evig intäktsandel utan bortre gräns håller när avtalet i övrigt kan sägas upp.
3. Indemnity- och ansvarsbegränsningen i 16 och 17. De är nedkortade ur förlagan och det är oklart
   om nedkortningen tappat något AP behöver.
4. Om exklusiviteten i 2.1 behöver kompletteras med en formulering om att The Gang avstår från att
   själv publicera på PC under löptiden.
5. Formkravet för själva undertecknandet givet AP:s firmateckning i förening.

## 6. Process

Signering går via OpenSign (`sign.runatyr.games`), enligt [[reference_digital_signatures]]. Notera
att det blir **tre undertecknare** om AP tecknar två i förening, alltså ordnad signering med The
Gang sist eller först beroende på vad Robert vill.
