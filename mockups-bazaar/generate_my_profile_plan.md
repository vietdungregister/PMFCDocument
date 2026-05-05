# Plan: Generate my_profile.html — Stallspot Bazaar Mockup

## Context
- Project: `/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/`
- Reference files: `token_list_v4.html` (shared layout), `events.html` (pattern)
- Output: `my_profile.html` (overwrite existing)
- FRD: `Function Requirements - Bazaar.md` §4 (lines 219-268)

## Task
Write a Python script `gen_my_profile.py` in the mockups-bazaar folder, then run it to produce `my_profile.html`.

---

## Shared Layout (copy exactly from events.html)

### CSS variables (`:root`) — copy from events.html lines 9-39
### Global resets — copy from events.html lines 40-41
### `.header`, `.logo`, `.logo-mascot`, `.logo-text`, `.logo-sub` — copy from events.html lines 42-46
### `.header-search`, `.header-actions`, `.btn-ghost`, `.btn-primary` — copy from events.html lines 47-53
### `.marquee`, `.marquee-track`, `@keyframes scroll` — copy from events.html lines 54-58
### `.sidebar`, `.nav-group`, `.nav-label`, `.nav-item`, `.nav-badge` — copy from events.html lines 59-66
### `.user-card`, `.user-mascot`, `.user-name`, `.user-tier` — copy from events.html lines 67-70
### `.main` — copy from events.html line 71 (use `padding:28px 32px 60px`)

---

## Header HTML (copy from events.html lines 104-141)
- Logo SVG (cat hawker), Stallspot brand, search bar, Connect wallet + Create token buttons

## Marquee HTML (copy from events.html lines 143-158)

## Sidebar HTML — copy structure from events.html lines 160-234, BUT:
- **Set `my_profile` nav-item as `.active`** (not Events)
- Sidebar nav items:
  - Discover group: Discover→`token_list_v4.html`, Arena→`FR-012_TokenWar.html`, Clubs→`clubs.html`, Events→`events.html`
  - Personal group: **My Profile→`my_profile.html` (class="nav-item active")** with badge 3, Leader Board→`leaderboard.html`
  - Earn group: Point System→`points.html`, Rewards→`points.html`, Referrals→`referrals.html`, Stake→`token_list_v4.html`
  - User card at bottom: NobleFlame / Regular · 642 pts

---

## Page-specific CSS (add after shared CSS)

