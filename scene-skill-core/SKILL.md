---
name: scene-skill-core
description: |
  使用当前 IP profile 生成多模式配图和视频：实物图走 2.0 简笔物件小现场；手绘图走 1.0 白板手绘解释图；知识卡走竖版收藏传播图；PPT 演讲模式走整套手绘风演讲页面；视频模式走 60-90 秒带旁白的动画讲解视频。默认 profile 是 default-little-stone（小石头 + 老杨双 IP 互动），可通过 ip-profiles/ 替换形象、persona、资产与 Logo 边界；也可切换 ip-profiles/none（不要人物 / 纯物件）。
when-to-use: |
  用户要用当前 IP profile 为中文内容生成配图、插图、shot list、解释图、知识卡、海报、演讲 PPT 或讲解视频时触发——**不必**要求用户写 `$scene-skill-core` 或 `Use $...`。
  双 IP 入口：老杨、yuezheng2006、老杨和小石头、老杨 IP 图解、让我和小石头一起——触发后默认「老杨讲、小石头干」双 IP 互动。
  老杨小剧场入口：必须含「小剧场」（小剧场 / 老杨小剧场 / IP小剧场）——潮玩视觉印记；默认同人；同句加「小石头」→ C 组合（flat 2D）；无「小剧场」不进此入口。
  无角色入口：不要人物、纯物件、无 IP、none——切换 ip-profiles/none。  显式风格词：实物图、实物场景、物件小现场；手绘图、手绘解释、白板图、逻辑图；知识卡、图文号知识卡、手机海报、方法拆解图、收藏图、竖版传播图；PPT、课件、直播分享页、主题演讲、整套演讲页面、按大纲逐页出图、演讲页面、导演规划卡；视频讲解、动画视频、手绘视频、配音视频、讲解视频、小石头视频。默认 profile 也接受「小石头实物图 / 小石头手绘图 / 小石头视频」。
  典型意图：生成/设计/出图/配图/插图；这篇内容想配图请先推荐；16:9 正文图；9:16 手机海报；3:4/4:5 知识卡；流程解释、结构拆解、方法论图；彩蛋模式、长卷、项目复盘；先分析配图方案暂不生图；改图、减标签、重生成；按大纲/逐字稿逐页出 PPT；生成讲解视频、带旁白的动画。
  输入可以是正文、主题、观点、节点列表、项目说明、演讲大纲/逐字稿/旧 PPT，或指定母版类型。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - imagen
context: fork
---

# Profile 化多模式配图

## 🚀 快速开始（Agent 必读）

**第一次执行任务？先读这个：**

→ **`QUICK-START.md`**（5 秒决策表：环境检测 + 模式判断 + 必读文件 + persona 触发 + 简化 Confirm Gate）

不要直接读完本文件全部内容；按 QUICK-START 的决策表按需加载。

**⚠️ 环境硬性约束**：本 Skill 必须在 **Codex 环境**运行，生图必须使用 Codex 自带的 **`imagen` 工具**。详见 `QUICK-START.md` § -1 和 `references/codex-environment-guidance.md`。

**常见场景快速跳转：**
- 实物图任务 → `QUICK-START.md` 决策表 A
- 手绘图任务 → `QUICK-START.md` 决策表 B
- 知识卡任务 → `QUICK-START.md` 决策表 C
- PPT 任务 → `QUICK-START.md` 决策表 D
- 触发 persona（老杨双 IP）→ `references/persona-quick-checklist.md`
- 触发老杨小剧场 → `references/persona-theater-checklist.md`
- 模式不确定 → `references/mode-decision-matrix.md`

## 触发方式

Skill 安装到 Codex 后，用户**直接用中文说意图即可**。默认 profile 是 `ip-profiles/default-little-stone/profile.md`（小石头 + 老杨双 IP）。Agent 应自动加载本 Skill，**不要**要求用户先写 `Use $scene-skill-core`。

可选：`$scene-skill-core` 仅用于用户想强制指定 Skill 时。

### 三条入口（默认 profile）

**路径 A — 小石头单 IP（未触发老杨）**

```text
小石头实物图：为这篇内容出 4 张 16:9 配图
小石头手绘图：解释这个 Agent 工作流
```

