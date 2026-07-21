# Codex 环境与 imagen 工具 - 实战经验与踩坑指南

> **关键发现**：本文档记录了 Codex 环境检测和 imagen 工具使用的实战经验，包括常见陷阱和解决方案。

---

## 一、核心发现

### 1.1 当前会话 vs 新会话

**关键踩坑**：

```text
❌ 错误认知：修改 SKILL.md 的 allowed-tools 后，当前会话立即获得新工具
✅ 正确理解：会话启动时工具列表已固定，需要启动新会话才能加载更新后的配置
```

**实战经验**：

当我们在当前会话中修改了 `SKILL.md` 添加 `imagen` 到 `allowed-tools`：

```yaml
# SKILL.md
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - imagen  # ← 新添加
```

在**当前会话**中，我们仍然无法直接调用 imagen 工具，因为：
1. 会话启动时的工具列表已经固定
2. 运行时不会重新读取 SKILL.md 的配置
3. 工具权限在会话初始化时确定

**解决方案**：

使用 `codex exec` 启动**新的子会话**：

```bash
codex exec "小石头实物图：环境检测通过"
```

这会：
- 启动一个新的 Codex 会话
- 重新读取 SKILL.md 配置
- 加载包含 imagen 的工具列表
- 执行完任务后退出

### 1.2 环境检测的正确时机

**关键发现**：

环境检测应该在 **Skill 加载后、生成前** 自动执行，而不是：
- ❌ 在用户提示之前手动检测
- ❌ 在生成失败后才发现环境问题
- ❌ 让用户自己检查环境

**实现方式**：

我们在 `QUICK-START.md § -1` 中定义了环境检测清单，Skill 加载时会自动读取并执行：

```markdown
## -1. 环境检测（首次任务必做）

执行任务前确认：
- [ ] 运行环境是 Codex（有 imagen、Read、Write、Bash 工具）
- [ ] 当前目录在 xiaoshitou-scenes 或其子目录
- [ ] 可以读取 character.md
- [ ] 可以读取参考图 primary-character-reference.png
```

**实战验证**（codex exec 日志）：

```text
codex
我将使用 `scene-skill-core`，先按它的 QUICK-START 做环境检测...
exec
/bin/zsh -lc "sed -n '1,240p' /Users/.../SKILL.md && ..."
```

Agent 自动：
1. 读取 QUICK-START.md
2. 执行环境检测清单
3. 确认工具和资产可用
4. 才开始生成

---

## 二、codex exec 实战技巧

### 2.1 基本用法

**命令格式**：

```bash
codex exec [OPTIONS] [PROMPT]
```

**常用选项**：

```bash
# 使用默认模型（推荐）
codex exec "小石头实物图：<内容>"

# 指定模型（注意权限）
codex exec -m opus "小石头实物图：<内容>"  # ⚠️ 需要 ChatGPT Plus 账号

# 从文件读取提示词
codex exec "$(cat prompt.txt)"

# 附带图片
codex exec -i reference.png "用这个风格生成配图"
```

### 2.2 实战案例：环境检测场景

**提示词文件** (`/tmp/generate_test_image.txt`)：

```text
使用 scene-skill-core Skill 生成一张测试图：

小石头实物图：环境检测通过，逐项打勾

具体场景：
- 一个白色剪贴板，上面夹着检查清单
- 清单上有 4 个复选框：
  1. ✓ Codex 环境
  2. ✓ imagen 工具
  3. ✓ 资产文件
  4. ✓ 开始生图（正在打勾）
- 小石头拿着笔，正在第 4 个复选框上画勾
- 16:9 横版，纯白背景，真实物件小现场

请按照 scene-skill-core 的标准流程：
1. 执行环境检测（QUICK-START.md § -1）
2. 读取 character.md 和参考图
3. 选择母版类型并锁定
4. 使用 imagen 工具生成图片
5. 执行 Confirm Gate 检查
6. 保存到 assets/ 目录
```

**执行命令**：

```bash
codex exec "$(cat /tmp/generate_test_image.txt)"
```

**输出结果**：

