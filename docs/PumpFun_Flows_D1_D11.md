# PumpFun Clone -- System Specification (Flows D1--D11)

## Overview

This document contains the consolidated functional flows for the
PumpFun-style meme-token platform.\
Vietnam users are blocked; all other regions can access the system.

------------------------------------------------------------------------

# D1 -- System Overview

-   Location check â†’ if VN â†’ block.
-   From Home Screen, user may navigate to:
    -   Token List (D2)
    -   Token Detail (via D2 â†’ D3)
    -   Buy/Sell Panel (via D3 â†’ D4)
    -   Search (D5)
    -   My Profile (D6)
    -   Public Profile (D7)
    -   Created Coins Management (D8)
    -   Token Management Detail (D8.1)
    -   Create Token (D9)
    -   Rewards (D10)
    -   Referrals (D11)

------------------------------------------------------------------------

# D2 -- Token List

-   Default list showing tokens.
-   6 Tabs:
    -   Discover
    -   Trending
    -   Top Volume
    -   Top Market Cap
    -   Graduated
    -   Favorite
-   Filters: NSFW, Market Cap, Volume, Trusted Level.
-   Search is inline (D5).
-   Clicking a token â†’ Token Detail (D3).
-   Add to Favorite available on each card.
-   From Leaderboard (in D1) user also goes to Token Detail.

------------------------------------------------------------------------

# D3 -- Token Detail

-   Shows:
    -   Chart
    -   Market Cap, Volume, Holders
    -   Trust Level
-   Community:
    -   View posts
    -   Like, reply
    -   Chat room
-   Holders List:
    -   Clicking a holder opens Public Profile (D7)
-   Transaction History
-   Buy/Sell button â†’ Trade Panel (D4)

------------------------------------------------------------------------

# D4 -- Trading

### Basic Mode

1.  User inputs amount.
2.  Optional settings: Anti-MEV, Speed, Auto-retry.
3.  System risk check:
    -   Red â†’ block Buy (Sell only)
    -   Yellow â†’ warning confirmation
    -   Green â†’ proceed
4.  Submit transaction â†’ success / fail.
5.  Success gives 1 reward ticket.
6.  Fail â†’ retry or exit.

### Advanced Order Mode

1.  User inputs amount and target price.
2.  Settings: Anti-MEV, Speed, Auto-retry.
3.  User confirms â†’ Save Advanced Order.
4.  Active orders shown in My Profile \> Limit Orders (D6).

------------------------------------------------------------------------

# D5 -- Search

-   Inline search inside Token List.
-   Matches by token name or symbol.
-   Combined with:
    -   Current tab
    -   Filters (NSFW, Market Cap, Volume, Trusted)
-   Clicking result â†’ Token Detail.

------------------------------------------------------------------------

# D6 -- My Profile

5 tabs:

### Holding Tokens

-   List of tokens user owns.
-   Click â†’ Token Detail.

### Created Tokens

-   List of tokens the user created (read-only).
-   No Manage Token here.
-   Click â†’ Token Detail.

### Staking

-   List of staked tokens.
-   Click â†’ Token Detail.

### Edit Profile

-   Editable: Username, Display name, Avatar, Bio, X, Telegram, Email.
-   Wallet address: read-only.

### Limit Orders

-   Shows only ACTIVE advanced orders.
-   Click â†’ Order Detail â†’ Cancel.

------------------------------------------------------------------------

# D7 -- Public Profile

-   Entirely read-only.
-   Tabs:
    -   Metadata (username, display name, bio, social links, email,
        wallet)
    -   Holding Tokens â†’ click â†’ Token Detail
    -   Created Tokens â†’ click â†’ Token Detail
    -   Staking â†’ click â†’ Token Detail
    -   Limit Orders (read-only)

------------------------------------------------------------------------

# D8 -- Created Coins Management (Level 1)

2 Tabs:

### Created Tokens

-   List of tokens user created.
-   Each item has **Manage Token** button.
-   Clicking â†’ Token Management Detail (D8.1).

### Creator Revenue

-   Shows:
    -   Total revenue
    -   Unclaimed revenue
-   Claim requires connected wallet.

------------------------------------------------------------------------

# D8.1 -- Token Management Detail (Level 2)

3 Tabs:

### Overview

-   Token name, avatar, description
-   Chart
-   Market Cap, Volume, Holders
-   Supply info
-   Status

### Trusted Level

-   LP Lock
-   Audit Token
-   Future settings placeholder.

### Community Management

-   List posts
-   View post detail
-   Delete post
-   Pin/unpin post
-   Create new post (title + content)

------------------------------------------------------------------------

# D9 -- Create Token

5-step flow: 1. Basic info: name, symbol, description (AI-assisted). 2.
Avatar upload or AI generator. 3. Trusted Level initial settings (LP
Lock, Audit, etc.) 4. Optional initial buy. 5. Create Token: - Deploy -
Initialize - Show success screen - No redirect to Creator Dashboard.

------------------------------------------------------------------------

# D10 -- Rewards

3 Tabs:

### Games

-   Select game â†’ spend ticket â†’ play â†’ win or lose.
-   Win â†’ reward added to balance.

### Missions

-   Login streak, trade streak, invite tasks.
-   Completing missions â†’ earn tickets.

### Reward Balance

-   View total rewards and claimable amount.
-   Claim requires wallet connection.

### Broadcast

-   Live feed of winners.

------------------------------------------------------------------------

# D11 -- Referrals

Sections:

### Referral Link

-   Copy invite link.

### Rewards Summary

-   Total referral earnings.
-   Claimable amount (requires wallet).
-   Claim rewards â†’ transfer to wallet.

### Referred Users List

-   Name
-   Join date
-   Trade volume
-   Earnings from that user
-   Click â†’ Public Profile (D7)

------------------------------------------------------------------------

# END OF DOCUMENT
