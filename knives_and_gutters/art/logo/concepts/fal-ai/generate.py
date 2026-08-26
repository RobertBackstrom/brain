#!/usr/bin/env python3
"""
One-shot generator for the K&G logo dry-run (Lanes A + B via fal.ai).

Lane A = Flux.dev (illustrative, primary)
Lane B = fast-SDXL (cross-check, second pass) — same vendor, same key, different model

Reads FAL_KEY from /home/assistant/projects/assistant/.env.
Writes images to ./fal-flux/ and ../stability-ai/ (Lane B is hosted on fal but lives in
the stability-ai/ folder per pipeline naming, since it represents the SDXL cross-check).

Replace once the fal-ai MCP server is wired (db-NNN).
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


def load_env():
    if not ENV_FILE.exists():
        sys.exit(f".env not found at {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        if line.startswith("FAL_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("FAL_KEY not found in .env")


FAL_KEY = load_env()


def fal_call(model: str, payload: dict, timeout: int = 180) -> dict:
    """POST to fal.run sync endpoint. Returns parsed JSON or raises."""
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


PROMPTS = {
    "angle1_composition": {
        "flux": (
            'A weathered tabletop game cover badge logo for a grimdark fantasy game titled "Knives & Gutters". '
            "Rectangular outer frame in chipped, ink-stained parchment. The two words split by a single curved blade "
            "running vertically through the center as a separator. Hand-painted illustrative weapons — knives, jagged "
            "spikes, hooks — flanking the type, drawn in thick real-ink outlines with painted gouache highlights in "
            "the style of Gary Chalk's Mordheim covers. Muted dirt-and-blood palette: bone-white, oxide red, charcoal. "
            "Type is hand-lettered, slightly off-register, with 80s tabletop-cover metallic highlight technique. "
            "Composition centered, isolated on flat dark background. Crude, weighty, hand-crafted, not digital-clean."
        ),
        "sdxl": (
            "(badge logo:1.3), (rectangular frame:1.2), grimdark fantasy game cover, hand-painted, "
            '"Knives & Gutters" wordmark, single blade vertical separator between two words, '
            "flanking knives and hooks, Gary Chalk style, Mordheim cover, real ink outlines, painted gouache "
            "highlights, 80s tabletop cover technique, hand-lettered type, off-register coin-stamp metallic "
            "highlight, muted bone-white oxide-red charcoal palette, weighty crude hand-crafted, centered "
            "isolated on dark flat background, 1:1 square, illustrative, painterly"
        ),
    },
    "angle2_detail": {
        "flux": (
            'An ornate hand-painted wordmark logo reading "Knives & Gutters" for a grimdark gang skirmish RPG. '
            "Every letter is individually designed and hand-rendered with painterly detail — no two characters alike "
            "— in the style of John Blanche's Warhammer illustrations: baroque, grotesque, surreal flourishes growing "
            "out of the letterforms. Tiny figures, mutant gangers, blades, hooks, and ruined-city silhouettes "
            "embedded into the type itself. Real-ink outlines, painted highlights, oil-and-gouache texture. "
            "Rectangular outer frame in tarnished metal. Muted grimdark palette with blood-rust accents. "
            "Coin-stamp embossed feel on the type. Detail density rewards extended looking. Centered composition, "
            "1:1 square, isolated on flat background."
        ),
        "sdxl": (
            '(ornate wordmark logo:1.4), "Knives & Gutters", (every letter individually hand-painted:1.3), '
            "John Blanche style, Warhammer illustration, baroque grotesque surreal flourishes, tiny mutant "
            "figures and weapons embedded in the letterforms, ruined-city silhouettes inside the type, "
            "(real ink outlines:1.2), painted highlights, oil and gouache texture, tarnished metal "
            "rectangular frame, grimdark palette, blood-rust accents, (coin-stamp embossed type:1.2), "
            "detail density, rewards close inspection, 1:1 square, centered, isolated flat dark background"
        ),
    },
    "angle3_crudeness": {
        "flux": (
            'A crude hand-painted badge logo for a grimdark fantasy gang skirmish game titled "Knives & Gutters", '
            "in the unmistakable style of Gary Chalk's Mordheim and Warhammer Fantasy Roleplay covers from the late "
            "1980s. Thick brush ink outlines bleeding slightly off-register. Painted gouache highlights with visible "
            "brush texture. Hand-lettered type with the 80s metallic-highlight technique — bone-white catch-light on "
            'chipped iron lettering. Single blade running vertically between "Knives" and "Gutters" as a separator. '
            "Rough rectangular ink-bordered frame. Two crude weapons — a notched knife and a hooked spike — flanking "
            "the type. Limited dirty palette: parchment, oxide red, charcoal black, bone. Govern by what was "
            "achievable with 1980s analog tabletop-cover tooling — no clean vector lines, no chrome 3D, no modern "
            "digital effects. Centered, isolated on flat dark background."
        ),
        "sdxl": (
            '(crude hand-painted badge logo:1.3), "Knives & Gutters", Gary Chalk Mordheim cover style, '
            "Warhammer Fantasy Roleplay 1989, (thick brush ink outlines:1.2), bleeding off-register, painted "
            "gouache, visible brush texture, hand-lettered type, (80s metallic highlight technique:1.2), "
            "bone-white catch-light on chipped iron, single blade vertical separator, rough rectangular ink "
            "frame, notched knife and hooked spike flanking, limited dirty palette parchment oxide-red "
            "charcoal bone, (analog tabletop cover tooling:1.2), no vector lines, no chrome, no digital "
            "effects, centered, isolated dark background, 1:1"
        ),
    },
}

NEGATIVE_SDXL = (
    "clean vector, chrome 3D, glossy plastic, AI typography, mechanical sans-serif, Y2K, glitch, dragon, "
    "skull, photoreal, modern digital effects, smooth gradient, neon, cyberpunk, pristine, polished, corporate"
)

SEEDS = [101, 202, 303, 404]  # 4 seeds per prompt, deterministic


def run_lane(lane_name: str, model: str, out_dir: Path, prompt_key: str):
    """Run 3 angles × 4 seeds for a lane. Save PNGs to out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    log = []
    for angle, prompts in PROMPTS.items():
        prompt = prompts[prompt_key]
        for seed in SEEDS:
            slug = f"{angle}_seed{seed}"
            dest = out_dir / f"{slug}.png"
            if dest.exists():
                print(f"[{lane_name}] skip (exists): {slug}")
                log.append({"slug": slug, "status": "skipped"})
                continue
            payload = {
                "prompt": prompt,
                "image_size": "square_hd",
                "num_inference_steps": 28 if "flux" in model else 30,
                "seed": seed,
                "num_images": 1,
                "enable_safety_checker": False,
            }
            if prompt_key == "sdxl":
                payload["negative_prompt"] = NEGATIVE_SDXL
            t0 = time.time()
            print(f"[{lane_name}] generate: {slug} ...", flush=True)
            try:
                resp = fal_call(model, payload)
                img_url = resp["images"][0]["url"]
                download(img_url, dest)
                elapsed = time.time() - t0
                print(f"  -> ok ({elapsed:.1f}s) {dest.name}")
                log.append({"slug": slug, "status": "ok", "elapsed": elapsed, "url": img_url})
            except Exception as e:
                print(f"  -> FAIL: {e}")
                log.append({"slug": slug, "status": "fail", "error": str(e)})
    return log


def main():
    lane_a_dir = LOGO_DIR / "concepts" / "fal-flux"
    lane_b_dir = LOGO_DIR / "concepts" / "fal-sdxl"

    print("=== Lane A: Flux.dev ===")
    log_a = run_lane("flux", "fal-ai/flux/dev", lane_a_dir, "flux")

    print("\n=== Lane B: fast-SDXL ===")
    log_b = run_lane("sdxl", "fal-ai/fast-sdxl", lane_b_dir, "sdxl")

    summary = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "lane_a_flux": log_a,
        "lane_b_sdxl": log_b,
    }
    (LOGO_DIR / "concepts" / "_run_log.json").write_text(json.dumps(summary, indent=2))
    print(f"\nLogs: {LOGO_DIR}/concepts/_run_log.json")


if __name__ == "__main__":
    main()
