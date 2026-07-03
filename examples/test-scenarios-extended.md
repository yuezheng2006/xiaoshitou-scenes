# 扩展试跑场景（新功能 · 2026-07-02）

> 实物图 01–18 见 [test-scenarios.md](test-scenarios.md)。本页为 **知识卡 / PPT 演讲 / 四种模式路由 / 老杨风格化资产** 对应的案例图与可复制提示词。

样张目录：`assets/test-output/`

---

## 四种模式路由（手绘图）

**摘要**：一张图讲清四种模式怎么选——处境走实物图、结构走手绘图、收藏走知识卡、演讲走 PPT。

**文件**：`test-handdrawn-four-mode-routing.png`

```text
小石头手绘图：四种模式路由，处境→实物图、结构→手绘图、收藏→知识卡、演讲→PPT。
结构：手绘分叉路 + 路由开关，小石头拉线把内容分到四个分支。
批注：处境 / 结构 / 收藏 / 演讲 / 路由
```

---

## 手绘图 · Agent 工作流 loop

**摘要**：输入 → 调工具 → 输出 → 回看，小石头拉橙色环线。

**文件**：`test-handdrawn-agent-loop.png`

```text
小石头手绘图：Agent 从任务输入到工具执行再到结果回看。
结构：Workflow loop，小石头拉橙色环线穿过模块。
批注：输入 / 调工具 / 结果 / 回看 / 别断
```

---

## 知识卡 · 四步方法论（3:4）

**摘要**：竖版收藏图，标题 + 四步模块 + 2 个小石头分工。

**文件**：`test-knowledge-card-four-steps.png`

```text
小石头知识卡：把『四步内容复用方法』（收集→沉淀→组合→输出）做成 3:4 收藏图。
2 个小石头分工：一个指向模块、一个搬运卡片；体型姿态明显不同。
形态：白板讲解卡 + 步骤模块。
```

---

## 知识卡 · 行动清单（4:5）

**摘要**：今晚就能做的清单，小石头举牌 + 标风险项。

**文件**：`test-knowledge-card-action-checklist.png`

```text
小石头知识卡：把「今晚就能做的 5 条」做成 4:5 竖版行动清单卡。
至少 2 个小石头：一个举「先做」牌，一个给第 3 条打叉标风险。
形态：行动清单卡。
```

---

## 知识卡 · 观点海报（9:16）

**摘要**：强观点竖版手机海报，一个小石头推开元素堆叠。

**文件**：`test-knowledge-card-opinion-poster.png`

```text
小石头知识卡：把观点「配图不是堆元素」做成 9:16 手机海报。
形态：观点卡；一个小石头推开杂乱图标堆。
标签：一个动作 / 一个物件 / 留白
```

---

## PPT 演讲 · 成套示例（8 页）

**主题**：《AI 时代，内容怎么配图才有效》——这是**可直接用于直播分享的 PPT 页面**，不是 Skill 功能说明图。

完整成套见 `assets/examples/ppt-mode/01-cover.png` … `08-closing.png`。

### 01 封面

**文件**：`assets/examples/ppt-mode/01-cover.png`（试跑目录：`ppt-01-cover-content-share.png`）

```text
PPT 演讲模式：主题《AI 时代，内容怎么配图才有效》，直播分享 8 页。先出导演规划卡，确认后出封面。
页面类型：封面页；沟通任务：定主题、定气质。
```

### 03 痛点页

**文件**：`assets/examples/ppt-mode/03-pain-points.png`（试跑目录：`ppt-03-pain-three-struggles.png`）

```text
PPT 演讲模式：第 3 页，页面类型「痛点页」。
标题：三个常见困境——写完不知道配什么 / 配图变成堆元素 / 改图比写文章还久。
```

### 05 方法页 · 06 案例页 · 08 结束页

| 页码 | 文件 | 类型 |
| --- | --- | --- |
| 05 | `05-method.png` | 方法：抽节点 → 选隐喻 → 留 3 标签 |
| 06 | `06-case.png` | 案例：需求评审被拉回，一张图说完 |
| 08 | `08-closing.png` | 收束：今晚只试一张图 |

---

## 老杨 × 小石头 · 实物图（轻 Q 3D）

**摘要**：双 IP 物件现场协作；读 `author-persona-spec.png` + `persona-scene-patterns.md`；老杨调度/递卡，小石头执行；老杨 3D，小石头 flat 2D。

**文件**：`test-author-persona-physical-prompt-review.png`

```text
老杨和小石头：一起评审提示词草稿，生成一张 16:9 实物图。
老杨递任务卡，小石头圈一句话；标签：这句行吗 / 再改 / 上线前
要求：双 IP 互动；老杨轻 Q 3D，小石头 flat 2D，渲染语言必须区分。
```

---

## 老杨 × 小石头 · 手绘图（扁平黑线）

**摘要**：双 IP 白板拆解；读 spec + handdrawn + `persona-scene-patterns.md`；老杨画结构，小石头拉线。

**文件**：`test-author-persona-handdrawn-routing.png`

```text
老杨：在白板旁解释双模式路由，小石头拉线连接实物图和手绘图。16:9 手绘图。
批注：内容 / 处境 / 结构 / 路由 / 拉过去
要求：双 IP 互动；老杨扁平黑线；读取 spec + handdrawn，不读取 actions。
```

---

## PPT 仅规划（不出图）

**摘要**：验证必须先出导演规划卡。

```text
PPT 演讲模式：10 页直播分享《小石头 IP 是怎么做出来的》，先不要出图。
```

**期望**：整套导演规划卡，确认后再出 1–2 页样张。

---

## 新功能样张索引

| 新功能 | 样张文件 | 对应 reference |
| --- | --- | --- |
| 四种模式路由 | `test-handdrawn-four-mode-routing.png` | `common-modes-and-sizes.md` |
| 知识卡 · 方法论 | `test-knowledge-card-four-steps.png` | `knowledge-card-mode.md` |
| 知识卡 · 行动清单 | `test-knowledge-card-action-checklist.png` | `knowledge-card-mode.md` |
| 知识卡 · 观点 9:16 | `test-knowledge-card-opinion-poster.png` | `knowledge-card-mode.md` |
| PPT · 成套 8 页 | `assets/examples/ppt-mode/01–08` | `ppt-presentation-mode.md` |
| 老杨 · 实物图 | `test-author-persona-physical-prompt-review.png` | `author-persona-spec.png` |
| 老杨 · 手绘图 | `test-author-persona-handdrawn-routing.png` | `author-persona-spec.png` + `author-persona-handdrawn.png` |
