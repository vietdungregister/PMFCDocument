#!/usr/bin/env python3
"""
final_sidebar_polish.py
Two tasks in one run:

TASK A — Sprout: revert teal → peach on .nav-item .icon
  - .nav-item .icon: teal-400 → peach-200
  - .nav-item:hover:not(.active) .icon: teal-300 → peach-100
  - Remove any remaining 642 / 12 nav badges (should already be gone, safety pass)

TASK B — Bazaar: apply 6 sidebar polish patches
  1. Footer utility block
  2. Active item amber glow
  3. Group label amber dot
  4. User card amber glow + border-top
  5. Hover lift on inactive nav items
  6. Remove stat badges (642, 12) if present

Run from PMFCDocument root: python3 scripts/final_sidebar_polish.py
"""
import re, os, glob

def read(p):
    with open(p, encoding="utf-8") as f: return f.read()

def write(p, c):
    with open(p, "w", encoding="utf-8") as f: f.write(c)

# ══════════════════════════════════════════════════════════════════════════════
# TASK A — Sprout: peach icons (revert Patch 5 Rev teal)
# ══════════════════════════════════════════════════════════════════════════════

SPROUT_DIR = "mockups-sprout"

def sprout_revert_teal(content):
    """Replace teal values in the Patch 5 Rev .nav-item .icon block with peach."""
    # Replace the entire Patch 5 Rev CSS block
    old_block = re.compile(
        r'(/\* === Patch 5 Rev: Teal icons \(inactive\) / Peach \(active\) === \*/\n'
        r'  \.nav-item \.icon \{.*?\})\s*\n'
        r'  (\.nav-item\.active \.icon \{.*?\})\s*\n'
        r'  (\.nav-item:hover:not\(\.active\) \.icon \{.*?\})',
        re.DOTALL
    )
    new_block = (
        "/* === Patch 5: Peach icons (inactive) / Peach bright (active) === */\n"
        "  .nav-item .icon {\n"
        "    color: var(--sp-peach-200);\n"
        "    fill: var(--sp-peach-200);\n"
        "    opacity: 0.85;\n"
        "    transition: fill 0.15s, color 0.15s, opacity 0.15s;\n"
        "  }\n"
        "  .nav-item.active .icon {\n"
        "    color: var(--sp-peach-400);\n"
        "    fill: var(--sp-peach-400);\n"
        "    opacity: 1;\n"
        "  }\n"
        "  .nav-item:hover:not(.active) .icon {\n"
        "    color: var(--sp-peach-100);\n"
        "    fill: var(--sp-peach-100);\n"
        "    opacity: 1;\n"
        "  }"
    )
    return old_block.sub(new_block, content)

def sprout_remove_stat_badges(content):
    """Remove any remaining 642 / 12 nav-badge-pts spans (safety pass)."""
    content = re.sub(r'\s*<span class="nav-badge-pts">(642|12)</span>', '', content)
    return content

def run_sprout():
    files = sorted(glob.glob(os.path.join(SPROUT_DIR, "*.html")))
    files = [f for f in files if "_mood_demos" not in f
             and os.path.basename(f) != "home_full_layout.html"]
    count = 0
    for filepath in files:
        fname = os.path.basename(filepath)
        content = read(filepath)
        before = content
        content = sprout_revert_teal(content)
        content = sprout_remove_stat_badges(content)
        if content != before:
            write(filepath, content)
            count += 1
            print(f"  ✓ [Sprout] {fname}")
        else:
            print(f"  – [Sprout] {fname} [no change]")
    print(f"  Sprout: {count} files updated.\n")

# ══════════════════════════════════════════════════════════════════════════════
# TASK B — Bazaar: 6 sidebar polish patches
# ══════════════════════════════════════════════════════════════════════════════

BAZAAR_DIR = "mockups-bazaar"
SKIP_BAZAAR = {"home_full_layout.html"}

# ── B1: Footer CSS + HTML ────────────────────────────────────────────────────

