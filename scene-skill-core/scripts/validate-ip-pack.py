#!/usr/bin/env python3
"""Validate a portable IP Pack without third-party packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "references/contracts/ip-pack.schema.json"


def _matches_type(value: Any, expected: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "null": value is None,
    }.get(expected, False)


def _schema_errors(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    if isinstance(expected, list):
        if not any(_matches_type(value, item) for item in expected):
            return [f"{path}: expected one of {expected}"]
    elif expected and not _matches_type(value, expected):
        return [f"{path}: expected {expected}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: expected one of {schema['enum']}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: must not be empty")
        pattern = schema.get("pattern")
        if pattern and not re.fullmatch(pattern, value):
            errors.append(f"{path}: does not match {pattern}")
    if isinstance(value, int) and value < schema.get("minimum", value):
        errors.append(f"{path}: must be >= {schema['minimum']}")
    if isinstance(value, list) and "items" in schema:
        for index, item in enumerate(value):
            errors.extend(_schema_errors(item, schema["items"], f"{path}[{index}]"))
    if isinstance(value, dict):
        for required in schema.get("required", []):
            if required not in value:
                errors.append(f"{path}: missing {required}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{path}: unknown field {key}")
        for key, child_schema in properties.items():
            if key in value:
                errors.extend(_schema_errors(value[key], child_schema, f"{path}.{key}"))
    return errors


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_path(root: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"path must stay inside pack root: {raw}")
    return root / path


def validate(pack_manifest: Path) -> list[str]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        manifest = json.loads(pack_manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read pack: {exc}"]

    errors = _schema_errors(manifest, schema)
    if errors:
        return errors

    root = pack_manifest.parent
    profile_manifest_path = root / "profile.manifest.json"
    if not profile_manifest_path.is_file():
        errors.append("profile.manifest.json is missing from the pack")
    else:
        try:
            profile = json.loads(profile_manifest_path.read_text(encoding="utf-8"))
            source = profile.get("identity", {}).get("description_source")
            if source and not (root / source).is_file():
                errors.append(f"profile description source is missing: {source}")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"profile.manifest.json cannot be read: {exc}")

    asset_ids: set[str] = set()
    for index, asset in enumerate(manifest["assets"]):
        asset_path = _safe_path(root, asset["path"])
        if asset["asset_id"] in asset_ids:
            errors.append(f"assets[{index}]: duplicate asset_id {asset['asset_id']}")
        asset_ids.add(asset["asset_id"])
        if not asset_path.is_file():
            errors.append(f"assets[{index}]: file does not exist: {asset['path']}")
            continue
        if asset_path.stat().st_size != asset["bytes"]:
            errors.append(f"assets[{index}]: bytes do not match: {asset['path']}")
        if _sha256(asset_path) != asset["sha256"]:
            errors.append(f"assets[{index}]: sha256 does not match: {asset['path']}")

    for index, mode in enumerate(manifest["modes"]):
        for asset_id in mode.get("calibration_asset_ids", []):
            if asset_id not in asset_ids:
                errors.append(f"modes[{index}]: unknown calibration asset: {asset_id}")
        if mode["status"] == "AVAILABLE" and not mode.get("calibration_asset_ids"):
            errors.append(f"modes[{index}]: AVAILABLE requires calibration assets")

    actual_private = sum(asset["visibility"] == "private" for asset in manifest["assets"])
    actual_public = len(manifest["assets"]) - actual_private
    if manifest["privacy"]["private_asset_count"] != actual_private:
        errors.append("privacy.private_asset_count does not match assets")
    if manifest["privacy"]["public_asset_count"] != actual_public:
        errors.append("privacy.public_asset_count does not match assets")
    if manifest["status"] == "READY":
        if manifest["source"]["consent"] != "CONFIRMED":
            errors.append("READY pack requires CONFIRMED consent")
        if manifest["qa"]["identity"] != "PASS":
            errors.append("READY pack requires identity QA PASS")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    errors = validate(args.manifest.expanduser().resolve())
    if errors:
        print(f"FAIL {args.manifest}")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"PASS {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