```text
✅ 环境检测通过
✅ Skill 自动加载
✅ 读取参考图成功
✅ 母版锁定：04-review-rework（变异为检查清单）
✅ imagen 生成成功：1672 × 941
✅ Confirm Gate: CONFIRMED
✅ 保存到：assets/little-stone-environment-check-passed.png

Token 使用: 118,479
执行时间: ~2 分钟
```

### 2.3 常见错误和解决

#### 错误 1: 模型不支持

```text
ERROR: The 'opus' model is not supported when using Codex with a ChatGPT account.
```

**原因**：使用的账号类型不支持指定的模型

**解决**：
```bash
# 不指定模型，使用默认模型
codex exec "小石头实物图：<内容>"
```

#### 错误 2: Skill 未加载

```text
ERROR: Unknown skill: scene-skill-core
```

**原因**：Skill 未正确安装或路径不对

**解决**：
```bash
# 检查 Skill 安装
ls ~/.codex/skills/scene-skill-core/

# 重新安装
cp -R ./scene-skill-core ~/.codex/skills/
```

#### 错误 3: 参考图找不到

```text
ERROR: Reference image not found
```

**原因**：相对路径解析错误或文件不存在

**解决**：
```bash
# 确认当前目录
pwd  # 应该在 xiaoshitou-scenes

# 确认参考图存在
ls scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png

# 使用绝对路径（备选）
/Users/.../xiaoshitou-scenes/scene-skill-core/...
```

---

## 三、环境检测最佳实践

### 3.1 检测清单（4 项核心）

**必须检测的项目**：

```text
1. Codex 环境
   - 确认有 imagen 工具
   - 确认有 Read/Write/Bash 工具
   - 确认工作目录正确

2. IP 资产文件
   - character.md 可读
   - 参考图 PNG 存在
   - 文件大小正常（非空）

3. 模式文档
   - 根据任务类型读取对应文档
   - 实物图 → physical-*
   - 手绘图 → handdrawn-*
   - 知识卡 → knowledge-card-mode.md
   - 视频 → video-mode.md

4. 权限和路径
   - 可以写入 assets/ 目录
   - 可以执行 bash 命令
   - 相对路径解析正确
```

### 3.2 检测失败的处理

**原则**：停止任务 → 明确错误 → 提供解决方案

**示例**：

```text
❌ 检测失败：imagen 工具不可用

原因：当前会话启动时未加载 imagen 工具

解决方案：
1. 使用 codex exec 启动新会话：
   codex exec "小石头实物图：<内容>"

2. 或者在新的交互式会话中使用：
   cd ~/Documents/github/xiaoshitou-scenes
   codex
   > 小石头实物图：<内容>

3. 如果问题持续，检查 SKILL.md 的 allowed-tools 配置
```

### 3.3 自动化检测脚本

**检测脚本示例**：

```bash
#!/bin/bash
# scene-skill-core 环境检测脚本

echo "=== 环境检测 ==="

# 检查 1: 当前目录
if [[ $(pwd) == *"xiaoshitou-scenes"* ]]; then
  echo "✓ 当前目录正确"
else
  echo "✗ 当前目录不正确，请 cd 到 xiaoshitou-scenes"
  exit 1
fi

# 检查 2: character.md
if [ -f "scene-skill-core/ip-profiles/default-little-stone/character.md" ]; then
  echo "✓ character.md 存在"
else
  echo "✗ character.md 不存在"
  exit 1
fi

# 检查 3: 参考图
if [ -f "scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png" ]; then
  size=$(stat -f%z "scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png")
  echo "✓ 参考图存在 ($size bytes)"
else
  echo "✗ 参考图不存在"
  exit 1
fi

# 检查 4: codex 命令
if command -v codex &> /dev/null; then
  echo "✓ codex 命令可用"
else
  echo "✗ codex 命令不可用，请安装 Codex CLI"
  exit 1
fi

echo "=== 环境检测通过 ==="
```

---

## 四、imagen 工具使用经验

### 4.1 参考图传递机制

**关键发现**：

imagen 工具支持传入本地参考图文件，这是保证 IP 形象一致性的核心机制。

