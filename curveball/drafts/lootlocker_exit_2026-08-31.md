# Behöver Curveball LootLocker?

Underlag inför svaret till Joel och Gustav, 2026-08-31. Mätt mot källkoden och den exporterade
Blueprint-logiken, inte uppskattat.

## 1. Hur djupt sitter det

| | |
|---|---|
| C++-filer som nämner LootLocker | 35, totalt 1 308 träffar |
| Blueprints som rör LootLocker | 50 av 635 |
| ... varav via The Gangs egen C++-wrapper | **45** |
| ... varav direkt mot SDK:t, förbi wrappern | **18** |

The Gang har redan lagt LootLocker bakom nio egna klasser i `Source/Mogadishu/*/LootLocker/`
(`LocalPlayerSubsystem`, `StoreSubsystem`, `FriendList`, `LookupPlayer`, `ApiQueue`, `JSONLibrary`,
`Helper`, `ServerGranter`, `ServerLoadoutValidator`). Det är en riktig söm, och den är vår att skriva
om i text som går att diffa.

De 18 som går förbi wrappern är den faktiska kostnaden, eftersom de är binära Blueprint-assets. Alla
utom en är meny- och ekonomiwidgets: `WB_Store`, `WB_BuyPopupBase`, `WB_BuyPopupResultBase`,
`WB_ListingButtonBase`, `WB_MyCurrency`, `WB_Loadout`, equip-menyerna, skin-varianterna,
`WB_PlayerProfile`, `WB_FriendList`, `WB_AddFriendPopup`, `WB_FriendProfilePicture`, `W_NextReward`.

**Det är inte "riv ut LootLocker överallt". Det är nio C++-klasser plus arton menywidgets.**

## 2. Vad som faktiskt ligger i LootLocker och inte i repot

Ur körloggen hämtar spelet vid start: `catalogs`, `GetAssetsByIds`, `ListCurrencies`,
`GetPlayerProgressions`, `GetWalletByHolderID`, `player/files`, `contexts`.

Definitionerna av vad de 38 vapnen, 11 skinsen och 14 förmågorna **är** som ägbara föremål ligger
alltså i LootLockers dashboard, inte i projektet. DataTables i repot är speltuning (deflect-tabeller,
skadekällor, botnamn), inte katalogen. Detsamma gäller progressionens nivåer och deras belöningar.

## 3. Det tidskritiska

Joel skriver att avtalet **inte är förlängt**. Tjänsten svarar ändå i dag, verifierat 28 och 31
augusti. Löper det ut förlorar vi två saker samtidigt: möjligheten att köra dagens bygge alls, och
den enda kopian av katalog-, asset- och progressionsdefinitionerna.

Slutsatsen är obekväm men enkel: **be om LootLocker-accessen nu och exportera definitionerna, även
om planen är att ta bort tjänsten.** Det kostar en timme och fönstret är begränsat.

## 4. Gustavs förslag

Gustav har rätt i huvudsaken. Går spelet från F2P till premium försvinner själva skälet till det
mesta av det här. Butiken, köp-popuperna, valutawidgeten och listing-knapparna har ingen funktion
när ingenting säljs i spelet. Det tar bort en stor del av de arton widgetarna av sig självt.

Tre saker som Steam Cloud inte täcker, och som är värda att säga innan vi svarar ja:

1. **Steam Cloud är inte auktoritativt.** Det synkar filer från spelarens disk. Deras egen kod har en
   `LootLockerServerLoadoutValidator`, alltså litade de inte på klienten med loadouts. Vapen och
   förmågor är loadout-föremål, så det här är en balansfråga och inte bara en kosmetisk.
2. **Det låser oss till Steam.** Steget "plattformsagnostiskt senare" blir då en ombyggnad vid det
   tillfället, inte en utbyggnad.
3. **Vänlistan följer med i beslutet.** LootLocker gör den i dag. För ett premiumspel på Steam är
   Steams egen vänlista och lobbyinbjudan en bättre passform ändå, och kodinbjudan du vill ha är
   vårt eget bygge oavsett.

## 5. Alternativet ingen har nämnt

**Steam Inventory Service.** Ingår i Steamworks, kostar inget, och är serverauktoritativt ägande av
föremål. Det ligger mellan Steam Cloud, som litar på klienten, och att bygga eget. Det är
Steam-låst precis som Cloud. Eftersom app-id:t ändå flyttar till AP är det vårt att konfigurera.

