# Monday 2026-08-10: recover before you repurpose

| | |
|---|---|
| **Date written** | 2026-08-04 |
| **Applies to** | The two machines coming online Monday: the **Linux server** (ex-Perforce + self-hosted Git, currently powered down) and **Petter Mikaelsson's Windows desktop** (the intended UE build machine) |
| **Why this exists** | Both machines are the only known copy of things we cannot get anywhere else. Both are scheduled to be repurposed. Those two facts in the same week are how source disappears. |

## 0. The one rule

**Inventory and copy first. Install, reformat or repurpose second.** No exceptions, on either machine.

The Linux server is the intended host for the Assistant stack after the bare-metal migration
([[project_baremetal_migration]]). A clean install is the natural first instinct and it would destroy
the only surviving copy of Aurora Punks' internal Git history. Nothing on the migration is urgent
enough to justify that risk.

## 1. What we know is on the Linux server

From Eriksson (Discord, 2026-08-04): it is the same physical box that used to run the ARK server, and
it hosted **both a self-hosted Git server and Perforce**. He notes "adresserna lär inte stämma", so
the old hostnames will not resolve. That does not matter for recovery, see 2.1.

Things we are actively missing that plausibly live there:

1. **The console wrapper / tool written by Petter Mikaelsson.** Confirmed by Robert as his work.
   Verified absent from GitHub: no commits by `ap-petter` or author name `petter` in
   `apds-console-wrapper`; `AP-Tools/Unreal/` is a `dummy.txt` placeholder on a single branch; the
   account has zero personal repos. The GitHub `apds-console-wrapper` repo is a **different, older
   artifact** (Peter Vestman, 2022, last touched by Linus Augustsson 2024-06-07). Two different
   people, near-identical names, do not conflate them.
2. **The Unreal console tool** Eriksson recalls Petter and Gustav building, "documented".
3. Whatever else never made it to GitHub. The Unreal game projects are the obvious candidates, since
   [[reference_source_control_map]] already records that AP's UE work lives on Perforce rather than
   GitHub.

## 2. Recovery order on the Linux server

### 2.1 Git first, because it is nearly free

A bare Git repository is just a directory. **The Git service does not need to be revived** and the
old hostnames do not need to resolve. Mount the disk, find the repos, clone them locally.

```bash
# Find bare repos wherever they were kept
sudo find / -maxdepth 7 -type d -name "*.git" 2>/dev/null
sudo find / -maxdepth 7 -type d \( -name repositories -o -name gitolite-admin \) 2>/dev/null
ls -la /home/git /srv/git /var/lib/gitea /opt/gitea 2>/dev/null

# Recover one, no server involved
git clone --mirror /path/to/thing.git ./thing.git
git -C ./thing.git log --all --oneline | head
```

Then **push every recovered repo to GitHub under Aurora-Punks** (private). The point is not tidiness,
it is that these stop being one copy on one box that is about to be reinstalled.

### 2.2 Perforce second, because it needs the daemon

Unlike Git, a P4 depot is not directly readable: metadata lives in `db.*` files that need `p4d`.

1. Locate `P4ROOT` and the `p4d` binary (`sudo find / -name "p4d" -o -name "db.domain" 2>/dev/null`).
2. Start `p4d` bound to localhost only. Do not expose it.
3. Take a checkpoint immediately: `p4d -r $P4ROOT -jc`. That plus the depot files is the backup.
4. Then enumerate: `p4 depots`, `p4 streams`, `p4 clients`, `p4 changes -m 20`.
5. Note: a `db.have` corruption was handled on AP Perforce in April 2026 (support case #01574233).
   If `p4d` complains, that is prior art, not a new disaster.

### 2.3 Only then decide what the machine becomes

With Git mirrored to GitHub and a P4 checkpoint copied off, the box is free to be reinstalled as the
Assistant host. Before that point it is an archive, not a server.

## 3. Petter's Windows desktop

Same rule, cheaper checks. Before installing Visual Studio or anything else:

1. **Sweep for Git remotes.** Even now that we know the server, a leftover clone confirms the exact
   host and path, and may hold commits never pushed back.

   ```powershell
   Get-ChildItem -Path C:\,D:\ -Filter config -Recurse -Force -ErrorAction SilentlyContinue |
     Where-Object { $_.DirectoryName -like "*\.git" } |
     ForEach-Object { Select-String -Path $_.FullName -Pattern "url\s*=" }
   ```

2. **Look for the wrapper and the Unreal tool locally**: `Documents`, `source`, `repos`,
   `Unreal Projects`, `Perforce`, and any drive root workspace folders. If he worked locally and the
   server was already down, the newest version is here and nowhere else.
3. **Perforce workspace config** (`.p4config`, `P4CLIENT`, `P4PORT` in the user environment) names
   the server and his client spec, which shortcuts 2.2.
4. Copy anything found to the VPS before the machine is repurposed.

Details for the build-machine side of that work are in
[curveball/drafts/build_machine_prep.md](../curveball/drafts/build_machine_prep.md).

## 4. Worth a look while you are in there, cheap

1. **Any Block'Em! web build.** Wavedash's agreement (Kyler, 2026-01-15) says they "commit back to
   the original location of code" and that game-specific improvements are ours to reuse on other
   platforms. `Aurora-Punks/block-em` has had no push since 2026-01-07 while the porting ran January
   to March, so their work went somewhere else. The internal Git is a long shot given the box was
   likely already dormant, but it costs one `ls` while the disk is mounted. That code is the biggest
   available shortcut to Poki and CrazyGames.
2. **Old build agents or CI config**, which would document how console builds were actually produced
   in 2022 to 2023.

## 5. What to report back

For each machine, a short list: what was found, where it was copied to, and what is now mirrored on
GitHub. That list is what tells us whether the console port starts from real prior work or from the
2024 GitHub state.
