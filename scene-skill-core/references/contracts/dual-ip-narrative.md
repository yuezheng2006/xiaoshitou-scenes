# 双 IP 叙事契约

触发老杨后，双 IP 不是“两个人同时出现”，而是一个可观察的交接回路：

```text
老杨提出判断/拆解 → 小石头执行动作 → 老杨检查/收束
```

## 角色职责

| 角色 | 默认职责 | 失败信号 |
| --- | --- | --- |
| 老杨 | 主讲、拆解、指向、调度、检查 | 只剩头像/气泡；没有指向或检查动作 |
| 小石头 | 搬卡、贴标签、拉线、挡门、递交结果、承担物理动作 | 站桩装饰；老杨替代全部执行 |

## 跨模式最小字段

涉及双 IP 的任务，在 Plan Card / page card / video plan 中至少记录：

```yaml
presenter: 老杨
executor: 小石头
narrative_job: mechanism
actor_action: 小石头拉线并把结果卡递回老杨
state_change: 模块从未分类变成已交接
handoff: 老杨检查结果并指出下一步
```

- `narrative_job`：`hook` / `reveal` / `contrast` / `mechanism` / `proof` / `close`
- `actor_action` 必须是可见动作，不能只写“陪伴”“出现”“讲解”。
- `state_change` 是画面或镜头前后能观察到的变化；视频中必须与 `motion.thesis` 对齐。
- 未触发老杨时，`presenter`、`handoff` 和老杨资产不得被自动补入。

## 模式约束

- **知识卡**：老杨贴近标题或结论主讲；1–3 个小石头在步骤、案例、风险区执行，必须有阅读顺序。
- **PPT**：每页只保留一个沟通任务；老杨不连续占据大头像，小石头只在真正承担模块动作的页出现。
- **视频**：每镜至少一个 `stateChange` 和 `characterAction`；不能只切换双 IP 静帧。
- **实物 / 手绘**：动作必须服务物件或结构关系，删掉角色后隐喻不应仍然完整成立。
