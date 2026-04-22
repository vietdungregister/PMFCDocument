# PUMPFUN CLONE - TEST CASES EXECUTION MATRIX

**Document Version:** 1.0  
**Created Date:** February 4, 2026  
**Purpose:** Track test case execution status

---

## 📊 SUMMARY DASHBOARD

### Overall Progress

| Category | Total | Passed | Failed | Blocked | Not Run | Pass Rate |
|----------|-------|--------|--------|---------|---------|-----------|
| Critical | 15 | - | - | - | 15 | 0% |
| High | 85 | - | - | - | 85 | 0% |
| Medium | 95 | - | - | - | 95 | 0% |
| Low | 22 | - | - | - | 22 | 0% |
| **TOTAL** | **217** | **0** | **0** | **0** | **217** | **0%** |

### Module Progress

| Module | Total TC | Passed | Failed | Status |
|--------|----------|--------|--------|--------|
| FR-001 Token List | 36 | - | - | ⏳ Not Started |
| FR-002 Token Detail | 28 | - | - | ⏳ Not Started |
| FR-003 Buy/Sell | 44 | - | - | ⏳ Not Started |
| FR-004 My Profile | 34 | - | - | ⏳ Not Started |
| FR-005 Public Profile | 15 | - | - | ⏳ Not Started |
| FR-006 Creator Dashboard | 28 | - | - | ⏳ Not Started |
| FR-007 Create Token | 40 | - | - | ⏳ Not Started |
| FR-008 Leaderboard | 8 | - | - | ⏳ Not Started |
| FR-009 Rewards | 10 | - | - | ⏳ Not Started |
| FR-010 Referrals | 13 | - | - | ⏳ Not Started |
| FR-011 Points | 17 | - | - | ⏳ Not Started |

---

## 🔴 CRITICAL TEST CASES (Must Pass 100%)

| TC ID | Module | Test Case | Priority | Status | Tester | Date | Defect |
|-------|--------|-----------|----------|--------|--------|------|--------|
| BS-033 | FR-003 | Execute BUY with wallet | Critical | ⬜ | - | - | - |
| BS-034 | FR-003 | Execute SELL | Critical | ⬜ | - | - | - |
| CT-034 | FR-007 | Create token flow | Critical | ⬜ | - | - | - |
| CD-009 | FR-006 | Claim creator revenue | Critical | ⬜ | - | - | - |
| RF-008 | FR-010 | Claim referral rewards | Critical | ⬜ | - | - | - |
| SC-001 | Security | XSS prevention | Critical | ⬜ | - | - | - |
| SC-002 | Security | SQL injection prevention | Critical | ⬜ | - | - | - |
| SC-004 | Security | Wallet signature verification | Critical | ⬜ | - | - | - |
| SC-007 | Security | Vietnam geolocation block | Critical | ⬜ | - | - | - |
| CM-005 | Compat | Phantom wallet integration | Critical | ⬜ | - | - | - |
| RW-004 | FR-009 | Spin slot machine | Critical | ⬜ | - | - | - |
| RW-005 | FR-009 | Spin without tickets blocked | Critical | ⬜ | - | - | - |
| RW-006 | FR-009 | Winning 3 of kind payout | Critical | ⬜ | - | - | - |
| RW-007 | FR-009 | Winning 5 of kind payout | Critical | ⬜ | - | - | - |
| MP-024 | FR-004 | Username one-time restriction | Critical | ⬜ | - | - | - |

**Legend:** ⬜ Not Run | ✅ Passed | ❌ Failed | 🚫 Blocked | ⏸️ Skipped

---

## 📋 FR-001: TOKEN LIST - Test Execution

### Tab Navigation (6 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TL-001 | Verify 5 tabs display | High | ⬜ | - | - | - | - |
| TL-002 | Verify Discover is default tab | High | ⬜ | - | - | - | - |
| TL-003 | Switch tabs | High | ⬜ | - | - | - | - |
| TL-004 | Verify tab filter retention | Medium | ⬜ | - | - | - | - |
| TL-005 | Verify Favorite tab empty state | Medium | ⬜ | - | - | - | - |
| TL-006 | Verify Graduated tab empty state | Medium | ⬜ | - | - | - | - |

