import re

# 1. Read the base events.html to extract the shared layout
with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/events.html', 'r', encoding='utf-8') as f:
    events_html = f.read()

# 2. Extract components
head_match = re.search(r'(<head>.*?</head>)', events_html, re.DOTALL)
head_content = head_match.group(1) if head_match else ''

# Replace title
head_content = head_content.replace('<title>Events — Stallspot</title>', '<title>My Profile — Stallspot</title>')

# Inject profile specific CSS
profile_css = """
/* Profile specific CSS */
.profile-hero { background: var(--surface-1); border: 1px solid var(--border-1); border-radius: var(--r-lg); padding: 28px; display: flex; align-items: flex-start; gap: 20px; margin-bottom: 24px; position: relative; }
.profile-avatar { width: 80px; height: 80px; border-radius: var(--r-pill); background: linear-gradient(135deg, var(--bz-amber-400), var(--bz-teal-500)); display: grid; place-items: center; font-family: var(--font-display); font-size: 32px; font-weight: 800; color: #2a1505; flex-shrink: 0; border: 3px solid var(--bz-amber-400); }
.profile-name { font-family: var(--font-display); font-size: 22px; font-weight: 800; color: var(--text-1); margin-bottom: 4px; }
.profile-wallet { display: flex; align-items: center; gap: 8px; font-family: var(--font-mono); font-size: 12.5px; color: var(--text-3); margin-bottom: 8px; }
.copy-btn { padding: 3px 8px; background: var(--surface-2); border: 1px solid var(--border-2); border-radius: var(--r-sm); color: var(--text-2); font-size: 11px; cursor: pointer; font-family: inherit; }
.copy-btn:hover { border-color: var(--bz-amber-400); color: var(--bz-amber-400); }
.profile-bio { font-size: 13px; color: var(--text-2); max-width: 480px; }
.edit-profile-btn { position: absolute; top: 20px; right: 20px; padding: 7px 14px; background: var(--surface-2); border: 1px solid var(--border-2); border-radius: var(--r-md); color: var(--text-2); font-size: 13px; font-weight: 600; cursor: pointer; font-family: inherit; }
.edit-profile-btn:hover { border-color: var(--bz-amber-400); color: var(--bz-amber-400); }

/* Stat cards */
.stat-cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-bottom: 28px; }
.stat-card { background: var(--surface-1); border: 1px solid var(--border-1); border-radius: var(--r-lg); padding: 18px 20px; }
.stat-card-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--text-3); font-weight: 600; margin-bottom: 6px; }
.stat-card-value { font-family: var(--font-display); font-size: 22px; font-weight: 800; color: var(--bz-amber-400); }
.stat-card-sub { font-size: 11.5px; color: var(--text-3); margin-top: 2px; }

/* Tabs */
.prof-tabs-wrap { border-bottom: 1px solid var(--border-1); margin-bottom: 24px; display: flex; }
.prof-tabs { display: flex; gap: 2px; }
.prof-tab { padding: 10px 18px; background: transparent; border: none; border-bottom: 2px solid transparent; color: var(--text-2); font-family: inherit; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.15s; margin-bottom: -1px; display: inline-flex; align-items: center; gap: 6px; }
.prof-tab:hover { color: var(--text-1); }
.prof-tab.active { color: var(--bz-amber-400); border-bottom-color: var(--bz-amber-400); }
.tab-badge { background: var(--bz-crimson); color: white; font-size: 10px; font-weight: 700; padding: 1px 6px; border-radius: var(--r-pill); }

/* Tab content */
.tab-panel { display: none; }
.tab-panel.active { display: block; }

/* Section cards */
.section-card { background: var(--surface-1); border: 1px solid var(--border-1); border-radius: var(--r-lg); padding: 22px 24px; margin-bottom: 16px; }
.section-title { font-family: var(--font-display); font-size: 14px; font-weight: 700; color: var(--bz-amber-400); margin-bottom: 18px; text-transform: uppercase; letter-spacing: 0.05em; }

/* Forms */
.field-row { margin-bottom: 16px; }
.field-label { font-size: 12px; color: var(--text-3); font-weight: 600; margin-bottom: 6px; }
.field-value { font-size: 14px; color: var(--text-1); }
.field-input { width: 100%; padding: 9px 12px; background: var(--surface-2); border: 1px solid var(--border-1); border-radius: var(--r-md); color: var(--text-1); font-family: inherit; font-size: 13.5px; }
.field-input:focus { outline: none; border-color: var(--bz-amber-400); }

/* Social Links */
.social-link-row { display: flex; align-items: center; gap: 10px; padding: 10px 14px; background: var(--surface-2); border: 1px solid var(--border-1); border-radius: var(--r-md); margin-bottom: 8px; }
.social-icon { width: 20px; height: 20px; color: var(--text-3); flex-shrink: 0; }
.social-value { font-size: 13px; color: var(--text-3); flex: 1; font-style: italic; }
.social-link-btn { font-size: 11px; color: var(--bz-amber-400); background: none; border: none; cursor: pointer; font-family: inherit; font-weight: 600; }

/* Privacy toggle */
.toggle-row { display: flex; justify-content: space-between; align-items: center; padding: 14px 0; border-top: 1px solid var(--border-1); }
.toggle-label-text { font-size: 14px; color: var(--text-1); font-weight: 500; }
.toggle-sub { font-size: 12px; color: var(--text-3); margin-top: 2px; }
.toggle-switch { position:relative; width:44px; height:24px; display:inline-block; }
.toggle-switch input { opacity:0; width:0; height:0; }
.toggle-slider { position:absolute; cursor:pointer; top:0; left:0; right:0; bottom:0; background:#374151; border-radius:12px; transition:0.2s; }
.toggle-slider:before { position:absolute; content:""; height:18px; width:18px; left:3px; bottom:3px; background:white; border-radius:50%; transition:0.2s; }
.toggle-switch input:checked + .toggle-slider { background: var(--bz-teal-500); }
.toggle-switch input:checked + .toggle-slider:before { transform:translateX(20px); }

/* Empty state */
.empty-state { text-align: center; padding: 60px 20px; color: var(--text-3); }
.empty-icon { font-size: 48px; margin-bottom: 12px; }
.empty-title { font-family: var(--font-display); font-size: 16px; font-weight: 700; color: var(--text-2); margin-bottom: 6px; }
.empty-sub { font-size: 13px; color: var(--text-3); }

/* Holding Stats */
.holding-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 20px; }
.holding-stat { background: var(--surface-1); border: 1px solid var(--border-1); border-radius: var(--r-md); padding: 14px 16px; }
.holding-stat-label { font-size: 11px; color: var(--text-3); font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 4px; }
.holding-stat-val { font-family: var(--font-mono); font-size: 16px; font-weight: 600; color: var(--text-1); }
.text-teal { color: var(--bz-teal-400); }

/* Notifications */
.notif-item { display: flex; align-items: flex-start; gap: 12px; padding: 14px 0; border-bottom: 1px solid var(--border-1); }
.notif-item:last-child { border-bottom: none; }
.notif-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--bz-amber-400); flex-shrink: 0; margin-top: 5px; }
.notif-dot.read { background: transparent; border: 1.5px solid var(--border-2); }
.notif-text { font-size: 13px; color: var(--text-2); flex: 1; }
.notif-text strong { color: var(--text-1); }
.notif-time { font-size: 11.5px; color: var(--text-mute); flex-shrink: 0; }
"""
head_content = head_content.replace('</style>', profile_css + '\n</style>')

