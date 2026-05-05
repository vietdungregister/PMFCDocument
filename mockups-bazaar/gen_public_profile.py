#!/usr/bin/env python3
"""Generate public_profile.html — Bazaar themed with app shell from points.html"""

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/points.html', 'r', encoding='utf-8') as f:
    pts = f.read()

import re
style_match = re.search(r'(<style>.*?</style>)', pts, re.DOTALL)
style_block = style_match.group(1)
shell_match = re.search(r'(<header class="header">.*?</aside>)', pts, re.DOTALL)
shell_html = shell_match.group(1)
# Set My Profile active (viewing another user's profile)
shell_html = shell_html.replace('class="nav-item active" href="points.html"', 'class="nav-item" href="points.html"')

page_css = """
/* ===== PUBLIC PROFILE ===== */
.profile-hero { background: var(--surface-1); border: 1px solid var(--border-1); border-radius: var(--r-lg); padding: 28px; display: flex; align-items: flex-start; gap: 20px; margin-bottom: 24px; position: relative; }
.profile-avatar { width: 80px; height: 80px; border-radius: var(--r-pill); background: linear-gradient(135deg, var(--bz-teal-400), var(--bz-amber-400)); display: grid; place-items: center; font-family: var(--font-display); font-size: 32px; font-weight: 800; color: #2a1505; flex-shrink: 0; border: 3px solid var(--bz-teal-400); }
.profile-name { font-family: var(--font-display); font-size: 22px; font-weight: 800; color: var(--text-1); margin-bottom: 2px; }
.profile-badges { display: flex; gap: 6px; margin-bottom: 6px; }
.p-badge { padding: 3px 9px; border-radius: var(--r-pill); font-size: 10.5px; font-weight: 700; }
.p-badge.creator { background: rgba(234,181,82,0.12); color: var(--bz-amber-400); }
.p-badge.whale { background: rgba(124,196,164,0.12); color: var(--bz-teal-400); }
.profile-wallet { display: flex; align-items: center; gap: 8px; font-family: var(--font-mono); font-size: 12.5px; color: var(--text-3); margin-bottom: 8px; }
.copy-btn { padding: 3px 8px; background: var(--surface-2); border: 1px solid var(--border-2); border-radius: var(--r-sm); color: var(--text-2); font-size: 11px; cursor: pointer; font-family: inherit; }
.copy-btn:hover { border-color: var(--bz-amber-400); color: var(--bz-amber-400); }
.profile-bio { font-size: 13px; color: var(--text-2); max-width: 480px; }
.profile-tier { font-size: 12px; color: var(--bz-amber-400); font-weight: 600; margin-bottom: 6px; }

.stat-cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 28px; }
.stat-card { background: var(--surface-1); border: 1px solid var(--border-1); border-radius: var(--r-lg); padding: 18px 20px; }
.stat-card-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--text-3); font-weight: 600; margin-bottom: 6px; }
.stat-card-value { font-family: var(--font-display); font-size: 22px; font-weight: 800; color: var(--bz-amber-400); }

.prof-tabs-wrap { border-bottom: 1px solid var(--border-1); margin-bottom: 24px; display: flex; }
.prof-tabs { display: flex; gap: 2px; }
.prof-tab { padding: 10px 18px; background: transparent; border: none; border-bottom: 2px solid transparent; color: var(--text-2); font-family: inherit; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.15s; margin-bottom: -1px; display: inline-flex; align-items: center; gap: 6px; }
.prof-tab:hover { color: var(--text-1); }
.prof-tab.active { color: var(--bz-amber-400); border-bottom-color: var(--bz-amber-400); }
.tab-panel { display: none; }
.tab-panel.active { display: block; }
.section-card { background: var(--surface-1); border: 1px solid var(--border-1); border-radius: var(--r-lg); padding: 22px 24px; margin-bottom: 16px; }
.section-title { font-family: var(--font-display); font-size: 14px; font-weight: 700; color: var(--bz-amber-400); margin-bottom: 18px; text-transform: uppercase; letter-spacing: 0.05em; }
.field-row { margin-bottom: 16px; }
.field-label { font-size: 12px; color: var(--text-3); font-weight: 600; margin-bottom: 6px; }
.field-value { font-size: 14px; color: var(--text-1); }
.social-link-row { display: flex; align-items: center; gap: 10px; padding: 10px 14px; background: var(--surface-2); border: 1px solid var(--border-1); border-radius: var(--r-md); margin-bottom: 8px; }
.social-icon { width: 20px; height: 20px; color: var(--text-3); flex-shrink: 0; }
.social-value { font-size: 13px; color: var(--bz-teal-400); flex: 1; }
.social-value a { color: var(--bz-teal-400); text-decoration: none; }
.social-value a:hover { text-decoration: underline; }
.token-item { display: flex; align-items: center; gap: 14px; padding: 14px 0; border-bottom: 1px solid var(--border-1); }
.token-item:last-child { border-bottom: none; }
.token-av { width: 44px; height: 44px; border-radius: var(--r-md); flex-shrink: 0; }
.token-meta { flex: 1; min-width: 0; }
.token-n { font-family: var(--font-display); font-size: 14px; font-weight: 700; color: var(--text-1); }
.token-sym { font-size: 12px; color: var(--text-3); margin-top: 2px; }
.token-right { text-align: right; }
.token-mc { font-family: var(--font-mono); font-size: 14px; font-weight: 600; color: var(--text-1); }
.token-holders { font-size: 11.5px; color: var(--text-3); margin-top: 2px; }
.tx-item { display: flex; align-items: center; gap: 12px; padding: 14px 0; border-bottom: 1px solid var(--border-1); }
.tx-item:last-child { border-bottom: none; }
.tx-type { padding: 3px 10px; border-radius: var(--r-sm); font-size: 11px; font-weight: 700; flex-shrink: 0; text-transform: uppercase; }
.tx-type.buy { background: rgba(124,196,164,0.12); color: var(--bz-teal-400); }
.tx-type.sell { background: rgba(214,90,84,0.12); color: var(--bz-crimson); }
"""

