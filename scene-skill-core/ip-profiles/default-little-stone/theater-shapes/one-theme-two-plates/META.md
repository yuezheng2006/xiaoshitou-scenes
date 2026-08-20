# one-theme-two-plates

```yaml
id: one-theme-two-plates
name: 一鱼两吃
outputs: [theater_process, theater_action]
default_ratio: "16:9"
default_input: topic
style_id: vinyl-theater
shape_anchors:
  - Plate A = process-breakdown; Plate B = core-action
  - identical face/hair/glasses/outfit/shoes from APPROVED sheet
  - order hard: fill topic recipe → A preview identity OK → B with same sheet refs → deliver both
must_preserve:
  - zero outfit change between plates
  - same vinyl-theater style atom on both plates
avoid_when_applying:
  - generating B before A identity check
  - different faces or outfits across plates
  - skipping topic recipe card
```

## Shape Intent

同一主题两张板：拆解「怎么走」+ 动作「这一下」。

## Derived Fields（主题配方卡）

- 主题：{TOPIC}
- 拆解板：结构类型；模块；姿态
- 动作板：隐喻动作；道具≤2；文案≤3
- 两板：同一设定图，零换装
- 命名：`{topic}-process.png` / `{topic}-action.png`
