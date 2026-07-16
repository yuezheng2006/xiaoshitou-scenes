# 老杨 · 校准图与全景资产

> **双参考协议（对齐人）**：设定图 = 01 主锚全景；校准图 = 本目录按主题选 1 张（可选）。  
> **验收索引**：[`examples/local-validation-dual-ip.md`](../../../../../examples/local-validation-dual-ip.md)

## 批内金样（多场景 likeness · 预览验收后）

| 文件 | 用途 |
| --- | --- |
| `validated-batch-anchor-handdrawn.png` | 用户验收 likeness 锚；同批后续场景**优先加传**（+ 主锚 + face-lock） |

## 01 主锚（每次必传 · 按模式）

| 文件 | 风格 | 用途 |
| --- | --- | --- |
| `../author-persona-panorama.png` | 真人实体 | 实物图 / 长卷身份主锚；金黄金渐层猫 |
| `../author-persona-panorama-handdrawn.png` | 手绘 | 手绘 / 知识卡 / PPT 身份主锚（**更重要**）；须与实体全景同一人 |

手绘出图：**手绘全景 + 实体全景** 同传，锁「同一个人」。

## 02 规范 / 纠偏（多场景 · 返修 · QA）

| 文件 | 用途 |
| --- | --- |
| `../author-persona-face-lock.png` | 多角度脸特写；**多场景同批必加** |
| `../author-persona-flat-ip-sheet.png` + `../author-persona-flat-ip-sheet-navy.png` | 最高相似度金样对（同脸同身材；藏蓝仅换色） |
| `../author-persona-face-lock.png` | 面相锁定（多角度） + **禁止偏移区**；**返修不像老杨时必对照** |

## 03 动作扩展（条件）

| 文件 | 用途 |
| --- | --- |
| `../author-persona-handdrawn-body.png` | 手绘全身比例金样（183cm · 4:6 上短下长） |
| `../author-persona-actions.png` | 实物小比例 / 复杂姿态 |
| `../author-persona-handdrawn.png` | 历史线稿动作（全景优先） |

## 按主题选校准图（身份漂移或质量不稳时 · 可选 1 张）

| 选用时机 | 文件 |
| --- | --- |
| 手绘多场景 / 脸漂 / 知识卡主讲 | `handdrawn/calibrate-persona-scene.png` |
| 实物小比例 / 复杂姿态 / 物件现场 | `physical/calibrate-persona-scene.png` |
| 宽脸 / 韩范 / 年龄漂移 | 不加校准图 → 改加 **face-lock + flat-ip-sheet 对** |
| 全身比例跑偏 | 加 **handdrawn-body**（非本目录） |

**分工**：主锚全景管身份；face-lock / flat-ip-sheet 管别跑偏；本目录 calibrate 管「该画风里仍像同一人」。禁止只传 calibrate 不传主锚。

## 小比例返修三件套

老杨占画面约 15–20% 或更小时：

1. 模式对应 **01 主锚**（实体或双全景）
2. `author-persona-actions.png`
3. `author-persona-face-lock.png`（多场景或仍不稳时）

走形修复索引见 `persona-author-prompts.md` 末尾。

`2026-07-15`
