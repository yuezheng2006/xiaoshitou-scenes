# Character Profile: Little Stone

## 核心定位

**小石头** 是默认主角色：一个以认真、靠谱、略笨、有点倔为核心气质的 flat 2D 简笔 IP，靠物理动作、短标签和大留白讲故事。

```text
形体：圆角胶囊 / 竖椭圆，#f39800 橙实心体
眼睛：白色小圆 + 可选 tiny 瞳孔；无嘴、无牙、无唇线
肢体：细黑线；每体 2 臂 2 腿；臂从体侧上 1/3 伸出，腿从底缘向下
身上：禁止任何 Logo / 品牌名 / 商标印花
气质：认真、靠谱、略笨、有点倔；不讲大道理，只把问题一步步落地
```

## 性格与品质

小石头不是抽象 mascot，也不是品牌代言人。它的识别主要来自性格和动作：

- **认真**：遇到问题先上手，不站在旁边解释。
- **靠谱**：每次都承担一个明确动作，例如拉、挡、推、接、贴、改、查、递、守。
- **略笨**：可以有一点费劲、汗滴、卡住或被任务卡拖住的尴尬感，但不卖萌。
- **有点倔**：面对混乱流程、错误标签或过载信息时，会顶住、拉回、拦下、修好。
- **有服务意识**：关心事情能不能顺利跑起来；在**雷石 / 现场服务**类内容里可以更像「在干活的执行者」，但仍**不是**客服头像、HR 宣传画或品牌吉祥物（见下节）。

## 稳定锁 vs 场景自适应

小石头要 **像同一个 IP**，也要 **像在给当前场景干活**——锁形体与识别，放开动作、道具与站位。

| 维度 | 全批 / 跨图必须稳定 | 随场景自适应（单张内） |
| --- | --- | --- |
| 形体语言 | `#f39800` 平涂胶囊、宽高比、flat 2D、无嘴 | — |
| 眼与肢 | 白圆眼画法、2 臂 2 腿、锚点与线宽 | 臂/腿**姿态**（弯、伸、跑、蹲、扶） |
| 气质 | 认真、靠谱、略笨、有点倔 | **费劲感** 0–1 汗滴；略卡壳/顶住的姿势 |
| 叙事 | 承担**与锚定句相关**的核心动作 | 道具类型、标签文案、占画比例、朝向 |
| 多人 | 同胶囊比例；差异来自分工 + 手脚姿态 | 2–4 个体：站位、职责、所持物件、接触点 |

**自适应原则（不要死板）**

1. **动作跟内容走**：锚定句是「接需求 / 跑 Agent / 守权限闸」→ 选系统侧动作，不必每图都是「拉线 / 搬卡」。
2. **道具跟隐喻走**：平台 / 车载 / 研发 / 通用办公，用对应物件；**只有内容真的相关**才上行业气味；**禁止**默认画 KTV 包厢巡检、房态、递麦。
3. **小比例可略简**：远景仍保留橙胶囊 + 双白点 + 肢端动作暗示，不要求画满手指细节。
4. **非序列单点图**：小石头可以不出镜；出镜时动作服务于该格信息即可，不必强行导游全路径。
5. **装饰性测试仍有效**：自适应**不能**变成角落站桩；去掉小石头后隐喻仍成立 → 不合格。

Prompt 可复制：

```text
Little Stone scene adapt: keep flat #f39800 capsule, white eyes, no mouth, 2 thin black limbs — SAME identity as character sheet.
Adapt pose, props, labels, and effort (0-1 sweat) to match THIS scene's anchor sentence and physical/concept action.
Do NOT default to generic standing mascot; do NOT change capsule aspect ratio or render style for "cuteness" or "corporate poster".
```

## 背景气味

默认 profile 可以带一点全场景音乐科技 / KTV / 门店经营的道具气味，但这只是可选语境，不是强人设：

