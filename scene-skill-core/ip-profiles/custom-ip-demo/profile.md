# Custom IP Demo · 用户参考图驱动示例

## 定位

这是一个用于演示“用户上传真实图 → IP 录入 → 模式校准 → 正式配图”的示例 Profile。

它不是默认 Profile，也不自动参与普通配图路由；状态停留在 `IDENTITY_PLAN`，用于展示 Profile Enrollment Card 如何承接真实参考图。

## Profile ID

`custom-ip-demo`

## Profile Contract

契约模板：`../../references/contracts/profile-contract.md`。

```yaml
id: custom-ip-demo
display_name: 用户参考图驱动的森林潮玩角色（示例）
status: IDENTITY_PLAN
identity:
  canonical_asset: assets/reference/reference-character-primary-brown.png
  reference_source: user_provided
  anchors:
    - 毛绒长耳
    - 圆润头身比例
    - 大椭圆眼睛
    - 小鼻子与顽皮笑容
    - 短手短脚
    - 紧凑潮玩体量
references:
  ref_mode: single
  ref_mode_policy: 主参考图锁身份；蓝色参考图只作为变体与动作辅助
  calibration:
    handdrawn: assets/examples/01-handdrawn-calibration-input-process-output.png
    physical: assets/examples/02-physical-scene-untangle-thread.png
    knowledge-card: assets/examples/03-knowledge-card-three-steps.png
    action-library: assets/examples/04-action-library-pull-brace-handoff.png
behavior:
  actions: [拉, 拖, 抱, 探, 爬, 递, 挡, 守, 庆]
  sequence_guide: 沿故事路径承担一个动作，不在每个节点复制角色或站桩装饰
qa:
  failure_signals: [长耳缺失, 头身比例漂移, 眼睛形状漂移, 多余角色, 品牌元素误复制]
privacy:
  public_assets: []
  private_assets:
    - assets/reference/reference-character-primary-brown.png
    - assets/reference/reference-character-variant-blue.png
```

## 参考图角色

| 文件 | 角色 | 用法 |
|---|---|---|
| `assets/reference/reference-character-primary-brown.png` | 主身份锚点 | 锁定核心外形、眼睛、耳朵、比例和整体气质 |
| `assets/reference/reference-character-variant-blue.png` | 变体参考 | 只辅助颜色、服装、动作和道具变化，不覆盖主身份 |

两张图中的吊坠、赛事标识、品牌文字不进入默认 IP Contract；如需商业使用，必须另行确认授权。

## 示例输出

- `01-handdrawn-calibration-input-process-output.png`：手绘模式校准图。
- `02-physical-scene-untangle-thread.png`：实物图模式正式场景。
- `03-knowledge-card-three-steps.png`：知识卡模式示例。
- `04-action-library-pull-brace-handoff.png`：动作库示例。
- `05-handdrawn-action-library-rich.png`：九宫格手绘丰富动作库。

## 录入状态

```text
USER_REFERENCE → IDENTITY_PLAN → 用户确认
                         ↓
              CANONICAL_ASSET / AVAILABLE
```

当前示例已经有用户真实参考图，但仍需用户确认身份锚点和公开范围，不能直接作为默认可用 IP 发布。
