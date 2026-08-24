#!/usr/bin/env python3
"""Validate a static image or video task manifest against profile and QA contracts."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROFILES_DIR = ROOT / "ip-profiles"
SCHEMA_PATH = ROOT / "references/contracts/task-manifest.schema.json"
IMAGE_CHECKER_PATH = ROOT / "scripts/check-image-assets.py"


def _matches_type(value: Any, expected: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
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
    if isinstance(value, list):
        for index, item in enumerate(value):
            if "items" in schema:
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


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: cannot read JSON: {exc}") from exc


def _image_errors(manifest_path: Path) -> list[str]:
    spec = importlib.util.spec_from_file_location("check_image_assets", IMAGE_CHECKER_PATH)
    if spec is None or spec.loader is None:
        return ["cannot load image asset checker"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.check_manifest(manifest_path)


def _safe_path(base: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"path must stay inside its base directory: {raw}")
    return base / path


def _semantic_errors(manifest_path: Path, manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    state = manifest["state"]
    qa_status = manifest["qa"]["status"]
    expected_state_status = {
        "DRAFT": "DRAFT",
        "NEEDS_REVIEW": "NEEDS_REVIEW",
        "CONFIRMED": "CONFIRMED",
        "REJECT": "REJECTED",
    }.get(qa_status)
    if expected_state_status and state["status"] != expected_state_status:
        errors.append(
            f"state.status {state['status']!r} does not match qa.status {qa_status!r}"
        )
    if qa_status == "CONFIRMED" and state["stale"]:
        errors.append("confirmed task cannot be stale")

    if manifest["reference_protocol"] == "dual":
        narrative = manifest.get("narrative")
        if not narrative:
            errors.append("dual task requires narrative fields")
        elif manifest["profile"]["id"] == "laoyang":
            if narrative["presenter"] != "老杨" or narrative["executor"] not in {"老杨（单人任务）", "小石头"}:
                errors.append("laoyang dual-reference task must assign 老杨 as presenter and 老杨（单人任务） or 小石头 as executor")
        elif narrative["presenter"] != "老杨" or narrative["executor"] != "小石头":
            errors.append("default dual-IP task must assign 老杨 as presenter and 小石头 as executor")

    profile_id = manifest["profile"]["id"]
    profile_manifest_path = PROFILES_DIR / profile_id / "profile.manifest.json"
    if not profile_manifest_path.exists():
        return [f"profile manifest does not exist: {profile_id}"]
    profile = _read_json(profile_manifest_path)
    if manifest["profile"]["version"] != profile.get("version"):
        errors.append(
            f"profile.version {manifest['profile']['version']!r} does not match "
            f"{profile_id} manifest {profile.get('version')!r}"
        )

    protocol = manifest["reference_protocol"]
    allowed = {"none", "single", "dual", "DEGRADED_TO_SINGLE"}
    if protocol not in allowed:
        errors.append(f"unknown reference protocol: {protocol}")
    profile_protocol = profile["references"]["ref_mode"]
    if profile_protocol == "none" and protocol != "none":
        errors.append("none profile cannot use a character reference protocol")
    if profile_protocol == "dual" and protocol not in {"dual", "DEGRADED_TO_SINGLE"}:
        errors.append("dual profile must record dual or DEGRADED_TO_SINGLE")
    if protocol == "dual" and not manifest["reference_assets"]:
        errors.append("dual task requires actual reference_assets")
    if protocol == "none" and manifest["reference_assets"]:
        errors.append("none task cannot pass reference_assets")

    profile_dir = profile_manifest_path.parent
    asset_source = profile.get("asset_source", {}).get("profile_id", profile_id)
    asset_dir = PROFILES_DIR / asset_source
    for index, raw_path in enumerate(manifest["reference_assets"]):
        try:
            path = _safe_path(asset_dir, raw_path)
        except ValueError as exc:
            errors.append(f"reference_assets[{index}]: {exc}")
            continue
        if not path.exists():
            errors.append(f"reference_assets[{index}]: asset does not exist: {raw_path}")

    task_dir = manifest_path.parent
    for index, output in enumerate(manifest["outputs"]):
        try:
            path = _safe_path(task_dir, output["path"])
        except ValueError as exc:
            errors.append(f"outputs[{index}]: {exc}")
            continue
        if manifest["qa"]["status"] == "CONFIRMED" and not path.exists():
            errors.append(f"outputs[{index}]: confirmed output does not exist: {output['path']}")
    if manifest["qa"]["status"] == "CONFIRMED":
        errors.extend(_image_errors(manifest_path))

    qa = manifest["qa"]
    if qa["status"] == "CONFIRMED":
        for field in ("profile_character", "mode", "content", "facts_authorization"):
            if qa[field] != "PASS" and qa[field] != "N/A":
                errors.append(f"qa.{field}: confirmed task cannot have {qa[field]}")
        if not manifest["outputs"]:
            errors.append("qa.status=CONFIRMED requires at least one output")
    if qa["status"] == "REJECT" and not qa.get("failed_layer"):
        errors.append("qa.status=REJECT requires qa.failed_layer")
    if qa["status"] == "DRAFT" and manifest["outputs"]:
        errors.append("draft task should not claim final outputs")
    return errors


def validate(manifest_path: Path) -> list[str]:
    schema = _read_json(SCHEMA_PATH)
    manifest = _read_json(manifest_path)
    errors = _schema_errors(manifest, schema)
    if not errors:
        errors.extend(_semantic_errors(manifest_path, manifest))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    path = args.manifest.resolve()
    try:
        errors = validate(path)
    except ValueError as exc:
        print(f"FAIL {exc}")
        return 1
    if errors:
        print(f"FAIL {path}")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"PASS {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
