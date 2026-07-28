#!/usr/bin/env python3
"""TTS provider router for Little Stone video mode (swap engines freely).

Downstream only depends on this contract — not on Fish / ElevenLabs / etc.:

  Continuous mode (default)
    - write public/audio/narration.mp3
    - set plan.voice.fullAudio = "audio/narration.mp3"
    - allocate scene durationInFrames from ffprobe(audio)

  Segmented mode
    - write public/audio/<scene-id>.mp3 per scene
    - set scene.audio + durationInFrames from each file

Then always prefer:
  python scripts/video_align_captions.py --project <dir>   # scripted

Providers
  fish-audio   → scripts/video_fish_audio.py (shipped)
  external     → bring-your-own audio file; only retime the plan
  elevenlabs   → typed, not shipped (add video_elevenlabs.py later)

Usage
  python scripts/video_tts.py --project <dir>
  python scripts/video_tts.py --project <dir> --provider fish-audio
  python scripts/video_tts.py --project <dir> --provider external --audio /path/to/voice.mp3
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

# Reuse Fish helpers for timing / caption draft (provider-agnostic math).
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import video_fish_audio as fish  # noqa: E402


KNOWN_PROVIDERS = ("fish-audio", "external", "elevenlabs")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_provider(plan: dict[str, Any], cli: str) -> str:
    if cli and cli != "auto":
        return cli.strip().lower()
    env = os.environ.get("VIDEO_TTS_PROVIDER", "").strip().lower()
    if env:
        return env
    voice = plan.get("voice") or {}
    return str(voice.get("provider") or "fish-audio").strip().lower()


def apply_continuous_audio(project: Path, plan: dict[str, Any], audio_src: Path, *, provider: str, voice_name: str) -> None:
    """Copy/place narration.mp3 and retime scenes from measured duration."""
    audio_dir = project / "public" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    dest = audio_dir / "narration.mp3"
    if audio_src.resolve() != dest.resolve():
        shutil.copy2(audio_src, dest)

    total_seconds = fish.duration(dest)
    allocated = fish.allocate_scene_seconds(plan["scenes"], total_seconds)
    target_total_frames = round((total_seconds + 0.8) * plan["fps"])
    used_frames = 0
    caption_map: dict[str, list] = {}
    for scene_index, (scene, seconds) in enumerate(zip(plan["scenes"], allocated)):
        if scene_index == len(plan["scenes"]) - 1:
            frames = max(1, target_total_frames - used_frames)
        else:
            frames = max(1, round(seconds * plan["fps"]))
            used_frames += frames
        scene["audio"] = ""
        scene["audioDurationSeconds"] = round(frames / plan["fps"], 3)
        scene["durationInFrames"] = frames
        caption_map[scene["id"]] = fish.captions(scene.get("caption") or scene["narration"], frames / plan["fps"])
        print(f"[{scene_index + 1}/{len(plan['scenes'])}] {scene['id']} {frames / plan['fps']:.2f}s")

    plan.setdefault("voice", {})
    plan["voice"].update({
        "provider": provider,
        "mode": "continuous",
        "fullAudio": "audio/narration.mp3",
        "voiceId": plan["voice"].get("voiceId") or "external",
        "voiceName": voice_name,
        "modelId": plan["voice"].get("modelId") or "external",
    })
    plan_path = project / "src" / "generated" / "plan.json"
    dump_json(plan_path, plan)
    dump_json(plan_path.parent / "captions.json", caption_map)
    print(f"Voice: {provider} / {voice_name} ({total_seconds:.2f}s)")


def run_fish(project: Path, passthrough: list[str]) -> int:
    script = HERE / "video_fish_audio.py"
    cmd = [sys.executable, str(script), "--project", str(project), *passthrough]
    return subprocess.call(cmd)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--project", type=Path, help="Remotion project dir (required except --list-providers)")
    parser.add_argument(
        "--provider",
        default="auto",
        help="auto | fish-audio | external | elevenlabs (default: plan.voice.provider or VIDEO_TTS_PROVIDER or fish-audio)",
    )
    parser.add_argument("--audio", type=Path, help="for --provider external: path to narration mp3/wav")
    parser.add_argument("--voice-name", default="", help="label written into plan.voice.voiceName")
    parser.add_argument("--list-providers", action="store_true")
    # Pass-through common Fish flags when provider=fish-audio
    parser.add_argument("--model", default="")
    parser.add_argument("--reference-id", default="")
    parser.add_argument("--speed", type=float, default=None)
    parser.add_argument("--mode", choices=("continuous", "segmented"), default=None)
    parser.add_argument("--dry-run", action="store_true")
    args, unknown = parser.parse_known_args()

    if args.list_providers:
        print(json.dumps({
            "providers": {
                "fish-audio": "shipped → video_fish_audio.py",
                "external": "bring-your-own audio → --audio PATH",
                "elevenlabs": "typed only — implement video_elevenlabs.py then register here",
            },
            "contract": "narration.mp3 + plan durations; then video_align_captions.py",
            "docs": "references/contracts/video-tts.md",
        }, ensure_ascii=False, indent=2))
        return 0

    if not args.project:
        raise SystemExit("--project is required (unless --list-providers)")
    project = args.project.resolve()
    plan_path = project / "src" / "generated" / "plan.json"
    if not plan_path.exists():
        raise SystemExit(f"missing plan: {plan_path}")
    plan = load_json(plan_path)
    fish.load_env(project)

    provider = resolve_provider(plan, args.provider)
    if provider not in KNOWN_PROVIDERS:
        raise SystemExit(
            f"unknown TTS provider {provider!r}. Known: {', '.join(KNOWN_PROVIDERS)}. "
            f"To add one: implement a backend that satisfies the contract in this file's docstring, "
            f"then register it in video_tts.py."
        )

    if args.dry_run:
        print(json.dumps({
            "project": str(project),
            "provider": provider,
            "scenes": len(plan.get("scenes") or []),
            "audio": str(args.audio) if args.audio else None,
        }, ensure_ascii=False, indent=2))
        return 0

    if provider == "fish-audio":
        passthrough: list[str] = []
        if args.model:
            passthrough += ["--model", args.model]
        if args.reference_id:
            passthrough += ["--reference-id", args.reference_id]
        if args.speed is not None:
            passthrough += ["--speed", str(args.speed)]
        if args.mode:
            passthrough += ["--mode", args.mode]
        passthrough += unknown
        return run_fish(project, passthrough)

    if provider == "elevenlabs":
        raise SystemExit(
            "provider=elevenlabs is reserved but not shipped. "
            "Options: (1) use --provider fish-audio; "
            "(2) synthesize elsewhere and --provider external --audio voice.mp3; "
            "(3) add scripts/video_elevenlabs.py and wire it in video_tts.py."
        )

    # external
    if not args.audio:
        raise SystemExit("--provider external requires --audio /path/to/narration.mp3")
    if not args.audio.exists():
        raise SystemExit(f"audio not found: {args.audio}")
    # wav → mp3 via ffmpeg if needed
    src = args.audio.resolve()
    if src.suffix.lower() == ".wav":
        mp3 = project / "public" / "audio" / "narration.mp3"
        mp3.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(src), "-codec:a", "libmp3lame", "-q:a", "2", str(mp3)],
            check=True,
        )
        src = mp3
    name = args.voice_name or plan.get("voice", {}).get("voiceName") or "external"
    apply_continuous_audio(project, plan, src, provider="external", voice_name=name)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
