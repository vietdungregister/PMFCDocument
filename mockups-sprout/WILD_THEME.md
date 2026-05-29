# WILD_THEME.md — Design system reference

This is the technical cheat sheet for the Wild theme. Every block below is **copy-paste ready** — pasting it into a mockup file's `<style>` (in the right place) will produce the intended visual.

The single source of truth for component visual is `../Sửa giao diện html/token_list_v4_wild.html`. When in doubt, look at how that file uses these tokens.

---

## 1. `:root` tokens (mandatory in every file)

Replace each mockup's existing `:root` block with this. Keep any file-specific tokens that don't conflict.

```css
:root {
  /* ── Mood B Living Garden surfaces ── */
  --bg:          #0a1610;
  --surface-1:   #131f18;
  --surface-2:   #1a2a20;
  --surface-3:   #243528;
  --border-1:    #1f2d24;
  --border-2:    #2d4234;

  /* ── Brand peach (primary accent) ── */
  --sp-peach-100: #f4cba0;
  --sp-peach-200: #e8a87c;
  --sp-peach-400: #e8a87c;
  --sp-peach-500: #d68a5b;
  --sp-peach-soft: rgba(232, 168, 124, 0.10);

  /* ── Teal + forest ── */
  --sp-forest-300: #5ba886;
  --sp-forest-500: #3d7458;
  --sp-forest-700: #3d7458;
  --sp-cream:      #f4cba0;
  --sp-teal-300:   #9ED8B8;
  --sp-teal-400:   #7CC4A4;
  --sp-teal-500:   #5BA886;

  /* ── Status ── */
  --sp-crimson:    #D65A54;
  --crimson-soft:  rgba(214, 90, 84, 0.10);
  --teal-soft:     rgba(124, 196, 164, 0.10);

  /* ── Text ── */
  --text-1: #f5f7f4;
  --text-2: #a3b0a7;
  --text-3: #6f7d74;
  --text-mute: #4a5650;

  /* ── Wild polaroid + sticker extensions ── */
  --w-paper:    #fdf8ec;
  --w-cream:    #f4ecdc;
  --w-ink:      #2a1505;
  --w-ink-2:    #6b4a30;
  --w-tape-y:   rgba(255, 216, 130, 0.60);
  --w-tape-p:   rgba(255, 107, 138, 0.40);
  --w-tape-g:   rgba(184, 226, 92, 0.55);
  --w-coral:    #ff8b5e;
  --w-pink:     #ff6b8a;
  --w-sunshine: #ffd35e;
  --w-lime:     #b8e25c;
  --w-sky:      #5ee2ff;
  --w-grape:    #a878ff;

  /* ── Typography ── */
  --font-display: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'SF Mono', monospace;
  --font-disp-it: 'Fraunces', 'Plus Jakarta Sans', serif;
  --font-hand:    'Caveat', cursive;

  /* ── Radius / size / motion ── */
  --r-sm: 6px; --r-md: 10px; --r-lg: 14px; --r-pill: 999px;
  --header-h: 60px; --marquee-h: 30px; --sidebar-w: 240px;
  --mascot-sm: 22px; --mascot-md: 30px; --mascot-lg: 40px;
  --ease: cubic-bezier(0.4, 0, 0.2, 1);
}
```

