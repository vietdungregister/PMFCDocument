#!/usr/bin/env python3
"""
Clone /mockups-bazaar/ → /mockups-sprout/ with brand swap.

Bazaar → Sprout transforms:
  · Color palette: amber → peach, brown → forest green
  · Mascot SVG: cat hawker → sprout (cây con với 2 lá)
  · Brand identity: Stallspot → Sprout, "the meme bazaar" → "the meme garden"
  · Tagline: surface-specific versions → Sprout equivalents
  · Marquee: bazaar phrases → garden phrases
  · Tier ladder: Newcomer/Regular/Local/Insider/Legend → Seed/Sprout/Sapling/Tree/Ancient Tree
  · Microcopy: "stall by" → "by", "the lucky draw" → "the daily harvest", etc.
  · Connected wallet, sidebar structure, page architecture: UNCHANGED (3-layer principle compliant)
  · Mood B signature glow: injected into every page after :root block (SPROUT_UI_SPEC.md §1.3a)

Run:
  cd /path/to/PMFCDocument
  python3 scripts/clone_to_sprout.py

Output: /mockups-sprout/ folder with 18 HTML files cloned + brand-swapped.
Last updated: 2026-05-06 — Mood B glow + surface palette refinement (locked values)
"""
import os, re, sys

# Auto-detect root directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
SRC = os.path.join(ROOT, 'mockups-bazaar')
DST = os.path.join(ROOT, 'mockups-sprout')

if not os.path.isdir(SRC):
    print(f'ERROR: source dir not found: {SRC}')
    print('Run this script from project root or /scripts/ subdirectory.')
    sys.exit(1)

os.makedirs(DST, exist_ok=True)

# ===== SVG: cat hawker → sprout =====
CAT_32_RE = re.compile(
    r'<svg viewBox="0 0 32 32" fill="none"[^>]*>\s*'
    r'<path d="M3 12L16 5L29 12L26 13L16 8L6 13Z"[\s\S]*?</svg>',
    re.MULTILINE
)
SPROUT_32 = '''<svg viewBox="0 0 32 32" fill="none">
        <ellipse cx="16" cy="24" rx="9" ry="6" fill="#8B4513"/>
        <ellipse cx="11" cy="14" rx="3" ry="6" transform="rotate(-25 11 14)" fill="#7cc4a4"/>
        <ellipse cx="21" cy="14" rx="3" ry="6" transform="rotate(25 21 14)" fill="#5ba886"/>
        <rect x="15" y="16" width="2" height="8" fill="#3d7458"/>
        <circle cx="13" cy="25" r="0.8" fill="#1a1208"/>
        <circle cx="19" cy="25" r="0.8" fill="#1a1208"/>
        <path d="M 13 27 Q 16 28.5 19 27" stroke="#1a1208" stroke-width="0.7" fill="none" stroke-linecap="round"/>
      </svg>'''

CAT_24_RE = re.compile(
    r'<svg viewBox="0 0 24 24" fill="none"[^>]*>\s*'
    r'<path d="M3 9L12 5L21 9"[\s\S]*?</svg>',
    re.MULTILINE
)
SPROUT_24 = '''<svg viewBox="0 0 24 24" fill="none">
        <ellipse cx="12" cy="18" rx="7" ry="4" fill="#8B4513"/>
        <ellipse cx="8" cy="10" rx="2.5" ry="5" transform="rotate(-25 8 10)" fill="#7cc4a4"/>
        <ellipse cx="16" cy="10" rx="2.5" ry="5" transform="rotate(25 16 10)" fill="#5ba886"/>
        <rect x="11" y="12" width="2" height="6" fill="#3d7458"/>
        <circle cx="10" cy="19" r="0.6" fill="#1a1208"/>
        <circle cx="14" cy="19" r="0.6" fill="#1a1208"/>
        <path d="M 10 20.5 Q 12 21.5 14 20.5" stroke="#1a1208" stroke-width="0.5" fill="none" stroke-linecap="round"/>
      </svg>'''

