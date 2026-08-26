# Agentiskt nätverk: allt som ska göras

**Uppdaterat:** 2026-08-22
**Varför detta dokument finns:** Death Board är i dag så belamrad att arbetet inte kan trackas där.
1080 tickets, varav 433 avslutade ligger kvar i aktiva lagret och 546 icke-avslutade inte har rörts
sedan juli eller tidigare. Det här dokumentet är trackern tills db-319 är klar. Sedan flyttar
allting tillbaka till boarden.

**Arkitektur och motivering:** `drafts/agentic_fleet_architecture.md` på brain.
**Epic:** db-309. Barn: db-310 till db-319.

---

## 0. Blockerare just nu

- [x] ~~**Robert:** lägg Nitros pubkey på brain.~~ **Löst.** `ssh edge` fungerar från Nitro.
- [x] ~~**Robert:** auktorisera Nitros nyckel på forge.~~ **Löst 2026-08-25.** `ssh forge` fungerar
      från Nitro. Nyckeln lades i `administrators_authorized_keys` och ACL:en höll. Detta låser
      dock **inte** upp Target Manager, som visade sig blockeras av NDI, se nedan.
- [ ] **Robert:** bekräfta om Linus och Anastasias kort är 4060 8 GB eller 4060 Ti 16 GB.
      Avgör om de kan ta art-jobb eller bara byggjobb.
- [x] ~~**Robert:** Nintendo Developer Portal-inlogg för PID 291215956.~~ **Löst 2026-08-25.**
      Portalen är genomsökt med `assistant/ndp-session.js`. Fyndet blev en ny blockerare i stället:
      **kontot får inte ladda ned NDI** (Nintendo Dev Interface), bara dokumentationspaket. NDI är
      värden för Target Manager, så utan det finns ingen applikationslogg från kitet. Se
      `aurora_punks/nintendo_devkit_inventory.md` §6. Rotorsaken är sannolikt licensee-entitlement,
      alltså samma entitetsfråga som titelöverföringen, och den tråden körs separat med Lawyer.
- [~] NDI-anskaffningen (Nintendo Dev Interface, värden för Target Manager) **ägs 2026-08-26 av
      sessionen "K2C Switch build to Devkit"**, eftersom den körs via forge. Följ inte upp den här.
      Kvarstående sak som ingen session äger: be NOE Ordering om den fulla devkit-listan på
      PID 291215956 och verifiera registreringen av XAL02100194870, det anslutna kitet.

---

## 1. Töm Death Board (db-319, blockerare för allt trackande)

- [ ] Normalisera de 17 avvikande statusvärdena till de fem kanoniska. Cirka 20 tickets.
- [ ] Arkivera de 433 avslutade ut ur aktiva lagret. Radera inte, de ska förbli sökbara via RAG.
- [ ] Flytta icke-ticket-filer ur followups-katalogen så de slutar parsas som tickets.
- [ ] Triagera de 546 stale icke-avslutade. Bulkstäng det döda, behåll det levande.
- [ ] Lös de 11 dubblerade db-numren, och landa db-290 (unikhetsgaranti) i samma svep.
- [ ] Inför automatisk rotation av avslutade ärenden, samma mönster som rotate-learnings.js.

## 2. Konsolidera styrplanet till Nitro (db-310, klockan tickar)

Varje timme som går är ännu en timme av två masterbrains som driver isär.

- [x] Fas 0: SSH-nyckel in på brain.
- [x] Fas 0: inventera vad som faktiskt kör på brain.
- [x] Fas 1: frys divergensen.
- [x] Fas 2: flytta cron-sviten, RAG-indexeraren, Death Board. **Klart 08-24.**
- [x] Fas 2: **säkerhetstimrarna, 2026-08-25.** 16 timrar flyttade med
      `migrate-timers-to-nitro.sh --apply`. Edge har kvar exakt den avsedda mängden:
      `opensign-watcher`, `nightly-recycle`, `reap-orphaned-vscode`, `launchpadlib-cache-clean`.
      Static sites stannar på edge, det är korrekt enligt edge-rollen.
- [x] Fas 2: stäng av på Hetzner så inget dubbelfyrar.
- [x] Fas 2: stäm av VPS-only-ändringar. RAG-deltat drogs in av kursorbaserad ingest,
      453 742 -> 453 994 mot edges 453 998.
- [x] **WhatsApp-ägarskapet avgjort: Nitro.** Bryggan disablad på edge, nattomstarten flyttad hit
      och TZ-pinnad till 07:10 Europe/Stockholm.
- [ ] Starta faktiskt om Nitro och verifiera att allt kommer tillbaka av sig självt. **Enda kvar.**

