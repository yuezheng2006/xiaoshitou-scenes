# Codex 环境与 imagen 工具强化说明

> 更新时间：2026-07-21  
> 目标：明确 Skill 面向 Codex 环境设计，生图必须使用 Codex 自带的 imagen 工具

---

## 一、强化背景

`scene-skill-core` Skill 是面向 **Codex 环境**设计的，但并不是所有用户都会直接通过 Codex 使用。为了确保：

1. **环境检测前置**：在任务开始前确认运行环境，避免生成过程中报错
2. **工具约束明确**：生图必须使用 Codex 自带的 `imagen` 工具（支持传入本地参考图文件）
3. **用户引导友好**：当用户不在正确环境或尝试使用外部工具时，给出清晰的引导

我们对 Skill 的环境检测和提示进行了系统性强化。

---

## 二、核心约束

### 2.1 环境要求

**必须在以下环境之一运行**：

- Codex CLI（终端命令行）
- Codex Desktop（桌面应用）
- claude.ai/code（Web 版 Codex）

**不支持的环境**：

- claude.ai 普通对话
- API 直接调用
- 第三方集成（除非明确支持 Codex Skill 协议）

### 2.2 工具要求

**图片生成工具**：

- ✅ **唯一选项**：Codex 自带的 `imagen` 工具
- ❌ **禁止使用**：DALL-E、Midjourney、Stable Diffusion 等外部工具
- ❌ **禁止行为**：要求用户自行生成图片后上传

**原因**：

1. `imagen` 支持传入本地参考图文件（小石头/老杨的 IP 资产）
2. 可以确保跨图形象一致性（通过参考图机制）
3. 集成在 Codex 工作流中，支持自动化 QA 检查

---

## 三、强化内容

### 3.1 新增文件

#### `scene-skill-core/references/codex-environment-guidance.md`

**全新的环境检测与引导文档**，包含：

1. **环境检测**（任务开始前）
   - Codex 环境确认
   - imagen 工具可用性检查
   - 本地资产路径检测

2. **imagen 工具使用规范**
   - 工具调用格式（单参考/双参考）
   - 提示词组装规范（槽位顺序）
   - 参考图传递机制（路径解析规则）

3. **模式与工具的映射**
   - 实物图模式 → imagen
   - 手绘图模式 → imagen
   - 知识卡模式 → imagen
   - PPT 演讲模式 → imagen（批量）
   - 视频模式 → imagen（批量场景）+ TTS + Remotion
   - 自定义 IP 录入 → imagen（校准阶段）

4. **失败恢复与引导**
   - imagen 调用失败的常见错误和解决方案
   - 用户尝试使用外部工具时的引导话术
   - 用户要求导出提示词时的说明
   - 视频模式的环境检测（TTS / Node.js / FFmpeg）

5. **用户教育与最佳实践**
   - 首次使用引导
   - 常见误解纠正
   - 高级用户提示

6. **架构透明化**
   - 用户视角的工具链
   - 与外部平台的边界
   - 开放性说明

7. **检查清单**（Agent 执行前）
   - 运行环境确认
   - 本地资产路径验证
   - 参考图可用性检查

### 3.2 更新的文件

#### `scene-skill-core/QUICK-START.md`

- 新增 **§ -1. 环境检测（首次任务必做）**
- 快速检测清单（4 项核心检查）
- 非 Codex 环境引导话术
- 指向 `codex-environment-guidance.md` 的详细规则

#### `scene-skill-core/SKILL.md`

- 更新 **§ 快速开始** 部分
- 添加 "⚠️ 环境硬性约束" 说明
- 强调必须在 Codex 环境运行，必须使用 imagen 工具

#### `scene-skill-core/README.md`

- 更新 **§ 🤖 Agent 开发** 部分
- 新增 "🔧 环境与工具" 条目，指向 `codex-environment-guidance.md`
- 调整文档导航顺序（环境检测 → 模式路由 → 完整规范）

#### `scene-skill-core/references/common-prompt-slots.md`

- 文件开头新增 "⚠️ 工具约束" 说明
- 明确提示词槽位专为 **Codex imagen 工具**优化
- 不得使用外部生图工具

#### `scene-skill-core/references/video-mode.md`

