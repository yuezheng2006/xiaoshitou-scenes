import React, {type CSSProperties} from 'react';
import type {Caption} from '@remotion/captions';
import {Audio} from '@remotion/media';
import {AbsoluteFill,Easing,Img,Sequence,interpolate,staticFile,useCurrentFrame,useVideoConfig} from 'remotion';
import captionJson from './generated/captions.json';
import {getMotionPreset,type MotionPreset} from './motionPresets';
import {presets,type LayoutFamily,type StylePreset} from './stylePresets';
import type {CaptionLookId,Plan,Scene} from './types';

const captionMap = captionJson as Record<string, Caption[]>;

const num = (index: number) => String(index + 1).padStart(2, '0');

const titleStyle = (fontFamily: string, preset: StylePreset, size = 86): CSSProperties => ({
  margin: 0,
  fontFamily,
  fontSize: size,
  fontWeight: 800,
  lineHeight: 1.15,
  letterSpacing: size >= 52 ? 0.5 : 0,
  color: preset.ink,
  whiteSpace: 'pre-line',
});

const captionStyle = (fontFamily: string, preset: StylePreset): CSSProperties => ({
  fontFamily,
  fontSize: 42,
  fontWeight: 650,
  lineHeight: 1.36,
  letterSpacing: 0,
  color: preset.ink,
});

const easeOut = Easing.bezier(0.16, 1, 0.3, 1);
const clamp = {extrapolateLeft:'clamp' as const,extrapolateRight:'clamp' as const};

const enterValue = (frame: number, frames: number) =>
  interpolate(frame,[0,frames],[0,1],{...clamp,easing:easeOut});

const motionShift = (frame: number, enter: number, from: {x: number; y: number}) => ({
  opacity: enter,
  translate: `${interpolate(enter,[0,1],[from.x,0],clamp)}px ${interpolate(enter,[0,1],[from.y,0],clamp)}px`,
});

const Art: React.FC<{
  scene: Scene;
  preset: StylePreset;
  motion: MotionPreset;
  boxed?: boolean;
  fit?: CSSProperties['objectFit'];
}> = ({scene,preset,motion,boxed = false,fit = 'contain'}) => {
  const frame = useCurrentFrame();
  const enter = enterValue(frame,motion.enterFrames + 8);
  const drift = Math.sin(frame / 45);
  const draw = interpolate(frame,[0,Math.max(14,motion.enterFrames + 14)],[0,1],clamp);
  const focus = interpolate(frame,[0,40],[0,1],{...clamp,easing:easeOut});
  return <div style={{
    position:'relative',
    width:'100%',
    height:'100%',
    minHeight:0,
    overflow:'hidden',
    border:boxed ? `3px solid ${preset.ink}32` : undefined,
    background:boxed ? preset.panel : undefined,
    boxShadow:boxed ? `12px 14px 0 ${scene.accent ?? preset.accent}28` : undefined,
    opacity:interpolate(enter,[0,1],[0.18,1],clamp),
    scale:interpolate(focus,[0,1],motion.artScale,clamp),
    translate:`${motion.artDrift.x * drift}px ${motion.artDrift.y * (0.5 + 0.5 * drift)}px`,
    rotate:`${motion.artDrift.rotate * drift}deg`,
  }}>
    <Img src={staticFile(scene.image)} style={{
      width:'100%',
      height:'100%',
      objectFit:fit,
      filter:`contrast(${interpolate(draw,[0,1],[0.82,1],clamp)}) saturate(${interpolate(draw,[0,1],[0.72,1.04],clamp)})`,
    }}/>
    <div style={{
      position:'absolute',
      inset:0,
      background:`linear-gradient(90deg, ${preset.background} 0%, ${preset.background} 28%, transparent 48%, transparent 100%)`,
      translate:`${interpolate(draw,[0,1],[0,120],clamp)}% 0px`,
      opacity:0.28,
      mixBlendMode:'multiply',
      pointerEvents:'none',
    }}/>
  </div>;
};

