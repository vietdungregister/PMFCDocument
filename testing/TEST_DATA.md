# PUMPFUN CLONE - TEST DATA REQUIREMENTS

**Version:** 1.0 | **Created:** February 4, 2026

---

## 1. TEST USER ACCOUNTS

### 1.1 Primary Test Accounts

| Account ID | Username | Role | Purpose | Wallet Balance |
|------------|----------|------|---------|----------------|
| USER-001 | `test_admin` | Admin | Admin features testing | 100 SOL |
| USER-002 | `test_creator` | Creator | Token creation, dashboard | 50 SOL + 5 tokens created |
| USER-003 | `test_trader` | Trader | Trading, portfolio | 20 SOL + various holdings |
| USER-004 | `test_new` | New User | Onboarding, empty states | 5 SOL |
| USER-005 | `test_private` | Private Profile | Privacy testing | 10 SOL |
| USER-006 | `test_whale` | Whale | Large holdings testing | 500 SOL |
| USER-007 | `test_referrer` | Referrer | Referral testing | 15 SOL + 10 referrals |
| USER-008 | `test_referred` | Referred | Referral recipient | 5 SOL |
| USER-009 | `test_points_seed` | Seed Rank | Points 0-499 | 2 SOL |
| USER-010 | `test_points_tree` | Tree Rank | Points 10,000+ | 10 SOL |

### 1.2 Test Wallet Addresses

| Wallet ID | Address (Truncated) | Purpose |
|-----------|---------------------|---------|
| WALLET-001 | `7xK9...mP3q` | Main test wallet |
| WALLET-002 | `8yL0...nQ4r` | Secondary test wallet |
| WALLET-003 | `9zM1...oR5s` | Empty wallet testing |
| WALLET-004 | `AaN2...pS6t` | Low balance (< 0.01 SOL) |
| WALLET-005 | `BbO3...qT7u` | Large balance whale |

### 1.3 Account States

```json
// USER-002: test_creator profile
{
  "username": "test_creator",
  "displayName": "Test Creator Account",
  "walletAddress": "7xK9...mP3q",
  "bio": "This is a test creator account for QA testing",
  "avatar": "https://test-assets.pumpfun.io/avatar-creator.png",
  "socialLinks": {
    "twitter": "https://twitter.com/test_creator",
    "telegram": "https://t.me/test_creator"
  },
  "privacy": {
    "profileVisibility": "public",
    "showHoldings": true,
    "showTransactions": true
  },
  "points": 5500,
  "rank": "Sapling",
  "createdAt": "2026-01-01T00:00:00Z"
}
```

---

## 2. TEST TOKENS

### 2.1 Token List

| Token ID | Name | Symbol | Status | Market Cap | Purpose |
|----------|------|--------|--------|------------|---------|
| TKN-001 | Test Meme High | TMHI | Active | $85,000 | High MC testing |
| TKN-002 | Test Meme Low | TMLO | Active | $5,000 | Low MC testing |
| TKN-003 | Test Graduated | TGRD | Graduated | $150,000 | Graduation testing |
| TKN-004 | Test NSFW Token | TNSF | Active | $25,000 | NSFW filter testing |
| TKN-005 | Test Trusted | TTRS | Active | $45,000 | Trust badges testing |
| TKN-006 | Test Volume | TVOL | Active | $30,000 | High volume testing |
| TKN-007 | Test New | TNEW | Active | $8,000 | New token testing |
| TKN-008 | Test Trending | TTRD | Active | $55,000 | Trending algorithm |
| TKN-009 | Test Favorite | TFAV | Active | $20,000 | Favorites testing |
| TKN-010 | Test Search | SRCH | Active | $15,000 | Search testing |

### 2.2 Token Configurations

```json
// TKN-005: Test Trusted Token
{
  "address": "TTrs123...abc",
  "name": "Test Trusted",
  "symbol": "TTRS",
  "description": "Token for testing trust level features",
  "avatar": "https://test-assets.pumpfun.io/ttrs-avatar.png",
  "creator": "test_creator",
  "createdAt": "2026-01-15T00:00:00Z",
  "totalSupply": 1000000000,
  "currentPrice": 0.000045,
  "marketCap": 45000,
  "volume24h": 12500,
  "priceChange24h": 5.5,
  "holders": 156,
  "liquidity": 25.5,
  "trustLevel": {
    "lpLocked": true,
    "lpLockPercent": 80,
    "lpLockDuration": "6 months",
    "audited": true,
    "auditFirm": "Test Audit Co",
    "auditDate": "2026-01-20",
    "freezeAuthorityDisabled": true
  },
  "isNSFW": false,
  "status": "active"
}
```

### 2.3 Token Price Data (Chart Testing)

| Token | 1H | 24H | 7D | 30D |
|-------|-----|------|-----|------|
| TMHI | +2.5% | +15.3% | +45.2% | +120.5% |
| TMLO | -1.2% | -8.5% | -25.3% | -45.0% |
| TGRD | +0.5% | +3.2% | +12.1% | +85.3% |
| TTRD | +8.5% | +35.2% | +125.5% | +250.0% |

---

