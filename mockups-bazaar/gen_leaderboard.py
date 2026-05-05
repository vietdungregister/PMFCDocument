import re

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/events.html', 'r', encoding='utf-8') as f:
    events_html = f.read()

# Extract head
head_match = re.search(r'(<head>.*?</head>)', events_html, re.DOTALL)
head_content = head_match.group(1)
head_content = head_content.replace('<title>Events — Stallspot</title>', '<title>Leaderboard — Stallspot</title>')

# Inject page CSS
page_css = """
/* ===================== LEADERBOARD PAGE CSS ===================== */

/* Top 3 grid */
.top3-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  margin-bottom: 28px;
}

/* Featured card */
.lb-card {
  background:
    radial-gradient(ellipse 120% 80% at 10% 0%, rgba(234,181,82,0.12), transparent 55%),
    radial-gradient(ellipse 80% 100% at 90% 100%, rgba(92,168,134,0.10), transparent 60%),
    var(--surface-1);
  border: 1px solid var(--border-1);
  border-radius: var(--r-lg);
  padding: 22px;
  position: relative;
  cursor: pointer;
  transition: transform 0.18s var(--ease), border-color 0.18s var(--ease);
}
.lb-card:hover {
  transform: translateY(-3px);
  border-color: var(--bz-amber-400);
}
.lb-card.rank-1 { border-color: rgba(234,181,82,0.35); }
.lb-card.rank-2 { border-color: rgba(156,216,184,0.2); }

.rank-badge {
  font-family: var(--font-mono);
  font-size: 11.5px;
  font-weight: 700;
  color: var(--text-mute);
  letter-spacing: 0.06em;
  margin-bottom: 16px;
}
.lb-card.rank-1 .rank-badge { color: var(--bz-amber-400); }
.lb-card.rank-2 .rank-badge { color: var(--bz-teal-400); }

.lb-card-head {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 14px;
}
.lb-avatar {
  width: 64px;
  height: 64px;
  border-radius: var(--r-md);
  flex-shrink: 0;
  overflow: hidden;
  display: grid;
  place-items: center;
}
.lb-token-info { flex: 1; min-width: 0; }
.lb-token-name {
  font-family: var(--font-display);
  font-size: 19px;
  font-weight: 800;
  color: var(--bz-amber-400);
  margin-bottom: 2px;
  letter-spacing: -0.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.lb-tagline {
  font-size: 11.5px;
  color: var(--text-3);
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.lb-buy {
  height: 32px;
  padding: 0 16px;
  background: var(--bz-teal-500);
  border: none;
  border-radius: var(--r-md);
  color: #ecfeff;
  font-family: var(--font-display);
  font-size: 12.5px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s;
  flex-shrink: 0;
  align-self: flex-start;
}
.lb-buy:hover { background: var(--bz-teal-400); }

.lb-metrics {
  display: flex;
  flex-direction: column;
  gap: 5px;
  margin-bottom: 14px;
  font-size: 13px;
}
.lb-metric-row {
  display: flex;
  align-items: baseline;
  gap: 6px;
  color: var(--text-3);
}
.lb-metric-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.04em; }
.lb-metric-val {
  font-family: var(--font-mono);
  font-weight: 600;
  color: var(--text-1);
  font-size: 13px;
}
.lb-metric-change {
  font-family: var(--font-mono);
  font-size: 11.5px;
  font-weight: 600;
}

.lb-creator {
  display: flex;
  align-items: center;
  gap: 8px;
  padding-top: 12px;
  border-top: 1px solid var(--border-1);
  font-size: 11.5px;
  color: var(--text-3);
}
.lb-creator-avatar {
  width: 22px;
  height: 22px;
  border-radius: var(--r-pill);
  flex-shrink: 0;
  border: 1px solid var(--border-2);
}
.lb-creator-name { color: var(--text-2); font-weight: 500; }
.lb-creator-age { margin-left: auto; color: var(--text-mute); }

/* Table */
.lb-table {
  background: var(--surface-1);
  border: 1px solid var(--border-1);
  border-radius: var(--r-lg);
  overflow: hidden;
}
.lb-table-header {
  display: grid;
  grid-template-columns: 2.2fr 1.4fr 0.8fr 1.1fr 0.5fr;
  padding: 12px 20px;
  font-size: 10.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-3);
  border-bottom: 1px solid var(--border-1);
}
.lb-row {
  display: grid;
  grid-template-columns: 2.2fr 1.4fr 0.8fr 1.1fr 0.5fr;
  align-items: center;
  padding: 13px 20px;
  border-top: 1px solid var(--border-1);
  cursor: pointer;
  transition: background 0.12s var(--ease);
}
.lb-row:first-child { border-top: none; }
.lb-row:hover { background: var(--surface-2); }

.lb-row-token {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 0;
}
.lb-row-avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--r-sm);
  flex-shrink: 0;
  overflow: hidden;
  display: grid;
  place-items: center;
}
.lb-row-name {
  font-family: var(--font-display);
  font-size: 14px;
  font-weight: 700;
  color: var(--bz-amber-400);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.lb-row-rank {
  font-family: var(--font-mono);
  font-size: 10.5px;
  color: var(--text-mute);
  margin-top: 1px;
}

.lb-row-creator {
  display: flex;
  align-items: center;
  gap: 7px;
  min-width: 0;
  font-size: 12.5px;
  color: var(--text-2);
}
.lb-row-creator-av {
  width: 20px;
  height: 20px;
  border-radius: var(--r-pill);
  flex-shrink: 0;
  border: 1px solid var(--border-2);
}
.lb-row-holders {
  font-family: var(--font-mono);
  font-size: 13px;
  color: var(--text-2);
}
.lb-row-mc {
  display: flex;
  flex-direction: column;
  gap: 1px;
}
.lb-row-mc-val {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  color: var(--text-1);
}
.lb-row-mc-change {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 600;
}
.lb-row-buy {
  height: 30px;
  padding: 0 14px;
  background: transparent;
  border: 1px solid var(--border-2);
  border-radius: var(--r-md);
  color: var(--text-2);
  font-family: var(--font-display);
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.12s;
}
.lb-row-buy:hover {
  border-color: var(--bz-teal-400);
  color: var(--bz-teal-400);
}

/* Color helpers */
.c-up { color: var(--bz-teal-400); }
.c-down { color: var(--bz-crimson); }
.c-flat { color: var(--text-3); }
"""
head_content = head_content.replace('</style>', page_css + '\n</style>')

