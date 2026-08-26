#!/usr/bin/env python3
"""
Pecha Kucha 2026 - Image generation script for Aurora Punks
fal.ai Flux.dev backend. Runs serially to avoid rate-limit issues.
"""

import json
import os
import time
import requests
from pathlib import Path
from datetime import datetime

FAL_KEY = "a6c4102c-3231-4859-b446-23012abe2de4:5beb27d81041d97a348b71a0710e59ef"
FAL_ENDPOINT = "https://fal.run/fal-ai/flux/dev"
OUT_DIR = Path("/home/assistant/projects/clients/aurora_punks/pecha_kucha_2026/visuals")
LOG_PATH = OUT_DIR / "generation_log.json"
COST_PER_IMAGE = 0.025
MAX_BUDGET = 1.00

# Flux.dev prompts - adapted from MJ v6.
# MJ-specific syntax removed: --ar 16:9 --style raw --v 6 --seed N
# Aspect ratio folded into image_size parameter (landscape_16_9)
# Style raw guidance folded into: "rough paper grain dominant, avoid over-rendering,
#   avoid smooth AI-generated sheen, avoid clean vector lines"
# Palette cues preserved exactly from brief

GLOBAL_STYLE = (
    "ink-wash gothic illustration on rough paper, "
    "deep Prussian blue (#0d1b2a) and oxblood red (#6b1a1a) dominant palette, "
    "aged gold (#c9a84c) used sparingly as accent only, "
    "bone white (#e8e0cc) highlights, "
    "amber candlelight or ember as sole warm light source, "
    "visible ink grain, rough paper texture throughout, "
    "no clean vector lines, no saturated colors, no modern UI aesthetic, "
    "no studio lighting, no photorealism, no lens flare, "
    "avoid smooth AI-generated sheen, "
    "masterwork illustration, 16:9 widescreen composition"
)

