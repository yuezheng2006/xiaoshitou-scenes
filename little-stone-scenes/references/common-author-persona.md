# 作者出镜规则

## 定位

「老杨」是本仓库作者 `yuezheng2006` 的数字形象。它是可选人物角色，用于作者自述、项目复盘、方法论讲解、Skill 介绍或用户明确要求作者出镜的场景。

## 触发词

只有出现以下意图时才启用作者出镜：

- 老杨
- 作者
- yuezheng2006
- 我本人
- 我的数字形象
- 让我和小石头一起
- 作者出镜 / 老杨出镜

没有这些触发词时，默认**不出现真人或作者形象**。

## 资产隐私边界（重要）

本仓库**不包含也不依赖任何真人照片**。老杨的身份来源就是下面三份**风格化资产**（轻 Q 3D / 手绘线稿），它们已经固化了发际线、脸型、眼镜、体态等全部识别锚点，不含可识别真实肖像细节，可以正常留在公开目录。

- 不要向任何生图请求传入真人照片；识别度靠风格化资产 + 本文的文字描述维持。
- 不要把真人照片提交进仓库；`assets/persona/private/` 在 `.gitignore` 里保留为防线，该目录本身不应存在内容。
- 如果生成结果跑偏，用 `author-persona-spec.png` 的「必须保留 / 禁止偏移」区做纠偏，不要凭空发明新的老杨长相。

## 老杨两种渲染风格

老杨**不是永远轻 Q 3D**。渲染风格必须跟着小石头配图的模式走，两种模式的渲染语言不能混用：

| 模式 | 老杨渲染风格 | 对应资产 |
| --- | --- | --- |
| 实物图模式（含彩蛋长卷） | 轻 Q 3D 数字玩偶 / 软黏土感角色，圆润体积、柔和阴影 | `author-persona-spec.png`、`author-persona-actions.png` |
| 手绘图模式 | 扁平黑色线稿手绘人物，白底，融入白板解释图 | `author-persona-handdrawn.png` |
| 知识卡模式 / PPT 演讲模式 | 继承手绘图视觉语言，同样按 **手绘图模式** 处理：扁平黑线人物 | `author-persona-handdrawn.png` |

不要把轻 Q 3D 数字玩偶直接塞进手绘图模式；也不要把手绘线稿人物用在实物图模式。两种风格共享同一套识别锚点（眼镜、发型、发际线、嘴唇、脸型、体态、年龄感），只是渲染语言不同——这和小石头「flat 2D 不变、场景载体变」的原则一致。

## 老杨三份资产

| 资产 | 文件 | 负责什么 | 默认是否传给生图模型 |
| --- | --- | --- | --- |
| 01 规范说明图（轻Q 3D） | `assets/persona/author-persona-spec.png` | 身份锚点 + 别跑偏：图内画出发际线、脸型、眼镜、体态等「必须保留」区和「禁止偏移」打叉区，实物图模式的识别来源 | 实物图模式默认必传 |
| 02 动作/表情/小比例场景扩展图（轻Q 3D） | `assets/persona/author-persona-actions.png` | 会动、会变小、会和小石头互动：递工具/看反馈/画批注/扶物件等姿态，以及老杨与小石头协作分区、小比例远景样例 | 实物图模式下，复杂动作或小比例场景时加传 |
| 03 手绘版参考图（扁平手绘） | `assets/persona/author-persona-handdrawn.png` | 手绘图/知识卡/PPT 模式专用：黑色线稿老杨的识别锚点、常用姿态、与小石头协作分区、小比例样例 | 手绘系模式触发作者出镜时必传 |

三份资产分工不同，不要一次塞给同一次生成——按下面的传图规则挑选组合。

## 引用优先级

实物图模式：

```text
author-persona-spec.png（规范说明图，身份来源）
  > author-persona-actions.png（动作/小比例场景扩展图）
  > 临时生成图 / 模型自由发挥
```

手绘图模式（知识卡 / PPT 演讲模式同）：

```text
author-persona-handdrawn.png（手绘版参考图，身份来源）
  > 临时生成图 / 模型自由发挥
```

## 传图规则

生成前按当前小石头图模式 + 场景挑选要读取的资产：

