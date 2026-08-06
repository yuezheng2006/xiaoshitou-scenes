#!/usr/bin/env python3
"""Validate machine-readable IP profile manifests without third-party packages."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROFILES_DIR = ROOT / "ip-profiles"
SCHEMA_PATH = ROOT / "references/contracts/profile-manifest.schema.json"
MANIFEST_NAME = "profile.manifest.json"


class ValidationError(Exception):
    """Raised for one invalid manifest."""


def _matches_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


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
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: must not be empty")
        pattern = schema.get("pattern")
        if pattern and not re.fullmatch(pattern, value):
            errors.append(f"{path}: does not match {pattern}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: requires at least {schema['minItems']} items")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(_schema_errors(item, item_schema, f"{path}[{index}]"))
    if isinstance(value, dict):
        for required in schema.get("required", []):
            if required not in value:
                errors.append(f"{path}: missing {required}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{path}: unknown field {key}")
        for key, child in value.items():
            if key in properties:
                errors.extend(_schema_errors(child, properties[key], f"{path}.{key}"))
            elif "additionalProperties" in schema and isinstance(schema["additionalProperties"], dict):
                errors.extend(
                    _schema_errors(child, schema["additionalProperties"], f"{path}.{key}")
                )
    return errors


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"{path}: cannot read JSON: {exc}") from exc


def _resolve_asset(profile_dir: Path, raw_path: str | None) -> Path | None:
    if raw_path is None:
        return None
    if raw_path.startswith("/") or ".." in Path(raw_path).parts:
        raise ValidationError(f"{profile_dir.name}: asset path must stay inside profile: {raw_path}")
    return profile_dir / raw_path.rstrip("/")


def _asset_root(profile_dir: Path, manifest: dict[str, Any]) -> Path:
    source = manifest.get("asset_source")
    if not source:
        return profile_dir
    source_dir = PROFILES_DIR / source["profile_id"]
    if not source_dir.is_dir():
        raise ValidationError(
            f"{profile_dir.name}: asset_source profile does not exist: {source['profile_id']}"
        )
    return source_dir


def _check_asset_paths(
    profile_dir: Path,
    asset_root: Path,
    manifest: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    def check(raw_path: str | None, field: str, *, required: bool = True) -> None:
        if raw_path is None:
            if required:
                errors.append(f"{field}: missing asset path")
            return
        try:
            path = _resolve_asset(asset_root, raw_path)
        except ValidationError as exc:
            errors.append(str(exc))
            return
        if path is None or not path.exists():
            errors.append(f"{field}: asset does not exist: {raw_path}")

    identity = manifest["identity"]
    if manifest["input_kind"] == "none":
        if identity["canonical_asset"] is not None:
            errors.append("identity.canonical_asset: none profile must use null")
    else:
        check(identity["canonical_asset"], "identity.canonical_asset")
    check(identity.get("identity_sheet"), "identity.identity_sheet", required=False)

    references = manifest["references"]
    for index, raw_path in enumerate(references.get("identity_assets", [])):
        check(raw_path, f"references.identity_assets[{index}]")
    for mode, raw_path in references["calibration"].items():
        check(raw_path, f"references.calibration.{mode}", required=False)

    privacy = manifest["privacy"]
    for kind in ("public_assets", "private_assets"):
        for index, raw_path in enumerate(privacy[kind]):
            check(raw_path, f"privacy.{kind}[{index}]")
            if kind == "public_assets" and "private" in Path(raw_path).parts:
                errors.append(f"privacy.public_assets[{index}]: private path cannot be public")
    if set(privacy["public_assets"]) & set(privacy["private_assets"]):
        errors.append("privacy: public_assets and private_assets overlap")
    return errors


def _semantic_errors(profile_dir: Path, manifest: dict[str, Any]) -> list[str]:
    try:
        asset_root = _asset_root(profile_dir, manifest)
    except ValidationError as exc:
        return [str(exc)]
    errors = _check_asset_paths(profile_dir, asset_root, manifest)
    profile_id = manifest["profile_id"]
    if profile_id != profile_dir.name:
        errors.append(f"profile_id {profile_id!r} must match directory {profile_dir.name!r}")

    input_kind = manifest["input_kind"]
    identity = manifest["identity"]
    references = manifest["references"]
    if input_kind == "none":
        if references["ref_mode"] != "none":
            errors.append("none profile must use ref_mode=none")
        if references.get("identity_assets"):
            errors.append("none profile cannot declare identity_assets")
    elif not references.get("identity_assets"):
        errors.append("non-none profile needs at least one identity asset")

    if input_kind == "brand_mark" and not identity.get("identity_sheet"):
        errors.append("brand_mark profile requires identity.identity_sheet")
    if manifest["status"] == "AVAILABLE" and input_kind != "none":
        if identity["canonical_asset"] is None:
            errors.append("AVAILABLE profile requires a canonical asset")
    if references["ref_mode"] == "dual":
        if not any(path for path in references["calibration"].values()):
            errors.append("dual profile requires at least one calibration asset")
    for mode, status in references.get("calibration_status", {}).items():
        has_asset = bool(references["calibration"].get(mode))
        if status == "AVAILABLE" and not has_asset:
            errors.append(f"references.calibration_status.{mode}: AVAILABLE requires an asset")
        if status == "DEFERRED" and has_asset:
            errors.append(f"references.calibration_status.{mode}: DEFERRED cannot have an asset")
    return errors


def validate_manifest(path: Path, schema: dict[str, Any]) -> list[str]:
    profile_dir = path.parent
    manifest = _load_json(path)
    errors = _schema_errors(manifest, schema)
    if not errors:
        errors.extend(_semantic_errors(profile_dir, manifest))
    return [f"{path.relative_to(ROOT)}: {error}" for error in errors]


def discover_manifests(profile: str | None) -> list[Path]:
    if profile:
        path = PROFILES_DIR / profile / MANIFEST_NAME
        return [path]
    return sorted(PROFILES_DIR.glob(f"*/{MANIFEST_NAME}"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", help="validate one profile directory")
    parser.add_argument("--json", action="store_true", help="emit machine-readable results")
    args = parser.parse_args()

    schema = _load_json(SCHEMA_PATH)
    manifests = discover_manifests(args.profile)
    if not manifests:
        print("No profile manifests found", file=sys.stderr)
        return 1

    results: dict[str, list[str]] = {}
    for manifest_path in manifests:
        if not manifest_path.exists():
            results[str(manifest_path.relative_to(ROOT))] = ["manifest does not exist"]
            continue
        results[str(manifest_path.relative_to(ROOT))] = validate_manifest(manifest_path, schema)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        failed = 0
        for path, errors in results.items():
            if errors:
                failed += 1
                print(f"FAIL {path}")
                for error in errors:
                    print(f"  - {error}")
            else:
                print(f"PASS {path}")
        print(f"{len(results) - failed} passed, {failed} failed")
    return 1 if any(results.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
