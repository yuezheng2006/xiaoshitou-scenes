#!/usr/bin/env python3
"""Approve / invalidate video gates with content-bound hashes (lingjian-inspired).

Gates (long-form · low-cost · high-IP):
  storyboard  Gate 1 — plan thesis + scene cards (before imagen)
  stills      Gate 2 — scene PNGs / contact sheet (partial pass allowed)
  preview     Gate 3 — Remotion still + plan+captions+audio fingerprint

Approval is bound to an artifact hash. If plan/images/captions change, status
becomes stale and delivery fails until re-approved (no silent --force).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def storyboard_fingerprint(plan: dict[str, Any]) -> str:
    payload = {
        "topic": plan.get("topic"),
        "title": plan.get("title"),
        "width": plan.get("width"),
        "height": plan.get("height"),
        "motion": plan.get("motion"),
        "scenes": [
            {
                "id": s.get("id"),
                "headline": s.get("headline"),
                "narration": s.get("narration"),
                "caption": s.get("caption"),
                "stateChange": s.get("stateChange"),
                "characterAction": s.get("characterAction"),
                "narrativeJob": s.get("narrativeJob"),
            }
            for s in plan.get("scenes") or []
        ],
    }
    return sha256_text(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def stills_fingerprint(project: Path, plan: dict[str, Any], scene_ids: list[str] | None = None) -> str:
    wanted = set(scene_ids) if scene_ids else None
    parts: list[str] = []
    for scene in plan.get("scenes") or []:
        sid = scene["id"]
        if wanted is not None and sid not in wanted:
            continue
        rel = scene.get("image") or f"images/{sid}.png"
        path = project / "public" / rel
        if not path.exists():
            path = project / rel
        digest = sha256_file(path) if path.exists() else f"MISSING:{sid}"
        parts.append(f"{sid}:{digest}")
    return sha256_text("\n".join(parts))


def preview_fingerprint(project: Path, plan: dict[str, Any]) -> str:
    parts = [storyboard_fingerprint(plan), stills_fingerprint(project, plan)]
    for rel in (
        "src/generated/captions.json",
        "public/audio/narration.mp3",
        "out/preview.png",
    ):
        path = project / rel
        parts.append(f"{rel}:{sha256_file(path) if path.exists() else 'MISSING'}")
    return sha256_text("\n".join(parts))


def ensure_gates(state: dict[str, Any]) -> dict[str, Any]:
    gates = state.setdefault("gates", {})
    for name in ("storyboard", "stills", "preview"):
        gates.setdefault(
            name,
            {
                "status": "not_started",
                "approved_at": None,
                "artifact_hash": None,
                "passed_scene_ids": [],
            },
        )
    return gates


def refresh_staleness(project: Path, state: dict[str, Any], plan: dict[str, Any] | None) -> list[str]:
    """Mark approved gates stale when fingerprints drift. Returns notes."""
    notes: list[str] = []
    gates = ensure_gates(state)
    if plan is None:
        return notes

    sb = gates["storyboard"]
    if sb.get("status") == "approved" and sb.get("artifact_hash"):
        now = storyboard_fingerprint(plan)
        if now != sb["artifact_hash"]:
            sb["status"] = "stale"
            state.setdefault("status", {})["gate1_storyboard"] = "stale"
            notes.append("gate1 storyboard stale — plan changed; re-approve before imagen")

    st = gates["stills"]
    if st.get("status") == "approved" and st.get("artifact_hash"):
        ids = st.get("passed_scene_ids") or [s["id"] for s in plan.get("scenes") or []]
        now = stills_fingerprint(project, plan, ids)
        if now != st["artifact_hash"]:
            st["status"] = "stale"
            state.setdefault("status", {})["gate2_stills"] = "stale"
            notes.append("gate2 stills stale — scene images changed; re-approve contact sheet")

    pv = gates["preview"]
    if pv.get("status") == "approved" and pv.get("artifact_hash"):
        now = preview_fingerprint(project, plan)
        if now != pv["artifact_hash"]:
            pv["status"] = "stale"
            state["status"]["approved_by_user"] = False
            state.setdefault("status", {})["preview"] = "stale"
            notes.append("gate3 preview stale — plan/captions/audio/preview changed; re-approve")
    return notes


def approve(
    project: Path,
    gate: str,
    scene_ids: list[str] | None,
    plan: dict[str, Any],
    state: dict[str, Any],
) -> dict[str, Any]:
    gates = ensure_gates(state)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if gate == "storyboard":
        digest = storyboard_fingerprint(plan)
        all_ids = [s["id"] for s in plan.get("scenes") or []]
        gates["storyboard"] = {
            "status": "approved",
            "approved_at": now,
            "artifact_hash": digest,
            "passed_scene_ids": scene_ids or all_ids,
        }
        state.setdefault("status", {})["gate1_storyboard"] = "approved"
    elif gate == "stills":
        ids = scene_ids or [s["id"] for s in plan.get("scenes") or []]
        digest = stills_fingerprint(project, plan, ids)
        gates["stills"] = {
            "status": "approved",
            "approved_at": now,
            "artifact_hash": digest,
            "passed_scene_ids": ids,
        }
        state.setdefault("status", {})["gate2_stills"] = "approved"
        state.setdefault("status", {})["scenes"] = "pass" if len(ids) == len(plan.get("scenes") or []) else "partial"
    elif gate == "preview":
        digest = preview_fingerprint(project, plan)
        gates["preview"] = {
            "status": "approved",
            "approved_at": now,
            "artifact_hash": digest,
            "passed_scene_ids": [s["id"] for s in plan.get("scenes") or []],
        }
        state.setdefault("status", {})["approved_by_user"] = True
        state.setdefault("status", {})["preview"] = "approved"
    else:
        raise SystemExit(f"unknown gate: {gate}")
    return gates[gate]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--gate", choices=("storyboard", "stills", "preview"))
    parser.add_argument("--scenes", default="", help="comma scene ids for partial stills pass")
    parser.add_argument("--check", action="store_true", help="refresh stale flags only")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    state_path = project / "work" / "job-state.json"
    plan_path = project / "src" / "generated" / "plan.json"
    if not state_path.exists():
        raise SystemExit(f"missing {state_path}; run video_init_job_state.py")
    state = load_json(state_path)
    plan = load_json(plan_path) if plan_path.exists() else None

    notes = refresh_staleness(project, state, plan)
    report: dict[str, Any] = {"project": str(project), "notes": notes, "gates": ensure_gates(state)}

    if args.check:
        dump_json(state_path, state)
        report["ok"] = not any("stale" in n for n in notes)
        print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else "\n".join(notes) or "all approvals fresh")
        return 0 if report["ok"] else 1

    if not args.gate:
        raise SystemExit("pass --gate storyboard|stills|preview or --check")
    if plan is None:
        raise SystemExit(f"missing plan: {plan_path}")

    scene_ids = [s.strip() for s in args.scenes.split(",") if s.strip()] or None
    if args.gate == "stills" and scene_ids:
        known = {s["id"] for s in plan.get("scenes") or []}
        unknown = [s for s in scene_ids if s not in known]
        if unknown:
            raise SystemExit(f"unknown scene ids: {unknown}")

    entry = approve(project, args.gate, scene_ids, plan, state)
    dump_json(state_path, state)
    report["approved"] = entry
    report["ok"] = True
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