main_html = """
<main class="main">
  <div class="profile-hero">
    <div class="profile-avatar">A</div>
    <div style="flex:1;min-width:0">
      <div class="profile-name">alice_trader</div>
      <div class="profile-badges">
        <span class="p-badge creator">👑 Creator</span>
        <span class="p-badge whale">🐋 Whale</span>
      </div>
      <div class="profile-tier">Local tier · joined Mar 2026</div>
      <div class="profile-wallet">
        <span>7xK9...mP3q</span>
        <button class="copy-btn" onclick="navigator.clipboard.writeText('7xK9mP3q')">Copy</button>
      </div>
      <div class="profile-bio">Passionate about discovering the next 100x meme token. Early supporter of DOGE and SHIB.</div>
    </div>
  </div>

  <div class="stat-cards">
    <div class="stat-card">
      <div class="stat-card-label">Portfolio Value</div>
      <div class="stat-card-value">$45,280</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Tokens Created</div>
      <div class="stat-card-value">3</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Total Trades</div>
      <div class="stat-card-value">127</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Member Since</div>
      <div class="stat-card-value">Mar 2026</div>
    </div>
  </div>

  <div class="prof-tabs-wrap">
    <div class="prof-tabs">
      <button class="prof-tab active" onclick="showTab('pub-info',this)">Profile Info</button>
      <button class="prof-tab" onclick="showTab('pub-holding',this)">Holding Tokens</button>
      <button class="prof-tab" onclick="showTab('pub-created',this)">Created Tokens</button>
      <button class="prof-tab" onclick="showTab('pub-tx',this)">Transaction History</button>
    </div>
  </div>

  <div class="tab-panel active" id="pub-info">
    <div class="section-card">
      <div class="section-title">Basic Information</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
        <div class="field-row"><div class="field-label">Username</div><div class="field-value">alice_trader</div></div>
        <div class="field-row"><div class="field-label">Display Name</div><div class="field-value">Alice - Meme Token Expert</div></div>
        <div class="field-row"><div class="field-label">Bio</div><div class="field-value">Passionate about discovering the next 100x meme token.</div></div>
        <div class="field-row"><div class="field-label">Member Since</div><div class="field-value">March 2026</div></div>
      </div>
    </div>
    <div class="section-card">
      <div class="section-title">Social Links</div>
      <div class="social-link-row">
        <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.008 3.827H5.053z"/></svg>
        <div class="social-value"><a href="#">@alice_crypto</a></div>
      </div>
      <div class="social-link-row">
        <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor"><path d="m20.665 3.717-17.73 6.837c-1.21.486-1.203 1.161-.222 1.462l4.552 1.42 10.532-6.645c.498-.303.953-.14.579.192l-8.533 7.701h-.002l.002.001-.314 4.692c.46 0 .663-.211.921-.46l2.211-2.15 4.599 3.397c.848.467 1.457.227 1.668-.785l3.019-14.228c.309-1.239-.473-1.8-1.282-1.434z"/></svg>
        <div class="social-value"><a href="#">@alicetrader</a></div>
      </div>
    </div>
  </div>

  <div class="tab-panel" id="pub-holding">
    <div class="section-card">
      <div class="token-item">
        <div class="token-av" style="background:linear-gradient(135deg,#f093fb,#f5576c)"></div>
        <div class="token-meta"><div class="token-n">Pepe Seed</div><div class="token-sym">PSEED · 50,000 tokens</div></div>
        <div class="token-right"><div class="token-mc">50,000</div><div class="token-holders">@$0.00123</div></div>
      </div>
      <div class="token-item">
        <div class="token-av" style="background:linear-gradient(135deg,#4facfe,#00f2fe)"></div>
        <div class="token-meta"><div class="token-n">Doge Killer</div><div class="token-sym">DOGEK · 125,000 tokens</div></div>
        <div class="token-right"><div class="token-mc">125,000</div><div class="token-holders">@$0.00035</div></div>
      </div>
      <div class="token-item">
        <div class="token-av" style="background:linear-gradient(135deg,#fa709a,#fee140)"></div>
        <div class="token-meta"><div class="token-n">Moon Token</div><div class="token-sym">MOON · 10,000 tokens</div></div>
        <div class="token-right"><div class="token-mc">10,000</div><div class="token-holders">@$0.0289</div></div>
      </div>
    </div>
  </div>

  <div class="tab-panel" id="pub-created">
    <div class="section-card">
      <div class="token-item">
        <div class="token-av" style="background:linear-gradient(135deg,#a8edea,#fed6e3)"></div>
        <div class="token-meta"><div class="token-n">Alice Token</div><div class="token-sym">ALICE · Created 1 week ago · <span style="color:var(--bz-amber-400)">Graduated</span></div></div>
        <div class="token-right"><div class="token-mc">MC: $125.5K</div><div class="token-holders">845 holders</div></div>
      </div>
      <div class="token-item">
        <div class="token-av" style="background:linear-gradient(135deg,#ffecd2,#fcb69f)"></div>
        <div class="token-meta"><div class="token-n">Crypto Queen</div><div class="token-sym">CQUEEN · Created 2 weeks ago · <span style="color:var(--bz-teal-400)">Active</span></div></div>
        <div class="token-right"><div class="token-mc">MC: $67.2K</div><div class="token-holders">512 holders</div></div>
      </div>
      <div class="token-item">
        <div class="token-av" style="background:linear-gradient(135deg,#ff9a9e,#fecfef)"></div>
        <div class="token-meta"><div class="token-n">Rocket Ship</div><div class="token-sym">ROCKET · Created 1 month ago · <span style="color:var(--bz-teal-400)">Active</span></div></div>
        <div class="token-right"><div class="token-mc">MC: $28.9K</div><div class="token-holders">234 holders</div></div>
      </div>
    </div>
  </div>

  <div class="tab-panel" id="pub-tx">
    <div class="section-card">
      <div class="tx-item">
        <span class="tx-type buy">BUY</span>
        <div class="token-av" style="width:36px;height:36px;background:linear-gradient(135deg,#f093fb,#f5576c)"></div>
        <div class="token-meta"><div class="token-n">Pepe Seed</div><div class="token-sym">2 hours ago</div></div>
        <div class="token-right"><div class="token-mc">+10,000 PSEED</div><div class="token-holders">0.5 SOL</div></div>
      </div>
      <div class="tx-item">
        <span class="tx-type sell">SELL</span>
        <div class="token-av" style="width:36px;height:36px;background:linear-gradient(135deg,#4facfe,#00f2fe)"></div>
        <div class="token-meta"><div class="token-n">Doge Killer</div><div class="token-sym">5 hours ago</div></div>
        <div class="token-right"><div class="token-mc" style="color:var(--bz-crimson)">-25,000 DOGEK</div><div class="token-holders">0.875 SOL</div></div>
      </div>
      <div class="tx-item">
        <span class="tx-type buy">BUY</span>
        <div class="token-av" style="width:36px;height:36px;background:linear-gradient(135deg,#fa709a,#fee140)"></div>
        <div class="token-meta"><div class="token-n">Moon Token</div><div class="token-sym">1 day ago</div></div>
        <div class="token-right"><div class="token-mc">+5,000 MOON</div><div class="token-holders">0.145 SOL</div></div>
      </div>
    </div>
  </div>
</main>
"""

js = """
<script>
function showTab(id, btn) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.prof-tab').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
"""

style_mod = style_block.replace('</style>', page_css + '\n</style>')
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>alice_trader — Stallspot</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
{style_mod}
</head>
<body>
{shell_html}
{main_html}
{js}
</body>
</html>"""

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/public_profile.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ public_profile.html generated")
