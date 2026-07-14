# Persona Profile: 老杨（Lao Yang）

## 核心定位

**老杨** 是默认 profile 的可触发主讲 persona（作者 `yuezheng2006` 的数字形象），与 **小石头** 组成双 IP 互动系统：

```text
老杨   = 主讲 / 拆解 / 批注 / 调度
小石头 = 执行 Agent（搬卡、贴标签、标风险、物理动作）
```

未触发时不出现老杨；触发后默认「老杨讲、小石头干」，互动场景读 `references/persona-scene-patterns.md`。

## 触发词

`老杨`、`yuezheng2006` 是一等触发词。完整列表：

- 老杨 / 作者 / yuezheng2006
- 我本人 / 我的数字形象
- 让我和小石头一起 / 老杨和小石头 / 老杨 IP 图解
- 作者出镜 / 老杨出镜

示例：`老杨：这篇内容想配图，请先推荐。` / `老杨和小石头：出一张白板图。`

## 分层文件（按需读取）

| 文件 | 负责什么 | 何时读 |
| --- | --- | --- |
| [persona-author-identity.md](persona-author-identity.md) | 识别锚点、表情预设 E0–E4、多场景锁、小比例线 | 生图前、返修「不像老杨」、QA 识别度 |
| [persona-author-assets.md](persona-author-assets.md) | 全景双风格、face-lock、配件层、预览门禁、传图 | 每次 persona 出镜必读 |
| [persona-author-modes.md](persona-author-modes.md) | 各模式画面职责、双 IP 权重、与小石头协作结构 | 锁定模式后 |
| [persona-author-prompts.md](persona-author-prompts.md) | 可复制提示词片段（双 IP / 小比例 / 返修 / 手绘） | 构造生图 prompt 时 |

不要一次读完四层；按上表按需加载。Agent 触发 persona 时的最小读取集：

```text
persona-author.md（本文件，确认触发与分工）
  → persona-author-assets.md（资产组合）
  → persona-scene-patterns.md（互动场景类型）
  → persona-author-modes.md（当前模式权重）
  → persona-author-prompts.md（写入 prompt）
  → persona-author-identity.md（QA 或返修时再读）
```

## 核心固定资产（摘要）

路径均在 `assets/persona/`：

| # | 文件 | 职责 |
| --- | --- | --- |
| 01 | `author-persona-panorama.png` | 真人实体全身身份（实物/长卷必传） |
| 02 | `author-persona-panorama-handdrawn.png` | 手绘全身身份（手绘系必传，更关键） |
| 03 | `author-persona-face-lock.png` | 多角度面相锁定（**多场景同批必加**；宽脸） |
| 03b | `author-persona-handdrawn-body.png` | 手绘全身比例金样（头肩腿协调） |
| 03c | `author-persona-flat-ip-sheet.png` | 复古扁平立体设定图金样（米色 · 用户认定满意） |
| 03d | `author-persona-flat-ip-sheet-navy.png` | 同脸 navy T 变体 |
| 04 | `author-persona-spec.png` | 面相规范补强 |
| 05 | `author-persona-actions.png` | 实物小比例/复杂姿态 |
| 06 | `author-persona-handdrawn.png` | 旧手绘动作参考（全景优先） |

传图组合与多场景一致性锁见 [persona-author-assets.md](persona-author-assets.md)。

## 双 IP 硬性底线

- 触发后每张图必须有老杨与小石头的**明确互动**，不能只有肖像或站桩。
- 小石头永远 flat 2D（`#f39800`），不能因为老杨是 3D 就被带成 3D 公仔。
- 不要照片级真人、证件照、个人品牌海报；不要发明单位、联系方式、履历或背书。

完整禁止项见 [persona-author-identity.md](persona-author-identity.md) 与 [persona-author-modes.md](persona-author-modes.md)。

## 英文称呼

`老杨（作者 yuezheng2006；英文语境可用 Lao Yang）`。公开仓库只用风格化资产，不含真人照片。
