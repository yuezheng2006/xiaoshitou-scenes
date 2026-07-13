# 文档架构与依赖关系

本文件是维护者参考，说明文档间的依赖关系与单一真相来源（Single Source of Truth）原则。

---

## 单一真相来源原则

| 概念 | 唯一定义位置 | 其他文件 |
|------|------------|---------|
| 小石头形象规范 | `ip-profiles/default-little-stone/character.md` | 其他文件只引用，不重复定义 |
| `{IP_DESC}` / `{IP_STYLE_ADAPT}` | 当前 profile 的 `character.md` | `common-prompt-slots.md` 只定义槽位顺序 |
| 双参考协议（对齐人） | `persona-author-assets.md` + `assets/persona/examples/README.md` | `common-prompt-slots.md` / QUICK-START 只引用；**对象是老杨，不是小石头** |
| 小石头参考图 | `character.md`（默认单锚点） | 可选 `assets/character/examples/` |
| 无角色路径 | `ip-profiles/none/` | 不在默认 profile 内重复 |
| 老杨形象规范 | `ip-profiles/default-little-stone/persona-author-identity.md` | 其他文件只引用 |
| 2D Flat Lock 完整 prompt | `character.md` | `common-character-lock.md` 不重复，只说"见 character.md" |
| Limbs Lock 完整 prompt | `character.md` | `common-character-lock.md` 不重复 |
| Persona Identity Lock 完整 prompt | `persona-author-identity.md` 或 `persona-quick-checklist.md` | `common-character-lock.md` 不重复 |
| Prompt 槽位组装顺序 | `references/common-prompt-slots.md` | 模板文件按此顺序填槽 |
| 实物图母版 01-06 规则 | `references/physical-master-anchors.md` | 不在其他文件重复描述母版 |
| 手绘图结构类型 | `references/handdrawn-composition-patterns.md` | 不在其他文件重复 |
| 知识卡形态库 | `references/knowledge-card-mode.md` | 不在其他文件重复 |
| PPT 页面类型库 | `references/ppt-presentation-mode.md` | 不在其他文件重复 |
| 尺寸与信息量分级 | `references/common-modes-and-sizes.md` | 所有模式统一引用 |
| 模式路由决策 | `references/mode-decision-matrix.md` | SKILL.md 只给简要说明 |
| 返修输出格式 | `references/common-qa-repair.md` | 所有 QA 文件统一引用 |
| Persona 快速决策 | `references/persona-quick-checklist.md` | 汇总双 IP 所有 CRITICAL 项 |

---

## 文档依赖图

```
QUICK-START.md（入口）
    ↓
    ├─ 决策表 A（实物图）
    │   ├─ character.md（唯一定义）
    │   ├─ physical-master-anchors.md
    │   ├─ physical-style-dna.md
    │   └─ physical-qa-checklist.md（可选）
    │
    ├─ 决策表 B（手绘图）
    │   ├─ character.md（唯一定义）
    │   ├─ handdrawn-style-dna.md
    │   ├─ handdrawn-composition-patterns.md
    │   └─ handdrawn-qa-checklist.md（可选）
    │
    ├─ 决策表 C（知识卡）
    │   ├─ character.md（唯一定义）
    │   ├─ knowledge-card-mode.md
    │   └─ common-modes-and-sizes.md
    │
    ├─ 决策表 D（PPT）
    │   ├─ character.md（唯一定义）
    │   ├─ ppt-presentation-mode.md
    │   └─ common-modes-and-sizes.md
    │
    └─ Persona 触发增补
        ├─ persona-quick-checklist.md（快速决策）
        ├─ persona-author.md（唯一定义入口）
        ├─ persona-author-identity.md（身份唯一定义）
        ├─ persona-author-assets.md（资产组合）
        ├─ persona-author-modes.md（各模式职责）
        └─ persona-scene-patterns.md（六类互动场景）

common-character-lock.md（通用机制）
    ├─ 引用 character.md（不重复定义）
    ├─ 引用 persona-author-identity.md（不重复定义）
    └─ 只描述"如何锁定""如何检查"

common-qa-repair.md（通用 QA）
    └─ 装饰性测试 + 用户反馈映射 + 返修格式（所有 QA 引用）

mode-decision-matrix.md（模式决策）
    └─ 四种模式对比 + 边界案例决策
```

---

## Agent 最小读取路径

### 场景 1：实物图 + 单 IP
```
QUICK-START.md → 决策表 A
→ character.md（小石头唯一定义 + {IP_DESC}/{IP_STYLE_ADAPT} + Flat/Limbs Lock；单锚点）
→ common-prompt-slots.md（组装顺序，首次或换 IP 时）
→ physical-master-anchors.md（选母版类型）
→ physical-style-dna.md（比例/留白/颜色）
→ 传小石头设定图后生成
→ 生成后：简化 Confirm Gate（L1-L2 + E1）
→ physical-qa-checklist.md（模式 QA）
```

