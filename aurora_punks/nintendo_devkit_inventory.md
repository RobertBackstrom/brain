# Nintendo Switch devkits - inventering och väg till CZP

**Datum:** 2026-08-25
**Syfte:** underlag för att sätta upp Nintendo-utvecklingsmiljön i subnätet.
**Källor:** NDP inloggad 2026-08-25, mailtråd "Devkit transfer" (2024-09/10), WLBS
överlåtelseavtal Bilaga 1+2, Aurora Punks Inventory List.

---

## 1. Först, det som INTE finns

**NDP har ingen hårdvaruinventering.** Det var min utgångshypotes och den är fel.
`Getting Started -> Development Tools -> Hardware List` är en **katalog över kit-typer**
(SDEV, EDEV, ADEV, HDEV) plus beställningsformulär per region (NCL, NOA, NOE). ADMIN-området
har Organization Information, Locations, User Groups, Agreements, Tasks, Financial Information
och Transfer Product Ownership. **Ingen serieregistrering, ingen kit-lista.**

Nintendo spårar alltså inte devkits mot licensee i portalen på det sätt Sony gör i DevNet.
Registret ligger hos **NOE Ordering** (`Ordering_Publisher@nintendo.de`) och är åtkomligt bara
genom att fråga dem.

**Inventory List-arket är oanvändbart för detta.** Fliken "E - Consoles & Devkits" har tre
ifyllda rader (Oculus Quest II, två PS5 test kits), alla märkta WLBS, alla hos personer som
slutat, och noll Nintendo-poster. Raderna E004 till E014 är tomma platshållare.

**WLBS-boet innehöll inget Nintendo-devkit.** Bilaga 2 listar PS5 Test kit (42), PS4 Pro test
kit (55), Xbox one dev kit (56) och på rad 72 "Nintendo switch - Obs! Oklart om den ägs av
bolaget", alltså en retailkonsol med oklart ägande. Switch-kiten kom från annat håll.

## 2. Devkiten kom från Kinda Brave, hösten 2024

Tråd "Devkit transfer", David Pennelle (Kinda Brave) till Robert, 2024-09-25 och framåt.

### Kit 1, BEKRÄFTAT REGISTRERAT

| Fält | Värde |
|---|---|
| Typ | **SDEV** |
| Modell | HAT-S-SDKAA (Oct 2021) |
| **Serienummer** | **XAL07100102962** |
| Från | Kinda Brave Entertainment Group AB |
| Till | Aurora Punks Development Services AB |
| Registrerat | 2024-09-26 av Elina Dobzinecka, NOE Ordering: "The transfer is fine from our side, **data registered successfully**" |
| NDID som användes | `aurorahektor` (Hektor Andreasson) |
| Organization UUID | `8a8a8b496d03ef87016d15ded1280553` |

Vincenzo Russo (Senior Developer Community Coordinator, NOE) godkände i sak:
"As Aurora Punks Development Services AB is an authorised Nintendo Switch developer, I do not
see any problem in this transfer."

### Kit 2 och 3, KÖPTA MEN REGISTRERING EJ BELAGD

Pennelle 2024-10-03, Robert svarade "It's a deal!" 2024-10-08:

| Kit | Typ | Pris | Notering |
|---|---|---|---|
| Ember | EDEV | $450 | med HDMI-till-USB dockningsstation |
| Dino | SDEV | $950 | |
| (namnlöst) | EDEV | $450 | "Aurora have already", alltså redan fysiskt hos AP |

Totalt **34 000 SEK** för alla tre, fakturerat till APDS tillsammans med möbler.

**Luckan:** Pennelle skrev "Hektor can add the other two items", men **serienumren för kit 2 och 3
skickades aldrig i tråden**, och det finns ingen motsvarande "data registered successfully" från
NOE för dem. Endast XAL07100102962 är belagt registrerat.

## 3. Vad detta betyder för att sätta upp miljön

**Minst ett SDEV är vårt och registrerat.** Det räcker för att ladda ned och testa byggen, vilket
är det närmaste behovet (K2C). Ett SDEV är dessutom rätt kit för det: HDMI-ut, debug-controller,
trådbunden ethernet mot PC.

