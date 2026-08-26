"""HTTP API in front of the pre-grade engine.

    python3 api/server.py            # listens on 127.0.0.1:3786

Exposed publicly as grade.runatyr.games through the Cloudflare tunnel. The tunnel
terminates TLS, so this speaks plain HTTP on loopback only and never binds a
public interface.

Stdlib on purpose. This is five endpoints serving one user; FastAPI + uvicorn
would add two dependencies to keep patched for no behaviour we need.

Auth: bearer token, constant-time compare, fails closed when the token is unset
(feedback_security_defaults rule 2). Requests arriving on loopback WITHOUT the
Cloudflare forwarding header are allowed through unauthenticated, mirroring
server.js checkCfAccess — that is how the CLI batch runner keeps working.
"""

import hmac
import json
import os
import re
import sys
import threading
import traceback
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pregrade import psa, run as engine  # noqa: E402

INTAKE = ROOT / "intake"
REPORTS = ROOT / "reports"

HOST = os.environ.get("PREGRADE_HOST", "127.0.0.1")
PORT = int(os.environ.get("PREGRADE_PORT", "3786"))
TOKEN = os.environ.get("PREGRADE_API_TOKEN", "")

# Centering-only mode: skips the Claude vision pass. Free, ~1s instead of ~60s,
# and the report then honestly reports every qualitative criterion as
# unassessable rather than silently guessing.
NO_VISION = os.environ.get("PREGRADE_NO_VISION") == "1"

MAX_UPLOAD = 40 * 1024 * 1024  # a full-res iPhone HEIC/JPEG is 3-8 MB; 40 is slack
MAX_JSON = 64 * 1024

# batch and card ids land straight in filesystem paths. Allowlist, not blocklist:
# anything outside this set is rejected rather than sanitised, so there is no
# normalisation step to get subtly wrong.
SAFE_SEGMENT = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{0,79}$")

# card key -> {"state": "running"|"done"|"error", "result"|"error", "started"}
_jobs = {}
_jobs_lock = threading.Lock()


def safe_segment(value):
    if not value or not SAFE_SEGMENT.match(value) or ".." in value:
        raise ValueError(f"ogiltigt id: {value!r}")
    return value


def card_dir(batch, card):
    return INTAKE / safe_segment(batch) / safe_segment(card)


def job_key(batch, card):
    return f"{batch}/{card}"


# --------------------------------------------------------------------------
# Engine result -> the shape the app renders.
#
# The app stays dumb on purpose: every label, rounding and fallback decision is
# made here, so a change in the engine's internal dict never requires a new
# TestFlight build to render correctly.
# --------------------------------------------------------------------------

CRITERIA_LABELS = [("corners", "Hörn"), ("edges", "Kanter"), ("surface", "Yta")]


def centering_line(measurement):
    """One display string for a centering measurement, or None.

    Delegates to psa.worse_axis so the app shows the SAME axis the grade cap was
    derived from. Reading `horizontal` directly would show the left/right ratio
    even when it was the vertical axis that limited the grade — the exact bug the
    self-test caught in the CLI report.
    """
    if not measurement or not measurement.get("ok"):
        return None
    _axis, _worse, ratio = psa.worse_axis(measurement)
    return ratio


def to_api(card_id, batch, res):
    band = res.get("band") or {}
    vis = res.get("vision") or {}
    cf = res.get("centering_front") or {}
    cb = res.get("centering_back") or {}
    ev = res.get("ev") or {}

    criteria = []
    for key, label in CRITERIA_LABELS:
        block = vis.get(key) or {}
        if not block:
            continue
        criteria.append({
            "name": label,
            "assessable": block.get("assessable", False),
            "grade_ceiling": block.get("grade_ceiling"),
            "observations": block.get("observations") or "",
        })

    out = {
        "status": "done",
        "batch": batch,
        "card": card_id,
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "band": {
            "low": band.get("grade_low"),
            "high": band.get("grade_high"),
            "limiting": band.get("limiting_factor"),
        },
        "call": res.get("call"),
        "reason": res.get("reason") or "",
        "centering": {
            "front": centering_line(cf),
            "back": centering_line(cb),
            "cap": band.get("centering_cap"),
            "confidence": cf.get("confidence"),
        },
        "criteria": criteria,
        "warnings": res.get("warnings") or [],
        "notes": vis.get("notes") or "",
    }

    if ev.get("computable"):
        out["ev"] = {
            "computable": True,
            "graded_net_sek": round(ev.get("graded_net_sek") or 0),
            "raw_net_sek": round(ev.get("raw_net_sek") or 0),
            "delta_sek": round(ev.get("delta_sek") or 0),
            "verdict": ev.get("verdict"),
        }
    else:
        # Never invent a price. If comps are missing the app shows nothing here
        # rather than a zero that reads like a real number.
        out["ev"] = {"computable": False, "reason": ev.get("reason") or "comps saknas"}

    return out


def run_analysis(batch, card):
    key = job_key(batch, card)
    try:
        res = engine.process_card(card_dir(batch, card), use_vision=not NO_VISION)
        payload = to_api(card, batch, res)
        out_dir = REPORTS / batch
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / f"{card}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        with _jobs_lock:
            _jobs[key] = {"state": "done", "result": payload}
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        with _jobs_lock:
            _jobs[key] = {"state": "error", "error": str(exc)}


