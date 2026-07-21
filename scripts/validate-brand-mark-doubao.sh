#!/usr/bin/env bash
# brand_mark · doubao-local 完整验证（合约 + 资产 + 协议 + 隐私）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOUBAO="$ROOT/.temp/brand-mark-enrollment/doubao-local"
CORE="$ROOT/scene-skill-core"
MARK="$CORE/ip-profiles/mark-demo"
FAIL=0

ok() { echo "  ✓ $1"; }
err() { echo "  ✗ $1"; FAIL=1; }

echo "== brand_mark · doubao-local 完整验证 =="
echo "ROOT: $ROOT"
echo

echo "[1] Profile Contract"
for f in profile.md character.md enrollment-card.md README.md RUN-LOG.md; do
  [[ -f "$DOUBAO/$f" ]] && ok "$f" || err "缺失 $DOUBAO/$f"
done
grep -q "identity_sheet" "$DOUBAO/profile.md" && ok "profile 含 identity_sheet" || err "profile 缺 identity_sheet"
grep -q "status: AVAILABLE" "$DOUBAO/profile.md" && ok "status AVAILABLE" || err "status 非 AVAILABLE"
grep -q "input_kind: brand_mark" "$DOUBAO/profile.md" && ok "input_kind brand_mark" || err "input_kind 错误"
grep -q "ref_mode: dual" "$DOUBAO/profile.md" && ok "ref_mode dual" || err "ref_mode 非 dual"

echo
echo "[2] 三层参考 + Layer 4"
for f in \
  assets/reference/doubao-app-icon.png \
  assets/examples/00-identity-sheet.png \
  assets/examples/01-handdrawn-calibration.png \
  assets/examples/02-physical-scene.png \
  assets/examples/03-action-library.png \
  assets/examples/04-content-demo-handdrawn.png
do
  if [[ -f "$DOUBAO/$f" ]]; then
    ok "$f"
  else
    err "缺失 $DOUBAO/$f"
  fi
done

echo
echo "[3] 协议与 QA 引用"
for f in \
  references/brand-mark-mode.md \
  references/contracts/profile-contract.md \
  references/handdrawn-qa-checklist.md \
  references/physical-qa-checklist.md \
  references/common-prompt-slots.md
do
  [[ -f "$CORE/$f" ]] && ok "$f" || err "缺失 $CORE/$f"
done
grep -q "identity_sheet" "$CORE/references/contracts/profile-contract.md" && ok "profile-contract identity_sheet 门禁" || err "profile-contract 缺 identity_sheet"
grep -q "brand_mark" "$CORE/references/handdrawn-qa-checklist.md" && ok "handdrawn-qa brand_mark 块" || err "handdrawn-qa 缺 brand_mark"
grep -q "brand_mark" "$CORE/references/physical-qa-checklist.md" && ok "physical-qa brand_mark 块" || err "physical-qa 缺 brand_mark"

echo
echo "[4] Evals"
python3 -c "
import json, sys
d=json.load(open('$CORE/evals/evals.json'))
ids=[e['id'] for e in d['evals']]
need=[
  'profile-enrollment-brand-mark',
  'profile-enrollment-brand-mark-no-icon-head',
  'profile-enrollment-brand-mark-identity-sheet',
  'profile-enrollment-brand-mark-no-default-ip',
  'profile-enrollment-brand-mark-gate-before-task',
]
for n in need:
    assert n in ids, f'missing eval: {n}'
print('  ✓ brand_mark evals present (total', len(d['evals']), ')')
" || FAIL=1

echo
echo "[5] 隐私边界"
if grep -rq "doubao" "$MARK/" 2>/dev/null; then
  err "mark-demo 含 doubao 引用（泄漏风险）"
else
  ok "mark-demo 无 doubao 泄漏"
fi
[[ -f "$MARK/assets/examples/00-identity-sheet.png" ]] && ok "mark-demo 公开 Layer2 独立" || err "mark-demo 缺 Layer2"

echo
echo "[6] 正文验证批（可选）"
VAL="$ROOT/.validation-output/brand-mark-doubao/generation"
if [[ -d "$VAL" ]]; then
  for f in 01-workflow-loop.png 02-goal-backward-design.png 03-failure-comparison.png 04-feedback-iteration.png; do
    [[ -f "$VAL/$f" ]] && ok "validation/$f" || err "缺失 validation/$f"
  done
else
  echo "  · 跳过（未跑正文 4 张批）"
fi

echo
if [[ $FAIL -eq 0 ]]; then
  echo "== 结果：PASS =="
else
  echo "== 结果：FAIL =="
fi
exit $FAIL