/** QuietChrome bottom caption looks (plan.style.captionLook). */
const captionLooks = {
  ink: (preset: StylePreset) => ({
    color: preset.ink,
    background: 'transparent' as const,
    padding: '8px 4px' as const,
    borderRadius: 0,
    textShadow: `0 2px 16px ${preset.background}, 0 0 4px ${preset.background}`,
  }),
  accent: (preset: StylePreset) => ({
    color: preset.accent,
    background: 'transparent' as const,
    padding: '8px 4px' as const,
    borderRadius: 0,
    textShadow: `0 2px 14px ${preset.background}, 0 0 3px ${preset.background}`,
  }),
  soft: (preset: StylePreset) => ({
    color: `${preset.ink}CC`,
    background: 'transparent' as const,
    padding: '8px 4px' as const,
    borderRadius: 0,
    textShadow: `0 1px 10px ${preset.background}`,
  }),
  'pill-light': (preset: StylePreset) => ({
    color: preset.ink,
    background: `${preset.background}F2`,
    padding: '12px 22px' as const,
    borderRadius: 18,
    textShadow: 'none' as const,
  }),
  'pill-dark': (preset: StylePreset) => ({
    color: preset.background,
    background: `${preset.ink}E8`,
    padding: '12px 22px' as const,
    borderRadius: 18,
    textShadow: 'none' as const,
  }),
  outline: (preset: StylePreset) => ({
    color: preset.ink,
    background: 'transparent' as const,
    padding: '8px 4px' as const,
    borderRadius: 0,
    textShadow: [
      `0 0 2px ${preset.background}`,
      `1px 0 0 ${preset.background}`,
      `-1px 0 0 ${preset.background}`,
      `0 1px 0 ${preset.background}`,
      `0 -1px 0 ${preset.background}`,
      `0 2px 12px ${preset.background}`,
    ].join(', '),
  }),
} as const;

