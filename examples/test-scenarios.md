# 试跑场景与提示词

## 生图是怎么走的

| 环节 | 说明 |
| --- | --- |
| **入口** | 在 **Codex** 对话里写 `Use $thunderstone-xiaoren ...` |
| **Skill** | Codex 加载 `thunderstone-xiaoren/` 包，读取 IP、母版、prompt 模板 |
| **生图** | Agent 按 `references/prompt-template.md` 组装英文生图 prompt，调用 Codex 内置 **`image_gen`** 逐张出图 |
| **你写什么** | 只写中文场景意图即可；配色、Character Lock、母版锁定由 Skill 内部处理 |

> 本仓库 `assets/xiaoshi-test/` 里的样张，均按上述 Codex Skill 流程设计 prompt；在 Cursor 等环境验证时可能走其他生图工具，但**用户侧可复制 prompt 与 Codex 一致**。

---

## 一图一摘要 + 可复制 prompt

格式：**摘要**（飞书/文档用）+ **Codex prompt**（直接复制到 Codex）。

### 01 · 问题打结

**摘要**：线上问题像打结的线，越急越难一下子扯开。

**文件**：`01-problem-knot-alert-test.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：线上问题像打结，小石头在解结。
标签：又打结了 / 先别硬拽 / 慢慢解
```

### 02 · 信息过载

**摘要**：模型告警、Bot 消息和待办同时涌来，得先护住头再排序。

**文件**：`02-info-overload-test.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：AI 告警和消息同时涌来，信息过载。
标签：太多了 / 先护头 / 排优先级
```

### 03 · 工牌场景

**摘要**：品牌 Logo 只出现在工牌等道具上，身上有严格禁区。

**文件**：`03-workplace-badge-thunderstone-test.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：小石头佩戴工牌，Logo 只在工牌牌面。
标签：工区 / 刷卡 / 别贴身上
```

### 04 · Prompt 调优

**摘要**：改 prompt 像给模型贴标签，贴完还得再跑一轮才知道对不对。

**文件**：`test-ai-prompt-tuning.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：改 prompt，像给模型贴标签试效果。
标签：改 prompt / 再试 / 这句不对
```

### 05 · RAG 检索

**摘要**：答案藏在文档堆里，RAG 的第一关永远是：先找到那段。

**文件**：`test-ai-rag-search.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：在一堆文档里检索，RAG 找 relevant 段落。
标签：在哪段 / 先检索 / 找到了
```

### 06 · 幻觉核验

**摘要**：模型回得很快，但「真的吗」这三个字永远要多问一遍。

**文件**：`test-ai-hallucination-check.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：核验模型回答有没有胡说，像验真伪。
标签：真的吗 / 先核验 / 别瞎编
```

### 07 · Context 溢出

**摘要**：上下文窗口快塞爆了，不截断、不摘要，后面全都得重来。

**文件**：`test-ai-context-overflow.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：context 窗口塞满，小石头在把内容往回塞。
标签：塞不下 / 得截 / 先摘要
```

### 08 · Multi-agent 接力（多人）

**摘要**：三个 Agent 像接力赛，任务卡片从左传到右，谁接谁接着干。

**文件**：`test-multi-agent-handoff.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：三个 Agent 接力传任务。多人场景，2-3 个相同小石头。
标签：Agent A / 传给 B / 接着干
```

### 09 · Prompt 评审会（多人）

**摘要**：上线前的 prompt 草案，永远要围过来改几句才安心。

**文件**：`test-ai-prompt-review.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：团队围看 prompt 草案一起改。多人场景，2-3 个相同小石头。
标签：这句行吗 / 再改改 / 上线前
```

### 10 · 结对搭 Workflow（多人）

**摘要**：一个人搭节点、一个人接线，先把最小链路跑通再说。

**文件**：`test-ai-pair-agents.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：两个人结对搭 AI workflow。多人场景，2 个相同小石头。
标签：你搭 / 我接 / 跑通先
```

### 11 · Eval 对标（多人）

**摘要**：分数涨没涨，两个人对着 eval 条子各执一词，那就再跑一轮。

**文件**：`test-ai-eval-benchmark.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：两个人对着 eval 分数讨论要不要重跑。多人场景，2 个相同小石头。
标签：涨分了 / 真的 / 再跑一轮
```

### 12 · Coding 排查

**摘要**：集成 AI 后的报错仍像打结线缆，本能还是先排查再上线。

**文件**：`test-coding-scene.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：coding 排查 bug，线缆打结要解开。
标签：又报错 / 先排查 / 今晚上线
```

### 13 · Demo 翻车

**摘要**：现场 Demo 屏幕突然空白，比 bug 本身更让人呼吸停滞。

**文件**：`test-demo-fail.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：产品 Demo 现场屏幕空白，小石头愣住。
标签：怎么白了 / Demo / 稳住
```

### 14 · 跨团队对齐（多人）

**摘要**：产品、研发、算法三个方向同时拉，对齐比调参还费神。

**文件**：`test-cross-team-align-v2.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：产品、研发、算法三方被不同方向拉。多人场景，3 个相同小石头。
标签：产品 / 研发 / 算法
```

### 15 · 版本回滚

**摘要**：模型或功能回滚像后悔药，按下去之前总要再犹豫三秒。

**文件**：`test-version-rollback.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：版本回滚，小石头手悬在回滚键上犹豫。
标签：要回滚吗 / 再想想 / 先止损
```

### 16 · 深夜值班

**摘要**：告警还没凉，咖啡先凉了，别在这会儿又响铃。

**文件**：`test-overtime-duty.png`

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：深夜 on-call 值班，咖啡凉了告警还在。
标签：深夜 / 还在 / 别响铃
```
