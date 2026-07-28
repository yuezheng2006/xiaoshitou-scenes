#!/usr/bin/env python3
"""Preflight a Remotion video project before paid TTS / batch imagen / full render."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any, Optional


def duration_seconds(path: Path) -> Optional[float]:
    ffprobe = shutil.which("ffprobe")
    if not ffprobe or not path.exists():
        return None
    proc = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        check=False,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        return None
    try:
        return float(proc.stdout.strip())
    except ValueError:
        return None


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def update_job_state(project: Path, patch_status: dict[str, Any]) -> None:
    state_path = project / "work" / "job-state.json"
    if not state_path.exists():
        return
    state = load_json(state_path)
    state.setdefault("status", {}).update(patch_status)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--require-images", action="store_true", help="require all scene PNGs to exist")
    parser.add_argument("--require-audio", action="store_true", help="require narration audio to exist")
    parser.add_argument(
        "--require-fish-key",
        action="store_true",
        help="require Fish key when provider is fish-audio (alias kept for old callers)",
    )
    parser.add_argument(
        "--require-tts",
        action="store_true",
        help="require TTS readiness for plan.voice.provider / VIDEO_TTS_PROVIDER",
    )
    args = parser.parse_args()

    project = args.project.resolve()
    issues: list[str] = []
    warnings: list[str] = []

    plan_path = project / "src" / "generated" / "plan.json"
    if not plan_path.exists():
        issues.append(f"missing plan: {plan_path}")
        plan = None
    else:
        plan = load_json(plan_path)
        scenes = plan.get("scenes") or []
        if not 6 <= len(scenes) <= 12:
            issues.append(f"scenes must be 6-12, got {len(scenes)}")
        thesis = (plan.get("motion") or {}).get("thesis") or ""
        if not str(thesis).strip():
            warnings.append("plan.motion.thesis is empty — read video-motion-director.md before imagen")
        missing_state = [s.get("id", "?") for s in scenes if not str(s.get("stateChange") or s.get("state_change") or "").strip()]
        if len(missing_state) > max(1, len(scenes) // 5):
            warnings.append(f"many scenes lack stateChange: {missing_state[:5]}")
        size = (int(plan.get("width", 0)), int(plan.get("height", 0)))
        allowed = {(1080, 1440), (1080, 1920), (1920, 1080)}
        if size not in allowed:
            issues.append(
                f"plan canvas {size[0]}x{size[1]} not in allowed set "
                f"{sorted(f'{w}x{h}' for w, h in allowed)} — set plan.width/height"
            )

        if args.require_images and plan:
            for scene in scenes:
                image = project / "public" / scene.get("image", f"images/{scene.get('id')}.png")
                if not image.exists():
                    issues.append(f"missing image: {image}")
                elif image.stat().st_size < 1000:
                    issues.append(f"image too small: {image}")

    handoff = project / "handoff.md"
    if not handoff.exists():
        warnings.append("handoff.md missing — create from references/contracts/video-handoff.md")

    if not shutil.which("ffprobe"):
        issues.append("ffprobe not found")
    if not shutil.which("ffmpeg"):
        warnings.append("ffmpeg not found (needed for preview trim / QA)")

    audio = project / "public" / "audio" / "narration.mp3"
    audio_duration = duration_seconds(audio) if audio.exists() else None
    if args.require_audio:
        if not audio.exists():
            issues.append(f"missing audio: {audio}")
        elif audio_duration is not None and audio_duration < 5:
            issues.append(f"narration too short: {audio_duration:.2f}s")

    # Detect Fish keys without printing them.
    fish_present = bool(
        os.environ.get("FISH_API_KEY", "").strip()
        or os.environ.get("FISH_AUDIO_API_KEY", "").strip()
    )
    if not fish_present:
        for env_file in (project / ".env", project.parent / ".env"):
            if not env_file.exists():
                continue
            for line in env_file.read_text(encoding="utf-8-sig").splitlines():
                if re.match(r"^(FISH_API_KEY|FISH_AUDIO_API_KEY)=\S+", line.strip()):
                    fish_present = True
                    break
            if fish_present:
                break

    voice = (plan or {}).get("voice") or {}
    provider = (
        os.environ.get("VIDEO_TTS_PROVIDER", "").strip().lower()
        or str(voice.get("provider") or "fish-audio").strip().lower()
    )
    need_tts = args.require_tts or args.require_fish_key
    if need_tts:
        if provider == "fish-audio" and not fish_present:
            issues.append("TTS provider=fish-audio but FISH_API_KEY / FISH_AUDIO_API_KEY missing")
        elif provider == "elevenlabs":
            issues.append("TTS provider=elevenlabs not shipped — use fish-audio or external via video_tts.py")
        elif provider == "external":
            warnings.append("TTS provider=external — pass --audio to video_tts.py after Gate2")
        elif provider not in {"fish-audio", "external", "elevenlabs"}:
            issues.append(f"unknown TTS provider: {provider}")

    package = project / "package.json"
    if not package.exists():
        warnings.append("package.json missing — run video_create_project.py first")

    ok = not issues
    update_job_state(project, {"preflight": "pass" if ok else "fail"})

    report = {
        "ok": ok,
        "project": str(project),
        "issues": issues,
        "warnings": warnings,
        "tts_provider": provider if plan else os.environ.get("VIDEO_TTS_PROVIDER", "fish-audio"),
        "fish_api_key_present": fish_present,
        "audio_duration_seconds": audio_duration,
        "scene_count": len(plan.get("scenes", [])) if plan else 0,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