# Extract header
header_match = re.search(r'(<header class="header">.*?</header>)', events_html, re.DOTALL)
header_content = header_match.group(1)

# Extract marquee
marquee_match = re.search(r'(<div class="marquee">.*?</div>)', events_html, re.DOTALL)
marquee_content = marquee_match.group(1)

# Extract sidebar, set Leader Board active
sidebar_match = re.search(r'(<aside class="sidebar">.*?</aside>)', events_html, re.DOTALL)
sidebar_content = sidebar_match.group(1)
# Remove any existing active from events
sidebar_content = sidebar_content.replace('<a class="nav-item active" href="events.html">', '<a class="nav-item" href="events.html">')
# Set leaderboard active
sidebar_content = sidebar_content.replace('<a class="nav-item" href="leaderboard.html">', '<a class="nav-item active" href="leaderboard.html">')

def svg_token(bg1, bg2, letter='', icon_type=0):
    icons = [
        # moon
        '<circle cx="30" cy="30" r="22" fill="rgba(0,0,0,0.3)"/><circle cx="22" cy="22" rx="14" fill="{c2}"/><circle cx="20" cy="20" r="8" fill="{c1}" opacity="0.8"/>',
        # star
        '<polygon points="30,8 35,22 50,22 38,30 42,45 30,36 18,45 22,30 10,22 25,22" fill="{c2}" opacity="0.9"/>',
        # flame
        '<path d="M30 52 C15 45 10 35 18 25 C20 35 26 38 28 30 C32 38 40 42 30 52Z" fill="{c2}"/><path d="M30 46 C22 42 20 36 25 30 C26 36 30 38 30 46Z" fill="{c1}" opacity="0.7"/>',
        # diamond
        '<polygon points="30,10 48,28 30,52 12,28" fill="{c2}" opacity="0.9"/><polygon points="30,10 48,28 30,34" fill="{c1}" opacity="0.5"/>',
        # rocket
        '<path d="M30 8 C30 8 20 25 20 38 L30 44 L40 38 C40 25 30 8 30 8Z" fill="{c2}"/><circle cx="30" cy="32" r="5" fill="{c1}" opacity="0.8"/>',
    ]
    icon = icons[icon_type % len(icons)].replace('{c1}', bg1).replace('{c2}', bg2)
    return f'<svg viewBox="0 0 60 60" style="width:100%;height:100%"><rect width="60" height="60" fill="transparent"/>{icon}</svg>'

