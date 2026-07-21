# Codex 环境检测与引导

> **核心约束**：本 Skill 面向 Codex 环境设计，生图**必须**使用 Codex 自带的 `imagen` 工具。

## 一、环境检测（任务开始前）

### 1.1 Codex 环境确认

执行任务前，Agent 必须确认运行环境：

```text
✓ 正确环境：Codex CLI / Codex Desktop / claude.ai/code
✗ 错误环境：claude.ai 普通对话 / API 直接调用 / 第三方集成
```

**检测方法**：

- Codex 环境会提供 `imagen` 工具（图片生成）
- Codex 环境会提供 `Read`、`Write`、`Bash` 等文件操作工具
- 如果用户在非 Codex 环境提及本 Skill，应引导切换环境

**引导话术**：

```text
这个 Skill 需要在 Codex 环境中运行，因为：
1. 生图必须使用 Codex 自带的 imagen 工具
2. 需要读取本地 IP profile 资产文件
3. 需要保存生成的图片到项目目录

请在以下环境之一使用：
- Codex CLI（终端命令行）
- Codex Desktop（桌面应用）
- claude.ai/code（Web 版 Codex）

当前建议：在您的项目目录下启动 Codex，然后说「老杨：这篇内容想配图」。
```

### 1.2 imagen 工具可用性检查

**硬性要求**：

- 本 Skill 的所有图片生成（实物图、手绘图、知识卡、PPT、视频场景）**必须**通过 Codex 的 `imagen` 工具完成
- 不得使用外部 API（DALL-E、Midjourney、Stable Diffusion 等）
- 不得要求用户自行生成图片后上传

**检测时机**：

```text
准备生成图片前 → 确认 imagen 工具存在 → 调用 imagen
如果 imagen 不可用 → 停止任务 → 引导用户检查环境
```

**失败引导**：

```text
无法找到 imagen 工具。请确认：
1. 您在 Codex 环境中（不是普通 claude.ai）
2. Codex 版本支持 imagen 工具（需 Codex 最新版本）
3. 如果在 Codex CLI，尝试运行 `codex --version` 确认版本

如果问题持续，请访问 claude.ai/code 或更新 Codex Desktop。
```

### 1.3 本地资产路径检测

本 Skill 依赖本地文件系统的 IP profile 资产：

**必需路径**（以 `scene-skill-core/` 为根目录）：

```text
ip-profiles/default-little-stone/
├── character.md
├── profile.md
├── assets/
│   ├── character/
│   │   └── primary-character-reference.png
│   └── persona/
│       ├── author-persona-panorama.png
│       └── author-persona-panorama-handdrawn.png
```

**检测方法**：

```bash
# Agent 在首次执行任务时，读取关键文件确认路径
Read scene-skill-core/ip-profiles/default-little-stone/character.md
Read scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png
```

**失败引导**：

```text
无法找到 IP profile 资产文件。请确认：
1. 您在 xiaoshitou-scenes 项目根目录或其子目录中
2. scene-skill-core/ 目录已正确安装
3. 运行以下命令检查：
   ls scene-skill-core/ip-profiles/default-little-stone/assets/character/

如果文件缺失，请重新克隆仓库或检查 .gitignore。
```

## 二、imagen 工具使用规范

### 2.1 工具调用格式

**标准调用**（单张图片）：

```python
# 伪代码示例（实际调用取决于 Codex 工具接口）
imagen(
    prompt="16:9, 纯白背景 #FFFFFF, ...",
    aspect_ratio="16:9",  # 或 "3:4", "4:5", "9:16"
    reference_images=[
        "scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png"
    ]
)
```

**双参考调用**（老杨出镜）：

```python
imagen(
    prompt="16:9, 纯白背景 #FFFFFF, ...",
    aspect_ratio="16:9",
    reference_images=[
        "scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png",
        "scene-skill-core/ip-profiles/default-little-stone/assets/persona/author-persona-panorama.png"
    ]
)
```

### 2.2 提示词组装规范

**槽位顺序**（见 `common-prompt-slots.md`）：

```text
1. 模式声明（16:9 实物图 / 16:9 手绘图 / 3:4 知识卡 / ...）
2. 背景约束（纯白背景 #FFFFFF / ...）
3. 内容描述（真实物件小现场 / 黑色手绘线稿结构 / ...）
4. 角色锁定（小石头：flat 2D 平涂胶囊体 / ...）
5. 参考图说明（Reference: [文件路径] / ...）
6. 负面约束（禁止：粗黑框眼镜、黑长袖、generic 人脸 / ...）
```

**中英文混合策略**：

- 主体描述、标签、批注：优先中文
- 视觉风格关键词：保留英文（flat 2D、soft shadow、white studio surface）
- 技术参数：英文（16:9、#FFFFFF、1080×1440）
- 负面约束：英文短语（NEVER stick-figure、NOT pure black-and-white）