```css
/* Profile header card */
.profile-hero {
  background: var(--surface-1);
  border: 1px solid var(--border-1);
  border-radius: var(--r-lg);
  padding: 28px;
  display: flex;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 24px;
  position: relative;
}
.profile-avatar {
  width: 80px; height: 80px;
  border-radius: var(--r-pill);
  background: linear-gradient(135deg, var(--bz-amber-400), var(--bz-teal-500));
  display: grid; place-items: center;
  font-family: var(--font-display);
  font-size: 32px; font-weight: 800;
  color: #2a1505;
  flex-shrink: 0;
  border: 3px solid var(--bz-amber-400);
}
.profile-name {
  font-family: var(--font-display);
  font-size: 22px; font-weight: 800;
  color: var(--text-1);
  margin-bottom: 4px;
}
.profile-wallet {
  display: flex; align-items: center; gap: 8px;
  font-family: var(--font-mono);
  font-size: 12.5px; color: var(--text-3);
  margin-bottom: 8px;
}
.copy-btn {
  padding: 3px 8px;
  background: var(--surface-2);
  border: 1px solid var(--border-2);
  border-radius: var(--r-sm);
  color: var(--text-2); font-size: 11px;
  cursor: pointer; font-family: inherit;
}
.copy-btn:hover { border-color: var(--bz-amber-400); color: var(--bz-amber-400); }
.profile-bio { font-size: 13px; color: var(--text-2); max-width: 480px; }
.edit-profile-btn {
  position: absolute; top: 20px; right: 20px;
  padding: 7px 14px;
  background: var(--surface-2);
  border: 1px solid var(--border-2);
  border-radius: var(--r-md);
  color: var(--text-2); font-size: 13px; font-weight: 600;
  cursor: pointer; font-family: inherit;
}
.edit-profile-btn:hover { border-color: var(--bz-amber-400); color: var(--bz-amber-400); }

/* Stat cards row */
.stat-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-bottom: 28px;
}
.stat-card {
  background: var(--surface-1);
  border: 1px solid var(--border-1);
  border-radius: var(--r-lg);
  padding: 18px 20px;
}
.stat-card-label {
  font-size: 11px; text-transform: uppercase;
  letter-spacing: 0.06em; color: var(--text-3);
  font-weight: 600; margin-bottom: 6px;
}
.stat-card-value {
  font-family: var(--font-display);
  font-size: 22px; font-weight: 800;
  color: var(--bz-amber-400);
}
.stat-card-sub { font-size: 11.5px; color: var(--text-3); margin-top: 2px; }

/* Profile tabs (line indicator style — same as token_list_v4) */
.prof-tabs-wrap {
  border-bottom: 1px solid var(--border-1);
  margin-bottom: 24px;
  display: flex;
}
.prof-tabs { display: flex; gap: 2px; }
.prof-tab {
  padding: 10px 18px;
  background: transparent; border: none;
  border-bottom: 2px solid transparent;
  color: var(--text-2); font-family: inherit;
  font-size: 13.5px; font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
  margin-bottom: -1px;
  display: inline-flex; align-items: center; gap: 6px;
}
.prof-tab:hover { color: var(--text-1); }
.prof-tab.active {
  color: var(--bz-amber-400);
  border-bottom-color: var(--bz-amber-400);
}
.tab-badge {
  background: var(--bz-crimson); color: white;
  font-size: 10px; font-weight: 700;
  padding: 1px 6px; border-radius: var(--r-pill);
}

/* Tab content panels */
.tab-panel { display: none; }
.tab-panel.active { display: block; }

/* Section card */
.section-card {
  background: var(--surface-1);
  border: 1px solid var(--border-1);
  border-radius: var(--r-lg);
  padding: 22px 24px;
  margin-bottom: 16px;
}
.section-title {
  font-family: var(--font-display);
  font-size: 14px; font-weight: 700;
  color: var(--bz-amber-400);
  margin-bottom: 18px;
  text-transform: uppercase; letter-spacing: 0.05em;
}

/* Form fields */
.field-row { margin-bottom: 16px; }
.field-label { font-size: 12px; color: var(--text-3); font-weight: 600; margin-bottom: 6px; }
.field-value { font-size: 14px; color: var(--text-1); }
.field-input {
  width: 100%; padding: 9px 12px;
  background: var(--surface-2); border: 1px solid var(--border-1);
  border-radius: var(--r-md); color: var(--text-1);
  font-family: inherit; font-size: 13.5px;
}
.field-input:focus { outline: none; border-color: var(--bz-amber-400); }

/* Social links */
.social-link-row {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 14px;
  background: var(--surface-2); border: 1px solid var(--border-1);
  border-radius: var(--r-md); margin-bottom: 8px;
}
.social-icon { width: 20px; height: 20px; color: var(--text-3); flex-shrink: 0; }
.social-value { font-size: 13px; color: var(--text-3); flex: 1; font-style: italic; }
.social-link-btn {
  font-size: 11px; color: var(--bz-amber-400);
  background: none; border: none; cursor: pointer;
  font-family: inherit; font-weight: 600;
}

/* Privacy toggle */
.toggle-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 14px 0; border-top: 1px solid var(--border-1);
}
.toggle-label-text { font-size: 14px; color: var(--text-1); font-weight: 500; }
.toggle-sub { font-size: 12px; color: var(--text-3); margin-top: 2px; }
.toggle-switch { position:relative; width:44px; height:24px; display:inline-block; }
.toggle-switch input { opacity:0; width:0; height:0; }
.toggle-slider {
  position:absolute; cursor:pointer; top:0; left:0; right:0; bottom:0;
  background:#374151; border-radius:12px; transition:0.2s;
}
.toggle-slider:before {
  position:absolute; content:""; height:18px; width:18px;
  left:3px; bottom:3px; background:white; border-radius:50%; transition:0.2s;
}
.toggle-switch input:checked + .toggle-slider { background: var(--bz-teal-500); }
.toggle-switch input:checked + .toggle-slider:before { transform:translateX(20px); }

/* Holding tokens — mini stats */
.holding-stats {
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 12px; margin-bottom: 20px;
}
.holding-stat {
  background: var(--surface-1); border: 1px solid var(--border-1);
  border-radius: var(--r-md); padding: 14px 16px;
}
.holding-stat-label { font-size: 11px; color: var(--text-3); font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 4px; }
.holding-stat-val { font-family: var(--font-mono); font-size: 16px; font-weight: 600; color: var(--text-1); }
.text-teal { color: var(--bz-teal-400); }

/* Empty state */
.empty-state {
  text-align: center; padding: 60px 20px;
  color: var(--text-3);
}
.empty-icon { font-size: 48px; margin-bottom: 12px; }
.empty-title { font-family: var(--font-display); font-size: 16px; font-weight: 700; color: var(--text-2); margin-bottom: 6px; }
.empty-sub { font-size: 13px; color: var(--text-3); }

/* Notifications item */
.notif-item {
  display: flex; align-items: flex-start; gap: 12px;
  padding: 14px 0; border-bottom: 1px solid var(--border-1);
}
.notif-item:last-child { border-bottom: none; }
.notif-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--bz-amber-400); flex-shrink: 0; margin-top: 5px; }
.notif-dot.read { background: transparent; border: 1.5px solid var(--border-2); }
.notif-text { font-size: 13px; color: var(--text-2); flex: 1; }
.notif-text strong { color: var(--text-1); }
.notif-time { font-size: 11.5px; color: var(--text-mute); flex-shrink: 0; }

/* Arena history row */
.arena-row {
  display: flex; align-items: center; gap: 14px;
  padding: 12px 0; border-bottom: 1px solid var(--border-1);
}
.arena-row:last-child { border-bottom: none; }
.arena-badge {
  padding: 3px 9px; border-radius: var(--r-pill);
  font-size: 11px; font-weight: 700; flex-shrink: 0;
}
.badge-win { background: rgba(92,168,134,0.15); color: var(--bz-teal-400); }
.badge-loss { background: rgba(214,90,84,0.15); color: var(--bz-crimson); }
.badge-pending { background: var(--bz-amber-soft); color: var(--bz-amber-400); }

/* Tx history row */
.tx-row {
  display: flex; align-items: center; gap: 14px;
  padding: 12px 0; border-bottom: 1px solid var(--border-1);
}
.tx-row:last-child { border-bottom: none; }
.tx-type {
  width: 48px; text-align: center; padding: 3px 0;
  border-radius: var(--r-sm); font-size: 11px; font-weight: 700; flex-shrink: 0;
}
.tx-buy { background: rgba(92,168,134,0.15); color: var(--bz-teal-400); }
.tx-sell { background: rgba(214,90,84,0.15); color: var(--bz-crimson); }
```