# Avatar gradients for variety
card_avs = [
    ('#1a3a4a', '#2a9d8f', 0),  # teal moon
    ('#1e3a5f', '#4a90d9', 3),  # blue diamond
    ('#5a2a10', '#d45a20', 2),  # orange flame
]
row_avs = [
    ('#1a3a4a', '#2a9d8f'), ('#1e3a5f', '#4a90d9'), ('#5a2a10', '#d45a20'),
    ('#2a1a4a', '#7c4a9d'), ('#1a3a2a', '#2a9d5a'), ('#3a2a10', '#9d7a2a'),
    ('#3a1a2a', '#9d4a6a'), ('#1a2a4a', '#2a5a9d'),
]

tokens = [
    # (name, tagline, mc, mc_pct, vol, vol_pct, creator, age, up/down/flat)
    ('STAR003', 'Stellar meme coin 🌟', '$3.57M', '+1.01%', '$10.2K', '+48.45%', 'kxce...vnWy', '2mos 23d', 'up', 12450),
    ('DIAMOND098', 'Diamond hands only 💎', '$3.21M', '+1.01%', '$0.00', '0.00%', 'eLK3...mHAt', '2mos 19d', 'flat', 0),
    ('FIRE094', 'Hot token of the week 🔥', '$3.21M', '+1.01%', '$4.34', '+100.00%', 'Ychp...enMU', '2mos 18d', 'up', 3911),
]
table_tokens = [
    ('STAR003', '#001', 'kxce...vnWy', '12,450', '$3.57M', '+1.01%', 'up'),
    ('DIAMOND098', '#002', 'eLK3...mHAt', 'n/a', '$3.21M', '+1.01%', 'up'),
    ('FIRE094', '#003', 'Ychp...enMU', '3,911', '$3.21M', '+1.01%', 'up'),
    ('MOON030', '#004', 'pvEM...V1pp', '8,234', '$3.17M', '+1.01%', 'up'),
    ('SILVER037', '#005', '24AF...cyEq', '5,123', '$3.04M', '+1.01%', 'up'),
    ('PEPE', '#006', '2Kx9...Qw3L', '3,456', '$450K', '+12.5%', 'up'),
    ('DOGE KILLER', '#007', '9Bn4...rT7m', '2,891', '$320K', '-5.2%', 'down'),
    ('ROCKET SHIP', '#008', '3Wx8...Km5N', '1,567', '$150K', '+15.3%', 'up'),
]

def color_class(direction):
    return {'up': 'c-up', 'down': 'c-down', 'flat': 'c-flat'}.get(direction, 'c-flat')