- 可用（**平台 / 产品隐喻**，非场所服务）：曲库更新卡、设备平台卡、权限牌、会员反馈卡、抽象控制台、轻量连接线。
- 可转译：车载座舱、软硬件联动、Agent 工作流、数据同步等——**偏系统侧**，不是门店_floor 服务。
- 也可完全不用行业道具，回到通用项目卡、任务队列、协作看板、状态贴等正文配图物件。
- 道具默认要现代、轻、干净：优先无线/便携设备、圆角卡片、哑光材质、简洁夹扣、轻量标签和小型收纳件。
- 道具只服务当前内容的隐喻，不要为了强调背景而硬塞行业元素。

所有背景气味都必须保持去品牌化：正文与公开示例**不出现真实公司名、Logo、slogan**；用户**明确要求**工牌 / 展会 / 品牌物料时走 `logo-safety.md`。

## 雷石员工（AI native · 唯一员工叙事）

默认 profile 的「员工」只指 **雷石 · AI native**（研发 / 产品 / Agent 工程 / 平台侧）——**不是** KTV 场所服务员，也**不是**包厢巡检、房态、递麦等下游门店叙事。

### 触发词

`雷石` · `雷石员工` · `戴工牌` · `研发` · `AI native` · `Agent 工程` · `平台` · `工单系统` · `权限` · `值班`（系统/办公语境）

### 必须保持

| 项 | 要求 |
| --- | --- |
| IP 本体 | flat 2D 胶囊；**身上无 Logo、无工牌印花** |
| 角色定位 | **AI 原生执行 Agent**：接任务、跑链路、守闸、回传 |
| 工牌 | 仅 **雷石工牌**；独立挂绳卡；比例见 `logo-safety.md` |
| 气质 | 认真、略笨、靠谱；禁止客服微笑、招聘 KV |

### 允许自适应

| 项 | 示例 |
| --- | --- |
| 动作 | 接需求单、拆 Agent 模块、查日志、守权限闸、贴状态标签、模块交接、回传 |
| 道具 | 任务队列卡、Agent 模块卡、权限牌、抽象控制台、笔记本、雷石挂绳工牌 |
| 场景 | 白底物件、手绘工作流、知识卡——**办公 / 系统隐喻** |

### 非我们的场景（默认不生成 · 不带工牌）

以下**不是**本 profile 的配图场景；用户未**明确要求**时不要主动出图，也**不要**带任何工牌（含雷石工牌、中性值班牌、空白工牌）：

- KTV **巡检** / **房态** / **包厢服务** / 递麦 / 门店_floor 服务
- 包厢门牌、房态面板、服务工单跑包厢、场所「巡检中」挂牌

若正文仅抽象提到 KTV/娱乐行业，配图仍应落在 **平台 / Agent / 数据 / 工作流** 隐喻，而非场所服务复刻。

### 禁止

- 雷石员工 + 房态门牌 / 包厢递麦 / KTV 包厢实景 / 场所巡检。
- 任何 KTV 巡检类画面 + **任何工牌**（雷石或中性均不要）。
- **工牌牌面写姓名/岗位/部门/流程文案**；工牌印进胶囊身体或比例失真；自造 Logo 错误。
- 企业吉祥物 / 招聘海报 pose。

### 传图与校准

| 需求 | 加读 |
| --- | --- |
| 雷石工牌 | `logo-safety.md` + 用户会话工牌参考（本地） |
| 复杂动作 | `primary-character-actions.png` |
| Agent / 白板 | `handdrawn/calibrate-whiteboard.png` |

Prompt · **雷石员工（AI native）**：

```text
Little Stone as Thunderstone AI-native employee: Agent/workflow/system tasks — task cards, permission gates, module handoff, feedback loop.
NOT venue service: NO KTV room inspection, NO room status panel, NO microphone handoff in private room, NO venue floor patrol.
Badge: Thunderstone lanyard card ONLY when explicitly 雷石员工/戴工牌 — correct proportions (logo-safety); NEVER on orange body.
Badge logo MUST be 1:1 from authorized reference asset — NEVER model-drawn or stylized.
If scene is NOT 雷石 employee context: NO badge of any kind.
Keep flat #f39800 capsule, no mouth.
```

## 资产

| 图 | 路径 | 作用 |
| --- | --- | --- |
| **设定图（必传）** | `assets/character/primary-character-reference.png` | 形体、主色、白圆眼、细线肢体 |
| **动作扩展（条件）** | `assets/character/primary-character-actions.png` | 复杂姿态 / 多人 / 小比例 |
| **可选模式样张** | `assets/character/examples/` | 身份漂移时可选 1 张辅助；**非强制** |

