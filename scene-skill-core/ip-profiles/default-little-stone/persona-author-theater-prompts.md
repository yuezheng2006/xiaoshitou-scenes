# 老杨小剧场 · 提示词片段

> **最新人物造型覆盖（2026-08-20 · expression-sheet v14 APPROVED）**：老杨 **182cm / 86kg**，结实匀称；下装 = 宽松卡其短裤微微过膝；浅色短袜；鞋 = New Balance **2002R**；面孔以 `assets/persona/theater/author-persona-theater-expression-sheet.png` + `author-persona-theater-face-lock.png`（likeness v2）为准，全身服装辅以 `author-persona-theater-sheet.png`。

仅用于**路径 C**。勿与 Dual-IP 片段混贴。  
方法来源：Adrian Punk「视觉印记」——**设定图 + 内容** 两步法；编排见 `persona-author-theater.md`（Plan Card / Confirm Gate / 输入契约 / 图型预算）。

> **隐私**：禁止把真人照写入公开仓/prompt 示例；生图默认只用风格化金样。会话临时校准照可不落仓。  
> **风格分界**：神似锚点+发型=我们的；画风/版式/服装/图型=Adrian（动漫 OK）。**不追照片级太像。**  
> **出场景前**：设定图须 `APPROVED`；长文先 Imprint Plan Card；缺图型先走场景轻确认门（见 `references/theater-prompt-blueprint.md`）。  
> **Prompt 编译（硬）**：`theater-prompt-blueprint.md` × `theater-styles/vinyl-theater` × 恰好一个 `theater-shapes/{shape}` → **一条**完整 brief。本文件片段供改写填空，**禁止**多段原文 concat / 禁止把 STYLE 第二段粘贴。

## Prompt 编译入口（出场景）

1. 读 `references/theater-prompt-blueprint.md`
2. 读 `theater-styles/vinyl-theater/META.md` + `STYLE.md`（唯一风格原子）
3. 读一个 shape META：`process-breakdown` | `core-action` | `one-theme-two-plates`
4. 用下方「Theater 基础 / 图型 / 面相锁 / 负向」**改写进蓝图章节**，落盘 `scenes/prompts/{slug}-{shape}.md` 再生图
5. Likeness Policy：保识别锚点；**不追照片级**；不传真人自拍进公开 prompt

校验：`python3 scene-skill-core/scripts/validate-theater-punk.py`

## 设定图片段（第一步 · 仅出设定时）

```text
Lao Yang Theater IP Character Sheet (Adrian vinyl-toy 3D anime style — 神似, NOT semi-real):
Generate ONE stable character design sheet.
STYLE LOCK (must match attached Punk style sheet rendering language):
- 3D stylized vinyl-toy / designer-collectible anime look: matte surfaces, soft diffused light, subtle outline, clean collectible figurine feel.
- Sheet layout like Punk ref: big title「老杨小剧场」+「角色设定」, hero 3/4 standing on small circular base, left accessories + color palette swatches, bottom front/left/back/right turnaround.
- FORBIDDEN: semi-realistic illustration, photo-real skin pores, painterly thick-paint realism, realistic anatomy shading, path-B whiteboard line art.
Likeness: 神似 ONLY via anchors — do NOT chase photo 1:1.
SPIRIT ANCHORS (OUR face/hair — NOT Punk's sunglasses face):
- Mature Chinese male ~36-40 成熟. Face: soft round-oval / soft-rectangle 憨厚 with cheek volume — NOT skinny V-face, NOT idol slim. Eyes medium NOT anime-large; LOWER LIP not thin; thick brows. Light stubble ok. Glasses: THICK black soft-rectangular frames. Warm tan.
- Hair (OURS): SHORT STRAIGHT HARD black 3-5cm textured spiky-up. FORBIDDEN curly/wavy/fluffy, FORBIDDEN 1cm scalp 毛寸.
BODY (hard): TALL+SOLID **182cm / 86kg**; legs LONG 4:6 — MUST look clearly taller than average **175cm** male; FORBIDDEN short stubby legs / average 175 squat toy / equal 5:5 torso-leg. Head ~1:7–1:7.5.
Hero outfit: navy crew tee + LOOSE khaki Bermuda shorts slightly past the knee + light short casual ankle socks (off-white/light gray, visible above shoe) + New Balance 2002R (match sheet) + black sports watch on left wrist. Glasses/face match APPROVED theater sheet. Solo. NO Little Stone.
Attach: Punk style sheet for STYLE only + face-lock/flat-ip-sheet for spirit anchors.
```

