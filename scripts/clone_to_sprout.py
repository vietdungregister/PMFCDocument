#!/usr/bin/env python3
"""
Clone /mockups-bazaar/ → /mockups-sprout/ with brand swap.

Bazaar → Sprout transforms:
  · Color palette: amber → peach, brown → forest green
  · Mascot SVG: cat hawker → sprout (cây con với 2 lá)
  · Brand identity: Stallspot → Sprout, "the meme bazaar" → "the meme garden"
  · Tagline: "Open a stall. Trade memes." → "Plant your seed in the memeconomy."
  · Marquee: bazaar phrases → garden phrases
  · Tier ladder: Newcomer/Regular/Local/Insider/Legend → Seed/Sprout/Sapling/Tree/Ancient Tree
  · Microcopy: "stall by" → "by", "lucky vendor draw" → "daily harvest", etc.
  · Connected wallet, sidebar structure, page architecture: UNCHANGED (3-layer principle compliant)

Run:
  cd /path/to/PMFCDocument
  python3 scripts/clone_to_sprout.py

Output: /mockups-sprout/ folder with 18 HTML files cloned + brand-swapped.
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
    ('--bz-crimson', '--sp-crimson'),
]

# ===== Hex color swaps =====
HEX_SWAPS = [
    # Surface palette: dark navy → green-tinted (matches MVP "garden under twilight")
    ('#0a0e1a', '#0a1610'),     # bg
    ('#131826', '#13201a'),     # surface-1
    ('#1a2138', '#1a2a22'),     # surface-2
    ('#232b46', '#23332b'),     # surface-3
    ('#1f2640', '#1f2a23'),     # border-1
    ('#2a3456', '#2a3a30'),     # border-2
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
    # Tagline & search
    ('Open a stall. Trade memes.', 'Plant your seed in the memeconomy.'),
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
    # Microcopy
    ('stall by ', 'by '),
    ('Stall story', 'Token story'),
    ('the lucky vendor draw', 'the daily harvest'),
    ('Bring a friend to the bazaar.', 'Plant a friend in the garden.'),
    ('Bring a friend to the bazaar', 'Plant a friend in the garden'),
    ('Hand out your stall card.', 'Share your seed packet.'),
    ('Hand out your stall card', 'Share your seed packet'),
    ('5% commission when they trade at your stall',
     '5% commission when they trade in your garden'),
    ('Showdown row', 'Garden arena'),
    ('back winners · the crowd predicts',
     'back winners · the garden predicts'),
    ('Earn points by trading, creating, and bringing the crowd. Climb the bazaar.',
     'Earn points by trading, creating, and bringing friends. Grow your garden.'),
    ('The lucky vendor draw. Spend a ticket, spin five reels, win SOL.',
     'The daily harvest. Spend a ticket, spin five reels, win SOL.'),
    ('Bring a friend to the bazaar. Earn when they trade.',
     'Plant a friend in the garden. Earn when they trade.'),
    ('No referrals yet', 'No seeds planted yet'),
    ('Share your link to start earning. The bazaar grows when you bring people in.',
     'Share your link to start earning. The garden grows when you bring people in.'),
    ('https://stallspot.app/join/@', 'https://sprout.app/join/@'),
    # CSS comments (cosmetic)
    ('Bazaar primary — amber (warm bazaar lantern)',
     'Sprout primary — peach (sunset over garden)'),
    ('Bazaar secondary — brown (counter, structural)',
     'Sprout secondary — forest green (stem, leaf)'),
    ('Teal — preserved from Sprout for SUCCESS / OK semantics',
     'Teal — leaf/bloom accents'),
]

def transform(html):
    # SVGs first (before any text or color changes)
    html = CAT_32_RE.sub(SPROUT_32, html)
    html = CAT_24_RE.sub(SPROUT_24, html)
    html = CAT_64_RE.sub(SPROUT_64, html)
    # CSS vars
    for old, new in CSS_RENAMES:
        html = html.replace(old, new)
    # Hex
    for old, new in HEX_SWAPS:
        html = html.replace(old, new)
    # CSS classes
    for old, new in CLASS_SWAPS:
        html = html.replace(old, new)
    # Text swaps
    for old, new in TEXT_SWAPS:
        html = html.replace(old, new)
    return html


def main():
    count = 0
    for fname in sorted(os.listdir(SRC)):
        if not fname.endswith('.html'):
            continue
        with open(os.path.join(SRC, fname), 'r', encoding='utf-8') as f:
            html = f.read()
        new_html = transform(html)
        with open(os.path.join(DST, fname), 'w', encoding='utf-8') as f:
            f.write(new_html)
        count += 1
        print(f'  OK  {fname}')

    print(f'\nCloned {count} file(s): mockups-bazaar/ → mockups-sprout/')
    print('\nNext steps:')
    print('  1. Open mockups-sprout/token_list_v4.html in browser to visually verify')
    print('  2. If brand swap looks correct, all 18 pages are ready')
    print('  3. If issues found, report back to AI for refinement')


if __name__ == '__main__':
    main()