BZ_FOOTER_CSS = """\
  /* === Bazaar Sidebar P1: Footer utility block === */
  .sidebar-footer { padding: 12px 16px; border-top: 1px solid var(--border-1); display: flex; flex-direction: column; gap: 10px; }
  .sf-social { display: flex; gap: 12px; }
  .sf-social a { color: var(--text-3); display: inline-grid; place-items: center; width: 22px; height: 22px; border-radius: 6px; transition: color 0.15s; text-decoration: none; }
  .sf-social a:hover { color: var(--bz-amber-400); }
  .sf-pills { display: flex; gap: 6px; flex-wrap: wrap; }
  .sf-pill { font-size: 10.5px; font-weight: 600; color: var(--text-3); background: var(--surface-2); padding: 4px 10px; border-radius: 999px; text-decoration: none; transition: all 0.15s; }
  .sf-pill:hover { color: var(--bz-amber-400); background: var(--bz-amber-soft); }
  .sf-copyright { font-size: 10px; color: var(--text-mute); text-align: center; margin-top: 2px; }
"""

BZ_FOOTER_HTML = """
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
    <div class="sf-copyright">© 2026 Stallspot</div>
  </div>
"""

# ── B2–5: Glow / label dot / user card / hover CSS ───────────────────────────

BZ_SIDEBAR_CSS = """\
  /* === Bazaar Sidebar P2: Active item amber glow === */
  .nav-item.active {
    box-shadow: 0 0 16px rgba(234, 181, 82, 0.18);
  }
  /* === Bazaar Sidebar P3: Group label amber dot === */
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
    background: var(--bz-amber-400);
    opacity: 0.6;
  }
  /* === Bazaar Sidebar P4: User card amber glow + border === */
  .user-card {
    box-shadow: 0 0 20px rgba(234, 181, 82, 0.10);
    border-top: 1px solid rgba(234, 181, 82, 0.20);
  }
  /* === Bazaar Sidebar P5: Hover lift === */
  .nav-item {
    transition: transform 0.15s var(--ease, ease), background 0.15s var(--ease, ease), color 0.12s var(--ease, ease), box-shadow 0.12s var(--ease, ease);
  }
  .nav-item:hover:not(.active) {
    transform: translateY(-1px);
    background: var(--bz-amber-soft);
  }
"""

BZ_MARKER = "Bazaar Sidebar P1"

def bz_patch_footer(content):
    """Inject footer CSS + HTML below user-card."""
    if "sidebar-footer" in content:
        return content  # already present
    content = content.replace("</style>", BZ_FOOTER_CSS + "</style>", 1)
    # Insert HTML after last </div> before </aside>
    content = re.sub(
        r'([ \t]*</div>\s*\n)([ \t]*</aside>)',
        r'\1' + BZ_FOOTER_HTML + r'\2',
        content, count=1
    )
    return content

def bz_patch_sidebar_css(content):
    """Inject P2–P5 CSS block."""
    if "Bazaar Sidebar P2" in content:
        return content  # already present
    return content.replace("</style>", BZ_SIDEBAR_CSS + "</style>", 1)

def bz_remove_stat_badges(content):
    """Remove 642 / 12 counter badges; keep My Profile red '3' badge."""
    # Remove numeric nav-badge-pts or nav-badge spans with specific numbers
    content = re.sub(r'\s*<span class="nav-badge-pts">(642|12)</span>', '', content)
    # Also handle plain nav-badge with those numbers
    content = re.sub(r'\s*<span class="nav-badge">(642|12)</span>', '', content)
    return content

def run_bazaar():
    files = sorted(glob.glob(os.path.join(BAZAAR_DIR, "*.html")))
    files = [f for f in files if "_mood_demos" not in f
             and os.path.basename(f) not in SKIP_BAZAAR]
    count = 0
    for filepath in files:
        fname = os.path.basename(filepath)
        content = read(filepath)
        before = content
        content = bz_patch_footer(content)
        content = bz_patch_sidebar_css(content)
        content = bz_remove_stat_badges(content)
        if content != before:
            write(filepath, content)
            count += 1
            print(f"  ✓ [Bazaar] {fname}")
        else:
            print(f"  – [Bazaar] {fname} [no change]")
    print(f"  Bazaar: {count} files updated.\n")

# ── main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Task A: Sprout — revert to peach icons ===")
    run_sprout()
    print("=== Task B: Bazaar — sidebar polish patches ===")
    run_bazaar()
    print("Done.")
