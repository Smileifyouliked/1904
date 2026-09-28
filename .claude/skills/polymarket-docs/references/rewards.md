# Polymarket-Docs_Docs - Rewards

**Pages:** 3

---

## Get Account Rewards

**URL:** https://docs.polymarket.com/api-reference/get-account-rewards.md

**Contents:**
- OpenAPI

Reward periods run from 12:00 UTC to 12:00 UTC and are labeled by their UTC end date. OI rewards pay 6% APR on the account's full daily average gross OI across all instruments when the combined daily average gross OI of its rewards entity is at least $5M. Accounts without an entity mapping qualify independently. The first reward period starts at 2026-07-06 12:00 UTC. If no date range is provided, the latest computed reward period is returned.

<Badge color="gray" size="md">Request Weight: **2**</Badge>

**Examples:**

Example 1 (text):
```text
openapi: 3.0.3
info:
  title: Polymarket Perps HTTP API
  version: 1.0.0
  description: HTTP API for Polymarket perpetual trading system.
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
servers:
  - url: https://api.perpetuals.polymarket.com
    description: Production Perps HTTP API
security: []
paths:
  /v1/account/rewards:
    get:
      summary: Get Account Rewards
      description: >
        Get per-instrument daily liquidity reward shares for the authenticated
        account.

        Reward periods run from 12:00 UTC to 12:00 UTC and are labeled by their
        UTC end date.

        OI rewards pay 6% APR on the account's full daily average gross OI
        across all

        instruments when the combined daily average gross OI of its rewards
        entity is

        at least $5M. Accounts without an entity mapping qualify independently.

        The first reward period starts at 2026-07-06 12:00 UTC. If no date range
        is provided,

        the latest computed reward period is returned.
      operationId: getAccountRewards
      parameters:
        - name: date
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/date'
        - name: start_date
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/start_date'
        - name: end_date
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/end_date'
        - name: limit
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/limit'
      responses:
        '200':
          description: Account rewards response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountRewards'
        '400':
          $ref: '#/components/responses/Error400Response'
        '401':
          $ref: '#/components/responses/Error401Response'
        '429':
          $ref: '#/components/responses/Error429Response'
        '500':
          $ref: '#/components/responses/Error500Response'
      security:
        - polymarket_proxy: []
          polymarket_secret: []
components:
  schemas:
    date:
      type: string
      description: UTC reward period end date in YYYY-MM-DD format
      example: '2026-05-10'
    start_date:
      type: string
      description: Inclusive UTC start date in YYYY-MM-DD format
      example: '2026-05-01'
    end_date:
      type: string
      description: Inclusive UTC end date in YYYY-MM-DD format
      example: '2026-05-10'
    limit:
      type: integer
      description: Maximum number of entries to return
      example: 100
    AccountRewards:
      type: object
      required:
        - data
        - more
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/AccountReward'
        more:
          $ref: '#/components/schemas/more'
    AccountReward:
      type: object
      required:
        - date
        - maker_share_7d
        - reward_distributed
        - breakdown
      properties:
        date:
          $ref: '#/components/schemas/date'
        maker_share_7d:
          $ref: '#/components/schemas/maker_share_7d'
        reward_distributed:
          $ref: '#/components/schemas/reward_distributed'
        breakdown:
          type: array
          items:
            $ref: '#/components/schemas/AccountRewardInstrument'
        oi_rewards:
          $ref: '#/components/schemas/AccountRewardOi'
    more:
      type: boolean
      description: More data available
    Error400:
      title: Error400
      type: object
      required:
        - status
        - error
      properties:
        status:
          type: string
          enum:
            - err
        error:
          $ref: '#/components/schemas/error'
    Error401:
      title: Error401
      type: object
      required:
        - status
        - error
      properties:
        status:
          type: string
          enum:
            - err
        error:
          $ref: '#/components/schemas/error'
    Error429:
      title: Error429
      type: object
      required:
        - status
        - error
      properties:
        status:
          type: string
          enum:
            - err
        error:
          $ref: '#/components/schemas/error'
    Error500:
      title: Error500
      type: object
      required:
        - status
        - error
      properties:
        status:
          type: string
          enum:
            - err
        error:
          $ref: '#/components/schemas/error'
    maker_share_7d:
      type: string
      description: Rolling 7-day account maker volume divided by total exchange volume
      example: '0.35'
    reward_distributed:
      type: boolean
      description: Whether rewards for this period have been marked as distributed
      example: true
    AccountRewardInstrument:
      type: object
      required:
        - instrument_id
        - reward_pool
        - reward_amount
      properties:
        instrument_id:
          $ref: '#/components/schemas/instrument_id'
        reward_pool:
          $ref: '#/components/schemas/reward_pool'
        reward_amount:
          $ref: '#/components/schemas/reward_amount'
    AccountRewardOi:
      type: object
      required:
        - account_oi
        - reward_amount
      properties:
        account_oi:
          $ref: '#/components/schemas/account_oi'
        reward_amount:
          $ref: '#/components/schemas/reward_amount'
    error:
      type: string
      description: >-
        Error identifier. For domain rejections and transport errors
        (`401`/`404`/`429`/`500`) this is a stable, machine-readable snake_case
        identifier that is part of the API contract and safe to branch on, e.g.
        `insufficient_margin`, `insufficient_balance`, `order_not_found`,
        `reduce_only_invalid`, `price_outside_bounds`, `position_not_found`,
        `position_exists`, `open_orders_exist`, `invalid_margin_mode`,
        `invalid_margin_amount`, `margin_below_required_initial`,
        `account_liquidating`, `unauthorized`, `not_found`. For `400` it is a
        human-readable validation detail whose wording may change. See the Error
        handling guide for the domain identifiers. (Post-only / Fill-or-Kill
        outcomes are order statuses such as `post_only_rejected`, not
        rejections.)
      example: insufficient_margin
    instrument_id:
      type: integer
      description: Instrument ID
    reward_pool:
      type: string
      description: Configured reward pool for the instrument
      example: '1000'
    reward_amount:
      type: string
      description: Reward amount attributed to this reward row
      example: '127.50344'
    account_oi:
      type: string
      description: >-
        Daily average gross open-interest notional for this account across all
        instruments
      example: '3200000'
  responses:
    Error400Response:
      description: |
        Bad request — the request was malformed or failed validation (bad query
        parameters, unparseable body, invalid signature, or a domain pre-check).
        The `error` field is a human-readable validation detail.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error400'
    Error401Response:
      description: >
        Unauthorized — missing or invalid `POLYMARKET-PROXY` /
        `POLYMARKET-SECRET`

        credentials. `error` is `unauthorized`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error401'
    Error429Response:
      description: >
        Too Many Requests. `error` distinguishes the limit that was hit:

        `ip_rate_limited` (per-IP token bucket), `action_rate_limited`
        (per-account

        action rate), or `open_orders_limit` (resting open-order cap).
      headers:
        Retry-After:
          description: >
            Whole seconds to wait before retrying. Present only on token-bucket

            rate-limit rejections (`ip_rate_limited` and `action_rate_limited`);
            a

            conservative estimate of when enough capacity will have refilled to

            admit the request. Absent on `open_orders_limit`, which is a
            capacity

            limit, not a rate limit — waiting does not free order slots; cancel

            resting orders or wait for fills instead.
          schema:
            type: integer
            example: 2
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error429'
    Error500Response:
      description: |
        Internal server error. `error` is `internal_error`.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error500'
  securitySchemes:
    polymarket_proxy:
      type: apiKey
      name: POLYMARKET-PROXY
      in: header
      description: Proxy address
    polymarket_secret:
      type: apiKey
      name: POLYMARKET-SECRET
      in: header
      description: Correponding proxy secret

````
```

