import sys

idx_path = r"C:\Users\WJLEE\SynologyDrive\NAS\github.com\My-TW-Coverage\index.html"
with open(idx_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Clean up duplicate window.$docsify.plugins before declaration
html = html.replace("""    // UX-Deck: Inject Brand Bar with Real Cute Owl SVG Mascot
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
    }, window.$docsify.plugins || []);\n""", "")

# 2. Insert properly into window.$docsify.plugins array
target = "plugins: ["
replacement = """plugins: [
        // UX-Deck: Inject Brand Bar with Real Cute Owl SVG Mascot
        function(hook, vm) {
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
          hook.doneEach(function() {
            var nav = document.querySelector('.app-nav');
            if (nav && !document.querySelector('.tw-nav-brand')) {
              var brand = document.createElement('a');
              brand.className = 'tw-nav-brand';
              brand.href = '#/';
              brand.innerHTML = '<div class="brand-icon-box"><svg class="ux-icon ux-icon-owl" style="width:22px;height:22px;"><use href="#icon-owl-coverage"></use></svg></div><span>My-TW-Coverage</span><span class="brand-tag">台股個股調研 🦉</span>';
              nav.appendChild(brand);
            }
          });
        },"""

if target in html and "UX-Deck: Inject Brand Bar" not in html:
    html = html.replace(target, replacement, 1)
    print("Correctly placed brand injection inside window.$docsify.plugins!")

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html hook fixed!")