**传递方式**（Codex 内部）：

```python
# 伪代码示例
imagen(
    prompt="16:9, 纯白背景 #FFFFFF, ...",
    aspect_ratio="16:9",
    reference_images=[
        "scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png"
    ]
)
```

**路径解析**：

- ✅ 相对路径（推荐）：从当前工作目录解析
- ✅ 绝对路径（备选）：完整路径，跨目录使用
- ❌ 不支持：URL、网络路径、base64 编码

**实战验证**：

```text
codex exec 日志：
codex
参考图已读取：小石头是橙色平涂竖胶囊、两只白圆眼、
细黑线四肢、无嘴；母版参考确认其核心是"主角色正在做验收动作"
```

参考图成功传入并生效，生成的图片中小石头形象与参考图一致。

### 4.2 提示词组装实战

**槽位顺序**（经过验证的最佳实践）：

```text
1. 模式声明（16:9 / 3:4 / 9:16）
2. 背景约束（#FFFFFF 纯白）
3. 主物件描述（真实物件）
4. 角色描述（小石头 IP）
5. 动作描述（核心动作）
6. 标签描述（短中文）
7. 负面约束（禁止项）
```

**实际生成的提示词**（codex exec 中自动组装）：

```text
16:9 横版，纯白背景 #FFFFFF，白色摄影棚表面，真实物件小现场。

主物件：白色剪贴板（clipboard），夹着一张白纸，纸上有 4 个复选框，
前 3 个已打绿色勾，第 4 个正在被打勾。

角色：小石头 - flat 2D #f39800 橙色平涂胶囊体，两只白色圆眼（无瞳孔），
无嘴，两条细黑线臂、两条细黑线腿。

动作：小石头站在剪贴板左侧，右臂握着一支简笔黑色笔，正在第 4 个复选框上画绿色勾。

标签：Codex 环境、imagen 工具、资产文件、开始生图

禁止：粗黑框眼镜、黑长袖、generic 人脸、3D 渲染、商业插画
```

### 4.3 Confirm Gate 验证

**自动执行**：

```text
codex
候选图已生成，视觉检查通过：
- 白色剪贴板与金属夹是真实物件 ✓
- 四行清单文字可读 ✓
- 第 4 项"开始生图"由笔尖正在完成绿色勾 ✓
- 小石头保持橙色平涂、白圆眼、两臂两腿、无嘴 ✓
- 背景纯白且留白充足 ✓

现在执行 Confirm Gate，并复制到项目 `assets/`。
```

**检查项**（自动）：

- L1 计数：恰好 2 臂 + 2 腿
- L2 锚点：臂从体侧上 1/3、腿从底缘连续向下
- E1 眼睛：两只白圆眼、批内一致
- 维度锁：flat 2D 平涂，禁止 3D 渲染

**结论**：

```text
Confirm Gate: CONFIRMED ✓
```

---

## 五、性能优化经验

### 5.1 Token 使用优化

**实测数据**：

- 单张实物图生成：118,479 tokens
- 执行时间：~2 分钟
- 图片大小：1.3 MB (1672×941)

**优化建议**：

1. **按需加载文档**：不要一次性读取所有 references/
2. **使用 QUICK-START**：5 秒决策表，快速定位必读文件
3. **缓存参考图**：同批次生成复用已读取的参考图
4. **简化提示词**：保留核心描述，移除冗余解释

### 5.2 批量生成优化

**场景**：生成多张图片时

**策略**：

```bash
# 方式 1: 单次调用生成多张（推荐）
codex exec "小石头实物图：为这篇文章生成 4 张配图
<粘贴内容>"

# 方式 2: 循环调用（Token 消耗大）
for i in {1..4}; do
  codex exec "小石头实物图：第 $i 张"
done
```

**原因**：
- 方式 1：一次会话，环境检测只执行一次，参考图只读取一次
- 方式 2：每次都是新会话，重复环境检测和资产读取

---

## 六、常见场景与模板

### 6.1 实物图生成

**模板**：

