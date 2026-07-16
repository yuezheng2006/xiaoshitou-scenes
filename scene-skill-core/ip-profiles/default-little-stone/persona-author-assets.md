# 老杨 · 固定资产与传图规则

所有老杨人像生成先执行 `../../references/common-persona-calibration.md`。资产传入不等于校准通过；必须完成校准卡并在生成后复核身份、年龄、比例和配件。

## 三档分工（Agent 速查）

| 档位 | 职责 | 核心文件 |
| --- | --- | --- |
| **01 主锚** | 像谁 · 日常生图默认传 | 实体 `panorama` / 手绘 `panorama-handdrawn` |
| **02 规范 / 纠偏** | 别跑偏 · 多场景 / 返修 / QA | `face-lock`、flat-ip-sheet 对、返修时 `spec` |
| **03 动作扩展** | 会动 · 小比例 / 复杂姿态 / 全身比例 | `actions`、`handdrawn-body` |

**日常生图**：01 主锚（按模式）即可。  
**多场景同批 / 脸漂 / 返修**：01 + 02。  
**小比例 / 复杂姿态 / 全身比例跑偏**：01 + 02 + 03。

## 引用优先级链（冲突时从高到低 · 精简版）

```text
手绘全景 handdrawn-panorama
  > 实体全景 panorama
  > face-lock（面相锁定 + 禁止偏移区）
  > handdrawn-body（全身比例）
  > actions（小比例 / 复杂姿态）
  > 会话临时 1:1 肖像（仅重建资产，不落仓）
```

返修「不像老杨」时：**必对照 face-lock 禁止偏移区**，文字细节见 `persona-author-identity.md`。

## 双 IP 同框 · 最小传图

触发老杨 + 小石头同框时：

1. **老杨**：按模式传 01 主锚（手绘系 = 手绘全景 + 实体全景；多场景 + face-lock）
2. **小石头**：`primary-character-reference.png`（**单锚点，不占老杨名额**）
3. **条件加传**：小比例老杨 → `actions`；复杂姿态小石头 → `primary-character-actions.png`；手绘全身 → `handdrawn-body`

完整决策见下文「传图决策表」。

## 资产清单（精简版 · 2026-07-16）

| # | 文件 | 负责什么 | 何时传给生图 |
| --- | --- | --- | --- |
| 01 真人实体全景 | `author-persona-panorama.png` | **真人实体风格**全身身份：正侧背、表情、动态、休闲穿搭、金黄金渐层猫 | 实物图 / 长卷出镜**必传** |
| 02 手绘全景 | `author-persona-panorama-handdrawn.png` | **手绘风格**全身身份（与①同一人）；线稿/轻色块全景 | 手绘 / 知识卡 / PPT 出镜**必传**（一致性更关键） |
| 03 面相锁定 | `author-persona-face-lock.png` | **多角度脸特写 + 禁止偏移区**（正面/3/4/讲解），压跨场景脸漂；**明显偏宽方圆脸** | **多场景同批必加传**；单张脸占比大或不稳、返修时加传 |
| 04 手绘身材比例 | `author-persona-handdrawn-body.png` | **手绘全身比例金样**（183cm · **上短下长 4:6**；头肩协调） | 手绘系全身出镜**建议加传**；比例跑偏返修**必传** |
| 05 动作扩展 | `author-persona-actions.png` | 实物小比例/复杂姿态 | 实物需要时加传 |
| **临时引用** | 会话临时 1:1 肖像 | 重建资产时的面相最高优先级 | 仅重建资产；不落仓 |
| **批内金样** | `assets/persona/examples/validated-batch-anchor-handdrawn.png` | **用户验收 likeness 锚** | 多场景同批、预览通过后**加传**；见 `examples/local-validation-dual-ip.md` |

**废弃资产**（保留文件但文档不再引用）：
- ~~`author-persona-spec.png`~~ → 功能已合并到 `face-lock.png`
- ~~`author-persona-handdrawn.png`~~ → 历史遗留，已被 `panorama-handdrawn.png` 替代
- ~~`author-persona-flat-ip-sheet.png` + `navy`~~ → 移至 `examples/` 作为可选校准参考

> **一致性原则：**  
> - 真人实体出图 → 跟 `author-persona-panorama.png`  
> - 手绘出图 → 跟 `author-persona-panorama-handdrawn.png`（**更重要**）  
> - 手绘全身比例 → 跟 `author-persona-handdrawn-body.png`（头不大、腿不短）  
> - 两张全景必须是**同一个人**；禁止串成泛化讲师脸  
> - **多场景同批** → 全景（按模式）+ `author-persona-face-lock.png`，跨图差异要小  
> - **最高相似度金样** → `author-persona-flat-ip-sheet.png` + `author-persona-flat-ip-sheet-navy.png` 成对对照；优先锁脸、颧骨、年龄档、眼镜、发型、嘴唇和体型，不把藏蓝色当作默认服装
> - 面相必须是**中国北方/山东男性脸**，禁止韩范偶像脸（见 `persona-author-identity.md` 面相族裔锁）

## 双风格对齐协议（强制）

### 实物图 / 长卷（真人实体）

1. **必传** `author-persona-panorama.png`
2. 多场景同批或脸特写不稳：**加传** `author-persona-face-lock.png`
3. 小比例/复杂姿态 **加传** `author-persona-actions.png`

### 手绘 / 知识卡 / PPT（手绘风格 · 优先加强）

