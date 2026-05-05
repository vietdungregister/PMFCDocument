#!/usr/bin/env python3
"""Generate create_token.html — 3-step wizard with Bazaar app shell from points.html"""

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/points.html', 'r', encoding='utf-8') as f:
    pts = f.read()

# Extract CSS block (lines 9-304 in points.html)
import re
style_match = re.search(r'(<style>.*?</style>)', pts, re.DOTALL)
style_block = style_match.group(1)

# Extract body shell (header+marquee+sidebar) — lines 306-433
shell_match = re.search(r'(<header class="header">.*?</aside>)', pts, re.DOTALL)
shell_html = shell_match.group(1)

# Remove Points active state, no sidebar item should be active for create_token
shell_html = shell_html.replace('class="nav-item active" href="points.html"', 'class="nav-item" href="points.html"')

# ---- PAGE-SPECIFIC CSS ----
page_css = """
/* ===== CREATE TOKEN WIZARD ===== */

/* Step indicator */
.step-indicator {
  display: flex; align-items: center; justify-content: center;
  gap: 8px; margin-bottom: 28px;
}
.step-dot {
  width: 32px; height: 32px; border-radius: 50%;
  display: grid; place-items: center;
  font-family: var(--font-display); font-size: 13px; font-weight: 700;
  border: 2px solid var(--border-2); color: var(--text-3);
  background: transparent; transition: all 0.2s var(--ease);
}
.step-dot.active {
  border-color: var(--bz-amber-400); color: var(--bz-amber-400);
  background: var(--bz-amber-soft);
}
.step-dot.done {
  border-color: var(--bz-teal-400); color: var(--bz-teal-400);
  background: var(--bz-teal-soft);
}
.step-line {
  width: 48px; height: 2px; background: var(--border-2);
  border-radius: 1px; transition: background 0.2s;
}
.step-line.done { background: var(--bz-teal-400); }

.step-panel { display: none; }
.step-panel.active { display: block; }

/* Wizard card (form container) */
.wiz-card {
  background: var(--surface-1); border: 1px solid var(--border-1);
  border-radius: var(--r-lg); padding: 28px 32px; margin-bottom: 20px;
}
.wiz-title {
  font-family: var(--font-display); font-size: 24px; font-weight: 800;
  color: var(--bz-amber-400); text-align: center; margin-bottom: 6px;
}
.wiz-sub {
  font-size: 13px; color: var(--text-3); text-align: center; margin-bottom: 24px;
}

/* Deployment cost info pill */
.deploy-pill {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 6px 12px; background: var(--surface-2); border: 1px solid var(--border-1);
  border-radius: var(--r-pill); font-size: 12px; color: var(--text-2);
  font-weight: 600; margin-bottom: 20px;
}
.deploy-pill svg { width: 14px; height: 14px; color: var(--bz-amber-400); }
.settings-icon {
  position: absolute; top: 20px; right: 20px;
  width: 20px; height: 20px; color: var(--text-3); cursor: pointer;
}
.settings-icon:hover { color: var(--text-1); }

/* Form fields */
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px; }
.form-group { display: flex; flex-direction: column; margin-bottom: 20px; }
.form-label {
  font-size: 12.5px; font-weight: 600; color: var(--text-2);
  margin-bottom: 6px; letter-spacing: 0.02em;
}
.form-input {
  width: 100%; padding: 10px 14px;
  background: var(--surface-2); border: 1px solid var(--border-1);
  border-radius: var(--r-md); color: var(--text-1);
  font-family: var(--font-body); font-size: 14px;
  transition: border-color 0.15s var(--ease);
}
.form-input:focus { outline: none; border-color: var(--bz-amber-400); }
.form-input::placeholder { color: var(--text-mute); }
textarea.form-input { resize: vertical; min-height: 100px; font-family: inherit; }
.form-input:disabled { opacity: 0.5; cursor: not-allowed; }

/* Upload zone */
.upload-zone {
  border: 2px dashed var(--border-2); border-radius: var(--r-md);
  padding: 40px 20px; text-align: center; cursor: pointer;
  transition: border-color 0.15s; background: var(--surface-2);
}
.upload-zone:hover { border-color: var(--bz-amber-400); }
.upload-zone svg { width: 36px; height: 36px; color: var(--text-3); margin-bottom: 10px; }
.upload-text { font-size: 13px; color: var(--text-2); }
.upload-text span { color: var(--bz-amber-400); font-weight: 600; cursor: pointer; }
.upload-hint { font-size: 11.5px; color: var(--text-mute); margin-top: 6px; }

/* Collapsible */
.collapse-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 16px; background: var(--surface-2); border: 1px solid var(--border-1);
  border-radius: var(--r-md); cursor: pointer; font-size: 13.5px;
  font-weight: 600; color: var(--text-2); transition: all 0.15s;
}
.collapse-header:hover { color: var(--text-1); border-color: var(--border-2); }
.collapse-header svg { width: 16px; height: 16px; transition: transform 0.2s; }
.collapse-header.open svg { transform: rotate(180deg); }
.collapse-body { display: none; padding: 16px; border: 1px solid var(--border-1); border-top: none; border-radius: 0 0 var(--r-md) var(--r-md); }
.collapse-body.open { display: block; }

/* Trust score sections */
.trust-section {
  background: var(--surface-1); border: 1px solid var(--border-1);
  border-radius: var(--r-md); padding: 20px 22px; margin-bottom: 14px;
}
.trust-header {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 16px;
}
.trust-title { font-family: var(--font-display); font-size: 14px; font-weight: 700; color: var(--text-1); }
.trust-badge {
  font-size: 11.5px; font-weight: 600; color: var(--text-3);
  display: flex; align-items: center; gap: 4px;
}

/* Slider */
.slider-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin-bottom: 12px; }
.slider-group label { font-size: 11.5px; color: var(--text-3); font-weight: 600; display: block; margin-bottom: 6px; }
.slider-group input[type="range"] {
  width: 100%; height: 6px; appearance: none; background: var(--border-2);
  border-radius: 3px; outline: none;
}
.slider-group input[type="range"]::-webkit-slider-thumb {
  appearance: none; width: 16px; height: 16px; border-radius: 50%;
  background: var(--bz-amber-400); cursor: pointer; border: 2px solid var(--bg);
}
.slider-val { font-family: var(--font-mono); font-size: 13px; font-weight: 600; color: var(--text-1); text-align: right; }
.sum-row { font-size: 12.5px; color: var(--text-2); margin-bottom: 8px; }
.sum-row .ok { color: var(--bz-teal-400); }

/* Radio + checkbox */
.radio-group { display: flex; gap: 16px; }
.radio-item {
  display: flex; align-items: center; gap: 6px;
  font-size: 13px; color: var(--text-2); cursor: pointer;
}
.radio-item input { accent-color: var(--bz-amber-400); }
.check-item { display: flex; align-items: center; gap: 6px; font-size: 13px; color: var(--text-2); }
.check-item input { accent-color: var(--bz-amber-400); }

/* Pill buttons (LP Lock) */
.pill-group { display: flex; gap: 8px; }
.pill-btn {
  padding: 8px 18px; border-radius: var(--r-pill); border: 1px solid var(--border-2);
  background: transparent; color: var(--text-2); font-size: 13px; font-weight: 600;
  cursor: pointer; font-family: inherit; transition: all 0.15s;
}
.pill-btn:hover { border-color: var(--bz-amber-400); color: var(--bz-amber-400); }
.pill-btn.active { background: var(--bz-amber-400); border-color: var(--bz-amber-400); color: #2a1505; }

/* Bottom action bar */
.wiz-actions {
  display: flex; justify-content: space-between; align-items: center;
  gap: 12px; margin-top: 20px;
}
.wiz-actions-left { display: flex; align-items: center; gap: 12px; }
.check-trust-link {
  font-size: 13px; font-weight: 600; color: var(--bz-amber-400);
  cursor: pointer; background: none; border: none; font-family: inherit;
}
.badge-text { font-size: 12px; color: var(--text-mute); }
.btn-back {
  height: 42px; padding: 0 24px; background: var(--surface-2);
  border: 1px solid var(--border-2); border-radius: var(--r-md);
  color: var(--text-2); font-size: 14px; font-weight: 600;
  cursor: pointer; font-family: inherit; transition: all 0.15s;
}
.btn-back:hover { border-color: var(--text-3); color: var(--text-1); }
.btn-next {
  height: 42px; padding: 0 28px;
  background: linear-gradient(180deg, #FAC775, #EAB552);
  border: none; border-radius: var(--r-md); color: #2a1505;
  font-family: var(--font-display); font-size: 14px; font-weight: 700;
  cursor: pointer; transition: all 0.15s;
}
.btn-next:hover { background: linear-gradient(180deg, #F5DBA8, #FAC775); }
.btn-next:disabled { opacity: 0.4; cursor: not-allowed; }
.btn-next-full { width: 100%; }

/* Finalize: big amount */
.finalize-amount {
  text-align: center; padding: 20px 0;
}
.finalize-amount .big-num {
  font-family: var(--font-mono); font-size: 64px; font-weight: 700;
  color: var(--text-1); letter-spacing: -0.03em;
}
.quick-amounts {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;
  margin-bottom: 16px;
}
.quick-btn {
  height: 42px; background: var(--surface-2); border: 1px solid var(--border-2);
  border-radius: var(--r-md); color: var(--text-2); font-family: var(--font-mono);
  font-size: 14px; font-weight: 600; cursor: pointer; transition: all 0.15s;
}
.quick-btn:hover { border-color: var(--bz-amber-400); color: var(--bz-amber-400); }
.buy-full-btn {
  width: 100%; height: 44px; background: var(--surface-2);
  border: 1px solid var(--border-2); border-radius: var(--r-md);
  color: var(--text-3); font-size: 14px; font-weight: 700;
  cursor: pointer; font-family: inherit; margin-bottom: 16px;
}
.tip-box {
  font-size: 13px; color: var(--text-2); margin-bottom: 16px;
  line-height: 1.5;
}
.tip-box strong { color: var(--text-1); }
"""