**Bugg värd att minnas, hittad vid apply:** TZ-patchen i migreringsscriptet var en tyst no-op,
vakten var `grep -F` men ersättningen `sed`-regex, och `*-*-*` betyder något helt annat som regex.
Dry-run och apply var alltså oense utan att något larmade. Lagat och verifierat. En vakt och dess
åtgärd måste använda samma stränglogik.

## 3. Hetzner till edge-roll (db-311)

- [ ] Off-site backup av masterbrain och rag.db från Nitro till edge.
- [ ] Watchdog som larmar när hemmanätet ligger nere, via en väg som inte själv beror på hemmanätet.
- [ ] Krymp CPX32 till minsta plan. Använd CPU-och-RAM-only-rescalen, den behåller disken och är
      reversibel.
- [ ] Döp om tailnet-noden så namnet brain frigörs till Nitro.

## 4. Delad MCP-layer (db-312, detta är fixen för OOM) — **KLART 2026-08-26, 7 av 7**

**Uppdaterat 2026-08-25 efter mätning på Nitro.** Texten nedan påstod tidigare att spåret inte var
påbörjat. Det stämmer inte, fyra av sju körs redan delat.

- [x] Kartlägg vilka av de 7 MCP-servrarna som är säkra att dela mellan sessioner.
- [x] Kör dem som långlivade tjänster istället för per-session-processer. **Klart för fyra:**
      `mcp-rag-http` (3790), `mcp-gmail-http` (3791), `mcp-gmail-personal-http` (3792),
      `mcp-whatsapp-http` (3793). Alla fyra `active` och konfigurerade som `http` i `~/.claude.json`.
- [x] **Kvar att dela: `gdrive`, `atlassian-jira`, `atlassian-confluence`.** **KLART 2026-08-26**
      via `assistant/mcp-stdio-bridge.js`, en generell stdio-till-HTTP-brygga, eftersom ingen av de
      tre har kod vi rår över. Portar 3794, 3795, 3796.
- [ ] Gamla sessioner startade före omläggningen håller kvar privata gmail/rag/whatsapp-stackar
      (~174 MB styck). De släpper vid sessionsomstart, inget kodarbete behövs.
- [ ] Mät före och efter, samma metod som db-285.
- [ ] Bekräfta att sessionsisolering behålls där den faktiskt behövs.

**Mätning 2026-08-25 på Nitro:** 42 MCP-processer, 2 531 MB, plus 2 394 MB i claude-code
extension-hostar. Alltså ~4,9 GB av 15 GB i sessionsoverhead, swap 3,2 av 4 GB.

**Fälla som redan har bitit en gång:** `reap-orphaned-vscode.sh` matchar `mcp-rag.js`,
`mcp-gmail.js` och `whatsapp/mcp-whatsapp.js` på ppid, och de delade tjänsterna är barn till
`systemd --user`. Reapern hade dödat den delade layern var tjugonde minut. Åtgärdat 2026-08-25:
scriptet härleder manager-PID i runtime i stället för att hårdkoda 915, och avvisar allt vars
cgroup är en `*.service`-unit. **Varje ny delad tjänst måste kontrolleras mot reaperns mönster.**

## 5. Beräkningsplan via TeamCity (db-313)

TeamCity kör redan på Nitro på port 8111. Vi behöver inte bygga en jobbdispatcher, bara koppla in oss.

**Topologi avgjord 2026-08-25 (Robert frågade om TC borde flytta till forge).** Servern stannar på
Nitro, forge blir agent. Servern är en lätt alltid-på tjänst som vill ha upptid, agenten är det som
vill ha kärnor och disk. Att flytta servern till en arbetsstation som sövs och GPU-lastas
återinför exakt skälet till att forge valdes bort som brain-host. Nattkörning är en
triggerinställning, inte ett topologiargument. **forge är också bättre byggare än david96gb:**
7950X3D 16c/32t mot i5-11400F 6c/12t, alltså ungefär tre gånger kompileringskapaciteten. 96 GB gör
noll nytta för en kompilering, den siffran är avgörande för editor-laster som ARK Dev Kit.

- [ ] TeamCity-agent på forge, per-agent-concurrency 1.
- [ ] Bygg-workspace och modellcache på olika NVMe-diskar. Disk-I/O är det bygg och art slåss om.
- [ ] Koppla agent-router.js så den kan lägga jobb i kön istället för att spawna lokalt.
- [ ] Kapacitetsregler för opportunistiska noder: endast lediga timmar, aldrig under arbetstid.

## 5b. Var byggen och submissionspaket ska lagras — BESLUTAT 2026-08-25

**Roberts val:** (1) slutför Rocky-migreringen av VCSBOY **först**, ingen interim på Windows.
(2) Oskar enrollas på tailnet som egen enhet. (3) Tailscale SSH slås på, men se korrigeringen i
punkt 10, den löser inte Windows-noderna.

