#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create_new_reserve_animals.py
Generates the 12 new reserve animal SVGs for Modern Emblem and Lucide.
"""

from pathlib import Path
import xml.etree.ElementTree as ET

BASE_DIR = Path(__file__).resolve().parent.parent if "scripts" in str(Path(__file__)) else Path(__file__).resolve().parent
TOKENS_DIR = BASE_DIR / "tokens" / "icons"
EMBLEM_DIR = TOKENS_DIR / "modern-emblem"
LUCIDE_DIR = TOKENS_DIR / "lucide"

EMBLEM_DIR.mkdir(parents=True, exist_ok=True)
LUCIDE_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------
# 1. LUCIDE ICONS (24x24 viewBox, stroke-width 1.8, round caps & joins)
# --------------------------------------------------------------------------

lucide_icons = {
    "lucide-cheetah.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
  <!-- Aerodynamic Low-Drag Cheetah Head & Muzzle -->
  <path d="M4 14c.5-3 2.5-6 6-7s6.5 1 8 4c1 2 .5 5-1 7l-3 1c-2.5.5-5 0-7-2l-3-3Z" />
  <!-- Small Round Ear -->
  <path d="M14 6a2 2 0 0 1 2.5-1.5 2 2 0 0 1 1.5 2.5" />
  <!-- Alert Eye -->
  <circle cx="13" cy="11" r=".6" fill="currentColor" />
  <!-- Iconic Tear-Stripe Line (from inner eye to corner of mouth) -->
  <path d="M13 12c-.5 1-1.5 2.5-2 3.5" />
  <!-- Nose and Jaw -->
  <path d="M18 14h-2" />
  <!-- Speed Dash Accents -->
  <path d="M2 8h2.5" />
  <path d="M1 11h2" />
</svg>""",

    "lucide-wolf.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
  <!-- Sharp Pointed Ears -->
  <path d="M5 10L7 3l4 4" />
  <path d="M19 10l-2-7-4 4" />
  <!-- Wolf Head Diamond Contour -->
  <path d="M4 12c0 4 3 8 8 9s8-5 8-9c-1-1-3-2-5-2-1 0-2 .5-3 1-1-.5-2-1-3-1-2 0-4 1-5 2Z" />
  <!-- Intense Predatory Eyes -->
  <path d="M8.5 13l2 .5" />
  <path d="M15.5 13l-2 .5" />
  <!-- Snout & Nose Tip -->
  <path d="M11 17h2l-1 1.5z" />
  <path d="M12 18.5V20" />
</svg>""",

    "lucide-shark.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
  <!-- Dynamic Slicing Shark Body & Pointed Snout -->
  <path d="M2 13c3-1 6-4 11-4 4 0 7 2 9 4-3 1-6 3-10 3-4 0-7-1.5-10-3Z" />
  <!-- Iconic Sharp Dorsal Fin -->
  <path d="M10 9L12 3c1.5 2 2.5 4.5 3 6" />
  <!-- Pectoral Fin -->
  <path d="M8 14l-2 5c2-.5 4-1.5 5-3" />
  <!-- Crescent Caudal Tail -->
  <path d="M21 13l2-4c-.5 2-.5 6 0 8l-2-4Z" />
  <!-- Gill Slits & Eye -->
  <circle cx="6" cy="12" r=".5" fill="currentColor" />
  <path d="M9 11.5v2" />
  <path d="M10.5 12v1.5" />
</svg>""",

    "lucide-fox.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
  <!-- Tall Alert Fox Ears -->
  <path d="M4 11L6 3l5 4" />
  <path d="M20 11L18 3l-5 4" />
  <!-- Cheek Tuft & Slender Pointed Muzzle -->
  <path d="M4 11c0 3 2.5 6 5 7l3 3 3-3c2.5-1 5-4 5-7-2 0-4-1-5-2-1 0-2 .5-3 1-1-.5-2-1-3-1-1 1-3 2-5 2Z" />
  <!-- Slanted Clever Eyes -->
  <path d="M8 12.5l2 .5" />
  <path d="M16 12.5l-2 .5" />
  <!-- Little Black Nose -->
  <circle cx="12" cy="19" r=".8" fill="currentColor" />