**路径 B — 老杨 × 小石头双 IP（推荐）**

```text
老杨：这篇内容想配图，请先推荐几张、什么类型。
老杨：把这套四步方法做成 4:5 知识卡，我主讲，小石头执行。
老杨和小石头：解释这个工作流，出一张白板图。
```

Persona 触发词：`老杨`、`yuezheng2006`、`老杨和小石头`、`老杨 IP 图解`、`让我和小石头一起` 等（完整列表见 profile）。**一旦出现，默认启用双 IP 互动**：老杨主讲/拆解/批注，小石头执行 Agent；读取 `persona-scene-patterns.md` 选互动场景。

**路径 C — 老杨小剧场（可组合小石头）**

```text
小剧场：这篇工作流长文配 4 张插图
老杨小剧场 · 一鱼两吃：写是所有内容形态的底层能力
老杨小剧场 + 小石头：给「目标倒推」出一张核心动作图
老杨小剧场 + 小石头 · 车载场景：流程拆解图
```

**硬门槛**：必须出现 `小剧场`。读 `persona-author-theater.md` / `persona-theater-checklist.md`。默认单人；同句「小石头」→ **C 组合**（潮玩底 + flat 2D，不打回 B）。仅说「老杨」无「小剧场」→ 路径 B。

未触发老杨且未触发小剧场时，只出现小石头，不出现老杨。

## 核心定位

把中文内容转译成五种清晰区分的 profile 配图和视频。默认 profile 在触发老杨后，五种模式都支持**老杨 × 小石头双 IP 互动**：

```text
实物图：物件小现场 + 小石头物理动作 + 老杨调度/递工具（双 IP 可选）
手绘图：老杨画结构/批注 + 小石头拉线/搬模块（双 IP 推荐）
知识卡：老杨主讲/指向 + 小石头在模块里执行分工（双 IP 推荐）
PPT 演讲：老杨主讲页 + 小石头执行点缀（双 IP 推荐）
视频讲解：实物图/手绘图场景 + 老杨旁白 + 小石头动作演示（双 IP 可选）
```

实物图/手绘图是默认主力模式；知识卡/PPT 演讲/视频模式体量更大、更容易过度设计，只在用户明确触发或内容明显需要独立传播容器/整套演讲页面/讲解视频时才进入，不要主动升级模式。

## 模式路由

### 自定义 IP 录入路由（优先于普通模式路由）

用户说“录入 IP / 新建 IP / 上传形象 / 用这套形象 / 创建角色档案 / 用这个 Logo / 用这个 Icon / 品牌标做 IP / App 图标录入”等意图时，立即进入 `profile_enrollment`，不要把请求当成普通配图或海报任务。

- 用户附带 Logo / Icon / 品牌标 / App 图标时，默认 `input_kind=brand_mark`；走自定义 IP 录入，不要路由到「贴 Logo 到小石头」或默认小石头 profile。
- `brand_mark` 方标可作为 canonical 候选；**须先 identity_sheet 再模式校准**；角色化必须可回溯原标锚点，禁止 icon-as-head。详见 `references/brand-mark-mode.md`。
- 推荐用户先提供一张真实图；首轮优先接收并登记该图作为身份锚点。
- 首轮只建立 Profile Enrollment Card，提取身份锚点、气质、参考图来源和待确认项。
- 用户确认身份方案前，不调用图片生成工具，不进入四种内容生成模式。
- 半身 / 胸像先标记为“用户真实图-待补全”，不能直接冒充全身 canonical asset。
- 没有真实图时，文字方案或系统生成草图只能标记为临时草稿；除非用户明确授权，不得作为正式 IP 参考。
- 当前模式没有校准图时使用 `single`，不能声称 `dual`。
- 只有状态进入 `AVAILABLE` 后，才把该 profile 接入普通 Task Card → Plan Card → Render Card → QA Card。

完整契约见 `references/contracts/profile-contract.md`。

本 Skill 内的相对路径均相对于 `scene-skill-core/` Skill 根目录解析；不要把 `QUICK-START.md`、`references/` 或 `ip-profiles/` 误解析为工作区根目录下的同名路径。

