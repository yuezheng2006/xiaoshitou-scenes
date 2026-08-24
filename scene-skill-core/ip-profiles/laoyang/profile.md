# Profile · 老杨

> **当前固定人物规则（2026-08-07）**：老杨约 34–35 岁，面部保留真人骨相、五官比例和自然不对称，采用有细节的扁平 2D 角色插画表达：清晰且有粗细变化的线稿、平涂色块、局部轻阴影、发丝分组和衣物褶皱；不做照片级写实、3D 渲染或无细节扁平图标。脸长适中、脸颊自然饱满，下唇体积明显但不画清晰唇线、嘴缝线或上下唇勾勒，不画成过短过圆或玻璃皮肤。身高 180cm、体重 86kg；略健壮的肩背与胸廓、饱满但不夸张的四肢，腰线收住，小腿略粗壮饱满且与大腿协调；腿比普通比例略长但自然，胯部到脚底约 55%–56%，头顶到胯部约 44%–45%，禁止 1:1 和超长腿怪物比例。Profile 不因每次校准反馈自动升级版本号。

## 定位

这是老杨的独立 Persona IP Profile。它可以单独生成老杨内容，也可以在双 IP 任务中作为主讲 IP 与 `default-little-stone` 组合。

```text
单人任务：老杨主讲、拆解、批注、检查和收束
双 IP 任务：老杨主讲/调度，小石头执行
```

## 资产来源

本 Profile 使用 `asset_source.profile_id=default-little-stone` 复用已经验收的风格化老杨资产，不复制真人照片，也不重复维护二进制文件。导出 IP Pack 时，Builder 会把声明的公开资产复制到 Pack 内。

核心资产：

- 身份主锚点：`assets/persona/reference/author-persona-panorama.png`
- 手绘模式校准：`assets/persona/reference/author-persona-panorama-handdrawn.png`
- 面相锁：`assets/persona/face-lock/author-persona-face-lock.png`
- 动作扩展：`assets/persona/reference/author-persona-actions.png`
- 手绘批内金样：`assets/persona/examples/validated-batch-anchor-handdrawn.png`

造型补充：老杨身高 180cm、体重 86kg，腿比普通比例略长但自然：胯部到脚底约 55%–56%，头顶到胯部约 44%–45%，大腿和小腿均匀拉长，小腿略粗壮饱满但不健美、不粗短，禁止 1:1 或超过 60% 的怪物长腿。肩背和胸廓略宽厚，上臂与大腿略饱满但腰线收住。常穿米色短袖 T 恤与橄榄卡其宽松短裤，裤长盖过膝盖一点，裤腿有余量，不贴腿、不紧身。日常最常穿 New Balance 1906R 或 2002R 复古跑鞋，以用户提供的两张鞋图为造型参考。生成全身或大半身时，鞋款作为固定配件层保留；除非用户明确改设定，不在同批任务中切换为帆布鞋、正装鞋或其他鞋型。

## Physical 人脸校准

physical 模式优先使用用户当前会话提供的真实人脸参考：约 34–35 岁的真实成年男性面相、黑色短碎发、较厚深色方框眼镜、脸长适中的宽方圆脸、自然鼻口结构与轻微全脸胡茬。该参考属于本次会话的临时校准素材，不复制进公开 Profile 或 IP Pack；handdrawn / knowledge-card 只借鉴真人的面部结构与比例，统一采用有细节的扁平 2D 角色插画表达，保留线稿层次、平涂、局部阴影、发丝分组和衣物褶皱；下唇保留体积但禁止清晰唇线、嘴缝线和上下唇勾勒，禁止照片级写实、3D 渲染、磨皮滤镜和无细节扁平图标。

## 身份边界

### 固定身份

- 约 34–35 岁、180cm / 86kg、略健壮且腿比普通比例略长的老杨。
- 宽方圆脸、脸长适中、浅灰细框大镜片眼镜、3–5cm 黑色短直发、下唇有体积但无唇线。
- 米色短袖 T 恤、橄榄卡其宽松过膝短裤、New Balance 1906R 或 2002R。
- handdrawn / knowledge-card 采用有细节的扁平 2D 角色插画；physical 使用成熟克制的风格化实物表达。

### 允许变化

- 只改变动作、姿态、朝向、视线、轻微表情和与内容相关的道具关系。
- 多 IP 场景可以改变老杨与小石头的站位和职责，但不改变老杨身份锚点。

### 禁止漂移

- 不得改变年龄感、身高视觉、腿部比例、脸型、眼镜、发型、嘴部无唇线特征、服装和 New Balance 鞋款。
- 不得把老杨变成 160/175 视觉档、矮宽小矮子、照片级肖像、3D 人物或无细节图标。
- 不得在单人任务中自动加入小石头；不得把角色设定板背景、标题或四视图排版复制进正文图。

上述边界对应 `profile.manifest.json` 的 `identity.allowed_variations` 与 `identity.forbidden_drift`，生成前用于组装身份提示，生成后用于 QA 返修定位。

## 模式边界

| 模式 | 老杨表达 | 当前状态 |
| --- | --- | --- |
| physical | 成熟克制的风格化 3D | AVAILABLE |
| handdrawn | 扁平黑线手绘人物 | AVAILABLE |
| knowledge-card | 手绘语言 + 批内金样 | AVAILABLE |
| ppt | 先做导演规划，暂不声称双参考校准 | DEFERRED |
| video | 走视频独立 Gate，不复用静态图结论 | DEFERRED |

模式校准缺失时只能降级为 `single`，不能伪称 `dual`。

## 单人 / 双 IP 边界

- 选择 `laoyang` Profile 的单人任务，不自动加入小石头。
- 只有用户明确要求“老杨和小石头”或任务显式组合两个 Profile 时，才启用双 IP。
- 双 IP 任务仍遵守老杨主讲、小石头执行的叙事契约。
- 老杨单人任务的 QA 重点是面相、眼镜、发型、体态、模式渲染语言和动作职责。

完整机器契约见同目录 `profile.manifest.json`；通用流程见 `references/contracts/profile-contract.md`。
