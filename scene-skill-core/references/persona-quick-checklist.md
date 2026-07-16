# Persona 快速检查清单

**目标**：触发 persona 后 5 秒内完成决策，无需跳转多个文件。

本文件汇总双 IP 生成的 CRITICAL 项；通用机制仍在 `common-persona-routing.md`，完整身份规范仍在 `persona-author-identity.md`，此处只提供快速决策路径。

---

## 第一步：确认触发（5 秒决策）

| 触发词 | 判断 |
|--------|------|
| **含「小剧场」**（`小剧场` / `老杨小剧场` / `IP小剧场`） | → **改走路径 C**：`persona-theater-checklist.md`（本文件不适用） |
| 小剧场 + 小石头 | → 仍走路径 C **组合档**（本文件不适用） |
| 老杨、yuezheng2006、老杨和小石头、老杨 IP 图解、让我和小石头一起、作者、我本人、我的数字形象（无「小剧场」） | ✅ 触发双 IP persona（路径 B） |
| 小石头、小石头实物图、小石头手绘图、未提及老杨 | ❌ 单 IP，不读本文件 |

**触发后立即确认**：
- 用户是否明确说"先推荐 / 先分析 / 先不生图"？→ 先输出双 IP 出图方案推荐
- 用户是否直接要生图？→ 继续第二步

---

## 第二步：选互动场景类型（必选其一）

| 场景类型 | 适合内容 | 分工模式 |
|---------|---------|---------|
| 1. 白板拆解 | 流程、方法论、系统结构、Agent 工作流 | 老杨画结构/批注，小石头拉线/搬模块 |
| 2. 知识卡调度 | 步骤、对比、案例、风险、行动清单 | 老杨主讲/指向，2-3 个小石头执行分工 |
| 3. 物件现场协作 | 处境、痛点、项目故事、服务现场 | 真实物件 + 小石头物理动作 + 老杨递工具/写便签 |
| 4. 大判断/金句主讲 | 反常识判断、一句话观点、引流 | 老杨占主视觉，0-1 个小石头点缀 |
| 5. 分镜对比 | 踩坑复盘、前后变化、失败到修正 | 老杨讲解转折，小石头每格承担动作变化 |
| 6. 长卷旁白 | 个人经历、项目复盘、产品演化 | 每节点：物件 + 小石头动作 + 老杨递卡/旁注 |

**硬性底线**：
- 每张图必须有老杨与小石头的**明确互动**
- 不能只有老杨肖像，也不能老杨站桩
- 小石头永远 flat 2D（`#f39800`），不能因老杨 3D 被带偏

---

## 第三步：资产组合 · 双风格老杨（精简版）

| 模式 | 必传 | 说明 |
|------|------|------|
| 实物图 | panorama（实体） | 脸不稳 +face-lock；复杂姿态 +actions |
| 手绘/知识卡/PPT | **panorama-handdrawn + panorama** | 手绘全景更重要；实体锁同一人 |
| 手绘全身比例 | 上表 + **handdrawn-body** | 头肩腿对齐金样；跑偏返修必加 |
| **多场景同批（≥2）** | 上表 + **face-lock** | **先 1 张预览门禁** → 通过再批跑；压跨图脸漂 |

小石头同框：+ `primary-character-reference.png`  
猫：金**黄**金渐层；仅点名/彩蛋

**资产组合详见**：`persona-author-assets.md`（5 个核心资产）；返修走形索引 `persona-author-prompts.md`

**废弃不再引用**：~~spec.png~~（已合并到 face-lock）、~~flat-ip-sheet~~（移至 examples/）、~~handdrawn.png~~（历史遗留）

**多场景预览门禁**：未出预览或预览 P1/P3/P6（全身/大半身再加 **P12**）FAIL → 不得批跑其余场景。

---

## 第四步：生成前并列写入（CRITICAL）

先完成 `common-persona-calibration.md` 的人像参考图校准卡；校准结论必须为 PASS，才能继续写入以下锁定内容。

每张双 IP 图的 prompt 必须**并列**写入以下 Lock（表情用预设，不要临场发挥）：