### 2.3 参考图传递机制

**路径解析规则**：

```text
相对路径（推荐）：
  scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png

绝对路径（备选）：
  /Users/.../xiaoshitou-scenes/scene-skill-core/ip-profiles/default-little-stone/assets/character/primary-character-reference.png

imagen 工具要求：
  - 文件必须存在且可读
  - 文件必须是图片格式（PNG / JPG）
  - 文件大小不超过 10MB（通常 < 2MB）
```

**失败处理**：

```text
如果 imagen 报错「参考图无法读取」：
1. 检查文件路径是否正确（使用 Read 工具验证）
2. 检查文件是否存在（使用 Bash ls 验证）
3. 尝试使用绝对路径
4. 确认文件格式是否正确（PNG 优先）
```

## 三、模式与工具的映射

### 3.1 实物图模式 → imagen

```text
触发词：实物图 / 实物场景 / 物件小现场 / 小石头实物图
工具：imagen（必须）
尺寸：16:9
参考图：
  - 小石头单 IP：primary-character-reference.png（单锚点）
  - 老杨出镜：+ author-persona-panorama.png（双参考）
提示词模板：references/common-generation-templates.md § 实物图
QA 检查：references/physical-qa-checklist.md
```

### 3.2 手绘图模式 → imagen

```text
触发词：手绘图 / 手绘解释 / 白板图 / 逻辑图
工具：imagen（必须）
尺寸：16:9
参考图：
  - 小石头单 IP：primary-character-reference.png（单锚点）
  - 老杨出镜：+ author-persona-panorama-handdrawn.png + author-persona-panorama.png（双参考，手绘优先）
提示词模板：references/common-generation-templates.md § 手绘图
QA 检查：references/handdrawn-qa-checklist.md
```

### 3.3 知识卡模式 → imagen

```text
触发词：知识卡 / 图文号知识卡 / 手机海报 / 竖版传播图
工具：imagen（必须）
尺寸：3:4 / 4:5 / 9:16（按内容选择）
参考图：同手绘图模式
提示词模板：references/knowledge-card-mode.md § Prompt 组装
QA 检查：references/knowledge-card-mode.md § QA
```

### 3.4 PPT 演讲模式 → imagen（批量）

```text
触发词：PPT / 课件 / 直播分享页 / 主题演讲 / 整套演讲页面
工具：imagen（必须，逐页生成）
尺寸：16:9
参考图：同手绘图模式
工作流：
  1. 导演规划卡（不调用 imagen）
  2. 样张确认（调用 imagen 生成 1-2 页）
  3. 批量生成（调用 imagen 逐页生成，每页独立提示词）
提示词模板：references/ppt-presentation-mode.md § page card
QA 检查：references/ppt-presentation-mode.md § QA
```

### 3.5 视频模式 → imagen（批量场景）

```text
触发词：视频讲解 / 动画视频 / 手绘视频 / 配音视频
工具组合：
  - imagen（必须，生成场景插图）
  - Fish Audio / ElevenLabs（TTS，可选）
  - Remotion（视频渲染，本地）
尺寸：1080×1440（竖版，9:16 比例）
参考图：同实物图/手绘图模式
工作流：
  1. 生成 plan.json（不调用 imagen）
  2. 为每个场景调用 imagen 生成插图（6-9 张）
  3. 生成旁白音频（Fish Audio / ElevenLabs）
  4. Remotion 渲染视频（本地）
提示词模板：references/video-mode.md § 图片生成约束
QA 检查：references/video-mode.md § QA 检查清单
```

### 3.6 自定义 IP 录入 → imagen（校准阶段）

```text
触发词：录入 IP / 新建 IP / 用这套形象 / 创建角色档案
工具：imagen（仅在 CANONICAL_ASSET 和 MODE_CALIBRATION 阶段使用）
状态机：
  REQUESTED → USER_REFERENCE（不调用 imagen）
  → IDENTITY_PLAN（不调用 imagen）
  → CONFIRMED → CANONICAL_ASSET（可能调用 imagen 生成 identity_sheet）
  → MODE_CALIBRATION（调用 imagen 生成校准图）
  → AVAILABLE
参考图：用户提供的 Logo / Icon / 立绘
提示词模板：references/brand-mark-mode.md § Prompt 片段
QA 检查：references/brand-mark-mode.md § QA
```

## 四、失败恢复与引导

### 4.1 imagen 调用失败

**常见错误**：

