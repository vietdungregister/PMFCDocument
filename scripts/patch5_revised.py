#!/usr/bin/env python3
"""
patch5_revised.py
Replace Patch 5 (group-based peach icon coloring) with Patch 5 Revised
(teal inactive / peach active icons via .icon class on SVGs).

Changes:
1. Remove old Patch 5 CSS block (group-container color approach)
2. Remove nav-group-discover/personal/earn class names from HTML divs
3. Add class="icon" to each SVG that is a direct child of a nav-item <a>
4. Inject new Patch 5 Rev CSS using .nav-item .icon selectors

Run from PMFCDocument root: python3 scripts/patch5_revised.py
"""
import re, os, glob

SPROUT_DIR = "mockups-sprout"
SKIP = {"home_full_layout.html"}

def read(p):
    with open(p, encoding="utf-8") as f: return f.read()

def write(p, c):
    with open(p, "w", encoding="utf-8") as f: f.write(c)

# ── 1. Remove old Patch 5 CSS block ──────────────────────────────────────────
OLD_P5_CSS = re.compile(
    r'\n  /\* === Patch 5: Colored nav icons by group === \*/\n'
    r'.*?'
    r'  \.nav-group-personal \.nav-item:hover svg \{\s*\n'
    r'    opacity: 1;\s*\n'
    r'  \}\n',
    re.DOTALL
)

# ── 2. Remove group class names from nav-group divs ──────────────────────────
def strip_group_classes(content):
    content = content.replace(
        ' class="nav-group nav-group-discover"', ' class="nav-group"'
    )
    content = content.replace(
        ' class="nav-group nav-group-personal"', ' class="nav-group"'
    )
    content = content.replace(
        ' class="nav-group nav-group-earn"', ' class="nav-group"'
    )
    return content

# ── 3. Add class="icon" to nav-item SVGs ─────────────────────────────────────
# Target SVGs inside <a class="nav-item..."> blocks.
# They look like: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
# We'll match the nav-item block and add class="icon" to the first svg in each.

NAV_ITEM_BLOCK = re.compile(
    r'(<a class="nav-item[^"]*"[^>]*>)(.*?)(</a>)',
    re.DOTALL
)

SVG_TAG = re.compile(
    r'<svg\b([^>]*?)>'
)

def add_icon_class_to_svg(m):
    opening = m.group(1)
    inner   = m.group(2)
    closing = m.group(3)

    def svg_replacer(sm):
        attrs = sm.group(1)
        if 'class="icon"' in attrs or "class='icon'" in attrs:
            return sm.group(0)  # already has class
        # Prepend class="icon" to attrs
        return f'<svg class="icon"{attrs}>'

    # Only replace the FIRST svg in this nav-item block
    modified, count = SVG_TAG.subn(svg_replacer, inner, count=1)
    return opening + modified + closing

def inject_icon_class(content):
    return NAV_ITEM_BLOCK.sub(add_icon_class_to_svg, content)

# ── 4. New Patch 5 Rev CSS ────────────────────────────────────────────────────
NEW_P5_CSS = """\
  /* === Patch 5 Rev: Teal icons (inactive) / Peach (active) === */
  .nav-item .icon {
    color: var(--sp-teal-400);       /* controls currentColor for stroke SVGs */
    fill: var(--sp-teal-400);        /* ready for fill-based icon swap */
    opacity: 0.85;
    transition: fill 0.15s, color 0.15s, opacity 0.15s;
  }
  .nav-item.active .icon {
    color: var(--sp-peach-400);
    fill: var(--sp-peach-400);
    opacity: 1;
  }
  .nav-item:hover:not(.active) .icon {
    color: var(--sp-teal-300);
    fill: var(--sp-teal-300);
    opacity: 1;
  }
"""

# ── main ─────────────────────────────────────────────────────────────────────

files = sorted(glob.glob(os.path.join(SPROUT_DIR, "*.html")))
files = [f for f in files if "_mood_demos" not in f]

count = 0
for filepath in files:
    filename = os.path.basename(filepath)
    if filename in SKIP:
        print(f"  – {filename:50s} [skipped]")
        continue

    content = read(filepath)
    before  = content

    # 1. Remove old P5 CSS
    content = OLD_P5_CSS.sub("", content)

    # 2. Strip group class names from divs
    content = strip_group_classes(content)

    # 3. Add class="icon" to nav-item SVGs
    content = inject_icon_class(content)

    # 4. Inject new P5 Rev CSS (replace old marker or append before </style>)
    if "Patch 5 Rev" not in content:
        content = content.replace("</style>", NEW_P5_CSS + "</style>", 1)

    if content != before:
        write(filepath, content)
        count += 1
        print(f"  ✓ {filename}")
    else:
        print(f"  – {filename} [no change]")

print(f"\n  Done — {count} files updated.")
