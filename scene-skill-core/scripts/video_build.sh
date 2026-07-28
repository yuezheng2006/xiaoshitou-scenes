#!/usr/bin/env bash
# Assemble Little Stone Remotion video after plan/images/audio exist.
#
# Inspired by limin112/min-skill explain-video build_video.sh:
#   - audio duration is the master clock (align captions to probed narration)
#   - steps skip when outputs exist; use --force / --from / --only to iterate
#
# Steps: align · still · render · check
#
# Usage:
#   bash scripts/video_build.sh /path/to/remotion-project
#   bash scripts/video_build.sh . --only align,still
#   bash scripts/video_build.sh . --from render --force
#   bash scripts/video_build.sh . --allow-unapproved   # skip preview gate in check
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "$HERE/.." && pwd)"
PROJECT="${1:-}"; shift || true
[[ -n "$PROJECT" ]] || { echo "usage: video_build.sh <remotion-project-dir> [options]" >&2; exit 2; }
PROJECT="$(cd "$PROJECT" && pwd)"

# Always run setup first (cheap); fail fast on missing tools
bash "$HERE/video_check_setup.sh" "$PROJECT" || exit 1

FROM=""; ONLY=""; FORCE=0
ALLOW_ESTIMATED=0; ALLOW_UNAPPROVED=0
ALIGN_MODE="scripted"
ALL_STEPS="align still render check"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --from) FROM="$2"; shift 2 ;;
    --only) ONLY="$2"; shift 2 ;;
    --force) FORCE=1; shift ;;
    --align-mode) ALIGN_MODE="$2"; shift 2 ;;
    --allow-estimated) ALLOW_ESTIMATED=1; shift ;;
    --allow-unapproved) ALLOW_UNAPPROVED=1; shift ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

known_step() { case " $ALL_STEPS " in *" $1 "*) return 0 ;; *) return 1 ;; esac; }

if [[ -n "$ONLY" ]]; then
  ENABLED=" ${ONLY//,/ } "
elif [[ -n "$FROM" ]]; then
  known_step "$FROM" || { echo "unknown step: $FROM (want: $ALL_STEPS)" >&2; exit 2; }
  ENABLED=""; seen=0
  for s in $ALL_STEPS; do
    [[ "$s" == "$FROM" ]] && seen=1
    [[ $seen == 1 ]] && ENABLED="$ENABLED $s"
  done
  ENABLED="$ENABLED "
else
  ENABLED=" $ALL_STEPS "
fi

enabled() { case "$ENABLED" in *" $1 "*) return 0 ;; *) return 1 ;; esac; }
should_run() {
  enabled "$1" || return 1
  if [[ $FORCE == 0 && -n "${2:-}" && -e "$2" ]]; then
    echo "skip $1 ($(basename "$2") exists — pass --force to redo)"
    return 1
  fi
  echo; echo "=== $1 ==="
  return 0
}

CAPTIONS="$PROJECT/src/generated/captions.json"
STILL="$PROJECT/out/preview.png"
VIDEO="$PROJECT/out/video.mp4"
mkdir -p "$PROJECT/out"

if should_run align "$CAPTIONS"; then
  python3 "$HERE/video_align_captions.py" --project "$PROJECT" --mode "$ALIGN_MODE"
fi

if should_run still "$STILL"; then
  (cd "$PROJECT" && npm run still)
fi

if should_run render "$VIDEO"; then
  (cd "$PROJECT" && npm run render)
fi

if enabled check; then
  echo; echo "=== check ==="
  CHECK_ARGS=(--project "$PROJECT" --video "$VIDEO")
  [[ $ALLOW_ESTIMATED == 1 ]] && CHECK_ARGS+=(--allow-estimated)
  [[ $ALLOW_UNAPPROVED == 1 ]] && CHECK_ARGS+=(--allow-unapproved)
  python3 "$HERE/video_check_delivery.py" "${CHECK_ARGS[@]}"
  python3 "$HERE/video_verify_output.py" "$VIDEO" --plan "$PROJECT/src/generated/plan.json" || true
  echo "done -> $VIDEO"
fi
