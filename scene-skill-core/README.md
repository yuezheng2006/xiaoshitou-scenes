# scene-skill-core

Codex Skill 核心包。默认 profile 是 **小石头 + 老杨双 IP 互动**（`ip-profiles/default-little-stone/`）。

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

## 文档索引

- 工作流：`SKILL.md`
- 双 IP 场景：`references/persona-scene-patterns.md`
- 老杨规范（分层）：`ip-profiles/default-little-stone/persona-author.md` 及 `persona-author-*.md`
- 可复制提示词：[examples/usage.md](../examples/usage.md)
- 验收用例：`evals/evals.json`