### Persona Identity Lock
```text
Persona Identity Lock（老杨 · 双风格）：
- 实物：author-persona-panorama.png（真人实体全景）
- 手绘系：author-persona-panorama-handdrawn.png + author-persona-panorama.png（手绘更重要，实体锁同一人）
- 脸型/年龄/比例校准：author-persona-flat-ip-sheet.png + author-persona-flat-ip-sheet-navy.png（用户确认最高相似度金样对照组；藏蓝仅换色）
- 六项识别：细框大镜片眼镜 / 短直发3-5cm / 米色T+橄榄卡其短裤 / **自然粗眉 + 高颧骨 + 厚下唇（中上脸三锚点）** / 小麦肤 / **35-40岁成熟男性（无法令纹）**
- **Age Lock**：35-40 岁成熟男性范围；所有图在此范围；NO 20s baby-faced drift、NO 45+/50+ elderly drift、NO nasolabial folds / deep forehead wrinkles；成熟不靠皱纹
- **Height Lock（CRITICAL · 全身/大半身必写）**：净身高视觉档 **183cm**；上身:下身 **4:6**（腿约占立姿 60%）；一眼偏高、上短下长。**禁止漂成 175cm 左右平均身高**、禁止短腿敦实/5:5 均分/头大玩具比。全身手绘必传 `author-persona-handdrawn-body.png`
- **Mouth Lock**：下唇厚于上唇；闭合中性；人中清晰；无法令纹
- **面相族裔**：中国北方/山东男性脸，脸宽结实；**禁止韩范**（小脸、V下巴、冷白皮、爱豆脸）
- **多场景**：same exact person；跨图脸/眼镜/发/穿搭/身高比例差异要小
- 猫（若出现）：金**黄**金渐层英短
- 小石头同框：+ primary-character-reference.png；小石头 flat 2D #f39800
```

### Height / Body Lock（全身或大半身出镜时 CRITICAL · 必写）
```text
Height Lock HARD (Lao Yang):
- Target silhouette = 183cm tall Chinese male — visibly TALLER than average ~175cm office male
- Upper:lower body = 4:6 (short torso, LONG legs; legs ~60% of standing height)
- Head ~1:7–1:7.5 of height — NOT big-head toy, NOT stubby 175 squat
- Full-body handdrawn/knowledge/PPT: MUST attach author-persona-handdrawn-body.png and match it
- Visual check: if he looks like a typical 175cm Chinese male next to desks/modules/door frames → FAIL, redraw taller with longer legs
Negative: 175cm average height drift, short stubby legs, 5:5 torso-leg split, 6:4 long-torso, oversized head, stocky-short, equal-leg squat toy
```

### Persona Feature Stability Lock + 配件层
```text
Persona Feature Stability Lock（特征稳定 · 多场景复用同一段）：
- 脸：长但不细的长方椭圆 + 圆下巴；整体比软萌窄脸再宽一点；下半脸有支撑；北方/山东男骨架
- 眼睛：适中偏小、略垂沉稳；禁止过大明亮偶像眼
- 颧骨：略高一点、中脸有骨感分明（比磨皮圆脸更高）；非刀削网红颧
- 眉毛：深色自然粗眉、轻柔自然拱形；可有少量散乱眉丝
- 皮肤：生活感小麦肤，极轻纹理；禁止韩系磨皮奶油肌 / 过度平滑
- Outfit Layer: 米色短袖棉 T + 橄榄卡其短裤 + 米白帆布鞋（同批禁止换装）
- Accessory Layer (场景/表情变化也必须保留):
  - face: 大镜片浅灰细框矩形眼镜
  - head: 短直发 3-5cm；接近平直发际线
- 唇：整体偏厚，下唇尤其明显
- 肤：健康小麦色（非冷白）
- 可见性：知识卡/手绘/PPT 须正面或 3/4 可见眼镜+短发+厚下唇
- Cross-scene: face proportions/glasses/hair/brows/cheekbones/outfit must match with minimal variation — do NOT redesign the face; do NOT drop glasses/hair when changing expression
Negative: thick black-frame glasses, black long sleeve, grey sweatpants, Korean idol face, V-line jaw, narrow soft face, oversized bright eyes, flat midface, over-smooth K-beauty skin, pale cream skin, thin groomed brows, back view only
```

### Persona Expression Lock（选用一个预设）
```text
Expression Preset: E0_calm | E1_explain | E2_think | E3_focus | E4_warm
- E0_calm: calm, slightly serious, lips gently closed, focused teaching presence
- E1_explain: micro-explain mouth slightly open WITHOUT teeth, light brow focus
- E2_think: thoughtful, slight side glance, optional hand near chin, lips closed
- E3_focus: focused gaze, subtle furrowed brow, lips closed
- E4_warm: subtle closed-mouth warm smile only if user asks for warmth
Repair tip: when fixing expression, strengthen face-lock refs and weaken expression rewrite (low denoise).
Negative: toothy smile, exaggerated laugh, back view, old lady silhouette
```

**小石头 Lock 仍需并列写入**（见 `character.md` 的 2D Flat Lock + Limbs Lock）。

---

## 第五步：生成后快检（CRITICAL）

### 老杨 P1-P7 快检