| 错误信息 | 原因 | 解决方案 |
|---------|------|----------|
| "Tool not found: imagen" | 不在 Codex 环境 | 引导用户切换到 Codex |
| "Reference image not found" | 文件路径错误 | 检查路径，使用 Read 验证 |
| "Invalid aspect ratio" | 尺寸参数错误 | 检查模式对应的尺寸（16:9 / 3:4 / 9:16） |
| "Prompt too long" | 提示词超长 | 压缩提示词，移除冗余描述 |
| "Generation failed" | 内容违规或技术故障 | 调整提示词，避免敏感内容 |

**通用恢复流程**：

```text
1. 记录错误信息
2. 检查环境和参数
3. 调整后重试（最多 2 次）
4. 如果仍失败，向用户报告并暂停任务
5. 不要无限重试或静默失败
```

### 4.2 用户尝试使用外部工具

**场景**：用户说"我用 Midjourney 生了图，怎么套用你们的风格"

**引导话术**：

```text
本 Skill 要求使用 Codex 自带的 imagen 工具生成图片，原因：

1. **IP 一致性**：imagen 可以传入小石头/老杨的参考图，确保形象稳定
2. **质量控制**：生成后会自动做 Confirm Gate 检查（四肢、眼睛、维度锁）
3. **工作流完整性**：从内容理解 → 结构锁定 → 生成 → QA 是一体化的

如果您已有图片，可以：
- 作为内容参考（描述「像这张图的构图」）
- 作为自定义 IP 的参考图（录入新 IP profile）

但不能：
- 跳过 imagen 直接交付外部生成的图
- 用外部工具替代本 Skill 的生图环节
```

### 4.3 用户要求导出提示词自己生成

**场景**：用户说"先别生成，给我提示词我自己去 DALL-E 生成"

**引导话术**：

```text
理解您想先看提示词。我可以输出提示词供您参考，但需要说明：

1. **本 Skill 的提示词是为 Codex imagen 优化的**，在其他平台可能效果不同
2. **参考图机制**：imagen 可以传入小石头/老杨的参考图文件，其他平台可能不支持
3. **QA 流程**：即使用其他工具生成，也无法自动做 Confirm Gate 检查

建议工作流：
- 我先用 imagen 生成候选图 → 您查看效果 → 确认或返修
- 如果您想完全自主生成，可以把提示词作为参考，但这不是本 Skill 的标准流程

您希望我继续用 imagen 生成，还是仅输出提示词供参考？
```

### 4.4 视频模式的特殊处理

**视频模式依赖更多工具**：

```text
必需：
- imagen（生成场景插图，6-9 张）
- Read / Write / Bash（文件操作）

可选（用户环境配置）：
- Fish Audio API key（TTS 旁白）
- Node.js 18+（Remotion 渲染）
- FFmpeg（音视频处理）
```

**环境检测时机**：

```text
用户触发视频模式 → 检测必需工具（imagen）→ 检测可选工具 → 给出清单

如果 TTS / Node.js / FFmpeg 缺失：
  选项 A：仅生成场景插图 + plan.json，用户自行配置后渲染
  选项 B：引导用户安装依赖后继续
  选项 C：降级为静态图片模式（实物图/手绘图）
```

**引导话术**：

```text
视频模式需要额外环境配置：

✓ 已就绪：imagen 工具（生成场景插图）
? 待确认：
  - Fish Audio API key（生成旁白）
  - Node.js 18+（渲染视频）
  - FFmpeg（音视频处理）

建议：
1. 我先生成场景插图和脚本（plan.json）
2. 您配置环境后，运行脚本完成视频渲染

或者，如果暂不需要视频，我可以：
- 生成静态实物图/手绘图（6-9 张）
- 生成知识卡（竖版，适合传播）

您希望继续视频模式，还是改用静态图片？
```

## 五、用户教育与最佳实践

### 5.1 首次使用引导

**用户第一次调用 Skill 时**，输出简短引导：

```text
欢迎使用 scene-skill-core！

快速开始：
- 双 IP（推荐）：老杨：这篇内容想配图 <粘贴内容>
- 单 IP：小石头实物图：为这篇内容出 4 张 16:9 配图

本 Skill 在 Codex 环境运行，会自动：
1. 使用 imagen 工具生成图片（传入小石头/老杨参考图）
2. 做 Confirm Gate 检查（确保形象一致）
3. 保存到 assets/ 目录

您可以直接粘贴内容，我会推荐配图方案。
```

### 5.2 常见误解纠正

| 误解 | 纠正 |
|------|------|
| "能不能用 Midjourney 更好看" | imagen 是唯一选项，因为需要传入 IP 参考图 |
| "我自己生成图你帮我排版" | 本 Skill 是端到端的（内容 → 图片 → QA），不支持外部图片接入 |
| "为什么不用最新的 DALL-E 4" | Codex imagen 已集成最新模型，且支持参考图机制 |
| "能不能导出提示词去别的平台" | 可以，但效果无法保证，且缺少 Confirm Gate |
| "视频模式能不能用 Sora" | 当前视频模式是静态场景 + TTS + Remotion，不是 AI 视频生成 |

