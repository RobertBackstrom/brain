#!/usr/bin/env python3
"""
K&G logo — SD 3.5 Large probe (2026-05-09).

Single merged prompt, 4 seeds, 1536x1024. Driven by Robert's heavy-metal/90s prompt
folded back into the locked 80s tabletop direction. Anchors restricted to:
  - approved/roc_logo02.png (density / Blanche)
  - approved/kg_metallic_mockup.png (composition / blade-as-separator)
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOGO_DIR = ROOT.parent.parent  # .../art/logo/
ENV_FILE = Path("/home/assistant/projects/assistant/.env")
MODEL = "fal-ai/stable-diffusion-v35-large"


def load_env():
    if not ENV_FILE.exists():
        sys.exit(f".env not found at {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        if line.startswith("FAL_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("FAL_KEY not found in .env")


FAL_KEY = load_env()


def fal_call(model: str, payload: dict, timeout: int = 240) -> dict:
    url = f"https://fal.run/{model}"
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Key {FAL_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"fal.ai {model} HTTP {e.code}: {body}") from e


def download(url: str, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as resp:
        dest.write_bytes(resp.read())


PROMPT = (
    'A highly detailed wordmark logo for a 1980s tabletop fantasy game titled "Knives & Gutters". '
    "Composition and typography drawn from late-80s tabletop game cover art — Mordheim, Warhammer "
    "Fantasy Roleplay, early Games Workshop and 1980s AD&D module covers — with the ornamental "
    "chaotic energy of John Blanche illustration and the crude weighty hand of Gary Chalk. Jagged "
    "gothic serif lettering, hand-painted not vector, slightly off-register with visible brush "
    "texture and the 80s metallic-highlight technique (bone-white catch-light on chipped iron "
    "lettering). Organic asymmetry, thorny embellishments, cracked stone and aged-metal letterforms. "
    "The composition centers a large decorative ampersand between the two words — itself a baroque "
    "ornamental piece, woven from blade silhouettes, vines, and a single skull fragment. Around and "
    "inside the lettering: vines, jagged spikes, hooks, weathered carvings, tiny figures and "
    "ruined-city silhouettes embedded in the type, in the surreal Blanche style. Color palette muted "
    "and grimy: parchment, oxide red, deep crimson, charcoal black, bone-white highlights, oxidized "
    "bronze and weathered gold accents. Layered depth, dramatic painted shading, distressed ink "
    "outlines, worn paint texture — feels like it was achievable with 1980s analog tabletop-cover "
    "tooling, no clean vectors, no chrome 3D, no modern digital effects. Centered composition, "
    "transparent background, extremely high detail, professional hand-painted logo rendering."
)

NEGATIVE_PROMPT = (
    "modern logo, minimalist, flat design, corporate branding, sans-serif, clean typography, sci-fi, "
    "cyberpunk, cartoon, anime, neon, glossy plastic, low detail, blurry, simple shapes, generic "
    "fantasy font, photorealism, watermark, background scenery, 90s aesthetic, DOS-era pixelation, "
    "sickly green, chrome 3D, vector lines, AI-generic typography, mechanical sans-serif, Y2K "
    "aesthetic, glitch effects"
)

SEEDS = [1337, 4242, 9001, 7777]


def main():
    out_dir = LOGO_DIR / "concepts" / "sd35-large"
    out_dir.mkdir(parents=True, exist_ok=True)
    log = []
    for seed in SEEDS:
        slug = f"merged_seed{seed}"
        dest = out_dir / f"{slug}.png"
        if dest.exists():
            print(f"skip (exists): {slug}")
            log.append({"slug": slug, "status": "skipped"})
            continue
        payload = {
            "prompt": PROMPT,
            "negative_prompt": NEGATIVE_PROMPT,
            "image_size": {"width": 1536, "height": 1024},
            "num_inference_steps": 40,
            "guidance_scale": 8,
            "seed": seed,
            "num_images": 1,
            "enable_safety_checker": False,
        }
        t0 = time.time()
        print(f"generate: {slug} ...", flush=True)
        try:
            resp = fal_call(MODEL, payload)
            img_url = resp["images"][0]["url"]
            download(img_url, dest)
            elapsed = time.time() - t0
            print(f"  -> ok ({elapsed:.1f}s) {dest.name}")
            log.append({"slug": slug, "status": "ok", "elapsed": elapsed, "url": img_url, "seed": seed})
        except Exception as e:
            print(f"  -> FAIL: {e}")
            log.append({"slug": slug, "status": "fail", "error": str(e), "seed": seed})

    summary = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "model": MODEL,
        "image_size": {"width": 1536, "height": 1024},
        "num_inference_steps": 40,
        "guidance_scale": 8,
        "seeds": SEEDS,
        "results": log,
    }
    (out_dir / "_run_log.json").write_text(json.dumps(summary, indent=2))
    print(f"\nLog: {out_dir}/_run_log.json")


if __name__ == "__main__":
    main()
