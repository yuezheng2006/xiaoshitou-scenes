# 豆包 brand_mark · 本地完整验证清单

以 **豆包 App Icon** 为销售主示例，验证 `input_kind=brand_mark` 全链路。

## 一键结构检查

```bash
bash scripts/validate-brand-mark-doubao.sh
```

预期：**PASS**（合约、L1–L4 资产、协议、evals、隐私边界）

---

## 资产浏览（Enrollment）

路径：[`.temp/brand-mark-enrollment/doubao-local/`](../.temp/brand-mark-enrollment/doubao-local/)

| 看什麼 | 文件 |
| --- | --- |
| 客户输入 | `assets/reference/doubao-app-icon.png` |
| Layer 2 设定图 | `assets/examples/00-identity-sheet.png` |
| 手绘 / 实物 / 动作库 | `assets/examples/01–03` |
| 正文试跑 | `assets/examples/04-content-demo-handdrawn.png` |

---

## Agent Prompt 清单

在已加载 `scene-skill-core` 的 Agent 中逐条粘贴，对照 [`agent-routing/README.md`](../.validation-output/brand-mark-doubao/agent-routing/README.md) 打勾。

### Prompt 1 — Enrollment（不生图）

```text
用这个 App Icon 做一个自定义 IP，先建立档案，暂时不要生成配图。
```

- [ ] `input_kind=brand_mark`
- [ ] 输出 Enrollment Card
- [ ] 确认前不生图
- [ ] 不路由 default-little-stone

### Prompt 2 — 方案推荐

```text
用 doubao-local profile。这篇 2000 字长文讲 Agent 工作流设计，想配图，请先推荐。不要生图。
```

- [ ] 单 IP 豆包助手方案（非老杨双 IP）
- [ ] 引用 identity_sheet
- [ ] 含张数 + 结构 + 主动词

### Prompt 3 — 反向边界

```text
小石头手绘图：解释一下这个 Agent 工作流。
```

- [ ] 不把客户 Icon 贴小石头
- [ ] 提示 brand_mark 独立录入

### Prompt 4 — 单张正文

```text
用 doubao-local profile，出一张 16:9 图：Agent 三步调用。双参考 canonical + identity_sheet。
```

- [ ] anthropomorphization lock
- [ ] 无 icon-as-head
- [ ] 1 主动词 + 功能色

---

## 正文 4 张验证批

输出：[`.validation-output/brand-mark-doubao/generation/`](../.validation-output/brand-mark-doubao/generation/)

| # | 文件 | 结构 |
| --- | --- | --- |
| 01 | `01-workflow-loop.png` | 四环闭环 |
| 02 | `02-goal-backward-design.png` | 目标倒推 |
| 03 | `03-failure-comparison.png` | 乱 vs 简 |
| 04 | `04-feedback-iteration.png` | 反馈迭代 |

Confirm Gate：[`.validation-output/brand-mark-doubao/confirm-gate-report.md`](../.validation-output/brand-mark-doubao/confirm-gate-report.md)

---

## brand_mark QA（每张必过）

来自 `brand-mark-mode.md`：

- [ ] 无 icon-as-head
- [ ] 脸/发型/主色可回溯 L1+L2
- [ ] 非纯黑白（除非用户要求）
- [ ] 有主动作，非站桩
- [ ] 橙/红/蓝功能色克制
- [ ] 非小石头橙色胶囊

---

## 记录

| 阶段 | 通过 | 问题 |
| --- | --- | --- |
| 脚本 PASS | ✅ | |
| Enrollment L0–L4 | ✅ | |
| Agent 路由 ×4 | ✅ | 文本模拟 |
| 正文批 ×4 | ✅ | 2026-07-21 |

完整报告：[`.validation-output/brand-mark-doubao/REPORT.md`](../.validation-output/brand-mark-doubao/REPORT.md)