- **实物图模式 · 普通出镜**（老杨站立/正常互动，非小比例、非复杂多姿态）：读 `author-persona-spec.png`。
- **实物图模式 · 小比例场景**（老杨退到远景，占比小）或**复杂/多姿态动作**（递工具、扶物件、和小石头协作等）：加读 `author-persona-actions.png`。
- **实物图模式 · 形象跑偏 / 返修 / 用户质疑不像老杨**：对照 `author-persona-spec.png` 的「必须保留」区逐项核对，并参考「禁止偏移」区排除对应问题；发际线宁可偏平直自然，不要画成夸张尖角。
- **手绘图模式 / 知识卡模式 / PPT 演讲模式 · 任何作者出镜**：读 `author-persona-handdrawn.png`，不加读实物图模式的 01/02 资产，避免把轻 Q 3D 渲染语言带进手绘线稿。
- 任何资产缺失的环境（例如别人 fork 本仓库丢了 PNG）：退回本文的文字描述维持识别度，交付时标注资产缺失，不要凭空发明新长相。
- 无论哪种场景，`little-stone-ref.png` 仍要在小石头同框时一并读取。

## 生图前必须读取

当作者出镜时，先判断当前是实物图模式还是手绘图模式，按上面的传图规则确定资产组合，再加读：

- 当前模式对应的参考文档和模板
- `assets/brand/little-stone-ref.png`（小石头同框时）

## 形象约束

老杨数字形象以 `author-persona-spec.png`（实物图模式）/ `author-persona-handdrawn.png`（手绘系模式）为识别锚点，只要求 **形似**，不要过度写实：

- 成熟亚洲男性，身高约 183cm、体重约 85kg，整体气质成熟、**阳光、略带潮男感**，不要过于内敛或严肃老气。
- **体型更高大结实、略健壮**：肩膀更宽、胸背更厚实，手臂和身形有克制的运动感/肌肉轮廓，站姿更挺拔（不是纤细的都市白领体型，也不要夸张成健身房肌肉猛男）；**面容硬朗，五官线条分明**，下颌线条清晰但收窄至略尖的下巴（见下方额头/下巴专项说明，不是宽方下颌，也不是柔和圆润的娃娃脸）；不要画得过瘦、少年感或幼态。
- **实际年龄感要再成熟一点**：整体基调是「成熟稳重的 35+ 到接近 40」，不是二十多岁的光滑幼态年轻脸，也不是「年轻实习生」；允许更明显一些的成熟痕迹（法令纹、更沉稳的五官比例、更宽更成熟的脸部骨相），但不要显老、疲惫、增加白发或过多皱纹。
- **肤色健康小麦色 / 略深**，不要白皙、不要苍白。
- **短直发，长度约 3-5cm，带自然碎发质感**：发丝顺直但不是完全服帖光滑，发尖有一点自然的碎发/微竖起纹理感，尤其额前一小片头发略带一点点立起的质感；不要画成蓬松堆叠的立体层次发型、不要打卷、不要大片炸开，但也不要画成一丝不乱、死贴头皮的"喷胶"光滑效果。
- **额头本身并不宽**（不要画成宽阔饱满的大额头）：发际线整体接近平直、只有非常轻微、柔和的高低变化——刘海中间比两侧略微靠下一点点，形成一个很浅、很自然的弧形/浅尖，**不是**夸张、锐利、对比强烈的 V 字尖角或明显内收的"M"型发际线；两侧鬓角只是略高一点，不要画成大幅后退外扩。发际线校正以 `author-persona-spec.png` 的画法为准，宁可偏平直、偏自然，也不要偏夸张尖角。
- **下巴是另一个重要识别特征**：下巴相对偏窄、略尖，不是宽方下巴或方形下颌；整体脸型呈"上宽下窄"的椭圆/锥形轮廓——额头和颧骨部分较宽，下巴收窄变尖，而不是左右对称的方脸或宽下巴。
- **嘴唇偏厚**：上下唇比例饱满、唇形轮廓清晰，尤其下唇略厚；不要画成薄唇或没有唇形细节的简化嘴巴。
- **表情基调：平静、略严肃内敛、直视镜头**，嘴唇自然闭合、不外扬大笑；不要画成浮夸笑容、卡通式眯眼笑或过度亲和的营销感表情。
- **脸型比例**需贴近参考照片的实际比例（接近平直、只有轻微柔和高低变化的发际线、额头本身不宽、下巴偏窄略尖的上宽下窄椭圆脸，见上两条），不要被简化成更圆润/更卡通泛化的通用脸型，也不要画成宽方脸或方下巴；渲染风格必须仍是轻 Q 3D，不能因为追求脸型/表情准确而变成写实人像。
- **浅灰 / 透明细框方形眼镜**（细金属或透明亚克力镜框，**不是**粗黑框）。
- **穿搭：短袖 T 恤 / Polo + 运动裤或运动休闲长裤**（jogger/训练裤风格，束脚或直筒都可以），干净阳光的运动休闲风格（不是长袖针织衫，不是正装西裤，也不是紧身牛仔裤）。
- 面容干净，不留胡茬。
- 实物图里优先画成轻 Q 3D 数字玩偶 / 软黏土感角色：五官更简洁，头身比例略 Q，轮廓更柔和，有圆润体积、柔和边缘和轻微立体阴影；即使简化，也要保留接近平直的自然发际线（额头本身不宽，不要画成夸张尖角）、自然短直发、和嘴唇偏厚这几个五官细节，不能被"简化"抹平。
- 皮肤和五官不要照片级纹理；保留形似，不追求真人皮肤、真实毛孔、真实人像光影。可以有干净的 3D 体积感，但不是写实人像。