```bash
codex exec "小石头实物图：<场景描述>

具体要求：
- 一个<真实物件>
- 小石头正在<动作>
- 标签：<2-4 个短词>
- 16:9 横版，纯白背景"
```

**示例**：

```bash
codex exec "小石头实物图：用户反馈太多，团队处理不过来

具体要求：
- 一堆便利贴
- 小石头正在整理分类
- 标签：用户反馈、优先级、待处理
- 16:9 横版，纯白背景"
```

### 6.2 双 IP 模式

**模板**：

```bash
codex exec "老杨：这篇关于<主题>的文章想配图

<粘贴内容>

请先推荐配图方案（模式、张数、互动场景类型）"
```

**示例**：

```bash
codex exec "老杨：这篇关于目标管理的文章想配图

<粘贴内容>

请先推荐配图方案"
```

### 6.3 视频模式

**模板**：

```bash
codex exec "小石头视频：<主题>

时长：60-90 秒
风格：<实物图/手绘图>
场景数：6-9 个"
```

**示例**：

```bash
codex exec "小石头视频：为什么环境检测很重要

时长：60 秒
风格：实物图
场景数：6 个"
```

---

## 七、踩坑总结

### 7.1 关键踩坑

| 踩坑 | 错误做法 | 正确做法 |
|------|---------|---------|
| 工具加载 | 修改 SKILL.md 后期望当前会话立即获得 imagen | 使用 codex exec 启动新会话 |
| 环境检测 | 生成失败后才发现环境问题 | 任务开始前自动执行环境检测 |
| 参考图路径 | 使用绝对路径或 URL | 使用相对路径（从工作目录） |
| 批量生成 | 循环调用 codex exec | 单次调用生成多张 |
| 模型选择 | 强制指定 opus | 使用默认模型（根据账号） |

### 7.2 最佳实践清单

**启动前**：
- [ ] 确认在项目根目录（xiaoshitou-scenes）
- [ ] 确认 SKILL.md 的 allowed-tools 包含 imagen
- [ ] 确认参考图文件存在且可读

**执行时**：
- [ ] 使用 codex exec 启动新会话
- [ ] 让 Skill 自动执行环境检测
- [ ] 按标准流程（QUICK-START）加载必读文件
- [ ] 传入参考图保证形象一致性

**验证后**：
- [ ] 检查 Confirm Gate 结果（CONFIRMED）
- [ ] 验证图片文件存在且尺寸正确
- [ ] 确认保存路径符合规范
- [ ] 必要时提交到 Git

---

## 八、文档索引

### 核心文档
- `codex-environment-guidance.md` - 完整环境检测指南（17 KB）
- `QUICK-START.md § -1` - 环境检测清单（4 项）
- `SUCCESS-REPORT.md` - 实战验证报告

### 模式文档
- `video-mode.md` - 视频模式 + imagen
- `brand-mark-mode.md` - 自定义 IP + imagen

### 实战案例
- `assets/little-stone-environment-check-passed.png` - 测试图片
- `/tmp/codex_exec_output2.log` - 完整执行日志（178 KB）

---

## 九、总结

### 9.1 核心收获

1. **codex exec 是关键** - 启动新会话才能加载更新后的配置
2. **环境检测前置** - 在生成前自动确认，不在失败后补救
3. **参考图机制有效** - imagen 成功传入并保证形象一致性
4. **Confirm Gate 自动化** - 不合格图片不交付

### 9.2 适用场景

- ✅ 配置更新后需要测试新工具
- ✅ 需要隔离的生图任务（不影响当前会话）
- ✅ 批量生成多张图片
- ✅ 自动化脚本中调用生图

### 9.3 注意事项

- ⚠️ codex exec 是新会话，不会保留当前会话的上下文
- ⚠️ 每次调用都有 token 消耗，建议合并多张图到一次调用
- ⚠️ 参考图必须存在且可读，否则生成会失败
- ⚠️ 不同账号类型支持的模型不同，建议使用默认模型

---

**更新时间**: 2026-07-21  
**验证状态**: ✅ 已通过实战验证  
**测试图片**: `assets/little-stone-environment-check-passed.png`
