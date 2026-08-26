# David96GB (blivande `brain`): fjärråtkomst-bootstrap

| | |
|---|---|
| **Date** | 2026-08-20 |
| **Author** | Assistant (DevOps), for Robert |
| **Scope** | ENDAST fjärråtkomst + inventering. Ingen wipe, ingen Linux, ingen stackflytt. |
| **Beslut** | Robert 2026-08-20: "bara fjärråtkomst först". |
| **Bygger på** | `drafts/fleet_network_tailscale.md` avsnitt 4.2 (samma block som fungerade på forge) |

## Utgångsläge, mätt 2026-08-20

1. Noden `David96GB` (100.90.140.53) joinade tailnet 2026-08-20 17:14 UTC. Online, men **via DERP-relä**
   (`direct connection not established`), inte direktanslutning.
2. Kör **Windows**. Port 22 och 3389 båda stängda/filtrerade från tailnet, alltså finns ingen väg in.
3. MagicDNS resolvar inte från VPS:en (`brain` startades med `--accept-dns=false` av rätt skäl), så
   adressera med 100.x eller via `~/.ssh/config`-posterna nedan.
4. Nodnamnet `brain` pekar fortfarande på Hetzner-VPS:en. Byts först vid faktisk cutover, inte nu.

## Vad blocket gör, och varför varje rad finns

| Steg | Varför |
|---|---|
| Entra-koll | Om burken är Entra-joinad mot APDS-tenanten gäller samma fälla som på forge: Win32-OpenSSH autentiserar inte Entra-konton (domänkvalificerat användarnamn ger "connection reset"). Ett lokalt konto är då inte bekvämlighet, det är enda vägen in, och det frikopplar burken från ett konkursbos katalog. |
| Lokalt adminkonto | Se ovan. Lösenordet sätts interaktivt, skrivs aldrig till fil (secrets läcker annars till RAG-indexet, db-287). |
| `Get-LocalGroup -SID S-1-5-32-544` | På svensk Windows heter gruppen "Administratörer" och engelska namnet failar. SID fungerar oavsett språk. |
| `administrators_authorized_keys` | För konton i administratörsgruppen läser Windows **den** filen, inte användarens `~/.ssh/authorized_keys`. Vanligaste orsaken till att nyckelauth "tyst inte fungerar". |
| `icacls` med SID | Samma språkfälla. `S-1-5-18` = SYSTEM, `S-1-5-32-544` = Administrators. Filen måste ha ärvda rättigheter borttagna, annars ignorerar sshd den. |
| Brandväggsregel till 100.64.0.0/10 | Utan den lyssnar sshd mot hela LAN:et. Regel 1 i [[feedback_security_defaults]]: verifiera exponeringen utifrån, lita inte på påståendet. |
| `tailscale set --unattended` | Annars tappar noden tailnet när ingen är inloggad, vilket är hela poängen med en always-on host. |

## Block att köra på burken (Robert vid tangentbordet eller via Parsec, elevated PowerShell)

```powershell
# 0. Var är vi, och är burken Entra-joinad?
whoami
dsregcmd /status | Select-String "AzureAdJoined|TenantName|MdmUrl|AzureAdPrtExpiryTime"

# 1. Lokalt adminkonto. Hoppa över om ett lokalt konto redan finns.
$pw = Read-Host "Satt losenord for lokalt konto 'robert'" -AsSecureString
New-LocalUser -Name robert -Password $pw -FullName "Robert Backstrom" -PasswordNeverExpires -AccountNeverExpires
Add-LocalGroupMember -Group (Get-LocalGroup -SID S-1-5-32-544) -Member robert

# 2. OpenSSH Server (inbyggd i Win11, ingen nedladdning)
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Set-Service -Name sshd -StartupType Automatic
Start-Service sshd

# 3. PowerShell som default SSH-shell, inte cmd.exe
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell `
  -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force

# 4. Las SSH till tailnet-intervallet
Set-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -RemoteAddress 100.64.0.0/10

# 5. Auktorisera VPS-nyckeln
$key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILHykmzjaMZtU32hmSUzzuTnP8X2kXZ3jlQvnP8wGCUr assistant-vps"
Add-Content -Path "C:\ProgramData\ssh\administrators_authorized_keys" -Value $key
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "*S-1-5-18:F" /grant "*S-1-5-32-544:F"

Restart-Service sshd

# 6. Overlev omstart, ingen nyckelutgang
tailscale set --unattended
```

I admin-konsolen efteråt: stäng av key expiry för `david96gb`. Byt **inte** nodnamn till `brain` ännu,
det kolliderar med VPS:en och sker vid cutover.

## Verifiering, från VPS:en

```bash
ssh david96gb "whoami; hostname"
tailscale ping -c 3 david96gb          # hoppas pa direkt, inte DERP
```

Extern kontroll enligt [[feedback_security_defaults]]: från en host utanför tailnet, bekräfta att port 22
mot burkens publika IP är stängd. Svarar den tog inte brandväggsscopingen.

## Direkt efter, inventering (läsning, inga ändringar)

1. Disk, RAM, CPU bekräftade mot Hardware_Inventory (96 GB, 2 TB NVMe, i5-11400F).
2. Vad ligger på disken? Samma fråga som på forge: finns AP-material, klient-IP eller David-profil som
   måste bevaras innan wipe. **Wipe:a inte förrän den frågan är besvarad.**
3. Nätläge: varför bara DERP och inte direktanslutning (`tailscale netcheck`, UPnP/NAT-typ). En
   relayad always-on host är onödig latens.
4. Öppen fråga sedan 2026-08-14: är ex-APDS-hårdvaran Roberts/AP:s eller konkursboets enligt KL 3:1.
   Gäller även denna burk. Inte blockerande för fjärråtkomst, blockerande för wipe.
