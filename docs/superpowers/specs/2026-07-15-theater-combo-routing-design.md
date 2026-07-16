# 老杨小剧场组合路由（方案 A）

日期：2026-07-15  
状态：已确认并落地  
范围：`scene-skill-core` 默认 profile 路径分流

## 问题

路径 C（老杨小剧场）与路径 B（双 IP）原为互斥：进小剧场默认不出小石头；同句「小剧场」+「老杨和小石头」曾优先打回 B。用户需要组合口令：

```text
老杨小剧场 + 小石头 + xx 场景
```

在保留小剧场潮玩金样的前提下，允许小石头同框。

## 决策

采用**方案 A**：含「小剧场」时始终进路径 C；潮玩画风为主；小石头保持 flat 2D；「xx 场景」为内容/场域，不默认切实物/手绘模式。

## 路由表

| 用户说法 | 路径 | 出镜 |
| --- | --- | --- |
| `小剧场` / `老杨小剧场` / `IP小剧场`（无小石头） | **C 单人** | 仅老杨 |
| `小剧场` + `小石头` / `Little Stone` | **C 组合** | 老杨 + 小石头 |
| `老杨` / `老杨和小石头`（无「小剧场」） | **B** | 双 IP，按模式画风 |
| 仅小石头 / 未触发老杨 | **A** | 仅小石头 |

**冲突规则（改）**：同句同时出现「小剧场」与「小石头」→ **C 组合**，不再打回 B。  
仅当「小剧场」+「老杨和小石头」且用户**同时显式要求**「手绘图/实物图/知识卡/PPT」时，再提示是否改走 B；默认仍 C 组合。

## 画风与职责

| 角色 | 渲染 | 职责 |
| --- | --- | --- |
| 老杨 | 潮玩 vinyl-toy，跟设定图金样 | 主讲 / 指向 / 批注 / 核心动作 |
| 小石头 | flat 2D `#f39800` 胶囊，永不 3D 同化 | 执行 / 递物 / 旁注协助（可选配角，非强制每张双 IP 握手） |

「xx 场景」= 场域与道具语境（车载、咖啡馆、工作流桌面等），不是模式切换词。

图型仍用小剧场语法：流程拆解图 / 核心动作图 / 一鱼两吃。

## 读取链（C 组合）

```text
persona-theater-checklist.md
  → persona-author-theater.md
  → persona-author-theater-prompts.md（含组合片段）
  → 设定图金样（必传）
  → character.md + little-stone 设定图（组合时必传）
```

**不要**套用 `persona-scene-patterns.md` 的路径 B「每张必须双 IP 互动」强制戏。

## 传图

| 档 | 必传 |
| --- | --- |
| C 单人 | `theater-character-sheet.png`（金样） |
| C 组合 | 金样 + `primary-character-reference.png`（+ 必要时 actions） |

禁止真人照。禁止把小石头画成橙色 3D 卵石。

## 文档改动面（实现时）

- `SKILL.md` / `QUICK-START.md` / `profile.md`
- `common-persona-routing.md`
- `persona-author-theater.md` / `persona-author-theater-prompts.md`
- `persona-theater-checklist.md`
- `persona-quick-checklist.md`（冲突行）
- 记忆库 `项目/xiaoshitou-scenes.md`（结论，无试跑版本号）

## 非目标

- 不把小剧场默认改成路径 B 手绘/实物画风
- 不要求 C 组合每张都必须双人互动
- 不把试跑中间版本号写入文档

## 验收口令

```text
老杨小剧场 + 小石头：写是所有内容形态的底层能力 · 流程拆解图
```

期望：潮玩底、老杨跟金样、小石头 flat 2D 在图内执行/协助、无路径 B 强制握手戏。
