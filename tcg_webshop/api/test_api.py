"""End-to-end tests for the pre-grade HTTP API.

    python3 api/test_api.py

Runs a real server on an ephemeral loopback port and talks to it over HTTP, so
the routing, the auth bypass for loopback, the JSON shapes and the on-disk
side effects are all exercised the way the app exercises them.

cv2 and numpy are stubbed when absent. Only `centering` and `vision` need them,
and neither is reached by anything tested here: comps, EV and reporting are
stdlib arithmetic over numbers the engine already produced. The stub is what
makes these tests runnable on the box the code is edited on, which does not
have OpenCV installed — the engine only ever runs on the API host.
"""

import json
import sys
import tempfile
import threading
import types
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

for missing in ("cv2", "numpy"):
    try:
        __import__(missing)
    except ImportError:
        sys.modules[missing] = types.ModuleType(missing)

sys.path.insert(0, str(ROOT / "api"))
import server  # noqa: E402

FAILURES = []


def check(name, condition, detail=""):
    if condition:
        print(f"PASS {name}")
    else:
        print(f"FAIL {name}{': ' + detail if detail else ''}")
        FAILURES.append(name)


def request(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{BASE}{path}", data=data, method=method)
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return res.status, json.loads(res.read() or b"{}")
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        try:
            return exc.code, json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return exc.code, {"raw": raw.decode(errors="replace")}


# A band and a vision result the engine could have produced. EV is a pure
# function of these plus comps, which is the whole reason repricing does not
# need the photos or another vision call.
RAW = {
    "band": {"grade_low": 8, "grade_high": 9, "limiting_factor": "front centering"},
    "vision": {"surface": {"assessable": True}, "corners": {"assessable": True}},
    "call": "KANSKE",
    "reason": "centrering tar taket till 9",
    "warnings": [],
}


def seed_analysed_card(batch, card):
    """Write the artifacts a completed analysis leaves behind."""
    out = server.REPORTS / batch
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{card}.raw.json").write_text(json.dumps(RAW), encoding="utf-8")
    (out / f"{card}.json").write_text(
        json.dumps({
            "status": "done", "batch": batch, "card": card,
            "band": {"low": 8, "high": 9, "limiting": "front centering"},
            "call": "KANSKE", "criteria": [], "warnings": [],
            "ev": {"computable": False, "reason": "comps saknas"},
        }),
        encoding="utf-8",
    )


def main():
    global BASE

    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name)
    server.INTAKE = root / "intake"
    server.REPORTS = root / "reports"
    server.INTAKE.mkdir()
    server.REPORTS.mkdir()
    server.TOKEN = ""  # loopback requests carry no cf-connecting-ip, so they pass

    srv = ThreadingHTTPServer(("127.0.0.1", 0), server.Handler)
    BASE = f"http://127.0.0.1:{srv.server_address[1]}"
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    try:
        # -- health ---------------------------------------------------------
        code, body = request("GET", "/api/health")
        check("health answers", code == 200 and body.get("ok"), f"{code} {body}")

        # -- validation refuses what the engine cannot read ------------------
        code, body = request("PUT", "/api/cards/b1/c1/comps", {"psa10_price": 9000})
        check(
            "unknown key rejected by name",
            code == 400 and "psa10_price" in body.get("error", ""),
            f"{code} {body}",
        )

        code, body = request("PUT", "/api/cards/b1/c1/comps", {"raw_sek": "1200"})
        check("string price rejected", code == 400, f"{code} {body}")

        code, body = request("PUT", "/api/cards/b1/c1/comps", {"card": "bara namn"})
        check("comps with no price rejected", code == 400, f"{code} {body}")

        code, body = request("PUT", "/api/cards/../etc/comps", {"raw_sek": 1})
        check("path traversal rejected", code in (400, 404), f"{code} {body}")

        # -- storing comps before the photos exist --------------------------
        code, body = request(
            "PUT", "/api/cards/b1/c1/comps",
            {"raw_sek": 1200, "psa9_sek": 2600, "psa8_sek": 1500, "card": "Test"},
        )
        check("comps stored pre-analysis", code == 200, f"{code} {body}")
        check(
            "no report to reprice yet",
            body.get("report") is None,
            f"report={body.get('report')}",
        )
        check(
            "card.json written where the engine reads it",
            (server.INTAKE / "b1" / "c1" / "card.json").exists(),
        )
        check(
            "checked stamped automatically",
            "checked" in body.get("comps", {}),
            f"{body.get('comps')}",
        )

        code, body = request("GET", "/api/cards/b1/c1/comps")
        check(
            "comps read back",
            code == 200 and body["comps"]["psa9_sek"] == 2600,
            f"{code} {body}",
        )

        # -- repricing an analysed card -------------------------------------
        seed_analysed_card("b2", "c2")
        code, body = request(
            "PUT", "/api/cards/b2/c2/comps",
            {"raw_sek": 1200, "psa9_sek": 2600, "psa8_sek": 1500},
        )
        ev = (body.get("report") or {}).get("ev") or {}
        # 0.5*1500 + 0.5*2600 = 2050 gross; *0.9 - 450 = 1395 net graded.
        # 1200 * 0.9 = 1080 net raw. Delta 315, over the 250 margin.
        check("repriced without re-analysis", code == 200 and ev.get("computable"), f"{code} {ev}")
        check("graded net correct", ev.get("graded_net_sek") == 1395, f"{ev}")
        check("raw net correct", ev.get("raw_net_sek") == 1080, f"{ev}")
        check("delta correct", ev.get("delta_sek") == 315, f"{ev}")
        check("verdict is GRADA", ev.get("verdict") == "GRADA", f"{ev}")

        code, body = request("GET", "/api/cards/b2/c2/report")
        check(
            "repriced report is what /report serves",
            code == 200 and body["ev"].get("delta_sek") == 315,
            f"{code} {body.get('ev')}",
        )

        # -- the zero that used to be invented ------------------------------
        seed_analysed_card("b3", "c3")
        code, body = request(
            "PUT", "/api/cards/b3/c3/comps", {"psa9_sek": 2600, "psa8_sek": 1500}
        )
        ev = (body.get("report") or {}).get("ev") or {}
        check("graded-only comps still compute", ev.get("computable"), f"{ev}")
        check(
            "no invented raw net",
            "raw_net_sek" not in ev,
            f"raw_net_sek={ev.get('raw_net_sek')}",
        )
        check("no invented delta", "delta_sek" not in ev, f"delta_sek={ev.get('delta_sek')}")
        check("no verdict without a raw price", "verdict" not in ev, f"{ev}")
        check(
            "missing raw_sek is warned about",
            any("raw_sek" in w for w in body.get("warnings", [])),
            f"{body.get('warnings')}",
        )

        # -- PUT replaces, it does not merge --------------------------------
        code, body = request("PUT", "/api/cards/b2/c2/comps", {"raw_sek": 1200})
        check(
            "PUT replaces the document",
            code == 200 and "psa9_sek" not in body["comps"],
            f"{body.get('comps')}",
        )
        ev = (body.get("report") or {}).get("ev") or {}
        check("dropping every graded price stops the maths", not ev.get("computable"), f"{ev}")

        # -- suspicious but legal comps warn rather than refuse --------------
        code, body = request(
            "PUT", "/api/cards/b4/c4/comps", {"psa9_sek": 5000, "psa10_sek": 1000}
        )
        check(
            "inverted grade prices warn",
            code == 200 and any("omkastade" in w for w in body.get("warnings", [])),
            f"{code} {body.get('warnings')}",
        )

        code, body = request("PUT", "/api/cards/b5/c5/comps", {"raw_sek": 90_000_000})
        check("fat-fingered price refused", code == 400, f"{code} {body}")

        # -- unrelated routes still behave ----------------------------------
        code, body = request("PUT", "/api/cards/b1/c1/report", {})
        check("PUT on a non-comps route is 404", code == 404, f"{code} {body}")
    finally:
        srv.shutdown()
        tmp.cleanup()

    print(f"\n{'FAILED: ' + ', '.join(FAILURES) if FAILURES else 'alla tester ok'}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