### DiscoverScore Algorithm (3 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TL-007 | Verify DiscoverScore calculation | High | ⬜ | - | - | - | - |
| TL-008 | Verify descending order | High | ⬜ | - | - | - | - |
| TL-009 | Verify score recalculation (10 min) | Medium | ⬜ | - | - | - | - |

### Token Card Display (10 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TL-010 | Verify token card elements | High | ⬜ | - | - | - | - |
| TL-011 | Verify price format < $0.01 | Medium | ⬜ | - | - | - | - |
| TL-012 | Verify price format $0.01-$1 | Medium | ⬜ | - | - | - | - |
| TL-013 | Verify price format > $1 | Medium | ⬜ | - | - | - | - |
| TL-014 | Verify market cap K format | Medium | ⬜ | - | - | - | - |
| TL-015 | Verify market cap M format | Medium | ⬜ | - | - | - | - |
| TL-016 | Verify 24h change colors | Medium | ⬜ | - | - | - | - |
| TL-017 | Verify favorite toggle | High | ⬜ | - | - | - | - |
| TL-018 | Verify card click navigation | High | ⬜ | - | - | - | - |
| TL-019 | Verify card hover effect | Low | ⬜ | - | - | - | - |

### Filters (8 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TL-020 | Verify NSFW filter default OFF | High | ⬜ | - | - | - | - |
| TL-021 | Toggle NSFW filter | Medium | ⬜ | - | - | - | - |
| TL-022 | Verify Market Cap filter | High | ⬜ | - | - | - | - |
| TL-023 | Verify Volume filter | High | ⬜ | - | - | - | - |
| TL-024 | Verify Trust Level filter OR logic | Medium | ⬜ | - | - | - | - |
| TL-025 | Verify combined filters AND logic | High | ⬜ | - | - | - | - |
| TL-026 | Verify active filters badge | Medium | ⬜ | - | - | - | - |
| TL-027 | Verify Reset Filters | Medium | ⬜ | - | - | - | - |

### Sort (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TL-028 | Verify sort panel opens | Medium | ⬜ | - | - | - | - |
| TL-029 | Sort by Price ascending | Medium | ⬜ | - | - | - | - |
| TL-030 | Sort by Market Cap descending | Medium | ⬜ | - | - | - | - |
| TL-031 | Verify sort overrides tab | Medium | ⬜ | - | - | - | - |

### Search (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TL-032 | Search by token name | High | ⬜ | - | - | - | - |
| TL-033 | Search by symbol | High | ⬜ | - | - | - | - |
| TL-034 | Search with special characters | Medium | ⬜ | - | - | - | - |
| TL-035 | Search no results | Medium | ⬜ | - | - | - | - |
| TL-036 | Search with filters | Medium | ⬜ | - | - | - | - |

---

## 📋 FR-002: TOKEN DETAIL - Test Execution

### Token Header (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TD-001 | Verify token metadata display | High | ⬜ | - | - | - | - |
| TD-002 | Verify creator link navigation | High | ⬜ | - | - | - | - |
| TD-003 | Verify favorite toggle | Medium | ⬜ | - | - | - | - |
| TD-004 | Verify social links | Medium | ⬜ | - | - | - | - |

### Price Chart (3 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TD-005 | Verify chart renders | High | ⬜ | - | - | - | - |
| TD-006 | Verify timeframe switch | Medium | ⬜ | - | - | - | - |
| TD-007 | Verify real-time updates | High | ⬜ | - | - | - | - |

### Market Metrics (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TD-008 | Verify all metrics display | High | ⬜ | - | - | - | - |
| TD-009 | Verify metrics update frequency | Medium | ⬜ | - | - | - | - |
| TD-010 | Verify price animation | Low | ⬜ | - | - | - | - |
| TD-011 | Verify graduation progress | Medium | ⬜ | - | - | - | - |

