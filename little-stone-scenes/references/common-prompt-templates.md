# 生图提示词模板

每张图单独生成。根据当前内容替换变量，不要把多张拼在一起。

## 共同底线

不论哪种模式，都必须保留小石头自己的识别：

```text
Little Stone (小石头): solid #f39200 rounded capsule body, small white circular eyes, optional tiny black pupils, thin black line limbs, flat 2D simple style. Serious, slightly clumsy, stubborn, action-driven. No logo, no brand text, no trademark mark on the body. Little Stone must perform the core physical/conceptual action, not decorate the scene.
```

**2D Flat Lock（每张必写，强制）**：

```text
2D Flat Lock for Little Stone ONLY:
Render Little Stone as a flat 2D sticker / paper cutout / simple vector illustration, NOT a 3D character. The capsule body must be a solid flat #f39200 fill with no gradient, no highlight, no ambient shading, no clay/vinyl/Pixar/soft-toy rendering, no bevel, no embossed edges, no glossy material. Eyes are flat white circles with optional tiny black dots, not glossy 3D spheres. Limbs are thin black lines only, not rounded 3D tubes or soft-clay arms/legs. Little Stone may touch real objects and may have a tiny contact shadow under the feet only, but the body itself must stay flat-colored with no internal volume shading. If the author persona appears, render the author per the current mode (light-Q 3D digital toy in physical-object mode; flat black-line sketch figure in handdrawn / knowledge-card / PPT modes), but Little Stone must always remain strictly flat 2D and visually distinct from the author.
Negative: no 3D mascot, no emoji 3D, no blind-box figure, no inflatable toy, no game character render, no Blender/C4D look, no gradient on orange body, no specular highlight on orange body.
```

共同约束：

- 纯白或近白背景，留白充足。
- 短中文标签 / 批注，不要大段解释。
- 一个核心动作，不要元素清单化。
- 实物图/手绘图：不要商业海报、PPT、UI 截图、复杂架构图；实物图允许真实物件质感，手绘图则保持白板线稿。知识卡模式允许海报级信息量，PPT 演讲模式本身就应该像 PPT 页面——这两种模式各自的规则见 `knowledge-card-mode.md` / `ppt-presentation-mode.md`，不受这条约束。
- 作者出镜只在用户明确提到「老杨 / 作者 / yuezheng2006 / 我本人 / 我的数字形象」时启用；否则不要出现真人或作者形象。
- “戴工牌”默认指小石头佩戴独立挂绳品牌工牌；Logo 只在工牌牌面，不直接印在小石头身体上。老杨和其他人物默认不戴工牌，除非用户明确说“老杨戴工牌 / 人物戴工牌”。
- 多人 / 多个 Agent / 团队协作场景中，多个小石头必须共享 IP 识别，但体型、姿态、朝向、动作分工要明显不同；不要像复制粘贴。

## 实物图模板

用于处境、情绪、项目故事、正文观点隐喻。生成 16:9 小石头实物图。

生成前：读取 `assets/brand/little-stone-ref.png`；从 `physical-master-anchors.md` 选择 `01`–`06` 中最匹配的母版类型；若对应 PNG 存在，只作质量锚点，不复制布局。

