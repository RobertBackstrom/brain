# Curveball: blueprint-svepet, Phase 0-checkpointen

| | |
|---|---|
| **Datum** | 2026-09-08 |
| **Författare** | GameDev-agenten |
| **Underlag** | `code-corpus/repos/curveball-bba/BlueprintExports/` (WP0.3-exporten 2026-08-28, 635 paket, 243 MB) + `Source/Mogadishu/` |
| **Uppdrag** | Besvara öppen fråga 5 och 6 i [dev_plan_p2p_steam.md](dev_plan_p2p_steam.md) §12, och om-estimera WP1.2 och WP1.3 mot exporten i stället för mot gissningar |
| **Metodgräns** | Allt under rubriken "verifierat" är läst i exporten eller i C++-koden. Allt annat är märkt som bedömning eller som icke avgörbart |

## 1. Sammanfattning, nya estimat först

1. **WP1.2 matchmaking-omkoppling: 24 till 36 timmar, centralt 28 h.** Var 24 till 40 h med låg tillförsikt. Tillförsikten är nu medelhög till hög. Skälet är mätt: bara **fem** blueprints rör `UMatchmakingSubsystem`, och av dem konsumerar **bara `BP_GameInstance`** fälten `IP`, `Port` och `PlayerSessionId` ur `FStatusUpdateEvent`. De fyra menywidgetarna läser enbart `Status`, `EstimatedWaitTime`, `QueuedPlayerCount` och `MatchmakingStartedAt`, alltså kan de lämnas helt orörda om signaturen fryses. Hela resan-in-i-matchen ligger i **en enda blueprintgraf**, `BP_GameInstance:GameLift`.
2. **WP1.3 party och inbjudningar: 32 till 52 timmar, centralt 40 h.** Var 40 till 60 h och kallades "largest single unknown". Den formuleringen håller inte. Den stora widgetmassan som planen fruktade är **vänlistan, och den hänger på LootLocker, inte på The Gangs backend**, alltså följer den inte med i en Steam-lobbyflytt. De hårda beroendena på `UBackendMessagePump` är **sju filer**, varav tre icke-triviala.
3. **Öppen fråga 5 är besvarad.** Grant-anropen finns på **fem ställen i fyra blueprints**, och match-slut-flödet är spårat nod för nod. Viktigaste fyndet: utdelningen är gatead på `IsDedicatedServer`, alltså **slutar ett listen-server-bygge dela ut belöningar helt tyst** i stället för att dela ut dubbelt.
4. **Öppen fråga 6 är besvarad.** Det finns **inga achievements** någonstans, varken egna, Steams eller LootLockers. Statistiken finns och sitter i `BP_StatTrack`, med en separat GameAnalytics-telemetrigren i `BP_GameAnalytics`. Inga leaderboards används.
5. **Följdeffekt på WP2.2:** alla blueprintanrop mot `LootLockerServerLoadoutValidator` är läsande accessorer med samma signatur, alltså krävs noll blueprintändringar om C++-sidan skrivs om bakom oförändrat gränssnitt. Bandet kan snävas till 8 till 14 h.
6. Hela projektets blueprintlogik är **31 587 grafnoder över 635 paket**. "5 GB oläst logik" är alltså en läsbar mängd, och den delen av planens riskspråk kan tas bort.

## 2. Så ska exporten läsas, tre fällor som annars ger fel svar

Det här är operativt och gäller alla som greppar i `BlueprintExports/` framöver.

1. **Varje funktionsgraf finns två gånger.** T3D:n innehåller både den redigerade grafen och en kompilerad kopia med suffixet `_MERGED`, plus `ExecuteUbergraph_<BP>` som är en tredje kopia av EventGraph. En rå `grep -c` på ett funktionsanrop ger därför ungefär **dubbla** antalet riktiga noder. Filtrera bort `_MERGED` och `ExecuteUbergraph_` innan du räknar.
2. **Sex av 635 filer är blandad teckenkodning.** `WB_LandingPage`, `WB_MyCurrency`, `WB_CreditPerson`, `ProcessParams`, `WB_ListingButtonBase` och `WB_ET_TrapStep` börjar med UTF-16-BOM och innehåller både UTF-16- och ASCII-partier i samma fil. Varken en vanlig grep eller en naiv UTF-8-läsning ser hela filen. Normalisera med `tr -d '\000\r'` och kasta BOM:en först.
3. **DataTables innehåller ingen data.** Alla 20 tabeller föll tillbaka på objekt-T3D, och den exportören skriver bara `RowStruct` och `RowStructPathName`, cirka 1 kB per fil. Det betyder att `DT_MatchMakingConfigurationNames`, `DT_StatTable`, `DT_CurrencyIDMapping`, `DT_StoreListings` och `DT_AssetIDBlueprintMappings` är **tomma på rader** i exporten. De 40 raderna i `_failures.log` är samma 20 tabeller gånger två försök, csv och json.

