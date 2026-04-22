# PUMPFUN CLONE - TEST PLAN

**Document Version:** 1.0  
**Created Date:** February 4, 2026
**Last Updated:** February 4, 2026  
**Author:** QA Team
## 1. GIỚI THIỆU
Tài liệu này xác định kế hoạch kiểm thử tổng thể cho dự án Pumpfun Clone, bao gồm các mục tiêu, phạm vi, nguồn lực và lịch trình kiểm thử để đảm bảo chất lượng hệ thống trước khi triển khai.

## 2. PHẠM VI TESTING
### 2.1. Trong phạm vi (In-Scope)
*   **Smart Contracts:** Kiểm tra logic Bonding Curve, cơ chế tạo token, mua/bán và rút tiền.
*   **Frontend:** Kiểm tra giao diện người dùng, biểu đồ thời gian thực, và tích hợp ví (Phantom/Solflare).
*   **Backend:** Kiểm tra API đồng bộ hóa dữ liệu từ blockchain, metadata và hệ

---

## 📋 MỤC LỤC

1. [Giới thiệu](#1-giới-thiệu)
2. [Phạm vi Testing](#2-phạm-vi-testing)
3. [Chiến lược Testing](#3-chiến-lược-testing)
4. [Môi trường Testing](#4-môi-trường-testing)
5. [Test Cases theo Module](#5-test-cases-theo-module)
6. [Non-Functional Testing](#6-non-functional-testing)
7. [Exit Criteria](#7-exit-criteria)
8. [Defect Management](#8-defect-management)
9. [Test Deliverables](#9-test-deliverables)

---

## 1. GIỚI THIỆU

### 1.1 Mục đích
Tài liệu này mô tả kế hoạch kiểm thử cho hệ thống **PumpFun Clone** - một nền tảng giao dịch meme token trên blockchain Solana.

### 1.2 Tổng quan hệ thống
Hệ thống bao gồm 11 Functional Requirements (FR):

| FR ID | Tên Module | Độ ưu tiên |
|-------|-----------|------------|
| FR-001 | Token List | High |
| FR-002 | Token Detail | High |
| FR-003 | Buy/Sell Trading | Critical |
| FR-004 | My Profile | Medium |
| FR-005 | Public Profile | Medium |
| FR-006 | Creator Dashboard | Medium |
| FR-007 | Create Token | High |
| FR-008 | Leaderboard | Low |
| FR-009 | Rewards & Games | Low |
| FR-010 | Referrals | Medium |
| FR-011 | Points & Ranking | Low |

### 1.3 Tài liệu tham chiếu
- Function Requirements.md
- FR-001 đến FR-011 documents
- HTML Mockups

---

## 2. PHẠM VI TESTING

### 2.1 Trong phạm vi (In Scope)

#### Functional Testing
- Tất cả 11 Functional Requirements
- User flows chính (Login, Trading, Token Creation)
- Integration giữa các modules
- Real-time data updates
- Wallet connection flows

#### Non-Functional Testing
- Performance testing
- Security testing
- Usability testing
- Compatibility testing (browsers, devices)
- Stress testing cho trading features

### 2.2 Ngoài phạm vi (Out of Scope)
- Smart contract auditing (sẽ thực hiện riêng)
- Penetration testing chuyên sâu
- Load testing > 10,000 concurrent users
- Mobile native app testing

---

## 3. CHIẾN LƯỢC TESTING

### 3.1 Test Levels

```
┌─────────────────────────────────────────────┐
│           System Testing (E2E)               │
├─────────────────────────────────────────────┤
│          Integration Testing                 │
├─────────────────────────────────────────────┤
│            Unit Testing                      │
└─────────────────────────────────────────────┘
```

### 3.2 Test Types

| Test Type | Mô tả | Coverage |
|-----------|-------|----------|
| Smoke Test | Kiểm tra chức năng cơ bản | 100% critical paths |
| Regression Test | Đảm bảo không ảnh hưởng features cũ | 80% test cases |
| Sanity Test | Quick validation sau mỗi build | Core features |
| UAT | User Acceptance Testing | All user stories |

### 3.3 Test Approach Matrix

| Module | Manual | Automated | Priority |
|--------|--------|-----------|----------|
| FR-001 Token List | ✓ | ✓ | High |
| FR-002 Token Detail | ✓ | ✓ | High |
| FR-003 Buy/Sell | ✓ | ✓ | Critical |
| FR-004 My Profile | ✓ | ○ | Medium |
| FR-005 Public Profile | ✓ | ○ | Medium |
| FR-006 Creator Dashboard | ✓ | ○ | Medium |
| FR-007 Create Token | ✓ | ✓ | High |
| FR-008 Leaderboard | ✓ | ○ | Low |
| FR-009 Rewards | ✓ | ○ | Low |
| FR-010 Referrals | ✓ | ○ | Medium |
| FR-011 Points | ✓ | ○ | Low |

**Legend:** ✓ = Full coverage, ○ = Partial coverage

---

## 4. MÔI TRƯỜNG TESTING

### 4.1 Environments

| Environment | Purpose | Data |
|-------------|---------|------|
| DEV | Developer testing | Mock data |
| QA/Staging | QA testing | Test data |
| UAT | User acceptance | Anonymized production data |
| Production | Post-release monitoring | Real data |

### 4.2 Browser Compatibility

| Browser | Version | Priority |
|---------|---------|----------|
| Chrome | Latest 2 versions | Must Pass |
| Firefox | Latest 2 versions | Must Pass |
| Safari | Latest 2 versions | Should Pass |
| Edge | Latest 2 versions | Should Pass |

### 4.3 Device Testing

| Device Type | Resolution | Priority |
|-------------|------------|----------|
| Desktop Large | 1920x1080 | Must Pass |
| Desktop Medium | 1440x900 | Must Pass |
| Tablet | 768x1024 | Should Pass |
| Mobile | 375x667 | Nice to Have |

### 4.4 Test Tools

| Tool | Purpose |
|------|---------|
| Playwright/Cypress | E2E Automation |
| Jest | Unit Testing |
| Postman | API Testing |
| JMeter | Performance Testing |
| Jira | Defect Tracking |

---

## 5. TEST CASES THEO MODULE

---

### 5.1 FR-001: Token List

#### 5.1.1 Tab Navigation Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TL-001 | Verify 5 tabs display | 1. Navigate to Token List page | 5 tabs visible: Discover, Trending, Top Volume, Graduated, Favorite | High |
| TL-002 | Verify Discover is default tab | 1. Navigate to home page first time | Discover tab is active | High |
| TL-003 | Switch tabs | 1. Click each tab | Content updates, pagination resets to page 1 | High |
| TL-004 | Verify tab filter retention | 1. Apply filters 2. Switch tab | Filters và search query giữ nguyên | Medium |
| TL-005 | Verify Favorite tab empty state | 1. Login với new user 2. Click Favorite tab | "Bạn chưa có token yêu thích nào" message | Medium |
| TL-006 | Verify Graduated tab empty state | 1. Navigate when no graduated tokens | "Chưa có token nào đạt graduation" message | Medium |

#### 5.1.2 DiscoverScore Algorithm Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TL-007 | Verify DiscoverScore calculation | 1. Check token with known metrics | Score = 0.40×Trending + 0.20×Liquidity + 0.20×Holders + 0.10×Trust + 0.10×Recency | High |
| TL-008 | Verify descending order | 1. Load Discover tab | Tokens sorted by DiscoverScore descending | High |
| TL-009 | Verify score recalculation | 1. Wait 10 minutes 2. Check scores | Scores update without interrupting scroll | Medium |

#### 5.1.3 Token Card Display Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TL-010 | Verify token card elements | 1. Inspect any token card | Avatar, Name, Symbol, Statement, Price, MC, Volume, Change%, Badges, Favorite button visible | High |
| TL-011 | Verify price format < $0.01 | 1. Check token with price $0.000123 | Display: $0.000123 (6 decimals) | Medium |
| TL-012 | Verify price format $0.01-$1 | 1. Check token with price $0.1234 | Display: $0.1234 (4 decimals) | Medium |
| TL-013 | Verify price format > $1 | 1. Check token with price $12.345 | Display: $12.34 (2 decimals) | Medium |
| TL-014 | Verify market cap K format | 1. Check token with MC $12,500 | Display: $12.5K | Medium |
| TL-015 | Verify market cap M format | 1. Check token with MC $1,200,000 | Display: $1.2M | Medium |
| TL-016 | Verify 24h change colors | 1. Check positive/negative/zero tokens | Green for +, Red for -, Gray for 0 | Medium |
| TL-017 | Verify favorite toggle | 1. Login 2. Click favorite button | Star fills/unfills, syncs with Favorite tab | High |
| TL-018 | Verify card click navigation | 1. Click on token card (not favorite) | Navigate to Token Detail page | High |
| TL-019 | Verify card hover effect | 1. Hover over token card | Shadow hoặc scale effect visible | Low |

#### 5.1.4 Filter Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TL-020 | Verify NSFW filter default | 1. Check NSFW toggle | Default: OFF (ẩn NSFW content) | High |
| TL-021 | Toggle NSFW filter | 1. Enable NSFW filter | NSFW tokens appear in list | Medium |
| TL-022 | Verify Market Cap filter | 1. Set MC range $10K-$100K | Only tokens within range displayed | High |
| TL-023 | Verify Volume filter | 1. Set Volume range | Only tokens within range displayed | High |
| TL-024 | Verify Trust Level filter OR logic | 1. Select LP Locked + Audited | Tokens matching ANY criteria shown | Medium |
| TL-025 | Verify combined filters AND logic | 1. Apply multiple filter types | Filters combine with AND logic | High |
| TL-026 | Verify active filters badge | 1. Apply 3 filters | Badge shows "3" | Medium |
| TL-027 | Verify Reset Filters | 1. Apply filters 2. Click Reset | All filters cleared, list refreshed | Medium |

#### 5.1.5 Sort Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TL-028 | Verify sort panel opens | 1. Click Sort button | Sort panel opens with options | Medium |
| TL-029 | Sort by Price ascending | 1. Select Price 2. Set ascending | Tokens sorted low to high | Medium |
| TL-030 | Sort by Market Cap descending | 1. Select MC 2. Set descending | Tokens sorted high to low | Medium |
| TL-031 | Verify sort overrides tab | 1. Apply sort on any tab | Tab's default sorting overridden | Medium |

#### 5.1.6 Search Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TL-032 | Search by token name | 1. Enter name 2. Press Enter | Matching tokens displayed | High |
| TL-033 | Search by symbol | 1. Enter symbol 2. Press Enter | Token with symbol displayed | High |
| TL-034 | Search with special characters | 1. Enter "token$" 2. Press Enter | Handles gracefully, no error | Medium |
| TL-035 | Search no results | 1. Enter gibberish 2. Press Enter | "No results" message | Medium |
| TL-036 | Search with filters | 1. Apply filter 2. Search | Search respects active filters | Medium |

---

### 5.2 FR-002: Token Detail

#### 5.2.1 Token Header Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TD-001 | Verify token metadata display | 1. Navigate to token detail | Avatar, Name, Symbol, Creator, Description visible | High |
| TD-002 | Verify creator link navigation | 1. Click creator name | Navigate to Public Profile (respect privacy) | High |
| TD-003 | Verify favorite toggle | 1. Click favorite button | Toggle state, syncs with list | Medium |
| TD-004 | Verify social links | 1. Click social links | Opens in new tab | Medium |

#### 5.2.2 Price Chart Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TD-005 | Verify chart renders | 1. Load token detail | Chart displays with data | High |
| TD-006 | Verify timeframe switch | 1. Click different timeframes | Chart updates accordingly | Medium |
| TD-007 | Verify real-time updates | 1. Monitor chart 10 seconds | Price updates visible | High |

#### 5.2.3 Market Metrics Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TD-008 | Verify all metrics display | 1. Check metrics section | Price, 24h Change, MC, Volume, Holders, Liquidity, Supply visible | High |
| TD-009 | Verify metrics update frequency | 1. Monitor Price (10s), MC (30s), Volume (1m), Holders (5m) | Updates at correct intervals | Medium |
| TD-010 | Verify price animation | 1. Wait for price change | Pulse animation visible | Low |
| TD-011 | Verify graduation progress | 1. Check liquidity section | Progress bar toward $69K MC accurate | Medium |

#### 5.2.4 Community Chat Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TD-012 | Verify chat loads | 1. View chat section | Previous messages load | High |
| TD-013 | Send message (logged in) | 1. Login 2. Type message 3. Enter | Message appears in chat | High |
| TD-014 | Send message (not logged in) | 1. Logout 2. Try to send | Login prompt/disabled | High |
| TD-015 | Verify max message length | 1. Try to send 201+ chars | Limited to 200 characters | Medium |
| TD-016 | Verify username click | 1. Click username in chat | Navigate to Public Profile | Medium |
| TD-017 | Verify real-time chat | 1. Have 2 users 2. One sends message | Other sees within 500ms | High |
| TD-018 | Verify chat history scroll | 1. Scroll up in chat | Infinite scroll loads history | Medium |
| TD-019 | Verify profanity filter | 1. Send message with profanity | Filtered or blocked | Medium |

#### 5.2.5 Holders List Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TD-020 | Verify top 100 holders display | 1. View holders section | Rank, Avatar, Username/Address, Balance, % of supply | High |
| TD-021 | Verify holder badges | 1. Check for 👑🐋💎 badges | Creator, Whale (>5%), Diamond Hands (>30 days) displayed correctly | Medium |
| TD-022 | Verify top 10 concentration | 1. Check summary | Percentage accurate, color coded (Green/Yellow/Red) | Medium |
| TD-023 | Verify holder click | 1. Click holder name | Navigate to Public Profile (respect privacy) | Medium |

#### 5.2.6 Transaction History Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| TD-024 | Verify 50 transactions display | 1. View transaction section | 50 most recent shown | High |
| TD-025 | Verify transaction type colors | 1. Check BUY/SELL | Green for BUY, Red for SELL | Medium |
| TD-026 | Verify TX hash link | 1. Click TX hash | Opens Solana Explorer in new tab | Medium |
| TD-027 | Verify whale indicator | 1. Check large transaction | 🐋 icon for >5% of 24h volume | Medium |
| TD-028 | Verify trader click | 1. Click trader name | Navigate to Public Profile | Medium |

#### 5.2.7 Trading Panel Tests
*(See FR-003 for detailed trading tests)*

---

### 5.3 FR-003: Buy/Sell Trading

#### 5.3.1 Panel Layout Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| BS-001 | Verify panel visibility | 1. Load token detail | Trading panel fixed on right | High |
| BS-002 | Verify BUY/SELL toggle | 1. Click BUY 2. Click SELL | Toggle works, form clears | High |
| BS-003 | Verify Market/Limit toggle | 1. Toggle between modes | Form updates accordingly | High |
| BS-004 | Verify current price display | 1. Check panel header | Token name, symbol, real-time price | High |
| BS-005 | Verify panel scrolling | 1. Scroll page down | Panel stays fixed/visible | Medium |

#### 5.3.2 Market Order - BUY Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| BS-006 | Verify amount input (SOL mode) | 1. Enter SOL amount | Valid input accepted | High |
| BS-007 | Verify quick buttons (SOL mode) | 1. Click 0.1/0.5/1/MAX | Amount fills correctly | Medium |
| BS-008 | Verify currency switch | 1. Click SOL ⇄ TOKEN | Input mode changes | Medium |
| BS-009 | Verify quick buttons (Token mode) | 1. Switch to Token 2. Click 25%/50%/75%/MAX | Percentage of balance fills | Medium |
| BS-010 | Verify "You Receive" calculation | 1. Enter amount | Estimated tokens calculated | High |
| BS-011 | Verify balance display | 1. Connect wallet 2. Check balance | SOL balance shown, updates real-time | High |
| BS-012 | Verify fees section expand | 1. Click fees chevron | Network fee, Anti-MEV, Priority fee shown | Medium |
| BS-013 | Verify BUY button enabled | 1. Enter valid amount | "Buy X TOKEN" button enabled | High |
| BS-014 | Verify BUY button disabled | 1. Enter invalid/0 amount | Button disabled | High |

#### 5.3.3 Market Order - SELL Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| BS-015 | Verify SELL mode | 1. Click SELL toggle | Form shows sell options | High |
| BS-016 | Verify token balance display | 1. Check balance | Token balance shown | High |
| BS-017 | Verify SELL disabled no balance | 1. User has 0 tokens | SELL button disabled | High |
| BS-018 | Verify SELL calculation | 1. Enter token amount | SOL received calculated | High |

#### 5.3.4 Advanced Settings Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| BS-019 | Verify settings expand | 1. Click ⚙️ icon | Advanced settings shown | Medium |
| BS-020 | Verify slippage presets | 1. Click 0.5%/1%/2%/5% | Slippage updates | Medium |
| BS-021 | Verify slippage custom | 1. Enter custom value | Value accepted within 0.1%-50% | Medium |
| BS-022 | Verify slippage warning low | 1. Set <0.5% | "May fail" warning shown | Medium |
| BS-023 | Verify slippage warning high | 1. Set >10% | "High slippage risk" warning | Medium |
| BS-024 | Verify Anti-MEV toggle | 1. Toggle ON | +0.5% fee added | Medium |
| BS-025 | Verify Priority Fee options | 1. Select Normal/Fast/Instant | Fees update accordingly | Medium |
| BS-026 | Verify Auto-retry toggle | 1. Toggle ON/OFF | Setting saved | Medium |

#### 5.3.5 Limit Order Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| BS-027 | Verify Limit form display | 1. Select Limit mode | Target price field appears | High |
| BS-028 | Verify USD mode target | 1. Enter absolute price | % from current calculated | Medium |
| BS-029 | Verify % mode target | 1. Toggle to % 2. Enter percentage | Price calculated | Medium |
| BS-030 | Verify USD ⇄ % toggle | 1. Switch modes | Values convert correctly | Medium |
| BS-031 | Place limit order | 1. Fill form 2. Submit | Order created, confirmation shown | High |

#### 5.3.6 Transaction Flow Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| BS-032 | Execute BUY without wallet | 1. Enter amount 2. Click BUY | Wallet connection prompt | High |
| BS-033 | Execute BUY with wallet | 1. Connect wallet 2. Enter amount 3. BUY | Transaction processes, success modal | Critical |
| BS-034 | Execute SELL | 1. Have tokens 2. Enter amount 3. SELL | Transaction processes, success modal | Critical |
| BS-035 | Verify success modal content | 1. Complete trade | TX hash, amounts, reward ticket shown | High |
| BS-036 | Verify balance update after trade | 1. Complete trade | Balances update immediately | High |
| BS-037 | Verify transaction in history | 1. Complete trade | Appears in transaction history | Medium |

#### 5.3.7 Error Handling Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| BS-038 | Insufficient balance | 1. Enter amount > balance | "Insufficient SOL balance" error | High |
| BS-039 | Slippage exceeded | 1. Set low slippage 2. Price moves 3. Execute | Error message, retry button | High |
| BS-040 | Network error | 1. Simulate network issue | "Network error. Please retry." | Medium |
| BS-041 | Transaction timeout | 1. Simulate timeout | Timeout message, retry button | Medium |
| BS-042 | Auto-retry logic | 1. Enable auto-retry 2. Transaction fails | Retries up to 3 times | Medium |

#### 5.3.8 Risk Assessment Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| BS-043 | Verify risk badge display | 1. Check risk section | Green/Yellow/Red badge shown | Medium |
| BS-044 | Verify risk factors | 1. Check token with low liquidity | Higher risk displayed | Medium |

---

### 5.4 FR-004: My Profile

#### 5.4.1 Page Layout Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| MP-001 | Verify login required | 1. Navigate to My Profile (not logged in) | Redirect to login | High |
| MP-002 | Verify header info | 1. Login 2. Navigate to My Profile | Avatar, Username, Display name, Wallet address visible | High |
| MP-003 | Verify copy wallet | 1. Click copy button | Wallet copied to clipboard | Medium |
| MP-004 | Verify 5 tabs display | 1. Check tabs | Holding, Created, Transaction, Edit Profile, Limit Orders | High |
| MP-005 | Verify default tab | 1. Navigate to My Profile | Holding Tokens tab active | Medium |

#### 5.4.2 Holding Tokens Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| MP-006 | Verify portfolio stats | 1. View Holding tab | Total Value, 24h Change, Total P&L accurate | High |
| MP-007 | Verify token list | 1. Have tokens 2. View list | Avatar, Name, Balance, Value, Price, Change, P&L | High |
| MP-008 | Verify P&L calculation | 1. Check P&L for known token | P&L = Current Value - Cost Basis | High |
| MP-009 | Verify token click | 1. Click token | Navigate to Token Detail | Medium |
| MP-010 | Verify empty state | 1. User with no tokens | "No tokens held" message | Medium |

#### 5.4.3 Created Tokens Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| MP-011 | Verify created tokens list | 1. View Created tab | All created tokens shown | High |
| MP-012 | Verify token info | 1. Check token card | Name, Created date, Status, MC, Price, Volume, Holders | Medium |
| MP-013 | Verify sorting options | 1. Sort by MC/Volume/Holders | List re-orders correctly | Medium |
| MP-014 | Verify token click | 1. Click token | Navigate to Token Detail | Medium |

#### 5.4.4 Transaction History Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| MP-015 | Verify transaction list | 1. View Transaction tab | All transactions shown | High |
| MP-016 | Verify BUY/SELL badges | 1. Check transactions | Green for BUY, Red for SELL | Medium |
| MP-017 | Verify TX hash link | 1. Click TX hash | Opens Solana Explorer | Medium |
| MP-018 | Verify empty state | 1. New user, no trades | "No transactions yet" message | Medium |

#### 5.4.5 Edit Profile Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| MP-019 | Verify privacy toggle | 1. View Edit Profile | Privacy settings at top | High |
| MP-020 | Verify privacy default | 1. Check toggle | Default: Public (OFF) | High |
| MP-021 | Toggle to private | 1. Toggle to Private | Granular settings hidden | Medium |
| MP-022 | Verify granular controls | 1. Keep public 2. Check controls | Holdings visibility, Transaction visibility checkboxes | Medium |
| MP-023 | Verify always public notice | 1. Check info box | "Tokens you create are always public" message | Medium |
| MP-024 | Verify username one-time | 1. Set username 2. Save 3. Try to change | Field locked after save | High |
| MP-025 | Verify display name one-time | 1. Set display name 2. Save | Field locked after save | High |
| MP-026 | Verify username uniqueness | 1. Enter taken username | Error: username already taken | High |
| MP-027 | Verify avatar update | 1. Upload new avatar 2. Save | Avatar updates | Medium |
| MP-028 | Verify social links | 1. Add Twitter/Telegram 2. Save | Links saved, displayed on profile | Medium |
| MP-029 | Verify save changes | 1. Make changes 2. Click Save | All changes persisted | High |
| MP-030 | Verify confirmation modal | 1. First time save username | Confirmation modal appears | Medium |

#### 5.4.6 Limit Orders Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| MP-031 | Verify active orders display | 1. Have limit orders 2. View tab | Active orders shown | High |
| MP-032 | Verify order details | 1. Check order | Token, Type, Amount, Target Price, Current Price, Created | Medium |
| MP-033 | Cancel limit order | 1. Click Cancel 2. Confirm | Order cancelled, removed from list | High |
| MP-034 | Verify empty state | 1. No active orders | "No active limit orders" message | Medium |

---

### 5.5 FR-005: Public Profile

#### 5.5.1 Page Layout Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| PP-001 | Verify no login required | 1. Logout 2. Navigate to public profile | Page accessible | High |
| PP-002 | Verify header info | 1. View public profile | Avatar, Username, Display name, Wallet address | High |
| PP-003 | Verify stats overview | 1. Check stats | Tokens Created, Total Trades, Member Since | Medium |
| PP-004 | Verify 4 tabs | 1. Check tabs | Profile Info, Holding, Created, Transaction | High |

#### 5.5.2 Private Profile Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| PP-005 | Verify private profile display | 1. View user with private profile | Lock icon, "This profile is private" message | High |
| PP-006 | Verify created tokens visible | 1. View private profile | Created tokens section visible | High |
| PP-007 | Verify hidden tabs | 1. View private profile | Only Created Tokens visible, others hidden | High |
| PP-008 | Verify granular privacy - holdings | 1. User hides holdings 2. View profile | Holdings shows "🔒 Holdings are private" | Medium |
| PP-009 | Verify granular privacy - transactions | 1. User hides transactions 2. View profile | Transactions shows "🔒 Transaction history is private" | Medium |

#### 5.5.3 Tabs Content Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| PP-010 | Verify Profile Info tab | 1. View Profile Info | Bio, Social links, Wallet, Stats | Medium |
| PP-011 | Verify Holding Tokens tab | 1. View Holdings (public profile) | Token list without P&L | Medium |
| PP-012 | Verify Created Tokens tab | 1. View Created | All created tokens visible | Medium |
| PP-013 | Verify Transaction History tab | 1. View Transactions (public profile) | Transaction list | Medium |
| PP-014 | Verify social links click | 1. Click Twitter/Telegram | Opens in new tab | Low |
| PP-015 | Verify token click | 1. Click any token | Navigate to Token Detail | Medium |

---

### 5.6 FR-006: Creator Dashboard

#### 5.6.1 Dashboard Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CD-001 | Verify login required | 1. Navigate without login | Redirect to login | High |
| CD-002 | Verify header display | 1. Login 2. Navigate | "Creator Dashboard" title | Medium |
| CD-003 | Verify 2 tabs | 1. Check tabs | Created Tokens, Creator Revenue | High |

#### 5.6.2 Created Tokens Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CD-004 | Verify token list | 1. View Created Tokens tab | All created tokens displayed | High |
| CD-005 | Verify status badges | 1. Check badges | Active (green), Graduated (yellow) | Medium |
| CD-006 | Verify Manage Token button | 1. Click Manage Token | Navigate to Token Management | High |
| CD-007 | Verify empty state | 1. User with no tokens | "You haven't created any tokens" + Create button | Medium |

#### 5.6.3 Creator Revenue Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CD-008 | Verify stats cards | 1. View Revenue tab | Total, Unclaimed, Claimed amounts | High |
| CD-009 | Verify claim function | 1. Have unclaimed revenue 2. Click Claim 3. Connect wallet | Revenue transferred to wallet | Critical |
| CD-010 | Verify claim disabled | 1. No unclaimed revenue | Claim button disabled | Medium |
| CD-011 | Verify revenue breakdown | 1. Check breakdown | Revenue per token listed | Medium |

#### 5.6.4 Token Management Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CD-012 | Verify breadcrumb navigation | 1. In Token Management | "Creator Dashboard > Token Name" | Medium |
| CD-013 | Verify back button | 1. Click Back | Returns to Dashboard | Medium |
| CD-014 | Verify 3 tabs | 1. Check tabs | Overview, Trusted Level, Community Management | High |

#### 5.6.5 Overview Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CD-015 | Verify metrics grid | 1. View Overview | MC, Price, Volume, Holders, Supply, Liquidity | High |
| CD-016 | Verify real-time updates | 1. Monitor metrics | Values update in real-time | Medium |
| CD-017 | Verify token info read-only | 1. Check token info | Name, Symbol, Description not editable | Medium |

#### 5.6.6 Trusted Level Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CD-018 | Verify LP Lock toggle | 1. Toggle LP Lock | State changes, trust score updates | High |
| CD-019 | Verify Request Audit | 1. Click Request Audit | Audit request submitted | Medium |
| CD-020 | Verify Freeze Authority | 1. Disable Freeze Authority | Permanent action, confirmation required | High |
| CD-021 | Verify info box | 1. Check info | Trust score impact explained | Low |

#### 5.6.7 Community Management Tab Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CD-022 | Create new post | 1. Click Create 2. Fill title/content 3. Submit | Post created, appears in list | High |
| CD-023 | Verify post validation | 1. Try empty title | Validation error | Medium |
| CD-024 | Pin post | 1. Click Pin on post | Post pinned, shows first | Medium |
| CD-025 | Verify max 1 pinned | 1. Pin second post | First post unpinned | Medium |
| CD-026 | Edit post | 1. Click Edit 2. Modify 3. Save | Changes saved | Medium |
| CD-027 | Delete post | 1. Click Delete 2. Confirm | Post removed | Medium |
| CD-028 | Verify empty state | 1. No posts | "No posts yet" message | Low |

---

### 5.7 FR-007: Create Token

#### 5.7.1 Wizard Flow Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CT-001 | Verify 5 steps indicator | 1. Start Create Token | 5 steps shown, Step 1 active | High |
| CT-002 | Verify step navigation | 1. Complete step 2. Click Next | Advances to next step | High |
| CT-003 | Verify Previous button | 1. On Step 2+ 2. Click Previous | Returns to previous step | Medium |
| CT-004 | Verify Previous disabled Step 1 | 1. On Step 1 | Previous button disabled | Medium |
| CT-005 | Verify validation before Next | 1. Leave required empty 2. Click Next | Error shown, stays on step | High |
| CT-006 | Verify draft saving | 1. Fill partial form 2. Navigate away 3. Return | Previously entered data restored | Medium |

#### 5.7.2 Step 1 - Basic Info Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CT-007 | Verify Token Name validation | 1. Leave empty 2. Click Next | Required error | High |
| CT-008 | Verify Token Name max length | 1. Enter 33+ chars | Limited to 32 characters | Medium |
| CT-009 | Verify Symbol validation | 1. Leave empty | Required error | High |
| CT-010 | Verify Symbol auto uppercase | 1. Enter lowercase | Converts to uppercase | Medium |
| CT-011 | Verify Symbol uniqueness | 1. Enter existing symbol | Uniqueness error | High |
| CT-012 | Verify Statement max length | 1. Enter 61+ chars | Limited to 60 characters | Medium |
| CT-013 | Verify Description max length | 1. Enter 201+ chars | Limited to 200 characters | Medium |
| CT-014 | Verify AI Assist - Statement | 1. Fill Name/Symbol 2. Click AI Assist | Statement generated | Medium |
| CT-015 | Verify AI Assist - Description | 1. Click AI Assist | Description generated | Medium |

#### 5.7.3 Step 2 - Avatar Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CT-016 | Verify upload image | 1. Click upload 2. Select PNG/JPG | Image uploaded, preview shown | High |
| CT-017 | Verify file type validation | 1. Upload non-image file | Error: invalid file type | Medium |
| CT-018 | Verify file size validation | 1. Upload >5MB file | Error: file too large | Medium |
| CT-019 | Verify auto crop | 1. Upload non-square image | Cropped to square | Medium |
| CT-020 | Verify AI Generate | 1. Click Generate with AI | Avatar generated from info | Medium |
| CT-021 | Verify default placeholder | 1. Skip avatar | 🚀 emoji placeholder | Low |

#### 5.7.4 Step 3 - Security Settings Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CT-022 | Verify LP Lock default | 1. Check toggle | Default: ON | Medium |
| CT-023 | Toggle LP Lock | 1. Toggle OFF/ON | State changes | Medium |
| CT-024 | Verify Audit Request toggle | 1. Toggle | State changes | Medium |
| CT-025 | Verify Freeze Authority warning | 1. Toggle Disable | Permanent action warning | Medium |
| CT-026 | Verify trust score display | 1. Toggle options | Trust score updates | Low |

#### 5.7.5 Step 4 - Initial Buy Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CT-027 | Verify amount input | 1. Enter SOL amount | Valid input accepted | High |
| CT-028 | Verify quick buttons | 1. Click 0.1/0.5/1 SOL | Amount fills | Medium |
| CT-029 | Verify Skip button | 1. Click Skip | Proceeds without initial buy | Medium |
| CT-030 | Verify token calculation | 1. Enter amount | Estimated tokens shown | High |
| CT-031 | Verify balance validation | 1. Enter > wallet balance | Error: insufficient balance | High |

#### 5.7.6 Step 5 - Review Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CT-032 | Verify summary display | 1. View Review step | All info from previous steps shown | High |
| CT-033 | Verify Create button | 1. Click Create Token | Wallet connection if needed | High |
| CT-034 | Create token flow | 1. Click Create 2. Sign transaction | Token created, success screen | Critical |
| CT-035 | Verify loading state | 1. During creation | "Creating token..." indicator | Medium |

#### 5.7.7 Success Screen Tests

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| CT-036 | Verify success content | 1. Token created | Celebration, Token info, Contract address | High |
| CT-037 | Verify View Token Detail | 1. Click button | Navigate to Token Detail | High |
| CT-038 | Verify Share on Twitter | 1. Click Share | Twitter opens with pre-filled tweet | Medium |
| CT-039 | Verify copy address | 1. Click contract address | Address copied | Medium |
| CT-040 | Verify Creator Dashboard updated | 1. Navigate to Creator Dashboard | New token appears | High |

---

### 5.8 FR-008: Leaderboard

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| LB-001 | Verify page layout | 1. Navigate to Leaderboard | Header, Top 3 cards, Table visible | High |
| LB-002 | Verify Top 3 featured cards | 1. Check top section | 3 large cards for #1, #2, #3 | High |
| LB-003 | Verify table list | 1. Check table | Rank #4+ tokens shown | High |
| LB-004 | Verify table columns | 1. Check columns | Token, Creator, Holders, MC, Buy button | Medium |
| LB-005 | Verify ranking by formula | 1. Compare rankings | Ordered correctly | Medium |
| LB-006 | Verify real-time updates | 1. Monitor rankings | Updates reflect changes | Medium |
| LB-007 | Verify Buy button | 1. Click Buy | Navigate to Token Detail with trading panel | Medium |
| LB-008 | Verify token click | 1. Click token name | Navigate to Token Detail | Medium |

---

### 5.9 FR-009: Rewards & Games

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| RW-001 | Verify broadcast banner | 1. Check top of page | Winners marquee scrolling | Medium |
| RW-002 | Verify stats cards | 1. Check stats | Reward Balance, Your Tickets displayed | High |
| RW-003 | Verify slot machine display | 1. Check slot section | 5 reels visible | High |
| RW-004 | Spin slot machine | 1. Have tickets 2. Click Spin | Reels spin, result shown | High |
| RW-005 | Verify spin without tickets | 1. No tickets 2. Try Spin | Spin disabled or error | High |
| RW-006 | Verify winning 3 of kind | 1. Get 3 matching | 0.001 SOL × multiplier awarded | High |
| RW-007 | Verify winning 5 of kind | 1. Get 5 matching | 0.01 SOL awarded | High |
| RW-008 | Verify multipliers table | 1. Check table | All symbol multipliers shown | Medium |
| RW-009 | Verify rules display | 1. Check rules section | Game rules explained | Medium |
| RW-010 | Verify history table | 1. Check history | Previous winning spins shown | Medium |

---

### 5.10 FR-010: Referrals

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| RF-001 | Verify page layout | 1. Navigate to Referrals | Header, Stats, Link, Rewards, Users visible | High |
| RF-002 | Verify stats cards | 1. Check stats | Total Referrals, Total Earnings accurate | High |
| RF-003 | Verify referral link generation | 1. Check link | Unique link based on username | High |
| RF-004 | Verify copy link | 1. Click Copy | Link copied, "✓ Copied!" shown | High |
| RF-005 | Verify Share on Twitter | 1. Click Share Twitter | Twitter opens with pre-filled text | Medium |
| RF-006 | Verify Share on Telegram | 1. Click Share Telegram | Telegram share opens | Medium |
| RF-007 | Verify claimable rewards display | 1. Have unclaimed | Amount shown correctly | High |
| RF-008 | Claim referral rewards | 1. Click Claim | Wallet signature, transfer to wallet | Critical |
| RF-009 | Verify claim disabled | 1. No claimable | Button disabled | Medium |
| RF-010 | Verify referred users table | 1. Check table | User, Joined, Trade Volume, Your Earnings | High |
| RF-011 | Verify earnings calculation | 1. Check earnings | User Volume × 0.2% (5% of trading fees) | High |
| RF-012 | Verify user click | 1. Click user row | Navigate to Public Profile (respect privacy) | Medium |
| RF-013 | Verify empty state | 1. No referrals | "No referrals yet" message | Medium |

---

### 5.11 FR-011: Points & Ranking

| TC ID | Test Case | Steps | Expected Result | Priority |
|-------|-----------|-------|-----------------|----------|
| PT-001 | Verify login required | 1. Navigate without login | Redirect to login | High |
| PT-002 | Verify header display | 1. Check header | "Points", Current/Next level points | High |
| PT-003 | Verify rank card | 1. Check rank card | Current rank emoji, name, progress bar | High |
| PT-004 | Verify progress bar | 1. Check progress | Percentage to next rank accurate | High |
| PT-005 | Verify Seed rank (0 pts) | 1. New user | 🌱 Seed displayed | Medium |
| PT-006 | Verify Sprout rank (500 pts) | 1. User with 500+ pts | 🌿 Sprout displayed | Medium |
| PT-007 | Verify Sapling rank (2K pts) | 1. User with 2000+ pts | 🌳 Sapling displayed | Medium |
| PT-008 | Verify Tree rank (10K pts) | 1. User with 10000+ pts | 🌲 Tree displayed | Medium |
| PT-009 | Verify Ancient Tree rank (50K pts) | 1. User with 50000+ pts | 🪷 Ancient Tree displayed | Medium |
| PT-010 | Verify history empty state | 1. New user | "NOTHING HERE" message | Medium |
| PT-011 | Verify history table | 1. User with activities | Date, Activities, Points columns | High |
| PT-012 | Verify referral points | 1. Refer user who trades | NetVolume × 10 points earned | High |
| PT-013 | Verify trade points | 1. Execute trade | Volume × 5 points earned | High |
| PT-014 | Verify token creation points | 1. Create token | 20 points for creation | Medium |
| PT-015 | Verify image+desc bonus | 1. Upload image + full description | +10 points | Medium |
| PT-016 | Verify first buys bonus | 1. Token gets 10 first buys | +30 points | Medium |
| PT-017 | Verify rank up notification | 1. Reach next tier | Notification/celebration shown | Medium |

---

## 6. NON-FUNCTIONAL TESTING

### 6.1 Performance Testing

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| PF-001 | Page load time < 3s | Token List loads within 3 seconds | High |
| PF-002 | Real-time updates latency | Chat message < 500ms, Price < 10s | High |
| PF-003 | 100+ token cards performance | Smooth scrolling, no lag | High |
| PF-004 | Trading panel response | Input changes reflect < 100ms | High |
| PF-005 | 1000 concurrent users | System stable, response < 5s | High |

### 6.2 Security Testing

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| SC-001 | XSS prevention | Script injection filtered | Critical |
| SC-002 | SQL injection prevention | Query injection blocked | Critical |
| SC-003 | CSRF protection | All forms protected | High |
| SC-004 | Wallet signature verification | Invalid signatures rejected | Critical |
| SC-005 | Rate limiting | Spam requests blocked | High |
| SC-006 | Session management | Proper timeout, secure cookies | High |
| SC-007 | Vietnam geolocation block | Vietnam IPs blocked | Critical |

### 6.3 Usability Testing

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| US-001 | Navigation clarity | Users can find features easily | High |
| US-002 | Error message clarity | Users understand what went wrong | High |
| US-003 | Mobile responsiveness | Usable on tablet/mobile | Medium |
| US-004 | Color contrast | Meets WCAG AA standards | Medium |
| US-005 | Loading indicators | Users know when to wait | Medium |

### 6.4 Compatibility Testing

| TC ID | Test Case | Expected Result | Priority |
|-------|-----------|-----------------|----------|
| CM-001 | Chrome latest | All features work | High |
| CM-002 | Firefox latest | All features work | High |
| CM-003 | Safari latest | All features work | Medium |
| CM-004 | Edge latest | All features work | Medium |
| CM-005 | Phantom wallet | Wallet integration works | Critical |
| CM-006 | Solflare wallet | Wallet integration works | High |

---

## 7. EXIT CRITERIA

### 7.1 Test Completion Criteria

| Criterion | Target |
|-----------|--------|
| Test case execution | 100% executed |
| Pass rate (Critical) | 100% passed |
| Pass rate (High) | 95% passed |
| Pass rate (Medium) | 90% passed |
| Pass rate (Low) | 80% passed |
| Critical defects | 0 open |
| High defects | ≤ 2 open (with workaround) |

### 7.2 Release Criteria

- [ ] All Critical test cases passed
- [ ] No Critical or Blocker defects open
- [ ] Performance benchmarks met
- [ ] Security scan passed
- [ ] UAT sign-off received
- [ ] Documentation complete

---

## 8. DEFECT MANAGEMENT

### 8.1 Defect Severity Levels

| Severity | Definition | SLA |
|----------|------------|-----|
| Blocker | System unusable, no workaround | Fix immediately |
| Critical | Major feature broken, no workaround | 24 hours |
| High | Feature broken, workaround exists | 48 hours |
| Medium | Minor feature issue | 1 week |
| Low | Cosmetic/minor issue | Next release |

### 8.2 Defect Lifecycle

```
New → Assigned → In Progress → Fixed → Verified → Closed
                      ↓
                   Reopened
```

### 8.3 Defect Report Template

```
Defect ID: DEF-XXX
Title: [Brief description]
Module: FR-XXX
Severity: Critical/High/Medium/Low
Priority: P1/P2/P3/P4

Environment:
- Browser: Chrome 120
- OS: Windows 11
- Wallet: Phantom

Steps to Reproduce:
1. 
2. 
3. 

Expected Result:
[What should happen]

Actual Result:
[What actually happened]

Attachments:
- Screenshot
- Video

Notes:
[Additional context]
```

---

## 9. TEST DELIVERABLES

### 9.1 Pre-Testing Phase
- [ ] Test Plan (this document)
- [ ] Test Cases (detailed)
- [ ] Test Data
- [ ] Test Environment setup

### 9.2 During Testing Phase
- [ ] Daily Test Status Reports
- [ ] Defect Reports
- [ ] Test Execution Logs

### 9.3 Post-Testing Phase
- [ ] Test Summary Report
- [ ] Defect Summary
- [ ] Test Coverage Report
- [ ] Recommendations
- [ ] Sign-off Document

---

## APPENDIX A: TEST DATA REQUIREMENTS

### A.1 User Accounts

| User Type | Username | Purpose |
|-----------|----------|---------|
| Admin | admin_test | Admin features |
| Creator | creator_test | Token creation, dashboard |
| Trader | trader_test | Trading features |
| New User | new_user_test | Empty states, onboarding |
| Private User | private_test | Privacy testing |

### A.2 Token Data

| Token | Purpose |
|-------|---------|
| TEST_HIGH_MC | High market cap testing |
| TEST_LOW_MC | Low market cap testing |
| TEST_GRADUATED | Graduated token testing |
| TEST_NSFW | NSFW content testing |
| TEST_TRUSTED | Trust badges testing |

### A.3 Wallet Addresses

| Wallet | Purpose | Balance |
|--------|---------|---------|
| Test Wallet 1 | Trading tests | 10 SOL |
| Test Wallet 2 | Insufficient balance tests | 0.001 SOL |
| Test Wallet 3 | Token holder tests | Various tokens |

---

## APPENDIX B: TEST SCHEDULE

### Phase 1: Unit & Component Testing (Week 1-2)
- Frontend components
- API endpoints
- Database operations

### Phase 2: Integration Testing (Week 3-4)
- Module integration
- Third-party integrations
- Wallet integration

### Phase 3: System Testing (Week 5-6)
- E2E scenarios
- Cross-browser testing
- Performance testing

### Phase 4: UAT (Week 7)
- User acceptance testing
- Stakeholder review
- Final sign-off

---

**END OF TEST PLAN DOCUMENT**