/** Three-band QuietChrome: title / stage / caption — art never fights type. */
const QuietChromeStage: React.FC<{
  scene: Scene;
  preset: StylePreset;
  index: number;
  headingFont: string;
  bodyFont: string;
  motion: MotionPreset;
  captionText?: string;
  issueRight?: boolean;
  captionLook?: CaptionLookId;
  captionBottomRatio?: number;
}> = ({
  scene,preset,index,headingFont,bodyFont,motion,captionText,issueRight = false,
  captionLook = 'ink',
  captionBottomRatio = 0.11,
}) => {
  const frame = useCurrentFrame();
  const {width,height} = useVideoConfig();
  const titleEnter = enterValue(frame,motion.enterFrames);
  const captionEnter = enterValue(frame,motion.enterFrames + 8);
  const titleMotion = motionShift(frame,titleEnter,motion.titleFrom);
  const captionMotion = motionShift(frame,captionEnter,motion.captionFrom);
  const accent = scene.accent ?? preset.accent;
  const issue = num(index);

  // Vertical rhythm for 3:4 / 9:16 explainers
  const padX = Math.round(width * 0.07);
  const titleTop = Math.round(height * 0.042);
  const titleBand = Math.round(height * 0.168);
  const captionBand = Math.round(height * Math.min(0.15, Math.max(0.1, captionBottomRatio ?? 0.11)));
  const stageGap = Math.round(height * 0.012);
  const stageTop = titleTop + titleBand + stageGap;
  const stageBottom = captionBand + stageGap;

  const titleSize = Math.round(Math.min(72, Math.max(52, width * 0.058)));
  const captionSize = Math.round(Math.min(32, Math.max(26, width * 0.026)));
  const issueSize = Math.round(titleSize * 0.32);
  const shadow = `0 2px 18px ${preset.background}, 0 0 5px ${preset.background}`;

  const caption = (captionText || scene.caption || '').trim();
  const showCaption = caption.length > 0 && caption !== scene.headline.trim();
  const look = (captionLooks as Record<string, typeof captionLooks.ink>)[captionLook ?? 'ink'] ?? captionLooks.ink;
  const lookStyle = look(preset);

  return <main style={{position:'absolute',inset:0,background:preset.background}}>
    {/* Content stage — reserved middle band */}
    <div style={{
      position:'absolute',
      top:stageTop,
      bottom:stageBottom,
      left:padX,
      right:padX,
      display:'flex',
      alignItems:'center',
      justifyContent:'center',
    }}>
      <div style={{width:'100%',height:'100%',minHeight:0}}>
        <Art scene={scene} preset={preset} motion={motion} fit="contain"/>
      </div>
    </div>

    {/* Title band wash */}
    <div style={{
      position:'absolute',left:0,right:0,top:0,height:stageTop,pointerEvents:'none',
      background:`linear-gradient(180deg, ${preset.background} 0%, ${preset.background}F2 62%, ${preset.background}00 100%)`,
    }}/>
    {/* Caption band wash */}
    <div style={{
      position:'absolute',left:0,right:0,bottom:0,height:stageBottom,pointerEvents:'none',
      background:`linear-gradient(0deg, ${preset.background} 0%, ${preset.background}F2 58%, ${preset.background}00 100%)`,
    }}/>

    <header style={{
      position:'absolute',left:padX,right:padX,top:titleTop,height:titleBand,
      display:'flex',flexDirection:issueRight ? 'row' : 'column',
      alignItems:issueRight ? 'flex-start' : 'flex-start',
      justifyContent:issueRight ? 'space-between' : 'flex-start',
      gap:issueRight ? 16 : 8,
      ...titleMotion,
      zIndex:4,
    }}>
      {issueRight ? <>
        <div style={{flex:1,minWidth:0}}>
          <h1 style={{...titleStyle(headingFont,preset,titleSize),textShadow:shadow}}>{scene.headline}</h1>
          <div style={{marginTop:10,width:Math.round(width * 0.12),height:3,background:accent,borderRadius:2,opacity:0.85}}/>
        </div>
        <div style={{fontFamily:bodyFont,fontSize:issueSize,fontWeight:800,color:accent,opacity:0.95,paddingTop:4,textShadow:shadow}}>{issue}</div>
      </> : <>
        <div style={{fontFamily:bodyFont,fontSize:issueSize,fontWeight:800,color:accent,letterSpacing:1.4,opacity:0.95,textShadow:shadow}}>{issue}</div>
        <h1 style={{...titleStyle(headingFont,preset,titleSize),maxWidth:'96%',textShadow:shadow}}>{scene.headline}</h1>
        <div style={{marginTop:4,width:Math.round(width * 0.1),height:3,background:accent,borderRadius:2,opacity:0.85}}/>
      </>}
    </header>

    {showCaption ? <div style={{
      position:'absolute',left:padX,right:padX,bottom:0,height:captionBand,
      display:'flex',alignItems:'center',justifyContent:'center',...captionMotion,
      zIndex:5,
    }}>
      <div style={{
        fontFamily:bodyFont,fontSize:captionSize,fontWeight:650,lineHeight:1.45,
        letterSpacing:0.6,textAlign:'center',maxWidth:'92%',
        color:lookStyle.color,
        background:lookStyle.background,
        padding:lookStyle.padding,
        borderRadius:lookStyle.borderRadius,
        textShadow:lookStyle.textShadow,
      }}>{caption}</div>
    </div> : null}
  </main>;
};

/** @deprecated name kept for call sites — use QuietChromeStage */
const QuietChromeOverlay = QuietChromeStage;

