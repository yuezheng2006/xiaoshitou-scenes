# 代码仓库结构与能力对应关系

> 本文档详细说明 xiaoshitou-scenes 仓库的代码结构与 Skill 能力的对应关系，帮助理解每个文件/目录的作用。

---

## 📁 仓库总览

```
xiaoshitou-scenes/
├── scene-skill-core/           # 核心 Skill 目录（Codex 加载）
├── assets/                     # 生成的图片资产
├── examples/                   # 使用示例
├── docs/                       # 项目文档
└── scripts/                    # 辅助脚本
```

---

## 🎯 核心能力与代码对应

### 能力 1: 环境检测与工具约束

**用户体验**: 自动检测 Codex 环境和 imagen 工具，失败时给出明确引导

**对应代码**:

```
scene-skill-core/
├── QUICK-START.md                        § -1 环境检测清单（4项）
├── references/
│   ├── codex-environment-guidance.md     完整环境检测指南（17 KB）
│   └── codex-exec-best-practices.md      实战经验与踩坑（本次新增）
└── SKILL.md                              allowed-tools: [imagen]
```

**工作原理**:
1. Skill 加载时自动读取 `QUICK-START.md`
2. 执行 § -1 的 4 项检测（Codex环境/目录/资产文件/参考图）
3. 失败时读取 `codex-environment-guidance.md` 给出引导
4. `codex-exec-best-practices.md` 记录实战踩坑经验

---

### 能力 2: 实物图生成（16:9）

**用户体验**: 输入"小石头实物图：<场景>"，生成真实物件小现场配图

**对应代码**:

```
scene-skill-core/
├── references/
│   ├── physical-style-dna.md             视觉 DNA 定义
│   ├── physical-master-anchors.md        6 个母版类型规则
│   └── physical-qa-checklist.md          质量检查清单
├── ip-profiles/default-little-stone/
│   ├── character.md                      小石头 IP 定义
│   └── assets/character/
│       └── primary-character-reference.png  参考图（imagen 传入）
└── assets/masters/
    ├── 01-alignment-pull-in.png          母版 01：对齐/拉入
    ├── 02-info-overload.png              母版 02：信息过载
    ├── 03-problem-knot-alert.png         母版 03：问题结/告警
    ├── 04-review-rework.png              母版 04：复核/返工
    ├── 05-automation-relabel.png         母版 05：自动化/重新标注
    └── 06-filter-loss.png                母版 06：过滤/损耗
```

**工作流程**:
1. 用户输入 → `QUICK-START.md` 路由到实物图模式
2. 读取 `physical-style-dna.md` 获取视觉 DNA
3. 读取 `physical-master-anchors.md` 选择母版类型（01-06）
4. 读取 `character.md` 获取小石头 IP 描述
5. 调用 imagen，传入 `primary-character-reference.png`
6. 生成后执行 `physical-qa-checklist.md` 质量检查
7. 通过后保存到 `assets/`

---

### 能力 3: 手绘图生成（16:9）

**用户体验**: 输入"小石头手绘图：<流程>"，生成白底黑线解释图

**对应代码**:

```
scene-skill-core/
├── references/
│   ├── handdrawn-style-dna.md            视觉 DNA 定义
│   ├── handdrawn-master-types.md         结构类型库
│   └── handdrawn-qa-checklist.md         质量检查清单
├── ip-profiles/default-little-stone/
│   ├── character.md                      小石头 IP 定义
│   └── assets/character/
│       └── primary-character-reference.png  参考图
```

**工作流程**:
1. 路由到手绘图模式
2. 读取 `handdrawn-style-dna.md` 获取视觉约束
3. 读取 `handdrawn-master-types.md` 选择结构类型
4. 组装提示词：白底 + 黑线 + 克制红橙蓝
5. 传入参考图生成
6. 执行 `handdrawn-qa-checklist.md` 检查

---

### 能力 4: 双 IP 模式（老杨 + 小石头）

**用户体验**: 输入"老杨：<内容>想配图"，老杨和小石头同框协作

**对应代码**:

