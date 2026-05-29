$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)

$extra = @'

/* === Codex Wild final polish === */
body {
  display: block !important;
  justify-content: initial !important;
  align-items: initial !important;
  padding: 0 !important;
  overflow-x: hidden;
}
.wiz-card, .edit-card, .settings-card, .reward-card, .reward-panel,
.referral-hero, .ref-code-card, .ev-card, .pod-card, .battle-side,
.war-card, .market-card, .creator-card, .token-row-card, .position-card {
  background: var(--w-paper) !important;
  color: var(--w-ink) !important;
  border: 0 !important;
  border-radius: var(--r-lg) !important;
  box-shadow: 0 14px 28px -8px rgba(0,0,0,0.55), 0 4px 8px rgba(0,0,0,0.3) !important;
  position: relative;
  overflow: visible;
}
.wiz-card::before, .edit-card::before, .settings-card::before,
.referral-hero::before, .ref-code-card::before, .ev-card::before,
.pod-card::before, .battle-side::before, .war-card::before, .market-card::before {
  content: "";
  position: absolute;
  top: -10px;
  left: 36px;
  width: 86px;
  height: 18px;
  background: var(--w-tape-y);
  transform: rotate(-2deg);
  border-radius: 3px;
}
.wiz-card *, .edit-card *, .settings-card *, .reward-card *, .reward-panel *,
.referral-hero *, .ref-code-card *, .ev-card *, .pod-card *, .battle-side *,
.war-card *, .market-card *, .creator-card *, .token-row-card *, .position-card * {
  color: inherit;
}
.step-title, .ev-title, .pod-name, .reward-name, .ref-code,
.battle-name, .market-title {
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
  font-weight: 900 !important;
  color: var(--w-ink) !important;
}
.btn-next, .btn-save, .btn-claim, .btn-bet, .btn-create, .buy-full-btn,
.execute-btn, .ev-btn, .btn-cancel, .btn-back {
  border-radius: var(--r-pill) !important;
  font-family: var(--font-disp-it) !important;
  font-style: italic !important;
  font-weight: 900 !important;
}
.trading-panel {
  width: min(420px, calc(100vw - 48px)) !important;
  margin: calc(var(--marquee-h) + 48px) auto 64px !important;
  background: var(--w-paper) !important;
  color: var(--w-ink) !important;
  border: 0 !important;
  border-radius: var(--r-lg) !important;
  box-shadow: 0 14px 28px -8px rgba(0,0,0,0.55), 0 4px 8px rgba(0,0,0,0.3) !important;
}
.trading-panel::before {
  content: "";
  position: absolute;
  top: -10px;
  left: 42px;
  width: 86px;
  height: 18px;
  background: var(--w-tape-y);
  transform: rotate(-2deg);
}
.trading-panel *, .primary-toggle *, .trade-section * { color: inherit; }
.trading-panel .preview-panel,
.trading-panel .settings-header,
.trading-panel .settings-content,
.trading-panel .input-wrapper,
.trading-panel .quick-btn,
.trading-panel .setting-btn {
  background: var(--w-cream) !important;
  color: var(--w-ink) !important;
  border-color: rgba(42,21,5,0.25) !important;
}
.trading-panel .primary-btn.buy,
.trading-panel .execute-btn.buy {
  background: linear-gradient(180deg, var(--sp-teal-300), var(--sp-forest-500)) !important;
  color: #06120c !important;
}
.trading-panel .primary-btn.sell,
.trading-panel .execute-btn.sell {
  background: linear-gradient(180deg, #ef8a84, var(--sp-crimson)) !important;
  color: #260705 !important;
}
.trading-panel .risk-card {
  background: var(--surface-1) !important;
  color: var(--text-1) !important;
  border-color: var(--sp-peach-400) !important;
}
.bz-bar {
  position: fixed !important;
  top: var(--marquee-h) !important;
  left: 12px !important;
  z-index: 1001 !important;
  background: var(--surface-2) !important;
  color: var(--text-1) !important;
  border: 1px solid var(--border-1) !important;
}
.badge-text::after { content: " Bronze"; }
/* === end Codex Wild final polish === */
'@

function Insert-BeforeLastStyleClose([string]$html, [string]$insert) {
  $idx = $html.LastIndexOf("</style>", [StringComparison]::OrdinalIgnoreCase)
  if ($idx -lt 0) { return $html }
  return $html.Insert($idx, $insert)
}

Get-ChildItem -LiteralPath $Root -Filter *.html | Where-Object { $_.Name -ne "home_full_layout.html" } | ForEach-Object {
  $html = Get-Content -Raw -LiteralPath $_.FullName
  if ($html -notmatch 'Codex Wild final polish') {
    $html = Insert-BeforeLastStyleClose $html $extra
  }
  Set-Content -LiteralPath $_.FullName -Value $html -Encoding UTF8
}

$trading = Join-Path $Root "trading_panel.html"
$html = Get-Content -Raw -LiteralPath $trading
$html = $html -replace '<span class="bz-back-arrow">[^<]*?/span>', '<span class="bz-back-arrow">&larr;</span>'
$html = $html -replace '<span>[^<]*?/span>', '<span>&rsaquo;</span>'
$html = $html -replace '<button class="swap-btn">[^<]*?/button>', '<button class="swap-btn">&darr;</button>'
$html = $html -replace '<span class="settings-icon">[^<]*?/span>', '<span class="settings-icon">Settings</span>'
Set-Content -LiteralPath $trading -Value $html -Encoding UTF8

$create = Join-Path $Root "create_token.html"
$html = Get-Content -Raw -LiteralPath $create
$html = $html -replace '<span class="badge-text">Badge: [^<]*?/span>', '<span class="badge-text">Badge:</span>'
Set-Content -LiteralPath $create -Value $html -Encoding UTF8

Write-Host "Applied final polish CSS and visible malformed tag fixes."
