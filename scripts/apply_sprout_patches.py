#!/usr/bin/env python3
"""
apply_sprout_patches.py
Apply 4 post-implementation polish patches to /mockups-sprout/*.html
DO NOT touch /mockups-bazaar/ or /mockups-sprout/_mood_demos/
Run from PMFCDocument root: python3 scripts/apply_sprout_patches.py
"""

import re
import os
import glob

SPROUT_DIR = "mockups-sprout"

# Files to skip (standalone pages without sidebar or meta-redirect)
SKIP_SIDEBAR = {"home_full_layout.html"}

# ── helpers ───────────────────────────────────────────────────────────────────

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def patch_count(content, marker):
    return content.count(marker)

# ── Patch 1: Remove duplicate brand element ───────────────────────────────────

# The duplicate is the orphaned span pair that has no logo SVG attached.
# Pattern: <span class="logo-text">Sprout</span><span class="logo-sub" ...>the meme garden</span>
# followed by </a> — the leftover from the Bazaar refactor that was never cleaned.
# It sits outside the proper logo <div> after line </div> </div>

DUPE_PATTERN = re.compile(
    r'\s*<span class="logo-text">Sprout</span>'
    r'<span class="logo-sub"[^>]*>the meme garden</span>\s*\n'
    r'\s*</a>\s*\n',
    re.DOTALL
)

DUPE_REPLACEMENT = "\n"

def patch1_remove_duplicate_brand(content, filename):
    """Remove orphaned logo-text/logo-sub span after the closing logo </div>"""
    # The duplicate always looks like:
    #     <span class="logo-text">Sprout</span><span class="logo-sub" ...>the meme garden</span>
    #   </a>
    # right before the header-search div.
    # It appears as a bare text outside the logo container.
    before = content
    content = re.sub(
        r'[ \t]*<span class="logo-text">Sprout</span>'
        r'<span class="logo-sub"[^>]*>the meme garden</span>\s*\n'
        r'[ \t]*</a>\s*\n',
        '\n',
        content
    )
    changed = content != before
    return content, changed

# ── Patch 2: Point System → Points ───────────────────────────────────────────

def patch2_point_system_to_points(content, filename):
    before = content
    content = content.replace("Point System", "Points")
    changed = content != before
    return content, changed

# ── Patch 3: Fix body ambient glow override ───────────────────────────────────
# The injected Mood B block sets background + background-image + background-attachment at lines ~55-60.
# Then the main stylesheet has a second body { background: var(--bg); ... } rule that strips background-image.
# Fix: replace the plain `background: var(--bg);` in the SECOND body block with the full 3-line glow.

BODY_OVERRIDE_PATTERN = re.compile(
    r'(  body \{\s*\n)'                      # "  body {\n"
    r'([ \t]+background: var\(--bg\);\s*\n)' # "    background: var(--bg);\n"  ← the offender
    r'([ \t]+color:)',                        # next line starts with "    color:"
    re.MULTILINE
)

BODY_GLOW_REPLACEMENT = (
    r'\1'
    r'    background: var(--bg);\n'
    r'    background-image:\n'
    r'      radial-gradient(ellipse 800px 400px at 20% 0%, rgba(232,168,124,0.06), transparent 60%),\n'
    r'      radial-gradient(ellipse 600px 400px at 90% 30%, rgba(124,196,164,0.05), transparent 60%);\n'
    r'    background-attachment: fixed;\n'
    r'\3'
)

def patch3_fix_body_glow(content, filename):
    """Replace stripped body background with full glow version in the second body block"""
    before = content
    # Only patch if the override pattern exists AND the glow isn't already in the second body block.
    # Count how many body { background: var(--bg); } occurrences there are without background-image following.
    # Strategy: find the second body { rule (after the glow injection block ends) and fix it.
    
    # Check if the second body block already has background-image (already fixed)
    # We look for the pattern: second body block with plain background: var(--bg); followed by color:
    if BODY_OVERRIDE_PATTERN.search(content):
        content = BODY_OVERRIDE_PATTERN.sub(BODY_GLOW_REPLACEMENT, content)
    changed = content != before
    return content, changed

# ── Patch 4a: Sidebar footer CSS + HTML ──────────────────────────────────────