SLIDES = [
    {
        "id": "slide_01",
        "filename": "slide_01_hero.png",
        "is_anchor": True,
        "use_anchor_seed": False,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a solitary figure standing in deep shadow, distorted proportions, elongated limbs, "
            "tattered coat with worn patched details, face partially obscured by shadow and hair, "
            "a faint warm amber glow emanating from the figure's chest as if carrying an ember, "
            "dark surreal background of tangled architectural fragments and gothic arches dissolving into darkness, "
            "occult aesthetic, beautiful darkness composition, "
            "deep Prussian blue and oxblood palette, aged gold accent, bone white highlights on edges, "
            "rough paper texture, visible ink grain throughout, "
            "generous negative space upper right for text overlay, "
            "punk-DIY sensibility meets gothic surrealism, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_03",
        "filename": "slide_03_engines.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a lone figure standing at the prow of a vessel in stormy dark water, "
            "one hand on a worn compass, the other holding a hammer, "
            "wings half-unfurled behind the figure composed of smoke and embers rather than feathers, "
            "returning-hero energy, comeback-and-craft composition, "
            "deep Prussian blue storm sky, oxblood sea, amber ember glow from the wingspread, "
            "rough paper texture, visible ink grain, "
            "single dominant subject with generous negative space upper left for text overlay, "
            "surreal dream-logic atmosphere, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_04",
        "filename": "slide_04_leadership.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a ship captain figure holding a brass compass with cracked glass, "
            "a hairline fracture in the compass glass glowing warm gold from within, "
            "behind the figure a lighthouse beam cuts through fog on one side "
            "while a storm churns on the other side simultaneously, "
            "the captain's expression calm and aware, tattered epaulettes, "
            "distorted surreal proportions, beautiful darkness composition, "
            "deep blue and oxblood palette, aged gold accent on the crack and lantern light, "
            "bone white highlights, rough paper texture, visible ink grain, "
            "generous negative space upper left for text overlay, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_05",
        "filename": "slide_05_ap_2021.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "note": "Fallback - Jillian Mood 2021 press shot not found in Gmail",
        "prompt": (
            "dark atmospheric photographic illustration style, "
            "a small creative collective gathered around a table in a dimly lit Stockholm studio space, "
            "late evening warm practical lighting from desk lamps, "
            "three or four people in their early thirties in casual creative clothing, "
            "looking at laptop screens and printed materials spread on the table, "
            "the space has the feeling of a starting point: sparse furniture, exposed brick or concrete, "
            "a whiteboard with early sketches visible in background, "
            "mood is focused and alive not posed, "
            "analog-warmth aesthetic, slight grain, 2021 vintage photography feel, "
            "deep shadow on periphery, warm practical light center, "
            "16:9 widescreen composition with negative space upper area"
        )
    },
    {
        "id": "slide_07",
        "filename": "slide_07_no_employees.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a mercenary campfire at dusk in a ruined courtyard, "
            "four or five shadowed figures loosely gathered around the fire, "
            "each figure slightly distinct in silhouette - some standing some crouching, "
            "the fire warm and amber, surrounding ruins deep Prussian blue, "
            "no faces visible, implied presence not permanence, camp-without-walls energy, "
            "figures might leave any moment, smoke curling into gothic arches above, "
            "deep shadow with warm ember accents, "
            "rough paper texture, visible grain, "
            "negative space in upper portion for text overlay, "
            "surreal atmosphere, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork ink illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_10",
        "filename": "slide_10_fixer.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "close-up of calm hands at a worn workbench holding delicate repair tools, "
            "the hands work over a partially disassembled mechanical object "
            "that is complex and beautiful - gears and glass and wire, "
            "amber candlelight from one side, deep shadow on the other, "
            "the hands are skilled and unhurried, the opposite of urgency, quiet competence, "
            "the workbench surface scarred wood with scattered small tools, "
            "deep blue and oxblood palette, gold candlelight on the hands, "
            "rough paper texture, visible ink grain, "
            "surreal slightly dreamlike proportions, "
            "generous negative space upper right for text overlay, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_11",
        "filename": "slide_11_pivot.png",
        "is_anchor": False,
        "use_anchor_seed": True,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a ruined gothic cathedral interior, "
            "the shell of the old structure intact: arched windows open to dark sky, stone crumbling, "
            "but inside scaffolding rises and new construction begins within the ruin, "
            "warm amber lanterns hanging from the scaffolding casting light upward against dark stone, "
            "the old bones visible with new life emerging inside them, "
            "beauty-from-ruin composition, surreal dreamlike scale with slightly distorted perspectives, "
            "deep Prussian blue stone and sky, oxblood accent on archways, "
            "aged gold from the lanterns, bone white on the scaffolding, "
            "rough paper texture, visible ink grain, "
            "generous negative space upper left for text overlay, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_14",
        "filename": "slide_14_third_attempt.png",
        "is_anchor": False,
        "use_anchor_seed": True,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a solitary figure crouching in darkness striking a match - this is visibly the third attempt, "
            "two spent matchsticks on the stone floor beside the figure, "
            "the new match just catching with a small warm amber flame emerging, "
            "the figure's face turned toward the tiny flame, third-attempt energy, "
            "quiet determination not despair, "
            "distorted slightly elongated figure proportions, surreal atmosphere, "
            "deep Prussian blue and bone-white palette with the single amber flame as the only warm accent, "
            "rough paper texture, visible ink grain, "
            "generous negative space in upper area for text overlay, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_15",
        "filename": "slide_15_studios_need_fixing.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a tangle of thick old cables and broken connectors on a dark floor, "
            "among the cables a small fire being carefully tended by unseen hands barely visible at frame edge, "
            "the fire warm amber, the cables Prussian blue-black, "
            "a torn and partially-visible roadmap or chart pinned to wall behind "
            "showing routes with gaps and erasures, "
            "send-me-your-broken-things energy, the mess is present but workable, "
            "deep shadow with warm focal light on the fire and map, "
            "rough paper texture, visible ink grain, "
            "generous negative space upper right for text overlay, "
            "surreal slightly dreamlike composition, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_16",
        "filename": "slide_16_peers_fire.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a small intimate circle of five or six figures seated and standing around a low campfire in deep darkness, "
            "the fire modest and warm amber, the figures in quiet conversation, "
            "no faces clearly visible but body language reads as ease and trust not performance, "
            "the surrounding darkness is absolute and comfortable, "
            "warmth-as-network composition, no heroism just fellowship, "
            "distorted slightly surreal figure proportions, "
            "deep Prussian blue darkness, oxblood earth tones underfoot, "
            "aged gold firelight on edges and shoulders, "
            "rough paper texture, visible ink grain, "
            "negative space at top for text overlay, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork gothic illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_17",
        "filename": "slide_17_scars.png",
        "is_anchor": False,
        "use_anchor_seed": True,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "a large dark ceramic vessel occupying most of the frame, "
            "the vessel has been broken and repaired with kintsugi gold joinery, "
            "the gold cracks glow faintly with warm inner light as if the vessel is alive in the repaired places, "
            "the unbroken ceramic is deep oxblood and Prussian blue, "
            "the kintsugi veins aged gold glowing, "
            "the vessel sits on a worn stone surface in deep shadow, "
            "beauty-through-damage composition, surreal slightly dreamlike atmosphere, "
            "rough paper texture, visible ink grain, "
            "generous negative space in upper area for text overlay, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork gothic illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "slide_18",
        "filename": "slide_18_playbook.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "prompt": (
            "ink-wash gothic illustration on rough paper, "
            "hands writing in a worn leather notebook by candlelight, "
            "the notebook open to a densely annotated page with small dense text and diagrams visible but not legible, "
            "the handwriting deliberate and careful, "
            "a single amber candle casting warm light on the hands and page, "
            "deep shadow on all sides, "
            "the hands are experienced not young, the notebook is battle-worn, "
            "a chess piece lying on its side on the table beside the notebook as if deliberately sacrificed, "
            "quiet competence under pressure, "
            "deep Prussian blue shadow, gold candlelight, bone-white page, "
            "rough paper texture, visible ink grain, "
            "generous negative space upper right for text overlay, "
            "no clean vector lines, no photorealism, no smooth sheen, "
            "masterwork gothic illustration, 16:9 widescreen composition"
        )
    },
    {
        "id": "text_plate",
        "filename": "text_plate_dark.png",
        "is_anchor": False,
        "use_anchor_seed": False,
        "prompt": (
            "abstract ink wash texture for presentation slide background, "
            "heavy black ink dispersed into deep Prussian blue water on rough paper, "
            "faint suggestion of gothic architectural linework dissolving into shadow, "
            "no clear subject, no figure, no focal point, near-monotone, very low contrast, "
            "occasional faint gold speck like a distant ember, "
            "rough paper grain very visible throughout, "
            "designed as dark background for white text overlay, "
            "masterwork abstract texture, 16:9 widescreen composition"
        )
    },
]


