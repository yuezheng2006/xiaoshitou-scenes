# Scene Skill Core 架构设计

## 1. 文档定位

本文说明 `scene-skill-core` 的架构意图、分层边界、依赖方向和可插拔点。

它不是运行时规则，也不是某个 IP 的视觉设定。具体触发词、Prompt 句式、角色锚点和 QA 检查仍以 `SKILL.md`、`QUICK-START.md`、`references/` 与 `ip-profiles/` 下的文件为准。

## 2. 核心目标

`scene-skill-core` 是一个 Profile 化的多模式内容视觉编排器。它把用户的文字内容转译为不同的视觉载体，同时保持当前 IP 的识别稳定性。

核心原则：

1. 内容先于画面：先理解处境、冲突、结构和事实，再选择视觉模式。
2. Profile 与模式解耦：模式改变表达载体，不改变主 IP 的身份约束。
3. 规则按需加载：入口负责路由，细则下沉到 references 和 profile。
4. 生成前锁定，生成后验证：没有结构锁和角色锁，不进入批量生成；没有通过 QA，不交付。
5. 公共规则与私有资产分离：通用流程进入 `references/`，具体 IP、Persona 和品牌资产进入 `ip-profiles/`。

## 3. 分层模型

```text
用户意图 / 内容输入
        ↓
入口与模式路由层
  SKILL.md · QUICK-START.md · mode-decision-matrix.md
        ↓
Profile 身份层
  ip-profiles/<ip-id>/
        ↓
模式表达层
  physical · handdrawn · knowledge-card · ppt
        ↓
公共编排层
  story extraction · prompt slots · generation templates · mode sizing
        ↓
资产与参考图层
  character · persona · masters · examples · logo boundaries
        ↓
生成与返修层
  image tool / external generator · revision prompt
        ↓
质量门禁层
  Confirm Gate · mode QA · persona calibration · decoration test
        ↓
交付层
  scenes · long-scroll · knowledge-card · ppt-mode
```

### 3.1 入口与路由层

职责：

- 识别用户意图和显式模式词。
- 在未指定模式时，根据内容类型做默认判断。
- 判断是否启用 Persona、无角色 Profile 或小剧场路径。
- 决定本次任务的最小读取路径。

入口层不应承载完整的视觉规则。它只负责“去哪一个模块”和“先做什么”。

### 3.2 Profile 身份层

路径：`ip-profiles/<ip-id>/`

职责：

- 定义主角色的名称、形体、颜色、维度锁和动作边界。
- 提供角色资产和 Persona 资产的路径。
- 定义 Logo、品牌和隐私边界。
- 决定是否允许作者 Persona 出镜，以及如何触发。

Profile 不应定义某个模式的完整构图流程。它只回答：画面里的角色是谁、如何保持一致、哪些资产可以使用。

当前默认 Profile：`default-little-stone`。

无角色 Profile：`none`。它用于验证系统可以在没有固定品牌角色的情况下复用公共模式流程。

### 3.3 模式表达层

当前模式：

| 模式 | 主要任务 | 默认容器 |
|---|---|---|
| 实物图 | 表达处境、情绪、故事和真实动作 | 16:9 物件小现场 |
| 手绘图 | 表达流程、结构、系统关系和方法 | 16:9 白板解释图 |
| 知识卡 | 表达可独立传播、收藏和复盘的完整内容 | 3:4 / 4:5 / 9:16 |
| PPT | 表达连续演讲、课程和主题分享 | 16:9 多页面 |

每个模式必须拥有自己的：

- 结构锁定规则
- 信息密度和尺寸规则
- Prompt 适配规则
- 模式专属 QA
- 失败信号和返修方向

模式不能直接重写 Profile 的角色身份，也不能绕过公共 Character Lock。

### 3.4 公共编排层

公共编排层负责跨模式复用的流程知识：

- `common-story-extraction.md`：从内容提取处境、动作和短标签。
- `common-prompt-slots.md`：统一 Prompt 槽位和组装顺序。
- `common-generation-templates.md`：生成模板。
- `common-modes-and-sizes.md`：尺寸和信息量语言。
- `common-qa-repair.md`：用户反馈映射和标准化返修格式。

公共编排层可以引用当前 Profile，但不应硬编码某一个 IP 的颜色、形体或 Persona 细节。

### 3.5 质量门禁层

质量检查分为三层：

1. Profile / Character Lock：角色形体、颜色、眼睛、四肢、比例和跨图一致性。
2. Persona Calibration：真人或作者形象的身份、年龄、面部和比例校准。
3. Mode QA：当前模式的内容准确性、构图、信息密度、文字和风格检查。

交付顺序必须是：

```text
生成候选图
  → Confirm Gate
  → Persona Calibration（如适用）
  → Mode QA
  → 返修或交付
```

任何 Critical 项失败，都不能直接交付。

## 4. 依赖方向

依赖应遵循以下方向：

```text
入口层 → 模式层 → 公共编排层 → Profile / 资产层 → 生成工具
                         ↓
                    质量门禁层
```

更具体地说：

- `SKILL.md` 可以引用所有层，但只负责生命周期和路由。
- `QUICK-START.md` 可以引用模式和 Profile，但只负责快速决策。
- 模式文件可以引用公共规则和当前 Profile。
- 公共规则可以读取 Profile 提供的变量和资产路径，但不能依赖默认 Profile 的具体名称。
- Profile 可以被模式使用，但不应反向控制模式路由。
- 生成工具属于外部适配边界，不应成为业务规则的来源。
- QA 可以检查生成结果，但不应重新定义角色身份。

