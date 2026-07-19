# Agent 快速决策表

**目标**：5 秒内判断模式 + 必读文件 + 是否触发 persona，无需完整阅读 SKILL.md。

## 0. 自定义 IP 录入优先级

| 触发词 | 路由 | 第一轮动作 |
|---|---|---|
| 录入 IP、新建 IP、上传形象、创建角色档案、用这套形象 | `profile_enrollment` | 优先接收用户真实图，读取 `references/contracts/profile-contract.md`，建立 Profile Enrollment Card；未确认前不生图 |
| 已有 IP + 普通配图 | 普通模式路由 | 读取当前 profile 的 Contract 声明，再进入模式决策 |

录入阶段必须先确认身份方案。用户真实图是推荐的身份锚点；半身图标记为待补全，不直接作为全身 canonical asset。没有真实图时，生成草图只能作为待授权临时参考；当前模式没有校准图时，使用 `single`，不得伪称 `dual`。

本表中的 `references/`、`ip-profiles/` 等相对路径均从 `scene-skill-core/` Skill 根目录解析，不从当前工作区根目录解析。

## 第一步：识别模式（显式风格词优先）

| 用户输入关键词 | 模式 | 跳转 |
|--------------|------|------|
| 实物图、物件小现场、小石头实物图 | 实物图模式 | → 决策表 A |
| 手绘图、白板图、逻辑图、小石头手绘图 | 手绘图模式 | → 决策表 B |
| 知识卡、手机海报、收藏图、竖版传播图 | 知识卡模式 | → 决策表 C |
| PPT、课件、直播分享页、整套演讲页面 | PPT 演讲模式 | → 决策表 D |
| 彩蛋、长卷、超横版、项目复盘 | 实物图长卷 | → 决策表 A（长卷变体） |

**未显式指定**：处境/情绪 → 实物图；流程/结构 → 手绘图；能收藏传播 → 知识卡；多页演讲 → PPT。

## 第二步：识别 Persona 触发

| 触发词 | 判断 |
|--------|------|
| **含「小剧场」**（`小剧场` / `老杨小剧场` / `IP小剧场`） | ✅ **路径 C** → `persona-theater-checklist.md` |
| C + `小石头` / `Little Stone` | ✅ **C 组合**（潮玩底 + flat 2D；不打回 B） |
| 无「小剧场」（仅视觉印记 / 流程拆解图等） | ❌ **不进 C** |
| 老杨、yuezheng2006、老杨和小石头、让我和小石头一起（无「小剧场」） | ✅ **路径 B** 双 IP → `persona-quick-checklist.md` |
| 小石头、未提及老杨 | ❌ 单 IP |
| 不要人物、纯物件、无 IP、none | → 改用 `ip-profiles/none/`（跳过默认角色资产） |

**路径 B 触发后**：所有模式都增加 `persona-quick-checklist.md`。none 模式不读 persona。  
**路径 C 触发后**：读 `persona-theater-checklist.md`，**不要**套双 IP「必须互动」规则。

**人像硬门禁**：只要任务涉及人像参考图，先读 `references/common-persona-calibration.md`，完成参考图校准卡；校准 FAIL 时不生成、不批量、不交付。

### 参考图协议（默认 profile）

**老杨出镜 → 双风格对齐**

- 实物：`author-persona-panorama.png`（真人实体）
- 手绘系：`author-persona-panorama-handdrawn.png` + `author-persona-panorama.png`（手绘更重要，实体锁同一人）
- 多场景/返修：+ `author-persona-face-lock.png`
- 猫：金**黄**金渐层（点名/彩蛋时）

**仅小石头 → 单锚点** `primary-character-reference.png`

---

## 决策表 A：实物图模式

### 必读文件（按顺序）
```
1. ip-profiles/default-little-stone/character.md  
   → 确认小石头形象、{IP_DESC}/{IP_STYLE_ADAPT}、维度锁
   
2. references/physical-master-anchors.md  
   → 选母版类型 01-06
   
3. references/physical-style-dna.md  
   → 比例、留白、颜色、真实物件规则
```

### 可选文件（按需）
```
- references/common-prompt-slots.md  
  → 首次组装或换 IP 时读
  
- references/physical-object-patterns.md  
  → 复杂场景、多物件隐喻时读
  
- references/physical-qa-checklist.md  
  → 生成后 QA 时读
  
- ip-profiles/default-little-stone/assets/character/primary-character-actions.png  
  → 复杂姿态、多人协作时读
```

### 生成前检查清单
- [ ] 已选定母版类型（01-06）
- [ ] 已写出至少 3 个变异点（不复刻母版拓扑）
- [ ] 小石头设定图已进上下文（单锚点）
- [ ] 若老杨出镜：实体 panorama 已进上下文；多场景另加 face-lock
- [ ] 若涉及人像：参考图校准卡已完成且结论为 PASS
- [ ] 已写入 `{IP_DESC}` + `{IP_STYLE_ADAPT}` + 2D Flat Lock + Limbs Lock
- [ ] 2 张及以上：已声明 Character Lock

