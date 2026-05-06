#!/usr/bin/env python3
"""
apply_sprout_patches_567.py
Apply Patches 5, 6, 7 to /mockups-sprout/*.html

Patch 5 — Color icons: CSS color per nav-group (stroke icons inherit via currentColor)
Patch 6 — Live counter badges on Points / Rewards pulse dot / Referrals
Patch 7 — Hover lift micro-interaction (translateY(-1px))

Run from PMFCDocument root: python3 scripts/apply_sprout_patches_567.py
"""

import re
import os
import glob

SPROUT_DIR = "mockups-sprout"
SKIP = {"home_full_layout.html"}

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ─────────────────────────────────────────────────────────────────────────────
# Patch 5 — Colored icons via CSS (no geometry change, stroke icons use
# currentColor which inherits color from the group container)
# Strategy:
#   1. Add CSS rules for .nav-group-discover / .nav-group-personal / .nav-group-earn
#   2. Add CSS override for .nav-item.active svg (peach-400, opacity 1)
#   3. Stamp group class names onto the 3 nav-group divs in HTML
# ─────────────────────────────────────────────────────────────────────────────

P5_CSS = """\
  /* === Patch 5: Colored nav icons by group === */
  /* Icons inherit stroke color via currentColor from these group containers */
  .nav-group-discover .nav-item svg,
  .nav-group-earn     .nav-item svg {
    color: var(--sp-peach-200);
    opacity: 0.85;
  }
  .nav-group-personal .nav-item svg {
    color: var(--sp-teal-300);
    opacity: 0.85;
  }
  /* Active overrides group color */
  .nav-item.active svg {
    color: var(--sp-peach-400);
    opacity: 1;
  }
  /* Hover inherits group tone at full opacity */
  .nav-group-discover .nav-item:hover svg,
  .nav-group-earn     .nav-item:hover svg {
    opacity: 1;
  }
  .nav-group-personal .nav-item:hover svg {
    opacity: 1;
  }
"""
P5_MARKER = "Patch 5"

def patch5_color_icons(content, filename):
    if filename in SKIP:
        return content, False
    before = content
    if P5_MARKER not in content:
        # 1. Inject CSS
        content = content.replace("</style>", P5_CSS + "</style>", 1)
        # 2. Add group class names to HTML nav-group divs
        content = content.replace(
            '<div class="nav-group">\n    <div class="nav-label">Discover</div>',
            '<div class="nav-group nav-group-discover">\n    <div class="nav-label">Discover</div>',
            1
        )
        content = content.replace(
            '<div class="nav-group">\n    <div class="nav-label">Personal</div>',
            '<div class="nav-group nav-group-personal">\n    <div class="nav-label">Personal</div>',
            1
        )
        content = content.replace(
            '<div class="nav-group">\n    <div class="nav-label">Earn</div>',
            '<div class="nav-group nav-group-earn">\n    <div class="nav-label">Earn</div>',
            1
        )
    changed = content != before
    return content, changed

# ─────────────────────────────────────────────────────────────────────────────
# Patch 6 — Live counter badges
# - Points nav item (href="rewards.html", text="Points"): badge "642"
# - Rewards nav item (href="points.html", text="Rewards"): 6px pulse dot
# - Referrals nav item (href="referrals.html"): badge "12"
# NOTE: "My Profile" badge (red "3") is KEPT AS-IS — only add new styles
# ─────────────────────────────────────────────────────────────────────────────

P6_CSS = """\
  /* === Patch 6: Live counter badges === */
  .nav-badge-pts {
    margin-left: auto;
    background: var(--sp-peach-soft);
    color: var(--sp-peach-400);
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 999px;
    line-height: 1.4;
    letter-spacing: -0.01em;
    flex-shrink: 0;
  }
  .nav-pulse {
    margin-left: auto;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--sp-peach-400);
    flex-shrink: 0;
    animation: pulse-ring 2s infinite;
    box-shadow: 0 0 0 0 rgba(232, 168, 124, 0.5);
  }
  @keyframes pulse-ring {
    0%   { box-shadow: 0 0 0 0   rgba(232, 168, 124, 0.5); }
    70%  { box-shadow: 0 0 0 5px rgba(232, 168, 124, 0); }
    100% { box-shadow: 0 0 0 0   rgba(232, 168, 124, 0); }
  }
"""
P6_MARKER = "Patch 6"

