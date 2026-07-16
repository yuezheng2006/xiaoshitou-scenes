# 老杨 · 身份与识别锚点

公开身份锚点：
- **真人实体全身** → `assets/persona/author-persona-panorama.png`
- **手绘全身（更关键）** → `assets/persona/author-persona-panorama-handdrawn.png`
- **手绘身材比例金样** → `assets/persona/author-persona-handdrawn-body.png`
- **多角度面相锁定（跨场景）** → `assets/persona/author-persona-face-lock.png`
- **面相锁定（多角度 + 禁止偏移）** → `assets/persona/author-persona-face-lock.png`
- **最高相似度金样对照组** → `assets/persona/author-persona-flat-ip-sheet.png` + `assets/persona/author-persona-flat-ip-sheet-navy.png`（同脸同身材，藏蓝仅为换色）

两张全景必须是同一个人。重建资产时，面相结构和比例可按用户会话临时 1:1 肖像还原，但不落仓。本文是文字版 ground truth，资产缺失时退回本文。

## 窄脸特写校准（相对修正 · CRITICAL）

若会话传入**正面窄脸特写**（椭圆偏瘦、肩偏窄、偏 175–178 观感），**不得 1:1 复刻其脸宽与肩宽**。老杨 canonical 相对该参考：

| 维度 | 相对窄脸特写 | 锁定目标 |
| --- | --- | --- |
| 脸宽 | 比参考 **再宽一档**（约 5–8% 视觉） | 明显偏宽短方 / 宽软长方；腮帮撑满；脸宽 ≥ 脸长 |
| 肩宽 / 躯干 | 比参考 **略宽、略稳** | 183cm / 86kg 稳实肩；非 Office 瘦削 |
| 身高比例 | 比参考 **更高、上短下长** | 净身高 **183cm**；**上身:下身 = 4:6**（腿占 60%）；对齐 `handdrawn-body` |
| 眼镜 | 不以特写粗黑框为准 | **大镜片浅灰/透明细框**（IP 第一识别件） |

Prompt 必写：
`Relative to narrow portrait reference: face SLIGHTLY WIDER (cheeks/jaw), shoulders SLIGHTLY BROADER, 183cm tall with 4:6 upper-to-lower body ratio (short torso, long legs, legs ~60% of height) — do NOT copy lean narrow oval, slim shoulders, or equal 5:5 proportions from close-up photo.`

## 面相族裔锁（CRITICAL）

老杨必须是**标准中国男性脸型，偏北方 / 山东人气质**，不是韩系偶像脸。

| 必须 | 禁止（韩范 / 错误族裔感） |
| --- | --- |
| 北方中国男性骨架：脸宽结实、下颌有支撑感 | 韩系小脸、V 字尖下巴、窄下颌 |
| 长但不细的长方椭圆脸 + 圆润但有骨感的下巴 | 精致锥子脸、幼态鹅蛋脸 |
| 眉眼距与五官间距偏中国男性常见比例 | 过大水光眼、平行高鼻梁韩系网红五官 |
| 小麦肤、生活感皮肤 | 苍白冷白皮、磨皮偶像肤 |
| 沉稳、接地气的山东大汉气质 | 韩剧男主、爱豆、精致潮流感 |

生成与返修时，prompt 必须显式写入：
`Northern Chinese / Shandong male face structure — NOT Korean idol face, NOT V-line jaw, NOT pale K-beauty skin.`

## 伴侣设定（金渐层）

老杨可有一只伴侣猫，仅作生活感/彩蛋识别，不改变主讲人设：

- **金渐层英短**：被毛**金黄色 / 暖金杏色**，绿或黄绿眼，圆脸英短
- 视觉锚点：`author-persona-panorama.png` 与 `author-persona-panorama-handdrawn.png` 蹲姿摸猫区
- 默认正文配图**不**强制出猫；用户说「猫 / 金渐层」或生活彩蛋时再出现
- 禁止：狸花灰虎斑、银渐层、不够金黄的杂色条纹猫

## 识别优先级（从高到低）

