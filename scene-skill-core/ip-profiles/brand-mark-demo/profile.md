# Mark Demo · 示意品牌标（公开）

## 定位

公开演示：客户已有 **App Icon / Logo** → Profile Enrollment → 多模式配图。
本 profile 使用项目自有示意标，不是第三方商标。

## Profile ID

`mark-demo`

## Profile Contract

契约：`../../references/contracts/profile-contract.md`。

```yaml
id: mark-demo
display_name: 示意品牌标（公开演示）
status: AVAILABLE
input_kind: brand_mark
identity:
  canonical_asset: assets/reference/brand-mark-primary.png
  identity_sheet: assets/examples/00-identity-sheet.png
  reference_source: user_provided  # 演示用：项目自有示意原件，语义等同客户提供的原件
  description_source: character.md
  anchors:
    - 圆角方标外轮廓
    - 深青绿底 #0F766E
    - 浅色 Y 形分叉图形（双圆角短枝 + 竖干）
    - 无文字
    - 扁平单层图标（非 3D 拟物）
  temperament: 利落、可执行、偏工具感
references:
  ref_mode: dual
  ref_mode_policy: 有模式校准图时 dual；知识卡/PPT 无校准则降级 single
  calibration:
    identity_sheet: assets/examples/00-identity-sheet.png
    handdrawn: assets/examples/01-handdrawn-calibration.png
    physical: assets/examples/02-physical-scene.png
    action-library: assets/examples/03-action-library.png
    knowledge-card: none
    ppt: none
behavior:
  actions: [指向, 拉动, 托举, 连接, 挡开, 递交]
  sequence_guide: 沿故事路径做一个主动作；图标角色化必须可回溯到 brand-mark-primary 锚点
qa:
  failure_signals:
    - 画成小石头白圆眼橙色胶囊
    - 丢失圆角方标外轮廓
    - 主色漂成橙/紫品牌风
    - 出现第三方商标或 Claude 形象
    - 站桩装饰无动作
privacy:
  public_assets:
    - assets/reference/brand-mark-primary.png
    - assets/examples/00-identity-sheet.png
    - assets/examples/01-handdrawn-calibration.png
    - assets/examples/02-physical-scene.png
    - assets/examples/03-action-library.png
  private_assets: []
```

## 与 custom-ip-demo

| | mark-demo | custom-ip-demo |
| --- | --- | --- |
| 输入 | 自创 brand mark | 第三方立绘参考 |
| 公开 | 是 | 否（private） |
| 叙事 | Logo/Icon → 管线 | 已有角色图流程样例 |

## 示意标设计锁（Task 4 生图依据）

```text
Name: Mark Demo / 示意品牌标
Shape: iOS-style rounded square App Icon
Palette: deep teal #0F766E fill; off-white #F8FAFC glyph
Glyph: abstract skill-fork — vertical rounded stem splitting into two short rounded branches at the top (Y / tuning-fork silhouette), not a letter C, not Anthropic starburst, not orange capsule, not Cursor L-corner
No text, no third-party logo, no Claude silhouette
```

## 资产索引

| 文件 | 角色 | 状态 |
| --- | --- | --- |
| `assets/reference/brand-mark-primary.png` | Layer 1 主身份锚点 | 已生成 |
| `assets/examples/00-identity-sheet.png` | Layer 2 拟人设定图 | 已生成 |
| `assets/examples/01-handdrawn-calibration.png` | Layer 3 手绘模式校准 | 已生成（identity_sheet 锚定） |
| `assets/examples/02-physical-scene.png` | Layer 3 实物图模式场景 | 已生成 |
| `assets/examples/03-action-library.png` | Layer 3 动作库示例 | 已生成 |
