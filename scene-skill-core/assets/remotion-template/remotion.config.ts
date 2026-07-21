import {Config} from '@remotion/cli/config';
import {existsSync} from 'node:fs';
Config.setOverwriteOutput(true);
Config.setVideoImageFormat('jpeg');
Config.setPixelFormat('yuv420p');
// Software-backed ANGLE avoids nondeterministic black rectangles on some Windows GPU drivers.
Config.setChromiumOpenGlRenderer('swangle');
const candidates=[process.env.REMOTION_BROWSER_EXECUTABLE,'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe','C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'].filter(Boolean) as string[];
const localBrowser=candidates.find((path)=>existsSync(path));
if(localBrowser) Config.setBrowserExecutable(localBrowser);
