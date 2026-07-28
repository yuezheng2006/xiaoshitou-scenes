#!/usr/bin/env bash
# Low-cost setup gate for Little Stone long-form video (gbro/lingjian inspired).
# Report only missing items. Exit 0 when ready for Gate 1 storyboard.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "$HERE/.." && pwd)"
PROJECT="${1:-.}"
PROJECT="$(cd "$PROJECT" 2>/dev/null && pwd)" || PROJECT=""

missing=0
ok() { printf '  ✓ %s\n' "$1"; }
bad() { printf '  ✗ %s\n' "$1"; missing=$((missing + 1)); }

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

# Fish key: env or project .env — never print the key
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
if [[ $fish_ok == 1 ]]; then ok "Fish Audio API key detectable"; else bad "Fish Audio API key not found (set FISH_AUDIO_API_KEY or project .env)"; fi

echo
if [[ $missing -eq 0 ]]; then
  echo "setup PASS — proceed to Gate 1 storyboard (no imagen yet)"
  exit 0
fi
echo "setup FAIL — $missing item(s). Fix before paid imagen / Fish TTS."
exit 1
