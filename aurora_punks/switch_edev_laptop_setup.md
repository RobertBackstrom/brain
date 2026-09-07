---
title: Switch EDEV on a laptop off the Nitro subnet
project: aurora_punks
tags: [nintendo, edev, devkit, tailscale, target-manager, build-drop, k2c]
updated: 2026-09-07
---

# Switch EDEV on a laptop off the Nitro subnet

Goal: plug an EDEV into a laptop that is **not** on `192.168.32.0/24` (where Nitro and the SDEV
live), and still run the full loop: pull a build off Nitro, install it to the kit, boot and test.

## The topology, and why it works

The EDEV is not a network device. It talks to Target Manager 2 over **USB**, through the grey dock
box, so it is never "on" any network at all. Whatever LAN the laptop sits on is irrelevant to the
kit. The only thing the network has to carry is the **build file**, laptop to Nitro.

| Node | Address | Role |
|---|---|---|
| Nitro | `192.168.32.9` (LAN), `100.77.150.9` (tailnet) | build drop, masterbrain |
| forge | `192.168.32.6` (LAN), `100.117.186.92` (tailnet) | Windows box with NintendoSDK + TM2 |
| SDEV | on `192.168.32.0/24` via **wired** NIC | the big ethernet kit, unaffected by this |
| **your laptop** | any network | tailnet client, USB host for the EDEV |
| **EDEV** | none | USB only, tethered to the laptop |

As of 2026-09-04 the build drop binds **both** the LAN address and the tailnet address
(`assistant/build-drop-server.js`). That is the whole bridge. It is not on `0.0.0.0`, so only our
own tailnet nodes and this /24 can reach it, which is what keeps NDA builds off any office LAN.

## Robert's Legion: already done, skip to step 3

Audited over SSH 2026-09-07. The Legion (`legion`, `100.125.204.92`, user `rober`) needs **none** of
steps 1 and 2. Verified present:

| Thing | State |
|---|---|
| Tailnet | joined, reaches the drop (`HTTP 200` to `100.77.150.9:8088`) |
| NDI | **2.6.0** (newer than the 2.5.4 below) |
| Target Manager 2 | **21.2.0.0** + NX Plugin 21.2.0.0 |
| Nintendo Package Manager | 1.7.0 |
| SDKs on disk | NativeSDK **16.2.6**, NativeSDK **20.5.17** |
| Unity NX addons | 2021.3.41 LTS/NXAddon 18.3.0, 6000.0.54 LTS/NXAddon 20.5.6 |
| `NintendoSdkDaemon` | **running** (not a Windows service, a plain process) |
| Free space on C: | ~333 GB |
| Paired kit | `USB\VID_057E&PID_3005\**XAL07100029344**` — driver installed |

Also on the box: PS4/PS5 Target Manager (11.00/12.00), so it is the console test laptop generally.

**Call the kits by the last four digits of the serial** (Robert, 2026-09-07) — those are readable
on the case, which is the only label that helps when you are holding the hardware. So: the **9344**
kit and the **0024** kit, not "Ember" and "the nameless one". The invoice names cannot be mapped to
serials anyway: Kinda Brave never sent the serials for kits 2 and 3. See [[reference_ap_switch_devkits]].

**Only 9344 has ever been attached to the Legion.** 0024 has no record in the USB enum registry, so
it would be a first-time attach with a driver install, not a reconnect.

Remote-driving the Legion from a session: pipe a script in, do not fight nested quoting.

```bash
ssh legion 'powershell -NoProfile -ExecutionPolicy Bypass -Command -' < probe.ps1
```

That session **is elevated** — `rober` is in BUILTIN\Administrators and `C:\Program Files` is
writable, so software installs work over SSH (verified by installing NNPM 1.9.3 this way).
Corrected 2026-09-07: an earlier note here said "unelevated". The one thing that *does* refuse is
`HKLM\SYSTEM\CurrentControlSet\Enum\...\Properties` (device arrival/removal timestamps), and that
is a SYSTEM/TrustedInstaller-protected key, not a privilege problem — admins are denied too. So
"when was the kit last plugged in" stays unanswerable; `setupapi.dev.log` has rotated past it.