SIDEBAR_FOOTER_CSS = """\
  /* === Patch 4a: Sidebar footer utility block === */
  .sidebar-footer { padding: 12px 16px; border-top: 1px solid var(--border-1); display: flex; flex-direction: column; gap: 10px; }
  .sf-social { display: flex; gap: 12px; }
  .sf-social a { color: var(--text-3); display: inline-grid; place-items: center; width: 22px; height: 22px; border-radius: 6px; transition: color 0.15s; text-decoration: none; }
  .sf-social a:hover { color: var(--sp-peach-400); }
  .sf-pills { display: flex; gap: 6px; flex-wrap: wrap; }
  .sf-pill { font-size: 10.5px; font-weight: 600; color: var(--text-3); background: var(--surface-2); padding: 4px 10px; border-radius: 999px; text-decoration: none; transition: all 0.15s; }
  .sf-pill:hover { color: var(--sp-peach-400); background: var(--sp-peach-soft); }
  .sf-copyright { font-size: 10px; color: var(--text-mute); text-align: center; margin-top: 2px; }
"""

SIDEBAR_FOOTER_HTML = """
  <!-- Sidebar footer: social + doc pills + copyright -->
  <div class="sidebar-footer">
    <div class="sf-social">
      <a href="#" aria-label="Telegram">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.894 8.221-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.447 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.12L7.167 13.958l-2.946-.924c-.64-.203-.658-.64.135-.954l11.566-4.463c.537-.194 1.006.131.972.604z"/></svg>
      </a>
      <a href="#" aria-label="X">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.745l7.73-8.835L1.254 2.25H8.08l4.261 5.632 5.903-5.632zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
      </a>
    </div>
    <div class="sf-pills">
      <a class="sf-pill" href="#">Doc</a>
      <a class="sf-pill" href="#">FAQ</a>
      <a class="sf-pill" href="#">How it works</a>
    </div>
    <div class="sf-copyright">© 2026 Sprout</div>
  </div>
"""

SIDEBAR_FOOTER_MARKER = "sidebar-footer"

def patch4a_sidebar_footer(content, filename):
    """Add sidebar footer CSS + HTML block below user-card"""
    if filename in SKIP_SIDEBAR:
        return content, False
    before = content

    # 1. Inject CSS (before </style> or before the first media query or layout rules)
    if SIDEBAR_FOOTER_MARKER not in content:
        # Add CSS before </style>
        content = content.replace("</style>", SIDEBAR_FOOTER_CSS + "</style>", 1)

        # 2. Add HTML: after the closing </div> of .user-card and before </aside>
        content = re.sub(
            r'([ \t]*</div>\s*\n)([ \t]*</aside>)',
            r'\1' + SIDEBAR_FOOTER_HTML + r'\2',
            content,
            count=1
        )

    changed = content != before
    return content, changed

# ── Patch 4b: Active item glow + group label refinement ──────────────────────

PATCH_4B_CSS = """\
  /* === Patch 4b: Active item glow + group label refinement === */
  .nav-item.active {
    box-shadow: 0 0 16px rgba(232, 168, 124, 0.18);
  }
  .nav-label {
    letter-spacing: 0.12em;
    position: relative;
    padding-left: 14px;
  }
  .nav-label::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: var(--sp-peach-400);
    opacity: 0.6;
  }
"""

PATCH_4B_MARKER = "Patch 4b"

def patch4b_active_glow_label(content, filename):
    if filename in SKIP_SIDEBAR:
        return content, False
    before = content
    if PATCH_4B_MARKER not in content:
        content = content.replace("</style>", PATCH_4B_CSS + "</style>", 1)
    changed = content != before
    return content, changed

# ── Patch 4c: User card bottom anchor ────────────────────────────────────────

PATCH_4C_CSS = """\
  /* === Patch 4c: User card anchor + tier-aware points color === */
  .user-card {
    box-shadow: 0 0 20px rgba(232, 168, 124, 0.10);
    border-top: 1px solid rgba(232, 168, 124, 0.20);
  }
  .uc-pts.tier-seed,
  .uc-pts.tier-sprout      { color: var(--text-1); }
  .uc-pts.tier-sapling     { color: var(--sp-peach-400); }
  .uc-pts.tier-tree        { color: var(--sp-teal-400); }
  .uc-pts.tier-ancient     { color: var(--sp-peach-200); text-shadow: 0 0 8px rgba(232,168,124,0.4); }
"""