CAT_64_RE = re.compile(
    r'<svg viewBox="0 0 64 64" fill="none"[^>]*>\s*'
    r'<path d="M5 22L32 12L59 22[\s\S]*?</svg>',
    re.MULTILINE
)
SPROUT_64 = '''<svg viewBox="0 0 64 64" fill="none">
        <ellipse cx="32" cy="46" rx="16" ry="11" fill="#8B4513"/>
        <ellipse cx="24" cy="28" rx="6" ry="11" transform="rotate(-25 24 28)" fill="#7cc4a4"/>
        <ellipse cx="40" cy="28" rx="6" ry="11" transform="rotate(25 40 28)" fill="#5ba886"/>
        <rect x="30" y="30" width="4" height="14" fill="#3d7458"/>
        <circle cx="27" cy="48" r="1.5" fill="#1a1208"/>
        <circle cx="37" cy="48" r="1.5" fill="#1a1208"/>
        <path d="M 27 51 Q 32 53.5 37 51" stroke="#1a1208" stroke-width="1.2" fill="none" stroke-linecap="round"/>
      </svg>'''

# ===== CSS Variable RENAMES (--bz-* → --sp-*) =====
CSS_RENAMES = [
    ('--bz-amber-100', '--sp-peach-100'),
    ('--bz-amber-200', '--sp-peach-200'),
    ('--bz-amber-400', '--sp-peach-400'),
    ('--bz-amber-500', '--sp-peach-500'),
    ('--bz-amber-soft', '--sp-peach-soft'),
    ('--bz-amber-glow', '--sp-peach-glow'),
    ('--bz-brown-300', '--sp-forest-300'),
    ('--bz-brown-500', '--sp-forest-500'),
    ('--bz-brown-700', '--sp-forest-700'),
    ('--bz-cream', '--sp-cream'),
    ('--bz-teal-300', '--sp-teal-300'),
    ('--bz-teal-400', '--sp-teal-400'),
    ('--bz-teal-500', '--sp-teal-500'),
    ('--bz-teal-soft', '--sp-teal-soft'),
    ('--bz-teal-glow', '--sp-teal-glow'),
    ('--bz-crimson', '--sp-crimson'),
]

# ===== Hex color swaps (ORDER MATTERS — longer/specific first) =====
HEX_SWAPS = [
    # Surface palette: dark navy → green-tinted twilight (Mood B locked 2026-05-05)
    ('#0a0e1a', '#0a1610'),     # bg
    ('#131826', '#131f18'),     # surface-1  (refined from #13201a)
    ('#1a2138', '#1a2a20'),     # surface-2  (refined from #1a2a22)
    ('#232b46', '#243528'),     # surface-3  (refined from #23332b)
    ('#1f2640', '#1f2d24'),     # border-1   (refined from #1f2a23)
    ('#2a3456', '#2d4234'),     # border-2   (refined from #2a3a30)
    # Text palette: slightly warmer for Sprout (greenish tint)
    ('#f4f4f5', '#f5f7f4'),     # text-1
    ('#a1a1aa', '#a3b0a7'),     # text-2
    ('#71717a', '#6f7d74'),     # text-3
    ('#52525b', '#4a5650'),     # text-mute
    # Brand: amber → peach
    ('#F5DBA8', '#f4cba0'),
    ('#FAC775', '#e8a87c'),
    ('#EAB552', '#e8a87c'),
    ('#C49152', '#d68a5b'),
    # Brown → forest green
    ('#8B5A3C', '#5ba886'),
    ('#5a3818', '#3d7458'),
    ('#3a2410', '#3d7458'),
    # rgba (amber → peach)
    ('rgba(234, 181, 82, 0.10)', 'rgba(232, 168, 124, 0.10)'),
    ('rgba(234, 181, 82, 0.18)', 'rgba(232, 168, 124, 0.18)'),
    ('rgba(234,181,82,0.10)', 'rgba(232,168,124,0.10)'),
    ('rgba(234,181,82,0.18)', 'rgba(232,168,124,0.18)'),
    # Teal soft (Bazaar rgba → Sprout rgba with 0.14 alpha per spec)
    ('rgba(124, 196, 164, 0.10)', 'rgba(124, 196, 164, 0.14)'),
    ('rgba(124,196,164,0.10)', 'rgba(124,196,164,0.14)'),
]

# ===== CSS class renames (.amber → .peach for marquee) =====
CLASS_SWAPS = [
    ('.marquee-track .amber {', '.marquee-track .peach {'),
    ('class="amber"', 'class="peach"'),
]

