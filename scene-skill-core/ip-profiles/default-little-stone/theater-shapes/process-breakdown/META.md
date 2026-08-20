# process-breakdown

```yaml
id: process-breakdown
name: 流程拆解图
outputs: [theater_process]
default_ratio: "16:9"
default_input: paragraph_or_topic
style_id: vinyl-theater
shape_anchors:
  - one core structure spine (steps / compare / loop / funnel / hierarchy)
  - 3-5 modules with short Chinese labels ≤6 chars each
  - Lao Yang inside the diagram ~25-40% of frame
  - pointing / annotating / walking the path — NOT a corner sticker
  - safe explain pose: elbow ~90° readable chain when pointing
must_preserve:
  - vinyl-theater identity + hero outfit
  - readable structure at article width
  - single current-step emphasis (point at the key node)
avoid_when_applying:
  - more than 5 modules
  - pasting full article paragraphs into the image
  - character as tiny corner sticker
  - melted / missing-elbow pointing arm (switch to pen/stick pointer)
  - multi-action collage
```

## Shape Intent

让读者一眼看见「流程怎么走」。人在结构里指当前步。

## Derived Fields（从段落/主题抽取）

- A 层结构名（≤6 字，可选）
- B 层节点标签 3–5 个（各 ≤6 字）
- C 层结果/风险注 0–1
- 姿态：指向哪个节点
- 场域（可选）：咖啡馆 / 车载 / 书桌…
- 看见什么：一句话
