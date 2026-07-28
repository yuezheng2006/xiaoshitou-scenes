# 视频模式

## 定位

**长视频 · 低成本 · 高 IP**：小石头竖版讲解片（默认 60–90 秒+）。

| 目标 | 做法 |
|------|------|
| 长视频 | 多镜叙事 + 连续旁白 + Remotion 组装；**音频是主时钟** |
| 低成本 | 贵步骤后置：Gate1 分镜确认 → 再生图；scripted 字幕；改字号/动效只重渲 |
| 高 IP | 小石头设定锁 + 图内禁止中文标签 + Remotion 统一大标题/小字幕 |

贵：`imagen × N` + 一条旁白。便宜：Remotion 重渲 / 字幕 / 切镜。

将小石头实物图/手绘图转化为带旁白的动画讲解视频。

**核心理念**：
- 复用 scene-skill-core 的图片生成能力（**Codex imagen 工具** + 小石头 IP）
- TTS / 字幕 / 版式按**契约可替换**（默认 Fish Audio）
- 使用 Remotion 渲染引擎组装成 MP4

### 可替换插槽（设计原则）

| 插槽 | 灵活度 | 换法 | 契约 |
|------|--------|------|------|
| TTS 引擎 | 高 | `video_tts.py --provider …` | `contracts/video-tts.md` → `narration.mp3` |
| 音色 ID | 最高 | `FISH_REFERENCE_ID` / `--reference-id` | 同上 |
| 自备旁白 | 高 | `--provider external --audio` | 同上 |
| 字幕对齐 | 中 | `video_align_captions.py --mode` | scripted 默认 |
| captionLook / 字号 | 高 | `plan.style` + 重渲 | QuietChrome |
| 分镜文案 | 高 | Gate1 前改 plan | handoff |
| imagen | 低 | 产品锁定 Codex imagen | IP 规范 |
| Remotion 模板 | 低 | 改 Explainer；整栈换 = 另一 skill | plan.json |

**⚠️ 工具硬性约束**：
- 场景插图生成**必须**使用 Codex 自带的 `imagen` 工具
- 不得使用外部 API（DALL-E、Midjourney 等）
- 不得要求用户自行生成图片后上传
- 详见 `codex-environment-guidance.md` § 三.5

---

## 触发方式

### 显式触发词
- **视频讲解** / **动画视频** / **手绘视频** / **配音视频**
- **讲解视频** / **带旁白的视频** / **小石头视频**

### 典型用户输入
```
小石头视频：为什么存钱越早越轻松
生成一个手绘视频解释这个工作流
把这篇内容做成 60 秒带旁白的动画
```

---

## 工作流

**生产门禁**（长视频·低成本·高 IP；吸收 gbro 三闸门 / 灵剪签名审批 / min-skill 音频主时钟）：

```text
check_setup → Gate1 分镜确认（approve storyboard）
→ imagen 仅通过镜 → contact sheet → Gate2 静帧确认（可部分通过）
→ video_tts.py（默认 fish-audio）→ align captions（scripted）
→ Remotion still → Gate3 preview 批准（哈希绑定）
→ full render → check_delivery
```

也可一条命令装配（已有 plan/images/audio 时）：
`bash scripts/video_build.sh <remotion项目> [--from still] [--only align,still] [--force]`

脚本：
- `bash scripts/video_check_setup.sh [项目]` — 缺什么只报缺失项
- `python scripts/video_approve.py --project <dir> --gate storyboard|stills|preview [--scenes scene-01,scene-03]`
- `python scripts/video_approve.py --project <dir> --check` — 内容变更则批准变 stale
- `python scripts/video_contact_sheet.py --project <dir>` — Gate2 编号总览

契约见 `contracts/video-handoff.md`；运动叙事见 `video-motion-director.md`。

### 从外部 skill 吸收的硬规则
1. **音频时长是主时钟**（min-skill）——`ffprobe` 实测旁白，再缩放分镜/字幕。
2. **不要用 ASR 转录自己的口播稿**（min-skill）——默认 `scripted`。
3. **图内不烧中文字**（本仓）——标题/字幕由 Remotion 统一字号。
4. **贵步骤后置 + 部分通过**（gbro）——先审分镜再生图；contact sheet 只放行通过镜。
5. **批准绑产物哈希**（灵剪）——改 plan/图/字幕后批准自动 stale，须重批。
6. **增量重跑**——`video_build.sh` 支持 `--from` / `--only` / `--force`。

### 什么时候不要用视频模式
- 只要 5 秒无旁白 B-roll / 半调拼贴垫片 → 用别的 skill
- 要发布级真动态口播短视频全栈（Seedance/多 TTS/导演台）→ 灵剪路线，不是本模式
- 要可逐层编辑时间线 → Remotion 源码级改，不要当黑箱一键片

