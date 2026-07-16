# IP 设计优化实施计划

日期：2026-07-16  
状态：执行中  
目标：降低系统复杂度，提升可维护性与 Agent 执行效率

## 背景

完整项目走查发现：
- 文档总量 10,000+ 行
- 老杨资产 11 个 PNG（冗余）
- Confirm Gate 检查项 20+ 项（过载）
- 路径 A/B/C + C组合 认知负担重
- 年龄锁定过度精确（38 岁 vs 模型能力）

核心矛盾：**追求极致一致性 vs 生图模型能力边界**

## 优先级分级

### P0 - 立即修复（本次实施）

1. **精简老杨资产**：11 个 → 5 个核心
2. **合并 spec 和 face-lock**：功能重叠
3. **年龄锁从精确值改为范围**：38 岁 → 35-40 岁

### P1 - 近期改进（下一阶段）

4. **简化 Confirm Gate**：分级检查
5. **路径命名优化**：简化 A/B/C 认知
6. **引入检查容忍度**：量化范围

### P2 - 长期优化（规划中）

7. **去品牌化雷石叙事**
8. **四种模式平等化**
9. **开发自动化检查工具**

## P0 详细方案

### 1. 精简老杨资产（11 → 5）

**保留核心**：
```
01. author-persona-panorama.png          # 实体全景（实物图必传）
02. author-persona-panorama-handdrawn.png # 手绘全景（手绘系必传）
03. author-persona-face-lock.png          # 面相锁定（多场景/返修）
04. author-persona-handdrawn-body.png     # 手绘身材比例（全身比例）
05. author-persona-actions.png            # 动作扩展（小比例/复杂姿态）
```

**废弃/合并**：
```
❌ author-persona-spec.png               # 功能被 face-lock 覆盖
❌ author-persona-handdrawn.png          # 历史遗留，被 panorama-handdrawn 替代
❌ author-persona-flat-ip-sheet.png      # 仅用于特定校准，移到 examples/
❌ author-persona-flat-ip-sheet-navy.png # 同上
⚠️  会话临时 1:1 肖像                    # 保留概念，但不作为固定资产
⚠️  批内金样                             # 保留概念，作为临时引用
```

**影响文件**：
- `persona-author-assets.md`：资产清单、传图决策表、引用优先级链
- `persona-quick-checklist.md`：传图协议
- `persona-author-prompts.md`：资产引用片段
- `QUICK-START.md`：决策表传图部分

### 2. 合并 spec 和 face-lock

**方案**：
- 删除 `spec.png` 作为独立资产
- `face-lock.png` 承担全部"面相锁定 + 禁止偏移区"功能
- 如需补充禁止偏移细节，在 `persona-author-identity.md` 文字描述

**修改**：
```text
旧：face-lock（多场景）+ spec（返修禁止偏移区）
新：face-lock（多场景 + 返修 + 禁止偏移）
```

### 3. 年龄锁改为范围

**修改点**：

`persona-author-identity.md`：
```markdown
旧：**锁定 38 岁视觉年龄档**
新：**视觉年龄范围：35-40 岁成熟男性**
```

`persona-author-prompts.md`：
```text
旧：Age Lock HARD: exactly the same 38-year-old Chinese male visual age
新：Age Lock: 35-40 year-old mature Chinese male visual age range
```

**说明**：
- 允许 ±2-3 岁的视觉波动
- 保留"不用皱纹堆年龄"的核心要求
- 强调禁止区间：NOT 20s baby-faced, NOT 50+ elderly

## 实施步骤

### Step 1: 备份与标记
- [x] 创建本计划文档
- [x] 标记待废弃资产（在文档中注释）

### Step 2: 更新资产文档
- [x] `persona-author-assets.md`：资产清单精简（11 → 5 核心）
- [x] `persona-author-assets.md`：传图决策表简化（删除 spec 引用）
- [x] `persona-author-assets.md`：引用优先级链更新（删除 spec/handdrawn/flat-ip-sheet）

### Step 3: 更新快速决策
- [x] `persona-quick-checklist.md`：传图协议简化（废弃资产标注）
- [x] `persona-quick-checklist.md`：年龄锁改为 35-40 岁范围
- [x] `QUICK-START.md`：决策表传图部分（加 face-lock 说明）

### Step 4: 更新身份文档
- [x] `persona-author-identity.md`：年龄锁改为 35-40 岁范围
- [x] `persona-author-identity.md`：外形约束表增加年龄范围行
- [x] `persona-author-identity.md`：删除 spec 引用

### Step 5: 更新 Prompts
- [x] `persona-author-prompts.md`：年龄锁 prompt（35-40 年龄范围）
- [x] `persona-author-prompts.md`：资产引用片段（删除 spec，改为 face-lock）
- [x] `persona-author-prompts.md`：返修片段更新

### Step 6: 更新通用规则
- [x] `common-character-lock.md`：Persona Lock 引用更新（已验证无需修改）
- [x] `common-persona-routing.md`：资产引用更新（已验证无需修改）
- [x] `common-generation-templates.md`：删除 spec 引用
- [x] `common-qa-repair.md`：删除 spec 引用
- [x] `physical-qa-checklist.md`：删除 spec 引用，更新年龄范围
- [x] `persona-author.md`：更新资产清单编号

