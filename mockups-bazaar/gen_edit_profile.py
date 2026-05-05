#!/usr/bin/env python3
"""Generate edit_profile_privacy.html — Bazaar themed with app shell"""

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/points.html', 'r', encoding='utf-8') as f:
    pts = f.read()

import re
style_match = re.search(r'(<style>.*?</style>)', pts, re.DOTALL)
style_block = style_match.group(1)
shell_match = re.search(r'(<header class="header">.*?</aside>)', pts, re.DOTALL)
shell_html = shell_match.group(1)
# Set My Profile active
shell_html = shell_html.replace('class="nav-item active" href="points.html"', 'class="nav-item" href="points.html"')
shell_html = shell_html.replace('class="nav-item" href="my_profile.html"', 'class="nav-item active" href="my_profile.html"')

page_css = """
/* ===== EDIT PROFILE ===== */
.edit-card { background: var(--surface-1); border: 1px solid var(--border-1); border-radius: var(--r-lg); padding: 24px 28px; margin-bottom: 20px; }
.edit-title { font-family: var(--font-display); font-size: 14px; font-weight: 700; color: var(--bz-amber-400); margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.05em; }

.avatar-section { display: flex; align-items: center; gap: 18px; margin-bottom: 24px; }
.av-circle { width: 72px; height: 72px; border-radius: var(--r-pill); background: linear-gradient(135deg, var(--bz-amber-400), var(--bz-teal-500)); display: grid; place-items: center; font-family: var(--font-display); font-size: 28px; font-weight: 800; color: #2a1505; flex-shrink: 0; border: 3px solid var(--bz-amber-400); }
.av-actions { display: flex; flex-direction: column; gap: 6px; }
.av-btn { height: 32px; padding: 0 14px; background: var(--surface-2); border: 1px solid var(--border-2); border-radius: var(--r-md); color: var(--text-2); font-size: 12.5px; font-weight: 600; cursor: pointer; font-family: inherit; transition: all 0.15s; }
.av-btn:hover { border-color: var(--bz-amber-400); color: var(--bz-amber-400); }
.av-hint { font-size: 11px; color: var(--text-mute); }

.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.form-group { display: flex; flex-direction: column; margin-bottom: 18px; }
.form-label { font-size: 12.5px; font-weight: 600; color: var(--text-2); margin-bottom: 6px; }
.form-input { width: 100%; padding: 10px 14px; background: var(--surface-2); border: 1px solid var(--border-1); border-radius: var(--r-md); color: var(--text-1); font-family: var(--font-body); font-size: 14px; }
.form-input:focus { outline: none; border-color: var(--bz-amber-400); }
.form-input::placeholder { color: var(--text-mute); }
.form-input:disabled { opacity: 0.45; cursor: not-allowed; }
textarea.form-input { resize: vertical; min-height: 90px; font-family: inherit; }
.form-hint { font-size: 11px; color: var(--text-mute); margin-top: 5px; }
.form-hint.warn { color: var(--bz-crimson); }
.char-counter { font-size: 11px; color: var(--text-mute); text-align: right; margin-top: 4px; }

.toggle-row { display: flex; justify-content: space-between; align-items: center; padding: 14px 16px; background: var(--surface-2); border: 1px solid var(--border-1); border-radius: var(--r-md); margin-bottom: 10px; }
.toggle-label-text { font-size: 14px; color: var(--text-1); font-weight: 500; }
.toggle-sub { font-size: 12px; color: var(--text-3); margin-top: 2px; }
.toggle-switch { position:relative; width:44px; height:24px; display:inline-block; flex-shrink: 0; }
.toggle-switch input { opacity:0; width:0; height:0; }
.toggle-slider { position:absolute; cursor:pointer; top:0; left:0; right:0; bottom:0; background:#374151; border-radius:12px; transition:0.2s; }
.toggle-slider:before { position:absolute; content:""; height:18px; width:18px; left:3px; bottom:3px; background:white; border-radius:50%; transition:0.2s; }
.toggle-switch input:checked + .toggle-slider { background: var(--bz-teal-500); }
.toggle-switch input:checked + .toggle-slider:before { transform:translateX(20px); }

.actions-bar { display: flex; gap: 12px; margin-top: 8px; }
.btn-cancel { flex: 1; height: 44px; background: var(--surface-2); border: 1px solid var(--border-2); border-radius: var(--r-md); color: var(--text-2); font-size: 14px; font-weight: 600; cursor: pointer; font-family: inherit; }
.btn-cancel:hover { border-color: var(--text-3); color: var(--text-1); }
.btn-save { flex: 1; height: 44px; background: linear-gradient(180deg, #FAC775, #EAB552); border: none; border-radius: var(--r-md); color: #2a1505; font-family: var(--font-display); font-size: 14px; font-weight: 700; cursor: pointer; }
.btn-save:hover { background: linear-gradient(180deg, #F5DBA8, #FAC775); }
"""