不要追求照片级复刻。不要发明明显不同的人物身份、年龄、发型、服装风格或夸张表情。不要把作者画成名人、二次元、儿童卡通、企业高管海报、真实人像摄影或过度商业写真。

## 小比例出镜最低识别线

当老杨在真实物件小现场里退到远景、占画面比例小（约 15%-20% 甚至更小）时，仍必须保留以下识别锚点，缺任何一项即判定为跑偏，参考 `author-persona-actions.png` 的小比例远景样例：

- **浅灰/透明细框眼镜**轮廓仍可见，不能糊成一团黑、变成粗黑框，或直接省略。
- **自然短直发的轮廓**仍可辨认，不能变成蓬松卷发、光头、长发或大背头。
- **接近平直、只有轻微柔和高低变化的发际线 + 下巴略尖的上宽下窄脸型轮廓**仍可辨认（哪怕只是简笔剪影），不能被简化成圆脸、方脸或宽下巴，额头也不能画宽，发际线也不能画成夸张尖角。
- **短袖 + 运动裤**的穿搭轮廓和健康小麦肤色不能换成深色长袖、正装长裤或苍白肤色。
- **高大结实略健壮、面容硬朗的体态比例**（相对场景中其他物件/小石头的身高关系）不能被压缩成矮小、纤细或娃娃脸比例。
- 必须在做一个**明确动作**（递、看、扶、画批注等），不能只是站在角落里当背景人形。

六项里任意一项在小比例下丢失，先重生成或改用局部放大关键部位（眼镜/发型/脸型）的方式返修，不要直接交付。

## 与小石头的关系

作者出现时，必须和小石头发生互动，不要只是并排站立：

- 作者递给小石头一张便签 / 卡片 / 工具。
- 小石头把纸条递给作者，作者在旁边检查。
- 作者扶住真实物件，小石头负责拉、挡、推、接。
- 作者在白板旁画结构，小石头拉线或搬模块。
- 作者坐在一侧写提示词，小石头在物件现场执行动作。

互动关系要表达「作者和小石头一起工作」，不是作者肖像展示。

## 实物图模式

实物图里：

- 真实物件仍然是主现场。
- 老杨可以作为略 Q 的数字人物/半身人物出现在一侧，但不能压过小石头和物件冲突。
- 作者大小通常不超过画面主视觉的 30%-35%；不要成为最大主体。
- 小石头仍然必须承担核心物理动作。
- **重要：小石头永远是自己的 flat 2D 形象**（`#f39200` 平涂胶囊身体、细黑线四肢、白圆眼，参考 `little-stone-ref.png`），不能因为老杨是轻 Q 3D 数字玩偶就被带成 3D 灰石头、卵石、软陶公仔或其他任何非官方形象——两者渲染语言必须明显不同、并存于同一画面。生成 `author-persona-actions.png` 等老杨与小石头同框资产时，小石头部分必须直接沿用 flat 2D 设定，不要临时发明新的小石头造型。
- 作者应与真实物件处在同一白色空间，但保持轻 Q 3D 数字玩偶质感；要有体积、圆润边缘和柔和接触阴影，不要变成扁平 2D 纸片人。
- 不要使用照片级真人皮肤、真实人像光影或商业人像海报质感。
- 画面不要做成头像展示、人物专访封面或个人品牌海报。

推荐结构：

```text
真实物件主现场 + 小石头执行动作 + 老杨递工具/看反馈/做旁白
```

## 手绘图模式

手绘图里，老杨**不用轻 Q 3D 数字玩偶**，改用扁平黑色线稿手绘人物，参考 `author-persona-handdrawn.png`：

