# 生图提示词模板

每张图单独生成。根据当前内容替换变量，不要把多张拼在一起。

**母版 PNG**：Read `assets/examples/` 中对应文件 + `master-selection.md` 抽象骨架。Fork 未同步 PNG 时仍须填写母版锁定字段。

## 标准 2.0 模板

```text
Generate one standalone 16:9 horizontal Chinese article illustration in Little Stone Scenes 2.0 style.

Core visual DNA:
Pure seamless #FFFFFF white background. Minimal flat 2D hand-drawn illustration — NOT 3D render, NOT photorealistic product photography, NOT Western editorial magazine style, NOT material textures or complex shadows. Simple stylized props with clean outlines and flat color blocks. Little Stone (flat #f39200 Little Stone capsule capsule, thin black lines, small white eyes) interacts physically with one simple prop. Premium, restrained, weird, clear, simple at a glance — not cute poster, not PPT, not infographic.

Template master lock:
Use master type {01–06，例如 03 problem-knot-alert} from references/master-selection.md as quality anchor. If assets/examples/03-problem-knot-alert.png exists, use it for visual comparison only — not as a layout to copy. Extract invariants: {比例/留白/真实物件质感/小石头动作清晰/标签稀疏}. Required mutations: {至少 3 项}. Do not reproduce exact spatial topology from any sample PNG.

3-second readability:
Without reading any explanation, a viewer should understand this conflict in 3 seconds: {画面 3 秒读懂句}. If the metaphor requires explanatory context, simplify or change the physical action.

Approved proportion:
The high-quality template examples are the required quality standard for restraint, whitespace, object realism, Little Stone presence, label density, and color accent rhythm. Scene footprint should feel medium-light: about 60%-72% of canvas width and 38%-50% of canvas height (align with style-dna.md). Do not make it miniature. Do not make it close-up. Any single dark object, such as a phone, laptop, or black box, must stay visually light and must not dominate the composition. Objects need air between them.

Scene budget:
One core physical action only. One real main object or one compact main object group only. At most 1 small prop for first-pass previews, 2 maximum only when necessary. At most 3 handwritten Chinese labels. Do not include every noun from the theme. Remove any object that does not serve the core physical conflict. Avoid using the same signature prop set as the selected master.

Little Stone IP — Little Stone capsule (ONLY skin change from black to #f39200):
Soft rounded capsule/vertical-oval body, moderate proportions (height:width 1.2-1.5), same silhouette as thunderstone-xiaoren-ref.png. Two small white circular eyes, optional tiny black pupil dots — NOT logo goggle eyes, NOT anime eyes. Thin black line limbs, subtle black outline OK. Body is PLAIN solid #f39200 only — NO chest logo, NO Thunderstone logo, NO 雷石 text, NO brand marks anywhere on Little Stone body. Reference: assets/brand/thunderstone-xiaoren-ref.png only. Thunderstone logo may appear ONLY on scene props (badge card, signage), never on the character.

Character lock (2+ images): same #f39200 orange, same Little Stone capsule, same flat 2D simple style, same eye style. Pose and props may change.

Brand disambiguation (CRITICAL):
Thunderstone = Chinese KTV / music entertainment tech company (雷石), NOT Thunderstone Quest board game, NOT puzzle MASTER cards, NOT private-equity 雷石投资 finance branding. Minimal flat 2D white-space scene with simple Chinese handwritten labels.

Theme:
{主题}

Reader situation:
{读者处境 / 痛点}

Physical metaphor:
{把抽象观点转译成的物理动作}

Real object scene:
{真实主物件 + 小配件 + 物件如何摆放}

Little Stone action:
{小石头具体正在做什么}

Handwritten Chinese labels:
{短标签1} / {短标签2} / {短标签3} / {可选短标签4}

Color accents:
Use only sparse small accents: cobalt blue tape, soft pink tape, lemon yellow tab or dot, tiny green dot, tomato-red underline or warning mark. 4-6 accents total.

Constraints:
No UI screenshot, no app logo, no unrequested company name, no unrequested personal information, no pasted rectangular photo edge, no collage chaos. User-provided names, project names, and self-introduction facts may appear only when they are essential to the requested image. No big title. No long explanation. No workflow chart. No multiple scenes. No office room background. No dark tech background. No off-white background, no grey background, no vignette, no gradient. No concept inventory, no element checklist image, no dumping laptop + phone + papers + cords unless they form one compact main object group. Do not copy the selected master as a topic-swap. Do not repeat its exact object combination, left-right layout, Little Stone pose, prop set, or label positions. The examples are high-quality template masters and the required quality bar, not layouts to trace.

Thunderstone logo rule (when logo appears on badge, signage, or props):
MUST match assets/brand/thunderstone-logo-core.png EXACTLY — three layers inside-out:
(1) transparent circular PUPIL hole at center of the eye — knockout showing badge background (WHITE on white badge), NOT solid black or orange dot;
(2) horizontal almond-shaped orange EYE body (#f39200 solid) — distinct eye shape, not just a ring;
(3) two thick symmetric curved orange orbital bands wrapping the eye (upper band curves from right over top to pointed left; lower band from left under bottom to pointed right).
On badge card below logo: Chinese text 雷石 in SAME orange #f39200 as logo — both characters same color, NOT black text. Do NOT invent spiral-only icons, generic eye marks, or filled pupils. Read logo-core before generating.

Scene labels: only narrative short tags like 工区 / 刷卡 pointing to environment or action. Do NOT add 雷石 label with arrow pointing at Little Stone character.
```

