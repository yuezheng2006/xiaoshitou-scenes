# 双 IP 本地验证清单

在 Codex（或已加载 `scene-skill-core` 的 Agent）里逐条粘贴下面 prompt，对照「预期行为」打勾。

先运行结构检查：

```bash
bash scripts/validate-skill-local.sh
```

用 Codex CLI 自动试跑（**必须** `< /dev/null`，否则会卡在 stdin）：

```bash
RUN_CODEX=1 bash scripts/validate-skill-local.sh

# 或单条：
codex exec -C . -s workspace-write --ephemeral \
  -o .validation-output/prompt1.txt \
  'Use $scene-skill-core。老杨：这篇 2000 字长文讲 Agent 工作流设计，想配图，请先推荐。不要生图。' \
  < /dev/null
```

Prompt 1 已通过，结果见 `.validation-output/prompt1.txt`。

安装 Skill（若尚未安装）：

```bash
cp -R ./scene-skill-core "${CODEX_HOME:-$HOME/.codex}/skills/"
```

---

## Prompt 1 — 双 IP 出图方案推荐

```text
老杨：这篇 2000 字长文讲 Agent 工作流设计，想配图，请先推荐。
```

**预期（对应 eval `dual-ip-recommendation`）**

- [ ] 识别 persona 触发（老杨）
- [ ] 读取链：`persona-author.md` → `persona-author-assets.md` → `persona-scene-patterns.md`
- [ ] 输出「双 IP 出图方案推荐」，含：视觉模式、张数、互动场景类型、老杨职责、小石头职责
- [ ] **不**逼用户先选「实物图还是手绘图」
- [ ] **不**默认只出小石头单 IP 方案
- [ ] 未要求出图时，不出 shot list 全量生成计划以外的生图 prompt

---

## Prompt 2 — 知识卡双 IP 分工

```text
老杨：把下面三步 onboarding 流程做成 4:5 收藏知识卡。
1. 读文档
2. 跑第一个例子
3. 提交反馈
```

**预期（对应 eval `knowledge-card-dual-ip`）**

- [ ] 模式 = 知识卡；尺寸 = 4:5 或 3:4
- [ ] 读取：`knowledge-card-mode.md`、`persona-author-modes.md`、`persona-author-prompts.md`（手绘系）
- [ ] 老杨 = 主讲/指向；小石头 = 2–3 个执行分工（搬卡/标风险等）
- [ ] 遵守多人差异锁（体型/姿态/分工不同）
- [ ] **不能**只有老杨 + 文字、没有小石头
- [ ] 资产：读 `author-persona-spec.png` + `author-persona-handdrawn.png`；**不**读 actions.png

---

## Prompt 3 — 手绘白板双 IP

```text
老杨和小石头：解释这个 Agent 工作流，出一张 16:9 白板图。

输入 → 检索 → 处理 → 输出
```

**预期（对应 eval `author-handdrawn-asset-routing` + 双 IP）**

- [ ] 模式 = 手绘图；结构类型 ≈ Workflow
- [ ] 读取：`handdrawn-composition-patterns.md`（双 IP 白板协作）
- [ ] 老杨画结构/批注；小石头拉线/搬模块
- [ ] 资产：spec + handdrawn；**不**读 actions；老杨 **不是** 3D 描述
- [ ] 小石头 flat 2D；结构锁定必填字段完整后再生图

---

## 反向边界（可选，30 秒）

```text
小石头手绘图：解释一下这个 Agent 工作流。
```

- [ ] **不应**出现老杨（eval `author-persona-trigger-boundary`）

---

## 记录

| Prompt | 通过 | 问题摘要 |
| --- | --- | --- |
| 1 推荐 | | |
| 2 知识卡 | | |
| 3 白板 | | |
| 反向边界 | | |