1. **大镜片浅灰/透明细框方形眼镜**（第一识别特征；不是粗黑框、小圆框、无框）
2. **中上脸三锚点（必须同时成立）** → 见下节「中上脸三锚点锁」：
   - **高颧骨**：略高、有支撑感，中脸不塌
   - **自然粗眉**：深色、清晰可见、轻柔拱形，非韩范细眉
   - **厚嘴唇**：下唇明显厚于上唇，整体唇量饱满，非薄唇线
3. **下半脸宽度**：宽腮、宽下颌、圆下巴；脸宽 ≥ 脸长；比窄脸特写 **再宽一档**
4. **米色/浅卡其短袖棉 T + 橄榄卡其短裤 + 米白帆布鞋**
5. **适中偏小、略垂、沉稳的眼睛**（不要大眼/动漫眼）
6. **左右两腮 / 下颌线极淡短茬**（不是嘴周胡子）

## 中上脸三锚点锁（CRITICAL · 生成必写 · 返修必查）

三项缺任一项或明显走形 → 形象检查 **FAIL**，不得交付。

### 高颧骨

| 必须 | 禁止 |
| --- | --- |
| 颧骨位置 **略高**，中脸有 **骨感支撑** | 中脸完全扁平、磨皮圆脸 |
| 颧弓到面颊过渡 **自然**，略分明但不刀削 | 刀削网红高颧、太阳穴深陷 |
| 与 **宽脸** 联动：颧骨撑开脸宽，不拉长脸型 | 低颧 + 窄长脸、韩系小脸 |

Prompt：
`Cheekbone Lock: slightly high cheekbones with clear mid-face bone support; natural soft malar definition; cheek width supported by bone, NOT flat midface, NOT sharp V-influencer cheekbones, NOT low flat round idol face.`

### 眉毛

| 必须 | 禁止 |
| --- | --- |
| **深色自然粗眉**，毛量可见 | 细弯韩范眉、几乎看不见 |
| **轻柔自然拱形**，可少量散乱眉丝 | 过度修眉、一字眉、剑眉夸张 |
| 眉色接近发色， **清晰可读**（手绘也要画出） | 淡眉、灰眉虚化、无眉 |

Prompt：
`Brow Lock: dark natural THICK eyebrows with soft gentle arch; visible hair mass; slight stray hairs OK; clearly readable in hand-drawn line art; NOT thin Korean brows, NOT over-groomed, NOT faded/absent brows.`

### 厚嘴唇

| 必须 | 禁止 |
| --- | --- |
| **下唇明显更厚、更高**于上唇 | 薄唇、细线嘴、上下同厚 |
| **整体唇量饱满**，闭合时仍可见厚度 | 过小嘴、唇线几乎消失 |
| 上唇唇峰柔和；人中清晰；嘴角中性 | 香肠嘴、露齿、营销笑 |

Prompt：
`Lip Lock HARD: noticeably FULL fleshy lips; LOWER lip clearly THICKER and TALLER than upper; soft cupid's bow; lips gently closed; clear philtrum; visible lip volume even in flat line art; NOT thin lips, NOT line-mouth, NOT small mouth.`

**三锚点合并句（每张 prompt 建议并列写入）：**
`Mid-face ID trio: slightly HIGH cheekbones + dark THICK natural brows + FULL lips (thicker lower lip) — all three must read clearly; NOT flat midface, NOT thin brows, NOT thin lips.`

## 外形约束

资产重建时要求 **高相似度还原面相结构**，不要把 1:1 还原误解成照片级皮肤复刻：

