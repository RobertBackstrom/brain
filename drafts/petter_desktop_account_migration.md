# Petter's desktop: preserve the data, then take the machine over

| | |
|---|---|
| **Date written** | 2026-08-14 |
| **Machine** | ASUS desktop (ex-Petter Mikaelsson). Windows 11 Pro, Ryzen 9 7950X3D (16C/32T), 64 GB RAM, 2x 2 TB NVMe, RTX 3060 |
| **Decided with Robert 2026-08-14** | Keep Windows 11 and add a new account alongside Petter's. Preserve Petter's profile plus every repo and workspace directory. Destination drive to be decided after the storage survey. |
| **Execution model** | Remote, over Tailscale plus OpenSSH, once [fleet_network_tailscale.md](fleet_network_tailscale.md) section 4.2 is bootstrapped. Parsec covers the interactive steps. |
| **Autonomy, agreed 2026-08-14** | The Assistant runs **Phase 1 through Phase 3 including verification** unattended, then stops and reports. Nothing on the machine is modified except new files written to the destination drive. Phase 4 onward (account creation, `icacls`, disabling Petter) needs explicit approval per run. |
| **Related** | [monday_hardware_recovery.md](monday_hardware_recovery.md) (the *other* box, the Linux server, still powered down), [build_machine_prep.md](../curveball/drafts/build_machine_prep.md) (what to install once this is done), [[project_baremetal_migration]] |

## 0. The rule, and what actually loses data

**Inventory and copy first. Install, reformat or repurpose second.**

Creating a second Windows account is not itself dangerous. A local administrator can always take
ownership of any file on an unencrypted NTFS volume, so file permissions are never a permanent
lockout. Four things *are* dangerous, and all four happen before you notice:

1. **BitLocker.** If the drives are encrypted and the recovery key lives in a Microsoft or Entra
   account you don't control, a TPM clear, a firmware update or a motherboard reset locks the disk
   permanently. Capture the recovery key before anything else.
2. **OneDrive Files On-Demand.** If Petter's Desktop and Documents are redirected into OneDrive and
   the files are online-only placeholders, a copy tool happily copies **0-byte stubs** and reports
   success. You end up with a backup of nothing. Worse, signing Petter's account out of OneDrive can
   remove the local copies.
3. **Signing Petter out or deleting his profile** before you have verified your own account works
   and the copy is complete.
4. **`takeown /r` pointed at a whole drive.** It rewrites ownership on Windows system directories
   that must stay owned by TrustedInstaller, and breaks servicing and updates. Never run it above a
   user folder.

Until Phase 3 is verified: do not delete Petter's profile, do not sign him out of anything, do not
uninstall OneDrive or P4V, do not run Disk Cleanup, do not accept a Windows feature update.

## Phase 1. Survey. Read-only, roughly 20 minutes

