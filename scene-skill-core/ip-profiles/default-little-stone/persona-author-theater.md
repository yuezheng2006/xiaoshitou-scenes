# 老杨小剧场（视觉印记 · 独立入口）

> **最新人物造型覆盖（2026-08-10）**：老杨身高 **182cm**、体重 **86kg**，腿较长，上短下长约 4:6；鞋 = 米白厚底休闲鞋，造型对齐 New Balance 1906R / 2002R。小剧场服装跟设定图 hero outfit 锁死；体态与鞋款识别遵守本覆盖。旧文 183/90 一律作废。

> **路径 C**。与路径 B **分流**（有「小剧场」走 C，无则 B）。  
> **默认单人**；同句出现「小石头」→ **C 组合**（潮玩底 + flat 2D 小石头）。  
> **细致版备忘（本地）**：`.temp/visual-imprint-feature-analysis-v2.md`。Adrian 原文留档：`.temp/adrian-punk-visual-imprint-ip-illustration.md`。

## 核心定位

长文 / 教程 / 方法论插图用的**视觉印记**——读者能「看见」流程、处境、关键动作，而不只靠文字。

```text
路径 A  小石头单 IP
路径 B  老杨 × 小石头双 IP（无「小剧场」）
路径 C  老杨小剧场（视觉印记）
        · C 单人：仅老杨（默认）
        · C 组合：小剧场 + 小石头（潮玩底，小石头 flat 2D）
```

```text
Adrian 两步法（本路径）：
  ① 先有一张稳定的 IP 角色设定图（风格化，非真人）→ Confirm Gate
  ② 再用「设定图 + 正文/主题」生成 IP 小剧场
长文额外：①⑤ 之间插入 Imprint Plan Card（先选点，再开批）
```

## 隐私边界（硬）

- **禁止**向生图传入真人照片、会话自拍、可识别真人参考。
- **禁止**把真人照写入公开仓库、prompt 示例、profile 资产路径。
- 用户说「用这张自拍当小剧场设定」→ **拒绝**，改走风格化设定图重生。
- 小剧场身份只来自**已风格化的设定图** + 公开 persona 金样（`flat-ip-sheet`、`panorama-handdrawn`、`face-lock`、`handdrawn-body`）。
- 用户本地 `.temp/` 试跑图可保留，**不得**提交进 Git。

Adrian 原文写「用自己的照片生成设定图」——本仓**不采用**该步骤，改为「用风格化 IP 设定图替代」，避免隐私泄露。

## 触发词

**硬门槛：必须含 `小剧场`。**

| 类型 | 词 |
| --- | --- |
| 入口 | `小剧场` / `老杨小剧场` / `IP小剧场` |
| 组合 | 同句再出现 `小石头` / `Little Stone` → **C 组合** |
| 子指令 | `流程拆解图` / `核心动作图` / `一鱼两吃` / `老杨设定图` / `IP设定图` |
| 概念别名 | `视觉印记`（须与「小剧场」同现，不能单独触发；Plan/Render 卡片标题可写「视觉印记 · 小剧场」） |
| 场域（可选） | `· 车载场景` / `咖啡馆` 等 → 只当内容场域，不切路径 B 模式 |

**分流**：仅 `老杨` 无「小剧场」→ 路径 B。含「小剧场」→ 始终 C；再加「小石头」→ C 组合（**不再**打回 B）。

## Agent 执行序（细致版 · Punk 编译）

```text
① 触发确认：含「小剧场」→ 路径 C（± 小石头 → 组合）
② Imprint Plan Card（长文必做；单主题/单金句可短卡）
③ 设定图 Confirm Gate：非 APPROVED → 只出/确认设定图，停
④ 场景轻确认门：缺图型且未 auto → 推荐 2–3 图型后停问
⑤ 编译 prompt：theater-prompt-blueprint × vinyl-theater × 恰好一个 shape
⑥ Preview：每批先 1 张身份预览（脸/发/眼镜/身材/服鞋）
⑦ Render：按点位出图（拆解 / 动作 / 一鱼两吃）
⑧ QA：对照本文件「场景 QA」+ checklist
⑨ 交付：图 + 每张一句「这张让读者看见什么」
```

