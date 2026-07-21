#!/usr/bin/env python3
"""Generate and time Fish Audio narration for an explainer project."""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.fish.audio"
DEFAULT_MODEL = "s2.1-pro-free"


def load_env(project: Path) -> None:
    for env_file in (project / ".env", project.parent / ".env"):
        if not env_file.exists():
            continue
        for raw in env_file.read_text(encoding="utf-8-sig").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def duration(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(result.stdout.strip())


def chunks(text: str) -> list[str]:
    if len(re.sub(r"\s", "", text)) <= 24:
        return [text.strip()]
    result = [s.strip() for s in re.split(r"(?<=[，。！？；,.!?;])", text) if s.strip()]
    return result or [text]


def captions(text: str, seconds: float) -> list[dict]:
    parts = chunks(text)
    weights = [max(1, len(re.sub(r"\W", "", p))) for p in parts]
    total, cursor, output = sum(weights), 0.0, []
    for index, (part, weight) in enumerate(zip(parts, weights)):
        end = seconds if index == len(parts) - 1 else cursor + seconds * weight / total
        output.append({"text": part, "startMs": round(cursor * 1000), "endMs": round(end * 1000), "timestampMs": None, "confidence": None})
        cursor = end
    return output


def text_weight(text: str) -> int:
    return max(1, len(re.sub(r"\s", "", text)))


def allocate_scene_seconds(scenes: list[dict], total_seconds: float) -> list[float]:
    weights = [text_weight(scene["narration"]) for scene in scenes]
    total_weight = sum(weights)
    raw = [total_seconds * weight / total_weight for weight in weights]
    # Keep the full-audio timeline stable, while giving every scene a small visual
    # breathing room for title/caption entrances.
    return [max(3.0, seconds) for seconds in raw]


def friendly_http_error(error: urllib.error.HTTPError) -> str:
    try:
        detail = error.read().decode("utf-8", errors="replace")[:800]
    except Exception:
        detail = ""
    if error.code == 401:
        return "Fish Audio rejected the key. Create an API key at https://fish.audio/zh-CN/app/api-keys/ and save FISH_API_KEY in .env."
    if error.code == 402:
        return "Fish Audio account has insufficient credit or the selected model is unavailable."
    if error.code == 429:
        return "Fish Audio rate limit reached. Wait briefly and run the same command again."
    return f"Fish Audio HTTP {error.code}: {detail}"


def synthesize(
    key: str,
    text: str,
    *,
    model: str,
    reference_id: str | None,
    speed: float,
    volume: float,
    latency: str,
) -> bytes:
    payload: dict = {
        "text": text,
        "format": "mp3",
        "mp3_bitrate": 128,
        "normalize": True,
        "latency": latency,
        "prosody": {"speed": speed, "volume": volume},
    }
    if reference_id:
        payload["reference_id"] = reference_id
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"{API}/v1/tts",
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
            "model": model,
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        return response.read()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--model", default=os.environ.get("FISH_MODEL", DEFAULT_MODEL))
    parser.add_argument("--reference-id", default=os.environ.get("FISH_REFERENCE_ID", ""))
    parser.add_argument("--speed", type=float, default=float(os.environ.get("FISH_SPEED", "1.0")))
    parser.add_argument("--volume", type=float, default=float(os.environ.get("FISH_VOLUME", "0")))
    parser.add_argument("--latency", choices=("normal", "balanced"), default=os.environ.get("FISH_LATENCY", "balanced"))
    parser.add_argument("--sample", action="store_true", help="generate one short sample instead of the full project")
    parser.add_argument("--sample-text", default="你好，我们用十秒钟，试一下 Fish Audio 的中文旁白效果。")
    parser.add_argument(
        "--mode",
        choices=("continuous", "segmented"),
        default=os.environ.get("FISH_TTS_MODE", "continuous"),
        help="continuous creates one unified voiceover file; segmented creates one file per scene.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    plan_path = project / "src" / "generated" / "plan.json"
    if not plan_path.exists():
        raise SystemExit(f"Missing plan: {plan_path}")
    plan = json.loads(plan_path.read_text(encoding="utf-8-sig"))
    load_env(project)
    key = os.environ.get("FISH_API_KEY", "").strip()
    reference_id = args.reference_id.strip() or None
    if args.dry_run:
        print(json.dumps({
            "project": str(project),
            "scenes": len(plan["scenes"]),
            "model": args.model,
            "reference_id": reference_id or "default",
            "mode": args.mode,
            "speed": args.speed,
            "latency": args.latency,
        }, ensure_ascii=False, indent=2))
        return
    if not key:
        raise SystemExit("Fish Audio is not configured. Add FISH_API_KEY to the project .env; never paste it into chat or commit it.")

    audio_dir = project / "public" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    if args.sample:
        sample_dir = project / "public" / "voice-samples"
        sample_dir.mkdir(parents=True, exist_ok=True)
        try:
            audio = synthesize(
                key,
                args.sample_text,
                model=args.model,
                reference_id=reference_id,
                speed=args.speed,
                volume=args.volume,
                latency=args.latency,
            )
        except urllib.error.HTTPError as error:
            raise SystemExit(friendly_http_error(error)) from error
        path = sample_dir / "fish-audio-sample.mp3"
        path.write_bytes(audio)
        print(path)
        return

    caption_map = {}
    if args.mode == "continuous":
        full_text = "\n\n".join(scene["narration"].strip() for scene in plan["scenes"])
        try:
            audio = synthesize(
                key,
                full_text,
                model=args.model,
                reference_id=reference_id,
                speed=args.speed,
                volume=args.volume,
                latency=args.latency,
            )
        except urllib.error.HTTPError as error:
            raise SystemExit(f"Fish Audio continuous narration: {friendly_http_error(error)}") from error
        audio_path = audio_dir / "narration.mp3"
        audio_path.write_bytes(audio)
        total_seconds = duration(audio_path)
        allocated = allocate_scene_seconds(plan["scenes"], total_seconds)
        # Correct rounding drift on the final scene so sum(scene frames) matches
        # the unified narration duration plus a short ending breath.
        target_total_frames = round((total_seconds + 0.8) * plan["fps"])
        used_frames = 0
        for scene_index, (scene, seconds) in enumerate(zip(plan["scenes"], allocated)):
            if scene_index == len(plan["scenes"]) - 1:
                frames = max(1, target_total_frames - used_frames)
            else:
                frames = max(1, round(seconds * plan["fps"]))
                used_frames += frames
            scene["audio"] = ""
            scene["audioDurationSeconds"] = round(frames / plan["fps"], 3)
            scene["durationInFrames"] = frames
            caption_map[scene["id"]] = captions(scene.get("caption") or scene["narration"], frames / plan["fps"])
            print(f"[{scene_index + 1}/{len(plan['scenes'])}] {scene['id']} {frames / plan['fps']:.2f}s")
        plan.setdefault("voice", {})
        plan["voice"].update({
            "provider": "fish-audio",
            "mode": "continuous",
            "fullAudio": "audio/narration.mp3",
            "voiceId": reference_id or "default",
            "voiceName": reference_id or "Fish Audio default voice",
            "modelId": args.model,
        })
    else:
        for scene_index, scene in enumerate(plan["scenes"]):
            try:
                audio = synthesize(
                    key,
                    scene["narration"],
                    model=args.model,
                    reference_id=reference_id,
                    speed=args.speed,
                    volume=args.volume,
                    latency=args.latency,
                )
            except urllib.error.HTTPError as error:
                raise SystemExit(f"Fish Audio scene {scene.get('id', scene_index + 1)}: {friendly_http_error(error)}") from error
            audio_path = audio_dir / f"{scene['id']}.mp3"
            audio_path.write_bytes(audio)
            seconds = duration(audio_path)
            scene["audio"] = f"audio/{scene['id']}.mp3"
            scene["audioDurationSeconds"] = round(seconds, 3)
            scene["durationInFrames"] = max(1, round((seconds + 0.6) * plan["fps"]))
            caption_map[scene["id"]] = captions(scene.get("caption") or scene["narration"], seconds)
            print(f"[{scene_index + 1}/{len(plan['scenes'])}] {scene['id']} {seconds:.2f}s")

        plan.setdefault("voice", {})
        plan["voice"].update({
            "provider": "fish-audio",
            "mode": "segmented",
            "voiceId": reference_id or "default",
            "voiceName": reference_id or "Fish Audio default voice",
            "modelId": args.model,
        })
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (plan_path.parent / "captions.json").write_text(json.dumps(caption_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Voice: Fish Audio {reference_id or 'default'} ({args.model})")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