- 定位部分新增 "⚠️ 工具硬性约束"
- 明确场景插图生成必须使用 Codex imagen
- 指向 `codex-environment-guidance.md` § 三.5

#### `scene-skill-core/references/brand-mark-mode.md`

- 文件开头新增 "⚠️ 工具约束" 说明
- 明确拟人设定图和模式校准图必须使用 imagen
- 指向 `codex-environment-guidance.md` § 三.6

#### `scene-skill-core/ARCHITECTURE-DESIGN.md`

- 更新 **§ 3. 分层模型**
- "生成与返修层" 明确标注 "**Codex imagen 工具**（必须）"

#### `scene-skill-core/references/README.md`

- 新增 **§ 环境与工具** 部分（置顶）
- 索引 `codex-environment-guidance.md`
- 更新 **§ 知识卡模式 / PPT 演讲模式 / 视频模式** 部分
- 索引 `video-mode.md` 并说明必须使用 Codex imagen

#### `README.md`（项目根目录）

- 更新 **§ 快速使用** 部分
- 新增 "⚠️ 环境要求" 说明
- 指向 `scene-skill-core/references/codex-environment-guidance.md`

---

## 四、用户体验流程

### 4.1 正确流程（用户在 Codex 环境）

```text
1. 用户在 Codex 中说：老杨：这篇内容想配图 <粘贴内容>
   ↓
2. Agent 快速检测：✓ Codex 环境 ✓ imagen 可用 ✓ 资产路径正确
   ↓
3. Agent 读取 QUICK-START.md → 判断模式 → 读取必读文件
   ↓
4. Agent 使用 imagen 生成图片（传入小石头/老杨参考图）
   ↓
5. Agent 做 Confirm Gate + 模式 QA
   ↓
6. 交付图片 + 保存路径 + 说明
```

### 4.2 错误流程 A（用户不在 Codex 环境）

```text
1. 用户在 claude.ai 普通对话说：用小石头生成配图
   ↓
2. Agent 检测：❌ 无 imagen 工具
   ↓
3. Agent 输出引导：
   "这个 Skill 需要在 Codex 环境中运行，因为：
    1. 生图必须使用 Codex 自带的 imagen 工具
    2. 需要读取本地 IP profile 资产文件
    3. 需要保存生成的图片到项目目录
    
    请在以下环境之一使用：
    - Codex CLI / Codex Desktop / claude.ai/code"
   ↓
4. 停止任务，等待用户切换环境
```

### 4.3 错误流程 B（用户尝试使用外部工具）

```text
1. 用户说：我用 Midjourney 生了图，怎么套用你们的风格
   ↓
2. Agent 输出引导：
   "本 Skill 要求使用 Codex 自带的 imagen 工具生成图片，原因：
    1. IP 一致性：imagen 可以传入小石头/老杨的参考图
    2. 质量控制：生成后会自动做 Confirm Gate 检查
    3. 工作流完整性：从内容理解 → 生成 → QA 是一体化的
    
    如果您已有图片，可以：
    - 作为内容参考（描述「像这张图的构图」）
    - 作为自定义 IP 的参考图（录入新 IP profile）
    
    但不能：
    - 跳过 imagen 直接交付外部生成的图"
   ↓
3. 询问用户是否继续用 imagen 生成
```

### 4.4 错误流程 C（用户要求导出提示词）

```text
1. 用户说：先别生成，给我提示词我自己去 DALL-E 生成
   ↓
2. Agent 输出引导：
   "理解您想先看提示词。我可以输出提示词供您参考，但需要说明：
    1. 本 Skill 的提示词是为 Codex imagen 优化的
    2. 参考图机制：imagen 可以传入本地参考图文件
    3. QA 流程：无法自动做 Confirm Gate 检查
    
    建议工作流：
    - 我先用 imagen 生成候选图 → 您查看效果 → 确认或返修
    
    您希望我继续用 imagen 生成，还是仅输出提示词供参考？"
   ↓
3. 等待用户选择
```

---

## 五、关键设计原则

### 5.1 检测前置，不在生成后报错

- 环境检测在任务开始前完成（QUICK-START.md § -1）
- 不要等到调用 imagen 时才发现环境不对
- 给用户明确的"继续/停止"决策点

### 5.2 引导清晰友好，不只说"不行"

