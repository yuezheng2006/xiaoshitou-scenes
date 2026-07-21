# brand_mark 模式 · Logo/Icon 拟人化配图

> 主路径：`input_kind=brand_mark`。客户已有 Logo / App Icon，不是从 0 捏吉祥物。  
> 契约：`contracts/profile-contract.md` · 槽位：`common-prompt-slots.md` §D

> **⚠️ 工具约束**：拟人设定图和模式校准图的生成**必须**使用 Codex 自带的 `imagen` 工具，支持传入 Logo/Icon 原件作为参考图。详见 `codex-environment-guidance.md` § 三.6。

## 一句话

**从 Icon 提取身份 → 生成拟人设定图 → 再进各模式校准**；场景里是「从头生长的小助手」，不是方标贴头。

## 三层参考（Enrollment 后）

```text
Layer 1  canonical_asset     App Icon / Logo 原件（身份锚点，只锁标内图形/主色/气质）
Layer 2  identity_sheet      拟人设定图（从头生长的完整角色，禁止 icon-as-head）
Layer 3  mode_calibration     手绘 / 实物 / 动作库 / …（该模式下怎么画、怎么动）
```

生成顺序：

```text
USER_REFERENCE → IDENTITY_PLAN（确认锚点 + 拟人方向）
  → 生成 identity_sheet（用户确认）
  → handdrawn_calibration → physical_calibration → action_library（按需）
  → AVAILABLE
```

Layer 2 完成前，不要批量产出正式内容图。

## 拟人化硬规则

| 必须 | 禁止 |
| --- | --- |
| 从 Icon **内**图形提取：脸、发型、主色、气质 | 圆角方标 / Logo 方块直接当脑袋（icon-as-head） |
| 完整头身比例的小角色（可 chibi，但像人） | stick figure + 贴一张方图 |
| 有表情、有主动作倾向（生动，不站桩） | 纯黑白（除非用户明确要求线稿） |
| 手绘保留暖色 + 橙/红/蓝功能色 | 画成小石头橙色胶囊 |
| 真标 `private_assets`，公开仓只用自创示意标 | 未授权第三方商标进公开 Git |

## 生动度（默认）

- 表情：友好、专注、略活泼；禁止僵硬证件照站桩。
- 动作：每张图 **1 个主动词**；身体可有 lean / 挥手 / 推拉倾向。
- 颜色：Icon 主色保留在服装/发色/点缀；功能色按 `handdrawn-style-dna.md`。
- 实物：小助手与物件有真实接触阴影；可带轻微「帮忙感」道具。

## Prompt 片段（brand_mark 校准）

```text
Brand mark anthropomorphization lock:
- Reference Layer 1: attach canonical App Icon — extract ONLY inner avatar/glyph identity (face, hair, palette, mood), NOT the rounded-square frame as the character head.
- Reference Layer 2: attach identity_sheet — this is the approved full-body anthropomorphized assistant derived from the icon.
- Render a complete friendly assistant character with normal head-and-body proportions. NEVER paste the app icon square as the head. NEVER stick-figure with icon sticker head.
- Keep warm soft colors from the brand; use orange/red/blue functional accents on whiteboard scenes (see handdrawn-style-dna.md). NOT pure black-and-white unless user explicitly asked.
- One clear verb; expressive face; dynamic but clean composition.
```

## QA（brand_mark 专用）

**手绘**

- [ ] 无 icon-as-head / 无方标贴头
- [ ] 脸/发型/主色可回溯 Layer 1 + Layer 2
- [ ] 非纯黑白（除非用户要求）
- [ ] 有主动作，非站桩装饰
- [ ] 功能色克制（橙路径、红重点、蓝补充）

**实物**

- [ ] 拟人小助手（或小巧玩偶感），非 Logo 方块道具
- [ ] 与物件有明确互动动词
- [ ] 身份可识别，非 generic 动漫女孩/男孩

**失败信号**

- icon-as-head、stick figure 贴方图
- 纯 monochrome 线稿（用户未要求）
- 站桩无动作、无表情
- 像小石头 / 像 unrelated 吉祥物
- 身份_sheet 与 canonical 气质完全脱节

## 销售演示

- **本地主示例（生动）**：`.temp/brand-mark-enrollment/doubao-local/`（豆包 Icon，不进 Git）
- **公开占位**：`ip-profiles/mark-demo/`（自创示意标）

## 相关文件

- `contracts/profile-contract.md` — 状态机 + input_kind
- `handdrawn-qa-checklist.md` — brand_mark 检查块
- `physical-qa-checklist.md` — brand_mark 检查块
- `examples/custom-ip-delivery.md` — 交付清单
