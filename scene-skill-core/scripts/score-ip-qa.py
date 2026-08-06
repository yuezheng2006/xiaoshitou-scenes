#!/usr/bin/env python3
"""Score structured IP QA observations and emit a Task Manifest QA patch."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


WEIGHTS = {
    "identity": 35,
    "style": 25,
    "action": 20,
    "role": 20,
}


def _read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: cannot read JSON: {exc}") from exc


def _dimension_score(observations: dict[str, Any], dimension: str) -> float:
    value = observations.get(dimension)
    if not isinstance(value, dict):
        raise ValueError(f"observations.{dimension} must be an object")
    passed = value.get("passed")
    total = value.get("total")
    if not isinstance(passed, int) or not isinstance(total, int):
        raise ValueError(f"observations.{dimension} needs integer passed/total")
    if total < 1 or passed < 0 or passed > total:
        raise ValueError(f"observations.{dimension} has invalid passed/total")
    return round(passed / total * 100, 2)


def score(profile_manifest: Path, mode: str, observations_path: Path) -> dict[str, Any]:
    profile = _read_json(profile_manifest)
    observations = _read_json(observations_path)
    dimensions = {
        dimension: _dimension_score(observations, dimension)
        for dimension in WEIGHTS
    }
    total = round(
        sum(dimensions[dimension] * weight for dimension, weight in WEIGHTS.items()) / 100,
        2,
    )

    violations = observations.get("negative_violations", [])
    if not isinstance(violations, list):
        raise ValueError("observations.negative_violations must be an array")
    critical = [
        item
        for item in violations
        if isinstance(item, dict) and item.get("severity") == "CRITICAL"
    ]
    important = [
        item
        for item in violations
        if isinstance(item, dict) and item.get("severity") == "IMPORTANT"
    ]
    if critical or total < 70:
        status = "REJECT"
    elif important or total < 85:
        status = "NEEDS_REVIEW"
    else:
        status = "CONFIRMED"

    failed_layer = None
    if critical:
        failed_layer = "qa"
    elif dimensions["identity"] < 100:
        failed_layer = "asset"
    elif dimensions["style"] < 100 or dimensions["action"] < 100:
        failed_layer = "qa"
    elif status == "REJECT":
        failed_layer = "qa"

    qa_patch = {
        "status": status,
        "profile_character": "PASS" if dimensions["identity"] == 100 and not critical else "FAIL",
        "mode": "PASS" if dimensions["style"] == 100 and not critical else "FAIL",
        "content": "N/A",
        "facts_authorization": "N/A",
        "failed_layer": failed_layer,
        "notes": f"IP QA score={total}; mode={mode}",
    }
    return {
        "schema_version": "1.0",
        "profile": {
            "id": profile["profile_id"],
            "version": profile["version"],
        },
        "mode": mode,
        "score": total,
        "dimensions": dimensions,
        "negative_violations": violations,
        "profile_failure_signals": profile["qa"]["failure_signals"],
        "decision": {
            "status": status,
            "critical_violation_count": len(critical),
            "important_violation_count": len(important),
            "failed_layer": failed_layer,
        },
        "task_manifest_qa": qa_patch,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-manifest", required=True, type=Path)
    parser.add_argument("--mode", required=True)
    parser.add_argument("--observations", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = score(
            args.profile_manifest.expanduser().resolve(),
            args.mode,
            args.observations.expanduser().resolve(),
        )
    except (OSError, ValueError, KeyError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1

    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.expanduser().resolve().write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0 if result["decision"]["status"] == "CONFIRMED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
