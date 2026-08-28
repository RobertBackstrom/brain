"""
export_blueprints.py - one-time (and re-runnable) Blueprint-to-text export for Curveball / BladeBallArena.

WP0.3 in curveball/drafts/dev_plan_p2p_steam.md. The game logic lives in 5,469 binary .uasset files
that no text tool can read. This turns them into T3D/JSON on disk so they can be diffed, grepped,
reviewed and indexed into RAG.

Run headless on the build machine (forge), UE 5.3:

    "D:\\UE\\UnrealEngine\\Engine\\Binaries\\Win64\\UnrealEditor-Cmd.exe" ^
        "D:\\Curveball\\BBA\\BladeBallArena.uproject" ^
        -run=pythonscript -script="D:\\Curveball\\Tools\\export_blueprints.py" ^
        -unattended -nosplash -nopause -NoShaderCompile

Configuration comes from environment variables so it needs no argv plumbing through the commandlet:

    CVB_EXPORT_DIR    output root          (default D:\\Curveball\\BlueprintExports)
    CVB_SCOPE         priority | all       (default all; "priority" = the WP0.3 review list only)
    CVB_RESUME        1 | 0                (default 1; skip assets whose export already exists)
    CVB_ROOT          content root to walk (default /Game)

Outputs under CVB_EXPORT_DIR:

    <package path>.T3D        one per Blueprint / WidgetBlueprint / AnimBlueprint, mirrors /Game tree
    <package path>.csv|.json  one per DataTable / CurveTable
    _manifest.csv             every asset attempted: path, class, status, bytes, seconds
    _summary.json             counts, failures, timing, the priority-asset dependency map
    _failures.log             full stack per failure
    _references.json          for each priority asset: what it hard-references and what references it

Design notes:
  - The exporter is picked by file extension (task.exporter = None). Naming the file .T3D gets the
    object T3D exporter; .csv/.json get the DataTable exporters. This avoids depending on exporter
    classes being exposed to Python, which varies between engine versions.
  - Assets are loaded one at a time and the export task runs per asset, so one bad asset cannot take
    the run down. Failures are recorded and the run continues.
  - Re-runnable: with CVB_RESUME=1 an interrupted run picks up where it stopped.
"""

import csv
import json
import os
import time
import traceback

import unreal

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

EXPORT_DIR = os.environ.get("CVB_EXPORT_DIR", r"D:\Curveball\BlueprintExports")
SCOPE = os.environ.get("CVB_SCOPE", "all").strip().lower()
RESUME = os.environ.get("CVB_RESUME", "1") not in ("0", "false", "False")
CONTENT_ROOT = os.environ.get("CVB_ROOT", "/Game")

# Classes we export as T3D text. Everything else is skipped unless it is tabular (below).
T3D_CLASSES = ("Blueprint", "WidgetBlueprint", "AnimBlueprint", "BlueprintGeneratedClass")

# Tabular assets export to both csv and json; json keeps types that csv flattens away.
TABLE_CLASSES = ("DataTable", "CurveTable")

