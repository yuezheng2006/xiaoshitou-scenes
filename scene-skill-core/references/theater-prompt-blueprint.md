# Theater Prompt Blueprint（路径 C）

仿 Punk「shape × style atom → 一条完整 prompt」：  
`vinyl-theater` 是风格原子；`theater-shapes/*` 是图型形状；本蓝图是编译骨架。

**禁止**：把 `STYLE.md` / 图型 META 原文第二段粘贴拼接。  
**必须**：改写进下列章节，输出**一条**可直接交给 imagen 的完整 brief。

出图前另须满足：设定图 Gate = **APPROVED**；长文已有 Imprint Plan Card（或用户 `auto`）。

---

## 场景轻确认门（缺则先问再渲）

若用户只给主题/段落、未指定图型，且未说 `auto`：

```text
设定图：APPROVED（路径…）· 默认画幅 16:9
建议图型：
- A：流程拆解 — …
- B：核心动作 — …
- C：一鱼两吃 — …
请选一个图型，或回复 auto。
```

已知图型 + APPROVED → 可直接编译生成。  
用户说「设定图」→ **只做设定图 Gate**，不批场景。

---

## Required Final Prompt Structure

将下列结构填满后写入  
`.validation-output/generation/theater/scenes/prompts/{slug}-{shape}.md`（或任务目录等价路径），再调用 bridge 生图。

```text
# Lao Yang Visual Theater · {shape_name} · vinyl-theater

You are generating ONE theater imprint plate for Lao Yang (路径 C).
Aspect ratio: {ratio}. Style atom: vinyl-theater ONLY — not a Punk cover style.

## Role / Task
Create one single {shape_name} image. Do not output grids, contact sheets, or alternatives.

## Inputs (derived fields only — Do NOT paste full article body)
- Path: C solo | C combo
- APPROVED sheet refs: expression-sheet (face) + face-lock + theater-sheet (body/outfit)
- Input form: paragraph | topic | quote
- Title/topic: {title_or_topic}
- Short context summary: {summary}
- Visual subject / structure: {visual_subject}
- Scene field (optional backdrop only): {scene_field}
- Mood / expression preset: {expression}
- Metaphor or key node: {metaphor_or_node}
- Banned elements: {banned_elements}
- What reader should see (one sentence): {see_what}

## Content Understanding
Use only derived fields. Long source text must be summarized into labels and structure — never copied into the image.

## Identity + Likeness Policy
- Face/hair/glasses from APPROVED expression-sheet + face-lock.
- Preserve recognizable anchors (soft rounder face with cheek volume, thick black soft-rect glasses, short hard spiky hair, navy tee, watch, NB 2002R when full-body).
- Translate into vinyl-toy matte — FORBIDDEN photoreal / selfie / biometric 1:1 claim.
- Solo: NO Little Stone. Combo: flat 2D Little Stone only if Combo fragment attached.

## Style Application (vinyl-theater)
Apply style anchors from theater-styles/vinyl-theater/META.md:
- {style_anchors_rewritten}
Must preserve: {must_preserve}
Avoid: {avoid_when_applying_to_theater}

## Shape Application ({shape_id})
Apply shape anchors from theater-shapes/{shape_id}/META.md:
- {shape_anchors_rewritten}
Must preserve: {shape_must_preserve}
Avoid: {shape_avoid}

## Composition
- Primary center: {primary_visual_center}
- Character placement / scale: {character_placement}
- Modules / props / labels: {modules_props_labels}
- Reading path: {reading_path}

## Negative Constraints
- {banned_elements}
- outfit change; thin wire / gold round glasses; photo-real skin; path-B whiteboard; face-paste seams
- shape-specific failures: {shape_avoid}
- style-specific failures: {avoid_when_applying_to_theater}

## Final Standard
One final image only. Must satisfy:
1. Clearly a {shape_name} at {ratio}
2. Same person/outfit as APPROVED sheet
3. vinyl-theater is the visible rendering language
4. Shape budget respected
5. Delivers: {see_what}
```

---

## Compilation Notes

1. Read exactly one style: `ip-profiles/default-little-stone/theater-styles/vinyl-theater/{META,STYLE}.md`
2. Read exactly one shape META（一鱼两吃则先 A=`process-breakdown` 再 B=`core-action`）
3. Fill derived fields；长文禁止正文进 prompt
4. Rewrite anchors into natural prose — leave no `{placeholders}`
5. Save prompt file **before** image generation
6. Generate with bridge；若工具未返回本轮明确产物路径，不要扫目录猜图冒充
7. 交付附图 + 一句「这张让读者看见什么」

## 产物建议路径

```text
.validation-output/generation/theater/scenes/
  IMPRINT-PLAN.md                 # 本批计划
  prompts/{slug}-process.md       # 编译后的完整 prompt
  prompts/{slug}-action.md
  {slug}-process.png
  {slug}-action.png
```

一鱼两吃硬序：配方卡 → Plate A 预览身份 OK → Plate B 同金样 → 一起交。