```text
Generate one standalone 16:9 horizontal Chinese article illustration in Little Stone Scenes 2.0 physical-object style.

Mode:
小石头实物图. A white-space physical-object scene. It must feel like a small real-object studio setup with Little Stone interacting inside it, not a whiteboard explanation diagram, not a line-art sketch.

Shared Little Stone identity:
Little Stone (小石头): solid #f39200 rounded capsule body, small white circular eyes, optional tiny black pupils, thin black line limbs, flat 2D simple style. Serious, slightly clumsy, stubborn, action-driven. No logo, no brand text, no trademark mark on the body. Little Stone must perform the core physical action.

Multi-person variation (only if the scene has 2-4 Little Stones):
Keep all Little Stones in the same IP family: same #f39200 orange body, same white circular eyes, same thin black limbs, same flat 2D simple style, no logos. But make them clearly different individuals, not duplicated clones: vary height, width, tilt angle, facing direction, arm/leg pose, foreground/background position, held prop, and action role. Each Little Stone must have a distinct job such as handing a card, receiving a card, holding a line, sticking a label, checking feedback, or pressing down an object. Avoid clone-stamp / copy-paste feeling: no identical body size, identical pose, identical angle, or identical limb shapes merely moved to different positions.

Core visual DNA:
Pure seamless #FFFFFF white background. A clean pure-white studio surface. No off-white, no warm white, no grey vignette, no background gradient, no paper texture. Real photographed objects naturally integrated with very light contact shadows only. Little Stone is flat 2D but physically interacts with the real objects. Premium, restrained, weird, clear, not cute poster, not PPT, not infographic.

Template master lock:
Use master type {01–06，例如 03 problem-knot-alert} from references/physical-master-anchors.md as quality anchor, not a layout to copy. Extract only these invariants: {比例/留白/真实物件质感/小石头动作清晰/标签稀疏等不变量}. Required mutations for this image: {至少 3 个变异点：主物件类别、空间方向、小石头动作、配件、标签位置、视角或叙事重心}. Do not reproduce the master image's exact spatial topology, object combination, prop placement, Little Stone pose, or label placement. The image must feel like the same quality family, but clearly be a new visual metaphor grown from the current theme.

Required mutations:
{至少 3 项：主物件类别 / 空间方向 / 小石头动作 / 道具组合 / 标签位置 / 视角 / 叙事重心}

3-second readability:
Without reading any explanation, a viewer should understand this conflict in 3 seconds: {画面 3 秒读懂句}.

Scene budget:
One core physical action only. One real main object or one compact main object group only. At most 1-2 small props. At most 4 handwritten Chinese labels, 3 preferred. Do not include every noun from the theme.

Physical-object requirements:
The main object must be real, clear, complete, and naturally integrated in the same white studio space. All objects must share consistent lighting, perspective, and very light contact shadows. The object should not look like a flat icon, a whiteboard line drawing, or a pasted stock asset. Little Stone must touch, push, pull, block, carry, inspect, or repair the object. The labels float around the physical scene; they must not become the main structure.

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
{短标签1} / {短标签2} / {短标签3}

Optional author presence (only if triggered):
{如触发老杨/作者/yuezheng2006：Include the author persona (老杨), the author yuezheng2006, using assets/persona/author-persona-spec.png as identity reference (follow its 必须保留 anchors closely, especially the hairline and chin shape). Keep only a likeness: mature 35+ Asian male leaning toward late-30s, about 183cm and 85kg, taller and solid build with a slightly athletic physique (broader shoulders, thicker chest/back, restrained muscle definition, not a slim office-worker build, not an exaggerated bodybuilder), upright posture, sunny and slightly trendy vibe, rugged face, healthy tan/wheat-toned skin (not pale). Two distinctive identity features: (1) a HAIRLINE that is nearly straight across with only a very subtle, soft dip in the center — NOT a sharp V-shaped widow's-peak point, NOT dramatically receded temples, NOT an M-shape; the forehead itself is moderate, NOT wide or broad; (2) a NARROWER, slightly pointed CHIN — the face tapers from the cheekbones down to a narrower chin, an oval/tapered face shape (not a wide square jaw, not a broad square chin). Also: fuller lips with a clear lip shape and a slightly thicker lower lip (not thin/simplified lips), clean-shaven, a natural short straight black crew-cut about 3-5cm long with a bit of natural textured/slightly-tousled feel at the front (not perfectly slicked flat, no big curls, no puffy volume, no messy explosion), thin rectangular glasses with a light-gray / translucent frame (not a thick black frame), short-sleeve T-shirt or polo with athletic/jogger-style long pants (sportswear, not dress pants, not skinny jeans), clean sunny athleisure style. Render him as a light-Q 3D digital toy / soft-clay character with rounded volume, soft edges, clean matte skin-color surfaces, and gentle contact shadow, NOT a flat 2D cutout, NOT a semi-realistic digital human, and NOT a photorealistic portrait. Keep the likeness through the nearly-straight hairline with a subtle soft center dip (not a sharp peak, not a wide forehead), the narrower tapered chin, fuller lip shape, thin light-frame glasses, short straight hair silhouette, tan skin tone, mature late-30s presence, and a taller, slightly athletic solid build. Simplify facial features but keep the hairline shape and chin shape recognizable; avoid curly/explosive fluffy hair, a wide full forehead, an exaggerated sharp widow's-peak hairline, a wide square jaw, pale skin, soft baby-face, thin lips, realistic skin texture, pores, photo lighting, and realistic human-arm details. Avoid making him too young, too thin, childish, anime-like, elderly, tired-looking, or exaggerated bodybuilder-like. The author persona must interact with Little Stone and the physical scene, such as handing a note/tool, checking feedback, or holding part of the object. Little Stone must stay in its own strict flat 2D #f39200 sticker style per little-stone-ref.png (solid flat orange capsule body, thin black line limbs, flat white circular eyes, no 3D volume/shading) even while the author is rendered as light-Q 3D — the two characters must look visually distinct in render style. Little Stone still performs the core physical action. Keep the author persona supporting, usually no more than 30%-35% of the main visual weight. Do not make it a portrait, personal branding poster, interview cover, ID photo, celebrity, anime character, childish cartoon, elderly man, tired worker, or muscle-man caricature. Do not invent employer, contact info, credentials, or private facts. 若未触发则删除本段。}

Color accents:
Use only sparse small accents: cobalt blue tape, soft pink tape, lemon yellow tab or dot, tiny green dot, tomato-red underline or warning mark. 4-6 accents total.

Constraints:
No whiteboard explanation diagram, no line-art-only sketch, no flat icon diagram, no flow arrows as the main subject. No UI screenshot, no app logo, no unrequested company name, no unrequested personal information, no pasted rectangular photo edge, no collage chaos. User-provided names, project names, and self-introduction facts may appear only when essential to the requested image. If the user asks for an exact real logo, generate a clean blank logo area on the prop and place the real logo asset afterward; do not ask the image model to redraw the logo. No big title. No long explanation. No workflow chart. No multiple scenes. No office room background. No dark tech background. No off-white background, no grey background, no vignette, no gradient. No concept inventory, no element checklist image, no dumping laptop + phone + papers + cords unless they form one compact main object group. Do not copy the selected master as a topic-swap. Do not repeat its exact object combination, left-right layout, Little Stone pose, prop set, or label positions. The examples are high-quality template masters and the required quality bar, not layouts to trace. Little Stone must stay flat 2D: no 3D rendering, no clay figure, no soft vinyl toy, no Pixar style, no gradient/highlight/volume shading on the orange body, no glossy 3D eyes, no rounded 3D limbs. Real objects may have studio lighting; Little Stone must not inherit that 3D render language.
```

