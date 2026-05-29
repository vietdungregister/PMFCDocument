# Wild theme application - report

## Summary
- Files modified: 18 / 18 in `mockup_final/`
- Files skipped for full visual theming: 1 (`home_full_layout.html`, redirect stub; viewport/lang only)
- Total line delta versus originals: +11,264
- Verification: 18 / 18 passed headless Chromium console/page-error checks
- Screenshots: 36 PNGs captured (`desktop` 1440x900 and `mobile` 390x844 for each file)
- Tooling: `_codex_tools/verify.js`, `_codex_tools/check-scripts.js`, `_codex_tools/final-polish.ps1`

## Files
| File | Phase 1 fix | Phase 3 theme | Mascot added | LA added | Screenshot |
| --- | --- | --- | --- | --- | --- |
| `home_full_layout.html` | n/a | stub only | no | no | `_codex_screenshots/home_full_layout_desktop.png` |
| `token_list_v4.html` | n/a | anchor from gold reference | yes | yes | `_codex_screenshots/token_list_v4_desktop.png` |
| `token_detail.html` | aliases included | yes | yes | no | `_codex_screenshots/token_detail_desktop.png` |
| `trading_panel.html` | aliases included | yes | yes | no | `_codex_screenshots/trading_panel_desktop.png` |
| `creator_dashboard.html` | aliases included | yes | yes | no | `_codex_screenshots/creator_dashboard_desktop.png` |
| `create_token.html` | n/a | yes | yes | no | `_codex_screenshots/create_token_desktop.png` |
| `leaderboard.html` | n/a | yes | yes | no | `_codex_screenshots/leaderboard_desktop.png` |
| `rewards.html` | n/a | yes | yes | no | `_codex_screenshots/rewards_desktop.png` |
| `points.html` | n/a | yes | yes | no | `_codex_screenshots/points_desktop.png` |
| `public_profile.html` | n/a | yes | yes | no | `_codex_screenshots/public_profile_desktop.png` |
| `FR-012b_TokenWar_PredictionMarket.html` | full tokens + aliases included | yes | yes | no | `_codex_screenshots/FR-012b_TokenWar_PredictionMarket_desktop.png` |
| `edit_profile_privacy.html` | n/a | yes | yes | no | `_codex_screenshots/edit_profile_privacy_desktop.png` |
| `my_profile.html` | n/a | yes | yes | no | `_codex_screenshots/my_profile_desktop.png` |
| `referrals.html` | n/a | yes | yes | no | `_codex_screenshots/referrals_desktop.png` |
| `clubs.html` | n/a | yes | yes | no | `_codex_screenshots/clubs_desktop.png` |
| `FR-012_TokenWar.html` | n/a | yes | yes | no | `_codex_screenshots/FR-012_TokenWar_desktop.png` |
| `events.html` | n/a | yes | yes | no | `_codex_screenshots/events_desktop.png` |
| `sidebar_navigation.html` | aliases included | sidebar synced | yes | no | `_codex_screenshots/sidebar_navigation_desktop.png` |

## Verification
- Ran: `node .\_codex_tools\verify.js`
- Result file: `_codex_screenshots/verify-results.json`
- Browser result: all files `OK`, no page errors or console errors.
- Local npm dependency: `puppeteer-core` installed under `_codex_tools/` only. Install required `--strict-ssl=false` because npm registry certificate validation failed in this environment.

## Open questions for the team
No new ambiguity or blocker was found during Phase 6 + 7.

## Known issues / TODOs
1. The rollout keeps each file standalone and uses appended Wild CSS layers rather than extracting shared CSS. This matches the brief but leaves duplication by design.

## Phase 6 + 7 - anchor restore + card polaroidization

### Phase 6 - token_list_v4 truncation fix
- byte-identical copy from gold reference: yes
- source bytes: 145,830
- output bytes: 145,830
- output lines: 3,766
- Live Activity panel present: yes
- mascot + closing tags present: yes
- emoji/domain marker count preserved: 48

### Phase 7 - polaroidize 12 pages
| File | Classes treated | Type assignments |
| --- | --- | --- |
| `FR-012_TokenWar.html` | `.arena-card` | 1x list-card |
| `clubs.html` | `.club-card`, `.pod-card` | 1x list-card, 1x data-frame |
| `events.html` | `.ev-card` | 1x list-card |
| `creator_dashboard.html` | `.metric-card`, `.stat-card` | 2x stat-card |
| `my_profile.html` | `.section-card`, `.stat-card` | 1x list-card, 1x stat-card |
| `public_prof