const CaptionBlock: React.FC<{
  text: string;
  preset: StylePreset;
  bodyFont: string;
  accent: string;
  motion: MotionPreset;
  variant?: 'bar' | 'note' | 'dark' | 'inline' | 'side';
}> = ({text,preset,bodyFont,accent,motion,variant = 'bar'}) => {
  const frame = useCurrentFrame();
  const enter = enterValue(frame,motion.enterFrames + 10);
  const underline = interpolate(enter,[0,1],[0,1],clamp);
  const dark = variant === 'dark';
  const quiet = variant === 'bar' || variant === 'inline';
  return <div style={{
    ...captionStyle(bodyFont,preset),
    ...motionShift(frame,enter,motion.captionFrom),
    fontSize:variant === 'side' ? 30 : variant === 'note' ? 34 : quiet ? 34 : 40,
    background:dark ? `${preset.ink}E6` : quiet ? 'transparent' : preset.panel,
    color:dark ? preset.background : preset.ink,
    borderTop:variant === 'bar' ? `2px solid ${accent}55` : undefined,
    borderLeft:variant === 'side' || variant === 'note' ? `3px solid ${accent}` : undefined,
    padding:variant === 'inline' ? '4px 0 0' : quiet ? '10px 4px 0' : '14px 18px',
    boxShadow:quiet || variant === 'inline' ? undefined : `0 8px 24px ${preset.ink}10`,
    textAlign:variant === 'side' ? 'left' : 'center',
  }}>
    <span>{text}</span>
    {variant !== 'inline' && variant !== 'bar' && <div style={{
      height:2,
      width:'100%',
      background:accent,
      marginTop:8,
      transformOrigin:'left center',
      scale:`${underline} 1`,
      opacity:0.45,
    }}/>}
  </div>;
};

