# scene-skill-core

当前正式 Skill 名称为 `scene-skill-core`。它取代早期的 `little-stone-scenes`；如果本机仍安装旧目录，请先移除或停用旧版本，再安装本目录。

Codex Skill 核心包。默认 profile 是 **小石头 + 老杨双 IP 互动**（`ip-profiles/default-little-stone/`）。无品牌角色见 `ip-profiles/none/`。

生图时：**双参考对齐老杨**（spec + 模式校准图）；小石头默认单锚点。Prompt 按 `references/common-prompt-slots.md` 组装。

## 📖 文档导航（按角色）

### 👤 用户使用
- **快速开始**：见下方"两条入口"章节
- **完整示例**：[examples/usage.md](../examples/usage.md)
- **测试场景**：[examples/test-scenarios.md](../examples/test-scenarios.md)

### 🤖 Agent 开发
- **⚡ 首次任务必读**：`QUICK-START.md`（5 秒决策表，避免过度加载）
- **👥 Persona 触发**：`references/persona-quick-checklist.md`（双 IP 快速决策）
- **🔀 模式路由不确定**：`references/mode-decision-matrix.md`（四种模式对比）
- **📚 完整规范**：`SKILL.md`（主工作流）

### 🔧 维护者
- **🏗️ 文档架构**：`ARCHITECTURE.md`（依赖关系 + 单一真相来源原则）
- **✅ Evals 测试**：`evals/evals.json`

---

## 两条入口

### 双 IP（推荐）

```text
老杨：这篇内容想配图，请先推荐几张、什么类型。

<粘贴内容>
```

```text
老杨：把下面这套方法论做成 4:5 知识卡，我主讲，小石头执行。

<粘贴内容>
```

### 小石头单 IP

```text
小石头实物图：把下面这篇内容生成 4 张 16:9 正文配图。

<粘贴内容>
```

```text
小石头手绘图：把下面这个流程解释成一张 16:9 白板图。

<粘贴内容>
```

## 双 IP 分工

| 角色 | 职责 |
| --- | --- |
| 老杨 | 主讲 / 拆解 / 批注 / 调度 |
| 小石头 | 执行 Agent：搬卡、贴标签、标风险、物理动作 |

触发词：`老杨`、`yuezheng2006`、`老杨和小石头`、`老杨 IP 图解` 等。互动场景库：`references/persona-scene-patterns.md`。

## 四种模式

| 模式 | 适合内容 | 双 IP 典型结构 |
| --- | --- | --- |
| 实物图 | 处境、情绪、项目故事 | 物件 + 小石头动作 + 老杨递工具 |
| 手绘图 | 流程、结构、方法论 | 老杨画结构 + 小石头拉线/搬模块 |
| 知识卡 | 步骤、对比、收藏传播 | 老杨主讲 + 小石头模块分工 |
| PPT 演讲 | 直播、课件、主题演讲 | 老杨主讲页 + 小石头执行点缀 |

## 文档索引（完整列表）

**核心入口**：
- `QUICK-START.md` - Agent 5 秒决策表（**推荐首次阅读**）
- `SKILL.md` - 完整工作流与规则
- `ARCHITECTURE.md` - 文档架构与维护指南

**角色规范**（单一真相来源）：
- `ip-profiles/default-little-stone/character.md` - 小石头形象唯一定义
- `ip-profiles/default-little-stone/persona-author.md` - 老杨规范入口（分层文件）

**模式规则**：
- `references/physical-master-anchors.md` - 实物图母版 01-06
- `references/handdrawn-composition-patterns.md` - 手绘图结构类型
- `references/knowledge-card-mode.md` - 知识卡模式
- `references/ppt-presentation-mode.md` - PPT 演讲模式

**快速决策**：
- `references/persona-quick-checklist.md` - 双 IP 快速决策
- `references/mode-decision-matrix.md` - 模式对比与边界案例
- `references/common-modes-and-sizes.md` - 尺寸与信息量分级
- `references/common-qa-repair.md` - 返修格式与反馈映射

**示例与测试**：
- [examples/usage.md](../examples/usage.md) - 可复制提示词
- [examples/test-scenarios.md](../examples/test-scenarios.md) - 测试场景
- `evals/evals.json` - 验收用例