```
scene-skill-core/
├── references/
│   ├── persona-quick-checklist.md        双 IP 快速决策（2秒）
│   ├── persona-scene-patterns.md         6 类互动场景
│   ├── common-persona-calibration.md     人像校准卡
│   └── common-persona-routing.md         Persona 路由规则
├── ip-profiles/default-little-stone/
│   ├── character.md                      小石头定义
│   ├── persona-author-identity.md        老杨身份定义
│   ├── persona-author-modes.md           各模式双 IP 职责
│   └── assets/
│       ├── character/primary-character-reference.png    小石头参考图
│       └── persona/author-persona-panorama.png          老杨参考图（全景）
```

**工作流程**:
1. 识别触发词"老杨" → `persona-quick-checklist.md`
2. 读取 `persona-scene-patterns.md` 选择互动场景类型
3. 读取 `persona-author-identity.md` 获取老杨身份锁
4. 读取 `persona-author-modes.md` 确定双 IP 分工
5. 调用 imagen，传入**两张参考图**（小石头 + 老杨）
6. 执行 `common-persona-calibration.md` 人像校准
7. 检查 P1-P7 Persona Identity Lock

---

### 能力 5: 知识卡模式（竖版传播图）

**用户体验**: 输入"做一张知识卡：<主题>"，生成 3:4 或 4:5 竖版图

**对应代码**:

```
scene-skill-core/
├── references/
│   └── knowledge-card-mode.md            知识卡模式完整规则
├── ip-profiles/default-little-stone/
│   └── character.md                      小石头定义
```

**工作流程**:
1. 识别触发词"知识卡" → `knowledge-card-mode.md`
2. 选择形态（封面型/流程型/对比型/清单型）
3. 确定比例（3:4 或 4:5）
4. 组装提示词：主讲区 + 执行模块 + 留白
5. 传入参考图生成竖版图

---

### 能力 6: PPT 演讲模式

**用户体验**: 输入"做一套 PPT：<主题>"，生成多页演讲配图

**对应代码**:

```
scene-skill-core/
├── references/
│   └── ppt-presentation-mode.md          PPT 模式完整规则
├── ip-profiles/default-little-stone/
│   └── character.md                      小石头定义
```

**工作流程**:
1. 识别触发词"PPT" → `ppt-presentation-mode.md`
2. 生成导演规划卡（分页策略）
3. 为每页生成 page card（页面类型 + 内容）
4. 逐页调用 imagen（批量）
5. 每页独立 QA 检查

---

### 能力 7: 视频模式

**用户体验**: 输入"小石头视频：<主题>"，生成 60-90 秒讲解视频

**对应代码**:

```
scene-skill-core/
├── references/
│   └── video-mode.md                     视频模式完整规则
├── scripts/
│   ├── video_create_project.py           创建 Remotion 项目
│   ├── video_fish_audio.py               调用 Fish Audio TTS
│   └── video_verify_output.py            验证输出视频
├── assets/remotion-template/             Remotion 模板
└── ip-profiles/default-little-stone/
    └── character.md                      小石头定义
```

**工作流程**:
1. 识别触发词"视频" → `video-mode.md`
2. 生成 plan.json（6-9 个场景）
3. 每个场景调用 imagen 生成插图（1080×1440）
4. 调用 `video_fish_audio.py` 生成旁白
5. 使用 `video_create_project.py` 创建 Remotion 项目
6. Remotion 渲染成 MP4
7. `video_verify_output.py` 验证输出

---

### 能力 8: 自定义 IP 录入

**用户体验**: 输入"用这个 Logo 录入新 IP"，从品牌标生成拟人 IP

**对应代码**:

```
scene-skill-core/
├── references/
│   ├── brand-mark-mode.md                Logo → IP 转换规则
│   └── contracts/
│       └── profile-contract.md           Profile Enrollment 状态机
├── ip-profiles/
│   ├── mark-demo/                        公开示例（豆包 App）
│   │   ├── character.md                  拟人 IP 定义
│   │   ├── logo-safety.md                Logo 边界
│   │   └── assets/
│   │       ├── reference/brand-mark-primary.png    Logo 原件
│   │       └── examples/                           校准图示例
│   └── [自定义]/                         用户录入的新 IP
```

