#!/usr/bin/env python3
"""
revert_patch6.py — Remove live counter badges (nav-badge-pts + nav-pulse) from all Sprout files.
Run from PMFCDocument root: python3 scripts/revert_patch6.py
"""
import re, os, glob

SPROUT_DIR = "mockups-sprout"

def read(p):
    with open(p, encoding="utf-8") as f: return f.read()

def write(p, c):
    with open(p, "w", encoding="utf-8") as f: f.write(c)

# ── Remove CSS block injected by Patch 6 ─────────────────────────────────────
CSS_PATTERN = re.compile(
    r'\n  /\* === Patch 6: Live counter badges === \*/\n'
    r'.*?'
    r'  \}\n',
    re.DOTALL
)

# ── Remove HTML badge/pulse spans ─────────────────────────────────────────────
# <span class="nav-badge-pts">642</span>  or  <span class="nav-badge-pts">12</span>
BADGE_SPAN  = re.compile(r'\s*<span class="nav-badge-pts">[^<]*</span>')
# <span class="nav-pulse" ...></span>
PULSE_SPAN  = re.compile(r'\s*<span class="nav-pulse"[^>]*></span>')

files = sorted(glob.glob(os.path.join(SPROUT_DIR, "*.html")))
files = [f for f in files if "_mood_demos" not in f]

count = 0
for filepath in files:
    content = read(filepath)
    before  = content

    content = CSS_PATTERN.sub("", content)
    content = BADGE_SPAN.sub("", content)
    content = PULSE_SPAN.sub("", content)

    if content != before:
        write(filepath, content)
        count += 1
        print(f"  ✓ {os.path.basename(filepath)}")
    else:
        print(f"  – {os.path.basename(filepath)} [no change]")

print(f"\n  Done — {count} files updated.")
