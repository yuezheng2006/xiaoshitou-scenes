# 自定义品牌标 IP · 交付说明

面向**已有 Logo / App Icon** 的品牌方与内容团队。把标识纳入 `scene-skill-core` 多模式配图管线，而不是从 0 捏吉祥物。

## 适合谁

- 已有 App Icon、扁平 Logo 或品牌标，希望配图里长期「像同一个标」
- 内容团队 / 讲师 / 运营，需要正文、白板、实物场景等多载体输出
- 不需要先设计完整角色立绘，只需把标识适配到各模式

## 客户提供

1. **标识原件** — PNG/SVG 等，Logo / App Icon / 扁平标均可
2. **授权确认** — 确认可在本地 Skill 与交付样张中使用（真标默认 `private_assets`，不进公开仓）
3. **（可选）** 主色色值、禁用项、是否允许角色化/拟人化

## 我方交付

| 交付物 | 说明 |
| --- | --- |
| `ip-profiles/<客户-ip-id>/` | profile.md、character.md、logo-safety.md、资产目录 |
| Enrollment 状态记录 | REQUESTED → … → AVAILABLE 全程 Card |
| **最小样张包** | Layer 1 身份锚点 + Layer 2 拟人设定图 + Layer 3（手绘 + 实物 + 动作库） |
| **一次正文试跑** | Layer 4：粘贴一篇内容，产出 1 张正式配图验证 |

## 里程碑

```text
客户提供 Logo/Icon
  → IDENTITY_PLAN（确认锚点 + 拟人方向，确认前不生图）
  → CANONICAL_ASSET（Layer 1）
  → IDENTITY_SHEET（Layer 2 · 拟人设定图，用户确认）
  → MODE_CALIBRATION（Layer 3 · handdrawn → physical → action-library）
  → AVAILABLE
  → 正文试跑（Layer 4 · 1 张正式场景图）
```

## 不含项

- 从 0 原创吉祥物 / 全新 IP 设计（可另议）
- 知识卡 / PPT 全套金样（可加购，协议支持懒加载校准）
- 客户真商标的公开仓库分发
- 在线支付 / SaaS（当前为 Skill + 服务交付）

## 服务档位（名称，不含报价）

| 档位 | 内容 |
| --- | --- |
| **录入基础包** | Enrollment + 最小样张 + 一次试跑 |
| **四模式加购** | 知识卡 / PPT 校准与样张 |
| **企业私有包** | 私有 profile + 行业物件 + 内部分发说明 |

## 销售主示例（本地 · 豆包）

**推荐对客户演示：** [`.temp/brand-mark-enrollment/doubao-local/`](../.temp/brand-mark-enrollment/doubao-local/)（真 App Icon → 拟人化小助手，样张更生动；**不进 Git**）

- [豆包 Icon 原件](../.temp/brand-mark-enrollment/doubao-local/assets/reference/doubao-app-icon.png)
- [00 拟人设定图](../.temp/brand-mark-enrollment/doubao-local/assets/examples/00-identity-sheet.png)
- [01 手绘校准](../.temp/brand-mark-enrollment/doubao-local/assets/examples/01-handdrawn-calibration.png)
- [02 实物场景](../.temp/brand-mark-enrollment/doubao-local/assets/examples/02-physical-scene.png)
- [03 动作库](../.temp/brand-mark-enrollment/doubao-local/assets/examples/03-action-library.png)
- [04 正文试跑 · Agent 三步](../.temp/brand-mark-enrollment/doubao-local/assets/examples/04-content-demo-handdrawn.png)

## 公开占位金样（无第三方商标）

可进 README / 公开仓：[`scene-skill-core/ip-profiles/mark-demo/`](../scene-skill-core/ip-profiles/mark-demo/)

- [Layer 1 示意标](../scene-skill-core/ip-profiles/mark-demo/assets/reference/brand-mark-primary.png)
- [Layer 2 拟人设定图](../scene-skill-core/ip-profiles/mark-demo/assets/examples/00-identity-sheet.png)
- [Layer 3 手绘 / 实物 / 动作库](../scene-skill-core/ip-profiles/mark-demo/assets/examples/)

## 与 custom-ip-demo 分流

| | doubao-local（本地） | mark-demo（公开） | custom-ip-demo |
| --- | --- | --- | --- |
| 输入 | 豆包 App Icon | 自创示意标 | 第三方立绘 |
| 公开 | 否，销售私演示 | 是 | 否 |
| 叙事 | **真 Icon → 生动拟人助手** | 占位金样 | 立绘支线 |

## Agent 触发示例

```text
用这个 App Icon 做一个自定义 IP，先建立档案，暂时不要生成配图。
```

确认身份方案后：

```text
用已录入的品牌标 profile，把下面这篇内容生成 1 张 16:9 手绘图。
```