- 告诉用户**为什么**必须用 Codex imagen（IP 一致性、QA 流程）
- 告诉用户**怎么做**（切换到哪个环境、如何安装）
- 提供**替代方案**（如果有的话，例如降级为静态图片）

### 5.3 失败快速明确

- 出错时立即停止任务
- 给出具体原因和解决步骤
- 不要无限重试或静默失败

### 5.4 架构透明，不搞黑盒

- 用户可以查看所有规则文件（Read 工具）
- 用户可以修改 IP profile（创建自定义 IP）
- 用户可以导出提示词（用于学习或参考）
- 但生图环节必须使用 Codex imagen（架构硬性约束）

---

## 六、测试场景

### 6.1 正常场景

- [x] 用户在 Codex CLI 中调用 Skill → 正常生成
- [x] 用户在 Codex Desktop 中调用 Skill → 正常生成
- [x] 用户在 claude.ai/code 中调用 Skill → 正常生成

### 6.2 错误场景

- [x] 用户在 claude.ai 普通对话中调用 → 输出环境引导 → 停止任务
- [x] 用户说"我用 Midjourney 生图" → 输出工具约束说明 → 询问是否继续
- [x] 用户说"给我提示词我自己生成" → 输出建议工作流 → 等待用户选择
- [x] 视频模式缺少 TTS / Node.js → 输出环境清单 → 提供降级选项

### 6.3 边界场景

- [x] 用户提供自定义 IP 参考图 → 录入 Profile Enrollment → 用 imagen 生成校准图
- [x] 用户要求"纯物件，不要小石头" → 切换 ip-profiles/none → 仍用 imagen
- [x] PPT 模式批量生成 20 页 → 逐页调用 imagen → 每页独立 QA

---

## 七、相关文件清单

### 新增文件

- `scene-skill-core/references/codex-environment-guidance.md`（核心文档）

### 更新文件

- `scene-skill-core/QUICK-START.md`（§ -1 环境检测）
- `scene-skill-core/SKILL.md`（§ 快速开始）
- `scene-skill-core/README.md`（§ 🤖 Agent 开发）
- `scene-skill-core/ARCHITECTURE-DESIGN.md`（§ 3 分层模型）
- `scene-skill-core/references/README.md`（§ 环境与工具）
- `scene-skill-core/references/common-prompt-slots.md`（文件开头）
- `scene-skill-core/references/video-mode.md`（§ 定位）
- `scene-skill-core/references/brand-mark-mode.md`（文件开头）
- `README.md`（项目根目录，§ 快速使用）

---

## 八、后续维护

### 8.1 新增模式时

如果新增模式（例如"动态视频模式""3D 预览模式"），必须：

1. 在 `codex-environment-guidance.md` § 三 中添加模式与工具的映射
2. 在新模式的文档中添加 "⚠️ 工具约束" 说明
3. 更新 `QUICK-START.md` 的决策表

### 8.2 新增 IP profile 时

新增 IP 不改变工具约束：

- 仍然必须使用 Codex imagen
- 仍然必须提供参考图资产
- 仍然必须通过 Confirm Gate

### 8.3 用户反馈收集

如果用户遇到环境问题，记录：

- 用户所在环境（Codex CLI / Desktop / claude.ai/code / 其他）
- 报错信息（imagen 不可用 / 路径找不到 / 其他）
- 用户意图（想用外部工具 / 想导出提示词 / 其他）
- 引导话术是否有效

持续优化 `codex-environment-guidance.md` 的引导话术和错误恢复流程。

---

## 九、总结

通过本次强化，我们实现了：

✅ **环境检测前置**：任务开始前确认 Codex 环境和 imagen 工具  
✅ **工具约束明确**：生图必须使用 Codex imagen，不支持外部工具  
✅ **引导友好清晰**：告诉用户为什么、怎么做、有什么替代方案  
✅ **失败快速明确**：出错时立即停止，给出具体原因和步骤  
✅ **架构透明开放**：用户可以查看规则、修改 IP、导出提示词  

**核心原则**：Codex imagen 是唯一生图工具 — 不提供替代方案，不妥协。

**用户体验目标**：用户在 Codex 中直接说需求 → 自动生成 → 交付；用户不在 Codex → 友好引导切换环境。
