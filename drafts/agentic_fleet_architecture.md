# The agentic fleet: one subnet, two planes

| | |
|---|---|
| **Date written** | 2026-08-22 |
| **Supersedes / extends** | [fleet_network_tailscale.md](fleet_network_tailscale.md) (2026-08-14), which stays correct on the overlay and the six rules |
| **Decided with Robert 2026-08-22** | Nitro becomes canonical `brain`. Hetzner drops to `edge` plus off-site backup. Forge stays the combined build and art box. Provider layer gets OpenAI, Gemini and local Ollama. |
| **Related** | [[project_baremetal_migration]], [[project_the_assistant]], [[reference_vps_capacity]], [[feedback_vps_operating_environment]], [[feedback_security_defaults]] |

## 1. What Robert asked for

A 24/7 agentic network living inside one subnet, behind a mobile 5G router that travels with the
team, reachable at `code.runatyr.games` from any machine. Fourteen functions: a RAG that keeps
learning, a Brain with agents that can borrow idle machines so OOM stops being a worry,
self-improvement loops, an assistant UX for biz-dev leads and PM and contract signing, headless dev
environments for porting and for Unreal and Unity, an art pipeline from concept to rigged animated
asset in engine, a QA and optimisation process with honest dead-tool reporting, LLM agnosticism,
security processes, bookkeeping through to annual accounts, pitch processes and websites, and short
form content.

Most of it exists already. It is just scattered across two hosts that are quietly diverging.

## 2. The five findings that shape the design

1. **The brain is split in half right now.** Robert works interactively on Nitro, while the Death
   Board, the cron suite, the RAG indexer, the security timers and the static sites all still run on
   the Hetzner box. Two masterbrains are writing apart from each other.
2. **The learning RAG is frozen on this side.** Nitro's `rag.db` is 8.2 GB, 453 718 documents,
   726 150 chunks, last written 2026-08-21 11:23. Nothing local updates it. The live index moves on
   Hetzner.
3. **The OOM worry is an architecture problem, not a RAM problem.** Every Claude session starts its
   **own private MCP stack**, about 900 MB across 9 processes, shared with nothing. Four sessions
   measured 4.3 GB on a 7.6 GB box. Buying RAM scales the symptom linearly. A **shared MCP layer**
   makes it constant. That single change is what turns OOM into a non-question.
4. **A 5G router means the whole fleet lives behind CGNAT.** There is no inbound, ever. Cloudflare
   Tunnel as the front door plus Tailscale between machines is already the right shape and survives
   a physical move. The trap is the move itself: when the LAN changes, `tailscaled` can land on an
   APIPA `169.254.x.x` address and **not recover on its own**. Observed on forge on 2026-08-18. The
   peer symptom is `offline, tx NNNN rx 0` while the node has working general internet, and the fix
   is a service restart, not a reinstall. This needs a boot watchdog before the first relocation.
5. **Only one node is off site.** Lose power or 5G at the flat and everything goes down together.
   Hetzner is currently the only machine that does not share that fate, which is precisely the role
   it should keep after it stops being the brain.

## 3. The fleet

`brain` is a **role, not a machine**. Rule 2 of the earlier fleet doc: the Assistant host is `brain`
whatever silicon it runs on this month, so the handover is a rename in the admin console and nothing
that referenced `brain` notices.

| Node | Hardware | Role after this plan | State today |
|---|---|---|---|
| `brain` (target) | Nitro, i5-12400F, 12 threads, 16 GB, 228 GB NVMe, GT 1030 | **Control plane.** Death Board, agent router, scheduler, RAG index, health. Also code-server, reels, web. | Online, serving code.runatyr.games and TeamCity, **zero cron** |
| `edge` | Hetzner CPX32, 4 vCPU, 7.6 GB | Off-site backup of masterbrain and RAG, plus the watchdog that alerts when the home net is down. Shrink to the smallest plan. | Online, still running everything, currently unreachable from Nitro |
| `forge` | ASUS 7950X3D, 64 GB, 2x2 TB NVMe, RTX 3060 12 GB | **Build and art.** Unreal, Unity, packaging, Steam depots, ComfyUI, local Ollama. | Online, doing no agent work |
| `vcsboy` | HPE ProLiant MicroServer Gen10 Plus v2, Windows, VROC | Version control only, not a compute node. Perforce: `groundzero`, `gzue`, `gzmarketplace`. | Online, SSL front door down (db-301) |
| `linus`, `anastasia` | 2x RTX 4060 workstations | **Opportunistic** compute. Idle hours only, never during their working day. | Not enrolled |
| `david96gb` | Unknown | Opportunistic compute once specced. | Enrolled, offline since 2026-08-21 |
| Tom's old box | Unknown | To be specced before assigning a role. | Not enrolled |