显式风格词优先：

- 用户说 **实物图 / 实物场景 / 物件小现场**：使用 **实物图模式**。
- 用户说 **手绘图 / 手绘解释 / 白板图 / 逻辑图**：使用 **手绘图模式**。
- 用户说 **彩蛋 / 长卷 / 超横版 / 项目复盘 / 产品演化 / 成长路径**：使用 **实物图长卷模式**。
- 用户说 **知识卡 / 图文号知识卡 / 手机海报 / 方法拆解图 / 收藏图 / 竖版传播图**：使用 **知识卡模式**，读取 `references/knowledge-card-mode.md`。
- 用户说 **PPT / 课件 / 直播分享页 / 主题演讲 / 整套演讲页面 / 按大纲逐页出图 / 演讲页面 / 逐页出图 / 导演规划卡**：使用 **PPT 演讲模式**，读取 `references/ppt-presentation-mode.md`。

未指定风格时，按内容类型判断：

- 处境、情绪、用户痛点、正文配图、项目故事、K 歌服务现场、员工工牌、值班与服务工单：默认 **实物图模式**。
- 流程、结构、系统关系、方法论、认知拆解、工作流解释：默认 **手绘图模式**。
- 用户明确想要"能单独发出去、值得收藏"的独立传播图，或内容是方法论/步骤/流程/对比/案例/诊断/课程总览且信息量偏高：默认 **知识卡模式**。
- 用户提供演讲大纲/逐字稿/旧 PPT，或要求连续多页、整套课件效果：默认 **PPT 演讲模式**。
- **已触发老杨且用户只粘贴内容、未指定模式**：先读 `persona-scene-patterns.md`，输出双 IP 出图方案推荐（模式 + 张数 + 互动场景类型），不要逼用户先选模式词。
- 仍不确定时，先给 1-2 句说明并选择最贴合内容的模式，不要反复追问；实物图/手绘图之外的两种模式不确定时优先退回实物图或手绘图，不要主动升级。

## 四种模式

- **实物图模式**：16:9 正文图，一个简笔物件小现场；也支持彩蛋长卷故事图。参考 `physical-style-dna.md`、`physical-master-anchors.md`、`physical-object-patterns.md`。
- **手绘图模式**：16:9 白板手绘解释图；用 1 个核心结构和少量红橙蓝批注解释流程、系统或方法。参考 `handdrawn-style-dna.md`、`handdrawn-composition-patterns.md`、`handdrawn-qa-checklist.md`。
- **知识卡模式**：3:4/4:5/9:16 竖版独立传播图，可承载标题、模块、步骤、风险、行动、多个主角色协作分工。参考 `knowledge-card-mode.md`。
- **PPT 演讲模式**：16:9 连续多页整套演讲页面，先出导演规划卡再分批生成。参考 `ppt-presentation-mode.md`。

## 当前 Profile（执行摘要）

- **默认 profile**：`ip-profiles/default-little-stone/profile.md`。
- **无角色 profile**：`ip-profiles/none/profile.md`（用户说不要人物 / 纯物件 / none 时切换）。
- **主角色（小石头）**：从 `character.md` 读取；生图默认**单锚点**设定图。
- **双参考（对齐人 · 老杨）**：实物跟 `author-persona-panorama.png`；手绘系跟 `author-persona-panorama-handdrawn.png` + 实体 panorama（手绘更重要）。猫为金**黄**金渐层（默认不强制出镜）。
- **Persona**：从当前 profile 的 persona 文件读取触发词、渲染语言和资产路由。
- **Logo 边界**：通用规则读 `references/common-logo-safety.md`，具体策略读当前 profile 的 `logo-safety.md`。
- **多图/多人**：2 张及以上必须锁定同一 profile 主角色；多人同图要像同一 IP 家族的不同个体，禁止复制粘贴。

完整规则：`references/common-character-lock.md` + 当前 profile 的 `character.md`。

## 共同底线（四种模式都必须保留）

模式只改变表达载体，不改变当前 profile 主角色自己的识别。