---

## Profile Hero HTML

```html
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
```

---

## Stat Cards HTML

4 cards:
1. Portfolio Value / `$12,458` / ↑ 2.82% today
2. Tokens Created / `2` / stalls opened
3. Total Trades / `47` / buys & sells
4. Member Since / `Mar 2026` / Regular · 642 pts

---

## Tabs HTML

```html
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
```

---

## Tab Panel: Profile Info

Two section cards:

**Card 1 — Basic Information:**
- Username: NobleFlame
- Member Since: March 2026
- Tier: Regular (642 pts)
- Email (optional): Not set

**Card 2 — Social Links:**
Three `.social-link-row` items with icons:
- X (Twitter): icon = bird SVG, value = "Not set", button "Add"
- Telegram: icon = paper plane SVG, value = "Not set", button "Add"
- Website: icon = globe SVG, value = "Not set", button "Add"

**Card 3 — Privacy:**
Toggle row: "Public Profile" / "Anyone can view your profile at the bazaar" / toggle (checked = public)

Save button: amber gradient, full width, "Save Changes"

---

## Tab Panel: Holding Tokens

Mini stats row (3 cards):
- Total Value: `$12,458`
- 24h Change: `+$342` (teal color)
- Total P&L: `+$2,145` (teal color)

Empty state (no tokens held yet):
```html
<div class="empty-state">
  <div class="empty-icon">🏪</div>
  <div class="empty-title">No holding tokens.</div>
  <div class="empty-sub">Browse the bazaar and buy your first token to see it here.</div>
</div>
```

---

## Tab Panel: Created Tokens

Section card with empty state:
```html
<div class="empty-state">
  <div class="empty-icon">🏮</div>
  <div class="empty-title">No stalls opened yet.</div>
  <div class="empty-sub">Create your first token to open a stall at the bazaar.</div>
  <button style="margin-top:16px;..." onclick="location.href='create_token.html'">Create Token →</button>
</div>
```

---

## Tab Panel: Transaction History

Section card with empty state:
```html
<div class="empty-state">
  <div class="empty-icon">📜</div>
  <div class="empty-title">No transactions yet.</div>
  <div class="empty-sub">Your trade history will appear here once you start trading.</div>
</div>
```

---

## Tab Panel: Arena History

Section card with empty state:
```html
<div class="empty-state">
  <div class="empty-icon">⚔️</div>
  <div class="empty-title">No arena battles yet.</div>
  <div class="empty-sub">Join a Token War or Bazaar Showdown to build your arena record.</div>
</div>
```

---

## Tab Panel: Notifications (3 unread)

Section card with 3 notification items:

1. (unread dot) **NobleFlame**, your token **MoonShard** gained +42% today! · 2h ago
2. (unread dot) You received **+50 pts** for completing the Daily Quest. · 5h ago
3. (unread dot) **PEPE Army** club invited you to join their Arena war. · 1d ago

---

## JavaScript

```javascript
function showTab(id, btn) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.prof-tab').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
function copyWallet() {
  navigator.clipboard.writeText('H3XQhXxxxxxxxxxxxxxxxxxxxxxxxxx');
  // optional toast feedback
}
```

---

## Execution Steps

1. Create `gen_my_profile.py` in `mockups-bazaar/`
2. Script builds the full HTML string combining:
   - Shared CSS (from events.html pattern)
   - Page-specific CSS above
   - Header HTML (from events.html)
   - Marquee HTML (from events.html)
   - Sidebar HTML (from events.html, with My Profile set active)
   - `<main class="main">` with profile hero + stat cards + tabs + all 6 tab panels
   - JS tab switcher
3. Write to `my_profile.html` (overwrite)
4. Run: `python3 gen_my_profile.py`
5. Open in browser to verify layout

## Key Rules
- Use **Bazaar palette only** (amber/teal/brown) — NO blue/purple primary colors
- Tabs use **line indicator** style (border-bottom), not pill/button style
- Shared layout (header/marquee/sidebar) **must be identical** to events.html
- My Profile nav-item in sidebar **must be `.active`** (amber highlight)
- All 6 tabs must be **functional** (JS switching, no page reload)
