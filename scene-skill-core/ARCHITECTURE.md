# 文档架构与依赖关系

本文件只记录单一真相来源、读取路径和维护影响范围；不保存历史优化记录或文件行数。

## 单一真相来源

| 概念 | 唯一定义位置 | 其他文件职责 |
|---|---|---|
| 小石头形象、IP 槽位、2D/Limbs Lock | `ip-profiles/default-little-stone/character.md` | 引用并按任务填入 |
| 老杨身份与识别锚点 | `ip-profiles/default-little-stone/persona-author-identity.md` | 引用，不重写身份细节 |
| 老杨资产组合与传图协议 | `ip-profiles/default-little-stone/persona-author-assets.md` | Quick Start 和 slots 只做路径索引 |
| 人像参考图校准协议 | `references/common-persona-calibration.md` | 所有涉及人像的模式和 QA 只引用 |
| Persona 入口与触发词 | 当前 profile 的 `persona-author.md` | 通用路由只描述机制 |
| 双 IP 场景库 | `references/persona-scene-patterns.md` | 模式文件引用场景类型 |
| 模式路由与边界 | `references/mode-decision-matrix.md` | SKILL / Quick Start 只做快速跳转 |
| Prompt 槽位顺序 | `references/common-prompt-slots.md` | 各模板填充槽位 |
| 通用锁与 Confirm Gate | `references/common-character-lock.md` | 角色形象回到 profile 定义 |
| 实物母版 | `references/physical-master-anchors.md` | 只引用母版类型，不复制布局 |
| 手绘结构类型 | `references/handdrawn-composition-patterns.md` | 只引用结构类型 |
| 知识卡形态 | `references/knowledge-card-mode.md` | 只引用形态和 QA |
| PPT 页面类型 | `references/ppt-presentation-mode.md` | 只引用页面类型和流程 |
| 返修格式 | `references/common-qa-repair.md` | 各模式 QA 引用 |
| 任务交接协议 | `references/contracts/` | Task Card、Plan Card、Render Card、QA Card；各模式按需填写 |
| IP 配置契约 | `references/contracts/profile-contract.md` | Profile 身份、参考协议、录入状态、动作库和发布边界 |

## Agent 最小读取路径

### 实物图 + 单 IP

```text
QUICK-START.md → character.md
→ physical-master-anchors.md → physical-style-dna.md
→ common-prompt-slots.md（首次组装/换 IP 时）
→ 生成后 common-character-lock.md + physical-qa-checklist.md
```

### 手绘图 + 双 IP

```text
QUICK-START.md → character.md
→ persona-quick-checklist.md
→ persona-author-assets.md → persona-scene-patterns.md
→ handdrawn-style-dna.md → handdrawn-composition-patterns.md
→ 生成后 common-character-lock.md + handdrawn-qa-checklist.md
```

### 知识卡 / PPT

```text
QUICK-START.md → character.md
→ persona-quick-checklist.md（触发 persona 时）
→ knowledge-card-mode.md 或 ppt-presentation-mode.md
→ common-modes-and-sizes.md
→ 生成后对应模式 QA
```

### 实物图试点 + 交接卡

```text
QUICK-START.md → task-card.md
→ plan-card.md → physical-master-anchors.md → physical-style-dna.md
→ render-card.md → 生成后 qa-card.md + physical-qa-checklist.md
```

## 修改影响范围

| 修改内容 | 唯一修改位置 | 只需检查 |
|---|---|---|
| 小石头颜色/形体/维度锁 | `character.md` | QUICK-START、common-character-lock 引用 |
| 老杨脸型/年龄/穿搭 | `persona-author-identity.md` | persona-quick-checklist 快速摘要 |
| 老杨参考图组合 | `persona-author-assets.md` | common-prompt-slots、QUICK-START |
| Persona 触发词 | 当前 profile 的 `persona-author.md` | profile、common-persona-routing |
| 模式路由 | `mode-decision-matrix.md` | SKILL、QUICK-START |
| 模式结构/预算 | 对应模式 reference | SKILL 中的跳转说明 |
| Prompt 槽位顺序 | `common-prompt-slots.md` | common-generation-templates |
| Confirm Gate | `common-character-lock.md` | QUICK-START、各模式 QA |

## 维护检查

- 角色细节是否仍只有 profile 文件定义？
- 老杨资产是否仍以实体全景/手绘全景为主锚？
- Quick Start 是否只是快速入口，没有创造新规则？
- 各模式 QA 是否只保留模式特有检查？
- 交接卡是否只传递上一阶段已确认的信息，没有重新发明事实？
- 是否出现旧资产名、旧颜色或旧 Skill 名称？
- 新增模式是否同步更新模式矩阵、Quick Start 和 SKILL 跳转？