Log in as Petter. Open **PowerShell as administrator** (right-click Start, "Terminal
(Administrator)"). Everything here reads, nothing writes to the data.

### 1.1 One script that captures the whole picture

```powershell
Start-Transcript -Path "$env:USERPROFILE\Desktop\machine_survey.txt" -Force

Write-Output "===== IDENTITY ====="
whoami
Get-LocalUser | Select-Object Name,Enabled,PrincipalSource,LastLogon | Format-Table -AutoSize
dsregcmd /status | Select-String "AzureAdJoined|DomainJoined|WorkplaceJoined|TenantName|DeviceId"

Write-Output "===== BITLOCKER ====="
manage-bde -status
Get-BitLockerVolume | Select-Object MountPoint,VolumeStatus,ProtectionStatus,EncryptionMethod | Format-Table -AutoSize

Write-Output "===== VOLUMES ====="
Get-Volume | Where-Object DriveLetter | Sort-Object DriveLetter |
  Select-Object DriveLetter,FileSystemLabel,FileSystem,DriveType,
    @{n='SizeGB';e={[math]::Round($_.Size/1GB,1)}},
    @{n='FreeGB';e={[math]::Round($_.SizeRemaining/1GB,1)}} | Format-Table -AutoSize

Write-Output "===== PHYSICAL DISKS ====="
Get-PhysicalDisk | Select-Object DeviceId,FriendlyName,MediaType,BusType,
  @{n='SizeGB';e={[math]::Round($_.Size/1GB,1)}},HealthStatus | Format-Table -AutoSize
Get-PhysicalDisk | Get-StorageReliabilityCounter -ErrorAction SilentlyContinue |
  Select-Object DeviceId,Wear,PowerOnHours,ReadErrorsTotal,WriteErrorsTotal | Format-Table -AutoSize

Write-Output "===== PROFILES ON DISK ====="
Get-ChildItem C:\Users -Force -Directory | Select-Object Name,LastWriteTime | Format-Table -AutoSize

Write-Output "===== TOP-LEVEL DIRS PER FIXED DRIVE ====="
foreach ($v in (Get-Volume | Where-Object { $_.DriveLetter -and $_.DriveType -eq 'Fixed' })) {
  Write-Output ("--- " + $v.DriveLetter + ":\ ---")
  Get-ChildItem ($v.DriveLetter + ":\") -Force -Directory -ErrorAction SilentlyContinue |
    Select-Object Name,LastWriteTime | Format-Table -AutoSize
}

Write-Output "===== FOLDER REDIRECTION (OneDrive Known Folder Move) ====="
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" |
  Select-Object Desktop,Personal,'{374DE290-123F-4565-9164-39C4925E467B}' | Format-List

Write-Output "===== ONLINE-ONLY PLACEHOLDER COUNT ====="
Get-ChildItem "$env:USERPROFILE" -Directory -Force |
  Where-Object { $_.Name -like 'OneDrive*' } |
  ForEach-Object {
    $n = (Get-ChildItem $_.FullName -Recurse -File -Force -ErrorAction SilentlyContinue |
          Where-Object { $_.Attributes -band [IO.FileAttributes]::Offline }).Count
    Write-Output ($_.FullName + " -> online-only files: " + $n)
  }

Stop-Transcript
```

Send me `machine_survey.txt` from the Desktop. Three things in it decide the rest:

1. `PrincipalSource` for Petter's account (`Local`, `MicrosoftAccount` or `AzureAD`).
2. Whether `manage-bde -status` shows any volume as `Protection On`.
3. Free space on the second NVMe, which decides whether the copy can start today or waits on an
   external drive.

### 1.2 Capture the BitLocker recovery key, if encryption is on

Only if 1.1 showed `Protection On`. Do this immediately, before anything else.

```powershell
foreach ($v in (Get-BitLockerVolume | Where-Object ProtectionStatus -eq 'On')) {
  manage-bde -protectors -get $v.MountPoint
}
```

Copy the 48-digit **Numerical Password** for every protected volume. Photograph the screen with your
phone as an immediate belt-and-braces, then get it off the machine properly. It is a secret, so it
goes in the registry at `/home/assistant/projects/secrets_registry.md` per [[feedback_secrets_registry]],
not in a chat message and not in a note on the machine itself. Send it to me and I will file it.

If a volume shows `Protection On` and you cannot produce a recovery key, stop and tell me. Copying
data off becomes the only safe move and every reboot is a risk until it is done.

### 1.3 Force any online-only files to download

Only if 1.1 reported a non-zero placeholder count. In File Explorer, right-click the OneDrive folder,
choose **Always keep on this device**, and wait for the sync client to finish. Or:

```powershell
attrib -U +P "$env:USERPROFILE\OneDrive*" /s /d
```

Re-run the placeholder count from 1.1 and confirm it reads 0 before you copy anything. This is the
single most common way a Windows profile backup silently ends up empty.

### 1.4 Find where the work actually lives

Two passes. The first is fast and precise, because applications record their own paths.

```powershell
Write-Output "===== PERFORCE ====="
p4 set 2>$null
reg query "HKCU\Software\Perforce\Environment" 2>$null
Get-Content "$env:USERPROFILE\.p4qt\ApplicationSettings.xml" -ErrorAction SilentlyContinue |
  Select-String "Port|Client|User|Root"
Get-ChildItem "$env:USERPROFILE" -Filter ".p4*" -Force -ErrorAction SilentlyContinue

Write-Output "===== GIT IDENTITY AND KEYS ====="
git config --global --list 2>$null
Get-ChildItem "$env:USERPROFILE\.ssh" -Force -ErrorAction SilentlyContinue
Get-Content "$env:USERPROFILE\.ssh\config","$env:USERPROFILE\.ssh\known_hosts" -ErrorAction SilentlyContinue

Write-Output "===== UNREAL RECENT PROJECTS ====="
Get-ChildItem "$env:LOCALAPPDATA\UnrealEngine" -Recurse -Filter "*.ini" -ErrorAction SilentlyContinue |
  Select-String "RecentlyOpenedProjectFiles|CreatedProjectPaths|\.uproject"
Get-ChildItem "$env:USERPROFILE\Documents\Unreal Projects" -Directory -ErrorAction SilentlyContinue

Write-Output "===== UNITY RECENT PROJECTS ====="
Get-Content "$env:APPDATA\UnityHub\projectDir.json" -ErrorAction SilentlyContinue
reg query "HKCU\Software\Unity Technologies\Unity Editor 5.x" 2>$null | Select-String "RecentlyUsedProjectPaths"

Write-Output "===== IDE RECENT WORKSPACES ====="
Get-ChildItem "$env:APPDATA\JetBrains" -Recurse -Filter "recentProjects.xml" -ErrorAction SilentlyContinue |
  ForEach-Object { Select-String -Path $_.FullName -Pattern 'key="\$USER_HOME\$[^"]*"' }
Get-ChildItem "$env:APPDATA\Code\User\globalStorage\storage.json" -ErrorAction SilentlyContinue
```

`.p4qt\ApplicationSettings.xml` is the highest-value file here. It records P4V's recent connections,
which names the old Perforce server, port and Petter's client specs outright, and that shortcuts the
Linux server recovery in [monday_hardware_recovery.md](monday_hardware_recovery.md).

The second pass is the brute-force sweep for Git checkouts. Do not use a whole-drive recursive
`Get-ChildItem` for sizing, it takes hours on an NVMe with millions of small engine files. Install
**WizTree** (free, reads the NTFS MFT directly, surveys a 2 TB drive in seconds) and use it to see
where the mass sits. For the remotes:

```powershell
$roots = @('C:\','D:\') | Where-Object { Test-Path $_ }
Get-ChildItem $roots -Directory -Force -Recurse -Filter ".git" -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -notmatch '\\Windows\\|\\Program Files' } |
  ForEach-Object {
    $cfg = Join-Path $_.FullName 'config'
    if (Test-Path $cfg) {
      [pscustomobject]@{
        Repo = $_.Parent.FullName
        Url  = ((Select-String -Path $cfg -Pattern 'url\s*=').Line -join '; ').Trim()
      }
    }
  } | Format-Table -AutoSize -Wrap
```

Any `url =` that is not `github.com` is the self-hosted Git server we have been looking for. That
single line is worth the whole exercise.

## Phase 2. Decide the destination

Send me the survey output and the WizTree summary. What I need to size it:

1. Free space on the second NVMe.
2. Total size of Petter's profile, of `Documents\Unreal Projects`, and of any Perforce workspace
   roots and repo directories found in 1.4.
3. Whether the drives are encrypted.

The likely shape: stage the copy onto the second internal NVMe first because it costs nothing and
gets the data out of a single user profile today, then mirror to an external drive once we know the
real size. Same-machine staging is not a backup, so it is a first move, not the finish line.

## Phase 3. Copy, still as Petter

Run as Petter so his own files are readable without any permission work. Dry run first.

```powershell
$src = "C:\Users\petter"
$dst = "D:\_preserve\petter-profile"     # adjust per Phase 2

# Dry run. Reports what would be copied and the total size, writes nothing.
robocopy $src $dst /E /L /XJ /R:0 /W:0 /NFL /NDL /NP /BYTES

# Real copy
robocopy $src $dst /E /COPY:DAT /DCOPY:T /XJ /R:1 /W:1 /MT:16 /NP /TEE `
  /LOG+:"D:\_preserve\robocopy-profile.log" `
  /XD "AppData\Local\Temp" "AppData\Local\Microsoft\Windows\INetCache" `
      "AppData\Local\Packages" "DerivedDataCache" "Intermediate" "Saved\Autosaves"
```

Repeat for each Perforce workspace root, repo directory and `Unreal Projects` path found in 1.4 that
sits outside the profile.

Flag notes, each of these matters:

1. **`/COPY:DAT`, not `/COPY:DATSO`.** Copies data, attributes and timestamps but *not* the ACLs.
   The copy inherits the destination's permissions, so your new account can read it without any
   takeown step. Copying Petter's ACLs would carry the access problem across with the files.
2. **`/XJ`** skips junction points. Without it, robocopy follows the legacy
   `Documents and Settings` style junctions and recurses until it dies.
3. **`/R:1 /W:1`** so locked files fail fast instead of retrying a million times.
4. **`/MT:16`** for NVMe to NVMe. Drop to `/MT:8` for a USB target.
5. **Never `/MIR`** here. It deletes anything in the destination that is not in the source.
6. Robocopy handles paths over 260 characters natively, which UE and Perforce trees hit routinely.
7. The `/XD` exclusions are regenerable caches. If you would rather not think about it, drop the
   `/XD` line and copy everything. Disk is cheaper than a judgement call at 1am.

### 3.1 Verify before you trust it

```powershell
$s = (Get-ChildItem $src -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum)
$d = (Get-ChildItem $dst -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum)
"source: {0} files, {1:N1} GB" -f $s.Count, ($s.Sum/1GB)
"dest  : {0} files, {1:N1} GB" -f $d.Count, ($d.Sum/1GB)
```

Expect a small shortfall from the `/XD` exclusions and locked files, and check the robocopy log tail
for a `FAILED` count. A large shortfall with 0 failures means placeholders, so go back to 1.3.

Then spot-check by opening two or three real files, ideally a `.uasset` and a source file, from the
copy.

## Phase 4. Create your account

Only after Phase 3 verifies. Make it a **local** account, not a Microsoft account, so it never
depends on a tenant or a cloud password reset. You can attach a Microsoft account later if you want
Store apps.

```powershell
$pw = Read-Host -AsSecureString "New password for robert"
New-LocalUser -Name "robert" -FullName "Robert Backstrom" -Password $pw -PasswordNeverExpires -AccountNeverExpires

# Use the SID, not the group name. This box may be a Swedish install where the
# group is "Administratorer" and Add-LocalGroupMember -Group "Administrators" fails.
Add-LocalGroupMember -Group (Get-LocalGroup -SID "S-1-5-32-544") -Member "robert"

Get-LocalGroupMember -Group (Get-LocalGroup -SID "S-1-5-32-544")
```

Sign out, sign in as `robert`, and let the profile finish building. Confirm an elevated PowerShell
opens and `whoami /groups | Select-String "S-1-5-32-544"` shows the administrators SID. Do not
proceed until that works.

## Phase 5. Reach the old data from the new account

Grant read access. Do not take ownership of the original.

**Do NOT run `icacls /T` against the profile root.** Learned the hard way 2026-08-14: a Windows
profile root contains ~10 legacy compatibility junctions (`Application Data` → `AppData\Roaming`,
`Local Settings` → `AppData\Local`, `My Documents`, `Recent`, `SendTo`, `Start Menu`, …) whose
targets contain junctions pointing back. **`icacls` has no junction-skip flag** — there is no
equivalent of robocopy's `/XJ` — so `/T` recurses the cycle indefinitely. Two attempts burned 2797
and 3192 CPU-seconds and had to be killed.

Iterate over the real subdirectories instead, skipping reparse points and `AppData`. This completed
in **32 seconds** with zero failures:

```powershell
$p = "C:\Users\PetterMikaelsson"

# Root level, no /T: catches loose files (.gitconfig, p4tickets.txt) without recursing
icacls $p /grant "robert:(OI)(CI)(RX)" /C /Q

# Each real subdirectory: skip reparse points (the cycles) and AppData (caches only)
Get-ChildItem $p -Force -Directory |
  Where-Object { -not ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) -and $_.Name -ne "AppData" } |
  ForEach-Object { icacls $_.FullName /grant "robert:(OI)(CI)(RX)" /T /C /Q }
