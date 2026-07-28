#!/usr/bin/env python3
"""Delivery gate for Little Stone Remotion videos (rachel + rnskill inspired)."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any, Optional


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--video", type=Path, help="default: out/video.mp4")
    parser.add_argument("--allow-estimated", action="store_true", help="allow captions timing_source=estimated")
    parser.add_argument("--allow-unapproved", action="store_true", help="skip approved_by_user gate")
    args = parser.parse_args()

    project = args.project.resolve()
    video = args.video or (project / "out" / "video.mp4")
    plan_path = project / "src" / "generated" / "plan.json"
    captions_meta = project / "src" / "generated" / "captions-meta.json"
    state_path = project / "work" / "job-state.json"
    issues: list[str] = []

    if not plan_path.exists():
        issues.append(f"missing plan: {plan_path}")
        plan = None
    else:
        plan = load_json(plan_path)

    if not video.exists() or video.stat().st_size < 10000:
        issues.append(f"video missing or too small: {video}")
    else:
        ffprobe = shutil.which("ffprobe")
        if not ffprobe:
            issues.append("ffprobe not found")
        else:
            info = json.loads(
                subprocess.check_output(
                    [ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)],
                    text=True,
                )
            )
            streams = info.get("streams") or []
            v = next((s for s in streams if s.get("codec_type") == "video"), None)
            a = next((s for s in streams if s.get("codec_type") == "audio"), None)
            if not v:
                issues.append("missing video stream")
            if not a:
                issues.append("missing audio stream")
            if v and v.get("codec_name") != "h264":
                issues.append(f"video codec must be h264, got {v.get('codec_name')}")
            if a and a.get("codec_name") != "aac":
                issues.append(f"audio codec must be aac, got {a.get('codec_name')}")
            if plan and v and (int(v["width"]), int(v["height"])) != (int(plan["width"]), int(plan["height"])):
                issues.append("wrong dimensions")
            if plan:
                expected = sum(int(s["durationInFrames"]) for s in plan["scenes"]) / int(plan["fps"])
                actual = float(info["format"]["duration"])
                if abs(actual - expected) > 0.35:
                    issues.append(f"duration mismatch: expected {expected:.2f}s, got {actual:.2f}s")
            narration = project / "public" / (plan or {}).get("voice", {}).get("fullAudio", "audio/narration.mp3")
            if not narration.is_absolute():
                narration = project / "public" / Path((plan or {}).get("voice", {}).get("fullAudio", "audio/narration.mp3"))
            audio_secs = duration_seconds(narration)
            video_secs = float(info["format"]["duration"]) if info.get("format") else None
            if audio_secs and video_secs and video_secs < audio_secs - 0.25:
                issues.append("video cuts narration audio tail")

    timing_source = None
    if captions_meta.exists():
        timing_source = load_json(captions_meta).get("timing_source")
    elif state_path.exists():
        timing_source = load_json(state_path).get("captions", {}).get("timing_source")

    if timing_source is None:
        issues.append("captions timing_source missing — run video_align_captions.py")
    elif timing_source == "estimated" and not args.allow_estimated:
        issues.append("captions timing_source=estimated is draft-only; use --mode scripted (default) or whisper, or pass --allow-estimated")

    if state_path.exists():
        state = load_json(state_path)
        # Refresh content-bound approvals (lingjian-style: change → stale).
        import importlib.util

        approve_path = Path(__file__).with_name("video_approve.py")
        spec = importlib.util.spec_from_file_location("video_approve", approve_path)
        mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
        assert spec and spec.loader
        spec.loader.exec_module(mod)
        if plan:
            notes = mod.refresh_staleness(project, state, plan)
            if notes:
                state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                for note in notes:
                    if "stale" in note and not args.allow_unapproved:
                        issues.append(note)

        gates = state.get("gates") or {}
        preview_gate = gates.get("preview") or {}
        approved = bool(state.get("status", {}).get("approved_by_user")) or preview_gate.get("status") == "approved"
        if preview_gate.get("status") == "stale":
            approved = False
        if not approved and not args.allow_unapproved:
            issues.append("job-state preview gate not approved (or stale) — re-run video_approve.py --gate preview")
        if state.get("status", {}).get("preflight") == "fail":
            issues.append("preflight previously failed")
        g1 = (gates.get("storyboard") or {}).get("status")
        if g1 == "stale":
            issues.append("gate1 storyboard stale — plan changed after approval")
    else:
        issues.append("missing work/job-state.json — run video_init_job_state.py")

    if not (project / "src" / "generated" / "captions.json").exists():
        issues.append("missing captions.json")

    thesis = ((plan or {}).get("motion") or {}).get("thesis") if plan else None
    if plan and not str(thesis or "").strip():
        issues.append("plan.motion.thesis missing")

    ok = not issues
    if state_path.exists() and ok:
        state = load_json(state_path)
        state.setdefault("status", {})["final"] = "pass"
        try:
            rel = str(video.relative_to(project))
        except ValueError:
            rel = str(video)
        state.setdefault("outputs", {})["final_video"] = rel
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "ok": ok,
        "project": str(project),
        "video": str(video),
        "timing_source": timing_source,
        "issues": issues,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