- 生成前必须 Read `author-persona-handdrawn.png`；不要把 `author-persona-spec.png` / `author-persona-actions.png` 的轻 Q 3D 描述带入手绘图 prompt。
- 老杨简化为黑色线稿的手绘人物或半身讲解者，视觉语言和小石头的手绘线稿一致：白底、黑色线条为主、少量红/橙/蓝批注。
- 保留细框眼镜、自然短直发（3-5cm 毛寸感）、接近平直的自然发际线（额头本身不宽）、上宽下窄略尖下巴、嘴唇偏厚、硬朗面容、35+ 偏近 40 年龄感、肩宽背厚的结实体态等识别点，即使线条简化也不能丢。
- 不要追求肖像写实；要融入白板解释图，不要出现圆润体积、柔和阴影等 3D 渲染语言。
- 小石头仍然承担核心概念动作。
- 作者可以在旁边写批注、画箭头、递模块。

推荐结构：

```text
老杨画结构 / 写批注 + 小石头拉线 / 搬模块 / 守门
```

## 禁止

- 未触发时自动加入作者形象。
- 把作者作为主视觉大头像，挤掉小石头和核心动作。
- 把作者画成照片级真人、真实商业肖像海报、证件照、社交媒体头像墙。
- 真实皮肤纹理、真实毛孔、照片级人像布光、过于真实的手臂/脸部细节。
- 把作者画得过于 Q 版幼态、二次元或儿童卡通，导致不像参考图。
- 让作者替代小石头承担核心动作。
- 使用作者形象表达未经用户提供的个人身份、单位、联系方式、履历或背书。

## Prompt 片段

基础片段（所有场景都用）：

```text
Author presence:
Include the author persona (老杨), the author yuezheng2006, using assets/persona/author-persona-spec.png as the identity reference (follow its 必须保留 anchors closely, especially the hairline and chin shape). Keep only a likeness: mature 35+ Asian male, leaning toward late-30s (must clearly read as mature, not a young smooth-skinned twenty-something, but also not elderly or tired-looking; a noticeable but restrained maturity around the nasolabial area and a more settled, wider facial structure is fine), about 183cm and 85kg, taller and solid build with a slightly athletic/fit physique (broader shoulders, thicker chest and back, a hint of muscle definition on the arms — not a slim office-worker build, but also not an exaggerated bodybuilder), upright posture, sunny and slightly trendy vibe (not overly reserved or formal), rugged defined face with clear facial structure (not soft or baby-faced), healthy tan/wheat-toned skin (not pale or fair). Two distinctive identity features to render carefully: (1) a HAIRLINE that is nearly straight across, with only a very subtle, soft, gentle dip in the very center (NOT a sharp V-shaped widow's-peak point, NOT dramatically receded temples, NOT an exaggerated M-shape) — the forehead itself is moderate, NOT wide or broad; (2) a NARROWER, slightly POINTED CHIN — the face tapers down from the cheekbones to a narrower chin, i.e. an oval/tapered face shape (not a wide square jaw, not a broad square chin). Also: fuller lips with a clearly defined lip shape, especially a slightly thicker lower lip (not thin or simplified lips), a calm, composed, slightly serious and reserved expression looking straight at the viewer with lips naturally closed (not a big cartoon smile, not squinty cheerful eyes, not an exaggerated friendly marketing expression), clean-shaven, a natural short straight black crew-cut about 3-5cm long with a bit of natural textured/slightly-tousled feel at the front hairline (not perfectly smooth or slicked-down, not big curls, not puffy volume, not a messy explosion — just normal natural short-hair texture), thin rectangular glasses with a light-gray / translucent acetate frame (not a thick black frame), short-sleeve T-shirt or polo with athletic/casual jogger-style long pants (sportswear, not dress pants, not skinny jeans), clean sunny athleisure vibe (not a long-sleeve knit sweater, not formal wear). In physical-object mode, render him as a light-Q 3D digital toy / soft-clay character with rounded volume, soft edges, clean matte skin-color surfaces, and gentle contact shadow, not a flat 2D cutout. Keep the likeness through the nearly-straight hairline with a subtle soft center dip (not a sharp peak, not a wide forehead), the narrower tapered chin, calm composed expression, fuller lip shape, thin light-frame glasses, short straight hair silhouette, tan skin tone, mature late-30s presence, and a taller, slightly athletic solid build. Do not make him a semi-realistic digital human or a photorealistic portrait. Avoid realistic skin texture, pores, photo lighting, and realistic human-arm details. Avoid making him too young, too thin, childish, pale-skinned, soft/baby-faced, rounded/generic cartoon-faced, wide square-jawed, broad-chinned, over-smiling, thin-lipped, an exaggerated sharp widow's-peak hairline, a wide full forehead, anime-like, elderly, tired-looking, or exaggerated bodybuilder-like. The author persona must interact with Little Stone and the scene, not appear as a standalone portrait. Keep the author persona supporting, usually no more than 30%-35% of the main visual weight. Do not make it a personal branding poster. Do not invent personal facts, employer, contact info, or credentials.
```