### 生成后检查清单
- [ ] **形象快检**（L1-L4 四肢 + E1-E2 眼面）→ 见简化 Confirm Gate
- [ ] 物件是否真实、留白是否足够
- [ ] 删掉小石头后隐喻是否还成立（装饰性测试）

---

## 决策表 B：手绘图模式

### 必读文件
```
1. ip-profiles/default-little-stone/character.md

2. references/handdrawn-style-dna.md  
   → 白底黑线、克制红橙蓝

3. references/handdrawn-composition-patterns.md  
   → 选结构类型（Workflow/系统局部/方法分层等）
```

### 可选文件
```
- references/common-prompt-slots.md
- primary-character-actions.png（复杂姿态时）
- references/handdrawn-qa-checklist.md  
  → 生成后 QA
```

### 生成前检查清单
- [ ] 已选定结构类型（不用实物母版）
- [ ] 已写出核心意思、主角色概念动作
- [ ] 小石头设定图已进上下文（单锚点）
- [ ] 若老杨出镜：手绘 panorama + 实体 panorama 已进上下文；多场景另加 face-lock
- [ ] 若涉及人像：参考图校准卡已完成且结论为 PASS
- [ ] 硬预算：1 个核心结构 + 3-5 模块 + 5-8 短批注
- [ ] 已写入 `{IP_DESC}` + `{IP_STYLE_ADAPT}` + 2D Flat Lock + Limbs Lock

### 生成后检查清单
- [ ] **形象快检**（L1-L4 + E1-E2）
- [ ] 是否只解释一个核心结构（未 PPT 化）
- [ ] 装饰性测试

---

## 决策表 C：知识卡模式

### 必读文件
```
1. ip-profiles/default-little-stone/character.md

2. references/knowledge-card-mode.md  
   → 形态库、必填字段、硬性预算

3. references/common-modes-and-sizes.md  
   → 确认尺寸（3:4/4:5/9:16）与信息量档位
```

### 可选文件
```
- references/common-prompt-slots.md
- references/handdrawn-style-dna.md  
  → 颜色规则（黑线+克制红橙蓝）
```

### 生成前检查清单
- [ ] 已选定知识卡形态（观点卡/路线图卡/行动清单卡等）
- [ ] 已完成必填字段（标题/模块拆分/角色分工）
- [ ] 小石头设定图已进上下文（有小石头时，单锚点）
- [ ] 若老杨出镜：手绘 panorama + 实体 panorama 已进上下文；多场景另加 face-lock
- [ ] 若涉及人像：参考图校准卡已完成且结论为 PASS
- [ ] 方法论/步骤类：已安排至少 2 个小石头分工
- [ ] 已写入 `{IP_DESC}` + `{IP_STYLE_ADAPT}` + 2D Flat Lock + Limbs Lock

### 生成后检查清单
- [ ] **形象快检**（L1-L4 + E1-E2；双 IP 时 + P1-P7）
- [ ] 是否有清楚的标题、阅读顺序、信息结构
- [ ] 未硬套参考形态

---

## 决策表 D：PPT 演讲模式

### 必读文件
```
1. ip-profiles/default-little-stone/character.md

2. references/ppt-presentation-mode.md  
   → 导演规划卡、page card、页面类型库

3. references/common-modes-and-sizes.md
```

### 工作流强制步骤
```
1. 输出整套导演规划卡（不直接批量出图）
2. 用户确认页数、节奏、密度
3. 选 1-2 页代表页做样张
4. 确认字体/人物/密度后分批生成
```

### 生成前检查清单
- [ ] 已输出导演规划卡并获确认
- [ ] 每页已有 page card
- [ ] 已写入 2D Flat Lock + Limbs Lock

### 生成后检查清单
- [ ] **形象快检**（每页）
- [ ] 整套 QA：字体系统、人物稳定、节奏变化
- [ ] 是否像 PPT 页面（不是知识卡或信息图海报）

---

## Persona 触发时增补（所有模式）

### 额外必读
```
references/persona-quick-checklist.md  
→ 5 秒决策 + 资产组合 + 互动场景 + 生成前 Lock + 生成后快检
```

### 核心变化
- **角色分工**：老杨主讲/拆解/批注，小石头执行 Agent
- **资产组合**：
  - 实物图 → `author-persona-panorama.png`（脸不稳 +face-lock；复杂动作 +actions）
  - 手绘/知识卡/PPT → **手绘全景 + 实体全景**（全身 +handdrawn-body；多场景 +face-lock）
- **生成前并列写入**：Identity + Feature/配件层 + Expression Preset（E0–E4）
- **人像参考校准**：先完成 `common-persona-calibration.md` 校准卡，PASS 后才允许生成
- **多场景**：先 1 张预览门禁，再批跑；FAIL 只返修单张
- **生成后检查**：P1–P7 + 跨图 X0–X6

---

## 简化 Confirm Gate（对用户隐藏技术术语）

### 生成后必做（内部检查）

