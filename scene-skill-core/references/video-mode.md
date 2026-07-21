# 视频模式

## 定位

将小石头实物图/手绘图转化为 60-90 秒带旁白的动画讲解视频。

**核心理念**：
- 复用 scene-skill-core 的图片生成能力（**Codex imagen 工具** + 小石头 IP）
- 增加 TTS 语音合成（Fish Audio 优先）
- 使用 Remotion 渲染引擎组装成 MP4

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

### 阶段 0：需求确认
1. 确认主题和内容
2. 确认视频风格：
   - **实物图风格**（默认）：简笔物件小现场 + 旁白
   - **手绘图风格**：白板手绘解释 + 旁白
3. 确认时长：默认 60-90 秒（6-9 个场景）

### 阶段 1：生成脚本和分镜
1. 从用户内容提炼核心观点
2. 生成 6-9 个场景，每个场景包含：
   - **场景标题**（headline）：4-22 个中文字符
   - **旁白文案**（narration）：口语化讲解，15-25 字
   - **画面描述**（caption）：简短概括，在画面底部显示
   - **图片提示词**（imagePrompt）：用于 imagegen 生成插图
3. 生成 `plan.json`（符合 muyang-handdrawn-video 的格式）

### 阶段 2：生成场景插图
1. 使用 imagegen 为每个场景生成 1080×1440 竖版插图
2. **必须遵守小石头 IP 规范**：
   - 单锚点设定图 `primary-character-reference.png`
   - 2D Flat Lock + Limbs Lock
   - 实物图风格：白色背景 + 真实物件 + 小石头动作
   - 手绘图风格：白底黑线 + 红橙蓝批注 + 小石头概念动作
3. 保存到项目的 `public/images/<scene-id>.png`

### 阶段 3：生成连续旁白
1. 使用 Fish Audio 或 ElevenLabs 合成旁白音频
2. **连续模式**（默认）：整段旁白一次合成，保存为 `public/audio/narration.mp3`
3. 使用 `ffprobe` 测算实际音频时长
4. 更新 `plan.json` 中的场景时长和字幕时间戳

### 阶段 4：Remotion 渲染
1. 创建 Remotion 项目（从 `assets/remotion-template` 复制）
2. 应用视觉风格预设：
   - 实物图 → `warm-editorial` 或 `modern-grid`
   - 手绘图 → `chalk-classroom` 或 `notebook`
3. 应用动效预设（自动匹配风格）
4. 运行 `npm install` 和 `npm run render`
5. 输出 `out/video.mp4`

### 阶段 5：质量验证
1. 检查视频时长是否符合预期
2. 检查字幕是否同步
3. 检查旁白是否完整（未截断）
4. 检查小石头形象是否一致（Confirm Gate）
5. 运行 `scripts/verify_output.py` 自动检查

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
    "intensity": "medium"
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
      "image": "images/scene-01.png",
      "imagePrompt": "16:9, 纯白背景 #FFFFFF, 简笔物件小现场...",
      "accent": "#D77B55",
      "audio": "",
      "audioDurationSeconds": 4.5,
      "durationInFrames": 135
    }
  ]
}
```

### 关键字段说明
- `width` × `height`：固定 1080×1440（竖版），适配手机观看
- `style.id`：视觉风格，从 muyang 的 10 种预设中选择
- `motion.id`：动效风格，可省略（自动匹配 style）
- `voice.provider`：优先 `fish-audio`，备选 `elevenlabs`
- `voice.mode`：默认 `continuous`（连续旁白）
- `scenes[].imagePrompt`：必须符合小石头 IP 规范

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
16:9 横版，纯白背景 #FFFFFF，白色摄影棚表面，真实物件小现场。

主角色：
- 小石头：flat 2D 平涂胶囊体，简笔两臂两腿，白圆双眼无瞳孔，
  暖珊瑚红主色 #E06C5F，无嘴无装饰无服装无配件。
- 参考图：[传入 primary-character-reference.png 的路径]

物件：
- 使用真实物件（非 icon）：钱包、笔记本、日历、手机等
- 物件有光影，主角色保持 flat 2D
- 中等覆盖面积，视觉重量轻

文字：
- 1-3 个短中文标签（3-8 字），黑色，干净字体
- 禁止大段解释、UI 截图、Logo

约束：
- 禁止：粗黑框眼镜、黑长袖衣服、generic 人脸、3D 渲染、商业插画
```