def generate_image(prompt, seed=None, image_size="landscape_16_9"):
    """Call fal.ai Flux.dev and return (image_url, seed_used, request_id)."""
    headers = {
        "Authorization": f"Key {FAL_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "prompt": prompt,
        "image_size": image_size,
        "num_images": 1,
        "enable_safety_checker": True
    }
    if seed is not None:
        body["seed"] = seed

    resp = requests.post(FAL_ENDPOINT, headers=headers, json=body, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    images = data.get("images", [])
    if not images:
        raise ValueError(f"No images in response: {data}")

    img_url = images[0]["url"]
    seed_used = data.get("seed")
    request_id = data.get("request_id", "unknown")
    return img_url, seed_used, request_id


def download_image(url, dest_path):
    """Download image from URL to dest_path."""
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    with open(dest_path, "wb") as f:
        f.write(resp.content)


def build_contact_sheet(visuals_dir, log_entries, out_path):
    """Build a 4x4 contact sheet from generated images."""
    from PIL import Image, ImageDraw, ImageFont

    images = []
    labels = []
    for entry in log_entries:
        if entry.get("skipped"):
            continue
        img_path = visuals_dir / entry["filename"]
        if img_path.exists():
            images.append(str(img_path))
            labels.append(entry["id"])

    if not images:
        print("No images to build contact sheet from.")
        return

    COLS = 4
    THUMB_W = 480
    THUMB_H = 270  # 16:9
    LABEL_H = 24
    PADDING = 6
    ROWS = (len(images) + COLS - 1) // COLS

    sheet_w = COLS * (THUMB_W + PADDING) + PADDING
    sheet_h = ROWS * (THUMB_H + LABEL_H + PADDING) + PADDING

    sheet = Image.new("RGB", (sheet_w, sheet_h), color=(10, 14, 20))
    draw = ImageDraw.Draw(sheet)

    for i, (img_path, label) in enumerate(zip(images, labels)):
        col = i % COLS
        row = i // COLS
        x = PADDING + col * (THUMB_W + PADDING)
        y = PADDING + row * (THUMB_H + LABEL_H + PADDING)

        try:
            img = Image.open(img_path).convert("RGB")
            img = img.resize((THUMB_W, THUMB_H), Image.LANCZOS)
            sheet.paste(img, (x, y))
        except Exception as e:
            print(f"  Could not load {img_path}: {e}")

        draw.text((x + 4, y + THUMB_H + 4), label, fill=(200, 180, 120))

    sheet.save(str(out_path), "PNG")
    print(f"Contact sheet saved: {out_path}")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    log = []
    total_cost = 0.0
    anchor_seed = None
    consecutive_failures = 0
    start_time = time.time()

    # Load existing log if present (resumable)
    if LOG_PATH.exists():
        with open(LOG_PATH) as f:
            log = json.load(f)
        existing_ids = {e["id"] for e in log if not e.get("failed")}
        print(f"Resuming: {len(existing_ids)} already done.")
        # Recover anchor seed
        for entry in log:
            if entry.get("is_anchor") and entry.get("seed"):
                anchor_seed = entry["seed"]
                print(f"Recovered anchor seed: {anchor_seed}")
    else:
        existing_ids = set()

    for slide in SLIDES:
        slide_id = slide["id"]
        filename = slide["filename"]
        dest = OUT_DIR / filename

        # Skip if already done
        if slide_id in existing_ids:
            print(f"  SKIP (already done): {slide_id}")
            continue

        # Budget check
        if total_cost >= MAX_BUDGET:
            print(f"BUDGET EXCEEDED (${total_cost:.3f}). Stopping.")
            break

        # Determine seed
        seed_to_use = None
        if slide.get("use_anchor_seed") and anchor_seed is not None:
            seed_to_use = anchor_seed
            print(f"  Using anchor seed {anchor_seed} for {slide_id}")

        prompt = slide["prompt"]
        print(f"\n[{slide_id}] Generating: {filename}")
        print(f"  Prompt length: {len(prompt)} chars")

        attempt = 0
        success = False
        while attempt < 3 and not success:
            attempt += 1
            try:
                t0 = time.time()
                img_url, seed_used, request_id = generate_image(
                    prompt=prompt,
                    seed=seed_to_use
                )
                elapsed = time.time() - t0
                print(f"  Attempt {attempt} OK in {elapsed:.1f}s, seed={seed_used}, req={request_id}")

                download_image(img_url, dest)
                print(f"  Saved: {dest}")

                total_cost += COST_PER_IMAGE
                consecutive_failures = 0
                success = True

                entry = {
                    "id": slide_id,
                    "filename": filename,
                    "prompt": prompt,
                    "seed": seed_used,
                    "seed_source": "anchor_reuse" if slide.get("use_anchor_seed") else ("anchor" if slide.get("is_anchor") else "fresh"),
                    "request_id": request_id,
                    "cost_usd": COST_PER_IMAGE,
                    "elapsed_sec": round(elapsed, 1),
                    "attempt": attempt,
                    "is_anchor": slide.get("is_anchor", False),
                    "note": slide.get("note", ""),
                    "timestamp": datetime.utcnow().isoformat(),
                    "failed": False
                }
                log.append(entry)

                # If this is the anchor, capture seed
                if slide.get("is_anchor"):
                    anchor_seed = seed_used
                    print(f"  ANCHOR SEED LOCKED: {anchor_seed}")

            except Exception as e:
                print(f"  Attempt {attempt} FAILED: {e}")
                consecutive_failures += 1
                if consecutive_failures >= 3:
                    print("3 consecutive failures. Stopping.")
                    log.append({
                        "id": slide_id,
                        "filename": filename,
                        "failed": True,
                        "error": str(e),
                        "timestamp": datetime.utcnow().isoformat()
                    })
                    with open(LOG_PATH, "w") as f:
                        json.dump(log, f, indent=2)
                    return
                if attempt < 3:
                    print("  Retrying with fresh seed...")
                    seed_to_use = None  # clear seed for retry
                    time.sleep(2)

        if not success:
            log.append({
                "id": slide_id,
                "filename": filename,
                "failed": True,
                "error": "3 attempts exhausted",
                "timestamp": datetime.utcnow().isoformat()
            })

        # Save log after each image
        with open(LOG_PATH, "w") as f:
            json.dump(log, f, indent=2)

    # Add skipped slide note
    slide_9_already = any(e["id"] == "slide_09" for e in log)
    if not slide_9_already:
        log.append({
            "id": "slide_09",
            "filename": "slide_09_proof.png",
            "skipped": True,
            "note": "skipped - public assets (The Finals, Ready or Not key art + Raw Fury logo). Robert to source manually.",
            "timestamp": datetime.utcnow().isoformat()
        })
        with open(LOG_PATH, "w") as f:
            json.dump(log, f, indent=2)

    wall_time = time.time() - start_time

    print(f"\n--- DONE ---")
    print(f"Total cost: ${total_cost:.3f}")
    print(f"Wall time: {wall_time:.0f}s ({wall_time/60:.1f} min)")
    print(f"Anchor seed: {anchor_seed}")

    # Build contact sheet
    print("\nBuilding contact sheet...")
    contact_path = OUT_DIR / "concepts_grid.png"
    build_contact_sheet(OUT_DIR, log, contact_path)

    # Final summary
    successes = [e for e in log if not e.get("failed") and not e.get("skipped")]
    failures = [e for e in log if e.get("failed")]
    print(f"\nSuccesses: {len(successes)}")
    print(f"Failures: {len(failures)}")
    print(f"Log: {LOG_PATH}")


if __name__ == "__main__":
    main()