**Följd av val 1: db-301 blir blockerare för hela bygglagringen.** Den ticketen har svällt, och
nu hänger TeamCitys artifact storage, den delade ytan mot Oskar och submissionsarkivet på att den
blir klar. Det bör synas i prioriteringen. Under tiden får inga skarpa byggen köras som skriver
artefakter, för då fyller de Nitros 122 GB.



Robert frågade: var har TeamCity sparat saker tidigare, och var ska det hamna nu, VCSBOY, Drive
eller Toms dator?

**Mätt läge 2026-08-25:**

| Nod | Lagring | Tjänster | Slutsats |
|---|---|---|---|
| **Nitro** | 228 GB NVMe, **122 GB fritt** | TeamCity-server (`/opt/TeamCity`, användare `teamcity`, port 8111) | **Diskvalificerad som artefaktlager.** Ett enda Switch-submissionspaket plus byggen äter 122 GB fort. Servern kan bo här, artefakterna kan inte. |
| **VCSBOY** | **10,6 TB RAID** | SSH 22, **SMB 139/445 redan igång**, RDP 3389, Perforce 1666 | **Enda bulklagringen i flottan.** Fildelningen finns redan, den behöver inte byggas. |
| **Toms dator** | 32 GB RAM, 8c/16t, ingen bulkdisk | (ej enrollad) | **Byggare, inte lager.** Ett artefaktlager ska inte ligga på en maskin som startas om och lastas för byggen. |

**Historiken, för att undvika att upprepa den:** Windswepts TeamCity körde server, agent och
lagring på *samma* burk i Skellefteå-kontoret. Det är precis den kopplingen vi separerar nu.

### Beslut

1. **TeamCity-servern stannar på Nitro.** Redan beslutat, se punkt 5. Men eftersom TeamCity som
   standard lägger artefakter i sin datakatalog måste **artefaktlagringen pekas om till VCSBOY**,
   annars fyller den Nitros 122 GB.
2. **VCSBOY är lagret**, både för CI-artefakter och för det delade upp- och nedladdningsutrymmet.
3. **Skilj på tre saker som lätt slås ihop:**
   - *CI-artefakter*: maskinskrivna, hög volym, automatisk retention per build-typ.
   - *Delad yta Robert och Oskar*: byggen att testa, kräver inloggning för en extern part.
   - *Submissionspaket*: slutartefakter som ska bevaras och vara spårbara mot Lotcheck-inlämning.
   Samma disk, olika kataloger och olika retention. Submissionspaket raderas aldrig automatiskt.
4. **Drive är fel verktyg för binärerna.** Multi-GB nsp-filer och konsolmaterial under NDA hör
   inte hemma på en Google-yta. Drive får bära dokument och metadata, inte byggen.

### Sekvensproblem som måste lösas först

VCSBOY kör **Windows med utgången eval** (se db-301) och ska till Rocky Linux. Att bygga en
permanent delning på den i dag betyder antingen att migreringen görs först, eller att vi accepterar
en utgången Windows-installation som lager. **Detta är den enda öppna frågan i punkt 5b**, och den
avgör om vi kan köra skarpt nu eller behöver en interimslösning.

### Steg

- [ ] Bestäm med Robert: slutför db-301 Rocky-migreringen först, eller ställ upp delningen på
      Windows-sidan som interim.
- [ ] Peka om TeamCitys artifact storage från Nitro till VCSBOY innan första bygget körs.
- [ ] Katalogstruktur på VCSBOY: `builds/<projekt>/<buildtyp>/`, `submissions/<projekt>/<titel>/`,
      `incoming/` för manuella uppladdningar.
- [ ] Enrolla Oskar på tailnet som enhet, ge honom åtkomst till `incoming/` och `builds/`.
      Det är den durabla vägen och slipper delade lösenord.
- [ ] Retention: byggen roteras per build-typ, **submissionspaket aldrig**.

## 6. Headless Unreal och Unity (db-314)

- [ ] Headless Unity-bygge på forge.
- [ ] Headless Unreal-cook och packaging på forge.
- [ ] Porteringsmatris: vilka plattformar och motorer vi faktiskt kan bygga för, och vad som saknas.
- [ ] Utvärdera Epics Horde som senare steg.

## 7. Artpipeline på forge (db-315)

- [ ] ComfyUI headless för 2D från Roberts koncept.
- [ ] 3D-generering, moln-API mot lokal modell.
- [ ] Autorig och anim.
- [ ] Väg in i motorn, hänger på punkt 6.
- [ ] Verktygsval diskuteras med Robert först, art tool selection är inte ett autonomt beslut.
- [ ] Landa db-125 (fal.ai och Stability), den befintliga lösa tråden.

## 8. Verktygshälsa, alltså 11-MCP-frågan (db-316)

