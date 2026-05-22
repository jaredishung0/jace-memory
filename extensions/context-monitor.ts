/**
 * Context Monitor Extension
 * Reminds agent every 2 turns if context >20%
 */
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

export default function contextMonitor(pi: ExtensionAPI) {
  let turnCount = 0;
  
  pi.on("turn_complete", async () => {
    turnCount++;
    if (turnCount % 2 === 0) {
      const usage = await pi.contextWindow.usage();
      if (usage && usage > 0.20) {
        pi.logger.info("[context-monitor] Context >20%. Run /condense-evict");
      }
    }
  });
}