const Layout: React.FC<{
  layout: LayoutFamily;
  scene: Scene;
  preset: StylePreset;
  index: number;
  headingFont: string;
  bodyFont: string;
  text: string;
  motion: MotionPreset;
  captionLook?: CaptionLookId;
  captionBottomRatio?: number;
}> = ({layout,scene,preset,index,headingFont,bodyFont,text,motion,captionLook,captionBottomRatio}) => {
  const frame = useCurrentFrame();
  const titleEnter = enterValue(frame,motion.enterFrames);
  const accent = scene.accent ?? preset.accent;
  const issue = num(index);
  const titleMotion = motionShift(frame,titleEnter,motion.titleFrom);
  const common = {scene,preset,motion};
  const quietProps = {scene,preset,index,headingFont,bodyFont,motion,captionText:text,captionLook,captionBottomRatio};

  if (layout === 'grid-briefing') {
    return <main style={{position:'absolute',inset:'86px 72px 86px',display:'grid',gridTemplateColumns:'340px 1fr',gap:34}}>
      <aside style={{display:'flex',flexDirection:'column',justifyContent:'space-between',borderRight:`3px solid ${accent}`,paddingRight:28}}>
        <div style={titleMotion}>
          <div style={{fontFamily:bodyFont,fontSize:32,fontWeight:800,color:accent,marginBottom:30}}>{issue}</div>
          <h1 style={titleStyle(headingFont,preset,60)}>{scene.headline}</h1>
        </div>
        <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="side"/>
      </aside>
      <Art {...common} boxed/>
    </main>;
  }

  if (layout === 'grid-spotlight') {
    return <main style={{position:'absolute',inset:'72px 76px 82px',display:'grid',gridTemplateRows:'auto 1fr auto',gap:26}}>
      <header style={{display:'grid',gridTemplateColumns:'96px 1fr',alignItems:'start',gap:22,borderBottom:`4px solid ${accent}`,paddingBottom:18,...titleMotion}}>
        <div style={{fontFamily:bodyFont,fontSize:30,fontWeight:900,color:accent,letterSpacing:1}}>{issue}</div>
        <h1 style={titleStyle(headingFont,preset,78)}>{scene.headline}</h1>
      </header>
      <section style={{position:'relative',display:'grid',placeItems:'center',minHeight:0}}>
        <div style={{position:'absolute',inset:'34px 38px',border:`2px solid ${accent}26`,boxShadow:`18px 18px 0 ${accent}12`}}/>
        <div style={{width:'82%',height:'88%',background:preset.panel,padding:28,boxShadow:`0 30px 80px ${preset.ink}12`}}>
          <Art {...common} boxed/>
        </div>
        <div style={{position:'absolute',left:6,top:28,width:68,height:68,borderTop:`5px solid ${accent}`,borderLeft:`5px solid ${accent}`,opacity:0.72}}/>
        <div style={{position:'absolute',right:6,bottom:28,width:68,height:68,borderRight:`5px solid ${accent}`,borderBottom:`5px solid ${accent}`,opacity:0.72}}/>
      </section>
      <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="bar"/>
    </main>;
  }

  if (layout === 'notebook-diary') {
    return <QuietChromeStage {...quietProps}/>;
  }

  if (layout === 'ink-poster') {
    return <main style={{position:'absolute',inset:'82px 72px 84px',display:'grid',gridTemplateRows:'auto 1fr auto',gap:24}}>
      <header style={{display:'grid',gridTemplateColumns:'1fr 104px',gap:20,alignItems:'start',...titleMotion}}>
        <h1 style={titleStyle(headingFont,preset,96)}>{scene.headline}</h1>
        <div style={{height:104,background:accent,color:preset.background,fontFamily:bodyFont,fontSize:38,fontWeight:900,display:'flex',alignItems:'center',justifyContent:'center'}}>{issue}</div>
      </header>
      <Art {...common} boxed fit="cover"/>
      <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="dark"/>
    </main>;
  }

  if (layout === 'storybook-plate') {
    return <main style={{position:'absolute',inset:'86px 82px 86px',display:'grid',gridTemplateRows:'auto 1fr auto',gap:28,textAlign:'center'}}>
      <header style={titleMotion}>
        <div style={{fontFamily:bodyFont,fontSize:28,fontWeight:800,color:accent,marginBottom:10}}>{issue}</div>
        <h1 style={{...titleStyle(headingFont,preset,82),textAlign:'center'}}>{scene.headline}</h1>
      </header>
      <div style={{borderRadius:28,overflow:'hidden',background:preset.panel,padding:26,boxShadow:`0 24px 70px ${preset.ink}14`}}>
        <Art {...common}/>
      </div>
      <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="inline"/>
    </main>;
  }

  if (layout === 'scroll-vertical') {
    return <main style={{position:'absolute',inset:'76px 84px 82px',display:'grid',gridTemplateColumns:'170px 1fr',gap:34}}>
      <header style={{display:'flex',alignItems:'center',justifyContent:'center',background:preset.panel,borderLeft:`5px solid ${accent}`,borderRight:`1px solid ${preset.ink}22`,...titleMotion}}>
        <h1 style={{...titleStyle(headingFont,preset,70),writingMode:'vertical-rl',textOrientation:'mixed',lineHeight:1.1,maxHeight:920}}>{scene.headline}</h1>
      </header>
      <section style={{display:'grid',gridTemplateRows:'1fr auto',gap:24}}>
        <Art {...common}/>
        <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="note"/>
      </section>
      <div style={{position:'absolute',left:116,top:18,fontFamily:bodyFont,fontSize:28,fontWeight:800,color:accent}}>{issue}</div>
    </main>;
  }

  if (layout === 'scroll-centerpiece') {
    return <main style={{position:'absolute',inset:'72px 78px 82px',display:'grid',gridTemplateRows:'auto 1fr auto',gap:24,textAlign:'center'}}>
      <header style={{...titleMotion,borderTop:`4px solid ${accent}`,borderBottom:`1px solid ${preset.ink}26`,padding:'22px 28px 18px',background:`linear-gradient(180deg, ${preset.panel}, transparent)`}}>
        <div style={{fontFamily:bodyFont,fontSize:26,fontWeight:800,color:accent,marginBottom:8}}>{issue}</div>
        <h1 style={{...titleStyle(headingFont,preset,82),textAlign:'center'}}>{scene.headline}</h1>
      </header>
      <section style={{position:'relative',minHeight:0,padding:'22px 42px 12px'}}>
        <div style={{position:'absolute',inset:'0 18px',background:preset.panel,borderTop:`4px solid ${preset.ink}22`,borderBottom:`4px solid ${preset.ink}22`,boxShadow:`0 22px 60px ${preset.ink}12`}}/>
        <div style={{position:'relative',height:'100%',padding:'30px 26px'}}>
          <Art {...common} boxed fit="contain"/>
        </div>
        <div style={{position:'absolute',right:34,bottom:20,width:36,height:36,borderRadius:999,background:accent,opacity:0.72}}/>
      </section>
      <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="note"/>
    </main>;
  }

  if (layout === 'newspaper-column') {
    return <main style={{position:'absolute',inset:'76px 70px 76px',display:'grid',gridTemplateRows:'auto 1fr auto',gap:22}}>
      <header style={{borderTop:`5px solid ${preset.ink}`,borderBottom:`2px solid ${preset.ink}`,padding:'18px 0 16px',display:'grid',gridTemplateColumns:'88px 1fr',gap:20,...titleMotion}}>
        <div style={{fontFamily:bodyFont,fontSize:34,fontWeight:900,color:accent}}>{issue}</div>
        <h1 style={titleStyle(headingFont,preset,76)}>{scene.headline}</h1>
      </header>
      <section style={{display:'grid',gridTemplateColumns:'1fr 290px',gap:28,minHeight:0}}>
        <Art {...common} boxed/>
        <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="side"/>
      </section>
      <div style={{height:3,background:accent}}/>
    </main>;
  }

  if (layout === 'newspaper-poster') {
    return <main style={{position:'absolute',inset:'70px 70px 76px',display:'grid',gridTemplateRows:'auto 1fr auto',gap:22}}>
      <header style={{borderTop:`6px solid ${preset.ink}`,borderBottom:`3px double ${preset.ink}`,padding:'20px 0 18px',textAlign:'center',...titleMotion}}>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:18,marginBottom:8}}>
          <span style={{height:2,width:110,background:accent}}/>
          <span style={{fontFamily:bodyFont,fontSize:26,fontWeight:900,color:accent}}>{issue}</span>
          <span style={{height:2,width:110,background:accent}}/>
        </div>
        <h1 style={{...titleStyle(headingFont,preset,78),textAlign:'center'}}>{scene.headline}</h1>
      </header>
      <section style={{minHeight:0,background:preset.panel,border:`2px solid ${preset.ink}30`,padding:26,boxShadow:`12px 14px 0 ${accent}18`}}>
        <Art {...common} boxed fit="cover"/>
      </section>
      <div style={{borderTop:`2px solid ${preset.ink}`,borderBottom:`2px solid ${preset.ink}`,padding:'14px 22px',background:preset.panel}}>
        <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="inline"/>
      </div>
    </main>;
  }

  if (layout === 'chalk-lesson' || layout === 'blueprint-callout') {
    return <QuietChromeStage {...quietProps} issueRight/>;
  }

  if (layout === 'sticker-stage') {
    return <main style={{position:'absolute',inset:'80px 78px 84px',display:'grid',gridTemplateRows:'auto 1fr auto',gap:24,textAlign:'center'}}>
      <header style={{background:preset.panel,border:`3px solid ${preset.ink}`,borderRadius:24,padding:'18px 24px',boxShadow:`9px 10px 0 ${accent}55`,...titleMotion}}>
        <div style={{fontFamily:bodyFont,fontSize:28,fontWeight:900,color:accent}}>{issue}</div>
        <h1 style={{...titleStyle(headingFont,preset,82),textAlign:'center'}}>{scene.headline}</h1>
      </header>
      <Art {...common}/>
      <CaptionBlock text={text} preset={preset} bodyFont={bodyFont} accent={accent} motion={motion} variant="note"/>
    </main>;
  }

  // editorial-opener / default quiet chrome
  return <QuietChromeStage {...quietProps}/>;
};

