# Video Handoff · 视频交接契约

## 用途

视频模式绑定生产契约。目标：**长视频 · 低成本 · 高 IP**。

吸收来源：rachel job-state、gbro 三闸门、灵剪批准绑产物、min-skill 音频主时钟。

Agent 在批量 `imagen` / Fish TTS / 全片 Remotion 渲染前，必须先有交接契约或等价 `work/job-state.json`。

## 项目目录（推荐）

```text
<video-project>/
├── handoff.md
├── work/job-state.json
├── src/generated/plan.json
├── src/generated/captions.json
├── public/images/scene-*.png
├── public/audio/narration.mp3
└── out/
    ├── contact-sheet.jpg
    ├── preview.png
    └── video.mp4
```

## handoff.md 模板

```markdown
---
topic: 为什么存钱越早越轻松
title: 存钱，越早越轻松
platform: douyin
ratio: 1080x1440
duration_target_s: 75
style_lane: physical
remotion_style: warm-editorial
voice:
  provider: fish-audio
  mode: continuous
caption:
  timing: scripted
  path: src/generated/captions.json
illustration: default-little-stone
status: queued
---

## Motion thesis
（一句话运动隐喻）

## Scenes
| id | headline | narration | state_change | image |
| --- | --- | --- | --- | --- |
| scene-01 | … | … | … | images/scene-01.png |

## Gates
- [ ] check_setup PASS
- [ ] Gate1 storyboard 已批准（`video_approve.py --gate storyboard`）
- [ ] Gate2 stills 已批准（可部分通过；有 contact sheet）
- [ ] TTS + captions timing=scripted
- [ ] Gate3 preview 已批准（哈希绑定）
- [ ] check_delivery PASS
```

## 生产门禁（硬规则）

```text
check_setup → Gate1 storyboard → imagen(通过镜)
→ contact sheet → Gate2 stills → Fish TTS → scripted captions
→ still → Gate3 preview → render → check_delivery
```

1. 未 Gate1 批准，不得批量 imagen。
2. 未写 motion thesis，不得进入场景图生成。
3. 图内禁止中文标签；字幕/标题由 Remotion 统一字号。
4. 批准绑产物哈希：改 plan/图/旁白/captions 后对应闸门变 stale，须重批。
5. 全片渲染前 Gate3 preview 必须 approved（除非用户显式跳过）。
6. 交付以 `video_check_delivery.py` exit 0 为准。

**禁止**写入 API key。
