# Profile · 老杨

> **当前固定人物规则（2026-08-06）**：老杨约 35 岁，身高 180cm、体重 86kg；长腿、躯干约 40% / 腿约 60%、头身约 1:7.5。Profile 不因每次校准反馈自动升级版本号。

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

造型补充：老杨身高 180cm、体重 86kg，腿比较长，保持上短下长的 4:6 体态。日常最常穿 New Balance 1906R 或 2002R 复古跑鞋，以用户提供的两张鞋图为造型参考。生成全身或大半身时，鞋款作为固定配件层保留；除非用户明确改设定，不在同批任务中切换为帆布鞋、正装鞋或其他鞋型。

## Physical 人脸校准

physical 模式优先使用用户当前会话提供的真实人脸参考：约 35 岁的真实成年男性面相、黑色短碎发、较厚深色方框眼镜、宽方圆脸、自然鼻口结构与轻微全脸胡茬。该参考属于私有校准素材，不复制进公开 Profile 或 IP Pack；handdrawn / knowledge-card 继续使用已验收的风格化人脸参考。

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
