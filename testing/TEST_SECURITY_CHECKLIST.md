# PUMPFUN CLONE - SECURITY TESTING CHECKLIST

**Version:** 1.0 | **Created:** February 4, 2026

---

## 📋 MỤC LỤC

1. [Authentication & Authorization](#1-authentication--authorization)
2. [Input Validation & Injection](#2-input-validation--injection)
3. [Session Management](#3-session-management)
4. [API Security](#4-api-security)
5. [Wallet & Blockchain Security](#5-wallet--blockchain-security)
6. [Data Protection](#6-data-protection)
7. [Frontend Security](#7-frontend-security)
8. [Infrastructure Security](#8-infrastructure-security)
9. [Business Logic Security](#9-business-logic-security)
10. [Compliance & Geolocation](#10-compliance--geolocation)

---

## 1. AUTHENTICATION & AUTHORIZATION

### 1.1 Wallet Authentication

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| AUTH-001 | Signature verification | Send invalid signature | Reject with 401 | ⬜ |
| AUTH-002 | Signature replay attack | Reuse old signature | Reject (nonce/timestamp) | ⬜ |
| AUTH-003 | Wallet address validation | Send malformed address | Reject with 400 | ⬜ |
| AUTH-004 | JWT token generation | Verify token structure | Valid JWT with expiry | ⬜ |
| AUTH-005 | Token expiration | Use expired token | Reject with 401 | ⬜ |
| AUTH-006 | Refresh token security | Verify refresh flow | New tokens, old revoked | ⬜ |
| AUTH-007 | Logout invalidation | Use token after logout | Reject with 401 | ⬜ |

### 1.2 Authorization Checks

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| AUTHZ-001 | Resource ownership | Access other user's data | 403 Forbidden | ⬜ |
| AUTHZ-002 | Token management | Manage non-owned token | 403 Forbidden | ⬜ |
| AUTHZ-003 | Limit order cancellation | Cancel other's order | 403 Forbidden | ⬜ |
| AUTHZ-004 | Profile editing | Edit other's profile | 403 Forbidden | ⬜ |
| AUTHZ-005 | Revenue claiming | Claim other's revenue | 403 Forbidden | ⬜ |
| AUTHZ-006 | Post management | Edit/delete other's post | 403 Forbidden | ⬜ |
| AUTHZ-007 | Private profile access | Access hidden data | 403 or filtered response | ⬜ |

---

## 2. INPUT VALIDATION & INJECTION

### 2.1 SQL Injection

| ID | Check | Payload | Location | Status |
|----|-------|---------|----------|--------|
| SQLI-001 | Basic SQL injection | `' OR '1'='1` | Login, search fields | ⬜ |
| SQLI-002 | Union-based | `' UNION SELECT * FROM users--` | Token search | ⬜ |
| SQLI-003 | Blind SQL injection | `' AND 1=1--` | All input fields | ⬜ |
| SQLI-004 | Time-based blind | `'; WAITFOR DELAY '0:0:5'--` | All inputs | ⬜ |
| SQLI-005 | Error-based | `' AND 1=CONVERT(int,(SELECT @@version))--` | Forms | ⬜ |

**Test Script:**
```bash
# Using sqlmap
sqlmap -u "https://api.pumpfun.io/v1/tokens?search=test" --level=5 --risk=3
```

### 2.2 XSS (Cross-Site Scripting)

| ID | Check | Payload | Location | Status |
|----|-------|---------|----------|--------|
| XSS-001 | Reflected XSS | `<script>alert(1)</script>` | Search, URL params | ⬜ |
| XSS-002 | Stored XSS | `<script>alert(1)</script>` | Chat, profile bio | ⬜ |
| XSS-003 | DOM XSS | `javascript:alert(1)` | URL, redirects | ⬜ |
| XSS-004 | Event handler XSS | `<img onerror="alert(1)">` | Avatar URL, social links | ⬜ |
| XSS-005 | SVG XSS | `<svg onload="alert(1)">` | Image uploads | ⬜ |
| XSS-006 | HTML entity bypass | `&lt;script&gt;` | All text inputs | ⬜ |
| XSS-007 | Unicode bypass | `\u003cscript\u003e` | All inputs | ⬜ |

**Test Payloads:**
```javascript
// Common XSS payloads to test
const xssPayloads = [
  '<script>alert("XSS")</script>',
  '<img src=x onerror=alert("XSS")>',
  '<svg/onload=alert("XSS")>',
  '"><script>alert("XSS")</script>',
  "'-alert('XSS')-'",
  '<body onload=alert("XSS")>',
  '<input onfocus=alert("XSS") autofocus>',
];
```

### 2.3 NoSQL Injection

| ID | Check | Payload | Location | Status |
|----|-------|---------|----------|--------|
| NOSQL-001 | Query operator injection | `{"$gt": ""}` | JSON body fields | ⬜ |
| NOSQL-002 | Where clause injection | `{$where: "sleep(5000)"}` | Query params | ⬜ |
| NOSQL-003 | Regex DoS | `{"$regex": "^(a+)+$"}` | Search fields | ⬜ |

### 2.4 Command Injection

| ID | Check | Payload | Location | Status |
|----|-------|---------|----------|--------|
| CMD-001 | OS command injection | `; ls -la` | File upload names | ⬜ |
| CMD-002 | Pipe injection | `| cat /etc/passwd` | Any processed field | ⬜ |

### 2.5 Input Validation

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| VAL-001 | Username format | Special chars, spaces | Only alphanumeric + underscore | ⬜ |
| VAL-002 | Username length | 1 char, 100 chars | 3-32 characters | ⬜ |
| VAL-003 | Token name length | 0, 50 chars | 1-32 characters | ⬜ |
| VAL-004 | Symbol format | lowercase, special | Uppercase, 2-10 chars | ⬜ |
| VAL-005 | Bio length | 300 chars | Max 200 characters | ⬜ |
| VAL-006 | Chat message length | 300 chars | Max 200 characters | ⬜ |
| VAL-007 | URL validation | Invalid URLs | Proper URL format | ⬜ |
| VAL-008 | Numeric ranges | Negative, huge numbers | Within valid range | ⬜ |
| VAL-009 | File upload type | .exe, .php | Only PNG, JPG, GIF | ⬜ |
| VAL-010 | File upload size | 10MB file | Max 5MB | ⬜ |

---

## 3. SESSION MANAGEMENT

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| SESS-001 | Session timeout | Wait for timeout | Auto logout after X mins | ⬜ |
| SESS-002 | Concurrent sessions | Login from 2 devices | Policy enforced | ⬜ |
| SESS-003 | Session fixation | Pre-set session ID | New session on login | ⬜ |
| SESS-004 | Secure cookie flags | Inspect cookies | HttpOnly, Secure, SameSite | ⬜ |
| SESS-005 | Session invalidation | Logout | Token blacklisted | ⬜ |
| SESS-006 | Sensitive action re-auth | Claim funds | Re-verify wallet | ⬜ |

**Cookie Inspection:**
```javascript
// Check cookie attributes
document.cookie  // Should not show HttpOnly cookies

// Verify in DevTools Network tab:
// Set-Cookie: token=xxx; HttpOnly; Secure; SameSite=Strict; Path=/
```

---

## 4. API SECURITY

### 4.1 Rate Limiting

| ID | Endpoint | Limit | Window | Test | Status |
|----|----------|-------|--------|------|--------|
| RATE-001 | POST /auth/connect | 5 | 1 min | 6th request | ⬜ |
| RATE-002 | POST /trading/market | 10 | 1 min | 11th request | ⬜ |
| RATE-003 | POST /tokens/:id/chat | 10 | 10 sec | Spam messages | ⬜ |
| RATE-004 | GET /tokens | 100 | 1 min | 101st request | ⬜ |
| RATE-005 | POST /creator/revenue/claim | 1 | 1 min | Double claim | ⬜ |

**Test Script:**
```bash
# Test rate limiting
for i in {1..15}; do
  curl -X POST https://api.pumpfun.io/v1/auth/connect \
    -H "Content-Type: application/json" \
    -d '{"walletAddress":"test","signature":"test"}' \
    -w "\n%{http_code}\n"
done
```

### 4.2 CORS Configuration

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| CORS-001 | Allowed origins | Request from unknown origin | CORS error | ⬜ |
| CORS-002 | Wildcard check | Check for `*` | Only specific domains | ⬜ |
| CORS-003 | Credentials handling | withCredentials: true | Proper handling | ⬜ |
| CORS-004 | Preflight caching | OPTIONS request | Appropriate max-age | ⬜ |

### 4.3 HTTP Headers

| Header | Expected Value | Status |
|--------|---------------|--------|
| X-Content-Type-Options | nosniff | ⬜ |
| X-Frame-Options | DENY or SAMEORIGIN | ⬜ |
| X-XSS-Protection | 1; mode=block | ⬜ |
| Strict-Transport-Security | max-age=31536000; includeSubDomains | ⬜ |
| Content-Security-Policy | Configured properly | ⬜ |
| Referrer-Policy | strict-origin-when-cross-origin | ⬜ |
| Cache-Control | no-store (for sensitive data) | ⬜ |

**Check Command:**
```bash
curl -I https://api.pumpfun.io/v1/tokens | grep -i "x-"
```

### 4.4 API Abuse Prevention

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| ABUSE-001 | Parameter tampering | Modify hidden params | Ignored or validated | ⬜ |
| ABUSE-002 | Mass assignment | Extra fields in POST | Only allowed fields | ⬜ |
| ABUSE-003 | IDOR | Change resource IDs | 403 or proper auth | ⬜ |
| ABUSE-004 | HTTP method override | X-HTTP-Method-Override | Not allowed | ⬜ |
| ABUSE-005 | Large payload | 10MB JSON body | 413 Payload Too Large | ⬜ |

---

## 5. WALLET & BLOCKCHAIN SECURITY

### 5.1 Wallet Integration

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| WALLET-001 | Signature validation | Tampered signature | Reject transaction | ⬜ |
| WALLET-002 | Address validation | Invalid Solana address | Reject with error | ⬜ |
| WALLET-003 | Transaction confirmation | Wait for confirmation | Only after blockchain confirm | ⬜ |
| WALLET-004 | Replay protection | Resubmit signed tx | Reject duplicate | ⬜ |
| WALLET-005 | Front-running protection | Anti-MEV check | MEV protection active | ⬜ |

### 5.2 Smart Contract Security

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| SC-001 | Reentrancy | Recursive call | Protected or reverts | ⬜ |
| SC-002 | Integer overflow | Large numbers | SafeMath or checked | ⬜ |
| SC-003 | Access control | Unauthorized call | Only owner/authorized | ⬜ |
| SC-004 | Withdrawal pattern | Fund withdrawal | Pull over push pattern | ⬜ |
| SC-005 | Slippage protection | High slippage | Transaction reverts | ⬜ |

### 5.3 Trading Security

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| TRADE-001 | Balance verification | Trade > balance | Reject before blockchain | ⬜ |
| TRADE-002 | Slippage enforcement | Price move > tolerance | Transaction fails | ⬜ |
| TRADE-003 | Rate limiting | Rapid trades | Rate limited | ⬜ |
| TRADE-004 | Price manipulation | Unusual price | Detection/alert | ⬜ |
| TRADE-005 | Double spending | Spend same funds twice | Only first succeeds | ⬜ |

---

## 6. DATA PROTECTION

### 6.1 Sensitive Data Handling

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| DATA-001 | Wallet PK exposure | Check logs, responses | Never exposed | ⬜ |
| DATA-002 | Password/secrets in code | Code review | No hardcoded secrets | ⬜ |
| DATA-003 | API key exposure | Frontend JS | Keys server-side only | ⬜ |
| DATA-004 | Personal data in logs | Log analysis | PII redacted | ⬜ |
| DATA-005 | Encryption at rest | Database check | Sensitive data encrypted | ⬜ |
| DATA-006 | Encryption in transit | TLS check | TLS 1.2+ only | ⬜ |

### 6.2 Privacy Settings

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| PRIV-001 | Private profile | View private user | Only created tokens visible | ⬜ |
| PRIV-002 | Hidden holdings | View hidden holdings | 403 or no data | ⬜ |
| PRIV-003 | Hidden transactions | View hidden txs | 403 or no data | ⬜ |
| PRIV-004 | API respects privacy | API call for private data | Filtered response | ⬜ |

### 6.3 Data Minimization

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| MIN-001 | Unnecessary data | API responses | Only required fields | ⬜ |
| MIN-002 | Internal IDs | Response analysis | No internal IDs exposed | ⬜ |
| MIN-003 | Debug information | Error responses | No stack traces in prod | ⬜ |

---

## 7. FRONTEND SECURITY

### 7.1 Content Security Policy

```
Content-Security-Policy: 
  default-src 'self';
  script-src 'self' https://trusted-cdn.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  connect-src 'self' https://api.pumpfun.io wss://ws.pumpfun.io;
  frame-ancestors 'none';
  form-action 'self';
```

| ID | Check | Test | Status |
|----|-------|------|--------|
| CSP-001 | Script-src restriction | Inline script | Blocked | ⬜ |
| CSP-002 | Connect-src restriction | External API | Blocked | ⬜ |
| CSP-003 | Frame-ancestors | iframe embedding | Blocked | ⬜ |

### 7.2 Client-Side Security

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| CLIENT-001 | localStorage sensitive data | DevTools check | No secrets stored | ⬜ |
| CLIENT-002 | sessionStorage | DevTools check | Minimal sensitive data | ⬜ |
| CLIENT-003 | Console logging | Production check | No sensitive logs | ⬜ |
| CLIENT-004 | Source maps | Production build | No source maps public | ⬜ |
| CLIENT-005 | Dependency vulnerabilities | npm audit | No high/critical vulns | ⬜ |

**Commands:**
```bash
# Check for vulnerabilities
npm audit --production
npx snyk test
```

---

## 8. INFRASTRUCTURE SECURITY

### 8.1 Server Configuration

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| INFRA-001 | SSL/TLS configuration | SSL Labs test | Grade A or A+ | ⬜ |
| INFRA-002 | Certificate validity | SSL check | Valid, not expiring soon | ⬜ |
| INFRA-003 | HTTP to HTTPS redirect | HTTP request | 301 redirect | ⬜ |
| INFRA-004 | Server version hiding | Response headers | No version info | ⬜ |
| INFRA-005 | Directory listing | Access /assets/ | 403 or index | ⬜ |
| INFRA-006 | Backup file exposure | /.git, /backup | 404 Not Found | ⬜ |
| INFRA-007 | Admin panel exposure | /admin, /wp-admin | Protected or 404 | ⬜ |

**SSL Test:**
```bash
# Test SSL configuration
curl https://www.ssllabs.com/ssltest/analyze.html?d=pumpfun.io
```

### 8.2 WebSocket Security

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| WS-001 | WSS only | HTTP WS connection | Rejected | ⬜ |
| WS-002 | Origin validation | Wrong origin | Connection rejected | ⬜ |
| WS-003 | Authentication | No auth token | Connection rejected | ⬜ |
| WS-004 | Message validation | Malformed message | Error, no crash | ⬜ |
| WS-005 | Rate limiting | Spam messages | Throttled/blocked | ⬜ |

---

## 9. BUSINESS LOGIC SECURITY

### 9.1 Trading Logic

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| BIZ-001 | Negative amount | amount: -1 | Rejected | ⬜ |
| BIZ-002 | Zero amount | amount: 0 | Rejected | ⬜ |
| BIZ-003 | Fractional abuse | 0.00000001 SOL | Within limits | ⬜ |
| BIZ-004 | Self-trading | Buy own token | Allowed but tracked | ⬜ |
| BIZ-005 | Slippage bypass | slippage: 100% | Capped or warned | ⬜ |

### 9.2 Token Creation

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| BIZ-006 | Duplicate symbol | Existing symbol | Rejected | ⬜ |
| BIZ-007 | Reserved names | "Solana", "Bitcoin" | Rejected | ⬜ |
| BIZ-008 | Offensive content | Profanity | Filtered/rejected | ⬜ |
| BIZ-009 | Impersonation | Similar to famous token | Warning/rejected | ⬜ |

### 9.3 Referral Abuse

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| BIZ-010 | Self-referral | Own referral code | Rejected | ⬜ |
| BIZ-011 | Referral farming | Multiple accounts, same IP | Detection | ⬜ |
| BIZ-012 | Wash trading referral | Back-and-forth trading | NetVolume-based | ⬜ |

### 9.4 Points Abuse

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| BIZ-013 | Wash trading | Buy then immediate sell | NetVolume-based points | ⬜ |
| BIZ-014 | Token creation abuse | Create many tokens | Only active tokens count | ⬜ |
| BIZ-015 | Multiple accounts | Same IP farming | Detection/limitation | ⬜ |

### 9.5 Username/Profile

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| BIZ-016 | Username change attempt | After first save | Permanently locked | ⬜ |
| BIZ-017 | Display name change | After first save | Permanently locked | ⬜ |
| BIZ-018 | Impersonation username | "admin", "support" | Reserved/rejected | ⬜ |

---

## 10. COMPLIANCE & GEOLOCATION

### 10.1 Vietnam Block

| ID | Check | Test Method | Pass Criteria | Status |
|----|-------|-------------|---------------|--------|
| GEO-001 | Direct VN IP | Vietnam IP address | 403 Blocked | ⬜ |
| GEO-002 | VN mobile carrier | Mobile network | 403 Blocked | ⬜ |
| GEO-003 | Known VN VPN exits | VPN endpoints | Consider blocking | ⬜ |
| GEO-004 | Geolocation header | X-Forwarded-For VN | Blocked | ⬜ |
| GEO-005 | Bypass attempts | X-Originating-IP | Checked | ⬜ |

**Test with VPN:**
```bash
# Test from Vietnam IP
curl -H "X-Forwarded-For: 113.160.xxx.xxx" https://api.pumpfun.io/v1/tokens
# Expected: 403 Forbidden with GEOLOCATION_BLOCKED error
```

### 10.2 Compliance Checks

| ID | Check | Status |
|----|-------|--------|
| COMP-001 | Terms of Service displayed | ⬜ |
| COMP-002 | Privacy Policy displayed | ⬜ |
| COMP-003 | Cookie consent (if applicable) | ⬜ |
| COMP-004 | Age verification (if required) | ⬜ |
| COMP-005 | Risk disclaimers | ⬜ |

---

## 📋 EXECUTION SUMMARY

### By Category

| Category | Total | Passed | Failed | Status |
|----------|-------|--------|--------|--------|
| Authentication | 14 | - | - | ⏳ |
| Injection/Validation | 27 | - | - | ⏳ |
| Session | 6 | - | - | ⏳ |
| API Security | 19 | - | - | ⏳ |
| Wallet/Blockchain | 15 | - | - | ⏳ |
| Data Protection | 13 | - | - | ⏳ |
| Frontend | 8 | - | - | ⏳ |
| Infrastructure | 12 | - | - | ⏳ |
| Business Logic | 18 | - | - | ⏳ |
| Geolocation | 7 | - | - | ⏳ |
| **TOTAL** | **139** | **0** | **0** | **0%** |

### Priority Summary

| Priority | Count | Must Pass |
|----------|-------|-----------|
| Critical | 25 | 100% |
| High | 60 | 95% |
| Medium | 54 | 90% |

---

## 🔧 SECURITY TESTING TOOLS

| Tool | Purpose | Command |
|------|---------|---------|
| OWASP ZAP | Web app scanning | `zap-baseline.py -t https://pumpfun.io` |
| Burp Suite | Manual testing | GUI tool |
| sqlmap | SQL injection | `sqlmap -u <url>` |
| Nmap | Port scanning | `nmap -sV pumpfun.io` |
| SSL Labs | SSL testing | Online tool |
| npm audit | Dependency check | `npm audit` |
| Snyk | Security scanning | `snyk test` |

---

**END OF SECURITY TESTING CHECKLIST**
