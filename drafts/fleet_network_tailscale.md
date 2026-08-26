# Fleet network: one overlay that survives the move off Hetzner

| | |
|---|---|
| **Date written** | 2026-08-14 |
| **Decided with Robert 2026-08-14** | Tailscale. Parsec stays for interactive GUI work. Build it as a fleet, not a point-to-point link, because the machines share a router today and will not always. |
| **Constraint that shapes everything** | The Assistant host moves from the Hetzner VPS to the local bare-metal Linux box ([[project_baremetal_migration]]). Whatever we build now must make that a rename, not a rewrite. |
| **Related** | [petter_desktop_account_migration.md](petter_desktop_account_migration.md), [monday_hardware_recovery.md](monday_hardware_recovery.md), [[feedback_security_defaults]], [[feedback_vps_operating_environment]] |

## 1. Why an overlay and not the LAN

They are on the same router today. Anything built on that fact breaks the first time a machine
moves, and two of these machines are explicitly going to move. An overlay network gives every box a
**stable identity that is independent of where it is plugged in**. Same name, same address, same
access, whether it is one metre away or on a hotel wifi.

Tailscale also solves the specific problem in front of us, which is that Petter's desktop sits behind
a NAT with no inbound ports and should stay that way.

Worth knowing: when two nodes are on the same LAN, Tailscale negotiates a **direct local connection**
rather than routing anywhere. So there is no throughput or latency cost today, and nothing changes
about how anything is addressed when they are later apart.

## 2. The fleet

Tailnet `tail648605.ts.net`, bound to `johanrobert.backstrom@gmail.com`. Registered as
`tailscale.tailnet` in `secrets_registry.md`.

| Role | Machine | State | Notes |
|---|---|---|---|
| **Assistant host** | Hetzner VPS `ubuntu-8gb-hel1-1`, Ubuntu 24.04 | **`brain`, enrolled 2026-08-14**, 100.94.230.77 | Moves to the bare-metal box later. Name it by role, not by hardware. Tailscale 1.102.2, `--operator=assistant` confirmed working. |
| **Build machine** | ASUS ex-Petter desktop, Win 11 Pro | powered on, Petter's account, **pending enrollment as `forge`** | Unreal, Unity, packaging, Steam depots. |
| **Archive / future host** | ex-ARK Linux server | **powered down, nothing recovered** | Holds AP's self-hosted Git and the Perforce depot. Joins the fleet when it comes up. |
| **Mobile** | Robert's Lenovo Legion, Win 11 | ad hoc | Optional, but free and useful. |

## 3. The six rules that make this survive the migration

1. **Never hardcode a Tailscale IP (`100.x.y.z`). Always use the MagicDNS name.** This is the single
   rule that turns the Hetzner to bare-metal move into a rename in the admin console instead of a
   sweep through every script, config and cron job. Every other rule here is secondary to this one.
2. **Name by role, not by hardware.** The Assistant host is `brain`, whatever silicon it is running
   on this month. When the bare-metal box takes over, it is renamed `brain` and the Hetzner node is
   removed. Nothing that referenced `brain` notices.
3. **Disable key expiry on every unattended node.** This is the classic Tailscale footgun: device
   keys expire on a default schedule and the machine silently drops off the network. On a headless
   server that means the fleet quietly falls apart months later with no error anyone sees. Set it per
   device in the admin console at enrollment time, not later.
4. **Tag devices and write an ACL.** The default tailnet policy is allow-all between every device.
   Use `tag:server` and `tag:workstation`, and grant only what is needed. Applies
   [[feedback_security_defaults]] rule 1: do not assume a network is closed, make it closed and then
   verify from outside.
5. **Bind services to the Tailscale interface, not `0.0.0.0`.** An overlay does not help if the
   service is also listening on the public interface. Concretely for Windows: restrict the OpenSSH
   firewall rule to Tailscale's `100.64.0.0/10` range.
6. **Choose the identity provider once, deliberately.** Every device is enrolled against it, and
   moving a tailnet to a different provider means re-enrolling all of them.

## 4. Bootstrap

### 4.1 On the VPS, needs Robert's sudo once

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --hostname=brain --accept-dns=false
```

`--accept-dns=false` deliberately, so Tailscale's DNS does not take over resolution on a host that
already runs Docker networks and public services. MagicDNS names are still resolvable from the
Windows side, which is the direction that matters.

Then in the admin console: disable key expiry for `brain`.

### 4.2 On the Windows box, Robert at the keyboard or via Parsec, roughly 15 minutes

Log in as Petter, elevated PowerShell.

```powershell
# 1. Tailscale
winget install --id Tailscale.Tailscale -e
# Then log in through the tray icon, same identity provider as the VPS.
# In the admin console: rename the device to "forge" and disable key expiry.

# 2. OpenSSH Server (built into Windows 11, no download)
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Set-Service -Name sshd -StartupType Automatic
Start-Service sshd