Utöver det saknas **user-defined structs och enums** helt i exporten (38 `S_*` och 12 `E_*` i `_ASSET_MANIFEST.txt`, noll i exporten), liksom **179 `.umap`** och därmed eventuella level blueprints. Fyra `GA_*`-abilities av 27 saknas också. Blueprint- och widgettäckningen är i övrigt fullständig.

## 3. Öppen fråga 5: grant-flödet och varje blueprintanropsställe

### 3.1 Anropsställena, verifierat

| Fil | Klass och typ | Anrop | Graf | Gameplay eller meny |
|---|---|---|---|---|
| `Game/Blueprints/TemporaryBps/BP_StatTrack.T3D` | `BP_StatTrack`, en `ActorComponent` som sitter på `BP_PlayerState` | `ULootLockerServerGranter::AddCurrencyToPlayer` x1, `AddProgressionForPlayer` x2 | `EventGraph` | **Gameplay.** Detta är hela utdelningen |
| `Game/HUDMenu/Widgets/WB_MyCurrency.T3D` | WidgetBlueprint | `ULootLockerServerGranter::GetMaxAllowedCurrency` x2 | `EventGraph` + `UpdateCurrency` | **Ekonomiwidget.** Ren läsning av taket, `BlueprintPure` mot CDO:n, inget serveranrop |
| `Game/Blueprints/GameInstance/BP_LootLocker.T3D` | GameInstance-basklass | `ULootLockerServerLoadoutValidator::PlayerProfileChanged` x1, `GetPlayerData` x1 | `EventGraph` | GameInstance, alltså varken meny eller match |
| `Game/Blueprints/PlayerState/BP_PlayerState.T3D` | `PlayerState` | `LootLockerServerLoadoutValidator::GetPlayerData` x2 | `EventGraph` | **Gameplay** |
| `Game/Blueprints/Characters/BP_PlayerCharacter.T3D` | ärver `MogadishuCharacter` | `LootLockerServerLoadoutValidator::GetPlayerData` x3 | `AbilitySystem` x1, `BeginPlay` x2 | **Gameplay** |

Två saker till, båda verifierade:

1. **`GrantAssetsToPlayer` har noll blueprintanrop.** Av granterns tre skrivande funktioner (`GrantAssetsToPlayer`, `AddCurrencyToPlayer`, `AddProgressionForPlayer`, se `Source/Mogadishu/Public/LootLocker/LootLockerServerGranter.h:37-44`) används alltså bara två från blueprint. Grant-tjänstens skarpa yta är mindre än specen antog.
2. **Validatorns blueprintanrop är alla läsande.** `GetPlayerData` och `PlayerProfileChanged` hämtar cachad profildata. Ingen blueprint anropar `CheckAndFix` eller `MakeSafeServerData`.

### 3.2 Flödet vid matchslut, verifierat nod för nod

Kedjan i `BP_StatTrack` är spårad genom exec-länkarna i `EventGraph`:

```
GS_Default byter tillstånd
  -> BP_StatTrack::StateRoundWInner (custom event, ej replikerad)
     -> ExecutionSequence -> AddRoundStat (flera) -> sätter ServerStatTime
        -> PostToLootLocker (funktion)
           -> Branch pa KismetSystemLibrary::IsDedicatedServer
              true -> EventPostStatsToLootLocker (custom event, ej replikerad)
                 -> cast + IsValid -> ForEachLoop over TotalStatsToSubmit
                    -> per stat: GetXPStatRewardAmount + GetCurrencyStatRewardAmount
                       -> Branch -> LootLockerServerGranter::AddProgressionForPlayer
                    -> loopen klar -> AddProgressionForPlayer -> AddCurrencyToPlayer
                       -> sätter TotalXPToSubmit / TotalCurrencyToSubmit
        -> UpdateToasterMulticastEvent (FunctionFlags 0x0D0200C0, alltså Net + Reliable
           + NetClient, det vill säga "Run on owning Client", trots namnet)
```