**Två frågor du behöver svara på, jag kan inte läsa dem ur något system:**
1. Var är kiten fysiskt? Hektor Andreasson stod som mottagare 2024 och är borta.
2. Fungerar de? Kit 1 är från oktober 2021.

**Nätverket:** SDEV ansluter trådbundet via ethernet till PC:n som kör NDI och Target Manager.
Det innebär att kitet och NDI-maskinen måste sitta på samma subnät, och att kitet **inte kan köra
Tailscale självt**. Det är precis det fall som motiverar en subnet router, se sista punkten i
db-318. Routern måste sitta på subnätet, så Hetzner kan inte fylla rollen. forge är vald som
konsolarbetsstation.

Referens för själva installationen finns i Drive: "Installera på Switch" (NDI-nedladdning,
Dev Environment, Target Manager) och "Download Nintendo Dev Interface 2" (16-stegs
installations- och testrutin för nsp-filer).

## 4. Vägen till CZP är LÄTT, till skillnad från titlarna

Detta är den goda nyheten. NOE Ordering krävde 2024 exakt tre fält för en devkit-överföring:

> Devkit serial number
> Aurora Punks NDID
> Transfer Start Date

Och registrerade samma dag. **Devkit-överföringen APDS till CZP är alltså ett mail till
`Ordering_Publisher@nintendo.de` med tre uppgifter**, inte den tunga produktöverföringsprocessen
med bilagekrav, månadsskiftesregel och tvåveckorsvarsel.

**Det betyder att devkiten kan flyttas till CZP oberoende av, och långt före, titlarna.**
Miljön behöver alltså inte vänta på titelöverföringen.

### Steg

- [ ] Lokalisera kiten fysiskt. Blockerat på Robert.
- [ ] Be NOE Ordering om en **förteckning över devkits registrerade på PID 291215956**. Det löser
      samtidigt luckan för kit 2 och 3, och ger serienummer vi inte har.
- [ ] Skicka överföringsbegäran till CZP med serienummer, CZP:s NDID och startdatum.
- [ ] Sätt upp forge som NDI-värd, subnet router på subnätet, DHCP-reservation för kitet.

## 5. Relaterat

- Titelöverföringen är ett helt annat spår, se
  `umbrella/aurora_punks/legal/nintendo_entity_transfer_APDS_to_CZP_2026-08-25.md` §7.
- **Chenso Club finns i katalogen**, produkt `A8GUA` plus `A8GUC` (Chenso Club_H2). Notera ur
  WLBS-avtalets Bilaga 1: "Chenso Club - IP ägs av Aurora Punks men produkten är distribuerad via
  konkursbolaget." IP:t ligger alltså hos AP, det är distributionsledet som flyttat.
- Full NDP-katalog per 2026-08-25: Kingdom Two Crowns (AD8PA), Rust Racers, 1993 Shenandoah
  (AX84A), 1993 Shenandoah Demo (AYRHA), 1993 Shenandoah (AX84C), Chenso Club (A8GUA),
  Chenso Club_H2 (A8GUC), Lootlocker.


---

## 6. LIVE-ANSLUTNING 2026-08-25: kitet är nått, läst och identifierat

Robert kopplade in ett kit på subnätet. Nitro sitter på samma nät (`192.168.32.9/24`), så det
gick att nå direkt utan mellanled.

### Hur det hittades

ARP-cachen räckte inte, den visar bara nyligen kontaktade värdar. Ett ping-svep över
`192.168.32.0/24` gav åtta värdar, och OUI-uppslag mot `/usr/share/ieee-data/oui.txt` pekade ut
en enda: **`70:48:F7` = Nintendo Co.,Ltd.** Ingen gissning behövdes.

### Identitet

| Fält | Värde |
|---|---|
| IP | **192.168.32.14** |
| MAC | `70:48:F7:F2:5D:96` |
| Typ | **SDEV**, Model MP |
| **Serienummer** | **XAL02100194870** |
| HostBridge Firmware | 5.11 (2021-05-28) |
| SDK-firmware på target | **NintendoSDK Firmware for NX 21.0.1-1.0** (`f31fe6d168`) |
| Svarstid från Nitro | 0,46 ms |