# ---- MAIN CONTENT ----
main_html = """
<main class="main">
  <!-- Step Indicator -->
  <div class="step-indicator" id="step-indicator">
    <div class="step-dot active" id="sd-1">1</div>
    <div class="step-line" id="sl-1"></div>
    <div class="step-dot" id="sd-2">2</div>
    <div class="step-line" id="sl-2"></div>
    <div class="step-dot" id="sd-3">3</div>
  </div>

  <!-- ========== STEP 1: Create New Token ========== -->
  <div class="step-panel active" id="step-1">
    <div class="wiz-card" style="position:relative">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px">
        <div class="deploy-pill">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          Deployment Cost Info
        </div>
        <svg class="settings-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      </div>

      <div class="wiz-title">Create New Token</div>
      <div class="wiz-sub">Open your stall. Pitch your meme to the bazaar.</div>

      <div class="form-row">
        <div class="form-group" style="margin-bottom:0">
          <label class="form-label">Token Name</label>
          <input type="text" class="form-input" placeholder="Enter token name">
        </div>
        <div class="form-group" style="margin-bottom:0">
          <label class="form-label">Token Symbol</label>
          <input type="text" class="form-input" placeholder="Enter token symbol">
        </div>
      </div>

      <div class="form-group">
        <label class="form-label">Token Description</label>
        <textarea class="form-input" placeholder="Describe your token"></textarea>
      </div>

      <div class="form-group">
        <label class="form-label">Token Image</label>
        <div class="upload-zone">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
          <div class="upload-text"><span>Upload a file</span> or drag and drop</div>
          <div class="upload-hint">PNG, JPG, GIF up to 1MB</div>
        </div>
      </div>

      <div class="collapse-header" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">
        Social Media Links (Optional)
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="collapse-body">
        <div class="form-group" style="margin-bottom:12px">
          <label class="form-label">Twitter / X</label>
          <input type="text" class="form-input" placeholder="https://twitter.com/...">
        </div>
        <div class="form-group" style="margin-bottom:12px">
          <label class="form-label">Telegram</label>
          <input type="text" class="form-input" placeholder="https://t.me/...">
        </div>
        <div class="form-group" style="margin-bottom:0">
          <label class="form-label">Website</label>
          <input type="text" class="form-input" placeholder="https://...">
        </div>
      </div>

      <div class="wiz-actions" style="justify-content:flex-end;margin-top:24px">
        <button class="btn-next btn-next-full" onclick="goStep(2)">Next</button>
      </div>
    </div>
  </div>

  <!-- ========== STEP 2: Trust Score Setting ========== -->
  <div class="step-panel" id="step-2">
    <div class="wiz-card">
      <div class="wiz-title">Trust Score Setting</div>
      <div class="wiz-sub">Configure tokenomics and security settings</div>

      <!-- 1. Vesting Plan -->
      <div class="trust-section">
        <div class="trust-header">
          <div class="trust-title">1. Vesting Plan — Tokenomics</div>
          <div class="trust-badge">Complete all → 🥉 Bronze</div>
        </div>
        <div class="form-row" style="margin-bottom:16px">
          <div class="form-group" style="margin-bottom:0">
            <label class="form-label">Initial Supply</label>
            <input type="text" class="form-input" value="1000000000">
          </div>
          <div class="form-group" style="margin-bottom:0">
            <label class="form-label">Mint Authority</label>
            <input type="text" class="form-input" placeholder="Wallet address / program id">
          </div>
        </div>
        <div class="slider-row">
          <div class="slider-group">
            <label>Creator % <span class="slider-val" id="sv-creator">40%</span></label>
            <input type="range" min="0" max="100" value="40" oninput="updateSliders(this,'creator')">
          </div>
          <div class="slider-group">
            <label>Community % <span class="slider-val" id="sv-community">40%</span></label>
            <input type="range" min="0" max="100" value="40" oninput="updateSliders(this,'community')">
          </div>
          <div class="slider-group">
            <label>Liquidity % <span class="slider-val" id="sv-liquidity">20%</span></label>
            <input type="range" min="0" max="100" value="20" oninput="updateSliders(this,'liquidity')">
          </div>
        </div>
        <div class="sum-row">Sum: <span class="ok">100%</span> (must be 100%)</div>
        <label class="check-item">
          <input type="checkbox"> Renounce mint authority
        </label>
      </div>

      <!-- 2. Freeze Authority -->
      <div class="trust-section">
        <div class="trust-header">
          <div class="trust-title">2. Freeze Authority</div>
          <div class="trust-badge">Complete → 🥈 Silver (+20% trust)</div>
        </div>
        <div class="radio-group">
          <label class="radio-item"><input type="radio" name="freeze" checked> Enable</label>
          <label class="radio-item"><input type="radio" name="freeze"> Disable</label>
          <svg style="width:16px;height:16px;color:var(--text-3);cursor:help" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
        </div>
      </div>

      <!-- 3. LP Lock -->
      <div class="trust-section">
        <div class="trust-header">
          <div class="trust-title">3. LP Lock</div>
          <div class="trust-badge">Complete → 🥇 Gold</div>
        </div>
        <div class="pill-group">
          <button class="pill-btn active" onclick="selectPill(this)">No lock</button>
          <button class="pill-btn" onclick="selectPill(this)">1 month</button>
          <button class="pill-btn" onclick="selectPill(this)">6 months</button>
        </div>
      </div>

      <div class="wiz-actions">
        <div class="wiz-actions-left">
          <button class="check-trust-link">Check Trust Score</button>
          <span class="badge-text">Badge: —</span>
        </div>
        <div style="display:flex;gap:10px">
          <button class="btn-back" onclick="goStep(1)">Back</button>
          <button class="btn-next" onclick="goStep(3)">Next</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========== STEP 3: Finalize ========== -->
  <div class="step-panel" id="step-3">
    <div class="wiz-card">
      <div class="wiz-title">Finalize</div>

      <div class="tip-box">
        <strong>Tip:</strong><br>
        Optional: Make an initial buy to gain the most from your token
      </div>

      <div class="finalize-amount">
        <div class="big-num">0.00</div>
      </div>

      <div class="quick-amounts">
        <button class="quick-btn">0.1</button>
        <button class="quick-btn">0.5</button>
        <button class="quick-btn">1</button>
        <button class="quick-btn">MAX</button>
      </div>

      <button class="buy-full-btn">BUY</button>

      <div class="wiz-actions">
        <button class="btn-back" onclick="goStep(2)">Back</button>
        <button class="btn-next" onclick="alert('Token created!')">Create Without Buying</button>
      </div>
    </div>
  </div>

</main>
"""

js_content = """
<script>
function goStep(n) {
  document.querySelectorAll('.step-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('step-' + n).classList.add('active');
  for (let i = 1; i <= 3; i++) {
    const dot = document.getElementById('sd-' + i);
    dot.classList.remove('active', 'done');
    if (i < n) dot.classList.add('done');
    else if (i === n) dot.classList.add('active');
  }
  for (let i = 1; i <= 2; i++) {
    const line = document.getElementById('sl-' + i);
    line.classList.toggle('done', i < n);
  }
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function selectPill(btn) {
  btn.parentElement.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
}

function updateSliders(el, name) {
  document.getElementById('sv-' + name).textContent = el.value + '%';
}
</script>
"""

# Assemble
title = '<title>Create Token — Stallspot</title>'
style_block_mod = style_block.replace('</style>', page_css + '\n</style>')

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{title}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
{style_block_mod}
</head>
<body>
{shell_html}
{main_html}
{js_content}
</body>
</html>"""

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/create_token.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ create_token.html generated")
