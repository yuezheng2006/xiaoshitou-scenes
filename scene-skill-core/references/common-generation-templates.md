# 生图提示词模板

每张图单独生成。根据当前内容替换变量，不要把多张拼在一起。

## 提示词语言

提示词默认尽量使用中文，尤其是交付给用户复制使用的完整提示词、返修提示词、图内文字、标签、批注和结构描述。只有这些内容可以保留英文：模型更稳定识别的风格关键词（如 `flat 2D`、`sticker`、`line art`）、资产文件名、比例/技术参数、专有名词和必要的负面约束短语。

不要为了显得专业而整段改成英文；如果英文关键词有助于生图稳定，也要用中文解释主要画面、动作、角色分工和禁止项。

## 共同底线

不论哪种模式，都必须保留主角色自己的识别：

```text
Current profile main character: use the character name, primary color, body shape, eyes, limbs, temperament, assets, and prohibitions from the active profile character.md. The main character must perform the core physical/conceptual action, not decorate the scene.
```

**2D Flat Lock（每张必写，强制）**：

```text
2D Flat Lock for the profile main character ONLY:
Render the profile main character as a flat 2D sticker / paper cutout / simple vector illustration, NOT a 3D character. The capsule body must be a solid flat profile-primary-color fill with one uniform color region: no gradient, no soft center-to-edge shading, no top-left lighting, no highlight, no ambient shading, no clay/vinyl/Pixar/soft-toy rendering, no bevel, no embossed edges, no glossy material. Eyes are flat white circles with optional tiny black dots, not glossy 3D spheres. Limbs are thin black lines only, not rounded 3D tubes or soft-clay arms/legs. the profile main character may touch real objects and may have a tiny contact shadow under the feet only, but the body itself must stay flat-colored with no internal volume shading. If the author persona appears, render the author per the active persona profile mode (for this profile: mature restrained stylized 3D in physical-object mode; flat black-line sketch figure in handdrawn / knowledge-card / PPT modes), but the profile main character must always remain strictly flat 2D and visually distinct from the author.
Negative: no 3D mascot, no emoji 3D, no blind-box figure, no inflatable toy, no game character render, no Blender/C4D look, no gradient on profile-primary-color body, no specular highlight on profile-primary-color body, no orange volume lighting, no shaded orange capsule. Even a mild orange gradient on the body fails the flat lock.
```

**Limbs Lock（每张必写，与 2D Flat Lock 并列）**：

```text
Limbs Lock for the profile main character ONLY:
Exactly 2 arms + 2 legs per individual. Each arm = one continuous thin black line from upper-third lateral body side. Each leg = one continuous thin black line from bottom edge (left/right or center). At most one simple hand terminal per arm (small circle / C-grip / line hook). No mouth, no teeth, no lip line on the capsule — emotion via pose and 0-1 sweat only. Rope/arrow/tether must NOT merge into an extra hand.
Negative limbs: extra arm, floating broken limb, forked fingers, thick 3D tube limbs, mouth on capsule.
```

共同约束：

- 纯白或近白背景，留白充足。
- 短中文标签 / 批注，不要大段解释。
- 一个核心动作，不要元素清单化。
- 实物图/手绘图：不要商业海报、PPT、UI 截图、复杂架构图；实物图允许真实物件质感，手绘图则保持白板线稿。知识卡模式允许海报级信息量，PPT 演讲模式本身就应该像 PPT 页面——这两种模式各自的规则见 `knowledge-card-mode.md` / `ppt-presentation-mode.md`，不受这条约束。
- 作者出镜只在用户明确提到「persona / 作者 / persona 触发词 / 我本人 / 我的数字形象 / 让我和主角色一起 / 作者出镜 / persona出镜」时启用；否则不要出现真人或作者形象。
- “戴工牌”默认指主角色佩戴独立挂绳品牌工牌；Logo 只在工牌牌面，不直接印在主角色身体上。persona 和其他人物默认不戴工牌，除非用户明确说“persona戴工牌 / 人物戴工牌”。
- 多人 / 多个 Agent / 团队协作场景中，多个主角色必须共享 IP 识别与**相同胶囊宽高比**（形体一致锁）；只允许整体等比缩放、姿态、朝向、动作分工不同；**禁止**瘦高/矮胖/横扁形体混用；眼睛（白圆眼+可选 tiny 瞳孔）与手臂（体侧连续细黑线、每侧一臂）批内严格一致；不要像复制粘贴。

