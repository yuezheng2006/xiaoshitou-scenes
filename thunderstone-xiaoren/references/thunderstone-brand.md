# Thunderstone 品牌语境（消歧）

生成配图时默认对齐的业务语境，**避免**与 Thunderstone Quest 桌游、雷石投资私募等同名视觉混淆。本节为 Skill 写作参考，**不代表**公司官方口径。
- **中文常用名**：雷石
- **英文常用名**：Thunderstone
- **默认业务语境**：KTV / 音乐娱乐科技（公开站点 [thunder.com.cn](http://www.thunder.com.cn/home) 可作背景参考）
- **不要混用**：Thunderstone Quest 桌游、雷石投资私募视觉

## 小石头（默认）

```text
小石头 (Little Stone) — #f39200 胶囊体 + flat 2D 简笔 + 物理动作
角色锚点：thunderstone-xiaoren-ref.png（唯一）
```

| 参考文件（Skill 包 `assets/brand/`） | 用途 |
| --- | --- |
| `thunderstone-xiaoren-ref.png` | **小石头角色锚点** |
| `thunderstone-logo-core.png` | **雷石 Logo 唯一标准源**（见下节） |
| `thunderstone-exhibition-brand-ref.png` | 展会品牌气质（背景/物料） |
| `thunderstone-logo-eye-ref.png` | Logo 眼型局部（**不用于**小石头五官） |
| `thunderstone-logo.png` | 橙底完整 Logo 变体 |

工牌：仅办公/权限/值班场景，叙事道具，非品牌胸标。工牌若出现 Logo，**必须**来自 `thunderstone-logo-core.png`；牌面「**雷石**」二字 **与 Logo 同色 `#f39200`**，禁止一字橙一字黑。

## 雷石 Logo 硬性规范（CRITICAL）

画面中凡出现 **Thunderstone / 雷石官方标识**（工牌、物料、展板、挂绳牌等），**禁止发挥、禁止重画、禁止近似替代**。

### 唯一标准源

```text
assets/brand/thunderstone-logo-core.png
```

生图前 **必须 Read** 该文件；生成后 **必须** 与标准源比对几何与比例。

### 允许 / 禁止

| 允许 | 禁止 |
| --- | --- |
| 工牌牌面 Logo +「雷石」二字（**同色 `#f39200`**） | 自画「漩涡眼」「螺旋 Logo」「简化版 Logo」 |
| 将 `logo-core` **原样**缩放到工牌 / 物料上 | 改瞳孔大小、改双弧角度、改宽高比 |
| 仅缩放、仅改变承载背景（白底工牌等） | Logo 与「雷石」**异色**（如橙 Logo + 黑字） |
| 场景叙事短标签（如「工区」「刷卡」） | 用 `thunderstone-logo.png` 橙底整图贴到工牌小区域 |
| | **小石头身上/旁** 用「雷石」等文字箭头引导标记 |
| | 把 Logo 眼型 **套到小石头脸上** |

### 标准几何（对照 logo-core 核验）

Logo 为 **三层结构（自内向外）**，须与 `thunderstone-logo-core.png` 一致：

```text
① 瞳孔 — 眼型正中的正圆透明孔（knockout，透出承载面颜色；白底 = 白圆，黑底 = 黑圆）
② 眼型 — 水平杏仁形「眼睛」实体（#f39200 实心，是 Logo 的中央图形，不是随意圆点）
③ 外轨 — 上下两条对称粗弧带，环绕眼型并向左右收尖（轨道/漩涡框）
```

- 整体 **横向** flat 矢量；单色 **#f39200** + 透明瞳孔。
- **不是** 单一螺旋圆、**不是** 只有圆点、**不是** 实心黑点瞳孔。
- 白底工牌：② 为橙色眼型，① 为 **白色透明圆孔**（禁止填黑/填橙）。
- 整体宽高比、眼型比例、弧带粗细 **与 logo-core 一致**，不可「灵感再设计」。

### QA 对照清单（Logo 专项）

- [ ] 中央能辨认 **眼睛形状**（水平杏仁），不只是圆环或漩涡
- [ ] 眼睛 **中心** 是透明圆孔，不是实心色块
- [ ] 外轨双弧对称、收尖方向与 logo-core 一致
- [ ] 工牌「雷石」与 Logo **同色 `#f39200`**

### 生图执行

1. 场景需 Logo → Read `thunderstone-logo-core.png`。
2. Prompt 写明三层结构：眼型（橙）+ 瞳孔（透明）+ 外轨（双弧）。
3. QA 失败信号：缺少中央 **眼型**、瞳孔非透明、外轨不对称、像 generic icon；**圆心误填实心黑点/橙点**。

### 精确交付（推荐）

AI 手绘 Logo 易错时，**优先合成**而非重画：

1. 生图时工牌牌面 **留空 Logo 区**（或生成后裁掉错误 Logo）。
2. 将 `thunderstone-logo-core.png` 去黑底（黑/近黑 → 透明）后 **原比例缩放** 贴到牌面。
3. 白底工牌上：眼型为橙，瞳孔区透出 **白色**；与 logo-core 像素一致。

## 同批一致性

2 张及以上：全批同一 **小石头** + flat 2D；动作与标签可不同。

## 写作口径

- 短标签用真实话术；不写经营原则。
- 不继承母版里他人经历或第三方品牌名。