小比例场景 / 复杂动作追加片段（同时读取 `author-persona-actions.png`）：

```text
Small-scale or complex-pose reference:
Also reference assets/persona/author-persona-actions.png for the target pose or the small-scale-in-scene example. When Lao Yang appears small in the frame (about 15%-20% width or less), he must still keep: visible thin light-frame glasses silhouette, short straight black hair silhouette close to the head, the narrower-chin tapered face silhouette with a nearly-straight hairline (not a round or square face silhouette, not a sharp widow's-peak point), tan skin tone, short-sleeve + athletic jogger-pants outfit silhouette, tall solid slightly-athletic body proportion relative to the scene, and a clear action (handing, looking, steadying, annotating). Do not let him become a generic faceless background figure at small scale.
```

跑偏返修追加片段（同时读取 `author-persona-spec.png`，仅实物图模式）：

```text
Repair / drift-correction reference:
Also reference assets/persona/author-persona-spec.png (identity ground truth). Fix any deviation shown in its 禁止偏移 panel: not too thin or childish, not a curly/messy explosive hairstyle (should be a natural short straight 3-5cm crew-cut with light natural texture, not fluffy or puffy), not photorealistic human skin, not a flat 2D paper-cutout, not elderly or tired-looking, not a thick black-frame glasses, not pale/fair skin (should be tan/wheat-toned), not a soft baby-face (should be rugged), not thin/simplified lips (should be fuller lips with a clear lip shape, slightly thicker lower lip), not a wide full forehead, and not an exaggerated sharp widow's-peak / M-shaped hairline either (should be a nearly-straight hairline with only a very subtle, soft center dip — match author-persona-spec.png, err toward flatter/more natural rather than a dramatic point), not a wide square jaw or broad square chin (should be a narrower, slightly pointed chin — oval/tapered face, wider at the cheekbones than at the chin), not a slim/plain office-worker build (should be taller and slightly athletic with broader shoulders), not dress pants or skinny jeans (should be athletic/casual jogger-style pants). Restore the 必须保留 anchors: thin light-gray/translucent frame glasses, natural short straight 3-5cm hair with light texture, nearly-straight hairline with a subtle soft center dip (not a sharp peak), narrower tapered chin, fuller lip shape, tan skin, rugged face, mature late-30s presence, tall solid slightly-athletic 183cm/85kg build, short-sleeve + athletic jogger-pants sunny outfit, light-Q 3D toy texture.
```

手绘图模式片段（替代基础片段，读取 `author-persona-handdrawn.png`，不使用轻 Q 3D 描述）：

```text
Author presence (handdrawn mode):
Include the author persona (老杨), using assets/persona/author-persona-handdrawn.png as identity and style reference. Render him as a flat black-line hand-drawn sketch figure matching Little Stone's handdrawn visual language: pure white background, minimalist black ink line art with slightly wobbly pen lines, no 3D volume, no clay/soft-toy rendering, no gradient or soft shadow on the body. Keep the likeness: mature, leaning toward late-30s (not young or smooth-skinned, not elderly or tired), taller and solid build with a slightly athletic physique, slightly broader shoulders, rugged face, healthy tan skin tone. A nearly-straight hairline with only a very subtle, soft center dip (NOT a sharp V-point widow's-peak, NOT dramatically receded temples; the forehead itself is moderate, not wide) and a narrower, slightly pointed chin (oval/tapered face, not a wide square jaw). Also fuller lips with a clear lip shape, a natural short straight 3-5cm crew-cut with light natural texture (not perfectly slicked flat, not fluffy, not curly, not puffy), thin rectangular glasses with a light-frame silhouette (not thick black frame), short-sleeve top with athletic/jogger-style long pants. Keep likeness, not realism; the whole figure should read as a hand-drawn sketch character, not a 3D toy. He should write annotations, draw a small arrow, or hand a module to Little Stone. Little Stone still performs the core conceptual action. Do not make it a realistic portrait, a 3D digital toy, an anime character, a childish cartoon, an elderly man, a tired worker, or a personal branding poster.
```
