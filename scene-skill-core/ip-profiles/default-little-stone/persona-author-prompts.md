# 老杨 · 提示词片段

构造生图 prompt 时按需插入。完整身份锚点见 [persona-author-identity.md](persona-author-identity.md)；传图组合见 [persona-author-assets.md](persona-author-assets.md)。

> 胡茬校准：主要位于两鬓、耳前至左右侧颊面，并向下颌侧线极淡过渡；鼻下、上唇、嘴角、下巴正面和面中保持干净。任何生图中不得把侧颊胡茬误画成前部胡子、山羊胡、八字胡或络腮胡。

## 双 IP 基础片段（实物图默认可用；手绘系见下节替代）

```text
Dual-IP interaction (Lao Yang + Little Stone):
Include the author persona (老杨), author yuezheng2006. Physical: attach author-persona-panorama.png (+ face-lock if multi-scene / face unstable). Handdrawn series: attach author-persona-panorama-handdrawn.png + author-persona-panorama.png (+ author-persona-handdrawn-body.png for full-body proportions; + face-lock for multi-scene). Lao Yang = presenter / explainer / annotator / dispatcher. Little Stone = execution Agent (carry cards, label risks, hand over results, physical actions). BOTH must appear with clear interaction — not a standalone Lao Yang portrait, not Little Stone working alone while Lao Yang stands idle. Keep only likeness through CORE ANCHORS: mature Chinese male 35-40 years old, calm and grounded, NOT 20s boyish, NOT baby-faced, NOT idol-like youthful; ~183cm/85kg tall solid build, keep the existing body proportion, do not redesign the body; short STRAIGHT black hair 3-5cm; LARGE-LENS thin light-gray rectangular glasses; long-but-not-thin rectangular-oval face with visible cheek width and jaw width; lower-face must be slightly wider and rounder than a young slim avatar, with mature cheek/jowl support, jaw width, rounded chin height, and no V-shape; lower-face structure must stay recognizable: natural nose-to-upper-lip distance, relaxed neutral mouth corners, noticeably fleshy lips with fuller lower lip; moderate-small calm slightly hooded/downturned eyes with very subtle crow's-foot / eye-corner fine lines, not heavy wrinkles; very subtle short stubble concentrated on BOTH side cheeks / lower cheeks, chin edge and jaw sides, with clean mouth area (no moustache, no goatee, no beard); darker tan skin, not pale; beige T-shirt + olive khaki shorts + off-white canvas sneakers; NO wristwatch. Physical-object mode: Lao Yang as mature restrained stylized 3D, not overly cute Q-version, not clay toy; preserve face proportions before stylizing. Little Stone MUST stay flat 2D #f39800 capsule (see primary-character-reference.png). Weight: physical scenes — object + Little Stone action primary, Lao Yang ~25-40%; knowledge card / PPT / handdrawn — Lao Yang presenter ~40-55%, 1-3 Little Stones executing in modules. Not a personal branding poster. Do not invent personal facts.
```

## 小比例 / 复杂动作追加（+ actions.png）

```text
Small-scale or complex-pose reference:
Also reference assets/persona/author-persona-actions.png for the target pose or the small-scale-in-scene example. When Lao Yang appears small in the frame (about 15%-20% width or less), he must still keep: large-lens thin light-gray glasses silhouette, short straight black 3-5cm hair silhouette, nearly-straight hairline + long-but-not-thin rectangular-oval face with cheek width, jaw width and a rounded chin silhouette (not a pointed/V chin, not a narrow teenager face, not a slim thin face, not a square face), tan skin tone, short-sleeve + olive khaki shorts outfit silhouette, tall solid slightly-athletic body proportion relative to the scene, and a clear action (handing, looking, steadying, annotating). Do not let him become a generic faceless background figure at small scale.
```

## 返修 / 跑偏纠正（对照 face-lock 禁止偏移区）

