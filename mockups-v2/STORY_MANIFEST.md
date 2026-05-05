# 🌱 THE MEMECONOMY GARDEN

**Story Manifest — Sprout Clone (placeholder name)**
**Version:** 1.0
**Locked on:** May 2026
**Status:** Source of truth — every design decision must trace back here.

---

## 📖 THE STORY (one paragraph)

> *Bạn là một **Explorer** lang thang trong khu vườn nơi meme mọc thành token. Mỗi hạt là hy vọng của một creator, mỗi cây là chiến thắng của community. Bạn không vội — bạn đi dạo, quan sát, tìm điều đang nở. Đôi khi bạn tự gieo hạt. Đôi khi bạn trồng cùng người khác. Càng dành thời gian, bạn càng lớn — từ Hạt thành Cây cổ thụ.*

---

## 🎯 THE THREE PILLARS

### 1. The Hero — Explorer

User là **Explorer**, không phải Hunter, Trader, hay Gambler.

| Explorer DOES | Explorer DOESN'T |
|---|---|
| Browse with curiosity | Rush in/out |
| Discover unknown gems | Chase pumps |
| Patient pace | FOMO panic |
| Observe before acting | Ape blindly |
| Builds knowledge over time | Maximizes per-trade |

**Implication on UX:**
- Default UI is **calm, low-pressure**
- No countdown timers, no aggressive red CTAs, no flashing alerts
- Pro Mode tồn tại nhưng KHÔNG default
- Discovery flow > Trade flow trong information architecture

### 2. The World — Memeconomy Garden

Mọi feature là một biome trong khu vườn:

| Feature | Garden biome | Visual cue chủ đạo |
|---|---|---|
| Discover | **Greenhouse** — hạt mới gieo | Light peach glow |
| Trending | **Bloom Field** — đang nở | Peach + petal motif |
| Top Volume | **Harvest Plaza** — được hái nhiều | Amber accent |
| Graduated | **Ancient Forest** — cây trưởng thành | Deep teal |
| Favorite | **My Plot** — vườn riêng | User mascot tier |
| Arena | **Tournament Garden** — battle plants | Crimson + teal duel |
| Clubs | **Greenhouse Cooperatives** — trồng chung | Soft peach glow |
| Stake | **Compost / Rich Soil** | Earth brown |
| Events | **Seasonal Festival** | Multi-color confetti |
| Rewards | **Harvest Festival** — slot = lucky harvest | Peach + amber |
| Point Tier | **Mascot Evolution** — Seed→Sprout→Sapling→Tree→Ancient Tree | 5 stages |

**Quy tắc:** Khi build feature mới, **PHẢI** tìm chỗ của nó trong khu vườn trước khi design. Nếu không fit → rethink feature.

### 3. The Three Feelings (priority order)

1. **Wonder** (PRIMARY) — curiosity, "what's blooming today?"
2. **Calm confidence** (SECONDARY) — patient, in control, no rush
3. **Belonging** (SUPPORTING) — Clubs/Arena/Events moments

**Cảm xúc bị loại trừ:**
- ❌ FOMO panic
- ❌ Triumph ăn mừng quá mức (confetti everywhere)
- ❌ Anxiety / urgency
- ❌ Aggression / competitive shouting

---

## 🎨 VISUAL REGISTER

### Color palette (extended to support story)

| Token | Hex | Story role | Allowed usage |
|---|---|---|---|
| `--peach-400` | `#e8a87c` | **Brand / Dawn** | Logo, headings, primary CTA, "near graduation" highlight, mascot fruit |
| `--peach-500` | `#d68a5b` | Peach hover/pressed | CTA hover state |
| `--teal-400` | `#7cc4a4` | **Growth / Leaves** | Buy button, success, price up, trust shield, mascot leaves |
| `--teal-500` | `#5ba886` | Teal hover/pressed | Buy hover, trust active |
| `--amber-400` | `#d4a256` | **Harvest / Mature** | Graduated state, Tier 4-5 mascot accent, milestones |
| `--crimson-400` | `#d65a54` | **Wilt / Danger** | Sell, price down, error (sparingly) |
| `--bg` | `#0a0e1a` | **Night sky** | Page background |
| `--surface-1` | `#131826` | **Earth surface** | Cards |
| `--surface-2` | `#1a2138` | **Soil layer** | Inputs, nested |

**Banned colors (will break the story):**
- ❌ Purple (`#8b5cf6`-style)
- ❌ Pink (`#ec4899`-style)
- ❌ Pure blue (clash with night sky bg + teal)
- ❌ Neon green (`#00ff00`-style)
- ❌ Gradient rainbows

### Typography

| Role | Font | Weight | Notes |
|---|---|---|---|
| Display (brand, headings, CTA) | **Plus Jakarta Sans** | 700-800 | Rounded sans, organic feel |
| Body | **Inter** | 400-600 | Neutral, readable |
| Numbers, addresses, prices | **JetBrains Mono** | 500-600 | Tabular, no ambiguity |