## 手绘图模板

用于流程、结构、系统关系、方法论、认知拆解。生成 16:9 小石头手绘图。

生成前：读取 `handdrawn-style-dna.md`、`handdrawn-composition-patterns.md`、`handdrawn-qa-checklist.md`，选择一个结构类型。

```text
Generate one standalone 16:9 horizontal Chinese article illustration in Little Stone hand-drawn explanation style.

Mode:
小石头手绘图. A pure-white hand-drawn explanation sketch, not a physical-object studio scene.

Shared Little Stone identity:
Little Stone (小石头): solid #f39200 rounded capsule body, small white circular eyes, optional tiny black pupils, thin black line limbs, flat 2D simple style. Serious, slightly clumsy, stubborn, action-driven. No logo, no brand text, no trademark mark on the body. Little Stone must perform the core conceptual action, not decorate the diagram.

Multi-person variation (only if the sketch has 2-4 Little Stones):
Keep all Little Stones in the same IP family: same #f39200 orange body, same white circular eyes, same thin black limbs, same flat 2D simple style, no logos. But make them clearly different individuals, not duplicated clones: vary height, width, tilt angle, facing direction, arm/leg pose, position in the structure, and conceptual action role. One can pull the line, one can hold a module, one can point at feedback, one can block a wrong path. Avoid clone-stamp / copy-paste feeling: no identical pose or identical body just repeated across the diagram.

Visual DNA:
Pure #FFFFFF white background. Minimalist black hand-drawn line art with slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. Clear structure, but not a formal diagram or course slide.

Structure type:
{Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：小石头在哪里、正在做什么、主要结构如何组织、信息如何流动}

Little Stone action:
{小石头承担的核心概念动作，例如拉线 / 守门 / 搬运 / 修补 / 称重 / 分拣 / 塞入}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Optional author presence (only if triggered):
{如触发老杨/作者/yuezheng2006：Include the author persona (老杨), using assets/persona/author-persona-handdrawn.png as identity and style reference. Render him as a flat black-line hand-drawn sketch figure matching Little Stone's handdrawn visual language (pure white background, minimalist black ink line art, no 3D volume, no clay/soft-toy rendering) — NOT the light-Q 3D digital toy used in physical-object mode. Keep the likeness: mature Asian male leaning toward late-30s (not young/smooth-skinned, not elderly/tired), taller and solid build with a slightly athletic physique, slightly broader shoulders, rugged face, healthy tan skin tone. A nearly-straight hairline with only a very subtle, soft center dip (NOT a sharp V-point widow's-peak, NOT dramatically receded temples; the forehead itself is moderate, not wide) and a narrower, slightly pointed chin (oval/tapered face, not a wide square jaw). Also fuller lips with a clear lip shape, a natural short straight 3-5cm crew-cut (neat and straight, not fluffy, not curly, not puffy), thin light-frame rectangular glasses (not thick black frame), short-sleeve top with athletic/jogger-style long pants. Keep likeness, not realism, but keep the hairline shape, chin shape, and mature age recognizable even when simplified into line art. Little Stone must stay in its own flat 2D hand-drawn line-art style per its own identity block — do not let Little Stone pick up any 3D rendering. Avoid making him too young, too thin, childish, pale-skinned, soft baby-faced, thin-lipped, a wide full forehead, a wide square jaw, curly/explosive fluffy hair, anime-like, elderly, tired-looking, or exaggerated bodybuilder-like. He should write annotations, draw a small arrow, or hand a module to Little Stone. Little Stone still performs the core conceptual action. Do not make it a realistic portrait, a 3D digital toy, anime character, childish cartoon, elderly man, tired worker, muscle-man caricature, or personal branding poster. 若未触发则删除本段。}

Color use:
Black for main line art, modules, text, and structure. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or system state. Keep colors sparse.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a PPT infographic, course slide, formal flowchart, dense architecture diagram, dashboard, UI screenshot, or physical-object studio scene. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific content. Little Stone must stay flat 2D hand-drawn sticker style: solid flat #f39200 fill, thin black line limbs, flat white eyes, no 3D mascot, no clay/vinyl toy, no gradient or volume shading on the orange body.
```