## Theater 基础片段（第二步 · 出场景时必写）

```text
Lao Yang Visual Theater (Adrian vinyl-toy 3D anime imprint + 神似 — solo default):
TWO inputs: (1) APPROVED stylized character sheet; (2) «{CONTENT_OR_TOPIC}» as paragraph|topic|quote.
STYLE: same 3D vinyl-toy / matte collectible anime rendering as Punk sheet — NOT semi-real, NOT photo-real.
Keep spirit face/hair/glasses + navy/khaki hero outfit + NB-silhouette sneakers + sports watch; only pose/expression/scene change.
BODY: **182cm / 86kg** with long legs 4:6 upright — visibly taller than ~175 average; SAFE pointing: elbow ~90° clear chain.
Character INSIDE idea (25-40% frame when process diagram). Solo unless Combo fragment is attached. NO Little Stone in solo mode.
Pick ONE expression E0–E4.
```

## C 组合片段（小剧场 + 小石头时必加）

```text
Theater Combo (C + Little Stone):
Host style = vinyl-toy theater (same as Lao Yang sheet). Attach Little Stone reference.
Little Stone MUST stay flat 2D orange #f39800 capsule body, white round eyes, thin black stick limbs — FORBIDDEN 3D pebble / clay / matching vinyl shading assimilation.
Roles: Lao Yang ~70-85% duties (points/annotates/explains); Little Stone optional execute/carry/label helper — NOT mandatory handshake dual-IP scene every frame; may omit Little Stone on some plates.
Do NOT apply path-B persona-scene-patterns forced interaction rules.
Optional scene field «{SCENE_FIELD}» = backdrop/props only (e.g. 车载), NOT mode switch to physical/handdrawn.
```

## 流程拆解图

```text
Theater type: Process Breakdown (流程拆解图) — Adrian imprint grammar.
Lao Yang inside the diagram — pointing, annotating, walking the path — NOT a tiny corner sticker; character ~25-40% of frame.
If Combo: Little Stone may move modules / stick labels as flat 2D helper inside the same vinyl scene.
HARD BUDGET: 1 core structure + 3-5 modules + short Chinese labels (≤6 chars each). Default 16:9. Readable at article width.
Layout: structure spine left/center; figure beside or on path pointing at current step; at most one result/risk note.
Character sheet identity + hero outfit locked; only pose changes. OUR face/hair/glasses locked.
```

## 核心动作图

```text
Theater type: Core Action (核心动作图) — Adrian imprint grammar.
ONE decisive moment / metaphor gesture ONLY — multi-action collage = FAIL.
HARD BUDGET: props ≤2; text labels 0-3 short. Default 16:9.
Same character sheet face/hair/glasses/outfit/shoes/accessories; only pose and scene change.
```

## 一鱼两吃

```text
One-theme two-plates (一鱼两吃) — same theme, same APPROVED character sheet:
ORDER: fill topic recipe → Plate A Process preview (identity OK) → Plate B Core Action with SAME sheet ref → deliver both.
Plate A = Process Breakdown. Plate B = Core Action.
IDENTICAL face, OUR hair, OUR glasses, outfit, shoes from sheet. Solo unless Combo fragment attached.
Both plates use Adrian visual-imprint style (NOT path-B whiteboard hand-drawn).
Filenames: {topic}-process / {topic}-action.
```

## 面相锁（风格化 · 神似真人 · 不追照片级 · Likeness Policy）

> 神似锚点以 `author-persona-theater-face-lock.png` 为准；真人自拍仅会话校准，**禁止**写入公开 prompt 示例或落仓公开金样。  
> 出场景时：将本节**改写进** `theater-prompt-blueprint.md` 的 Identity + Likeness Policy 章，勿只靠本文件单独拼接。