### 阶段 0：交接与预检
1. `bash scripts/video_check_setup.sh <项目目录>`
2. 写 `handoff.md`（或确认用户已提供等价契约）
3. `python scripts/video_init_job_state.py --project <项目目录>`
4. 生成 `plan.json`（含 motion.thesis + 每镜 stateChange）后 **Gate1**：把分镜表给用户审；通过后：
   `python scripts/video_approve.py --project <dir> --gate storyboard`
5. `python scripts/video_preflight.py --project <项目目录> --require-tts`
6. 未 Gate1 批准，不得批量 imagen

### 阶段 0.5：运动叙事（Anti-PPT）
1. 读 `video-motion-director.md`
2. 写入一句 `plan.motion.thesis`
3. 每个场景补 `stateChange` + `characterAction`（可见状态变化，禁止纯切图）

### 阶段 1：生成脚本和分镜
1. 从用户内容提炼核心观点
2. 生成 6-9 个场景，每个场景包含：
   - **场景标题**（headline）：4-22 个中文字符
   - **旁白文案**（narration）：口语化讲解，15-25 字
   - **画面描述**（caption）：简短概括，叠在画面底部（Remotion 小字幕；图内禁止烧中文）
   - **状态变化**（stateChange）：这一镜画面上具体变了什么
   - **图片提示词**（imagePrompt）：用于 `imagen` 生成插图
3. 生成 `plan.json` → **先停在 Gate1**，给候选讲法时优先 2 版提纲让用户挑，不要只问「可以吗」

### 阶段 2：生成场景插图
1. 仅对 Gate1 `passed_scene_ids` 使用 Codex `imagen`（竖版；图内禁止中文标签）
2. **必须遵守小石头 IP 规范**
3. `python scripts/video_contact_sheet.py --project <dir>` → 用户审总览
4. 部分通过：`python scripts/video_approve.py --project <dir> --gate stills --scenes scene-01,scene-02,scene-04`
5. 未过镜只重生图，不整批重做

### 阶段 3：生成连续旁白
1. 经路由调用（推荐）：`python scripts/video_tts.py --project <项目目录>`
   - 默认 `fish-audio`（已实现）；或 `--provider external --audio voice.mp3`
   - 契约见 `contracts/video-tts.md`
2. **连续模式**（默认）：整段旁白 → `public/audio/narration.mp3`
3. `ffprobe` 实测时长，回写 `plan.json` 场景 `durationInFrames`
4. 直接调 `video_fish_audio.py` 仍可用（等价于 `--provider fish-audio`）

