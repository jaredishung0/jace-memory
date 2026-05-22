---
name: context-monitor
description: Lifecycle hook that reminds agent to evict context every other turn
---

# Context Monitor Hook

## Location
Create as pi extension: `~/.pi/agent/extensions/context-monitor.ts`

## Code
```typescript
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

export default function contextMonitor(pi: ExtensionAPI) {
  let turnCount = 0;
  
  pi.on("turn_complete", () => {
    turnCount++;
    if (turnCount % 2 === 0) {
      pi.contextWindow.usage().then(usage => {
        if (usage > 0.20) {
          pi.logger.info("[context-monitor] Context >20%. Consider /condense-evict");
        }
      });
    }
  });
}
```

## Activation
1. Save to `~/.pi/agent/extensions/context-monitor.ts`
2. Restart pi