## 极简变体

用于封面感、强隐喻、海报式正文图：

```text
Ultra restrained Little Stone Scenes 2.0 variant. Keep one real core object, one Little Stone action, and 2-3 short handwritten Chinese labels. Scene still uses real object photography on a pure white studio surface. Preserve object scale and breathing room. Do not explain the full system; keep one strange but precise physical metaphor.
```

## 彩蛋长卷模式模板

用于个人经历、项目复盘、产品演化、成长路径、内容资产演进。核心母版是 `assets/examples/07-brand-evolution-long-scroll.png`。目标是一条连续的真实物件人生线。

```text
Generate one ultra-wide horizontal Little Stone long-scroll story image in Little Stone Scenes 2.0 style.

Use the long-scroll master example assets/examples/07-brand-evolution-long-scroll.png as the core template master and quality bar. Preserve its spatial logic and narrative rhythm, not its specific sample master facts.

Core visual DNA:
An ultra-wide white-space long scroll, about 2.6:1 to 3:1 ratio. A thin hand-drawn black winding line travels from left to right across the whole image. Along the route, 5-8 real object milestone nodes appear with airy spacing and gentle vertical ups and downs. Each node has Little Stone physically interacting with the object or the route. Small handwritten Chinese notes sit close to each node. The milestone nodes must not use numbers, numbered circles, step labels, or visible sequence markers; the order should feel natural through the winding route. The left side starts with identity / origin text. The right side closes with current focus / conclusion / next stage.

Strict long-scroll master layout requirements:
The route must feel hand-drawn and organic, not mathematical. Use irregular vertical rhythm and uneven node spacing: one quiet low stretch, one sudden climb, one shallow arc, one deeper dip, then an unforced right-side finish. Do not create a regular sine wave, do not alternate high-low-high-low, and do not place milestones at equal intervals. Do not align all milestones on one baseline. Keep the layout loose and balanced, with large clean white gaps between nodes; no dense cluster, no full-width object pile, no oversized central hero object. Node copy should be handwritten directly in the open white space beside or under objects, not inside sticky notes, cards, paper slips, labels, or caption boxes. Use colored tape, dots, and short underlines only as tiny rhythm accents, not as text containers.

Background:
Use a premium near-white background, not dead pure white. Keep a subtle white studio air feeling close to #FAFAF8 or #FBFBFA. The background must still be clean, light, and high-end: no dirty grey, no warm yellow, no paper texture, no heavy vignette, no poster gradient. Only very light contact shadows under objects and Little Stone.

Little Stone IP:
FIXED moderate Little Stone capsule capsule (#f39200), small white eyes with optional tiny pupils — reference thunderstone-xiaoren-ref.png only. NO logo eyes. Thin limbs. NO chest logo.

Story theme:
{长卷主题}

Left opening:
{左侧身份 / 起点 / 开场文案}

Milestone nodes, written as unnumbered natural life notes:
- {节点主题} | object: {真实物件} | Little Stone action: {动作} | note: {短注释}
- {节点主题} | object: {真实物件} | Little Stone action: {动作} | note: {短注释}
- {节点主题} | object: {真实物件} | Little Stone action: {动作} | note: {短注释}
- {节点主题} | object: {真实物件} | Little Stone action: {动作} | note: {短注释}
- {节点主题} | object: {真实物件} | Little Stone action: {动作} | note: {短注释}
- {可选节点}
- {可选节点}
- {可选节点}

Right closing:
{右侧现在关注 / 结论 / 下一阶段}

Color accents:
Sparse rhythm accents only: tiny blue tape, soft pink tape, small yellow tab or dot, tiny green dot, tomato-red underline. Accents should mark milestones and route rhythm, not become decoration noise.

Constraints:
Do not redesign into a timeline infographic. Do not create separate cards or modules. Do not add numbered circles, step numbers, milestone numbers, or timeline markers. Do not put every milestone note on sticky notes, paper slips, cards, flags, or boxed labels. Do not make a tight horizontal row. Do not make a regular sine-wave route. Do not make equal node spacing. Do not make one giant object dominate the whole canvas. Do not make it a PPT, poster, UI screenshot, dashboard, collage, or multiple scenes. Do not copy the original sample master's third-party platforms, brand names, personal resume facts, or exact object/text details unless the user explicitly provides equivalent facts to include. Keep the long-scroll master skeleton: left opening, organic winding route with irregular vertical rhythm, airy real object nodes, Little Stone at every node, freehand notes in open space, right closing, premium near-white background.
```