Två felmoder, båda observerade. Tyst zombie: WhatsApp-bryggan sa ready i 25,5 timmar medan varje
anrop gav 500. Zombie-probe: linkedin-sd larmade var fjärde timme i 361 timmar om ett känt fel.

- [ ] Varje verktyg deklarerar en probe som gör ett riktigt anrop, inte en statusläsning.
- [ ] Resultaten landar på en hälsovy.
- [ ] Ett dött verktyg öppnar eller uppdaterar en enda ticket, med dedup.
- [ ] Att parkera ett verktyg retirerar automatiskt dess probe.

## 9. LLM-leverantörslager (db-317)

Valt 2026-08-22: OpenAI, Google Gemini och lokal Ollama på forge.

- [ ] Abstrahera tier till leverantör plus modell, istället för till ett modell-ID.
- [ ] Wire OpenAI och Gemini.
- [ ] Ollama på forge för klassificering, triage och rutin. Fungerar även utan internet.
- [ ] Generalisera The Reviewer till andra åsikt från en annan leverantör, inte bara en starkare modell.
- [ ] Nycklar enligt secrets_registry-konventionen.

## 10. Tailscale: härdning och enrollment (db-318)

- [ ] ~~Slå på Tailscale SSH. Då behövs inga nycklar alls i flottan.~~ **KORRIGERAT 2026-08-25:
      det löser inte flottan.** Tailscale SSH-*servern* finns bara för Linux, macOS och BSD.
      Uppmätt nodlista: forge (`PetterBox`), VCSBOY och David96GB är **Windows**, bara Nitro och
      edge är Linux, och dem når vi redan med nyckel. Tailscale SSH hjälper alltså exakt de noder
      som inte var problemet. **Windows-noderna kräver OpenSSH-server plus authorized_keys**,
      samma bootstrap-mönster som användes på apservices. Slå gärna ändå på Tailscale SSH för
      Linux-sidan, men räkna inte med den som flottans lösning.
- [ ] Stäng av key expiry på varje obevakad nod. Detta är den verkliga utelåsningsrisken.
- [ ] Taggar och ACL. Default-policyn är allow-all mellan alla enheter.
- [ ] Skapa en återanvändbar pre-auth key för headless enrollment av nya maskiner.
- [ ] Boot-watchdog mot APIPA. Gör detta före första flytten av 5G-routern, inte efter.
- [ ] Enrolla Linus och Anastasia opportunistiskt. Opt in och synligt för dem, det är deras
      arbetsmaskiner.
- [ ] Speca David96GB och Toms gamla maskin innan roller tilldelas.
- [~] Subnet router för att nå devkitet utifrån flottan. **Hanteras 2026-08-26 i sessionen
      "K2C Switch build to Devkit", inte här.** Den måste sitta på subnätet, så Hetzner kan inte
      fylla rollen. forge och kitet ser redan varandra utan router.

---

## Maskinparken

| Nod | Hårdvara | Roll efter planen |
|---|---|---|
| brain (Nitro) | i5-12400F, 16 GB, 228 GB NVMe | Styrplan: Death Board, agent-router, schemaläggare, RAG, hälsa. Plus code-server, reels, webb. |
| edge (Hetzner) | CPX32, 7,6 GB | Off-site backup och watchdog. Enda noden utanför lägenheten. |
| forge | 7950X3D, 64 GB, 2x2 TB NVMe, RTX 3060 12 GB | Bygg och art. Unreal, Unity, packaging, ComfyUI, Ollama. |
| vcsboy | HPE MicroServer, Windows | Endast versionshantering. Perforce. |
| linus, anastasia | 2x RTX 4060 | Opportunistisk beräkning, lediga timmar. |
| david96gb | Okänd | Opportunistisk, när den är specad. |
| Toms gamla | Okänd | Roll bestäms efter specning. |

**GPU-noteringen som avgör art-routningen:** forges RTX 3060 har 12 GB VRAM mot desktop-4060:ns 8 GB.
För diffusion slår VRAM-taket rå hastighet, så det äldre kortet är det bättre art-kortet. Detta
vänder om 4060-maskinerna visar sig vara Ti-varianten med 16 GB.

## Risker

1. **Flyttrisken.** När 5G-routern flyttas byter alla LAN-adresser, och tailscaled kan fastna på en
   APIPA-adress utan att återhämta sig själv. Watchdog före första flytten.
2. **Ensiterisken.** Ett strömavbrott tar ner brain, beräkningsplanet och ytterdörren samtidigt.
   Edge-rollen är hela mitigeringen och ska inte strykas för att spara några euro.
3. **Divergensfönstret.** Varje timme före fas 2 är ännu en timme av två masterbrains som driver isär.
4. **Opportunistiska noder tillhör människor.** Linus och Anastasia jobbar på sina maskiner. Lediga
   timmar, opt in, synligt, annars blir flottan ett politiskt problem istället för ett tekniskt.