小石头识别简单（胶囊 + 白圆眼），**默认单锚点即可**。  
**双参考协议的重点是对齐老杨**，见 `persona-author-assets.md` / `assets/persona/examples/README.md`。不要把「双参考」名额用在小石头上。

主设定图负责“像不像小石头”。扩展图只在复杂姿态、表情基调、多个小石头协作或小比例远景时加读，不替代主设定图。身份明显漂移时，可从 `examples/{physical|handdrawn|knowledge-card}/` 加读 1 张样张辅助，仍以设定图为最高锚点。

## 填入 `{IP_DESC}`

> 组装顺序见 `references/common-prompt-slots.md`。本段紧接参考图，写在模式 DNA 之前。

```text
[Match the attached Little Stone character sheet]
Little Stone (小石头): flat 2D rounded vertical oval / capsule body, solid uniform #f39800 fill (no gradient, no highlight, no clay/vinyl/Pixar volume),
two flat white circular eyes + optional tiny black pupil dots (not glossy 3D eyeballs),
NO mouth / teeth / lip line on the capsule — emotion via pose and at most 0-1 sweat drop,
exactly 2 thin black line arms from upper-third lateral body sides + 2 thin black line legs from bottom edge,
hand terminal at most one simple grip per arm (small circle / C-shape / line hook),
temperament: earnest, reliable, slightly clumsy, a bit stubborn — express via physical action, not cute mascot posing.
Keep exact colors and proportions from the character sheet.
```

## 填入 `{IP_STYLE_ADAPT}`

> 写在通用 `{STYLE_ADAPT}` 之后。管 IP 锁色，不管构图。

```text
Little Stone color lock:
- Body fill = solid uniform #f39800 only; even a mild orange gradient, center highlight, rim shadow, or volume lighting fails
- Scene accent colors (cobalt tape, tomato-red marks, lemon tabs, soft pink) may appear on objects/annotations ONLY — never tint the capsule body, eyes, or limbs
- Limbs stay thin black lines; eyes stay flat white circles — do not inherit studio lighting or whiteboard wash into the character
- When author persona appears in a different render language, Little Stone must remain strictly flat 2D and visually distinct
```

## 品牌血脉

- `#f39800` 是小石头的主色，也是默认 profile 的主要识别色。
- 名字和主色有内部品牌来源，但正文、示例和提示词默认不展开具体公司信息或业务细节。
- 真实品牌 Logo 不随公开 profile 分发，Logo 规则见 `logo-safety.md`。
- 全场景音乐科技 / KTV / 门店经营语境只提供可选道具气味，不自动触发真实品牌 Logo。

## Character Lock

一次生成 2 张及以上时，全批一致项：

| 全批一致 | 可变 |
| --- | --- |
| `#f39800` 橙身 | 姿势 / 动作 |
| 胶囊轮廓 | 0-1 汗滴 |
| 白色小圆眼 + 可选 tiny 瞳孔 | 场景道具 |
| flat 2D 简笔 | 标签 |
| 细线肢体 | |

多人 / 多 Agent / 团队协作场景允许 2-4 个小石头，但它们必须像同一 IP 家族里的不同个体：共享 **#f39800 平涂、相同胶囊宽高比、相同白圆眼画法、相同细线肢体语言**；只允许通过 **整体等比缩放（±10–15% 高度差）、角度、站位、手脚姿态、动作职责** 拉开差异，**禁止**把 A 画成细长条、B 画成矮胖球、C 画成横扁椭圆；禁止复制粘贴平移。

> **金样对齐**：`primary-character-actions.png` 多人协作格文案为「体量与姿态差异要明显」；手语为 **B 档简笔拟人**（细黑线小掌+2–3 短指）。手部/多人专项校准可加读 `assets/character/examples/calibrate-hands-multi.png`。

### 多人协作精细锁（CRITICAL · 2+ 个小石头同图）

