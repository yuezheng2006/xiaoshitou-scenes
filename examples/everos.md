# EverOS 项目解读 · 配图提示词

公开分析来源：[EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) + `docs/how-memory-works.md`

**成套示例图**（PPT 8 页 + 密度递进 4 张）：[`assets/examples/everos/`](../assets/examples/everos/README.md)

---

## 实物图 · 五个亮点（16:9）

```text
小石头实物图：生成一张 16:9 配图：多个 coding Agent 共享一层记忆盒，跨 Agent 可携带。多人场景，2-3 个同 IP 小石头（共享 #f39800 橙身、白圆眼，但体型、姿态、朝向、分工明显不同，不要复制粘贴）。
标签：一个记忆层 / 多 Agent / 都能用
```

```text
小石头实物图：生成一张 16:9 配图：小石头编辑 Markdown 文件，SQLite 和 LanceDB 是派生索引。
标签：.md 是真相 / 可编辑 / 索引可重建
```

```text
小石头实物图：生成一张 16:9 配图：EverOS 记忆闭环，写入、flush、search 找回。
标签：写入 / flush / 搜回来
```

```text
小石头实物图：生成一张 16:9 配图：用户轨与 Agent 轨分开存储。多人场景，2 个同 IP 小石头（共享 #f39800 橙身、白圆眼，但体型、姿态、朝向、分工明显不同，不要复制粘贴）。
标签：用户轨 / Agent 轨 / 分开存
```

```text
小石头实物图：生成一张 16:9 配图：离线 Reflection，session 之间合并 episode 簇，记忆越用越准。
标签：离线合并 / 越用越准 / Reflection
```

---

## PPT 演讲 · EverOS 解读（8 页成套）

```text
PPT 演讲模式：主题《EverOS 项目解读》，8 页分享。先出导演规划卡，确认后逐页出图。

大纲：
1 封面：EverOS 跨 Agent 可携带、自进化本地记忆层
2 大判断：记忆首先是 Markdown，不是黑盒向量库
3 模块：三件套 Markdown + SQLite + LanceDB
4 标准：五个核心亮点
5 场景：多 Agent 共用一层记忆
6 时间线：add → flush → search
7 方法：用户轨 + Agent 轨
8 收束：现在就开始试 EverOS
```

样张：`assets/examples/everos/ppt-mode/01-cover.png` … `08-closing.png`

---

## 知识卡 · 五个亮点（3:4）

```text
小石头知识卡：把 EverOS 五个核心亮点做成 3:4 竖版收藏图。
亮点：跨Agent可携带 / Markdown源真相 / add-flush-search闭环 / 双轨记忆 / Reflection自进化
安排 2 个小石头分工协作，体型姿态明显不同。
```

样张：`assets/examples/everos/gallery/04-knowledge-card.png`

---

## 手绘图 · 记忆管线（16:9）

```text
小石头手绘图：画 EverOS 完整写入管线，从 /add buffer 到 flush 写 episode.md 再到 LanceDB cascade。
结构：系统局部；批注：add / flush / episode.md / OME / 检索
```

样张：`assets/examples/everos/gallery/03-handdrawn-high-density.png`