Also update the Google Fonts `<link>` in `<head>` to include the two new families:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@500;600;700&family=Fraunces:ital,wght@1,700;1,800;1,900&family=Caveat:wght@500;700&display=swap" rel="stylesheet">
```

---

## 2. Legacy-token alias block (Phase 1 only)

For the 5 critical-broken files, append this to the `:root` to make undeclared legacy tokens resolve to the new ones:

```css
:root {
  /* Legacy aliases — compatibility for files that still reference these names */
  --card:           var(--surface-1);
  --card2:          var(--surface-2);
  --card-boarder:   var(--border-1);   /* sic: typo "boarder" kept */
  --card-hover:     var(--surface-3);
  --primary:        var(--sp-peach-400);
  --primary-hover:  var(--sp-peach-500);
  --accent:         var(--sp-teal-400);
  --danger:         var(--sp-crimson);
  --danger-hover:   #c14844;
  --text-primary:   var(--text-1);
  --text-secondary: var(--text-2);
  --text-tertiary:  var(--text-3);
}
```

For `FR-012b_TokenWar_PredictionMarket.html` specifically, paste the FULL `:root` block from §1 *first* (it's missing the core `--bg` token, body is renders white otherwise), THEN append the alias block above.

---

## 3. Body + page background

```css
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: var(--bg);
  background-image:
    radial-gradient(ellipse 800px 400px at 20% 0%, rgba(232,168,124,0.06), transparent 60%),
    radial-gradient(ellipse 600px 400px at 90% 30%, rgba(124,196,164,0.05), transparent 60%);
  background-attachment: fixed;
  color: var(--text-1);
  font-family: var(--font-body);
  font-size: 14px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
}
```

---

## 4. Marquee (top strip)

HTML (place as first element after `<body>`):

```html
<div class="marquee">
  <div class="marquee-track">
    <span class="peach">PLANT YOUR SEED</span><span>·</span>
    <span>MAKE MONEY ON THE MEMECONOMY</span><span>·</span>
    <span class="teal">FAIR LAUNCH</span><span>·</span>
    <span>NO BOT DRAMA</span><span>·</span>
    <span class="peach">TALLEST TREE WINS</span><span>·</span>
    <span>SEEDS PLANTED HERE</span><span>·</span>
    <!-- repeat -->
    <span class="peach">PLANT YOUR SEED</span><span>·</span>
    <span>MAKE MONEY ON THE MEMECONOMY</span><span>·</span>
    <span class="teal">FAIR LAUNCH</span><span>·</span>
    <span>NO BOT DRAMA</span><span>·</span>
    <span class="peach">TALLEST TREE WINS</span><span>·</span>
    <span>SEEDS PLANTED HERE</span>
  </div>