class Handler(BaseHTTPRequestHandler):
    server_version = "pregrade/1.0"
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {fmt % args}\n")

    # -- plumbing ----------------------------------------------------------

    def send_json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def fail(self, code, msg):
        self.send_json(code, {"error": msg})

    def authorised(self):
        # Did this request traverse the Cloudflare tunnel?
        via_cf = bool(self.headers.get("cf-connecting-ip"))
        peer = self.client_address[0] if self.client_address else ""
        local = peer in ("127.0.0.1", "::1", "::ffff:127.0.0.1")
        if not via_cf and local:
            return True

        if not TOKEN:
            sys.stderr.write("[auth] PREGRADE_API_TOKEN unset — refusing remote request\n")
            return False

        header = self.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return False
        return hmac.compare_digest(header[7:], TOKEN)

    def read_body(self, limit):
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return None
        if length <= 0 or length > limit:
            return None
        return self.rfile.read(length)

    # -- routes ------------------------------------------------------------

    def do_HEAD(self):
        """Health checks and uptime monitors probe with HEAD.

        BaseHTTPRequestHandler answers 501 for any verb it has no do_* for, so
        without this every standard monitor would report the service down while
        it was serving GET traffic perfectly well.
        """
        path = self.path.split("?", 1)[0].rstrip("/")
        if path == "/api/health":
            code = 200
        elif not self.authorised():
            code = 401
        else:
            code = 200 if path.startswith("/api/") else 404
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", "0")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?", 1)[0].rstrip("/")

        if path == "/api/health":
            return self.send_json(200, {
                "ok": True,
                "service": "pregrade",
                "auth": "token" if TOKEN else "loopback-only",
            })

        if not self.authorised():
            return self.fail(401, "unauthorised")

        m = re.fullmatch(r"/api/cards/([^/]+)/([^/]+)/report", path)
        if m:
            batch, card = m.group(1), m.group(2)
            try:
                safe_segment(batch), safe_segment(card)
            except ValueError as exc:
                return self.fail(400, str(exc))

            with _jobs_lock:
                job = _jobs.get(job_key(batch, card))
            if job and job["state"] == "running":
                return self.send_json(200, {"status": "running"})
            if job and job["state"] == "error":
                return self.send_json(200, {"status": "error", "error": job["error"]})
            if job and job["state"] == "done":
                return self.send_json(200, job["result"])

            # No live job — fall back to a report written by an earlier run,
            # including one produced by the CLI batch runner.
            cached = REPORTS / batch / f"{card}.json"
            if cached.exists():
                return self.send_json(200, json.loads(cached.read_text(encoding="utf-8")))
            return self.fail(404, "ingen rapport för det kortet")

        return self.fail(404, "no such route")

    def do_POST(self):
        path = self.path.split("?", 1)[0].rstrip("/")

        if not self.authorised():
            return self.fail(401, "unauthorised")

        if path == "/api/cards":
            raw = self.read_body(MAX_JSON)
            if raw is None:
                return self.fail(413, "body saknas eller för stor")
            try:
                data = json.loads(raw)
                batch = safe_segment(data["batch"])
                card = safe_segment(data["card_id"])
            except (json.JSONDecodeError, KeyError, ValueError) as exc:
                return self.fail(400, str(exc))

            d = card_dir(batch, card)
            d.mkdir(parents=True, exist_ok=True)
            if data.get("note"):
                (d / "note.txt").write_text(str(data["note"])[:2000], encoding="utf-8")
            return self.send_json(201, {"batch": batch, "card": card, "path": str(d)})

        m = re.fullmatch(r"/api/cards/([^/]+)/([^/]+)/shots/([^/]+)", path)
        if m:
            try:
                batch = safe_segment(m.group(1))
                card = safe_segment(m.group(2))
                shot = safe_segment(m.group(3))
            except ValueError as exc:
                return self.fail(400, str(exc))

            raw = self.read_body(MAX_UPLOAD)
            if raw is None:
                return self.fail(413, f"bild saknas eller över {MAX_UPLOAD // 1024 // 1024} MB")

            d = card_dir(batch, card)
            d.mkdir(parents=True, exist_ok=True)
            # The engine maps role by filename prefix (run.classify_shots), so the
            # shot id from the app IS the contract. Keep the extension .jpg.
            (d / f"{shot}.jpg").write_bytes(raw)
            return self.send_json(201, {"shot": shot, "bytes": len(raw)})

        m = re.fullmatch(r"/api/cards/([^/]+)/([^/]+)/analyze", path)
        if m:
            try:
                batch = safe_segment(m.group(1))
                card = safe_segment(m.group(2))
            except ValueError as exc:
                return self.fail(400, str(exc))

            if not card_dir(batch, card).is_dir():
                return self.fail(404, "inga bilder uppladdade för det kortet")

            key = job_key(batch, card)
            with _jobs_lock:
                existing = _jobs.get(key)
                if existing and existing["state"] == "running":
                    return self.send_json(202, {"status": "running"})
                _jobs[key] = {"state": "running", "started": datetime.now(timezone.utc).isoformat()}

            # The vision call takes 30-90s. Answer immediately and let the client
            # poll /report, rather than holding a connection open that mobile
            # networks will drop anyway.
            threading.Thread(target=run_analysis, args=(batch, card), daemon=True).start()
            return self.send_json(202, {"status": "running"})

        return self.fail(404, "no such route")


def main():
    INTAKE.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    srv = ThreadingHTTPServer((HOST, PORT), Handler)
    mode = "token auth" if TOKEN else "LOOPBACK ONLY (PREGRADE_API_TOKEN unset)"
    print(f"pregrade api on http://{HOST}:{PORT} — {mode}", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        srv.shutdown()


if __name__ == "__main__":
    main()