```

`(OI)(CI)` makes it inherit to files and subfolders, `(RX)` is read and execute, `/C` continues past
errors on files that are locked or already inaccessible.

If some directories still refuse, because the ACL references an orphaned SID from a domain that no
longer exists, then and only then take ownership, and scope it tightly:

```powershell
takeown /F "C:\Users\petter\Documents" /R /D Y
icacls "C:\Users\petter\Documents" /grant "robert:(OI)(CI)F" /T /C
```

Never point `takeown /R` at `C:\` or `C:\Users`. Prefer running any ownership change against the
Phase 3 **copy** rather than the original, so the original stays a pristine fallback.

## Phase 6. Retire Petter's account — mostly moot, and NOT via `Disable-LocalUser`

**Corrected 2026-08-14 against the live machine.** The original plan here was
`Disable-LocalUser -Name "petter"`. **That cannot work.** `Get-LocalUser` on `forge` returns only
`robert` plus the built-in disabled accounts (`Administrator`, `DefaultAccount`, `Guest`,
`WDAGUtilityAccount`, `WsiAccount`). Petter never appears, because **`AzureAD\PetterMikaelsson` is an
Entra account, not a local one**. The local-account cmdlets do not see it and cannot disable it.

What this means in practice:

1. **There is no local action to take.** Blocking that sign-in would mean removing the account from
   the device or unjoining from Entra, and unjoining is explicitly on the do-not-do list in Phase 0.
2. **It retires itself.** Sign-in depends on the APDS tenant. `AzureAdPrtExpiryTime` was 2026-08-28,
   and the Primary Refresh Token renews only while that tenant still authenticates. When the tenant
   lapses, the account stops working with no action from anyone.
3. **The data is unaffected either way.** `C:\Users\PetterMikaelsson` stays on disk regardless, the
   Phase 5 grant means `robert` can read all of it in place, and there is a verified copy at
   `D:\_preserve\petter-profile`.

So: do nothing here. Do not unjoin the device, do not attempt to delete the profile folder. The only
thing worth watching is that nothing you need was still living inside that account's cloud state.

## Phase 7. Feed the useful part into RAG

Do not push game-asset trees to the VPS. It is an 8 GB CPX32 ([[reference_vps_capacity]]) and these
are hundreds of GB of binaries. Follow the pattern already used for
`code-corpus/repos/curveball-bba/`: extract `Source/`, `Config/`, `Plugins/`, `Content/**/*.uasset`
listed by name only in an `_ASSET_MANIFEST.txt`, plus any documentation, and ship that subset. The
binaries stay on the preserve drive.

I will write the extraction script once Phase 3 tells us what actually exists.

## Open risk, unrelated to this machine

The Linux server, the ex-ARK box that held Aurora Punks' self-hosted Git and the Perforce depot, is
still powered down and nothing has been copied off it. That box, not this one, holds the only known
copy of AP's internal Git history and the console wrapper Petter wrote. Petter's desktop may name
the server and the client specs (step 1.4), but it will not contain the depot. That recovery still
needs to happen, and it has no Death Board ticket.
