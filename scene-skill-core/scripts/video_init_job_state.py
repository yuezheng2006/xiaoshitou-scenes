#!/usr/bin/env python3
"""Create work/job-state.json for a Little Stone video project (rachel + lingjian inspired)."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any


def build_state(name: str) -> dict[str, Any]:
    return {
        "project": name,
        "created_at": date.today().isoformat(),
        "positioning": {
            "goal": "long-form + low-cost + high-IP",
            "costly": ["imagen scenes", "Fish TTS"],
            "cheap": ["Remotion re-render", "scripted captions", "typography"],
        },
        "handoff": "handoff.md",
        "plan": "src/generated/plan.json",
        "voice": {
            "provider": "fish-audio",
            "mode": "continuous",
            "full_audio": "public/audio/narration.mp3",
        },
        "captions": {
            "timing_source": None,
            "path": "src/generated/captions.json",
        },
        "gates": {
            "storyboard": {
                "status": "not_started",
                "approved_at": None,
                "artifact_hash": None,
                "passed_scene_ids": [],
            },
            "stills": {
                "status": "not_started",
                "approved_at": None,
                "artifact_hash": None,
                "passed_scene_ids": [],
                "contact_sheet": "out/contact-sheet.jpg",
            },
            "preview": {
                "status": "not_started",
                "approved_at": None,
                "artifact_hash": None,
                "passed_scene_ids": [],
            },
        },
        "status": {
            "preflight": "not_started",
            "gate1_storyboard": "not_started",
            "scenes": "not_started",
            "gate2_stills": "not_started",
            "tts": "not_started",
            "captions": "not_started",
            "preview": "not_started",
            "approved_by_user": False,
            "final": "not_started",
        },
        "outputs": {
            "contact_sheet": "out/contact-sheet.jpg",
            "preview_still": "out/preview.png",
            "final_video": "out/video.mp4",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path, help="Remotion project directory")
    parser.add_argument("--name", default="", help="project display name (default: directory name)")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    project: Path = args.project.resolve()
    project.mkdir(parents=True, exist_ok=True)
    out = project / "work" / "job-state.json"
    if out.exists() and not args.force:
        raise SystemExit(f"{out} already exists; pass --force to overwrite")
    name = args.name.strip() or project.name
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build_state(name), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
