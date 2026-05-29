$ErrorActionPreference = 'Stop'
$root = 'C:\Users\duongvietdung\Documents\PMFCDocument\mockups-sprout\mockup_final'

$file = Join-Path $root 'FR-012b_TokenWar_PredictionMarket.html'
$html = Get-Content -Raw -LiteralPath $file
$cleanSpec = @"
<div id="tab-spec" class="tab-content active">
<div class="spec">
  <div class="tag">Option B - Prediction Market</div>
  <h1>FR-012b: Meme Bazaar Showdown</h1>
  <p class="subtitle">Internal BA note for the prediction-market variant.</p>

  <hr class="divider">

  <h2>Problem</h2>
  <p>The pari-mutuel model in FR-012 does not clearly answer: <strong>"If I enter now, how much can I win?"</strong> Odds keep changing until the war ends. The prediction-market model makes payout expectations clearer at entry.</p>

  <hr class="divider">

  <h2>Core mechanism</h2>
  <p>Users buy shares for a specific outcome. Each share has a market price that changes with supply and demand, but winning shares always pay <strong>1 SOL per share</strong> at settlement.</p>

  <pre>War: DOGE vs PEPE

Current market:
  DOGE wins share: 0.58 SOL
  PEPE wins share: 0.42 SOL

User buys 2 PEPE wins shares @ 0.42 SOL/share:
  Cost: 0.84 SOL
  If PEPE wins: receives 2 SOL, profit 1.16 SOL (2.38x)
  If DOGE wins: receives 0 SOL, loses 0.84 SOL

The final payout is known at purchase time.</pre>

  <div class="highlight">Later users may move PEPE share price from 0.42 to 0.70 SOL, but existing shares still settle at 1 SOL/share if PEPE wins.</div>

  <hr class="divider">

  <h2>How share price is set</h2>
  <p>No admin sets the price manually. Price forms through an AMM, similar to a bonding curve. The two outcome shares roughly sum to 1 SOL.</p>

  <pre>Initial pool: 50 / 50
  DOGE wins: 0.50 SOL
  PEPE wins: 0.50 SOL

If users buy DOGE wins:
  DOGE wins price rises to 0.65 SOL
  PEPE wins price falls to 0.35 SOL</pre>

  <hr class="divider">

  <h2>Platform revenue and risk</h2>
  <pre>Every share buy/sell charges a platform fee, for example 2%.

Example:
  Total share trading volume in one war: 200 SOL
  Platform fee at 2%: 4 SOL

The platform does not need to know the winner in advance.
Winners are paid from the market pool.</pre>

  <div class="vs-box">
    <div class="vs-col">
      <h4>Pari-mutuel (FR-012)</h4>
      <p>Platform takes rake from the pool. Low platform risk, but users do not know their exact payout when entering.</p>
    </div>
    <div class="vs-col">
      <h4>Prediction Market (FR-012b)</h4>
      <p>Platform takes trading fees. Users know expected settlement payout immediately after buying shares.</p>
    </div>
  </div>

  <hr class="divider">

  <h2>Open decisions</h2>
  <ul>
    <li>Initial liquidity per war.</li>
    <li>Final fee rate.</li>
    <li>Whether users can sell shares before settlement.</li>
    <li>War duration: 1h, 6h, or 24h.</li>
  </ul>
</div>
</div>
"@
$html = [regex]::Replace($html, '<div id="tab-spec" class="tab-content active">[\s\S]*?<!-- .*?TAB: LIST -->', $cleanSpec + "`r`n<!-- TAB: LIST -->", [System.Text.RegularExpressions.RegexOptions]::Singleline)
$html = $html -replace '笞費ｸ・Wars List', 'Wars List'
$html = $html -replace '笨・Ended', 'Ended'
Set-Content -LiteralPath $file -Value $html -Encoding UTF8

Get-ChildItem -LiteralPath $root -Filter *.html | ForEach-Object {
  $html = Get-Content -Raw -LiteralPath $_.FullName
  $html = $html -replace 'ﾂｧ', 'section '
  $html = $html -replace '<span class="bz-back-arrow">竊</span>', '<span class="bz-back-arrow">&larr;</span>'
  $html = $html -replace '<span>窶ｺ</span>', '<span>&rsaquo;</span>'
  $html = $html -replace 'ﾃ・', 'x'
  $html = $html -replace '筴</span>', 'Copy</span>'
  $html = $html -replace 'v盻嬖 ring \(Moon Token = Gold 64\)\. Trade panel Buy/Sell m蘯ｷc ﾄ黛ｻ杵h Buy active\.', 'visible ring (Moon Token = Gold 64). Trade panel Buy/Sell defaults to Buy active.'
  $html = $html -replace '笨ｿ', '*'
  $html = $html -replace 'coral竊恥ink', 'coral-pink'
  Set-Content -LiteralPath $_.FullName -Value $html -Encoding UTF8
}