**Detta är INTE XAL07100102962**, alltså inte det kit som NOE registrerade 2024-09-26. Serienumren
skiljer sig. Det inkopplade kitet är med stor sannolikhet ett av de två från oktoberköpet
(SDEV "Dino"), och det är just de vars registrering aldrig kunde beläggas i mailtråden.
**Konsekvens: när vi ber NOE om kit-förteckningen ska XAL02100194870 uttryckligen nämnas, för det
är oklart om det ens står på oss.**

### Öppna tjänster

| Port | Tjänst |
|---|---|
| 23 | telnet |
| 80 | SDEV-webmeny (`/cgi-bin/info`, `/sion`, `/config`, LCD-capture, loggar) |
| **8000** | **Data Transfer, det är porten Target Manager använder** |

Konfiguration: DHCP på, Jumbo Frame på, MTU 4082, UPnP Discovery på.
Target-status: **Target Power On**, Battery Attached, USB Port Available, Boot Mode Flash.

### Vad som redan ligger på kitet

Skärmdumpen (`/cgi-bin/lcd/landscape.png`, 1280x720) visar DevMenu med:

- **Shoe it All** ×2 (`0x0100fed026fec000` och `0x01004b9000490000`, v0.1)
- DevMenu Application (`0x0100000000002065`)
- DevKitUpdater (`0x01000000000020d4`)
- **Strike Force Heroes** (`0x01007d...c000`, v1.28)

Systemminne 47,11 GB fritt av 54,97 GB. SD-kort ej isatt. Batteri 49 %.

**Noteringar.** *Shoe it All* står som Amberbite GmbH i NDP:s notismail, och jag antog först att
det var en annan utgivares bygge som borde rensas av NDA-skäl. **Robert 2026-08-25: fel antagande,
det är Oskar Hansen och AP som arbetat på titeln, den får ligga kvar.** Utgivarnamnet i NDP säger
alltså inget om vem som utfört arbetet, och den slutsatsen ska inte dras igen.
*Strike Force Heroes* stämmer med kitets ursprung hos Kinda Brave.

### Det praktiska genombrottet: Target Manager behövs inte

DevMenu visar tre installationsvägar, och **"Install via HTTP"** är en av dem. Kombinerat med att
kitet exponerar en HTTP-tjänst på port 80 betyder det att en nsp kan pushas **utan** Target
Manager, alltså utan en Windows-maskin i loopen.

Det ändrar uppsättningen i grunden. Ursprungsplanen var forge som NDI-värd med Target Manager.
Men för det närmaste behovet, alltså ladda ned ett K2C-bygge och testa det, räcker HTTP-vägen
från Nitro. Windows plus NDI behövs först när vi ska **skapa** byggen (BlockEm) och köra cert.

### Nästa steg

- [x] ~~Rensa Shoe it All.~~ Behövs inte, det är AP:s och Oskars eget arbete.
- [ ] Verifiera HTTP-installationsvägen med en riktig nsp. NDP-artikeln "Attempt to Install an
      nsp File on a Devkit via HTTP" är referensen.
- [ ] Ta med **XAL02100194870** i förfrågan till NOE Ordering, och be om full förteckning över
      kit registrerade på PID 291215956.
- [ ] Kontrollera att SDK-firmware 21.0.1-1.0 är submission-godkänd. Mailboxen visar ett tidigare
      Lotcheck-ärende "[Issue 11-001] NSP file requires special approval (uses SDK version not
      accepted for submission)", så versionsmatchning är en känd fallgrop.
- [ ] Ge kitet en DHCP-reservation, det står på DHCP i dag och IP:t kan flytta.


---

## 7. forge upplåst 2026-08-25, och vad som återstår för Target Manager

Robert la in Nitros nyckel i `C:\ProgramData\ssh\administrators_authorized_keys` på forge.
Första försöket föll på att PowerShell-fönstret inte var förhöjt, andra gick igenom.

**Uppmätt läge på forge:**

