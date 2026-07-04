#!/usr/bin/env bash
# 本地 Skill 结构验证：引用链、资产、双 IP eval 映射
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CORE="$ROOT/scene-skill-core"
PROFILE="$CORE/ip-profiles/default-little-stone"
FAIL=0

ok() { echo "  ✓ $1"; }
err() { echo "  ✗ $1"; FAIL=1; }

echo "== scene-skill-core 本地验证 =="
echo "ROOT: $ROOT"
echo

echo "[1] 核心入口"
for f in \
  "$CORE/SKILL.md" \
  "$CORE/README.md" \
  "$PROFILE/profile.md" \
  "$PROFILE/character.md" \
  "$PROFILE/persona-author.md" \
  "$PROFILE/persona-author-identity.md" \
  "$PROFILE/persona-author-assets.md" \
  "$PROFILE/persona-author-modes.md" \
  "$PROFILE/persona-author-prompts.md" \
  "$CORE/references/persona-scene-patterns.md" \
  "$CORE/references/common-persona-routing.md" \
  "$CORE/references/knowledge-card-mode.md" \
  "$CORE/references/handdrawn-composition-patterns.md" \
  "$CORE/evals/evals.json"
do
  [[ -f "$f" ]] && ok "$(basename "$f")" || err "缺失: $f"
done

echo
echo "[2] 角色资产 PNG"
for f in \
  "$PROFILE/assets/character/primary-character-reference.png" \
  "$PROFILE/assets/character/primary-character-actions.png" \
  "$PROFILE/assets/persona/author-persona-spec.png" \
  "$PROFILE/assets/persona/author-persona-actions.png" \
  "$PROFILE/assets/persona/author-persona-handdrawn.png"
do
  if [[ -f "$f" ]]; then
    size=$(wc -c < "$f" | tr -d ' ')
    ok "$(basename "$f") (${size} bytes)"
  else
    err "缺失: $f"
  fi
done

echo
echo "[3] 母版 01-06"
for i in 01 02 03 04 05 06; do
  f="$CORE/assets/masters/${i}"*.png
  ls $f >/dev/null 2>&1 && ok "masters/${i}-*.png" || err "缺失母版: $i"
done

echo
echo "[4] 双 IP 三条试跑 prompt → 应对 eval / 读取链"
declare -A PROMPTS
PROMPTS[1]="老杨：这篇 2000 字长文讲 Agent 工作流设计，想配图，请先推荐。"
PROMPTS[2]="老杨：把下面三步 onboarding 流程做成 4:5 收藏知识卡。\\n1. 读文档 2. 跑第一个例子 3. 提交反馈"
PROMPTS[3]="老杨和小石头：解释这个 Agent 工作流，出一张 16:9 白板图。"

declare -A EVAL_IDS
EVAL_IDS[1]="dual-ip-recommendation"
EVAL_IDS[2]="knowledge-card-dual-ip"
EVAL_IDS[3]="author-handdrawn-asset-routing"

for i in 1 2 3; do
  echo "  --- Prompt $i ---"
  echo "  ${PROMPTS[$i]}"
  eid="${EVAL_IDS[$i]}"
  if python3 -c "
import json, sys
data=json.load(open('$CORE/evals/evals.json'))
m=[e for e in data['evals'] if e['id']=='$eid']
sys.exit(0 if m else 1)
"; then
    ok "eval 用例存在: $eid"
  else
    err "eval 用例缺失: $eid"
  fi
done

echo
echo "[5] persona 触发词在 SKILL.md / profile.md 一致"
for kw in "老杨" "yuezheng2006" "老杨和小石头" "老杨 IP 图解"; do
  grep -q "$kw" "$CORE/SKILL.md" && grep -q "$kw" "$PROFILE/profile.md" \
    && ok "触发词: $kw" || err "触发词不一致或缺失: $kw"
done

echo
echo "[6] Codex 安装路径探测"
CODEX_SKILLS="${CODEX_HOME:-$HOME/.codex}/skills"
TARGET="$CODEX_SKILLS/scene-skill-core"
if [[ -d "$TARGET" ]]; then
  if [[ "$TARGET" -ef "$CORE" ]] || diff -q "$TARGET/SKILL.md" "$CORE/SKILL.md" >/dev/null 2>&1; then
    ok "已安装到 $TARGET 且 SKILL.md 一致"
  else
    echo "  ⚠ 已安装但版本可能旧: $TARGET"
    echo "    建议: cp -R '$CORE' '$CODEX_SKILLS/'"
  fi
else
  echo "  ⚠ 未安装到 Codex skills 目录"
  echo "    安装: cp -R '$CORE' '$CODEX_SKILLS/'"
fi

echo
echo "[7] Codex CLI 双 IP 试跑（可选，需 codex 已登录）"
OUT_DIR="$ROOT/.validation-output"
mkdir -p "$OUT_DIR"
if command -v codex >/dev/null 2>&1; then
  run_codex() {
    local id="$1" prompt="$2"
    echo "  运行 $id ..."
    if codex exec -C "$ROOT" -s workspace-write --ephemeral \
      -o "$OUT_DIR/${id}.txt" "$prompt" < /dev/null >/dev/null 2>&1; then
      ok "$id → $OUT_DIR/${id}.txt"
    else
      err "$id codex exec 失败（检查登录: codex login）"
    fi
  }
  if [[ "${RUN_CODEX:-}" == "1" ]]; then
    run_codex "prompt1" 'Use $scene-skill-core。老杨：这篇 2000 字长文讲 Agent 工作流设计，想配图，请先推荐。不要生图，只输出双 IP 出图方案推荐。'
  else
    echo "  跳过（结构验证通过后，运行: RUN_CODEX=1 bash scripts/validate-skill-local.sh）"
    echo "  注意: codex exec 必须加 < /dev/null，否则会卡在 Reading additional input from stdin"
  fi
else
  echo "  跳过（未安装 codex CLI）"
fi

echo
if [[ $FAIL -eq 0 ]]; then
  echo "== 结构验证通过 =="
  exit 0
else
  echo "== 结构验证失败 =="
  exit 1
fi