const MotionOverlay: React.FC<{preset: StylePreset; motion: MotionPreset; accent: string}> = ({preset,motion,accent}) => {
  const frame = useCurrentFrame();
  const sweep = interpolate(frame,[0,34],[-140,1220],clamp);
  const reveal = interpolate(frame,[4,34],[0,1],clamp);
  if (motion.accent === 'scan') {
    return <div style={{position:'absolute',top:0,bottom:0,left:sweep,width:90,background:`linear-gradient(90deg, transparent, ${accent}38, transparent)`,opacity:0.9}}/>;
  }
  if (motion.accent === 'chalk') {
    return <AbsoluteFill style={{backgroundImage:`radial-gradient(${preset.ink}35 1px, transparent 1px)`,backgroundSize:'28px 28px',opacity:0.08 + 0.04 * Math.sin(frame / 9)}}/>;
  }
  if (motion.accent === 'wipe' || motion.accent === 'underline') {
    return <div style={{position:'absolute',left:72,top:48,height:6,width:936,background:accent,transformOrigin:'left center',scale:`${reveal} 1`,opacity:0.92}}/>;
  }
  if (motion.accent === 'stamp') {
    const pop = interpolate(frame,[0,8,14],[0.92,1.08,1],clamp);
    return <div style={{position:'absolute',right:72,top:42,width:44,height:44,border:`4px solid ${accent}`,opacity:0.28,rotate:'8deg',scale:pop}}/>;
  }
  return null;
};

