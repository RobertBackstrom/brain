# WP1.2 Matchmaking-rewire bakom befintligt API, implementationsplan

**Datum:** 2026-09-14
**Gren:** `wp1.2-matchmaking-rewire`, utgår från `wp1.1-steam-sockets` (`51bfaab`)
**Underlag:** `dev_plan_p2p_steam.md` 3.2 och 6, `blueprint_sweep_2026-09-08.md` 5, `CLAUDE.md` Tekniska beslut 2026-09-08
**Förutsättning som inte är uppfylld:** WP1.1:s runtimeacceptans är fortfarande overifierad. Bygget kompilerar och läser Steam-stacken, men anslutningsmatrisen mellan två riktiga Steam-konton är inte körd. WP1.2 skrivs alltså mot ett lager som är granskat men inte bevisat. Det är Roberts beslut 2026-09-14 att köra parallellt, och konsekvensen är att WP1.2:s acceptanskriterier inte kan stängas förrän WP1.1:s är det.

## 1. Mål

`UMatchmakingSubsystem` byter internt ut HTTP mot `mlc-backend-dev.thegang.io` mot `IMLCMatchSessionProvider`, utan att en enda blueprintvänd signatur ändras. Quick match blir: sök publika sessioner för läget, anslut till bästa träffen, hosta själv om det inte finns någon.

## 2. Det som fryses, ordagrant

Ingen av dessa får byta namn, typ, parameterordning eller parameterantal. Blueprint-svepet visade att det räcker för att lämna alla fem konsumenter orörda.

1. `FStatusUpdateEvent` med sina sju parametrar i oförändrad ordning: `Status`, `IP`, `Port`, `MatchmakingStartedAt`, `EstimatedWaitTime`, `PlayerSessionId`, `QueuedPlayerCount`.
2. `FMatchmakingRunningEvent(bool IsRunning)` och `FMatchmakingConfigurationChanged()`.
3. `StartMatchmaking(EMatchmakingConfiguration = FFA)`, `StopMatchmaking()`, `SetSelectedMatchmakingConfiguration(EMatchmakingConfiguration)`, `GetSelectedMatchmakingConfiguration()`.
4. Egenskaperna `bIsRunning` och `QueueingStartedAt`.
5. Enumen `EMLCMatchmakingStatus` med sina sex värden, och `EMatchmakingConfiguration` med sina tre.
6. Hela ytan på `UMLCMatchmakingHandler`, alltså den asynkrona blueprintnoden. Den filen rörs inte alls.

Verifierade konsumenter, från svepet och kontrollerade om i exporten idag:

| Fil | Läser |
|---|---|
| `BP_GameInstance` (grafen `GameLift`) | `IP`, `Port`, `PlayerSessionId`, `Status`, `QueuedPlayerCount`. Enda konsumenten av `IP`/`Port` |
| `WB_ReadyButton` | `Status`, `EstimatedWaitTime`, `QueuedPlayerCount`, `MatchmakingStartedAt`, `bIsRunning`, och anropar `StartMatchmaking` på tre ställen med `FFA`, `DUEL` och en inkopplad pinne |
| `WB_LookingForMatch` | samma statusfält |
| `WB_GamemodeButton` | vald konfiguration + `IsRunningUpdatedEvent` |
| `WB_GameMode` | vald konfiguration |

Nytt fynd idag, som avgör resedesignen i avsnitt 4: `BP_GameInstance:GameLift` bygger sin resa som `OpenLevel(LevelName = Conv_StringToName(IP + ":" + Port), Options = "", bAbsolute = true)`. `PlayerSessionId` går **inte** till `Options`, den sätts i en medlemsvariabel. Kolonet är alltså en hårdkodad konstant i grafen, och ett tomt `Port` skulle ge en reseadress som slutar på kolon.

## 3. Filer som ändras

| Fil | Ändring |
|---|---|
| `Source/Mogadishu/Public/MatchmakingSubsystem.h` | Privat yta byts ut: HTTP-hjälparna och `<functional>`-callbacktypen försvinner, tillståndsmaskinen kommer in. Publik yta oförändrad plus två additiva funktioner enligt 6. |
| `Source/Mogadishu/Private/MatchmakingSubsystem.cpp` | Omskriven. Inga `FHttpModule`-anrop, ingen `UGameLiftRegionLatencySubsystem`, ingen `szBackendUriBase`. |
| `Config/Windows/Custom/Steam/WindowsEngine.ini` | Nya nycklar under `[MLCOnline]`: `TravelMode`, `DefaultVisibilityPublic`, `HostMap`, `EstimatedWaitSeconds`, `SearchTimeoutSeconds`, `MaxSearchAttempts`. |

