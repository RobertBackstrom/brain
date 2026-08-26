---
name: Game Engine MCP Landscape
description: MCP servers for Unity, Unreal, Godot and game backends, plus the architectural constraint that decides whether an engine MCP is usable at all
type: reference
originSessionId: a741bd10-9dc6-4a08-988d-6aad3e576458
modified: 2026-08-05T22:08:18.034Z
---

Refreshed 2026-08-05 (previous version was 116 days old and predated Epic shipping a first-party MCP).

## Read this before picking one

**Every Unreal MCP runs its server inside a live UE Editor process.** That single fact decides most
of the question:

1. It cannot run on the Hetzner VPS. Headless Linux, 8 GB, no GPU, no editor.
2. It has to live on a Windows dev machine, which breaks the "VPS is the runtime" default and makes
   the capability depend on someone's box being awake.
3. It gives you *live editor manipulation* (building levels, iterating in PIE). It does **not** give
   you code understanding, which is what most of our work actually needs.

**For reading and reviewing a UE project, export instead of remote-control.** Dump Blueprint graphs
to text once (T3D or JSON, via a commandlet or Python editor scripting) on a machine that can run the
editor, commit the dumps, index them. That is permanent, VPS-native, greppable by every agent, and
survives the laptop being asleep. Reach for an MCP only when live manipulation is the actual need.

Robert, 2026-08-04: "inget självändamål att skohorna en mcp". Constraint is temporary, see
[[project_baremetal_migration]], but do not build for a machine that does not exist yet.

## Unreal

- **Epic's official ModelContextProtocol plugin** — ships with **UE 5.8**, experimental, **requires a
  source build**. Embeds an MCP server in the editor over local HTTP. Nothing official exists for
  5.3 through 5.7, which is where most shipping projects actually sit (Curveball is 5.3).
- **Third party** targets 5.7/5.8 almost exclusively now: StraySpark (commercial, 200+ tools),
  `remiphilippe/mcp-unreal`, `tumourlove/monolith`, `ChiR24/Unreal_mcp`, `lilklon/UEBlueprintMCP`.
  A few community plugins claim 5.3+ coverage; verify version support before committing, it is the
  thing that most often turns out to be aspirational.
- The older `chongdashu/unreal-mcp` reference from the 2026-04 version of this note is superseded.

## Unity

- Unity 6.3+ ships a built-in MCP bridge (docs.unity3d.com).
- OSS: `CoplayDev/unity-mcp`, `CoderGamester/mcp-unity`.
- Same editor-process constraint applies, though Unity is far lighter than UE to run.

## Godot

- `Coding-Solo/godot-mcp` (foundational), GodotIQ MCP (spatial, Godot 4), Godot MCP Pro (commercial).

## Game data / backend

- PlayFab: `akiojin/playfab-mcp-server`. GameAnalytics: native MCP for telemetry. AccelByte: crash
  analysis. None of these need an editor, so they are the ones that can actually live on the VPS.

## Discovery

mcpmarket.com/categories/game-development · github.com/TensorBlock/awesome-mcp-servers (gaming.md)

## Why this matters

Still a consulting differentiator, but sell it accurately: the useful pitch is AI-assisted dev
workflow grounded in indexed source, not a demo of an agent dragging actors around a viewport.