### Community Chat (8 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TD-012 | Verify chat loads | High | ⬜ | - | - | - | - |
| TD-013 | Send message (logged in) | High | ⬜ | - | - | - | - |
| TD-014 | Send message (not logged in) | High | ⬜ | - | - | - | - |
| TD-015 | Verify max message length | Medium | ⬜ | - | - | - | - |
| TD-016 | Verify username click | Medium | ⬜ | - | - | - | - |
| TD-017 | Verify real-time chat | High | ⬜ | - | - | - | - |
| TD-018 | Verify chat history scroll | Medium | ⬜ | - | - | - | - |
| TD-019 | Verify profanity filter | Medium | ⬜ | - | - | - | - |

### Holders List (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TD-020 | Verify top 100 holders display | High | ⬜ | - | - | - | - |
| TD-021 | Verify holder badges | Medium | ⬜ | - | - | - | - |
| TD-022 | Verify top 10 concentration | Medium | ⬜ | - | - | - | - |
| TD-023 | Verify holder click | Medium | ⬜ | - | - | - | - |

### Transaction History (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| TD-024 | Verify 50 transactions display | High | ⬜ | - | - | - | - |
| TD-025 | Verify transaction type colors | Medium | ⬜ | - | - | - | - |
| TD-026 | Verify TX hash link | Medium | ⬜ | - | - | - | - |
| TD-027 | Verify whale indicator | Medium | ⬜ | - | - | - | - |
| TD-028 | Verify trader click | Medium | ⬜ | - | - | - | - |

---

## 📋 FR-003: BUY/SELL - Test Execution

### Panel Layout (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| BS-001 | Verify panel visibility | High | ⬜ | - | - | - | - |
| BS-002 | Verify BUY/SELL toggle | High | ⬜ | - | - | - | - |
| BS-003 | Verify Market/Limit toggle | High | ⬜ | - | - | - | - |
| BS-004 | Verify current price display | High | ⬜ | - | - | - | - |
| BS-005 | Verify panel scrolling | Medium | ⬜ | - | - | - | - |

### Market Order - BUY (9 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| BS-006 | Verify amount input (SOL mode) | High | ⬜ | - | - | - | - |
| BS-007 | Verify quick buttons (SOL mode) | Medium | ⬜ | - | - | - | - |
| BS-008 | Verify currency switch | Medium | ⬜ | - | - | - | - |
| BS-009 | Verify quick buttons (Token mode) | Medium | ⬜ | - | - | - | - |
| BS-010 | Verify "You Receive" calculation | High | ⬜ | - | - | - | - |
| BS-011 | Verify balance display | High | ⬜ | - | - | - | - |
| BS-012 | Verify fees section expand | Medium | ⬜ | - | - | - | - |
| BS-013 | Verify BUY button enabled | High | ⬜ | - | - | - | - |
| BS-014 | Verify BUY button disabled | High | ⬜ | - | - | - | - |

### Market Order - SELL (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| BS-015 | Verify SELL mode | High | ⬜ | - | - | - | - |
| BS-016 | Verify token balance display | High | ⬜ | - | - | - | - |
| BS-017 | Verify SELL disabled no balance | High | ⬜ | - | - | - | - |
| BS-018 | Verify SELL calculation | High | ⬜ | - | - | - | - |

### Advanced Settings (8 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| BS-019 | Verify settings expand | Medium | ⬜ | - | - | - | - |
| BS-020 | Verify slippage presets | Medium | ⬜ | - | - | - | - |
| BS-021 | Verify slippage custom | Medium | ⬜ | - | - | - | - |
| BS-022 | Verify slippage warning low | Medium | ⬜ | - | - | - | - |
| BS-023 | Verify slippage warning high | Medium | ⬜ | - | - | - | - |
| BS-024 | Verify Anti-MEV toggle | Medium | ⬜ | - | - | - | - |
| BS-025 | Verify Priority Fee options | Medium | ⬜ | - | - | - | - |
| BS-026 | Verify Auto-retry toggle | Medium | ⬜ | - | - | - | - |