## 彩蛋长卷模板

用于个人经历、项目复盘、产品演化、成长路径、内容资产演进。长卷属于 `实物图` 家族，但比例为超横版。

```text
Generate one ultra-wide horizontal Little Stone long-scroll story image in Little Stone physical-object scene style.

Mode:
小石头实物图 · 彩蛋长卷. An ultra-wide white-space story scroll, not a boxed timeline infographic.

Shared Little Stone identity:
Little Stone (小石头): solid #f39200 rounded capsule body, small white circular eyes, optional tiny black pupils, thin black line limbs, flat 2D simple style. Serious, slightly clumsy, stubborn, action-driven. No logo, no brand text, no trademark mark on the body.

Core visual DNA:
Ultra-wide white-space long scroll, about 2.6:1 to 3:1 ratio. A thin hand-drawn black winding line travels from left to right. Along the route, 5-8 real object milestone nodes appear with airy spacing and irregular vertical rhythm. Each node has Little Stone physically interacting with the object or route. Small handwritten Chinese notes sit directly in open white space near each node.

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

Right closing:
{右侧现在关注 / 结论 / 下一阶段}

Constraints:
Do not create separate cards or modules. Do not add numbered circles, step numbers, milestone numbers, or timeline markers. Do not make a tight horizontal row, a regular sine-wave route, or equal node spacing. Do not make one giant object dominate the canvas. Do not make it a PPT, UI screenshot, dashboard, collage, or multiple scenes. Do not copy any sample master's personal facts, third-party names, or exact object/text details unless the user explicitly provides equivalent facts. Little Stone must stay flat 2D at every node: solid flat #f39200 fill, thin black line limbs, flat white eyes, no 3D clay/vinyl/Pixar rendering, no gradient or volume shading on the orange body.
```

