#!/usr/bin/env python3
"""Export a profile into a portable, privacy-aware IP Pack."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROFILES_DIR = ROOT / "ip-profiles"


def _read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: cannot read JSON: {exc}") from exc


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_relative(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"asset path must stay inside the profile: {raw}")
    return path


def _asset_visibility(raw: str, profile: dict[str, Any]) -> str:
    privacy = profile["privacy"]
    public_assets = [str(path) for path in privacy.get("public_assets", [])]
    private_assets = [str(path) for path in privacy.get("private_assets", [])]

    def matches(pattern: str) -> bool:
        return raw == pattern or raw.startswith(pattern.rstrip("/") + "/")

    if any(matches(pattern) for pattern in private_assets):
        return "private"
    if any(matches(pattern) for pattern in public_assets):
        return "public"
    return "private"


def _asset_role(raw: str, profile: dict[str, Any]) -> tuple[str, str | None]:
    identity = profile["identity"]
    references = profile["references"]
    if raw == identity.get("canonical_asset"):
        return "canonical", None
    if raw == identity.get("identity_sheet"):
        return "identity_sheet", None
    for mode, calibration in references.get("calibration", {}).items():
        if raw == calibration:
            return "calibration", mode
    if raw in references.get("identity_assets", []):
        if "action" in raw.lower():
            return "action_sheet", None
        return "identity_reference", None
    return "identity_reference", None


def _asset_id(raw: str, role: str, mode: str | None) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", Path(raw).stem.lower()).strip("-")
    parts = [role]
    if mode:
        parts.append(mode)
    if slug:
        parts.append(slug)
    return "-".join(parts)


def _status(profile_status: str) -> str:
    if profile_status == "AVAILABLE":
        return "READY"
    if profile_status in {
        "REQUESTED",
        "USER_REFERENCE",
        "IDENTITY_PLAN",
        "CONFIRMED",
        "CANONICAL_ASSET",
        "MODE_CALIBRATION",
    }:
        return "CALIBRATING"
    return "DRAFT"


def _collect_asset_paths(profile: dict[str, Any]) -> list[str]:
    identity = profile["identity"]
    references = profile["references"]
    candidates = [
        identity.get("canonical_asset"),
        identity.get("identity_sheet"),
        *references.get("identity_assets", []),
        *references.get("calibration", {}).values(),
    ]
    return list(dict.fromkeys(str(path) for path in candidates if path))


def create_pack(
    profile_id: str,
    output_dir: Path,
    consent: str,
    include_private: bool,
) -> Path:
    profile_dir = PROFILES_DIR / profile_id
    manifest_path = profile_dir / "profile.manifest.json"
    if not manifest_path.exists():
        raise ValueError(f"profile manifest does not exist: {profile_id}")
    profile = _read_json(manifest_path)
    asset_profile_id = profile.get("asset_source", {}).get("profile_id", profile_id)
    asset_profile_dir = PROFILES_DIR / asset_profile_id
    if not asset_profile_dir.is_dir():
        raise ValueError(f"asset source profile does not exist: {asset_profile_id}")
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"output directory must be empty: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    pack_assets: list[dict[str, Any]] = []
    for raw in _collect_asset_paths(profile):
        source = asset_profile_dir / _safe_relative(raw)
        if not source.is_file():
            raise ValueError(f"profile asset does not exist: {raw}")
        visibility = _asset_visibility(raw, profile)
        if visibility == "private" and not include_private:
            continue
        destination = output_dir / raw
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        role, mode = _asset_role(raw, profile)
        pack_assets.append(
            {
                "asset_id": _asset_id(raw, role, mode),
                "role": role,
                "mode": mode,
                "path": raw,
                "visibility": visibility,
                "sha256": _sha256(destination),
                "bytes": destination.stat().st_size,
            }
        )

    shutil.copy2(manifest_path, output_dir / "profile.manifest.json")
    for document in profile_dir.glob("*.md"):
        shutil.copy2(document, output_dir / document.name)
    output_manifest = output_dir / "pack.manifest.json"
    calibration_status = profile["references"].get("calibration_status", {})
    modes = []
    for mode, calibration in profile["references"].get("calibration", {}).items():
        asset_ids = [
            asset["asset_id"]
            for asset in pack_assets
            if asset["path"] == calibration
        ]
        status = calibration_status.get(mode)
        if status is None:
            status = "AVAILABLE" if calibration else "DEFERRED"
        modes.append(
            {
                "mode": mode,
                "status": status,
                "calibration_asset_ids": asset_ids,
            }
        )

    private_count = sum(asset["visibility"] == "private" for asset in pack_assets)
    manifest = {
        "schema_version": "1.0",
        "pack_id": profile_id,
        "display_name": profile["display_name"],
        "profile_id": profile_id,
        "profile_version": profile["version"],
        "status": _status(profile["status"]),
        "source": {
            "input_kind": profile["input_kind"],
            "consent": consent,
        },
        "assets": pack_assets,
        "modes": modes,
        "privacy": {
            "public_asset_count": len(pack_assets) - private_count,
            "private_asset_count": private_count,
        },
        "qa": {
            "identity": "PASS" if any(asset["role"] == "canonical" for asset in pack_assets) else "PENDING",
            "calibration": "PASS" if any(asset["role"] == "calibration" for asset in pack_assets) else "PENDING",
            "packaging": "PASS",
        },
    }
    output_manifest.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", help="profile id under scene-skill-core/ip-profiles")
    parser.add_argument("--output", required=True, type=Path, help="empty output directory")
    parser.add_argument(
        "--consent",
        choices=["CONFIRMED", "PENDING", "NOT_REQUIRED"],
        default="PENDING",
    )
    parser.add_argument(
        "--include-private",
        action="store_true",
        help="copy assets classified as private; requires explicit consent",
    )
    args = parser.parse_args()
    if args.include_private and args.consent != "CONFIRMED":
        print("FAIL --include-private requires --consent CONFIRMED", file=sys.stderr)
        return 2
    try:
        path = create_pack(
            args.profile,
            args.output.expanduser().resolve(),
            args.consent,
            args.include_private,
        )
    except (OSError, ValueError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    print(f"PASS {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
