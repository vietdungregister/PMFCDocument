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
| `public_profile.html` | `.section-card`, `.stat-card` | 1x list-card, 1x stat-card |
| `token_detail.html` | `.token-info-card`, `.trade-card`, `.chart-card`, `.tabs-card`, `.trust-card` | 3x list-card, 2x data-frame |
| `referrals.html` | `.link-card`, `.stat-card`, `.table-card` | 1x list-card, 1x stat-card, 1x table-card |
| `rewards.html` | `.history-card`, `.reels-card` | 1x table-card, 1x data-frame |
| `points.html` | `.history-card`, `.rank-card` | 1x table-card, 1x stat-card |
| `leaderboard.html` | `.lb-card-head` | 1x data-frame |
| `edit_profile_privacy.html` | `.edit-card` | 1x list-card |

### Phase 6 + 7 verification
- Phase 6 byte comparison: byte-identical to `../Sửa giao diện html/token_list_v4_wild.html`
- Phase 6 structural checks: `live-activity` 1, `la-feed` 1, `la-item` 9, `</body>` 1, `</html>` 1
- Phase 7 selector checks: list/stat/data-frame selectors contain `var(--w-paper)`; table-card selectors use the specified flat dark trim recipe
- Encoding checks: emoji/domain marker counts stayed at or above pre-edit counts for every written file
- Browser verification: `node .\_codex_tools\verify.js` passed 18 / 18 files and refreshed `_codex_screenshots/`

## Phase 8 + 9 + 10 - sidebar canon, tier system, LA on detail

### Phase 8 - sidebar consistency
- Extracted the canonical sidebar block from `token_list_v4.html`, including the sticker-dock base plus cream-pill v0.4, v0.5, v0.6, and v0.8 layers.
- Wrote the extracted block to `_codex_tools/sidebar-block.css`.
- Injected the canonical sidebar CSS into 16 other pages, excluding `token_list_v4.html` and `home_full_layout.html`.
- Added a final `!important` radial-background override inside the Phase 8 block so it wins over the earlier Codex linear-gradient `!important` sidebar rule.
- Computed background verification: all pages with a `.sidebar` now report the radial-gradient anchor signature instead of the old dark linear-gradient.

### Phase 9 - tier system
- Removed the Phase 7 polaroid CSS block from all pages.
- Re-applied per tier:

| Page | Tier | Cards touched |
| --- | --- | --- |
| `token_list_v4.html` | T1 | `.token-card` retained from anchor; no reapply |
| `token_detail.html` | T1 + data-frame | `.token-info-card`, `.trade-card`, `.trust-card`, `.chart-card`, `.tabs-card` |
| `clubs.html` | T2 | `.club-card`, `.pod-card` |
| `events.html` | T2 | `.ev-card` |
| `leaderboard.html` | T2 | `.lb-card-head` |
| `rewards.html` | T2 | `.history-card`, `.reels-card` |
| `points.html` | T2 | `.history-card`, `.rank-card` |
| `my_profile.html` | T3 | `.profile-hero`, `.section-card:first-of-type`, `.section-card:not(:first-of-type)`, `.stat-card` |
| `public_profile.html` | T3 | `.profile-hero`, `.section-card:first-of-type`, `.section-card:not(:first-of-type)`, `.stat-card` |
| `referrals.html` | T3 | `.link-card`, `.stat-card`, `.table-card` |
| `edit_profile_privacy.html` | T3 | `.edit-card:first-of-type`, `.edit-card:not(:first-of-type)` |
| `create_token.html` | T4 | verified only; no Phase 9 card changes |
| `trading_panel.html` | T4 | verified only; no Phase 9 card changes |
| `creator_dashboard.html` | T5 | `.metric-card`, `.stat-card` |
| `FR-012_TokenWar.html` | T6 | doc typography, `.arena-card` dark reset |
| `FR-012b_TokenWar_PredictionMarket.html` | T6 | doc typography |
| `sidebar_navigation.html` | n/a | Phase 8 sidebar only |
| `home_full_layout.html` | n/a | skipped redirect stub |

### Phase 10 - LA on token_detail
- Copied the Live Activity panel structure from `token_list_v4.html` into `token_detail.html`.
- Filtered static feed token chips and mock pool token values to `MOON`.
- Header updated: `Live · MOON token`.
- LA scope verified: only `token_list_v4.html` and `token_detail.html` contain `<aside class="live-activity">`.

### Phase 8 + 9 + 10 verification
- `Wild Phase 7` markers: none remain in `mockup_final/*.html`.
- Sidebar computed style: no rendered `.sidebar` reports the old `linear-gradient(rgb(19, 31, 24), rgb(14, 26, 19))` background.
- Encoding checks: marker counts stayed at or above pre-edit counts after each write.
- Browser verification: `node .\_codex_tools\verify.js` passed 18 / 18 files and refreshed `_codex_screenshots/`.

## Resolved questions
- Sidebar variant: cream-pill gold reference sidebar applied consistently by CSS override.
- Tier system: applied as T1, T2, T3, T4, T5, and T6 per `WILD_PHASE3.md`.
- LA scope: `token_list_v4.html` plus contextual `token_detail.html` only.

## Remaining open
- `creator_dashboard.html` and `trading_panel.html` do not currently include a `.sidebar` element in their HTML. Phase 8 injected the canonical CSS into both files, but rendering an actual sidebar there would require adding sidebar markup, which was outside this CSS-focused fix scope.
- Some non-anchor pages carry legacy multiple `.nav-item.active` classes in the existing sidebar markup. Phase 8 normalized the canonical CSS and background, but did not edit navigation class attributes because the brief prohibited class/id/data-attribute churn.