## 知识卡模板

用于方法论、步骤、对比、案例、诊断、课程总览等需要独立传播/收藏的内容。生成前完成 `knowledge-card-mode.md` 的必填字段结构锁定。

```text
Generate one standalone knowledge-card image in Little Stone hand-drawn visual language, sized for social/collection sharing (not a 16:9 article illustration, not a PPT slide).

Mode:
小石头知识卡. A complete content container with a clear title, reading order, and information structure — not a single-metaphor illustration.

Shared Little Stone identity:
Little Stone (小石头): solid #f39200 rounded capsule body, small white circular eyes, optional tiny black pupils, thin black line limbs, flat 2D simple style. No logo, no brand text, no trademark mark on the body.

Multi-person collaboration (default for method/step/process/comparison/case/risk/action-list content):
Assign 1 Little Stone as the main presenter/pointer near the title or conclusion, and 1-3 more Little Stones performing concrete actions inside the steps/cases/risks: handing a card, carrying, holding up a sign, pointing at an error, weighing, marking a risk with an X. Keep the same IP identity but vary height, width, tilt, facing direction, pose, and action role — no clone-stamp duplicates. Pure opinion/quote cards may use only one Little Stone or none.

Aspect ratio:
{3:4 / 4:5 / 9:16，按 knowledge-card-mode.md 判断}

Card form:
{观点卡 / 路线图卡 / 白板讲解卡 / 行动清单卡 / 章节总览卡 / 诊断评分卡 / 分镜对比卡 / 或为当前内容定制的新形态}

Information density:
{讲清楚重点 / 内容更完整 / 完整海报}

Title:
{图内标题}

Modules / steps:
{模块1} / {模块2} / {模块3} / {可选模块4-8}

Core message:
{核心观点}

Little Stone action per module:
{每个小石头在哪个模块做什么}

Chinese labels:
{标注词1} / {标注词2} / {标注词3}

Visual DNA:
Pure or near-white background. Black hand-drawn line art as the main structure, inherited from Little Stone's whiteboard style. Orange for main path/emphasis, red only for risk/warning/result, blue only for secondary notes. Colors sparse. Allowed: a clear title, module separators, light section blocks — but no large gradient, no glossy commercial template blocks.

Constraints:
Must have a readable title and top-to-bottom or left-to-right reading order — not just one metaphor plus a few labels. Must not look like a PPT slide (see ppt-presentation-mode.md for that distinction) or a photographed physical-object scene. Do not copy a prior knowledge-card layout; design structure from the current content. Chinese text must stay accurate and readable; if too much text, split into two cards instead of cramming. Little Stone must stay flat 2D: no 3D gradient/highlight/clay/vinyl/Pixar rendering.
```

## PPT 演讲页面模板