| 维度 | 必须保留 | 禁止偏移 |
| --- | --- | --- |
| 年龄感 | **视觉年龄范围：35-40岁成熟男性**；沉稳成熟但不显老；**所有资产与同批图一致**；成熟靠骨相/气质，**绝不靠皱纹** | 幼态娃娃脸（20多岁）；法令纹/抬头纹/眼袋堆年龄；显老叔感（45+/50+）；同批年龄跳变 |
| 体型 | 约 **183cm / 86kg**；肩宽稳实；观感**明显偏高、上短下长**；**上身:下身 = 4:6**（头+躯干约 40%，腿约 60%）；手绘全身对齐 `author-persona-handdrawn-body.png` 并朝更高更长腿校正 | 头过大/短腿/5:5 均分/ torso 过长、整体偏矮敦实、少年细肢、Office 瘦削体 |
| 发型 | 短直发 3–5cm；顺直、自然立起 | 卷/波浪/蓬松乱发、板寸、长发 |
| 发际线 | 接近平直，中间仅极轻微柔和下探 | 夸张 V 字尖角、大 M 型后退 |
| 脸型 | **1:1 跟宽脸校准图**：**明显偏宽**的方圆/短方脸；颧骨位置略高且有自然立体支撑，颧骨到下颌横向撑满；腮帮有肉；下巴略宽圆；脸宽 ≥ 脸长观感，绝不纵向拉长 | 瘦长脸、窄椭圆、中等偏窄脸、颧骨过低或面中塌平、颧骨以下被拉空、韩系小脸、V 字尖下巴、清瘦细脸 |
| 眼睛 | **适中偏小、略垂、沉稳**；不要水光大眼 | 过大明亮偶像眼、动漫大眼、过分有神「亮晶晶」 |
| 颧骨 | **略高、有轻微分明感**（中脸有支撑，非扁平）；与宽脸联动 | 完全扁平中脸；刀削高颧；低颧窄脸 |
| 眉毛 | **深色自然粗眉**，毛量清晰，**轻柔自然拱形** | 细弯韩范眉、过淡、无眉、过度修眉 |
| 皮肤质感 | 生活感小麦肤；可有极轻纹理/毛孔暗示；**禁止磨皮到偶像光滑** | 韩系冷白磨皮、水光奶油肌、过度平滑塑料脸 |
| 族裔感 | 标准中国人脸型，山东人气质；中脸骨感略明显 | 韩范偶像脸、日系二次元、混血网红脸、K-beauty 精致小脸 |
| 肤色 | 健康小麦色 / 略深；整体比普通白净头像更深一点 | 苍白、过白、滤镜磨白 |
| 眼镜 | 大镜片、细浅灰框 | 粗黑框、小圆框、无框 |
| 眼周 | 眼睛适中偏小、略垂；眼角可有极轻微成熟纹理（35-40 岁范围内） | 大眼、动漫眼、20 多岁光滑眼周、重眼袋、深皱纹 |
| 鼻口关系 | 鼻底到上唇距离自然贴近真人参考；嘴巴位置不要下移 | 鼻口距离过长、嘴巴太低、下半脸被拉空 |
| 嘴唇 | **厚唇整体饱满**；**下唇明显更厚更高**；上唇相对薄；闭合中性；人中清晰 | 薄嘴唇、细线嘴、过小嘴、唇量消失 |
| 法令纹/抬头纹 | **不画** | 任何可见法令纹、深抬头纹 |
| 下半脸 | 腮帮、下颌宽度、圆下巴高度、嘴唇厚度和胡茬分布要一起还原；比普通年轻头像更宽、更圆润一点 | 只改嘴唇、不改腮帮/下颌/下巴/胡茬，导致下半脸仍像年轻瘦脸 |
| 胡茬 | 主要集中在两鬓、耳前和左右侧颊面，向下颌侧线极淡过渡；鼻下、上唇、嘴角、下巴正面和面中保持干净，嘴部只保留下唇偏厚 | 把胡茬画成上唇胡、嘴角胡、前部下巴胡、八字胡、山羊胡或络腮胡 |
| 表情 | 平静、略严肃内敛、唇自然闭合 | 浮夸笑、营销亲和感 |
| 配饰 | 无手表、无腕饰 | 任何手表或腕部配饰 |
| 伴侣猫 | 金渐层英短（见上） | 灰虎斑狸花、银渐层、随意橘猫条纹 |

## 表情稳定域（生成前声明 + 生成后核对）

老杨的表情是 **识别稳定项**，不是自由发挥区。与 `common-character-lock.md` 的 Persona Expression Lock 对齐。