1. **必传** `author-persona-panorama-handdrawn.png`（手绘全身身份）
2. **必传** `author-persona-panorama.png`（真人实体锚点，锁「同一个人」）
3. **全身出镜建议加** `author-persona-handdrawn-body.png`（锁身材比例；比例跑偏返修必加）
4. **多场景同批必加** `author-persona-face-lock.png`；单张脸漂也可加

硬门禁：对应风格的全景未进上下文，不得声称已锁定老杨。多场景未加 face-lock 且跨图差异大 → 整批返修。全身头大短腿 → 对照 handdrawn-body 返修。

## 金渐层猫

- **金黄色 / 暖金杏色**被毛的金渐层英短（非灰虎斑、非银渐层）
- 绿或黄绿眼，圆脸英短
- 锚点：两张全景蹲姿摸猫区
- 默认正文不强制带猫；点名「猫 / 金渐层」或生活彩蛋时再出

## 穿搭与配件层（CRITICAL · 场景必带）

分两层写进每张 prompt，**表情/场景变化时配件层不得省略**：

| 层 | 字段 | 锁定内容 |
| --- | --- | --- |
| **服装** | top / bottom / shoes | 米色短袖棉 T / 橄榄卡其短裤 / 米白帆布鞋 |
| **配件 · face** | glasses | 大镜片浅灰/透明细框方框（第一识别件） |
| **配件 · head** | hair | 短直发 3–5cm、接近平直发际 |
| **配件 · 禁止** | — | 粗黑框、帽子（默认无）、手表腕饰 |

Prompt 可复制片段：
```text
Outfit Layer: beige cotton T + olive khaki shorts + off-white canvas sneakers.
Accessory Layer (MUST keep across scenes/expressions): large thin light-gray rectangular glasses on face; short straight 3-5cm black hair, near-flat hairline. Do NOT drop or redesign glasses/hair when changing pose or expression.
```

与两张全景一致；**同批多场景禁止换装**（含禁止漂成深灰运动裤），除非用户明确要求工装/运动场景。

## 多场景传图（人物一致性加强）

一次出 2 张及以上 / 跨多场景时：

1. **预览门禁（强制）**：先只生成 **1 张预览**（目标模式 + 最代表场景）；过 P1/P3/P6（手绘全身加比例）与配件层可见性后，才允许批跑其余场景
2. **同批固定同一套参考**：不要中途换全景版本
3. 实物多场景：每张都传 `author-persona-panorama.png` + `author-persona-face-lock.png`
4. 手绘多场景：每张都传 **手绘全景 + 实体全景 + face-lock**（全身再加 handdrawn-body）
5. Prompt 复用同一段 Feature Stability Lock + **Outfit/Accessory Layer**；显式写 `same exact person, minimal face variation`
6. 交付前做跨图并排快检：不像同一人 → **只返修 FAIL 张**（合格样保留），禁止为修一张而整批重跑；若预览都 FAIL → 整批不得开跑

### 批内金样锚定（多场景 likeness）

预览图 likeness 验收通过后，同批后续场景优先引用金样 + face-lock：

```text
Batch likeness anchor: attach user-approved scene image from same style batch as PRIMARY likeness reference.
Keep Lao Yang IDENTICAL: mid-face trio (thick brows + high cheekbones + full lips) + wide face + 4:6 body + thin light-gray glasses.
Also keep: handdrawn-panorama + panorama + face-lock + handdrawn-body (if full body).
Do NOT fix likeness by thinning brows, flattening cheekbones, or thinning lips.
```

金样文件：`assets/persona/examples/validated-batch-anchor-handdrawn.png` · 验收索引 [`examples/local-validation-dual-ip.md`](../../../../examples/local-validation-dual-ip.md)

## 与小石头

同框另加 `primary-character-reference.png`（单锚点）。小石头不占老杨锚点名额。

## 传图决策表

| 场景 | 传图 |
| --- | --- |
| 实物 · 普通 | panorama（实体） |
| 实物 · 脸不稳 / 返修 | panorama + face-lock |
| 实物 · 小比例复杂姿态 | panorama + actions（± face-lock） |
| 实物 · **多场景同批** | **先 1 张预览** → 通过后每张 panorama + **face-lock** |
| 手绘 / 知识卡 / PPT | **panorama-handdrawn + panorama**（双风格锁同一人） |
| 手绘 · **全身比例** | 上表 + **handdrawn-body**（头肩腿比例金样） |
| 手绘 · **多场景同批** | **先 1 张预览** → 通过后每张双全景 + **face-lock**（± handdrawn-body） |
| 要猫 | 对应风格全景（金黄金渐层） |
| 小石头同框 | + primary-character-reference.png |
| 格子过小 | 抽象符号，不画 generic 脸 |

## 失败信号

- 韩范脸：小脸、V下巴、冷白皮、爱豆五官
- 手绘出图却只传实体全景、未传手绘全景
- 实体/手绘两套脸不像同一个人
- **多场景未做预览门禁就整批开跑**
- **多场景并排放：眼镜/发际/下颌/唇厚漂移到像换人**
- **场景变了眼镜/发型消失或换款**（配件层未带入）
- **手绘全身头过大、短腿、躯干过长**（未对齐 handdrawn-body）
- **同批一张短裤一张运动裤 / 一张幼态一张叔感**
- 猫是灰虎斑或不够金黄
- 粗黑框、幼态、过叔、泛化商务男

## 隐私

公开仓只留风格化 PNG；1:1 肖像不落仓。fork 时同步替换两张全景与其余 persona 资产。