## 3. TEST TRANSACTIONS

### 3.1 Transaction History Data

| TX ID | Type | Token | User | Amount | SOL Value | Timestamp |
|-------|------|-------|------|--------|-----------|-----------|
| TX-001 | BUY | TMHI | test_trader | 50,000 | 0.5 | 2h ago |
| TX-002 | SELL | TMHI | test_whale | 100,000 | 1.2 | 3h ago |
| TX-003 | BUY | TMLO | test_new | 10,000 | 0.1 | 5h ago |
| TX-004 | BUY | TTRS | test_trader | 25,000 | 0.25 | 1d ago |
| TX-005 | SELL | TTRS | test_creator | 15,000 | 0.18 | 2d ago |

### 3.2 Transaction Templates

```json
// Successful BUY transaction
{
  "transactionHash": "5XyZ123...abc",
  "type": "buy",
  "tokenAddress": "TTrs123...abc",
  "trader": "test_trader",
  "amountIn": 0.5,
  "amountInCurrency": "SOL",
  "amountOut": 50000,
  "amountOutCurrency": "TTRS",
  "pricePerToken": 0.00001,
  "fees": {
    "network": 0.00001,
    "antiMEV": 0.0025
  },
  "timestamp": "2026-02-04T10:30:00Z",
  "status": "confirmed"
}
```

---

## 4. TEST HOLDERS DATA

### 4.1 Holder Distribution (TKN-005: TTRS)

| Rank | Address | Username | Balance | % Supply | Badges |
|------|---------|----------|---------|----------|--------|
| 1 | 7xK9...mP3q | test_creator | 100,000,000 | 10.0% | 👑 Creator |
| 2 | BbO3...qT7u | test_whale | 80,000,000 | 8.0% | 🐋 Whale |
| 3 | 8yL0...nQ4r | test_trader | 25,000,000 | 2.5% | 💎 Diamond |
| 4-100 | Various | Various | <25M each | <2.5% | - |

### 4.2 Concentration Metrics

| Token | Top 10 % | Risk Level |
|-------|----------|------------|
| TMHI | 35% | 🟢 Low |
| TMLO | 55% | 🟡 Medium |
| TTRS | 42% | 🟡 Medium |
| TGRD | 28% | 🟢 Low |

---

## 5. TEST REFERRAL DATA

### 5.1 Referrer Account (USER-007)

```json
{
  "username": "test_referrer",
  "referralCode": "TESTREF123",
  "referralLink": "https://pumpfun.io/ref/TESTREF123",
  "stats": {
    "totalReferrals": 10,
    "activeReferrals": 8,
    "totalEarnings": 2.5,
    "totalEarningsUSD": 375.00,
    "unclaimedEarnings": 0.5,
    "claimedEarnings": 2.0
  }
}
```

### 5.2 Referred Users

| User | Joined | Trade Volume | Earnings |
|------|--------|--------------|----------|
| ref_user_1 | 30 days ago | 45.8 SOL | 0.092 SOL |
| ref_user_2 | 25 days ago | 32.5 SOL | 0.065 SOL |
| ref_user_3 | 20 days ago | 28.0 SOL | 0.056 SOL |
| ref_user_4 | 15 days ago | 15.2 SOL | 0.030 SOL |
| ref_user_5 | 10 days ago | 8.5 SOL | 0.017 SOL |

---

## 6. TEST POINTS DATA

### 6.1 Points Distribution

| User | Points | Rank | Activities |
|------|--------|------|------------|
| test_points_seed | 450 | 🌱 Seed | 5 trades |
| test_trader | 1,800 | 🌿 Sprout | 20 trades, 1 token |
| test_creator | 5,500 | 🌳 Sapling | 10 trades, 5 tokens |
| test_points_tree | 12,000 | 🌲 Tree | 50 trades, 10 tokens |
| test_whale | 55,000 | 🪷 Ancient Tree | 200 trades |

### 6.2 Points History Sample

| Date | Activity | Description | Points |
|------|----------|-------------|--------|
| 2026-02-04 | Trade | Bought 0.5 SOL of TTRS | +2.5 |
| 2026-02-03 | Referral | ref_user_5 traded 8.5 SOL | +85 |
| 2026-02-02 | Token Creation | Created TNEW token | +20 |
| 2026-02-01 | Trade | Sold 1.0 SOL of TMHI | +5 |

---

## 7. TEST REWARDS DATA

### 7.1 Reward Balance

| User | Tickets | Balance (SOL) | Spins Today |
|------|---------|---------------|-------------|
| test_trader | 5 | 0.025 | 2 |
| test_creator | 12 | 0.085 | 5 |
| test_new | 1 | 0.000 | 0 |

### 7.2 Slot Machine Results (Pre-defined)

| Spin ID | Reels | Match | Multiplier | Win |
|---------|-------|-------|------------|-----|
| SPIN-001 | 🌱🌱🌱🌿🌼 | 3 | 1x | 0.001 SOL |
| SPIN-002 | 🌿🌿🌿🌿🌳 | 4 | 2x | 0.002 SOL |
| SPIN-003 | 🌳🌱🌿🌼🍀 | 0 | - | 0 |
| SPIN-004 | 🌼🌼🌼🌼🌼 | 5 | 10x | 0.01 SOL |