# 3. PowerShell as the default SSH shell, so I get a real shell and not cmd.exe
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell `
  -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force

# 4. Lock SSH to the Tailscale range. Without this it listens to the whole LAN.
Set-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -RemoteAddress 100.64.0.0/10

# 5. Authorise the VPS key. Note: for accounts in the administrators group Windows
#    reads this file, NOT the user's ~/.ssh/authorized_keys. Getting this wrong is
#    the usual reason key auth "silently doesn't work" on Windows.
$key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILHykmzjaMZtU32hmSUzzuTnP8X2kXZ3jlQvnP8wGCUr assistant-vps"
Add-Content -Path "C:\ProgramData\ssh\administrators_authorized_keys" -Value $key
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "*S-1-5-18:F" /grant "*S-1-5-32-544:F"

Restart-Service sshd
```

Two notes on that block:

1. Tailscale SSH does not act as a server on Windows, only on Linux and macOS. So the built-in
   OpenSSH Server is the right tool here, with Tailscale providing the network and the ACL.
2. `icacls` takes the SIDs `S-1-5-18` (SYSTEM) and `S-1-5-32-544` (Administrators) rather than the
   names, because on a Swedish Windows install the group is "Administratörer" and the English name
   fails. Same trap as `Add-LocalGroupMember`.

### 4.3 Verify, from both directions

```bash
# From the VPS
tailscale status
ssh petter@forge "whoami; hostname"
```

Then apply [[feedback_security_defaults]] rule 1 and **check the exposure claim from outside rather
than trusting it**. From any host that is not on the tailnet, confirm port 22 on the desktop's public
IP is closed. If it answers, the firewall scoping in step 4 did not take.

## 5. Where Parsec fits, and where it does not

Parsec is already installed and it stays. It is the right tool for the things a shell cannot do:
watching a long build, driving WizTree, clicking through OneDrive's "Always keep on this device",
BIOS-adjacent work, and the first interactive sign-in on a new Windows account.

It is not a substitute for SSH, for three reasons:

1. **No CLI and no API.** It streams a screen to a human. There is nothing for an agent to drive.
2. **It is per-user-session.** Parsec hosts out of the logged-in user's session. After we create
   Robert's account, Parsec has to be set up again in that account, and it is awkward when nobody is
   logged in at all. **That transition is exactly the window where relying on Parsec alone loses
   access to the machine.**
3. It gives no file transfer worth using for a multi-hundred-GB preservation job.

So: Parsec for eyes and hands, Tailscale plus SSH for automation. Complementary, not competing.

## 6. Migration playbook, for when the bare-metal box takes over

1. Install Tailscale on the bare-metal box, enroll it, tag it `tag:server`, disable key expiry.
2. Carry the Assistant's SSH keypair across, or add the new host's public key to
   `administrators_authorized_keys` on `forge` alongside the existing one. Adding beats replacing:
   both hosts work during the overlap.
3. Move the services.
4. Rename the Hetzner node off `brain`, rename the new box to `brain`, remove the old node.
5. Nothing that followed rule 1 needs editing. Anything that breaks at this step was hardcoding an
   IP, and that is the audit.

## 7. Decisions, settled 2026-08-14

1. **Identity provider: personal Google, `johanrobert.backstrom@gmail.com`.** Rationale: infra
   already bills CZP rather than AP ([[reference_infra_billing_entity]]) and CZP is 100% Robert's, the
   fleet includes personal machines, and AP AB's balance sheet should not be able to complicate
   access to Robert's own network. External collaborators can still be invited to the tailnet
   individually if a dev ever needs the build machine. **Use the same login on every node**, or the
   devices land in separate tailnets and cannot see each other.
2. **Sequence: bootstrap `forge` now, ex-ARK server next.** The desktop is powered on and in front of
   him, and its `.p4qt` settings likely name the old Perforce server and client specs, which makes
   the ARK recovery cheaper when it starts.
3. **The ex-ARK server is recovered before it is networked.** Git mirror and P4 checkpoint per
   [monday_hardware_recovery.md](monday_hardware_recovery.md) first, tailnet enrollment after. It is
   an archive until those two things exist.

## 8. Follow-ups once the fleet is up

1. **Register the tailnet in `secrets_registry.md`**: the identity it is bound to, the admin console
   URL, and any auth keys minted for unattended enrollment. Auth keys are credentials and belong
   there, per [[feedback_secrets_registry]].
2. **Done at enrollment via `--operator=assistant`, not via sudoers.** The Assistant needs to run
   `tailscale status` / `ping` / link management unattended. The first instinct was a NOPASSWD
   sudoers entry for `/usr/bin/tailscale`; the correct answer is Tailscale's own `--operator` flag on
   `tailscale up`, which grants one user access to the tailscaled socket. Scoped to Tailscale rather
   than a sudo grant, and it survives reinstalls. Set it at enrollment on every node the Assistant
   must manage, including the bare-metal host later. Fits [[feedback_approval_is_the_enemy]] and
   [[feedback_long_term_solutions]].
3. **Write the ACL policy.** Until then the tailnet is allow-all between devices, which is fine for a
   two-node fleet owned by one person and is not fine once the ARK server and any collaborator join.
