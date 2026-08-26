---
name: Reel camera and crop rules
description: When cropping 16:9 gameplay to 9:16 vertical for reels, center on the character party, not mouse/geometric center. Verify at exact timestamps.
type: feedback
---

Center the vertical crop on the party of characters or group action, NOT the mouse cursor or geometric center of the frame.

**Why:** Robert reviewed reel drafts and the camera kept missing the action — following the mouse pointer or landing on empty terrain while characters were offscreen.

**How to apply:**
1. Extract a full 16:9 frame at the exact segment start timestamp (not the scene detection frame — those can be seconds off)
2. Visually identify where the party/characters are in the frame (x position)
3. Set crop_x = party_center_x - (crop_width / 2), clamped to valid range
4. Prefer slower, stable crops — don't jump wildly between different x positions across segments
5. For battle scenes, center between the two armies rather than just on the player's army
6. The HUD bar at the bottom of the frame will get partially visible — that's acceptable