**禁止**：长文任务跳过 Plan Card 直接开批。  
**禁止**：把 `STYLE.md` / shape META 原文第二段粘贴拼接；必须编成**一条**完整 brief。

### 编译读取链（出场景必读）

```text
references/theater-prompt-blueprint.md          # 形状蓝图 + 轻确认门 + Likeness Policy
ip-profiles/.../theater-styles/vinyl-theater/   # 唯一风格原子 META + STYLE
ip-profiles/.../theater-shapes/{shape}/META.md  # process-breakdown | core-action | one-theme-two-plates
persona-author-theater-prompts.md               # 片段库存（供编译改写，勿直接 concat 完事）
APPROVED 金样（expression-sheet + face-lock + sheet）
```

产物建议：`.validation-output/generation/theater/scenes/prompts/{slug}-{shape}.md` 先落盘，再生图。  
结构校验：`python3 scene-skill-core/scripts/validate-theater-punk.py`

## Imprint Plan Card

长文 / 多点位任务**先出此卡，用户确认或默认可执行后再生图**。单点主题可缩成 3 行短卡，但仍须标明图型与设定图状态。

```markdown
## Imprint Plan Card · 视觉印记 · 小剧场
- 路径：C 单人 | C 组合
- 设定图：DRAFT | PREVIEW | APPROVED（路径）
- 画幅默认：16:9（用户要竖版再 4:5）
- 点位：
  1. [流程拆解|核心动作|一鱼两吃] 输入形态：段落|主题|金句
     锚文：「…」→ 结构/动作：…
- 待确认：…
```

## 设定图 Confirm Gate

设定图 = **人物身份标准**。状态机：

```text
DRAFT → PREVIEW（出 1 张设定图）→ USER_OK → APPROVED_SHEET → 可批场景
任意返修脸 / 发 / 服 / 鞋 / 体态 → 退回 PREVIEW
```

| 规则 | 说明 |
| --- | --- |
| 未 `APPROVED` | **禁止**批量出小剧场场景 |
| 用户说「老杨设定图 / IP设定图」 | 只做 Gate，**不要**同时批场景 |
| 自拍求定妆 | 拒绝；风格化重生 |

| 来源 | 用途 |
| --- | --- |
| **小剧场设定图金样**（已验收 / APPROVED） | 批内最高优先级 |
| `author-persona-flat-ip-sheet.png`（+ navy 对照） | 脸型 / 年龄 / 比例校准（辅） |
| `author-persona-panorama-handdrawn.png` + `panorama` | 手绘 + 实体锁同一人（辅） |
| `author-persona-face-lock.png` | 多场景 / 返修脸漂（辅） |
| `author-persona-handdrawn-body.png` | 全身 **182 / 4:6**（辅） |

**设定图金样（2026-08-20 · expression-sheet v14 APPROVED）**：

```text
assets/persona/theater/author-persona-theater-expression-sheet.png  # 制作表：三视图+表情（脸部身份优先 · v14）
assets/persona/theater/author-persona-theater-face-lock.png         # 唯一脸锁 likeness v2（= face-lock-approved）
assets/persona/theater/author-persona-theater-sheet.png             # 小剧场全身设定图（服装/体态）
.validation-output/generation/theater/expression-sheet/laoyang-character-ref-sheet.png  # 工作副本
```

备忘：likeness v2（面颊有肉软圆方、粗黑方框眼镜）；潮玩哑光不追照片级；浅色短袜 + NB 2002R；宽松卡其 Bermuda。  
批场景传图：表情制作表（脸）+ 全身设定图（服/体）优先同传。Gate：`.validation-output/generation/theater/GATE-STATUS.md`（**APPROVED**）。

风格参考（仅画风，非身份）：`.temp/theater-punk-refs/adrian-punk-style-sheet-ref.png`

### 设定图版式检查

- [ ] 大标题含「老杨小剧场」或「角色设定」
- [ ] Hero 3/4 站姿 + 小圆底座
- [ ] 配件特写 + 色板色卡
- [ ] 底栏四向 turnaround（前/左/后/右）
- [ ] 无小石头（设定图阶段）
- [ ] vinyl 哑光，非半写实 / 非照片级

## 输入契约（第二步必选一种）