### Limit Order (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| BS-027 | Verify Limit form display | High | ⬜ | - | - | - | - |
| BS-028 | Verify USD mode target | Medium | ⬜ | - | - | - | - |
| BS-029 | Verify % mode target | Medium | ⬜ | - | - | - | - |
| BS-030 | Verify USD ⇄ % toggle | Medium | ⬜ | - | - | - | - |
| BS-031 | Place limit order | High | ⬜ | - | - | - | - |

### Transaction Flow (6 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| BS-032 | Execute BUY without wallet | High | ⬜ | - | - | - | - |
| BS-033 | Execute BUY with wallet | **Critical** | ⬜ | - | - | - | - |
| BS-034 | Execute SELL | **Critical** | ⬜ | - | - | - | - |
| BS-035 | Verify success modal content | High | ⬜ | - | - | - | - |
| BS-036 | Verify balance update after trade | High | ⬜ | - | - | - | - |
| BS-037 | Verify transaction in history | Medium | ⬜ | - | - | - | - |

### Error Handling (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| BS-038 | Insufficient balance | High | ⬜ | - | - | - | - |
| BS-039 | Slippage exceeded | High | ⬜ | - | - | - | - |
| BS-040 | Network error | Medium | ⬜ | - | - | - | - |
| BS-041 | Transaction timeout | Medium | ⬜ | - | - | - | - |
| BS-042 | Auto-retry logic | Medium | ⬜ | - | - | - | - |

### Risk Assessment (2 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| BS-043 | Verify risk badge display | Medium | ⬜ | - | - | - | - |
| BS-044 | Verify risk factors | Medium | ⬜ | - | - | - | - |

---

## 📋 FR-004: MY PROFILE - Test Execution

### Page Layout (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| MP-001 | Verify login required | High | ⬜ | - | - | - | - |
| MP-002 | Verify header info | High | ⬜ | - | - | - | - |
| MP-003 | Verify copy wallet | Medium | ⬜ | - | - | - | - |
| MP-004 | Verify 5 tabs display | High | ⬜ | - | - | - | - |
| MP-005 | Verify default tab | Medium | ⬜ | - | - | - | - |

### Holding Tokens Tab (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| MP-006 | Verify portfolio stats | High | ⬜ | - | - | - | - |
| MP-007 | Verify token list | High | ⬜ | - | - | - | - |
| MP-008 | Verify P&L calculation | High | ⬜ | - | - | - | - |
| MP-009 | Verify token click | Medium | ⬜ | - | - | - | - |
| MP-010 | Verify empty state | Medium | ⬜ | - | - | - | - |

### Created Tokens Tab (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| MP-011 | Verify created tokens list | High | ⬜ | - | - | - | - |
| MP-012 | Verify token info | Medium | ⬜ | - | - | - | - |
| MP-013 | Verify sorting options | Medium | ⬜ | - | - | - | - |
| MP-014 | Verify token click | Medium | ⬜ | - | - | - | - |

### Transaction History Tab (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| MP-015 | Verify transaction list | High | ⬜ | - | - | - | - |
| MP-016 | Verify BUY/SELL badges | Medium | ⬜ | - | - | - | - |
| MP-017 | Verify TX hash link | Medium | ⬜ | - | - | - | - |
| MP-018 | Verify empty state | Medium | ⬜ | - | - | - | - |

