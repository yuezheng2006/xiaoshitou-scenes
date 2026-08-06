#!/usr/bin/env python3
"""Run a child Codex session from Cursor and keep generated images in the project."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()
GENERATED_IMAGES = CODEX_HOME / "generated_images"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        required=False,
        type=Path,
        help="directory where the child Codex must save final images",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="print the Cursor bridge capability and authentication result",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="print structured output; only valid with --check",
    )
    parser.add_argument(
        "--prompt-file",
        type=Path,
        help="UTF-8 prompt file; otherwise read the prompt from stdin",
    )
    parser.add_argument(
        "--image",
        action="append",
        default=[],
        type=Path,
        help="reference image to attach to the child session; repeatable",
    )
    return parser.parse_args()


def _read_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        return args.prompt_file.read_text(encoding="utf-8")
    return sys.stdin.read()


def _validate_images(images: list[Path]) -> list[Path]:
    resolved: list[Path] = []
    for image in images:
        path = image.expanduser().resolve()
        if not path.is_file():
            raise ValueError(f"reference image does not exist: {image}")
        resolved.append(path)
    return resolved


def _capability_result() -> dict[str, object]:
    """Return one provider-neutral capability result for the Cursor bridge."""
    cli_path = shutil.which("codex")
    if cli_path is None:
        return {
            "schema_version": "1.0",
            "transport": "cursor-bridge",
            "provider": "codex",
            "codex_cli_available": False,
            "authenticated": False,
            "can_generate": False,
            "api_key_required": False,
            "reason": "codex CLI not found",
        }
    result = subprocess.run(
        ["codex", "login", "status"],
        capture_output=True,
        text=True,
        check=False,
    )
    authenticated = result.returncode == 0
    return {
        "schema_version": "1.0",
        "transport": "cursor-bridge",
        "provider": "codex",
        "codex_cli_available": True,
        "authenticated": authenticated,
        "can_generate": authenticated,
        "api_key_required": False,
        "reason": None if authenticated else "codex login status failed",
    }


def _check_codex_login() -> bool:
    """Require Codex session auth before starting a potentially long generation."""
    capability = _capability_result()
    if capability["authenticated"]:
        return True
    print(
        "ERROR: Codex CLI is not logged in. Run `codex login` or "
        "`codex login --device-auth` before using the Cursor bridge.",
        file=sys.stderr,
    )
    return False


def _bridge_instructions(output_dir: Path) -> str:
    return f"""

You are the child Codex session for a parent Cursor agent.
Execute the requested image-generation task now; do not only explain or return prompts.

Bridge rules:
1. Use the repository's ./scene-skill-core/SKILL.md as the source of truth and
   Codex's native imagen tool for every image. Do not rely on a stale globally
   installed copy if it differs from the repository.
2. Authenticate through the existing Codex login session. Do not ask for,
   read, or require OPENAI_API_KEY, and do not call an external image API.
3. Read the required local profile and mode references before generating.
4. Save every final candidate image, after Confirm Gate and mode QA, under:
   {output_dir}
5. Use stable names such as 01-topic.png, 02-topic.png. Do not save only under
   ~/.codex/generated_images/.
6. Do not modify unrelated repository files. In your final response list the exact
   generated paths and QA status.
"""


def _copy_fallback_images(output_dir: Path, started_at: float) -> list[Path]:
    if any(output_dir.glob("*.png")):
        return []
    if not GENERATED_IMAGES.exists():
        return []
    candidates = [
        path
        for path in GENERATED_IMAGES.rglob("*.png")
        if path.is_file() and path.stat().st_mtime >= started_at
    ]
    copied: list[Path] = []
    for index, source in enumerate(sorted(candidates, key=lambda item: item.stat().st_mtime), 1):
        destination = output_dir / f"{index:02d}-codex-generated.png"
        shutil.copy2(source, destination)
        copied.append(destination)
    return copied


def main() -> int:
    args = _parse_args()
    if args.json and not args.check:
        print("ERROR: --json is only valid with --check.", file=sys.stderr)
        return 2
    if args.check:
        capability = _capability_result()
        if args.json:
            print(json.dumps(capability, ensure_ascii=False, sort_keys=True))
        else:
            for key, value in capability.items():
                print(f"{key}: {value}")
        return 0 if capability["can_generate"] else 2
    if args.output_dir is None:
        print("ERROR: --output-dir is required unless using --check.", file=sys.stderr)
        return 2
    if shutil.which("codex") is None:
        print("ERROR: codex CLI not found; install/login to Codex before using the Cursor bridge.", file=sys.stderr)
        return 2
    if not _check_codex_login():
        return 2

    try:
        prompt = _read_prompt(args).strip()
        reference_images = _validate_images(args.image)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if not prompt:
        print("ERROR: prompt is empty; pass --prompt-file or pipe a prompt on stdin.", file=sys.stderr)
        return 2

    output_dir = args.output_dir.expanduser()
    if not output_dir.is_absolute():
        output_dir = ROOT / output_dir
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    command = [
        "codex",
        "exec",
        "-C",
        str(ROOT),
        "-s",
        "workspace-write",
        "--ephemeral",
        "-o",
        str(output_dir / "codex-last-message.txt"),
    ]
    for image in reference_images:
        command.extend(["-i", str(image)])
    command.append("-")

    started_at = time.time()
    child_prompt = prompt + _bridge_instructions(output_dir)
    print(f"Starting child Codex session; output directory: {output_dir}")
    result = subprocess.run(command, input=child_prompt, text=True, cwd=ROOT)
    copied = _copy_fallback_images(output_dir, started_at)
    if copied:
        print("Copied generated images from Codex cache:")
        for path in copied:
            print(f"  {path}")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
