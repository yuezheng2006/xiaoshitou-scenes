#!/usr/bin/env python3
"""Resolve IP Pack assets into a Task Manifest reference fragment."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


MODES = {
    "physical",
    "physical-long-scroll",
    "handdrawn",
    "knowledge-card",
    "ppt",
    "video",
}


def _read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: cannot read JSON: {exc}") from exc


def _select(
    assets: list[dict[str, Any]],
    role: str,
    mode: str | None = None,
) -> list[dict[str, Any]]:
    return [
        asset
        for asset in assets
        if asset["role"] == role and (mode is None or asset.get("mode") == mode)
    ]


def resolve(
    pack_manifest: Path,
    mode: str,
    action: str | None = None,
) -> dict[str, Any]:
    if mode not in MODES:
        raise ValueError(f"unsupported mode: {mode}")
    pack = _read_json(pack_manifest)
    pack_root = pack_manifest.parent
    assets = pack["assets"]
    warnings: list[str] = []
    errors: list[str] = []

    if pack["status"] == "DEPRECATED":
        errors.append("cannot resolve assets from a DEPRECATED pack")
    if pack["source"]["consent"] != "CONFIRMED":
        warnings.append("pack consent is not CONFIRMED; ordinary delivery remains blocked")

    if pack["source"]["input_kind"] == "none":
        return {
            "schema_version": "1.0",
            "profile": {
                "id": pack["profile_id"],
                "version": pack["profile_version"],
            },
            "mode": mode,
            "reference_protocol": "none",
            "reference_assets": [],
            "resolution": {
                "pack_id": pack["pack_id"],
                "selected_assets": [],
                "warnings": warnings,
                "errors": errors,
                "blocked": bool(errors),
            },
        }

    canonical = _select(assets, "canonical")
    if not canonical:
        errors.append("pack has no canonical identity asset")
        identity_assets: list[dict[str, Any]] = []
    else:
        identity_assets = canonical[:1]
        identity_sheet = _select(assets, "identity_sheet")
        if identity_sheet:
            identity_assets.append(identity_sheet[0])

    mode_info = next(
        (item for item in pack["modes"] if item["mode"] == mode),
        {"status": "DEFERRED", "calibration_asset_ids": []},
    )
    calibration = [
        asset
        for asset in assets
        if asset["asset_id"] in mode_info.get("calibration_asset_ids", [])
    ]
    protocol = "single"
    selected = list(identity_assets)
    if mode_info["status"] == "REJECTED":
        errors.append(f"{mode} calibration is REJECTED")
    elif mode_info["status"] == "AVAILABLE" and calibration:
        protocol = "dual"
        selected.extend(calibration)
    else:
        warnings.append(f"{mode} calibration is unavailable; degraded to single reference")

    if action:
        action_assets = _select(assets, "action_sheet")
        if not action_assets:
            warnings.append(f"requested action {action!r} but pack has no action_sheet")
        else:
            selected.append(action_assets[0])

    selected = list({asset["asset_id"]: asset for asset in selected}.values())
    for asset in selected:
        if not (pack_root / asset["path"]).is_file():
            errors.append(f"selected asset is missing: {asset['path']}")

    return {
        "schema_version": "1.0",
        "profile": {
            "id": pack["profile_id"],
            "version": pack["profile_version"],
        },
        "mode": mode,
        "reference_protocol": protocol if not errors else "DEGRADED_TO_SINGLE",
        "reference_assets": [asset["path"] for asset in selected],
        "resolution": {
            "pack_id": pack["pack_id"],
            "selected_assets": [
                {
                    "asset_id": asset["asset_id"],
                    "role": asset["role"],
                    "mode": asset.get("mode"),
                    "path": asset["path"],
                }
                for asset in selected
            ],
            "warnings": warnings,
            "errors": errors,
            "blocked": bool(errors),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pack", required=True, type=Path, help="pack.manifest.json")
    parser.add_argument("--mode", required=True, help="target output mode")
    parser.add_argument("--action", help="optional action hint, e.g. handoff")
    parser.add_argument("--output", type=Path, help="write JSON resolution to this path")
    args = parser.parse_args()

    try:
        result = resolve(args.pack.expanduser().resolve(), args.mode, args.action)
    except (OSError, ValueError, KeyError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.expanduser().resolve().write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 1 if result["resolution"]["blocked"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
