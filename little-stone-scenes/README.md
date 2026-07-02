# 小石头 IP 配图

个人 Codex Skill 包。安装后直接用中文说配图意图即可，不必写 `$little-stone-scenes`。

## 四种模式用法

```text
小石头实物图：把下面这篇内容生成 4 张 16:9 正文配图。

<粘贴内容>
```

```text
小石头手绘图：把下面这个流程解释成一张 16:9 白板图。

<粘贴内容>
```

```text
小石头知识卡：把下面这套方法论做成一张 3:4 收藏图。

<粘贴内容>
```

```text
PPT 演讲模式：按下面的大纲先出导演规划卡，确认后再逐页出 16:9 演讲页面。

<粘贴大纲或逐字稿>
```

## 模式区别

| 模式 | 适合内容 |
| --- | --- |
| 小石头实物图 | 处境、情绪、项目故事、正文观点隐喻、长卷 |
| 小石头手绘图 | 流程、结构、系统关系、方法论、认知拆解 |
| 知识卡（`references/knowledge-card-mode.md`） | 方法论、步骤、对比、案例、诊断、课程总览等需要独立传播/收藏的内容 |
| PPT 演讲模式（`references/ppt-presentation-mode.md`） | 直播分享、课程课件、主题演讲、案例复盘的整套页面 |

无论哪种模式，都必须保留小石头的 `#f39200` 胶囊体、白圆眼、物理/概念动作和短标签；实物图/手绘图还必须保留充足留白，知识卡/PPT 演讲模式默认不主动触发，只在用户明确要求时使用。

## 作者出镜

当用户提到 `老杨`、`作者`、`yuezheng2006`、`我本人` 或 `我的数字形象` 时，按当前模式读取风格化资产：实物图模式读 `assets/persona/author-persona-spec.png`（身份锚点，小比例/复杂动作时加读 `author-persona-actions.png`）；手绘图/知识卡/PPT 模式读 `author-persona-handdrawn.png`，把作者数字形象加入场景，并让他和小石头互动。详见 `references/common-author-persona.md`。

默认不出现作者形象。仓库不包含真人照片，全部资产均为风格化图（轻 Q 3D / 手绘线稿）。

- 工作流与规范：`SKILL.md`、`references/`
- 可复制 prompt：[examples/prompts.md](../examples/prompts.md)
- 合规说明：[NOTICE.md](../NOTICE.md)
