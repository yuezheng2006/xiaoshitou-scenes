#!/usr/bin/env bash
# Low-cost setup gate for Little Stone long-form video (gbro/lingjian inspired).
# Report only missing items. Exit 0 when ready for Gate 1 storyboard.
# TTS is provider-swappable (VIDEO_TTS_PROVIDER / plan.voice.provider).
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "$HERE/.." && pwd)"
PROJECT="${1:-.}"
PROJECT="$(cd "$PROJECT" 2>/dev/null && pwd)" || PROJECT=""

missing=0
ok() { printf '  ✓ %s\n' "$1"; }
bad() { printf '  ✗ %s\n' "$1"; missing=$((missing + 1)); }
note() { printf '  · %s\n' "$1"; }

echo "=== video_check_setup (long-form · low-cost · high-IP) ==="

if command -v python3 >/dev/null 2>&1; then ok "python3 $(python3 -V 2>&1 | awk '{print $2}')"; else bad "python3 missing"; fi
if command -v ffmpeg >/dev/null 2>&1; then ok "ffmpeg"; else bad "ffmpeg missing (brew install ffmpeg)"; fi
if command -v ffprobe >/dev/null 2>&1; then ok "ffprobe"; else bad "ffprobe missing"; fi
if command -v node >/dev/null 2>&1; then ok "node $(node -v)"; else bad "node missing (Remotion render)"; fi
if command -v npm >/dev/null 2>&1; then ok "npm"; else bad "npm missing"; fi

if [[ -d "$SKILL_ROOT/assets/remotion-template" ]]; then
  ok "remotion-template present"
else
  bad "missing assets/remotion-template under skill"
fi

# Resolve TTS provider without printing secrets
provider="${VIDEO_TTS_PROVIDER:-}"
if [[ -z "$provider" && -n "$PROJECT" && -f "$PROJECT/src/generated/plan.json" ]]; then
  provider="$(python3 -c "import json,sys; p=json.load(open(sys.argv[1],encoding='utf-8-sig')); print((p.get('voice') or {}).get('provider') or '')" "$PROJECT/src/generated/plan.json" 2>/dev/null || true)"
fi
provider="$(printf '%s' "${provider:-fish-audio}" | tr '[:upper:]' '[:lower:]')"

fish_ok=0
if [[ -n "${FISH_AUDIO_API_KEY:-}" || -n "${FISH_API_KEY:-}" ]]; then
  fish_ok=1
fi
if [[ -n "$PROJECT" ]]; then
  for envf in "$PROJECT/.env" "$PROJECT/../.env"; do
    if [[ -f "$envf" ]] && grep -Eq '^(FISH_AUDIO_API_KEY|FISH_API_KEY)=' "$envf"; then
      fish_ok=1
    fi
  done
fi

case "$provider" in
  fish-audio)
    if [[ $fish_ok == 1 ]]; then ok "TTS provider=fish-audio (API key detectable)"; else bad "TTS provider=fish-audio but key missing (FISH_AUDIO_API_KEY or FISH_API_KEY)"; fi
    ;;
  external)
    ok "TTS provider=external (bring audio later: python scripts/video_tts.py --provider external --audio …)"
    ;;
  elevenlabs)
    bad "TTS provider=elevenlabs is typed but not shipped — use fish-audio or external via video_tts.py"
    ;;
  *)
    bad "unknown VIDEO_TTS_PROVIDER=$provider (want: fish-audio | external | elevenlabs)"
    ;;
esac

if [[ -f "$HERE/video_tts.py" ]]; then
  ok "video_tts.py router present"
else
  note "video_tts.py missing — call provider scripts directly"
fi

echo
if [[ $missing -eq 0 ]]; then
  echo "setup PASS — proceed to Gate 1 storyboard (no imagen yet)"
  exit 0
fi
echo "setup FAIL — $missing item(s). Fix before paid imagen / TTS."
exit 1