### Edit Profile Tab (12 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| MP-019 | Verify privacy toggle | High | ⬜ | - | - | - | - |
| MP-020 | Verify privacy default | High | ⬜ | - | - | - | - |
| MP-021 | Toggle to private | Medium | ⬜ | - | - | - | - |
| MP-022 | Verify granular controls | Medium | ⬜ | - | - | - | - |
| MP-023 | Verify always public notice | Medium | ⬜ | - | - | - | - |
| MP-024 | Verify username one-time | **Critical** | ⬜ | - | - | - | - |
| MP-025 | Verify display name one-time | High | ⬜ | - | - | - | - |
| MP-026 | Verify username uniqueness | High | ⬜ | - | - | - | - |
| MP-027 | Verify avatar update | Medium | ⬜ | - | - | - | - |
| MP-028 | Verify social links | Medium | ⬜ | - | - | - | - |
| MP-029 | Verify save changes | High | ⬜ | - | - | - | - |
| MP-030 | Verify confirmation modal | Medium | ⬜ | - | - | - | - |

### Limit Orders Tab (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| MP-031 | Verify active orders display | High | ⬜ | - | - | - | - |
| MP-032 | Verify order details | Medium | ⬜ | - | - | - | - |
| MP-033 | Cancel limit order | High | ⬜ | - | - | - | - |
| MP-034 | Verify empty state | Medium | ⬜ | - | - | - | - |

---

## 📋 FR-005: PUBLIC PROFILE - Test Execution

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| PP-001 | Verify no login required | High | ⬜ | - | - | - | - |
| PP-002 | Verify header info | High | ⬜ | - | - | - | - |
| PP-003 | Verify stats overview | Medium | ⬜ | - | - | - | - |
| PP-004 | Verify 4 tabs | High | ⬜ | - | - | - | - |
| PP-005 | Verify private profile display | High | ⬜ | - | - | - | - |
| PP-006 | Verify created tokens visible | High | ⬜ | - | - | - | - |
| PP-007 | Verify hidden tabs | High | ⬜ | - | - | - | - |
| PP-008 | Verify granular privacy - holdings | Medium | ⬜ | - | - | - | - |
| PP-009 | Verify granular privacy - transactions | Medium | ⬜ | - | - | - | - |
| PP-010 | Verify Profile Info tab | Medium | ⬜ | - | - | - | - |
| PP-011 | Verify Holding Tokens tab | Medium | ⬜ | - | - | - | - |
| PP-012 | Verify Created Tokens tab | Medium | ⬜ | - | - | - | - |
| PP-013 | Verify Transaction History tab | Medium | ⬜ | - | - | - | - |
| PP-014 | Verify social links click | Low | ⬜ | - | - | - | - |
| PP-015 | Verify token click | Medium | ⬜ | - | - | - | - |

---

## 📋 FR-006: CREATOR DASHBOARD - Test Execution

### Dashboard (3 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CD-001 | Verify login required | High | ⬜ | - | - | - | - |
| CD-002 | Verify header display | Medium | ⬜ | - | - | - | - |
| CD-003 | Verify 2 tabs | High | ⬜ | - | - | - | - |

### Created Tokens Tab (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CD-004 | Verify token list | High | ⬜ | - | - | - | - |
| CD-005 | Verify status badges | Medium | ⬜ | - | - | - | - |
| CD-006 | Verify Manage Token button | High | ⬜ | - | - | - | - |
| CD-007 | Verify empty state | Medium | ⬜ | - | - | - | - |

### Creator Revenue Tab (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CD-008 | Verify stats cards | High | ⬜ | - | - | - | - |
| CD-009 | Verify claim function | **Critical** | ⬜ | - | - | - | - |
| CD-010 | Verify claim disabled | Medium | ⬜ | - | - | - | - |
| CD-011 | Verify revenue breakdown | Medium | ⬜ | - | - | - | - |

### Token Management (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CD-012 | Verify breadcrumb navigation | Medium | ⬜ | - | - | - | - |
| CD-013 | Verify back button | Medium | ⬜ | - | - | - | - |
| CD-014 | Verify 3 tabs | High | ⬜ | - | - | - | - |
| CD-015 | Verify metrics grid | High | ⬜ | - | - | - | - |