| # | 检查项 | PASS 条件 | 典型 FAIL |
|---|--------|----------|-----------|
| P1 | 眼镜 | 大镜片浅灰**细框** | 粗黑框、无框、小圆框 |
| P2 | 发型 | 短直发 3-5cm；平直发际线 | 卷发、灰白发、板寸贴皮 |
| P3 | 脸型 | 长但不细长方椭圆；圆下巴；下半脸略宽；**略高颧骨有支撑感** | 窄长少年脸、V 脸、中脸塌平、老太太轮廓 |
| P4 | 嘴唇 | **厚唇饱满**；下唇尤其明显更厚更高 | 薄唇、过小嘴、线嘴 |
| P4b | 眉毛 | **深色自然粗眉**；毛量清晰；轻柔拱形 | 细弯韩范眉、过淡、无眉 |
| P5 | 穿搭 | 米色短袖 T + 橄榄卡其短裤 | 黑长袖、正装、运动裤、批内换装 |
| P6 | 可见性 | 正面或 3/4 可见上述锚点 | 背身、后脑勺、仅气泡无脸 |
| P7 | 表情 | 平静/专注/略严肃；唇闭合或微解释不露齿 | 夸张笑、露齿、疲惫叔、幼态脸 |
| **P12** | **身高比例** | **183 视觉档**；上短下长 **4:6**；腿长舒展；一眼偏高 | **漂成 ~175**、短腿敦实、5:5 均分、头大玩具比 |

> **P12 适用范围**：全身 / 大半身 / 立姿出镜时为 **CRITICAL**（与 P1/P3/P6 同级）。仅头肩特写可不检 P12，但半身以下可见时必须检。

**小石头 L1-L4 + E1-E2 快检**（见 `common-character-lock.md`）：
- L1 计数：每体 2 臂 + 2 腿
- L2 锚点：臂从体侧上 1/3、腿从底缘连续
- E1 眼睛：两只白圆眼、批内一致

### 交付确认
```text
形象快检结果：
- 小石头 L1-L2 + E1：PASS / FAIL（失败项：...）
- 老杨 P1/P3/P6（核心识别）：PASS / FAIL（失败项：...）
- 老杨 P12 身高比例（全身/大半身 CRITICAL）：PASS / FAIL / N/A（失败项：...）
- 老杨 P2/P4/P4b/P5/P7（细节）：PASS / FAIL（失败项：...）

结论：CONFIRMED 可交付 | REJECT 需返修
```

**只有结论为 CONFIRMED 才能交付**。

### 多场景 / 同批跨图快检（2 张及以上 · CRITICAL）

**先确认预览门禁**：本批是否已有通过的 1 张预览？无 → 不得交付批结果。

把本批各张脸部并排对照全景：

| # | 检查 | PASS | FAIL |
|---|------|------|------|
| X0 | 预览门禁 | 已出预览且 P1/P3/P6 过（全身/大半身再过 **P12**） | 未预览就批跑 / 预览偏矮像 175 |
| X1 | 像同一人 | 旁人一眼认出同一个人 | 每张脸像换人 / 差异过大 |
| X2 | 眼镜一致（配件层） | 同框型同粗细且未丢失 | 一张细框一张粗黑框 / 某张无眼镜 |
| X3 | 下颌/唇厚 | 宽下颌+厚下唇稳定 | 一张宽脸一张尖下巴/薄唇 |
| X4 | 穿搭一致（服装层） | 米色T+卡其短裤全批 | 中途换裤/换色 |
| X5 | 年龄肤色 | 小麦肤、35-40岁成熟男性范围稳定 | 任一张跳出范围（20多岁幼态或45+显老） |
| X6 | 表情预设 | 仅 E0–E4 内 | 露齿/大笑/未声明预设 |

X 项 FAIL → **只返修 FAIL 张**（合格样保留）；对照双全景 + face-lock（± handdrawn-body）。禁止只改标签文案。预览 FAIL → 整批不得开跑。

---

## 第六步：双 IP 出图方案推荐格式（触发但未生图时）

用户说"老杨：推荐配图方案"或"老杨：这篇内容想配图"时，先给推荐不生图：

```text
双 IP 互动方案：
视觉模式：[实物图 / 手绘图 / 知识卡 / PPT 演讲]
首选图类型：[具体描述]
默认尺寸：16:9 / 3:4 / 4:5 / 9:16
图内信息量：[画面更空 / 讲清楚重点 / 内容更完整]
互动场景类型：[从 1-6 选一个]
老杨职责：[主讲 / 拆解 / 批注 / 调度 / 旁白]
小石头职责：[搬卡 / 标风险 / 物理动作 / 拉线 / 守门 / ...]
出图效果：[一句话]
推荐原因：[为什么选这个模式和互动场景]

还可以选：
1. [备选模式]：[效果说明]
2. [备选模式]：[效果说明]
```

