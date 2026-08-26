---
name: Content Editor Agent Learnings
description: Cross-project knowledge accumulated by the Content Editor agent from video/image editing and social posting
type: agent_memory
agent: content_editor
---

# Content Editor Learnings

## Video Production

- Camera centering: must verify party position at exact timestamps, not scene-start frames [ToA, 2026-03]
- Slower panning preferred over quick cuts between segments [ToA, 2026-03]
- 608px to 1080px upscale is inherently soft; Lanczos helps but limited [ToA, 2026-03]
- ASS subtitle fonts: Cinzel Decorative 110pt for titles, Montserrat 78pt for body text [ToA, 2026-03]

## Social Media

- LinkedIn event content works best as a 6-post arc: 2 pre (announcement + thought leadership), 2 at (vibe + hot take), 2 post (recap + deep dive). The deep dive post is where the consulting CTA lives. [Personal Brand, 2026-04]
- Cross-referencing multiple events in post-event content doubles visibility. When DD and NGC are back-to-back, each post-event recap should mention the other. [Personal Brand, 2026-04]
- Building-in-public series need real numbers in brackets that Robert fills in. Never fabricate metrics. Template the structure but flag every data point that needs real input. [ToA, 2026-04]
- LinkedIn thought leadership posts (no image, pure opinion) work well as pre-event engagement bait since everyone has opinions on process/business topics. [Personal Brand, 2026-04]

## Orchestration

- A "one-line brief → multi-platform draft" pattern works as a *front-door skill* into `content_production_workflow`, not a parallel pipeline. The orchestration skill plans (platform-adapt + reuse-check + Content Package); production builds (build_reel.py / build_carousels.py). Keep them as separate skills so the orchestration doesn't accidentally re-implement editing. [ToA / gen-104, 2026-05]
- Machine-readable YAML block in `client_channels.md` (`active_platforms`, `publish_capable`, `asset_root`, paths to calendar/tracking/brand) is the load-bearing data structure — without it, orchestration falls back to asking Robert which platforms are active. Prove the shape on one client (ToA) before replicating. [gen-104, 2026-05]
- Approval is per-platform, not per-package. Robert may approve Instagram while skipping LinkedIn for the same brief; orchestration output must list each platform as its own approve/edit/skip decision. [gen-104, 2026-05]
- Skip a new `/post` slash command — `/content $ARGUMENTS` covers it. Triggers fire on wording ("post about X for Y"), not command name. Adding command surface area is dead weight. [gen-104, 2026-05]

## Brand Guidelines

_No learnings yet._

## Platform Specs

- PlayStation Store promotional submissions (Mid-Year Deals, July Savings, etc.) are separate from content creation — they require upfront parameter decisions (which regions, discount %, duration) before any Content Editor work. Content Editor's role is research/asset drafting; actual PS Partners portal submission is Robert's call. When a PS Store task arrives, escalate via IPC to confirm region/discount/approval before proceeding. [ToA, 2026-06-01]
