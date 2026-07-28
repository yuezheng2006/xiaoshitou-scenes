#!/usr/bin/env python3
"""Build a numbered contact sheet from scene PNGs (gbro-inspired Gate 2 review).

Uses ffmpeg xstack (tile is single-stream only). Partial scene lists supported.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--scenes", default="", help="comma ids; default all in plan")
    parser.add_argument("--out", type=Path, help="default: out/contact-sheet.jpg")
    parser.add_argument("--cell-width", type=int, default=360)
    parser.add_argument("--cell-height", type=int, default=640)
    parser.add_argument("--cols", type=int, default=0, help="0 = auto")
    args = parser.parse_args()

    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg required")

    project = args.project.resolve()
    plan = load_json(project / "src" / "generated" / "plan.json")
    wanted = [s.strip() for s in args.scenes.split(",") if s.strip()]
    scenes = plan.get("scenes") or []
    if wanted:
        by_id = {s["id"]: s for s in scenes}
        selected = [by_id[i] for i in wanted if i in by_id]
    else:
        selected = scenes
    if not selected:
        raise SystemExit("no scenes selected")

    paths: list[Path] = []
    for scene in selected:
        rel = scene.get("image") or f"images/{scene['id']}.png"
        path = project / "public" / rel
        if not path.exists():
            path = project / rel
        if not path.exists():
            raise SystemExit(f"missing image for {scene['id']}: {path}")
        paths.append(path)

    out = (args.out or (project / "out" / "contact-sheet.jpg")).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    n = len(paths)
    cols = args.cols or (2 if n <= 2 else 3 if n <= 9 else 4)
    rows = int(math.ceil(n / cols))
    # pad with last frame if needed for full tile grid
    while len(paths) < cols * rows:
        paths.append(paths[-1])

    cmd: list[str] = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
    for path in paths:
        cmd += ["-i", str(path)]
    n_pad = len(paths)
    scales = "".join(
        f"[{i}:v]scale={args.cell_width}:{args.cell_height}:force_original_aspect_ratio=decrease,"
        f"pad={args.cell_width}:{args.cell_height}:(ow-iw)/2:(oh-ih)/2:white,setsar=1[v{i}];"
        for i in range(n_pad)
    )
    # 3x2 layout example: 0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0
    layout_parts: list[str] = []
    for i in range(n_pad):
        r, c = divmod(i, cols)
        if c == 0:
            x = "0"
        else:
            x = "+".join([f"w{j}" for j in range(c)])
        if r == 0:
            y = "0"
        else:
            y = "+".join([f"h{j * cols}" for j in range(r)])
        layout_parts.append(f"{x}_{y}")
    layout = "|".join(layout_parts)
    stack_in = "".join(f"[v{i}]" for i in range(n_pad))
    filt = f"{scales}{stack_in}xstack=inputs={n_pad}:layout={layout}:fill=white[out]"
    cmd += ["-filter_complex", filt, "-map", "[out]", "-frames:v", "1", str(out)]
    subprocess.run(cmd, check=True)

    # record in job-state if present
    state_path = project / "work" / "job-state.json"
    if state_path.exists():
        state = load_json(state_path)
        try:
            rel = str(out.relative_to(project))
        except ValueError:
            rel = str(out)
        state.setdefault("outputs", {})["contact_sheet"] = rel
        state.setdefault("gates", {}).setdefault("stills", {})["contact_sheet"] = rel
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({"ok": True, "out": str(out), "scenes": [s["id"] for s in selected], "grid": f"{cols}x{rows}"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
