import type {MotionId, StyleId} from './types';

export type MotionTexture = 'paper' | 'grid' | 'dust' | 'ink' | 'chalk' | 'blueprint' | 'stickers';
export type MotionAccent = 'underline' | 'scan' | 'stamp' | 'wipe' | 'chalk' | 'none';

export type MotionPreset = {
  id: MotionId;
  enterFrames: number;
  titleFrom: {x: number; y: number};
  captionFrom: {x: number; y: number};
  artScale: [number, number];
  artDrift: {x: number; y: number; rotate: number};
  texture: MotionTexture;
  accent: MotionAccent;
};

export const styleMotionMap: Record<StyleId, MotionId> = {
  'warm-editorial': 'editorial-drift',
  'modern-grid': 'grid-scan',
  notebook: 'notebook-flip',
  'ink-poster': 'poster-snap',
  'watercolor-storybook': 'watercolor-float',
  'calligraphy-scroll': 'scroll-reveal',
  'retro-newspaper': 'newspaper-press',
  'chalk-classroom': 'chalk-write',
  'technical-blueprint': 'blueprint-scan',
  'playful-sticker': 'sticker-pop',
};

export const motionPresets: Record<MotionId, MotionPreset> = {
  'calm-explainer': {
    id: 'calm-explainer',
    enterFrames: 18,
    titleFrom: {x: 0, y: 18},
    captionFrom: {x: 0, y: 20},
    artScale: [1.025, 1],
    artDrift: {x: 4, y: -7, rotate: 0},
    texture: 'paper',
    accent: 'underline',
  },
  'editorial-drift': {
    id: 'editorial-drift',
    enterFrames: 20,
    titleFrom: {x: 0, y: 24},
    captionFrom: {x: 0, y: 18},
    artScale: [1.035, 1.01],
    artDrift: {x: 6, y: -10, rotate: -0.2},
    texture: 'paper',
    accent: 'underline',
  },
  'grid-scan': {
    id: 'grid-scan',
    enterFrames: 16,
    titleFrom: {x: -22, y: 0},
    captionFrom: {x: -16, y: 0},
    artScale: [1.02, 1],
    artDrift: {x: -8, y: 0, rotate: 0},
    texture: 'grid',
    accent: 'scan',
  },
  'notebook-flip': {
    id: 'notebook-flip',
    enterFrames: 18,
    titleFrom: {x: -14, y: 20},
    captionFrom: {x: 0, y: 24},
    artScale: [1.04, 1],
    artDrift: {x: 4, y: -8, rotate: -0.35},
    texture: 'paper',
    accent: 'wipe',
  },
  'poster-snap': {
    id: 'poster-snap',
    enterFrames: 10,
    titleFrom: {x: 0, y: -18},
    captionFrom: {x: 0, y: 18},
    artScale: [1.08, 1],
    artDrift: {x: 0, y: 0, rotate: -0.15},
    texture: 'ink',
    accent: 'stamp',
  },
  'watercolor-float': {
    id: 'watercolor-float',
    enterFrames: 24,
    titleFrom: {x: 0, y: 18},
    captionFrom: {x: 0, y: 18},
    artScale: [1.03, 1],
    artDrift: {x: 7, y: -12, rotate: 0.18},
    texture: 'paper',
    accent: 'none',
  },
  'scroll-reveal': {
    id: 'scroll-reveal',
    enterFrames: 24,
    titleFrom: {x: 0, y: -30},
    captionFrom: {x: 0, y: 24},
    artScale: [1.02, 1],
    artDrift: {x: 0, y: -8, rotate: 0},
    texture: 'ink',
    accent: 'wipe',
  },
  'newspaper-press': {
    id: 'newspaper-press',
    enterFrames: 14,
    titleFrom: {x: 0, y: -12},
    captionFrom: {x: 12, y: 0},
    artScale: [1.045, 1],
    artDrift: {x: 3, y: -4, rotate: -0.05},
    texture: 'paper',
    accent: 'stamp',
  },
  'chalk-write': {
    id: 'chalk-write',
    enterFrames: 22,
    titleFrom: {x: -18, y: 10},
    captionFrom: {x: 0, y: 16},
    artScale: [1.025, 1],
    artDrift: {x: 4, y: -6, rotate: 0},
    texture: 'chalk',
    accent: 'chalk',
  },
  'blueprint-scan': {
    id: 'blueprint-scan',
    enterFrames: 18,
    titleFrom: {x: -18, y: 0},
    captionFrom: {x: 0, y: 16},
    artScale: [1.018, 1],
    artDrift: {x: -5, y: 0, rotate: 0},
    texture: 'blueprint',
    accent: 'scan',
  },
  'sticker-pop': {
    id: 'sticker-pop',
    enterFrames: 14,
    titleFrom: {x: 0, y: -14},
    captionFrom: {x: 0, y: 20},
    artScale: [0.94, 1],
    artDrift: {x: 5, y: -9, rotate: 0.4},
    texture: 'stickers',
    accent: 'stamp',
  },
};

export const getMotionPreset = (styleId: StyleId, motionId?: MotionId): MotionPreset => {
  return motionPresets[motionId ?? styleMotionMap[styleId] ?? 'calm-explainer'];
};