### Trusted Level Tab (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CD-016 | Verify real-time updates | Medium | ⬜ | - | - | - | - |
| CD-017 | Verify token info read-only | Medium | ⬜ | - | - | - | - |
| CD-018 | Verify LP Lock toggle | High | ⬜ | - | - | - | - |
| CD-019 | Verify Request Audit | Medium | ⬜ | - | - | - | - |
| CD-020 | Verify Freeze Authority | High | ⬜ | - | - | - | - |
| CD-021 | Verify info box | Low | ⬜ | - | - | - | - |

### Community Management Tab (7 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CD-022 | Create new post | High | ⬜ | - | - | - | - |
| CD-023 | Verify post validation | Medium | ⬜ | - | - | - | - |
| CD-024 | Pin post | Medium | ⬜ | - | - | - | - |
| CD-025 | Verify max 1 pinned | Medium | ⬜ | - | - | - | - |
| CD-026 | Edit post | Medium | ⬜ | - | - | - | - |
| CD-027 | Delete post | Medium | ⬜ | - | - | - | - |
| CD-028 | Verify empty state | Low | ⬜ | - | - | - | - |

---

## 📋 FR-007: CREATE TOKEN - Test Execution

### Wizard Flow (6 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CT-001 | Verify 5 steps indicator | High | ⬜ | - | - | - | - |
| CT-002 | Verify step navigation | High | ⬜ | - | - | - | - |
| CT-003 | Verify Previous button | Medium | ⬜ | - | - | - | - |
| CT-004 | Verify Previous disabled Step 1 | Medium | ⬜ | - | - | - | - |
| CT-005 | Verify validation before Next | High | ⬜ | - | - | - | - |
| CT-006 | Verify draft saving | Medium | ⬜ | - | - | - | - |

### Step 1 - Basic Info (9 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CT-007 | Verify Token Name validation | High | ⬜ | - | - | - | - |
| CT-008 | Verify Token Name max length | Medium | ⬜ | - | - | - | - |
| CT-009 | Verify Symbol validation | High | ⬜ | - | - | - | - |
| CT-010 | Verify Symbol auto uppercase | Medium | ⬜ | - | - | - | - |
| CT-011 | Verify Symbol uniqueness | High | ⬜ | - | - | - | - |
| CT-012 | Verify Statement max length | Medium | ⬜ | - | - | - | - |
| CT-013 | Verify Description max length | Medium | ⬜ | - | - | - | - |
| CT-014 | Verify AI Assist - Statement | Medium | ⬜ | - | - | - | - |
| CT-015 | Verify AI Assist - Description | Medium | ⬜ | - | - | - | - |

### Step 2 - Avatar (6 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CT-016 | Verify upload image | High | ⬜ | - | - | - | - |
| CT-017 | Verify file type validation | Medium | ⬜ | - | - | - | - |
| CT-018 | Verify file size validation | Medium | ⬜ | - | - | - | - |
| CT-019 | Verify auto crop | Medium | ⬜ | - | - | - | - |
| CT-020 | Verify AI Generate | Medium | ⬜ | - | - | - | - |
| CT-021 | Verify default placeholder | Low | ⬜ | - | - | - | - |

### Step 3 - Security (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CT-022 | Verify LP Lock default | Medium | ⬜ | - | - | - | - |
| CT-023 | Toggle LP Lock | Medium | ⬜ | - | - | - | - |
| CT-024 | Verify Audit Request toggle | Medium | ⬜ | - | - | - | - |
| CT-025 | Verify Freeze Authority warning | Medium | ⬜ | - | - | - | - |
| CT-026 | Verify trust score display | Low | ⬜ | - | - | - | - |

### Step 4 - Initial Buy (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CT-027 | Verify amount input | High | ⬜ | - | - | - | - |
| CT-028 | Verify quick buttons | Medium | ⬜ | - | - | - | - |
| CT-029 | Verify Skip button | Medium | ⬜ | - | - | - | - |
| CT-030 | Verify token calculation | High | ⬜ | - | - | - | - |
| CT-031 | Verify balance validation | High | ⬜ | - | - | - | - |