**Rule:** Display font cho brand moments + numbers always mono + body Inter. **Không bao giờ** mix random.

### Texture / shape language

- **Rounded corners only** — no sharp 90° corners on interactive elements
- **Border radius scale:** 6 / 10 / 14 / 20 / pill
- **No grid patterns, no neon grid, no isometric tech**
- **Leaf-shaped icons** for trust/badge moments (not generic shields)
- **Organic curves preferred** over geometric lines (vd: progress bar có shimmer mềm, không có hard 90° transition)

### Motion

- **Easing:** `cubic-bezier(0.4, 0, 0.2, 1)` (calm, no bounce)
- **Durations:** 0.15s (micro), 0.25s (default), 0.4s (large transitions)
- **No aggressive animations** (shake, flash, big bounce)
- **Allowed:** gentle leaf sway, water ripple, slow shimmer on progress, mascot breathing
- **Banned:** confetti spam, screen shake, neon pulse, fire animation

---

## 🗣️ BRAND VOICE

### Vocabulary swap table (USE TIES sang bên phải, KHÔNG bao giờ trái)

| ❌ Old voice (ditch) | ✅ Garden voice (use) |
|---|---|
| Ape in now | Plant your seed |
| To the moon 🚀 | Watch this one bloom |
| Make money fast | Tend your portfolio |
| 100x gem | A sprout worth watching |
| Stake your claim | Find your plot |
| Whale alert! | A seasoned grower joined |
| Rug pull | Wilted (for educational copy) |
| HODL | Tend it |
| Diamond hands | Patient gardener |
| Pump | Bloom |
| Dump | Wilt |
| Bag holders | Garden caretakers |
| Bullish | Sprouting |
| Bearish | Dormant season |

### Voice principles

1. **Curious, not loud.** Empty states, errors, success messages — tone là "thì thầm trong vườn", không "hét trong sân vận động"
2. **Informative, not greedy.** "Volume +24%" thay vì "VOLUME EXPLODING 🚀🚀🚀"
3. **Warm, not infantile.** Ngôn ngữ cute nhưng không trẻ con — Phantom wallet là benchmark, không phải Candy Crush
4. **Witty in micro-moments.** Empty state, 404, loading — đây là chỗ cá tính lộ. Body text vẫn neutral.

### Example copy

| Context | ❌ Don't | ✅ Do |
|---|---|---|
| Empty Discover | "No results found" | "Nothing's blooming in this corner yet — try Trending" |
| Token graduated | "🚀 GRADUATED 🚀" | "This sprout reached the canopy" |
| Wallet not connected | "Please connect your wallet" | "Connect your wallet to start tending" |
| Trade success | "BUY EXECUTED ✅" | "Planted. 410K tokens are yours" |
| Network error | "Error 500" | "The garden hit a glitch — try again in a moment" |
| Tier upgrade | "LEVEL UP!" | "You've grown into a Sapling" |
| Loading | "Loading..." | "Watering the soil..." (used sparingly, only on long loads) |

### Marquee text (final, locked)

```
MAKE MONEY ON THE MEMECONOMY • PLANT YOUR SEED • WATCH WHAT'S BLOOMING • NO BOT DRAMA •
```

(Compromise: giữ "MAKE MONEY ON THE MEMECONOMY" theo yêu cầu user, nhưng thêm "PLANT YOUR SEED" + "WATCH WHAT'S BLOOMING" để hybrid với Garden voice. Bỏ "FAIR LAUNCH" vì redundant với "NO BOT DRAMA".)

---

## 🌟 SIGNATURE MOMENTS (8)

Đây là 8 chỗ story phải lộ ra rõ ràng. Đây là **lý do user nhớ product**.

### 1. Mascot Evolution (Tier-based avatar)

5 stages, vẽ từ vector chỉn chu:

| Tier | Pts | Mascot | Visual cue |
|---|---|---|---|
| 1 | 0 | 🌱 **Seed** | Hạt nâu, mầm xanh nhú, dáng "happy" |
| 2 | 500 | 🌿 **Sprout** | 2 lá xanh đối xứng, thân ngắn, mặt cười |
| 3 | 2K | 🌳 **Sapling** | Cây non, 4-5 lá rộng, thân chắc |
| 4 | 10K | 🌲 **Tree** | Cây trưởng thành, có 1-2 quả/hoa amber |
| 5 | 50K | 🪷 **Ancient Tree** | Cây cổ thụ vàng, gốc to, thiền |

**Xuất hiện ở:**
- Sidebar user card (always — primary identity touchpoint)
- My Profile page header (large, hero-size)
- Public Profile (small, beside username)
- Leaderboard rank icon
- Tier upgrade modal (full-screen celebration)
- Empty states (Seed mascot smiles, kéo cảm xúc)