## Persona Identity Lock（画面出现 persona 时必写）

persona 触发，或画面主动画出 persona 肖像（含双 IP、文档预览、能力总览）时，prompt 必须包含：

```text
Persona Identity Lock:
Must reference author-persona-spec.png as identity ground truth; for hand-drawn/line-art panels also reference author-persona-handdrawn.png. Lao Yang = large thin LIGHT-GRAY rectangular glasses (NOT thick black frames), short straight black hair 3-5cm, beige short-sleeve T-shirt + dark gray jogger pants + cream sneakers, thicker lower lip, tan skin, mature Chinese male ~40, restrained stylized 3D in physical panels / flat black-line in sketch panels. Front or 3/4 face visible in hand-drawn/knowledge-card/PPT — NO back view, NO speech bubble only without face. Expression: calm, focused, slightly serious; lips closed or micro-explain without teeth; NO exaggerated smile or marketing grin. Do NOT invent a generic business man, cartoon lecturer, black long-sleeve shirt, or thick black glasses. If panel is too small for a locked portrait, use abstract dual-IP symbols only (labels, arrows, silhouettes) — NO generic human face.
When Little Stone appears together, also reference primary-character-reference.png; Little Stone stays flat 2D profile-primary-color with Limbs Lock and NO mouth.
Negative persona: thick black glasses, black sweater/long sleeve, generic avatar, photo-real face, chibi/clay toy, wrong outfit, back view, toothy smile, old-lady silhouette.
```

与 Character Lock / 2D Flat Lock **并列**写入，不可省略。

## 预览 / 文档 / 能力总览模板

用于 README、飞书、gallery、工作流总览等多格说明图。**每一格若含 persona 脸，仍须 Persona Identity Lock；格子太小则用抽象符号，禁止 generic 人脸。**

```text
Generate one 16:9 documentation/preview illustration for scene-skill-core.

Rules:
- Pure white background, minimal hand-drawn infographic style, Chinese labels only.
- For panels about dual IP: either (A) use abstract symbols only — arrows, role labels「老杨讲」「小石头干」, orange capsule icon for Little Stone, NO human face; OR (B) if drawing Lao Yang, MUST attach author-persona-spec.png (+ author-persona-handdrawn.png for line-art style) and follow Persona Identity Lock above exactly.
- For Little Stone in any panel: attach primary-character-reference.png; flat 2D #f39800 uniform fill, **vertical rounded oval capsule** (NOT grey pebble, NOT smooth river stone, NOT orange blob with black-dot eyes only), **two flat white circle eyes** + optional tiny pupil, thin black limbs.
- After generation, run identity QA before saving to assets/examples/.

Panel content: {描述各格主题，如四模式/路由/双IP/母版/工作流}
Negative: generic business man, thick black glasses, black long-sleeve shirt, uninvented mascot, 3D Little Stone, grey pebble Little Stone, smiley orange blob without white circle eyes, version numbers, brand logos.
```

## 实物图模板

用于处境、情绪、项目故事、正文观点隐喻。生成 16:9 主角色实物图。

生成前：读取当前 profile 的主角色锚点资产（默认 `ip-profiles/default-little-stone/assets/character/primary-character-reference.png`）；从 `physical-master-anchors.md` 选择 `01`–`06` 中最匹配的母版类型；若对应 PNG 存在，只作质量锚点，不复制布局。

