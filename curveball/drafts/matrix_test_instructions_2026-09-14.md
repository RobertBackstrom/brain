# Anslutningsmatris WP1.1, körinstruktion 14 sep 2026

Bygget ska ligga på legion i `E:\Curveball\PackagedClient\Windows`, samma artefakt som på forge
(exe 285 826 560 byte, 14 sep 15:08:25, SHA256 `755F427C...41E44DD`). Brandvägg och startgenvägar
är på plats på båda maskinerna.

**Steg 0, väck legion.** Hela arkivet kom över (2 547 958 724 byte, exit 0), uppackningen startade,
och sedan somnade maskinen och föll av tailnet. Väck den och säg till, så läser jag
`E:\Curveball\logs\stage_extract.log` och bekräftar hash och tidsstämpel innan du kör något.
Sätt samtidigt legion på att aldrig vila, annars dör en körning mitt i.

**Först:** legions Steam är inloggad som Alouatta, alltså samma konto som forge kör. Två maskiner
på samma konto ser aldrig varandras lobbyer, så testet ger noll träffar om du hoppar över steg 1.

1. På legion: Steam, Konto, Logga ut. Logga in med ditt andra konto. Låt Steam ligga kvar igång.
2. På forge: kör `D:\Curveball\matrix_host.cmd`. Värden startar utan fönster.
3. Vänta en halv minut. `D:\Curveball\logs\matrix_host.log` ska innehålla
   `SteamSocketsNetDriver started listening on 7777`. Står det inte där, säg till, då är resten meningslös.
4. På legion: kör `E:\Curveball\matrix_client.cmd`. Spelet startar i fönster.
5. Öppna konsolen med tangenten under Esc (funkar den inte, prova Tab). Skriv `mlc.session.find ffa`.
   Förväntat: en rad med index 0, forges kontonamn, 1/6 spelare och ett ping.
   Noll träffar är inte ett fel i körningen, det är testresultatet, och då stannar vi där.
6. Skriv `mlc.session.join 0`.
   Förväntat: `[MLC] join -> ok (error 0), connect string 'steam.76561198022662496:7777'`.
7. Skriv `open steam.76561198022662496:7777`, alltså strängen du fick i steg 6.
   Förväntat: du hamnar i arenan, och värdloggen visar att en spelare anslutit.
8. Låt det stå en minut. Stäng sedan med `E:\Curveball\matrix_stop.cmd` på legion och
   `D:\Curveball\matrix_stop.cmd` på forge.

Kör sedan samma sak åt andra hållet: `matrix_host.cmd` på legion, `matrix_client.cmd` på forge,
steg 5 till 8 identiskt.

**Loggar jag behöver efteråt, från båda körningarna.** Hämtar dem själv över SSH, säg bara till:
`D:\Curveball\logs\matrix_host.log` + `matrix_client.log` på forge,
`E:\Curveball\logs\matrix_host.log` + `matrix_client.log` på legion.

---

## Autologon på forge, det du kör själv

Jag kan inte ladda ner verktyget eller skriva lösenordet åt dig. Vid forges skrivbord:

1. Hämta `https://download.sysinternals.com/files/AutoLogon.zip`, packa upp i `D:\Curveball\tools`.
2. Kör `D:\Curveball\tools\Autologon64.exe`. Användare `robert`, domän `PetterBox`, lösenord i
   rutan, Enable. Lösenordet hamnar då som krypterad LSA-hemlighet, inte i klartext i registret.
3. Starta om forge när inget bygge kör. Säg till efteråt, jag verifierar att session 1 är tillbaka
   och att Steam och `cvb_start_steam` fungerar som förut.
