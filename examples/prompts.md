# 使用示例

## 生图入口（Codex）

在 **Codex** 里触发 Skill，Agent 会读取 `thunderstone-xiaoren/` 并调用内置 **`image_gen`** 出图。你只需写中文场景意图，不必写配色或角色细节。

```bash
# 安装（一次性）
cp -R ./thunderstone-xiaoren "${CODEX_HOME:-$HOME/.codex}/skills/"
```

---

## 常用 prompt

### 先规划，暂不生图

```text
Use $thunderstone-xiaoren 先不要生图。
请分析下面这篇中文内容，输出约 5 张配图方案（每张：主题、核心动作、2–4 个短标签）。

<粘贴内容>
```

### 生成一组正文配图

```text
Use $thunderstone-xiaoren 把下面这篇内容生成 4 张 16:9 正文配图。

<粘贴内容>
```

### 单个观点一张图

```text
Use $thunderstone-xiaoren 为这个观点生成一张 16:9 正文配图：

产品功能很多，但用户真正记住的往往只有一个瞬间。
```

### 长卷故事图

```text
Use $thunderstone-xiaoren 把这个项目复盘做成一张超横版长卷故事图。

主题：从一个本地 KTV 点歌想法，慢慢变成全场景音乐科技产品。
节点：起点、原型、试点、反馈、规模化、家庭场景、持续迭代。
```

### 改图

```text
Use $thunderstone-xiaoren 这张方向对，但文字太多。请减到 3 个短标签，其他保持不变。
```

---

## 试跑场景（含 prompt）

16 个 AI native 试跑样张（含多人场景）的**一图一摘要 + 可复制 Codex prompt**，见 **[test-scenarios.md](test-scenarios.md)**。

示例：

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：三个 Agent 接力传任务。多人场景，2-3 个相同小石头。
标签：Agent A / 传给 B / 接着干
```

```text
Use $thunderstone-xiaoren 生成一张 16:9 配图：核验模型回答有没有胡说，像验真伪。
标签：真的吗 / 先核验 / 别瞎编
```

样张 PNG 在 `assets/xiaoshi-test/`。