```text
Generate one standalone 16:9 horizontal Chinese article illustration in 主角色实物图风格.

Mode:
主角色实物图. A white-space physical-object scene. It must feel like a small real-object studio setup with the profile main character interacting inside it, not a whiteboard explanation diagram, not a line-art sketch.

Shared the profile main character identity:
Current profile main character: use character.md for name, primary color, shape, eyes, limbs, temperament, assets, and prohibitions. The main character must perform the core physical action.

Multi-person variation (only if the scene has 2-4 profile main characters):
Keep all profile main characters in the same IP family: same profile-primary-color body, same white circular eyes, same thin black limbs, same flat 2D simple style, same capsule width:height ratio as primary-character-reference.png, no logos. Make them clearly different individuals via overall scale (±10-15% height only), tilt angle, facing direction, arm/leg pose, foreground/background position, held prop, and action role — NEVER vary body width:height ratio (no skinny stick, no fat ball, no horizontal blob). Each profile main character must have a distinct job such as handing a card, receiving a card, holding a line, sticking a label, checking feedback, or pressing down an object. Avoid clone-stamp / copy-paste feeling.

Core visual DNA:
Pure seamless #FFFFFF white background. A clean pure-white studio surface. No off-white, no warm white, no grey vignette, no background gradient, no paper texture. Real photographed objects naturally integrated with very light contact shadows only. the profile main character is flat 2D but physically interacts with the real objects. Premium, restrained, weird, clear, not cute poster, not PPT, not infographic.

Template master lock:
Use master type {01–06，例如 03 problem-knot-alert} from references/physical-master-anchors.md as quality anchor, not a layout to copy. Extract only these invariants: {比例/留白/真实物件质感/主角色动作清晰/标签稀疏等不变量}. Required mutations for this image: {至少 3 个变异点：主物件类别、空间方向、主角色动作、配件、标签位置、视角或叙事重心}. Do not reproduce the master image's exact spatial topology, object combination, prop placement, the profile main character pose, or label placement. The image must feel like the same quality family, but clearly be a new visual metaphor grown from the current theme.

Required mutations:
{至少 3 项：主物件类别 / 空间方向 / 主角色动作 / 道具组合 / 标签位置 / 视角 / 叙事重心}

3-second readability:
Without reading any explanation, a viewer should understand this conflict in 3 seconds: {画面 3 秒读懂句}.

Scene budget:
One core physical action only. One real main object or one compact main object group only. At most 1-2 small props. At most 4 handwritten Chinese labels, 3 preferred. Do not include every noun from the theme.

Physical-object requirements:
The main object must be real, clear, complete, and naturally integrated in the same white studio space. All objects must share consistent lighting, perspective, and very light contact shadows. The object should not look like a flat icon, a whiteboard line drawing, or a pasted stock asset. the profile main character must touch, push, pull, block, carry, inspect, or repair the object. The labels float around the physical scene; they must not become the main structure.

Theme:
{主题}

Reader situation:
{读者处境 / 痛点}

Physical metaphor:
{把抽象观点转译成的物理动作}

Real object scene:
{真实主物件 + 小配件 + 物件如何摆放}

the profile main character action:
{主角色具体正在做什么}

Handwritten Chinese labels:
{短标签1} / {短标签2} / {短标签3}

Optional author presence (only if triggered):
{如触发当前 profile persona：读取 common-persona-routing.md、persona-author.md、persona-author-assets.md、persona-author-modes.md，从 persona-author-prompts.md 插入对应模式片段。若未触发则删除本段。}

Color accents:
Use only sparse small accents: cobalt blue tape, soft pink tape, lemon yellow tab or dot, tiny green dot, tomato-red underline or warning mark. 4-6 accents total.

Constraints:
No whiteboard explanation diagram, no line-art-only sketch, no flat icon diagram, no flow arrows as the main subject. No UI screenshot, no app logo, no unrequested company name, no unrequested personal information, no pasted rectangular photo edge, no collage chaos. User-provided names, project names, and self-introduction facts may appear only when essential to the requested image. If the user asks for an exact real logo, generate a clean blank logo area on the prop and place the real logo asset afterward; do not ask the image model to redraw the logo. No big title. No long explanation. No workflow chart. No multiple scenes. No office room background. No dark tech background. No off-white background, no grey background, no vignette, no gradient. No concept inventory, no element checklist image, no dumping laptop + phone + papers + cords unless they form one compact main object group. Do not copy the selected master as a topic-swap. Do not repeat its exact object combination, left-right layout, the profile main character pose, prop set, or label positions. The examples are high-quality template masters and the required quality bar, not layouts to trace. the profile main character must stay flat 2D: no 3D rendering, no clay figure, no soft vinyl toy, no Pixar style, no gradient/highlight/volume shading on the profile-primary-color body, no glossy 3D eyes, no rounded 3D limbs. Real objects may have studio lighting; the profile main character must not inherit that 3D render language.
```