**小石头 CRITICAL 项**：
- L1 计数：每个体恰好 2 臂 + 2 腿
- L2 锚点：臂从体侧上 1/3、腿从底缘连续向下
- E1 眼睛：两只白圆眼、批内一致
- **多人时**：同胶囊比例（只许整体缩放 ±10–15%）；每人独立动词；递接物在两握点之间；手=简笔拟人小掌+2–3 短指（握物可读）——详见 `character.md`

**老杨 CRITICAL 项**（双 IP / 小剧场时）：
- P1 眼镜：大镜片浅灰细框（非粗黑框）
- P3 脸型：长但不细的长方椭圆
- P6 可见性：正面或 3/4（禁止背身/后脑勺）
- **P12 身高**（全身/大半身）：**183 视觉档 + 4:6 长腿**；禁止漂成 ~175 平均身高 / 短腿敦实

### 交付标准
- ✅ **所有 CRITICAL 项 PASS** → 继续模式 QA → 交付
- ❌ **任一 CRITICAL 项 FAIL** → 对用户说明具体问题（不说 L1/P3 代号）→ 返修

**对用户说明示例**（FAIL 时）：
```
❌ 不合格："这张图小石头多了一只手臂，需要重新生成"
   而不是："形象 Confirm Gate: L1 FAIL (extra arm)"

❌ 不合格："老杨的眼镜是粗黑框，不符合他的形象（应该是浅灰细框），我来返修"
   而不是："Persona Feature Stability Lock: P1 FAIL"

❌ 不合格："老杨这张看起来像普通 175 身高，腿偏短，我按 183、上短下长加长腿返修"
   而不是："P12 Height Lock FAIL (~175 drift)"
```

---

## 典型场景快查

| 用户输入 | 5 秒决策 |
|---------|---------|
| "小石头实物图：这篇内容配 4 张图" | 实物图 + 单 IP → 读 character + master-anchors + style-dna |
| "老杨：推荐配图方案" | 触发 persona → 读 persona-quick-checklist + persona-scene-patterns → 先推荐不生图 |
| "老杨和小石头：白板图解释工作流" | 手绘图 + 双 IP → 读 character + handdrawn-style-dna + handdrawn-composition + persona-quick-checklist |
| "做一张能发朋友圈的方法论图" | 知识卡（竖版+收藏） → 读 knowledge-card-mode + modes-and-sizes |
| "把这 10 页大纲做成 PPT" | PPT 演讲 → 读 ppt-presentation-mode → 先出导演规划卡 |
| "纯物件，不要小石头" | none profile → 读 `ip-profiles/none/`，跳过角色资产 |

---

## 常见错误快速拦截

| 错误 | 拦截 |
|------|------|
| 一次读完所有 references/ 文件 | ❌ 按决策表按需读取 |
| 跳过母版锁定直接生图 | ❌ 实物图必须先选母版类型 + 写变异点 |
| 跳过导演规划直接批量出 PPT | ❌ PPT 必须先出规划卡 |
| 把 Confirm Gate 输出给用户看 | ❌ 只在内部检查，FAIL 时用自然语言说明问题 |
| 触发 persona 但忘记读 persona-quick-checklist | ❌ 所有双 IP 任务必读 |
| 韩范脸 / 非中国山东脸 | ❌ 必须北方中国男性脸型，禁止小脸V下巴冷白皮 |
| 手绘老杨缺手绘全景 | ❌ 必传 panorama-handdrawn + 实体 panorama |
| 多场景未预览就批跑 | ❌ 先 1 张预览过门再批跑 |
| 换表情丢眼镜/发型 | ❌ 配件层 face/head 每张必带 |
| 猫不够金黄 / 灰虎斑 | ❌ 必须金黄金渐层英短 |
| 方法论知识卡只有老杨+文字 | ❌ 必须安排小石头执行分工 |
| 老杨漂成 ~175 / 短腿敦实 | ❌ 全身必写 Height Lock 183+4:6；加传 handdrawn-body；P12 FAIL 必返修 |
| 多人瘦高+矮胖混用 / 假互动 | ❌ 同胶囊比例只许缩放；每人独立动词；递接物在两握点间；手脚末端按动作选型 |
| 手太抽象（纯 C/环）或写实五指 | ❌ 简笔拟人手：小掌+2–3 短指；绳与臂分笔 |
| 无关内容硬塞麦/包厢 | ❌ K 歌动作仅内容相关；加读 calibrate-karaoke-actions |
| K 歌画成舞台麦/巡检递麦 | ❌ 现代短柄无线麦 + 握麦/点歌/合唱等执行动作 |
| 悬浮断手 / 无连接假肢 | ❌ L1 硬禁；对麦合唱让歌词屏悬浮，勿叉腰+握麦+扶屏三接触 |
| 为凑双手反复重绘指形 | ⚠️ 放宽：可读握姿可接受；优先自然动作，勿过度清点手数 |

---

**使用建议**：
1. 每次任务开始先看本文件（QUICK-START.md），不要直接读 SKILL.md 全文
2. 按决策表顺序读取必读文件，完成检查清单
3. 涉及人像时先做参考图校准，再做简化 Confirm Gate，最后做模式 QA
4. 返修时参考 `references/common-qa-repair.md`