PATCH_4C_MARKER = "Patch 4c"

def patch4c_user_card(content, filename):
    if filename in SKIP_SIDEBAR:
        return content, False
    before = content
    if PATCH_4C_MARKER not in content:
        content = content.replace("</style>", PATCH_4C_CSS + "</style>", 1)

        # Apply tier class to the points span in user-tier.
        # Current markup: <div class="user-tier">Sprout · 642 pts</div>
        # or <div class="user-tier">Sapling · 1,200 pts</div>
        # We wrap the pts value in a span with the appropriate tier class.
        # Detect tier from the text and add class to the whole div as data, 
        # or simply tag the user-tier div with a tier class for use.
        
        def add_tier_class(m):
            text = m.group(0)
            tier_lower = ""
            t = m.group(1).lower()
            if "ancient" in t:
                tier_lower = "tier-ancient"
            elif "tree" in t:
                tier_lower = "tier-tree"
            elif "sapling" in t:
                tier_lower = "tier-sapling"
            elif "sprout" in t:
                tier_lower = "tier-sprout"
            else:
                tier_lower = "tier-seed"
            # Replace <div class="user-tier"> with one that includes uc-pts on the pts part
            # user-tier text is like "Sprout · 642 pts"
            # We'll add a span around the pts portion
            inner = m.group(2)
            # Split at ·
            parts = inner.split("·")
            if len(parts) >= 2:
                pts_part = parts[-1].strip()
                tier_part = "·".join(parts[:-1])
                new_inner = f'{tier_part}· <span class="uc-pts {tier_lower}">{pts_part}</span>'
                return text.replace(inner, new_inner)
            return text

        content = re.sub(
            r'<div class="user-tier">(([^<]*(?:Seed|Sprout|Sapling|Tree|Ancient)[^<]*?))</div>',
            add_tier_class,
            content,
            flags=re.IGNORECASE
        )

    changed = content != before
    return content, changed

# ── main ──────────────────────────────────────────────────────────────────────

def main():
    files = sorted(glob.glob(os.path.join(SPROUT_DIR, "*.html")))
    # Exclude _mood_demos (they are in a subdir, glob won't get them, but safety check)
    files = [f for f in files if "_mood_demos" not in f]

    stats = {
        "p1": 0, "p2": 0, "p3": 0, "p4a": 0, "p4b": 0, "p4c": 0
    }

    for filepath in files:
        filename = os.path.basename(filepath)
        content = read(filepath)
        changed_any = False

        content, c1 = patch1_remove_duplicate_brand(content, filename)
        if c1: stats["p1"] += 1

        content, c2 = patch2_point_system_to_points(content, filename)
        if c2: stats["p2"] += 1

        content, c3 = patch3_fix_body_glow(content, filename)
        if c3: stats["p3"] += 1

        content, c4a = patch4a_sidebar_footer(content, filename)
        if c4a: stats["p4a"] += 1

        content, c4b = patch4b_active_glow_label(content, filename)
        if c4b: stats["p4b"] += 1

        content, c4c = patch4c_user_card(content, filename)
        if c4c: stats["p4c"] += 1

        changed_any = any([c1, c2, c3, c4a, c4b, c4c])
        if changed_any:
            write(filepath, content)
            patches_applied = ", ".join([
                k for k, v in [("P1", c1), ("P2", c2), ("P3", c3), ("P4a", c4a), ("P4b", c4b), ("P4c", c4c)] if v
            ])
            print(f"  ✓ {filename:50s} [{patches_applied}]")
        else:
            print(f"  – {filename:50s} [no changes]")

    print()
    print("=== Summary ===")
    print(f"  Patch 1 (duplicate brand removed):     {stats['p1']} files")
    print(f"  Patch 2 (Point System → Points):       {stats['p2']} files")
    print(f"  Patch 3 (body glow override fixed):    {stats['p3']} files")
    print(f"  Patch 4a (sidebar footer added):       {stats['p4a']} files")
    print(f"  Patch 4b (active glow + label dot):    {stats['p4b']} files")
    print(f"  Patch 4c (user card tier styling):     {stats['p4c']} files")

if __name__ == "__main__":
    main()