</svg>""",

    "lucide-penguin.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
  <!-- Stately Upright Body & Head -->
  <path d="M12 3c-3 0-5 2.5-5 6 0 3-1 6-2 9 0 2 2 3 7 3s7-1 7-3c-1-3-2-6-2-9 0-3.5-2-6-5-6Z" />
  <!-- Tuxedo Wings / Flippers -->
  <path d="M6 11c-1.5 2-2 5-1.5 7" />
  <path d="M18 11c1.5 2 2 5 1.5 7" />
  <!-- White Chest & Belly Oval -->
  <path d="M9 13c0-2.5 1.3-4 3-4s3 1.5 3 4c0 3.5-1.3 6-3 6s-3-2.5-3-6Z" />
  <!-- Cute Sharp Bill -->
  <path d="M10.5 8h3l-1.5 2z" fill="currentColor" />
  <!-- Feet -->
  <path d="M9 21l-1 1" />
  <path d="M15 21l1 1" />
</svg>""",

    "lucide-gorilla.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
  <!-- Powerful Domed Crest & Head -->
  <path d="M7 11C7 6 9 3 12 3s5 3 5 8" />
  <!-- Heavy Brow Ridge -->
  <path d="M6 10h12" />
  <!-- Broad Titan Jaw & Cheek Contour -->
  <path d="M5 11c-.5 3 0 7 2 9 1.5 1.5 3 1.5 5 1.5s3.5 0 5-1.5c2-2 2.5-6 2-9" />
  <!-- Deep Inset Eyes -->
  <circle cx="9.5" cy="9.5" r=".6" fill="currentColor" />
  <circle cx="14.5" cy="9.5" r=".6" fill="currentColor" />
  <!-- Broad Twin Nostrils -->
  <path d="M10.5 15c0 .8.5 1.2 1.5 1.2s1.5-.4 1.5-1.2" />
  <circle cx="10.5" cy="14.5" r=".4" fill="currentColor" />
  <circle cx="13.5" cy="14.5" r=".4" fill="currentColor" />
</svg>""",

    "lucide-panda.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
  <!-- Round Chubby Panda Head -->
  <circle cx="12" cy="13" r="7.5" />
  <!-- Iconic Solid Round Ears -->
  <path d="M6 8a3 3 0 1 0-3-3 5.5 5.5 0 0 1 3 3Z" fill="currentColor" />
  <path d="M18 8a3 3 0 1 1 3-3 5.5 5.5 0 0 0-3 3Z" fill="currentColor" />
  <!-- Signature Slanted Dark Eye Patches -->
  <ellipse cx="9" cy="12" rx="1.6" ry="2" transform="rotate(-15 9 12)" fill="currentColor" />
  <ellipse cx="15" cy="12" rx="1.6" ry="2" transform="rotate(15 15 12)" fill="currentColor" />
  <!-- White Pupils -->
  <circle cx="9.2" cy="11.8" r=".5" fill="#ffffff" />
  <circle cx="14.8" cy="11.8" r=".5" fill="#ffffff" />
  <!-- Cute Inverted Triangle Snout & Smile -->
  <path d="M11 16h2l-1 1z" fill="currentColor" />
  <path d="M12 17v1.2" />
  <path d="M10.5 18.2a1.5 1.5 0 0 0 3 0" />
</svg>"""
}

# --------------------------------------------------------------------------
# 2. MODERN EMBLEM SVGs (120x120 viewBox, Gradient Shading, Bottom Tagline)
# --------------------------------------------------------------------------

