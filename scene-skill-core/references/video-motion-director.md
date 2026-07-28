# 视频运动导演（Anti-PPT）

## 定位

把「主题 → 小石头视频」从切图幻灯片，抬成**运动叙事**。吸收 [rnskill `rn-motion-director`](https://github.com/Pluviobyte/rnskill) 的 motion-first 原则；不替代 `video-mode.md` 的制作流水线，而是卡在场景图生成之前。

## 硬规则

1. **先找会动的隐喻**，再拆场景。禁止从「第 1 页 / 第 2 页」开始想。
2. 每个 beat 必须有**可见状态变化**（物件形态、数量、位置、角色动作、结构连线），不能只靠淡入淡出或换字幕。
3. 文字是锚点，不是主载体。旁白 15–25 字；画面标签 1–3 个短词。
4. 至少 **80%** 的场景有独立 `state_change`；否则判 PPT 风险，重写分镜。
5. 小石头必须承担物理/概念动作（拉、塞、挡、递、看、扛），禁止站桩装饰。

## Motion thesis（必写一句）

```text
本片靠 <视觉隐喻> 从 <起点状态> 变成 <终点状态>，证明 <核心主张>。
```

例：

- 存钱：空钱包散落 → 硬币进罐 → 小球变大球，证明「越早开始越轻松」。
- Agent 工作流：需求卡进闸 → 模块接力 → 回传闭环，证明「多 Agent 要共用一层记忆」。

写不出这句 → 停，先发明隐喻，再写 `plan.json`。

## Beat 字段（写入 plan 或 handoff）

每个场景最少：

| 字段 | 含义 |
| --- | --- |
| `narrative_job` | hook / reveal / contrast / mechanism / proof / close |
| `state_change` | 画面上具体变了什么 |
| `character_action` | 小石头动词 |
| `ppt_risk` | 若只切图会怎样；如何避免 |

可选写入 `plan.json`：

```json
"motion": {
  "id": "editorial-drift",
  "intensity": "medium",
  "thesis": "空钱包散落到复利雪球长大，证明越早存越轻松",
  "anti_ppt": true
}
```

以及每个 scene：

```json
"narrativeJob": "hook",
"stateChange": "钱包摊开，钞票与收据散落在地面",
"characterAction": "双手扶头"
```

## 与 Remotion 的关系

- 模板默认是**插图铺满 + 文字叠层**（克制边框）。
- 动效只辅助状态变化，不能用复杂边框/色带冒充「有运动」。
- 若一镜只有静物无变化，回去改 `imagePrompt` / 分镜，不要堆 MotionOverlay。

## QA 失败信号

- 连续 2 个以上场景只换标题、物件拓扑相同
- 小石头每镜同一姿势
- 旁白在讲机制，画面只是装饰插画
- 分镜读起来像 PPT 目录