# Extract header & marquee
header_match = re.search(r'(<header class="header">.*?</header>)', events_html, re.DOTALL)
header_content = header_match.group(1) if header_match else ''

marquee_match = re.search(r'(<div class="marquee">.*?</div>)', events_html, re.DOTALL)
marquee_content = marquee_match.group(1) if marquee_match else ''

# Extract sidebar and modify active state
sidebar_match = re.search(r'(<aside class="sidebar">.*?</aside>)', events_html, re.DOTALL)
sidebar_content = sidebar_match.group(1) if sidebar_match else ''

sidebar_content = sidebar_content.replace('href="events.html"\n      class="nav-item active"', 'href="events.html"\n      class="nav-item"')
sidebar_content = sidebar_content.replace('href="events.html"\n      class="nav-item"\n      >Events</a>', 'href="events.html"\n      class="nav-item active"\n      >Events</a>')
sidebar_content = sidebar_content.replace('<a class="nav-item active" href="events.html">', '<a class="nav-item" href="events.html">')
sidebar_content = sidebar_content.replace('<a class="nav-item" href="my_profile.html">', '<a class="nav-item active" href="my_profile.html">')


# Main Content
main_content = """
<main class="main">
  <!-- Profile Hero -->
  <div class="profile-hero">
    <div class="profile-avatar">N</div>
    <div style="flex:1;min-width:0">
      <div class="profile-name">NobleFlame</div>
      <div class="profile-wallet">
        <span>H3XQ...hX</span>
        <button class="copy-btn" onclick="navigator.clipboard.writeText('H3XQhX')">Copy</button>
      </div>
      <div class="profile-bio">Meme trader at the bazaar. Regular at the stall since Mar 2026.</div>
    </div>
    <button class="edit-profile-btn">Edit Profile</button>
  </div>

  <!-- Stats -->
  <div class="stat-cards">
    <div class="stat-card">
      <div class="stat-card-label">Portfolio Value</div>
      <div class="stat-card-value">$12,458</div>
      <div class="stat-card-sub" style="color:var(--bz-teal-400)">↑ 2.82% today</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Tokens Created</div>
      <div class="stat-card-value">2</div>
      <div class="stat-card-sub">stalls opened</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Total Trades</div>
      <div class="stat-card-value">47</div>
      <div class="stat-card-sub">buys & sells</div>
    </div>
    <div class="stat-card">
      <div class="stat-card-label">Member Since</div>
      <div class="stat-card-value">Mar 2026</div>
      <div class="stat-card-sub">Regular · 642 pts</div>
    </div>
  </div>

  <!-- Tabs -->
  <div class="prof-tabs-wrap">
    <div class="prof-tabs" id="prof-tabs">
      <button class="prof-tab active" onclick="showTab('profile-info',this)">Profile Info</button>
      <button class="prof-tab" onclick="showTab('holding',this)">Holding Tokens</button>
      <button class="prof-tab" onclick="showTab('created',this)">Created Tokens</button>
      <button class="prof-tab" onclick="showTab('tx',this)">Transaction History</button>
      <button class="prof-tab" onclick="showTab('arena-hist',this)">Arena History</button>
      <button class="prof-tab" onclick="showTab('notifs',this)">
        Notifications <span class="tab-badge">3</span>
      </button>
    </div>
  </div>

  <!-- Tab Panels -->

  <!-- Profile Info -->
  <div class="tab-panel active" id="profile-info">
    <div class="section-card">
      <div class="section-title">Basic Information</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
        <div class="field-row">
          <div class="field-label">Username</div>
          <div class="field-value">NobleFlame</div>
        </div>
        <div class="field-row">
          <div class="field-label">Member Since</div>
          <div class="field-value">March 2026</div>
        </div>
        <div class="field-row">
          <div class="field-label">Tier</div>
          <div class="field-value">Regular (642 pts)</div>
        </div>
        <div class="field-row">
          <div class="field-label">Email (Optional)</div>
          <div class="field-value" style="color:var(--text-3);font-style:italic">Not set</div>
        </div>
      </div>
    </div>

    <div class="section-card">
      <div class="section-title">Social Links</div>
      <div class="social-link-row">
        <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.008 3.827H5.053z"/></svg>
        <div class="social-value">Not set</div>
        <button class="social-link-btn">Add</button>
      </div>
      <div class="social-link-row">
        <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor"><path d="m20.665 3.717-17.73 6.837c-1.21.486-1.203 1.161-.222 1.462l4.552 1.42 10.532-6.645c.498-.303.953-.14.579.192l-8.533 7.701h-.002l.002.001-.314 4.692c.46 0 .663-.211.921-.46l2.211-2.15 4.599 3.397c.848.467 1.457.227 1.668-.785l3.019-14.228c.309-1.239-.473-1.8-1.282-1.434z"/></svg>
        <div class="social-value">Not set</div>
        <button class="social-link-btn">Add</button>
      </div>
      <div class="social-link-row">
        <svg class="social-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/><path d="M2 12h20"/></svg>
        <div class="social-value">Not set</div>
        <button class="social-link-btn">Add</button>
      </div>
    </div>

    <div class="section-card">
      <div class="section-title">Privacy</div>
      <div class="toggle-row">
        <div>
          <div class="toggle-label-text">Public Profile</div>
          <div class="toggle-sub">Anyone can view your profile at the bazaar</div>
        </div>
        <label class="toggle-switch">
          <input type="checkbox" checked>
          <span class="toggle-slider"></span>
        </label>
      </div>
      <button class="btn-primary" style="width:100%;margin-top:16px;height:44px;font-size:14px">Save Changes</button>
    </div>
  </div>

  <!-- Holding Tokens -->
  <div class="tab-panel" id="holding">
    <div class="holding-stats">
      <div class="holding-stat">
        <div class="holding-stat-label">Total Value</div>
        <div class="holding-stat-val">$12,458</div>
      </div>
      <div class="holding-stat">
        <div class="holding-stat-label">24h Change</div>
        <div class="holding-stat-val text-teal">+$342</div>
      </div>
      <div class="holding-stat">
        <div class="holding-stat-label">Total P&L</div>
        <div class="holding-stat-val text-teal">+$2,145</div>
      </div>
    </div>
    <div class="section-card">
      <div class="empty-state">
        <div class="empty-icon">🏪</div>
        <div class="empty-title">No holding tokens.</div>
        <div class="empty-sub">Browse the bazaar and buy your first token to see it here.</div>
      </div>
    </div>
  </div>

  <!-- Created Tokens -->
  <div class="tab-panel" id="created">
    <div class="section-card">
      <div class="empty-state">
        <div class="empty-icon">🏮</div>
        <div class="empty-title">No stalls opened yet.</div>
        <div class="empty-sub">Create your first token to open a stall at the bazaar.</div>
        <button class="btn-primary" style="margin-top:20px" onclick="location.href='create_token.html'">Create Token &rsaquo;</button>
      </div>
    </div>
  </div>

  <!-- Transaction History -->
  <div class="tab-panel" id="tx">
    <div class="section-card">
      <div class="empty-state">
        <div class="empty-icon">📜</div>
        <div class="empty-title">No transactions yet.</div>
        <div class="empty-sub">Your trade history will appear here once you start trading.</div>
      </div>
    </div>
  </div>

  <!-- Arena History -->
  <div class="tab-panel" id="arena-hist">
    <div class="section-card">
      <div class="empty-state">
        <div class="empty-icon">⚔️</div>
        <div class="empty-title">No arena battles yet.</div>
        <div class="empty-sub">Join a Token War or Bazaar Showdown to build your arena record.</div>
      </div>
    </div>
  </div>

  <!-- Notifications -->
  <div class="tab-panel" id="notifs">
    <div class="section-card">
      <div class="notif-item">
        <div class="notif-dot"></div>
        <div class="notif-text"><strong>NobleFlame</strong>, your token <strong>MoonShard</strong> gained +42% today!</div>
        <div class="notif-time">2h ago</div>
      </div>
      <div class="notif-item">
        <div class="notif-dot"></div>
        <div class="notif-text">You received <strong>+50 pts</strong> for completing the Daily Quest.</div>
        <div class="notif-time">5h ago</div>
      </div>
      <div class="notif-item">
        <div class="notif-dot"></div>
        <div class="notif-text"><strong>PEPE Army</strong> club invited you to join their Arena war.</div>
        <div class="notif-time">1d ago</div>
      </div>
    </div>
  </div>

</main>
"""

# JS scripts
js_content = """
<script>
function showTab(id, btn) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.prof-tab').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
"""

final_html = f"<!DOCTYPE html>\n<html lang=\"en\">\n{head_content}\n<body>\n{header_content}\n{marquee_content}\n{sidebar_content}\n{main_content}\n{js_content}\n</body>\n</html>"

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/my_profile.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated my_profile.html successfully.")