---

## Liquidity Rewards

**URL:** https://docs.polymarket.com/perps/liquidity-rewards.md

**Contents:**
- How Rewards Are Allocated
- Eligibility And Maker Score
- Liquidity Score
  - Distance Tiers
  - Two-Sided Liquidity
- Uptime
- Summary Of Program Parameters

Every Perps account is automatically considered for daily liquidity rewards. There is no application or participant allowlist: the same eligibility threshold and scoring rules apply to every maker.

Rewards are calculated for 24-hour periods from 12:00 UTC to 12:00 UTC. Each period is labeled by its end date, and earned rewards are credited in pUSD to the earning Perps account.

The program distributes **\$75,000 per day**, split evenly across active Perps markets. Each market has one daily pool. Makers with a nonzero score divide that market's entire pool in proportion to their scores.

A maker's score combines three inputs:

| Input                  | What it rewards                                              | | ---------------------- | ------------------------------------------------------------ | | Maker score            | Meaningful maker participation over the trailing seven days  | | Active liquidity score | Deep, balanced liquidity close to the midpoint while quoting | | Uptime                 | Consistent two-sided quoting throughout the reward period    |

The final reward for an account is its share of all positive raw scores in that market multiplied by the market's daily pool.

An account must represent at least **1% of trailing seven-day maker volume** to qualify. For accounts in a rewards entity, the entity's combined maker share is used. During the first seven days of the program, the lookback begins at the program start rather than reaching into earlier trading.

