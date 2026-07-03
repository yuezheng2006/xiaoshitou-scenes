# Default IP Profile: Little Stone + 老杨

## 定位

这是 `scene-skill-core` 的默认 IP profile，包含**双 IP 互动系统**：

```text
小石头 = 主角色 / 执行 Agent（flat 2D 胶囊）
老杨   = 可选 persona / 主讲 IP（触发后出现，与小石头互动）
```

未触发老杨时，只使用小石头。触发老杨后，从 `persona-author.md` 进入分层读取链，并读 `references/persona-scene-patterns.md`。

## Profile ID

`default-little-stone`

## 主角色

- 角色文件：`character.md`
- 主锚点：`assets/character/primary-character-reference.png`
- 动作/多人/小比例扩展：`assets/character/primary-character-actions.png`
- 默认触发词：`小石头`、`Little Stone`
- 主要颜色：`#f39800`
- 角色气质：认真、靠谱、略笨、有点倔；默认可带一点全场景音乐科技 / KTV / 软硬件联动 / 门店经营的道具气味，但不作为强人设。

## 可选 Persona（老杨）

分层入口：`persona-author.md`（摘要 + 读取顺序）

| 文件 | 职责 |
| --- | --- |
| `persona-author.md` | 触发词、双 IP 分工、最小读取链 |
| `persona-author-identity.md` | 识别锚点、小比例线、禁止偏移 |
| `persona-author-assets.md` | 三份固定资产、传图规则 |
| `persona-author-modes.md` | 各模式职责与画面权重 |
| `persona-author-prompts.md` | 可复制提示词片段 |

- 互动场景库：`../../references/persona-scene-patterns.md`（触发 persona 时必读）
- 触发词：`老杨`、`作者`、`yuezheng2006`、`我本人`、`我的数字形象`、`让我和小石头一起`、`作者出镜`、`老杨出镜`、`老杨和小石头`、`老杨 IP 图解`
- 触发后：启用双 IP 互动；未触发时不出现老杨。

## Logo 与品牌边界

- Profile Logo 规则：`logo-safety.md`
- 公开包不随 profile 分发真实品牌 Logo 源文件。
- 私有授权 Logo 只放本地 `assets/brand-private/`，该目录必须保持 git ignored。
- `K 歌 / KTV / 音乐科技 / 车载 / 汽车内 / 智能电动 / 家用 / 商用 / 门店经营` 只触发可选物件语境，不自动触发真实 Logo。
- 小石头的背景气味通过中性道具、动作和场景关系表达，不通过真实公司名或商标表达。

## 读取顺序

1. 读取本文件确认当前 profile。
2. 读取 `character.md` 获取主角色形象锁和资产锚点。
3. 若触发 persona：读 `persona-author.md` → `persona-author-assets.md` → `persona-scene-patterns.md`；锁定模式后读 `persona-author-modes.md`；写 prompt 读 `persona-author-prompts.md`；QA/返修读 `persona-author-identity.md`。
4. 若触发 Logo / 工牌 / 展会 / 品牌物料，读取 `logo-safety.md`。
5. 再进入 `references/` 中的通用模式、母版、QA 和提示词模板。

## 替换 IP 的原则

新增 IP 时复制本目录结构为 `ip-profiles/<ip-id>/`，只替换 profile 文件、角色资产、persona 和 Logo 策略；不要修改通用模式路由、母版 QA 或生成流程，除非新 IP 真的需要新的通用能力。
