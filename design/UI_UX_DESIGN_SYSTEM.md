# 🎨 PUMPFUN - UI/UX DESIGN SYSTEM

**Version:** 1.0  
**Last Updated:** February 7, 2026  
**Target Platform:** Web (Desktop-first, Mobile-responsive)

---

## 📋 MỤC LỤC

1. [Tổng Quan](#1-tổng-quan)
2. [Design Principles](#2-design-principles)
3. [Color System](#3-color-system)
4. [Typography](#4-typography)
5. [Spacing & Grid](#5-spacing--grid)
6. [Components](#6-components)
7. [Layout Patterns](#7-layout-patterns)
8. [Animations & Transitions](#8-animations--transitions)
9. [Responsive Design](#9-responsive-design)
10. [Accessibility](#10-accessibility)
11. [Page-by-Page Guidelines](#11-page-by-page-guidelines)
12. [UI Patterns Library](#12-ui-patterns-library)

---

## 1. TỔNG QUAN

### 1.1 Product Vision
PumpFun là nền tảng launchpad cho meme tokens trên Solana blockchain. Sản phẩm cần truyền tải:
- **Sự thú vị & năng động** của meme culture
- **Sự tin cậy & chuyên nghiệp** của một trading platform  
- **Sự dễ sử dụng** cho cả người mới và traders chuyên nghiệp

### 1.2 Target Users
| Persona | Đặc điểm | Nhu cầu |
|---------|----------|---------|
| 🐣 **New Trader** | Lần đầu trade crypto, 18-25 tuổi | UI đơn giản, guidance rõ ràng |
| 💹 **Active Trader** | Trade hàng ngày, 25-35 tuổi | Tốc độ, real-time data, shortcuts |
| 🎨 **Token Creator** | Muốn launch meme token | Wizard dễ follow, preview đẹp |
| 🐋 **Whale** | High-value trader | Advanced features, trust indicators |

### 1.3 Design Style
**"Premium Crypto Dark"** - Dark theme với accents rực rỡ, mang phong cách:
- Glassmorphism cho cards
- Gradient accents
- Subtle glow effects
- Micro-animations

---

## 2. DESIGN PRINCIPLES

### 2.1 Core Principles

#### 🚀 Speed First
- Tối ưu cho hành động nhanh
- Quick buttons (0.1, 0.5, 1 SOL)
- Keyboard shortcuts
- One-click trades

#### 👁️ Information Hierarchy
- Thông tin quan trọng nhất (price, P&L) nổi bật
- Secondary info dễ tìm nhưng không gây nhiễu
- Progressive disclosure cho advanced settings

#### 🎯 Action-Oriented
- CTA buttons luôn nổi bật
- Mỗi screen có 1 primary action rõ ràng
- Minimize steps to complete tasks

#### 🛡️ Trust & Safety
- Trust badges cho mọi token
- Risk indicators rõ ràng (🟢🟡🔴)
- Confirmation cho high-risk actions

### 2.2 UX Principles

```
┌─────────────────────────────────────────────────────────┐
│                     CLARITY                              │
│   Mọi element phải có mục đích rõ ràng                  │
├─────────────────────────────────────────────────────────┤
│                    FEEDBACK                              │
│   Mọi action phải có response (loading, success, error) │
├─────────────────────────────────────────────────────────┤
│                   CONSISTENCY                            │
│   Patterns đồng nhất across toàn bộ product             │
├─────────────────────────────────────────────────────────┤
│                    RECOVERY                              │
│   Dễ undo, cancel, hoặc fix mistakes                    │
└─────────────────────────────────────────────────────────┘
```

---

## 3. COLOR SYSTEM

### 3.1 Primary Palette

```css
/* === CORE COLORS === */

/* Primary - Green (Trust, Success, Buy) */
--primary-50:  #ecfdf5;
--primary-100: #d1fae5;
--primary-200: #a7f3d0;
--primary-300: #6ee7b7;
--primary-400: #34d399;
--primary-500: #10b981;  /* Main Primary */
--primary-600: #059669;  /* Hover */
--primary-700: #047857;
--primary-800: #065f46;
--primary-900: #064e3b;

/* Danger - Red (Risk, Sell, Error) */
--danger-50:  #fef2f2;
--danger-100: #fee2e2;
--danger-200: #fecaca;
--danger-300: #fca5a5;
--danger-400: #f87171;
--danger-500: #ef4444;   /* Main Danger */
--danger-600: #dc2626;   /* Hover */
--danger-700: #b91c1c;
--danger-800: #991b1b;
--danger-900: #7f1d1d;

/* Warning - Amber (Caution, Medium Risk) */
--warning-50:  #fffbeb;
--warning-100: #fef3c7;
--warning-200: #fde68a;
--warning-300: #fcd34d;
--warning-400: #fbbf24;
--warning-500: #f59e0b;  /* Main Warning */
--warning-600: #d97706;  /* Hover */
--warning-700: #b45309;
--warning-800: #92400e;
--warning-900: #78350f;

/* Accent - Purple (CTAs, Highlights) */
--accent-50:  #f5f3ff;
--accent-100: #ede9fe;
--accent-200: #ddd6fe;
--accent-300: #c4b5fd;
--accent-400: #a78bfa;
--accent-500: #8b5cf6;   /* Main Accent */
--accent-600: #7c3aed;   /* Hover */
--accent-700: #6d28d9;
--accent-800: #5b21b6;
--accent-900: #4c1d95;

/* Info - Blue (Links, Information) */
--info-500: #3b82f6;
--info-600: #2563eb;

/* Cyan (Special highlights) */
--cyan-500: #06b6d4;
--cyan-600: #0891b2;

/* Pink (Favorites, Hearts) */
--pink-500: #ec4899;
--pink-600: #db2777;
```

### 3.2 Background & Surface Colors

```css
/* === DARK THEME (Default) === */

/* Backgrounds */
--bg-primary:    #0a0e1a;    /* Main background */
--bg-secondary:  #0f1419;    /* Alternative bg */

/* Surfaces */
--surface-1:     #1a1a2e;    /* Cards, Modals */
--surface-2:     #16213e;    /* Nested cards, Inputs */
--surface-3:     #252b3b;    /* Hover states */
--surface-4:     #2d3548;    /* Active states */

/* Borders */
--border-primary:   #2d3748;  /* Normal borders */
--border-secondary: #374151;  /* Subtle borders */
--border-focus:     #8b5cf6;  /* Focus rings */
```

### 3.3 Text Colors

```css
/* === TEXT HIERARCHY === */
--text-primary:    #f9fafb;  /* Headings, Important */
--text-secondary:  #9ca3af;  /* Body text */
--text-tertiary:   #6b7280;  /* Labels, Hints */
--text-disabled:   #4b5563;  /* Disabled states */
--text-inverse:    #111827;  /* On light backgrounds */
```

### 3.4 Semantic Colors

```css
/* === SEMANTIC USAGE === */

/* Trading */
--color-buy:       var(--primary-500);   /* Buy actions */
--color-sell:      var(--danger-500);    /* Sell actions */
--color-profit:    var(--primary-500);   /* Positive P&L */
--color-loss:      var(--danger-500);    /* Negative P&L */

/* Trust Levels */
--trust-high:      var(--primary-500);   /* 70-100 */
--trust-medium:    var(--warning-500);   /* 40-69 */
--trust-low:       var(--danger-500);    /* 0-39 */

/* Risk Indicators */
--risk-low:        var(--primary-500);   /* Green - Safe */
--risk-medium:     var(--warning-500);   /* Yellow - Caution */
--risk-high:       var(--danger-500);    /* Red - Danger */
```

### 3.5 Gradients

```css
/* === GRADIENTS === */

/* Primary Gradient - CTAs, Headers */
--gradient-primary: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);

/* Buy Gradient */
--gradient-buy: linear-gradient(135deg, #10b981 0%, #059669 100%);

/* Sell Gradient */
--gradient-sell: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);

/* Card Highlight */
--gradient-card: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(236, 72, 153, 0.1) 100%);

/* Stats Banner */
--gradient-banner: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);

/* Shimmer Effect */
--gradient-shimmer: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
```

---

## 4. TYPOGRAPHY

### 4.1 Font Stack

```css
/* Primary Font */
--font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', 'Helvetica Neue', sans-serif;

/* Monospace - Numbers, Addresses */
--font-mono: 'SF Mono', 'Fira Code', 'Roboto Mono', Consolas, monospace;

/* Display - Logo, Headlines */
--font-display: 'Inter', 'Plus Jakarta Sans', var(--font-sans);
```

### 4.2 Type Scale

```css
/* === SIZE SCALE === */
--text-xs:   12px;   /* line-height: 16px */
--text-sm:   13px;   /* line-height: 18px */
--text-base: 14px;   /* line-height: 22px */
--text-md:   16px;   /* line-height: 24px */
--text-lg:   18px;   /* line-height: 26px */
--text-xl:   20px;   /* line-height: 28px */
--text-2xl:  24px;   /* line-height: 32px */
--text-3xl:  28px;   /* line-height: 36px */
--text-4xl:  32px;   /* line-height: 40px */
--text-5xl:  40px;   /* line-height: 48px */
```

### 4.3 Font Weights

```css
--font-normal:    400;   /* Body text */
--font-medium:    500;   /* Emphasis */
--font-semibold:  600;   /* Buttons, Labels */
--font-bold:      700;   /* Headings */
--font-extrabold: 800;   /* Display, Page titles */
```

### 4.4 Typography Styles

| Element | Size | Weight | Color | Line Height |
|---------|------|--------|-------|-------------|
| **Page Title** | 28-32px | 800 | text-primary | 36-40px |
| **Section Header** | 20-24px | 700 | text-primary | 28-32px |
| **Card Title** | 18-19px | 700-800 | text-primary | 24-26px |
| **Subsection** | 16px | 600-700 | text-secondary | 24px |
| **Body** | 14px | 400-500 | text-secondary | 22px |
| **Label** | 12-13px | 600-700 | text-tertiary | 16-18px |
| **Caption** | 11-12px | 400-500 | text-tertiary | 14-16px |
| **Button Text** | 14-16px | 600-700 | #ffffff | auto |
| **Stat Value** | 17-20px | 700-800 | text-primary | auto |

### 4.5 Special Typography

```css
/* Price Display */
.price-large {
    font-size: 24px;
    font-weight: 800;
    font-variant-numeric: tabular-nums;
    font-family: var(--font-mono);
}

/* Wallet Address */
.address {
    font-size: 11px;
    font-family: var(--font-mono);
    color: var(--text-tertiary);
}

/* Percentage Change */
.change-positive {
    color: var(--color-profit);
    font-weight: 700;
}

.change-negative {
    color: var(--color-loss);
    font-weight: 700;
}
```

---

## 5. SPACING & GRID

### 5.1 Spacing Scale

```css
/* === 4px BASE UNIT === */
--space-0:  0;
--space-1:  4px;
--space-2:  8px;
--space-3:  12px;
--space-4:  16px;
--space-5:  20px;
--space-6:  24px;
--space-7:  28px;
--space-8:  32px;
--space-10: 40px;
--space-12: 48px;
--space-16: 64px;
--space-20: 80px;
```

### 5.2 Layout Constants

```css
/* Fixed Elements */
--header-height:  70px;
--sidebar-width:  260px;
--bottom-nav:     60px;    /* Mobile only */
--trading-panel:  380px;   /* Token Detail page */

/* Container */
--container-max:  1400px;
--container-padding: 24px; /* Desktop */
--container-padding-mobile: 16px;

/* Card Padding */
--card-padding-sm: 16px;
--card-padding-md: 20px;
--card-padding-lg: 24px;
```

### 5.3 Grid System

```css
/* Main Content Grid */
.token-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 20px;
}

/* Two Column Layout (Token Detail) */
.two-column {
    display: grid;
    grid-template-columns: 1fr 380px;
    gap: 24px;
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 24px;
}

/* Metrics Grid */
.metrics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
}
```

### 5.4 Border Radius Scale

```css
--radius-xs:  4px;
--radius-sm:  6px;
--radius-md:  8px;
--radius-lg:  10px;
--radius-xl:  12px;
--radius-2xl: 16px;
--radius-3xl: 20px;
--radius-full: 9999px;  /* Pills, Avatars */
```

---

## 6. COMPONENTS

### 6.1 Buttons

#### Primary Button
```css
.btn-primary {
    background: var(--gradient-primary);
    color: white;
    padding: 12px 24px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 15px;
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 20px rgba(139, 92, 246, 0.3);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(139, 92, 246, 0.4);
}

.btn-primary:active {
    transform: translateY(0);
}
```

#### Buy/Sell Buttons
| State | Background | Text | Shadow |
|-------|------------|------|--------|
| Buy | gradient-buy | white | green glow |
| Sell | gradient-sell | white | red glow |
| Buy Hover | primary-600 | white | stronger glow |
| Sell Hover | danger-600 | white | stronger glow |

#### Button Sizes
| Size | Padding | Font Size | Radius |
|------|---------|-----------|--------|
| Small | 8px 16px | 13px | 6px |
| Medium | 10px 20px | 14px | 8px |
| Large | 14px 28px | 16px | 10px |
| XL (Execute) | 18px 32px | 16px | 12px |

#### Quick Amount Buttons
```css
.quick-btn {
    background: var(--surface-1);
    border: 1px solid var(--border-primary);
    padding: 8px 12px;
    border-radius: 8px;
    color: var(--text-secondary);
    font-size: 12px;
    font-weight: 600;
}

.quick-btn:hover {
    border-color: var(--accent-500);
    color: var(--accent-500);
}

.quick-btn.active {
    background: var(--accent-500);
    border-color: var(--accent-500);
    color: white;
}
```

### 6.2 Cards

#### Base Card
```css
.card {
    background: var(--surface-1);
    border: 1px solid var(--border-primary);
    border-radius: 12px;
    padding: 20px;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-4px);
    border-color: var(--accent-500);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
}

/* Top accent line on hover */
.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--gradient-primary);
    opacity: 0;
    transition: opacity 0.3s;
}

.card:hover::before {
    opacity: 1;
}
```

#### Token Card Structure
```
┌─────────────────────────────────────────┐
│ [Social Proof Badge - optional]         │
├─────────────────────────────────────────┤
│ [Avatar 68px]  [Name]                   │
│                [Symbol]                  │
│                [Statement - 2 lines]     │
├─────────────────────────────────────────┤
│ [Trust Badge] [LP Locked] [Audit]       │
├─────────────────────────────────────────┤
│ [Progress Bar - Graduation %]           │
├─────────────────────────────────────────┤
│ [MC: $XX.XK]  [24h: $X.XK]             │
│ [Holders: XX] [Volume: $X.X↑]           │
├─────────────────────────────────────────┤
│ [Buy Button]             [❤️ Favorite]  │
└─────────────────────────────────────────┘
```

### 6.3 Inputs

#### Text Input
```css
.input {
    background: var(--surface-2);
    border: 1px solid var(--border-primary);
    border-radius: 10px;
    padding: 14px 16px;
    color: var(--text-primary);
    font-size: 16px;
    font-weight: 600;
    transition: all 0.2s ease;
}

.input:focus {
    outline: none;
    border-color: var(--accent-500);
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15);
}

.input::placeholder {
    color: var(--text-tertiary);
}
```

#### Input with Actions
```
┌──────────────────────────────────┬──────┐
│ 0.00                             │ MAX  │
└──────────────────────────────────┴──────┘
```

#### Search Input
```css
.search {
    width: 100%;
    padding: 13px 16px 13px 44px;
    background: var(--surface-2);
    border: 1px solid var(--border-primary);
    border-radius: 10px;
    background-image: url('search-icon.svg');
    background-repeat: no-repeat;
    background-position: 16px center;
}
```

### 6.4 Tabs

#### Tab Container
```css
.tabs-container {
    background: var(--surface-1);
    padding: 16px;
    border-radius: 14px;
    border: 1px solid var(--border-primary);
}

.tabs {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    scrollbar-width: none;
}
```

#### Tab Button
```css
.tab {
    background: var(--surface-2);
    border: 1px solid var(--border-primary);
    padding: 11px 18px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 14px;
    color: var(--text-secondary);
    white-space: nowrap;
    transition: all 0.2s ease;
}

.tab.active {
    background: var(--gradient-primary);
    color: white;
    border-color: var(--accent-500);
    box-shadow: 0 4px 20px rgba(139, 92, 246, 0.3);
}

.tab:hover:not(.active) {
    border-color: var(--accent-500);
    color: var(--accent-500);
    background: rgba(139, 92, 246, 0.1);
}
```

### 6.5 Badges

#### Trust Badges
| Type | Background | Border | Text |
|------|------------|--------|------|
| High Trust | rgba(16, 185, 129, 0.15) | rgba(16, 185, 129, 0.3) | primary-500 |
| Medium Trust | rgba(245, 158, 11, 0.15) | rgba(245, 158, 11, 0.3) | warning-500 |
| Low Trust | rgba(239, 68, 68, 0.15) | rgba(239, 68, 68, 0.3) | danger-500 |
| Locked | rgba(59, 130, 246, 0.15) | rgba(59, 130, 246, 0.3) | info-500 |

#### Badge Structure
```css
.badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 5px 11px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    border: 1px solid;
}
```

### 6.6 Progress Bars

#### Graduation Progress
```css
.progress-bar {
    height: 7px;
    background: var(--surface-2);
    border-radius: 999px;
    overflow: hidden;
    border: 1px solid var(--border-primary);
}

.progress-fill {
    height: 100%;
    background: var(--gradient-primary);
    border-radius: 999px;
    transition: width 0.5s ease;
    position: relative;
}

/* Shimmer animation */
.progress-fill::after {
    content: '';
    position: absolute;
    inset: 0;
    background: var(--gradient-shimmer);
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}
```

### 6.7 Toggles & Switches

#### Toggle Switch
```css
.toggle {
    width: 44px;
    height: 24px;
    background: var(--border-primary);
    border-radius: 12px;
    position: relative;
    cursor: pointer;
    transition: background 0.2s;
}

.toggle.active {
    background: var(--primary-500);
}

.toggle-knob {
    width: 20px;
    height: 20px;
    background: white;
    border-radius: 50%;
    position: absolute;
    top: 2px;
    left: 2px;
    transition: transform 0.2s;
}

.toggle.active .toggle-knob {
    transform: translateX(20px);
}
```

### 6.8 Modals & Overlays

```css
.modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.modal {
    background: var(--surface-1);
    border: 1px solid var(--border-primary);
    border-radius: 16px;
    padding: 24px;
    max-width: 480px;
    width: 90%;
    max-height: 90vh;
    overflow-y: auto;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}
```

---

## 7. LAYOUT PATTERNS

### 7.1 Master Layout

```
┌─────────────────────────────────────────────────────────────┐
│                         HEADER (70px)                        │
│  [Logo]  [Search............]            [Login] [Create]   │
├───────────────┬─────────────────────────────────────────────┤
│   SIDEBAR     │                                              │
│   (260px)     │              MAIN CONTENT                    │
│               │                                              │
│  [Main]       │   [Page Title]                              │
│  · Token List │   [Subtitle]                                 │
│  · Leaderboard│                                              │
│  · Create     │   [Tabs: Tab1 | Tab2 | Tab3]   [Sort][Filter]│
│               │                                              │
│  [Personal]   │   ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  · My Profile │   │ Card 1  │ │ Card 2  │ │ Card 3  │       │
│  · Dashboard  │   └─────────┘ └─────────┘ └─────────┘       │
│               │                                              │
│  [Earn]       │   ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  · Rewards    │   │ Card 4  │ │ Card 5  │ │ Card 6  │       │
│  · Referrals  │   └─────────┘ └─────────┘ └─────────┘       │
│               │                                              │
│  ─────────────│                                              │
│  [User Card]  │                                              │
└───────────────┴─────────────────────────────────────────────┘
```

### 7.2 Token Detail Layout

```
┌─────────────────────────────────────────────────────────────┐
│                         HEADER                               │
├───────────────┬──────────────────────────────┬──────────────┤
│   SIDEBAR     │         LEFT COLUMN          │  RIGHT COL   │
│               │                              │  (Trading)   │
│               │ [Token Header]               │              │
│               │ Avatar + Name + Symbol       │ [Token Info] │
│               │ + Description + Socials      │              │
│               │                              │ [BUY | SELL] │
│               │ [Progress Bar to DEX]        │              │
│               │                              │ [Amount]     │
│               │ [Market Metrics Grid]        │ [0.1][0.5][1]│
│               │ Price | MC | Volume | etc    │              │
│               │                              │ [Preview]    │
│               │ [Trust Level Section]        │              │
│               │ Score + Badges               │ [Settings]   │
│               │                              │              │
│               │ [Price Chart]                │ [Risk Badge] │
│               │ TradingView Integration      │              │
│               │                              │ [Execute]    │
│               │ [Tabs: Trades|Chat|Holders]  │              │
│               │ [Tab Content]                │              │
│               │                              │              │
└───────────────┴──────────────────────────────┴──────────────┘
```

### 7.3 Mobile Layout

```
┌─────────────────────────┐
│       HEADER (56px)      │
│  [Logo]         [Menu]   │
├─────────────────────────┤
│                          │
│      MAIN CONTENT        │
│   (Full Width, Scroll)   │
│                          │
│   [Search]               │
│                          │
│   [Tabs - Horizontal     │
│    Scroll]               │
│                          │
│   ┌───────────────────┐  │
│   │     Token Card    │  │
│   └───────────────────┘  │
│   ┌───────────────────┐  │
│   │     Token Card    │  │
│   └───────────────────┘  │
│                          │
├─────────────────────────┤
│     BOTTOM NAV (60px)    │
│ [🏠][📊][➕][👤][⚙️]     │
└─────────────────────────┘
```

---

## 8. ANIMATIONS & TRANSITIONS

### 8.1 Timing Functions

```css
/* Easing */
--ease-out:      cubic-bezier(0, 0, 0.2, 1);
--ease-in:       cubic-bezier(0.4, 0, 1, 1);
--ease-in-out:   cubic-bezier(0.4, 0, 0.2, 1);
--ease-spring:   cubic-bezier(0.47, 1.64, 0.41, 0.8);

/* Durations */
--duration-fast:   0.15s;
--duration-normal: 0.2s;
--duration-slow:   0.3s;
--duration-slower: 0.5s;
```

### 8.2 Standard Transitions

| Element | Property | Duration | Easing |
|---------|----------|----------|--------|
| Button hover | all | 0.2s | ease-out |
| Card hover | transform, shadow | 0.3s | ease-out |
| Tab switch | background, color | 0.2s | ease-in-out |
| Input focus | border, shadow | 0.2s | ease-out |
| Modal open | opacity, transform | 0.3s | ease-out |
| Dropdown | max-height, opacity | 0.2s | ease-out |

### 8.3 Micro-Animations

```css
/* Button Press */
.btn:active {
    transform: scale(0.98);
}

/* Card Lift */
.card:hover {
    transform: translateY(-4px);
}

/* Buy Button Pulse */
.buy-btn:hover {
    transform: translateY(-2px);
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4); }
    50% { box-shadow: 0 4px 30px rgba(16, 185, 129, 0.6); }
}

/* Progress Bar Shimmer */
@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Skeleton Loading */
@keyframes skeleton {
    0%, 100% { opacity: 0.4; }
    50% { opacity: 0.8; }
}
```

### 8.4 Page Transitions

```css
/* Page Enter */
.page-enter {
    opacity: 0;
    transform: translateY(10px);
}

.page-enter-active {
    opacity: 1;
    transform: translateY(0);
    transition: all 0.3s ease-out;
}

/* Page Exit */
.page-exit {
    opacity: 1;
}

.page-exit-active {
    opacity: 0;
    transition: opacity 0.2s ease-in;
}
```

---

## 9. RESPONSIVE DESIGN

### 9.1 Breakpoints

```css
/* Mobile First Approach */
--bp-xs:  0;        /* 0 - 479px */
--bp-sm:  480px;    /* 480 - 767px */
--bp-md:  768px;    /* 768 - 1023px */
--bp-lg:  1024px;   /* 1024 - 1279px */
--bp-xl:  1280px;   /* 1280 - 1535px */
--bp-2xl: 1536px;   /* 1536+ */
```

### 9.2 Responsive Behavior

| Component | Mobile (<768px) | Tablet (768-1024px) | Desktop (>1024px) |
|-----------|-----------------|---------------------|-------------------|
| **Header** | Logo + Menu icon | Full header | Full header |
| **Sidebar** | Hidden → Drawer | Collapsed (icons) | Full (260px) |
| **Token Grid** | 1 column | 2 columns | 3-4 columns |
| **Trading Panel** | Full-width modal | Side drawer | Fixed right column |
| **Tabs** | Horizontal scroll | Horizontal scroll | Full visible |
| **Bottom Nav** | Visible (60px) | Hidden | Hidden |
| **Card padding** | 16px | 20px | 24px |

### 9.3 Mobile-Specific Patterns

```css
/* Touch-friendly targets */
@media (max-width: 768px) {
    .btn {
        min-height: 44px;
        min-width: 44px;
    }
    
    .tab {
        padding: 12px 16px;
    }
    
    /* Full-width cards */
    .token-card {
        margin: 0 -16px;
        border-radius: 0;
        border-left: none;
        border-right: none;
    }
    
    /* Sticky CTA */
    .mobile-cta {
        position: fixed;
        bottom: 70px;
        left: 16px;
        right: 16px;
        z-index: 50;
    }
}
```

---

## 10. ACCESSIBILITY

### 10.1 Color Contrast

| Element | Min Contrast | Target |
|---------|--------------|--------|
| Body text | 4.5:1 (AA) | 7:1 (AAA) |
| Large text | 3:1 (AA) | 4.5:1 (AAA) |
| UI components | 3:1 | 4.5:1 |
| Focus indicators | 3:1 | 4.5:1 |

### 10.2 Focus States

```css
/* Custom focus ring */
*:focus-visible {
    outline: 3px solid var(--accent-500);
    outline-offset: 2px;
}

/* Remove default on styled elements */
button:focus,
input:focus,
a:focus {
    outline: none;
}

/* Add custom focus */
button:focus-visible,
input:focus-visible,
a:focus-visible {
    outline: 3px solid var(--accent-500);
    outline-offset: 2px;
}
```

### 10.3 Screen Reader Support

```html
<!-- Visually hidden but accessible text -->
<span class="sr-only">Current price</span>

<!-- ARIA labels -->
<button aria-label="Add to favorites">❤️</button>

<!-- ARIA roles -->
<div role="tablist">
    <button role="tab" aria-selected="true">Tab 1</button>
    <button role="tab" aria-selected="false">Tab 2</button>
</div>

<!-- Live regions for dynamic content -->
<div aria-live="polite" aria-atomic="true">
    Price updated: $0.00125
</div>
```

### 10.4 Keyboard Navigation

| Action | Key |
|--------|-----|
| Navigate tabs | ← → Arrow keys |
| Close modal | Escape |
| Submit form | Enter |
| Focus Buy | B |
| Focus Sell | S |
| Quick amounts | 1, 2, 3, 4 |

---

## 11. PAGE-BY-PAGE GUIDELINES

### 11.1 Token List (FR-001)

**Purpose:** Discovery và browsing tokens

**Key UI Elements:**
- Stats banner với KPIs
- Tab navigation (Discover, Trending, Top Volume, Graduated, Favorite)
- Search với auto-complete
- Filter/Sort dropdowns
- Token card grid

**UX Flow:**
```
User → Tabs → Browse/Search → View Card → Click → Token Detail
             ↓
        Filter/Sort → Refined Results
```

**Critical Metrics to Display:**
1. Token Name + Symbol + Avatar
2. Market Cap (primary metric)
3. 24h Volume + Change %
4. Holders count + trend
5. Trust Score badge
6. Graduation progress

---

### 11.2 Token Detail (FR-002)

**Purpose:** Phân tích token trước khi trade

**Key UI Elements:**
- Token header với full info
- Graduation progress bar (to $69K)
- Market metrics grid (6 items)
- Trust level section
- TradingView chart
- Tabs: Trades | Chat | Holders
- Fixed trading panel (right side)

**Information Hierarchy:**
1. **Hero Section:** Name, Price, 24h Change
2. **Progress:** How close to DEX graduation
3. **Trust:** Safety indicators
4. **Data:** Chart + Metrics
5. **Social:** Community chat

---

### 11.3 Trading Panel (FR-003)

**Purpose:** Execute trades nhanh và an toàn

**Key UI Elements:**
- BUY/SELL toggle (prominent)
- Market/Limit radio
- Amount input với quick buttons
- Currency switch (SOL ⇄ Token)
- Preview section (collapsible)
- Advanced settings (collapsible)
- Risk badge (🟢🟡🔴)
- Execute button

**UX Priorities:**
1. Minimize clicks to trade
2. Clear risk communication
3. Prevent accidental trades
4. Real-time price updates

**States:**
| State | Visual |
|-------|--------|
| Ready | Green CTA, clear preview |
| Processing | Loading spinner |
| Success | Green checkmark + confetti |
| Error | Red alert + error message |

---

### 11.4 My Profile (FR-004)

**Purpose:** Personal dashboard

**Tabs:**
1. **Holding Tokens** - Portfolio với P&L
2. **Created Tokens** - Read-only list
3. **Transaction History** - Trade logs
4. **Edit Profile** - Settings form
5. **Limit Orders** - Active orders

**Key UX Notes:**
- Username/Display Name: One-time edit → show warning
- Privacy toggles for Holdings/Transactions
- Portfolio value prominent với total P&L

---

### 11.5 Public Profile (FR-005)

**Purpose:** View other users

**Tabs:**
1. **Profile Info** - Bio, stats, badges
2. **Holding Tokens** - May be hidden
3. **Created Tokens** - Always visible
4. **Transaction History** - May be hidden

**Key UX Notes:**
- Respect privacy settings
- Show badges: Creator, Whale
- Link to their tokens

---

### 11.6 Creator Dashboard (FR-006)

**Purpose:** Manage created tokens

**2-Level Navigation:**
```
Level 1: Dashboard
├── Created Tokens     → [Manage Token] → Level 2
└── Creator Revenue    → [Claim]

Level 2: Token Management
├── Overview           → Metrics, Chart
├── Trusted Level      → LP Lock, Audit, Freeze
└── Community          → Create/Edit/Delete/Pin posts
```

---

### 11.7 Create Token (FR-007)

**Purpose:** 5-step wizard

**Steps:**
1. **Basic Info** - Name, Symbol, Statement, Description + AI Assist
2. **Avatar** - Upload or AI Generate
3. **Security** - LP Lock, Audit, Freeze (affects Trust Score)
4. **Initial Buy** - Optional 0.1-1 SOL
5. **Review** - Summary → Create → Success

**Wizard UX:**
- Progress indicator (1/5, 2/5...)
- Back/Next buttons
- Save draft option
- Validation before next step
- Success screen với Share + View Token buttons

---

### 11.8 Leaderboard (FR-008)

**Purpose:** Ranking by Market Cap

**Layout:**
```
┌──────────────────────────────────────────────┐
│     🥇 #1          🥈 #2          🥉 #3       │
│  [Featured]     [Featured]     [Featured]    │
│   Card x3       Card x3        Card x3       │
└──────────────────────────────────────────────┘
┌──────────────────────────────────────────────┐
│  # | Token | Creator | Holders | MC | Buy   │
├──────────────────────────────────────────────┤
│  4 | ...   | ...     | ...     | ... | [Buy]│
│  5 | ...   | ...     | ...     | ... | [Buy]│
└──────────────────────────────────────────────┘
```

---

### 11.9 Rewards (FR-009)

**Purpose:** Slot machine game

**Sections:**
1. **Broadcast Banner** - Live winners feed (marquee)
2. **Stats Cards** - Reward Balance | Your Tickets
3. **Slot Machine** - 5 reels với spin animation
4. **Game Info** - Multipliers + Rules
5. **History** - Winning spins table

**Gamification:**
- Exciting spin animation
- Celebration on win
- Clear payout rules

---

### 11.10 Referrals (FR-010)

**Purpose:** Invite & earn

**Sections:**
1. **Stats Overview** - 3 cards
2. **Referral Link** - Copy + Share buttons
3. **Claimable Rewards** - Amount + Claim CTA
4. **Referred Users Table** - Who, When, Volume, Earnings

**UX Focus:**
- One-click copy
- Pre-filled share messages
- Clear commission breakdown

---

### 11.11 Points (FR-011)

**Purpose:** Gamification & ranking

**Sections:**
1. **Points Display** - Current / Next Level
2. **Rank Card** - Tier + Progress bar
3. **How to Earn** - Collapsible info
4. **History Table** - Recent point activities

**Tier Visualization:**
```
🌱 Seed (0) → 🌿 Sprout (500) → 🌳 Sapling (2K) → 🌲 Tree (10K) → 🪷 Ancient (50K)
```

---

## 12. UI PATTERNS LIBRARY

### 12.1 Empty States

```
┌─────────────────────────────────────┐
│                                     │
│              [Icon]                 │
│                                     │
│        No tokens found              │
│                                     │
│   Try adjusting your filters or     │
│   search for something else         │
│                                     │
│        [Clear Filters]              │
│                                     │
└─────────────────────────────────────┘
```

### 12.2 Loading States

- **Cards:** Skeleton với shimmer animation
- **Tables:** Skeleton rows
- **Charts:** Placeholder với spinner
- **Buttons:** Spinner thay thế text

### 12.3 Error States

```
┌─────────────────────────────────────┐
│ ⚠️ Transaction Failed               │
│                                     │
│ Insufficient balance. You need      │
│ 0.5 more SOL to complete trade.     │
│                                     │
│ [Deposit SOL]        [Dismiss]      │
└─────────────────────────────────────┘
```

### 12.4 Success States

```
┌─────────────────────────────────────┐
│ ✅ Trade Completed!                  │
│                                     │
│ You bought 410,000 PSEED            │
│ for 1.0 SOL                         │
│                                     │
│ +1 Reward Ticket earned! 🎟️         │
│                                     │
│ [View Transaction]   [Close]        │
└─────────────────────────────────────┘
```

### 12.5 Confirmation Dialogs

```
┌─────────────────────────────────────┐
│ ⚠️ Confirm Sell                      │
│                                     │
│ You are selling all your PSEED      │
│ tokens at current market price.     │
│                                     │
│ Amount: 410,000 PSEED               │
│ Est. Receive: ~1.0 SOL              │
│                                     │
│ [Cancel]          [Sell Now]        │
└─────────────────────────────────────┘
```

### 12.6 Tooltips

- Trigger: Hover (desktop) / Long press (mobile)
- Delay: 200ms before show
- Position: Above element, auto-flip if edge
- Max-width: 280px
- Style: Dark bg, white text, arrow pointing to trigger

### 12.7 Toast Notifications

| Type | Icon | Color | Duration |
|------|------|-------|----------|
| Success | ✅ | green | 3s |
| Error | ❌ | red | 5s (with dismiss) |
| Warning | ⚠️ | yellow | 4s |
| Info | ℹ️ | blue | 3s |

---

## 📎 APPENDIX

### A. Icon Set

Sử dụng emoji cho MVP, có thể upgrade lên icon library sau:
- 🚀 Logo, Launch
- 📊 Token List
- 🏆 Leaderboard
- ➕ Create
- 👤 Profile
- ⚙️ Settings
- 🎁 Rewards
- 👥 Referrals
- ❤️ Favorite
- 🔒 Locked
- ✓ Verified
- 🟢🟡🔴 Risk levels

### B. Image Guidelines

| Type | Size | Format | Notes |
|------|------|--------|-------|
| Token Avatar | 256x256px min | PNG/WebP | Square, transparent OK |
| User Avatar | 128x128px min | PNG/WebP | Circular crop |
| Banner | 1200x400px | JPG/WebP | 3:1 ratio |

### C. Motion Principles

1. **Fast feedback** - Clicks respond immediately
2. **Smooth transitions** - No jarring changes
3. **Purpose-driven** - Animation serves function
4. **Subtle celebration** - Success feels rewarding

---

**END OF UI/UX DESIGN SYSTEM**

*Ready for implementation handoff to development team*
