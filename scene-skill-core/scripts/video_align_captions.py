#!/usr/bin/env python3
"""Align Remotion captions.json to final narration audio.

Timing sources (inspired by limin112/min-skill explain-video):

1. **scripted** (default / recommended) — known narration text stretched across
   measured audio by CJK character weight. Do NOT ASR your own script; Whisper
   only adds transcription errors when the text is already known.
2. whisper-api / whisper-local — optional when you need ASR on unknown audio
3. estimated — legacy alias of scripted (kept for CLI compat); delivery gate
   treats scripted as shippable, estimated as draft-only

Audio duration is the master clock: scene frame budgets are scaled to the
probed narration length, never the other way around.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

SENT_END = "。！？；;!?"
CLAUSE_END = "，,、:：—"


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


def duration_seconds(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def glyph_weight(text: str) -> float:
    """Spoken/visual weight: CJK glyph = 1, latin/digit = 0.5 (min-skill build_srt)."""
    weight = 0.0
    for ch in text:
        if "\u2e80" <= ch <= "\u9fff" or "\u3000" <= ch <= "\u303f":
            weight += 1.0
        elif ch.isspace():
            continue
        else:
            weight += 0.5
    return max(weight, 1.0)


def split_units(para: str) -> list[str]:
    sents = [s.strip() for s in re.split(rf"(?<=[{re.escape(SENT_END)}])", para) if s.strip()]
    units: list[str] = []
    for sent in sents:
        parts = [p.strip() for p in re.split(rf"(?<=[{re.escape(CLAUSE_END)}])", sent) if p.strip()]
        units.extend(parts or [sent])
    return units or [para.strip()]


def chunk_text(text: str, max_w: float = 18.0) -> list[str]:
    """Break narration into short on-screen cues."""
    text = text.strip()
    if not text:
        return [""]
    if glyph_weight(text) <= max_w:
        return [text]
    out: list[str] = []
    buf = ""
    for unit in split_units(text):
        if not buf:
            buf = unit
        elif glyph_weight(buf) + glyph_weight(unit) <= max_w:
            buf += unit
        else:
            out.append(buf)
            buf = unit
        if buf and buf[-1] in SENT_END and glyph_weight(buf) >= max_w * 0.45:
            out.append(buf)
            buf = ""
    if buf:
        out.append(buf)
    return out or [text]


def weighted_captions(text: str, start_s: float, end_s: float, max_w: float = 18.0) -> list[dict[str, Any]]:
    chunks = [c for c in chunk_text(text, max_w=max_w) if c.strip()]
    if not chunks:
        chunks = [text.strip() or ""]
    weights = [glyph_weight(part) for part in chunks]
    total = sum(weights) or 1.0
    span = max(0.01, end_s - start_s)
    cursor = start_s
    out: list[dict[str, Any]] = []
    for index, (part, weight) in enumerate(zip(chunks, weights)):
        next_cursor = end_s if index == len(chunks) - 1 else cursor + span * weight / total
        # Keep cues readable: minimum ~0.7s except final clip.
        if index < len(chunks) - 1 and (next_cursor - cursor) < 0.7:
            next_cursor = min(end_s, cursor + 0.7)
        out.append(
            {
                "text": part,
                "startMs": round(cursor * 1000),
                "endMs": round(next_cursor * 1000),
                "timestampMs": None,
                "confidence": None,
            }
        )
        cursor = next_cursor
    if out:
        out[-1]["endMs"] = round(end_s * 1000)
    return out


def scene_boundaries(plan: dict[str, Any], total_seconds: float) -> list[tuple[float, float]]:
    """Map composition frames onto real audio length (audio = master clock)."""
    scenes = plan["scenes"]
    fps = float(plan.get("fps", 30))
    frames = [max(1, int(s.get("durationInFrames") or round(fps * 7))) for s in scenes]
    total_frames = sum(frames)
    scale = total_seconds / (total_frames / fps) if total_frames else 1.0
    boundaries: list[tuple[float, float]] = []
    cursor = 0.0
    for index, frame_count in enumerate(frames):
        span = (frame_count / fps) * scale
        end = total_seconds if index == len(frames) - 1 else min(total_seconds, cursor + span)
        boundaries.append((cursor, end))
        cursor = end
    return boundaries


def whisper_api_segments(audio: Path, language: str = "zh") -> list[dict[str, Any]]:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY missing")
    boundary = "----CodexFormBoundary7MA4YWxkTrZu0gW"
    body = bytearray()
    fields = {
        "model": "whisper-1",
        "response_format": "verbose_json",
        "language": language,
        "timestamp_granularities[]": "segment",
    }
    for name, value in fields.items():
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(f'Content-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode())
    data = audio.read_bytes()
    body.extend(f"--{boundary}\r\n".encode())
    body.extend(
        f'Content-Disposition: form-data; name="file"; filename="{audio.name}"\r\n'
        f"Content-Type: audio/mpeg\r\n\r\n".encode()
    )
    body.extend(data)
    body.extend(b"\r\n")
    body.extend(f"--{boundary}--\r\n".encode())
    request = urllib.request.Request(
        "https://api.openai.com/v1/audio/transcriptions",
        data=bytes(body),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"Whisper API HTTP {error.code}: {detail}") from error
    return payload.get("segments") or []


def local_whisper_segments(audio: Path, language: str = "zh") -> list[dict[str, Any]]:
    whisper = shutil.which("whisper")
    if not whisper:
        raise RuntimeError("whisper CLI not found")
    out_dir = audio.parent / "_whisper_tmp"
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [whisper, str(audio), "--model", "base", "--language", language, "--output_format", "json", "--output_dir", str(out_dir)],
        check=True,
    )
    json_path = out_dir / f"{audio.stem}.json"
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    return payload.get("segments") or []


def map_segments_to_scenes(
    plan: dict[str, Any],
    segments: list[dict[str, Any]],
    boundaries: list[tuple[float, float]],
) -> dict[str, list[dict[str, Any]]]:
    """Build scene-local caption maps (0-based ms within each Remotion Sequence)."""
    caption_map: dict[str, list[dict[str, Any]]] = {}
    for scene, (start_s, end_s) in zip(plan["scenes"], boundaries):
        local: list[dict[str, Any]] = []
        for seg in segments:
            seg_start = float(seg.get("start", 0))
            seg_end = float(seg.get("end", seg_start))
            if seg_end <= start_s or seg_start >= end_s:
                continue
            text = str(seg.get("text", "")).strip()
            if not text:
                continue
            clipped_start = max(start_s, seg_start)
            clipped_end = min(end_s, seg_end)
            local.append(
                {
                    "text": text,
                    "startMs": round((clipped_start - start_s) * 1000),
                    "endMs": round((clipped_end - start_s) * 1000),
                    "timestampMs": None,
                    "confidence": seg.get("avg_logprob"),
                }
            )
        if not local:
            local = weighted_captions(scene["narration"], 0.0, end_s - start_s)
        caption_map[scene["id"]] = local
    return caption_map


def scripted_caption_map(plan: dict[str, Any], boundaries: list[tuple[float, float]]) -> dict[str, list[dict[str, Any]]]:
    """Known narration × measured audio (min-skill: do not ASR your own script)."""
    caption_map: dict[str, list[dict[str, Any]]] = {}
    for scene, (start_s, end_s) in zip(plan["scenes"], boundaries):
        narration = str(scene.get("narration") or scene.get("caption") or "").strip()
        caption_map[scene["id"]] = weighted_captions(narration, 0.0, end_s - start_s)
    return caption_map


def update_job_state(project: Path, timing_source: str) -> None:
    state_path = project / "work" / "job-state.json"
    if not state_path.exists():
        return
    state = json.loads(state_path.read_text(encoding="utf-8-sig"))
    state.setdefault("captions", {})["timing_source"] = timing_source
    state.setdefault("captions", {})["path"] = "src/generated/captions.json"
    state.setdefault("status", {})["captions"] = "pass"
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--audio", type=Path, help="default: public/audio/narration.mp3")
    parser.add_argument(
        "--mode",
        choices=("auto", "scripted", "whisper-api", "whisper-local", "estimated"),
        default="auto",
        help="auto→scripted (recommended). Whisper only when ASR is needed.",
    )
    args = parser.parse_args()

    project = args.project.resolve()
    load_env(project)
    plan_path = project / "src" / "generated" / "plan.json"
    if not plan_path.exists():
        raise SystemExit(f"missing plan: {plan_path}")
    plan = json.loads(plan_path.read_text(encoding="utf-8-sig"))
    audio = args.audio or (project / "public" / "audio" / "narration.mp3")
    if not audio.exists():
        raise SystemExit(f"missing audio: {audio}")

    total_seconds = duration_seconds(audio)
    boundaries = scene_boundaries(plan, total_seconds)

    mode = args.mode
    if mode == "auto":
        mode = "scripted"
    if mode == "estimated":
        # Legacy name; same algorithm as scripted but tagged draft for old callers.
        mode = "scripted"
        tag_as_estimated = True
    else:
        tag_as_estimated = False

    if mode == "whisper-api":
        segments = whisper_api_segments(audio)
        caption_map = map_segments_to_scenes(plan, segments, boundaries)
        timing_source = "whisper-api"
    elif mode == "whisper-local":
        segments = local_whisper_segments(audio)
        caption_map = map_segments_to_scenes(plan, segments, boundaries)
        timing_source = "whisper-local"
    else:
        caption_map = scripted_caption_map(plan, boundaries)
        timing_source = "estimated" if tag_as_estimated else "scripted"

    out = project / "src" / "generated" / "captions.json"
    out.write_text(json.dumps(caption_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    meta = {
        "timing_source": timing_source,
        "audio": str(audio),
        "audio_duration_seconds": round(total_seconds, 3),
        "scenes": len(plan["scenes"]),
        "captions_path": str(out),
        "note": "scripted = known narration × measured audio (min-skill); prefer over Whisper for own TTS",
    }
    (project / "src" / "generated" / "captions-meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    update_job_state(project, timing_source)
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