## 1. Put the laptop on the tailnet

Install Tailscale, sign in with the same account as the other nodes (`johanrobert.backstrom@`),
then confirm it can see Nitro:

```powershell
tailscale up
tailscale status                       # apservices-nitro-n50-640 should be listed
curl.exe -I http://100.77.150.9:8088/  # expect 200
```

If `tailscale status` lists Nitro but the curl times out, the laptop is up but the drop is not
reachable: check on Nitro with `ss -ltnp | grep 8088` that both binds are present, and
`systemctl --user status build-drop`.

Give the laptop a recognisable hostname before you auth it. The tailnet already has `vcsboy`,
`forge`, `edge` and `david96gb`, and a machine called `DESKTOP-XXXXXX` helps nobody later.

## 2. Nintendo dev environment (Windows only, no way around it)

There is no headless install path. Confirmed 2026-08-26: TM2's port 8000 is a proprietary binary
protocol, the only documented headless equivalent is the SDK's `ControlTarget`/`RunOnTarget`, both
Windows binaries under NDA. Linux and wine are dead ends. So:

1. `developer.nintendo.com` → Downloads → **Nintendo Dev Interface (NDI) 2.5.4**, log in with your
   Nintendo dev account.
2. NDI → **Dev Environments** → `+ Add Environment` → Create My Own → Install to Disk → Switch,
   No Specific Product, Standard, latest SDK.
3. That pulls **Target Manager 2** with it. NDI installs `NintendoSdkDaemon`, which must be running
   before TM2 can connect to anything. Opening TM2 starts it. **It is not a Windows service** —
   corrected 2026-09-07: `Get-Service *Nintendo*` returns nothing on a working install, while
   `Get-Process NintendoSdkDaemon` finds it. Check for the process, not the service, or you will
   conclude a healthy machine is broken.

Full step-by-step lives in Drive: "Installera på Switch"
(`1r_nnIpdeyiaavcqBNKEF0yRQJN2WYITNJ7NH1k7OXYM`) and the 16-step test routine in "Download
Nintendo Dev Interface 2" (`1s9Nye50snLBN5DcGCi1QSXXWdEjb3f65OIXgISMtLtI`).

## 3. Plug in the kit

Order matters, and three things look like a dead kit but are not:

1. **The grey box is a breakout dock, not a power requirement.** It merges power, HDMI and the
   debug USB into the kit's single USB-C port, so you need it when you want the computer attached
   *at the same time* as power and video. To just charge the kit, a standard retail Switch adapter
   straight into its USB-C is fine and is the cleaner path. The grey box is the HDMI-to-USB dock
   that came with the Ember kit, in the little net bag.
2. **The screen is black on purpose while tethered.** From the AP doc: *"skärmen på switchen kommer
   vara släckt när den är kopplad till datorn, skit störande"*. A black screen plus a power button
   that seems dead is often a perfectly working kit. Pull the USB **data** cable (keep power) and
   test it standalone before condemning it.
3. **The 2024 batteries deep-discharge.** Allow 20 to 30 min on the charger plus a 15 second hard
   reset before you decide it is broken.

Then the data cable, the one with the odd connector: grey box ↔ laptop USB.

## 3b. Firmware: check first, and do NOT flash from the Legion

**The rule is `kit firmware >= the build's SDK`.** A build that violates it fails at install/run with
`0x00015410` "Your application and firmware version are not compatible. Update the target's
firmware." That is what stopped Oskar's K2C build on the SDEV in Aug 2026; the fix was flashing the
kit 21.0.1-1.0 to **NX 22.5.0-1.1**.

**You probably do not need to update anything. Find out before you touch it:** connect in TM2 and
read the target's firmware version, then just try the install. Only a `0x00015410` means you need a
flash. Do not pre-emptively update a working kit.