```text
Repair / drift-correction reference:
Also reference assets/persona/author-persona-face-lock.png (identity ground truth with 禁止偏移 panel). Fix deviations by restoring the CORE ANCHORS: large-lens thin light-gray glasses, short straight 3-5cm hair, long-but-not-thin rectangular-oval face with visible cheek width and jaw width, slightly wider and rounder lower cheeks / jaw / rounded chin for a 35-40 year-old mature male, natural nose-to-upper-lip distance, relaxed neutral mouth corners, noticeably fleshy lips with fuller lower lip, moderate-small slightly hooded/downturned eyes with very subtle eye-corner fine lines, very subtle short stubble on both side cheeks / lower cheeks, chin edge and jaw sides only, clean mouth area, darker tan skin, mature Chinese male 35-40 years old range, calm and grounded, tall solid 183cm/85kg build while keeping the existing body proportion, beige T + olive khaki shorts + off-white canvas sneakers, no wristwatch, mature restrained stylized 3D texture. Do not fix likeness by adding moustache, goatee, beard, heavy wrinkles, heavy nasolabial lines, eye bags, pores, photo lighting, or exact facial texture. Avoid 20s baby-faced, boyish, idol-like youthful, overly smooth skin, too thin, childish, overly cute Q-version, clay toy, curly/fluffy hair, photorealistic human skin, 45+/50+ elderly/tired face, narrow/slim/over-elongated face, thick black/rimless glasses, pale skin, soft baby-face, thin lips, line-mouth, too-small mouth, overly low mouth position, pointed/V chin, overly narrow jaw, slim V-face, wide square jaw, exaggerated M-shaped hairline, slim office-worker build, redesigned heavier body, skinny arms/legs, dress pants, skinny jeans, or bodybuilder muscles.
```

## 资产重建追加（仅本地私有参考）

```text
When rebuilding Lao Yang persona assets, use the 1:1 portrait reference provided in the current session as the highest-priority face and proportion reference, but do not save that photo-real reference into the repository. Aim for high likeness in facial structure and proportions: face width-to-height relationship, cheek width, lower-cheek / jaw width, slightly rounded lower-face support, eye spacing, glasses size relative to face, nose-mouth spacing, relaxed mouth corners, lower-lip height and lip thickness ratio, rounded chin length/width, stubble distribution on lower cheeks / chin edge / jawline, darker tan skin tone, and overall calm mature Chinese male expression. Keep body proportion from the existing public persona sheet unless the user explicitly asks to change body. Stylize only after these proportions are locked. Do not average it into a generic handsome avatar. Do not turn 1:1 likeness into photo-real skin, real pores, ID-photo lighting, or a commercial portrait.
```

## 手绘系替代片段（手绘 / 知识卡 / PPT；不用 3D 描述）

```text
Author presence (handdrawn mode):
Include the author persona (老杨). Read author-persona-panorama-handdrawn.png + author-persona-panorama.png (+ author-persona-handdrawn-body.png for full-body proportions; + author-persona-face-lock.png for multi-scene). Flat black-line hand-drawn, no 3D. Match body proportions of handdrawn-body when full body is visible. Northern Chinese / Shandong male face — NOT Korean idol. Preserve facial structure anchors: mature Chinese male 35-40 years old, calm and grounded, NOT 20s baby-faced or boyish; long-but-not-thin rectangular-oval face with visible cheek width, slightly wider rounded lower cheeks / jaw width and ROUNDED chin; large-lens thin light-gray glasses; short STRAIGHT black 3-5cm hair, not wavy/curly; natural nose-to-mouth spacing, relaxed mouth corners, lips noticeably thick, lower lip thicker and taller than upper; moderate-small slightly hooded/downturned calm eyes with tiny eye-corner fine lines; tiny subtle stubble dots mainly on BOTH side cheeks / lower cheeks, chin edge and jaw sides; clean mouth area, NOT moustache/goatee/beard; darker tan skin; tall solid 183cm/85kg build; beige T + olive khaki shorts; NO wristwatch. Dual-IP: Lao Yang presents/annotates; Little Stone executes in structure. Do not chase photo-real facial detail, deep wrinkles, nasolabial folds, eye bags, pores, or ID-photo texture.
```

## 穿搭配件层（每张必带）

```text
Outfit Layer: beige cotton T + olive khaki shorts + off-white canvas sneakers.
Accessory Layer (MUST keep across scenes/expressions): large thin light-gray rectangular glasses on face; short straight 3-5cm black hair, near-flat hairline. Do NOT drop or redesign glasses/hair when changing pose or expression.
```

