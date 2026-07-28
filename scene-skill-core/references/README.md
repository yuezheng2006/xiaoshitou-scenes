# References 命名说明（L3 On-demand）

本目录是 Agent Skills progressive disclosure 的 **L3**：只在 `QUICK-START.md` 或 `SKILL.md`「一层加载表」点名时再读，不要在激活 Skill 时全量加载。

加载约定：

1. 从 `SKILL.md` / `QUICK-START.md` 只跳 **一层** 到本目录某个文件。
2. 该文件内部可再指向同目录或 `../ip-profiles/` 的下一层；Agent 按需打开，不要预读整树。
3. 完整路由表见 `../SKILL.md` → Before Starting；本文件是索引，不是启动必读。

本目录按用途前缀区分。具体 IP 形象、persona、Logo 边界和资产路径放在 `../ip-profiles/<ip-id>/`；本目录只保留通用流程、模式、QA 和模板。

## 环境与工具

- `codex-environment-guidance.md`：**Codex 环境检测与 imagen 工具使用规范**。本 Skill 面向 Codex 环境设计，生图必须使用 Codex 自带的 `imagen` 工具。包含环境检测清单、工具调用格式、失败恢复、用户引导。
- `codex-exec-best-practices.md`：**codex exec 实战经验与踩坑指南**。记录环境检测 + 生图的完整实战流程，包括：当前会话 vs 新会话、环境检测时机、imagen 参考图传递、Confirm Gate 验证、性能优化、常见场景模板。已通过实战验证（assets/little-stone-environment-check-passed.png）。

## `common-*`

多种模式都会用到的公共规则：

- `common-character-lock.md`：通用 Character Lock、Persona Identity Lock、维度锁、形象检查、多人差异锁；具体角色读取当前 profile。
- `common-persona-calibration.md`：所有人像参考图的生成前校准卡、生成后身份/年龄/比例复核；校准失败不得生成或交付。
- `common-persona-routing.md`：通用 persona 触发、双 IP 路由和安全边界。
- `persona-scene-patterns.md`：默认 profile 触发老杨时的六类互动场景、出图方案推荐和失败信号。
- `common-logo-safety.md`：通用 Logo / 品牌资产安全规则；具体品牌边界读取当前 profile。
- `common-story-extraction.md`：从正文提炼处境、动作、标签的方法。
- `common-prompt-slots.md`：通用 prompt 槽位组装；**双参考用于对齐老杨（人）**；`{IP_DESC}` / `{IP_STYLE_ADAPT}` 分层。
- `common-generation-templates.md`：实物图、手绘图、长卷和批量图的提示词模板（按槽位填入）。
- `common-qa-repair.md`：装饰性测试、用户反馈映射表、标准化返修输出格式。
- `common-modes-and-sizes.md`：尺寸池与图内信息量分级语言。

## `physical-*`

只服务于实物图模式：

- `physical-style-dna.md`：实物图视觉 DNA、白底、真实物件与留白规则。
- `physical-object-patterns.md`：真实物件选择、场景类型和原创隐喻。
- `physical-master-anchors.md`：实物图 01-06 母版锚点、抽象骨架和变异规则。
- `physical-qa-checklist.md`：实物图生成后的 QA 与失败信号。

## `handdrawn-*`

只服务于手绘图模式：

- `handdrawn-style-dna.md`：手绘图视觉 DNA、颜色、标注和禁忌。
- `handdrawn-composition-patterns.md`：手绘图结构类型和隐喻生成规则。
- `handdrawn-qa-checklist.md`：手绘图生成后的 QA 与失败信号。

## `persona-author-*`（profile 内，默认老杨）

触发 persona 时分层读取，入口 `../ip-profiles/<ip-id>/persona-author.md`：

- `persona-author-identity.md`：识别锚点、小比例线
- `persona-author-assets.md`：三固定资产、传图规则
- `persona-author-modes.md`：各模式双 IP 职责
- `persona-author-prompts.md`：可复制 prompt 片段
- `persona-scene-patterns.md`：六类互动场景（本目录）

## `brand-mark-mode.md`

`input_kind=brand_mark` 专用：Logo/App Icon → **三层参考**（canonical → identity_sheet → mode calibration）→ AVAILABLE → 正文试跑。拟人化硬规则、生动度、QA、prompt 片段。与 `contracts/profile-contract.md`、`common-prompt-slots.md` §D 联动。

## 知识卡模式 / PPT 演讲模式 / 视频模式

体量较大的容器型模式，各用一份文件覆盖触发词、结构、必填字段、QA：

- `knowledge-card-mode.md`：知识卡模式的形态库、角色分工、硬性预算和失败信号。
- `ppt-presentation-mode.md`：PPT 演讲模式的导演规划卡、page card、页面类型库和 QA。
- `video-mode.md`：视频模式生产门禁、plan.json、imagen 场景、TTS、字幕对齐、Remotion、交付检查。
- `video-motion-director.md`：运动 thesis、stateChange、Anti-PPT（场景图前必读）。
- `contracts/video-handoff.md`：handoff / job-state / 预览批准契约（参考 rachel 数字人生产门禁）。
