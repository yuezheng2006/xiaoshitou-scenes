#!/usr/bin/env python3
import argparse, json, shutil, subprocess, wave
from pathlib import Path

def audio_duration(path, ffprobe):
    if path.suffix.lower() == ".wav":
        with wave.open(str(path), "rb") as source:
            return source.getnframes() / source.getframerate()
    raw = subprocess.check_output(
        [ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        text=True,
        encoding="utf-8",
    )
    return float(raw.strip())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("video",type=Path); ap.add_argument("--plan",required=True,type=Path); args=ap.parse_args()
    if not args.video.exists() or args.video.stat().st_size < 10000: raise SystemExit("Video missing or too small")
    ffprobe=shutil.which("ffprobe");
    if not ffprobe: raise SystemExit("ffprobe not found")
    raw=subprocess.check_output([ffprobe,"-v","error","-show_streams","-show_format","-of","json",str(args.video)],text=True,encoding="utf-8")
    info=json.loads(raw); plan=json.loads(args.plan.read_text(encoding="utf-8")); streams=info["streams"]
    video=next((s for s in streams if s["codec_type"]=="video"),None); audio=next((s for s in streams if s["codec_type"]=="audio"),None)
    errors=[]
    if not video: errors.append("missing video stream")
    if not audio: errors.append("missing audio stream")
    if video and video.get("codec_name") != "h264": errors.append(f"video codec must be h264, got {video.get('codec_name')}")
    if audio and audio.get("codec_name") != "aac": errors.append(f"audio codec must be aac, got {audio.get('codec_name')}")
    if video and (int(video["width"]),int(video["height"])) != (int(plan["width"]),int(plan["height"])): errors.append("wrong dimensions")
    if video:
        num,den=map(int,video.get("avg_frame_rate","0/1").split("/")); actual_fps=num/den if den else 0
        if abs(actual_fps-float(plan["fps"])) > .01: errors.append(f"wrong FPS: {actual_fps}")
    expected=sum(int(s["durationInFrames"]) for s in plan["scenes"])/int(plan["fps"])
    actual=float(info["format"]["duration"])
    if abs(actual-expected) > .2: errors.append(f"duration mismatch: expected {expected:.2f}s, got {actual:.2f}s")
    project=args.plan.resolve().parents[2]
    full_audio=plan.get("voice",{}).get("fullAudio")
    if full_audio:
        wav=project/"public"/full_audio
        if not wav.exists():
            errors.append(f"missing full narration audio: {wav}")
        else:
            seconds=audio_duration(wav, ffprobe)
            if actual < seconds-.2: errors.append("video cuts full narration audio tail")
    else:
        for scene in plan["scenes"]:
            if not scene.get("audio"):
                errors.append(f"missing scene audio field: {scene['id']}")
                continue
            wav=project/"public"/scene["audio"]
            if not wav.exists(): errors.append(f"missing scene audio: {wav}"); continue
            seconds=audio_duration(wav, ffprobe)
            scene_seconds=int(scene["durationInFrames"])/int(plan["fps"])
            if scene_seconds < seconds+.45: errors.append(f"scene {scene['id']} cuts audio tail")
    if errors: raise SystemExit("Verification failed:\n- " + "\n- ".join(errors))
    print(f"PASS {args.video} {actual:.2f}s {video['width']}x{video['height']} {video['codec_name']}+{audio['codec_name']}")

if __name__=="__main__": main()
