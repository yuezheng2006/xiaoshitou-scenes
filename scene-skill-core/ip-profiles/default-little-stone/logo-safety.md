# Logo 与品牌资产安全规则

本 Skill 默认面向**通用正文配图**，不主动绑定任何特定公司或商标。

公开仓库不随包分发真实品牌 Logo 源文件。若用户明确要求工牌、展会、物料或公司内部场景中的真实 Logo，必须由用户在本地私有资产区自行提供，并自行确认授权。默认情况下，正文、示例和生成图里**都不出现真实品牌 Logo**。

小石头可以带一点数字娱乐 / KTV / 门店经营的道具气味，但这只是可选语境，不等于自动出现真实公司名、Logo 或商标。

**雷石员工（AI native）**：见 `character.md`「雷石员工」——工牌**仅**在此语境出现。  
**KTV 巡检 / 房态 / 场所服务**：**非本 profile 场景**；默认不生成，且**不带任何工牌**。

内部 VI、Logo 源文件、PPT 模板和品牌规范文档只作为用户本地私有参考。公开 README、examples、profile 文档和生成提示词不得引用这些私有链接、文件名或品牌规范细节。

## 硬性规则

- **小石头身上**：禁止 Logo、品牌名、商标符号或「某某公司」引导标签。
- **背景气味表达**：可用任务卡、权限牌、抽象控制台等**系统侧**中性道具；**不要**默认房态牌、包厢巡检、挂绳工牌。
- **场景道具**：默认不出现真实品牌 Logo；只有用户**明确要求** Logo / 员工工牌 / 戴工牌 / 雷石 / 展会物料时，才把 Logo 放在工牌、展板、物料、贴纸等道具上。
- **使用方式**：品牌 Logo 必须来自用户本地私有参考图，不要凭空重画、近似替代或改造几何；公开核心包不提供真实 Logo 源文件。
- **内部资料**：VI 手册、Logo 压缩包、AI 源文件、PPT 模板、字体包等不进入公开仓库；若需要参考，只能在本地私有目录使用，并避免把原始文件名、下载链接或品牌规范内容写进公开文档。
- **公开示例**：默认示例、试跑样张和文档**不展示具体品牌 Logo**；需要时由用户在自己的生成请求里显式说明，并自行确认授权。
- **禁止**在公开示例中复刻任何第三方官方标识几何。

## 参考图

| 文件 | 用途 |
| --- | --- |
| `primary-character-reference.png` | 小石头角色锚点，不是 Logo |
| `primary-character-actions.png` | 小石头动作/小比例参考，不是 Logo |

## 品牌 Logo 使用约束

- Logo 可出现在工牌、挂绳牌、展板、物料、背景贴纸等**场景道具**上。
- Logo 不得直接印在小石头身体、眼睛、帽子或皮肤上；用户说“戴工牌”时，小石头可以佩戴**独立挂绳工牌**，Logo 只出现在工牌牌面。
- “戴工牌”默认指 **小石头戴品牌工牌**；“人物戴工牌 / 老杨戴工牌”只有在用户明确这样说时才触发人物佩戴。
- 若画面出现品牌文字，应作为道具上的品牌文字，不要用箭头指向小石头解释身份。
- 用户没有明确触发 Logo / 工牌 / 展会 / 品牌物料时，生成图里不要自动加入任何品牌 Logo。

## 员工工牌系列

> 小石头 **IP + 雷石员工**：`character.md`「雷石员工」。

当用户明确要求 **雷石员工工牌 / 戴工牌 / 雷石 / AI native 员工** 时，使用下文 **雷石工牌规格**。  
**KTV 巡检 / 房态 / 包厢服务** 不是我们的场景——默认不生成；若出现也 **不带任何工牌**。

### 雷石工牌规格（比例 · Logo 区 · 挂绳）

对照用户本地工牌参考（会话传入，**不落公开库**）。**默认只用品牌卡（Logo only）**：

**品牌卡 · Logo only（默认 · 唯一推荐形态）**

| 项 | 规格 |
| --- | --- |
| 比例 | **竖版长方形 3:5（宽:高）**——竖长、比 9:16 略宽；佩戴时牌面宽度约 **小石头体宽的 25–32%**，**必须小于头宽/眼距** |
| 牌面 | **雷石橙 `#f39800` 同系饱和橙** 哑光塑料感；圆角矩形；**无照片、无姓名、无岗位、无部门** |
| **Logo** | 牌面内 **居中、可读、突出**——字标占**牌面**可视区约 50–70%（不是把工牌本身放大）；**默认带字标**（眼形 swirl + **THUNDERSTONE** 全大写） |
| 挂绳 | **白色扁带**；橙色重复 THUNDERSTONE + 眼形图标；白色方扣 |

