# Video TTS · 旁白引擎契约（可替换）

## 用途

下游（字幕对齐、Remotion、交付检查）**只依赖产物契约**，不依赖具体 TTS 厂商。

换引擎 = 实现同一契约 + 在 `scripts/video_tts.py` 注册，不必改 Explainer / gates / align。

## 产物契约（continuous 默认）

| 产物 | 要求 |
|------|------|
| `public/audio/narration.mp3` | 整段旁白；音频是主时钟 |
| `plan.voice.provider` | `fish-audio` \| `external` \| `elevenlabs`（或自注册名） |
| `plan.voice.fullAudio` | 通常 `audio/narration.mp3` |
| `plan.scenes[].durationInFrames` | 按 `ffprobe` 总时长分配 |
| `src/generated/captions.json` | 草稿即可；终稿用 `video_align_captions.py` |

Segmented：每镜 `public/audio/<scene-id>.mp3` + `scene.audio`，同样以实测时长写 `durationInFrames`。

## 调用入口（唯一推荐）

```bash
python scripts/video_tts.py --project <dir>                          # 读 plan / VIDEO_TTS_PROVIDER
python scripts/video_tts.py --project <dir> --provider fish-audio
python scripts/video_tts.py --project <dir> --provider external --audio /path/voice.mp3
python scripts/video_tts.py --list-providers
```

然后：

```bash
python scripts/video_align_captions.py --project <dir>   # scripted
```

## 已注册 provider

| provider | 状态 | 后端 |
|----------|------|------|
| `fish-audio` | 已实现 | `video_fish_audio.py` |
| `external` | 已实现 | 自备音频，路由只负责 copy + 重算时长 |
| `elevenlabs` | 类型预留 | 补 `video_elevenlabs.py` 后在 `video_tts.py` 注册 |

## 新增引擎清单

1. 写 `scripts/video_<name>.py`，产出满足上表契约。
2. 在 `video_tts.py` 的 `KNOWN_PROVIDERS` + `main()` 分支注册。
3. 更新 `types.ts` 的 `VoiceConfig.provider` 联合类型。
4. 勿在 Remotion / Gate / align 里硬编码厂商名。

## 环境变量

```bash
VIDEO_TTS_PROVIDER=fish-audio   # 或 external / elevenlabs
# Fish only:
FISH_AUDIO_API_KEY=…            # 或 FISH_API_KEY
FISH_REFERENCE_ID=…             # 音色可换，最高频替换点
```

## 与门禁的关系

- Gate1 / Gate2 通过后再跑 TTS（贵步骤后置）。
- 换音色 / 换引擎 → 重跑 TTS + align；改字号 / captionLook → 只重渲。
- 改旁白音频后 Gate3 preview 哈希变 stale，须重批。