| Fält | Värde |
|---|---|
| Maskinnamn | `PetterBox` (tailnet-namn `forge`, 100.117.186.92) |
| **LAN-IP** | **192.168.32.6, alltså samma subnät som devkitet på .14** |
| Inloggning | `petterbox\robert`, **lokalt konto**, medlem i Administrators |
| Disk | C: 102 GB fritt av 1 862, D: 290 GB fritt av 1 863 |
| Når devkitet | **Ja**, `Test-Connection 192.168.32.14` svarar |
| Nintendo-verktyg | **Inga.** Varken NDI, NintendoSDK eller `NINTENDO_SDK_ROOT` |
| PlayStation-verktyg | Target Manager for PlayStation 5 v11.00 (server, klient, explorer-integration) |

**Två saker som förenklar planen:**
1. **Ingen subnet router behövs för Target Manager.** forge och devkitet ligger på samma /24 och
   ser varandra direkt. Subnet routern i db-318 behövs fortfarande för att nå kitet **utifrån**
   flottan, men inte för forge-till-kit.
2. **Entra-oron gäller inte denna inloggning.** `robert` är ett lokalt konto på PetterBox, inte
   ett AzureAD-konto, så Win32-OpenSSH autentiserar det rent och PRT-utgången 2026-08-28 påverkar
   inte vår åtkomst. **Den kvarstår som risk för `AzureAD\PetterMikaelsson`**, som också ligger i
   Administrators, men den vägen använder vi inte.

### Blockeraren: NDI går inte att hämta från portalen med detta konto

Genomsökt `Downloads` under `g1kr9vj6` samt hela sektionsträdet (Technical Information, Online
Documentation, Forums, Downloads). **Listan innehåller enbart dokumentationspaket**: Guidelines,
ECommerce Guide, Play Report Guide, Master ROM Lotcheck Procedures, amiibo Artwork, Online Play
Guide, Independent Server Setup Manual. Inget NDI, ingen NintendoSDK, inget Target Manager.

Listfiltret (`#search-package-ALL`) filtrerar inte listan, samma innehåll returneras oavsett
sökord, så det är inte ett sökproblem utan ett innehållsproblem.

**Trolig orsak: kontot saknar entitlement för verktygsnedladdning.** Det hänger ihop med
licensee-frågan i `nintendo_entity_transfer_APDS_to_CZP_2026-08-25.md` §3: licensavtalet är det som
grindar rätten att ladda ned SDK och NDI överhuvudtaget.

> **Ägarskap 2026-08-26:** NDI-anskaffningen drivs av sessionen **"K2C Switch build to Devkit"**,
> eftersom den körs via forge. Vägvalet nedan står kvar som underlag, men beslutet och
> genomförandet ligger inte i flott-/infrastruktursessionen.

### Tre vägar framåt, i ordning efter hur snabbt de ger loggar

1. **Fråga Oskar.** Han har en fungerande NDI-installation i dag. Snabbast, och kräver inget av
   Nintendo. NDI-versionen i Drive-dokumentationen är 2.5.4.
2. **Fråga Vincenzo Russo** (Senior Developer Community Coordinator, NOE, `Vincenzo.Russo@nintendo.de`)
   om verktygs-entitlement på PID 291215956. Han var hjälpsam i devkit-överföringen 2024.
3. **Under tiden:** logg utan Target Manager. `/cgi-bin/messages` och `/cgi-bin/dmesg` på kitet ger
   host bridge-loggar, alltså Linux-sidan. De visar boot, nätverk, bryggans sessioner och target
   power, men **inte** applikationens egen utdata. För att se spelets loggar krävs
   Target Manager-kanalen.

**Operativ varning:** en TCP-anslutning som öppnas och släpps mot port 8000 får bryggan att cykla
ned och upp (`[Bridge][BeginShutdown] exitReason = 2` i `messages`). Portskanna inte 8000 på ett
kit som används.

---

## 7. 2026-08-26: K2C-bygge från Oskar levererat till kitet via HTTP-drop

Oskar la ett K2C Switch-bygge på Drive (`2026-08-25 Nintendo Switch KingdomTwoCrowns.zip`,
Drive-id `1NmMjan9O1epdRC9YzV1Svx4-qJ_yq_4_`, ägare oskar@aurorapunks.com). Zipen innehöll
exakt en fil, `KingdomTwoCrowns.nsp` (2 259 458 411 B). Zip-md5 `98ca791199aafb02970e7957efd124f8`
verifierad efter nedladdning till Nitro.