Rimlig delning: **Steam Cloud för inställningar och progression, Steam Inventory Service för vad
spelaren äger.** Då försvinner LootLocker helt utan att loadout-integriteten gör det.

## 6. Kopplingen till term sheetet

Att bygga eget backend höjer kostnaden. Det gör två olika saker beroende på vilket alternativ vi
landar i:

1. I **alternativ 1**, 50/50 utan recoup, finns ingen recoup. Varje extra vecka är då ren
   AP-kostnad som aldrig kommer tillbaka.
2. I **alternativ 2** är taket satt till 100 000 SEK, och den siffran sattes innan den här frågan
   fanns. Bygger vi backend måste taket upp, och då förhandlar vi för den struktur vi helst vill
   undvika.

**Den billigaste tekniska vägen är alltså också den som skyddar 50/50.** Det är ovanligt att de
sammanfaller, och det är ett argument värt att använda internt.

## 7. DLC-entitlements är inte samma sak som Inventory Service

Två olika system på Steam, och skillnaden avgör vilket som passar här.

**DLC-entitlements.** Varje föremål blir ett eget appid som spelaren **köper**. Ägandet kontrolleras
med `BIsSubscribedApp` eller `BIsDlcInstalled`. Det är köpformat. Det är rätt verktyg för ett fåtal
stora betalda saker, en supporter pack eller en expansion, och det är upplägget vi körde på Sir
Whoopass. Det är fel verktyg för 63 småföremål som spelaren **förtjänar** genom progression: det
skulle bli 63 butiksprodukter, och man kan inte dela ut en DLC för att någon spelat, man måste
faktiskt skänka ett paket.

**Steam Inventory Service.** Ett per-spelare-inventarium som Valve håller, med föremålen definierade
i ett JSON-schema. Föremål kan delas ut baserat på speltid eller på händelser i spelet. Det är
förtjänstformat, alltså exakt vad de 38 vapnen, 11 skinsen och 14 förmågorna är.

De utesluter inte varandra. Vill vi senare sälja en supporter pack är DLC rätt för den, samtidigt som
unlocksen ligger i Inventory Service.

## 8. Rättelse: grant-tjänsten blir inte onödig

Jag skrev tidigare i dag att grant-tjänsten från 27 augusti blir onödig. Det stämmer inte, och skälet
är värt att veta eftersom det ändrar kostnadsbilden.

Utdelning av föremål i Inventory Service går via `IInventoryService/AddItem`. Valves egen
dokumentation är tydlig: anropet **kräver en publisher key, måste ske från en säker server och får
aldrig göras från klienten**, just för att en nyckel i en klient alltid kan plockas ut. Anropet tar
dessutom ett `requestid` för idempotens.

Det är precis formen på tjänsten som redan är byggd och deployad: den håller den privilegierade
nyckeln, autentiserar värden, dedupliceras på `requestId` och har tak per match och per rullande
timme. Att byta ut `LootLockerClient` mot en `SteamInventoryClient` är en modul, inte ett nytt
system.

Kostnaden för "bygga eget" är alltså mycket lägre än den såg ut när frågan ställdes.

## 9. Rekommendation

1. **Ta bort LootLocker.** Steam Cloud för inställningar och progression, **Steam Inventory Service
   för vad spelaren äger**, Steams vänlista för det sociala. Kostar inget löpande.
2. **Dela ut föremål via grant-tjänsten**, inte från klienten. Den finns, den är testad, och Valves
   krav på en säker server med publisher key är samma krav den redan byggdes för.
3. **Behåll sömmen.** Ersätt LootLocker *bakom* The Gangs befintliga C++-wrapper i stället för att
   lägga Steam-anrop i widgetarna. 45 av 50 Blueprints går redan via wrappern. De 18 som går förbi
   bör pekas om mot den medan vi ändå är inne. Då är en framtida konsolport en ny implementation av
   nio klasser, inte en ny jakt på widgets.
4. **Be om LootLocker-accessen den här veckan** och exportera katalog, assets och progression innan
   avtalet hinner löpa ut.
5. **Svara Joel** att han inte behöver förhandla någon per-spelare-modell.