### Step 7: 验证与清理
- [x] 搜索所有 spec 引用，确认已删除或标注废弃（剩余 0 处活跃引用）
- [x] 搜索所有"38岁"精确值，确认已改为范围（剩余 12 处，均为历史文档或非核心引用）
- [x] 运行 `scripts/validate-skill-local.sh` - 结构验证通过
- [x] 更新 ARCHITECTURE.md（无需修改，单一真相来源原则未变）
- [ ] 提交 Git commit

## 预期收益

**量化指标**：
- 老杨资产：11 个 → 5 个（-55%）
- Agent 决策点：减少 4 个"何时用 spec/flat-ip-sheet"判断
- 年龄容忍度：0 岁 → ±3 岁范围

**质量提升**：
- Agent 传图决策更清晰
- 生图成功率提升（年龄范围放宽）
- 文档维护负担降低

## 风险与应对

**风险 1**：现有 assets/ 中的 spec.png 已有内容
- **应对**：保留文件但标记为废弃，文档不再引用

**风险 2**：年龄范围放宽后一致性降低
- **应对**：保留"禁止幼态/显老"硬边界，范围内波动可接受

**风险 3**：用户已习惯 38 岁精确表述
- **应对**：在交付说明中仍可说"约 38 岁"，内部执行用范围

## 后续计划

P0 完成后，评估效果并启动 P1：
1. 简化 Confirm Gate（分级检查）
2. 路径命名优化（A/B/C 认知简化）
3. 引入检查容忍度（量化范围）

## 实施结果（2026-07-16）

### ✅ 已完成项（P0）

**1. 老杨资产精简：11 个 → 5 个核心资产**
- 保留：panorama（实体）、panorama-handdrawn（手绘）、face-lock（面相锁定 + 禁止偏移）、handdrawn-body（全身比例）、actions（动作扩展）
- 废弃：spec.png（功能合并到 face-lock）、handdrawn.png（历史遗留）、flat-ip-sheet 对（移至 examples/）
- 影响：Agent 决策点减少 4 个，传图协议简化

**2. 年龄锁定改为范围：38 岁 → 35-40 岁成熟男性**
- 修改文件：persona-author-identity.md、persona-author-prompts.md、persona-quick-checklist.md、physical-qa-checklist.md
- Prompt 更新：从 "exactly 38-year-old" 改为 "35-40 year-old mature male range"
- 容忍度：允许范围内 ±2-3 岁自然波动
- 保留底线：禁止 20 多岁幼态、禁止 45+/50+ 显老、禁止用皱纹堆年龄

**3. 资产引用全面更新**
- 删除所有 spec.png 活跃引用（0 处剩余）
- 引用优先级链简化：从 9 层 → 5 层
- 传图决策表简化：删除"可选 spec"条目
- 文档标注废弃资产，避免误用

### 📊 量化指标

| 维度 | 优化前 | 优化后 | 改进 |
|------|--------|--------|------|
| 老杨资产数 | 11 个 PNG | 5 个核心 | -55% |
| 引用优先级链 | 9 层 | 5 层 | -44% |
| 年龄容忍度 | 精确 38 岁 | 35-40 岁范围 | ±3 岁 |
| Agent 决策点 | "何时用 spec/flat-ip-sheet" | 直接用 face-lock | -4 判断 |
| 活跃 spec 引用 | 8 处 | 0 处 | -100% |

### 🎯 预期收益

**可维护性提升**：
- 资产冗余减少，单一真相来源更清晰
- Agent 不再困惑"spec vs face-lock 哪个优先"
- 文档引用链路缩短

**生成成功率提升**：
- 年龄范围放宽，减少"38 岁精确匹配"失败
- 模型有更大的容忍空间（35-40 岁）
- 保留核心约束（禁止幼态/显老）

**Agent 体验改善**：
- 传图决策更简单：panorama + face-lock（多场景）
- 无需判断"是否需要 spec 补强"
- 返修流程统一：直接对照 face-lock

### 🔍 验证结果

```bash
✓ scripts/validate-skill-local.sh 通过
✓ 核心入口文件完整
✓ 资产 PNG 存在（包括待废弃的 spec.png 文件保留）
✓ Eval 用例 27 条通过
✓ 触发词一致性检查通过
✓ 小石头颜色统一 #f39800
```

**剩余"38岁"引用**：12 处，均为非核心位置
- 历史文档注释
- 示例说明（"约 38 岁"作为参考）
- 不影响核心生成逻辑

### 📝 文档变更摘要

| 文件 | 变更类型 | 关键修改 |
|------|----------|----------|
| `persona-author-assets.md` | 重构 | 资产清单 11→5，标注废弃资产 |
| `persona-author-identity.md` | 更新 | 年龄锁改为范围，删除 spec 引用 |
| `persona-author-prompts.md` | 更新 | 年龄 prompt 改范围，返修用 face-lock |
| `persona-quick-checklist.md` | 更新 | 传图协议简化，年龄锁范围化 |
| `QUICK-START.md` | 更新 | 决策表加 face-lock 说明 |
| `common-generation-templates.md` | 更新 | 删除 spec 引用 |
| `common-qa-repair.md` | 更新 | 删除 spec 引用 |
| `physical-qa-checklist.md` | 更新 | spec→face-lock，年龄改范围 |
| `persona-author.md` | 更新 | 资产清单编号调整 |

### ⚠️ 注意事项

1. **废弃资产文件仍保留**：spec.png 等文件未删除，仅标记废弃
2. **向后兼容**：已生成的图不受影响，新图使用新规则
3. **需要同步更新**：如有其他 profile，需同步应用相同优化原则
