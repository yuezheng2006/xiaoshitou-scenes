import type {StyleId} from './types';

export type LayoutFamily =
  | 'editorial-opener'
  | 'grid-briefing'
  | 'grid-spotlight'
  | 'notebook-diary'
  | 'ink-poster'
  | 'storybook-plate'
  | 'scroll-vertical'
  | 'scroll-centerpiece'
  | 'newspaper-column'
  | 'newspaper-poster'
  | 'chalk-lesson'
  | 'blueprint-callout'
  | 'sticker-stage';
export type StylePreset = {
  background: string;
  ink: string;
  muted: string;
  accent: string;
  panel: string;
  headingFont: string;
  bodyFont: string;
  layout: LayoutFamily;
  texture: string;
};

export const presets: Record<StyleId, StylePreset> = {
  'warm-editorial': {background:'#F5F0E6',ink:'#27231F',muted:'#6E675F',accent:'#D77B55',panel:'#FFFCF5E8',headingFont:'"Noto Serif SC","Source Han Serif SC",SimSun,serif',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'editorial-opener',texture:'radial-gradient(#27231F12 0.8px, transparent 0.8px)'},
  'modern-grid': {background:'#F4F1E8',ink:'#121B2A',muted:'#596273',accent:'#2D63D8',panel:'#FBFAF5EE',headingFont:'DengXian,"Noto Sans SC",sans-serif',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'grid-spotlight',texture:'linear-gradient(#2D63D812 1px,transparent 1px),linear-gradient(90deg,#2D63D812 1px,transparent 1px)'},
  notebook: {background:'#FFFDF5',ink:'#263044',muted:'#6C7381',accent:'#E36E54',panel:'#FFFDF5EE',headingFont:'"ZCOOL KuaiLe",KaiTi,cursive',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'notebook-diary',texture:'repeating-linear-gradient(0deg,transparent 0 35px,#6D91C018 36px 37px)'},
  'ink-poster': {background:'#EFE8DA',ink:'#171512',muted:'#5E5850',accent:'#B9362A',panel:'#F7F0E4E8',headingFont:'"Ma Shan Zheng",STKaiti,KaiTi,cursive',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'ink-poster',texture:'radial-gradient(#17151218 0.9px, transparent 0.9px)'},
  'watercolor-storybook': {background:'#F7F1E8',ink:'#3C3530',muted:'#766D67',accent:'#5D8F83',panel:'#FFFDF4D9',headingFont:'"ZCOOL XiaoWei","Noto Serif SC",serif',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'storybook-plate',texture:'radial-gradient(#6C8A7C16 1px, transparent 1px)'},
  'calligraphy-scroll': {background:'#EEE4D0',ink:'#221F1B',muted:'#6D6255',accent:'#A53229',panel:'#F7EFDDE6',headingFont:'"Liu Jian Mao Cao","Long Cang",STKaiti,KaiTi,cursive',bodyFont:'"Noto Serif SC",SimSun,serif',layout:'scroll-centerpiece',texture:'linear-gradient(90deg,#5A4A3410 1px,transparent 1px)'},
  'retro-newspaper': {background:'#E8DFC9',ink:'#29251F',muted:'#696052',accent:'#9D2F28',panel:'#F0E6D2E8',headingFont:'"Noto Serif SC",SimSun,serif',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'newspaper-poster',texture:'radial-gradient(#29251F22 0.7px, transparent 0.7px)'},
  'chalk-classroom': {background:'#203D37',ink:'#F5F0DC',muted:'#C8CFBE',accent:'#F2B84B',panel:'#17322DEB',headingFont:'"ZCOOL KuaiLe","Microsoft YaHei",sans-serif',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'chalk-lesson',texture:'radial-gradient(#F5F0DC1B 0.8px, transparent 0.8px)'},
  'technical-blueprint': {background:'#153D69',ink:'#F4F7F7',muted:'#B8D0E4',accent:'#F19A4A',panel:'#0F3159E8',headingFont:'"Noto Sans SC",DengXian,sans-serif',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'blueprint-callout',texture:'linear-gradient(#FFFFFF12 1px,transparent 1px),linear-gradient(90deg,#FFFFFF12 1px,transparent 1px)'},
  'playful-sticker': {background:'#FFF2C9',ink:'#272431',muted:'#686275',accent:'#F05E71',panel:'#FFFDF3F0',headingFont:'"ZCOOL KuaiLe",YouYuan,cursive',bodyFont:'"Noto Sans SC","Microsoft YaHei",sans-serif',layout:'sticker-stage',texture:'radial-gradient(#5E64D515 1.2px, transparent 1.2px)'},
};