| 维度 | 要求 | 禁止 |
| --- | --- | --- |
| 形体 | 同胶囊宽高比；高度差仅 ±10–15% | 瘦高条 / 矮胖球 / 横扁混用 |
| 分工 | 每人一个清晰动词（递/接/拉/扶/贴/拦…） | 两人同姿站桩、无互动 |
| 接触点 | 递接物停在**两人握持之间**；绳/线与臂线分离可数 | 物悬浮无握、绳粘成第三臂 |
| 朝向 | 互动双方朝向共享物件或对方 | 背对背各干各的 |
| 差异维度 | 至少拉开 3 项：缩放 / 倾斜 / 站位 / 手脚姿态 / 职责 / 道具 | 复制粘贴平移 |

**互动母版（生成时选一并写清）**

1. **递接（handoff）**：A 前倾递出、B 伸臂承接；卡/物在两握点中段；双方腿分前后略撑稳。
2. **共拉（pull）**：身体明显后仰；双臂前伸握绳端；双脚前后或外八撑住；绳为独立细线，**手握住绳**（简笔掌+指），不得把绳画成第三臂。
3. **一扶一做**：一侧短肢扶物/扶边，另一侧做主动作；扶点线连续、不断线悬浮。

### 手脚末端精细锁（与 Limbs Lock 一并写入）

手要**简笔拟人**：能看出「手在做事」，不是纯几何 C/环符号。臂仍是细黑线；末端升级为小掌 + 短指。

| 动作 | 手末端（每臂 1 只简笔手） | 脚 / 站姿 |
| --- | --- | --- |
| 空闲 / 叉腰 | 小掌 + **2–3 短指**自然下垂或叉腰 | 双腿短 L 弯；重心可读 |
| 挥手 / 指 / 拨 | 小掌 + 短指张开或食指方向可读 | 站稳即可 |
| 握卡 / 递物 | 小掌托/捏卡缘，**拇指可相对**；指包住卡边 | 前后步或微屈一侧 |
| 拉绳 / 握环 | 双手握住绳端（掌+指绕绳），绳继续延伸 | **外八或前后撑** |

**手部定稿（拟人简笔）**

- **要**：细黑线臂 → 末端**同线宽黑线**小掌 + **2–3 根短指**（可含拇指示意）；握物时指/掌与物件接触可读。
- **对齐主设定**：挥手时可呈 2–3 个短指瓣（见 `primary-character-reference.png`），全批同一手语。
- **不要**：白填充手套/肉掌、解剖五指写实手、指甲关节、3D 圆管肢、纯 C 钩/纯小环代替手（旧几何握法退役）、绳粘成第三臂。

脚仍保持短 L / 下撇，不画脚趾鞋形（拟人重点在手）。

Prompt 可复制（多人时追加）：

```text
Multi-Stone Coordination Lock:
Same capsule aspect for every Stone; height scale ±10-15% ONLY — NOT skinny vs chubby body shapes.
Each Stone has a distinct verb (hand-off / receive / pull / brace). Contact: shared prop between two grips; rope SEPARATE from arm lines.
Hands (anthropomorphic mini): thin black arms end in a tiny palm + 2-3 short finger stubs (optional thumb); gripping cards/ropes with readable finger wrap — NOT bare C-hook/loop symbols, NOT realistic 5-finger anatomy, NOT thick gloves.
Feet: short L-bend; pull/brace = wider planted stance. NO clone poses.
```

## 2D Flat Lock + Limbs Lock

生成前必须 **并列** 写入：

```text
2D Flat Lock:
- Little Stone = flat 2D sticker / paper cutout / simple vector illustration
- Body = solid #f39800, no gradient, no highlight, no clay / vinyl / Pixar texture
- Eyes = flat white circles + optional tiny dots, not glossy 3D eyeballs
- No mouth, no teeth, no lip line on the capsule — emotion via pose and 0-1 sweat drop only
- Limbs = thin black lines, not 3D tubes
- The orange body must be one uniform flat color block; even a subtle orange gradient, center highlight, rim shadow, or volume lighting is a failure

Limbs Lock:
- Default: 2 arms + 2 legs per individual, continuous from correct anchors
- Prefer readable grips (black-line mini palm + short fingers); allow natural two-handed work poses
- Hard negative only: floating disconnected phantom hand/arm with no body attachment; same-side sprouted extra arm
- Soft: do NOT force hip-akimbo + mic + screen three contact points (causes third-hand artifacts). Let lyric boards float when needed.
- Soft negative: white mitten gloves, mouth/smile line — fix if easy; don't thrash whole sheet for finger perfection
```