---

## 常见失败信号（双 IP 专属）

| 失败类型 | 描述 | 拦截 |
|---------|------|------|
| 只有老杨无小石头 | persona 触发任务里只出现老杨肖像 | ❌ 必须有明确互动 |
| 老杨站桩无动作 | 老杨站旁边，无指向/批注/递工具 | ❌ 装饰性测试 FAIL |
| 小石头 3D 漂移 | 小石头因老杨 3D 被带成灰石头/软陶公仔 | ❌ 2D Flat Lock FAIL |
| 粗黑框眼镜 | 老杨眼镜变成粗黑框商务男 | ❌ P1 FAIL，对照 spec 返修 |
| 背身/后脑勺 | 知识卡/手绘/PPT 里老杨背对观众 | ❌ P6 FAIL，须正面/3/4 |
| 老太太/老妇人形 | 灰卷白发、盘发、老年女性轮廓 | ❌ P2/P3 FAIL，性别/年龄不符 |
| 仅气泡无脸 | 只有"老杨讲"标签，无老杨肖像 | ❌ P6 FAIL，必须可见面部 |
| 知识卡只有老杨+文字 | 方法论/步骤类无小石头执行分工 | ❌ 违反知识卡模式规则 |

---

## 画面权重参考（按模式）

| 模式 | 老杨占比 | 小石头占比 | 场景重心 |
|------|---------|-----------|---------|
| 知识卡/PPT/手绘（老杨触发） | 40-55% | 25-40%（1-3 个分工） | 结构 + 互动 |
| 实物图（老杨触发） | 25-40% | 30-45% | 物件小现场 |
| 彩蛋长卷（老杨触发） | 逐段旁白 | 每节点物理动作 | 人生线物件 |
| 观点金句/9:16 海报（老杨触发） | 主视觉 | 0-1 个点缀 | 一句话传播 |

---

## 小比例最低识别线（长卷/远景/小格子）

画面中老杨占比 < 15% 或格子过小时：

**可辨识底线**（至少满足 4/6 项）：
1. 浅灰细框眼镜轮廓可见
2. 短发 3-5cm 发际线可见
3. 米色短袖 + 卡其短裤辨识度
4. 健康肤色（非苍白/灰调）
5. 成熟男性体态（非少年/女性）；全身时仍要有 **183 偏高** 轮廓，勿压成 175 敦实
6. 厚下唇至少在某帧可见

**格子太小无法辨识时**：
- 优先用抽象符号（双 IP 箭头、职责标签、剪影图标）
- **禁止**画 generic 人脸或未锁定肖像
- 若必须出现肖像，仍走完整 Persona Lock + 资产传图

---

## 返修映射（双 IP 专属）

| 用户反馈 | 返修方向 |
|---------|---------|
| 不像老杨 / 不像我 | 实物对照实体全景；手绘系对照手绘全景 + 实体全景；面相漂移再加 face-lock/spec，强化六项识别 |
| 老杨偏矮 / 像 175 / 短腿 | **P12**：加传 handdrawn-body；Height Lock HARD 183+4:6；加长腿、压矮头；禁 175 平均身高漂移 |
| 预览图老杨不像 / 粗黑框 | 文档/总览图也必须走 Persona Lock；过小格子改抽象符号 |
| 老杨背身/后脑勺 | 知识卡/手绘/PPT 须正面或 3/4；传手绘全景 + 实体全景返修 |
| 老杨像老太太 | 禁止灰卷白发、盘发、老年女性轮廓；对照 P2/P3 返修 |
| 小石头被带成 3D | 重申 2D Flat Lock：主角色始终 flat 2D，即使老杨是 3D |
| 批内特征漂移 | 同批共用 Persona Feature Stability Lock + 配件层；禁止一张粗框一张细框 |
| 多场景不像同一人 | 先预览门禁；每张复用同一段 Lock + 双全景；并排快检 X0–X6；**只返修 FAIL 张** |
| 换表情丢眼镜/发型 | 配件层（face/head）必须写入每张 prompt |
| 表情过猛把脸改没 | 降低表情改写力度，加重 face-lock（低 denoise） |

---

**使用建议**：
1. 触发 persona 后立即读本文件，按 6 步流程执行
2. 生成前写入 Identity + Feature/配件层 + Expression Preset（E0–E4）
3. 多场景：先预览门禁，再批跑；生成后做 X0–X6
4. 返修时优先对照 face-lock / 全景；表情返修用低 denoise，只修 FAIL 张
