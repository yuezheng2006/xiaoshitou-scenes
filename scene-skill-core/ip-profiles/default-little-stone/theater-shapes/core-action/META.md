# core-action

```yaml
id: core-action
name: 核心动作图
outputs: [theater_action]
default_ratio: "16:9"
default_input: quote_or_situation
style_id: vinyl-theater
shape_anchors:
  - ONE decisive moment or metaphor gesture only
  - props ≤2
  - text labels 0-3 short Chinese
  - same identity/outfit as APPROVED sheet; only pose/scene change
must_preserve:
  - vinyl-theater identity + hero outfit
  - single primary action readable at a glance
avoid_when_applying:
  - multi-action collage / multiple competing gestures
  - props >2 or label spam
  - turning the plate into a process flowchart
  - photo-real chase
```

## Shape Intent

一个决定性瞬间或隐喻手势——「这一下」就是观点。

## Derived Fields

- 主动作 / 隐喻手势
- 道具 ≤2
- 短标签 0–3
- 表情预设 E0–E4（选一）
- 看见什么：一句话