## 手绘图模板

用于流程、结构、系统关系、方法论、认知拆解。生成 16:9 主角色手绘图。

生成前：读取 `handdrawn-style-dna.md`、`handdrawn-composition-patterns.md`、`handdrawn-qa-checklist.md`，选择一个结构类型。

```text
Generate one standalone 16:9 horizontal Chinese article illustration in the profile main character hand-drawn explanation style.

Mode:
主角色手绘图. A pure-white hand-drawn explanation sketch, not a physical-object studio scene.

Shared the profile main character identity:
Current profile main character: use character.md for name, primary color, shape, eyes, limbs, temperament, assets, and prohibitions. The main character must perform the core conceptual action, not decorate the diagram.

Multi-person variation (only if the sketch has 2-4 profile main characters):
Keep all profile main characters in the same IP family: same profile-primary-color body, same white circular eyes, same thin black limbs, same flat 2D simple style, same capsule width:height ratio as primary-character-reference.png, no logos, NO mouth on any capsule. Make them clearly different individuals via overall scale (±10-15% height only), tilt angle, facing direction, arm/leg pose, position in the structure, and conceptual action role — NEVER vary body width:height ratio (no skinny stick, no fat ball, no horizontal blob). Apply Limbs Lock to every individual. One can pull the line, one can hold a module, one can point at feedback, one can block a wrong path. Avoid clone-stamp / copy-paste feeling.

Visual DNA:
Pure #FFFFFF white background. Minimalist black hand-drawn line art with slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. Clear structure, but not a formal diagram or course slide.

Structure type:
{Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：主角色在哪里、正在做什么、主要结构如何组织、信息如何流动}

the profile main character action:
{主角色承担的核心概念动作，例如拉线 / 守门 / 搬运 / 修补 / 称重 / 分拣 / 塞入}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Optional author presence (only if triggered):
{如触发当前 profile persona：读取 common-persona-routing.md、persona-author.md、persona-author-assets.md、persona-author-modes.md，从 persona-author-prompts.md 插入手绘系片段。若未触发则删除本段。}

Color use:
Black for main line art, modules, text, and structure. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or system state. Keep colors sparse.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a PPT infographic, course slide, formal flowchart, dense architecture diagram, dashboard, UI screenshot, or physical-object studio scene. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific content. the profile main character must stay flat 2D hand-drawn sticker style: solid flat profile-primary-color fill, thin black line limbs, flat white eyes, no 3D mascot, no clay/vinyl toy, no gradient or volume shading on the profile-primary-color body.
```

## 彩蛋长卷模板

用于个人经历、项目复盘、产品演化、成长路径、内容资产演进。长卷属于 `实物图` 家族，但比例为超横版。

