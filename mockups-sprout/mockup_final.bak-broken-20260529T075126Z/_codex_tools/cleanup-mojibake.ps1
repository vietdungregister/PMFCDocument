$ErrorActionPreference = 'Stop'
$root = 'C:\Users\duongvietdung\Documents\PMFCDocument\mockups-sprout\mockup_final'
$files = Get-ChildItem -LiteralPath $root -Filter *.html
foreach ($file in $files) {
  $html = Get-Content -Raw -LiteralPath $file.FullName

  # Fix malformed tags first.
  $html = $html -replace '窶・/td>', '-</td>'
  $html = $html -replace '窶・/span>', '</span>'
  $html = $html -replace '・/span>', '</span>'
  $html = $html -replace '竏・/button>', '-</button>'
  $html = $html -replace '竍・/button>', '&darr;</button>'

  # Fix signed numeric changes before generic replacements.
  $html = $html -replace '(class="[^"]*(?:price-up|up|positive)[^"]*"[^>]*>)竊・', '$1+'
  $html = $html -replace '(class="[^"]*(?:price-down|down|negative)[^"]*"[^>]*>)竊・', '$1-'

  # Common mojibake punctuation and UI separators.
  $html = $html -replace '窶｢', '&bull;'
  $html = $html -replace '窶・', ' - '
  $html = $html -replace '窶ｦ', '...'
  $html = $html -replace 'ﾂｷ', '*'
  $html = $html -replace 'ﾂｩ', '&copy;'
  $html = $html -replace '竊・', '+'
  $html = $html -replace '竍・', '&rsaquo;'
  $html = $html -replace '笆ｼ', '&rsaquo;'
  $html = $html -replace '筴・', 'Copy'
  $html = $html -replace '笨ｨ', '*'
  $html = $html -replace '笘・', '#'
  $html = $html -replace '笘・', '*'
  $html = $html -replace '笞｡', 'WR'
  $html = $html -replace '笞呻ｸ・', 'Settings'

  # Replace broken emoji placeholders with plain text where they are user-visible.
  $html = $html -replace '[\u0080-\uFFFF]?', ''
  $html = $html -replace '筐・', 'Home'
  $html = $html -replace '竏・', '-'

  # Normalize known labels after stripping glyphs.
  $html = $html -replace 'Search the garden\s*-\s*tokens, creators, addresses\.\.\.', 'Search the garden - tokens, creators, addresses...'
  $html = $html -replace '7xK9\.\.\.mP3q', '7xK9...mP3q'
  $html = $html -replace 'Sprout \* tap for tips', 'Sprout * tap for tips'
  $html = $html -replace 'Seed \* ', 'Seed * '
  $html = $html -replace 'Sprout \* ', 'Sprout * '

  Set-Content -LiteralPath $file.FullName -Value $html -Encoding UTF8
}