### Build-drop-tjänsten (permanent, svarar på fråga 2 = permanent)

- **Kod:** [assistant/build-drop-server.js](../assistant/build-drop-server.js), zero-dep Node.
- **Unit:** `~/.config/systemd/user/build-drop.service`, `enable --now`, linger på → överlever reboot/utloggning.
- **Bind:** bara LAN-interfacet `enp2s0` (resolvar Nitros DHCP-adress vid start), **inte** tailnet
  eller docker. Port 8088. GET/HEAD only, **Range-stöd** (DevMenu drar multi-GB), path-traversal-skydd.
- **Filträd:** `/home/assistant/builds/<projekt>/<datum>/`, korta symlänkar i roten (`k2c.nsp`).
  Originalzip kvar i `builds/incoming/` för spårbarhet. Varje drop får en `BUILD.md`.
- **Kitet drar bygget:** DevMenu → Application → **Install via HTTP** → `http://192.168.32.9:8088/k2c.nsp`.

### Headless-frågan besvarad: Target Manager går inte från Nitro

- Port 8000 = Target Managers proprietära binärprotokoll, odokumenterat för oss.
- SDK-CLI (`ControlTarget`/`RunOnTarget`) kräver NintendoSDK = Windows-binärer under NDA, finns inte
  på Nitro (ingen SDK, ingen wine). **Att skapa/installera headless kräver en Windows+SDK-maskin** (forge).
- Telnet:23 är HostBridge-kortets PetaLinux (`PetaLinux v2014.4 / Yocto 1.7`), inte NX-targeten,
  och ger ingen nsp-push.
- **Slutsats:** för att *testa* Oskars bygge nu är Install via HTTP rätt väg (människa vid kitet).
  Windows+SDK behövs först när vi ska *bygga* och köra cert.

### Nytt säkerhetsfynd

- **FTP:21 på kitet är öppet, anonymt och skrivbart** (`220/230 Operation successful` utan pass,
  STOR/DELE i rot funkar). Kitets egen filtjänst, men oautentiserat write på LAN. Rotlistning tom,
  undermappar ger 550. Inte kritiskt (LAN, devkit), men noterat.


---

## 8. 2026-08-27: firmware-gapet löst, K2C körbar, EDEV-topologi

**SDEV XAL02100194870 firmware uppdaterad 21.0.1-1.0 → NX 22.5.0-1.1** (InitializeSdevWin på forge,
bekräftat på kitets LCD-footer). Det löser `0x00015410` "application and firmware version not
compatible" som stoppade Oskars K2C-bygge. Regel: kitets firmware måste vara ≥ byggets SDK, och
senaste NDP-firmware täcker vilket dev-bygge som helst.

**Reinitialize torkar allt.** Firmware-uppdateringen nollställer systemminnet: appar, save, parade
kontroller och klocka försvinner, och NintendoSdkDaemon stoppas. K2C ominstallerades via
TargetManager2 ("Install application" → `D:\builds\k2c.nsp`) och **startar nu** på nya firmwaren.
LCD:n visade spelets riddjur bakom kontrollprompten, alltså firmware-fixen tog.

**Joy-Con-parning efter reinit.** Parade kontroller rensas → "Controller Not Connecting". Joy-Con i
handheld mode (fastklickad på en konsols skena) binds till den enheten och broadcastar inte
trådlöst, så de kan inte para mot SDEV-lådan. Lossa dem, håll sync-knappen ~3s tills lamporna löper.
Trådbunden debug-kontroller (USB) kringgår parning.

**EDEV-kiten (Ember + namnlöst) är helt annan hårdvara än SDEV:t.** Ström via **grå dosa**
(adapter → dosa → EDEV, inte direkt i USB-C), skärmen svart med flit när tjudrad till PC, och EDEV
pratar med Target Manager över **USB** (inte ethernet som SDEV). Setup-referens: Drive-doc
"Installera på Switch". Ett EDEV som "verkar dött" är ofta bara tjudrat med svart skärm, eller
djupurladdat sedan 2024 (kräver 20-30 min laddning + 15s hård reset innan livstecken).