### 手绘图场景
```
16:9 横版，纯白背景 #FFFFFF，黑色手绘线稿结构。

主角色：
- 小石头：flat 2D 平涂胶囊体（同实物图）
- 参考图：[传入 primary-character-reference.png 的路径]

结构：
- 黑色手绘线条：流程图、系统结构、方法拆解
- 3-5 个核心模块
- 5-8 个短批注（红色 #E74C3C / 橙色 #F39C12 / 蓝色 #3498DB）

约束：
- 禁止：真实物件光影、UI 截图、PPT 化、复杂架构图
```

---

## TTS 配置

### Fish Audio（推荐）
1. 用户需配置 `.env` 文件：
   ```
   FISH_API_KEY=your_key_here
   FISH_MODEL=s2.1-pro-free
   ```
2. 调用脚本：`python scripts/fish_audio_project.py --project <项目目录>`
3. 成本：约 ¥0.05/分钟

### ElevenLabs（备选）
1. 用户需配置 `.env` 文件：
   ```
   ELEVENLABS_API_KEY=your_key_here
   ```
2. 调用脚本：`python scripts/elevenlabs_project.py --project <项目目录> --auto-voice`
3. 仅使用中文/普通话声音，禁止英文声音配中文

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
- [ ] 运行 `python scripts/verify_output.py out/video.mp4 --plan src/generated/plan.json`

---

## 脚本文件清单

从 muyang-handdrawn-video 复制并适配的脚本：

```
scene-skill-core/
├── scripts/
│   ├── video_create_project.py     # 创建 Remotion 项目
│   ├── video_fish_audio.py         # Fish Audio TTS
│   ├── video_elevenlabs.py         # ElevenLabs TTS（备选）
│   └── video_verify_output.py     # 视频质量验证
└── assets/
    └── remotion-template/          # Remotion 模板（复制自 muyang）
        ├── package.json
        ├── remotion.config.ts
        └── src/
            ├── Explainer.tsx
            ├── Root.tsx
            ├── stylePresets.ts
            ├── motionPresets.ts
            └── types.ts
```

---

## 完整流程示例

### 用户输入
```
小石头视频：为什么存钱越早越轻松
```

### Agent 执行流程
```
1. 读取 video-mode.md
2. 生成脚本和分镜（6 个场景）
3. 创建 plan.json
4. 为每个场景调用 imagegen：
   - 读取 character.md（小石头 IP 规范）
   - 读取 physical-style-dna.md（实物图规则）
   - 生成 6 张 1080×1440 PNG
   - 做 Confirm Gate 检查
5. 创建 Remotion 项目：
   python scripts/video_create_project.py --plan plan.json --output video-project
6. 生成旁白：
   python scripts/video_fish_audio.py --project video-project
7. 渲染视频：
   cd video-project
   npm install
   npm run render
8. 验证输出：
   python ../scripts/video_verify_output.py out/video.mp4 --plan src/generated/plan.json
9. 交付：
   - 视频文件：video-project/out/video.mp4
   - 可编辑项目：video-project/
   - 脚本导出：video-project/script/
```

---

## 失败信号

| 失败信号 | 原因 | 解决方案 |
|---------|------|----------|
| 小石头形象不一致 | 未传设定图或 Lock 失效 | 重新生成，确保传入 primary-character-reference.png |
| 旁白截断 | 音频生成失败或时长计算错误 | 检查 TTS API 配置，重新生成音频 |
| 字幕不同步 | 音频时长未更新到 plan.json | 重新运行 TTS 脚本，确保更新时长 |
| 视频黑屏 | 图片文件缺失或路径错误 | 检查 public/images/ 目录，确保所有场景图片存在 |
| Remotion 渲染失败 | Node.js 版本过低或依赖缺失 | 升级 Node.js 到 18+，运行 npm install |
| 声音不自然 | TTS 参数不当 | 调整 Fish Audio 模型或 ElevenLabs 声音 |

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
- **图片生成**：6 张 × 约 ¥0.1 = ¥0.6（imagegen）
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
| BLOCKED | 缺少 TTS API 配置、Node.js 环境或 FFmpeg |

---

## 注意事项

1. **首次使用需配置环境**：
   - 安装 Node.js 18+
   - 安装 FFmpeg
   - 配置 Fish Audio API key
2. **图片必须符合小石头 IP 规范**，不能因为是视频就放松角色一致性
3. **连续旁白优先于分段旁白**，保证声音连贯
4. **视频时长控制在 60-90 秒**，过长用户难以看完
5. **字幕是强制的**，即使有旁白也要显示字幕（无声观看场景）
