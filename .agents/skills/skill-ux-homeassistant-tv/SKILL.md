---
name: skill-ux-homeassistant-tv
description: >-
  10-foot UI design, glanceable frosted HUD overlays, and remote-control accessible popup notifications
  for HomeAssistant on Android TV. Use this skill when designing, building, or styling Home Assistant
  Lovelace dashboards, browser_mod dialogs, and Android TV notifications.
---

# UX Skill: HomeAssistant (Android TV 10-foot Popup UI)

This skill provides design guidelines, CSS specifications, and Lovelace/notification templates for **HomeAssistant on Android TV**, delivering high-visibility, elegant, non-intrusive living room popups.

## 10-Foot UI Principles

1. **Viewing Distance Ergonomics (3–4 Meters)**:
   - Minimum font size: `20px` for body/meta, `28px - 36px` for headers.
   - High contrast ratio: Crisp white text (`#ffffff`) over translucent frosted dark slate (`rgba(10, 10, 16, 0.88)`).
2. **D-pad Focus Navigation**:
   - Every interactive control must have an unmissable focus state: `3px solid #38bdf8` outline with a cyan glow (`box-shadow: 0 0 16px rgba(56, 189, 248, 0.6)`).
3. **Corner Picture-in-Picture (PIP) Placement**:
   - Notifications dock to the top-right or bottom-right corner to avoid blocking focal TV content (subtitles or central movie scenes).
4. **Auto-Dismiss Visual Timer**:
   - A smooth shrinking countdown progress bar indicates time remaining before auto-dismissal.
5. **Animal Mascot (客廳守護夜鷹/靈犬 Living Room Sentinel 🐕🦉)**:
   - **Symbol**: `#icon-sentinel-tv` (from [animal-icons.svg](../../tokens/icons/animal-icons.svg)).
   - **Purpose**: Symbolizes loyal household vigilance; engineered with bold outlines and pricked ears for instant recognition from 3–4 meters away.
   - **Application**: Rendered at `32px - 48px` within the HUD header, paired with a cyan ambient backlight glow.

---

## Component Specs & Code

### 1. TV Notification Toast / HUD
See [tv-popup.css](./resources/tv-popup.css) for full styling.

### 2. Home Assistant Lovelace / Automation Configuration
See [tv-notification-card.yaml](./examples/tv-notification-card.yaml) for sample automation payloads (using `notifications_for_android_tv` or `browser_mod.popup`).