# Build Top 3 cards
cards_html = '<div class="top3-grid">\n'
rank_class = ['rank-1', 'rank-2', '']
for i, (name, tagline, mc, mc_pct, vol, vol_pct, creator, age, direction, holders) in enumerate(tokens):
    bg1, bg2, icon_i = card_avs[i]
    svg = svg_token(bg1, bg2, icon_type=icon_i)
    cclass = color_class(direction)
    cards_html += f'''  <div class="lb-card {rank_class[i]}" onclick="location.href='token_detail.html'">
    <div class="rank-badge">#{str(i+1).zfill(3)}</div>
    <div class="lb-card-head">
      <div class="lb-avatar" style="background:linear-gradient(135deg,{bg1},{bg2})">{svg}</div>
      <div class="lb-token-info">
        <div class="lb-token-name">{name}</div>
        <div class="lb-tagline">{tagline}</div>
      </div>
      <button class="lb-buy" onclick="event.stopPropagation()">buy</button>
    </div>
    <div class="lb-metrics">
      <div class="lb-metric-row">
        <span class="lb-metric-label">mc</span>
        <span class="lb-metric-val {cclass}">{mc_pct}</span>
        <span class="lb-metric-val">{mc}</span>
      </div>
      <div class="lb-metric-row">
        <span class="lb-metric-label">24h vol</span>
        <span class="lb-metric-val {color_class('up' if vol_pct.startswith('+') else 'flat' if vol_pct == '0.00%' else 'down')}">{vol_pct}</span>
        <span class="lb-metric-val">{vol}</span>
      </div>
    </div>
    <div class="lb-creator">
      <div class="lb-creator-avatar" style="background:linear-gradient(135deg,{bg2},{bg1})"></div>
      <span>stall by</span>
      <span class="lb-creator-name">{creator}</span>
      <span class="lb-creator-age">• {age} ago</span>
    </div>
  </div>
'''
cards_html += '</div>\n'

# Build table
table_html = '''<div class="lb-table">
  <div class="lb-table-header">
    <div>Token</div>
    <div>Creator</div>
    <div>Holders</div>
    <div>Market Cap</div>
    <div></div>
  </div>
'''
for i, (name, rank, creator, holders, mc, mc_pct, direction) in enumerate(table_tokens):
    bg1, bg2 = row_avs[i]
    icon_i = i % 5
    svg = svg_token(bg1, bg2, icon_type=icon_i)
    cclass = color_class(direction)
    table_html += f'''  <div class="lb-row" onclick="location.href='token_detail.html'">
    <div class="lb-row-token">
      <div class="lb-row-avatar" style="background:linear-gradient(135deg,{bg1},{bg2})">{svg}</div>
      <div>
        <div class="lb-row-name">{name}</div>
        <div class="lb-row-rank">{rank}</div>
      </div>
    </div>
    <div class="lb-row-creator">
      <div class="lb-row-creator-av" style="background:linear-gradient(135deg,{bg2},{bg1})"></div>
      {creator}
    </div>
    <div class="lb-row-holders">{holders}</div>
    <div class="lb-row-mc">
      <div class="lb-row-mc-val">{mc}</div>
      <div class="lb-row-mc-change {cclass}">{mc_pct}</div>
    </div>
    <button class="lb-row-buy" onclick="event.stopPropagation()">buy</button>
  </div>
'''
table_html += '</div>\n'

main_content = f"""
<main class="main">
  <div style="margin-bottom:24px">
    <h1 style="font-family:var(--font-display);font-size:28px;font-weight:800;color:var(--text-1);letter-spacing:-0.02em;margin-bottom:4px">Leaderboard</h1>
    <p style="font-size:13px;color:var(--text-3)">Top tokens ranked by market cap · Updated live</p>
  </div>

  {cards_html}
  {table_html}
</main>
"""

final_html = f"<!DOCTYPE html>\n<html lang=\"vi\">\n{head_content}\n<body>\n{header_content}\n{marquee_content}\n</div>\n{sidebar_content}\n{main_content}\n</body>\n</html>"

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/leaderboard.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Done! leaderboard.html generated.")
