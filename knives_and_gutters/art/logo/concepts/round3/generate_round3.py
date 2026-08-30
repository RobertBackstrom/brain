#!/usr/bin/env python3
"""
K&G logo — Round 3 (2026-08-30, 4am sweep, unattended).

Executes the three branches Robert left open on 2026-05-11 so he can curate in one pass:
  A. gnarl/   — seed-7777 direction pushed gnarlier (4 seeds, SD3.5-large)
  B. clean/   — seed-9001 direction pushed cleaner-readable (4 seeds, SD3.5-large)
  C. fluxpro/ — same merged prompt on Flux Pro v1.1 for comparison (4 seeds)

Base prompt = the validated 2026-05-09 merged prompt (80s tabletop + heavy-metal fold-in).
"""

import json
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENV_FILE = Path("/home/assistant/projects/assistant/.env")

SD35 = "fal-ai/stable-diffusion-v35-large"
FLUXPRO = "fal-ai/flux-pro/v1.1"


def load_env():
    for line in ENV_FILE.read_text().splitlines():
        if line.startswith("FAL_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("FAL_KEY not found in .env")


FAL_KEY = load_env()


def fal_call(model, payload, timeout=300):
    req = urllib.request.Request(
        f"https://fal.run/{model}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Key {FAL_KEY}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"fal.ai {model} HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}") from e


def download(url, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as resp:
        dest.write_bytes(resp.read())


BASE = (
    'A highly detailed wordmark logo for a 1980s tabletop fantasy game titled "Knives & Gutters". '
    "Composition and typography drawn from late-80s tabletop game cover art — Mordheim, Warhammer "
    "Fantasy Roleplay, early Games Workshop and 1980s AD&D module covers — with the ornamental "
    "chaotic energy of John Blanche illustration and the crude weighty hand of Gary Chalk. Jagged "
    "gothic serif lettering, hand-painted not vector, slightly off-register with visible brush "
    "texture and the 80s metallic-highlight technique (bone-white catch-light on chipped iron "
    "lettering). Organic asymmetry, thorny embellishments, cracked stone and aged-metal letterforms. "
    "The composition centers a large decorative ampersand between the two words — itself a baroque "
    "ornamental piece, woven from blade silhouettes, vines, and a single skull fragment. "
)

TAIL = (
    "Color palette muted and grimy: parchment, oxide red, deep crimson, charcoal black, bone-white "
    "highlights, oxidized bronze and weathered gold accents. Layered depth, dramatic painted shading, "
    "distressed ink outlines, worn paint texture — feels like it was achievable with 1980s analog "
    "tabletop-cover tooling, no clean vectors, no chrome 3D, no modern digital effects. Centered "
    "composition, transparent background, extremely high detail, professional hand-painted logo rendering."
)

GNARL_MID = (
    "Around and inside the lettering: dense thorny overgrowth, jagged spikes, hooks, weathered "
    "carvings, tiny grotesque figures and ruined-city silhouettes embedded deep in the type, in the "
    "surreal Blanche style pushed to maximum chaotic density — ornament nearly consuming the "
    "letterforms, deeply gnarled bark-like texture on every stroke, yet the two words still readable. "
)

CLEAN_MID = (
    "Ornament restrained and purposeful: decoration lives in the ampersand and around the outer "
    "edges, the letterforms themselves kept as strong clean silhouettes with high figure-ground "
    "contrast so the wordmark reads instantly even at small size, a few vines and spikes touching "
    "the type but never obscuring it. "
)

NEG = (
    "modern logo, minimalist, flat design, corporate branding, sans-serif, clean typography, sci-fi, "
    "cyberpunk, cartoon, anime, neon, glossy plastic, low detail, blurry, simple shapes, generic "
    "fantasy font, photorealism, watermark, background scenery, 90s aesthetic, DOS-era pixelation, "
    "sickly green, chrome 3D, vector lines, AI-generic typography, mechanical sans-serif, Y2K "
    "aesthetic, glitch effects"
)

BRANCHES = [
    {"dir": "gnarl", "model": SD35, "prompt": BASE + GNARL_MID + TAIL, "seeds": [7777, 7781, 7793, 7807]},
    {"dir": "clean", "model": SD35, "prompt": BASE + CLEAN_MID + TAIL, "seeds": [9001, 9013, 9027, 9041]},
    {"dir": "fluxpro", "model": FLUXPRO, "prompt": BASE + GNARL_MID.replace("pushed to maximum chaotic density — ornament nearly consuming the letterforms, deeply gnarled bark-like texture on every stroke, yet the two words still readable. ", "") + TAIL, "seeds": [7777, 9001, 4242, 5150]},
]


def main():
    log = []
    for br in BRANCHES:
        out = ROOT / br["dir"]
        for seed in br["seeds"]:
            dest = out / f"seed{seed}.png"
            if dest.exists():
                log.append({"branch": br["dir"], "seed": seed, "status": "skipped"})
                continue
            if br["model"] == SD35:
                payload = {
                    "prompt": br["prompt"], "negative_prompt": NEG,
                    "image_size": {"width": 1536, "height": 1024},
                    "num_inference_steps": 40, "guidance_scale": 8,
                    "seed": seed, "num_images": 1, "enable_safety_checker": False,
                }
            else:
                payload = {
                    "prompt": br["prompt"],
                    "image_size": {"width": 1536, "height": 1024},
                    "seed": seed, "num_images": 1, "enable_safety_checker": False,
                }
            t0 = time.time()
            print(f"generate: {br['dir']}/seed{seed} ...", flush=True)
            try:
                resp = fal_call(br["model"], payload)
                download(resp["images"][0]["url"], dest)
                print(f"  -> ok ({time.time()-t0:.1f}s)")
                log.append({"branch": br["dir"], "seed": seed, "status": "ok", "elapsed": round(time.time() - t0, 1)})
            except Exception as e:
                print(f"  -> FAIL: {e}")
                log.append({"branch": br["dir"], "seed": seed, "status": "fail", "error": str(e)})

    (ROOT / "_run_log.json").write_text(json.dumps({
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "branches": [{k: b[k] for k in ("dir", "model", "seeds")} for b in BRANCHES],
        "results": log,
    }, indent=2))
    fails = [r for r in log if r["status"] == "fail"]
    print(f"\ndone: {len(log)-len(fails)} ok, {len(fails)} failed")


if __name__ == "__main__":
    main()