Fyra konsekvenser, i fallande ordning av betydelse för planen:

1. **Grinden är `IsDedicatedServer`, inte `HasAuthority`.** Under en listen server returnerar den falskt, alltså går `PostToLootLocker` in i sin falska gren och **ingenting delas ut**. Felet blir "spelarna får aldrig XP eller valuta", inte "spelarna får dubbelt". Det är en tyst regression som inte syns i en kort speltest, och den ligger i kundens blueprint, inte i C++. Fixen är att byta villkoret till värdauktoritet, en nod, men den måste in i WP2.1 explicit.
2. **Utdelningen är per `PlayerState`, en gång per spelare.** `BP_StatTrack` är en komponent på `BP_PlayerState`, alltså kör värden loopen en gång per ansluten spelare. Det är rätt form för en värdbaserad rapportör och behöver ingen omstrukturering.
3. **Klienten får inte veta om utdelningen i matchen.** Belöningsvisningen sker när spelaren är tillbaka i menyn: `WB_MainMenu` binder `LootLockerLocalPlayerSubsystem::OnProgressionUpdated` och `OnNewlyGrantedAssets` och anropar `FetchNewlyGrantedAssets`. Grant-tjänsten får alltså vara asynkron utan att UI:t behöver röras.
4. **`UpdateToasterMulticastEvent` är felaktigt namngiven.** Flaggorna säger owning client, inte multicast. Bara den egna spelaren ser sin toast. Ingen åtgärd behövs, men namnet leder fel i en felsökning.

Ett förbehåll: i `EventGraph` pekar `IfThenElse_3` framåt mot `AddProgressionForPlayer`-noden `CallFunction_20` medan `CallFunction_10`, som också är `AddProgressionForPlayer`, listar samma branch på sin ingående exec-pin. T3D:n är alltså inte entydig om vilken av de två progressionsnoderna som sitter i loopkroppen och vilken som sitter efter loopen. Det går inte att avgöra ur texten och behöver en blick i editorn. Antalet anropsställen är däremot entydigt.

## 4. Öppen fråga 6: achievements och stats

### 4.1 Achievements: finns inte

Verifierat negativt på tre nivåer.

1. Ordet "achievement" förekommer **noll gånger** i hela blueprintexporten.
2. I `Source/` förekommer det bara i konfiguration: `Config/DefaultEngine.ini:316` `bMirrorAchievementsToEOS=False` och `Config/Windows/Custom/Epic/WindowsEngine.ini:12` `bEnableAchievements=true`, båda EOS-artefakter från `TGEAC`-pluginet som tvingar på `OnlineSubsystemEOS`. Ingen kod läser dem.
3. Noll anrop mot `WriteAchievementProgress`, `CacheAchievements`, `SteamUserStats` eller motsvarande i vare sig blueprint eller C++.

Slutsats: Steam-achievements är **greenfield** om AP vill ha dem till EA. De är inte en migrering utan en nybyggnad, och de ligger inte i någon nuvarande work package.

### 4.2 Stats: finns, och hänger på tre olika ben