**The trap (verified 2026-09-07):** the Legion and forge do not carry the same firmware.

| Machine | Newest SDK | Bundled firmware |
|---|---|---|
| forge (`D:\Nintendo\NX-Target`) | 22.x | **NX 22.5.0-1.1** |
| **Legion** (`C:\Nintendo\NativeSDK20.5.17`) | 20.5.17 | **NX 20.4.0-1.0** |

So the Legion's updater is **older** than what the K2C line needed in August. Running it against a
kit risks pushing firmware *down* below what the build requires, turning a working kit into a
`0x00015410`. If a flash is genuinely needed, first bring the Legion up to a 22.x env with `nnpm`
(the `NintendoSDK DevKitVersionUpdater for NX` package is already in the env, so it comes with the
SDK bump), or plug the kit into forge instead — but note the EDEV is **USB**, so the kit has to be
physically at whichever machine does the flashing. forge cannot flash a kit that is on your desk.

Tools present on both boxes, per kit type: `InitializeEdevWin.exe` (GUI, the EDEV twin of the
`InitializeSdevWin` used on the SDEV) and `SystemUpdateEdev.exe` (CLI), in
`NintendoSDK\Tools\CommandLineTools`. Firmware images sit in `Resources\Firmwares\NX`
(`DevKitUpdaterEdevI1.nsp`, `SystemUpdaterEdevI1.nsp`). `NINTENDO_SDK_ROOT` is **unset** on the
Legion and the CLI tools want it, so set it for the session before using them.

**A firmware flash is run by a human, not by an agent.** It can brick the kit, and the CLI path is
deliberately outside what the Assistant executes. Agent prepares and verifies afterwards; Robert
runs the flash. Close the TM2 GUI first or it holds the kit connection and the updater reports
"Retrieve firmware version failed / 0.0.0-0.0".

## 4. Pull the build from Nitro

```powershell
curl.exe -O http://100.77.150.9:8088/k2c.nsp        # ~2.2 GB, Range-resumable
```

Browse `http://100.77.150.9:8088/` for the listing. Short names at the root (`k2c.nsp`) are symlinks
into dated per-project folders, so the alias always points at the current drop. Range requests are
supported and verified, so a dropped transfer resumes with `curl -C -` instead of restarting.

## 5. Install and test

TM2 → **Add target** (the USB-attached EDEV appears; no IP to type, unlike the SDEV) →
**Install application** → pick the `.nsp` → boot.

**Remote video** (the film-camera icon in TM2, after Connect) is the only way to see the EDEV's
screen while it is tethered. Use it, do not fight the black screen.

Then follow the 16-step routine from the Drive doc: create a "User", install, boot, play through
menus, close, delete the title from the console, repeat, delete via TM2, delete the "User", pass the
kit on. The user-deletion steps are not busywork, they are what keeps one tester's save data and
account off the next tester's session.

## Gotchas worth keeping in mind

- **A kit refusing an install is often a version mismatch**, not a broken build. The known error text
  is "SDK version not accepted for submission". Check the kit's firmware against the SDK the build
  was made with before debugging anything else.
- **TM2 needs `NintendoSdkDaemon` running.** If Add target sees nothing, open TM2 fresh (it starts
  the daemon) before touching cables.
- **Reinitialize wipes everything**, including paired controllers and the clock, and stops the
  daemon. Budget a reinstall plus controller re-pairing if you go there.
- **NDA hygiene:** check what is already installed on a kit you take over. One of ours arrived with
  another publisher's title on it. Same rule as the Forge handover.
- This is all EDEV. The SDEV path is different and stays available: it is on ethernet, has a web
  menu, does LCD capture at `/cgi-bin/lcd/landscape.png`, and can install straight from the drop via
  DevMenu **Install via HTTP** with no Windows in the loop at all.

## If Nitro's IP moves

The drop resolves its LAN address from DHCP at start, so a new lease is picked up on restart. The
**tailnet** address `100.77.150.9` is stable and is the one to bookmark on the laptop.