**GPU note that matters for the art pipeline.** Forge's RTX 3060 carries 12 GB of VRAM against the
desktop 4060's 8 GB. For diffusion the VRAM ceiling beats raw speed, so the older card is the better
art card and forge stays primary. This flips only if the two machines turn out to be 4060 **Ti 16 GB**,
which is worth confirming before any work is routed to them.

## 4. Two planes

**Control plane.** Small, always on, exactly one machine. Death Board, agent router, scheduler, RAG
index, health monitoring. This is `brain`.

**Compute plane.** Elastic, allowed to die at any moment. Agents and builds run on whatever machine
is free. TeamCity already runs on Nitro on port 8111 and is built for exactly this: agents on forge,
on the opportunistic workstations, with queues and capacity rules. **We do not need to build a job
dispatcher. We need to connect the agent router to the one that already exists.**

### Why builds and art can share forge

A headless Unreal cook is CPU, RAM and disk bound. Shader compilation saturates every core and a
large cook can want 32 to 64 GB. Diffusion is GPU and VRAM bound with low CPU. The two profiles are
largely complementary, so one 7950X3D with 64 GB and two NVMe drives can carry both, provided that:

1. Jobs are **queued, not run concurrently**, which TeamCity gives for free with a per-agent
   concurrency limit of 1.
2. The build workspace and the model cache sit on **different drives**, because disk I/O is the one
   resource they genuinely fight over.
3. Nobody expects to do **interactive** art work on that box while a build pins 32 threads. A queued
   headless job does not care about interactivity. A human does.

## 5. The path

| Phase | What | Blocked by |
|---|---|---|
| 0 | SSH key onto brain, inventory what actually runs there | Robert pasting one line |
| 1 | Freeze the divergence, pick the canonical side, stop double writes | Phase 0 |
| 2 | Move the control plane to Nitro, disable on Hetzner, reconcile VPS-only changes | Phase 1 |
| 3 | Shared MCP layer, then TeamCity agents on forge. **OOM stops being a worry here.** | Phase 2 |
| 4 | Headless Unity and Unreal on forge, porting matrix | Phase 3 |
| 5 | Art pipeline on the forge GPU | Phase 3 |
| 6 | Tool health contracts and the LLM provider layer | Phase 2 |
| 7 | Enroll the opportunistic machines | Phase 3 |

**Reconciliation direction, decided:** Nitro is the winning side. Anything written on Hetzner since
the repoint merges **into** Nitro. New tickets written on Nitro from now on are therefore on the
canonical side and do not deepen the split.

## 6. The two genuine gaps

Everything else on Robert's list exists in some form. These two do not.

### 6.1 Tool health, which is the "11 MCP issue"

The failure mode that actually bit was the **silent zombie**: the WhatsApp bridge reported
`ready: true` for 25.5 hours while every real call returned a 500 on a detached frame. The mirror
failure is the **zombie probe**: a parked integration that keeps its health check becomes a spammer,
and linkedin-sd alerted every 4 hours for 361 hours about a failure that was known and diagnosed.

The right shape is a **tool contract**. Every MCP and tool declares a cheap probe that performs a
**real call** rather than reading a status flag, results land on a health view, a dead tool opens or
updates exactly **one** ticket with dedup, and parking a tool automatically retires its probe.

### 6.2 The provider layer

`agent-router.js` already has `resolveModel()` and a four-tier ladder. What is missing is a provider
abstraction underneath the tier names, so `sonnet` can resolve to a different vendor without a single
call site changing. Robert selected OpenAI, Google Gemini and local Ollama on forge. With that in
place, The Reviewer pattern generalises from "second opinion from a stronger model" to "second
opinion from a **different vendor**", which is what QA actually wants.

## 7. Risks worth naming

1. **The relocation risk.** Moving the 5G router changes every LAN address and can strand nodes on
   APIPA until `tailscaled` is kicked. Fix the watchdog before the first move, not after.
2. **The single-site risk.** One power cut takes down the brain, the compute and the front door at
   once. The `edge` role is the mitigation and should not be skipped to save a few euros.
3. **The divergence window.** Every hour before phase 2 lands is another hour of two masterbrains
   drifting. This is the item with a real clock on it.
4. **Opportunistic nodes belong to people.** Linus and Anastasia use those machines for work. Idle
   hours only, opt in, and visible to them, or the fleet becomes a political problem instead of a
   technical one.