**牌面禁止出现**：真实/虚构**姓名**、**岗位**、**部门**、工号、二维码、照片区文字、`接工单` / `跑链路` / `回传` / `AI native` 等流程或场景文案。工牌**只承载公司 Logo**。

**Logo 1:1 还原（强制 · 禁止模型发挥）**

雷石 Logo（眼形 swirl 图标；字标场景用 **THUNDERSTONE**）**不得**手绘、近似或改形。

**生图方式：prompt + 参考图**（不做 Python / ImageMagick 后处理贴图）

| 步骤 | 要求 |
| --- | --- |
| 1 · 传参 | **工牌牌面必传** `assets/brand-private/thunderstone-logo-with-wordmark.png`（图标 + THUNDERSTONE 字标）；仅纯图标场景才用 `thunderstone-logo-mark.png` |
| 2 · prompt | 写清工牌规格 + **reproduce attached logo-with-wordmark reference 1:1 on badge face, no redraw, no stylize** |
| 3 · 禁止 | prompt 里不要写「画 swirl / 画 THUNDERSTONE 字体」——只引用参考图几何与字标 |
| 4 · 返修 | Logo 走形 → 加强参考图权重、缩小工牌占比、重生成；**不要**走脚本合成 |

**授权 Logo 源（profile 内）**

路径根：`scene-skill-core/ip-profiles/default-little-stone/assets/brand-private/`

| 文件 | 用途 |
| --- | --- |
| `thunderstone-logo-with-wordmark.png` | **工牌牌面默认** · 眼形 swirl 图标 + THUNDERSTONE 字标 |
| `thunderstone-logo-mark.png` | 纯图标（挂绳重复 icon、小尺寸牌面等） |

**禁止**：模型自画 Logo、改 swirl 曲线、换字体、加瞳孔/螺旋眼、异色 Logo、近似替代。

**佩戴方式**

- 独立挂绳卡悬于颈前；**小尺寸**、细白带；卡面略倾斜可读；**禁止**工牌贴在小石头橙身上、**禁止工牌 ≥ 头宽**。
- 小石头仍是 flat 2D 执行者；工牌是道具，不是第二身体。
- **牌面禁止承载流程/场景/人事文案**：姓名、岗位、部门、工号、流程标签等**一律不得**上工牌；工牌**只体现公司 Logo**，且 Logo **居中、大、突出**。

**Prompt 可复制**

```text
Attach reference: assets/brand-private/thunderstone-logo-with-wordmark.png (required — icon + THUNDERSTONE wordmark on badge face).
Thunderstone employee badge: separate SMALL lanyard ID card, **portrait rectangle 3:5 (width:height)** — taller than wide, NOT square, NOT ultra-narrow 9:16; card width ~25-32% of body, smaller than head.
Reproduce attached logo-with-wordmark on orange badge face 1:1 — eye-swirl icon + THUNDERSTONE text exactly as reference. NO redraw, NO stylize, NO approximate geometry.
Logo-only orange card: NO photo, NO name, NO job title, NO department, NO workflow text on badge face.
White lanyard optional. Logo NEVER on orange capsule body.
Little Stone = AI-native employee context, NOT KTV venue service.
```

## 禁止

- 把 Logo 直接印在小石头身体上，或把工牌画成身体纹身 / 胸口印花。
- 工牌比例失真（**非 3:5 竖长形**、过窄如 9:16、接近正方形、大于头宽、占满胸口）。
- 雷石员工 + KTV 巡检 / 房态 / 包厢递麦。
- **KTV 巡检类画面 + 任何工牌**（雷石或中性均不要）。
- 用户只说「戴工牌」时，让老杨或其他人物戴工牌、小石头不戴。
- 生成真实姓名、手机号、工号、二维码、部门架构或未经提供的履历信息。
- **让生图模型手绘/改形雷石 Logo**（必须 1:1 贴授权资产；不能发挥）。
- **工牌牌面写姓名/岗位/流程文案**；工牌 Logo 须**居中、大、突出**。
- Logo 占满**整张插图**成为画面主角（工牌牌面上的 Logo 可以且应当**大、居中、突出**）。