使用小剧场 prompt 时，**同时提供两项**：

1. **角色设定图**（`APPROVED` 必传）
2. **一段话** 或 **一个主题** 或 **一句金句**

### 段落输入（Paragraph）

```text
输入：120–400 字连续段落（或用户指定段落）
默认产出：1 张流程拆解图（用户指定动作图则改）
抽取：
  1. 找 1 个主结构（步骤链 / 对比 / 循环 / 漏斗 / 层级）
  2. 抽 3–5 个节点标签（≤6 字/标签）
  3. 人物动作 = 指向当前关键节点，或走在路径上
禁止：整段字贴进画面；模块 >5
```

### 主题输入（Topic）

```text
输入：一个可命名的主题 / 方法名
默认：一鱼两吃（除非用户只要一张）
Agent 填空（主题配方卡）：
  主题：{TOPIC}
  拆解板：结构类型=步骤|对比|循环|层级 ；模块=… ；姿态=指向/批注/行走
  动作板：隐喻动作=… ；道具≤2 ；文案≤3 短标签
  两板：同一设定图，零换装
```

### 金句输入（Quote）

```text
输入：一句可独立传播的命题
默认：核心动作图 1 张（隐喻优先）
可选升级：一鱼两吃（拆解「为什么成立」+ 动作「怎么做」）
画面：≤1 行主标题 + 0–2 辅标签
```

示例金句（Adrian）：「写，是所有内容形态的底层能力」→ 可一鱼两吃。

## 跨图身份锁

| 跨图不变（硬） | 只改 |
| --- | --- |
| **我们的**脸型、发型、眼镜 | 动作、姿态 |
| **Hero outfit**（见下）服装、配色、鞋子、配件 | 场景结构、道具、信息密度 |
| 身材 **182cm / 86kg** · 4:6 · 腿较长 | 表情预设 E0–E4（显式选一） |
| 视觉年龄 ~36–38；北方骨相；非日韩风 | |

### Hero outfit（统一）

```text
上衣：藏蓝 crew neck T（navy）
下装：卡其/米色**宽松休闲短裤**，微微过膝（盖过膝盖上缘一点；裤腿有余量）
袜：浅色休闲短袜（米白/浅灰；短款 ankle，鞋口上方可见一截）
鞋：New Balance **2002R**（灰橄榄复古跑鞋，大写 N；以 APPROVED 设定图为准）
配件：左手黑色运动表
眼镜：以 APPROVED 设定图为准（v14 face-lock：粗黑软方框大镜片）
体态：182cm / 86kg · 结实匀称 · 头身约成人 1:7；观感约 180，禁 1.9m 竹竿、禁 170 短腿敦实
```

用户改设定图并重新 APPROVED 后，场景跟新设定图走；未改则禁止换装。

**风格化面相（无真人 · 我们自己的）**：

| 部位 | 锚点 |
| --- | --- |
| 年龄 | ~36–38，**成熟一丝丝、不显老**；无法令纹/深抬头纹；不显幼态 |
| 颧骨 | **略高、有支撑**；中脸有体积；脸型 **软圆方憨厚、面颊有肉**（likeness v2）——**禁止**幼态娃娃圆脸 / 削尖 V 脸 / 瘦长窄脸 |
| 族裔 | 北方中国男性骨相；**禁止**日韩偶像风 |
| 眉/唇/胡茬 | 自然粗眉；厚下唇；**胡茬主要在两腮侧短茬**，嘴周/上唇不明显（禁八字胡、禁嘴周浓茬） |
| 发型 | **我们的**：短直硬发 3–5cm；**刘海不对称，右侧略长**——禁止软卷/对称齐刘海/贴头皮毛寸/尖角发际 |
| 眼镜 | **我们的**：粗黑软方框大镜片（跟 v14 face-lock；非细丝金圆框、非 Adrian 深棕潮男框） |

**身材**：182cm / 86kg，腿较长，上短下长 4:6；**一眼高于普通 ~175 成年男**；运动场景用站立/微屈膝，禁止深蹲压成 1:1 / 禁止短腿敦实玩具比。

## 风格分界（硬 · 2026-07-15 定稿）

深度参考 Adrian Punk「视觉印记」：**除形象与发型外，其余跟 Adrian**。