实物图里的真实物件可以有摄影棚光影，但小石头本体不能跟着变 3D。作者 persona 可以按模式使用不同渲染语言，但不能带偏小石头。

## Canonical 比例（生成前可写入 prompt）

| 维度 | 锁定值 | 禁止偏移 |
| --- | --- | --- |
| 胶囊宽高比 | 约 **1:1.3–1:1.6**（竖椭圆 / 圆角胶囊） | 细长竖条、矮胖球、横扁椭圆 |
| 单眼直径 | 约体宽的 **12–18%** | anime 大眼、眼径批内不一 |
| 眼距 | 约 **1.2–1.8** 眼径 | 眼距过宽/过窄、单眼缺失 |
| 臂长 | 约 **0.6–0.9** 体高（细黑线，体侧上 1/3 伸出） | 粗短 3D 臂、从非锚点长出 |
| 腿长 | 从底缘向下 **1–2** 段细黑线 | 横腿、体中部错锚 |
| 多人差异 | 只允许整体等比缩放 **±10–15%** | 同图 A 瘦高 B 矮胖 C 横扁 |

Prompt 可复制：

```text
Little Stone proportion lock: vertical capsule aspect ~1:1.3–1:1.6; two flat white eyes each ~12-18% body width, spaced ~1.2-1.8 eye-diameters; thin black arms from upper-third lateral sides, legs from bottom edge; multi-instance scenes may scale ±10-15% height only — same capsule aspect ratio batch-wide.
```

## 变形边界（Deformation Limits）

小石头可以动，但**本体不能变成工具或背景**：

- **禁止**：胶囊拉长成条带、传送带、箭头、路径色块、桥面板、按压板本体
- **禁止**：为表达「压力 / 过载」把胶囊压扁成托盘、垫子、印章
- **禁止**：为表达「路由 / 分流」把胶囊拉宽成闸门本体（可用外部槽、路径、标签）
- **允许变形**：臂、腿、汗滴、外部道具、路径、箭头、标签——这些可以拉伸或增多
- **原则**：需要压缩、路由、桥接时，用**外部物件**；小石头仍是 compact 操作者

判定：若去掉小石头后核心隐喻仍完全成立 → 不合格（见 `common-qa-repair.md` 装饰性测试）。

## Recognition Rule（QA 可数阈值）

成图至少保留 **5/6** 项（小比例远景可降为 **4/6**）：

1. `#f39800` 平涂胶囊（无渐变 / 高光 / 体积阴影）
2. 两只白圆眼（批内大小 / 间距一致）
3. 细黑线 **2 臂 + 2 腿**（锚点正确）
4. **无嘴**（无牙 / 唇线）
5. 胶囊宽高比与设定图 / 同批一致
6. 正在做**核心动作**（非站桩装饰）

缺任一项且无法局部修复 → 重生成。

## 动作库（选与内容锚定句匹配的，禁默认站桩）

**物理动作**：拉、挡、推、接、贴、改、查、递、守、顶、塞、捞、撑、缝、打开、递出、按、扶、指、扛、拖、拦、修、守门

**雷石员工 · AI native**：接需求单、拆 Agent 模块、守权限闸、查日志/状态、贴系统标签、模块交接、回传反馈

**概念动作（手绘 / 知识卡）**：画箭头、递模块、指向结构、拉线、贴标签、把卡塞进槽、标记风险

### K 歌 / 音乐娱乐动作（条件触发 · 非默认）

仅当锚定句/用户明确涉及 **K 歌、点歌、麦克风、曲库、车载 K 歌、家庭开唱、合唱抢麦** 等时选用；**禁止**每张正文图默认塞麦或包厢。