1. **Matchstatistiken är egen och bor i `BP_StatTrack`** (469 noder, näst största gameplay-blueprinten efter `BP_PlayerCharacter`). Den håller `TotalStatsToSubmit`, `RoundStats`, `Placement`, `AliveStartTime`, `ServerStatTime` och en `StatKeys`-map av typen `E_MatchStats` till sträng. Datamodellen ligger i `Game/Blueprints/PlayerData/Data/Stats/` som `S_Stat`, `S_RoundStats`, `S_FinalScoreClient`, `S_FinalScoreServer`, `S_BestPerformingRound`, `S_StatTracking` plus `DT_StatTable`. **Ingen av dessa structar och ingen tabellrad finns i exporten**, alltså är fältnamnen och stat-nycklarna inte läsbara i dag.
2. **Persistensen går till LootLocker**, dels via granterns progression, dels via `LootLockerLocalPlayerSubsystem`. Blueprintsidan binder `OnStatUpdated` på fyra ställen (`WB_ProfilePictureLocal`, `WB_AbilitySlot`, `BP_PlayerCharacter`, `BP_MenuPlayerCharacter`) och läser `GetPlayerProgression` i `WB_MainMenu`, `WB_PlayerProfile` och `W_NextReward`. Dessutom finns `BP_GameInstance::ReportPlayerStat` och en `PlayerStatDispatcher`-graf som `BP_StatTrack` anropar.
3. **Telemetrin är GameAnalytics och är helt separat**, samlad i `Game/Blueprints/GameInstance/BP_GameAnalytics.T3D` (317 noder): 12 `AddDesignEventWithValue`, 3 `AddProgressionEventWithOne`, 3 `AddDesignEvent`, plus `StartSession` och `EndSession` från `AnalyticsBlueprintLibrary`. Den har egna funnel-begrepp (`StartFunnelEvent`, `CompleteFunnelEvent`, `SubmitDropOffRate`, `GetMatchPlacement`) och läser `BP_StatTrack::Placement` för att rapportera matchplacering. Den rör inte utdelningen.
4. **Inga leaderboards.** LootLocker-SDK:t har leaderboard-stöd, men noll anropsställen finns i vare sig blueprint eller `Source/Mogadishu`.

Arkitektoniskt värt att veta: `BP_GameInstance` är sista ledet i en fyra nivåer djup blueprintarvskedja, `BP_GameInstance` -> `BP_GameAnalytics` -> `BP_LootLocker` -> `BP_MusicSequencer` -> `UMogadishuGameInstance` (C++). Allt som rör GameInstance-beteende måste alltså läsas i fyra filer, inte en.

## 5. Om-estimering av WP1.2, matchmaking-omkoppling

### 5.1 Vad som ska frysas, mätt

`UMatchmakingSubsystem` exponerar en liten yta mot blueprint (`Source/Mogadishu/Public/MatchmakingSubsystem.h`):

- Funktioner: `StartMatchmaking`, `StopMatchmaking`, `SetSelectedMatchmakingConfiguration`, `GetSelectedMatchmakingConfiguration`
- Egenskaper: `bIsRunning`, `QueueingStartedAt`
- Delegater: `FStatusUpdateEvent` (sju parametrar: `Status`, `IP`, `Port`, `MatchmakingStartedAt`, `EstimatedWaitTime`, `PlayerSessionId`, `QueuedPlayerCount`), `FMatchmakingRunningEvent`, `FMatchmakingConfigurationChanged`

### 5.2 Vem som faktiskt konsumerar den, verifierat

| Fil | Noder | Vad den läser |
|---|---|---|
| `Game/Blueprints/GameInstance/BP_GameInstance.T3D` | 579 totalt, varav `GameLift`-grafen 212 | **Enda konsumenten av `IP`, `Port` och `PlayerSessionId`.** De går in i `Matchmaking Status Update` och vidare till `ConnectToMatch` |
| `Game/HUDMenu/Widgets/Party/WB_ReadyButton.T3D` | 236 | `Status`, `EstimatedWaitTime`, `QueuedPlayerCount`, `MatchmakingStartedAt`, `bIsRunning` |
| `Game/HUDMenu/Widgets/Party/WB_LookingForMatch.T3D` | 68 | samma, plus `GetTimePassedInQueue` |
| `Game/HUDMenu/Widgets/Party/WB_GamemodeButton.T3D` | 76 | vald konfiguration + `IsRunningUpdatedEvent` |
| `Game/HUDMenu/Widgets/Friends/WB_GameMode.T3D` | 57 | vald konfiguration |

Resan in i matchen sker med `GameplayStatics::OpenLevel`, inte `ClientTravel`. Två anropsställen finns: ett i `BP_GameInstance:GameLift` (matad via `Conv_StringToName` från en sammanslagen IP-och-port-sträng, med `PlayerSessionId` på `Options`-pinnen) och ett i `WB_ReadyButton`, sannolikt för den lokala practice-vägen. Det andra är inte verifierat till sitt syfte.

### 5.3 Nytt estimat: 24 till 36 h, centralt 28 h, tillförsikt medelhög till hög

Vad som drar bandet:

1. **Nedåt:** noll widgetomskrivningar krävs om `FStatusUpdateEvent` behålls och `steam.<SteamID64>` läggs i `IP`-fältet med tomma `Port` och `PlayerSessionId`. Bara `BP_GameInstance` behöver röras, och helst inte ens det, om resan flyttas in i C++ bakom `IMatchSessionProvider`.
2. **Uppåt, konkret:** `WB_ReadyButton` är den enda platsen där matchmaking, party, play slots och lägesval är sammanflätade. Dess `EventGraph` är 150 noder och den har egna grafer som `ShowGameUnavailableDueToPlaySlots` (23 noder) och `Is 2Players in Party`. Varje ändring som ändrar när kön får startas landar där.
3. **Uppåt, konkret:** kopplingen mellan `EMatchmakingConfiguration` (FFA, PRACTICE, DUEL) och backendens konfigurationsnycklar bygger på substrängsmatchning mot en GameLift-ARN, och nycklarna ligger i `DT_MatchMakingConfigurationNames` **som inte har några läsbara rader i exporten**. Räkna 2 till 4 h för att läsa dem i editorn och mappa dem till lobbyfilter.
4. **Kvarstående okänt:** maxantal spelare per läge (öppen fråga 2) låg i backendens GameLift-konfiguration och finns inte i klienten. Det bekräftas av svepet, det är alltså fortfarande en fråga till The Gang, inte något exporten kan svara på.

## 6. Om-estimering av WP1.3, party och inbjudningar

### 6.1 Mätningen planen bad om

Blueprints som rör matchmaking, party, inbjudningar, presence eller vänlista, med nodantal och beroende:

| Noder | Fil | Beroenden (anrops- och bindningsnoder) |
|---|---|---|
| 484 | `Game/HUDMenu/Widgets/Friends/WB_FriendList.T3D` | LootLockerFriendList 10, **BackendMessagePump 2** |
| 315 | `Game/HUDMenu/Widgets/WB_PlayerProfile.T3D` | LootLockerFriendList 7 |
| 236 | `Game/HUDMenu/Widgets/Party/WB_ReadyButton.T3D` | GameParty 11, Matchmaking 14, **BackendMessagePump 2** |
| 172 | `Game/Blueprints/Characters/BP_MenuPlayerCharacter.T3D` | GameParty 3 |
| 155 | `Game/HUDMenu/Widgets/Settings/WB_UINavFriendDropdownButton.T3D` | GameParty 5, LootLockerFriendList 10 |
| 110 | `Game/HUDMenu/Widgets/Friends/WB_AddFriendPopup.T3D` | LootLockerFriendList 2 |
| 101 | `Game/HUDMenu/Widgets/Friends/WB_ListedFriend.T3D` | LootLockerFriendList 4 |
| 92 | `Game/HUDMenu/Widgets/Billboard/WB_MenuPlayerInfo.T3D` | GameParty 8 |
| 85 | `Game/HUDMenu/Widgets/PartyNew/WB_InvitePlayersToParty.T3D` | GameParty 3, LootLockerFriendList 2 |
| 77 | `Game/Blueprints/Characters/BP_RemotePartyMemberCharacter.T3D` | GameParty 6 |
| 76 | `Game/HUDMenu/Widgets/Party/WB_GamemodeButton.T3D` | Matchmaking 4, GameParty 4 |
| 74 | `Game/HUDMenu/Widgets/PartyNew/WB_InvitablePlayer.T3D` | GameParty 3 |
| 72 | `Game/HUDMenu/Widgets/WB_PresenceIndicator.T3D` | **BackendMessagePump 6**, inget annat |
| 68 | `Game/HUDMenu/Widgets/Party/WB_LookingForMatch.T3D` | Matchmaking 5 |
| 57 | `Game/HUDMenu/Widgets/Friends/WB_GameMode.T3D` | Matchmaking 3, GameParty 2, **BackendMessagePump 1** |
| 50 | `Game/HUDMenu/Widgets/Toasts/WB_ToastScreen.T3D` | **BackendMessagePump 1** |
| 50 | `Game/HUDMenu/Widgets/Party/WB_PartyInfo.T3D` | GameParty 4 |
| 46 | `Game/HUDMenu/Widgets/Toasts/WB_ToastNotificationPartyInvite.T3D` | GameParty 2 |
| 35 | `Game/HUDMenu/Widgets/Toasts/WB_ToastNotificationFriendRequest.T3D` | LootLockerFriendList 4 |
| 31 + 31 | `Game/Levels/MainMenu/GM_MainMenu.T3D` och `GM_MainMenu_Rework.T3D` | **BackendMessagePump 2 vardera** (`StartListen` + `OnMessageReceived`), GameParty 1 |
| 29, 21, 16, 16, 6 | `WB_InvitePlayerButton`, `WB_MainMenuPartyWidget`, `WB_FriendProfilePicture`, `WB_KickPlayer`, `WB_LeaveParty` | GameParty eller LootLockerFriendList, 1 till 2 vardera |