# Patterns to find each nav item end-line and inject badge before </a>
# The Points item: href="rewards.html" with text "Points"
# The Rewards item: href="points.html" with text "Rewards"
# The Referrals item: href="referrals.html"

# Matching approach: find the nav-item block by href, replace the text node to add badge
# We'll use a targeted regex for each item.

def _inject_badge_into_item(content, href, badge_html):
    """
    Find <a class="nav-item..." href="{href}">...[no existing badge-pts/pulse]...</a>
    and insert badge_html before </a>.
    Only injects if badge is not already present.
    """
    # Skip if already injected
    if f'href="{href}"' not in content:
        return content
    
    # Build pattern: find the specific nav-item, check it doesn't already have our badge
    pattern = re.compile(
        r'(<a class="nav-item[^"]*" href="' + re.escape(href) + r'">'
        r'(?:(?!</a>).)*?)'
        r'(\s*</a>)',
        re.DOTALL
    )
    def replacer(m):
        block = m.group(1)
        # Don't double-inject
        if 'nav-badge-pts' in block or 'nav-pulse' in block:
            return m.group(0)
        return block + '\n      ' + badge_html + m.group(2)
    
    return pattern.sub(replacer, content)

def patch6_live_badges(content, filename):
    if filename in SKIP:
        return content, False
    before = content
    if P6_MARKER not in content:
        # 1. Inject CSS
        content = content.replace("</style>", P6_CSS + "</style>", 1)
        # 2. Add badges to specific nav items
        # Points item (rewards.html → "Points")
        content = _inject_badge_into_item(
            content, "rewards.html",
            '<span class="nav-badge-pts">642</span>'
        )
        # Rewards item (points.html → "Rewards") — pulse dot
        content = _inject_badge_into_item(
            content, "points.html",
            '<span class="nav-pulse" title="Unclaimed rewards"></span>'
        )
        # Referrals item
        content = _inject_badge_into_item(
            content, "referrals.html",
            '<span class="nav-badge-pts">12</span>'
        )
    changed = content != before
    return content, changed

# ─────────────────────────────────────────────────────────────────────────────
# Patch 7 — Hover micro-interaction (translateY(-1px) lift)
# Adds transform to nav-item hover, blocks it on active
# ─────────────────────────────────────────────────────────────────────────────

P7_CSS = """\
  /* === Patch 7: Hover lift micro-interaction === */
  .nav-item {
    transition: transform 0.15s var(--ease, ease), background 0.15s var(--ease, ease), color 0.12s var(--ease, ease), box-shadow 0.12s var(--ease, ease);
  }
  .nav-item:hover {
    transform: translateY(-1px);
    background: var(--sp-peach-soft);
    color: var(--text-1);
  }
  .nav-item.active:hover {
    transform: none;
  }
"""
P7_MARKER = "Patch 7"

def patch7_hover_lift(content, filename):
    if filename in SKIP:
        return content, False
    before = content
    if P7_MARKER not in content:
        content = content.replace("</style>", P7_CSS + "</style>", 1)
    changed = content != before
    return content, changed

# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    files = sorted(glob.glob(os.path.join(SPROUT_DIR, "*.html")))
    files = [f for f in files if "_mood_demos" not in f]

    stats = {"p5": 0, "p6": 0, "p7": 0}

    for filepath in files:
        filename = os.path.basename(filepath)
        content = read(filepath)

        content, c5 = patch5_color_icons(content, filename)
        if c5: stats["p5"] += 1

        content, c6 = patch6_live_badges(content, filename)
        if c6: stats["p6"] += 1

        content, c7 = patch7_hover_lift(content, filename)
        if c7: stats["p7"] += 1

        changed = any([c5, c6, c7])
        if changed:
            write(filepath, content)
            applied = ", ".join([k for k, v in [("P5", c5), ("P6", c6), ("P7", c7)] if v])
            print(f"  ✓ {filename:50s} [{applied}]")
        else:
            print(f"  – {filename:50s} [no changes]")

    print()
    print("=== Summary ===")
    print(f"  Patch 5 (colored icons CSS + group classes):  {stats['p5']} files")
    print(f"  Patch 6 (live badges + pulse dot):            {stats['p6']} files")
    print(f"  Patch 7 (hover translateY lift):              {stats['p7']} files")

if __name__ == "__main__":
    main()
