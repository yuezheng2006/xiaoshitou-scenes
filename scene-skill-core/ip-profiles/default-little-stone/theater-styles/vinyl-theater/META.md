# vinyl-theater

```yaml
id: vinyl-theater
name: 潮玩小剧场
input_modes: [text, approved_sheet]
subjects: [person]
outputs: [theater_process, theater_action, theater_sheet]
default_ratio: "16:9"
required_fields: [approved_expression_sheet, approved_face_lock_or_sheet, content_or_topic]
optional_fields: [scene_field, expression_preset, combo_little_stone]
source: theater-styles/vinyl-theater/STYLE.md
style_anchors:
  - 3D stylized vinyl-toy / designer-collectible matte look
  - soft diffused light, clean subtle outline, collectible figurine feel
  - Lao Yang identity from APPROVED theater expression sheet + face-lock only
  - hero outfit locked: navy crew tee, loose khaki Bermuda past knee, light short socks, NB 2002R, left sports watch
  - likeness via recognizable anchors — NOT photo-real skin / NOT selfie look
  - character inside the idea diagram (not corner sticker) for process plates
must_preserve:
  - same person as APPROVED sheet across all panels in a batch
  - thick black soft-rectangular glasses; short hard spiky black hair; soft rounder face with cheek volume
  - matte vinyl rendering language (no photo pores, no semi-real painterly skin)
  - body read ~182/86 with long legs 4:6 when full-figure
avoid_when_applying_to_theater:
  - photorealistic / documentary selfie / hyperreal CGI skin chase
  - path-B flat whiteboard + beige teaching tee
  - outfit change vs APPROVED sheet
  - Little Stone in solo mode; 3D orange pebble assimilation in combo
  - pasting face rectangles / white haze neck seams
  - dumping full article body into the image or prompt
```

## Style Intent

老杨小剧场默认唯一画风原子：潮玩 vinyl + 固定 IP。本 atom 只负责渲染语言与身份锁；图型形状（流程/动作/一鱼两吃）由 `theater-shapes/` + `theater-prompt-blueprint.md` 负责。

## Use For

- 路径 C 场景板（流程拆解 / 核心动作 / 一鱼两吃）
- 设定图表情制作表（同一渲染语言）

## Avoid

- 把 Punk Cover 的 25 种封面风格混进小剧场
- 多风格混贴或把 STYLE 原文第二段粘贴进 prompt
