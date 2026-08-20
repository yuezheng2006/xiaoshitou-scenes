#!/usr/bin/env python3
"""Validate Punk-inspired theater shape×style wiring for path C."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "ip-profiles" / "default-little-stone"
STYLES = PROFILE / "theater-styles"
SHAPES = PROFILE / "theater-shapes"
BLUEPRINT = ROOT / "references" / "theater-prompt-blueprint.md"
THEATER_MD = PROFILE / "persona-author-theater.md"
PROMPTS_MD = PROFILE / "persona-author-theater-prompts.md"
CHECKLIST = ROOT / "references" / "persona-theater-checklist.md"
GATE = ROOT.parent / ".validation-output" / "generation" / "theater" / "GATE-STATUS.md"

REQUIRED_STYLE_IDS = ["vinyl-theater"]
REQUIRED_SHAPE_IDS = ["process-breakdown", "core-action", "one-theme-two-plates"]

STYLE_META_MARKERS = [
    "style_anchors:",
    "must_preserve:",
    "avoid_when_applying_to_theater:",
    "outputs:",
]
SHAPE_META_MARKERS = [
    "shape_anchors:",
    "must_preserve:",
    "avoid_when_applying:",
    "style_id: vinyl-theater",
]
BLUEPRINT_MARKERS = [
    "Likeness Policy",
    "Style Application (vinyl-theater)",
    "Shape Application",
    "场景轻确认门",
    "Do NOT paste full article body",
]
DOC_MARKERS = [
    "theater-prompt-blueprint.md",
    "theater-styles/vinyl-theater",
    "theater-shapes/",
]


def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)


def main() -> int:
    failures: list[str] = []

    for path in [BLUEPRINT, THEATER_MD, PROMPTS_MD, CHECKLIST]:
        if not path.is_file():
            fail(f"missing file: {path.relative_to(ROOT)}", failures)

    for style_id in REQUIRED_STYLE_IDS:
        meta = STYLES / style_id / "META.md"
        style = STYLES / style_id / "STYLE.md"
        for p in (meta, style):
            if not p.is_file():
                fail(f"missing style file: {p.relative_to(ROOT)}", failures)
        if meta.is_file():
            text = meta.read_text(encoding="utf-8")
            for marker in STYLE_META_MARKERS:
                if marker not in text:
                    fail(f"{meta.relative_to(ROOT)} missing `{marker}`", failures)

    for shape_id in REQUIRED_SHAPE_IDS:
        meta = SHAPES / shape_id / "META.md"
        if not meta.is_file():
            fail(f"missing shape META: {meta.relative_to(ROOT)}", failures)
            continue
        text = meta.read_text(encoding="utf-8")
        for marker in SHAPE_META_MARKERS:
            if marker not in text:
                fail(f"{meta.relative_to(ROOT)} missing `{marker}`", failures)

    if BLUEPRINT.is_file():
        bp = BLUEPRINT.read_text(encoding="utf-8")
        for marker in BLUEPRINT_MARKERS:
            if marker not in bp:
                fail(f"blueprint missing `{marker}`", failures)

    for doc in (THEATER_MD, PROMPTS_MD, CHECKLIST):
        if not doc.is_file():
            continue
        text = doc.read_text(encoding="utf-8")
        for marker in DOC_MARKERS:
            if marker not in text:
                fail(f"{doc.relative_to(ROOT)} should reference `{marker}`", failures)

    # Gold sample paths mentioned in theater.md should exist when present
    gold = PROFILE / "assets" / "persona" / "theater"
    for name in (
        "author-persona-theater-expression-sheet.png",
        "author-persona-theater-face-lock.png",
        "author-persona-theater-sheet.png",
    ):
        p = gold / name
        if not p.is_file():
            fail(f"missing gold asset: {p.relative_to(ROOT)}", failures)

    # Gate is runtime under .validation-output/ (gitignored). Optional for repo CI;
    # when present, require a known status token.
    warnings: list[str] = []
    if GATE.is_file():
        gate = GATE.read_text(encoding="utf-8")
        if "APPROVED" not in gate and "PREVIEW" not in gate and "DRAFT" not in gate:
            fail("GATE-STATUS.md missing DRAFT|PREVIEW|APPROVED", failures)
    else:
        warnings.append(
            f"no local GATE-STATUS.md yet (ok for fresh clone): {GATE}"
        )

    # Thin consistency: prompts should not still forbid thick black frames (likeness v2)
    if PROMPTS_MD.is_file():
        prompts = PROMPTS_MD.read_text(encoding="utf-8")
        if "NO thick black/dark-brown glasses frames" in prompts:
            fail("prompts still forbid thick black glasses (conflicts likeness v2)", failures)
        if "Likeness Policy" not in prompts and "theater-prompt-blueprint" not in prompts:
            fail("prompts.md not wired to blueprint / likeness policy", failures)

    if failures:
        print("validate-theater-punk: FAIL")
        for item in failures:
            print(f"  - {item}")
        for item in warnings:
            print(f"  ! {item}")
        return 1

    print("validate-theater-punk: PASS")
    print(f"  styles={REQUIRED_STYLE_IDS}")
    print(f"  shapes={REQUIRED_SHAPE_IDS}")
    print(f"  blueprint={BLUEPRINT.relative_to(ROOT)}")
    for item in warnings:
        print(f"  ! {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