### 命名表情预设（优先选用 · 勿临场乱写）

每张图生成前声明一个 `Expression Preset`，只在下表切换；**换表情不得换脸/换眼镜**：

| ID | 中文名 | 何时用 | 写入 prompt（英文锁） | 禁止 |
| --- | --- | --- | --- | --- |
| `E0_calm` | 平静默认 | 大多数场景 | `calm, slightly serious, lips gently closed, focused teaching presence` | 露齿、大笑 |
| `E1_explain` | 微解释 | 讲解/指向结构 | `micro-explain mouth slightly open WITHOUT teeth, light brow focus, pointing or annotating` | 营销笑、张嘴过大 |
| `E2_think` | 托腮思考 | 判断、停顿、复盘 | `thoughtful, slight side glance, optional hand near chin, lips closed` | 呆滞、幼态卖萌 |
| `E3_focus` | 专注凝视 | 强调风险/关键结论 | `focused gaze, subtle furrowed brow, lips closed, grounded seriousness` | 怒喷、瞪眼夸张 |
| `E4_warm` | 温和闭合笑 | 仅用户明确要求亲和时 | `subtle closed-mouth warm smile, still mature and grounded` | 露齿、偶像式露齿笑 |

返修表情时（类比 Face Detailer 低 denoise）：**加重 face-lock / 全景，减弱表情改写力度**；禁止用强表情覆盖脸漂。

| 档位 | 允许 | 禁止 |
| --- | --- | --- |
| 默认 | `E0_calm` | 夸张大笑、露齿、哭脸、怒喷 |
| 讲解 | `E1_explain` | 营销亲和笑、偶像式微笑 |
| 批内变化 | 仅在上表预设间切换 | 一张幼态一张叔感；一张背身一张正脸 |
| 手绘/知识卡 | 正面或 3/4，表情与锚点同时可见 | 仅气泡「老杨讲」无脸、后脑勺、侧背剪影 |

**同批多张**：眼镜框型、发长、唇厚、脸型、穿搭必须一致；表情只能在预设表内变化，不得用表情变化掩盖特征漂移。

生成后按 Confirm Gate **P7** 核对；FAIL 则对照 face-lock / spec 返修，禁止只改文案不改脸。

## 多场景人物一致性锁（CRITICAL · 跨图差异要小）

一次任务出 **2 张及以上**，或同一系列跨实物/手绘/知识卡多场景时，老杨必须像**同一个人连拍**，不允许「每张换一张脸」。

### 全批硬锁（不可变）

| 维度 | 锁死内容 | 允许的最大差异 |
| --- | --- | --- |
| 面相结构 | 北方/山东男：脸宽、下颌支撑、长方椭圆、厚下唇、鼻口距离 | 几乎不可变；旁人一眼应认出是同一人 |
| 眼镜（配件层 face） | 同一副大镜片浅灰/透明细框方框 | 框线粗细、镜片形状不可漂；场景变了也不能丢 |
| 发型发际（配件层 head） | 短直发 3–5cm、接近平直发际 | 不可一卷一短、一黑一灰 |
| 肤色年龄 | 小麦肤、**约38岁成熟感（批内不可跳变；无法令纹）** | 不可一张幼态一张显老；不可用皱纹堆年龄 |
| 穿搭（服装层） | 米色短袖棉 T + 橄榄卡其短裤 + 米白帆布鞋 | **同批禁止换装**（除非用户明确要求工装/运动） |
| 体型 | ~183cm / 稳实肩宽；**上短下长 4:6**；手绘全身对齐 `author-persona-handdrawn-body.png` | 不可 5:5 均分；不可头大短腿/偏矮敦实 |
| 族裔感 | 中国北方男性 | 禁止韩范小脸 / V 下巴 / 冷白皮 |
| 年龄范围 | **35-40 岁成熟男性**；允许范围内 ±2-3 岁波动 | 20 多岁幼态；45+/50+ 显老；同批跳变 |

### 允许变化（仅这些）

姿势、朝向（仍须正面或 3/4 可见脸）、站位、手部动作（指/递/画/扶）、占画比例、场景物件、**表情预设表内**切换。