# ===== Brand text swaps (ORDER MATTERS — apply longest specific first) =====
TEXT_SWAPS = [
    # Brand FIRST (must run before "Regular" → "Sprout" tier swap)
    ('Stallspot', 'Sprout'),
    ('the meme bazaar', 'the meme garden'),
    # Taglines — Group A introduced surface-specific taglines; map to Sprout equivalent
    ('Open a stall. Pitch your meme.', 'Plant your seed in the memeconomy.'),  # creator funnel
    ('Trade memes at the bazaar.', 'Plant your seed in the memeconomy.'),       # hero
    ('Open a stall. Trade memes.', 'Plant your seed in the memeconomy.'),       # deprecated compound (safety)
    # Search placeholder
    ('Search the bazaar — tokens, vendors, addresses…',
     'Search the garden — tokens, creators, addresses…'),
    # Marquee phrases
    ('OPEN A STALL', 'PLANT YOUR SEED'),
    ('TRADE MEMES', "WATCH WHAT'S BLOOMING"),
    ('WATCH THE CROWD', 'MAKE MONEY ON THE MEMECONOMY'),
    ('NO RIGGED SCALES', 'NO BOT DRAMA'),
    ('BIGGEST CROWD WINS', 'TALLEST TREE WINS'),
    ('TIPS WHISPERED HERE', 'SEEDS PLANTED HERE'),
    # Tier ladder names — replace LONGER specific phrases first
    ('Bazaar baron', 'Ancient Tree'),    # in case any leftover
    ('Newcomer', 'Seed'),
    ('Regular', 'Sprout'),
    ('Local', 'Sapling'),
    ('Insider', 'Tree'),
    ('Legend', 'Ancient Tree'),
    # Tier descriptions
    ('Just arrived at the bazaar.', 'A fresh seed in the soil.'),
    ('Coming back often.', 'Sprouting roots.'),
    ('You belong here.', 'Growing strong in the garden.'),
    ('You know the deals.', 'A sturdy tree.'),
    ('Everyone knows your name.', 'An ancient tree of legend.'),
    # Microcopy — precise replacements
    ('stall by ', 'by '),           # trailing-space variant (token cards, etc.)
    ('<span>stall by</span>', '<span>by</span>'),  # no-space variant (leaderboard spans)
    ('Stall story', 'Token story'),
    # Rewards — Bazaar Group A changed subtitle to "The lucky draw." → Sprout uses "the daily harvest."
    ('The lucky draw. Spend a ticket, spin five reels, win SOL.',
     'The daily harvest. Spend a ticket, spin five reels, win SOL.'),
    ('the lucky draw', 'the daily harvest'),
    ('the lucky vendor draw', 'the daily harvest'),
    # Referrals
    ('Bring a friend to the bazaar.', 'Plant a friend in the garden.'),
    ('Bring a friend to the bazaar', 'Plant a friend in the garden'),
    ('Hand out your stall card.', 'Share your seed packet.'),
    ('Hand out your stall card', 'Share your seed packet'),
    ('5% commission when they trade at your stall',
     '5% commission when they trade in your garden'),
    # Arena
    ('Showdown row', 'Garden arena'),
    ('back winners · the crowd predicts',
     'back winners · the garden predicts'),
    # Points
    ('Earn points by trading, creating, and bringing the crowd. Climb the bazaar.',
     'Earn points by trading, creating, and bringing friends. Grow your garden.'),
    # Referrals longer forms
    ('Bring a friend to the bazaar. Earn when they trade.',
     'Plant a friend in the garden. Earn when they trade.'),
    ('No referrals yet', 'No seeds planted yet'),
    ('Share your link to start earning. The bazaar grows when you bring people in.',
     'Share your link to start earning. The garden grows when you bring people in.'),
    ('https://stallspot.app/join/@', 'https://sprout.app/join/@'),
    # Graduation moment
    ('has franchised across the bazaar', 'has bloomed in the garden'),
    # CSS comments (cosmetic)
    ('Bazaar primary — amber (warm bazaar lantern)',
     'Sprout primary — peach (sunset over garden)'),
    ('Bazaar secondary — brown (counter, structural)',
     'Sprout secondary — forest green (stem, leaf)'),
    ('Teal — preserved from Sprout for SUCCESS / OK semantics',
     'Teal — leaf/bloom accents'),
]

