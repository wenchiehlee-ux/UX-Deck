import matplotlib.pyplot as plt
import matplotlib.patches as patches
from svgpath2mpl import parse_path

fig, ax = plt.subplots(figsize=(2, 2), dpi=128)
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)

# Exact paths from #icon-sentinel-tv (showcase.html / animal-icons.svg N-2 version)
paths = [
    "M8.5 8.5c-.38 1.05-1.08 2.03-2.34 2.5-1.93.72-3.58-.3-3.66-1-.11-.99 1.18-6.53 4-7 1.92-.32 3.65.85 3.65 2.24A7.5 7.5 0 0 1 14 5.28c0-1.39 1.84-2.6 3.77-2.28 2.82.47 4.11 6.01 4 7-.08.7-1.73 1.72-3.66 1-1.26-.47-1.85-1.45-2.24-2.5",
    "M4.42 11.25A13.15 13.15 0 0 0 4 14.56C4 18.73 7.58 21 12 21s8-2.27 8-6.44a11.7 11.7 0 0 0-.49-3.31",
    "M8 14v.5",
    "M16 14v.5",
    "M11.25 16.25h1.5L12 17z"
]

# Draw dark slate rounded squircle badge background with cyan border
badge = patches.FancyBboxPatch(
    (0.8, 0.8), 22.4, 22.4,
    boxstyle="round,pad=0.2,rounding_size=5",
    facecolor="#0a0c12",
    edgecolor="#38bdf8",
    linewidth=2.2,
    alpha=0.96
)
ax.add_patch(badge)

for d in paths:
    patch = patches.PathPatch(
        parse_path(d),
        facecolor="none",
        edgecolor="#38bdf8",
        linewidth=4.5, # Bold on 24x24 for high TV clarity
        capstyle="round",
        joinstyle="round"
    )
    ax.add_patch(patch)

ax.set_xlim(0, 24)
ax.set_ylim(24, 0) # Invert y to match SVG
ax.axis("off")
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

out_file = r"C:\Users\WJLEE\SynologyDrive\NAS\github.com\UX-Deck\sentinel_icon.png"
plt.savefig(out_file, transparent=True, dpi=128)
plt.close()
print("Generated:", out_file)
