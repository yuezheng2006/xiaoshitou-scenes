# Character Profile: Little Stone

## 核心定位

**小石头** 是默认主角色：一个以认真、靠谱、略笨、有点倔为核心气质的 flat 2D 简笔 IP，靠物理动作、短标签和大留白讲故事。

```text
形体：圆角胶囊 / 竖椭圆，#f39800 橙实心体
眼睛：白色小圆 + 可选 tiny 瞳孔；无嘴、无牙、无唇线
肢体：细黑线；每体 2 臂 2 腿；臂从体侧上 1/3 伸出，腿从底缘向下
身上：禁止任何 Logo / 品牌名 / 商标印花
气质：认真、靠谱、略笨、有点倔；不讲大道理，只把问题一步步落地
```

## 性格与品质

小石头不是抽象 mascot，也不是品牌代言人。它的识别主要来自性格和动作：

- **认真**：遇到问题先上手，不站在旁边解释。
- **靠谱**：每次都承担一个明确动作，例如拉、挡、推、接、贴、改、查、递、守。
- **略笨**：可以有一点费劲、汗滴、卡住或被任务卡拖住的尴尬感，但不卖萌。
- **有点倔**：面对混乱流程、错误标签或过载信息时，会顶住、拉回、拦下、修好。
- **有服务意识**：关心事情能不能顺利跑起来，但不需要被画成客服、员工或品牌代言人。

## 背景气味

默认 profile 可以带一点全场景音乐科技 / KTV / 门店经营的道具气味，但这只是可选语境，不是强人设：

- 可用：麦克风、点歌单、房态卡、设备巡检单、权限牌、会员反馈卡、经营看板、曲库更新卡。
- 可转译：车载、汽车内、主流智能电动车座舱、商用、家用、轻量休闲娱乐、软硬件联动、曲库更新、设备巡检、会员反馈、服务响应等场景。
- 也可完全不用这些道具，回到更通用的轻薄项目卡、权限卡、消息卡、任务队列卡、协作看板卡、状态贴、标签条、轻量连接线、透明资料托等正文配图物件。
- 道具默认要现代、轻、干净：优先无线/便携设备、圆角卡片、哑光材质、简洁夹扣、轻量标签和小型收纳件。
- 道具只服务当前内容的隐喻，不要为了强调背景而硬塞行业元素。

所有背景气味都必须保持去品牌化：不出现真实公司名、真实 Logo、工牌品牌名、使命愿景原文、slogan 或具体公司业务说明。

## 资产

| 图 | 路径 | 作用 |
| --- | --- | --- |
| **设定图（必传）** | `assets/character/primary-character-reference.png` | 形体、主色、白圆眼、细线肢体 |
| **动作扩展（条件）** | `assets/character/primary-character-actions.png` | 复杂姿态 / 多人 / 小比例 |
| **可选模式样张** | `assets/character/examples/` | 身份漂移时可选 1 张辅助；**非强制** |

小石头识别简单（胶囊 + 白圆眼），**默认单锚点即可**。  
**双参考协议的重点是对齐老杨**，见 `persona-author-assets.md` / `assets/persona/examples/README.md`。不要把「双参考」名额用在小石头上。

主设定图负责“像不像小石头”。扩展图只在复杂姿态、表情基调、多个小石头协作或小比例远景时加读，不替代主设定图。身份明显漂移时，可从 `examples/{physical|handdrawn|knowledge-card}/` 加读 1 张样张辅助，仍以设定图为最高锚点。

## 填入 `{IP_DESC}`

> 组装顺序见 `references/common-prompt-slots.md`。本段紧接参考图，写在模式 DNA 之前。

```text
[Match the attached Little Stone character sheet]
Little Stone (小石头): flat 2D rounded vertical oval / capsule body, solid uniform #f39800 fill (no gradient, no highlight, no clay/vinyl/Pixar volume),
two flat white circular eyes + optional tiny black pupil dots (not glossy 3D eyeballs),
NO mouth / teeth / lip line on the capsule — emotion via pose and at most 0-1 sweat drop,
exactly 2 thin black line arms from upper-third lateral body sides + 2 thin black line legs from bottom edge,
hand terminal at most one simple grip per arm (small circle / C-shape / line hook),
temperament: earnest, reliable, slightly clumsy, a bit stubborn — express via physical action, not cute mascot posing.
Keep exact colors and proportions from the character sheet.
```

## 填入 `{IP_STYLE_ADAPT}`

> 写在通用 `{STYLE_ADAPT}` 之后。管 IP 锁色，不管构图。

