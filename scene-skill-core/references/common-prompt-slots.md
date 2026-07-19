# 通用 Prompt 槽位组装

> 本文件只定义组装顺序与槽位职责。具体 IP 文案来自当前 `ip-profiles/<id>/character.md`（及 persona 文件）；模式 DNA 来自 `physical-*` / `handdrawn-*` / 知识卡 / PPT 文件。不要在本文件硬编码具体角色名或主色。

每张图单独组装。交付给用户的完整提示词仍以中文为主；槽位内部可保留稳定的英文锁色 / 风格关键词。

---

## 组装顺序

```text
{REF_IMAGE}            ← 附件见下方：老杨双参考 / 小石头单锚点 / none
{IP_DESC}              ← 主角色 character.md「填入 {IP_DESC}」；none 读 none profile
{PERSONA_DESC}         ← 仅老杨出镜：Persona Identity Lock + 面相锚点；否则删除
{MODE_DNA}             ← 当前模式视觉 DNA（实物/手绘/知识卡/PPT）
{WHITESPACE_DESC}      ← 留白与背景约束
{STYLE_ADAPT}          ← 通用层：模式如何适配有角色的画面（不写死具体锚点色）
{IP_STYLE_ADAPT}       ← 主角色 character.md「填入 {IP_STYLE_ADAPT}」；无则留空
{PERSONA_STYLE_ADAPT}  ← 仅老杨出镜：渲染语言锁（3D vs 线稿）+ 防串台；否则删除
{FLAT_LIMBS_LOCK}      ← 来自 character.md 维度锁（flat 2D profile 必写）
{COMPOSITION_DESC}     ← 构图 / 母版变异 / 结构类型
{MESSAGE_DESC}         ← 3 秒读懂句 / 核心信息
{SUBJECT_DESC}         ← 主物件或结构 + 角色动作
{LABEL_DESC}           ← 短中文标签 / 批注
{RATIO_DESC}           ← 比例
{NEGATIVE_DESC}        ← 模式负面 + IP/persona 负面合并
```

与 `common-generation-templates.md` 的关系：模板仍可按模式给出完整示例；**生成前必须能指出上述槽位各自填了什么**。换 IP 时只改 profile 内文案与资产路径，不要改本文件顺序。

---

## 变量来源

| 槽位 | 来源 | 说明 |
| --- | --- | --- |
| `{REF_IMAGE}` | 见下方参考图协议 | **双参考只用于对齐老杨** |
| `{IP_DESC}` / `{IP_STYLE_ADAPT}` | `character.md` | 小石头等主角色 |
| `{PERSONA_DESC}` / `{PERSONA_STYLE_ADAPT}` | `persona-author-*` | 老杨出镜时必填 |
| `{MODE_DNA}` | 模式 style / mode 文件 | 只描述「怎么画」，不描述「画谁」 |
| `{FLAT_LIMBS_LOCK}` | `character.md` | 2D Flat Lock + Limbs Lock（若 profile 声明 flat 2D） |

---

## 参考图协议

每次组装前先读取当前 profile 的 Profile Contract，确认 `ref_mode` 和当前模式是否有 calibration asset：

- `none`：不传固定角色设定图。
- `single`：只传身份锚点。
- `dual`：传身份锚点 + 当前模式校准图。
- profile 默认是 `single` 且当前模式存在可用校准图时，可在本次 Render Card 中升级为 `dual`。
- 当前模式没有校准图：运行降级为 `single`，并记录可懒加载校准图；不得声称已使用双参考。

### A. 老杨出镜 → 双风格对齐（强制）

**实物 / 长卷（真人实体）**
1. 必传 `author-persona-panorama.png`
2. 多场景或脸不稳：加 `author-persona-face-lock.png`；复杂姿态加 `actions`

**手绘 / 知识卡 / PPT（手绘更重要）**
1. 必传 `author-persona-panorama-handdrawn.png`
2. 必传 `author-persona-panorama.png`（锁与实体同一人）
3. 全身出镜建议加 `author-persona-handdrawn-body.png`（身材比例金样）
4. 多场景同批必加 `author-persona-face-lock.png`；脸漂时单张也可加
5. 可选加 spec / 旧 handdrawn 补强

猫若出现：金**黄**色金渐层英短（见全景蹲姿区）。

同框小石头：另加 `primary-character-reference.png`。

### B. 仅小石头（未触发老杨）→ 单锚点

1. **必传** `assets/character/primary-character-reference.png`
2. 复杂姿态 / 多人 / 小比例：可加 `primary-character-actions.png`
3. 身份漂移时可选 `assets/character/examples/` 样张 1 张（**非强制**）

### C. `$IP=none` / `ip-profiles/none`

不传角色设定图；画面以物件/结构为主；需要「谁在操作」时可画功能性简笔人。

---

## `{STYLE_ADAPT}` vs `{IP_STYLE_ADAPT}` vs `{PERSONA_STYLE_ADAPT}`

| 层 | 管什么 | 不管什么 |
| --- | --- | --- |
| `{STYLE_ADAPT}` | 线稿/摄影棚质感、场景点睛色如何稀疏使用 | 具体角色/人脸锚点 |
| `{IP_STYLE_ADAPT}` | 主角色主色不漂（如 `#f39800`） | 构图、老杨面相 |
| `{PERSONA_STYLE_ADAPT}` | 老杨 3D vs 线稿不串台、面相比例优先于 Q 感 | 小石头锁色 |

---

## 组装检查（生成前）

- [ ] 实物老杨：实体 panorama 已进上下文
- [ ] 手绘老杨：手绘 panorama + 实体 panorama 已进上下文（锁同一人）
- [ ] 多场景同批：已做 **1 张预览门禁**；通过后再批跑
- [ ] 多场景同批：每张同一套参考 + face-lock + 同一段 Feature Stability Lock + Outfit/Accessory Layer
- [ ] 表情：已声明 Expression Preset（E0–E4），未临场乱写
- [ ] 手绘全身：已加 handdrawn-body（或比例已确认对齐金样）
- [ ] 出猫：金黄金渐层，非灰虎斑
- [ ] 仅小石头：设定图已进上下文（单锚点）
- [ ] `{IP_DESC}` / `{IP_STYLE_ADAPT}` 已按主角色填写
- [ ] 老杨出镜：`{PERSONA_DESC}` / `{PERSONA_STYLE_ADAPT}` 已填写
- [ ] flat 2D profile：`{FLAT_LIMBS_LOCK}` 已写入
- [ ] 未触发老杨：无 persona 肖像
- [ ] none profile：无品牌角色