**工作流程**:
1. 识别触发词"Logo/Icon/品牌标" → `brand-mark-mode.md`
2. 读取 `profile-contract.md` 创建 Enrollment Card
3. 提取身份锚点（Logo 内图形/主色/气质）
4. 状态：PENDING → CANONICAL_ASSET
5. 用户确认后，imagen 生成 identity_sheet（拟人设定图）
6. 状态：CANONICAL_ASSET → IDENTITY_SHEET
7. imagen 生成 mode calibration（各模式校准图）
8. 状态：IDENTITY_SHEET → MODE_CALIBRATION → AVAILABLE
9. 保存到 `ip-profiles/[自定义]/`

---

### 能力 9: Confirm Gate 自动质量检查

**用户体验**: 生成后自动检查 IP 形象，不合格图片不交付

**对应代码**:

```
scene-skill-core/
├── references/
│   ├── common-character-lock.md          通用 Character Lock
│   ├── common-persona-calibration.md     Persona 校准锁
│   ├── physical-qa-checklist.md          实物图 QA
│   └── handdrawn-qa-checklist.md         手绘图 QA
└── ip-profiles/default-little-stone/
    └── character.md                      小石头规格定义
```

**检查层级**:

| 检查项 | 文件 | 内容 |
|--------|------|------|
| L1 计数 | common-character-lock.md | 恰好 2 臂 + 2 腿 |
| L2 锚点 | common-character-lock.md | 臂从体侧上 1/3，腿从底缘 |
| L3 遮挡 | common-character-lock.md | 遮挡后仍可识别 |
| L4 比例 | common-character-lock.md | 头身比、肢体比例 |
| E1 眼睛 | common-character-lock.md | 两只白圆眼，批内一致 |
| E2 表情 | common-character-lock.md | 无嘴、无牙、无唇线 |
| P1-P7 | common-persona-calibration.md | Persona 身份锁（双 IP） |

**工作原理**:
1. 生成后自动读取 `common-character-lock.md`
2. 逐项检查 L1-L4, E1-E2
3. 双 IP 模式额外检查 P1-P7
4. 不通过 → 自动返修（最多 2 次）
5. 仍不通过 → 停止任务，报告原因

---

## 🗂️ 公共编排层

### 能力 10: 提示词组装

**对应代码**:

```
scene-skill-core/references/
├── common-prompt-slots.md                提示词槽位顺序
├── common-generation-templates.md        常用模板片段
└── common-story-extraction.md            内容提取规则
```

**槽位顺序** (来自 `common-prompt-slots.md`):

```text
1. {REF_IMAGE}              老杨双参考 / 小石头单锚点 / none
2. {IP_DESC}                当前 profile 的 character.md
3. {PERSONA_DESC}           仅老杨出镜时
4. {MODE_DNA}               physical / handdrawn / knowledge-card / ppt
5. {WHITESPACE_DESC}        留白与背景约束
6. {STYLE_ADAPT}            通用层：模式如何适配有角色画面
7. {IP_STYLE_ADAPT}         主角色主色不漂（如 #f39800）
8. {PERSONA_STYLE_ADAPT}    老杨面相锁（仅双 IP）
9. {NEGATIVE}               禁止项（粗黑框眼镜、黑长袖等）
```

---

### 能力 11: 内容理解与提取

**对应代码**:

```
scene-skill-core/references/
└── common-story-extraction.md
```

**提取维度**:
- 处境（Situation）
- 动作（Action）
- 标签（Labels，2-4 个短词）
- 冲突（Conflict）
- 主物件（Main Object）

**工作原理**:
1. 读取用户输入的内容
2. 按 `common-story-extraction.md` 规则提取
3. 不直接把内容当提示词
4. 转换为视觉元素（物件 + 动作 + 标签）

---

## 📂 IP Profile 系统

### Profile 结构

每个 IP 的完整定义：

