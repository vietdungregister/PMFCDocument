# PUMPFUN CLONE - API TEST CASES

**Version:** 1.0 | **Created:** February 4, 2026

---

## 1. API OVERVIEW

### Base URLs
```
Production:  https://api.pumpfun.io/v1
Staging:     https://api-staging.pumpfun.io/v1
```

### Common Headers
```json
{
  "Content-Type": "application/json",
  "Authorization": "Bearer <JWT_TOKEN>",
  "X-Wallet-Address": "0x..."
}
```

---

## 2. AUTHENTICATION APIs

### API-AUTH-001: Connect Wallet
```
POST /auth/connect
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Valid wallet | `{"walletAddress": "7xK9...", "signature": "..."}` | 200, JWT token | High |
| Invalid address | `{"walletAddress": "invalid"}` | 400 Bad Request | High |
| Invalid signature | Wrong signature | 401 Unauthorized | Critical |
| Missing signature | No signature field | 400 Bad Request | High |

### API-AUTH-002: Verify Token
```
GET /auth/verify
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Valid token | Bearer <valid> | 200, user data | High |
| Expired token | Bearer <expired> | 401 Token Expired | High |
| Invalid token | Bearer <malformed> | 401 Invalid | High |
| Missing header | No Authorization | 401 Unauthorized | High |

### API-AUTH-003: Logout
```
POST /auth/logout
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Valid logout | Auth header | 200 OK | Medium |
| Already logged out | Reuse token | 401 Unauthorized | Medium |

---

## 3. TOKEN APIs

### API-TOKEN-001: Get Token List
```
GET /tokens?tab=discover&page=1&limit=20
```

| TC | Query | Expected | Priority |
|-----|-------|----------|----------|
| Default | `/tokens` | 200, paginated list | High |
| Tab trending | `?tab=trending` | 200, trending sorted | High |
| Pagination | `?page=2&limit=10` | 200, correct page | High |
| Search | `?search=pepe` | 200, filtered | High |
| MC filter | `?minMC=10000&maxMC=100000` | 200, within range | High |
| NSFW on | `?nsfw=true` | 200, includes NSFW | Medium |
| Invalid tab | `?tab=invalid` | 400 Bad Request | Medium |
| Combined filters | `?minMC=10000&nsfw=false` | 200, combined | High |

### API-TOKEN-002: Get Token Detail
```
GET /tokens/:address
```

| TC | Path | Expected | Priority |
|-----|------|----------|----------|
| Valid address | `/tokens/7xK9...` | 200, full data | High |
| Invalid | `/tokens/invalid` | 404 Not Found | High |

### API-TOKEN-003: Get Holders
```
GET /tokens/:address/holders
```

| TC | Query | Expected | Priority |
|-----|-------|----------|----------|
| Top 100 | No params | 200, max 100 | High |
| With limit | `?limit=50` | 200, 50 holders | Medium |

### API-TOKEN-004: Get Transactions
```
GET /tokens/:address/transactions
```

| TC | Query | Expected | Priority |
|-----|-------|----------|----------|
| Latest 50 | No params | 200, 50 txs | High |
| Filter buy | `?type=buy` | 200, only buys | Medium |

### API-TOKEN-005: Toggle Favorite
```
POST /tokens/:address/favorite
```

| TC | State | Expected | Priority |
|-----|-------|----------|----------|
| Add | Not favorited | 200, favorited: true | High |
| Remove | Already favorited | 200, favorited: false | High |
| No auth | Missing token | 401 Unauthorized | High |

### API-TOKEN-006: Send Chat
```
POST /tokens/:address/chat
```

| TC | Body | Expected | Priority |
|-----|------|----------|----------|
| Valid | `{"content": "Hello"}` | 201 Created | High |
| Empty | `{"content": ""}` | 400 Bad Request | High |
| Too long | 201+ chars | 400 Bad Request | Medium |
| Rate limit | 10 msgs/10s | 429 Too Many | High |

---

## 4. TRADING APIs

### API-TRADE-001: Market Order
```
POST /trading/market
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Valid BUY | type: buy, amount: 0.5 | 200, tx hash | Critical |
| Valid SELL | type: sell | 200, tx hash | Critical |
| Insufficient | amount > balance | 400 Insufficient | Critical |
| Invalid token | Bad address | 404 Not Found | High |
| Zero amount | amount: 0 | 400 Bad Request | High |
| No auth | Missing token | 401 Unauthorized | High |

### API-TRADE-002: Create Limit Order
```
POST /trading/limit
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Valid BUY | Valid body | 201 Created | High |
| Valid SELL | type: sell | 201 Created | High |
| Same as current | target = current | 400 Invalid | Medium |

### API-TRADE-003: Cancel Limit Order
```
DELETE /trading/limit/orders/:id
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Valid cancel | Active order | 200 OK | High |
| Already cancelled | Cancelled | 400 Already Cancelled | Medium |
| Not owner | Other's order | 403 Forbidden | High |

### API-TRADE-004: Get Price Quote
```
GET /trading/quote?token=addr&type=buy&amount=0.5
```

| TC | Query | Expected | Priority |
|-----|-------|----------|----------|
| BUY quote | Valid params | 200, estimated output | High |
| SELL quote | type=sell | 200, estimated SOL | High |
| Invalid token | Bad address | 404 Not Found | Medium |

---

## 5. USER PROFILE APIs

### API-PROFILE-001: Get My Profile
```
GET /users/me
```

