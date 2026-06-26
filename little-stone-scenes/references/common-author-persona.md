# 作者出镜规则

## 定位

「老杨」是本仓库作者 `yuezheng2006` 的数字形象。它是可选人物角色，用于作者自述、项目复盘、方法论讲解、Skill 介绍或用户明确要求作者出镜的场景。

参考图：

```text
assets/persona/author-persona-ref.jpg
```

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

## 生图前必须读取

当作者出镜时，生成前必须读取：

- `assets/persona/author-persona-ref.jpg`
- `assets/brand/little-stone-ref.png`
- 当前模式对应的参考文档和模板

## 形象约束

老杨数字形象应参考用户提供头像，但只要求 **形似**，不要过度写实：

- 成熟亚洲男性，身高约 183cm、体重约 85kg，整体气质成熟、亲和、认真、克制。
- 体型更高大结实，站姿更挺拔，肩膀略宽，脖颈和下颌更成熟，面容有接近四十岁的稳重感；不要画得过瘦、少年感或幼态，也不要画老、画疲惫，或夸张成健身房肌肉人。
- 短黑直发。
- 黑色矩形眼镜。
- 干净浅色上衣。
- 实物图里优先画成轻 Q 3D 数字玩偶 / 软黏土感角色：五官更简洁，头身比例略 Q，轮廓更柔和，有圆润体积、柔和边缘和轻微立体阴影。
- 皮肤和五官不要照片级纹理；保留形似，不追求真人皮肤、真实毛孔、真实人像光影。可以有干净的 3D 体积感，但不是写实人像。

不要追求照片级复刻。不要发明明显不同的人物身份、年龄、发型、服装风格或夸张表情。不要把作者画成名人、二次元、儿童卡通、企业高管海报、真实人像摄影或过度商业写真。

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
- 作者应与真实物件处在同一白色空间，但保持轻 Q 3D 数字玩偶质感；要有体积、圆润边缘和柔和接触阴影，不要变成扁平 2D 纸片人。
- 不要使用照片级真人皮肤、真实人像光影或商业人像海报质感。
- 画面不要做成头像展示、人物专访封面或个人品牌海报。

推荐结构：

```text
真实物件主现场 + 小石头执行动作 + 老杨递工具/看反馈/做旁白
```

## 手绘图模式

手绘图里：

- 老杨可以简化为手绘人物或半身讲解者，但保留黑框眼镜、短黑发等识别点。
- 不要追求肖像写实；要融入白板解释图。
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

```text
Author presence:
Include the author persona (老杨), the author yuezheng2006, using assets/persona/author-persona-ref.jpg as the identity reference. Keep only a likeness: mature 35+ Asian male, about 183cm and 85kg, taller and solid build, slightly broader shoulders, upright posture, more mature face, mature neck and jawline, short straight black hair, black rectangular glasses, clean light top, calm and friendly. In physical-object mode, render him as a light-Q 3D digital toy / soft-clay character with rounded volume, soft edges, clean matte skin-color surfaces, and gentle contact shadow, not a flat 2D cutout. Keep the likeness through face shape, glasses, short straight hair silhouette, hairline, mature late-30s presence, and taller solid build. Do not make him a semi-realistic digital human or a photorealistic portrait. Avoid realistic skin texture, pores, photo lighting, and realistic human-arm details. Avoid making him too young, too thin, childish, anime-like, elderly, tired-looking, or exaggerated bodybuilder-like. The author persona must interact with Little Stone and the scene, not appear as a standalone portrait. Keep the author persona supporting, usually no more than 30%-35% of the main visual weight. Do not make it a personal branding poster. Do not invent personal facts, employer, contact info, or credentials.
```