### 场景 2：手绘图 + 双 IP
```
QUICK-START.md → 决策表 B + Persona 增补
→ character.md（小石头唯一定义）
→ persona-quick-checklist.md（老杨快速决策）
    → persona-author-assets.md（资产组合：spec + handdrawn）
    → persona-scene-patterns.md（选互动场景类型）
→ handdrawn-style-dna.md（白底黑线）
→ handdrawn-composition-patterns.md（选结构类型）
→ 生成后：简化 Confirm Gate（L1-L2 + E1 + P1/P3/P6）
→ handdrawn-qa-checklist.md（模式 QA）
```

### 场景 3：知识卡 + 双 IP
```
QUICK-START.md → 决策表 C + Persona 增补
→ character.md（小石头唯一定义）
→ persona-quick-checklist.md（老杨快速决策）
→ knowledge-card-mode.md（形态库 + 必填字段）
→ common-modes-and-sizes.md（尺寸与信息量）
→ 生成后：简化 Confirm Gate（L1-L2 + E1 + P1/P3/P6）
→ knowledge-card-mode.md QA 章节
```

---

## 常见修改场景与影响范围

| 修改内容 | 唯一修改位置 | 需同步检查 |
|---------|------------|-----------|
| 小石头形象调整（颜色/形体） | `character.md` | `QUICK-START.md`（确认引用正确） |
| `{IP_DESC}` / `{IP_STYLE_ADAPT}` | `character.md` | `common-prompt-slots.md` 槽位名不变 |
| 老杨双参考 / 校准样张 | `persona-author-assets.md` + `assets/persona/examples/` | `persona-quick-checklist.md`、QUICK-START |
| 无角色路径调整 | `ip-profiles/none/` | `QUICK-START.md` 触发词 |
| 老杨形象调整（眼镜/穿搭） | `persona-author-identity.md` | `persona-quick-checklist.md`（确认快速版同步） |
| 新增母版类型 07 | `physical-master-anchors.md` | `QUICK-START.md` 决策表 A 无需改 |
| 新增知识卡形态 | `knowledge-card-mode.md` | 无需改其他文件 |
| Limbs Lock 调整 | `character.md` | `persona-quick-checklist.md`（确认核心要点同步）、`QUICK-START.md`（确认简化版同步） |
| Persona Lock 调整 | `persona-author-identity.md` | `persona-quick-checklist.md`（同步快速版） |
| 新增模式 | 新建 `references/new-mode.md` | 更新 `QUICK-START.md`（增加决策表）、`mode-decision-matrix.md`（增加对比行）、`SKILL.md`（更新模式路由） |

---

## 去重检查清单（定期维护）

每次修改后检查：

- [ ] `character.md` 是否仍是小石头形象的唯一定义（单锚点 + IP 槽位）？
- [ ] `persona-author-assets.md` 是否仍把双参考定义为**对齐老杨**？
- [ ] `common-prompt-slots.md` 是否只定义组装顺序、不硬编码具体角色？
- [ ] `ip-profiles/none/` 是否仍可独立运行、不依赖默认角色资产？
- [ ] `persona-author-identity.md` 是否仍是老杨形象的唯一定义？
- [ ] `common-character-lock.md` 是否只描述机制、不重复具体 Lock 内容？
- [ ] `persona-quick-checklist.md` 的快速版是否与完整版（`persona-author-identity.md`）一致？
- [ ] `QUICK-START.md` 的简化 Confirm Gate 是否与 `common-character-lock.md` 一致？
- [ ] 所有 QA 文件是否统一引用 `common-qa-repair.md` 的返修格式？

---

## 文档长度参考（当前）

| 文件 | 行数 | 职责 |
|------|-----|------|
| SKILL.md | 310 | 主入口（已增加快速跳转） |
| QUICK-START.md | ~350 | 5 秒决策表（新增） |
| persona-quick-checklist.md | ~280 | 双 IP 快速决策（新增） |
| mode-decision-matrix.md | ~200 | 模式对比（新增） |
| common-character-lock.md | 209 | 通用锁机制（已去重） |
| character.md | 109 | 小石头唯一定义 |
| persona-author-identity.md | ~150 | 老杨唯一定义 |
| physical-master-anchors.md | 301 | 实物图母版 |
| knowledge-card-mode.md | 113 | 知识卡模式 |
| ppt-presentation-mode.md | 146 | PPT 演讲模式 |
| common-qa-repair.md | 70 | 通用 QA（已优化返修格式） |

---

## 新增文件说明

### QUICK-START.md
- **目标**：Agent 5 秒决策，无需读完 SKILL.md 全文
- **内容**：四种模式决策表 + 必读文件 + 简化 Confirm Gate + 常见场景快查
- **维护**：新增模式时增加决策表

### persona-quick-checklist.md
- **目标**：触发 persona 后 5 秒决策，无需跳转多个文件
- **内容**：六类互动场景 + 资产组合速查 + 生成前三个 Lock + P1-P7 快检
- **维护**：`persona-author-identity.md` 修改时同步快速版

### mode-decision-matrix.md
- **目标**：快速区分四种模式，避免误判
- **内容**：详细对比表 + 典型用户输入映射 + 边界案例决策
- **维护**：新增模式时增加对比行

---

**维护建议**：
1. 修改前先查本文件确认唯一定义位置
2. 修改后检查"需同步检查"列
3. 定期执行"去重检查清单"
4. 新增文件时更新本文件的依赖图