| TC | Auth | Expected | Priority |
|-----|------|----------|----------|
| Authenticated | Valid token | 200, full profile | High |
| No auth | Missing | 401 Unauthorized | High |

### API-PROFILE-002: Update Profile
```
PATCH /users/me
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Set username 1st | username: "unique" | 200 OK | Critical |
| Change after set | Already has | 400 Locked | Critical |
| Duplicate | Existing username | 400 Taken | High |
| Update bio | bio: "new" | 200 OK | Medium |

### API-PROFILE-003: Update Privacy
```
PATCH /users/me/privacy
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Set private | profileVisibility: private | 200 OK | High |
| Hide holdings | showHoldings: false | 200 OK | High |

### API-PROFILE-004: Get Holdings
```
GET /users/me/holdings
```

| TC | Query | Expected | Priority |
|-----|-------|----------|----------|
| All | No params | 200, with P&L | High |
| Sorted | `?sort=value` | 200, sorted | Medium |

### API-PROFILE-005: Get Public Profile
```
GET /users/:username
```

| TC | User | Expected | Priority |
|-----|------|----------|----------|
| Public user | Public profile | 200, full data | High |
| Private user | Private | 200, limited | High |
| Not found | Non-existent | 404 Not Found | Medium |

---

## 6. CREATOR APIs

### API-CREATOR-001: Get Dashboard
```
GET /creator/dashboard
```

| TC | Auth | Expected | Priority |
|-----|------|----------|----------|
| Has tokens | Valid creator | 200, data | High |
| No auth | Missing | 401 Unauthorized | High |

### API-CREATOR-002: Claim Revenue
```
POST /creator/revenue/claim
```

| TC | State | Expected | Priority |
|-----|-------|----------|----------|
| Has unclaimed | > 0 | 200, tx hash | Critical |
| Nothing | = 0 | 400 Nothing | High |

### API-CREATOR-003: Update Trust Settings
```
PATCH /creator/tokens/:address/trust
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Enable LP Lock | lpLocked: true | 200 OK | High |
| Disable Freeze | freezeDisabled: true | 200, permanent | Critical |
| Re-enable Freeze | After disabled | 400 Permanent | High |

### API-CREATOR-004: CRUD Posts
```
POST /creator/tokens/:address/posts
PATCH /creator/tokens/:address/posts/:id
DELETE /creator/tokens/:address/posts/:id
```

| TC | Action | Expected | Priority |
|-----|--------|----------|----------|
| Create post | title, content | 201 Created | High |
| Pin post | pinned: true | 200 OK | Medium |
| Delete post | Valid ID | 200 OK | High |
| Not owner | Other's token | 403 Forbidden | High |

---

## 7. REFERRAL & POINTS APIs

### API-REF-001: Get Referral Info
```
GET /referral
```

| TC | Auth | Expected | Priority |
|-----|------|----------|----------|
| Valid | Auth header | 200, referral data | High |

### API-REF-002: Claim Referral
```
POST /referral/claim
```

| TC | State | Expected | Priority |
|-----|-------|----------|----------|
| Has unclaimed | > 0 | 200, tx hash | Critical |
| Nothing | = 0 | 400 Nothing | High |

### API-REF-003: Apply Code
```
POST /referral/apply
```

| TC | Input | Expected | Priority |
|-----|-------|----------|----------|
| Valid code | `{"code": "abc"}` | 200 OK | High |
| Invalid | Non-existent | 404 Not Found | High |
| Self refer | Own code | 400 Cannot Self | High |

### API-POINTS-001: Get Points
```
GET /points
```

| TC | Auth | Expected | Priority |
|-----|------|----------|----------|
| Valid | Auth header | 200, points & rank | High |

---

## 8. REWARDS APIs

### API-REWARD-001: Spin Slot
```
POST /rewards/spin
```

| TC | State | Expected | Priority |
|-----|-------|----------|----------|
| Has tickets | > 0 | 200, spin result | Critical |
| No tickets | = 0 | 400 No Tickets | Critical |

---

## 9. ERROR HANDLING

| Error Code | HTTP | Trigger |
|------------|------|---------|
| UNAUTHORIZED | 401 | No/invalid token |
| TOKEN_EXPIRED | 401 | Expired JWT |
| FORBIDDEN | 403 | No permission |
| NOT_FOUND | 404 | Missing resource |
| VALIDATION_ERROR | 400 | Invalid input |
| RATE_LIMITED | 429 | Too many requests |
| INSUFFICIENT_BALANCE | 400 | Not enough SOL |
| GEOLOCATION_BLOCKED | 403 | Vietnam IP |

### Rate Limits

| Endpoint | Limit | Window |
|----------|-------|--------|
| POST /auth/connect | 5 | 1 min |
| POST /trading/market | 10 | 1 min |
| POST /tokens/:id/chat | 10 | 10 sec |
| GET /tokens | 100 | 1 min |

---

## 📋 EXECUTION TRACKING

| Section | Total | Status |
|---------|-------|--------|
| Authentication | 10 | ⏳ |
| Token APIs | 20 | ⏳ |
| Trading APIs | 15 | ⏳ |
| Profile APIs | 12 | ⏳ |
| Creator APIs | 12 | ⏳ |
| Referral/Points | 8 | ⏳ |
| Rewards | 4 | ⏳ |
| Errors | 8 | ⏳ |
| **TOTAL** | **89** | **0%** |

---

**END OF API TEST CASES**
