#!/usr/bin/env python3
"""Create an editable Remotion explainer project from a UTF-8 plan."""

import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "assets" / "remotion-template"
STYLE_IDS = {
    "warm-editorial", "modern-grid", "notebook", "ink-poster",
    "watercolor-storybook", "calligraphy-scroll", "retro-newspaper",
    "chalk-classroom", "technical-blueprint", "playful-sticker",
}
MOTION_IDS = {
    "calm-explainer", "editorial-drift", "grid-scan", "notebook-flip",
    "poster-snap", "watercolor-float", "scroll-reveal", "newspaper-press",
    "chalk-write", "blueprint-scan", "sticker-pop",
}


def caption_chunks(text: str) -> list[str]:
    if len(re.sub(r"\s", "", text)) <= 24:
        return [text.strip()]
    chunks = [s.strip() for s in re.split(r"(?<=[，。！？；,.!?;])", text) if s.strip()]
    return chunks or [text.strip()]


def build_captions(text: str, duration_seconds: float) -> list[dict]:
    chunks = caption_chunks(text)
    weights = [max(1, len(re.sub(r"[，。！？；,.!?;\s]", "", part))) for part in chunks]
    total = sum(weights)
    cursor = 0.0
    captions = []
    for index, (part, weight) in enumerate(zip(chunks, weights)):
        end = duration_seconds if index == len(chunks) - 1 else cursor + duration_seconds * weight / total
        captions.append({
            "text": part,
            "startMs": round(cursor * 1000),
            "endMs": round(end * 1000),
            "timestampMs": None,
            "confidence": None,
        })
        cursor = end
    return captions


def write_script_exports(output: Path, plan: dict) -> None:
    script_dir = output / "script"
    script_dir.mkdir(parents=True, exist_ok=True)
    title = plan.get("title") or plan.get("topic") or "Hand-drawn explainer"
    voiceover = [f"# {title}", ""]
    captions = [f"# {title} - captions", ""]
    scene_plan = [f"# {title} - scene plan", ""]
    for index, scene in enumerate(plan["scenes"], 1):
        label = f"{index:02d} {scene['headline']}"
        voiceover.extend([f"## {label}", "", scene["narration"].strip(), ""])
        captions.extend([f"## {label}", "", scene.get("caption", "").strip(), ""])
        scene_plan.extend([
            f"## {label}",
            "",
            f"- Caption: {scene.get('caption', '').strip()}",
            f"- Voiceover: {scene['narration'].strip()}",
            f"- Image: {scene.get('image', '')}",
            f"- Image prompt: {scene.get('imagePrompt', '').strip()}",
            "",
        ])
    (script_dir / "voiceover-script.md").write_text("\n".join(voiceover), encoding="utf-8")
    (script_dir / "captions-script.md").write_text("\n".join(captions), encoding="utf-8")
    (script_dir / "scene-plan.md").write_text("\n".join(scene_plan), encoding="utf-8")


def normalize(plan: dict) -> dict:
    errors = []
    for key in ("topic", "title", "fps", "width", "height", "scenes"):
        if not plan.get(key):
            errors.append(f"missing {key}")
    scenes = plan.get("scenes", [])
    if not 6 <= len(scenes) <= 12:
        errors.append("scenes must contain 6-12 items")
    style = plan.setdefault("style", {})
    style.setdefault("id", "warm-editorial")
    if style["id"] not in STYLE_IDS:
        errors.append(f"unknown style.id: {style['id']}")
    motion = plan.setdefault("motion", {})
    if motion.get("id") and motion["id"] not in MOTION_IDS:
        errors.append(f"unknown motion.id: {motion['id']}")
    motion.setdefault("intensity", "medium")
    if motion["intensity"] not in {"low", "medium", "high"}:
        errors.append(f"unknown motion.intensity: {motion['intensity']}")
    plan.setdefault("language", "zh-CN")
    plan.setdefault("targetDurationSeconds", 75)
    voice = plan.setdefault("voice", {})
    voice.setdefault("provider", "elevenlabs")
    voice.setdefault("voiceId", "auto")
    voice.setdefault("voiceName", "auto")
    voice.setdefault("modelId", "eleven_multilingual_v2")
    seen = set()
    for index, scene in enumerate(scenes):
        prefix = f"scenes[{index}]"
        for key in ("id", "headline", "narration"):
            if not scene.get(key):
                errors.append(f"{prefix} missing {key}")
        scene_id = scene.get("id", "")
        if not re.fullmatch(r"[A-Za-z0-9_-]+", scene_id):
            errors.append(f"{prefix}.id is not filesystem-safe")
        if scene_id in seen:
            errors.append(f"duplicate scene id {scene_id}")
        seen.add(scene_id)
        if len(scene.get("headline", "")) > 44:
            errors.append(f"{prefix}.headline is too long")
        scene.setdefault("caption", scene.get("narration", ""))
        scene.setdefault("image", f"images/{scene_id}.png")
        scene.setdefault("imagePrompt", "")
        scene.setdefault("audio", f"audio/{scene_id}.mp3")
        scene.setdefault("accent", "#D77B55")
        scene.setdefault("durationInFrames", int(plan.get("fps", 30) * 7))
    if errors:
        raise ValueError("Invalid plan:\n- " + "\n- ".join(errors))
    return plan


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    plan = normalize(json.loads(args.plan.read_text(encoding="utf-8-sig")))
    output = args.output.resolve()
    if output.exists():
        if not args.force:
            raise SystemExit(f"Output exists: {output}; pass --force to replace it")
        protected = {Path(output.anchor).resolve(), Path.home().resolve(), ROOT.resolve()}
        recognizable = (output / ".handdrawn-explainer-project").exists() or (
            (output / "src" / "generated" / "plan.json").exists() and (output / "package.json").exists()
        )
        if output in protected or not recognizable:
            raise SystemExit(f"Refusing to replace an unrecognized or protected directory: {output}")
        shutil.rmtree(output)
    shutil.copytree(TEMPLATE, output)
    generated = output / "src" / "generated"
    generated.mkdir(parents=True, exist_ok=True)
    (generated / "plan.json").write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    captions = {}
    for scene in plan["scenes"]:
        provisional = scene["durationInFrames"] / plan["fps"]
        captions[scene["id"]] = build_captions(scene["caption"], provisional)
    (generated / "captions.json").write_text(
        json.dumps(captions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    write_script_exports(output, plan)
    for folder in ("audio", "images", "fonts"):
        (output / "public" / folder).mkdir(parents=True, exist_ok=True)
    print(output)


if __name__ == "__main__":
    main()