### 生成协议（多场景强制）

1. **预览门禁**：先出 1 张预览；P1/P3/P6（全身/大半身再加 **P12**）通过后才批跑。
2. **同批共用同一套参考图**：实物跟实体全景；手绘系跟「手绘全景 + 实体全景」；多场景加 face-lock；全身加 handdrawn-body。
3. **每张 prompt 复用**同一段 Feature Stability Lock + Outfit/Accessory Layer；表情只写预设 ID + 对应英文锁。
4. Prompt 显式写入：
   `Same exact person across all scenes — face proportions, glasses, hair, skin tone, and outfit must match the reference panoramas with minimal variation. Do NOT redesign the face between scenes. Keep Accessory Layer (glasses + hair) when changing expression.`
5. 生成后做 **跨图叠影快检**；不像同一人 → **只返修 FAIL 张**，合格样保留。

### 失败信号（跨场景专属）

- 一张山东宽脸、一张韩范小脸
- 一张细框、一张粗黑框
- 一张卡其短裤、一张运动裤/正装
- 一张厚下唇、一张薄唇
- 同批或参考资产之间出现任何明显显嫩/显老漂移（即使未达到5岁）
- 「每张都还行，但并排放一起不像同一个人」
- 手绘全身：**头过大 / 短腿 / 躯干过长**（对照 `author-persona-handdrawn-body.png` FAIL）
- 未预览就批跑；或用强表情改写把脸改没了

## 年龄锁（CRITICAL · 禁止跳变）

老杨视觉年龄范围为 **35-40 岁成熟男性**。角色设定图、face-lock、场景图必须在此范围；禁止幼态或显老：

| 必须 | 禁止 |
| --- | --- |
| 35-40 岁成熟男性观感；沉稳、生活感；骨相结实 | 20 多岁幼态；45+/50+ 显老叔感 |
| **无法令纹、无深抬头纹、无重眼袋** | 用皱纹「修」成熟或 likeness |
| 全部资产、不同服装设定图和同批场景年龄在此范围内一致 | 任一张明显跳出 35-40 岁范围 |
| 允许范围内 ±2-3 岁的自然波动 | 同批一张 28 岁幼态一张 48 岁叔感 |

Prompt 必写：
`Age Lock: 35-40 year-old mature Chinese male visual age range as the canonical face-lock and panoramas. Keep the same slightly high cheekbones and midface structure across every view. Mature via bone structure, calm presence, and subtle cheek/jaw stubble only, never through aging lines. NO 20s baby-faced drift. NO 45+/50+ elderly/tired drift. NO deep nasolabial folds, NO deep forehead wrinkles, NO heavy eye bags. Consistent visual age range across ALL views, expressions, poses, outfits, and reference sheets.`

## 嘴部锁（CRITICAL · 厚唇）

对照 `face-lock` / `spec` / 宽脸金样，嘴是 **第二识别特征**（与眉、颧并列中上脸三锚点）：

| 必须 | 禁止 |
| --- | --- |
| 下唇明显厚于上唇，下唇高度可见 | 薄唇、细线嘴、上下唇同厚 |
| 上唇唇峰柔和、不高耸 | 夸张丘比特弓、香肠嘴 |
| 自然闭合；嘴角中性放松 | 露齿、营销上扬笑、刻意下撇愁相 |
| 人中清晰；鼻口距离自然 | 嘴巴过低、鼻口被拉空 |
| 唇色自然哑光；嘴周干净（可有两腮淡茬，不画八字胡） | 深法令纹连带嘴周老化；八字胡/山羊胡 |

Prompt 必写：
`Lip Lock HARD: noticeably FULL fleshy lips; LOWER lip clearly THICKER and TALLER than upper; soft subtle cupid's bow; lips gently closed; neutral relaxed corners; clear philtrum; visible lip volume in line art; clean mouth area. NO thin lips, NO line-mouth. NO nasolabial folds beside the mouth.`

## 手绘全身比例锁（CRITICAL · 183cm · 上短下长 4:6）

