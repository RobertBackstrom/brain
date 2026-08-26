"""Vision pass: qualitative condition assessment from card photos.

Centering is measured in centering.py and passed in here as a fact. The model
is told not to re-estimate it. Its job is corners, edges, surface, print
defects, and an honest statement of what the photos cannot show.
"""

import base64
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

import cv2

# Current Opus sits in the high-resolution vision tier: 2576px on the long edge.
MAX_LONG_EDGE = 2576

CONFIG = Path(__file__).resolve().parent.parent.parent / "assistant" / "config.json"


def resolve_model():
    """Model id from the project's single source of truth, never hardcoded.

    config.json agent_governance.model_tiers is what server.js and agent-router.js
    read, so the pre-grade tracks the same tier. PREGRADE_MODEL overrides for a
    one-off run.
    """
    override = os.environ.get("PREGRADE_MODEL")
    if override:
        return override
    try:
        tiers = json.loads(CONFIG.read_text(encoding="utf-8"))
        return tiers["agent_governance"]["model_tiers"]["opus"]
    except Exception:
        return "claude-opus-5"

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "card",
        "corners",
        "edges",
        "surface",
        "print_defects",
        "authenticity_flags",
        "photo_quality",
        "estimated_grade_low",
        "estimated_grade_high",
        "limiting_factor",
        "notes",
    ],
    "properties": {
        "card": {
            "type": "object",
            "additionalProperties": False,
            "required": ["name", "set_or_series", "number", "finish", "confident"],
            "properties": {
                "name": {"type": "string"},
                "set_or_series": {"type": "string"},
                "number": {"type": "string"},
                "finish": {
                    "type": "string",
                    "enum": ["non-holo", "holo", "reverse-holo", "full-art", "textured", "unknown"],
                },
                "confident": {"type": "boolean"},
            },
        },
        "corners": {
            "type": "object",
            "additionalProperties": False,
            "required": ["assessable", "worst_corner", "observations", "grade_ceiling"],
            "properties": {
                "assessable": {"type": "boolean"},
                "worst_corner": {
                    "type": "string",
                    "enum": ["top-left", "top-right", "bottom-left", "bottom-right", "none", "unknown"],
                },
                "observations": {"type": "string"},
                "grade_ceiling": {"type": "integer"},
            },
        },
        "edges": {
            "type": "object",
            "additionalProperties": False,
            "required": ["assessable", "whitening_sides", "observations", "grade_ceiling"],
            "properties": {
                "assessable": {"type": "boolean"},
                "whitening_sides": {
                    "type": "array",
                    "items": {"type": "string", "enum": ["top", "bottom", "left", "right"]},
                },
                "observations": {"type": "string"},
                "grade_ceiling": {"type": "integer"},
            },
        },
        "surface": {
            "type": "object",
            "additionalProperties": False,
            "required": ["assessable", "defects", "observations", "grade_ceiling"],
            "properties": {
                "assessable": {"type": "boolean"},
                "defects": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "scratches",
                            "print-lines",
                            "roller-lines",
                            "indentation",
                            "scuffing",
                            "loss-of-gloss",
                            "stain",
                            "crease",
                            "none-visible",
                        ],
                    },
                },
                "observations": {"type": "string"},
                "grade_ceiling": {"type": "integer"},
            },
        },
        "print_defects": {"type": "array", "items": {"type": "string"}},
        "authenticity_flags": {"type": "array", "items": {"type": "string"}},
        "photo_quality": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "front_straight_on",
                "sharp",
                "raking_light_present",
                "corner_macros_present",
                "back_present",
                "issues",
            ],
            "properties": {
                "front_straight_on": {"type": "boolean"},
                "sharp": {"type": "boolean"},
                "raking_light_present": {"type": "boolean"},
                "corner_macros_present": {"type": "boolean"},
                "back_present": {"type": "boolean"},
                "issues": {"type": "array", "items": {"type": "string"}},
            },
        },
        "estimated_grade_low": {"type": "integer"},
        "estimated_grade_high": {"type": "integer"},
        "limiting_factor": {"type": "string"},
        "notes": {"type": "string"},
    },
}

SYSTEM = """You pre-screen trading cards for PSA submission. You are the filter that
decides which cards are worth the grading fee, so a false optimistic call costs real money.

Rules:
1. Never estimate centering. It has been measured optically and is given to you as fact.
   Treat it as a hard ceiling you cannot argue above.
2. Grade only what the supplied photos can actually show. Under flat diffuse light,
   holo scratches and print lines are close to invisible, so without a raking-light
   shot you must set surface.assessable = false and cap surface.grade_ceiling at 9.
   Without close corner shots, set corners.assessable = false and cap corners at 9.
3. Be conservative. When a defect is ambiguous, assume it is real. It is cheaper to
   skip a good card than to pay for a slab that comes back an 8.
4. estimated_grade_high must be the minimum of your per-criterion ceilings.
   estimated_grade_low is the realistic downside if the invisible criteria are bad.
5. limiting_factor is one short clause naming the single thing that caps the grade.
6. Flag anything that looks off about authenticity: wrong font, wrong colour saturation,
   wrong border thickness, fuzzy print, wrong back rosette pattern.

PSA reference points: 10 needs sharp corners and a clean surface; 9 tolerates one very
minor flaw; 8 tolerates slight fraying at one or two corners and a minor print blemish;
7 shows slight surface wear on close inspection; 6 shows visible wear or slightly
rounded corners; 5 shows rounded corners and loss of gloss."""