### 5.3 高级用户提示

**对于熟悉 Codex 的用户**：

```text
进阶技巧：

1. **自定义 IP**：
   - 提供 Logo/Icon → 录入自定义 IP → 复用四种模式
   - 参考：examples/custom-ip-delivery.md

2. **批量生成**：
   - PPT 模式：导演规划卡 → 样张 → 批量（10-20 页）
   - 视频模式：plan.json → 场景插图（6-9 张）→ 渲染

3. **返修优化**：
   - 收到图后说「减少标签」「调整留白」「重生成第 3 张」
   - 参考：references/common-qa-repair.md

4. **本地资产复用**：
   - 把私有 Logo 放到 ip-profiles/<your-ip>/assets/brand-private/
   - 引用时会自动读取

5. **Evals 测试**：
   - 运行 scene-skill-core/evals/evals.json 验证路由和 QA
```

## 六、架构透明化

### 6.1 用户视角的工具链

```text
用户输入
  ↓
scene-skill-core（Codex Skill）
  ↓
内容理解 + 模式路由（SKILL.md / QUICK-START.md）
  ↓
结构锁定（母版 / 结构类型）
  ↓
【关键节点】调用 Codex imagen 工具
  - 传入：提示词 + 参考图（小石头/老杨）
  - 返回：PNG 图片
  ↓
Confirm Gate + 模式 QA
  ↓
保存到 assets/ + 交付
```

### 6.2 与外部平台的边界

| 平台 | 本 Skill 是否支持 | 原因 |
|------|------------------|------|
| Codex imagen | ✅ 唯一生图工具 | 支持参考图 + 面向 Codex 优化 |
| DALL-E / GPT-4V | ❌ 不支持 | 无法传入本地参考图文件 |
| Midjourney | ❌ 不支持 | 非 Codex 工具，无法自动化调用 |
| Stable Diffusion | ❌ 不支持 | 需要本地部署，脱离 Codex 环境 |
| Fish Audio | ✅ 视频模式可选 | TTS 旁白，用户需配置 API key |
| Remotion | ✅ 视频模式本地 | 开源视频渲染，本地运行 |

### 6.3 开放性说明

**本 Skill 不是黑盒**：

```text
所有规则文件都在 scene-skill-core/references/ 可读：
- 模式规则：physical-*.md / handdrawn-*.md / knowledge-card-mode.md / ppt-presentation-mode.md
- 提示词槽位：common-prompt-slots.md
- QA 检查：*-qa-checklist.md
- 交接协议：contracts/*.md

用户可以：
- 查看任何规则文件（Read 工具）
- 修改 IP profile（创建自定义 IP）
- 导出提示词（用于学习或参考）
- Fork 仓库自定义规则

但生图环节必须使用 Codex imagen，这是架构硬性约束。
```

## 七、检查清单（Agent 执行前）

**每次任务开始前，Agent 应快速确认**：

- [ ] 运行环境是 Codex（有 imagen、Read、Write、Bash 工具）
- [ ] 当前目录在 xiaoshitou-scenes 或其子目录
- [ ] 可以读取 scene-skill-core/ip-profiles/default-little-stone/character.md
- [ ] 可以读取小石头参考图 primary-character-reference.png
- [ ] 如果触发老杨，可以读取 author-persona-panorama*.png
- [ ] 如果是自定义 IP，目标 profile 的资产文件存在

**如果任何一项失败**：

```text
停止任务 → 输出清晰的错误信息和解决方案 → 等待用户修复
不要：静默失败、猜测路径、用占位符跳过
```

## 八、总结

**核心原则**：

1. **imagen 是唯一生图工具** — 不提供替代方案，不妥协
2. **环境检测前置** — 在生成前确认，不在生成后报错
3. **引导清晰友好** — 告诉用户为什么、怎么做，不只说"不行"
4. **失败快速明确** — 出错时立即停止，给出具体原因和步骤

**用户体验目标**：

```text
✓ 用户在 Codex 中直接说需求 → 自动生成 → 交付
✓ 用户不在 Codex → 友好引导切换环境
✓ 用户尝试外部工具 → 解释原因 + 提供正确路径
✓ 环境缺失依赖 → 给出清单 + 可选降级方案
```

---

**相关文件**：

- `SKILL.md` — 主工作流
- `QUICK-START.md` — 快速决策表
- `common-prompt-slots.md` — 提示词槽位组装（imagen 专用）
- `contracts/profile-contract.md` — IP 录入状态机
- `video-mode.md` — 视频模式（imagen + TTS + Remotion）
- `brand-mark-mode.md` — 自定义 IP（imagen 用于校准）