modern_emblems = {
    "emblem-giraffe.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="gir-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>
    <linearGradient id="gir-grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
  </defs>
  <!-- Background Disc -->
  <circle cx="60" cy="50" r="38" fill="#fffbeb"/>
  <!-- Elegant Long Neck & Body -->
  <path d="M 52 82 L 56 36 C 56 30 62 26 68 28 C 72 30 74 34 72 40 L 68 82 Z" fill="url(#gir-grad1)"/>
  <!-- Pair of Horns (Ossicones) -->
  <path d="M 64 28 L 62 18 M 68 29 L 69 19" stroke="url(#gir-grad2)" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="62" cy="18" r="2" fill="url(#gir-grad2)"/>
  <circle cx="69" cy="19" r="2" fill="url(#gir-grad2)"/>
  <!-- Cute Ears -->
  <path d="M 58 32 C 52 30 50 34 54 36 Z" fill="url(#gir-grad1)"/>
  <path d="M 72 32 C 78 30 80 34 76 36 Z" fill="url(#gir-grad1)"/>
  <!-- Distinctive Giraffe Geometric Spots -->
  <polygon points="56,44 64,42 63,48 57,49" fill="url(#gir-grad2)" opacity="0.85"/>
  <polygon points="58,54 66,52 65,59 59,60" fill="url(#gir-grad2)" opacity="0.85"/>
  <polygon points="56,66 65,64 64,72 57,73" fill="url(#gir-grad2)" opacity="0.85"/>
  <!-- Gentle Eye & Muzzle -->
  <circle cx="66" cy="33" r="1.5" fill="#451a03"/>
  <path d="M 68 36 C 72 37 72 41 68 41 Z" fill="#fde68a"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10" fill="#0f172a" letter-spacing="2.5">GIRAFFE</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#d97706" letter-spacing="1.2">― MACRO VISION ―</text>
</svg>""",

    "emblem-tiger.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="tig-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#ea580c"/>
    </linearGradient>
    <linearGradient id="tig-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Background Shield -->
  <circle cx="60" cy="50" r="38" fill="#fff7ed"/>
  <!-- Round Tiger Ears -->
  <circle cx="40" cy="32" r="9" fill="url(#tig-dark)"/>
  <circle cx="40" cy="32" r="5" fill="#fed7aa"/>
  <circle cx="80" cy="32" r="9" fill="url(#tig-dark)"/>
  <circle cx="80" cy="32" r="5" fill="#fed7aa"/>
  <!-- Powerful Head Contour -->
  <circle cx="60" cy="52" r="28" fill="url(#tig-grad1)"/>
  <!-- Forehead King '王' Character Stripes -->
  <path d="M 52 35 H 68 M 54 39 H 66 M 52 43 H 68 M 60 35 V 43" stroke="url(#tig-dark)" stroke-width="2.2" stroke-linecap="round"/>
  <!-- Cheek Whiskers/Stripes -->
  <polygon points="34,48 44,50 36,53" fill="url(#tig-dark)"/>
  <polygon points="35,56 45,56 37,60" fill="url(#tig-dark)"/>
  <polygon points="86,48 76,50 84,53" fill="url(#tig-dark)"/>
  <polygon points="85,56 75,56 83,60" fill="url(#tig-dark)"/>
  <!-- Sharp Amber Eyes -->
  <ellipse cx="50" cy="51" rx="3.5" ry="2.5" fill="#fef08a"/>
  <circle cx="50" cy="51" r="1.5" fill="#0f172a"/>
  <ellipse cx="70" cy="51" rx="3.5" ry="2.5" fill="#fef08a"/>
  <circle cx="70" cy="51" r="1.5" fill="#0f172a"/>
  <!-- White Snout Muzzle & Nose -->
  <ellipse cx="60" cy="64" rx="10" ry="7" fill="#ffffff" opacity="0.95"/>
  <polygon points="57,60 63,60 60,64" fill="#0f172a"/>
  <path d="M 60 64 V 67 M 56 68 C 58 70 62 70 64 68" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10.5" fill="#0f172a" letter-spacing="2.8">TIGER</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#c2410c" letter-spacing="1.2">― APEX MOMENTUM ―</text>
</svg>""",

    "emblem-monkey.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="mon-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="mon-face" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef3c7"/>
      <stop offset="100%" stop-color="#fde68a"/>
    </linearGradient>
  </defs>
  <!-- Background Disc -->
  <circle cx="60" cy="50" r="38" fill="#fefce8"/>
  <!-- Prominent Big Round Ears -->
  <circle cx="34" cy="48" r="14" fill="url(#mon-grad1)"/>
  <circle cx="34" cy="48" r="8" fill="url(#mon-face)"/>
  <circle cx="86" cy="48" r="14" fill="url(#mon-grad1)"/>
  <circle cx="86" cy="48" r="8" fill="url(#mon-face)"/>
  <!-- Head Contour -->
  <circle cx="60" cy="50" r="26" fill="url(#mon-grad1)"/>
  <!-- Heart-Shaped Cheek / Face Mask -->
  <path d="M 60 44 C 54 36 44 38 44 48 C 44 58 56 66 60 68 C 64 66 76 58 76 48 C 76 38 66 36 60 44 Z" fill="url(#mon-face)"/>
  <!-- Inquisitive Intelligent Eyes -->
  <ellipse cx="53" cy="48" rx="3" ry="4" fill="#1e293b"/>
  <circle cx="52" cy="46.5" r="1.2" fill="#ffffff"/>
  <ellipse cx="67" cy="48" rx="3" ry="4" fill="#1e293b"/>
  <circle cx="66" cy="46.5" r="1.2" fill="#ffffff"/>
  <!-- Cute Snout & Playful Smile -->
  <ellipse cx="60" cy="59" rx="8" ry="5.5" fill="#fde68a"/>
  <circle cx="57.5" cy="58" r="1" fill="#78350f"/>
  <circle cx="62.5" cy="58" r="1" fill="#78350f"/>
  <path d="M 55 61 C 58 64 62 64 65 61" stroke="#78350f" stroke-width="1.4" stroke-linecap="round"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10" fill="#0f172a" letter-spacing="2.5">MONKEY</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#b45309" letter-spacing="1.2">― AGILE AUTOMATION ―</text>
</svg>""",

    "emblem-zebra.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="zeb-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Background Disc -->
  <circle cx="60" cy="50" r="38" fill="#f8fafc"/>
  <!-- Sleek Zebra Mane & Neck Contour -->
  <path d="M 44 80 L 52 34 C 54 28 64 26 70 30 C 76 34 76 42 74 48 L 70 80 Z" fill="#ffffff"/>
  <!-- Serrated Mane on Crest -->
  <polygon points="50,42 42,40 50,48" fill="url(#zeb-dark)"/>
  <polygon points="49,52 40,50 49,58" fill="url(#zeb-dark)"/>
  <polygon points="47,62 38,60 47,68" fill="url(#zeb-dark)"/>
  <!-- Bold Graphic Monochrome Stripes -->
  <polygon points="52,38 68,36 67,42 53,44" fill="url(#zeb-dark)"/>
  <polygon points="51,50 68,48 67,54 51,56" fill="url(#zeb-dark)"/>
  <polygon points="49,62 69,60 68,66 48,68" fill="url(#zeb-dark)"/>
  <!-- Pointed Ears -->
  <polygon points="54,32 52,20 58,28" fill="url(#zeb-dark)"/>
  <polygon points="62,32 66,20 68,28" fill="url(#zeb-dark)"/>
  <!-- Dark Muzzle & Eye -->
  <circle cx="68" cy="36" r="2" fill="url(#zeb-dark)"/>
  <path d="M 70 42 C 75 44 75 48 70 50 Z" fill="url(#zeb-dark)"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10.5" fill="#0f172a" letter-spacing="2.8">ZEBRA</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#475569" letter-spacing="1.2">― CLEAR EQUILIBRIUM ―</text>
</svg>""",

    "emblem-hippo.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="hip-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="hip-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#0c4a6e"/>
    </linearGradient>
  </defs>
  <!-- Background Disc -->
  <circle cx="60" cy="50" r="38" fill="#f0f9ff"/>
  <!-- Little Alert Ears -->
  <circle cx="42" cy="28" r="6" fill="url(#hip-dark)"/>
  <circle cx="78" cy="28" r="6" fill="url(#hip-dark)"/>
  <!-- Massive Broad Head & Snout Contour -->
  <path d="M 38 48 C 38 32 82 32 82 48 C 82 54 86 58 86 66 C 86 78 74 82 60 82 C 46 82 34 78 34 66 C 34 58 38 54 38 48 Z" fill="url(#hip-grad1)"/>
  <!-- Waterline Ripples Beneath -->
  <path d="M 28 76 Q 44 72 60 76 T 92 76" stroke="#bae6fd" stroke-width="3" stroke-linecap="round" fill="none"/>
  <!-- Alert Round Eyes on Top -->
  <ellipse cx="49" cy="42" rx="3.5" ry="4.5" fill="#ffffff"/>
  <circle cx="50" cy="42" r="2" fill="#082f49"/>
  <ellipse cx="71" cy="42" rx="3.5" ry="4.5" fill="#ffffff"/>
  <circle cx="70" cy="42" r="2" fill="#082f49"/>
  <!-- Broad Muzzle Plate & Prominent Twin Nostrils -->
  <path d="M 40 56 C 40 52 80 52 80 56 C 80 68 72 74 60 74 C 48 74 40 68 40 56 Z" fill="url(#hip-dark)"/>
  <ellipse cx="50" cy="62" rx="3" ry="4" fill="#082f49"/>
  <ellipse cx="70" cy="62" rx="3" ry="4" fill="#082f49"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10.5" fill="#0f172a" letter-spacing="2.8">HIPPO</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#0284c7" letter-spacing="1.2">― STEADFAST CAPACITY ―</text>
</svg>""",

    "emblem-cheetah.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="che-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
  </defs>
  <!-- Background Disc -->
  <circle cx="60" cy="50" r="38" fill="#fff7ed"/>
  <!-- Aerodynamic Sleek Cheetah Profile -->
  <path d="M 32 68 C 36 50 48 38 64 36 C 76 34 88 40 88 52 C 88 62 76 72 60 76 C 48 78 36 74 32 68 Z" fill="url(#che-grad)"/>
  <!-- Rounded Aerodynamic Ear -->
  <circle cx="58" cy="34" r="6" fill="#c2410c"/>
  <circle cx="58" cy="34" r="3" fill="#ffedd5"/>
  <!-- Intense Piercing Eye -->
  <ellipse cx="72" cy="44" rx="2.5" ry="3.5" fill="#fef08a"/>
  <circle cx="72" cy="44" r="1.5" fill="#0f172a"/>
  <!-- Signature Tear Stripe Line -->
  <path d="M 72 47 C 73 54 78 60 84 62" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" fill="none"/>
  <!-- Speed Cheetah Spots -->
  <circle cx="48" cy="52" r="2.2" fill="#7c2d12"/>
  <circle cx="42" cy="62" r="2" fill="#7c2d12"/>
  <circle cx="56" cy="64" r="2.4" fill="#7c2d12"/>
  <!-- Velocity Streak Waves -->
  <path d="M 22 42 H 34 M 18 52 H 28 M 22 62 H 30" stroke="#fdba74" stroke-width="2" stroke-linecap="round"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10" fill="#0f172a" letter-spacing="2.5">CHEETAH</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#ea580c" letter-spacing="1.2">― ULTRA VELOCITY ―</text>
</svg>""",

    "emblem-wolf.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="wol-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
    <linearGradient id="wol-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Background Shield / Crest -->
  <polygon points="60,14 96,30 96,70 60,88 24,70 24,30" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
  <!-- Prismatic Geometric Wolf Head -->
  <!-- Left & Right Pointed Ears -->
  <polygon points="34,42 36,20 52,34" fill="url(#wol-dark)"/>
  <polygon points="86,42 84,20 68,34" fill="url(#wol-dark)"/>
  <!-- Central Brow & Cheek Facets -->
  <polygon points="60,34 50,46 60,54 70,46" fill="url(#wol-grad1)"/>
  <polygon points="36,46 50,46 44,64 32,56" fill="url(#wol-dark)"/>
  <polygon points="84,46 70,46 76,64 88,56" fill="url(#wol-dark)"/>
  <!-- Predatory Ice-Gold Eyes -->
  <polygon points="46,47 52,49 48,53" fill="#fde047"/>
  <polygon points="74,47 68,49 72,53" fill="#fde047"/>
  <!-- Muzzle, Nose Tip & Fang Angle -->
  <polygon points="60,54 52,66 60,78 68,66" fill="url(#wol-grad1)"/>
  <polygon points="57,74 63,74 60,78" fill="#0f172a"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10.5" fill="#0f172a" letter-spacing="2.8">WOLF</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#2563eb" letter-spacing="1.2">― APEX SENTINEL ―</text>
</svg>""",

    "emblem-shark.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="sha-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee"/>
      <stop offset="100%" stop-color="#0891b2"/>
    </linearGradient>
    <linearGradient id="sha-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e7490"/>
      <stop offset="100%" stop-color="#164e63"/>
    </linearGradient>
  </defs>
  <!-- Background Disc -->
  <circle cx="60" cy="50" r="38" fill="#ecfeff"/>
  <!-- Iconic High Dorsal Fin Slicing Ocean -->
  <polygon points="52,42 66,16 74,42" fill="url(#sha-dark)"/>
  <!-- Hydrodynamic Shark Body Profile -->
  <path d="M 20 62 C 34 50 64 46 94 56 C 98 64 88 74 74 76 C 52 78 30 74 20 62 Z" fill="url(#sha-grad1)"/>
  <!-- Pectoral Fin -->
  <polygon points="46,66 38,82 58,72" fill="url(#sha-dark)"/>
  <!-- Caudal Tail Fluke -->
  <polygon points="88,56 102,42 98,58 104,70" fill="url(#sha-dark)"/>
  <!-- Cold Eye & Gill Slits -->
  <circle cx="34" cy="58" r="1.6" fill="#083344"/>
  <path d="M 44 56 L 42 64 M 48 57 L 46 63 M 52 58 L 50 62" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10.5" fill="#0f172a" letter-spacing="2.8">SHARK</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#0891b2" letter-spacing="1.2">― MARKET APEX ―</text>
</svg>""",

    "emblem-fox.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="fox-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f87171"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
    <linearGradient id="fox-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#450a0a"/>
    </linearGradient>
  </defs>
  <!-- Background Disc -->
  <circle cx="60" cy="50" r="38" fill="#fef2f2"/>
  <!-- Lush Bushy Fox Tail with White Tip -->
  <path d="M 76 68 C 96 64 100 44 88 34 C 84 40 82 48 76 54 Z" fill="url(#fox-grad1)"/>
  <polygon points="92,38 98,34 94,44" fill="#ffffff"/>
  <!-- Pointed Ears with Dark Tips -->
  <polygon points="38,40 40,20 54,34" fill="url(#fox-dark)"/>
  <polygon points="82,40 80,20 66,34" fill="url(#fox-dark)"/>
  <polygon points="41,38 42,26 50,34" fill="#fee2e2"/>
  <polygon points="79,38 78,26 70,34" fill="#fee2e2"/>
  <!-- Face & Snout Contour -->
  <polygon points="60,34 40,46 60,76 80,46" fill="url(#fox-grad1)"/>
  <!-- White Cheek Accents -->
  <polygon points="40,46 54,58 48,66" fill="#ffffff"/>
  <polygon points="80,46 66,58 72,66" fill="#ffffff"/>
  <!-- Slanted Clever Eyes & Button Nose -->
  <polygon points="48,46 54,49 50,52" fill="#0f172a"/>
  <polygon points="72,46 66,49 70,52" fill="#0f172a"/>
  <circle cx="60" cy="74" r="2" fill="#0f172a"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10.5" fill="#0f172a" letter-spacing="2.8">FOX</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#dc2626" letter-spacing="1.2">― TACTICAL AGILITY ―</text>
</svg>""",

    "emblem-penguin.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="pen-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14b8a6"/>
      <stop offset="100%" stop-color="#0f766e"/>
    </linearGradient>
    <linearGradient id="pen-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Background Disc -->
  <circle cx="60" cy="50" r="38" fill="#f0fdfa"/>
  <!-- Solid Tuxedo Body -->
  <path d="M 60 22 C 48 22 40 34 40 54 C 40 70 48 80 60 80 C 72 80 80 70 80 54 C 80 34 72 22 60 22 Z" fill="url(#pen-dark)"/>
  <!-- Flipper Wings -->
  <path d="M 40 46 C 34 52 32 64 38 70 C 40 64 41 54 42 48 Z" fill="url(#pen-grad1)"/>
  <path d="M 80 46 C 86 52 88 64 82 70 C 80 64 79 54 78 48 Z" fill="url(#pen-grad1)"/>
  <!-- Crisp White Belly -->
  <ellipse cx="60" cy="56" rx="12" ry="18" fill="#ffffff"/>
  <!-- Amber Beak & Eyes -->
  <circle cx="54" cy="34" r="1.6" fill="#ffffff"/>
  <circle cx="54" cy="34" r=".9" fill="#0f172a"/>
  <circle cx="66" cy="34" r="1.6" fill="#ffffff"/>
  <circle cx="66" cy="34" r=".9" fill="#0f172a"/>
  <polygon points="56,38 64,38 60,45" fill="#f59e0b"/>
  <!-- Cute Feet -->
  <ellipse cx="52" cy="80" rx="5" ry="2.5" fill="#f59e0b"/>
  <ellipse cx="68" cy="80" rx="5" ry="2.5" fill="#f59e0b"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="9.5" fill="#0f172a" letter-spacing="2.5">PENGUIN</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#0f766e" letter-spacing="1.2">― RESILIENT ENDURANCE ―</text>
</svg>""",

    "emblem-gorilla.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="gor-dark1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="gor-dark2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Background Shield -->
  <polygon points="60,14 96,30 96,70 60,88 24,70 24,30" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
  <!-- Imposing Domed Crest -->
  <path d="M 44 42 C 44 26 50 20 60 20 C 70 20 76 26 76 42 Z" fill="url(#gor-dark1)"/>
  <!-- Powerful Shoulders & Massive Face Plate -->
  <path d="M 32 60 C 32 46 44 42 60 42 C 76 42 88 46 88 60 C 88 76 76 82 60 82 C 44 82 32 76 32 60 Z" fill="url(#gor-dark2)"/>
  <!-- Heavy Brow Ridge -->
  <rect x="42" y="44" width="36" height="5" rx="2.5" fill="#64748b"/>
  <!-- Deep Inset Determined Eyes -->
  <circle cx="50" cy="46.5" r="1.5" fill="#f8fafc"/>
  <circle cx="70" cy="46.5" r="1.5" fill="#f8fafc"/>
  <!-- Signature Broad Snout Plate & Nostrils -->
  <ellipse cx="60" cy="62" rx="11" ry="8" fill="#1e293b"/>
  <ellipse cx="55" cy="62" rx="2.5" ry="3.5" fill="#0f172a"/>
  <ellipse cx="65" cy="62" rx="2.5" ry="3.5" fill="#0f172a"/>
  <!-- Firm Set Jawline -->
  <path d="M 50 72 H 70" stroke="#64748b" stroke-width="1.8" stroke-linecap="round"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10" fill="#0f172a" letter-spacing="2.5">GORILLA</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#475569" letter-spacing="1.2">― TITANIC STRENGTH ―</text>
</svg>""",

    "emblem-panda.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="pan-green" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="pan-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Background Disc with Jade Green Glow -->
  <circle cx="60" cy="50" r="38" fill="#ecfdf5"/>
  <!-- Round Black Ears -->
  <circle cx="38" cy="30" r="9" fill="url(#pan-dark)"/>
  <circle cx="82" cy="30" r="9" fill="url(#pan-dark)"/>
  <!-- Chubby Round Face -->
  <circle cx="60" cy="52" r="28" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <!-- Signature Slanted Eye Patches -->
  <ellipse cx="49" cy="48" rx="5.5" ry="7" transform="rotate(-15 49 48)" fill="url(#pan-dark)"/>
  <ellipse cx="71" cy="48" rx="5.5" ry="7" transform="rotate(15 71 48)" fill="url(#pan-dark)"/>
  <!-- Inquisitive Pupils -->
  <circle cx="50" cy="47" r="1.8" fill="#ffffff"/>
  <circle cx="50" cy="47" r=".9" fill="#0f172a"/>
  <circle cx="70" cy="47" r="1.8" fill="#ffffff"/>
  <circle cx="70" cy="47" r=".9" fill="#0f172a"/>
  <!-- Cute Snout & Bamboo Leaf Accent -->
  <ellipse cx="60" cy="62" rx="4" ry="2.8" fill="url(#pan-dark)"/>
  <path d="M 60 65 V 68 M 56 68 C 58 70 62 70 64 68" stroke="url(#pan-dark)" stroke-width="1.3" stroke-linecap="round"/>
  <!-- Fresh Bamboo Leaf in Mouth -->
  <path d="M 63 67 Q 72 65 76 60 Q 70 66 63 67 Z" fill="url(#pan-green)"/>
  <!-- Typography -->
  <text x="60" y="103" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="10.5" fill="#0f172a" letter-spacing="2.8">PANDA</text>
  <text x="60" y="112" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-weight="600" font-size="4.2" fill="#059669" letter-spacing="1.2">― HARMONIC EQUILIBRIUM ―</text>
</svg>"""
}

# --------------------------------------------------------------------------
# Write & Validate SVGs
# --------------------------------------------------------------------------

def main():
    print("[*] Generating Lucide SVGs...")
    for filename, content in lucide_icons.items():
        out_path = LUCIDE_DIR / filename
        # Validate XML
        try:
            ET.fromstring(content)
        except Exception as e:
            print(f"[!] XML Error in {filename}: {e}")
            continue
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  [✓] {filename} written successfully.")

    print("\n[*] Generating Modern Emblem SVGs...")
    for filename, content in modern_emblems.items():
        out_path = EMBLEM_DIR / filename
        # Validate XML
        try:
            ET.fromstring(content)
        except Exception as e:
            print(f"[!] XML Error in {filename}: {e}")
            continue
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  [✓] {filename} written successfully.")

    print("\n[🎉] All 19 SVGs successfully created and validated!")

if __name__ == "__main__":
    main()