```text
Generate one ultra-wide horizontal the profile main character long-scroll story image in the profile main character physical-object scene style.

Mode:
主角色实物图 · 彩蛋长卷. An ultra-wide white-space story scroll, not a boxed timeline infographic.

Shared the profile main character identity:
Current profile main character: follow active profile character.md exactly. No logo, brand text, or trademark mark unless the active profile explicitly allows it and the user authorizes it.

Core visual DNA:
Ultra-wide white-space long scroll, about 2.6:1 to 3:1 ratio. A thin hand-drawn black winding line travels from left to right. Along the route, 5-8 real object milestone nodes appear with airy spacing and irregular vertical rhythm. Each node has the profile main character physically interacting with the object or route. Small handwritten Chinese notes sit directly in open white space near each node.

Story theme:
{长卷主题}

Left opening:
{左侧身份 / 起点 / 开场文案}

Milestone nodes, written as unnumbered natural life notes:
- {节点主题} | object: {真实物件} | the profile main character action: {动作} | note: {短注释}
- {节点主题} | object: {真实物件} | the profile main character action: {动作} | note: {短注释}
- {节点主题} | object: {真实物件} | the profile main character action: {动作} | note: {短注释}
- {节点主题} | object: {真实物件} | the profile main character action: {动作} | note: {短注释}
- {节点主题} | object: {真实物件} | the profile main character action: {动作} | note: {短注释}

Right closing:
{右侧现在关注 / 结论 / 下一阶段}

Constraints:
Do not create separate cards or modules. Do not add numbered circles, step numbers, milestone numbers, or timeline markers. Do not make a tight horizontal row, a regular sine-wave route, or equal node spacing. Do not make one giant object dominate the canvas. Do not make it a PPT, UI screenshot, dashboard, collage, or multiple scenes. Do not copy any sample master's personal facts, third-party names, or exact object/text details unless the user explicitly provides equivalent facts. the profile main character must stay flat 2D at every node: solid flat profile-primary-color fill, thin black line limbs, flat white eyes, no 3D clay/vinyl/Pixar rendering, no gradient or volume shading on the profile-primary-color body.
```

## 知识卡模板

用于方法论、步骤、对比、案例、诊断、课程总览等需要独立传播/收藏的内容。生成前完成 `knowledge-card-mode.md` 的必填字段结构锁定。

```text
Generate one standalone knowledge-card image in the profile main character hand-drawn visual language, sized for social/collection sharing (not a 16:9 article illustration, not a PPT slide).

Mode:
主角色知识卡. A complete content container with a clear title, reading order, and information structure — not a single-metaphor illustration.

Persona Identity Lock (when author persona triggered — CRITICAL):
Read author-persona-spec.png + author-persona-handdrawn.png. Lao Yang = flat black-line hand-drawn mature Chinese man ~40, front or 3/4 view facing reader, pointing/annotating near title or conclusion. Six anchors: large light-gray thin-frame glasses / 3-5cm short straight dark hair / beige short-sleeve T + dark gray sweatpants / thick lower lip / wheat skin / calm mature face. FORBIDDEN: back view, rear silhouette, speech bubble only without face, gray curly white hair, old woman/elderly lady silhouette, generic businessman, thick black glasses, black long sleeves. Little Stone still flat 2D #f39800 + primary-character-reference.png.

Shared the profile main character identity:
the profile main character (主角色): solid profile primary color rounded capsule body, small white circular eyes, optional tiny black pupils, thin black line limbs, flat 2D simple style. No logo, no brand text, no trademark mark on the body.

Multi-person collaboration (default for method/step/process/comparison/case/risk/action-list content):
Assign one profile main character as the main presenter/pointer near the title or conclusion, and 1-3 more profile main characters performing concrete actions inside the steps/cases/risks: handing a card, carrying, holding up a sign, pointing at an error, weighing, marking a risk with an X. Keep the same IP identity but vary height, width, tilt, facing direction, pose, and action role — no clone-stamp duplicates. Pure opinion/quote cards may use only one profile main character or none.

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

the profile main character action per module:
{每个主角色在哪个模块做什么}

Chinese labels:
{标注词1} / {标注词2} / {标注词3}

Visual DNA:
Pure or near-white background. Black hand-drawn line art as the main structure, inherited from the profile main character's whiteboard style. Orange for main path/emphasis, red only for risk/warning/result, blue only for secondary notes. Colors sparse. Allowed: a clear title, module separators, light section blocks — but no large gradient, no glossy commercial template blocks.

Constraints:
Must have a readable title and top-to-bottom or left-to-right reading order — not just one metaphor plus a few labels. Must not look like a PPT slide (see ppt-presentation-mode.md for that distinction) or a photographed physical-object scene. Do not copy a prior knowledge-card layout; design structure from the current content. Chinese text must stay accurate and readable; if too much text, split into two cards instead of cramming. the profile main character must stay flat 2D: no 3D gradient/highlight/clay/vinyl/Pixar rendering.
```