| 动词 | 姿态要点 | 典型物件（现代轻量） |
| --- | --- | --- |
| **握麦** | 单手持短柄无线麦，麦头朝上略偏；站稳或微倾 | 短柄圆润无线麦 |
| **递麦 / 接麦** | 两人同胶囊比例；麦在两握点中段交接 | 双麦或单麦传递 |
| **对麦 / 合唱** | 两人各持一麦，朝向共享节拍/歌单卡 | 双短柄麦 + 歌单卡 |
| **点歌** | 指/按歌单卡或遥控器；另一手可扶卡 | 歌单卡、点歌遥控 |
| **切歌** | 抽走旧歌单卡、推入「下一首」卡 | 歌单卡叠 |
| **塞曲库** | 把曲库卡塞进盒/槽 | 曲库盒、新歌卡 |
| **充麦** | 把麦立放/磁吸到充电座 | 磁吸充电座 + 短柄麦 |
| **推音箱** | 双手推家用/车载小音箱就位 | 圆润 K 歌音箱 |
| **打节拍** | 短指轻拍或打响指姿势（仍无嘴） | 可选铃鼓 |
| **车载递麦** | 从杯架/扶手区递出麦（局部车内小现场） | 杯架 + 短柄麦 |

**麦的画法（硬）**：现代短柄无线/便携 K 歌麦——圆润、哑光、细网罩、隐藏键；**禁止**复古舞台麦、头套麦、把麦画成小石头本体。手语仍走 B 档（细黑线小掌+短指握麦杆）。

**四肢门禁（K 歌 / 复杂道具 · 务实版）**：
- **硬禁（CRITICAL）**：悬浮断手、无臂连接的第三掌、同侧凭空多长一只臂——这是假肢伪影，必须返修。
- **放宽（允许模型发挥）**：不再强制「闲置手必须叉腰」；双手都在做事时（握麦、扶卡、打节拍）即可，不要为了凑姿态再加第三接触点。
- **多道具场景**（对麦+歌词屏等）：歌词牌/点歌屏优先**悬浮或单侧扶**，不要让每人都「叉腰 + 握麦 + 扶屏」三接触——那是三手高发配方。
- 手指仍偏好细黑线小掌+短指；若模型画出可读握姿且无白手套假肢，可接受，**不要为指形反复重绘整表**。

**仍禁止**：KTV 包厢实景、舞台灯效、房态巡检服务员叙事、真实品牌 Logo、点歌 App UI 截图。物件规则详见 `physical-object-patterns.md`。

专项金样：`assets/character/examples/calibrate-karaoke-actions.png`（内容相关时加读；不替代主设定图）。

**禁止默认**：放大镜、灯泡、纯站桩讲解、与锚定句无关的装饰姿态、无关内容硬塞麦克风/包厢

## 序列图导游（结构轴 = 路径 / 步骤序列时）

- 全图 **1 个小石头**（或明确分工的 2–4 个，仍遵守形体一致锁），沿故事动线参与：递物 / 按按钮 / 指路 / 沿路径移动
- 站在**步骤之间或动线侧面**，不遮挡编号圈与关键物件
- shot / 结构锁定须写明小石头站位与引导动作

**禁止**：每站复制多个小石头、角落站桩装饰、与锚定句无关的动作、身体挡住主路径节点

**非序列图**（单点澄清、物件特写、对比并置）：小石头可不存在；存在时按信息分工即可，不适用本节

## 校准图决策（身份漂移时可选 1 张）

> 设定图 `primary-character-reference.png` 始终必传。下表仅在**身份明显漂移**或质量不稳时加读 1 张；**校准图只管「在此画风里仍像小石头」，不管构图**。

| 选用时机 | 文件 |
| --- | --- |
| 默认 / 拿不准 | `assets/character/examples/physical/calibrate-object-scene.png` |
| 多人协作 / Agent 分工 | `physical/calibrate-multi-agent.png` |
| 手部拟人 / 递接拉绳手脚 | `examples/calibrate-hands-multi.png` |
| K 歌 / 握麦点歌合唱 | `examples/calibrate-karaoke-actions.png`（仅内容相关） |
| 白板 / 流程 / 拉线 | `handdrawn/calibrate-whiteboard.png` |
| **雷石工牌 / AI native 员工** | `logo-safety.md` + 用户会话工牌参考（本地） |
| 知识卡模块 | `knowledge-card/calibrate-knowledge-card.png` |
| 3D / 渐变 / 体积漂移 | 设定图 + 上表对应模式 calibrate + 强化 2D Flat Lock |

