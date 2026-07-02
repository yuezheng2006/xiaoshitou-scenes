# 小石头 IP 配图

> 个人 Codex Skill：用「小石头」把中文内容转成四类配图。
>
> 小石头实物图 | 小石头手绘图 | 知识卡 | PPT 演讲模式 | 16:9 正文图 | 彩蛋长卷 | Codex Skill

---

## 命名

| 名称 | 值 |
| --- | --- |
| **项目** | 小石头 IP 配图 |
| **建议仓库名** | `xiaoshitou-scenes` |
| **Skill 目录** | `little-stone-scenes/`（Codex 安装包；安装后自然语言即可触发） |
| **角色** | 小石头 (Little Stone) |

---

## 是什么

个人维护的 **Codex Skill**，用来指导 AI 生成「小石头」风格正文配图。我主要自己用；做法和文档可以在团队里分享交流。

安装 Skill 到 Codex 后，直接用中文说配图意图即可。推荐用两个明确风格词：

```text
小石头实物图：为这篇内容生成 4 张 16:9 正文配图。
```

```text
小石头手绘图：把下面的 Agent 工作流解释成一张白板图。
```

不必写 `Use $little-stone-scenes`；该写法仅作可选强制指定。

---

## 四种模式

| 模式 | 适合内容 | 视觉核心 |
| --- | --- | --- |
| **小石头实物图** | 处境、情绪、项目故事、正文观点隐喻、彩蛋长卷 | 小石头 + 简笔物件 + 物理动作 + 短标签 + 留白 |
| **小石头手绘图** | 流程、结构、系统关系、方法论、认知拆解 | 小石头 + 白板手绘结构 + 红橙蓝批注 + 核心概念动作 |
| **小石头知识卡** | 方法论、步骤、对比、案例、诊断、课程总览等需要独立传播/收藏的内容 | 小石头 + 竖版收藏容器（3:4/4:5/9:16）+ 标题/模块 + 多人协作分工 |
| **PPT 演讲模式** | 直播分享、课程课件、主题演讲、案例复盘 | 小石头 + 整套 16:9 手绘风演讲页面 + 导演规划卡 + 页面节奏 |

实物图、手绘图是默认主力模式；知识卡、PPT 演讲模式体量更大，只在用户明确触发或内容明显需要独立传播容器/整套演讲页面时才使用。

不论哪种模式，都必须保留小石头自己的特点：`#f39200` 胶囊体、白圆眼、细线肢体、物理/概念动作、短中文标签，以及认真但有点笨的气质；实物图和手绘图还必须保留充足留白，不做成信息堆叠。

IP 规范：[little-stone-scenes/references/common-little-stone-ip.md](little-stone-scenes/references/common-little-stone-ip.md)

---

## 作者出镜

当 prompt 提到 **老杨 / 作者 / yuezheng2006 / 我本人 / 我的数字形象** 时，Skill 会读取作者数字形象参考图，并把作者加入画面，与小石头互动。

```text
小石头实物图：老杨和小石头一起整理一堆 prompt 草稿，生成一张 16:9 配图。
```

默认不出现真人或作者形象；只有明确触发时才启用。作者出镜时，小石头仍然承担核心动作，作者只作为协作角色出现。

合规说明见 [NOTICE.md](NOTICE.md)。

---

## 品牌与去敏感化

小石头的品牌感内化在角色本身：皮肤色 `#f39200` 取自雷石品牌橙，「小石头」之名也由此而来。除这一层血脉外，正文、示例与提示词默认**不展开公司业务详情**，避免敏感信息外泄。

可选的品牌 Logo / 工牌资产保留在 `assets/brand/`，但**默认不启用**，仅在用户明确要求工牌、展会或物料场景时使用；公开示例不展示具体品牌。详见 [NOTICE.md](NOTICE.md) 与 `little-stone-scenes/references/common-logo-safety.md`。

---

## 致谢

本仓库是对 Ian / helloianneo 配图工作流的二次整理与小石头化改写：

| 本仓库模式 | 主要承袭 | 说明 |
| --- | --- | --- |
| 小石头实物图 | Ian / helloianneo 实物场景工作流 | 2.0：真实物件场景 + 长卷故事图 |
| 小石头手绘图 | Ian / helloianneo 手绘解释工作流 | 1.0：纯白手绘解释图 |

本仓库将角色 IP 换为原创的 **小石头 (Little Stone)**，并重写了示例、触发方式、双模式路由与公开版合规文档；在此向 Ian 及原仓库致谢。

---

## 目录结构

```text
.
├── README.md / LICENSE / NOTICE.md
├── examples/prompts.md               # 四种模式常用 prompt
├── examples/test-scenarios.md        # 18 个实物图试跑场景（含 15 张样张）+ prompt
└── little-stone-scenes/             # ← 复制到 Codex skills
    ├── SKILL.md
    ├── agents/                       # Codex agent 接口配置
    ├── assets/brand/                 # 小石头锚点 + 可选品牌 Logo / 参考（默认不启用）
    ├── assets/persona/               # 作者数字形象风格化资产（可选出镜，不含真人照片）
    ├── assets/examples/              # 实物图母版 01–06
    ├── evals/                        # 关键验收用例
    └── references/                   # common-* / physical-* / handdrawn- / knowledge-card- / ppt- 规则
```

---

## 安装

```bash
git clone git@github.com:yuezheng2006/xiaoshitou-scenes.git
cd xiaoshitou-scenes

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./little-stone-scenes "${CODEX_HOME:-$HOME/.codex}/skills/"
```

更多可复制示例见 [examples/prompts.md](examples/prompts.md)。

**飞书使用指南**：[小石头 IP 配图 Skill 使用指南](https://m2miovoqda.feishu.cn/docx/UZaWdBpyLoQi6Hx37TKcWx2rnmd)

---

## 实物图母版 01–06

| 文件 | 场景 |
| --- | --- |
| `01-alignment-pull-in.png` | 需求对齐 / 被拉回 |
| `02-info-overload.png` | 信息过载 |
| `03-problem-knot-alert.png` | 问题打结 |
| `04-review-rework.png` | 审查返工 |
| `05-automation-relabel.png` | 自动化 / 改标签 |
| `06-filter-loss.png` | 筛选流失 |

PNG 位于 `little-stone-scenes/assets/examples/`（安装 Skill 后路径为 `assets/examples/`）。

手绘图不使用实物母版，走 `references/handdrawn-*` 结构规则。

---

## License

MIT — 见 [LICENSE](LICENSE)。
