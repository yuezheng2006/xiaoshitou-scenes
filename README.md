# 小石头 IP 配图

> 个人 Codex Skill：把中文内容变成「小石头 + 简笔物件 + 物理动作 + 短标签 + 留白叙事」配图。
>
> 16:9 正文图 | 彩蛋长卷 | flat 2D 简笔 | Codex Skill

---

## 命名

| 名称 | 值 |
| --- | --- |
| **项目** | 小石头 IP 配图 |
| **建议仓库名** | `xiaoshi-ip-scenes` |
| **Skill 目录** | `thunderstone-xiaoren/`（Codex 安装包，调用 `$thunderstone-xiaoren`） |
| **角色** | 小石头 (Little Stone) |

---

## 是什么

个人维护的 **Codex Skill**，用来指导 AI 生成「小石头」风格正文配图。我主要自己用；做法和文档可以在团队里分享交流。

**生图方式**：在 Codex 里 `Use $thunderstone-xiaoren ...` → Agent 加载 Skill → 按 `prompt-template.md` 组装 prompt → 调用 Codex 内置 **`image_gen`** 逐张出图。使用者只写中文场景意图即可。

核心公式：

```text
小石头 + 简笔物件 + 物理动作 + 短中文标签 + 留白叙事
```

IP 规范：[thunderstone-xiaoren/references/thunderstone-xiaoren-ip.md](thunderstone-xiaoren/references/thunderstone-xiaoren-ip.md)

品牌与 Logo 消歧、合规说明见 [NOTICE.md](NOTICE.md)。

---

## 目录结构

```text
.
├── README.md / LICENSE / NOTICE.md
├── assets/xiaoshi-test/              # 测试预览样张（浏览用）
├── examples/prompts.md               # 常用 prompt
├── examples/test-scenarios.md        # 16 个试跑场景 + 对应 Codex prompt
└── thunderstone-xiaoren/             # ← 复制到 Codex skills（含 brand + 母版）
    ├── assets/brand/
    ├── assets/examples/              # 母版 01–07
    └── references/
```

---

## 安装

```bash
git clone git@github.com:yuezheng2006/xiaoshi-ip-scenes.git
cd xiaoshi-ip-scenes

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./thunderstone-xiaoren "${CODEX_HOME:-$HOME/.codex}/skills/"
```

```text
Use $thunderstone-xiaoren 把下面这篇内容生成 4 张 16:9 正文配图。

<粘贴内容>
```

更多可复制示例见 [examples/prompts.md](examples/prompts.md)（试跑场景 + prompt 见 [test-scenarios.md](examples/test-scenarios.md)）。

**飞书使用指南**：[小石头 IP 配图 Skill 使用指南](https://m2miovoqda.feishu.cn/docx/UZaWdBpyLoQi6Hx37TKcWx2rnmd)（含试跑样张预览）

---

## 母版 01–07

| 文件 | 场景 |
| --- | --- |
| `01-alignment-pull-in.png` | 需求对齐 / 被拉回 |
| `02-info-overload.png` | 信息过载 |
| `03-problem-knot-alert.png` | 问题打结 |
| `04-review-rework.png` | 审查返工 |
| `05-automation-relabel.png` | 自动化 / 改标签 |
| `06-filter-loss.png` | 筛选流失 |
| `07-brand-evolution-long-scroll.png` | 演化长卷 |

PNG 位于 `thunderstone-xiaoren/assets/examples/`（安装 Skill 后路径为 `assets/examples/`）。

---

## License

MIT — 见 [LICENSE](LICENSE)。第三方商标与 Logo 见 [NOTICE.md](NOTICE.md)。