| 我们自己的（硬锁 · 不得漂成 Adrian 本人） | 可跟 Adrian 参考 |
| --- | --- |
| **神似锚点**（不追照片级 1:1）：软圆方憨厚有面颊体积 · 粗黑软方框眼镜 · 短硬上冲发 · 下唇不薄 · 粗眉 | **画风（硬）**：Adrian 同款 **3D 潮玩 / vinyl-toy**——哑光、柔光；**禁止写实皮肤/照片级**（风格原子：`theater-styles/vinyl-theater`） |
| **发型**：短直黑发 **3–5cm**，**硬直发质感**；刘海**不左右对称，右边略长**——**禁止卷/波浪/蓬松软刺、禁止对称齐刘海** | **设定图版式**：大标题 + hero 站姿 + 配件特写 + 色板 + 四向 turnaround |
| **身材**：**182 / 86** · **一眼偏壮**（微健壮 + 小肚子，禁偏瘦白领）· **上短下长 4:6** · **腿修长且略粗壮** · 头身约成人潮玩 1:7（禁大头矮比例 / 禁平均 175） | **服装模板**：见 Hero outfit |
| | **图型语法**：流程拆解图 / 核心动作图 / 一鱼两吃；人物进图内指向批注，非角落贴纸 |
| | **场景气质**：同潮玩渲染语言下的小剧场；忌证件照海报、忌半写实插画 |

**神似原则（硬）**：小剧场要的是可读 IP 印记，**不要追求太像真人**。抓 4–6 个识别锚点即可；过度贴脸容易漂成韩范磨皮脸或照片级皮肤。

**一句话定调**：

```text
脸 + 发型 = 我们的老杨
画风 + 版式 + 服装模板 + 小剧场图型 = 跟 Adrian Punk 视觉印记
```

**禁止混轨**：不要用路径 B「扁平黑线 + 米色 T」；不要半写实/厚涂写实；不要照片级；不要漂成 Adrian 本人脸（墨镜寸头潮男）；**禁止扁平韩风偶像脸**。

**默认画风**：与 Adrian Punk 设定图一致的 **3D 潮玩 / vinyl-toy**（哑光、柔光、干净描边、圆形底座设定图语言）。风格参考：`.temp/theater-punk-refs/adrian-punk-style-sheet-ref.png`。身份金样：`assets/persona/theater/author-persona-theater-sheet.png`（APPROVED）。

## 图型与预算

图型 = **shape**（`theater-shapes/*/META.md`）。画风 = 唯一 **vinyl-theater**。出图时用 blueprint 编译，勿多风格混贴。

| 图型 | shape id | 默认输入 | 预算（硬） | 画面 |
| --- | --- | --- | --- | --- |
| **流程拆解图** | `process-breakdown` | 段落 / 主题 | **1** 核结构 + **3–5** 模块 + 短中文标签；人物约 **25–40%**；默认 16:9 | 结构可读；老杨在图内指向/批注/走路径，**禁止角落贴纸** |
| **核心动作图** | `core-action` | 金句 / 处境 | **1** 个主动作；道具 **≤2**；文案 **0–3** 短标签 | 决定性瞬间 / 隐喻手势；多动作并列 = 不合格 |
| **一鱼两吃** | `one-theme-two-plates` | 主题（默认） | 拆解 + 动作各 1；身份完全同一设定图 | 见下节编排 |

### 流程拆解 · 构图母版

```text
[左/中] 结构骨架（箭头 / 步骤块）
[人物] 站在结构旁或踩在路径上，手指/笔指向「当前步」
[右/下] 至多 1 个结果区或风险注
背景：潮玩柔光干净底，忌办公室写实
指向失败：改持笔/棍指向（见 prompts · Pointing Anatomy Lock）
```

### 核心动作 · 选型库（可扩）

```text
指向关键一击 · 拉开遮挡 · 按下开关 · 把两块拼上 · 挡住分叉 ·
把「写」托在手里 · 把漏斗扶正 · 从混沌里抽出一条线
```

### 一鱼两吃 · 编排（硬序）

