---
name: reference_vps_capacity
description: "What the VPS actually is (CPX32, 8GB) and what a Claude session costs (~1GB) — governs how freely to spawn agents/sessions"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f8ffe187-dd9d-4c62-a3c8-33c89e7fef56
  modified: 2026-07-22T18:04:52.661Z
---

The VPS (`board.runatyr.games`, `ubuntu-8gb-hel1-1`, Hetzner Helsinki) is a **CPX32**:
4 vCPU AMD EPYC-Genoa, **7.6 GB usable RAM**, 160 GB SSD, 4 GB swap, $41.99/mo.
This is the whole runtime - see [[feedback_vps_operating_environment]].

**The number that matters: one Claude Code session costs ~900 MB - 1.1 GB.**
Every session spawns its **own private MCP stack** (gdrive, jira, confluence, gmail,
gmail-personal, rag, whatsapp, linkedin) - nothing is shared between sessions. Measured
2026-07-22: 893 MB across 9 processes for a session, plus ~300 MB for `claude` itself.

Practical ceiling: **two concurrent sessions is comfortable, four is the strain point.**
Closing a finished conversation frees the whole ~900 MB stack immediately. Sessions are
conversations in the Claude panel, **not** VS Code windows - four conversations in one
browser tab cost exactly the same as four windows.

**Corrected 2026-08-19: the failure mode is swap starvation, not OOM.** This memory used to
say four sessions "causes OOM kills". During the 2026-08-17 incident that made code-server
unusable there were **zero OOM kills in the journal**, and there have been none since. What
actually happens: `code-server.service` carried `MemoryHigh=2G` with `MemoryMax=infinity` AND
`MemorySwapMax=infinity`, so the cgroup pinned at its soft limit and reclaim pushed pages into
the 4 GB swap without any bound until everything sat in I/O wait. Load hit ~11 on 4 cores with
near-zero CPU. **Watching for OOM kills means watching for a signal that never arrives.**

**Watch these instead**, all on
`/sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/app.slice/code-server.service/`:
- `memory.events` → the `high` counter. 8521 throttle events was the tell that the soft cap was
  pinned; `max`/`oom`/`oom_kill` all stayed 0.
- `memory.swap.current` against `memory.swap.max`.
- `vmstat` si/so sustained non-zero is real thrash; a parked swap figure is a swappiness artifact
  (swappiness is now **10**, was 60).

**Limits now in force** (set via `systemctl --user set-property`, persisted in
`~/.config/systemd/user.control/code-server.service.d/`, applied live without a restart):
`MemoryHigh=2.5G`, `MemoryMax=3.5G`, `MemorySwapMax=1G`. The swap cap is the load-bearing one —
`MemoryHigh` without `MemorySwapMax` is not a guard, it is a swap pump. See [[devops_learnings]]
2026-08-18.

**Upgrade deferred 2026-07-22, still deferred 2026-08-19.** CPX32 → CPX42 (8 vCPU / 16 GB) is
$81.99/mo, i.e. +$480/yr, and half of that is CPU that sits near idle. The old re-evaluation
trigger ("upgrade only if OOM kills recur", date ~2026-08-05) was **the wrong signal** and has
passed unmet. **New trigger: upgrade if the cgroup hits `memory.max` (the `max` counter in
`memory.events` leaves 0) or `vmstat` si/so stays non-zero with low available RAM** — that is
real pressure the limits cannot absorb. Throttling alone (`high` climbing) is the guard working
as designed, not a reason to pay. Hetzner's rescale page offers
a **CPU-and-RAM-only** option that keeps the disk and is reversible - use that one. Note
rescaling cannot change architecture, so ARM/Ampere plans are unavailable regardless of price.

Optimisation history and per-service memory figures live in DevOps learnings and `db-285`.