Summering, verifierat:

- **17 blueprints rör `UGamePartySubsystem`.**
- **5 rör `UMatchmakingSubsystem`.**
- **7 rör `UBackendMessagePump`**, och bara tre av dem icke-trivialt: `WB_PresenceIndicator` (6 anrop, hela presence-ytan), `WB_ToastScreen` (bindningen som levererar aviseringar) och de två main menu-gamemoderna som startar pumpen.
- **6 blueprints rör enbart `LootLockerFriendList`**, alltså vänlistan.
- **Bara 3 blueprints rör `FStatusUpdateEvent`**: `BP_GameInstance`, `WB_ReadyButton`, `WB_LookingForMatch`.
- Hela mängden meny-, party- och vänrelaterade blueprints är 2 120 noder. **Ungefär 1 216 av dem, alltså 57 procent, är vänlistan och profilen som hänger på LootLocker och som inte behöver flyttas alls.**

Det är svaret på planens oro. Presence- och toast-UI:t är inte djupt begravt. Det är två widgets och två gamemoder.

### 6.2 Vad som faktiskt är svårt

1. **Nyckelbytet.** Hela partyt är nycklat på LootLockers ULID-strängar. `UGamePartySubsystem` tar `PlayerPublicUid` och `PlayerUlid` i `SendPartyInvite`, `IsPlayerInParty`, `KickPlayerFromParty` och `FOnReadyStateChanged`, och `FPartyPlayerResponse` bär `Player Ulid`. Steam-lobbies är nycklade på `CSteamID`. En dubbelriktad mappning måste publiceras i lobbyns member data, och den måste finnas innan man ens kan bjuda in.
2. **Inbjudningslistan är LootLocker-vänner, inte Steam-vänner.** `WB_InvitablePlayer` och `WB_InvitePlayersToParty` bygger sin lista ur `LootLockerFriendList`. Om inbjudningar bara går via Steam-overlayen blir de två widgetarna verkningslösa, och om de ska behållas måste varje LootLocker-vän gå att slå upp till en SteamID. `LootLockerFriendList.h:235-236` har redan begreppet plattformsvänner (`UnhandledPlatformFriendsToSyncWithOutgoing` och `...Incoming`), alltså finns en ingång, men `FLootLockerFriend` exponerar inget SteamID-fält i headern. **Det här går inte att avgöra ur exporten och inte heller ur klientkoden.** Det behöver ett svar från LootLockers dashboard eller API, och det är den enskilt största kvarvarande osäkerheten i WP1.3.
3. **Presence är inte gratis på Steam.** `UBackendMessagePump::GetPresenceInfo` svarar på godtyckligt spelar-id. Steam visar bara presence för dem du är Steam-vän med, alltså tappar en LootLocker-vän som inte är Steam-vän sin online-indikator. Det är ett produktbeslut, inte ett tekniskt, och det är exakt öppen fråga 4.
4. **Det finns två huvudmenyer.** `Game/HUDMenu/Widgets/WB_MainMenu` (469 noder, 43 grafer) mot `Game/HUDMenu_Rework/Widgets/WB_MainMenu`, och `GM_MainMenu` mot `GM_MainMenu_Rework`. **Rework-widgetarna har noll referenser till party, matchmaking, message pump eller vänlista**, men `GM_MainMenu_Rework` startar ändå message pumpen. Reworken är alltså halvbyggd. Om den ska leva vidare fördubblas menyarbetet, om den ska skrotas är det ett beslut som bör tas nu och inte i WP3.4.

### 6.3 Nytt estimat: 32 till 52 h, centralt 40 h, tillförsikt medel