Maker share is capped at 25% before it is converted into the maker score:

This gives additional credit for maker participation above the 1% threshold without allowing historical volume to dominate the full calculation. Maker share above 25% receives no additional maker-score credit.

Trades between the same account, or between accounts in the same known rewards entity, do not count toward maker share.

The order book is sampled repeatedly throughout each reward period. Only resting liquidity within 20 basis points of the midpoint can score.

| Distance From Midpoint             | Weight | | ---------------------------------- | -----: | | Within 5 bps                       |   1.00 | | More than 5 bps and within 10 bps  |   0.25 | | More than 10 bps and within 20 bps |   0.10 | | Beyond 20 bps                      |      0 |

The midpoint is the average of the best bid and best ask. Each tier boundary is rounded outward to the next valid price tick, so an order is always evaluated at a valid price for its market.

For each account, side, market, and snapshot, resting notional in the same tier is added together. Scored notional is capped at **\$100,000 per tier** before the tier weight is applied.

The same \$100,000 cap applies to every market and independently to each side and each of the three distance tiers. It is not one shared cap across an account's entire order book.

Bid and ask tier scores are added separately, then combined with a harmonic mean:

A snapshot scores only when both sides have nonzero liquidity within 20 bps. The harmonic mean penalizes an imbalanced book and produces a score of zero when either side is absent.

Uptime is the share of completed snapshots in which the account had qualifying liquidity on both sides:

The active liquidity score is the account's average snapshot score across its qualifying snapshots. Keeping liquidity quality and uptime separate means deep quotes receive credit when they are live, while intermittent quoting is still penalized.

| Parameter                | Value                  | | ------------------------ | ---------------------- | | Daily program budget     | \$75,000               | | Reward period            | 12:00 UTC to 12:00 UTC | | Maker-share lookback     | 7 days                 | | Eligibility threshold    | 1% maker share         | | Maker-score cap          | 25% maker share        | | Maker-score exponent     | 0.35                   | | Liquidity-score exponent | 0.65                   | | Uptime exponent          | 1.0                    | | Scoring bands            | 5, 10, and 20 bps      | | Band weights             | 1.00, 0.25, and 0.10   | | Credited notional cap    | \$100,000 per tier     | | Reference price          | Midpoint               | | Side combination         | Harmonic mean          |

<Note> Polymarket may change program parameters or disqualify activity that is manipulative, abusive, or otherwise violates the Terms of Service. </Note>

**Examples:**

Example 1 (text):
```text
raw_score = maker_score^0.35 × active_liquidity_score^0.65 × uptime
```

Example 2 (text):
```text
maker_score = log(1 + min(maker_share, 25%) / 1%) / log(1 + 25% / 1%)
```

Example 3 (text):
```text
tier_score = min(resting_notional_in_tier, $100,000) × tier_weight
```

Example 4 (text):
```text
snapshot_score = 2 × bid_score × ask_score / (bid_score + ask_score)
```

---

## Liquidity Rewards

**URL:** https://docs.polymarket.com/programs/liquidity-rewards.md

**Contents:**
- Crypto TWAP Rewards
  - 5-Minute Markets — \$550k
  - 15-Minute Markets — \$350k
  - 4-Hour Markets — \$100k
- Methodology
  - Variables
- Equations
  - 1. Order Scoring Function
  - 2. First Market Side Score
  - 3. Second Market Side Score

By posting resting limit orders, liquidity providers (makers) are automatically eligible for Polymarket's incentive program. Rewards are distributed directly to maker addresses daily at midnight UTC.

The program is designed to:

<Note> The minimum reward payout is **\$1**; amounts below this will not be paid. </Note>