def _encode(path):
    """Downscale to the model's high-resolution ceiling and return base64 JPEG."""
    img = cv2.imread(str(path))
    if img is None:
        raise ValueError(f"could not read image: {path}")
    h, w = img.shape[:2]
    scale = MAX_LONG_EDGE / float(max(h, w))
    if scale < 1.0:
        img = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)
    ok, buf = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 92])
    if not ok:
        raise ValueError(f"could not encode image: {path}")
    return base64.standard_b64encode(buf.tobytes()).decode("utf-8")


def _image_block(path):
    return {
        "type": "image",
        "source": {"type": "base64", "media_type": "image/jpeg", "data": _encode(path)},
    }


def _centering_brief(centering_front, centering_back):
    def fmt(m, side):
        if not m or not m.get("ok"):
            reason = m.get("reason") if m else "not supplied"
            return f"{side}: NOT MEASURABLE ({reason})"
        h, v = m["horizontal"], m["vertical"]
        return (
            f"{side}: {h['left_pct']:.1f}/{h['right_pct']:.1f} left/right, "
            f"{v['top_pct']:.1f}/{v['bottom_pct']:.1f} top/bottom, "
            f"measurement confidence {m['confidence']}"
        )

    return (
        "Measured centering (optical, do not re-estimate):\n"
        f"  {fmt(centering_front, 'FRONT')}\n"
        f"  {fmt(centering_back, 'BACK')}\n\n"
        "Assess corners, edges, surface, print defects and authenticity from the "
        "photos, state honestly what these photos cannot show, and return the grade band."
    )


def _assess_via_cli(shots, brief, model, timeout=600):
    """Vision pass through the Claude Code CLI.

    This is the VPS-native path: it runs on Robert's Max subscription the same
    way server.js drives its agents, so no console API key is needed. See the
    DevOps note from db-036 (2026-04-16).
    """
    listing = "\n".join(f"  - {label}: {Path(p).resolve()}" for label, p in shots.items())
    schema_text = json.dumps(SCHEMA, indent=2)
    prompt = (
        f"{SYSTEM}\n\n"
        "Read every image file listed below with the Read tool, then assess the card.\n\n"
        f"Photos:\n{listing}\n\n"
        f"{brief}\n\n"
        "Return ONLY a single JSON object conforming exactly to this JSON Schema. "
        "No prose, no markdown fences, no commentary before or after.\n\n"
        f"{schema_text}"
    )

    cmd = [
        os.environ.get("CLAUDE_CLI", "claude"),
        "--dangerously-skip-permissions",
        "--output-format",
        "json",
        "--model",
        model,
        "-p",
        prompt,
    ]
    env = dict(os.environ)
    # Avoid inheriting the parent session's identity into the child run.
    env.pop("CLAUDE_CODE_SESSION_ID", None)

    proc = subprocess.run(
        cmd, capture_output=True, text=True, timeout=timeout, env=env, cwd=tempfile.gettempdir()
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude CLI failed ({proc.returncode}): {proc.stderr[-800:]}")

    envelope = json.loads(proc.stdout)
    text = envelope.get("result", "")
    return _parse_json_object(text)


def _parse_json_object(text):
    """Pull a JSON object out of a model response, fences and preamble tolerated."""
    text = text.strip()
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    if fenced:
        text = fenced.group(1)
    else:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end > start:
            text = text[start : end + 1]
    return json.loads(text)


def _assess_via_api(shots, brief, model, client=None):
    """Vision pass through the Anthropic SDK, when a console API key is set."""
    import anthropic

    client = client or anthropic.Anthropic()

    content = []
    for label, path in shots.items():
        content.append({"type": "text", "text": f"Photo: {label}"})
        content.append(_image_block(path))
    content.append({"type": "text", "text": brief})

    response = client.messages.create(
        model=model,
        max_tokens=16000,
        system=SYSTEM,
        messages=[{"role": "user", "content": content}],
        output_config={"format": {"type": "json_schema", "schema": SCHEMA}},
    )

    if response.stop_reason == "refusal":
        raise RuntimeError(f"vision pass refused: {response.stop_details}")

    text = next(b.text for b in response.content if b.type == "text")
    result = json.loads(text)
    result["_usage"] = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }
    return result


def assess(shots, centering_front, centering_back, client=None, backend=None):
    """Run the vision pass. `shots` maps a label to an image path.

    Backend defaults to the CLI (Max subscription, no key needed) and switches
    to the SDK only when a console API key is present.
    """
    model = resolve_model()
    brief = _centering_brief(centering_front, centering_back)
    backend = backend or os.environ.get("PREGRADE_BACKEND")
    if not backend:
        backend = "api" if os.environ.get("ANTHROPIC_API_KEY") else "cli"

    if backend == "api":
        result = _assess_via_api(shots, brief, model, client=client)
    else:
        result = _assess_via_cli(shots, brief, model)
    result["_model"] = model
    result["_backend"] = backend
    return result