## PPT 演讲页面模板

用于已完成导演规划卡和 page card 后的单页生成。每页单独生成，严格对齐 page card。

```text
Generate one standalone 16:9 PPT-style presentation page in the profile main character hand-drawn visual language, following the confirmed page card. It must look like a real presentation page — not a knowledge card, not an infographic poster, not a training handout.

Page card reference:
Page type: {页面类型，例如 封面页/机制页/场景页/大判断页}
Visual weight: {anchor / dense / breathing}
Communication task: {沟通任务}
Core message: {核心观点}

Shared the profile main character identity:
Current profile main character: follow active profile character.md exactly. No logo or brand text on the body unless explicitly allowed and authorized.

the profile main character / author role on this page:
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
Must look like one page of a real presentation deck with a single communication task — not a knowledge card, not an infographic poster, not a training handout, not a business report template. Do not put the character too large unless this is a cover/identity/turning-point/closing page. the profile main character must stay flat 2D: no 3D gradient/highlight/clay/vinyl/Pixar rendering.
```

## 多图批量生成提示

当用户要求一次生成多张，先为每张写独立主题，再逐张调用生图工具。

```text
Character lock: same profile primary color the profile main character capsule body, same white-eye style, same flat 2D simple style — see the active profile main character anchor. 2D Flat Lock: flat sticker / paper cutout only, solid flat profile primary-color fill, no 3D gradient/shading/clay/vinyl/Pixar look, thin black line limbs, flat white eyes. For multi-person scenes, keep the same IP identity but vary body height/width, tilt, facing direction, limb poses, action roles, and position depth so the characters feel like different individuals rather than copy-pasted clones.
```

```text
Create separate 16:9 images one by one, not a collage. First choose the mode for each image: 主角色实物图 or 主角色手绘图. Apply the shared the profile main character identity to every image. For 实物图, lock one master type from assets/masters/01-06 as quality anchor and list required mutations. For 手绘图, lock one structure type from handdrawn-composition-patterns.md. After each image, compare the profile main character against the active profile main character anchor and the selected mode QA checklist before continuing.
```

## 局部编辑提示

去掉错误文字：

```text
Edit the provided image. Remove only the incorrect handwritten text "{错误文字}" and its underline. Replace it with clean white background matching the surrounding area. Preserve all objects, the profile main character, line style, composition, and image quality.
```

缩减复杂度：

```text
Regenerate the image with the same core metaphor, but reduce visual complexity. Keep one main action, one the profile main character action, short Chinese labels, sparse color accents, and large white space.
```

修正主角色：

```text
Adjust the profile main character: solid profile primary color profile primary color rounded capsule body per the active profile main character anchor, small white circular eyes, thin black limbs, flat 2D simple style, no logo, no brand mark. Keep the original composition and mode.
```

修正 3D 漂移（主角色被画成 3D 时优先用）：

```text
Fix the profile main character rendering only: convert the profile main character back to a strict flat 2D sticker / paper cutout / simple vector character. Solid flat profile-primary-color fill with no gradient, no highlight, no ambient shading, no clay/vinyl/Pixar/soft-toy look. Flat white circular eyes, thin black line limbs only. No 3D mascot, no glossy spheres, no rounded 3D arms/legs, no volume modeling on the profile-primary-color body. Keep all real objects, labels, composition, author persona (if any), and scene lighting unchanged. Only flatten the profile main character.
```
