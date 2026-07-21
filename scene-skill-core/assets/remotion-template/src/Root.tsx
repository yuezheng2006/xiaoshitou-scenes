import {Composition} from 'remotion';
import planJson from './generated/plan.json';
import {Explainer} from './Explainer';
import type {Plan} from './types';

const plan=planJson as Plan;
export const RemotionRoot=()=> <Composition
  id="HanddrawnExplainer"
  component={Explainer}
  durationInFrames={plan.scenes.reduce((n,s)=>n+s.durationInFrames,0)}
  fps={plan.fps}
  width={plan.width}
  height={plan.height}
  defaultProps={{plan}}
/>;