### 阶段 3.5：对齐字幕（终稿音频）
1. 旁白定稿后运行：
   `python scripts/video_align_captions.py --project <项目目录>`
   （默认 `--mode scripted`：已知旁白 × 实测音频，参考 [min-skill](https://github.com/limin112/min-skill)）
2. 可选 `--mode whisper-api` / `whisper-local`（未知音频才需要 ASR）
3. `timing_source=scripted|whisper-*` 可交付；`estimated` 仅草稿（见 `video_check_delivery.py`）

### 阶段 4：预览门禁 → Remotion 渲染
1. 创建 Remotion 项目（从 `assets/remotion-template` 复制）——若尚未创建
2. 应用视觉风格预设：
   - 实物图 → `warm-editorial` 或 `modern-grid`
   - 手绘图 → `chalk-classroom` 或 `notebook`
   - **小石头视频默认插图铺满**。Remotion 管全部文字：**大标题（约宽 7.8%）+ 小字幕（约宽 2.8%）**。**硬规则：图内禁止烧中文标签**；**禁止大面积底部蒙层**
3. 先出 still 预览：`npm run still` → `out/preview.png`
4. **Gate3**：`python scripts/video_approve.py --project <dir> --gate preview`（用户明确批准后）
5. 用户明确跳过预览门禁时才可直接全片渲染（delivery 须 `--allow-unapproved`）
6. `npm run render` → `out/video.mp4`


### 阶段 5：质量验证与交付
1. 检查视频时长是否符合预期
2. 检查字幕是否同步（`captions-meta.json` 的 timing_source）
3. 检查旁白是否完整（未截断）
4. 检查小石头形象是否一致（Confirm Gate）
5. 运行媒体规格检查：
   `python scripts/video_verify_output.py out/video.mp4 --plan src/generated/plan.json`
6. 运行交付门禁：
   `python scripts/video_check_delivery.py --project .`
   （草稿可用 `--allow-estimated --allow-unapproved`）
7. 改 plan/图/旁白后先 `video_approve.py --check`；出现 stale 必须重批对应闸门

---

## plan.json 格式

基于 muyang-handdrawn-video 的格式，适配小石头 IP：

```json
{
  "topic": "为什么存钱越早越轻松",
  "title": "存钱，越早越轻松",
  "language": "zh-CN",
  "fps": 30,
  "width": 1080,
  "height": 1440,
  "targetDurationSeconds": 75,
  "style": {
    "id": "warm-editorial",
    "headingFont": "Noto Sans SC, Microsoft YaHei, sans-serif",
    "bodyFont": "Noto Sans SC, Microsoft YaHei, sans-serif"
  },
  "motion": {
    "id": "editorial-drift",
    "intensity": "medium",
    "thesis": "空钱包散落到复利雪球长大，证明越早存越轻松",
    "anti_ppt": true
  },
  "voice": {
    "provider": "fish-audio",
    "voiceId": "auto",
    "voiceName": "auto",
    "modelId": "s2.1-pro-free",
    "mode": "continuous",
    "fullAudio": "audio/narration.mp3"
  },
  "scenes": [
    {
      "id": "scene-01",
      "headline": "月光族的困境",
      "narration": "每个月工资到手，还没捂热就花光了。",
      "caption": "月光族：工资秒光",
      "stateChange": "钱包摊开，钞票与收据散落",
      "characterAction": "双手扶头",
      "narrativeJob": "hook",
      "image": "images/scene-01.png",
      "imagePrompt": "1080x1440 vertical (3:4), pure white background #FFFFFF, miniature physical object scene...",
      "accent": "#f39800",
      "audio": "",
      "audioDurationSeconds": 4.5,
      "durationInFrames": 135
    }
  ]
}
```

### 关键字段说明
- `width` × `height`：**可设置**。常用竖版 `1080×1440`（3:4，默认）或 `1080×1920`（9:16）；横版可用 `1920×1080`。改 plan 后 Remotion 按此画布渲染；`video_preflight.py` 校验白名单尺寸。
- `style.id`：视觉风格，从 muyang 的 10 种预设中选择
- `style.captionLook`：QuietChrome 字幕配色（可选）：`ink`（默认）/ `accent` / `soft` / `pill-light` / `pill-dark` / `outline`
- `style.captionBottomRatio`：字幕区高度比例，默认 `0.11`–`0.12`（三区布局：顶标题 / 中插画 / 底字幕，互不叠压）
- `motion.id`：动效风格，可省略（自动匹配 style）
- `motion.thesis`：**必填**运动主张（见 `video-motion-director.md`）
- `scenes[].stateChange` / `characterAction`：可见状态变化与小石头动词
- `voice.provider`：默认 `fish-audio`；也可用 `external`（自备音频）或预留 `elevenlabs`。统一经 `video_tts.py` 路由，契约见 `contracts/video-tts.md`
- `voice.mode`：默认 `continuous`（连续旁白）
- `scenes[].imagePrompt`：必须符合小石头 IP 规范；**画布比例须与 plan.width/height 一致**（不要写错成 16:9 横构图去填竖版）

---

## 视觉风格映射

### 实物图风格 → muyang 风格
| scene-skill-core | muyang-handdrawn-video | 适用场景 |
|------------------|------------------------|----------|
| 实物图（默认） | `warm-editorial` | 金融、习惯、心理学 |
| 实物图（现代） | `modern-grid` | 商业、技术、系统 |
| 实物图（笔记） | `notebook` | 学习、成长、教程 |

### 手绘图风格 → muyang 风格
| scene-skill-core | muyang-handdrawn-video | 适用场景 |
|------------------|------------------------|----------|
| 手绘图（默认） | `chalk-classroom` | 科学、教学 |
| 手绘图（技术） | `technical-blueprint` | 工程、工作流 |
| 手绘图（笔记） | `notebook` | 流程拆解 |

---

## 图片生成约束

视频模式的图片生成**必须遵守**小石头 IP 规范：

### 实物图场景
```
1080×1440 竖版（3:4），纯白背景 #FFFFFF，白色摄影棚表面，真实物件小现场。

主角色：
- 小石头：flat 2D 平涂胶囊体，简笔两臂两腿，白圆双眼无瞳孔，
  主色以 `character.md` 为准（`#f39800` 橙实心体），无嘴无装饰无服装无配件。
- 参考图：[传入 primary-character-reference.png 的路径]

物件：
- 使用真实物件（非 icon）：钱包、笔记本、日历、手机等
- 物件有光影，主角色保持 flat 2D
- 中等覆盖面积，视觉重量轻；构图按竖版留白，避免按 16:9 横构图再裁切

文字：
- **视频模式硬规则：图内禁止任何中文标题/字幕/标签**（全部由 Remotion 统一字号叠：大标题 + 小字幕）
- 物件上的英文/字段示意可以保留（如 Task/Owner），但不要写中文说明字
- 禁止大段解释、UI 截图、Logo

约束：
- 禁止：粗黑框眼镜、黑长袖衣服、generic 人脸、3D 渲染、商业插画
```

### 手绘图场景
```
1080×1440 竖版（3:4），纯白背景 #FFFFFF，黑色手绘线稿结构。

主角色：
- 小石头：flat 2D 平涂胶囊体（同实物图）
- 参考图：[传入 primary-character-reference.png 的路径]

结构：
- 黑色手绘线条：流程图、系统结构、方法拆解
- 3-5 个核心模块
- 5-8 个短批注（红色 #E74C3C / 橙色 #F39C12 / 蓝色 #3498DB）

约束：
- 禁止：真实物件光影、UI 截图、PPT 化、复杂架构图；禁止写 16:9 横版
```

---

## TTS 配置（可替换）

统一入口：`python scripts/video_tts.py --project <dir>`（见 `contracts/video-tts.md`）。

### Fish Audio（默认后端）
1. `.env`：
   ```
   FISH_API_KEY=your_key_here
   FISH_MODEL=s2.1-pro-free
   # FISH_REFERENCE_ID=…   # 换音色（最高频替换点）
   # VIDEO_TTS_PROVIDER=fish-audio
   ```
2. `python scripts/video_tts.py --project <项目目录>`  
   或直调：`python scripts/video_fish_audio.py --project <项目目录>`
3. 成本：约 ¥0.05/分钟

### external（自备旁白）
```bash
python scripts/video_tts.py --project <dir> --provider external --audio /path/to/voice.mp3
```
路由只负责拷贝 + 按时长重算分镜；其后仍跑 scripted align。

### ElevenLabs（类型预留）
- `plan.voice.provider: "elevenlabs"` 可写；合成时 `video_tts.py` 会明确报未实现
- 临时方案：外部合成后走 `external`；长期：补 `video_elevenlabs.py` 并在路由注册

---

## QA 检查清单

### 生成前检查
- [ ] 已生成 plan.json，包含 6-9 个场景
- [ ] 每个场景的 imagePrompt 符合小石头 IP 规范
- [ ] 已选定视觉风格（warm-editorial / chalk-classroom 等）
- [ ] 旁白文案口语化，每句 15-25 字

### 图片生成后检查
- [ ] 每个场景都有 1080×1440 的 PNG 图片
- [ ] **小石头形象 Confirm Gate**：
  - L1 计数：恰好 2 臂 + 2 腿
  - L2 锚点：臂从体侧上 1/3、腿从底缘连续向下
  - E1 眼睛：两只白圆眼、批内一致
- [ ] 实物图：背景纯白、物件真实、留白充足
- [ ] 手绘图：白底黑线、批注克制、结构清晰

### 旁白生成后检查
- [ ] 音频文件存在且可播放
- [ ] 音频时长与脚本匹配（无截断）
- [ ] 声音自然（非机器人腔）

### 视频渲染后检查
- [ ] 视频时长符合预期（60-90 秒）
- [ ] 字幕与旁白同步
- [ ] 场景切换流畅
- [ ] 标题、图片、字幕都清晰可见
- [ ] 无黑屏、无闪烁
- [ ] 字幕已对齐（`captions-meta.json` timing_source ≠ estimated，或明确草稿）
- [ ] 运行 `python scripts/video_verify_output.py out/video.mp4 --plan src/generated/plan.json`
- [ ] 运行 `python scripts/video_check_delivery.py --project .`（交付）

---

## 脚本文件清单

```
scene-skill-core/
├── scripts/
│   ├── video_check_setup.sh        # 环境自检
│   ├── video_create_project.py     # 创建 Remotion 项目
│   ├── video_init_job_state.py     # job-state + 三闸门
│   ├── video_approve.py            # Gate1/2/3 哈希批准
│   ├── video_contact_sheet.py      # Gate2 contact sheet
│   ├── video_preflight.py          # 付费/批量步骤前预检
│   ├── video_tts.py                # TTS 路由（可替换引擎）
│   ├── video_fish_audio.py         # Fish Audio 后端
│   ├── video_align_captions.py     # scripted 字幕
│   ├── video_build.sh              # align→still→render→check
│   ├── video_verify_output.py      # 媒体规格
│   └── video_check_delivery.py     # 交付门禁（含 stale）
└── assets/
    └── remotion-template/
```

---

## 完整流程示例

### 用户输入
```
小石头视频：为什么存钱越早越轻松
```

### Agent 执行流程
```
1. video_check_setup.sh + 读 video-mode / motion-director / video-handoff
2. 写 motion.thesis 与 6 场景 plan → Gate1 给用户审
   python scripts/video_approve.py --project video-project --gate storyboard
3. 创建项目 / init job-state / preflight
4. imagen 仅通过镜（图内无中文）→ contact_sheet → Gate2
   python scripts/video_approve.py --project video-project --gate stills
5. video_tts.py 旁白 → video_align_captions.py（scripted）
6. npm run still → Gate3 approve preview → npm run render
7. video_check_delivery.py
```

---

## 失败信号

| 失败信号 | 原因 | 解决方案 |
|---------|------|----------|
| 小石头形象不一致 | 未传设定图或 Lock 失效 | 重新生成，确保传入 primary-character-reference.png |
| 旁白截断 | 音频生成失败或时长计算错误 | 检查 TTS API 配置，重新生成音频 |
| 字幕不同步 | 未按终稿音频对齐 | 跑 `video_align_captions.py`（默认 scripted）；勿用 estimated 当交付 |
| 字幕字号乱飘 / 双字幕 | 图内烧了中文标签 | 生图禁止中文；Remotion 叠大标题+小时长字幕 |
| 底部被白块挡住 | 大面积底部蒙层 | 禁止底部蒙层；字幕用固定小字号叠层 |
| 预览未批就全片 | 跳过 Gate3 | still 后 `video_approve.py --gate preview`；改产物后 `--check` 见 stale 须重批 |
| 视频黑屏 | 图片文件缺失或路径错误 | 检查 public/images/ 目录，确保所有场景图片存在 |
| Remotion 渲染失败 | Node.js 版本过低或依赖缺失 | 升级 Node.js 到 18+，运行 npm install |
| 声音不自然 | TTS 参数不当 | 换 `FISH_REFERENCE_ID` / provider，或 `--provider external` 自备旁白 |
| 幻灯片感 | 无 motion thesis / stateChange | 读 `video-motion-director.md` 重写分镜 |

---

## 与其他模式的关系

- **实物图模式** → 视频模式：复用实物图生成能力，增加旁白和动效
- **手绘图模式** → 视频模式：复用手绘图生成能力，增加旁白和动效
- **知识卡模式**：暂不支持视频化（竖版静态图更适合收藏传播）
- **PPT 演讲模式**：暂不支持视频化（多页演讲有独立录屏需求）

---

## 未来扩展方向

1. **支持老杨双 IP 视频**：老杨主讲 + 小石头执行
2. **支持更长视频**：3-5 分钟（15-25 个场景）
3. **支持横版视频**：16:9 适配 B 站、YouTube
4. **支持动态镜头**：AI 视频生成模型（Runway、Pika）
5. **支持背景音乐**：情绪增强
6. **支持多语言**：英文旁白 + 英文字幕

---

## 成本估算

### 单个 60 秒视频（6 个场景）
- **图片生成**：6 张 × 约 ¥0.1 = ¥0.6（Codex `imagen`）
- **语音合成**：1 分钟 × ¥0.05 = ¥0.05（Fish Audio）
- **视频渲染**：本地免费（Remotion 开源）
- **总成本**：约 ¥0.65

### 时间成本
- 生成脚本：1-2 分钟
- 生成图片：6 张 × 30 秒 = 3 分钟
- 生成旁白：30 秒
- 渲染视频：1-2 分钟
- **总时间**：约 5-8 分钟

---

## Completion States

| 状态 | 含义 |
|------|------|
| DONE | 视频已生成并通过 QA 检查 |
| DONE_WITH_CONCERNS | 视频已交付，但存在字幕稳定性、声音自然度等待优化项 |
| BLOCKED | 缺少 TTS 就绪（Fish key 或 external 音频）、Node.js 环境或 FFmpeg |

---

## 注意事项

1. **首次使用需配置环境**：
   - 安装 Node.js 18+
   - 安装 FFmpeg
   - TTS：默认配置 Fish Audio API key；或准备自备旁白走 `video_tts.py --provider external`
2. **图片必须符合小石头 IP 规范**，不能因为是视频就放松角色一致性
3. **连续旁白优先于分段旁白**，保证声音连贯；统一经 `video_tts.py`，下游只认 `narration.mp3` 契约
4. **视频时长控制在 60-90 秒**，过长用户难以看完
5. **字幕是强制的**，即使有旁白也要显示字幕（无声观看场景）