# ===== Mood B Signature Glow CSS =====
# Locked 2026-05-05 — SPROUT_UI_SPEC.md §1.3a. Do NOT modify without spec update.
GLOW_CSS = """
/* === Mood B signature glow (locked 2026-05-05 — SPROUT_UI_SPEC.md §1.3a) === */
/* Do NOT modify without updating spec section 1.3a first. */
body {
  background: var(--bg);
  background-image:
    radial-gradient(ellipse 800px 400px at 20% 0%, rgba(232,168,124,0.06), transparent 60%),
    radial-gradient(ellipse 600px 400px at 90% 30%, rgba(124,196,164,0.05), transparent 60%);
  background-attachment: fixed;
}
.logo-mascot {
  box-shadow: 0 0 24px rgba(232,168,124,0.35), inset 0 1px 0 rgba(255,255,255,0.2);
}
.btn-primary {
  box-shadow: 0 0 20px rgba(232,168,124,0.30);
}
.marquee-track .peach { color: var(--sp-peach-200); text-shadow: 0 0 12px rgba(232,168,124,0.4); }
.marquee-track .teal  { color: var(--sp-teal-300);  text-shadow: 0 0 12px rgba(124,196,164,0.4); }
.token-card.featured, .tk-card.featured, .card.featured {
  border-color: rgba(232,168,124,0.55);
  background: radial-gradient(ellipse 300px 200px at 100% 0%, rgba(232,168,124,0.10), transparent 70%), var(--surface-1);
  box-shadow: 0 0 32px rgba(232,168,124,0.18), inset 0 1px 0 rgba(255,255,255,0.04);
}
.token-card:hover, .tk-card:hover {
  box-shadow: 0 0 24px rgba(124,196,164,0.08);
}
.token-av, .tk-av { box-shadow: 0 0 16px rgba(124,196,164,0.15); }
.bar-fill { box-shadow: 0 0 10px rgba(232,168,124,0.5); }
/* === end Mood B glow === */
"""

# ===== Sprout-specific palette additions (inject into :root if not already present) =====
SPROUT_ROOT_ADDITIONS = """
  /* Sprout Mood B additions */
  --sp-teal-glow: rgba(124, 196, 164, 0.22);
  --sp-peach-glow: rgba(232, 168, 124, 0.18);
"""


def find_root_end(content):
    """Find the position just after the first :root { … } closing brace."""
    root_start = content.find(':root')
    if root_start == -1:
        return -1
    brace_start = content.find('{', root_start)
    if brace_start == -1:
        return -1
    depth = 0
    for i, c in enumerate(content[brace_start:], brace_start):
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i + 1
    return -1


def inject_glow(content):
    """Inject Mood B glow CSS after the first :root {…} block."""
    if 'Mood B signature glow' in content:
        return content  # already injected — idempotent
    pos = find_root_end(content)
    if pos != -1:
        return content[:pos] + '\n' + GLOW_CSS + content[pos:]
    return content


def transform(html):
    # SVGs first (before any text or color changes)
    html = CAT_32_RE.sub(SPROUT_32, html)
    html = CAT_24_RE.sub(SPROUT_24, html)
    html = CAT_64_RE.sub(SPROUT_64, html)
    # CSS vars
    for old, new in CSS_RENAMES:
        html = html.replace(old, new)
    # Hex (and text palette)
    for old, new in HEX_SWAPS:
        html = html.replace(old, new)
    # CSS classes
    for old, new in CLASS_SWAPS:
        html = html.replace(old, new)
    # Text swaps
    for old, new in TEXT_SWAPS:
        html = html.replace(old, new)
    # Inject Mood B glow
    html = inject_glow(html)
    return html


def main():
    count = 0
    skipped = []
    for fname in sorted(os.listdir(SRC)):
        if not fname.endswith('.html'):
            continue
        src_path = os.path.join(SRC, fname)
        dst_path = os.path.join(DST, fname)
        with open(src_path, 'r', encoding='utf-8') as f:
            html = f.read()
        new_html = transform(html)
        with open(dst_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        count += 1
        has_glow = 'Mood B signature glow' in new_html
        has_surface = '--surface-1: #131f18' in new_html
        glow_mark = '✓ glow' if has_glow else '✗ NO GLOW'
        surf_mark = '✓ surface' if has_surface else '✗ NO SURFACE'
        print(f'  OK  {fname:<50} [{glow_mark}] [{surf_mark}]')

    print(f'\nCloned {count} file(s): mockups-bazaar/ → mockups-sprout/')
    print('\nNext steps:')
    print('  1. Open mockups-sprout/token_list_v4.html in browser to visually verify Mood B glow')
    print('  2. Run verification greps per SPROUT_MOOD_B_IMPLEMENTATION_PLAN.md §4a')
    print('  3. Confirm _mood_demos/ files are unchanged (not touched by this script)')


if __name__ == '__main__':
    main()
