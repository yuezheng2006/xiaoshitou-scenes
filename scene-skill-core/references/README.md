# References 命名说明

本目录按用途前缀区分。具体 IP 形象、persona、Logo 边界和资产路径放在 `../ip-profiles/<ip-id>/`；本目录只保留通用流程、模式、QA 和模板。

## `common-*`

多种模式都会用到的公共规则：

- `common-character-lock.md`：通用 Character Lock、Persona Identity Lock、维度锁、形象检查、多人差异锁；具体角色读取当前 profile。
- `common-persona-routing.md`：通用 persona 触发、双 IP 路由和安全边界。
- `persona-scene-patterns.md`：默认 profile 触发老杨时的六类互动场景、出图方案推荐和失败信号。
- `common-logo-safety.md`：通用 Logo / 品牌资产安全规则；具体品牌边界读取当前 profile。
- `common-story-extraction.md`：从正文提炼处境、动作、标签的方法。
- `common-generation-templates.md`：实物图、手绘图、长卷和批量图的提示词模板。
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

## 知识卡模式 / PPT 演讲模式

体量较大的两种容器型模式，各用一份文件覆盖触发词、结构、必填字段、QA：

- `knowledge-card-mode.md`：知识卡模式的形态库、角色分工、硬性预算和失败信号。
- `ppt-presentation-mode.md`：PPT 演讲模式的导演规划卡、page card、页面类型库和 QA。