<Tip> Each incentivized market defines a minimum qualifying order size, maximum qualifying spread, and reward allocation. See [Liquidity Reward Settings](/market-data/market-details#liquidity-reward-settings) to read the current configuration for a market. </Tip>

To support liquidity through this transition, Polymarket is adding **\$1M** in liquidity rewards across impacted markets through the month of August. This allocation applies only to crypto **5-minute**, **15-minute**, and **4-hour** markets that settle on TWAP.

<Info> This program has ended. The August allocation is no longer active. </Info>

<Note> The pools below are configured reward caps. Actual payouts depend on eligible quoting and the scoring methodology on this page. </Note>

| Allocation          | Amount              | | ------------------- | ------------------- | | BTC                 | \$300k              | | SOL, ETH, HYPE, XRP | \$200k split evenly | | BNB, DOGE           | \$50k split evenly  |

| Allocation          | Amount              | | ------------------- | ------------------- | | BTC                 | \$225k              | | SOL, ETH, HYPE, XRP | \$100k split evenly | | BNB, DOGE           | \$25k split evenly  |

| Allocation          | Amount             | | ------------------- | ------------------ | | BTC                 | \$50k              | | SOL, ETH, HYPE, XRP | \$40k split evenly | | BNB, DOGE           | \$10k split evenly |

Liquidity providers are rewarded based on a formula that rewards participation in markets, boosts two-sided depth (single-sided orders still score), and tighter spread vs the size-cutoff-adjusted midpoint. Each market configures a max spread and min size cutoff within which orders are considered. The average of rewards earned is determined by the relative share of each participant's Q<sub>n</sub> in market m.

| Variable       | Description                                                      | | -------------- | ---------------------------------------------------------------- | | S              | Order position scoring function                                  | | v              | Max spread from midpoint (in cents)                              | | s              | Spread from size-cutoff-adjusted midpoint                        | | b              | In-game multiplier                                               | | m              | Market                                                           | | m'             | Market complement (i.e. NO if m = YES)                           | | n              | Trader index                                                     | | u              | Sample index                                                     | | c              | Scaling factor (currently 3.0 on all markets)                    | | Q<sub>ne</sub> | Point total for book one for a sample                            | | Q<sub>no</sub> | Point total for book two for a sample                            | | Spread%        | Distance from midpoint (bps or relative) for order n in market m | | BidSize        | Share-denominated quantity of bid                                | | AskSize        | Share-denominated quantity of ask                                |

Quadratic scoring rule for an order based on position between the adjusted midpoint and the minimum qualifying spread:

$S(v,s)= (\frac{v-s}{v})^2 \cdot b$

$Q*{one}= S(v,Spread*{m*1}) \cdot BidSize*{m*1} + S(v,Spread*{m*2}) \cdot BidSize*{m*2} + \dots $ $ + S(v, Spread*{m^\prime*1}) \cdot AskSize*{m^\prime*1} + S(v, Spread*{m^\prime*2}) \cdot AskSize*{m^\prime_2}$

$Q*{two}= S(v,Spread*{m*1}) \cdot AskSize*{m*1} + S(v,Spread*{m*2}) \cdot AskSize*{m*2} + \dots $ $ + S(v, Spread*{m^\prime*1}) \cdot BidSize*{m^\prime*1} + S(v, Spread*{m^\prime*2}) \cdot BidSize*{m^\prime_2}$

Boosts two-sided liquidity by taking the minimum of Q<sub>ne</sub> and Q<sub>no</sub>, while still rewarding single-sided liquidity at a reduced rate (divided by c).

**If midpoint is in range \[0.10, 0.90]** — single-sided liquidity can score:

$Q*{\min} = \max(\min({Q*{one}, Q*{two}}), \max(Q*{one}/c, Q_{two}/c))$

**If midpoint is in range \[0, 0.10) or (0.90, 1.0]** — liquidity must be double-sided to score:

$Q*{\min} = \min({Q*{one}, Q_{two}})$

Q<sub>min</sub> of a market maker divided by the sum of all Q<sub>min</sub> across market makers in a given sample:

$Q*{normal} = \frac{Q*{min}}{\sum*{n=1}^{N}{(Q*{min})_n}}$

Sum of all Q<sub>normal</sub> for a trader across all samples in an epoch. An epoch is one UTC day; the order book is sampled once per minute at a random offset, so an epoch contains up to 1,440 samples:

$Q*{epoch} = \sum*{u=1}^{1,440}{(Q*{normal})*u}$

Normalizes Q<sub>epoch</sub> by dividing by the sum of all market makers' Q<sub>epoch</sub> in a given epoch. This value is multiplied by the rewards available for the market to get a trader's reward:

$Q*{final}=\frac{Q*{epoch}}{\sum*{n=1}^{N}{(Q*{epoch})_n}}$

Assume an adjusted market midpoint of 0.50 and a max spread config of 3 cents for both m and m'.

A trader has the following open orders:

$$ Q_{ne} = \left( \frac{(3-1)}{3} \right)^2 \cdot 100 + \left( \frac{(3-2)}{3} \right)^2 \cdot 200 + \left( \frac{(3-1)}{3} \right)^2 \cdot 100 $$

Q<sub>ne</sub> is calculated every minute using random sampling.

The same trader also has:

$$ Q_{no} = \left( \frac{(3-1.5)}{3} \right)^2 \cdot 100 + \left( \frac{(3-2)}{3} \right)^2 \cdot 100 + \left( \frac{(3-.5)}{3} \right)^2 \cdot 200 $$

Q<sub>no</sub> is calculated every minute using random sampling.

---
