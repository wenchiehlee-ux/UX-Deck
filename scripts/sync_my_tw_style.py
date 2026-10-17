import sys, os

idx_path = r"C:\Users\WJLEE\SynologyDrive\NAS\github.com\My-TW-Coverage\index.html"
with open(idx_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Google fonts to include Plus Jakarta Sans and Inter
old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">'
new_fonts = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700;800&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">'
)
if old_fonts in html:
    html = html.replace(old_fonts, new_fonts)
    print("Updated Google Fonts links.")

# 2. Add brand header element inside #app or inject via JavaScript hook so it always renders with the actual SVG icon
script_hook = """
    // UX-Deck: Inject Brand Bar with Real Cute Owl SVG Mascot
    window.$docsify.plugins = [].concat(function(hook, vm) {
      hook.ready(function() {
        var nav = document.querySelector('.app-nav');
        if (nav && !document.querySelector('.tw-nav-brand')) {
          var brand = document.createElement('a');
          brand.className = 'tw-nav-brand';
          brand.href = '#/';
          brand.innerHTML = '<div class="brand-icon-box"><svg class="ux-icon ux-icon-owl" style="width:22px;height:22px;"><use href="#icon-owl-coverage"></use></svg></div><span>My-TW-Coverage</span><span class="brand-tag">台股個股調研 🦉</span>';
          nav.appendChild(brand);
        }
      });
    }, window.$docsify.plugins || []);
"""

if "tw-nav-brand" not in html:
    html = html.replace("window.$docsify = {", script_hook + "\n    window.$docsify = {")
    print("Added brand injection hook.")

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(html)

print("My-TW-Coverage index.html fully synchronized with showcase.html style!")