Filer som uttryckligen **inte** rörs: `MLCMatchmakingHandler.h/.cpp`, `MatchmakingData.h`, `GamePartySubsystem`, `BackendMessagePump`, `Mogadishu.Build.cs` (`OnlineSubsystem` och `OnlineSubsystemUtils` finns redan), och varenda blueprint.

## 4. Resan in i matchen, designbeslutet

Det här är den enda platsen där en rak översättning inte finns, och skälet är att den dedikerade servern aldrig hade någon värdroll att kopiera.

1. **Klientfallet** kan gå genom blueprinten som förut, om `IP` och `Port` delas på sista kolonet i den upplösta connect-strängen. Då bygger grafen tillbaka exakt samma sträng.
2. **Värdfallet** har ingen blueprintväg alls. Under GameLift var varje spelare klient. En värd måste öppna en karta med `?listen`, och den koden finns inte i någon graf.
3. Att blanda de två, alltså låta blueprinten resa som klient och C++ resa som värd, ger två olika ägare till samma tillstånd och gör WP1.4:s felhantering (värden lämnar, anslutning nekas) omöjlig att placera.

**Beslut:** C++ äger resan för båda rollerna. `[MLCOnline] TravelMode` styr det och har två lägen:

- `Code` (standard): `UMatchmakingSubsystem` reser själv. Värden kör `OpenLevel(HostMap, bAbsolute, "listen")`, klienten `ClientTravel(ConnectString, TRAVEL_Absolute)`. Statusen som går ut till UI:t är `QUEUED` under sökningen och `NOT_QUEUED` när resan påbörjats, alltså broadcastas **inte** `MATCH_FOUND` och blueprintens `ConnectToMatch` nås aldrig. Den grafen blir död kod, vilket WP3.1 ändå ska riva.
- `Blueprint`: `MATCH_FOUND` broadcastas med connect-strängen uppdelad på sista kolonet, och C++ reser inte. Finns som jämförelseläge under playtest utan att något behöver byggas om, och som säkerhetsventil om `Code` visar sig krocka med något i `BP_GameInstance` som exporten inte visar.

`HostMap` har standardvärdet från `[/Script/EngineSettings.GameMapsSettings] ServerDefaultMap`, alltså `/Game/Levels/Arenas/EmptyLevel`. Det är exakt vad den dedikerade servern startade på (fleet-skriptet `CreateGameliftFleetForBuildId.bat` skickar ingen kartparameter), så värden hamnar i samma utgångsläge som servern gjorde och `GM_MogadishuBasic` sköter arenavalet som förut.

## 5. Tillståndsmaskinen

`StartMatchmaking(Mode)`:

1. Om `bIsRunning` redan är sant, returnera. Samma vakt som idag.
2. `bIsRunning = true`, `QueueingStartedAt = Now`, `IsRunningUpdatedEvent.Broadcast(true)`, broadcasta `QUEUED`.
3. Hämta providern ur `UMLCOnlineSubsystem`. Saknas den, broadcasta `FAILED` och avsluta. Inget tyst läge.
4. `FindSessions(Mode, MaxResults)`.
5. Träffar finns: välj bästa kandidaten (har plats kvar, lägst ping) och `JoinSession`. Lyckas det, res enligt 4.
6. Inga träffar: `CreateSession(Mode, MaxPlayers, Visibility)` och res som värd.
7. Misslyckas sökningen eller anslutningen transient: `SOFT_FAILED` och nytt försök, **men högst `MaxSearchAttempts` gånger** (standard 3), därefter `FAILED`. Det är den direkta rättelsen av fyndet 2026-09-08: mot den döda backenden retryade klienten i evighet på `SOFT_FAILED` utan felmeddelande eller väg tillbaka, alltså köade spelaren mot ingenting utan att få veta det.
8. Sökningen har en egen timeout, `SearchTimeoutSeconds`, så en provider som aldrig svarar inte hänger kön.

`StopMatchmaking()`: avbryt pågående operation, lämna sessionen om vi hunnit skapa eller ansluta till en, broadcasta `CANCELLED` följt av `NOT_QUEUED`, sätt `bIsRunning = false` och broadcasta det. Idag går `NOT_QUEUED` via backendsvaret, alltså behåller vi ordningen så att widgetarna ser samma sekvens.

