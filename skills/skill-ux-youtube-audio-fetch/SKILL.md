---
name: skill-ux-youtube-audio-fetch
description: >-
  UX styling, layout components, and multimodal sync controls for YoutubeAudio.Fetch (GitHub Pages web player & extractor).
  Use this skill when developing or improving the audio player interface, channel tabs, episode drawers,
  real-time transcript (lyrics-live) sync, and atmospheric media aesthetics for YoutubeAudio.Fetch.
---

# UX Skill: YoutubeAudio.Fetch (Atmospheric Media · 典雅酒紅與琥珀金)

This skill provides UI components, visual styling, and multimodal media controls for **YoutubeAudio.Fetch**, delivering a clean, high-fidelity YouTube audio extraction, podcast streaming, and live synchronized transcript listening experience.

## UX Identity & Design System

1. **Warm Alabaster Basis**: Clean, warm off-white background (`#faf9f8`) with pure white card elevations (`#ffffff` / `#f4f1ef`) and subtle borders (`#e8e2df`) ensuring maximum reading comfort for long-form podcasts and financial morning calls.
2. **Crimson Wine Primary (`#a83245`)**: Rich burgundy / deep wine red for active tab gradients (`linear-gradient(135deg, #963044, #bd3d50)`), audio player progress bars, and high-priority action elements.
3. **Warm Amber Gold Accent (`#ad792d`)**: Golden highlight for timestamps (`.ts`, `.date`), channel group category tags (`DAILY`, `PLAYLIST`), and dynamic transcript sync callout borders (`.lyrics-live`).
4. **Animal Mascot (聲波座頭鯨 Soundwave Singing Whale 🐋)**:
   - **Symbol**: `#icon-whale-sonic` (from [animal-icons.svg](../../tokens/icons/animal-icons.svg)).
   - **Mascot Glow Badge**: `linear-gradient(135deg, #a83245 0%, #ad792d 100%)` representing rich burgundy acoustic resonance, spectrum harmonics, and lossless audio fidelity.
   - **Application**: Placed on media player identity headers and UX-Deck overview.

---

## Key Components & Architecture

### 1. Sticky Floating Brand Bar (`.yaf-brand-bar`)
Stays pinned at the top with:
- Mascot glow badge (`#icon-whale-sonic`)
- Site title & subtitle (`Atmospheric Media · 聲波座頭鯨`)
- Quick navigation pills: `🏠 主題首頁` (link to UX-Deck) and `📦 GitHub 儲存庫` (link to source repository).

### 2. Grouped Channel Pill Tabs (`.tabs` & `.tab-group`)
Classified into channel groups (`DAILY`, `PLAYLIST`) with pill-shaped buttons:
- Active state: `linear-gradient(135deg, #963044, #bd3d50)` with white typography and subtle crimson glow.
- Inactive state: Translucent white with gold hover borders.

### 3. Responsive Two-Column Streaming Layout
- **Left Column (Episode Drawer `.episode-list`)**:
  - Displays episode date, duration, phase status badges (`Phase 3` Gold, `Phase 2` Blue, `Phase 1` Wine Red), and title.
  - Active item features an accent left indicator border (`#bd3d50`) and soft gradient tint.
- **Right Column (Player & Multimodal Sync `.main`)**:
  - **Themed Playback Control Panel (`.yaf-playback-panel`)**: Wine-red circular play/pause button (`linear-gradient(135deg, #963044, #bd3d50)`), smooth scrubber track with amber gold playhead, 15s skip controls, monospace timestamp (`JetBrains Mono`), animated spectrum wavebars, volume slider, and audio download button.
  - **Dynamic Live Transcript (`.lyrics-live`)**: Real-time scrolling transcript subtitle card with amber gold left accent border and warm glow background.
  - **Video Keyframe Alignment (`.keyframe`)**: High-contrast video snapshot cards synchronized with audio playback timestamp.
  - **Topic Chapters & Cue List (`.cue-list`)**: Clickable timestamps with topic inferences for quick jumping.

---

## Real Deployed Reference
- **Live Site**: [https://zhongzheng782.github.io/YoutubeAudio.Fetch/](https://zhongzheng782.github.io/YoutubeAudio.Fetch/)
- **Repository**: [https://github.com/ZhongZheng782/YoutubeAudio.Fetch](https://github.com/ZhongZheng782/YoutubeAudio.Fetch)
