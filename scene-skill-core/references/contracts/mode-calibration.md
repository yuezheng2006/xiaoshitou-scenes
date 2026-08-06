# 模式校准契约

模式校准图回答“这个 Profile 在当前输出容器里怎么画”，不能用身份设定图或其他模式的样张代替。

## 状态

| 状态 | 含义 | 允许生成 |
| --- | --- | --- |
| `AVAILABLE` | 当前模式有已验收校准资产，并可升级为 `dual` 参考 | 可以按该模式生成 |
| `DEFERRED` | 当前模式尚未建立校准资产 | 可以降级为 `single`，但不得声称使用了双参考 |
| `REJECTED` | 校准资产存在明确失败 | 不得生成，先返修校准资产 |

默认 Profile 的当前状态：

```text
physical       AVAILABLE
handdrawn      AVAILABLE
knowledge-card AVAILABLE
ppt            DEFERRED
video          DEFERRED
```

## 模式边界

- **知识卡**：单张竖版传播容器；关注标题、阅读顺序、模块和行动清单。
- **PPT**：连续 16:9 页面；必须先有导演规划卡，页面节奏和单页沟通任务优先。
- **视频**：1080×1440 的连续镜头；必须先有 `motion.thesis`、`stateChange`、旁白时长和 Gate1，不能把 PPT 或知识卡直接切成视频。

## 降级规则

当前模式的 `calibration` 为 `null` 时：

1. 身份锚点仍可使用；
2. 本次 `reference_protocol` 只能记录 `single`；
3. Task Manifest 的 `reference_assets` 不得伪造不存在的校准图；
4. 生成后仍必须经过对应模式 QA；
5. 首次建立校准资产后，先做一张代表样张并通过人工 Confirm Gate，再把状态升级为 `AVAILABLE`。

校准资产路径必须使用当前 Profile 内的实际文件名；已退役的 `author-persona-spec.png`、`author-persona-handdrawn.png` 不得重新写入新任务。
