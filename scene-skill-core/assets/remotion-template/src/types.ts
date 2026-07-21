export type StyleId =
  | 'warm-editorial' | 'modern-grid' | 'notebook' | 'ink-poster'
  | 'watercolor-storybook' | 'calligraphy-scroll' | 'retro-newspaper'
  | 'chalk-classroom' | 'technical-blueprint' | 'playful-sticker';

export type MotionId =
  | 'calm-explainer' | 'editorial-drift' | 'grid-scan' | 'notebook-flip'
  | 'poster-snap' | 'watercolor-float' | 'scroll-reveal' | 'newspaper-press'
  | 'chalk-write' | 'blueprint-scan' | 'sticker-pop';

export type StyleConfig = {id: StyleId; headingFont?: string; bodyFont?: string};
export type MotionConfig = {id?: MotionId; intensity?: 'low' | 'medium' | 'high'};
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