---

## 8. TEST LIMIT ORDERS

### 8.1 Active Orders

| Order ID | User | Token | Type | Amount | Target | Current | Status |
|----------|------|-------|------|--------|--------|---------|--------|
| ORD-001 | test_trader | TMHI | BUY | 0.5 SOL | $0.00012 | $0.00010 | Active |
| ORD-002 | test_trader | TMLO | SELL | 50,000 | $0.000008 | $0.000006 | Active |
| ORD-003 | test_creator | TTRS | BUY | 1.0 SOL | $0.00004 | $0.000045 | Active |

### 8.2 Order Templates

```json
{
  "orderId": "ORD-001",
  "userId": "test_trader",
  "token": {
    "address": "TMhi123...abc",
    "name": "Test Meme High",
    "symbol": "TMHI"
  },
  "type": "buy",
  "amount": 0.5,
  "currency": "SOL",
  "targetPrice": 0.00012,
  "targetPriceType": "absolute",
  "currentPrice": 0.00010,
  "status": "active",
  "createdAt": "2026-02-04T08:00:00Z"
}
```

---

## 9. TEST CHAT MESSAGES

### 9.1 Chat History Sample (TTRS Token)

| Message ID | User | Content | Time |
|------------|------|---------|------|
| MSG-001 | test_trader | "Just bought some TTRS! 🚀" | 2m ago |
| MSG-002 | test_whale | "Nice entry point" | 5m ago |
| MSG-003 | test_creator | "Thanks for the support everyone!" | 10m ago |
| MSG-004 | test_new | "What's this token about?" | 15m ago |

### 9.2 Chat Test Data

```json
// Profanity test - should be filtered
{ "content": "This is a [bad_word] message" }

// Max length test - should fail (201 chars)
{ "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut." }

// Valid message
{ "content": "Great project! When moon? 🌙" }
```

---

## 10. TEST COMMUNITY POSTS

### 10.1 Posts for TTRS Token

| Post ID | Title | Content | Pinned | Created |
|---------|-------|---------|--------|---------|
| POST-001 | Welcome! | "Welcome to TTRS community..." | Yes | 7d ago |
| POST-002 | Roadmap Update | "Q1 2026 goals..." | No | 3d ago |
| POST-003 | Partnership | "Excited to announce..." | No | 1d ago |

---

## 11. NEGATIVE TEST DATA

### 11.1 Invalid Inputs

| Field | Invalid Value | Expected Error |
|-------|---------------|----------------|
| Username | `test@user!` | Invalid characters |
| Username | `ab` | Too short (min 3) |
| Symbol | `toolongsymbol` | Too long (max 10) |
| Amount | `-1` | Invalid amount |
| Amount | `0` | Amount required |
| Slippage | `60` | Max 50% |
| Wallet | `invalid_address` | Invalid wallet |
| URL | `notaurl` | Invalid URL |
| File | `malware.exe` | Invalid file type |
| File Size | `10MB.png` | File too large |

### 11.2 XSS Test Payloads

```javascript
const xssPayloads = [
  '<script>alert("XSS")</script>',
  '<img src=x onerror=alert("XSS")>',
  '"><script>alert("XSS")</script>',
  "javascript:alert('XSS')",
];

// Apply to: Username, Bio, Chat, Post Title/Content
```

### 11.3 SQL Injection Payloads

```sql
-- Apply to: Search, Filters
' OR '1'='1
' UNION SELECT * FROM users--
'; DROP TABLE tokens;--
```

---

## 12. ENVIRONMENT-SPECIFIC DATA

### 12.1 API Endpoints

| Environment | Base URL | WebSocket |
|-------------|----------|-----------|
| Development | http://localhost:3000/v1 | ws://localhost:3001 |
| Staging | https://api-staging.pumpfun.io/v1 | wss://ws-staging.pumpfun.io |
| Production | https://api.pumpfun.io/v1 | wss://ws.pumpfun.io |

### 12.2 Test Configuration

```json
// test-config.json
{
  "environment": "staging",
  "baseUrl": "https://api-staging.pumpfun.io/v1",
  "wsUrl": "wss://ws-staging.pumpfun.io",
  "testWallet": {
    "address": "7xK9...mP3q",
    "privateKey": "ENV_VARIABLE"
  },
  "timeouts": {
    "api": 10000,
    "transaction": 30000,
    "websocket": 5000
  }
}
```

---

## 13. DATA RESET PROCEDURES

### 13.1 Before Each Test Run

```bash
# Reset test data script
npm run test:reset

# Steps:
# 1. Clear test transactions older than 24h
# 2. Reset user balances to default
# 3. Clear test chat messages
# 4. Reset limit orders
# 5. Refresh token metrics
```

### 13.2 Database Seed Commands

```bash
# Seed all test data
npm run db:seed:test

# Seed specific data
npm run db:seed:users
npm run db:seed:tokens
npm run db:seed:transactions
```

---

**END OF TEST DATA REQUIREMENTS**