手绘 / 知识卡 / PPT / 小剧场里老杨占全身或大半身时，身材比例必须满足：

| 维度 | 锁定值 | 禁止（高频漂移） |
| --- | --- | --- |
| 净身高 | **183cm** 视觉档 — **一眼高于普通成年男** | **~175cm 平均身高**、178 偏矮、190+ 巨人感 |
| 上下身比 | **上身:下身 = 4:6**（头+肩+躯干 : 腿） | 5:5 均分、6:4 上身偏长 |
| 腿 | 约占立姿身高 **60%**；站姿舒展、膝下够长 | 短腿、膝下被截、下半身压缩、敦实玩具腿 |
| 头身 | 约 **1:7–1:7.5**；头与肩宽协调 | 漫画大头、头占身高 >1/7、潮玩矮胖头身 |
| 肩 | 稳实略宽，非瘦削 Office 体 | 窄肩、少年细肢 |

**肉眼判定句（生成后必问）**：

```text
把他放在门框 / 桌沿 / 流程图模块旁：像 183 高挑，还是普通 175？
若像 175 → P12 FAIL，加长腿、压矮头、加传 handdrawn-body 返修。
```

生成时**必须**写入（全身/大半身）：
`Height Lock HARD: 183cm tall Chinese male — visibly TALLER than average ~175cm office male; upper:lower = 4:6 (short torso, LONG legs ~60% height); head ~1:7–1:7.5; align author-persona-handdrawn-body.png. FORBIDDEN: 175cm average drift, short stubby legs, 5:5 split, stocky-short, oversized head.`

全身手绘 / 知识卡 / PPT：**必传** `author-persona-handdrawn-body.png`（比例金样），不能只口头写 183。

## 渲染语言（随模式，识别锚点不变）

- **实物图 / 长卷**：成熟克制的风格化 3D；可以有圆润体积和柔和边缘，但不追求强 Q 版、软黏土或玩偶化。若 Q 感与面相比例冲突，优先面相比例。
- **手绘 / 知识卡 / PPT**：扁平黑线人物；不要 3D 体积与阴影；锚点仍对齐 spec 图。

1:1 还原边界：还原 **脸型、五官位置、眼镜比例、鼻口距离、嘴唇厚度、下半脸宽度、胡茬分布和肤色深浅**；不还原真实毛孔、照片级布光、皮肤瑕疵、证件照质感或可直接替代真人照片的商业肖像。

手绘版额外要求：不画法令纹、抬头纹、眼袋；可以保留眼角极细微纹理。成熟感靠约38岁的沉稳骨相、长但不细的脸型、眉、略垂眼型、厚下唇、自然鼻口距离、大眼镜+短直发组合；不要画成二十多岁幼态脸，也不要画成带法令纹的偏老脸。

## 小比例最低识别线

老杨占画面约 15–20% 或更小时（参考 `author-persona-actions.png` 远景样例），以下六项缺任一项即判定跑偏：

1. 大镜片细框眼镜轮廓仍可见
2. 短直发 3–5cm 轮廓仍可辨认
3. 接近平直发际线 + 长但不细的长方椭圆脸 / 圆下巴轮廓
4. 短袖 + 卡其短裤穿搭轮廓 + 小麦肤色
5. 相对场景的高大稳实体态比例
6. 明确动作（递、看、扶、画批注等），不能是背景人形

动作图额外约束：动态姿态中的老杨应保持 **约38岁**，不能因为蹲下、记录或侧脸动作被画成40+/45–50岁。不要用重眼袋、法令纹、抬头纹、下垂嘴角、灰暗肤色或疲惫表情来表达成熟。

## 禁止（身份层）

- 照片级真人、证件照、商业肖像、社交媒体头像墙
- 真实毛孔、照片级布光、过度写实面部细节
- 名人脸、二次元、儿童卡通、企业高管海报
- 用皱纹、法令纹、眼袋「修」 likeness
- 向生图请求传入真人照片；向公开仓库提交真人照片

隐私：`assets/persona/private/` 仅作本地防线，公开包不应存在该目录内容。