Värden på de sju parametrarna i varje broadcast:

| Parameter | Under kö | Vid match |
|---|---|---|
| `Status` | `QUEUED` | `NOT_QUEUED` i `Code`-läge, `MATCH_FOUND` i `Blueprint`-läge |
| `IP` | tom | tom respektive värdvärdelen av connect-strängen |
| `Port` | tom | tom respektive portvärdelen |
| `MatchmakingStartedAt` | `QueueingStartedAt` som unix-sekunder | samma |
| `EstimatedWaitTime` | `EstimatedWaitSeconds` (standard 5) | 0 |
| `PlayerSessionId` | tom | tom. Begreppet är GameLifts och har ingen motsvarighet på Steam |
| `QueuedPlayerCount` | 0 | antal spelare i sessionen vi anslöt till, eller 1 när vi hostar |

Att `EstimatedWaitTime` blir ett riktigt tal i stället för backendens `-1` är värt att notera: UI:t visar idag en hårdkodad platshållare "02:00" just för att svaret var `-1`.

## 6. Additiv yta, inget som ändras

1. `SetHostSessionPublic(bool)` och `IsHostSessionPublic()` som `BlueprintCallable`. Det är synlighetsflaggan från MECCHA CHAMELEON-modellen, uttryckt som `bool` i stället för `EMLCSessionVisibility` för att slippa en cirkulär include mellan `MatchmakingSubsystem.h` och `Online/MLCOnlineTypes.h` (den senare inkluderar den förra för `EMatchmakingConfiguration`). Standardvärde från `[MLCOnline] DefaultVisibilityPublic`.
2. Konsolkommandon `mlc.mm.start`, `mlc.mm.stop`, `mlc.mm.status` så hela quick match-flödet kan köras headless med `-nullrhi`, precis som `mlc.session.*` gjorde för WP1.1.
3. Sessionslistan som blueprintvänd yta, alltså serverbläddraren, byggs **inte** här. `IMLCMatchSessionProvider::FindSessions` returnerar redan hela listan och `mlc.session.find` skriver ut den. Widgeten som visar den hör till WP1.3 där menyn ändå öppnas, och en `USTRUCT`-baserad lista i det här headern skulle dra in samma cirkulära include. Noterat som medvetet uppskjutet, inte som glömt.

## 7. Det som medvetet lämnas kvar

1. `SetSelectedMatchmakingConfiguration` anropar fortfarande `UGamePartySubsystem::SetGameMode`, som går mot den döda backenden. Party ligger i WP1.3, och anropet är ett fire and forget-HTTP som inte blockerar något. Att riva det här skulle blanda ihop två work packages.
2. `OnPartyUpdated` läser fortfarande `Party.gamelift_matchmaking_configuration`. Samma skäl.
3. `GameLiftRegionLatency` som plugin och config-block ligger kvar. Bara anropet från matchmakingen försvinner. Rivningen är WP3.1.

## 8. Acceptans, och vad som faktiskt går att bevisa nu

Planens kriterium är "från det paketerade byggets huvudmeny klickar spelare A Play och hostar, spelare B klickar Play och ansluter inom en sökcykel". Det kräver två Steam-konton på två maskiner och en löst `SteamAPI failed to initialize` på forge, alltså är det inte något den här körningen kan stänga.

Det som stängs nu:

1. Båda targets bygger rent, `BladeBallArena` och `BladeBallArenaClient`.
2. Diffen innehåller noll ändringar av blueprintvända signaturer, och noll ändrade `.uasset`.
3. Ingen kodväg i `MatchmakingSubsystem` når `mlc-backend-dev.thegang.io` längre.

Det som återstår och som ska stå i rapporten: runtimeverifieringen, både WP1.1:s anslutningsmatris och WP1.2:s quick match.

## 9. Arbetsordning

1. Den här planen skriven. Klar.
2. Ny gren `wp1.2-matchmaking-rewire` från `51bfaab`.
3. C++ enligt 3 till 6.
4. Bygg båda targets på forge via `.cmd` plus `schtasks`, aldrig dold PowerShell-pipeline, enligt lärdomen 2026-08-27. Toolchain är redan pinnad maskinbrett till MSVC 14.38 + SDK 22621 enligt 2026-08-28, ingen ytterligare åtgärd.
5. Committa och pusha grenen. Ingenting publiceras utanför repot.