```text
1) 确认设定图 APPROVED
2) 填主题配方卡（见「主题输入」）
3) 先出 Plate A（流程拆解）预览 → 身份 OK
4) 再出 Plate B（核心动作），强制复用同一设定图引用
5) 两张一起交：同脸同服同鞋；仅姿态/场景不同
命名建议：{topic}-process.png / {topic}-action.png
```

## 读取链

```text
persona-author-theater.md
  → references/theater-prompt-blueprint.md
  → theater-styles/vinyl-theater/{META,STYLE}.md
  → theater-shapes/{process-breakdown|core-action|one-theme-two-plates}/META.md
  → persona-author-theater-prompts.md（片段库存，供编译改写）
  → 设定图金样（APPROVED 必传）
  → C 组合时 + character.md + primary-character-reference.png
  → persona-author-identity.md（QA / 返修）
```

**不要读**：`persona-scene-patterns` 双 IP 强制规则（C 组合也不套「每张必须握手戏」）。  
**不要读**：Punk Cover 的 `styles/*` 封面原子当作小剧场画风菜单。

## C 组合（小剧场 + 小石头）

| | 规则 |
| --- | --- |
| 画风 | 潮玩 vinyl 为主；老杨跟金样 |
| 小石头 | flat 2D `#f39800` 胶囊，**禁止** 3D 同化 |
| 权重 | 老杨约 **70–85%** 画面职责（讲/指/批）；小石头执行点缀，**可不出现在每张** |
| 职责 | 老杨主讲/指向/批注；小石头执行/递物/协助（可选配角，非强制每张双人互动） |
| 传图 | 金样 + `primary-character-reference.png`（必要时 + actions） |
| 场域 | 「xx 场景」= 道具/背景语境，不默认切实物/手绘模式 |
| 一鱼两吃 | 两板都允许小石头；老杨身份仍跟设定图锁 |

## 场景 QA（每张）

- [ ] 与设定图同一人、同套 hero outfit（藏蓝 T + 卡其短裤 + NB 造型米白厚底鞋 + 运动表）
- [ ] 只改姿态 / 表情 / 场景；未换发 / 镜 / 装
- [ ] 流程拆解：模块 3–5；人物非贴纸；约 25–40% 画面
- [ ] 核心动作：主动作唯一；道具 ≤2；文案 ≤3
- [ ] C 单人无小石头；组合则小石头 flat 2D、无 3D 卵石
- [ ] 指向手臂解剖可读（或改持笔）
- [ ] 交付附一句「这张让读者看见什么」

## 硬性底线

- 设定图 + 场景：**同一张我们自己的风格化脸**；服装配色鞋与设定图一致。
- **形象+发型=我们的**；画风/版式/服装模板/图型可跟 Adrian——**禁止**漂成 Adrian 本人脸或寸头 buzz。
- **禁止**真人照、**禁止**证件照/履历海报；**C 单人**默认无小石头；**C 组合**才出小石头且须 flat 2D。
- **禁止**换发型/镜框/主色穿搭（跟设定图走）；**禁止**把路径 B 米色教学手绘当小剧场默认。
- 多场景：先 1 张预览（脸/发/眼镜/身材/设定图一致）再批跑。
- 长文：先 Imprint Plan Card；设定图非 APPROVED 禁止开批。
- 场景 prompt：**blueprint 编译**（`theater-prompt-blueprint.md` × `vinyl-theater` × 一个 shape）；禁止 STYLE 原文二段粘贴。
- 缺图型且未 `auto`：先走场景轻确认门，再渲。

## 与路径 B

| | B 双 IP | C 单人 | C 组合 |
| --- | --- | --- | --- |
| 触发 | `老杨` 等（无小剧场） | 含 `小剧场` | `小剧场` + `小石头` |
| 目的 | 协作配图 | 长文视觉印记 | 潮玩印记 + 执行配角 |
| 画风 | 按实物/手绘等模式 | 潮玩 vinyl | 潮玩 vinyl + flat 2D |
| 输入 | 模式 + 双 IP | **设定图 + 段落/主题/金句** | 金样 + 小石头锚点 + 同上 |
| 服装 | 米色 T 锁（双 IP） | **Hero outfit（藏蓝 T）** | 同 C 单人 |
| 编排 | 模式 Task Card | **Plan Card + Confirm Gate** | 同 C 单人 |