Vad som drar bandet:

- **Nedåt:** `UBackendMessagePump` har sex `UFUNCTION` och två delegater. Att ersätta den med en lokal meddelandebuss plus en Steam-presence-adapter bakom oförändrade signaturer är ett par arbetsdagar, inte en vecka. `UGamePartySubsystem` har tretton blueprintanropbara funktioner och fem delegater, alla väl avgränsade.
- **Uppåt:** ULID-till-SteamID-mappningen enligt 6.2 punkt 2 är värd 8 till 16 h om LootLocker inte redan bär plattforms-id på den publika profilen. Det är det som gör toppen av bandet.
- **Uppåt:** `WB_ReadyButton` igen. Den är både partyts och matchmakingens gränssnitt och delas därför mellan WP1.2 och WP1.3. Räkna med att den rörs två gånger.
- **Oförändrat okänt:** öppen fråga 4 måste besvaras innan arbetet startar. Om svaret är "Steam-vänner räcker för EA" ligger estimatet i botten av bandet. Om vänlistan i LootLocker ska överleva ligger det i toppen.

## 7. Följdeffekter på övriga work packages

1. **WP2.1, grant-tjänst.** Lägg till en explicit punkt: `BP_StatTrack:PostToLootLocker` måste byta `IsDedicatedServer` mot värdauktoritet, annars delas ingenting ut. Anropsställena är nu uppräknade, alltså är WP0.3:s acceptanskriterium uppfyllt. Estimatet 30 till 40 h står, men de 10 till 14 h på spelsidan bör innehålla den här blueprintändringen och ett dubbelutdelningsskydd.
2. **WP2.2, loadout-validering på värden.** Alla fem blueprintanrop mot validatorn är läsande accessorer. Skrivs C++ om bakom oförändrade signaturer krävs noll blueprintändringar. Bandet kan snävas från 8 till 16 h till **8 till 14 h**.
3. **WP3.1, riv GameLift.** Nu mätbart: GameLift finns i blueprint på **exakt ett ställe**, `BP_GameInstance:GameLift` med 212 noder, som utöver GameLift-anropen även innehåller matchmakinglyssnaren, resan in i matchen och spelarsessionshanteringen. Det är alltså inte en ren rivning utan en grafdelning. Ingen ändring av estimatet, men arbetet ligger på ett annat ställe än planen antog.
4. **Achievements** är inte med i någon work package i dag. Om de ska med till EA är det ett nytt paket, inte en utökning.
5. **LootLocker-utgången** enligt `drafts/lootlocker_exit_2026-08-31.md` träffar exakt de fem anropsställen som räknas upp i avsnitt 3. Om beslutet blir Steam Inventory Service blir den här listan arbetsordern för den migreringen också.

## 8. Vad som fortfarande inte går att avgöra

1. **Alla DataTable-rader.** Stat-nycklar, valuta-id, matchmakingkonfigurationer, butikslistningar och asset-mappningar. Kräver en ny export i editorn med rätt exportör eller en manuell csv-export.
2. **Alla user-defined structs och enums**, inklusive `E_MatchStats`, `S_Stat` och `S_RoundStats`. De ligger utanför exportens klassurval.
3. **179 `.umap` och deras level blueprints.** Om något gameplayflöde ligger i en nivåblueprint syns det inte här.
4. **Vilken av de två `AddProgressionForPlayer`-noderna som sitter i loopkroppen** enligt avsnitt 3.2.
5. **Om LootLockers publika spelarprofil bär ett Steam-id.** Avgörande för WP1.3:s övre band.
6. **Maxantal spelare per matchmakinglagsläge.** Bekräftat att det inte finns i klienten. Fortsatt en fråga till The Gang.

## 9. Rekommenderad ordning härifrån

1. Ställ öppen fråga 4 till Robert som ett beslut innan WP1.3 planeras i detalj, eftersom svaret flyttar estimatet 20 timmar.
2. Kör en ny tabellexport i editorn, det är en halvdag och den låser upp punkt 1 och 2 i avsnitt 8.
3. Ta beslutet om `HUDMenu_Rework` nu.
4. Lägg in blueprintändringen i `PostToLootLocker` i WP2.1:s acceptanskriterier, formulerad som "en listen server delar ut exakt en gång per spelare".