## 表情预设（选一写入）

```text
Expression Preset E0_calm: calm, slightly serious, lips gently closed, focused teaching presence.
Expression Preset E1_explain: micro-explain mouth slightly open WITHOUT teeth, light brow focus, pointing or annotating.
Expression Preset E2_think: thoughtful, slight side glance, optional hand near chin, lips closed.
Expression Preset E3_focus: focused gaze, subtle furrowed brow, lips closed, grounded seriousness.
Expression Preset E4_warm: subtle closed-mouth warm smile (only if user asks); still mature and grounded.
When repairing expression: strengthen face-lock / panorama refs; weaken expression rewrite (low denoise). Do not use strong expression to cover face drift.
```

## 年龄锁（CRITICAL）

```text
Age Lock: 35-40 year-old mature Chinese male visual age range as the canonical face-lock and panoramas. Mature via bone structure, calm presence, and subtle cheek/jaw stubble only, never through aging lines. NO 20s baby-faced drift. NO 45+/50+ elderly/tired drift. NO deep nasolabial folds, NO deep forehead wrinkles, NO heavy eye bags. Consistent visual age range across ALL views, expressions, poses, outfits, and reference sheets.
```

## 嘴部锁（CRITICAL · 厚唇）

```text
Lip Lock HARD: noticeably FULL fleshy lips; LOWER lip clearly THICKER and TALLER than upper; soft subtle cupid's bow; lips gently closed; neutral relaxed corners (not smile, not frown); clear philtrum; visible lip volume even in flat line art; clean mouth area. NO thin lips, NO line-mouth, NO small mouth. NO nasolabial folds beside the mouth. NO toothy smile.
```

## 中上脸三锚点锁（CRITICAL · 眉 / 颧 / 唇 · 每张必写）

```text
Mid-face ID trio (ALL THREE must read clearly):
Cheekbone Lock: slightly HIGH cheekbones with clear mid-face bone support; natural soft malar definition; NOT flat midface, NOT sharp V-influencer cheekbones, NOT low flat idol round face.
Brow Lock: dark natural THICK eyebrows with soft gentle arch; visible hair mass; clearly readable in hand-drawn art; NOT thin Korean brows, NOT faded/absent brows, NOT over-groomed.
Lip Lock HARD: noticeably FULL lips; LOWER lip clearly THICKER and TALLER than upper; NOT thin lips, NOT line-mouth.
Do NOT fix likeness by removing brow thickness, flattening cheekbones, or thinning lips.
```

## 脸型比例锁（CRITICAL · 1:1 跟宽脸校准图）

```text
Face Width Lock HARD (1:1 to wide-face calibrate photo): NOTICEABLY WIDE short-square / wide soft-rectangle Northern Chinese face. Bizygomatic & jaw width dominate — cheek-to-cheek span is a primary ID trait. Face width reads as wide as or wider than face length. Full solid cheeks, broad soft jaw, moderately broad rounded chin, sturdy neck. Match the calibrate photo's horizontal proportions first. NOT medium oval, NOT slender, NOT long face, NOT narrow jaw, NOT V-line, NOT elongated midface. If unsure, go WIDER not longer.

If a narrow close-up portrait is attached: keep likeness but face and jaw MUST be SLIGHTLY WIDER than that reference (~5-8%); do NOT copy lean narrow oval.
```

## 相对窄脸修正（会话特写传入时）

```text
Relative narrow-portrait correction:
Match identity from attached portrait, but face SLIGHTLY WIDER than reference — fuller cheeks, broader jaw, wider chin; shoulders SLIGHTLY BROADER and sturdier.
Body Lock 183cm net height: upper-to-lower body ratio **4:6** (short torso, long legs; legs ~60% of standing height); visibly tall silhouette; balanced head-to-shoulder — align author-persona-handdrawn-body.png; NOT 5:5 equal split, NOT short legs, NOT stocky-short, NOT slim office build from close-up crop.
Glasses: large thin LIGHT-GRAY rectangular frames (NOT thick black frames from casual portrait).
```