禁止形成的依赖：

- 手绘模式依赖实物母版的空间布局。
- `none` Profile 依赖默认角色资产。
- 公共 Prompt 槽位写死老杨或小石头的视觉细节。
- 某个模式直接修改另一个模式的尺寸、信息密度或结构规则。
- 生成平台的限制反向污染内容理解和模式判断。

## 5. 可插拔边界

### 5.1 IP Profile 插件

新增 IP 的最小实现：

```text
ip-profiles/<ip-id>/
├── profile.md
├── character.md
├── logo-safety.md
└── assets/
    ├── character/
    ├── persona/
    └── brand-private/
```

新增 IP 不应要求修改四种模式的核心规则。

### 5.2 Persona 插件

Persona 是跨模式能力，但应保持为独立插件：

```text
Persona Profile
├── trigger words
├── identity lock
├── asset routing
├── mode adaptation
├── prompt fragments
└── QA rules
```

Persona 的核心接口是“如何触发、传哪些资产、在当前模式承担什么职责、如何验收”，而不是重新定义模式。

### 5.3 Mode 插件

新增模式至少需要提供：

```text
Mode Profile
├── trigger and routing entry
├── structure lock
├── size / density rules
├── prompt adaptation
├── mode QA
└── delivery convention
```

新增模式还必须更新：

- `mode-decision-matrix.md`
- `QUICK-START.md` 的快速索引
- `SKILL.md` 的生命周期跳转
- `evals/evals.json` 的路由和 QA 用例

### 5.4 Prompt 插件

Prompt 不应是一整段不可拆分的长文本，而应由槽位组装：

```text
内容槽位
 + 模式槽位
 + Profile 槽位
 + Persona 槽位
 + 参考图槽位
 + 尺寸槽位
 + QA / 负向约束槽位
```

这样可以替换模型语言、生成平台或视觉风格，而不改变内容理解流程。

### 5.5 QA 插件

QA 分成公共门禁和模式扩展：

```text
公共 Confirm Gate
  + physical QA
  + handdrawn QA
  + knowledge-card QA
  + PPT QA
  + Persona QA（如适用）
```

公共 QA 只检查跨模式不变量；模式 QA 只检查本模式特有问题，避免重复定义。

## 6. 标准生命周期

```text
1. 识别输入
2. 选择 Profile
3. 选择模式
4. 提取内容处境和事实
5. 输出 shot list / 内容确认卡
6. 完成结构锁定
7. 选择母版或结构类型
8. 组装 Prompt
9. 生成候选图
10. 执行 Confirm Gate
11. 执行模式 QA
12. 返修或交付
```

不同模式可以跳过不适用步骤，但不能跳过身份锁、结构锁和交付前 QA。

## 6.1 交接协议

每个阶段通过一张交接卡向下一阶段传递信息：

```text
Task Card → Plan Card → Render Card → QA Card
```

对应文件位于 `references/contracts/`。单张且内容明确的简单任务可以内部快速填写，不必全部展示给用户；多图、长文、Persona、品牌或事实推断较多的任务必须保留这些中间产物。

交接卡的价值不是增加文档数量，而是让失败可以定位到具体层：

```text
内容错误 → Task Card / Plan Card
资产错误 → Plan Card / Render Card
Prompt 错误 → Render Card
形象错误 → Profile / Confirm Gate
模式质量问题 → Mode QA
```

## 7. 当前设计的主要风险

### 7.1 路由规则重复

模式路由同时出现在 `SKILL.md`、`QUICK-START.md` 和 `mode-decision-matrix.md`。长期维护时应把 `mode-decision-matrix.md` 设为唯一真相源，其余文件只做摘要和跳转。

### 7.2 Persona 横切面较大

Persona 同时影响入口、资产、Prompt、模式职责和 QA。新增 Persona 时，应严格按 Persona contract 实现，避免把 Persona 特殊规则写进模式文件。

### 7.3 入口文件持续膨胀

`SKILL.md` 应保持为编排层。新的视觉细节、模式细则、资产规则和 QA 项应优先进入 references 或 profile，而不是继续堆入入口文件。

## 8. 演进约束

新增能力时，按以下顺序判断归属：

1. 这是所有模式都需要的规则吗？是则进入 `common-*`。
2. 这是某个 IP 的身份或资产吗？是则进入 `ip-profiles/<ip-id>/`。
3. 这是某种视觉容器特有的规则吗？是则进入对应 Mode Profile。
4. 这是某个平台的调用方式吗？是则进入生成适配边界。
5. 这是生成结果的判断标准吗？是则进入公共或模式 QA。

如果一条规则无法归入以上五类，先不要新增文件，先确认它是否属于已有层的职责。

## 9. 架构验收清单

- [ ] 新增 IP 不需要修改模式的视觉规则。
- [ ] 新增模式有独立的结构锁和模式 QA。
- [ ] `none` Profile 可以跳过所有默认角色资产。
- [ ] Persona 规则没有散落进多个模式文件。
- [ ] Prompt 可以通过槽位替换风格或生成平台。
- [ ] 公共规则没有写死具体 IP 名称和资产路径。
- [ ] 新模式已补充路由、Quick Start、SKILL 跳转和 eval。
- [ ] 生成失败可以定位到内容、资产、Prompt、生成或 QA 中的单一层。
- [ ] 交付目录和文件命名不会覆盖已有资产。
- [ ] 多图或高推断任务保留 Task / Plan / Render / QA Card。