const SceneView: React.FC<{scene:Scene;plan:Plan;index:number;playSceneAudio:boolean}> = ({scene,plan,index,playSceneAudio}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const preset = presets[plan.style?.id ?? 'warm-editorial'];
  const motion = getMotionPreset(plan.style?.id ?? 'warm-editorial',plan.motion?.id);
  const headingFont = plan.style?.headingFont || preset.headingFont;
  const bodyFont = plan.style?.bodyFont || preset.bodyFont;
  const captions = captionMap[scene.id] ?? [];
  const timeMs = frame / fps * 1000;
  const active = captions.find((caption) => timeMs >= caption.startMs && timeMs < caption.endMs);
  const accent = scene.accent ?? preset.accent;
  const textureMove = motion.texture === 'grid' || motion.texture === 'blueprint' ? frame * 0.15 : frame * 0.04;

  const quietChrome = preset.layout === 'editorial-opener' || preset.layout === 'chalk-lesson' || preset.layout === 'notebook-diary';
  return <AbsoluteFill style={{background:preset.background,color:preset.ink,overflow:'hidden'}}>
    <AbsoluteFill style={{backgroundImage:preset.texture,backgroundSize:preset.layout.includes('grid') || preset.layout.includes('blueprint') ? '42px 42px':'18px 18px',opacity:quietChrome ? 0.28 : 0.74,translate:`${textureMove}px ${textureMove}px`}}/>
    {!quietChrome ? <MotionOverlay preset={preset} motion={motion} accent={accent}/> : null}
    {!quietChrome ? <div style={{position:'absolute',top:36,left:40,right:40,height:2,background:accent,opacity:0.55}}/> : null}
    <Layout
      layout={preset.layout}
      scene={scene}
      preset={preset}
      index={index}
      headingFont={headingFont}
      bodyFont={bodyFont}
      text={active?.text ?? scene.caption ?? scene.narration}
      motion={motion}
      captionLook={plan.style?.captionLook}
      captionBottomRatio={plan.style?.captionBottomRatio}
    />
    {playSceneAudio && scene.audio ? <Audio src={staticFile(scene.audio)}/> : null}
  </AbsoluteFill>;
};

export const Explainer: React.FC<{plan:Plan}> = ({plan}) => {
  let from = 0;
  const background = presets[plan.style?.id ?? 'warm-editorial'].background;
  const fullAudio = plan.voice?.fullAudio;
  return <AbsoluteFill style={{background}}>
    {fullAudio ? <Audio src={staticFile(fullAudio)}/> : null}
    {plan.scenes.map((scene,index) => {
    const start = from;
    from += scene.durationInFrames;
    return <Sequence key={scene.id} from={start} durationInFrames={scene.durationInFrames}>
      <SceneView scene={scene} plan={plan} index={index} playSceneAudio={!fullAudio}/>
    </Sequence>;
  })}
  </AbsoluteFill>;
};
