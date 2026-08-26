# Getting our work into The Gang's repo

| | |
|---|---|
| **Date** | 2026-08-04 |
| **Author** | The Assistant |
| **Question** | We are writing code now, against a zip, with no access to their repo. How does it land in a branch on theirs? |
| **Status** | Asked The Gang for p4/git access 2026-08-04. No answer yet. This plan works either way. |

## 1. The short answer

**The best migration plan is to not need one.** If The Gang gives us Perforce access, we work
directly in their depot on a branch, and the question dissolves. Everything below is about making
that outcome cheap to reach, and surviving the outcome where it never arrives.

Two properties of what we are building make this much less risky than it sounds.

**Almost all of our work is new files.** The whole `Online/` layer is additive: six new headers plus
their implementations in a folder that does not exist in their tree. New files cannot conflict.

**The edits to their existing files are a small enumerable set.** From the Fable plan and the backend
spec, the files we will actually modify are:

| File | Change |
|---|---|
| `MatchmakingSubsystem.cpp/.h` | internals swapped, signatures frozen |
| `Backend/GamePartySubsystem.cpp` | internals swapped, delegates frozen |
| `Backend/BackendMessagePump.cpp` | HTTP poll becomes a local bus |
| `MLCMatchmakingHandler.cpp` | internals only |
| `GameLiftClientComponent.*` | deleted |
| `Mogadishu.Build.cs` | module dependencies |
| `BladeBallArena.uproject` | plugin list |
| `Config/*.ini` | NetDriver, app id, build target |
| `LootLocker/LootLockerServerGranter.*`, `LootLockerServerLoadoutValidator.*` | call sites rerouted |

That is roughly a dozen files out of 182. The merge surface is small by construction, because the
abstraction-layer approach was chosen partly to keep it that way.

## 2. The baseline discipline, starting now

Whatever repo we end up on, everything we do from here is expressed as **a diff against an
identified vendor state**. That is the one thing that has to be right from day one, and it costs
nothing to do.

1. **Commit the delivered zip verbatim as the first commit**, on a branch called `vendor`, tagged
   `vendor/bba-zip-2026-06-04`. Extracted exactly as received, nothing tidied, nothing reformatted.
   Never edited afterwards.
2. **All our work branches off that tag.** Every change we make is then a clean diff against a state
   The Gang can recognise.
3. **When their repo arrives**, sync their mainline and commit it onto the same `vendor` branch as
   `vendor/p4-<changelist>`. Now two things become visible that are otherwise guesswork:
   - `git diff vendor/bba-zip-2026-06-04 vendor/p4-<CL>` shows **what The Gang changed in the two
     months since Olle sent the zip**. If that is empty, we are lucky. If it is not, we need to know
     before we merge, not after.
   - our branch rebases onto the newer vendor state, and conflicts surface in the dozen files above
     rather than everywhere.
4. **Delivering back** is then either a Perforce changelist generated from that diff, or a Git branch
   they pull, depending on what they run.

This is the standard vendor-branch pattern. Nothing clever, but skipping it is how you end up with a
folder of files and no way to prove what they were derived from.

## 3. Perforce or Git

They ran Perforce (`.p4ignore` is in the tree). Recommendation if we get access: **use Perforce for
the project and do not fight it.**

Perforce is genuinely the right tool for a 5.2 GB binary asset tree with exclusive checkout, and
their history lives there. Forcing that into Git LFS creates a storage bill, a migration risk and a
second source of truth, in exchange for tooling preferences.

What I would keep in Git regardless, as a mirror rather than a source of truth:

1. `Source/` (roughly 1 MB of C++)
2. `Config/`
3. `/BlueprintExports/` once WP0.3 produces it
4. `/Tools/`

That is the text, which is what I need for review, diffing and RAG indexing, and it is small enough
to be free. The binary assets stay in Perforce where they belong. If we later need to edit Blueprints
(WP0.3 will tell us how many), those edits happen in Perforce like any other asset change.

If they cannot give us Perforce access, then we own a Git repo with LFS, and the LFS host matters:
GitHub's LFS pricing at 5.2 GB is not free. Azure DevOps offers unlimited free LFS and is the usual
escape hatch. That decision only has to be made in the no-Perforce branch of the plan.

## 4. What happens if they do not answer

We can start B1 (first build) against the zip. It is incomplete (the `MajorLeagueCurveball` build
target it references is missing) but that is a known defect to work around rather than a blocker.
Everything in Lane A is unaffected.

The cost of a long silence is not being blocked, it is **drift**. Their tree has already moved two
months past our zip, or it has not, and we cannot tell which. Every week we build on a stale baseline
without knowing, the eventual reconciliation gets more expensive.

So: if Olle has not answered by end of week, worth a nudge. Not because we are stuck, but because the
cheapest moment to discover a divergence is before we have built on top of it.

## 5. One thing to settle in the agreement

Where our work lands legally is a different question from where it lands technically. Robert has
ruled that new files carry The Gang's existing copyright header, which is the right call for keeping
the tree consistent and matches the co-dev shape. Worth making sure the co-dev agreement says the
same thing explicitly, so the header and the contract agree rather than the header being the only
record.
