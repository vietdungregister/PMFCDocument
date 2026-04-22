# PUMPFUN CLONE - E2E TEST SCENARIOS

**Document Version:** 1.0  
**Created Date:** February 4, 2026  
**Purpose:** End-to-End Test Scenarios for critical user journeys

---

## 📋 MỤC LỤC

1. [User Journeys Overview](#1-user-journeys-overview)
2. [New User Onboarding](#2-new-user-onboarding)
3. [Token Discovery & Trading](#3-token-discovery--trading)
4. [Token Creation](#4-token-creation)
5. [Creator Management](#5-creator-management)
6. [Profile & Privacy](#6-profile--privacy)
7. [Earning Features](#7-earning-features)
8. [Edge Cases & Negative Scenarios](#8-edge-cases--negative-scenarios)

---

## 1. USER JOURNEYS OVERVIEW

### Critical User Journeys

| Journey ID | Journey Name | Priority | Modules Involved |
|------------|--------------|----------|------------------|
| UJ-001 | New User Registration & First Trade | Critical | FR-001, FR-002, FR-003, FR-004 |
| UJ-002 | Token Discovery to Buy | Critical | FR-001, FR-002, FR-003 |
| UJ-003 | Create & Launch Token | Critical | FR-007, FR-006 |
| UJ-004 | Limit Order Lifecycle | High | FR-002, FR-003, FR-004 |
| UJ-005 | Creator Revenue Claim | High | FR-006 |
| UJ-006 | Referral & Earnings | High | FR-010, FR-011 |
| UJ-007 | Profile Privacy Setup | Medium | FR-004, FR-005 |
| UJ-008 | Slot Machine Rewards | Medium | FR-003, FR-009 |

---

## 2. NEW USER ONBOARDING

### Scenario E2E-001: New User First Trade

**Objective:** Verify complete flow from landing to first successful trade

**Preconditions:**
- New browser session
- No previous account
- Phantom wallet installed with SOL balance

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Navigate to https://pumpfun.io | Home page loads with Token List | ✓ Page loads < 3s |
| 2 | Verify Discover tab active | Tokens displayed in grid | ✓ Token cards visible |
| 3 | Click "Connect Wallet" | Wallet connection modal appears | ✓ Phantom option shown |
| 4 | Select Phantom wallet | Phantom extension popup appears | ✓ Extension triggered |
| 5 | Approve connection in Phantom | Modal closes, wallet connected | ✓ Address shown in header |
| 6 | Click on any token card | Token Detail page opens | ✓ Chart, metrics displayed |
| 7 | In Trading Panel, enter 0.1 SOL | Amount accepted | ✓ "You Receive" calculated |
| 8 | Click "Buy X TOKEN" button | Transaction confirmation | ✓ Wallet popup appears |
| 9 | Sign transaction in Phantom | Transaction processing | ✓ Loading state shown |
| 10 | Wait for confirmation | Success modal appears | ✓ TX hash, amounts shown |
| 11 | Click "Close" on modal | Modal closes | ✓ Balance updated |
| 12 | Navigate to My Profile | Profile page loads | ✓ Login redirected if needed |
| 13 | Check Holding Tokens tab | Purchased token visible | ✓ Token in holdings |
| 14 | Check Transaction History | BUY transaction visible | ✓ Correct amount/time |

**Postconditions:**
- User wallet connected
- Token balance increased
- SOL balance decreased
- Transaction recorded

**Pass Criteria:** All 14 steps complete without errors

---

### Scenario E2E-002: New User Profile Setup

**Objective:** Verify first-time profile configuration

**Preconditions:**
- User connected wallet (from E2E-001)
- No username set yet

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Navigate to My Profile | Profile page loads | ✓ |
| 2 | Click Edit Profile tab | Edit form appears | ✓ Privacy section shown |
| 3 | Verify Privacy Settings section | Toggle visible, default Public | ✓ |
| 4 | Click Username field | Field is editable | ✓ |
| 5 | Enter unique username | Character counter shows | ✓ |
| 6 | Enter Display Name | Field accepts input | ✓ |
| 7 | Enter Bio | Text accepted (max 200 chars) | ✓ |
| 8 | Add Twitter link | URL accepted | ✓ |
| 9 | Click "Save Changes" | Confirmation modal appears | ✓ "Cannot change after saving" |
| 10 | Click "Confirm" | Changes saved | ✓ Success message |
| 11 | Refresh page | Data persisted | ✓ |
| 12 | Try to edit Username | Field is locked/disabled | ✓ One-time restriction works |
| 13 | Verify Avatar can still be edited | Avatar upload available | ✓ |
| 14 | Verify Bio can still be edited | Bio field editable | ✓ |

**Pass Criteria:** Username locked after first save, other fields editable

---

## 3. TOKEN DISCOVERY & TRADING

### Scenario E2E-003: Discover, Filter, Search, Buy

**Objective:** Test complete token discovery flow

**Preconditions:**
- Connected wallet with SOL
- Testnet has various tokens

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Navigate to Token List | Discover tab active | ✓ |
| 2 | Note first 3 tokens | Tokens ordered by DiscoverScore | ✓ |
| 3 | Click "Trending" tab | Tab switches | ✓ Different order |
| 4 | Click "Top Volume" tab | Tab switches | ✓ Volume sorted |
| 5 | Return to Discover | Original order | ✓ |
| 6 | Click Filter button | Filter panel opens | ✓ |
| 7 | Set Market Cap: $10K - $100K | Filter applied | ✓ Badge shows "1" |
| 8 | Toggle NSFW: ON | More tokens may appear | ✓ |
| 9 | Verify badge shows "2" | Active filters count | ✓ |
| 10 | Type "TEST" in search, press Enter | Results filtered | ✓ Only matching tokens |
| 11 | Click Reset Filters | All filters cleared | ✓ Original list |
| 12 | Click Sort button | Sort options shown | ✓ |
| 13 | Select "Market Cap" descending | List re-ordered | ✓ Highest MC first |
| 14 | Add token to Favorites (♡) | Icon fills (♥) | ✓ |
| 15 | Click Favorite tab | Favorited token shown | ✓ |
| 16 | Click token to open Detail | Detail page loads | ✓ |
| 17 | Execute market buy | Trade completes | ✓ |

**Pass Criteria:** All discovery features work together seamlessly

---

### Scenario E2E-004: Limit Order Complete Lifecycle

**Objective:** Verify limit order from creation to execution/cancellation

**Preconditions:**
- Connected wallet with SOL
- Token at known price

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Open Token Detail | Trading panel visible | ✓ |
| 2 | Note current price | e.g., $0.00123 | ✓ |
| 3 | Select "Limit" order type | Limit form appears | ✓ Target price field |
| 4 | Enter amount: 0.5 SOL | Amount accepted | ✓ |
| 5 | Set target price: +20% | Price calculated | ✓ Shows $0.001476 |
| 6 | Toggle USD ⇄ % mode | Values convert correctly | ✓ |
| 7 | Click "Place Order" | Order created | ✓ Success message |
| 8 | Navigate to My Profile | Profile loads | ✓ |
| 9 | Click Limit Orders tab | Order visible | ✓ All details shown |
| 10 | Verify order details | Amount, Target, Current Price | ✓ |
| 11 | Click "Cancel Order" | Confirmation modal | ✓ |
| 12 | Confirm cancellation | Order removed | ✓ Empty state shown |
| 13 | Create new limit order | Order placed | ✓ |
| 14 | Wait for price to reach target | (Or simulate) Order executes | ✓ Notification received |
| 15 | Check Holdings | Token balance increased | ✓ |
| 16 | Check Transaction History | Limit order execution logged | ✓ |

**Pass Criteria:** Limit orders can be created, monitored, cancelled, and executed

---

### Scenario E2E-005: Sell Token Flow

**Objective:** Verify selling tokens back to SOL

**Preconditions:**
- Have tokens in wallet
- Connected

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Navigate to Token Detail | For token you hold | ✓ |
| 2 | Click "SELL" toggle | Sell mode active (red) | ✓ |
| 3 | Form shows token balance | Correct balance | ✓ |
| 4 | Enter half balance amount | Valid input | ✓ |
| 5 | Click "50%" quick button | 50% of balance fills | ✓ |
| 6 | Verify "You Receive" SOL | Calculation correct | ✓ |
| 7 | Click "Sell X TOKEN" | Wallet popup | ✓ |
| 8 | Sign transaction | Processing | ✓ |
| 9 | Verify success modal | SOL received shown | ✓ |
| 10 | Check SOL balance | Increased | ✓ |
| 11 | Check Token balance | Decreased | ✓ |
| 12 | Check Transaction History | SELL transaction logged | ✓ |

**Pass Criteria:** Sell executes correctly with accurate calculations

---

## 4. TOKEN CREATION

### Scenario E2E-006: Create Token Complete Flow

**Objective:** Verify full token creation wizard

**Preconditions:**
- Connected wallet with >= 1 SOL
- Unique token name/symbol prepared

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Click "Create Token" in sidebar | Step 1 loads | ✓ 5-step indicator |
| 2 | Verify Step 1: Basic Info | All fields visible | ✓ |
| 3 | Leave all fields empty, click Next | Validation errors | ✓ Required field errors |
| 4 | Enter Token Name: "TestMeme2026" | Accepted | ✓ Counter shows chars |
| 5 | Enter Symbol: "tm26" | Auto uppercased to "TM26" | ✓ |
| 6 | Click AI Assist for Statement | Statement generated | ✓ |
| 7 | Enter Description manually | Accepted | ✓ |
| 8 | Click Next | Step 2: Avatar | ✓ |
| 9 | Verify avatar section | Upload + AI generate options | ✓ |
| 10 | Upload 5MB+ image | Error: file too large | ✓ |
| 11 | Upload valid PNG image | Preview updated | ✓ |
| 12 | Click Next | Step 3: Security | ✓ |
| 13 | Verify LP Lock default ON | Toggle is ON | ✓ |
| 14 | Toggle Freeze Authority | Warning appears | ✓ Permanent action |
| 15 | Click Next | Step 4: Initial Buy | ✓ |
| 16 | Click "0.5 SOL" quick button | Amount set | ✓ |
| 17 | Verify token preview | Estimated tokens shown | ✓ |
| 18 | Click Next | Step 5: Review | ✓ |
| 19 | Verify all information | Name, Symbol, Avatar, Settings, Initial Buy | ✓ |
| 20 | Click "Create Token 🚀" | Wallet confirmation | ✓ |
| 21 | Sign transaction | Creating... | ✓ Loading state |
| 22 | Wait for completion | Success screen | ✓ Celebration |
| 23 | Verify token info | Name, Contract address, MC | ✓ |
| 24 | Click "View Token Detail" | Token page opens | ✓ Your token live |
| 25 | Navigate to Creator Dashboard | Dashboard loads | ✓ |
| 26 | Verify token in Created Tokens | Token listed | ✓ |

**Pass Criteria:** Token created on-chain, visible in all relevant places

---

### Scenario E2E-007: Create Token Skip Initial Buy

**Objective:** Verify token creation without initial purchase

**Preconditions:**
- Connected wallet

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Complete Steps 1-3 | Reach Step 4 | ✓ |
| 2 | Click "Skip" button | Step 5: Review | ✓ |
| 3 | Verify Initial Buy shows "Skipped" | Summary correct | ✓ |
| 4 | Create token | Token created | ✓ |
| 5 | Check Holdings in My Profile | Token NOT in holdings | ✓ 0 balance |

**Pass Criteria:** Token creation works without initial buy

---

## 5. CREATOR MANAGEMENT

### Scenario E2E-008: Creator Dashboard Full Flow

**Objective:** Verify creator management features

**Preconditions:**
- User has created at least one token (from E2E-006)
- Some trades have occurred on their token

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Navigate to Creator Dashboard | Dashboard loads | ✓ |
| 2 | Click "Created Tokens" tab | List of tokens | ✓ Token from E2E-006 |
| 3 | Click "Creator Revenue" tab | Revenue stats shown | ✓ 3 cards visible |
| 4 | Verify Total Revenue | Value accurate | ✓ |
| 5 | Verify Unclaimed Revenue | Amount >= 0 | ✓ |
| 6 | If Unclaimed > 0, click Claim | Wallet signature | ✓ |
| 7 | Confirm Claim | Revenue transferred | ✓ SOL received |
| 8 | Return to Created Tokens | Token list | ✓ |
| 9 | Click "Manage Token" | Token Management page | ✓ 3 tabs |
| 10 | Verify Overview tab | Metrics displayed | ✓ |
| 11 | Click "Trusted Level" tab | Security settings | ✓ |
| 12 | Toggle LP Lock | State changes | ✓ |
| 13 | Click "Community Management" tab | Posts section | ✓ |
| 14 | Click "Create New Post" | Post modal | ✓ |
| 15 | Enter Title and Content | Form accepts input | ✓ |
| 16 | Click "Create" | Post appears in list | ✓ |
| 17 | Click "Pin" on post | Post pinned | ✓ Shows first |
| 18 | Create second post and Pin | First post unpinned | ✓ Max 1 pinned |
| 19 | Edit a post | Modal opens, save works | ✓ |
| 20 | Delete a post | Confirmation, post removed | ✓ |
| 21 | Navigate to Token Detail | Token page | ✓ |
| 22 | Verify posts visible in community | Posts shown | ✓ |

**Pass Criteria:** All creator management features functional

---

## 6. PROFILE & PRIVACY

### Scenario E2E-009: Privacy Settings Impact

**Objective:** Verify privacy settings affect Public Profile

**Preconditions:**
- User A: Profile is Public
- User B: Will check User A's profile

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| **User A Actions** |
| 1 | Login as User A | Profile loads | ✓ |
| 2 | Go to Edit Profile | Privacy section visible | ✓ |
| 3 | Verify default: Public | Toggle OFF | ✓ |
| 4 | Verify granular options visible | Holdings, Transactions checkboxes | ✓ |
| 5 | Uncheck "Show Holdings" | Setting changed | ✓ |
| 6 | Click Save | Changes saved | ✓ |
| **User B Actions** |
| 7 | Login as User B | Different session | ✓ |
| 8 | Navigate to User A's Public Profile | Profile loads | ✓ |
| 9 | Click Holdings tab | "🔒 Holdings are private" | ✓ |
| 10 | Transaction tab should work | Transactions visible | ✓ |
| 11 | Created Tokens visible | Always public | ✓ |
| **User A Sets Full Private** |
| 12 | User A: Toggle to "Private" | Granular options hidden | ✓ |
| 13 | Save changes | Saved | ✓ |
| **User B Checks Again** |
| 14 | User B: Refresh User A's profile | Lock icon shown | ✓ |
| 15 | Message: "This profile is private" | Clear message | ✓ |
| 16 | Only Created Tokens visible | Token list shown | ✓ Everything else hidden |

**Pass Criteria:** Privacy settings correctly restrict profile visibility

---

### Scenario E2E-010: Public Profile from Multiple Entry Points

**Objective:** Verify public profile accessible from various places

**Preconditions:**
- User with public profile exists
- Has created tokens, has transactions

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Open Token Detail | Find token by this user | ✓ |
| 2 | Click creator name in header | Public Profile opens | ✓ |
| 3 | Press Back | Return to Token Detail | ✓ |
| 4 | Find user in Community Chat | User sent a message | ✓ |
| 5 | Click username in chat | Public Profile opens | ✓ |
| 6 | Press Back | Return to Token Detail | ✓ |
| 7 | View Holders list | User is a holder | ✓ |
| 8 | Click holder name | Public Profile opens | ✓ |
| 9 | Press Back | Return to Token Detail | ✓ |
| 10 | View Transaction History | User made a trade | ✓ |
| 11 | Click trader name | Public Profile opens | ✓ |
| 12 | Navigate directly via URL | /profile/username | ✓ Same profile |

**Pass Criteria:** Public profile consistent from all entry points

---

## 7. EARNING FEATURES

### Scenario E2E-011: Referral Complete Flow

**Objective:** Test referral program end-to-end

**Preconditions:**
- User A: Registered, has referral link
- User B: New user

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| **User A Gets Referral Link** |
| 1 | Login as User A | Dashboard | ✓ |
| 2 | Navigate to Referrals | Referral page | ✓ |
| 3 | Copy referral link | Clipboard: https://pumpfun.io/ref/usera | ✓ |
| 4 | Note current stats | Total Referrals: X, Earnings: Y | ✓ |
| **User B Uses Referral** |
| 5 | User B opens referral link | Landing page | ✓ Ref code tracked |
| 6 | User B connects wallet | New account created | ✓ |
| 7 | User B completes a trade | 1 SOL volume | ✓ |
| **User A Checks Earnings** |
| 8 | User A refreshes Referrals page | Stats updated | ✓ |
| 9 | Total Referrals increased | X + 1 | ✓ |
| 10 | User B appears in table | Joined date, volume visible | ✓ |
| 11 | Earnings calculated | 1 SOL × 0.2% = 0.002 SOL | ✓ |
| 12 | If claimable > 0, click Claim | Wallet signature | ✓ |
| 13 | Confirm claim | SOL transferred to wallet | ✓ |
| 14 | Verify SOL balance increased | +0.002 SOL | ✓ |

**Pass Criteria:** Referral tracking and earnings work correctly

---

### Scenario E2E-012: Points & Ranking Progression

**Objective:** Verify points earned from activities

**Preconditions:**
- User with some trading history
- Note current points

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Navigate to Points page | Current rank shown | ✓ |
| 2 | Note current points | e.g., 450 points | ✓ |
| 3 | Note current rank | 🌱 Seed | ✓ |
| 4 | Execute a 0.1 SOL trade | Trade completes | ✓ |
| 5 | Return to Points page | Points updated | ✓ +0.5 pts (0.1×5) |
| 6 | Verify history table | Trade activity logged | ✓ |
| 7 | Create a token | Token created | ✓ |
| 8 | Return to Points page | +20 pts for creation | ✓ |
| 9 | If points now >= 500 | Rank up to 🌿 Sprout | ✓ |
| 10 | Verify progress bar | Shows progress to next tier | ✓ |

**Pass Criteria:** Points calculated correctly, ranks progress

---

### Scenario E2E-013: Slot Machine Rewards

**Objective:** Verify slot machine game flow

**Preconditions:**
- User has reward tickets (from trading)

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Navigate to Rewards | Rewards page | ✓ |
| 2 | Check "Your Tickets" | e.g., 5 tickets | ✓ |
| 3 | Check current Reward Balance | e.g., 0.01 SOL | ✓ |
| 4 | Click "Spin" button | Reels spin animation | ✓ |
| 5 | Wait for result | Reels stop | ✓ |
| 6 | If win (3+ match) | Win amount shown | ✓ Balance increases |
| 7 | Tickets decreased | -1 ticket | ✓ |
| 8 | Check History table | Spin logged | ✓ |
| 9 | Spin until 0 tickets | All tickets used | ✓ |
| 10 | Try to spin | Button disabled / error | ✓ "No tickets" |
| 11 | Execute another trade | Should earn ticket | ✓ |
| 12 | Return to Rewards | Tickets = 1 | ✓ |

**Pass Criteria:** Slot machine operates correctly with ticket system

---

## 8. EDGE CASES & NEGATIVE SCENARIOS

### Scenario E2E-014: Insufficient Balance Handling

**Objective:** Verify system handles insufficient funds

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Connect wallet with 0.001 SOL | Connected | ✓ |
| 2 | Try to buy token with 1 SOL | Error: Insufficient balance | ✓ |
| 3 | Try to create token | Error on confirmation | ✓ Not enough for fees |
| 4 | Fill wallet with SOL | Balance updated | ✓ |
| 5 | Retry operations | Success | ✓ |

---

### Scenario E2E-015: Network Error Recovery

**Objective:** Verify graceful handling of network issues

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Navigate to Token List | Page loads | ✓ |
| 2 | Simulate network disconnect | Browser offline | ✓ |
| 3 | Try to switch tabs | Error message shown | ✓ "Network error" |
| 4 | Try to execute trade | Error, retry button | ✓ |
| 5 | Reconnect network | Connection restored | ✓ |
| 6 | Click Retry | Operation completes | ✓ |

---

### Scenario E2E-016: Vietnam Geolocation Block

**Objective:** Verify Vietnam users blocked

**Preconditions:**
- VPN set to Vietnam IP

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Set VPN to Vietnam | IP in Vietnam | ✓ |
| 2 | Navigate to pumpfun.io | Access blocked | ✓ Block message shown |
| 3 | Switch VPN to Singapore | Different IP | ✓ |
| 4 | Refresh page | Page accessible | ✓ |

---

### Scenario E2E-017: Session Timeout

**Objective:** Verify session management

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Login and connect wallet | Session started | ✓ |
| 2 | Wait for session timeout | (Or simulate) | ✓ |
| 3 | Try to execute trade | Re-authentication required | ✓ |
| 4 | Re-connect wallet | Session restored | ✓ |

---

### Scenario E2E-018: Duplicate Token Symbol

**Objective:** Verify symbol uniqueness enforcement

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Note existing token symbol | e.g., "TEST" | ✓ |
| 2 | Start Create Token | Step 1 | ✓ |
| 3 | Enter same symbol "TEST" | Check uniqueness | ✓ |
| 4 | Click Next | Error: Symbol already exists | ✓ |
| 5 | Change to "TEST2" | Unique | ✓ |
| 6 | Proceed successfully | Next step | ✓ |

---

### Scenario E2E-019: Wallet Disconnect During Transaction

**Objective:** Verify handling of wallet disconnect

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Start a buy transaction | Wallet popup appears | ✓ |
| 2 | Disconnect wallet in Phantom | Connection lost | ✓ |
| 3 | Observe behavior | Error displayed | ✓ "Wallet disconnected" |
| 4 | Reconnect wallet | Must re-initiate | ✓ |
| 5 | Retry transaction | Completes | ✓ |

---

### Scenario E2E-020: Concurrent Limit Orders

**Objective:** Verify multiple limit orders management

**Test Steps:**

| Step | Action | Expected Result | Checkpoint |
|------|--------|-----------------|------------|
| 1 | Create limit order on Token A | Order created | ✓ |
| 2 | Create limit order on Token B | Order created | ✓ |
| 3 | Create limit order on Token C | Order created | ✓ |
| 4 | Navigate to Limit Orders tab | 3 orders visible | ✓ |
| 5 | Cancel one order | 2 orders remain | ✓ |
| 6 | Verify SOL reserved correctly | Balance reflects locked amounts | ✓ |

---

## 📝 SCENARIO EXECUTION TRACKING

### Execution Status

| Scenario ID | Name | Priority | Status | Tester | Date | Notes |
|-------------|------|----------|--------|--------|------|-------|
| E2E-001 | New User First Trade | Critical | ⬜ | - | - | - |
| E2E-002 | New User Profile Setup | High | ⬜ | - | - | - |
| E2E-003 | Discover, Filter, Search, Buy | Critical | ⬜ | - | - | - |
| E2E-004 | Limit Order Lifecycle | High | ⬜ | - | - | - |
| E2E-005 | Sell Token Flow | Critical | ⬜ | - | - | - |
| E2E-006 | Create Token Complete Flow | Critical | ⬜ | - | - | - |
| E2E-007 | Create Token Skip Initial Buy | Medium | ⬜ | - | - | - |
| E2E-008 | Creator Dashboard Full Flow | High | ⬜ | - | - | - |
| E2E-009 | Privacy Settings Impact | Medium | ⬜ | - | - | - |
| E2E-010 | Public Profile Entry Points | Medium | ⬜ | - | - | - |
| E2E-011 | Referral Complete Flow | High | ⬜ | - | - | - |
| E2E-012 | Points & Ranking Progression | Medium | ⬜ | - | - | - |
| E2E-013 | Slot Machine Rewards | Medium | ⬜ | - | - | - |
| E2E-014 | Insufficient Balance Handling | High | ⬜ | - | - | - |
| E2E-015 | Network Error Recovery | High | ⬜ | - | - | - |
| E2E-016 | Vietnam Geolocation Block | Critical | ⬜ | - | - | - |
| E2E-017 | Session Timeout | Medium | ⬜ | - | - | - |
| E2E-018 | Duplicate Token Symbol | Medium | ⬜ | - | - | - |
| E2E-019 | Wallet Disconnect | Medium | ⬜ | - | - | - |
| E2E-020 | Concurrent Limit Orders | Medium | ⬜ | - | - | - |

**Legend:** ⬜ Not Run | ✅ Passed | ❌ Failed | 🚫 Blocked

---

**END OF E2E TEST SCENARIOS**
