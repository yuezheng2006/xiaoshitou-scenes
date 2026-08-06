#!/usr/bin/env python3
"""Check static image outputs without requiring a third-party image library."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path
from typing import Any


IMAGE_KINDS = {"png", "jpg"}
RATIO_TOLERANCE = 0.03
KNOWN_RATIOS = {
    "16:9": 16 / 9,
    "3:2": 3 / 2,
    "4:3": 4 / 3,
    "3:4": 3 / 4,
    "4:5": 4 / 5,
    "9:16": 9 / 16,
    "2.6:1": 2.6,
    "3:1": 3.0,
}


class ImageCheckError(ValueError):
    """Raised when an image cannot be inspected."""


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _png_metadata_clean(data: bytes) -> bool:
    offset = 8
    while offset + 12 <= len(data):
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        chunk_type = data[offset + 4 : offset + 8]
        if chunk_type in {b"tEXt", b"zTXt", b"iTXt", b"eXIf"}:
            return False
        offset += 12 + length
        if chunk_type == b"IEND":
            break
    return True


def _jpeg_dimensions_and_metadata(data: bytes) -> tuple[int, int, bool]:
    if not data.startswith(b"\xff\xd8"):
        raise ImageCheckError("invalid JPEG signature")
    offset = 2
    metadata_clean = True
    sof_markers = set(range(0xC0, 0xC4)) | set(range(0xC5, 0xC8)) | set(
        range(0xC9, 0xCC)
    ) | set(range(0xCD, 0xD0))
    while offset + 4 <= len(data):
        if data[offset] != 0xFF:
            offset += 1
            continue
        while offset < len(data) and data[offset] == 0xFF:
            offset += 1
        if offset >= len(data):
            break
        marker = data[offset]
        offset += 1
        if marker in {0xD8, 0xD9}:
            continue
        if marker == 0xDA:
            break
        if offset + 2 > len(data):
            raise ImageCheckError("truncated JPEG segment")
        length = struct.unpack(">H", data[offset : offset + 2])[0]
        if length < 2 or offset + length > len(data):
            raise ImageCheckError("invalid JPEG segment length")
        segment = data[offset + 2 : offset + length]
        if marker == 0xE1 and segment.startswith(b"Exif\x00\x00"):
            metadata_clean = False
        if marker in sof_markers and len(segment) >= 5:
            height, width = struct.unpack(">HH", segment[1:5])
            return width, height, metadata_clean
        offset += length
    raise ImageCheckError("JPEG dimensions not found")


def inspect_image(path: Path, kind: str) -> dict[str, Any]:
    if not path.is_file():
        raise ImageCheckError("file does not exist")
    data = path.read_bytes()
    if not data:
        raise ImageCheckError("file is empty")

    if kind == "png":
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            raise ImageCheckError("file is not a PNG")
        if len(data) < 24 or data[12:16] != b"IHDR":
            raise ImageCheckError("PNG IHDR is missing")
        width, height = struct.unpack(">II", data[16:24])
        metadata_clean = _png_metadata_clean(data)
    elif kind == "jpg":
        width, height, metadata_clean = _jpeg_dimensions_and_metadata(data)
    else:
        raise ImageCheckError(f"unsupported image kind: {kind}")

    if width <= 0 or height <= 0:
        raise ImageCheckError("image dimensions must be positive")
    ratio = width / height
    nearest_name, nearest_ratio = min(
        KNOWN_RATIOS.items(), key=lambda item: abs(item[1] - ratio)
    )
    aspect_ratio = nearest_name if abs(nearest_ratio - ratio) <= RATIO_TOLERANCE else f"{width}:{height}"
    return {
        "sha256": _sha256(path),
        "width": width,
        "height": height,
        "aspect_ratio": aspect_ratio,
        "metadata_clean": metadata_clean,
        "bytes": path.stat().st_size,
    }


def _safe_output_path(base: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        raise ImageCheckError(f"output path must stay inside manifest directory: {raw}")
    return base / path


def check_manifest(manifest_path: Path) -> list[str]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for index, output in enumerate(manifest.get("outputs", [])):
        kind = output.get("kind")
        if kind not in IMAGE_KINDS:
            continue
        try:
            path = _safe_output_path(manifest_path.parent, output["path"])
            actual = inspect_image(path, kind)
        except (KeyError, OSError, ImageCheckError, json.JSONDecodeError) as exc:
            errors.append(f"outputs[{index}]: {exc}")
            continue
        for field in ("sha256", "width", "height", "aspect_ratio", "metadata_clean", "bytes"):
            if field not in output:
                errors.append(f"outputs[{index}]: missing image metadata {field}")
            elif output[field] != actual[field]:
                errors.append(
                    f"outputs[{index}].{field}: manifest={output[field]!r}, actual={actual[field]!r}"
                )
        if not actual["metadata_clean"]:
            errors.append(f"outputs[{index}]: image contains EXIF/text metadata")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, nargs="?")
    parser.add_argument("--image", type=Path, help="inspect one image directly")
    parser.add_argument("--kind", choices=sorted(IMAGE_KINDS), help="image kind for --image")
    args = parser.parse_args()
    if args.image:
        if not args.kind:
            parser.error("--kind is required with --image")
        try:
            result = inspect_image(args.image.resolve(), args.kind)
        except (OSError, ImageCheckError) as exc:
            print(f"FAIL {args.image}: {exc}")
            return 1
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0 if result["metadata_clean"] else 1
    if not args.manifest:
        parser.error("manifest is required unless --image is used")
    path = args.manifest.resolve()
    try:
        errors = check_manifest(path)
    except (OSError, json.JSONDecodeError, ImageCheckError) as exc:
        print(f"FAIL {path}: {exc}")
        return 1
    if errors:
        print(f"STALE {path}")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"PASS {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
