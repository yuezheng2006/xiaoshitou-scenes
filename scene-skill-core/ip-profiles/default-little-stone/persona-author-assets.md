# 老杨 · 固定资产与传图规则

## 资产清单

| # | 文件 | 负责什么 | 何时传给生图 |
| --- | --- | --- | --- |
| 00 会话临时 1:1 肖像 | 用户当前会话临时参考 | 重建资产时的面相最高优先级 | 仅重建资产；不落仓 |
| 01 真人实体全景 | `author-persona-panorama.png` | **真人实体风格**全身身份：正侧背、表情、动态、休闲穿搭、金黄金渐层猫 | 实物图 / 长卷出镜**必传** |
| 02 手绘全景 | `author-persona-panorama-handdrawn.png` | **手绘风格**全身身份（与①同一人）；线稿/轻色块全景 | 手绘 / 知识卡 / PPT 出镜**必传**（一致性更关键） |
| 03 面相锁定表 | `author-persona-face-lock.png` | **多角度脸特写**（正面/3/4/讲解），压跨场景脸漂 | **多场景同批必加传**；单张脸占比大或不稳时加传 |
| 03b 手绘身材比例 | `author-persona-handdrawn-body.png` | **手绘全身比例金样**（头肩协调、腿长自然；用户认定契合） | 手绘系全身出镜**建议加传**；比例跑偏返修**必传** |
| 04 面相规范图 | `author-persona-spec.png` | 面相特写与禁止偏移区（历史补强） | 仍可加传；优先用③面相锁定表 |
| 05 动作扩展 | `author-persona-actions.png` | 实物小比例/复杂姿态 | 实物需要时加传 |
| 06 旧手绘参考 | `author-persona-handdrawn.png` | 历史线稿动作参考 | 可作补充；**手绘全景②优先** |

> **一致性原则：**  
> - 真人实体出图 → 跟 `author-persona-panorama.png`  
> - 手绘出图 → 跟 `author-persona-panorama-handdrawn.png`（**更重要**）  
> - 手绘全身比例 → 跟 `author-persona-handdrawn-body.png`（头不大、腿不短）  
> - 两张全景必须是**同一个人**；禁止串成泛化讲师脸  
> - **多场景同批** → 全景（按模式）+ `author-persona-face-lock.png`，跨图差异要小  
> - 面相必须是**中国北方/山东男性脸**，禁止韩范偶像脸（见 `persona-author-identity.md` 面相族裔锁）

## 双风格对齐协议（强制）

### 实物图 / 长卷（真人实体）

1. **必传** `author-persona-panorama.png`
2. 多场景同批或脸特写不稳：**加传** `author-persona-face-lock.png`（可再加 spec）
3. 小比例/复杂姿态 **加传** `author-persona-actions.png`

### 手绘 / 知识卡 / PPT（手绘风格 · 优先加强）

1. **必传** `author-persona-panorama-handdrawn.png`（手绘全身身份）
2. **必传** `author-persona-panorama.png`（真人实体锚点，锁「同一个人」）
3. **全身出镜建议加** `author-persona-handdrawn-body.png`（锁身材比例；比例跑偏返修必加）
4. **多场景同批必加** `author-persona-face-lock.png`；单张脸漂也可加
5. 可选加 `author-persona-handdrawn.png` / `author-persona-spec.png` 作表情或面相补强

硬门禁：对应风格的全景未进上下文，不得声称已锁定老杨。多场景未加 face-lock 且跨图差异大 → 整批返修。全身头大短腿 → 对照 handdrawn-body 返修。

## 金渐层猫

- **金黄色 / 暖金杏色**被毛的金渐层英短（非灰虎斑、非银渐层）
- 绿或黄绿眼，圆脸英短
- 锚点：两张全景蹲姿摸猫区
- 默认正文不强制带猫；点名「猫 / 金渐层」或生活彩蛋时再出

## 穿搭（全景锁定 · 同批不可变）

米色短袖棉 T + **橄榄卡其短裤** + 米白帆布鞋。  
与两张全景一致；**同批多场景禁止换装**（含禁止漂成深灰运动裤），除非用户明确要求工装/运动场景。

## 多场景传图（人物一致性加强）

一次出 2 张及以上 / 跨多场景时：

1. **同批固定同一套参考**：不要中途换全景版本
2. 实物多场景：每张都传 `author-persona-panorama.png` + `author-persona-face-lock.png`
3. 手绘多场景：每张都传 **手绘全景 + 实体全景 + face-lock**
4. Prompt 复用同一段 Feature Stability Lock；显式写 `same exact person, minimal face variation across scenes`
5. 交付前做跨图并排快检：不像同一人 → 整批返修

## 与小石头

同框另加 `primary-character-reference.png`（单锚点）。小石头不占老杨锚点名额。

## 传图决策表

| 场景 | 传图 |
| --- | --- |
| 实物 · 普通 | panorama（实体） |
| 实物 · 脸不稳 / 返修 | panorama + face-lock（± spec） |
| 实物 · 小比例复杂姿态 | panorama + actions（± face-lock） |
| 实物 · **多场景同批** | 每张 panorama + **face-lock** |
| 手绘 / 知识卡 / PPT | **panorama-handdrawn + panorama**（双风格锁同一人） |
| 手绘 · **全身比例** | 上表 + **handdrawn-body**（头肩腿比例金样） |
| 手绘 · **多场景同批** | 每张双全景 + **face-lock**（± handdrawn-body） |
| 要猫 | 对应风格全景（金黄金渐层） |
| 小石头同框 | + primary-character-reference.png |
| 格子过小 | 抽象符号，不画 generic 脸 |

## 失败信号

- 韩范脸：小脸、V下巴、冷白皮、爱豆五官
- 手绘出图却只传实体全景、未传手绘全景
- 实体/手绘两套脸不像同一个人
- **多场景并排放：眼镜/发际/下颌/唇厚漂移到像换人**
- **手绘全身头过大、短腿、躯干过长**（未对齐 handdrawn-body）
- **同批一张短裤一张运动裤 / 一张幼态一张叔感**
- 猫是灰虎斑或不够金黄
- 粗黑框、幼态、过叔、泛化商务男

## 隐私

公开仓只留风格化 PNG；1:1 肖像不落仓。fork 时同步替换两张全景与其余 persona 资产。