### Step 5 - Review (4 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CT-032 | Verify summary display | High | ⬜ | - | - | - | - |
| CT-033 | Verify Create button | High | ⬜ | - | - | - | - |
| CT-034 | Create token flow | **Critical** | ⬜ | - | - | - | - |
| CT-035 | Verify loading state | Medium | ⬜ | - | - | - | - |

### Success Screen (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CT-036 | Verify success content | High | ⬜ | - | - | - | - |
| CT-037 | Verify View Token Detail | High | ⬜ | - | - | - | - |
| CT-038 | Verify Share on Twitter | Medium | ⬜ | - | - | - | - |
| CT-039 | Verify copy address | Medium | ⬜ | - | - | - | - |
| CT-040 | Verify Creator Dashboard updated | High | ⬜ | - | - | - | - |

---

## 📋 FR-008: LEADERBOARD - Test Execution

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| LB-001 | Verify page layout | High | ⬜ | - | - | - | - |
| LB-002 | Verify Top 3 featured cards | High | ⬜ | - | - | - | - |
| LB-003 | Verify table list | High | ⬜ | - | - | - | - |
| LB-004 | Verify table columns | Medium | ⬜ | - | - | - | - |
| LB-005 | Verify ranking by formula | Medium | ⬜ | - | - | - | - |
| LB-006 | Verify real-time updates | Medium | ⬜ | - | - | - | - |
| LB-007 | Verify Buy button | Medium | ⬜ | - | - | - | - |
| LB-008 | Verify token click | Medium | ⬜ | - | - | - | - |

---

## 📋 FR-009: REWARDS - Test Execution

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| RW-001 | Verify broadcast banner | Medium | ⬜ | - | - | - | - |
| RW-002 | Verify stats cards | High | ⬜ | - | - | - | - |
| RW-003 | Verify slot machine display | High | ⬜ | - | - | - | - |
| RW-004 | Spin slot machine | **Critical** | ⬜ | - | - | - | - |
| RW-005 | Verify spin without tickets | **Critical** | ⬜ | - | - | - | - |
| RW-006 | Verify winning 3 of kind | **Critical** | ⬜ | - | - | - | - |
| RW-007 | Verify winning 5 of kind | **Critical** | ⬜ | - | - | - | - |
| RW-008 | Verify multipliers table | Medium | ⬜ | - | - | - | - |
| RW-009 | Verify rules display | Medium | ⬜ | - | - | - | - |
| RW-010 | Verify history table | Medium | ⬜ | - | - | - | - |

---

## 📋 FR-010: REFERRALS - Test Execution

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| RF-001 | Verify page layout | High | ⬜ | - | - | - | - |
| RF-002 | Verify stats cards | High | ⬜ | - | - | - | - |
| RF-003 | Verify referral link generation | High | ⬜ | - | - | - | - |
| RF-004 | Verify copy link | High | ⬜ | - | - | - | - |
| RF-005 | Verify Share on Twitter | Medium | ⬜ | - | - | - | - |
| RF-006 | Verify Share on Telegram | Medium | ⬜ | - | - | - | - |
| RF-007 | Verify claimable rewards display | High | ⬜ | - | - | - | - |
| RF-008 | Claim referral rewards | **Critical** | ⬜ | - | - | - | - |
| RF-009 | Verify claim disabled | Medium | ⬜ | - | - | - | - |
| RF-010 | Verify referred users table | High | ⬜ | - | - | - | - |
| RF-011 | Verify earnings calculation | High | ⬜ | - | - | - | - |
| RF-012 | Verify user click | Medium | ⬜ | - | - | - | - |
| RF-013 | Verify empty state | Medium | ⬜ | - | - | - | - |

---