### 2. Graduation Animation

Khi token đạt $69K MC → graduate to Raydium:
- Card "blooms" — peach + teal petal animation 1.5-2s
- Sound (optional) — soft chime, không celebration loud
- Badge changes from "Progress to DEX 99%" → "🌳 Graduated"
- Token now lives in "Ancient Forest" tab

### 3. "Just Sprouted" Badge

Token <24h tuổi:
- Leaf-shaped badge top-left of card
- Color: teal-500
- Copy: "🌱 Just sprouted"
- Tự biến mất sau 24h

### 4. Tier Upgrade Modal

User lên Tier (vd: Sprout → Sapling):
- Full screen, soft peach background
- Mascot animation: current stage → grows into next stage (2s morph)
- Copy: "You've grown into a Sapling. New mascot unlocked."
- Subcopy: short tip về Tier mới (vd: "Saplings can join Greenhouse Clubs")
- CTA: "Continue tending" (close modal)

### 5. Empty States — mascot-led

Mọi empty state có mascot Seed + warm copy + rõ next action.

```
[Mascot Seed cute illustration]
Nothing's blooming here yet
Try Discover or watch what's trending today
[Browse Discover button]
```

### 6. Loading State — Watering

Long loads (>500ms):
- Mascot Seed cute đang được tưới (watering can animation)
- Hoặc text "Watering the soil..." nếu space hẹp
- Skeleton skeleton with subtle shimmer (peach→teal)

### 7. Trust Shield — Leaf-shaped

Thay vì shield generic 🛡️, dùng **leaf icon** 🍃:
- Leaf màu teal khi trust score >70
- Leaf amber khi 50-70
- Leaf wilted (crimson) khi <50

### 8. Marquee — Garden voice mixed

```
MAKE MONEY ON THE MEMECONOMY • PLANT YOUR SEED • WATCH WHAT'S BLOOMING • NO BOT DRAMA •
```

(Bỏ "FAIR LAUNCH" — redundant)

---

## ⚖️ DECISION TREE — When in doubt, ask:

Khi gặp ngã ba design, áp 4 câu hỏi này theo thứ tự:

1. **Story check:** "Quyết định này có support 'Explorer trong Garden' không?"
   - Nếu KHÔNG → bỏ
2. **Feeling check:** "Nó có làm user thấy Wonder / Calm / Belonging không, hay chỉ FOMO?"
   - Nếu chỉ FOMO → reject
3. **Voice check:** "Copy có nằm trong vocabulary table không?"
   - Nếu rớt vào ❌ column → rewrite
4. **Visual check:** "Có dùng banned colors / patterns không?"
   - Nếu có → swap or remove

Nếu qua hết 4 → ship.

---

## 🚫 ANTI-PATTERNS (do NOT do)

1. ❌ **Confetti everywhere.** Confetti chỉ ở Tier upgrade + first trade. Không spam.
2. ❌ **Aggressive red.** Red chỉ cho sell/error/wilted token. Không bao giờ làm CTA.
3. ❌ **Pump.fun-style FOMO copy.** "PUMPING NOW! 100x INCOMING!" sai story.
4. ❌ **Photon-style data density.** Dense 6-panel terminal sai story.
5. ❌ **Cyber/neon accents.** Glow, grid, isometric tech sai story.
6. ❌ **Title Case everywhere.** Sentence case là default. Title Case chỉ cho proper nouns.
7. ❌ **Mascot replaced với generic emoji.** 🌱 emoji có thể dùng inline copy, nhưng KHÔNG thay được illustrated mascot.
8. ❌ **"Loading..." plain text.** Mọi loading > 500ms phải có mascot watering hoặc skeleton có shimmer.
9. ❌ **Logo "Pumpfun Clone".** Tên này phá story. Placeholder = "Sprout".
10. ❌ **Multi-color tab indicator (rainbow active state).** Tab active chỉ dùng peach.

---

## ✅ THE ULTIMATE TEST

> *"If a returning user closes their eyes after using the product, what do they remember?"*

Answer phải là:
- "Cảm giác đang ở trong vườn"
- "Cái mascot dễ thương lớn dần khi tôi up Tier"
- "Không stress khi browse"
- "Thấy mình đang trồng gì đó"

NOT:
- "Đỏ với xanh khắp nơi"
- "Toàn 🚀💎🔥"
- "Đầy số"
- "Giống Pump.fun"

---

## 📅 CHANGELOG

- **v1.0 (May 2026)** — Initial story locked. Hero=Explorer, World=Garden, Feelings=Wonder/Calm/Belonging, Visual=Organic+Premium discipline. Marquee compromise: keep "MAKE MONEY ON MEMECONOMY" + add "PLANT YOUR SEED + WATCH WHAT'S BLOOMING".

---

**End of manifest.**

*Print this. Stick it on the wall. Read before every design session.*
