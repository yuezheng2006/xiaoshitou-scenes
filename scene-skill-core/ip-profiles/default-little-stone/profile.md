# Default IP Profile: Little Stone + 老杨

## 定位

这是 `scene-skill-core` 的默认 IP profile，包含**双 IP 互动系统**，以及独立的**老杨小剧场**入口：

```text
小石头 = 主角色 / 执行 Agent（flat 2D 胶囊）
老杨   = 可选 persona
         · 路径 B：触发后与小石头双 IP 互动（无「小剧场」）
         · 路径 C：老杨小剧场（潮玩视觉印记；默认同人；+小石头 → C 组合）
```

未触发老杨时，只使用小石头。触发路径 B 后，从 `persona-author.md` 进入分层读取链，并读 `references/persona-scene-patterns.md`。触发路径 C（必须含 `小剧场`）时，读 `persona-author-theater.md`；C 组合时另传小石头锚点，**不要**套双 IP 强制互动规则。

## Profile ID

`default-little-stone`

## Profile Contract

契约模板：`../../references/contracts/profile-contract.md`。

```yaml
id: default-little-stone
display_name: 小石头 + 老杨
identity:
  canonical_asset: assets/character/primary-character-reference.png
  reference_source: user_provided
  anchors: [橙色胶囊, 白圆眼, 无嘴, 2 臂 2 腿, flat 2D]
  temperament: 认真、靠谱、略笨、有点倔
references:
  ref_mode: single
  ref_mode_policy: 默认单锚点；当前模式明确使用校准图时升级为 dual
  calibration:
    physical: assets/character/examples/
    handdrawn: assets/character/examples/
    knowledge-card: none
    ppt: none
behavior:
  actions: [拉, 挡, 推, 扛, 解, 贴, 接, 修, 守, 递]
  sequence_guide: 沿故事路径承担一个连续动作，不在每个节点复制或站桩装饰
qa:
  failure_signals: [颜色漂移, 胶囊比例漂移, 有嘴, 多手臂, 角色只站桩]
privacy:
  public_assets: [主角色设定图, 非品牌公开样张]
  private_assets: [品牌 Logo, 用户授权的人像参考图]
```

默认小石头主角色使用 `single` 身份锚点；老杨是独立 persona，遵循 persona 自己的双参考协议，不把双 IP 的参考图规则混入小石头 Profile。

## 主角色

- 角色文件：`character.md`（含 `{IP_DESC}` / `{IP_STYLE_ADAPT}`；默认**单锚点**）
- 设定图：`assets/character/primary-character-reference.png`（必传）
- 动作/多人/小比例扩展：`assets/character/primary-character-actions.png`（条件）
- 可选样张：`assets/character/examples/`（身份漂移时可选，非强制）
- 默认触发词：`小石头`、`Little Stone`
- 主要颜色：`#f39800`
- 角色气质：认真、靠谱、略笨、有点倔；**雷石员工 = AI native**（见 `character.md`）。KTV 巡检/房态/场所服务**不是我们的场景**，且不带工牌。
- Prompt 槽位：`../../references/common-prompt-slots.md`

## 可选 Persona（老杨）

### 路径 B — 双 IP 互动（默认）

分层入口：`persona-author.md`（摘要 + 读取顺序）

| 文件 | 职责 |
| --- | --- |
| `persona-author.md` | 触发词、双 IP 分工、最小读取链 |
| `persona-author-identity.md` | 识别锚点、小比例线、禁止偏移 |
| `persona-author-assets.md` | **双参考（对齐人）**、三固定资产、传图规则 |
| `persona-author-modes.md` | 各模式职责与画面权重 |
| `persona-author-prompts.md` | 可复制提示词片段 |

- **双参考**：实物 → `author-persona-panorama.png`；手绘系 → `author-persona-panorama-handdrawn.png` + 实体 panorama。猫：金黄金渐层。
- 互动场景库：`../../references/persona-scene-patterns.md`（触发 persona 时必读）
- 触发词：`老杨`、`作者`、`yuezheng2006`、`我本人`、`我的数字形象`、`让我和小石头一起`、`作者出镜`、`老杨出镜`、`老杨和小石头`、`老杨 IP 图解`
- 触发后：启用双 IP 互动；未触发时不出现老杨。

### 路径 C — 老杨小剧场（潮玩印记 · 可组合小石头）

长文**视觉印记**（Adrian 两步法）。有「小剧场」走 C；再加「小石头」→ **C 组合**（不打回 B）。

| 文件 | 职责 |
| --- | --- |
| `persona-author-theater.md` | 触发、隐私、两步流、C 单人/组合 |
| `persona-author-theater-prompts.md` | 设定图 + 场景 + 组合 prompt |
| `../../references/persona-theater-checklist.md` | Agent 5 秒决策 |

- **硬门槛**：必须含 `小剧场`
- **两步**：① 风格化 IP 设定图 → ② **设定图 + 正文/主题**
- **C 组合**：潮玩底 + 老杨金样 + 小石头 flat 2D；场域词不切模式
- **隐私**：禁止真人照；金样路径见 theater 文档
- 子指令：`流程拆解图` / `核心动作图` / `一鱼两吃` / `老杨设定图`

## Logo 与品牌边界

- Profile Logo 规则：`logo-safety.md`
- 公开包不随 profile 分发真实品牌 Logo 源文件。
- 雷石 Logo 参考：`assets/brand-private/thunderstone-logo-with-wordmark.png`（工牌牌面默认）、`thunderstone-logo-mark.png`（纯图标）；**prompt + 传参考图**。
- `K 歌 / KTV / 音乐科技 / 车载 / 汽车内 / 智能电动 / 家用 / 商用 / 门店经营` 只触发可选物件语境，不自动触发真实 Logo。
- 小石头的背景气味通过中性道具、动作和场景关系表达，不通过真实公司名或商标表达。

## 读取顺序

1. 读取本文件确认当前 profile。
2. 读取 `character.md` 获取主角色形象锁、`{IP_DESC}` / `{IP_STYLE_ADAPT}`（单锚点）。
3. 若触发 **路径 C（老杨小剧场）**：读 `persona-author-theater.md` → `persona-author-theater-prompts.md`；速查 `persona-theater-checklist.md`；有「小石头」则 C 组合并传小石头锚点；**禁止真人照**；**不要**读双 IP 场景库。
4. 若触发 **路径 B（双 IP）**：读 `persona-author.md` → `persona-author-assets.md`（**老杨双参考**）→ `persona-scene-patterns.md`；锁定模式后读 `persona-author-modes.md`；写 prompt 读 `persona-author-prompts.md`；QA/返修读 `persona-author-identity.md`。
5. 若触发 Logo / 工牌 / 展会 / 品牌物料，读取 `logo-safety.md`。
6. 再进入 `references/`：`common-prompt-slots.md`（组装顺序）+ 通用模式、母版、QA 和 `common-generation-templates.md`。

## 无角色路径

用户说「不要人物 / 纯物件 / 无 IP / none」时，切换到 `../none/profile.md`，不要继续使用本 profile 的角色资产。

## 替换 IP 的原则

新增 IP 时复制本目录结构为 `ip-profiles/<ip-id>/`，只替换 profile 文件、角色资产、persona（含双参考资产与 `examples/`）、`{IP_DESC}` / `{IP_STYLE_ADAPT}` 和 Logo 策略；不要修改通用模式路由、母版 QA 或生成流程，除非新 IP 真的需要新的通用能力。无品牌角色可直接用 `ip-profiles/none/`。有「要对齐的人」时，把双参考写在 persona/人物层，不要写在简笔主角色层。