</div>
```

CSS:

```css
.marquee {
  position: fixed; top: 0; left: 0; right: 0;
  height: var(--marquee-h);
  background: var(--surface-1);
  border-bottom: 1px solid var(--border-1);
  overflow: hidden;
  display: flex; align-items: center;
  z-index: 100;
}
.marquee-track {
  display: flex; gap: 36px;
  white-space: nowrap;
  animation: scroll 42s linear infinite;
  font-family: var(--font-display);
  font-size: 12px; font-weight: 700;
  letter-spacing: 0.12em;
  color: var(--text-3);
}
.marquee:hover .marquee-track { animation-duration: 14s; }
.marquee-track .peach { color: var(--sp-peach-400); text-shadow: 0 0 12px rgba(232,168,124,0.35); }
.marquee-track .teal  { color: var(--sp-teal-400); text-shadow: 0 0 12px rgba(124,196,164,0.35); }
@keyframes scroll {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

---

## 5. Sidebar (Wild cream-pill, the default)

HTML structure (240px fixed-left column, place as the next element after marquee):

```html
<aside class="sidebar">
  <!-- "today's garden" banner sits at the top via ::before -->

  <a class="logo" href="token_list_v4.html">
    <div class="logo-mascot">
      <!-- 30×30 mascot SVG, see §10 for the path -->
    </div>
    <div>
      <div class="logo-name">Sprout</div>
      <span class="logo-sub">the meme garden</span>
    </div>
  </a>

  <nav class="nav">
    <div class="nav-group">
      <a class="nav-item" href="token_list_v4.html">
        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><!-- discover icon --></svg>
        Discover
      </a>
      <a class="nav-item" href="FR-012_TokenWar.html">
        <svg class="icon"><!-- flame icon --></svg>
        Arena
      </a>
      <a class="nav-item" href="clubs.html">
        <svg class="icon"><!-- swords icon --></svg>
        Clubs
      </a>
      <a class="nav-item" href="events.html">
        <svg class="icon"><!-- calendar icon --></svg>
        Events
      </a>
      <a class="nav-item" href="leaderboard.html">
        <svg class="icon"><!-- trophy icon --></svg>
        Leader Board
      </a>
    </div>
    <div class="nav-group">
      <a class="nav-item" href="my_profile.html">
        <svg class="icon"><!-- user icon --></svg>
        My Profile
        <span class="nav-badge">3</span>
      </a>
    </div>
    <div class="nav-group">
      <a class="nav-item" href="points.html">Points</a>
      <a class="nav-item" href="rewards.html">Rewards</a>
      <a class="nav-item" href="referrals.html">Referrals</a>
      <a class="nav-item" href="#">Stake</a>
    </div>
  </nav>

  <div class="user-card" onclick="location.href='my_profile.html'">
    <div class="user-mascot"><!-- mini mascot SVG --></div>
    <div class="user-info">
      <div class="user-name">NobleFlame</div>
      <div class="user-tier">Sprout · <span class="uc-pts tier-sprout">642 pts</span></div>
    </div>
  </div>

  <div class="sidebar-footer">
    <div class="sf-social"><!-- Telegram + X icons --></div>
    <div class="sf-pills"><a href="#">Doc</a><a href="#">FAQ</a><a href="#">How it works</a></div>
    <div class="sf-copyright">© 2026 Sprout</div>
  </div>
</aside>
```

CSS — paste the entire Wild sidebar block (Mood B base + v0.2/0.4/0.5/0.6/0.7/0.8 overrides) verbatim from `../Sửa giao diện html/token_list_v4_wild.html`. The block is large (~600 lines) so don't try to retype it — find the comment markers below and copy between them:

```
  /* ╔═══ "STICKER + TEXT" — sidebar v0.4 ═══╗ */
  ...
  /* ╚═══ end "STICKER + TEXT" sidebar v0.4 ═══╝ */

  /* ╔═══ v0.5 SIMPLIFY ═══╗ */
  ...
  /* ╚═══ end v0.5 SIMPLIFY ═══╝ */

  /* ╔═══ v0.6 FIX — unify nav-item PILL background ═══╗ */
  ...

  /* ╔═══ v0.8 — unify sidebar nav icon bg ═══╗ */
  ...
```

Each of these blocks must be present together for the final cream-pill sidebar to render correctly (later layers override earlier ones — this is the explicit cascade order chosen by the team).

**Active nav item**: the sidebar logic in the reference assumes the page currently being viewed has `class="active"` on its matching `.nav-item`. Update each page's sidebar HTML so the relevant item is active (e.g. on `leaderboard.html`, the Leader Board nav item has `class="nav-item active"`).

---

## 6. Header (60px top bar)

If a page already has a header (search box + wallet + create button), keep its structure and apply the Wild treatment from the reference. Pages without a header (e.g. dashboard, profile) don't need one — the sidebar + marquee are enough.

Reference selectors to look for: `.header`, `.logo`, `.header-search`, `.header-actions`, `.btn-primary`, `.btn-ghost`, `.wallet-connected`, `.wc-*`. Copy those CSS blocks verbatim from the reference.

Key visual moves:
- Header height 60px, position fixed top (just under the marquee — `top: var(--marquee-h)`).
- Logo: peach gradient text + 40×40 mascot tile.
- "Create token" → **"Plant a seed"** italic Fraunces pill with peach gradient.
- Wallet pill stays as the reference shows (pill with mascot avatar, SOL balance, address, network dot).

---

## 7. Token cards (polaroid, the visual hero)

This is the single most distinctive visual in the theme. Apply to: token list grid, clubs grid, events grid, rewards grid, leaderboard rows, public/my profile token holdings.

### 7a. HTML structure

```html
<div class="token-grid">
  <div class="token-card" onclick="location.href='token_detail.html'">
    <!-- favorite heart top-right -->
    <span class="favorite"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
      <path d="M12 21.35..."/></svg></span>

    <!-- avatar + meta block -->
    <div class="card-head">
      <div class="token-avatar" style="background:linear-gradient(135deg,#1a3a4a,#2a9d8f)">
        <svg viewBox="0 0 60 60"><!-- token icon --></svg>
      </div>
      <div class="token-meta">
        <div class="token-name-row">
          <span class="token-name">Moon Token</span>
          <span class="trust-leaf trust-gold" title="Gold · 64/100">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/>
            </svg>
          </span>
        </div>
        <div class="token-symbol">MOON</div>
        <div class="token-desc">A community-driven meme reaching escape velocity 🌙</div>
      </div>
    </div>

    <div class="price-row">
      <span class="price-value">$0.0234</span>
      <span class="price-change price-up">↑ 38.5%</span>
    </div>

    <div class="stats-row">
      <div class="stat-cell">
        <span class="stat-label">Volume 24h</span>
        <span class="stat-value">$1.95M</span>
      </div>
      <div class="stat-cell">
        <span class="stat-label">Market cap</span>
        <span class="stat-value">$242.2K</span>
      </div>
    </div>

    <div class="card-footer">
      <div class="creator-info">
        <div class="creator-avatar" style="background:linear-gradient(135deg,#7cc4a4,#5ba886)"></div>
        <span class="creator-name">by alice · Sapling tier · 12d ago</span>
      </div>
    </div>

    <div class="graduation">
      <span class="graduation-label">To DEX</span>
      <div class="graduation-bar"><div class="graduation-fill" style="width:22%"></div></div>
      <span class="graduation-percent">22%</span>
    </div>
  </div>
  <!-- more cards -->
</div>
```

### 7b. Grid container

```css
.token-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 18px;
}
```

### 7c. Card polaroid styles

Reference comment marker in `token_list_v4_wild.html`:
```
/* ╔═══ "STICKER GARDEN" — WILD v0.2 — added 2026-05-27 ═══╗ */
```
Copy the full polaroid block (from `.token-card { background: var(--w-paper); ...` through the end of `.card.almost-there` and `.card.featured` rules).

Visual highlights:
- Cards have **cream paper bg** (`var(--w-paper)`) with multi-layer drop shadow (no border).
- **No rotation** on cards themselves (we tilt only stickers, see Wild philosophy rule #3 in AGENTS.md §3).
- **Washi tape on top** of each card via `::before` on `.card-head` — alternating yellow / pink / lime colors using `nth-of-type(even)` and `nth-of-type(3n)`.
- **Avatar** has 2.5px black border + 3px offset shadow.
- **Ink-color text** (`var(--w-ink)`) throughout the card — name in italic Fraunces 19px, symbol mono caps, description ink-2.
- **Price** in mono 22px ink. Price change as a **pill chip**: green bg for up, pink-soft bg for down.
- **Almost-there** state: peach soft bg fade + shimmering sun stripe sweeping across.
- **Featured** state: 3px coral outline + heartbeat glow pulse.

### 7d. Sticker badges (JS-injected)

Append to the page's main script (after DOMContentLoaded or at end of body):

```js
(function() {
  const stickers = [
    { cls: 's-hot',    text: '🔥 Blazing' },
    { cls: 's-fresh',  text: '🌱 Fresh' },
    { cls: 's-gem',    text: '💎 Gem' },
    { cls: 's-rising', text: '🚀 Rising' },
    { cls: 's-rare',   text: '✨ Rare drop' },
    { cls: 's-yum',    text: '🍑 Juicy' }
  ];
  document.querySelectorAll('.token-card').forEach((card, i) => {
    const s = stickers[i % stickers.length];
    const b = document.createElement('div');
    b.className = 'sticker-badge ' + s.cls;
    b.textContent = s.text;
    const rot = (Math.random() * 6 - 3).toFixed(1);
    if (i % 2 === 1) {
      b.style.right = 'auto';
      b.style.left = '-12px';
      b.style.transform = 'rotate(' + (-rot) + 'deg)';
    } else {
      b.style.transform = 'rotate(' + rot + 'deg)';
    }
    card.appendChild(b);
  });
})();
```

Sticker CSS (all 6 variants now unified to peach per team direction — see v0.7 override in the reference file):

```css
.sticker-badge {
  position: absolute; top: -14px; right: -10px;
  font-family: var(--font-disp-it); font-style: italic;
  font-weight: 900; font-size: 11px; color: var(--w-ink);
  padding: 5px 11px;
  border-radius: 8px; border: 2px solid var(--w-ink);
  box-shadow: 3px 3px 0 var(--w-ink);
  z-index: 5; white-space: nowrap; text-transform: uppercase;
  pointer-events: none; letter-spacing: 0.02em;
}
/* All variants → unified peach (v0.7 decision) */
.sticker-badge.s-hot,
.sticker-badge.s-fresh,
.sticker-badge.s-gem,
.sticker-badge.s-rising,
.sticker-badge.s-rare,
.sticker-badge.s-yum {
  background: var(--sp-peach-400);
  color: var(--w-ink);
}
```

---

## 8. Forms (create_token, edit_profile_privacy)

Form container = cream paper polaroid. Input fields = cream-light bg + ink-color border. Submit button = peach polaroid pill.

```css
.form-container {
  max-width: 720px;
  margin: 0 auto;
  background: var(--w-paper);
  color: var(--w-ink);
  border-radius: var(--r-lg);
  padding: 32px 28px;
  box-shadow: 0 14px 28px -8px rgba(0,0,0,0.55),
              0 4px 8px rgba(0,0,0,0.3);
  position: relative;
}
/* Washi tape at top */
.form-container::before {
  content: '';
  position: absolute;
  top: -10px; left: 50%;
  transform: translateX(-50%) rotate(-3deg);
  width: 100px; height: 18px;
  background: var(--w-tape-y);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.5);
}
.form-title {
  font-family: var(--font-disp-it); font-style: italic;
  font-weight: 900; font-size: 28px;
  color: var(--w-ink);
  margin-bottom: 4px;
}
.form-subtitle {
  font-family: var(--font-hand);
  font-size: 18px; color: var(--w-ink-2);
  margin-bottom: 24px;
}
.form-row {
  display: flex; flex-direction: column;
  gap: 6px; margin-bottom: 18px;
}
.form-label {
  font-family: var(--font-disp-it); font-style: italic;
  font-weight: 700; font-size: 13px;
  color: var(--w-ink);
}
.form-input, .form-textarea, .form-select {
  background: var(--w-cream);
  color: var(--w-ink);
  border: 1.5px solid var(--w-ink-2);
  border-radius: 8px;
  padding: 10px 14px;
  font-family: var(--font-body); font-size: 14px;
  transition: border-color 0.15s;
}
.form-input:focus, .form-textarea:focus, .form-select:focus {
  outline: none;
  border-color: var(--sp-peach-500);
  box-shadow: 0 0 0 3px var(--sp-peach-soft);
}
.form-submit {
  background: linear-gradient(180deg, var(--sp-peach-200), var(--sp-peach-500));
  color: var(--w-ink);
  border: none;
  height: 44px; padding: 0 28px;
  border-radius: var(--r-pill);
  font-family: var(--font-disp-it); font-style: italic;
  font-weight: 900; font-size: 14px;
  cursor: pointer;
  box-shadow: 0 4px 0 var(--w-ink);
  transition: transform 0.15s;
}
.form-submit:hover { transform: translateY(-2px); box-shadow: 0 6px 0 var(--w-ink); }
.form-submit:active { transform: scale(0.97); }
```

For toggle switches in `edit_profile_privacy.html`, the existing `.tt-toggle` style in the codebase already works — just retint the active state to `var(--sp-teal-500)` (matches reference). Do not switch to a different toggle component.

---

## 9. Stat cards / dashboard panels (token_detail, dashboards, profile)

Two patterns: **big-number polaroid card** (for headline stats like total volume, points) and **mini stat row** (for compact secondary stats).

```css
/* Big stat polaroid */
.stat-polaroid {
  background: var(--w-paper); color: var(--w-ink);
  border-radius: var(--r-lg);
  padding: 22px 24px 20px;
  box-shadow: 0 14px 28px -8px rgba(0,0,0,0.55),
              0 4px 8px rgba(0,0,0,0.3);
  position: relative; overflow: visible;
}
.stat-polaroid::before {
  content: ''; position: absolute;
  top: -10px; left: 30%;
  transform: translateX(-50%) rotate(-3deg);
  width: 70px; height: 16px;
  background: var(--w-tape-y);
}
.stat-polaroid-label {
  font-family: var(--font-disp-it); font-style: italic;
  font-weight: 700; font-size: 12px;
  color: var(--w-ink-2); text-transform: uppercase;
  letter-spacing: 0.06em; margin-bottom: 4px;
}
.stat-polaroid-value {
  font-family: var(--font-mono); font-weight: 700;
  font-size: 32px; color: var(--w-ink);
  letter-spacing: -0.02em; line-height: 1;
}
.stat-polaroid-delta {
  margin-top: 6px;
  font-family: var(--font-mono); font-weight: 700;
  font-size: 12px;
  padding: 2px 8px; border-radius: var(--r-pill);
  display: inline-block;
}
.stat-polaroid-delta.up   { color: #2e8b57; background: rgba(184,226,92,0.45); }
.stat-polaroid-delta.down { color: #b94842; background: rgba(255,107,138,0.28); }
```

For charts: keep the chart on a dark surface (`var(--surface-1)`) so data lines stay legible, but wrap it in a cream polaroid frame using `.stat-polaroid` as the outer container and an inner `.chart-canvas { background: var(--surface-1); border-radius: 10px; padding: 12px; }` for the actual chart. This gives the polaroid look without making digit columns unreadable.

---

## 10. Mascot character + chat affordance (universal — every functional page)

Place this just before `</body>` on every functional page.

### 10a. HTML

```html
<div class="mascot-character" id="mascotChar">
  <div class="mc-body" title="Ask Sprout">
    <svg viewBox="0 0 64 64" fill="none">
      <ellipse cx="32" cy="50" rx="20" ry="12" fill="#3d7458"/>
      <ellipse cx="22" cy="26" rx="7" ry="13" transform="rotate(-28 22 26)" fill="#7cc4a4"/>
      <ellipse cx="42" cy="26" rx="7" ry="13" transform="rotate(28 42 26)" fill="#5ba886"/>
      <ellipse cx="32" cy="20" rx="5" ry="10" fill="#9ED8B8"/>
      <rect x="29.5" y="28" width="5" height="18" fill="#3d7458"/>
      <circle cx="26" cy="51" r="3" fill="#1a1208"/>
      <circle cx="38" cy="51" r="3" fill="#1a1208"/>
      <circle cx="27" cy="50" r="1.1" fill="#fff"/>
      <circle cx="39" cy="50" r="1.1" fill="#fff"/>
      <path d="M 26 56 Q 32 60 38 56" stroke="#1a1208" stroke-width="1.8" fill="none" stroke-linecap="round"/>
      <ellipse cx="20" cy="55" rx="3" ry="2" fill="#ff6b8a" opacity="0.7"/>
      <ellipse cx="44" cy="55" rx="3" ry="2" fill="#ff6b8a" opacity="0.7"/>
    </svg>
    <span class="mc-label">Sprout · tap for tips</span>
  </div>
</div>
```

The speech-bubble version (with the rotating "Hey!" tip) is intentionally suppressed by the v0.7 override (`.mc-bubble { display: none }`). Don't re-enable it.

### 10b. CSS — copy from reference

Find the block bounded by `/* ╔═══ v0.7 — sticker unify + hide bubble + live activity panel ═══╗ */` in the reference and grab the `.mascot-character`, `.mc-body`, `.mc-label`, `.mc-bubble`, `.mc-cta` rules.

Visual: 110×110 round body, sunshine→peach gradient, 6px offset black drop shadow, idle bobbing animation, tap label sticker pinned to the bottom-right.

### 10c. Chat panel (optional but recommended)

If you have time, include the chat panel (`.chat-panel` block, ~150 lines of CSS) that opens when the mascot is clicked. Reference: same v0.7 block. Mock-conversation JS lives at the bottom of the reference file in a self-invoking IIFE — copy that too.

Decision: chat panel is fine to include on every page (no performance cost when closed). If a particular page is space-constrained on mobile, the existing media-query rule already hides it at <640px.

---

## 11. Live Activity panel (ONLY on `token_list_v4.html`)

This is a right-side dock that shows real-time mock feed of buys / sells / mints / graduations. **Do NOT add this to any page other than the token list anchor** — it would be noise on detail/profile/form pages and confuses information architecture.

The full implementation (HTML + CSS + JS) is already in the reference file. Look for these markers:
```
/* ╔═══ v0.9 — Live Activity → FLAT DARK feed (Option A) ═══╗ */
...
<!-- v0.7 LIVE ACTIVITY (Option A flat dark via v0.9 overrides) -->
```

The feed pushes a new mock entry every 8s. Trim to 14 items. Color-coded left bar per action type (green = buy, crimson = sell, peach = mint, grape = graduated).

If the team later decides to spread this pattern to other pages (e.g. "Trending tokens" on profile, "Recent winners" on leaderboard), they will tell you. Don't pre-spread it.

---

## 12. Verification (headless Chromium)

Quick verify script template — save as `_codex_tools/verify.js`:

```js
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const FILES = fs.readdirSync('.')
  .filter(f => f.endsWith('.html') && !f.startsWith('_'));

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
    // executablePath: '/path/to/chromium'
  });

  fs.mkdirSync('_codex_screenshots', { recursive: true });

  for (const file of FILES) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });

    const url = 'file://' + path.resolve(file);
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
    await new Promise(r => setTimeout(r, 1500));
    await page.screenshot({
      path: '_codex_screenshots/' + file.replace('.html', '_desktop.png')
    });

    // mobile
    await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
    await new Promise(r => setTimeout(r, 500));
    await page.screenshot({
      path: '_codex_screenshots/' + file.replace('.html', '_mobile.png')
    });

    console.log(file, errors.length ? 'ERRORS: ' + errors.join('; ') : 'OK');
    await page.close();
  }

  await browser.close();
})();
```

Run with `node _codex_tools/verify.js`. Browse `_codex_screenshots/` for visual review.

---

## 13. Quick-reference: which selector lives where

If you're searching the reference for a specific pattern, here are the key class names:

| Class | What it is | Section |
|-------|------------|---------|
| `.marquee`, `.marquee-track` | Top scrolling text | §4 |
| `.sidebar`, `.nav-item`, `.user-card` | Left navigation | §5 |
| `.header`, `.logo`, `.btn-primary` | Top header | §6 |
| `.token-grid`, `.token-card` | Token list cards | §7 |
| `.card-head`, `.token-avatar`, `.token-meta` | Inside each card | §7 |
| `.sticker-badge`, `.s-hot`/`s-fresh`/etc. | Floating sticker label | §7d |
| `.trust-leaf`, `.trust-gold`/`silver`/`bronze` | Token trust shield | §7 |
| `.graduation`, `.graduation-bar`, `.graduation-fill` | DEX progress bar | §7 |
| `.form-container`, `.form-input`, `.form-submit` | Form pages | §8 |
| `.stat-polaroid`, `.stat-polaroid-value` | Big-number cards | §9 |
| `.mascot-character`, `.mc-body`, `.mc-label` | Bottom-right mascot | §10 |
| `.live-activity`, `.la-feed`, `.la-item` | Right-side activity feed | §11 |

---

## 14. Style decisions the team has already made (don't re-litigate)

- **Cream polaroid cards on dark page** — kept.
- **Italic Fraunces for display, Caveat for handwritten labels** — kept. Mix carefully (only use Caveat for small captions and "today's garden"-type labels, never for body text).
- **Sticker icon sidebar (cream pills with colored sticker icons)** — ✅ **chosen by the team**. Use this everywhere. The alternative flat-dark sidebar at `../Sửa giao diện html/token_list_v4_wild_A.html` is NOT to be applied — do not consider it.
- **Sticker badges all unified to peach** — kept.
- **Live activity = flat dark feed** — kept (not polaroid).
- **No rotations on cards / buttons / tabs** — kept. Tilt only stickers and washi tape (max ±3°).
- **Mood B spec lock §1.3a is overridden** — the original "signature glow" comment in some files (`/* === Mood B signature glow (locked 2026-05-05 — SPROUT_UI_SPEC.md §1.3a) === */`) is **no longer binding**. The team granted creative freedom; the Wild treatment supersedes it. You may modify those blocks.

---

## 15. End

That's it. With this file + AGENTS.md + the gold reference HTML, you have everything you need. Start at AGENTS.md §2 (required reading) → §5 phase 1.

If something is genuinely ambiguous (a screen's existing structure can't map cleanly to the Wild patterns above), stop and flag it — don't invent.
