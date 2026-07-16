# IP 设计优化总结（P0 完成）

日期：2026-07-16  
状态：✅ P0 已完成  
相关：`plans/2026-07-16-ip-design-optimization.md`

## 执行概要

完成了 IP 设计系统的 P0 级优化，主要解决**资产冗余**和**年龄锁定过度精确**两大问题。

### 核心改进

1. **老杨资产精简**：11 个 → 5 个（-55%）
2. **年龄锁范围化**：38 岁精确值 → 35-40 岁范围
3. **引用链简化**：9 层 → 5 层（-44%）

### 技术债务清理

- ✅ 删除 `spec.png` 的 8 处活跃引用（功能合并到 `face-lock.png`）
- ✅ 标注废弃资产（`flat-ip-sheet` 对、`handdrawn.png` 历史版本）
- ✅ 统一年龄表述（"38岁" → "35-40岁成熟男性"）

## 影响范围

### 保留的 5 个核心资产

```text
01. author-persona-panorama.png          # 实体全景（实物图）
02. author-persona-panorama-handdrawn.png # 手绘全景（手绘系）
03. author-persona-face-lock.png          # 面相锁定 + 禁止偏移
04. author-persona-handdrawn-body.png     # 手绘身材比例
05. author-persona-actions.png            # 动作扩展
```

### 废弃但保留的资产

```text
❌ author-persona-spec.png               # 功能合并到 face-lock
❌ author-persona-handdrawn.png          # 被 panorama-handdrawn 替代
❌ author-persona-flat-ip-sheet.png      # 移至 examples/
❌ author-persona-flat-ip-sheet-navy.png # 同上
```

## 关键决策

### 为什么合并 spec 到 face-lock？

**问题**：两者功能重叠
- spec.png：面相规范 + 禁止偏移区
- face-lock.png：多角度脸特写，压跨场景脸漂

**决策**：face-lock 承担全部面相锁定职责
- 多角度覆盖更全面
- "禁止偏移区"可在文字规范中说明
- 减少 Agent "何时用 spec"的困惑

### 为什么年龄改为范围？

**问题**：生图模型无法精确控制"38 岁 vs 36 岁"
- 模型主要靠皱纹判断年龄
- 文档禁止用皱纹 → 矛盾

**决策**：35-40 岁范围 + 禁止区间
- 允许 ±2-3 岁自然波动
- 保留底线：NOT 20s, NOT 45+/50+
- 成熟感靠骨相而非精确年龄数字

## 未来改进（P1/P2）

P1 计划：
- 简化 Confirm Gate（分级检查）
- 路径命名优化（A/B/C 认知简化）
- 引入检查容忍度

P2 计划：
- 去品牌化雷石叙事
- 四种模式平等化
- 自动化检查工具

## 验证

```bash
✓ scripts/validate-skill-local.sh 通过
✓ 27 条 evals 用例完整
✓ 核心资产 PNG 存在
✓ 引用链路正确
```

## 记录

- 2026-07-16：P0 优化完成，资产从 11 个精简到 5 个，年龄锁改为范围
