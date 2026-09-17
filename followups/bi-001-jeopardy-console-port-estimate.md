---
project: bi
status: open
priority: high
created: 2026-09-16
updated: 2026-09-16
type: deal
owner: Robert
---

# bi-001 - Jeopardy! console port, initial estimate delivered

## State

Initial estimate delivered 2026-09-16 as a gated web pitch at
https://pitch.aurorapunks.com/bandit-island/ (`bandit` / creds in `assistant/pitch-auth.json`).
Cover mail drafted on the existing thread `1a0a9cb279aa62e5`, voice-passed, sitting in Gmail
drafts for Robert to send.

Waiting on Bandit Island. Woody 2026-09-16 16:14: Amazon talks are mid-flight, positive signals
but nothing decided. They need an early approval tier cleared before source-code access, and he
expects to know more early in the week of 21 Sep.

## The estimate as delivered

Scope is six SKUs: PS5, PS4, Xbox Series X/S, Xbox One, Switch, Switch 2. Steam is theirs.
Five roles, 30,7 FTE-months, **3 684 000 SEK** at the 120 000 SEK per
FTE-month rate Robert gave them in the office on 11 Sep.

Confirmed by Robert 17 Sep: engine is **Unity**; the title is **unreleased** with a target
release of February 2027, not shipping as first assumed; and Robert bills **EP at 20 %**
allocation rather than giving it away, which is the fifth role and the 264 000 SEK difference
from the 16 Sep figure of 3 420 000.

| Phase | Window | FTE-mo |
|---|---|---|
| Architecture + companion prototype | Dec 2026 to Feb 2027 | 8,1 |
| Main port, six SKUs | Mar to Aug 2027 | 19,2 |
| Certification | Sep to Oct 2027 | 3,4 |

Release-ready Nov 2027. The pre-phase deliberately runs while they finish the game, so the
riskiest unknown is settled before the expensive months start. Because the title is unreleased,
the pre-phase works against a build that is still moving, which is now stated as a weakness in
the SWOT rather than glossed.

Alternates priced in the pitch: the second quiz title on the same codebase, 8 to 10 FTE-months;
gamepad-only with no phone and no voice, roughly 1,1 MSEK and explicitly not recommended.
QA and release management are excluded on the stated assumption that Amazon covers them, with
roughly 600 000 SEK named as the add if that turns out to be wrong.

## The technical call the pitch rests on

Luna gives them phone-as-controller and voice answering as **platform services**, running in
Amazon's data centre beside the game. None of it survives the move to a console in a living room.
The replacement is a room-code join into a phone browser with a small hosted relay, which is the
model party games have shipped on console for a decade.

The load-bearing decision: **speech recognition runs on the relay, not on the console.** The phone
captures audio and sends it to the relay, the relay returns text, the console never sees audio and
never loads a speech model. That removes the Switch 1 memory problem Robert was worried about and
gives one identical code path across all six SKUs.

Why the phone is mandatory and not a nice-to-have: **Switch 1 has no microphone anywhere in the
system**, not in the console and not in the Joy-Con, only via a wired headset the player has to
own. Xbox controllers have none either. Only PS5 (DualSense mic array) and Switch 2 (system mic)
have one. For four people answering out loud on all six SKUs, the phone is the only microphone
reliably in the room.

## Open items

- [ ] Source-code access. Blocked on Amazon. Everything else is downstream of it, and the estimate is worth materially more once we have had two weeks with the code.
- [ ] How separable the Luna input layer is from game logic. Engine confirmed Unity, so that half is closed; if input handling is woven through game logic the port side still grows.
- [ ] How coupled the game is to Luna identity, entitlement, session and storage services beyond input and voice.
- [ ] Jeopardy! rights for console distribution. Not our work, on our critical path. Cheaper to start in parallel with Gate 1 than to find at submission.
- [ ] Who publishes and who holds the platform accounts, Amazon or Bandit Island.
- [ ] Confirm whether Amazon really does cover QA and release management.
- [ ] Old-gen in or out. PS4 and Xbox One are the one line that removes cleanly, roughly two months of the porting engineer.

## Next

If nothing has landed by the end of the week of 21 Sep, a light nudge to Woody rather than a chase.
The relationship is personal-friend tier with Stephen and the delay is genuinely on Amazon's side.
