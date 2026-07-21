# Mark Demo · 示意品牌标

公开演示 profile：`input_kind=brand_mark`，展示客户已有 **App Icon / Logo** 如何进入 Profile Enrollment 并完成多模式配图。

## 流程

```text
App Icon / Logo（示意标 · Layer 1）
  → Profile Enrollment（brand_mark）
  → 拟人 identity_sheet（Layer 2 · 用户确认）
  → 模式校准图（Layer 3 · handdrawn / physical / action-library）
  → status: AVAILABLE
  → 正式内容场景（Layer 4）
```

与 `custom-ip-demo`（私有立绘支线）对比见 `profile.md` 表格。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| [profile.md](profile.md) | Profile Contract、资产索引、与 custom-ip-demo 对比 |
| [character.md](character.md) | 身份锁、`{IP_DESC}`、`{IP_STYLE_ADAPT}` |
| [logo-safety.md](logo-safety.md) | 公开示意标 vs 客户真标边界 |
| [assets/reference/](assets/reference/README.md) | 主身份锚点 [brand-mark-primary.png](assets/reference/brand-mark-primary.png) |
| [assets/examples/](assets/examples/README.md) | 模式校准与场景示例 |

## 示例资产

- [brand-mark-primary.png](assets/reference/brand-mark-primary.png) — Layer 1 主标
- [00-identity-sheet.png](assets/examples/00-identity-sheet.png) — Layer 2 拟人设定图
- [01-handdrawn-calibration.png](assets/examples/01-handdrawn-calibration.png) — Layer 3 手绘校准
- [02-physical-scene.png](assets/examples/02-physical-scene.png) — Layer 3 实物图场景
- [03-action-library.png](assets/examples/03-action-library.png) — Layer 3 动作库

## 边界

- 本 profile **公开**；客户真实商标默认 **私有**，不得进入公开示例。
- Claude Code 等第三方标识仅作**本地私有** QA 对照，**不得 commit**。
- 录入期间勿路由到默认小石头或「贴 Logo 到小石头」流程。

契约详情：`../../references/contracts/profile-contract.md`。