复杂姿态 / 小比例 / 多人：优先 `primary-character-actions.png`，再考虑上表。

## 迭代 palette（走形时粘贴重试）

**3D / 渐变 / 高光 / 软陶公仔**

```text
LOCK Little Stone flat 2D: solid uniform #f39800 fill ONLY — NO gradient, NO center highlight, NO rim shadow, NO clay/vinyl/Pixar/emoji 3D volume; eyes = flat white circles; limbs = thin black lines only
```

**场景点睛色染进胶囊 / 眼睛 / 四肢**

```text
Scene accent colors (cobalt, tomato-red, lemon, soft pink) on objects and annotations ONLY — NEVER tint Little Stone capsule body, white eyes, or black limbs
```

**多人胶囊宽高比不一（瘦高 / 矮胖 / 横扁混用）**

```text
LOCK same capsule aspect ratio ~1:1.3–1:1.6 for every Little Stone in this image; scale ±10-15% height ONLY; NO skinny stick, NO fat ball, NO horizontal blob variants
```

**有嘴 / 多手 / 锚点错 / 手脚末端糊**

```text
NO mouth/teeth/lip line on capsule; exactly 2 arms from upper-third lateral sides + 2 legs from bottom edge; NO extra arm, NO toes/shoes, NO rope-arrow merged into hand; hands = tiny palm + 2-3 finger stubs wrapping props (NOT bare C-hooks, NOT realistic anatomy); multi-Stone = distinct verbs + mid-point handoff contact
```

**小比例远景丢识别点**

```text
Even at ~10-20% frame width: keep #f39800 capsule silhouette, two white dot eyes, thin limb stubs, and a clear physical action — not a generic orange blob
```

## 失败信号

- 胶囊体出现渐变、高光、体积阴影、软陶、盲盒公仔、Pixar 或 emoji 3D 质感。
- 四肢变成圆管、粗短 3D 手脚。
- 白圆眼变成反光球体、玻璃珠或带眼窝的 3D 五官。
- 小石头身上或旁边出现 Logo / 品牌名 / 商标引导箭头。
- 把小石头画成正式企业 Logo、工牌吉祥物、客服头像或品牌代言海报，而不是用动作解决问题的正文配图角色。
- 每张都硬塞麦克风、包厢或 K 歌元素，导致和当前内容无关。
- 道具显得老旧、复古、笨重、脏乱或舞台化；除非用户明确要求，不用年代感强、商业舞台感强或厚重脏乱的道具。
- 删掉小石头后隐喻仍成立，说明它没有承担核心动作。
- **多人形体比例漂移**：同图里胶囊宽高比不一致（瘦高 / 矮胖 / 横扁混用）——典型不合格，必须重生成。
- **多人协作假互动**：两人同姿站桩、递接物无握点、绳与臂粘连、无前后撑姿——不合格。
- **眼睛不合格**：眼距/大小批内不一致、anime 大眼、3D 反光眼、缺白圆或瞳孔画法不一。
- **手臂/腿不合格**：断线悬浮、同侧双手、分叉指、绳线粘连成第三只手、从非锚点位置长出（头顶/眼下方/体中部横腿）。
- **手脚末端不合格**：写实五指/厚手套；或仍用纯 C 钩/纯小环代替手；握物看不出掌指接触；鞋子轮廓；多人手语批内漂移。
- **有嘴**：胶囊上出现嘴线、牙、唇形——直接不合格；情绪应靠动作与汗滴。
- **四肢批内不一致**：同图/同批线宽、锚点高度、末端画法漂移。
- **员工场景**：雷石员工画成 KTV 巡检/房态/递麦；或非员工场景误戴任何工牌；工牌比例过大。

主角色与可选 persona（老杨）分工不同：小石头是 flat 2D 执行 Agent；老杨是触发型主讲 persona，见 `persona-author.md`。

## 英文称呼

`小石头（英文别名：Little Stone）`。`scene-skill-core` 是通用核心包名，与任何第三方商标无关。