```
ip-profiles/[profile-id]/
├── profile.md                    Profile 元数据
├── character.md                  主角色定义（必需）
├── persona-*.md                  Persona 定义（可选）
├── logo-safety.md                Logo 边界（自定义 IP）
└── assets/
    ├── character/                主角色资产
    │   ├── primary-character-reference.png    参考图（必需）
    │   ├── primary-character-actions.png      动作库
    │   └── examples/                          示例图
    ├── persona/                  Persona 资产（双 IP）
    │   ├── author-persona-panorama.png        全景参考
    │   ├── author-persona-face-lock.png       面相锁
    │   └── examples/                          示例图
    └── reference/                Logo 原件（自定义 IP）
        └── brand-mark-primary.png
```

### 三个内置 Profile

1. **default-little-stone** - 默认双 IP（小石头 + 老杨）
2. **none** - 无角色 Profile（纯物件场景）
3. **mark-demo** - 自定义 IP 示例（豆包 App）

---

## 🔧 辅助工具

### 脚本目录

```
scripts/
├── validate-brand-mark-doubao.sh    豆包 IP 本地验证脚本
└── (其他辅助脚本)
```

### 视频模式脚本

```
scene-skill-core/scripts/
├── video_create_project.py          创建 Remotion 项目
├── video_fish_audio.py              TTS 语音合成
└── video_verify_output.py           验证输出视频
```

---

## 📊 资产输出目录

### 生成的图片保存位置

```
assets/
├── little-stone-environment-check-passed.png    测试图 1（环境检测）
├── showcase/                                    展示图集
│   ├── 01-tech-debt.png                        技术债务场景
│   ├── 02-workflow-revised.png                 工作流程
│   └── 03-collaboration.png                    双 IP 协作
└── (其他生成的图片)
```

---

## 📖 文档目录

### 项目文档

```
docs/
├── CODEX-ENVIRONMENT-ENHANCEMENT.md    环境检测强化总结
└── (其他项目文档)
```

### 根目录文档

```
xiaoshitou-scenes/
├── README.md                           项目总览
├── SUCCESS-REPORT.md                   测试验证报告
├── SETUP-COMPLETE.md                   使用说明
├── FEISHU_DOC_UPDATE.md                飞书文档更新内容
├── CODEBASE-CAPABILITY-MAPPING.md      本文件
├── IP-NOTICE.md                        角色形象边界
└── NOTICE.md                           致谢与参考
```

---

## 🔄 完整工作流示例

### 实物图生成完整路径

```
用户输入: "小石头实物图：技术债务越积越多"
    ↓
1. QUICK-START.md § -1
   执行环境检测（Codex / imagen / 资产）
    ↓
2. QUICK-START.md § 1
   判断模式 → physical（实物图）
    ↓
3. physical-style-dna.md
   读取视觉 DNA（纯白背景、真实物件、大留白）
    ↓
4. physical-master-anchors.md
   选择母版类型 → 03-problem-knot-alert
    ↓
5. common-story-extraction.md
   提取：处境=债务堆积，动作=支撑/加固，标签=技术债、重构、风险
    ↓
6. character.md
   读取小石头 IP 定义（橙色胶囊、白圆眼、细黑肢）
    ↓
7. common-prompt-slots.md
   按槽位顺序组装提示词
    ↓
8. imagen 工具
   传入 primary-character-reference.png + 提示词
   生成 1672×941 PNG
    ↓
9. common-character-lock.md
   Confirm Gate 检查 L1-L4, E1-E2
    ↓
10. physical-qa-checklist.md
    实物图专项 QA（留白、物件、标签）
    ↓
11. 保存到 assets/
    文件名：tech-debt-scene.png
    交付给用户
```

---

## 🎯 能力与代码对应表

| 能力 | 触发方式 | 核心文件 | 输出 |
|------|---------|---------|------|
| 环境检测 | 自动（首次任务） | QUICK-START § -1, codex-environment-guidance.md | 检测报告 |
| 实物图 | "小石头实物图：..." | physical-*.md, character.md | 16:9 PNG |
| 手绘图 | "小石头手绘图：..." | handdrawn-*.md, character.md | 16:9 PNG |
| 双 IP | "老杨：..." | persona-*.md, 双参考图 | 16:9 PNG |
| 知识卡 | "做一张知识卡：..." | knowledge-card-mode.md | 3:4/4:5 PNG |
| PPT | "做一套 PPT：..." | ppt-presentation-mode.md | 多张 16:9 PNG |
| 视频 | "小石头视频：..." | video-mode.md, scripts/ | MP4 |
| 自定义 IP | "用这个 Logo..." | brand-mark-mode.md, profile-contract.md | 新 Profile |
| Confirm Gate | 自动（每次生成后） | common-character-lock.md | 质量报告 |
| 提示词组装 | 自动（生成前） | common-prompt-slots.md | 完整提示词 |
| 内容提取 | 自动（理解阶段） | common-story-extraction.md | 视觉元素 |