```text
Little Stone color lock:
- Body fill = solid uniform #f39800 only; even a mild orange gradient, center highlight, rim shadow, or volume lighting fails
- Scene accent colors (cobalt tape, tomato-red marks, lemon tabs, soft pink) may appear on objects/annotations ONLY — never tint the capsule body, eyes, or limbs
- Limbs stay thin black lines; eyes stay flat white circles — do not inherit studio lighting or whiteboard wash into the character
- When author persona appears in a different render language, Little Stone must remain strictly flat 2D and visually distinct
```

## 品牌血脉

- `#f39800` 是小石头的主色，也是默认 profile 的主要识别色。
- 名字和主色有内部品牌来源，但正文、示例和提示词默认不展开具体公司信息或业务细节。
- 真实品牌 Logo 不随公开 profile 分发，Logo 规则见 `logo-safety.md`。
- 全场景音乐科技 / KTV / 门店经营语境只提供可选道具气味，不自动触发真实品牌 Logo。

## Character Lock

一次生成 2 张及以上时，全批一致项：

| 全批一致 | 可变 |
| --- | --- |
| `#f39800` 橙身 | 姿势 / 动作 |
| 胶囊轮廓 | 0-1 汗滴 |
| 白色小圆眼 + 可选 tiny 瞳孔 | 场景道具 |
| flat 2D 简笔 | 标签 |
| 细线肢体 | |

多人 / 多 Agent / 团队协作场景允许 2-4 个小石头，但它们必须像同一 IP 家族里的不同个体：共享 **#f39800 平涂、相同胶囊宽高比、相同白圆眼画法、相同细线肢体语言**；只允许通过 **整体等比缩放（±10–15% 高度差）、角度、站位、动作职责** 拉开差异，**禁止**把 A 画成细长条、B 画成矮胖球、C 画成横扁椭圆；禁止复制粘贴平移。

## 2D Flat Lock + Limbs Lock

生成前必须 **并列** 写入：

```text
2D Flat Lock:
- Little Stone = flat 2D sticker / paper cutout / simple vector illustration
- Body = solid #f39800, no gradient, no highlight, no clay / vinyl / Pixar texture
- Eyes = flat white circles + optional tiny dots, not glossy 3D eyeballs
- No mouth, no teeth, no lip line on the capsule — emotion via pose and 0-1 sweat drop only
- Limbs = thin black lines, not 3D tubes
- The orange body must be one uniform flat color block; even a subtle orange gradient, center highlight, rim shadow, or volume lighting is a failure

Limbs Lock:
- Exactly 2 arms + 2 legs per individual
- Arms: one continuous thin black line from each upper-third lateral body side
- Legs: one continuous thin black line from each bottom edge side or bottom center
- Hand terminal: at most one simple grip (small circle / C-shape / line hook) per arm
- Negative: extra arm, floating broken limb, forked fingers, rope-arrow merged into hand
```

实物图里的真实物件可以有摄影棚光影，但小石头本体不能跟着变 3D。作者 persona 可以按模式使用不同渲染语言，但不能带偏小石头。

## 失败信号

- 胶囊体出现渐变、高光、体积阴影、软陶、盲盒公仔、Pixar 或 emoji 3D 质感。
- 四肢变成圆管、粗短 3D 手脚。
- 白圆眼变成反光球体、玻璃珠或带眼窝的 3D 五官。
- 小石头身上或旁边出现 Logo / 品牌名 / 商标引导箭头。
- 把小石头画成正式企业 Logo、工牌吉祥物、客服头像或品牌代言海报，而不是用动作解决问题的正文配图角色。
- 每张都硬塞麦克风、包厢或 K 歌元素，导致和当前内容无关。
- 道具显得老旧、复古、笨重、脏乱或舞台化；除非用户明确要求，不用年代感强、商业舞台感强或厚重脏乱的道具。
- 删掉小石头后隐喻仍成立，说明它没有承担核心动作。
- **多人形体比例漂移**：同图里胶囊宽高比不一致（瘦高 / 矮胖 / 横扁混用）——典型不合格，必须重生成。
- **眼睛不合格**：眼距/大小批内不一致、anime 大眼、3D 反光眼、缺白圆或瞳孔画法不一。
- **手臂/腿不合格**：断线悬浮、同侧双手、分叉指、绳线粘连成第三只手、从非锚点位置长出（头顶/眼下方/体中部横腿）。
- **有嘴**：胶囊上出现嘴线、牙、唇形——直接不合格；情绪应靠动作与汗滴。
- **四肢批内不一致**：同图/同批线宽、锚点高度、末端画法漂移。

主角色与可选 persona（老杨）分工不同：小石头是 flat 2D 执行 Agent；老杨是触发型主讲 persona，见 `persona-author.md`。

## 英文称呼

`小石头（英文别名：Little Stone）`。`scene-skill-core` 是通用核心包名，与任何第三方商标无关。
