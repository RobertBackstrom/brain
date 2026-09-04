---
title: Switch EDEV on a laptop off the Nitro subnet
project: aurora_punks
tags: [nintendo, edev, devkit, tailscale, target-manager, build-drop, k2c]
updated: 2026-09-04
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
3. That pulls **Target Manager 2** with it. NDI installs a service, `NintendoSdkDaemon`, which must
   be running before TM2 can connect to anything. Opening TM2 starts it.

Full step-by-step lives in Drive: "Installera på Switch"
(`1r_nnIpdeyiaavcqBNKEF0yRQJN2WYITNJ7NH1k7OXYM`) and the 16-step test routine in "Download
Nintendo Dev Interface 2" (`1s9Nye50snLBN5DcGCi1QSXXWdEjb3f65OIXgISMtLtI`).

## 3. Plug in the kit

Order matters, and three things look like a dead kit but are not:

1. **Power goes through the grey box, not into the kit.** Nintendo adapter → grey box → EDEV. The
   adapter straight into the EDEV's USB-C is not enough. The grey box is the HDMI-to-USB dock that
   came with the Ember kit, in the little net bag.
2. **The screen is black on purpose while tethered.** From the AP doc: *"skärmen på switchen kommer
   vara släckt när den är kopplad till datorn, skit störande"*. A black screen plus a power button
   that seems dead is often a perfectly working kit. Pull the USB **data** cable (keep power) and
   test it standalone before condemning it.
3. **The 2024 batteries deep-discharge.** Allow 20 to 30 min on the charger plus a 15 second hard
   reset before you decide it is broken.

Then the data cable, the one with the odd connector: grey box ↔ laptop USB.

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