```text
Spirit Face Lock / Likeness Policy (theater — 神似 vinyl-toy, NOT photo-real chase):
Face: soft round-oval / soft-rectangle 憨厚 with VISIBLE cheek volume — fuller midface, soft solid jaw (NOT skinny V-face, NOT idol slim, NOT baby round dumpling).
Eyes medium (not anime-large); thick straight-ish brows; nose bridge clear with slightly wider alae; lips medium — lower lip NOT thin; light stubble ok.
Hair SHORT STRAIGHT HARD textured 3-5cm spiky-up; bangs natural, slight asymmetry ok.
Glasses: THICK black soft-rectangular frames, large lenses (match face-lock) — NOT thin wire, NOT gold round.
Age ~36-40 mature calm. Warm natural tan. BODY when full-figure: 182/86 sturdy, LONG 4:6 legs.
STYLE: matte vinyl-toy / clean collectible — FORBIDDEN photo pores, selfie filter, hyperreal CGI skin chase, biometric 1:1 claim.
```
## 表情

复用 `persona-author-prompts.md` 表情预设 E0–E4（选一）。身材以 **182/86 · 长腿 · 4:6** 为准。

## 指向姿势解剖锁（流程拆解常用）

```text
Pointing Anatomy Lock (theater):
Prefer SAFE explain pose: upper arm close to torso, elbow bent ~90° clearly visible, forearm forward, index finger points.
Shoulder → elbow → wrist → hand must form one readable chain with normal adult proportions.
FORBIDDEN: melted/fused arm, missing elbow, sausage forearm, tiny hand, broken joint, floating forearm, twisted wrist.
If pointing repeatedly breaks anatomy, switch to marker/stick as pointer instead of long outstretched arm.
```

## 负向

```text
NO real-person photos or photo-real skin, NO dual-IP path-B forced handshake,
NO Little Stone in solo theater (unless Combo fragment), NO 3D orange pebble assimilation when Combo,
NO path-B flat classroom whiteboard style as theater default,
NO outfit change vs character sheet, NO glasses/hair swap to another IP,
NO buzz-cut hair, NO widow's peak, NO thin wire glasses, NO gold round spectacles,
NO skinny 175cm average stocky toy, NO 1:1 torso-legs squat, NO K/J idol face, NO baby-face, NO skinny V-face,
NO flat plane face / Korean beauty filter, NO photo-real skin pores / selfie look,
NO melted pointing arm / missing elbow / broken joint,
NO badge/logo unless asked, NO copying Adrian Punk's personal likeness.
```

## 走形

| 走形 | 处理 |
| --- | --- |
| 不像设定图 / 漂成别人脸 | 加强传设定图金样 + flat-ip-sheet + face-lock；重写 Face Lock |
| 平面脸 / 低颧 / 日韩风 | 粘贴「面相锁」；强调 HIGH cheekbones + midface planes；face-lock 优先 |
| 指向手臂融化/缺肘 | 粘贴 Pointing Anatomy Lock；改屈肘 90° 或改持笔指向 |
| 发型变软卷/对称齐刘海/贴头皮毛寸 | 锁 3–5cm **硬直**；刘海**右略长**非对称 |
| 幼态娃娃圆脸 / 削尖 V 脸 | 拉回软圆方憨厚、面颊有肉（likeness v2）；禁磨皮偶像脸 |
| 脸漂 / 显老 | 回调脸部神似校准 + 成熟一丝丝（禁深皱纹叔感） |
| 嘴周胡子太重 / 八字胡 | 改为两腮侧短茬；嘴周淡化或干净 |
| 眼镜变细丝/金丝圆框 | 回粗黑软方框（跟 face-lock） |
| 画风退回路径 B 白底黑线 | 重写 Style：Adrian editorial imprint |
| 换装 / 米色 T 教学服 | 禁止——跟设定图 hero outfit（藏蓝 T） |
| 偏瘦 / 矮 / 1:1 蹲姿 | BODY **86kg** + handdrawn-body；改站立；4:6 长腿 |
| 鞋漂成无关款 | 锁米白厚底 + NB 1906R/2002R 造型语言 |
| 误出小石头 | Negatives + 去掉小石头参考 |
| 跳过 Plan / 无 APPROVED 开批 | 停；补 Imprint Plan Card 或设定图 Gate |