用于已完成导演规划卡和 page card 后的单页生成。每页单独生成，严格对齐 page card。

```text
Generate one standalone 16:9 PPT-style presentation page in Little Stone hand-drawn visual language, following the confirmed page card. It must look like a real presentation page — not a knowledge card, not an infographic poster, not a training handout.

Page card reference:
Page type: {页面类型，例如 封面页/机制页/场景页/大判断页}
Visual weight: {anchor / dense / breathing}
Communication task: {沟通任务}
Core message: {核心观点}

Shared Little Stone identity:
Little Stone (小石头): solid #f39200 rounded capsule body, small white circular eyes, thin black line limbs, flat 2D simple style. No logo, no brand text on the body.

Little Stone / author role on this page:
{是否出镜、比例大小、承担的讲解/指向/演示/收束职责；若不出镜则省略}

Title:
{主标题，稳定粗黑清晰字体}

Visual/text ratio:
{图文比例}

Main visual:
{本页核心画面结构}

Chinese on-page text:
{标题文字} / {模块标签，控制数量，字多就建议拆页}

Visual style:
White or near-white background, black-gray line art as the main structure. Orange only for emphasis/path/annotation. Blue only for structure/connector lines. No large gradient, no glossy commercial template colors. Stable, business-appropriate title typography; handwritten text only for light annotations, not primary information.

Constraints:
Must look like one page of a real presentation deck with a single communication task — not a knowledge card, not an infographic poster, not a training handout, not a business report template. Do not put the character too large unless this is a cover/identity/turning-point/closing page. Little Stone must stay flat 2D: no 3D gradient/highlight/clay/vinyl/Pixar rendering.
```

## 多图批量生成提示

当用户要求一次生成多张，先为每张写独立主题，再逐张调用生图工具。

```text
Character lock: same #f39200 Little Stone capsule body, same white-eye style, same flat 2D simple style — see little-stone-ref.png. 2D Flat Lock: flat sticker / paper cutout only, solid flat orange fill, no 3D gradient/shading/clay/vinyl/Pixar look, thin black line limbs, flat white eyes. For multi-person scenes, keep the same IP identity but vary body height/width, tilt, facing direction, limb poses, action roles, and position depth so the characters feel like different individuals rather than copy-pasted clones.
```

```text
Create separate 16:9 images one by one, not a collage. First choose the mode for each image: 小石头实物图 or 小石头手绘图. Apply the shared Little Stone identity to every image. For 实物图, lock one master type from assets/examples/01-06 as quality anchor and list required mutations. For 手绘图, lock one structure type from handdrawn-composition-patterns.md. After each image, compare Little Stone against little-stone-ref.png and the selected mode QA checklist before continuing.
```

## 局部编辑提示

去掉错误文字：

```text
Edit the provided image. Remove only the incorrect handwritten text "{错误文字}" and its underline. Replace it with clean white background matching the surrounding area. Preserve all objects, Little Stone, line style, composition, and image quality.
```

缩减复杂度：

```text
Regenerate the image with the same core metaphor, but reduce visual complexity. Keep one main action, one Little Stone action, short Chinese labels, sparse color accents, and large white space.
```

修正小石头：

```text
Adjust Little Stone: solid orange #f39200 rounded capsule body per little-stone-ref.png, small white circular eyes, thin black limbs, flat 2D simple style, no logo, no brand mark. Keep the original composition and mode.
```

修正 3D 漂移（小石头被画成 3D 时优先用）：

```text
Fix Little Stone rendering only: convert Little Stone back to a strict flat 2D sticker / paper cutout / simple vector character. Solid flat #f39200 fill with no gradient, no highlight, no ambient shading, no clay/vinyl/Pixar/soft-toy look. Flat white circular eyes, thin black line limbs only. No 3D mascot, no glossy spheres, no rounded 3D arms/legs, no volume modeling on the orange body. Keep all real objects, labels, composition, author persona (if any), and scene lighting unchanged. Only flatten Little Stone.
```
