# Agent 快速决策表

**目标**：5 秒内判断模式 + 必读文件 + 是否触发 persona，无需完整阅读 SKILL.md。

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
| 老杨、yuezheng2006、老杨和小石头、让我和小石头一起 | ✅ 触发 persona |
| 小石头、未提及老杨 | ❌ 单 IP |
| 不要人物、纯物件、无 IP、none | → 改用 `ip-profiles/none/`（跳过默认角色资产） |

**触发后**：所有模式都增加 `persona-quick-checklist.md`（见后文）。none 模式不读 persona。

### 参考图协议（默认 profile）

**老杨出镜 → 双风格对齐**

- 实物：`author-persona-panorama.png`（真人实体）
- 手绘系：`author-persona-panorama-handdrawn.png` + `author-persona-panorama.png`（手绘更重要，实体锁同一人）
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
- [ ] 若老杨出镜：实体 panorama 已进上下文
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
- [ ] 若老杨出镜：手绘 panorama + 实体 panorama 已进上下文
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
- [ ] 若老杨出镜：手绘 panorama + 实体 panorama 已进上下文
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
  - 实物图 → `author-persona-spec.png`（复杂动作 + `actions.png`）
  - 手绘图/知识卡/PPT → `spec.png` + `handdrawn.png`
- **生成前并列写入**：Persona Identity Lock + Feature Stability Lock + Expression Lock
- **生成后增加检查**：P1-P7（老杨六项识别 + 表情）

---

## 简化 Confirm Gate（对用户隐藏技术术语）

### 生成后必做（内部检查）

**小石头 CRITICAL 项**：
- L1 计数：每个体恰好 2 臂 + 2 腿
- L2 锚点：臂从体侧上 1/3、腿从底缘连续向下
- E1 眼睛：两只白圆眼、批内一致

**老杨 CRITICAL 项**（双 IP 时）：
- P1 眼镜：大镜片浅灰细框（非粗黑框）
- P3 脸型：长但不细的长方椭圆
- P6 可见性：正面或 3/4（禁止背身/后脑勺）

### 交付标准
- ✅ **所有 CRITICAL 项 PASS** → 继续模式 QA → 交付
- ❌ **任一 CRITICAL 项 FAIL** → 对用户说明具体问题（不说 L1/P3 代号）→ 返修

**对用户说明示例**（FAIL 时）：
```
❌ 不合格："这张图小石头多了一只手臂，需要重新生成"
   而不是："形象 Confirm Gate: L1 FAIL (extra arm)"

❌ 不合格："老杨的眼镜是粗黑框，不符合他的形象（应该是浅灰细框），我来返修"
   而不是："Persona Feature Stability Lock: P1 FAIL"
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
| 猫不够金黄 / 灰虎斑 | ❌ 必须金黄金渐层英短 |
| 方法论知识卡只有老杨+文字 | ❌ 必须安排小石头执行分工 |

---

**使用建议**：
1. 每次任务开始先看本文件（QUICK-START.md），不要直接读 SKILL.md 全文
2. 按决策表顺序读取必读文件，完成检查清单
3. 生成后先做简化 Confirm Gate，再做模式 QA
4. 返修时参考 `references/common-qa-repair.md`