# The WP0.3 review order, from dev_plan_p2p_steam.md section 7. These gate replication and
# services work, so they are exported first and get the reference map even in a full run.
PRIORITY = [
    "/Game/Blueprints/GameInstance/BP_GameInstance",
    "/Game/Blueprints/Gamemodes/GM_MogadishuBasic",
    "/Game/Blueprints/Gamemodes/GM_Tutorial",
    "/Game/Blueprints/Gamemodes/BP_TestGamemode",
    "/Game/Levels/MainMenu/GM_MainMenu",
    "/Game/Levels/MainMenu/GM_MainMenu_Rework",
    "/Game/Blueprints/Ball/BP_Ball_New",
    "/Game/Blueprints/Ball/BP_Ball_New_FX",
    "/Game/Blueprints/Characters/BP_PlayerCharacter",
    "/Game/Blueprints/Characters/BP_RemotePartyMemberCharacter",
    "/Game/Blueprints/Matchmaking/DT_MatchMakingConfigurationNames",
    "/Game/Blueprints/Matchmaking/S_MatchMakingConfiguration",
    "/Game/HUDMenu/Widgets/Party/WB_InvitePlayerButton",
    "/Game/HUDMenu/Widgets/Party/WB_KickPlayer",
    "/Game/HUDMenu/Widgets/Party/WB_LeaveParty",
    "/Game/HUDMenu/Widgets/Party/WB_GamemodeButton",
    "/Game/HUDMenu/Widgets/Friends/WB_FriendList",
    "/Game/HUDMenu/Widgets/Friends/WB_AddFriendPopup",
    "/Game/HUDMenu/Widgets/Friends/WB_GameMode",
    "/Game/HUD/Widgets/LocalHud/Popups/W_NewMatchOverPopup",
    "/Game/HUD/Widgets/LocalHud/Popups/W_MatchStat",
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def log(msg):
    unreal.log("[cvb-export] {}".format(msg))


def log_warn(msg):
    unreal.log_warning("[cvb-export] {}".format(msg))


def ensure_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def out_path_for(package_name, extension):
    """/Game/Foo/BP_Bar -> <EXPORT_DIR>/Game/Foo/BP_Bar.T3D"""
    relative = package_name.lstrip("/").replace("/", os.sep)
    full = os.path.join(EXPORT_DIR, relative + extension)
    ensure_dir(os.path.dirname(full))
    return full


def asset_class_name(asset_data):
    """asset_class_path exists in 5.1+, asset_class in older builds. Handle both."""
    try:
        return str(asset_data.asset_class_path.asset_name)
    except AttributeError:
        return str(asset_data.asset_class)


def export_one(asset, filename):
    task = unreal.AssetExportTask()
    task.object = asset
    task.filename = filename
    task.automated = True
    task.prompt = False
    task.replace_identical = True
    task.write_empty_files = False
    # exporter left unset on purpose: the engine resolves it from the extension.
    ok = unreal.Exporter.run_asset_export_task(task)
    if not ok:
        raise RuntimeError("run_asset_export_task returned False")
    if not os.path.isfile(filename):
        raise RuntimeError("exporter reported success but wrote no file")
    return os.path.getsize(filename)


def collect_assets():
    """Return [(package_name, class_name, object_path)] for everything in scope."""
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    registry.wait_for_completion()

    wanted = T3D_CLASSES + TABLE_CLASSES
    found = []
    for asset_data in registry.get_assets_by_path(CONTENT_ROOT, recursive=True):
        cls = asset_class_name(asset_data)
        if cls not in wanted:
            continue
        package = str(asset_data.package_name)
        # BlueprintGeneratedClass duplicates its Blueprint; keep the Blueprint only.
        if cls == "BlueprintGeneratedClass":
            continue
        found.append((package, cls, str(asset_data.get_full_name()).split(" ")[-1]))

    if SCOPE == "priority":
        priority_set = set(PRIORITY)
        found = [f for f in found if f[0] in priority_set]
    else:
        # priority assets first, so a run that gets killed halfway still delivers the review set
        order = {name: i for i, name in enumerate(PRIORITY)}
        found.sort(key=lambda f: (order.get(f[0], 10 ** 6), f[0]))
    return found


def build_reference_map(package_names):
    """Hard dependencies and referencers for the priority set. Cheap, and it answers
    'who actually calls this' without opening the editor."""
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    options = unreal.AssetRegistryDependencyOptions(
        include_soft_package_references=True,
        include_hard_package_references=True,
        include_searchable_names=False,
        include_soft_management_references=False,
        include_hard_management_references=False,
    )
    out = {}
    for name in package_names:
        try:
            deps = registry.get_dependencies(name, options) or []
            refs = registry.get_referencers(name, options) or []
            out[name] = {
                "depends_on": sorted(str(d) for d in deps),
                "referenced_by": sorted(str(r) for r in refs),
            }
        except Exception as exc:  # a missing asset must not kill the run
            out[name] = {"error": str(exc)}
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    started = time.time()
    ensure_dir(EXPORT_DIR)
    log("output   : {}".format(EXPORT_DIR))
    log("scope    : {} (resume={})".format(SCOPE, RESUME))

    assets = collect_assets()
    log("assets in scope: {}".format(len(assets)))

    manifest_path = os.path.join(EXPORT_DIR, "_manifest.csv")
    failures_path = os.path.join(EXPORT_DIR, "_failures.log")
    rows = []
    failures = 0
    skipped = 0
    exported = 0

    with open(failures_path, "a") as failures_file:
        for index, (package, cls, object_path) in enumerate(assets, start=1):
            extensions = [".T3D"] if cls in T3D_CLASSES else [".csv", ".json"]
            table_wrote_something = False
            for extension in extensions:
                target = out_path_for(package, extension)
                if RESUME and os.path.isfile(target) and os.path.getsize(target) > 0:
                    skipped += 1
                    rows.append((package, cls, extension, "skipped", os.path.getsize(target), 0.0))
                    continue

                asset_started = time.time()
                try:
                    asset = unreal.load_asset(package)
                    if asset is None:
                        raise RuntimeError("load_asset returned None")
                    size = export_one(asset, target)
                    exported += 1
                    table_wrote_something = True
                    rows.append(
                        (package, cls, extension, "ok", size, round(time.time() - asset_started, 2))
                    )
                except Exception:
                    failures += 1
                    rows.append((package, cls, extension, "FAILED", 0, round(time.time() - asset_started, 2)))
                    failures_file.write("=== {} ({}{})\n".format(package, cls, extension))
                    failures_file.write(traceback.format_exc())
                    failures_file.write("\n")
                    failures_file.flush()
                    log_warn("FAILED {}{}".format(package, extension))

            # 5.3 headless has no csv/json exporter registered for DataTable or
            # CurveTable ("No csv exporter found for DataTable ..."), so a table
            # would otherwise produce no text at all. The object T3D exporter works
            # for any UObject, so fall back to it and keep the rows readable.
            if cls in TABLE_CLASSES and not table_wrote_something:
                target = out_path_for(package, ".T3D")
                asset_started = time.time()
                try:
                    asset = unreal.load_asset(package)
                    if asset is None:
                        raise RuntimeError("load_asset returned None")
                    size = export_one(asset, target)
                    exported += 1
                    rows.append((package, cls, ".T3D", "ok (table fallback)", size,
                                 round(time.time() - asset_started, 2)))
                    log("table fallback to T3D: {}".format(package))
                except Exception:
                    failures += 1
                    rows.append((package, cls, ".T3D", "FAILED", 0,
                                 round(time.time() - asset_started, 2)))
                    failures_file.write("=== {} ({}.T3D fallback)\n".format(package, cls))
                    failures_file.write(traceback.format_exc())
                    failures_file.write("\n")
                    failures_file.flush()
                    log_warn("FAILED fallback {}".format(package))

            if index % 50 == 0 or index == len(assets):
                log(
                    "{}/{} assets, exported={} skipped={} failed={} elapsed={}s".format(
                        index, len(assets), exported, skipped, failures, int(time.time() - started)
                    )
                )

    with open(manifest_path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["package", "class", "extension", "status", "bytes", "seconds"])
        writer.writerows(rows)

    references = build_reference_map(PRIORITY)
    with open(os.path.join(EXPORT_DIR, "_references.json"), "w") as handle:
        json.dump(references, handle, indent=2, sort_keys=True)

    summary = {
        "generated_by": "export_blueprints.py (WP0.3)",
        "engine": unreal.SystemLibrary.get_engine_version(),
        "project_content_root": CONTENT_ROOT,
        "scope": SCOPE,
        "assets_in_scope": len(assets),
        "exported": exported,
        "skipped_existing": skipped,
        "failed": failures,
        "elapsed_seconds": int(time.time() - started),
        "priority_assets_missing": [
            name for name in PRIORITY if not any(a[0] == name for a in assets)
        ],
    }
    with open(os.path.join(EXPORT_DIR, "_summary.json"), "w") as handle:
        json.dump(summary, handle, indent=2, sort_keys=True)

    log("DONE exported={} skipped={} failed={} in {}s".format(
        exported, skipped, failures, int(time.time() - started)))
    if summary["priority_assets_missing"]:
        log_warn("priority assets not found in the registry: {}".format(
            ", ".join(summary["priority_assets_missing"])))


main()