main_html = """
<main class="main">
  <h1 style="font-family:var(--font-display);font-size:28px;font-weight:800;color:var(--text-1);margin-bottom:4px">Edit profile</h1>
  <p style="font-size:13px;color:var(--text-3);margin-bottom:24px">Update your profile information and privacy settings</p>

  <!-- Avatar -->
  <div class="edit-card">
    <div class="edit-title">Avatar</div>
    <div class="avatar-section">
      <div class="av-circle">N</div>
      <div class="av-actions">
        <button class="av-btn">Change Avatar</button>
        <div class="av-hint">Max 5MB, JPG/PNG/GIF</div>
      </div>
    </div>
  </div>

  <!-- Profile Info -->
  <div class="edit-card">
    <div class="edit-title">Profile Information</div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">Username * (One-time only)</label>
        <input type="text" class="form-input" value="NobleFlame" disabled>
        <div class="form-hint warn">🔒 Cannot be changed after first save</div>
      </div>
      <div class="form-group">
        <label class="form-label">Display Name * (One-time only)</label>
        <input type="text" class="form-input" value="NobleFlame">
        <div class="form-hint warn">🔒 Can only be set once</div>
      </div>
    </div>
    <div class="form-group">
      <label class="form-label">Bio</label>
      <textarea class="form-input" placeholder="Tell us about yourself" maxlength="200">Meme trader at the bazaar. Regular at the stall since Mar 2026.</textarea>
      <div class="char-counter"><span id="charCount">58</span> / 200</div>
    </div>
    <div class="form-grid">
      <div class="form-group">
        <label class="form-label">Twitter / X</label>
        <input type="text" class="form-input" placeholder="https://twitter.com/username">
      </div>
      <div class="form-group">
        <label class="form-label">Telegram</label>
        <input type="text" class="form-input" placeholder="@username or URL">
      </div>
      <div class="form-group">
        <label class="form-label">Email</label>
        <input type="email" class="form-input" placeholder="your@email.com">
      </div>
      <div class="form-group">
        <label class="form-label">Wallet Address</label>
        <input type="text" class="form-input" value="H3XQ...hX" disabled>
        <div class="form-hint">Cannot be changed</div>
      </div>
    </div>
  </div>

  <!-- Privacy -->
  <div class="edit-card">
    <div class="edit-title">Privacy Settings</div>
    <div class="toggle-row">
      <div>
        <div class="toggle-label-text">Public Profile</div>
        <div class="toggle-sub">Anyone can view your profile at the bazaar</div>
      </div>
      <label class="toggle-switch"><input type="checkbox" checked><span class="toggle-slider"></span></label>
    </div>
    <div class="toggle-row">
      <div>
        <div class="toggle-label-text">Show Holdings</div>
        <div class="toggle-sub">Display your token holdings publicly</div>
      </div>
      <label class="toggle-switch"><input type="checkbox" checked><span class="toggle-slider"></span></label>
    </div>
    <div class="toggle-row">
      <div>
        <div class="toggle-label-text">Show Referral Activity</div>
        <div class="toggle-sub">Display your referral stats on your public profile</div>
      </div>
      <label class="toggle-switch"><input type="checkbox"><span class="toggle-slider"></span></label>
    </div>
  </div>

  <!-- Actions -->
  <div class="actions-bar">
    <button class="btn-cancel" onclick="location.href='my_profile.html'">Cancel</button>
    <button class="btn-save">Save Changes</button>
  </div>
</main>
"""

js = """
<script>
const textarea = document.querySelector('textarea');
const charCount = document.getElementById('charCount');
if (textarea && charCount) {
  charCount.textContent = textarea.value.length;
  textarea.addEventListener('input', function() { charCount.textContent = this.value.length; });
}
</script>
"""

style_mod = style_block.replace('</style>', page_css + '\n</style>')
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Edit Profile — Stallspot</title>
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

with open('/Users/duongvietdung/Documents/Projects/PMFCDocument/mockups-bazaar/edit_profile_privacy.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ edit_profile_privacy.html generated")
