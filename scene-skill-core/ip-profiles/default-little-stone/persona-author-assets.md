# 老杨 · 三份固定资产与传图规则

## 资产清单

| # | 文件 | 负责什么 | 何时传给生图 |
| --- | --- | --- | --- |
| 01 规范说明图 | `author-persona-spec.png` | 身份锚点 +「必须保留 / 禁止偏移」纠偏区 | 实物图必传；手绘系必读作身份来源 |
| 02 动作扩展图 | `author-persona-actions.png` | 复杂姿态、小比例远景、与小石头 3D 协作分区 | 实物图 · 小比例或复杂动作时加传 |
| 03 手绘参考图 | `author-persona-handdrawn.png` | 扁平线稿渲染语言、协作版式 | 手绘 / 知识卡 / PPT 触发老杨时与 spec 同读 |

三份分工不同，**不要一次全塞**；按下方规则选组合。

## 双渲染语言（不能混用）

| 模式 | 老杨渲染 | 使用资产 |
| --- | --- | --- |
| 实物图、彩蛋长卷 | 轻 Q 3D 数字玩偶 | spec；必要时 + actions |
| 手绘图 | 扁平黑线人物 | spec + handdrawn |
| 知识卡、PPT | 同手绘图 | spec + handdrawn |

不要把 3D 玩偶塞进手绘模式，也不要把手绘线稿用在实物模式。与小石头同框时，**必须**加读 `assets/character/primary-character-reference.png`。

## 引用优先级

实物图：

```text
author-persona-spec.png > author-persona-actions.png > 临时生成图
```

手绘系（手绘 / 知识卡 / PPT）：

```text
author-persona-spec.png（身份）> author-persona-handdrawn.png（渲染）> 临时生成图
```

手绘系**不加读** actions，避免 3D 分区带乱线稿版式。

## 传图决策表

| 场景 | 读取资产 |
| --- | --- |
| 实物图 · 普通互动 | spec |
| 实物图 · 小比例 / 复杂多姿态 / 长卷远景节点 | spec + actions |
| 实物图 · 返修不像老杨 | spec（对照必须保留 / 禁止偏移区） |
| 手绘 / 知识卡 / PPT · 任何老杨出镜 | spec + handdrawn |
| 小石头同框 | + primary-character-reference.png |
| 资产缺失（fork 丢 PNG） | 退回 persona-author-identity.md 文字锚点；交付标注资产缺失 |

## 与小石头渲染隔离

生成 `author-persona-actions.png` 等同框资产时，小石头部分必须沿用 flat 2D 设定（`#f39800` 平涂、细线、白圆眼），不得临时发明 3D 小石头或灰石头。

## 隐私与开源边界

- 公开仓库只分发**风格化** PNG，不含真人照片或照片级反例。
- 识别度靠风格化资产 + `persona-author-identity.md` 文字锚点维持。
- fork 者替换 persona 时，应替换本目录三份 PNG 并同步改 identity 文档中的文字锚点。
