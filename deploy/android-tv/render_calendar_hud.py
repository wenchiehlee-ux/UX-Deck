#!/usr/bin/env python3
"""
Dynamic HUD Generator for Home Assistant on Android TV (Solution B)
Generates an 18px rounded corner 32-bit RGBA frosted glass notification card
with the Sentinel Dog mascot and Zen Maru Gothic typography.
"""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from PIL import Image, ImageDraw, ImageFont

def render_hud(
    title: str,
    message: str,
    out_path: str,
    font_path: str = None,
    icon_path: str = None,
    accent_color: tuple = (56, 189, 248),  # #38bdf8 Ice Cyan
    progress_pct: float = 0.45
):
    width, height = 480, 104
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Background: 60% translucent dark slate with 18px true rounded corners
    # RGBA: (15, 23, 42, 120) corresponds to ~47% alpha
    draw.rounded_rectangle(
        [(2, 2), (width - 3, height - 3)],
        radius=18,
        fill=(15, 23, 42, 130),
        outline=(accent_color[0], accent_color[1], accent_color[2], 140),
        width=2
    )

    # 2. Sentinel Dog mascot icon
    if icon_path and os.path.exists(icon_path):
        try:
            mascot = Image.open(icon_path).convert("RGBA").resize((56, 56), Image.Resampling.LANCZOS)
            img.paste(mascot, (16, 24), mascot)
        except Exception as e:
            print(f"Warning: could not paste icon {icon_path}: {e}", file=sys.stderr)

    # 3. Typography
    font_title = None
    font_msg = None
    if font_path and os.path.exists(font_path):
        try:
            font_title = ImageFont.truetype(font_path, 21)
            font_msg = ImageFont.truetype(font_path, 16)
        except Exception as e:
            print(f"Warning: could not load font {font_path}: {e}", file=sys.stderr)

    if not font_title:
        font_title = ImageFont.load_default()
        font_msg = ImageFont.load_default()

    # Smart text truncation / fitting
    clean_title = title.strip()
    clean_msg = message.strip()

    # Truncate if exceeds max display length
    if len(clean_msg) > 30:
        clean_msg = clean_msg[:29] + "…"

    draw.text((84, 18), clean_title, font=font_title, fill=(accent_color[0], accent_color[1], accent_color[2], 255))
    draw.text((84, 52), clean_msg, font=font_msg, fill=(241, 245, 249, 255))

    # 4. Progress bar at bottom
    bar_left = 84
    bar_right = width - 24
    bar_y = height - 16
    draw.rounded_rectangle([(bar_left, bar_y), (bar_right, bar_y + 3)], radius=2, fill=(accent_color[0], accent_color[1], accent_color[2], 60))
    active_width = int((bar_right - bar_left) * max(0.05, min(1.0, progress_pct)))
    draw.rounded_rectangle([(bar_left, bar_y), (bar_left + active_width, bar_y + 3)], radius=2, fill=(accent_color[0], accent_color[1], accent_color[2], 255))

    # Ensure parent dir exists
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    img.save(out_path, "PNG")
    if out_path.endswith("calendar_event.png"):
        cal_path = out_path.replace("calendar_event.png", "calendar.png")
        try:
            img.save(cal_path, "PNG")
        except Exception:
            pass
    print(f"Rendered dynamic HUD -> {out_path} ({title} | {message})")


def main():
    title = sys.argv[1] if len(sys.argv) > 1 else "今日行程提醒 📅"
    message = sys.argv[2] if len(sys.argv) > 2 else "今日行程 ⏰"
    out_path = sys.argv[3] if len(sys.argv) > 3 else "/config/www/ux-deck/huds/calendar_event.png"

    # Search for font and icon in candidate directories
    candidate_dirs = [
        "/config/www/ux-deck",
        "/config/scripts",
        os.path.join(os.path.dirname(__file__), "..", "..", "www", "ux-deck"),
        os.path.join(os.path.dirname(__file__), "huds"),
        os.path.dirname(__file__),
        "deploy/android-tv",
        "."
    ]

    font_path = None
    for d in candidate_dirs:
        candidate = os.path.join(d, "ZenMaruGothic-Bold.ttf")
        if os.path.exists(candidate):
            font_path = candidate
            break

    icon_path = None
    for d in candidate_dirs:
        for icon_name in ["sentinel_mascot_amber.png", "sentinel_mascot_clean.png", "sentinel_icon.png"]:
            candidate = os.path.join(d, icon_name)
            if os.path.exists(candidate):
                icon_path = candidate
                break
        if icon_path:
            break

    render_hud(
        title=title,
        message=message,
        out_path=out_path,
        font_path=font_path,
        icon_path=icon_path
    )


if __name__ == "__main__":
    main()