- 必须是同一个 **profile 主角色**：名称、主色、形体、眼睛、肢体和维度锁以当前 profile 为准。
- 必须靠 **物理动作 / 概念动作** 讲故事：拉、挡、推、扛、解、贴、塞、接、修、守；知识卡/PPT 里也可以是递卡、指向、批注等结构动作，但不能只是站旁边装饰。
- 必须使用 **短中文标签 / 批注**，不要大段解释；知识卡/PPT 允许更多结构性文字（标题、模块），但仍要克制字数。
- 必须保留「认真、略笨、有点倔」的气质，不要变成可爱吉祥物、商业 mascot、3D 卡通或正式企业图标。
- 禁止把真实 Logo、品牌名或任何商标直接贴在主角色身上，除非 profile 明确允许且用户明确授权；默认 profile 禁止。

实物图模式和手绘图模式额外必须有 **留白**，不要做成信息堆叠、海报或 PPT——这两种是默认轻量模式，信息量升级的需求应该导向知识卡模式，连续多页需求应该导向 PPT 演讲模式，而不是把这两种模式硬塞成容器。

## 模式来源

- **手绘图模式** 承袭 Ian / helloianneo 手绘解释工作流（1.0）：白底手绘解释图，适合拆流程、结构和方法。
- **实物图模式** 承袭 Ian / helloianneo 实物场景工作流（2.0）：简笔物件小现场，适合表达处境、情绪和故事。
- **知识卡模式** / **PPT 演讲模式**：在实物图/手绘图的 profile 主角色和视觉语言基础上新增的两种容器型模式，参考 [haloshin/ip-diagram-creator](https://github.com/haloshin/ip-diagram-creator) 的知识卡与 PPT 演讲模式思路本地化而来，默认不主动触发。公开示例图见仓库根目录 `assets/examples/gallery/` 与 `assets/examples/ppt-mode/`；Skill 包内 `assets/masters/` 只放实物图母版 01–06。
- 四种模式共享当前 profile，但生成时必须按当前任务只选一种，不要把不同模式的构图/尺寸/信息量混成一张。

## Before Starting

按任务需要读取，不要一次全部塞进上下文。`references/` 文件按前缀分组：

公共规则（多种模式都可能用）：

- `ip-profiles/default-little-stone/profile.md`：默认 IP profile 总入口；更换 IP 时优先替换 profile。
- `ip-profiles/none/profile.md`：无品牌角色路径。
- `references/common-prompt-slots.md`：通用 prompt 槽位组装；**双参考用于对齐老杨**。
- `references/common-character-lock.md`：通用 Character Lock、维度锁、多人差异锁机制。
- `references/common-persona-calibration.md`：所有人像参考图的生成前校准卡、生成后身份/年龄/比例检查；未通过不得生成或交付。
- `references/common-persona-routing.md`：通用 persona 触发、双 IP 路由和安全边界。
- `references/persona-scene-patterns.md`：**触发 persona 时必读**——老杨 × 小石头六类互动场景、出图方案推荐、失败信号。
- `references/common-logo-safety.md`：通用 Logo / 品牌资产安全规则；具体 Logo 边界读取当前 profile 的 `logo-safety.md`。
- `references/common-story-extraction.md`：如何从正文里提炼用户处境、动作和短标签。
- `references/common-generation-templates.md`：实物图、手绘图、长卷与批量图的提示词模板。
- `references/common-qa-repair.md`：装饰性测试、用户反馈映射表、标准化返修输出格式；收到主观返修意见或做角色装饰性检查时读取。
- `references/common-modes-and-sizes.md`：尺寸池与图内信息量分级语言；判断出图方案或触发知识卡/PPT 演讲模式时读取。

交接协议：

- `references/contracts/task-card.md`：记录用户需求、事实、Profile 和 Persona 入口。
- `references/contracts/plan-card.md`：记录模式、结构、动作、资产和生成前方案。
- `references/contracts/render-card.md`：记录 Prompt、参考图、硬性限制和返修预案。
- `references/contracts/qa-card.md`：记录 Confirm Gate、模式 QA 和返修定位。
- `references/contracts/profile-contract.md`：记录 IP 身份、参考图、录入状态和发布边界。

实物图规则：

- `references/physical-style-dna.md`：实物图视觉 DNA、比例、留白、颜色、真实物件规则。
- `references/physical-object-patterns.md`：真实物件选择、场景类型、原创隐喻和反复刻规则。
- `references/physical-master-anchors.md`：实物图 01-06 母版类型、抽象骨架、变异与拦截规则。
- `references/physical-qa-checklist.md`：实物图生成后质量检查、失败信号和迭代方向。

手绘图规则：

- `references/handdrawn-style-dna.md`：手绘图视觉 DNA、颜色、标注和禁忌。
- `references/handdrawn-composition-patterns.md`：手绘图结构类型、隐喻生成和反复刻规则。
- `references/handdrawn-qa-checklist.md`：手绘图生成后质量检查。

知识卡模式规则（仅触发知识卡模式时读取）：

- `references/knowledge-card-mode.md`：知识卡触发词、结构形态库、角色分工、必填字段、硬性预算、QA 与失败信号——一份文件涵盖全部规则。

PPT 演讲模式规则（仅触发 PPT 演讲模式时读取）：

- `references/ppt-presentation-mode.md`：PPT 演讲模式工作流、导演规划卡、page card、页面类型库、节奏规则、QA——一份文件涵盖全部规则。

资产：

- 当前 profile 的主角色资产：默认位于 `ip-profiles/default-little-stone/assets/character/`。
- 当前 profile 的 persona 资产：默认位于 `ip-profiles/default-little-stone/assets/persona/`，仅触发 persona 时读取。
- `assets/masters/`：实物图母版 `01`–`06`；只作为质量锚点，不和根目录公开示例混用。

开始前确认：

- 先判定模式、尺寸、是否作者出镜、是否涉及事实/品牌/Logo。
- `K 歌服务` 不自动触发品牌 Logo；Logo/工牌/展会/物料才读取 `common-logo-safety.md` 和当前 profile 的 `logo-safety.md`，只预留 Logo 区或使用用户本地私有授权 Logo。
- 未明确要生成时，只输出 shot list 或方案；明确“看效果 / 输出 / 生成”时，必须先完成对应模式锁定。
- 生图前：小石头传设定图（单锚点）；老杨出镜执行双参考（spec + 模式校准）；复杂姿态/小比例再加对应扩展；实物母版按上方规则读取。老杨双参考未进上下文不得声称已走对齐流程。
- **凡涉及人像参考图，必须先完成 `common-persona-calibration.md` 校准卡；校准 FAIL 不得生成。**

## Core Flow

### 0. Profile Enrollment（仅自定义 IP）

自定义 IP 录入使用独立状态机：

```text
REQUESTED → USER_REFERENCE → IDENTITY_PLAN → CONFIRMED → CANONICAL_ASSET
          → MODE_CALIBRATION（可懒加载）→ AVAILABLE
```

该状态机只负责让 Profile 变得可用，不负责生成普通内容图。录入阶段的确认和资产状态必须记录在 Profile Enrollment Card 中；完成后才回到普通交接卡协议。

### 1. 消化内容

先提炼当前内容里的“处境”，不要急着找物件：

- 这张图要让谁产生共鸣？
- 他们正在被什么东西拉扯、筛选、压住、拽回、催促、重组？
- 抽象概念能变成什么物理动作？
- 哪 2-4 个短词能一秒戳中痛点？
- 哪个真实物件天然承载这个处境？

优先选择高共鸣节点：会议、消息、返工、审查、筛选、加码、被替代、下班失败、项目卡住、内容资产沉淀、产品演化断点。

如果用户要求彩蛋模式，先把内容拆成 5-8 个连续节点：

- 左侧起点：身份、起点、最初处境。
- 中间节点：关键经历、项目转折、内容资产、产品演化。
- 右侧终点：现在在做什么、核心关注、结论或下一阶段。
- 每个节点都要有一个真实物件、主角色动作和 1-3 行短注释。

完成标记：已经明确读者处境、核心冲突、真实物件、主角色动作和短中文标签；彩蛋模式已经得到 5-8 个可视化节点。

### 1B. 事实锚定

涉及个人经历、品牌名、公司名、项目名、粉丝数、时间跨度、成绩数字时，只能使用用户输入、用户提供素材或用户明确确认的事实。

- 用户没有提供的事实，不要从母版继承，也不要补成看起来更完整的履历。
- 无法确认的内容，用概括性标签替代，例如“内容平台”“项目节点”“用户反馈”“产品实验”。
- 如果用户要求保留但信息不完整，在 shot list 或交付说明里标注“待确认”，不要把它画成确定事实。

完成标记：所有具体事实都能回到用户输入或素材；不能回溯的事实已删除、抽象化或标注待确认。

### 1C. Character / 2D / 多人锁 + Persona Identity Lock

- 2 张及以上必须读取 `common-character-lock.md` 和当前 profile 的 `character.md`，声明全批 Character Lock。
- 每张都必须写入当前 profile 的维度锁；默认 profile 是 flat 2D 平涂胶囊，但未来 profile 可定义自己的维度锁。
- **双参考（老杨出镜强制 · 对齐人）**：实物用实体 panorama；手绘系用 **手绘 panorama + 实体 panorama**（手绘更重要）。见 `persona-author-assets.md`。
- 小石头：设定图单锚点 + `{IP_DESC}` / `{IP_STYLE_ADAPT}`；不要把双参考名额用在小石头上。
- **画面出现 persona 肖像时**（含双 IP、文档预览、能力总览、README/飞书示例）：必须写入 **Persona Identity Lock**，并传双参考资产；格子过小则用抽象符号，禁止 generic 人脸。
- 实物图物件可以有光影，**主角色不能被非本 profile 的渲染语言带偏**；persona 也不能带偏主角色。
- 多人/多 Agent/团队协作场景允许 2-4 个主角色个体，但必须像同一 IP 家族里的不同个体：**胶囊宽高比全批一致**（见 `common-character-lock.md` 形体一致锁），只允许整体等比缩放（±10–15%）、倾斜、朝向、站位、动作职责不同，禁止瘦高/矮胖/横扁形体混用；生成前写入 **Limbs Lock**，生成后必做 **Confirm Gate**（L1–L4 四肢 + E1–E2 眼面；老杨出现则 P1–P7）。
- 画面出现 persona 肖像时：除 Persona Identity Lock 外，并列 **Persona Feature Stability Lock + Persona Expression Lock**（见 `common-character-lock.md`）。
- 复杂姿态、多人协作或小比例远景时，加读 profile 的动作扩展资产。
- 用户要求无角色时，切换 `ip-profiles/none/`，跳过本段角色资产。

### 1D. 双 IP 互动（persona 触发时强制）

Persona 触发词由当前 profile 定义。默认 profile 里，`老杨`、`yuezheng2006`、`老杨和小石头` 等是一等触发词。

触发后必须：

1. 读取 `common-persona-routing.md`、`common-persona-calibration.md`、当前 profile 的 `persona-author.md` 与 `persona-author-assets.md`、`persona-scene-patterns.md`；锁定模式后读 `persona-author-modes.md`；写 prompt 读 `persona-author-prompts.md`。
2. 选定互动场景类型（白板拆解 / 知识卡调度 / 物件现场 / 大判断主讲 / 分镜对比 / 长卷旁白）。
3. 写出双 IP 分工：老杨动作 + 小石头执行 Agent 动作。
4. 按模式执行老杨双参考并完成参考图校准；小石头同框时另加设定图单锚点。

硬性要求：每张图必须有老杨与小石头的明确互动；不能只有老杨肖像，也不能老杨触发后只有小石头干活。不得发明单位、联系方式、履历或背书。

未触发 persona 时，只使用小石头，不出现老杨。

### 2. 先出 shot list

如果用户说“分析 / 思考 / 怎么配图”，先给 shot list；每张必须写清模式/母版或结构类型、主题、共鸣点、核心动作、主物件或结构、主角色动作、短中文标签和成图理由。用户明确要“看效果 / 输出 / 生成”时可以直接生图，但仍必须先完成对应模式锁定。

### 2A-0. 交接卡协议

所有多图、长文、Persona、品牌或事实推断较多的任务，按以下顺序建立交接卡：

```text
Task Card → Plan Card → Render Card → 生成 → QA Card
```

单张且内容明确的简单任务可以内部快速填写，不必把完整卡片展示给用户；但生成前仍必须完成对应模式锁定，生成后仍必须通过 Confirm Gate 和模式 QA。

实物图试点优先使用：

- `references/contracts/task-card.md`
- `references/contracts/plan-card.md`
- `references/contracts/render-card.md`
- `references/contracts/qa-card.md`

### 2A. 内容确认卡（长文/多图任务强制）

shot list 张数 ≥ 3，或隐喻/标签/事实推断较多时，先输出内容确认卡，再进入母版锁定 / 结构锁定；单张且内容明确时跳过。确认卡必须区分用户原话和我的推断，不得把推断包装成确认事实。

### 2B. 母版锁定（标准模式强制）

实物图每张生成前读取 `physical-master-anchors.md`，从 `01`–`06` 选最匹配的质量锚点；母版只提供动作类型、比例、留白和信息密度，不允许复制空间拓扑。必须写出母版类型、不变量、至少 3 个当前内容变异点、3 秒读懂句、适配点和失败信号。硬预算：一个核心物理动作、一个真实主物件或紧凑主物件组、最多 1-2 个小配件、最多 4 个短标签。

### 2C. 手绘图结构锁定（手绘图模式强制）

手绘图不使用实物母版。生成前读取 `handdrawn-style-dna.md`、`handdrawn-composition-patterns.md`、`handdrawn-qa-checklist.md`，选择结构类型，并写出核心意思、画面结构、主角色概念动作、建议元素、中文批注和失败信号。硬预算：一张图只解释一个核心结构，3-5 个核心模块，最多 5-8 个短批注；不得 PPT 化、复杂架构化或画成真实物件摄影棚场景。

### 2D. 知识卡结构锁定（知识卡模式强制）

用户触发知识卡模式时，读取 `references/knowledge-card-mode.md` 和 `references/common-modes-and-sizes.md`，先选一个知识卡形态并完成该文件里的「必填字段」结构锁定，再进入生成；不要跳过结构锁定直接按手绘图的思路出图。

完成标记：已选定知识卡形态、尺寸、图内信息量、角色分工，并完成必填字段；没有硬套参考形态。

### 2E. PPT 导演规划（PPT 演讲模式强制）

用户触发 PPT 演讲模式时，读取 `references/ppt-presentation-mode.md`，先输出整套导演规划卡，等用户确认页数、节奏、密度和人物出现频率后，再选 1-2 页代表页做样张；样张确认后才分批生成剩余页面。不要跳过导演规划直接批量出图。

完成标记：已输出整套导演规划卡并获用户确认；样张已确认字体/人物/密度后才继续分批生成。

### 3. 单张生成

每张图单独生成，不要把多张拼成一张（PPT 演讲模式除外——按 page card 分批生成整套页面）。

提示词默认尽量使用中文。交付给用户复制使用的完整提示词、返修提示词、图内文字、标签、批注和结构描述都优先中文；仅保留必要英文风格关键词、资产文件名、技术参数、专有名词和少量负面约束短语。

提示词必须包含对应模式：

- 实物图：16:9，母版锁定与 Character Lock，`#FFFFFF` 纯白背景，真实物件小现场，白色摄影棚表面，真实物件光影统一；**主角色必须保持当前 profile 的维度锁，禁止继承物件的 3D 渲染语言**；中等主体覆盖面积但视觉重量轻；禁止截图、UI、Logo、PPT、商业插画、贴图边界和大段解释。
- 手绘图：16:9，结构类型锁定与 Character Lock，`#FFFFFF` 纯白背景，黑色手绘线稿结构，少量红 / 橙 / 蓝批注；禁止截图、UI、Logo、PPT、商业插画、贴图边界和大段解释。
- 知识卡：按 2D 知识卡结构锁定选定的尺寸（3:4/4:5/9:16）与信息量，白底黑线为主 + 克制红橙蓝，包含标题/模块/步骤等结构；允许比手绘图更多文字，但仍要克制。
- PPT 演讲：16:9，按 page card 的页面类型、视觉权重和图文比例生成，必须像 PPT 页面但不能像知识卡、信息图海报或培训讲义。
- 主角色：按当前 profile 的 `character.md` 填入 `{IP_DESC}` / `{IP_STYLE_ADAPT}` / 维度锁（单锚点）。
- 老杨出镜：遵守双参考（对齐人）并写入 Persona Identity Lock。

完成标记：每张图都有独立提示词，且包含模式、比例、背景、主角色动作、短标签/批注、点缀和负面约束。

### 3B. 彩蛋长卷生成

当用户说“彩蛋模式 / 长卷故事图 / 超横版 / 个人经历 / 项目复盘 / 产品演化 / 成长路径 / 像这张长图”时，使用彩蛋模式。

彩蛋模式锁定长卷骨架：`2.6:1` 到 `3:1` 超横版、高级近白背景、细黑手绘曲线路径、5-8 个真实物件节点、主角色逐段参与、左起右收、节点不编号、不机械等距、不做信息图模块。按当前内容替换节点，不复刻样例经历、第三方平台或品牌名，除非用户提供等价事实。

### 4. 使用母版类型

母版是质量标尺与动作类型索引，不是可复制布局。`assets/masters/` 的 01–06 PNG 只用于校准场景覆盖面积、留白、物件光影、比例、短标签、点缀密度和动作关系；根目录 `assets/examples/` 是公开示例图库，不作为母版目录。每次都要让当前内容重新决定隐喻，并写出至少 3 个变异点。

### 5. QA 和迭代

按模式选 QA：实物图/长卷读 `physical-qa-checklist.md`；手绘图读 `handdrawn-qa-checklist.md`；知识卡和 PPT 读各自模式文件；主观返修先查 `common-qa-repair.md`。**每张候选图必须先做形象检查并输出 Confirm Gate**（小石头 L1–L4/E1–E2；老杨 P1–P7；见 `common-character-lock.md`），**只有结论 `CONFIRMED` 才可交付**，再做模式 QA。文档/预览/仓库示例与正文配图同一标准。第一张生成图永远只是候选图，必须查看并比对后才能交付。元素清单化、母版复刻化、读不懂、商品图感、素材拼贴、标签概念化、主角色不动作、维度漂移、**四肢锚点错误/有嘴/多手**、**形象锁定失败（粗黑框/黑长袖/generic 人脸/背身/露齿）**、隐私/Logo 未授权，均不得交付为最终图。

### 6. 保存交付

默认保存目录：实物图 `assets/<topic-slug>-scenes/`，长卷 `assets/<topic-slug>-long-scroll/`，知识卡 `assets/<topic-slug>-knowledge-card/`，PPT `assets/<topic-slug>-ppt-mode/`。按 `01-topic-name.png` 顺序命名；PPT 按页码和页面类型命名。保留原始生成文件，不覆盖已有资产，除非用户明确要求替换。

## 输出口径

生成前：短而准，给 shot list 或生成计划。

生成后：展示图片、说明用途、给保存路径，并标出哪些最稳、哪些可选或需要再收一轮。

不要长篇解释理论。让图先说话。

## Completion States

| 状态 | 含义 |
| --- | --- |
| DONE | 已完成 shot list 或图片生成，并按 QA 检查通过 |
| DONE_WITH_CONCERNS | 已交付，但存在文字稳定性、物件真实感、背景纯度/近白空气感等待优化项 |
| BLOCKED | 缺少主题/正文/节点，或用户要求的事实、人物、品牌信息不可确认 |

## Quality Gates

实物图/长卷的 CRITICAL：模式锁定、母版或长卷骨架、至少 3 个变异点、主角色符合 profile 维度锁且承担动作、真实物件小现场、正确尺寸、短中文标签、3 秒读懂、无元素清单化/母版复刻化/未授权信息。手绘图、知识卡、PPT 的门禁写在各自 reference 中，不在入口文件重复。

## Suppressions

- 用户明确提供的个人经历、品牌名、项目名，不算“未授权个人信息”，但不要额外发明。
- 母版里的具体物件可以在内容匹配时复用，不算机械复刻；机械复刻指不看当前内容直接照搬旧图。
- 生图模型偶发的轻微文字不稳不等于 Skill 失败，但必须在交付时标注并建议迭代。
