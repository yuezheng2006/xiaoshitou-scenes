# EverOS 项目解读 · 示例图

对标 [ip-diagram-creator](https://github.com/haloshin/ip-diagram-creator) 的「真实内容成套产出」展示方式，为 **EverOS 项目解读** 生成可公开引用的示例图。

内容来源：[EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) 及其公开文档。

---

## PPT 演讲 · 8 页成套（`ppt-mode/`）

主题：**EverOS 项目解读** — 可直接用于分享/导读的 PPT 页面，不是 Skill 能力说明。

| 页 | 文件 | 页面类型 | 内容 |
| --- | --- | --- | --- |
| 01 | `01-cover.png` | 封面 | EverOS 项目解读 |
| 02 | `02-big-judgment.png` | 大判断 | 记忆首先是 Markdown，不是黑盒向量库 |
| 03 | `03-module.png` | 模块 | 三件套：Markdown + SQLite + LanceDB |
| 04 | `04-standard.png` | 标准 | 五个核心亮点 |
| 05 | `05-scene.png` | 场景 | 多 Agent 共用一层记忆 |
| 06 | `06-timeline.png` | 时间线 | add → flush → search 闭环 |
| 07 | `07-method.png` | 方法 | 双轨记忆：用户轨 + Agent 轨 |
| 08 | `08-closing.png` | 收束 | 现在就开始试 EverOS |

### 生成提示词（整套）

```text
PPT 演讲模式：主题《EverOS 项目解读》，8 页分享。先出导演规划卡，确认后逐页出图。

页1封面 EverOS跨Agent可携带自进化本地记忆层
页2大判断 记忆首先是Markdown不是黑盒向量库
页3模块 三件套 Markdown源真相 SQLite状态队列 LanceDB检索索引
页4标准 五个亮点 跨Agent/Markdown/add-flush-search/双轨/Reflection
页5场景 多Agent共用一层记忆盒
页6时间线 add→flush→search第一次记忆解锁
页7方法 用户轨与Agent轨分开存储
页8收束 everos demo / init / 开始试用
```

---

## 信息密度递进（`gallery/`）

同一主题（EverOS 记忆）从低到高的产出差异，对应 ip-diagram-creator 的「从低信息量插图到知识卡」：

| 档位 | 文件 | 模式 |
| --- | --- | --- |
| 低 | `01-physical-low-density.png` | 小石头实物图：多 Agent 共享记忆盒 |
| 中 | `02-handdrawn-medium.png` | 手绘图：add → flush → search |
| 高 | `03-handdrawn-high-density.png` | 手绘标注：完整写入管线 |
| 知识卡 | `04-knowledge-card.png` | 竖版：EverOS 五个亮点 |

### 单张提示词见

[examples/everos.md](../../../examples/everos.md)

---

## 与 ip-diagram-creator 的对应

| ip-diagram-creator 示例 | 本目录 |
| --- | --- |
| PPT 模式 8 页（如 21 天实战营） | `ppt-mode/01–08` EverOS 解读 |
| 低→中→高→知识卡 四档 | `gallery/01–04` |
| 角色三件套 | 使用默认 profile：`scene-skill-core/ip-profiles/default-little-stone/assets/character/` + `assets/persona/` |