## 📋 FR-011: POINTS - Test Execution

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| PT-001 | Verify login required | High | ⬜ | - | - | - | - |
| PT-002 | Verify header display | High | ⬜ | - | - | - | - |
| PT-003 | Verify rank card | High | ⬜ | - | - | - | - |
| PT-004 | Verify progress bar | High | ⬜ | - | - | - | - |
| PT-005 | Verify Seed rank (0 pts) | Medium | ⬜ | - | - | - | - |
| PT-006 | Verify Sprout rank (500 pts) | Medium | ⬜ | - | - | - | - |
| PT-007 | Verify Sapling rank (2K pts) | Medium | ⬜ | - | - | - | - |
| PT-008 | Verify Tree rank (10K pts) | Medium | ⬜ | - | - | - | - |
| PT-009 | Verify Ancient Tree rank (50K pts) | Medium | ⬜ | - | - | - | - |
| PT-010 | Verify history empty state | Medium | ⬜ | - | - | - | - |
| PT-011 | Verify history table | High | ⬜ | - | - | - | - |
| PT-012 | Verify referral points | High | ⬜ | - | - | - | - |
| PT-013 | Verify trade points | High | ⬜ | - | - | - | - |
| PT-014 | Verify token creation points | Medium | ⬜ | - | - | - | - |
| PT-015 | Verify image+desc bonus | Medium | ⬜ | - | - | - | - |
| PT-016 | Verify first buys bonus | Medium | ⬜ | - | - | - | - |
| PT-017 | Verify rank up notification | Medium | ⬜ | - | - | - | - |

---

## 📋 NON-FUNCTIONAL TESTING - Execution

### Performance (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| PF-001 | Page load time < 3s | High | ⬜ | - | - | - | - |
| PF-002 | Real-time updates latency | High | ⬜ | - | - | - | - |
| PF-003 | 100+ token cards performance | High | ⬜ | - | - | - | - |
| PF-004 | Trading panel response | High | ⬜ | - | - | - | - |
| PF-005 | 1000 concurrent users | High | ⬜ | - | - | - | - |

### Security (7 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| SC-001 | XSS prevention | **Critical** | ⬜ | - | - | - | - |
| SC-002 | SQL injection prevention | **Critical** | ⬜ | - | - | - | - |
| SC-003 | CSRF protection | High | ⬜ | - | - | - | - |
| SC-004 | Wallet signature verification | **Critical** | ⬜ | - | - | - | - |
| SC-005 | Rate limiting | High | ⬜ | - | - | - | - |
| SC-006 | Session management | High | ⬜ | - | - | - | - |
| SC-007 | Vietnam geolocation block | **Critical** | ⬜ | - | - | - | - |

### Usability (5 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| US-001 | Navigation clarity | High | ⬜ | - | - | - | - |
| US-002 | Error message clarity | High | ⬜ | - | - | - | - |
| US-003 | Mobile responsiveness | Medium | ⬜ | - | - | - | - |
| US-004 | Color contrast | Medium | ⬜ | - | - | - | - |
| US-005 | Loading indicators | Medium | ⬜ | - | - | - | - |

### Compatibility (6 TCs)

| TC ID | Test Case | Priority | Status | Tester | Date | Defect | Notes |
|-------|-----------|----------|--------|--------|------|--------|-------|
| CM-001 | Chrome latest | High | ⬜ | - | - | - | - |
| CM-002 | Firefox latest | High | ⬜ | - | - | - | - |
| CM-003 | Safari latest | Medium | ⬜ | - | - | - | - |
| CM-004 | Edge latest | Medium | ⬜ | - | - | - | - |
| CM-005 | Phantom wallet | **Critical** | ⬜ | - | - | - | - |
| CM-006 | Solflare wallet | High | ⬜ | - | - | - | - |

---

## 📝 NOTES & OBSERVATIONS

### Test Execution Notes

| Date | Tester | Module | Notes |
|------|--------|--------|-------|
| - | - | - | - |

### Environment Issues

| Date | Issue | Status | Resolution |
|------|-------|--------|------------|
| - | - | - | - |

---

**END OF TEST CASES MATRIX**