## 多图批量生成提示

当用户要求一次生成多张，先为每张写独立主题，再逐张调用生图工具。

**必须先写 Character Lock**（见 `thunderstone-xiaoren-ip.md`），全批共用后再生成：

```text
Character lock: #f39200 Little Stone capsule body, flat 2D simple, same eye style — see thunderstone-xiaoren-ref.png
```

```text
Create 8 separate 16:9 images, one by one, not a collage. Before each image, lock one specific standard template master from assets/examples/01-06 as a quality anchor. Apply the same Character Lock to every image in this batch. For each image, list invariants and at least 3 required mutations so it cannot become a master-image topic swap. Maintain the same Little Stone Scenes 2.0 flat minimalist style, pure-white background, simple stylized props, sparse labels, and color rhythm across the series. After each image, compare Little Stone against thunderstone-xiaoren-ref.png and the previous image in the batch before continuing. Do not deliver the first generated candidate until it has been visually compared with the selected master and passed QA for originality, scale, 3-second readability, and character consistency.
```

彩蛋长卷模式默认先生成 1 张母版效果图，确认后再迭代。

## 常用负面约束

```text
Negative for standard 16:9 mode: no UI screenshot, no phone chat interface, no code editor screenshot, no GitHub screenshot, no unrequested app logo, no unrequested company logo, no personal photo, no dense text, no huge red arrows, no PPT infographic, no formal flowchart, no business dashboard, no cute mascot, no children's cartoon, no 3D render, no photorealistic product photo, no Western editorial illustration, no material grain, no complex shadows on Little Stone, no overseas ad-agency polish, no soft CGI look, no dark cyberpunk, no off-white background, no grey background, no background gradient, no vignette, no paper texture, no frame, no pasted rectangular image.
Additional negative for standard mode: no Thunderstone Quest board game, no fantasy card game, no puzzle MASTER cards, no private-equity finance poster, no full microphone replacing Little Stone, no microphone head-cover mascot.
Additional negative for standard mode: no concept inventory, no element checklist image, no overloaded scene, no multiple unrelated objects, no laptop-and-phone-and-papers pile unless it is one compact physical scene, no big product close-up, no tags scattered everywhere.
Anti-copy negative for standard mode: no direct master replica, no topic-swap remake of the selected example, no same phone + paper slips + Little Stone shield + hourglass arrangement, no same laptop + cards + pull-lines arrangement, no same magnifier + paper stack + stamp arrangement, no same badge + correction tape arrangement, no same sieve + resume stack arrangement.

Negative for long-scroll mode: no UI screenshot, no phone chat interface, no code editor screenshot, no unrequested app logo, no unrequested company logo, no dense text blocks, no separate cards, no boxed timeline, no numbered circles, no step numbers, no milestone numbers, no visible sequence badges, no PPT infographic, no formal flowchart, no business dashboard, no cute mascot, no children's cartoon, no dark cyberpunk, no dirty grey background, no warm yellow background, no heavy vignette, no poster gradient, no paper texture, no pasted rectangular image, no multi-image collage.
```

## 局部编辑提示

去掉错误文字：

```text
Edit the provided image. Remove only the incorrect handwritten text "{错误文字}" and its underline. Replace it with clean white background matching the surrounding area. Preserve all real objects, Little Stone, shadows, accents, composition, and image quality.
```

缩减复杂度：

```text
Regenerate the image with the same core metaphor, but reduce visual complexity. Keep one main real object, one Little Stone action, at most 3 short Chinese labels, 1-2 small props, and sparse color accents. Preserve medium scene coverage and airy spacing.
```

修正小石头：

```text
Adjust Little Stone: orange (#f39200) Little Stone capsule per thunderstone-xiaoren-ref.png, small white eyes, NO logo eyes, NO chest logo. Keep flat 2D simple.
```
