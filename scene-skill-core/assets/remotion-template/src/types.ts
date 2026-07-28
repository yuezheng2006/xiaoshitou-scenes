export type StyleId =
  | 'warm-editorial' | 'modern-grid' | 'notebook' | 'ink-poster'
  | 'watercolor-storybook' | 'calligraphy-scroll' | 'retro-newspaper'
  | 'chalk-classroom' | 'technical-blueprint' | 'playful-sticker';

export type MotionId =
  | 'calm-explainer' | 'editorial-drift' | 'grid-scan' | 'notebook-flip'
  | 'poster-snap' | 'watercolor-float' | 'scroll-reveal' | 'newspaper-press'
  | 'chalk-write' | 'blueprint-scan' | 'sticker-pop';

export type CaptionLookId =
  | 'ink'          // 正文色，轻阴影（默认）
  | 'accent'       // 品牌强调色
  | 'soft'         // 深灰半透明字
  | 'pill-light'   // 浅底圆角条 + 深字
  | 'pill-dark'    // 深底圆角条 + 浅字
  | 'outline';     // 白描边深字，压在杂色图上更稳

export type StyleConfig = {
  id: StyleId;
  headingFont?: string;
  bodyFont?: string;
  /** QuietChrome 底部旁白字幕配色；默认 ink */
  captionLook?: CaptionLookId;
  /** 字幕距底边比例，0.08–0.22，默认 0.12 */
  captionBottomRatio?: number;
};

export type MotionConfig = {
  id?: MotionId;
  intensity?: 'low' | 'medium' | 'high';
  thesis?: string;
  anti_ppt?: boolean;
};
export type VoiceConfig = {
  provider: 'elevenlabs' | 'fish-audio';
  voiceId: string;
  voiceName?: string;
  modelId: string;
  mode?: 'continuous' | 'segmented';
  fullAudio?: string;
};
export type Scene = {
  id: string;
  headline: string;
  narration: string;
  caption?: string;
  stateChange?: string;
  characterAction?: string;
  narrativeJob?: string;
  image: string;
  imagePrompt?: string;
  accent?: string;
  audio?: string;
  audioDurationSeconds?: number;
  durationInFrames: number;
};
export type Plan = {
  topic: string;
  title: string;
  language?: string;
  fps: number;
  width: number;
  height: number;
  targetDurationSeconds?: number;
  style: StyleConfig;
  motion?: MotionConfig;
  voice: VoiceConfig;
  scenes: Scene[];
};