## 身材锁（CRITICAL · 183cm · 上短下长 4:6）

```text
Body Lock HARD: ~183cm / 85-86kg tall solid Chinese male — upper body to legs ratio 4:6 (short upper body, long lower body; legs ~60% of standing height); visibly taller elegant silhouette; stable slightly broad shoulders; balanced head-to-shoulder; align author-persona-handdrawn-body.png. NOT 5:5 equal split, NOT short legs, NOT short stocky body, NOT oversized head, NOT long torso / short leg (6:4).
```

## 眉毛 / 颧骨 / 厚唇校准（面相精修 · 与上节三锚点一致）

```text
Face mid/upper calibrate (keep glasses, hair, body locks):
Cheekbones: slightly HIGH with clear mid-face bone support — visible in 3/4 and front; NOT flat midface, NOT sharp V-influencer cheekbones.
Eyebrows: dark natural THICK brows with soft gentle arch; visible hair mass; NOT thin Korean brows, NOT over-groomed, NOT missing in hand-drawn simplification.
Lips: FULL fleshy lips; lower lip clearly THICKER than upper; NOT thin lips, NOT line-mouth.
Face width: WIDER short-rectangular / soft-square Northern Chinese face — NOT slender long face, NOT narrow oval.
Eyes: moderate-small, slightly hooded/downturned, calm — NOT large bright sparkly idol eyes.
Skin: lived-in wheat/tan skin with subtle texture; NOT over-smooth K-beauty airbrush, NOT pale cream idol skin.
Ethnicity: Northern Chinese / Shandong male bone structure — wide solid jaw; NOT Korean idol face.
Do not redesign glasses frame type (keep thin light-gray) or hair length while applying this calibrate.
```

## 多场景预览门禁

```text
Multi-scene Preview Gate: generate ONE preview image first for the target mode. Only if P1 glasses / P3 face / P6 visibility (+ body proportion for full-body handdrawn) PASS, proceed to the remaining scenes with the SAME Feature Stability Lock + Outfit/Accessory Layer. If preview FAIL, do not batch. Repair only failing images; keep passing ones.
```

---

## 走形修复索引（返修时先查此表）

| 走形类型 | 先加传 | 粘贴段落 |
| --- | --- | --- |
| 韩范小脸 / V 下巴 / 冷白皮 | face-lock + flat-ip-sheet 对 | 「脸型比例锁」+ 「眉毛/颧骨校准」+ Ethnicity 句 |
| 粗黑框 / 无框 / 小圆框眼镜 | spec（禁止偏移区） | 「穿搭配件层」+ P1 返修；弱化表情改写 |
| 幼态 / 叔感 / 年龄跳变 | flat-ip-sheet 对 | 「年龄锁」 |
| 薄唇 / 嘴位低 / 法令纹 | face-lock 或 spec | 「嘴部锁」Lip Lock HARD |
| 眉过细 / 无眉 / 韩范眉 | face-lock + flat-ip-sheet 对 | 「中上脸三锚点锁」Brow Lock |
| 中脸塌 / 低颧 / 磨皮圆脸 | face-lock + flat-ip-sheet 对 | Cheekbone Lock + Face Width Lock |
| 手绘头大 / 短腿 / 5:5 均分 / 偏矮敦实 | handdrawn-body | 「身材锁」4:6 上短下长 |
| 换表情丢眼镜 / 发型 | face-lock + 双全景 | 「穿搭配件层」Accessory Layer MUST keep |
| 多场景不像同一人 | 双全景 + face-lock | 「多场景预览门禁」+ Feature Stability Lock 全段 |
| 小比例远景丢识别 | panorama + **actions** + face-lock | 「小比例/复杂动作追加」 |
| 宽脸不够 / 被拉成长脸 | flat-ip-sheet 对 + face-lock | 「脸型比例锁」If unsure, go WIDER not longer |
| 双 IP 小石头变 3D | primary-character-reference | `character.md` 迭代 palette「3D/渐变」 |

**返修原则**：加强 02 档参考（face-lock / spec / flat-ip-sheet），减弱表情改写；只返修 FAIL 张，合格样保留。

---

`v1.1` · 2026-07-14 · 三档资产 + 走形修复索引