---

## 💡 关键设计思想

### 1. Profile 与模式解耦

**设计**:
- IP 身份定义在 `ip-profiles/[id]/character.md`
- 模式规则定义在 `references/[mode]-*.md`
- 两者独立，通过 `common-prompt-slots.md` 组装

**好处**:
- 换 IP 不改模式规则
- 换模式不改 IP 定义
- 支持自定义品牌 IP

### 2. 环境检测前置

**设计**:
- 环境检测在 `QUICK-START.md § -1`（最优先）
- Skill 加载后立即执行
- 失败立即停止，不在生成后报错

**好处**:
- 避免浪费 token
- 明确告知用户环境问题
- 提供解决方案

### 3. Confirm Gate 自动化

**设计**:
- 生成后自动执行检查
- 不合格自动返修（最多 2 次）
- 仍不合格停止任务

**好处**:
- 保证 IP 形象一致性
- 减少人工检查成本
- 可追溯质量问题

### 4. 文档按需加载

**设计**:
- `QUICK-START.md` 是 5 秒决策表
- 只读取当前模式需要的文件
- 不一次性加载所有 references/

**好处**:
- 节省 token
- 加快响应速度
- 降低上下文复杂度

---

## 📈 代码统计

| 类别 | 文件数 | 行数 | 说明 |
|------|--------|------|------|
| 入口文档 | 3 | ~3,000 | SKILL / QUICK-START / README |
| 模式规则 | 12 | ~8,000 | physical / handdrawn / knowledge-card / ppt / video |
| IP Profile | 3 | ~2,000 | default-little-stone / none / mark-demo |
| 公共编排 | 8 | ~4,000 | prompt-slots / story-extraction / generation-templates |
| 环境检测 | 2 | ~2,000 | codex-environment-guidance / codex-exec-best-practices |
| 质量检查 | 5 | ~3,000 | character-lock / persona-calibration / qa-checklists |
| 脚本工具 | 4 | ~500 | video / validation |
| 参考资产 | 20+ | - | PNG 图片 |
| 项目文档 | 6 | ~3,000 | README / SUCCESS-REPORT / FEISHU_DOC_UPDATE |
| **总计** | **60+** | **~25,000** | - |

---

## 🔗 快速导航

### 按角色导航

**用户**（想快速使用）:
- 先读 `README.md`
- 再读 `QUICK-START.md` § 0-2
- 直接用 `codex exec "小石头实物图：<内容>"`

**开发者**（想理解原理）:
- 读本文件（CODEBASE-CAPABILITY-MAPPING.md）
- 读 `ARCHITECTURE-DESIGN.md`
- 读具体模式的 `*-style-dna.md`

**贡献者**（想扩展功能）:
- 读 `profile-contract.md`（新增 IP）
- 读 `common-prompt-slots.md`（新增槽位）
- 读 `codex-exec-best-practices.md`（实战经验）

### 按任务导航

**生成实物图**:
→ `physical-style-dna.md` → `physical-master-anchors.md`

**生成手绘图**:
→ `handdrawn-style-dna.md` → `handdrawn-master-types.md`

**老杨出镜**:
→ `persona-quick-checklist.md` → `persona-scene-patterns.md`

**自定义 IP**:
→ `brand-mark-mode.md` → `profile-contract.md`

**生成视频**:
→ `video-mode.md` → `scripts/video_*.py`

---

**最后更新**: 2026-07-21  
**文档版本**: v1.0  
**维护者**: [@yuezheng2006](https://github.com/yuezheng2006)
