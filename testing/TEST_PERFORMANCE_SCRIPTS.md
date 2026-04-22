# PUMPFUN CLONE - PERFORMANCE TEST SCRIPTS

**Version:** 1.0 | **Created:** February 4, 2026

---

## 1. PERFORMANCE TESTING OVERVIEW

### 1.1 Objectives
- Page load time < 3 seconds
- API response time < 500ms (95th percentile)
- Support 1,000 concurrent users
- Real-time updates latency < 500ms
- Trading transaction < 3 seconds

### 1.2 Tools
- **k6** - Load testing
- **Lighthouse** - Frontend performance
- **WebSocket Tester** - Real-time testing
- **Grafana** - Monitoring

---

## 2. LOAD TEST SCENARIOS

### 2.1 Token List Load Test (k6)

```javascript
// k6-token-list.js
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate, Trend } from 'k6/metrics';

const errorRate = new Rate('errors');
const tokenListDuration = new Trend('token_list_duration');

export const options = {
  stages: [
    { duration: '1m', target: 100 },   // Ramp up to 100 users
    { duration: '3m', target: 100 },   // Stay at 100
    { duration: '1m', target: 500 },   // Ramp up to 500
    { duration: '5m', target: 500 },   // Stay at 500
    { duration: '2m', target: 1000 },  // Peak at 1000
    { duration: '3m', target: 1000 },  // Stay at 1000
    { duration: '2m', target: 0 },     // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% requests < 500ms
    errors: ['rate<0.01'],              // Error rate < 1%
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://api-staging.pumpfun.io/v1';

export default function () {
  // Test discover tab (default)
  const discoverRes = http.get(`${BASE_URL}/tokens?tab=discover&limit=20`);
  
  check(discoverRes, {
    'discover status 200': (r) => r.status === 200,
    'discover has tokens': (r) => JSON.parse(r.body).data.tokens.length > 0,
  });
  
  tokenListDuration.add(discoverRes.timings.duration);
  errorRate.add(discoverRes.status !== 200);
  
  sleep(1);
  
  // Test trending tab
  const trendingRes = http.get(`${BASE_URL}/tokens?tab=trending&limit=20`);
  
  check(trendingRes, {
    'trending status 200': (r) => r.status === 200,
  });
  
  sleep(1);
  
  // Test with filters
  const filteredRes = http.get(`${BASE_URL}/tokens?minMC=10000&maxMC=100000&limit=20`);
  
  check(filteredRes, {
    'filtered status 200': (r) => r.status === 200,
  });
  
  sleep(1);
  
  // Test search
  const searchRes = http.get(`${BASE_URL}/tokens?search=test&limit=20`);
  
  check(searchRes, {
    'search status 200': (r) => r.status === 200,
  });
  
  sleep(Math.random() * 3 + 1);
}
```

**Run Command:**
```bash
k6 run --env BASE_URL=https://api-staging.pumpfun.io/v1 k6-token-list.js
```

### 2.2 Token Detail Load Test

```javascript
// k6-token-detail.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 200 },
    { duration: '5m', target: 200 },
    { duration: '2m', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<800'],
    http_req_failed: ['rate<0.01'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://api-staging.pumpfun.io/v1';
const TEST_TOKEN = __ENV.TOKEN_ADDRESS || 'TestToken123';

export default function () {
  // Get token detail
  const detailRes = http.get(`${BASE_URL}/tokens/${TEST_TOKEN}`);
  check(detailRes, { 'detail 200': (r) => r.status === 200 });
  sleep(0.5);
  
  // Get holders
  const holdersRes = http.get(`${BASE_URL}/tokens/${TEST_TOKEN}/holders`);
  check(holdersRes, { 'holders 200': (r) => r.status === 200 });
  sleep(0.5);
  
  // Get transactions
  const txRes = http.get(`${BASE_URL}/tokens/${TEST_TOKEN}/transactions`);
  check(txRes, { 'transactions 200': (r) => r.status === 200 });
  sleep(0.5);
  
  // Get chat
  const chatRes = http.get(`${BASE_URL}/tokens/${TEST_TOKEN}/chat`);
  check(chatRes, { 'chat 200': (r) => r.status === 200 });
  
  sleep(Math.random() * 2 + 1);
}
```

### 2.3 Trading API Stress Test

```javascript
// k6-trading.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  scenarios: {
    trading_load: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '1m', target: 50 },
        { duration: '3m', target: 50 },
        { duration: '1m', target: 0 },
      ],
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<1000'],
    http_req_failed: ['rate<0.05'],
  },
};

const BASE_URL = __ENV.BASE_URL;
const AUTH_TOKEN = __ENV.AUTH_TOKEN;
const TOKEN_ADDRESS = __ENV.TOKEN_ADDRESS;

export default function () {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${AUTH_TOKEN}`,
  };
  
  // Get quote first
  const quoteRes = http.get(
    `${BASE_URL}/trading/quote?token=${TOKEN_ADDRESS}&type=buy&amount=0.01&currency=SOL`
  );
  
  check(quoteRes, { 'quote 200': (r) => r.status === 200 });
  
  // Note: Actual trade execution would be done with test accounts
  // Do not execute real trades in load test
  
  sleep(Math.random() * 5 + 2);
}
```

### 2.4 Concurrent Users Simulation

```javascript
// k6-concurrent-simulation.js
import http from 'k6/http';
import { check, sleep, group } from 'k6';

export const options = {
  scenarios: {
    browse_users: {
      executor: 'constant-vus',
      vus: 500,
      duration: '5m',
      exec: 'browseTokens',
    },
    active_traders: {
      executor: 'constant-vus',
      vus: 100,
      duration: '5m',
      exec: 'tradingActivity',
    },
    profile_viewers: {
      executor: 'constant-vus',
      vus: 100,
      duration: '5m',
      exec: 'viewProfiles',
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<1000'],
    http_req_failed: ['rate<0.02'],
  },
};

const BASE_URL = __ENV.BASE_URL;

export function browseTokens() {
  group('Token Browsing', () => {
    http.get(`${BASE_URL}/tokens?tab=discover`);
    sleep(2);
    http.get(`${BASE_URL}/tokens?tab=trending`);
    sleep(2);
    http.get(`${BASE_URL}/tokens/some-token-address`);
    sleep(3);
  });
}

export function tradingActivity() {
  group('Trading Activity', () => {
    http.get(`${BASE_URL}/tokens/some-token`);
    sleep(1);
    http.get(`${BASE_URL}/trading/quote?token=x&type=buy&amount=0.1`);
    sleep(5);
  });
}

export function viewProfiles() {
  group('Profile Viewing', () => {
    http.get(`${BASE_URL}/users/some-user`);
    sleep(3);
  });
}
```

---

## 3. REAL-TIME PERFORMANCE TESTS

### 3.1 WebSocket Latency Test

```javascript
// websocket-test.js
const WebSocket = require('ws');

const WS_URL = 'wss://ws.pumpfun.io';
const TEST_TOKEN = 'TestToken123';

const metrics = {
  connected: false,
  connectionTime: 0,
  messageLatencies: [],
  errors: 0,
};

function measureLatency() {
  const startTime = Date.now();
  const ws = new WebSocket(WS_URL);
  
  ws.on('open', () => {
    metrics.connectionTime = Date.now() - startTime;
    metrics.connected = true;
    
    // Subscribe to token updates
    ws.send(JSON.stringify({
      type: 'subscribe',
      channel: `token:${TEST_TOKEN}`,
    }));
  });
  
  ws.on('message', (data) => {
    const message = JSON.parse(data);
    if (message.timestamp) {
      const latency = Date.now() - new Date(message.timestamp).getTime();
      metrics.messageLatencies.push(latency);
    }
  });
  
  ws.on('error', (err) => {
    metrics.errors++;
    console.error('WebSocket error:', err);
  });
  
  // Run for 60 seconds
  setTimeout(() => {
    ws.close();
    printResults();
  }, 60000);
}

function printResults() {
  const latencies = metrics.messageLatencies;
  const sorted = latencies.sort((a, b) => a - b);
  
  console.log('\n=== WebSocket Performance Results ===');
  console.log(`Connection Time: ${metrics.connectionTime}ms`);
  console.log(`Total Messages: ${latencies.length}`);
  console.log(`Errors: ${metrics.errors}`);
  
  if (latencies.length > 0) {
    console.log(`Min Latency: ${sorted[0]}ms`);
    console.log(`Max Latency: ${sorted[sorted.length - 1]}ms`);
    console.log(`Avg Latency: ${(latencies.reduce((a, b) => a + b) / latencies.length).toFixed(2)}ms`);
    console.log(`P50 Latency: ${sorted[Math.floor(latencies.length * 0.5)]}ms`);
    console.log(`P95 Latency: ${sorted[Math.floor(latencies.length * 0.95)]}ms`);
    console.log(`P99 Latency: ${sorted[Math.floor(latencies.length * 0.99)]}ms`);
  }
  
  // Pass/Fail
  const p95 = sorted[Math.floor(latencies.length * 0.95)] || 0;
  console.log(`\n=== Result: ${p95 < 500 ? 'PASS ✓' : 'FAIL ✗'} ===`);
  console.log(`P95 < 500ms requirement: ${p95}ms`);
}

measureLatency();
```

### 3.2 Chat Real-time Test

```javascript
// chat-realtime-test.js
const WebSocket = require('ws');

async function testChatLatency(tokenAddress, numMessages = 20) {
  const ws = new WebSocket('wss://ws.pumpfun.io');
  const latencies = [];
  let messagesSent = 0;
  
  return new Promise((resolve) => {
    ws.on('open', () => {
      ws.send(JSON.stringify({
        type: 'subscribe',
        channel: `chat:${tokenAddress}`,
      }));
      
      // Send test messages
      const interval = setInterval(() => {
        const sendTime = Date.now();
        ws.send(JSON.stringify({
          type: 'chat_message',
          token: tokenAddress,
          content: `Test message ${messagesSent}`,
          clientTime: sendTime,
        }));
        messagesSent++;
        
        if (messagesSent >= numMessages) {
          clearInterval(interval);
        }
      }, 500);
    });
    
    ws.on('message', (data) => {
      const msg = JSON.parse(data);
      if (msg.type === 'chat_message' && msg.clientTime) {
        const latency = Date.now() - msg.clientTime;
        latencies.push(latency);
        
        if (latencies.length >= numMessages) {
          ws.close();
          resolve(latencies);
        }
      }
    });
  });
}

// Run test
testChatLatency('TestToken123', 20).then((latencies) => {
  console.log('Chat Latencies:', latencies);
  console.log('Average:', (latencies.reduce((a, b) => a + b) / latencies.length).toFixed(2), 'ms');
});
```

---

## 4. FRONTEND PERFORMANCE TESTS

### 4.1 Lighthouse CI Config

```javascript
// lighthouserc.js
module.exports = {
  ci: {
    collect: {
      url: [
        'https://staging.pumpfun.io/',
        'https://staging.pumpfun.io/token/TestToken',
        'https://staging.pumpfun.io/profile/testuser',
        'https://staging.pumpfun.io/create-token',
      ],
      numberOfRuns: 3,
    },
    assert: {
      assertions: {
        'categories:performance': ['error', { minScore: 0.8 }],
        'first-contentful-paint': ['error', { maxNumericValue: 2000 }],
        'largest-contentful-paint': ['error', { maxNumericValue: 3000 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'total-blocking-time': ['error', { maxNumericValue: 300 }],
        'speed-index': ['error', { maxNumericValue: 3000 }],
      },
    },
    upload: {
      target: 'filesystem',
      outputDir: './lighthouse-results',
    },
  },
};
```

**Run Command:**
```bash
npx lhci autorun
```

### 4.2 Page Load Time Test

```javascript
// page-load-test.js
const puppeteer = require('puppeteer');

const PAGES = [
  { name: 'Home', url: 'https://staging.pumpfun.io/' },
  { name: 'Token Detail', url: 'https://staging.pumpfun.io/token/Test' },
  { name: 'Create Token', url: 'https://staging.pumpfun.io/create-token' },
  { name: 'Leaderboard', url: 'https://staging.pumpfun.io/leaderboard' },
  { name: 'Referrals', url: 'https://staging.pumpfun.io/referrals' },
];

async function measurePageLoad(page, url, name) {
  const start = Date.now();
  
  await page.goto(url, { waitUntil: 'networkidle2' });
  
  const loadTime = Date.now() - start;
  
  const metrics = await page.metrics();
  const performanceTiming = JSON.parse(
    await page.evaluate(() => JSON.stringify(performance.timing))
  );
  
  return {
    name,
    url,
    loadTime,
    domContentLoaded: performanceTiming.domContentLoadedEventEnd - performanceTiming.navigationStart,
    firstPaint: metrics.FirstMeaningfulPaint,
    jsHeapSize: Math.round(metrics.JSHeapUsedSize / 1024 / 1024),
  };
}

async function runTests() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  console.log('\n=== Page Load Performance Test ===\n');
  
  const results = [];
  
  for (const { name, url } of PAGES) {
    const result = await measurePageLoad(page, url, name);
    results.push(result);
    
    const status = result.loadTime < 3000 ? '✓ PASS' : '✗ FAIL';
    console.log(`${name}: ${result.loadTime}ms ${status}`);
  }
  
  await browser.close();
  
  console.log('\n=== Summary ===');
  const passed = results.filter(r => r.loadTime < 3000).length;
  console.log(`Passed: ${passed}/${results.length}`);
  
  return results;
}

runTests();
```

---

## 5. DATABASE PERFORMANCE TESTS

### 5.1 Query Performance Test

```sql
-- query-performance.sql

-- Test 1: Token list with DiscoverScore (should be < 100ms)
EXPLAIN ANALYZE
SELECT t.*, 
       (0.40 * t.trending_score + 
        0.20 * t.liquidity_points + 
        0.20 * t.holders_points + 
        0.10 * t.trust_score + 
        0.10 * t.recency_points) as discover_score
FROM tokens t
WHERE t.is_nsfw = false
  AND t.market_cap BETWEEN 10000 AND 100000
ORDER BY discover_score DESC
LIMIT 20 OFFSET 0;

-- Test 2: Token holders (should be < 50ms)
EXPLAIN ANALYZE
SELECT h.wallet_address, 
       h.balance,
       (h.balance * 100.0 / t.total_supply) as percent_of_supply,
       u.username
FROM token_holders h
JOIN tokens t ON h.token_address = t.address
LEFT JOIN users u ON h.wallet_address = u.wallet_address
WHERE h.token_address = 'TestToken123'
ORDER BY h.balance DESC
LIMIT 100;

-- Test 3: Transaction history (should be < 50ms)
EXPLAIN ANALYZE
SELECT tx.*, u.username
FROM transactions tx
LEFT JOIN users u ON tx.trader_address = u.wallet_address
WHERE tx.token_address = 'TestToken123'
ORDER BY tx.created_at DESC
LIMIT 50;

-- Test 4: User portfolio with P&L (should be < 100ms)
EXPLAIN ANALYZE
SELECT h.token_address,
       t.name, t.symbol, t.current_price,
       h.balance,
       h.balance * t.current_price as current_value,
       h.cost_basis,
       (h.balance * t.current_price - h.cost_basis) as pnl
FROM token_holders h
JOIN tokens t ON h.token_address = t.address
WHERE h.wallet_address = 'UserWallet123'
  AND h.balance > 0
ORDER BY (h.balance * t.current_price) DESC;
```

### 5.2 Index Recommendations

```sql
-- Recommended indexes for performance

-- Token queries
CREATE INDEX idx_tokens_discover ON tokens 
  (is_nsfw, market_cap) 
  INCLUDE (trending_score, liquidity_points, holders_points, trust_score, recency_points);

CREATE INDEX idx_tokens_trending ON tokens (trending_score DESC);
CREATE INDEX idx_tokens_volume ON tokens (volume_24h DESC);

-- Holders queries
CREATE INDEX idx_holders_token_balance ON token_holders 
  (token_address, balance DESC);

-- Transaction queries
CREATE INDEX idx_transactions_token_time ON transactions 
  (token_address, created_at DESC);

CREATE INDEX idx_transactions_user_time ON transactions 
  (trader_address, created_at DESC);

-- User queries
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_wallet ON users (wallet_address);
```

---

## 6. PERFORMANCE KPIs

### 6.1 Target Metrics

| Metric | Target | Critical |
|--------|--------|----------|
| Page Load (Home) | < 3s | < 5s |
| Page Load (Token Detail) | < 3s | < 5s |
| API Response (GET) | < 500ms (p95) | < 1s |
| API Response (POST) | < 1s (p95) | < 2s |
| Trade Execution | < 3s | < 5s |
| WebSocket Latency | < 500ms | < 1s |
| Chat Message | < 500ms | < 1s |
| Concurrent Users | 1,000 | 500 |
| Error Rate | < 1% | < 5% |

### 6.2 Test Report Template

```
=== PERFORMANCE TEST REPORT ===
Date: YYYY-MM-DD
Environment: Staging / Production
Duration: X minutes

--- Load Test Results ---
Virtual Users: X
Total Requests: X
Requests/sec: X
Avg Response Time: Xms
P95 Response Time: Xms
P99 Response Time: Xms
Error Rate: X%
Status: PASS/FAIL

--- Page Load Results ---
Home: Xms [PASS/FAIL]
Token Detail: Xms [PASS/FAIL]
Create Token: Xms [PASS/FAIL]
Profile: Xms [PASS/FAIL]

--- Real-time Results ---
WebSocket Connection: Xms
Message Latency P95: Xms
Status: PASS/FAIL

--- Recommendations ---
1. ...
2. ...
```

---

## 7. EXECUTION COMMANDS

```bash
# Run all k6 tests
k6 run k6-token-list.js
k6 run k6-token-detail.js
k6 run k6-trading.js
k6 run k6-concurrent-simulation.js

# Run Lighthouse
npx lhci autorun

# Run WebSocket test
node websocket-test.js

# Run page load test
node page-load-test.js

# Generate HTML report
k6 run --out json=results.json k6-token-list.js
```

---

**END OF PERFORMANCE TEST SCRIPTS**
