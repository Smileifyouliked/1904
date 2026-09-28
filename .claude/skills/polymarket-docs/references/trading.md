# Polymarket-Docs_Docs - Trading

**Pages:** 27

---

## Fees

**URL:** https://docs.polymarket.com/trading/fees.md

**Contents:**
- Fee Structure
- Fee Tables (100 Shares)
- Fee Precision

Polymarket charges a small taker fee on certain markets. Fees are set by the protocol and applied at match time — you don't include fee information in your orders. These fees fund the [Maker Rebates Program](/programs/maker-rebates), which redistributes fees daily to market makers to incentivize deeper liquidity and tighter spreads. Takers can also earn a portion of fees back through the tiered [Taker Rebate Program](/programs/taker-rebates).

**Geopolitical and world events markets are fee-free.** Polymarket does not charge fees or profit from trading activity on these markets. There are also no Polymarket fees to deposit or withdraw USDC (though intermediaries like Coinbase or MoonPay may charge their own fees).

Fees are calculated using the following formula:

Where **C** = number of shares traded and **p** = price of the shares. See [Market Details](/market-data/market-details#trading-fees) to read the fee parameters for a market.

<Note>**Makers are never charged fees.** Only takers pay fees.</Note>

The fee parameters differ by market category:

| Category        | Taker Fee Rate | Maker Fee Rate | Maker Rebate | | --------------- | -------------- | -------------- | ------------ | | Crypto          | 0.07           | 0              | 20%          | | Sports          | 0.05           | 0              | 15%          | | Finance         | 0.04           | 0              | 25%          | | Politics        | 0.04           | 0              | 25%          | | Economics       | 0.05           | 0              | 25%          | | Culture         | 0.05           | 0              | 25%          | | Weather         | 0.05           | 0              | 25%          | | Other / General | 0.05           | 0              | 25%          | | Mentions        | 0.04           | 0              | 25%          | | Tech            | 0.04           | 0              | 25%          | | Geopolitics     | 0              | 0              | —            |

Taker fees are calculated in USDC and vary based on the share price. The fee amount in USDC is symmetric around 50% probability — a trade at 30¢ incurs the same dollar fee as a trade at 70¢.

<Frame> <div className="p-3 bg-white rounded-xl"> <iframe title="Fee Curves" aria-label="Line chart" id="datawrapper-chart-dJ74e" src="https://datawrapper.dwcdn.net/dJ74e/" scrolling="no" frameborder="0" width={700} style={{ width: "0", minWidth: "100% !important", border: "none" }} height="450" data-external="1" /> </div> </Frame>

<Tabs> <Tab title="Crypto"> | Price  | Trade Value | Taker Fee (USDC) | | ------ | ----------- | ---------------- | | \$0.01 | \$1         | \$0.07           | | \$0.05 | \$5         | \$0.33           | | \$0.10 | \$10        | \$0.63           | | \$0.15 | \$15        | \$0.89           | | \$0.20 | \$20        | \$1.12           | | \$0.25 | \$25        | \$1.31           | | \$0.30 | \$30        | \$1.47           | | \$0.35 | \$35        | \$1.59           | | \$0.40 | \$40        | \$1.68           | | \$0.45 | \$45        | \$1.73           | | \$0.50 | \$50        | \$1.75           | | \$0.55 | \$55        | \$1.73           | | \$0.60 | \$60        | \$1.68           | | \$0.65 | \$65        | \$1.59           | | \$0.70 | \$70        | \$1.47           | | \$0.75 | \$75        | \$1.31           | | \$0.80 | \$80        | \$1.12           | | \$0.85 | \$85        | \$0.89           | | \$0.90 | \$90        | \$0.63           | | \$0.95 | \$95        | \$0.33           | | \$0.99 | \$99        | \$0.07           |

<Tab title="Sports"> | Price  | Trade Value | Taker Fee (USDC) | | ------ | ----------- | ---------------- | | \$0.01 | \$1         | \$0.05           | | \$0.05 | \$5         | \$0.24           | | \$0.10 | \$10        | \$0.45           | | \$0.15 | \$15        | \$0.64           | | \$0.20 | \$20        | \$0.80           | | \$0.25 | \$25        | \$0.94           | | \$0.30 | \$30        | \$1.05           | | \$0.35 | \$35        | \$1.14           | | \$0.40 | \$40        | \$1.20           | | \$0.45 | \$45        | \$1.24           | | \$0.50 | \$50        | \$1.25           | | \$0.55 | \$55        | \$1.24           | | \$0.60 | \$60        | \$1.20           | | \$0.65 | \$65        | \$1.14           | | \$0.70 | \$70        | \$1.05           | | \$0.75 | \$75        | \$0.94           | | \$0.80 | \$80        | \$0.80           | | \$0.85 | \$85        | \$0.64           | | \$0.90 | \$90        | \$0.45           | | \$0.95 | \$95        | \$0.24           | | \$0.99 | \$99        | \$0.05           |

<Tab title="Finance / Politics / Mentions / Tech"> | Price  | Trade Value | Taker Fee (USDC) | | ------ | ----------- | ---------------- | | \$0.01 | \$1         | \$0.04           | | \$0.05 | \$5         | \$0.19           | | \$0.10 | \$10        | \$0.36           | | \$0.15 | \$15        | \$0.51           | | \$0.20 | \$20        | \$0.64           | | \$0.25 | \$25        | \$0.75           | | \$0.30 | \$30        | \$0.84           | | \$0.35 | \$35        | \$0.91           | | \$0.40 | \$40        | \$0.96           | | \$0.45 | \$45        | \$0.99           | | \$0.50 | \$50        | \$1.00           | | \$0.55 | \$55        | \$0.99           | | \$0.60 | \$60        | \$0.96           | | \$0.65 | \$65        | \$0.91           | | \$0.70 | \$70        | \$0.84           | | \$0.75 | \$75        | \$0.75           | | \$0.80 | \$80        | \$0.64           | | \$0.85 | \$85        | \$0.51           | | \$0.90 | \$90        | \$0.36           | | \$0.95 | \$95        | \$0.19           | | \$0.99 | \$99        | \$0.04           |

<Tab title="Economics / Culture / Weather / Other"> | Price  | Trade Value | Taker Fee (USDC) | | ------ | ----------- | ---------------- | | \$0.01 | \$1         | \$0.05           | | \$0.05 | \$5         | \$0.24           | | \$0.10 | \$10        | \$0.45           | | \$0.15 | \$15        | \$0.64           | | \$0.20 | \$20        | \$0.80           | | \$0.25 | \$25        | \$0.94           | | \$0.30 | \$30        | \$1.05           | | \$0.35 | \$35        | \$1.14           | | \$0.40 | \$40        | \$1.20           | | \$0.45 | \$45        | \$1.24           | | \$0.50 | \$50        | \$1.25           | | \$0.55 | \$55        | \$1.24           | | \$0.60 | \$60        | \$1.20           | | \$0.65 | \$65        | \$1.14           | | \$0.70 | \$70        | \$1.05           | | \$0.75 | \$75        | \$0.94           | | \$0.80 | \$80        | \$0.80           | | \$0.85 | \$85        | \$0.64           | | \$0.90 | \$90        | \$0.45           | | \$0.95 | \$95        | \$0.24           | | \$0.99 | \$99        | \$0.05           |

Fees are rounded to 5 decimal places. The smallest fee charged is **0.00001 USDC**. Anything smaller rounds to zero, so very small trades near the extremes may incur no fee at all.

**Examples:**

Example 1 (text):
```text
fee = C × feeRate × p × (1 - p)
```

Example 2 (text):
```text
The fee in USDC **peaks at 50%** probability (\$1.75) and decreases symmetrically toward both extremes.
```

Example 3 (text):
```text
The fee in USDC **peaks at 50%** probability (\$1.25) and decreases symmetrically toward both extremes.
```

Example 4 (text):
```text
The fee in USDC **peaks at 50%** probability (\$1.00) and decreases symmetrically toward both extremes.
```

---

## Place Orders

**URL:** https://docs.polymarket.com/trading/place-orders.md

**Contents:**
- Limit Orders
  - Place a Limit Order
  - Post-Only Orders
- Market Orders
  - Place a Market Order
  - Cap Market Buy Spending
  - Market Order Types
- Create and Post Separately
- Post a Batch of Orders
- Builder Attribution

Place a market order to trade against available liquidity immediately, or use a limit order to specify a price and wait for a match.

Before placing an order, choose an outcome token and confirm that the market is [accepting orders](/market-data/market-details#market-status). The examples below assume you already have a market object; to find or fetch one, see [Discover Markets](/market-data/discover-markets).

<Tabs> <Tab title="TypeScript"> Given a market, read its outcome token IDs:

<Tab title="Python"> Given a market, read its outcome token IDs:

<Tab title="API"> Given a market object, its outcome token IDs are stored as a JSON-encoded array:

A limit order specifies the price at which you are willing to trade and can rest on the book until it fills, expires, or you cancel it. Use one when price control matters more than immediate execution.

A limit order also defines how long any unfilled amount remains active:

| Lifetime                  | Behavior                                              | Use when                                      | | ------------------------- | ----------------------------------------------------- | --------------------------------------------- | | Good Till Cancelled (GTC) | Remains active until it fills or you cancel it.       | The order has no deadline.                    | | Good Till Date (GTD)      | Remains active until the expiration time you specify. | The order should expire before a known event. |

<Note> GTD orders expire one minute before their stated expiration as a security threshold. To set an effective lifetime of N seconds, use `now + 60 + N`. In addition, the expiration must be at least **3 minutes** in the future — orders expiring sooner are rejected — so the minimum effective lifetime is about two minutes. </Note>

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, place the limit order and check its response:

<Tab title="Python"> Given an `AsyncSecureClient`, place the limit order and check its response. The synchronous `SecureClient` provides the same method.

<Tab title="API"> Build the limit order from its price and size, then sign and submit it:

A post-only order adds liquidity only: if it would match immediately against the book, it is rejected instead of taking. Use it to guarantee you quote as a maker.

<Tip> Market makers use post-only orders to add liquidity with resting orders. </Tip>

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, set `postOnly` when placing the limit order:

<Tab title="Python"> Given an `AsyncSecureClient`, set `post_only` when placing the limit order. The synchronous `SecureClient` provides the same method.

<Tab title="API"> Follow the API workflow in [Place a Limit Order](#place-a-limit-order), then add `postOnly: true` to the final request alongside a GTC or GTD `orderType`. For example, submit a GTC post-only order:

A market order uses the same underlying order as a limit order but derives a marketable price from current order-book liquidity. This allows it to execute immediately instead of resting on the book. Use a market order when execution matters more than setting an exact price.

Read the market's [trading constraints](/market-data/market-details#trading-constraints) before deciding how much to buy or sell.

The examples below use Fill and Kill (FAK), which fills available liquidity immediately and cancels any remainder. See [Market Order Types](#market-order-types) for Fill or Kill (FOK).

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, estimate the price and place the market order:

<Tab title="Python"> Given an `AsyncSecureClient`, estimate the price and place the market order. The synchronous `SecureClient` provides the same methods.

<Tab title="API"> Market orders reuse the construction and signing flow from [Place a Limit Order](#place-a-limit-order). Start from the current order book, calculate market-order amounts, then build and sign the same Exchange order with those values. The steps below call out what changes when the order should execute against current liquidity:

A market BUY's amount is the pre-fee USD notional. Applicable [platform fees](/market-data/market-details#trading-fees) and [builder taker fees](/programs/builders/fees) are charged on top. Set an all-in spending limit when the complete cost must remain within a fixed budget.

<Tabs> <Tab title="TypeScript"> Set `maxSpend` to the most you want to spend, including fees:

<Tab title="Python"> Set `max_spend` to the most you want to spend, including fees:

<Tab title="API"> Before signing, reduce `makerAmount` so the order notional plus applicable platform and builder taker fees does not exceed the intended limit. Then use the fee-adjusted value when calculating the market-order amounts above. </Tab> </Tabs>

A market order uses one of two execution types, depending on whether a partial fill is acceptable:

| Type                | Behavior                                                                              | | ------------------- | ------------------------------------------------------------------------------------- | | Fill and Kill (FAK) | Fills against the available liquidity immediately and cancels any unfilled remainder. | | Fill or Kill (FOK)  | Fills the entire order immediately or does not fill any of it.                        |

<Tabs> <Tab title="TypeScript"> Set `orderType` when calling `placeMarketOrder()` on a `SecureClient`. Fill and Kill is the default.

<Tab title="Python"> Set `order*type` when calling `place*market_order()` on an `AsyncSecureClient`. Fill and Kill is the default, and the synchronous `SecureClient` provides the same method.

<Tab title="API"> `orderType` is not part of the signed EIP-712 order typed data. Set it to `FAK` or `FOK` alongside the signed order in the top-level `/order` body:

Create and sign an order without submitting it when you need to inspect it, store it temporarily, or include it in a later batch.

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, create the signed order locally, then post it when ready:

<Tab title="Python"> Given an `AsyncSecureClient`, create the signed order locally, then post it when ready. The synchronous `SecureClient` provides the same methods.

<Tab title="API"> The API is inherently two-step: signing happens locally and submission is a separate HTTP request. Build and sign the order as described in [Place a Limit Order](#place-a-limit-order), then keep the signed order until you are ready to submit it. </Tab> </Tabs>

Submit several signed orders in one request. This is useful for placing a ladder of quotes across multiple price levels when market making.

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, create each signed order, then pass them together to `postOrders()`:

<Tab title="Python"> Given an `AsyncSecureClient`, create each signed order, then pass them together to `post_orders()`. The synchronous `SecureClient` provides the same methods.

<Tab title="API"> Send an array of 1 to 15 signed-order entries to `/orders`:

As part of the [Builder Program](/programs/builders/overview), attach your builder code to orders so matched trades are credited to your builder profile. The code is a 32-byte hex string that identifies your profile.

In the builder account, open polymarket.com → Settings → Builders and copy the **Builder Code** from your profile:

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/1lJ*npwaE*MShiVL/images/builder-code-tutorial.png?fit=max&auto=format&n=1lJ*npwaE*MShiVL&q=85&s=6648f4bfed0dd365fc1ad40664371032" alt="Open Settings, select Builders, and copy the Builder Code" width="1512" height="1040" data-path="images/builder-code-tutorial.png" /> </Frame>

Include the builder code in every order you want attributed to your integration. Because it is part of the signed order, add it before signing.

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, pass the code as `builderCode` when placing the order:

<Tab title="Python"> Given an `AsyncSecureClient` (or `SecureClient` for synchronous code), pass the code as `builder_code` when placing the order:

<Tab title="API"> Set the `builder` field of the order struct to your builder code before signing, in place of its 32-byte zero default. The code becomes part of the signed order and attributes any resulting trades to your builder profile.

After an attributed order matches, query builder trades using your builder code to confirm that the trade was credited to your profile. Orders that have not matched do not appear in builder trade results.

<Tabs> <Tab title="TypeScript"> Use `listBuilderTrades` with a `PublicClient` or `SecureClient`, then fetch the first page of matching trades:

<Tab title="Python"> Use `list*builder*trades` with an `AsyncPublicClient` or `AsyncSecureClient`, then fetch the first page of matching trades. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Builder trades are a public read and do not require authentication headers:

You can also monitor credited volume on the [Builder Leaderboard](https://builders.polymarket.com). Allow up to 24 hours for matched volume to appear there.

**Examples:**

Example 1 (text):
```text
    const yesTokenId = market.outcomes.yes.tokenId!;
    const noTokenId = market.outcomes.no.tokenId!;
```

Example 2 (text):
```text
    if market.outcomes.yes.token_id is None or market.outcomes.no.token_id is None:
        raise RuntimeError("Market token IDs not found")

    yes_token_id = market.outcomes.yes.token_id
    no_token_id = market.outcomes.no.token_id
```

Example 3 (text):
```text
    {
      "clobTokenIds": "[\"<yes_token_id>\", \"<no_token_id>\"]"
    }
```

Example 4 (text):
```text
Parse the array, then select the outcome you want to trade:

```bash theme={null}
TOKEN_ID="<yes_token_id>"
```
```

---

## Withdraw

**URL:** https://docs.polymarket.com/trading/bridge/withdraw.md

**Contents:**
- How It Works
- Create Withdrawal Addresses
  - Address Types
- Withdrawal Flow
- Next Steps

Withdraw pUSD from your Polymarket wallet to any supported chain and token. Funds are automatically bridged and swapped to your desired token on the destination chain.

<Warning> Do not pre-generate withdrawal addresses. Only generate them when you are ready to execute the withdrawal. Each address is configured for a specific destination. </Warning>

<Warning> When withdrawing, pUSD is unwrapped to USDC via the Collateral Offramp and swapped through the [Uniswap v3 pool](https://polygonscan.com/address/0xd36ec33c8bed5a9f7b6630855f1533455b98a418) for USDC (native). The UI enforces less than 10bp difference in output amount. At times, this pool may be exhausted. If you are having withdraw issues, try breaking your withdraw into smaller amounts or waiting for the pool to be rebalanced. Alternatively, you can withdraw pUSD directly, which does not require Uniswap liquidity — just be aware that some exchanges no longer accept pUSD deposits directly. </Warning>

<Tip> For very large withdrawals (over \$50,000), consider breaking the withdrawal into smaller amounts or using a third-party bridge to minimize slippage. </Tip>

Generate bridge addresses configured for your withdrawal destination. See [Create withdrawal addresses](/api-reference/bridge/create-withdrawal-addresses) for the full request and response schemas.

<Tip> **Builders: attach your code.** If you route user funds through this endpoint, pass your builder code via the optional `X-Builder-Code` header (bytes32 hex; `0x` + 64 hex chars). It lets our bridge provider attribute traffic to your app, so stuck or delayed transfers can be traced and prioritized. The header is optional. Requests without it still succeed but return a `missing*builder*code` warning, and a malformed code returns `400`. Get your code at [Settings → Builder](https://polymarket.com/settings?tab=builder). </Tip>

Tell the bridge where you're sending funds, including the destination chain, the destination token, and the recipient wallet, and it hands back one address per address type.

Your Polymarket wallet lives on Polygon, so you always send pUSD to the `evm` address. The response also carries bridge addresses for the other chain families because withdrawals and deposits share the same response format. Ignore those addresses when withdrawing.

| Address | Use For                                                  | | ------- | -------------------------------------------------------- | | `evm`   | Ethereum, Arbitrum, Base, Optimism, and other EVM chains | | `svm`   | Solana                                                   | | `btc`   | Bitcoin                                                  | | `tron`  | Tron                                                     |

Withdrawals are **instant** and **free** — Polymarket does not charge withdrawal fees.

<Steps> <Step title="Check Supported Assets"> Verify your destination chain and token are supported via `/supported-assets`. </Step>

<Step title="Get a Quote"> Preview fees and estimated output via `POST /quote`. </Step>

<Step title="Create Withdrawal Addresses"> Call `POST /withdraw` with your wallet address, destination chain, token, and recipient. </Step>

<Step title="Send pUSD"> Transfer pUSD from your Polymarket wallet to the appropriate bridge address. </Step>

<Step title="Track Status">Monitor progress using `/status/{address}`.</Step> </Steps>

<CardGroup cols={2}> <Card title="Get a Quote" icon="calculator" href="/trading/bridge/quote"> Preview fees and estimated output before withdrawing. </Card>

<Card title="Check Status" icon="clock" href="/trading/bridge/status"> Track your withdrawal progress. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
curl -X POST https://bridge.polymarket.com/withdraw \
  -H "Content-Type: application/json" \
  -H "X-Builder-Code: <builder_code>" \
  -d '{
    "address": "0x9156dd10bea4c8d7e2d591b633d1694b1d764756",
    "toChainId": "1",
    "toTokenAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "recipientAddr": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
  }'
```

Example 2 (text):
```text
{
  "address": {
    "evm": "0x23566f8b2E82aDfCf01846E54899d110e97AC053",
    "svm": "CrvTBvzryYxBHbWu2TiQpcqD5M7Le7iBKzVmEj3f36Jb",
    "btc": "bc1q8eau83qffxcj8ht4hsjdza3lha9r3egfqysj3g"
  },
  "note": "Send funds to these addresses to bridge to your destination chain and token."
}
```

---

## Matching Engine Restarts

**URL:** https://docs.polymarket.com/trading/matching-engine.md

**Contents:**
- Announcements
- Handle Matching Engine Restarts
  - Recommended Retry Strategy
  - Retry Order Placement
- Handle Restricted Trading Modes
  - Handle Request-Level Restrictions
  - Handle Batch Post-Only Rejections
- Best Practices

The Polymarket matching engine periodically restarts for maintenance and upgrades. Prepare your order workflow to pause safely, honor server-provided delays, and resume under the temporary post-only rules that follow a restart.

Matching engine changes — planned restarts, updates, and maintenance windows — are announced **before they happen** in these channels:

<CardGroup cols={2}> <Card title="Telegram" icon="telegram" href="https://t.me/polytradingapis"> Join the Polymarket Trading APIs channel for real-time announcements. </Card>

<Card title="Discord" icon="discord" href="https://discord.com/channels/710897173927297116/1473553279421255803"> Join the #trading-api-announcements channel in the Polymarket Discord. </Card> </CardGroup>

Announcements typically include **what's changing**, the **scheduled time**, and the **expected downtime window**. The goal is about two days' notice when possible.

During a restart, order-related actions reject new work temporarily. After the engine returns, it enters post-only mode for two minutes: cancels remain available, but new orders must be eligible maker orders submitted as post-only.

Your integration controls whether and when to retry. Use a delay supplied by the service when one is available; otherwise, fall back to exponential backoff.

<Steps> <Step title="Detect the Restart"> Treat the restart signal as a temporary condition. Do not retry unrelated request failures under the same policy. </Step>

<Step title="Wait Before Retrying"> Honor the server-provided delay when present. Otherwise, start with a one-to-two-second delay and increase it after each failed attempt. </Step>

<Step title="Resume in Post-Only Mode"> Once restart rejections stop, continue canceling as needed and submit only eligible maker orders as post-only for the next two minutes. </Step> </Steps>

Retry an eligible post-only limit order only when the rejection identifies a matching engine restart:

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, catch `RequestRejectedError` and check its `restriction` field. The SDK does not retry automatically.

<Tab title="Python"> Given an `AsyncSecureClient`, catch `RequestRejectedError` and check its `restriction` field. The synchronous `SecureClient` raises the same error, and neither client retries automatically.

<Tab title="API"> An order-related request returns HTTP `425` while the matching engine is restarting. Honor `Retry-After` when the response includes it; otherwise, apply bounded exponential backoff before resubmitting the signed request.

Restricted modes change which new orders are accepted. Cancels remain available unless trading is fully disabled. A cancel-only restriction blocks all new orders; a post-only restriction allows eligible maker orders submitted as post-only.

Pause new submissions when trading is unavailable. Switch to eligible post-only orders only when the rejection identifies post-only mode:

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, handle rejections from `placeLimitOrder()`:

<Tab title="Python"> Given an `AsyncSecureClient`, handle rejections from `place*limit*order()`. The synchronous `SecureClient` raises the same error.

<Tab title="API"> Inspect the response when an order submission is rejected:

A batch can be accepted at the request level while individual non-post-only orders are rejected. Check every result before treating the batch as successful:

<Tabs> <Tab title="TypeScript"> `postOrders()` returns an `OrderResponse` for each submitted order. Compare rejected results with `OrderResponseErrorCode.POST*ONLY*MODE`.

<Tab title="Python"> `post*orders()` returns an `OrderResponse` for each submitted order. The `code` on a post-only rejection is `"post*only_mode"`.

<Tab title="API"> `POST /orders` returns per-order errors in its successful response array:

Do not retry the same non-post-only order unchanged. Pause new submissions in cancel-only mode, wait for an indicated delay when appropriate, or submit an eligible maker order as post-only.

**Examples:**

Example 1 (javascript):
```javascript
Don't have the TypeScript SDK installed? Start with the [TypeScript SDK
guide](/getting-started/typescript), then come back.

```typescript TypeScript theme={null} theme={null}
import {
  OrderSide,
  RequestRejectedError,
  TradingRestriction,
} from "@polymarket/client";

async function placeWithRestartRetry() {
  const MAX_RETRIES = 10;
  let fallbackDelayMs = 1000;

  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    try {
      return await client.placeLimitOrder({
        tokenId: yesTokenId,
        side: OrderSide.BUY,
        price: "0.52",
        size: "10",
        postOnly: true,
      });
    } catch (error) {
      if (
        !(error instanceof RequestRejectedError) ||
        error.restriction !== TradingRestriction.RESTARTING
      ) {
        throw error;
      }

      const delayMs =
        error.retryAfter === undefined
          ? fallbackDelayMs
          : error.retryAfter * 1000;

      await new Promise((resolve) => setTimeout(resolve, delayMs));

      if (error.retryAfter === undefined) {
        fallbackDelayMs = Math.min(fallbackDelayMs * 2, 30000);
      }
    }
  }

  throw new Error("Engine restart exceeded maximum retry attempts");
}

const response = await placeWithRestartRetry();
// response: OrderResponse
```
```

Example 2 (python):
```python
Don't have the Python SDK installed? Start with the [Python SDK
guide](/getting-started/python), then come back.

```python Python theme={null} theme={null}
import asyncio

from polymarket import RequestRejectedError


async def place_with_restart_retry():
    max_retries = 10
    fallback_delay = 1

    for _ in range(max_retries):
        try:
            return await client.place_limit_order(
                token_id=yes_token_id,
                side="BUY",
                price="0.52",
                size="10",
                post_only=True,
            )
        except RequestRejectedError as error:
            if error.restriction != "restarting":
                raise

            delay = (
                fallback_delay
                if error.retry_after is None
                else error.retry_after
            )
            await asyncio.sleep(delay)

            if error.retry_after is None:
                fallback_delay = min(fallback_delay * 2, 30)

    raise RuntimeError("Engine restart exceeded maximum retry attempts")


response = await place_with_restart_retry()
# response: OrderResponse
```
```

Example 3 (text):
```text
    HTTP/1.1 425 Too Early
    Retry-After: 1
```

Example 4 (text):
```text
    import {
      OrderSide,
      RequestRejectedError,
      TradingRestriction,
    } from "@polymarket/client";

    try {
      const response = await client.placeLimitOrder({
        tokenId: yesTokenId,
        side: OrderSide.BUY,
        price: "0.52",
        size: "10",
      });
      // response: OrderResponse
    } catch (error) {
      if (!(error instanceof RequestRejectedError)) {
        throw error;
      }

      if (error.restriction === TradingRestriction.POST_ONLY) {
        if (error.retryAfter !== undefined) {
          const delayMs = error.retryAfter * 1000;
          await new Promise((resolve) => setTimeout(resolve, delayMs));
        }
        // Submit only eligible maker orders with postOnly: true.
      } else {
        throw error;
      }
    }
```

---

## Transaction Status

**URL:** https://docs.polymarket.com/trading/bridge/status.md

**Contents:**
- Check Status
- Transaction Statuses
- Read Older Transactions
  - Query Parameters
- Next Steps

After sending assets to a bridge address, use the status endpoint to follow the transfer until the funds land. The same request covers deposits and withdrawals: you always query the bridge address that received the funds, not the wallet on either end.

Request the transactions for a bridge address.

<Note> Use the bridge address from the `/deposit` or `/withdraw` response (EVM, SVM, Tron, or BTC), not your Polymarket wallet address. </Note>

| Field                | Description                                                                               | | -------------------- | ----------------------------------------------------------------------------------------- | | `transactions`       | One page of transactions, newest first                                                    | | `nextCursor`         | Token for the next page, or `null` when there is nothing older to read                    | | `fromChainId`        | Source chain ID                                                                           | | `fromTokenAddress`   | Token sent                                                                                | | `fromAmountBaseUnit` | Amount in base units                                                                      | | `toChainId`          | Destination chain ID (137 for Polygon on deposits)                                        | | `toTokenAddress`     | Token received                                                                            | | `status`             | Current status (see table below)                                                          | | `txHash`             | Destination transaction hash (only when `COMPLETED`)                                      | | `createdTimeMs`      | Unix timestamp in milliseconds (only present once the transaction has started processing) |

If no transfers have been detected at the address yet, `transactions` comes back empty.

Each transfer progresses through these statuses:

| Status                | Terminal | Description                                        | | --------------------- | -------- | -------------------------------------------------- | | `DEPOSIT*DETECTED`    | No       | Funds detected on source chain, not yet processing | | `PROCESSING`          | No       | Transaction is being routed and swapped            | | `ORIGIN*TX_CONFIRMED` | No       | Source chain transaction confirmed                 | | `SUBMITTED`           | No       | Submitted to the destination chain                 | | `COMPLETED`           | Yes      | Funds arrived — transaction successful             | | `FAILED`              | Yes      | Transaction encountered an error                   |

<Note> If a bridge transaction fails, remains stuck, or funds are held due to a compliance check, direct users to [our Bridge API provider's support](https://intercom.help/funxyz/en/articles/10732578-contact-us) to resolve the issue. </Note>

<Tip> Transfers typically complete within a few minutes, but may take longer depending on network conditions. Poll every 10-30 seconds until `COMPLETED` or `FAILED`. </Tip>

Transactions come back newest first, so a request without a cursor always returns the most recent activity. That first page is all you need to track a transfer you just initiated.

| Parameter  | Type    | Default | Description                                                                                                        | | ---------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------ | | `limit`    | integer | `50`    | Transactions per page, from `1` to `100`                                                                           | | `cursor`   | string  | None    | Continuation token from the previous response's `nextCursor`. Omit it to request the first page.                   | | `paginate` | string  | None    | Compatibility parameter for existing integrations. Send `paginate=true` or omit it; pagination applies either way. |

To read further back, replay the cursor exactly as you received it and repeat until `nextCursor` is `null`:

Cursors are opaque. Never decode, edit, or build one yourself, never reuse a cursor against a different address, and always URL-encode it — a cursor can contain `+`, `/`, or `=`. A rejected cursor returns `400 {"error": "invalid request"}`; restart the walk without one.

<Warning> Stop only when `nextCursor` is `null`. A page can be empty, or shorter than the `limit` you asked for, and still be followed by more pages. </Warning>

<CardGroup cols={2}> <Card title="Create Deposit" icon="arrow-right-to-bracket" href="/trading/bridge/deposit"> Generate bridge addresses for your wallet. </Card>

<Card title="Supported Assets" icon="coins" href="/trading/bridge/supported-assets"> Check supported chains and minimum amounts. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
curl --get https://bridge.polymarket.com/status/0x23566f8b2E82aDfCf01846E54899d110e97AC053 \
  --data-urlencode 'limit=50'
```

Example 2 (text):
```text
{
  "transactions": [
    {
      "fromChainId": "1",
      "fromTokenAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
      "fromAmountBaseUnit": "1000000000",
      "toChainId": "137",
      "toTokenAddress": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
      "status": "COMPLETED",
      "txHash": "0xabc123…",
      "createdTimeMs": 1697875200000
    }
  ],
  "nextCursor": "eyJsYXN0SWQiOiI0MiJ9"
}
```

Example 3 (text):
```text
curl --get https://bridge.polymarket.com/status/0x23566f8b2E82aDfCf01846E54899d110e97AC053 \
  --data-urlencode 'limit=100' \
  --data-urlencode 'cursor=eyJsYXN0SWQiOiI0MiJ9'
```

---

## Session Keys

**URL:** https://docs.polymarket.com/trading/session-keys.md

**Contents:**
- Authorize a Session Key
- Place an Order
- Fetch Session Keys
- Revoke a Session Key
- Session Key Considerations

<Note> Session Keys are in beta. We welcome feedback as you integrate them. </Note>

A Session Key is a separate signer that a Deposit Wallet Owner authorizes to trade for a Deposit Wallet. It lets an integration perform routine trading without using the owner's key. A Session Key cannot withdraw funds from the Deposit Wallet.

<Note> Session Keys work only with Deposit Wallets. A dedicated migration flow from Safe Wallets and Proxy Wallets is planned. </Note>

A Session Key can be scoped to trade on specific supported venues or all venues:

central limit order book.

The Deposit Wallet Owner authorizes a session signer address with an expiration of 180 days and scoped permissions.

<Warning> Session Keys are Externally Owned Accounts (EOAs). Keep their private keys secret to prevent unauthorized trading on behalf of your Deposit Wallet. </Warning>

Authorizing a Session Key requires a Builder API key. See [Create New Accounts](/trading/wallets-auth#create-new-accounts) to generate one.

<Warning> During the initial rollout, contact [builder@polymarket.com](mailto:builder@polymarket.com) to authorize your Builder API key for session-key management. If you are already a member of the Builder Program Telegram group, you can also ask there. </Warning>

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Generate a Session Key"> First, generate a fresh EVM keypair for the Session Key.

<Tab title="Python"> <Steps> <Step title="Generate a Session Key"> First, generate a fresh EVM keypair for the Session Key.

<Tab title="API"> Authorize the session signer through the Relayer, then confirm that it is available for trading.

This section shows how to place an order using a Session Key. See [Place Orders](/trading/place-orders) for the complete order workflow.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Create the Session Client"> First, create a `SecureClient` for the Deposit Wallet with the session signer.

<Tab title="Python"> <Steps> <Step title="Create the Session Client"> First, create an `AsyncSecureClient` for the Deposit Wallet with the Session Key.

<Tab title="API"> Authenticate with the CLOB using the Session Key, then place an order. See [API Authentication](/getting-started/api#authentication) for the complete signing flow.

List the active Session Keys for a Deposit Wallet to see which signers can currently act on its behalf.

<Tabs> <Tab title="TypeScript"> Call `fetchSessionKeys()` on the Deposit Wallet Owner's `SecureClient`:

<Tab title="Python"> Call `fetch*session*keys()` on the Deposit Wallet Owner's `AsyncSecureClient`. The synchronous `SecureClient` provides the same method without `await`.

<Tab title="API"> Authenticate the Deposit Wallet Owner with the CLOB, then fetch the Deposit Wallet's active Session Keys. See [API Authentication](/getting-started/api#authentication) for the complete signing flow.

Revoke a Session Key when an integration no longer needs access or its private key may have been exposed. Revocation prevents further trading by that key and cancels its open orders without affecting orders placed by other Session Keys.

<Tabs> <Tab title="TypeScript"> Call `revokeSessionKey()` on the Deposit Wallet Owner's `SecureClient` with the Session Key's public address:

<Tab title="Python"> Call `revoke*session*key()` on the Deposit Wallet Owner's `AsyncSecureClient` with the Session Key's public address. The synchronous `SecureClient` provides the same method without `await`.

<Tab title="API"> Authorize the revocation as the Deposit Wallet Owner, then submit it with Builder authentication.

Configurable shorter Session Key expirations are not currently supported. To end access before 180 days, [revoke the Session Key](#revoke-a-session-key).

If you are adding Session Key support to an existing integration, keep these access boundaries in mind:

[notifications](/trading/wallet-activity#notifications) and [real-time order and trade updates](/trading/realtime-order-updates#user-stream) generated by its own activity.

order](/trading/manage-orders#fetch-an-order) or [list open orders](/trading/manage-orders#list-open-orders) only for orders it submitted. A Deposit Wallet Owner cannot fetch orders submitted by its authorized Session Keys.

trades](/trading/manage-orders#list-account-trades) only for trades associated with its own orders.

**Examples:**

Example 1 (text):
```text
        import { generatePrivateKey, privateKeyToAccount } from "viem/accounts";

        const sessionKeyPrivateKey = generatePrivateKey();
        const { address: sessionKeyAddress } =
          privateKeyToAccount(sessionKeyPrivateKey);
```

Example 2 (text):
```text
    Store **your private key** in a secrets manager or another secure key
    store.
  </Step>

  <Step title="Create the Deposit Wallet Owner Client">
    Then, create a `SecureClient` with the Deposit Wallet Owner's private key
    and Builder API credentials.

    ```ts theme={null}
    import { createSecureClient } from "@polymarket/client";
    import { builderApiKey } from "@polymarket/client/node";
    import { privateKey } from "@polymarket/client/viem";

    const secureClient = await createSecureClient({
      signer: privateKey(process.env.POLYMARKET_PRIVATE_KEY),
      wallet: process.env.POLYMARKET_DEPOSIT_WALLET!,
      apiKey: builderApiKey({
        key: process.env.POLYMARKET_BUILDER_API_KEY!,
        secret: process.env.POLYMARKET_BUILDER_SECRET!,
        passphrase: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
      }),
    });
    ```
  </Step>

  <Step title="Authorize the Session Key">
    Finally, call `authorizeSessionKey()` to authorize your Session Key.

    ```ts theme={null}
    const authorization = await secureClient.authorizeSessionKey({
      address: sessionKeyAddress,
    });

    // authorization: AuthorizeSessionKeyResult
    ```

    You can also authorize only the desired trading venues with the `scopes`
    parameter:

    ```ts theme={null}
    import { SessionKeyKnownScope } from "@polymarket/client";

    const scopedAuthorization = await secureClient.authorizeSessionKey({
      address: sessionKeyAddress,
      scopes: [SessionKeyKnownScope.CLOB, SessionKeyKnownScope.COMBOSRFQ],
    });

    // scopedAuthorization: AuthorizeSessionKeyResult
    ```
  </Step>
</Steps>
```

Example 3 (text):
```text
        from eth_account import Account

        session_key = Account.create()
        session_key_private_key = "0x" + session_key.key.hex().removeprefix("0x")
        session_key_address = session_key.address
```

Example 4 (text):
```text
    Store **your private key** in a secrets manager or another secure key
    store.
  </Step>

  <Step title="Create the Deposit Wallet Owner Client">
    Then, create an `AsyncSecureClient` with the Deposit Wallet Owner's
    private key and Builder API credentials.

    ```python theme={null}
    import os

    from polymarket import AsyncSecureClient, BuilderApiKey

    secure_client = await AsyncSecureClient.create(
        private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
        wallet=os.environ["POLYMARKET_DEPOSIT_WALLET"],
        api_key=BuilderApiKey(
            key=os.environ["POLYMARKET_BUILDER_API_KEY"],
            secret=os.environ["POLYMARKET_BUILDER_SECRET"],
            passphrase=os.environ["POLYMARKET_BUILDER_PASSPHRASE"],
        ),
    )
    ```
  </Step>

  <Step title="Authorize the Session Key">
    Finally, call `authorize_session_key()` to authorize your Session Key.

    ```python theme={null}
    authorization = await secure_client.authorize_session_key(
        address=session_key_address,
    )

    # authorization: AuthorizeSessionKeyResult
    ```

    You can also authorize only the desired trading venues with the `scopes`
    parameter:

    ```python theme={null}
    from polymarket import SessionKeyKnownScope

    scoped_authorization = await secure_client.authorize_session_key(
        address=session_key_address,
        scopes=(
            SessionKeyKnownScope.CLOB,
            SessionKeyKnownScope.COMBOSRFQ,
        ),
    )

    # scoped_authorization: AuthorizeSessionKeyResult
    ```
  </Step>
</Steps>
```

---

## Market Making

**URL:** https://docs.polymarket.com/trading/market-making.md

**Contents:**
- Set Up for Market Making
- Quote and Manage Orders
  - Build Two-Sided Quotes
  - Choose Order Types
  - Submit and Maintain Orders
- Manage Inventory
  - Inventory Strategies
- Best Practices
  - Quote Management
  - Latency

A market maker (MM) provides liquidity by continuously posting bids and asks. By quoting both sides of a market, market makers make it easier for other traders to execute while seeking to earn the spread in exchange for the risks they take.

On Polymarket, market makers deepen order books, tighten spreads, support price discovery, and absorb trading flow as market conditions change.

<Note> Building a product that routes orders for its users? See the [Builder Program](/programs/builders/overview). This page is for traders providing liquidity from their own account. </Note>

Complete these account-level requirements before quoting a market.

<Steps> <Step title="Connect Your Account"> Create or connect the wallet that will hold funds, positions, and orders, then authenticate the integration. See [Wallets and Authentication](/trading/wallets-auth) for the supported workflows. </Step>

<Step title="Fund the Wallet"> The wallet needs pUSD on Polygon before it can trade. To deposit another supported asset or transfer funds from another network, use the [Bridge](/trading/bridge/deposit). </Step>

<Step title="Set Up Trading Approvals"> Authorize the contracts required to trade outcome tokens and manage positions. See [Set Up Trading Approvals](/trading/wallets-auth#set-up-trading-approvals). </Step> </Steps>

Market makers maintain bids and asks around their fair value so other traders can execute in either direction. The midpoint describes the current book, but the quoting strategy must determine whether it represents fair value and how much risk to take around it.

In a binary market, complementary outcomes provide another way to express the two sides. Buying NO at `0.48`, for example, is economically equivalent to selling YES at `0.52`.

Before submitting a quote, confirm that the market is accepting orders and validate its current minimum price increment and minimum order size. See [Market Details](/market-data/market-details) for these constraints.

Choose the order type according to what the strategy needs to accomplish:

| Type                     | Behavior                                                         | When to use                                             | | ------------------------ | ---------------------------------------------------------------- | ------------------------------------------------------- | | Good-Til-Cancelled (GTC) | Rests on the book until filled or canceled                       | Default for passive quotes                              | | Good-Til-Date (GTD)      | Rests on the book until filled, canceled, or expired             | Expire a passive quote at a known time                  | | Fill-or-Kill (FOK)       | Fills the entire amount immediately or cancels                   | Rebalance immediately when a partial fill is not useful | | Fill-and-Kill (FAK)      | Fills the available amount immediately and cancels the remainder | Rebalance immediately while allowing a partial fill     |

GTC and GTD are the primary order types for passive market making. Add the [post-only option](/trading/place-orders#post-only-orders) when an order must add liquidity rather than execute immediately. FAK and FOK are the execution types used by market orders for immediate rebalancing.

Submit related price levels as a [batch](/trading/place-orders#post-a-batch-of-orders) to reduce submission latency. Each order is evaluated independently, so check every result rather than treating the batch as a single success or failure. See [Place Orders](/trading/place-orders) for the complete order workflows.

Once submitted, the quotes become orders resting on the book. Orders cannot be edited in place, so changing a quote means canceling the existing order and submitting a replacement:

data](/market-data/realtime-data#market-stream).

Updates](/trading/realtime-order-updates).

trades](/trading/manage-orders) before resuming the strategy.

Inventory is the outcome-token exposure accumulated through trading. Every fill changes that exposure and the pUSD or tokens available for new orders, so inventory must be part of every pricing and sizing decision.

Buy orders use available pUSD, while sell orders require the corresponding outcome tokens. Splitting pUSD creates a complete set of outcome tokens; merging a complete set returns pUSD; and redeeming a winning position releases its value after resolution. See [Manage Positions](/trading/positions/manage) for these workflows.

| Phase            | Guidance                                                                                                                                                                        | | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | Before quoting   | Estimate the intended order sizes and prepare enough pUSD and outcome tokens to support them. Confirm that the required trading approvals are in place.                         | | During trading   | Track exposure by market and outcome. Skew quote prices or sizes to reduce an imbalance, split additional pUSD when tokens run low, and merge complete sets to release capital. | | When exiting     | Cancel the market's remaining orders, merge any complete sets that are no longer needed, and retain or reduce the remaining directional exposure deliberately.                  | | After resolution | Confirm that the market has resolved, redeem winning positions, and return the released capital to the strategy.                                                                |

Multi-outcome events use [negative-risk markets](/concepts/negative-risk), which change how complete sets are created and merged. Account for the market type when planning inventory operations.

Use these practices to keep quotes current and limit avoidable execution risk.

request](/trading/place-orders#post-a-batch-of-orders).

updates](/market-data/realtime-data#market-stream) instead of polling.

the available inventory.

orders](/trading/manage-orders#cancel-all-orders) when errors or position limits require the strategy to stop.

updates](/trading/realtime-order-updates) to track executions.

In addition to the spread captured through executions, qualifying market-making activity may earn incentives through two separate programs.

<CardGroup cols={2}> <Card title="Liquidity Rewards" icon="chart-line" href="/programs/liquidity-rewards"> Earn rewards by maintaining qualifying resting liquidity in incentivized markets. </Card>

<Card title="Maker Rebates" icon="receipt" href="/programs/maker-rebates"> Earn rebates when maker liquidity executes in eligible fee-enabled markets. </Card> </CardGroup>

Eligibility, calculations, and payouts differ between the programs. See each program page for its current terms.

For market maker onboarding and support, contact [support@polymarket.com](mailto:support@polymarket.com).

---

## Requesters

**URL:** https://docs.polymarket.com/trading/combos/requesters.md

**Contents:**
- Request and Execute a Quote
- Handle Errors

Use the Requester API to request executable Combo quotes, accept a winning quote, and track the trade through onchain execution. This guide walks through the complete workflow.

<Warning> Keep the CLOB API secret and passphrase on trusted infrastructure. Never expose them in a browser or other untrusted client. </Warning>

<Tabs> <Tab title="API"> The production gateway is `https://combos-rfq-gateway-requester-api.polymarket.com`, with base path `/v1/requester/rfq`.

<Tab title="TypeScript"> <Info> TypeScript SDK support is coming soon. Use the API workflow in the API tab for now. </Info> </Tab>

<Tab title="Python"> <Info> Python SDK support is coming soon. Use the API workflow in the API tab for now. </Info> </Tab> </Tabs>

Validation and dependency failures use non-`200` HTTP statuses with stable string codes:

| HTTP status | Common codes                                                                                                                                                            | | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | `400`       | `INVALID*JSON`, `INVALID*RFQ`, `INVALID*IDENTITY`, `INVALID*ACCEPTANCE`, `INVALID*SIGNATURE`, `UNSUPPORTED*REQUESTER*SIGNATURE*TYPE`, `BUILDER*ATTRIBUTION*NOT*ALLOWED` | | `401`       | `UNAUTHENTICATED`                                                                                                                                                       | | `403`       | `ADDRESS*MISMATCH`, `REQUEST*FAILED`                                                                                                                                    | | `404`       | `UNKNOWN*RFQ`                                                                                                                                                           | | `409`       | `REQUEST*FAILED`, `QUOTE*MISMATCH`, `EXPIRED*RFQ`, `INVALID*RFQ*STATE`                                                                                                  | | `429`       | `RATE*LIMITED`                                                                                                                                                          | | `503`       | `SERVICE*UNAVAILABLE`, `PRE*EXECUTION*BALANCE*RESERVATION*FAILED`, `TRADE*SUBMISSION_FAILED`                                                                            |

Treat codes as strings so integrations remain compatible with new codes. HTTP `200` can still contain a failed business outcome; always inspect both `status` and the nested `error` object.

**Examples:**

Example 1 (python):
```python
<Steps>
  <Step title="Prepare the Trading Account">
    Create a Polymarket account, obtain its [CLOB API
    credentials](/getting-started/api#authentication), and fund the account wallet.
    Set up the wallet and trading approvals by following [Wallets and
    Authentication](/trading/wallets-auth).

    Resolve the CLOB credential address, order signer, order maker, and signature
    type for the account's wallet:

    | Wallet type    | `signature_type` | `POLY_ADDRESS`                                  | `signer_address`       | `maker_address`        |
    | -------------- | ---------------- | ----------------------------------------------- | ---------------------- | ---------------------- |
    | Deposit Wallet | `3` POLY\_1271   | Account or session signer with CLOB credentials | Deposit Wallet address | Deposit Wallet address |
    | Proxy Wallet   | `1` Proxy        | Account signer with CLOB credentials            | Account signer         | Proxy Wallet address   |
    | Safe Wallet    | `2` Safe         | Account signer with CLOB credentials            | Account signer         | Safe Wallet address    |
    | EOA            | `0` EOA          | Not supported                                   | Not supported          | Not supported          |

    Both requester gateways reject EOA accounts. The Requester API returns
    `UNSUPPORTED_REQUESTER_SIGNATURE_TYPE`; use a Deposit, Proxy, or Safe Wallet.
  </Step>

  <Step title="Sign Request Headers">
    Every request requires these CLOB L2 headers:

    * `POLY_ADDRESS`
    * `POLY_API_KEY`
    * `POLY_PASSPHRASE`
    * `POLY_TIMESTAMP`
    * `POLY_SIGNATURE`

    `POLY_ADDRESS` is the address associated with the CLOB API credentials. Use the
    wallet identity values resolved in the previous step for the request body and
    signed order.

    Compute `POLY_SIGNATURE` with HMAC-SHA256, using the base64-decoded CLOB secret
    as the key. Sign an uppercase method, a Unix timestamp in seconds, the full
    request path without the host or query string, and the exact serialized body
    sent on the wire. Omit the body for `GET` requests. Encode the digest as
    base64url with padding preserved.

    ```text theme={null}
    HMAC-SHA256(
      base64Decode(secret),
      timestamp + HTTP_METHOD + FULL_REQUEST_PATH + REQUEST_BODY
    )
    ```

    Generate a fresh timestamp and signature for every request, including each
    status poll.
  </Step>

  <Step title="Choose the Combo Legs">
    Fetch active Combo-enabled markets from the public catalog:

    ```bash theme={null}
    curl -G "https://combos-rfq-api.polymarket.com/v1/rfq/combo-markets" \
      --data-urlencode "limit=50"
    ```

    The response contains a `markets` array and an opaque `next_cursor`. Pass the
    cursor back as `cursor` to fetch the next page. For each market,
    `position_ids`, `outcomes`, and `outcome_prices` are aligned by array index:
    index `0` is YES and index `1` is NO.

    Choose 2–50 unique, mutually compatible outcome position IDs and pass them in
    `leg_position_ids`.
  </Step>

  <Step title="Create the RFQ">
    Choose the request direction and size:

    * A BUY sets the maximum collateral budget, including fees. Use
      `unit: "notional"`.
    * A SELL specifies the number of Combo shares to sell. Use `unit: "shares"`.

    `value_e6` is a string in 6-decimal base units, and `side` must currently be
    `"YES"`. The gateway holds the request until the quote competition finishes.
    The examples below use a Deposit Wallet. The API accepts at most 15 create
    requests per rolling minute for each `maker_address`; requests above that limit
    return HTTP `429` with `RATE_LIMITED`.

    <CodeGroup>
      ```http BUY theme={null}
      POST /v1/requester/rfq/requests
      Content-Type: application/json
      POLY_ADDRESS: <clob-credential-address>
      POLY_API_KEY: <clob-api-key>
      POLY_PASSPHRASE: <clob-passphrase>
      POLY_TIMESTAMP: <unix-seconds>
      POLY_SIGNATURE: <l2-signature>

      {
        "signer_address": "<deposit-wallet-address>",
        "maker_address": "<deposit-wallet-address>",
        "signature_type": 3,
        "leg_position_ids": ["<yes-position-id-1>", "<yes-position-id-2>"],
        "direction": "BUY",
        "side": "YES",
        "requested_size": {
          "unit": "notional",
          "value_e6": "1000000"
        }
      }
      ```

      ```http SELL theme={null}
      POST /v1/requester/rfq/requests
      Content-Type: application/json
      POLY_ADDRESS: <clob-credential-address>
      POLY_API_KEY: <clob-api-key>
      POLY_PASSPHRASE: <clob-passphrase>
      POLY_TIMESTAMP: <unix-seconds>
      POLY_SIGNATURE: <l2-signature>

      {
        "signer_address": "<deposit-wallet-address>",
        "maker_address": "<deposit-wallet-address>",
        "signature_type": 3,
        "leg_position_ids": ["<yes-position-id-1>", "<yes-position-id-2>"],
        "direction": "SELL",
        "side": "YES",
        "requested_size": {
          "unit": "shares",
          "value_e6": "1000000"
        }
      }
      ```
    </CodeGroup>

    An executable response includes the server-owned RFQ ID, winning quote, and
    acceptance deadline:

    <Accordion title="Create RFQ Response">
      ```json theme={null}
      {
        "rfq_id": "<rfq-id>",
        "status": "AWAITING_REQUESTER_ACCEPTANCE",
        "expires_at": 1773890763000,
        "request": {
          "rfq_id": "<rfq-id>",
          "maker_address": "<deposit-wallet-address>",
          "requestor_public_id": "<requester-public-id>",
          "leg_position_ids": ["<yes-position-id-1>", "<yes-position-id-2>"],
          "condition_id": "<combo-condition-id>",
          "yes_position_id": "<combo-yes-position-id>",
          "no_position_id": "<combo-no-position-id>",
          "direction": "BUY",
          "side": "YES",
          "requested_size": {
            "unit": "notional",
            "value_e6": "1000000"
          },
          "created_at": 1773890758000
        },
        "quote": {
          "quote_id": "<quote-id>",
          "blended_price_e6": "500000",
          "maker_amount_e6": "966191",
          "taker_amount_e6": "1932381",
          "total_required_e6": "1000000",
          "net_receive_e6": "1932381"
        }
      }
      ```
    </Accordion>

    `expires_at` and `request.created_at` are Unix timestamps in milliseconds. The
    acceptance window is five seconds from quote readiness. Sign and accept the
    order before `expires_at`. `total_required_e6` is the exact balance required:
    collateral including fees for BUY, or Combo shares for SELL. For BUY,
    `net_receive_e6` is the Combo shares received. For SELL, it is the exact
    collateral proceeds after fees.

    If no usable quote is available, the gateway returns HTTP `200` with a terminal
    business outcome:

    ```json theme={null}
    {
      "rfq_id": "<rfq-id>",
      "status": "FAILED",
      "error": {
        "code": "NO_QUOTES",
        "message": "no quotes"
      }
    }
    ```

    <Warning>
      A local create timeout or lost connection has an unknown outcome. The RFQ may
      have been created even if you never received its server-owned ID. This API has
      no idempotency key or lookup for that case, and retrying may create another
      RFQ.
    </Warning>
  </Step>

  <Step title="Build and Sign the Requester Order">
    Build an Exchange v3 order from the returned request and quote. Use Polygon
    chain ID `137` and Exchange v3 contract
    `0xe3333700cA9d93003F00f0F71f8515005F6c00Aa` for the EIP-712 domain.

    For both directions, copy `maker_amount_e6` to `makerAmount` and
    `taker_amount_e6` to `takerAmount`, and use the returned Combo YES position ID
    as `tokenId`. Set `side` to `0` for BUY or `1` for SELL.

    The `builder` field must be the zero bytes32 value. A non-zero value is rejected
    with `BUILDER_ATTRIBUTION_NOT_ALLOWED`. This gateway does not support Builder
    attribution. Approved builders that need orders attributed to their Builder
    code must authenticate and submit them through the [Builder Gateway
    workflow](/trading/combos/builders#request-and-execute-a-quote) instead.

    Use the same wallet identity selected when creating the RFQ. The wallet type
    determines which payload to sign and how to encode `signed_order.signature`:

    | Wallet type    | `signatureType` | Payload to sign            | Submitted signature            |
    | -------------- | --------------- | -------------------------- | ------------------------------ |
    | Deposit Wallet | `3`             | `depositWalletTypedData`   | ERC-7739-wrapped signature     |
    | Proxy Wallet   | `1`             | `exchangeV3OrderTypedData` | Standard 65-byte EVM signature |
    | Safe Wallet    | `2`             | `exchangeV3OrderTypedData` | Standard 65-byte EVM signature |

    For a Deposit Wallet, wrap the Exchange v3 order in the Deposit Wallet's
    `TypedDataSign` structure. Both `maker` and `signer` in `contents` are the
    Deposit Wallet address. The account or session signer signs this outer payload.

    ```json Deposit Wallet Typed Data theme={null}
    {
      "domain": {
        "name": "Polymarket CTF Exchange",
        "version": "3",
        "chainId": 137,
        "verifyingContract": "0xe3333700cA9d93003F00f0F71f8515005F6c00Aa"
      },
      "types": {
        "Order": [
          { "name": "salt", "type": "uint256" },
          { "name": "maker", "type": "address" },
          { "name": "signer", "type": "address" },
          { "name": "tokenId", "type": "uint256" },
          { "name": "makerAmount", "type": "uint256" },
          { "name": "takerAmount", "type": "uint256" },
          { "name": "side", "type": "uint8" },
          { "name": "signatureType", "type": "uint8" },
          { "name": "timestamp", "type": "uint256" },
          { "name": "metadata", "type": "bytes32" },
          { "name": "builder", "type": "bytes32" }
        ],
        "TypedDataSign": [
          { "name": "contents", "type": "Order" },
          { "name": "name", "type": "string" },
          { "name": "version", "type": "string" },
          { "name": "chainId", "type": "uint256" },
          { "name": "verifyingContract", "type": "address" },
          { "name": "salt", "type": "bytes32" }
        ]
      },
      "primaryType": "TypedDataSign",
      "message": {
        "contents": {
          "salt": "<salt>",
          "maker": "<deposit-wallet-address>",
          "signer": "<deposit-wallet-address>",
          "tokenId": "<combo-yes-position-id>",
          "makerAmount": "966191",
          "takerAmount": "1932381",
          "side": 0,
          "signatureType": 3,
          "timestamp": "<unix-seconds>",
          "metadata": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "builder": "0x0000000000000000000000000000000000000000000000000000000000000000"
        },
        "name": "DepositWallet",
        "version": "1",
        "chainId": 137,
        "verifyingContract": "<deposit-wallet-address>",
        "salt": "0x0000000000000000000000000000000000000000000000000000000000000000"
      }
    }
    ```

    For a Proxy or Safe Wallet, sign the Exchange v3 `Order` directly. Set `maker`
    to the Proxy or Safe Wallet address, `signer` to the account signer, and
    `signatureType` to `1` or `2`, respectively.

    ```json Proxy or Safe Wallet Typed Data theme={null}
    {
      "domain": {
        "name": "Polymarket CTF Exchange",
        "version": "3",
        "chainId": 137,
        "verifyingContract": "0xe3333700cA9d93003F00f0F71f8515005F6c00Aa"
      },
      "types": {
        "EIP712Domain": [
          { "name": "name", "type": "string" },
          { "name": "version", "type": "string" },
          { "name": "chainId", "type": "uint256" },
          { "name": "verifyingContract", "type": "address" }
        ],
        "Order": [
          { "name": "salt", "type": "uint256" },
          { "name": "maker", "type": "address" },
          { "name": "signer", "type": "address" },
          { "name": "tokenId", "type": "uint256" },
          { "name": "makerAmount", "type": "uint256" },
          { "name": "takerAmount", "type": "uint256" },
          { "name": "side", "type": "uint8" },
          { "name": "signatureType", "type": "uint8" },
          { "name": "timestamp", "type": "uint256" },
          { "name": "metadata", "type": "bytes32" },
          { "name": "builder", "type": "bytes32" }
        ]
      },
      "primaryType": "Order",
      "message": {
        "salt": "<salt>",
        "maker": "<proxy-or-safe-wallet-address>",
        "signer": "<account-signer-address>",
        "tokenId": "<combo-yes-position-id>",
        "makerAmount": "966191",
        "takerAmount": "1932381",
        "side": 0,
        "signatureType": 1,
        "timestamp": "<unix-seconds>",
        "metadata": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "builder": "0x0000000000000000000000000000000000000000000000000000000000000000"
      }
    }
    ```

    Sign the selected payload with the account or session signer. Deposit Wallets
    must wrap the raw signature for ERC-7739 validation; Proxy and Safe Wallets
    submit the signature returned by signing the Exchange `Order` directly.

    <CodeGroup>
      ```js Deposit Wallet theme={null}
      import { privateKeyToAccount } from "viem/accounts";

      const signer = privateKeyToAccount(process.env.SIGNER_PRIVATE_KEY);
      const innerSignature = await signer.signTypedData(depositWalletTypedData);
      const signature = wrapDepositWalletSignature(
        depositWalletTypedData,
        innerSignature,
      );
      ```

      ```js Proxy or Safe Wallet theme={null}
      import { privateKeyToAccount } from "viem/accounts";

      const signer = privateKeyToAccount(process.env.SIGNER_PRIVATE_KEY);
      const signature = await signer.signTypedData(exchangeV3OrderTypedData);
      ```

      ```js wrapDepositWalletSignature() theme={null}
      import { concatHex, encodeAbiParameters, keccak256, toHex } from "viem";

      const ORDER_TYPE =
        "Order(uint256 salt,address maker,address signer,uint256 tokenId,uint256 makerAmount,uint256 takerAmount,uint8 side,uint8 signatureType,uint256 timestamp,bytes32 metadata,bytes32 builder)";
      const EIP712_DOMAIN_TYPE =
        "EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)";

      function wrapDepositWalletSignature(typedData, innerSignature) {
        const order = typedData.message.contents;
        const exchangeDomain = typedData.domain;

        const appDomainSeparator = keccak256(
          encodeAbiParameters(
            [
              { type: "bytes32" },
              { type: "bytes32" },
              { type: "bytes32" },
              { type: "uint256" },
              { type: "address" },
            ],
            [
              keccak256(toHex(EIP712_DOMAIN_TYPE)),
              keccak256(toHex(exchangeDomain.name)),
              keccak256(toHex(exchangeDomain.version)),
              BigInt(exchangeDomain.chainId),
              exchangeDomain.verifyingContract,
            ],
          ),
        );
        const contentsHash = keccak256(
          encodeAbiParameters(
            [
              { type: "bytes32" },
              { type: "uint256" },
              { type: "address" },
              { type: "address" },
              { type: "uint256" },
              { type: "uint256" },
              { type: "uint256" },
              { type: "uint8" },
              { type: "uint8" },
              { type: "uint256" },
              { type: "bytes32" },
              { type: "bytes32" },
            ],
            [
              keccak256(toHex(ORDER_TYPE)),
              BigInt(order.salt),
              order.maker,
              order.signer,
              BigInt(order.tokenId),
              BigInt(order.makerAmount),
              BigInt(order.takerAmount),
              order.side,
              order.signatureType,
              BigInt(order.timestamp),
              order.metadata,
              order.builder,
            ],
          ),
        );

        return concatHex([
          innerSignature,
          appDomainSeparator,
          contentsHash,
          toHex(ORDER_TYPE),
          toHex(ORDER_TYPE.length, { size: 2 }),
        ]);
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Accept the Quote">
    Submit the signed order with the winning `quote_id` before the returned
    `expires_at` deadline.

    ```http theme={null}
    POST /v1/requester/rfq/requests/<rfq-id>/accept
    Content-Type: application/json
    POLY_ADDRESS: <clob-credential-address>
    POLY_API_KEY: <clob-api-key>
    POLY_PASSPHRASE: <clob-passphrase>
    POLY_TIMESTAMP: <unix-seconds>
    POLY_SIGNATURE: <l2-signature>

    {
      "quote_id": "<quote-id>",
      "signed_order": {
        "salt": "<salt>",
        "maker": "<deposit-wallet-address>",
        "signer": "<deposit-wallet-address>",
        "tokenId": "<combo-yes-position-id>",
        "makerAmount": "966191",
        "takerAmount": "1932381",
        "side": 0,
        "signatureType": 3,
        "timestamp": "<unix-seconds>",
        "metadata": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "builder": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "signature": "<order-signature>"
      }
    }
    ```

    The response contains the latest known state. If Last Look is pending, the
    gateway waits up to one second for an execution or terminal update before
    returning.

    ```json theme={null}
    {
      "rfq_id": "<rfq-id>",
      "status": "EXECUTING",
      "taker_order_hash": "<order-hash>"
    }
    ```

    `EXECUTING` is not a confirmed fill. A response may instead remain
    `AWAITING_MAKER_CONFIRMATION`, or return HTTP `200` with `status: "FAILED"` and
    an `error` object if the maker declines or execution fails. Retrying the same
    authenticated acceptance does not execute the order twice; use `rfq_id` as the
    stable recovery identifier.
  </Step>

  <Step title="Poll Status">
    After acceptance, fetch durable status with a newly signed L2 request.

    ```http theme={null}
    GET /v1/requester/rfq/requests/<rfq-id>
    Accept: application/json
    POLY_ADDRESS: <clob-credential-address>
    POLY_API_KEY: <clob-api-key>
    POLY_PASSPHRASE: <clob-passphrase>
    POLY_TIMESTAMP: <unix-seconds>
    POLY_SIGNATURE: <l2-signature>
    ```

    ```json theme={null}
    {
      "rfq_id": "<rfq-id>",
      "status": "FILLED",
      "tx_hash": "<transaction-hash>"
    }
    ```

    Status reads before acceptance return HTTP `409`. Poll while the state is
    `AWAITING_MAKER_CONFIRMATION`, `EXECUTING`, `MINED`, or `RETRYING`. Stop on a
    successful `CONFIRMED` or `FILLED` state, or a terminal `FAILED`, `EXPIRED`, or
    `CANCELED` state. A local polling timeout does not mean the trade failed; resume
    polling the same `rfq_id`.
  </Step>
</Steps>
```

Example 2 (text):
```text
{
  "error": "invalid acceptance",
  "code": "INVALID_ACCEPTANCE"
}
```

---

## How Positions Work

**URL:** https://docs.polymarket.com/trading/positions/how-positions-work.md

**Contents:**
- What Is CTF?
- Core Operations
- Token Flow
- Token Identifiers
- Standard and Negative-Risk Markets
- Contract Addresses
- Next Steps

Polymarket tokenizes market outcomes using the [Conditional Token Framework (CTF)](https://github.com/gnosis/conditional-tokens-contracts), an open standard developed by Gnosis. Understanding CTF explains how positions are created, combined, and redeemed onchain.

CTF creates ERC-1155 tokens that represent prediction-market outcomes. Each binary market has two outcome tokens:

| Token   | Redeems for | Condition                | | ------- | ----------- | ------------------------ | | **YES** | \$1.00 pUSD | The event occurs         | | **NO**  | \$1.00 pUSD | The event does not occur |

These tokens are fully collateralized. Every YES and NO pair is backed by exactly `$1` of collateral locked through the CTF contracts.

CTF provides three operations for moving between collateral and positions:

<CardGroup cols={3}> <Card title="Split" icon="scissors" href="/trading/positions/manage#split-a-position"> Convert pUSD into a YES and NO token pair. </Card>

<Card title="Merge" icon="merge" href="/trading/positions/manage#merge-positions"> Convert a YES and NO token pair back into pUSD. </Card>

<Card title="Redeem" icon="hand-holding-dollar" href="/trading/positions/manage#redeem-resolved-positions"> Exchange resolved outcome tokens for their payout. </Card> </CardGroup>

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/token-flow.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=36f5a57946ac2b83136e17b6c06b358c" alt="pUSD can be split into YES and NO outcome tokens, which can be traded, merged, or redeemed after resolution." className="dark:hidden" width="1596" height="952" data-path="images/core-concepts/token-flow.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/token-flow.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=69d150ea49ffa18cd7f24689342b1bec" alt="pUSD can be split into YES and NO outcome tokens, which can be traded, merged, or redeemed after resolution." className="hidden dark:block" width="1596" height="952" data-path="images/dark/core-concepts/token-flow.png" /> </Frame>

Each outcome token has a unique **position ID**, which is used as its ERC-1155 token ID. CTF computes it onchain in three steps.

<Steps> <Step title="Compute the Condition ID">

<Step title="Compute the Collection IDs">

<Step title="Compute the Position IDs">

Polymarket uses different CTF configurations for standard and negative-risk markets:

| Feature           | Standard markets    | Negative-risk markets      | | ----------------- | ------------------- | -------------------------- | | CTF contract      | ConditionalTokens   | ConditionalTokens          | | Exchange contract | CTF Exchange        | Negative Risk CTF Exchange | | Multiple outcomes | Independent markets | Linked through conversion  |

For negative-risk markets, a conversion operation can exchange one NO token for YES tokens in the event's other outcomes. See [Negative Risk Markets](/concepts/negative-risk) for details.

See [Contracts](/resources/contracts) for Polymarket's current smart contract addresses on Polygon.

<CardGroup cols={3}> <Card title="Split a Position" icon="scissors" href="/trading/positions/manage#split-a-position"> Create outcome token pairs from pUSD. </Card>

<Card title="Merge Positions" icon="merge" href="/trading/positions/manage#merge-positions"> Convert balanced token pairs back into pUSD. </Card>

<Card title="Redeem Positions" icon="hand-holding-dollar" href="/trading/positions/manage#redeem-resolved-positions"> Collect payouts after resolution. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
getConditionId(oracle, questionId, outcomeSlotCount)
```

| Parameter          | Type      | Value                                                            |
| ------------------ | --------- | ---------------------------------------------------------------- |
| `oracle`           | `address` | [UMA CTF Adapter](https://github.com/Polymarket/uma-ctf-adapter) |
| `questionId`       | `bytes32` | Hash of the UMA ancillary data                                   |
| `outcomeSlotCount` | `uint`    | `2` for binary markets                                           |
```

Example 2 (text):
```text
getCollectionId(parentCollectionId, conditionId, indexSet)
```

| Parameter            | Type      | Value                                                             |
| -------------------- | --------- | ----------------------------------------------------------------- |
| `parentCollectionId` | `bytes32` | `bytes32(0)` for top-level positions                              |
| `conditionId`        | `bytes32` | Condition ID from the previous step                               |
| `indexSet`           | `uint`    | `1` (`0b01`) for the first outcome or `2` (`0b10`) for the second |

The `indexSet` is a bitmask identifying which outcome slots belong to a
collection. It must be a nonempty proper subset of the condition's outcome
slots. A binary market has one collection for each outcome.
```

Example 3 (text):
```text
getPositionId(collateralToken, collectionId)
```

| Parameter         | Type      | Value                                |
| ----------------- | --------- | ------------------------------------ |
| `collateralToken` | `IERC20`  | pUSD contract address on Polygon     |
| `collectionId`    | `bytes32` | Collection ID for one market outcome |

The resulting position IDs are the ERC-1155 token IDs for the market's YES and
NO outcomes. Most integrations should read these token IDs from market data.
Computing them manually is only necessary for direct contract integrations.
```

---

## Combinatorial Positions

**URL:** https://docs.polymarket.com/trading/positions/combinatorial.md

**Contents:**
- What They Represent
- How Tokens Work
- Resolution
- Related Pages

Combinatorial positions let traders express a single view across multiple Polymarket outcomes. Instead of trading one market at a time, a combinatorial position combines existing outcome tokens into one new YES/NO pair.

A combinatorial **YES** position represents a conjunction of legs:

It pays out when every leg in the combination pays out -- in above example, if Market A resolves YES AND Market B resolves YES AND Market C resolves NO. The matching combinatorial **NO** position is the complement:

It pays out when the full conjunction does not pay out. In this example, it will pay out if Market A resolves NO OR Market B resolves NO OR Market C resolves YES.

A combinatorial condition represents a conjuction of legs, but not a side. The combinatorial condition from above would be:

Each combinatorial condition has two **combinatorial positions**, the YES and the NO, which each have their own ERC 1155 token ID:

| Position | Meaning                               | | -------- | ------------------------------------- | | YES      | The full combination pays out         | | NO       | The full combination does not pay out |

Like standard CTF positions, the YES and NO pair is fully collateralized. Splitting collateral creates matching YES and NO combinatorial tokens, and merging a matching pair returns collateral.

However, these positions are *not* on the Conditional Tokens Framework. These positions exist on a new framework called the Positions Framework.

For normal binary outcomes, a combinatorial YES position pays out only if every leg wins. If any leg loses, the corresponding combinatorial NO position pays out.

If some legs are already resolved and others remain open, the position can be compressed into a simpler position that keeps only the unresolved legs and realizes any resolved collateral value.

<CardGroup cols={3}> <Card title="CTF Overview" icon="coins" href="/trading/positions/how-positions-work"> Minimal overview of Conditional Tokens </Card>

<Card title="Split Tokens" icon="scissors" href="/trading/positions/manage#split-a-position"> Create YES and NO token pairs </Card>

<Card title="Combos" icon="code" href="/trading/combos/overview"> Quote combinatorial positions through RFQ </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
YES(
  YES(Market A) and YES(Market B) and NO(Market C)
)
```

Example 2 (text):
```text
NO(
  YES(Market A) and YES(Market B) and NO(Market C)
)
```

Example 3 (text):
```text
YES(Market A) and YES(Market B) and NO(Market C)
```

---

## Wallets and Authentication

**URL:** https://docs.polymarket.com/trading/wallets-auth.md

**Contents:**
- Wallet Types
- Connect Your Account
- Create New Accounts
- Execute Gasless Transactions
- Set Up Trading Approvals
- Advanced Options
  - Derive a Deposit Wallet Address
  - Set Up EOA Trading
  - Remote Builder Signing
  - Opt Out of Beacon Upgrades

Start by identifying the account's wallet type. You can then connect an existing Polymarket account or create new accounts for your users.

A Deposit Wallet is the default smart wallet for trading on Polymarket. Your wallet type depends on how and when the account wallet was created.

| Wallet type        | When it applies                                                                              | | ------------------ | -------------------------------------------------------------------------------------------- | | **Deposit Wallet** | All Polymarket account wallets deployed on or after May 4, 2026 use it.                      | | **Proxy Wallet**   | A legacy smart wallet created through Magic Link or Google authentication on polymarket.com. | | **Safe Wallet**    | A legacy smart wallet created with an external signer such as MetaMask or Rabby Wallet.      |

A Deposit Wallet owner can give a separate signer scoped, time-limited trading access. See [Session Keys](/trading/session-keys) to authorize the signer and use its credentials.

Connect an existing polymarket.com account to trade with its funds and positions. Copy the account wallet address from the profile menu:

<Frame> <img className="hidden lg:block" src="https://mintcdn.com/polymarket-292d1b1b/1lJ*npwaE*MShiVL/images/deposit-wallet-desktop.png?fit=max&auto=format&n=1lJ*npwaE*MShiVL&q=85&s=6be3b87c53d6718f973db37e134ee944" alt="Polymarket profile menu showing the account wallet address on desktop" width="1280" height="274" data-path="images/deposit-wallet-desktop.png" />

<img className="block lg:hidden" src="https://mintcdn.com/polymarket-292d1b1b/1lJ*npwaE*MShiVL/images/deposit-wallet-mobile.png?fit=max&auto=format&n=1lJ*npwaE*MShiVL&q=85&s=4d6f87ed5440c5297e60d6331c47dc73" alt="Polymarket profile menu showing the account wallet address on mobile" width="529" height="274" data-path="images/deposit-wallet-mobile.png" /> </Frame>

Create a Relayer API key under polymarket.com → Settings → API Keys → Relayer API Keys:

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/1lJ*npwaE*MShiVL/images/relay-api-key-tutorial.png?fit=max&auto=format&n=1lJ*npwaE*MShiVL&q=85&s=674de7b1f46982a57fbe2bf57b905963" alt="Creating a Relayer API key from Polymarket settings" width="1269" height="785" data-path="images/relay-api-key-tutorial.png" /> </Frame>

This key authorizes gasless wallet operations for the account. Copy the **Signer Address** and **API Key** shown after creation.

<Tabs> <Tab title="TypeScript"> With the wallet address and Relayer API key ready, connect the account with `createSecureClient`.

<Tab title="Python"> With the wallet address and Relayer API key ready, connect the account with `AsyncSecureClient.create` (`SecureClient.create` is available for synchronous workflows).

<Tab title="API"> Authenticate with the CLOB and create L2 credentials.

Create a polymarket.com account to serve as your builder account. It represents your integration and owns the builder profile and API credentials used to create Deposit Wallets for your users. Each wallet remains controlled by its signer.

In the builder account, open polymarket.com → Settings → Builders and create an API key:

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/1lJ*npwaE*MShiVL/images/builder-key-1.png?fit=max&auto=format&n=1lJ*npwaE*MShiVL&q=85&s=70d5709ef4dbf6bc276ef7caa41cdb23" alt="Open Settings, select Builders, and create a Builder API key" width="1512" height="1040" data-path="images/builder-key-1.png" /> </Frame>

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/1lJ*npwaE*MShiVL/images/builder-key-2.png?fit=max&auto=format&n=1lJ*npwaE*MShiVL&q=85&s=509d270f5f5ff4dc882d7d8b7db17679" alt="Copy the generated Builder API key, secret, and passphrase" width="1494" height="1052" data-path="images/builder-key-2.png" /> </Frame>

Copy the **API Key**, **Secret**, and **Passphrase** shown after creation.

<Warning> Builder API credentials are secrets. Keep them on your server, and never expose or share them. </Warning>

<Tabs> <Tab title="TypeScript"> With the Builder API key ready, create the new account with `createSecureClient`.

<Tab title="Python"> With the Builder API key ready, create the new account with `AsyncSecureClient.create` (`SecureClient.create` is available for synchronous workflows).

<Tab title="API"> With the Builder API key ready, deploy a Deposit Wallet for each new signer through the Relayer.

Approve token spending, transfer funds, and manage positions from the account wallet without paying gas.

<Tabs> <Tab title="TypeScript"> `SecureClient` provides named methods for supported wallet actions. Each method returns a `TransactionHandle`; call `.wait()` to wait for the action to settle.

<Tab title="Python"> `AsyncSecureClient` provides named methods for supported wallet actions. Each method returns a transaction handle; call `await handle.wait()` to wait for the action to settle. The same methods are available on the synchronous `SecureClient`.

<Tab title="API"> A Deposit Wallet executes one or more contract calls as an ordered batch. The signer authorizes the complete batch, and the Relayer submits it gaslessly.

Set up the ERC-20 and ERC-1155 approvals that allow Polymarket's exchange contracts to spend the account wallet's pUSD and Conditional Tokens when placing orders. For Deposit Wallets, Safe Wallets, and Proxy Wallets, these approvals are submitted as a gasless transaction.

<Tabs> <Tab title="TypeScript"> Create a `SecureClient` with either a Relayer or Builder API key:

<Tab title="Python"> Create an `AsyncSecureClient` with either a Relayer or Builder API key (the same workflow is available with the synchronous `SecureClient`):

<Tab title="API"> Configure both CLOB exchange contracts so a Deposit Wallet can buy and sell in standard and neg-risk markets.

Explore additional wallet and authentication patterns for advanced integrations.

If you need to compute a Deposit Wallet address before deployment, use the deterministic derivation algorithm below.

<Note> Deposit Wallets deployed before the June 29, 2026 upgrade use a UUPS proxy. Deposit Wallets deployed after the upgrade use a beacon proxy. The following algorithm derives the address for a new Deposit Wallet with a beacon proxy. </Note>

See [Contract Addresses](/resources/contracts#wallet-factory-contracts) for the current Deposit Wallet factory and beacon.

If your EOA is allowlisted for trading, use it as the account wallet. Every onchain action—including token approvals, ERC-20 transfers, splits, merges, and redemptions—is submitted directly from the EOA and requires POL for gas.

<Tabs> <Tab title="TypeScript"> Pass the signer address as `wallet`. The SDK identifies the account as an EOA and skips Deposit Wallet deployment.

<Tab title="Python"> Pass the signer address as `wallet`. The SDK identifies the account as an EOA and skips Deposit Wallet deployment.

<Tab title="API"> <Steps> <Step title="Set Up Trading Approvals"> First, approve both CLOB exchange contracts to spend pUSD and manage Conditional Tokens. Submit each required approval transaction from the EOA and pay gas with POL held at that address.

Remote Builder Signing keeps Builder API credentials on your server while a TypeScript client requests signed headers for Builder-authenticated actions.

<Steps> <Step title="Create a Signing Endpoint"> Authenticate and authorize the caller on your server, then sign the request details supplied by the client.

<Step title="Connect the Client"> Pass the user's signer and the signing endpoint to the client. Authenticate signing requests with the application's session credentials or custom headers.

Deposit Wallets deployed after June 29, 2026 use an [ERC-1967 beacon proxy](https://eips.ethereum.org/EIPS/eip-1967#beacon-contract-address). This proxy pattern resolves the implementation for multiple wallets through a shared beacon, allowing Polymarket to send implementation upgrades without changing their addresses. The wallet owner can instead pin the wallet to the implementation that is current when it opts out. The owner-only calls below are submitted directly and require POL for gas.

<Warning> An opted-out wallet does not receive future security fixes, bug fixes, or features delivered through beacon upgrades. Review the current implementation and accept responsibility for maintaining the wallet before opting out. </Warning>

<Steps> <Step title="Pause the Wallet"> Send a direct onchain transaction from the wallet owner to call `pause()` on the Deposit Wallet. </Step>

<Step title="Wait for the Timelock"> Read `timelockDelay()` from the Deposit Wallet factory and wait until that interval has elapsed after the wallet was paused. </Step>

<Step title="Opt Out"> Send another transaction from the wallet owner to call `optOut()` on the Deposit Wallet. This pins the wallet to the beacon implementation that is current when the transaction executes. </Step>

<Step title="Unpause the Wallet"> Call `unpause()` from the wallet owner to clear the paused state. </Step> </Steps>

To resume receiving beacon upgrades, repeat the pause and timelock steps, call `optIn()`, and then unpause the wallet. Review the beacon's current default implementation before opting back in.

**Examples:**

Example 1 (text):
```text
<Steps>
  <Step title="Create a Secure Client">
    First, provide the signer and account wallet. Include the Relayer API
    key to authorize gasless wallet operations.

    ```ts theme={null}
    import { createSecureClient, relayerApiKey } from "@polymarket/client";
    import { privateKey } from "@polymarket/client/viem";

    const client = await createSecureClient({
      wallet: process.env.POLYMARKET_WALLET_ADDRESS,
      signer: privateKey(process.env.SIGNER_PRIVATE_KEY),
      apiKey: relayerApiKey({
        key: process.env.RELAYER_API_KEY!,
        address: process.env.RELAYER_API_KEY_ADDRESS!,
      }),
    });
    ```

    <Note>
      This example uses Viem with a private key. See [Wallet
      Integrations](/getting-started/typescript#wallet-integrations) to connect a
      signer from another supported wallet library.
    </Note>
  </Step>

  <Step title="Inspect the Account">
    Then, inspect the resolved account identity and wallet type.

    `client.account` contains the signer, account wallet, and wallet type for the session.

    <CodeGroup>
      ```ts AccountIdentity Type theme={null}
      type AccountIdentity = {
        signer: EvmAddress;
        wallet: EvmAddress;
        walletType: WalletType;
      };

      enum WalletType {
        EOA = 0,
        POLY_PROXY = 1,
        GNOSIS_SAFE = 2,
        DEPOSIT_WALLET = 3,
      }
      ```

      ```json AccountIdentity Example theme={null}
      {
        "signer": "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063",
        "wallet": "0x2e234dae75c793f67a35089c9d99245e1c58470b",
        "walletType": 3
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

That's it—you have connected your account.
```

Example 2 (python):
```python
<Steps>
  <Step title="Create a Secure Client">
    First, create an `AsyncSecureClient` or `SecureClient` with the private
    key and account wallet.
    Include the Relayer API key to authorize gasless wallet operations.

    <CodeGroup>
      ```python Async theme={null}
      import os

      from polymarket import AsyncSecureClient, RelayerApiKey

      client = await AsyncSecureClient.create(
          private_key=os.environ["SIGNER_PRIVATE_KEY"],
          wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
          api_key=RelayerApiKey(
              key=os.environ["POLYMARKET_RELAYER_API_KEY"],
              address=os.environ["POLYMARKET_RELAYER_API_KEY_ADDRESS"],
          ),
      )
      ```

      ```python Sync theme={null}
      import os

      from polymarket import RelayerApiKey, SecureClient

      client = SecureClient.create(
          private_key=os.environ["SIGNER_PRIVATE_KEY"],
          wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
          api_key=RelayerApiKey(
              key=os.environ["POLYMARKET_RELAYER_API_KEY"],
              address=os.environ["POLYMARKET_RELAYER_API_KEY_ADDRESS"],
          ),
      )
      ```
    </CodeGroup>
  </Step>

  <Step title="Inspect the Account">
    Then, inspect the resolved account wallet and wallet type.

    `client.wallet` and `client.wallet_type` contain the resolved account wallet and wallet type for the session.

    <CodeGroup>
      ```python Async theme={null}
      EvmAddress = NewType("EvmAddress", str)

      WalletType: TypeAlias = Literal["EOA", "POLY_PROXY", "GNOSIS_SAFE", "DEPOSIT_WALLET"]

      class AsyncSecureClient:
          wallet: EvmAddress
          wallet_type: WalletType
      ```

      ```python Sync theme={null}
      EvmAddress = NewType("EvmAddress", str)

      WalletType: TypeAlias = Literal["EOA", "POLY_PROXY", "GNOSIS_SAFE", "DEPOSIT_WALLET"]

      class SecureClient:
          wallet: EvmAddress
          wallet_type: WalletType
      ```
    </CodeGroup>
  </Step>
</Steps>

That's it—you have connected your account.
```

Example 3 (text):
```text
<Steps>
  <Step title="Create an L1 Signature">
    First, create an L1 signature to attest to ownership of the signer
    address. See [API Authentication](/getting-started/api#authentication)
    for the complete signing flow.

    ```json clobAuthTypedData theme={null}
    {
      "domain": {
        "name": "ClobAuthDomain",
        "version": "1",
        "chainId": 137
      },
      "types": {
        "ClobAuth": [
          { "name": "address", "type": "address" },
          { "name": "timestamp", "type": "string" },
          { "name": "nonce", "type": "uint256" },
          { "name": "message", "type": "string" }
        ]
      },
      "primaryType": "ClobAuth",
      "message": {
        "address": "<signer_address>",
        "timestamp": "<unix_seconds>",
        "nonce": "<nonce>",
        "message": "This message attests that I control the given wallet"
      }
    }
    ```

    Sign `clobAuthTypedData` with the signer that controls
    `<signer_address>`. The returned signature is `<clob_l1_signature>`.
  </Step>

  <Step title="Create L2 Credentials">
    Then, create L2 credentials by sending the signer address, timestamp,
    nonce, and L1 signature to the CLOB.

    <CodeGroup>
      ```bash Create theme={null}
      curl -X POST "https://clob.polymarket.com/auth/api-key" \
        -H "POLY_ADDRESS: <signer_address>" \
        -H "POLY_SIGNATURE: <clob_l1_signature>" \
        -H "POLY_TIMESTAMP: <unix_seconds>" \
        -H "POLY_NONCE: <nonce>"
      ```

      ```bash Derive theme={null}
      curl "https://clob.polymarket.com/auth/derive-api-key" \
        -H "POLY_ADDRESS: <signer_address>" \
        -H "POLY_SIGNATURE: <clob_l1_signature>" \
        -H "POLY_TIMESTAMP: <unix_seconds>" \
        -H "POLY_NONCE: <nonce>"
      ```
    </CodeGroup>

    Store the returned L2 credentials for authenticating private requests,
    including requests that place orders:

    ```json Response theme={null}
    {
      "apiKey": "<clob_api_key>",
      "secret": "<clob_api_secret>",
      "passphrase": "<clob_api_passphrase>"
    }
    ```
  </Step>
</Steps>

That's it—you have connected your account.
```

Example 4 (text):
```text
<Steps>
  <Step title="Create a Deposit Wallet">
    First, create a `SecureClient` with the signer and Builder API key. The SDK
    derives the signer's Deposit Wallet address and deploys the wallet
    automatically.

    ```ts theme={null}
    import { createSecureClient } from "@polymarket/client";
    import { builderApiKey } from "@polymarket/client/node";
    import { privateKey } from "@polymarket/client/viem";

    const client = await createSecureClient({
      signer: privateKey(process.env.SIGNER_PRIVATE_KEY),
      apiKey: builderApiKey({
        key: process.env.POLYMARKET_BUILDER_API_KEY!,
        secret: process.env.POLYMARKET_BUILDER_SECRET!,
        passphrase: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
      }),
    });
    ```

    <Note>
      This example uses Viem with a private key. See [Wallet
      Integrations](/getting-started/typescript#wallet-integrations) to connect a
      signer from another supported wallet library.
    </Note>
  </Step>

  <Step title="Inspect the Account">
    Then, inspect the resolved account identity and wallet type.

    `client.account` contains the signer, account wallet, and wallet type for the session.

    <CodeGroup>
      ```ts AccountIdentity Type theme={null}
      type AccountIdentity = {
        signer: EvmAddress;
        wallet: EvmAddress;
        walletType: WalletType;
      };

      enum WalletType {
        EOA = 0,
        POLY_PROXY = 1,
        GNOSIS_SAFE = 2,
        DEPOSIT_WALLET = 3,
      }
      ```

      ```json AccountIdentity Example theme={null}
      {
        "signer": "0x8f3cf7ad23cd3cadbd9735aff958023239c6a063",
        "wallet": "0x2e234dae75c793f67a35089c9d99245e1c58470b",
        "walletType": 3
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

That's it—you have created the new account.
```

---

## Supported Assets

**URL:** https://docs.polymarket.com/trading/bridge/supported-assets.md

**Contents:**
- Get Supported Assets
- Supported Chains
- Minimum Amounts
- Next Steps

The Bridge API supports deposits from multiple chains and tokens. All deposits are automatically converted to **pUSD on Polygon**, which is used as collateral for trading on Polymarket.

Retrieve the full list of supported chains and tokens with their minimum deposit amounts.

The bridge supports deposits from these blockchain networks:

| Chain           | Address Type | Min Deposit | Example Tokens                              | | --------------- | ------------ | ----------- | ------------------------------------------- | | Ethereum        | EVM          | \$7         | ETH, USDC, USDT, WBTC, DAI, LINK, UNI, AAVE | | Polygon         | EVM          | \$2         | POL, USDC, USDT, DAI, WETH, SAND            | | Arbitrum        | EVM          | \$2         | ETH, ARB, USDC, USDT, DAI, WBTC, USDe       | | Base            | EVM          | \$2         | ETH, USDC, USDT, DAI, cbBTC, AERO, USDS     | | Optimism        | EVM          | \$2         | ETH, OP, USDC, USDT, DAI, USDe              | | BNB Smart Chain | EVM          | \$2         | BNB, USDC, USDT, DAI, ETH, BTCB, BUSD       | | Solana          | SVM          | \$2         | SOL, USDC, USDT, USDe, TRUMP                | | Bitcoin         | BTC          | \$9         | BTC                                         | | Tron            | Tron         | \$9         | USDT                                        | | HyperEVM        | EVM          | \$2         | HYPE, USDC, USDe, stHYPE, UBTC, UETH        | | Abstract        | EVM          | \$2         | ETH, USDC, USDT                             | | Monad           | EVM          | \$2         | MON, USDC, USDT                             | | Ethereal        | EVM          | \$2         | USDe, WUSDe                                 | | Katana          | EVM          | \$2         | AUSD                                        | | Lighter         | EVM          | \$2         | USDC                                        |

<Note> Supported assets change over time. Always call `/supported-assets` for the current list before initiating a deposit. </Note>

Each asset has a `minCheckoutUsd` value, the minimum deposit amount in USD equivalent. Deposits below this threshold may fail to process, so check it before you tell a user how much to send.

Most L2 chains (Polygon, Arbitrum, Base, Optimism) have low minimums of \$2, while Ethereum deposits require \$7 minimum. Bitcoin and Tron have \$9 minimums due to higher bridging costs.

<CardGroup cols={2}> <Card title="Create Deposit" icon="arrow-right-to-bracket" href="/trading/bridge/deposit"> Generate bridge addresses for your wallet. </Card>

<Card title="Check Status" icon="clock" href="/trading/bridge/status"> Track your deposit progress. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
curl https://bridge.polymarket.com/supported-assets
```

Example 2 (text):
```text
{
  "supportedAssets": [
    {
      "chainId": "137",
      "chainName": "Polygon",
      "token": {
        "name": "USD Coin",
        "symbol": "USDC",
        "address": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
        "decimals": 6
      },
      "minCheckoutUsd": 2
    }
  ]
}
```

---

## Place Your First Order

**URL:** https://docs.polymarket.com/trading/quickstart.md

This guide shows you how to place your first order using an existing Polymarket account. For this guide, we recommend having at least 10 pUSD available. Create or fund an account at [polymarket.com](https://polymarket.com/) before you start.

Find your Polymarket wallet address in your profile menu:

<Frame> <img className="hidden lg:block" src="https://mintcdn.com/polymarket-292d1b1b/1lJ*npwaE*MShiVL/images/deposit-wallet-desktop.png?fit=max&auto=format&n=1lJ*npwaE*MShiVL&q=85&s=6be3b87c53d6718f973db37e134ee944" alt="Polymarket profile menu showing the account wallet address on desktop" width="1280" height="274" data-path="images/deposit-wallet-desktop.png" />

<img className="block lg:hidden" src="https://mintcdn.com/polymarket-292d1b1b/1lJ*npwaE*MShiVL/images/deposit-wallet-mobile.png?fit=max&auto=format&n=1lJ*npwaE*MShiVL&q=85&s=4d6f87ed5440c5297e60d6331c47dc73" alt="Polymarket profile menu showing the account wallet address on mobile" width="529" height="274" data-path="images/deposit-wallet-mobile.png" /> </Frame>

<Steps> <Step title="Authenticate"> First, authenticate with the CLOB.

<Step title="Choose an Outcome"> Then, fetch the market and select the outcome you want to buy. Orders identify each outcome by its token ID. See [Market Data](/market-data/overview) to find a different market.

<Step title="Place a Market Order"> Then, submit a small market buy. The order fills against available liquidity, and any unfilled amount is canceled instead of remaining open.

<Step title="Wait for Settlement"> Your order matched, but its trade settles on-chain asynchronously. Wait for settlement before checking your position.

<Step title="Check Your Position"> Finally, list your positions for the selected market and find the outcome you bought.

To let a separate signer place and cancel orders without using the owner key, continue to [Session Keys](/trading/session-keys).

**Examples:**

Example 1 (text):
```text
<Tabs>
  <Tab title="TypeScript">
    Pass the signer and wallet address to `createSecureClient`.

    ```ts theme={null}
    import { createSecureClient, OrderSide } from "@polymarket/client";
    import { privateKey } from "@polymarket/client/viem";

    const client = await createSecureClient({
      wallet: process.env.POLYMARKET_WALLET_ADDRESS,
      signer: privateKey(process.env.POLYMARKET_PRIVATE_KEY),
    });
    ```

    <Note>
      This example uses Viem. See [Wallet
      Integrations](/getting-started/typescript#wallet-integrations) to connect a
      signer from another supported wallet library.
    </Note>
  </Tab>

  <Tab title="Python">
    Pass the private key and wallet address to `AsyncSecureClient.create`.

    ```python theme={null}
    import os

    from polymarket import AsyncSecureClient

    client = await AsyncSecureClient.create(
        private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
        wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
    )
    ```
  </Tab>
</Tabs>
```

Example 2 (text):
```text
<Tabs>
  <Tab title="TypeScript">
    ```ts theme={null}
    const market = await client.fetchMarket({
      slug: "will-the-us-confirm-that-aliens-exist-before-2027-789-924-249",
    });

    const tokenId = market.outcomes.yes.tokenId!;
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    market = await client.get_market(
        slug="will-the-us-confirm-that-aliens-exist-before-2027-789-924-249",
    )

    token_id = market.outcomes.yes.token_id
    assert token_id is not None
    ```
  </Tab>
</Tabs>
```

Example 3 (text):
```text
<Tabs>
  <Tab title="TypeScript">
    Use `placeMarketOrder` to place the market order.

    ```ts theme={null}
    const response = await client.placeMarketOrder({
      tokenId,
      side: OrderSide.BUY,
      amount: "10", // Spend up to 10 pUSD
    });

    if (!response.ok) {
      throw new Error(response.message);
    }

    // response.orderId: string
    ```
  </Tab>

  <Tab title="Python">
    Use `place_market_order` to place the market order.

    ```python theme={null}
    response = await client.place_market_order(
        token_id=token_id,
        side="BUY",
        amount="10",  # Spend up to 10 pUSD
    )

    if not response.ok:
        raise RuntimeError(response.message)

    # response.order_id: str
    ```
  </Tab>
</Tabs>
```

Example 4 (text):
```text
<Tabs>
  <Tab title="TypeScript">
    Use `waitForOrderFillSettlement` to wait for the trade to settle.

    ```ts theme={null}
    const hashes = await client.waitForOrderFillSettlement(response);

    // hashes: TxHash[]
    ```
  </Tab>

  <Tab title="Python">
    Use `wait_for_order_fill_settlement` to wait for the trade to settle.

    ```python theme={null}
    hashes = await client.wait_for_order_fill_settlement(response)

    # hashes: tuple[TransactionHash, ...]
    ```
  </Tab>
</Tabs>
```

---

## Real-Time Order Updates

**URL:** https://docs.polymarket.com/trading/realtime-order-updates.md

**Contents:**
- User Stream
- Understand Order Updates
- Understand Trade Updates
- Recover After Reconnecting

Use real-time order updates to keep your view of a trading account current without polling. The user stream reports changes to the account's orders and the trades created when those orders match. For public order-book and market updates, see [Real-Time Data](/market-data/realtime-data).

<Note> Before subscribing, authenticate the account whose activity you want to monitor. See [Wallets and Authentication](/trading/wallets-auth). </Note>

The user stream delivers order changes and trade updates for the authenticated account. Subscribe without a market filter to follow the entire account, or provide condition IDs to follow selected markets.

<Tabs> <Tab title="TypeScript"> Given a `SecureClient`, subscribe to the `user` topic:

<Tab title="Python"> Given an `AsyncSecureClient`, subscribe with `UserSpec`. Real-time subscriptions are not available from the synchronous `SecureClient`.

<Tab title="API"> Connect to the authenticated user WebSocket:

Order updates tell you why the account's open-order state changed:

| Update       | Meaning                                 | | ------------ | --------------------------------------- | | Placement    | A new order was accepted.               | | Update       | Some or all of the order matched.       | | Cancellation | The remaining open amount was canceled. |

Trade updates follow a match through onchain settlement. Confirmation and permanent failure are terminal; a trade being retried may later be mined and confirmed.

| State                  | Terminal | Meaning                                                             | | ---------------------- | -------- | ------------------------------------------------------------------- | | Matched, not broadcast | No       | The orders matched before an onchain transaction was broadcast.     | | Matched                | No       | The orders matched and the transaction was submitted for execution. | | Mined                  | No       | The transaction was observed onchain but has not reached finality.  | | Confirmed              | Yes      | The trade reached finality successfully.                            | | Retrying               | No       | Settlement failed temporarily and is being retried.                 | | Failed                 | Yes      | Settlement failed permanently.                                      |

Real-time updates do not replace authoritative account reads or replay every change missed during a disconnection. After reconnecting, fetch the account's open orders and recent trades from [Manage Orders](/trading/manage-orders), then resume applying new stream events from that refreshed state.

**Examples:**

Example 1 (text):
```text
    const stream = await client.subscribe([{ topic: "user" }]);

    for await (const event of stream) {
      switch (event.type) {
        case "order":
          // event: UserOrderEvent
          break;
        case "trade":
          // event: UserTradeEvent
          break;
      }
    }
```

Example 2 (text):
```text
<Accordion title="User Events">
  #### Order Update

  <CodeGroup>
    ```ts UserOrderEvent Type theme={null}
    type UserOrderEvent = {
      topic: "user";
      type: "order";
      payload: {
        id: string;
        owner: string;
        market: string;
        tokenId: TokenId;
        side: OrderSide;
        orderOwner?: string | null;
        originalSize: DecimalString;
        sizeMatched: DecimalString;
        price: DecimalString;
        associateTrades?: string[] | null;
        outcome?: string | null;
        orderEventType: "PLACEMENT" | "UPDATE" | "CANCELLATION";
        createdAt?: IsoDateTimeString | null;
        expiresAt?: IsoDateTimeString | null;
        orderType?: "GTC" | "FOK" | "GTD" | "FAK" | null;
        status?: "LIVE" | "MATCHED" | "DELAYED" | "UNMATCHED" | "CANCELED" | null;
        makerAddress?: string | null;
        timestamp: EpochMilliseconds;
      };
    };
    ```

    ```json UserOrderEvent Example theme={null}
    {
      "topic": "user",
      "type": "order",
      "payload": {
        "id": "<order_id>",
        "owner": "<clob_api_key>",
        "market": "<condition_id>",
        "tokenId": "<token_id>",
        "side": "BUY",
        "originalSize": "10",
        "sizeMatched": "0",
        "price": "0.52",
        "outcome": "Yes",
        "orderEventType": "PLACEMENT",
        "status": "LIVE",
        "timestamp": 1782753357257
      }
    }
    ```
  </CodeGroup>

  #### Trade Update

  <CodeGroup>
    ```ts UserTradeEvent Type theme={null}
    type TradeMakerOrder = {
      orderId: string;
      owner: string;
      makerAddress?: string | null;
      matchedAmount: DecimalString;
      price: DecimalString;
      feeRateBps?: DecimalString | null;
      tokenId: TokenId;
      outcome?: string | null;
      outcomeIndex?: number | null;
      side: OrderSide;
    };

    type UserTradeEvent = {
      topic: "user";
      type: "trade";
      payload: {
        id: string;
        takerOrderId: string;
        market: string;
        tokenId: TokenId;
        side: OrderSide;
        size: DecimalString;
        feeRateBps?: DecimalString | null;
        price: DecimalString;
        status:
          | "TRADE_STATUS_MATCHED"
          | "TRADE_STATUS_MATCHED_NOT_BROADCASTED"
          | "TRADE_STATUS_MINED"
          | "TRADE_STATUS_CONFIRMED"
          | "TRADE_STATUS_RETRYING"
          | "TRADE_STATUS_FAILED";
        matchedAt?: IsoDateTimeString | null;
        updatedAt?: IsoDateTimeString | null;
        outcome?: string | null;
        owner: string;
        tradeOwner?: string | null;
        makerAddress?: string | null;
        transactionHash?: string | null;
        bucketIndex?: number | null;
        makerOrders?: TradeMakerOrder[] | null;
        traderSide?: "TAKER" | "MAKER" | null;
        timestamp: EpochMilliseconds;
      };
    };
    ```

    ```json UserTradeEvent Example theme={null}
    {
      "topic": "user",
      "type": "trade",
      "payload": {
        "id": "<trade_id>",
        "takerOrderId": "<order_id>",
        "market": "<condition_id>",
        "tokenId": "<token_id>",
        "side": "BUY",
        "size": "10",
        "price": "0.52",
        "status": "TRADE_STATUS_MATCHED",
        "owner": "<clob_api_key>",
        "traderSide": "TAKER",
        "timestamp": 1782753357257
      }
    }
    ```
  </CodeGroup>
</Accordion>

To receive updates only for selected markets, pass their condition IDs in
`markets`:

```ts theme={null}
const stream = await client.subscribe([
  {
    topic: "user",
    markets: ["<condition_id>"],
  },
]);
```
```

Example 3 (text):
```text
    from polymarket.streams import UserSpec


    async with await client.subscribe(UserSpec()) as stream:
        async for event in stream:
            if event.type == "order":
                ...  # event: UserOrderEvent
            elif event.type == "trade":
                ...  # event: UserTradeEvent
```

Example 4 (text):
```text
<Accordion title="User Events">
  #### Order Update

  <CodeGroup>
    ```python UserOrderEvent Type theme={null}
    class UserOrderPayload:
        id: str
        owner: str
        market: str
        token_id: TokenId
        side: Literal["BUY", "SELL"]
        order_owner: str | None
        original_size: Decimal
        size_matched: Decimal
        price: Decimal
        associate_trades: tuple[str, ...] | None
        outcome: str | None
        order_event_type: Literal["PLACEMENT", "UPDATE", "CANCELLATION"]
        created_at: datetime | None
        expires_at: datetime | None
        order_type: Literal["GTC", "FOK", "IOC", "GTD", "FAK"] | None
        status: Literal["LIVE", "MATCHED", "DELAYED", "UNMATCHED", "CANCELED"] | None
        maker_address: str | None
        timestamp: datetime | None

    class UserOrderEvent:
        topic: Literal["user"]
        type: Literal["order"]
        payload: UserOrderPayload
    ```

    ```json UserOrderEvent Example theme={null}
    {
      "topic": "user",
      "type": "order",
      "payload": {
        "id": "<order_id>",
        "owner": "<clob_api_key>",
        "market": "<condition_id>",
        "token_id": "<token_id>",
        "side": "BUY",
        "original_size": "10",
        "size_matched": "0",
        "price": "0.52",
        "outcome": "Yes",
        "order_event_type": "PLACEMENT",
        "status": "LIVE",
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>

  #### Trade Update

  <CodeGroup>
    ```python UserTradeEvent Type theme={null}
    class UserTradeMakerOrder:
        order_id: str
        owner: str
        maker_address: str | None
        matched_amount: Decimal
        price: Decimal
        fee_rate_bps: Decimal | None
        token_id: TokenId
        outcome: str | None
        outcome_index: int | None
        side: Literal["BUY", "SELL"]

    class UserTradePayload:
        id: str
        taker_order_id: str
        market: str
        token_id: TokenId
        side: Literal["BUY", "SELL"]
        size: Decimal
        fee_rate_bps: Decimal | None
        price: Decimal
        status: Literal[
            "MATCHED",
            "MATCHED_NOT_BROADCASTED",
            "MINED",
            "CONFIRMED",
            "RETRYING",
            "FAILED",
        ]
        matched_at: datetime | None
        updated_at: datetime | None
        outcome: str | None
        owner: str
        trade_owner: str | None
        maker_address: str | None
        transaction_hash: str | None
        bucket_index: int | None
        maker_orders: tuple[UserTradeMakerOrder, ...] | None
        trader_side: Literal["TAKER", "MAKER"] | None
        timestamp: datetime | None

    class UserTradeEvent:
        topic: Literal["user"]
        type: Literal["trade"]
        payload: UserTradePayload
    ```

    ```json UserTradeEvent Example theme={null}
    {
      "topic": "user",
      "type": "trade",
      "payload": {
        "id": "<trade_id>",
        "taker_order_id": "<order_id>",
        "market": "<condition_id>",
        "token_id": "<token_id>",
        "side": "BUY",
        "size": "10",
        "price": "0.52",
        "status": "MATCHED",
        "owner": "<clob_api_key>",
        "trader_side": "TAKER",
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>
</Accordion>

To receive updates only for selected markets, pass their condition IDs to
`UserSpec`:

```python theme={null}
async with await client.subscribe(
    UserSpec(markets=["<condition_id>"]),
) as stream:
    async for event in stream:
        ...
```
```

---

## Mark Price

**URL:** https://docs.polymarket.com/perps/learn-about-trading/mark-price.md

**Contents:**
- C1: Smoothed Order Book Mid
- C2: Local Market Activity
- C3: Aggregated External Mark
- Why Three Candidates?
- Finalization
- Fallback Summary

Mark Price is the price used across the system for margin, unrealized PnL, liquidation triggers, funding premium computation, and risk checks. It is updated every 200 milliseconds.

Mark Price is computed as the median of three candidates, each capturing a different view of fair value.

C1 anchors to Index and adjusts gradually based on where the local order book mid is trading relative to it.

C2 reflects what is actually trading on the local book.

C3 is built from external mark feeds, separate from Index feeds, that provide an independent view of fair value outside the local order book.

For each market, the system:

If no valid external mark data is available, C3 falls back to Index.

Using the median of three independent price signals provides resilience:

The median ensures that no single signal can unilaterally move Mark Price. At least two of the three candidates must agree for the mark to shift.

After computing `median(C1, C2, C3)`, the raw mark is normalized before being published:

Every input degrades gracefully to [Index Price](/perps/learn-about-trading/index-price).

| Condition                       | Behavior                                                    | | ------------------------------- | ----------------------------------------------------------- | | Index input stale               | Falls back to last known market index                       | | Order book mid unavailable      | C1 falls back to Index                                      | | No recent trades or quotes      | C2 falls back to Index                                      | | External mark feeds unavailable | C3 falls back to Index                                      | | All inputs missing              | Mark tracks Index because all candidates fall back to Index |

In the worst case, when there is no local book, no recent trades, and no external mark feeds, all three candidates converge to Index and Mark Price tracks Index directly.

**Examples:**

Example 1 (text):
```text
Mark = median(C1, C2, C3)
```

Example 2 (text):
```text
C1 = Index + EMA(Mid - Index)
```

Example 3 (text):
```text
C2 = median(BestBid, BestAsk, LastTrade)
```

---

## Market Makers

**URL:** https://docs.polymarket.com/trading/combos/market-makers.md

**Contents:**
- Start Quoting
- Handle Quote Requests
  - Authorize the Quote
  - Quote Partial Fills
  - Use Inventory
  - Cancel Quotes
  - Last Look
- Manage Combo Positions
  - List Combo Positions
  - List Combo Activity

This guide shows market makers how to handle Combo RFQs. You will open a quoting session, respond to incoming requests, cancel submitted quotes when needed, confirm fills through Last Look, and monitor execution updates.

<Note> For development updates on market making for Combos, join the [Combos market maker Telegram group](https://t.me/+eyMtdtKasWZjYTMx). </Note>

Start by preparing an authenticated quoting session with the RFQ system. You need a Polymarket account; create one at [polymarket.com](https://polymarket.com).

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Install the Package"> Install the Unified TypeScript SDK with the package manager of your choice.

<Tab title="Python"> <Steps> <Step title="Install the Package"> Install the Python SDK with the package manager of your choice.

<Tab title="API"> <Note> Use Polygon mainnet chain ID `137` for CLOB authentication and Exchange v3 order signing. </Note>

Quote requests describe a user's intent to buy or sell shares in a Combo defined by a given set of legs. A quote request can currently only buy or sell the YES side of a Combo.

The following cases show how a market maker can satisfy a user's buy or sell request using collateral or inventory.

| Quote Request | Using Collateral      | From Inventory         | | ------------- | --------------------- | ---------------------- | | Buy YES       | Buy NO at `1 - price` | Sell YES at `price`    | | Sell YES      | Buy YES at `price`    | Sell NO at `1 - price` |

See [Combinatorial Positions](/trading/positions/combinatorial) for more detail on the YES/NO position model.

The diagram below shows the maker-side quote lifecycle, from receiving a quote request through its terminal outcome.

Authorize each quote by pricing the request and returning a signed order to the RFQ system. Quoters should respond within the **400 ms** submission window.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Switch on Event Type"> First, switch on `event.type` to handle quote requests from the session stream.

<Tab title="Python"> <Steps> <Step title="Check Event Type"> First, use `isinstance(...)` to handle quote requests from the session stream.

<Tab title="API"> <Steps> <Step title="Receive the Quote Request"> The RFQ system sends `RFQ_REQUEST` messages over the authenticated WebSocket. Inspect the request before pricing it.

<Tabs> <Tab title="TypeScript"> If you only want to fill part of the requested size, pass `size` with the quote. `size` is a normalized decimal value: `"10"` means 10 shares, or 10,000,000 base units. When omitted, the SDK quotes the full requested size.

<Tab title="Python"> If you only want to fill part of the requested size, pass `size` with the quote. `size` is a `Decimal`-compatible value: `Decimal("10")` means 10 shares, or 10,000,000 base units. When omitted, the SDK quotes the full requested size.

<Tab title="API"> Partial fills use the same signed-order flow as a full quote.

<Tabs> <Tab title="TypeScript"> By default, quotes use collateral (pUSD) to buy YES or NO tokens as needed to satisfy the quote request according to the combinatorial position logic. Pass `source: "inventory"` when you want to quote from existing inventory instead.

<Tab title="Python"> By default, quotes use collateral (pUSD) to buy YES or NO tokens as needed to satisfy the quote request according to the combinatorial position logic. Pass `source=RfqQuoteSource.INVENTORY` when you want to quote from existing inventory instead.

<Tab title="API"> Inventory quotes sell existing outcome tokens instead of spending collateral. The RFQ quote price still means pUSD per YES Combo share.

After you submit a quote, keep the returned quote reference. If your price, inventory, or risk changes before the quote is selected, use that reference to request cancellation.

<Note> A cancellation acknowledgement means the RFQ system processed the cancellation request. It does not guarantee the quote was withdrawn from an RFQ that was already selected. </Note>

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Store the Quote Reference"> First, keep the quote reference returned by `event.quote(…)`. It contains the `rfqId` and `quoteId` needed to cancel the quote.

<Tab title="Python"> <Steps> <Step title="Store the Quote Reference"> First, keep the quote reference returned by `event.quote(...)`. It contains the `rfq*id` and `quote*id` needed to cancel the quote.

<Tab title="API"> Send a cancellation request with the RFQ ID and quote ID. On the WebSocket, the RFQ system acknowledges a processed cancellation request with `ACK*RFQ*QUOTE_CANCEL`.

Last Look is a separate final review step for makers that have it enabled. If a selected quote requires Last Look, run a final risk check before the deadline and accept or reject the fill.

Last Look is offered to makers with approximately \$2,500 in Combo notional volume and an established line of communication with Polymarket. This keeps the program reliable and helps Polymarket resolve system issues quickly.

To request access, complete the [Last Look request form](https://forms.gle/dk5A1DRw8EN5uP9z5).

<Warning> Makers are expected to accept most selected quotes. We track acceptance rates, and makers who reject more than 15% of selected quotes over a one-hour lookback window may be paused from quoting for a few minutes. </Warning>

Once access is enabled, your quoting system will immediately be asked to review selected fills. Make sure it is ready to evaluate and answer them before approval is activated.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Switch on the Event Type"> First, switch on `event.type` to handle confirmation requests from the same session stream.

<Tab title="Python"> <Steps> <Step title="Check Event Type"> First, use `isinstance(...)` to handle confirmation requests from the same session stream.

<Tab title="API"> If Last Look is enabled for your maker, the RFQ WebSocket sends `RFQ*CONFIRMATION*REQUEST` after your quote is selected.

Use Combo position workflows to manage inventory throughout the quote lifecycle.

<Tip> Quoting can leave pUSD locked across related Combo positions. Use [Collateral Return](/trading/combos/collateral-return) to release available pUSD before resolution while preserving unmatched exposure. </Tip>

List Combo positions as part of your background inventory sync. Keep this state fresh outside the quote path.

<Note> Default listings omit open positions with a share balance below 0.001, such as dust left after a sell-all cashout. Resolved positions are always returned, and incremental sync requests return every position regardless of balance. </Note>

<Tabs> <Tab title="TypeScript"> Use `client.listComboPositions(...)` to page through Combo positions for the authenticated account.

<Tab title="Python"> Call `list*combo*positions()` on an existing `AsyncSecureClient`.

<Tab title="API"> Use the Data API to list Combo positions for a wallet.

Use Combo activity when you need an audit trail for inventory-changing events, including splits, merges, conversions, wraps, unwraps, and redeems. Use Combo positions for current inventory state.

<Tabs> <Tab title="TypeScript"> Use `client.listComboActivity(...)` to page through Combo lifecycle activity for the authenticated account.

<Tab title="Python"> Call `list*combo*activity()` on an existing `AsyncSecureClient`.

<Tab title="API"> Use the Data API to list Combo lifecycle activity for a wallet.

If you want to quote from inventory, build the inventory before quote requests arrive. Splitting converts collateral into complementary Combo positions for a set of legs. Merging converts matching complementary Combo positions back into collateral.

<Note> Splitting and merging manage complementary inventory directly. When capital is locked across related positions that cannot be merged as-is, use [Collateral Return](/trading/combos/collateral-return). </Note>

<Tabs> <Tab title="TypeScript"> Use `client.splitPosition(...)` with `legs` to create Combo inventory from collateral. `amount` is in pUSD base units.

<Tab title="Python"> Use `client.split_position(...)` with `legs` to create Combo inventory from collateral. `amount` is in pUSD base units.

<Tab title="API"> Use the Relayer API to split or merge Combo inventory by sending an ordered list of encoded contract calls in one batch. The following steps assume you are using a Deposit Wallet.

When a Combo position resolves, redeem the winning position to settle it back to collateral.

<Tabs> <Tab title="TypeScript"> Use `client.redeemPositions(...)` with a Combo `positionId`. The SDK redeems the available balance for that resolved position.

<Tab title="Python"> Use `client.redeem*positions(...)` with a Combo `position*id`. The SDK redeems the available balance for that resolved position.

<Tab title="API"> Use the Relayer API to redeem resolved Combo positions by sending an ordered list of encoded contract calls in one batch. The following steps assume you are using a Deposit Wallet.

Use the Combo markets catalog to retrieve active markets that can be used as Combo legs. Markets are ordered by volume descending.

<Tabs> <Tab title="TypeScript"> Use `client.listComboMarkets(...)` to page through markets that can be used as Combo legs.

<Tab title="Python"> Use `client.list*combo*markets(...)` to page through markets that can be used as Combo legs.

<Tab title="API"> Fetch the first page of Combo-enabled markets.

Market makers should build their own view of the markets that support Combos before quote requests arrive. Combo-enabled markets expose a list of position IDs with two entries: the first is the YES position ID and the second is the NO position ID. These IDs identify the outcome positions your pricing system can map back to market data.

<Tabs> <Tab title="TypeScript"> Fetch non-closed markets and index Combo-enabled markets by position ID in your own market data store.

<Tab title="Python"> Fetch non-closed markets and index Combo-enabled markets by position ID in your own market data store.

<Tab title="API"> Use Gamma `GET /markets/keyset` to resolve Combo leg position IDs into market metadata. Build this mapping outside the quote path.

Execution updates tell you what happened after one of your quotes was selected. Use them to reconcile RFQ state, transaction hashes, and terminal execution outcomes in your own systems.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Switch on the Event Type"> First, switch on `event.type` to handle execution updates from the same session stream.

<Tab title="Python"> <Steps> <Step title="Check Event Type"> First, use `isinstance(...)` to handle execution updates from the same session stream.

<Tab title="API"> Listen for `RFQ*EXECUTION*UPDATE` messages on the RFQ WebSocket after one of your quotes is selected.

Confirmed trade broadcasts tell connected market makers when any Combo RFQ trade has completed successfully. Use them to build a public trade tape, update risk, or reconcile market activity that was filled by another maker.

Trade broadcasts are best-effort and may be replayed after reconnects. Deduplicate them by RFQ ID: `rfqId` in TypeScript or `rfq_id` in Python and raw WebSocket messages.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Switch on the Event Type"> First, switch on `event.type` to handle trade broadcasts from the same session stream.

<Tab title="Python"> <Steps> <Step title="Check Event Type"> First, use `isinstance(...)` to handle trade broadcasts from the same session stream.

<Tab title="API"> Listen for `RFQ_TRADE` messages on the RFQ WebSocket after Combo executions are confirmed. These messages are sent to authenticated quoter sessions and exclude maker identity and per-maker fill allocations.

In this section, we will talk you through how to handle errors with the RFQ system.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

<Tab title="API"> When a WebSocket command fails validation or cannot be applied, the RFQ system sends `RFQ_ERROR`.

When an RFQ rejection includes a code, its value is stable across integrations. New codes may be introduced over time, so handle unrecognized values as rejections rather than assuming this list is exhaustive.

<AccordionGroup> <Accordion title="Common RFQ Error Codes"> | Code                                       | Meaning                                                        | | ------------------------------------------ | -------------------------------------------------------------- | | `INVALID*MESSAGE`                          | Request or action type is invalid                              | | `UNAUTHORIZED*ROLE`                        | Action is not allowed for the authenticated role               | | `ADDRESS*MISMATCH`                         | Request identity does not match the authenticated session      | | `UNKNOWN*RFQ`                              | RFQ ID is not active or no longer exists                       | | `EXPIRED*RFQ`                              | RFQ has expired                                                | | `SUBMISSION*WINDOW*CLOSED`                 | Quote arrived after the submission window closed               | | `ALLOWANCE*VALIDATION*FAILED`              | Maker allowance is insufficient for the quoted order           | | `BALANCE*VALIDATION*FAILED`                | Maker balance is insufficient for the quoted order             | | `PRE*EXECUTION*BALANCE*RESERVATION*FAILED` | Balance reservation failed before execution                    | | `INVALID*QUOTE`                            | Quote is invalid and no more specific code applies             | | `INVALID*SIGNATURE`                        | Signed order signature could not be verified                   | | `INVALID*RFQ*STATE`                        | RFQ is not in a state that accepts the requested command       | | `INVALID*CONFIRMATION`                     | Last Look response is invalid                                  | | `MAKER*NOT*REQUIRED`                       | This quote maker is not required for last-look confirmation    | | `MAKER*ALREADY*RESPONDED`                  | This quote maker already responded to the confirmation request | | `MAKER*QUOTE*LIMITED`                      | Quote submissions from this maker are temporarily limited      | | `SERVICE_UNAVAILABLE`                      | RFQ system is temporarily unavailable                          | </Accordion>

<Accordion title="Quote Validation Codes"> | Code                                              | Meaning                                                         | | ------------------------------------------------- | --------------------------------------------------------------- | | `MISSING*QUOTE*ID`                                | Server-generated quote identifier was not assigned              | | `MISSING*RFQ*ID`                                  | RFQ identifier is missing from the quote                        | | `MISSING*SIGNER*ADDRESS*IN*QUOTE`                 | Authenticated signer identity was not applied                   | | `MISSING*MAKER*ADDRESS*IN*QUOTE`                  | Authenticated maker identity was not applied                    | | `PRICE*E6*NOT*POSITIVE`                           | Quote price is not positive                                     | | `SIZE*E6*NOT*POSITIVE`                            | Quote size is not positive                                      | | `MISSING*SALT*IN*SIGNED*ORDER`                    | Signed order is missing its salt                                | | `MISSING*MAKER*IN*SIGNED*ORDER`                   | Signed order is missing its maker                               | | `MISSING*SIGNER*IN*SIGNED*ORDER`                  | Signed order is missing its signer                              | | `MISSING*TOKEN*ID*IN*SIGNED*ORDER`                | Signed order is missing its token identifier                    | | `MISSING*MAKER*AMOUNT*IN*SIGNED*ORDER`            | Signed order is missing its maker amount                        | | `MISSING*TAKER*AMOUNT*IN*SIGNED*ORDER`            | Signed order is missing its taker amount                        | | `MISSING*TIMESTAMP*IN*SIGNED*ORDER`               | Signed order is missing its timestamp                           | | `MISSING*SIGNATURE*IN*SIGNED*ORDER`               | Signed order is missing its signature                           | | `INVALID*ORDER*SIDE`                              | Signed order uses an invalid side                               | | `INVALID*SIGNATURE*TYPE`                          | Signed order uses an unsupported signature type                 | | `SIGNED*ORDER*SIGNER*DOES*NOT*MATCH*AUTH`         | Signed-order signer differs from the authenticated signer       | | `SIGNED*ORDER*MAKER*DOES*NOT*MATCH*AUTH`          | Signed-order maker differs from the authenticated maker         | | `SIGNED*ORDER*SIGNATURE*TYPE*DOES*NOT*MATCH*AUTH` | Signed-order signature type differs from the authenticated type | | `QUOTED*PRICE*ABOVE*SAFETY*THRESHOLD`             | BUY quote exceeds the `0.90909` safety maximum                  | | `QUOTED*PRICE*OUT*OF*RANGE`                       | Quote price exceeds `1`                                         | | `ORDER*SIDE*OR*TOKEN*DOES*NOT*MATCH*REQUEST`      | Signed-order side or token does not match the RFQ direction     | | `SIGNED*ORDER*MAKER*AMOUNT*NOT*POSITIVE`          | Signed-order maker amount is not a positive integer             | | `SIGNED*ORDER*TAKER*AMOUNT*NOT*POSITIVE`          | Signed-order taker amount is not a positive integer             | | `SIGNED*ORDER*SIZE*DOES*NOT*COVER*QUOTE`          | Signed order cannot cover the quoted size                       | | `SIGNED*ORDER*PRICE*WORSE*THAN*QUOTE`             | Signed-order limit price is worse than the quoted price         | </Accordion> </AccordionGroup>

When quoting Combos, account for these pricing and data risks:

Remember that as with all trading, RFQs you choose to quote and fill are your responsibility to vet.

**Examples:**

Example 1 (text):
```text
    <CodeGroup>
      ```bash pnpm theme={null}
      pnpm add @polymarket/client@latest viem
      ```

      ```bash npm theme={null}
      npm install @polymarket/client@latest viem
      ```

      ```bash yarn theme={null}
      yarn add @polymarket/client@latest viem
      ```
    </CodeGroup>

    <Note>
      This page uses Viem for wallet signing. See the [TypeScript tooling
      guide](/getting-started/typescript#wallet-integrations) for other wallet
      library integrations.
    </Note>
  </Step>

  <Step title="Create a Secure Client">
    Create a `SecureClient` with a wallet that has funds for fulfilling
    user requests and its signer details.

    ```ts theme={null}
    import { createSecureClient, relayerApiKey } from "@polymarket/client";
    import { privateKey } from "@polymarket/client/viem";

    const client = await createSecureClient({
      wallet: process.env.POLYMARKET_WALLET_ADDRESS!,
      signer: privateKey(process.env.PRIVATE_KEY!),
      apiKey: relayerApiKey({
        key: process.env.RELAYER_API_KEY!,
        address: process.env.RELAYER_API_KEY_ADDRESS!,
      }),
    });
    ```

    The Relayer API key is necessary for setting up trading approvals in the next
    step. Create a [Relayer API key](https://polymarket.com/settings?tab=api-keys)
    from polymarket.com → Settings → API Keys.
  </Step>

  <Step title="Set Up Trading Approvals">
    Set up the approvals required to fill user requests.

    ```ts theme={null}
    await client.setupTradingApprovals();
    ```
  </Step>

  <Step title="Open an RFQ Session">
    Open the RFQ session.

    ```ts theme={null}
    const session = await client.openRfqSession();

    for await (const event of session) {
      // event: RfqEvent
    }
    ```
  </Step>

  <Step title="Close the Session">
    You can close the session at any time by calling `session.close()`.

    ```ts theme={null}
    for await (const event of session) {
      if (shouldCloseSession) {
        await session.close();
        break;
      }

      // …
    }
    ```
  </Step>
</Steps>
```

Example 2 (text):
```text
    <CodeGroup>
      ```bash uv theme={null}
      uv add polymarket-client
      ```

      ```bash pip theme={null}
      pip install polymarket-client
      ```

      ```bash poetry theme={null}
      poetry add polymarket-client
      ```
    </CodeGroup>
  </Step>

  <Step title="Create a Secure Client">
    Create an `AsyncSecureClient` with a wallet that has funds for fulfilling user
    requests and its signer details.

    ```python theme={null}
    import os

    from polymarket import AsyncSecureClient, RelayerApiKey


    client = await AsyncSecureClient.create(
        private_key=os.environ["PRIVATE_KEY"],
        wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
        api_key=RelayerApiKey(
            key=os.environ["RELAYER_API_KEY"],
            address=os.environ["RELAYER_API_KEY_ADDRESS"],
        ),
    )
    ```

    The Relayer API key is necessary for setting up trading approvals in the next
    step. Create a [Relayer API key](https://polymarket.com/settings?tab=api-keys)
    from polymarket.com → Settings → API Keys.
  </Step>

  <Step title="Set Up Trading Approvals">
    Set up the approvals required to fill user requests.

    ```python theme={null}
    await client.setup_trading_approvals()
    ```
  </Step>

  <Step title="Open an RFQ Session">
    Open the RFQ session.

    ```python theme={null}
    async with client.open_rfq_session() as session:
        async for event in session:
            # event: RfqEvent
            ...
    ```
  </Step>

  <Step title="Close the Session">
    You can close the session at any time by calling `await session.close()`.

    ```python theme={null}
    async with client.open_rfq_session() as session:
        async for event in session:
            if should_close_session:
                await session.close()
                break

            ...
    ```
  </Step>
</Steps>
```

Example 3 (text):
```text
<Steps>
  <Step title="Open the WebSocket">
    Connect to the RFQ system WebSocket.

    ```text theme={null}
    wss://combos-rfq-gateway-quoter.polymarket.com/ws/rfq
    ```

    To inspect the stream before integrating:

    ```bash theme={null}
    wscat -c "wss://combos-rfq-gateway-quoter.polymarket.com/ws/rfq"
    ```

    Some write operations are also available through the REST API.

    ```text theme={null}
    https://combos-rfq-api.polymarket.com
    ```
  </Step>

  <Step title="Acquire CLOB Credentials">
    RFQ WebSocket authentication uses CLOB API credentials: API key, secret, and
    passphrase. If you need credentials, start with [Getting API
    Credentials](/getting-started/api#authentication).
  </Step>

  <Step title="Resolve Quoter Identity">
    Resolve the order signer identity before sending `auth`. The RFQ system needs
    the address that signs the order, the wallet that funds the order, and the
    signature type that connects those two addresses.

    | Wallet Type    | `signature_type` | `signer_address`              | `maker_address`      |
    | -------------- | ---------------- | ----------------------------- | -------------------- |
    | Deposit Wallet | `3` POLY\_1271   | Deposit wallet address        | Deposit wallet       |
    | Safe Wallet    | `2` Safe         | Authenticated signing address | Derived Safe wallet  |
    | Proxy Wallet   | `1` Proxy        | Authenticated signing address | Derived proxy wallet |
    | EOA            | `0` EOA          | EOA address                   | Same EOA address     |

    For more detail, see [Wallets and Authentication](/trading/wallets-auth#wallet-types).
  </Step>

  <Step title="Authenticate">
    Send `auth` as the first WebSocket message within 30 seconds. Include the CLOB
    credentials and the `signer_address`, `maker_address`, and `signature_type`
    values resolved in the previous step. This example uses a Deposit Wallet.

    ```json theme={null}
    {
      "type": "auth",
      "auth": {
        "apiKey": "YOUR_API_KEY",
        "secret": "YOUR_API_SECRET",
        "passphrase": "YOUR_API_PASSPHRASE"
      },
      "identity": {
        "signer_address": "<signer_address>",
        "maker_address": "<maker_address>",
        "signature_type": 3 // <signature_type>
      }
    }
    ```

    Authentication returns a success or failure response.

    <CodeGroup>
      ```json Success theme={null}
      {
        "type": "auth",
        "success": true,
        "address": "0xAuthenticatedAddress",
        "role": "maker"
      }
      ```

      ```json Failure theme={null}
      {
        "type": "auth",
        "success": false,
        "error": "unauthenticated"
      }
      ```
    </CodeGroup>

    <Note>
      The RFQ system uses WebSocket protocol heartbeat frames to keep the connection
      alive. It sends a ping frame every 30 seconds with payload `rfq`; your client
      must respond with a pong frame that echoes the same payload. Most WebSocket
      clients handle this automatically. These are protocol frames, not JSON
      messages in the RFQ event stream. The gateway closes stale connections after 2
      minutes without an inbound message or pong.
    </Note>
  </Step>

  <Step title="Check Approval Requirements">
    Before posting quotes or managing Combo inventory, `maker_address` must approve
    the contracts that may transfer its assets.

    | Approval                    | Required when                                     | Contract call                                           |
    | --------------------------- | ------------------------------------------------- | ------------------------------------------------------- |
    | pUSD collateral             | The quoted order transfers pUSD                   | `CollateralToken.approve(ExchangeV3, maxUint256)`       |
    | Combo positions             | The quoted order transfers Combo positions        | `PositionManager.setApprovalForAll(ExchangeV3, true)`   |
    | Router pUSD collateral      | You split pUSD into positions through the Router  | `CollateralToken.approve(Router, maxUint256)`           |
    | Router positions            | You manage or redeem positions through the Router | `PositionManager.setApprovalForAll(Router, true)`       |
    | AutoRedeemer Combo operator | You want automatic redemption flows to use it     | `PositionManager.setApprovalForAll(AutoRedeemer, true)` |

    Use these contract addresses to build the approval calls.

    | Contract              | Address                                      |
    | --------------------- | -------------------------------------------- |
    | pUSD collateral token | `0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB` |
    | Exchange v3           | `0xe3333700cA9d93003F00f0F71f8515005F6c00Aa` |
    | Router                | `0x12121212006e4CD160D18e3f00711DA5c3372600` |
    | PositionManager       | `0x006F54F7f9A22e0000CC2AB60031000000ae9fEF` |
    | AutoRedeemer          | `0xa1200000d0002264C9a1698e001292D00E1b00af` |

    <Note>
      The following steps use the Deposit Wallet [gasless transaction
      flow](/trading/wallets-auth#execute-gasless-transactions). If you are trading
      with an EOA, submit the approvals directly from `maker_address`. For Safe or
      Proxy Wallet flows, use an SDK.
    </Note>
  </Step>

  <Step title="Build the Approval Call List">
    Encode the approval calls that are not already in place.

    <CodeGroup>
      ```solidity ERC-20 Approval theme={null}
      function approve(address spender, uint256 amount) returns (bool);
      ```

      ```solidity ERC-1155 Approval theme={null}
      function setApprovalForAll(address operator, bool approved);
      ```
    </CodeGroup>

    Build a relayer call list from the encoded calldata.

    ```json theme={null}
    [
      {
        "target": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
        "value": "0",
        "data": "<approve_exchange_v3_calldata>"
      },
      {
        "target": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
        "value": "0",
        "data": "<approve_router_calldata>"
      },
      {
        "target": "0x006F54F7f9A22e0000CC2AB60031000000ae9fEF",
        "value": "0",
        "data": "<approve_exchange_v3_operator_calldata>"
      },
      {
        "target": "0x006F54F7f9A22e0000CC2AB60031000000ae9fEF",
        "value": "0",
        "data": "<approve_router_operator_calldata>"
      },
      {
        "target": "0x006F54F7f9A22e0000CC2AB60031000000ae9fEF",
        "value": "0",
        "data": "<approve_auto_redeemer_operator_calldata>"
      }
    ]
    ```
  </Step>

  <Step title="Fetch the Nonce">
    Fetch a fresh `WALLET` nonce before signing the batch.

    ```bash theme={null}
    curl -G "https://relayer-v2.polymarket.com/v1/account/transactions/params" \
      -H "RELAYER_API_KEY: $RELAYER_API_KEY" \
      -H "RELAYER_API_KEY_ADDRESS: $RELAYER_API_KEY_ADDRESS" \
      --data-urlencode "address=$RELAYER_API_KEY_ADDRESS" \
      --data-urlencode "type=WALLET"
    ```

    The response includes the nonce to sign with the transaction.

    ```json theme={null}
    {
      "address": "<RELAYER_API_KEY_ADDRESS>",
      "nonce": "<wallet_nonce>"
    }
    ```
  </Step>

  <Step title="Submit the Transaction">
    Build and sign a Deposit Wallet `Batch` with the owner. Use the approval calls
    from the call-list step as `calls`.

    ```json EIP-712 Batch theme={null}
    {
      "domain": {
        "name": "DepositWallet",
        "version": "1",
        "chainId": 137,
        "verifyingContract": "<maker_address>"
      },
      "types": {
        "Call": [
          { "name": "target", "type": "address" },
          { "name": "value", "type": "uint256" },
          { "name": "data", "type": "bytes" }
        ],
        "Batch": [
          { "name": "wallet", "type": "address" },
          { "name": "nonce", "type": "uint256" },
          { "name": "deadline", "type": "uint256" },
          { "name": "calls", "type": "Call[]" }
        ]
      },
      "primaryType": "Batch",
      "message": {
        "wallet": "<maker_address>",
        "nonce": "<wallet_nonce>",
        "deadline": "<unix_seconds>",
        "calls": [
          {
            "target": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
            "value": "0",
            "data": "<approval_calldata>"
          }
        ]
      }
    }
    ```

    Submit the signed batch to the relayer.

    ```bash theme={null}
    curl -X POST "https://relayer-v2.polymarket.com/submit" \
      -H "Content-Type: application/json" \
      -H "RELAYER_API_KEY: $RELAYER_API_KEY" \
      -H "RELAYER_API_KEY_ADDRESS: $RELAYER_API_KEY_ADDRESS" \
      -d '{
        "type": "WALLET",
        "from": "<relayer_api_key_address>",
        "to": "0x00000000000Fb5C9ADea0298D729A0CB3823Cc07",
        "nonce": "<wallet_nonce>",
        "signature": "<wallet_batch_signature>",
        "metadata": "Approve Combo RFQ contracts",
        "depositWalletParams": {
          "depositWallet": "<maker_address>",
          "deadline": "<unix_seconds>",
          "calls": [
            {
              "target": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
              "value": "0",
              "data": "<approval_calldata>"
            }
          ]
        }
      }'
    ```

    The response includes the relayer transaction ID.

    ```json theme={null}
    {
      "transactionID": "<transaction_id>",
      "state": "STATE_NEW"
    }
    ```
  </Step>

  <Step title="Poll the Transaction">
    Poll the relayer transaction until it reaches `STATE_CONFIRMED` before posting
    quotes that rely on those approvals.

    ```bash theme={null}
    curl "https://relayer-v2.polymarket.com/v1/account/transactions/<transaction_id>" \
      -H "RELAYER_API_KEY: $RELAYER_API_KEY" \
      -H "RELAYER_API_KEY_ADDRESS: $RELAYER_API_KEY_ADDRESS"
    ```

    ```json theme={null}
    {
      "transaction_id": "<transaction_id>",
      "transaction_hash": "<transaction_hash>",
      "state": "STATE_CONFIRMED",
      "error_msg": null
    }
    ```

    Treat `STATE_FAILED` and `STATE_INVALID` as terminal failures.
  </Step>
</Steps>
```

Example 4 (text):
```text
flowchart TD
    A[Receive request] --> B[Send quote]
    B --> C[Active quote]
    C --> D[Canceled]
    C --> E[Selected]
    E --> F{Last Look?}
    F -->|No| G[Execution]

    subgraph lastLook["Last Look"]
        F -->|Yes| H[Review fill]
        H --> I[Confirm]
        H --> J[Decline]
        H --> K[Timeout]
    end

    I --> G
    G --> L[Confirmed]
    G --> M[Failed]

    style lastLook fill:#165DFC14,stroke:#165DFC66,stroke-width:1px
```

---

## Margin

**URL:** https://docs.polymarket.com/perps/learn-about-trading/margin.md

**Contents:**
- Equity
  - Unrealized PnL
- Margin Requirements
- Default Leverage and Margin Mode
- Margin States
- Margin Checks
  - Pre-Trade
  - Continuous Monitoring
- Deposits and Withdrawals
  - Withdrawal Margin Requirements

Margin is the collateral required to open and maintain leveraged positions. It ensures traders have enough collateral to cover potential losses and gives the system a buffer to close positions before they become insolvent.

Trading uses two thresholds. **Initial margin (IM)** is the collateral required to open or increase a position. **Maintenance margin (MM)** is the minimum collateral required to keep a position open. When equity drops below maintenance margin, the position is [liquidated](/perps/learn-about-trading/liquidation-mechanics).

Equity is the real-time value of an account, incorporating all open positions at current Mark Price.

Because equity depends on Mark Price, equity follows live mark updates. See [Mark Price](/perps/learn-about-trading/mark-price).

Initial margin is set by your configured leverage:

Leverage tiers cap the leverage available as your position grows — larger positions must run at lower leverage and therefore post proportionally more initial margin. The cap is enforced against your worst-case position notional (position plus resting orders on the heavier side): an order that would grow it into a tier whose `max*leverage` is below your configured leverage is rejected with `invalid*leverage`, and you must lower your leverage setting first. Your configured leverage applies to your entire notional, not bracket by bracket. Fetch each market's tier schedule from [Market Data](/perps/market-data#fetch-instruments).

Maintenance margin uses a flat per-market rate, independent of position size, tier, and your leverage setting:

`MaxLeverage` is the market's maximum leverage, so on a 20x market `MMR = 2.5%` for every position. MM equals half the initial margin of a position opened at max leverage; at lower leverage your IM is higher but MM stays the same, so the gap between entry requirement and liquidation grows.

Margin requirements are static across sessions.

Every position uses one of two margin modes. **Cross margin** backs the position with the account's shared free collateral. **Isolated margin** backs the position only with the collateral allocated to it.

The exchange may assign your account to a group with shared leverage or margin defaults. Each setting resolves independently for each instrument:

| Priority | Leverage                                                       | Margin Mode                                                                           | | -------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------- | | 1        | Your explicit per-instrument setting                           | Your explicit per-instrument setting                                                  | | 2        | Your account group's default, capped at the instrument maximum | Your account group's default; cross resolves to isolated on isolated-only instruments | | 3        | The instrument's maximum leverage                              | Isolated margin                                                                       |

Group defaults also apply to future listings. An explicit per-instrument setting is retained when group defaults or membership change.

Set your preferred leverage and margin mode after the instrument is listed and before placing your first order, using [Update Leverage](/perps/trading#update-leverage). Account configuration reads report the resolved values; an update sets both values explicitly. Setting the current resolved pair explicitly preserves it against later group changes.

Before switching between isolated and cross margin:

Leverage changes within the same mode still require sufficient margin and a positive leverage no greater than the instrument maximum. If the account is subscribed to the Backstop Liquidity Provider program for that instrument, unsubscribe before updating either setting, even to re-submit the current pair.

An account is always in one of three states.

| State       | Condition           | What Happens                                   | | ----------- | ------------------- | ---------------------------------------------- | | Healthy     | `Equity >= IM`      | Normal trading                                 | | Margin call | `MM <= Equity < IM` | Can only reduce exposure or deposit collateral | | Liquidation | `Equity < MM`       | The system begins closing the position         |

Before any order executes, the system verifies the account can afford it:

This prevents accounts from entering a margin-call state through new trades.

The system continuously evaluates accounts:

Deposits increase equity. A deposit during margin call can restore the account to healthy status immediately.

Withdrawals must leave enough collateral to cover existing margin commitments and at least **10% of the total notional value of all open positions**:

`TotalPositionValue` includes both cross and isolated positions at current Mark Price. `CollateralReserved` covers cross-position initial margin, isolated collateral allocations, and margin and fee reserves for accepted open orders. For a cross-only account with no open orders, it equals required initial margin.

The 10% floor applies to withdrawals, independently of the leverage used to open a position. It does not increase the opening-margin requirement or change the maintenance-margin threshold for liquidation.

For example, assume a \$100 position at 20x, no other positions or orders, and no fees, funding, or unrealized PnL:

With \$20 of collateral, \$10 is available for withdrawal. With only \$5 of collateral, the position can open, but nothing is available for withdrawal. In this example, the floor is stricter than initial margin above 10x leverage; at 10x or below, initial margin already covers the floor.

<Accordion title="How is the withdrawable balance calculated?"> The account's withdrawal capacity in USD is:

`CollateralValue` is the account's valued collateral. `CrossUnrealizedPnL` includes only cross positions; isolated unrealized PnL is not added to withdrawal equity. `PendingOrderMargin` is the additional initial margin reserved for orders still awaiting risk checks.

Use the returned `withdrawable` value from [Get Portfolio](/api-reference/get-portfolio) rather than subtracting initial margin from account equity. A withdrawal is also limited by the balance of the asset being withdrawn and is checked again when processed. </Accordion>

For each position, `initial_margin` reports the collateral currently backing the position. For cross positions, it is the required initial margin based on position size, Mark Price, the applicable risk tier, and configured leverage. For isolated positions, it is the position's current equity:

The isolated value is a point-in-time snapshot that changes with Mark Price and funding. The legacy `initial_margin` name is retained for API compatibility; `margin` would describe this value more accurately.

A positive margin adjustment moves free account collateral into the isolated allocation. A negative adjustment releases value back to free collateral and may include unrealized profit, so the signed allocation itself can reach zero or become negative. The request is accepted only when the resulting position equity remains at or above current required initial margin.

Removing isolated margin releases collateral within the account. This uses the position's initial-margin check above; withdrawing the released collateral from the account must also satisfy the [withdrawal margin requirements](#withdrawal-margin-requirements).

Both additions and removals are blocked while the account is in cross liquidation or the target position is in isolated liquidation. An isolated liquidation on a different instrument does not block the request. Cancel-only mode does not gate margin adjustments.

**Examples:**

Example 1 (text):
```text
Equity = Collateral + UnrealizedPnL(Mark) - FeesDue - FundingDue
```

Example 2 (text):
```text
Long PnL = PositionSize * (Mark - EntryPrice)
Short PnL = PositionSize * (EntryPrice - Mark)
```

Example 3 (text):
```text
IM = Notional / Leverage
```

Example 4 (text):
```text
MM = Notional × MMR        where MMR = 0.5 / MaxLeverage
```

---

## Deposit

**URL:** https://docs.polymarket.com/trading/bridge/deposit.md

**Contents:**
- How It Works
- Create Bridge Addresses
  - Address Types
- Deposit Flow
- USDC vs pUSD
- Large Deposits
- Minimum Deposits
- Deposit Recovery
- Next Steps

Polymarket uses **pUSD** (Polymarket USD) on Polygon as collateral for all trading. The Bridge API lets you deposit assets from Ethereum, Solana, Bitcoin, and other chains—they're automatically converted to pUSD on Polygon.

Generate unique bridge addresses linked to your Polymarket wallet. See [Create bridge addresses](/api-reference/bridge/create-bridge-addresses) for the full request and response schemas.

<Tip> **Builders: attach your code.** If you route user funds through this endpoint, pass your builder code via the optional `X-Builder-Code` header (bytes32 hex; `0x` + 64 hex chars). It lets our bridge provider attribute traffic to your app, so stuck or delayed transfers can be traced and prioritized. The header is optional. Requests without it still succeed but return a `missing*builder*code` warning, and a malformed code returns `400`. Get your code at [Settings → Builder](https://polymarket.com/settings?tab=builder). </Tip>

The response returns one bridge address per address type (`evm`, `svm`, `btc`, `tron`). Send from the matching source chain to the matching address.

| Address | Use For                                                  | | ------- | -------------------------------------------------------- | | `evm`   | Ethereum, Arbitrum, Base, Optimism, and other EVM chains | | `svm`   | Solana                                                   | | `btc`   | Bitcoin                                                  | | `tron`  | Tron                                                     |

<Warning> Each address is unique to your wallet. Only send assets from supported chains to the correct address type. </Warning>

<Steps> <Step title="Get Your Bridge Address"> Call `POST /deposit` with your Polymarket wallet address to get bridge addresses. </Step>

<Step title="Check Supported Assets"> Verify your token is supported and meets the minimum deposit amount via `/supported-assets`. </Step>

<Step title="Send Assets"> Transfer tokens to the appropriate bridge address from your source chain. </Step>

<Step title="Track Status"> Monitor your deposit progress using `/status/{address}`. </Step> </Steps>

You can deposit either USDC (native) or USDC.e (bridged) as the source asset to your Polymarket wallet. Either way, the incoming USDC or USDC.e is wrapped into pUSD via the Collateral Onramp, and pUSD is what you hold and trade with on Polymarket.

For deposits over \$50,000 originating from a chain other than Polygon, we recommend using a third-party bridge to minimize slippage:

Bridge directly to your Polymarket USDC (Polygon) bridge address. Polymarket is not affiliated with or responsible for any third-party bridge.

Each asset has a minimum deposit amount. Deposits below the minimum will not be processed. Check `/supported-assets` for current minimums.

If you deposited the wrong token, use this tool to recover your funds:

[recovery.polymarket.com](https://recovery.polymarket.com/)

<Warning> Sending unsupported tokens may cause **irrecoverable loss**. Always verify your token is listed in [Supported Assets](/trading/bridge/supported-assets) before depositing. </Warning>

<CardGroup cols={2}> <Card title="Supported Assets" icon="coins" href="/trading/bridge/supported-assets"> See all supported chains and tokens with minimum amounts. </Card>

<Card title="Check Status" icon="clock" href="/trading/bridge/status"> Track your deposit progress through completion. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
curl -X POST https://bridge.polymarket.com/deposit \
  -H "Content-Type: application/json" \
  -H "X-Builder-Code: <builder_code>" \
  -d '{"address": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"}'
```

---

## Wallet Activity

**URL:** https://docs.polymarket.com/trading/wallet-activity.md

**Contents:**
- Open Positions
- Closed Positions
- Activity History
- Notifications
  - List Notifications
  - Drop Notifications
- Portfolio Value
- Wallet Stats
- Wallet PnL History
- Wallet Trading Volume

Use a wallet address to understand an account's current exposure and trace how its activity has changed over time.

Inspect a wallet's current outcome exposure and unrealized performance.

<Tabs> <Tab title="TypeScript"> Call `listPositions()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `list_positions()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> List the open positions for a wallet:

Review the positions a wallet has exited or that have resolved, including their realized performance.

<Tabs> <Tab title="TypeScript"> One method serves the whole position lifecycle: call `listPositions()` with `status: PositionStatus.Closed`. Closed rows keep the same `Position` shape with realized economics (`currentSize` is a \~0 residual and `realizedPnl` carries the outcome); they default to sorting by realized PnL.

<Tab title="Python"> Call `list_positions()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Closed positions are served by the same route behind the `status` filter:

Follow the timeline for a wallet across trades and other activity.

<Tabs> <Tab title="TypeScript"> Call `listActivity()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `list_activity()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> List the activity for a wallet:

Notifications provide a short-lived record of unread events for the connected account. The CLOB retains them for 48 hours.

<Note> Clients authenticated with [Session Keys](/trading/session-keys#session-key-considerations) receive only notifications generated by those Session Keys. </Note>

<Tabs> <Tab title="TypeScript"> Call `fetchNotifications()` on a `SecureClient`:

<Tab title="Python"> Call `get_notifications()` on an `AsyncSecureClient`. The synchronous `SecureClient` provides the same method:

<Tab title="API"> List unread notifications for the account:

Mark notifications as read after processing them. Dropped notifications no longer appear when you list unread notifications.

<Tabs> <Tab title="TypeScript"> Call `dropNotifications()` on a `SecureClient` with the notification IDs:

<Tab title="Python"> Call `drop_notifications()` on an `AsyncSecureClient`. The synchronous `SecureClient` provides the same method:

<Tab title="API"> Send the notification IDs as a comma-separated list:

Read the current portfolio value for a wallet.

<Tabs> <Tab title="TypeScript"> Call `fetchPortfolioValue()` on a `PublicClient` or `SecureClient`. It returns a single object: the wallet's marked portfolio value in USDC, rounded to four decimals.

<Tab title="Python"> Call `get*portfolio*value()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Fetch the portfolio value for a wallet:

Read a wallet's lifetime trading statistics.

<Tabs> <Tab title="TypeScript"> Call `fetchUserStats()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `get*user*stats()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Fetch the wallet's profile statistics:

Track a wallet's cumulative profit and loss over time.

<Tabs> <Tab title="TypeScript"> Call `fetchUserPnl()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `get*user*pnl()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Fetch the last day's cumulative PnL observations:

Measure a wallet's trading volume over a selected period.

<Tabs> <Tab title="TypeScript"> Call `fetchUserVolume()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `get*user*volume()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Fetch trading volume from the start of September:

**Examples:**

Example 1 (text):
```text
    const address = "0x8ba1f109551bD432803012645Ac136ddd64DBA72";

    const pages = client.listPositions({ user: address, pageSize: 1 });

    for await (const page of pages) {
      // page.items: Position[]
    }
```

Example 2 (text):
```text
<Accordion title="Output: Position[]">
  <CodeGroup>
    ```ts Position Type theme={null}
    // Trimmed for brevity.
    type Position = {
      wallet: EvmAddress;
      assetId: TokenId | PositionId;
      conditionId: ConditionId;
      /** The current holding, in shares. */
      currentSize: DecimalString;
      avgPrice: DecimalString;
      /** Fee-exclusive entry basis in USD. */
      entryCostUsdc: DecimalString;
      /** Attributed BUY fees in USD (disclosure; already excluded from entryCostUsdc). */
      entryFeesUsdc: DecimalString;
      /** Always entryCostUsdc + entryFeesUsdc. */
      totalCostUsdc: DecimalString;
      currentPrice: DecimalString;
      currentValue: DecimalString;
      realizedPnl: DecimalString;
      /** currentValue - entryCostUsdc. */
      unrealizedPnl: DecimalString;
      /** Always realizedPnl + unrealizedPnl. */
      totalPnl: DecimalString;
      percentPnl: DecimalString;
      status: PositionStatus;
      redeemable: boolean;
      mergeable: boolean;
      negativeRisk: boolean;
      title?: string;
      slug?: string;
      eventSlug?: string;
      outcome?: string;
      outcomeIndex?: number;
      endDate?: IsoCalendarDateString;
      lastEventAt?: EpochMilliseconds;
    };
    ```

    ```json Position Example theme={null}
    [
      {
        "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "wallet": "0x8ba1f109551bd432803012645ac136ddd64dba72",
        "assetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "currentSize": "125.5",
        "avgPrice": "0.42",
        "entryCostUsdc": "52.71",
        "entryFeesUsdc": "0",
        "totalCostUsdc": "52.71",
        "currentPrice": "0.49",
        "currentValue": "61.495",
        "realizedPnl": "0",
        "unrealizedPnl": "8.785",
        "totalPnl": "8.785",
        "percentPnl": "16.66",
        "status": "OPEN",
        "redeemable": false,
        "mergeable": false,
        "negativeRisk": false,
        "title": "Will the US confirm that aliens exist before 2027?",
        "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
        "eventSlug": "will-the-us-confirm-that-aliens-exist-before-2027",
        "outcome": "Yes",
        "outcomeIndex": 0
      }
    ]
    ```
  </CodeGroup>
</Accordion>
```

Example 3 (text):
```text
    address = "0x8ba1f109551bD432803012645Ac136ddd64DBA72"

    pages = client.list_positions(
        user=address,
        page_size=1,
    )

    async for page in pages:
        # page.items: tuple[Position, ...]
        pass
```

Example 4 (text):
```text
<Accordion title="Output: Position">
  <CodeGroup>
    ```python Position Type theme={null}
    class Position:
        wallet: EvmAddress
        asset_id: ClobAssetId
        condition_id: ConditionId
        current_size: Decimal
        avg_price: Decimal
        entry_cost_usdc: Decimal
        entry_fees_usdc: Decimal
        total_cost_usdc: Decimal
        current_price: Decimal
        current_value: Decimal
        total_size: Decimal
        realized_pnl: Decimal
        unrealized_pnl: Decimal
        total_pnl: Decimal
        percent_pnl: Decimal
        percent_realized_pnl: Decimal
        status: PositionStatus
        redeemable: bool
        mergeable: bool
        negative_risk: bool
        archived: bool
        verified: bool
        title: str | None
        slug: str | None
        icon: str | None
        event_slug: str | None
        outcome: str | None
        opposite_outcome: str | None
        name: str | None
        profile_image: str | None
        event_id: EventId | None
        outcome_index: int | None
        opposite_asset_id: ClobAssetId | None
        end_date: date | None
        last_event_at: datetime | None
    ```

    ```json Position Example theme={null}
    {
      "wallet": "0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b",
      "asset_id": "94476829201604408463453426454480212459887267917122244941405244686637914508323",
      "condition_id": "0x7ad403c3508f8e3912940fd1a913f227591145ca0614074208e0b962d5fcc422",
      "current_size": "400000.0",
      "avg_price": "0.5",
      "entry_cost_usdc": "200000.0",
      "entry_fees_usdc": "0.0",
      "total_cost_usdc": "200000.0",
      "current_price": "0.7545",
      "current_value": "301800.0",
      "total_size": "10386654.0",
      "realized_pnl": "0.0",
      "unrealized_pnl": "101800.0",
      "total_pnl": "101800.0",
      "percent_pnl": "50.9",
      "percent_realized_pnl": "-94.1886",
      "status": "OPEN",
      "redeemable": false,
      "mergeable": true,
      "negative_risk": true,
      "archived": false,
      "verified": true,
      "title": "Will JD Vance win the 2028 US Presidential Election?",
      "slug": "will-jd-vance-win-the-2028-us-presidential-election",
      "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/will-jd-vance-win-the-2028-us-presidential-election-P-zEgXjCWbdY.png",
      "event_slug": "presidential-election-winner-2028",
      "outcome": "No",
      "opposite_outcome": "Yes",
      "name": "Car",
      "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/profile-image-501613-aa434e55-7732-41b1-9650-83a9d1d716ef.png",
      "event_id": "31552",
      "outcome_index": 1,
      "opposite_asset_id": "16040015440196279900485035793550429453516625694844857319147506590755961451627",
      "end_date": "2028-11-07",
      "last_event_at": "2026-08-23T15:46:10Z"
    }
    ```
  </CodeGroup>
</Accordion>

`current_size` is in shares. Costs, values, and PnL use `Decimal` values in USDC. `entry_cost_usdc` excludes fees. Do not subtract `entry_fees_usdc` from it again.

Position reads have no time bounds by default. `full_history=True` preserves that behavior, including holdings without activity timestamps. Use `start` and `end` to filter by last activity instead.
```

---

## Manage Orders

**URL:** https://docs.polymarket.com/trading/manage-orders.md

**Contents:**
- Fetch an Order
- List Open Orders
- List Account Trades
- List Builder Trades
- Cancel Orders
  - Cancel Orders by ID
  - Cancel Market Orders
  - Cancel All Orders
  - Cancellation Results
- Order Heartbeats

After submitting an order, use authenticated account reads to check its current state, reconcile open orders and resulting trades, and cancel liquidity you no longer want resting on the book.

<Note> Clients authenticated with [Session Keys](/trading/session-keys#session-key-considerations) can only fetch orders and trades associated with those Session Keys. **Deposit Wallet Owners** cannot fetch orders from authorized Session Keys. </Note>

Look up a single order by its ID. Use this to check the current status of an order you already know about, rather than scanning the full list of open orders.

<Tabs> <Tab title="TypeScript"> Call `fetchOrder()` on a `SecureClient` to fetch an order by ID:

<Tab title="Python"> Call `get_order()` on an `AsyncSecureClient` to fetch an order by ID. The synchronous `SecureClient` provides the same method.

<Tab title="API"> Fetch the order with an authenticated CLOB request. See [API Authentication](/getting-started/api#authentication) for the complete signing flow.

See the [order response reference](/api-reference/trade/get-single-order-by-id) for quantity units and statuses.

Retrieve every resting order on the account, optionally narrowed to one token or market. Filtering by a specific order ID can also return a canceled or fully matched order.

<Tabs> <Tab title="TypeScript"> Call `listOpenOrders()` on a `SecureClient` to iterate over the account's open orders:

<Tab title="Python"> Call `list*open*orders()` on an `AsyncSecureClient` to iterate over the account's open orders. The synchronous `SecureClient` provides the same method.

<Tab title="API"> List open orders with an authenticated CLOB request, optionally filtering by `id`, `market`, or `asset_id`. See [API Authentication](/getting-started/api#authentication) for the complete signing flow.

See the [order response reference](/api-reference/trade/get-single-order-by-id) for quantity units and statuses.

Retrieve executed fills for the account, as opposed to orders that are still resting on the book. Use this to reconstruct fill history, compute realized position size, or audit what actually matched.

<Tabs> <Tab title="TypeScript"> Call `listAccountTrades()` on a `SecureClient` to iterate over the account's trades:

<Tab title="Python"> Call `list*account*trades()` on an `AsyncSecureClient` to iterate over the account's trades. The synchronous `SecureClient` provides the same method.

<Tab title="API"> List account trades with an authenticated CLOB request, optionally filtering by `id`, `market`, `asset*id`, `maker*address`, `after`, or `before`. See [API Authentication](/getting-started/api#authentication) for the complete signing flow.

See [Trade Statuses](/concepts/order-lifecycle#trade-statuses) to follow each trade's `status` through settlement.

Retrieve matched trades attributed to a builder code across the accounts your application serves. Use this instead of an account trade read when you need to reconcile fills or measure activity for the builder integration as a whole. Orders do not appear here until they match.

<Tabs> <Tab title="TypeScript"> Call `listBuilderTrades()` on a `PublicClient` or `SecureClient` to iterate over trades attributed to your builder code:

<Tab title="Python"> Call `list*builder*trades()` on an `AsyncPublicClient` or `AsyncSecureClient` to iterate over trades attributed to your builder code. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> List trades attributed to a builder code with a public CLOB request. Filter the results with `id`, `market`, `asset_id`, `after`, or `before` when needed:

See [Builder Programs](/programs/builders/overview) to learn how attribution works.

Cancel only as broadly as needed. Start with known order IDs, use a market or token filter when withdrawing a set of quotes, and reserve account-wide cancellation for exceptional situations. Cancellation remains available while the exchange is in cancel-only mode, when new orders are rejected. For a partially filled order, cancellation removes only its unfilled remainder, including when the market resolves. It preserves the original and matched sizes and does not undo settled fills.

Cancel one order when you know its ID. To cancel a known set of orders in one request, submit a batch of up to 3,000 IDs. Duplicate IDs in the batch are ignored.

<Tabs> <Tab title="TypeScript"> Call `cancelOrder()` on a `SecureClient` to cancel one order:

<Tab title="Python"> Call `cancel_order()` on an `AsyncSecureClient` to cancel one order. The synchronous `SecureClient` provides the same method without `await`.

<Tab title="API"> Cancel one order with an authenticated CLOB request. See [API Authentication](/getting-started/api#authentication) for the complete signing flow.

Cancel by token to withdraw orders for one outcome, or by market to withdraw orders for every outcome in the condition. At least one filter is required.

<Tabs> <Tab title="TypeScript"> Call `cancelMarketOrders()` on a `SecureClient` with a token ID or condition ID:

<Tab title="Python"> Call `cancel*market*orders()` on an `AsyncSecureClient` with a token ID or condition ID. The synchronous `SecureClient` provides the same method without `await`.

<Tab title="API"> Cancel every open order for one outcome with an authenticated CLOB request. See [API Authentication](/getting-started/api#authentication) for the complete signing flow.

Use account-wide cancellation when you need to remove every resting order, such as during an emergency shutdown.

<Warning> This action cancels every open order associated with the authenticated CLOB API credentials. </Warning>

<Tabs> <Tab title="TypeScript"> Call `cancelAll()` on a `SecureClient`:

<Tab title="Python"> Call `cancel_all()` on an `AsyncSecureClient`. The synchronous `SecureClient` provides the same method without `await`.

<Tab title="API"> Cancel every open order with an authenticated CLOB request. See [API Authentication](/getting-started/api#authentication) for the complete signing flow.

A cancellation can succeed for only some of the requested orders. Reconcile the result before retrying: it identifies the orders that were canceled and gives a reason for each order that could not be canceled.

<Tabs> <Tab title="TypeScript"> The TypeScript SDK returns a `CancelOrdersResponse`:

<Tab title="Python"> The Python SDK returns a `CancelOrdersResponse`:

<Tab title="API"> The API returns the cancellation result as JSON. This response shows one canceled order and one order that had already matched:

Use order heartbeats to cancel resting orders automatically if your trading process stops responding. Once the first heartbeat is accepted, the CLOB expects the account to keep sending them; if a valid heartbeat is not received within 10 seconds, all open orders owned by those CLOB API credentials are canceled. The cancellation check runs every five seconds, so cancellation may occur up to five seconds after the timeout.

<Tabs> <Tab title="API"> Send a heartbeat every **5 seconds**.

<Tab title="TypeScript">Content coming soon.</Tab> <Tab title="Python">Content coming soon.</Tab> </Tabs>

Closed-only mode is an account-level circuit breaker for a market. When it's on, the account can only place orders that reduce an existing position, not new opening orders. Check this before placing an order if you want to fail fast instead of waiting for a rejection.

<Tabs> <Tab title="TypeScript"> Call `fetchClosedOnlyMode()` on a `SecureClient`:

<Tab title="Python"> Call `get*closed*only_mode()` on an `AsyncSecureClient`. The synchronous `SecureClient` provides the same method.

<Tab title="API"> Read the account's closed-only state:

An order scores when it is live on a market with [liquidity rewards](/programs/liquidity-rewards) and meets the market's minimum qualifying size, maximum qualifying spread, and required live duration. Because eligibility changes as the order book moves, treat the result as a point-in-time check.

<Tabs> <Tab title="TypeScript"> Call `fetchOrderScoring()` on a `SecureClient` with the order ID:

<Tab title="Python"> Call `get*order*scoring()` on an `AsyncSecureClient` with the order ID. The synchronous `SecureClient` provides the same method.

<Tab title="API"> Check whether an order currently qualifies for rewards:

**Examples:**

Example 1 (text):
```text
    const order = await client.fetchOrder({ orderId: "ORDER_ID" });

    // order: OpenOrder
```

Example 2 (text):
```text
The method returns an `OpenOrder` with normalized token, decimal, and date
values:

<CodeGroup>
  ```ts OpenOrder Type theme={null}
  type OpenOrder = {
    id: string;
    conditionId: CtfConditionId;
    tokenId: TokenId;
    owner: string;
    makerAddress: string;
    side: string;
    price: DecimalString;
    originalSize: DecimalString;
    sizeMatched: DecimalString;
    outcome: string;
    orderType: string;
    status: string;
    associateTrades: string[];
    createdAt: IsoDateTimeString;
    expiresAt?: IsoDateTimeString;
  };
  ```

  ```json OpenOrder Example theme={null}
  {
    "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
    "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
    "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
    "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
    "makerAddress": "0x1234567890123456789012345678901234567890",
    "side": "BUY",
    "price": "0.52",
    "originalSize": "10",
    "sizeMatched": "0",
    "outcome": "Yes",
    "orderType": "GTD",
    "status": "LIVE",
    "associateTrades": [],
    "createdAt": "2026-06-01T12:00:00.000Z",
    "expiresAt": "2026-06-01T13:00:00.000Z"
  }
  ```
</CodeGroup>

`expiresAt` is present when the response includes an expiration; otherwise,
the field is omitted.
```

Example 3 (text):
```text
    order = await client.get_order(order_id="ORDER_ID")

    # order: OpenOrder
```

Example 4 (text):
```text
The method returns an `OpenOrder` with normalized token, decimal, and date
values:

<CodeGroup>
  ```python OpenOrder Type theme={null}
  class OpenOrder:
      id: str
      condition_id: CtfConditionId
      token_id: TokenId
      owner: str
      maker_address: str
      side: Literal["BUY", "SELL"]
      price: Decimal
      original_size: Decimal
      size_matched: Decimal
      outcome: str
      order_type: str
      status: str
      associate_trades: tuple[str, ...]
      created_at: datetime
      expires_at: datetime | None
  ```

  ```json OpenOrder Example theme={null}
  {
    "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
    "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
    "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
    "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
    "maker_address": "0x1234567890123456789012345678901234567890",
    "side": "BUY",
    "price": "0.52",
    "original_size": "10",
    "size_matched": "0",
    "outcome": "Yes",
    "order_type": "GTD",
    "status": "LIVE",
    "associate_trades": [],
    "created_at": "2026-06-01T12:00:00Z",
    "expires_at": "2026-06-01T13:00:00Z"
  }
  ```
</CodeGroup>

`expires_at` contains the normalized expiration when one is returned and
can otherwise be `None`.
```

---

## Quote

**URL:** https://docs.polymarket.com/trading/bridge/quote.md

**Contents:**
- Get a Quote
  - Request Parameters
  - Response
  - Fee Breakdown
- Next Steps

Get an estimated quote before executing a deposit or withdrawal. Quotes include estimated output amounts, checkout time, and a detailed fee breakdown.

| Parameter            | Type   | Description                                                   | | -------------------- | ------ | ------------------------------------------------------------- | | `fromAmountBaseUnit` | string | Amount to send in base units (e.g., `"10000000"` for 10 USDC) | | `fromChainId`        | string | Source chain ID (e.g., `"137"` for Polygon)                   | | `fromTokenAddress`   | string | Token contract address on the source chain                    | | `recipientAddress`   | string | Destination wallet address to receive funds                   | | `toChainId`          | string | Destination chain ID                                          | | `toTokenAddress`     | string | Token contract address on the destination chain               |

The quote response includes an estimated output amount, a fee breakdown, and a `quoteId` you can log for your own records. To track the transfer itself once it's underway, poll [`/status`](/trading/bridge/status) with your bridge address.

| Field                | Type   | Description                             | | -------------------- | ------ | --------------------------------------- | | `estCheckoutTimeMs`  | number | Estimated checkout time in milliseconds | | `estInputUsd`        | number | Estimated input value in USD            | | `estOutputUsd`       | number | Estimated output value in USD           | | `estToTokenBaseUnit` | string | Estimated output amount in base units   | | `quoteId`            | string | Unique identifier for this quote        | | `estFeeBreakdown`    | object | Detailed fee breakdown (see below)      |

The `estFeeBreakdown` object contains:

<ResponseField name="gasUsd" type="number"> Gas fee in USD </ResponseField>

<ResponseField name="appFeeLabel" type="string"> Label of the app fee </ResponseField>

<ResponseField name="appFeePercent" type="number"> App fee as a percentage of the total amount </ResponseField>

<ResponseField name="appFeeUsd" type="number"> App fee in USD </ResponseField>

<ResponseField name="fillCostPercent" type="number"> Fill cost as a percentage of the total amount </ResponseField>

<ResponseField name="fillCostUsd" type="number"> Fill cost in USD </ResponseField>

<ResponseField name="maxSlippage" type="number"> Maximum potential slippage as a percentage </ResponseField>

<ResponseField name="minReceived" type="number"> Minimum amount received after slippage </ResponseField>

<ResponseField name="swapImpact" type="number"> Swap impact as a percentage of the total amount </ResponseField>

<ResponseField name="swapImpactUsd" type="number"> Swap impact in USD </ResponseField>

<ResponseField name="totalImpact" type="number"> Total impact as a percentage of the total amount </ResponseField>

<ResponseField name="totalImpactUsd" type="number"> Total impact cost in USD </ResponseField>

<Note> Quotes are estimates. Actual amounts may vary slightly due to market conditions. </Note>

<CardGroup cols={2}> <Card title="Create Deposit" icon="arrow-right-to-bracket" href="/trading/bridge/deposit"> Execute a deposit to Polymarket. </Card>

<Card title="Withdraw" icon="arrow-right-from-bracket" href="/trading/bridge/withdraw"> Withdraw from Polymarket to another chain. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
curl -X POST https://bridge.polymarket.com/quote \
  -H "Content-Type: application/json" \
  -d '{
    "fromAmountBaseUnit": "10000000",
    "fromChainId": "137",
    "fromTokenAddress": "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
    "recipientAddress": "0x17eC161f126e82A8ba337f4022d574DBEaFef575",
    "toChainId": "137",
    "toTokenAddress": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"
  }'
```

Example 2 (text):
```text
{
  "estCheckoutTimeMs": 45000,
  "estInputUsd": 10,
  "estOutputUsd": 9.94,
  "estToTokenBaseUnit": "9940000",
  "quoteId": "0x00c34ba467184b0146406d62b0e60aaa24ed52460bd456222b6155a0d9de0ad5",
  "estFeeBreakdown": {
    "gasUsd": 0.02,
    "appFeeLabel": "Bridge fee",
    "appFeePercent": 0.3,
    "appFeeUsd": 0.03,
    "fillCostPercent": 0.1,
    "fillCostUsd": 0.01,
    "maxSlippage": 0.5,
    "minReceived": 9.89,
    "swapImpact": 0.05,
    "swapImpactUsd": 0.005,
    "totalImpact": 0.6,
    "totalImpactUsd": 0.06
  }
}
```

---

## Trading

**URL:** https://docs.polymarket.com/perps/trading.md

**Contents:**
- Start an Authenticated Session
- Prepare a Trade
- Choose Direction and Size
- Place Orders
- Take Profit & Stop Loss
  - How Triggers Work
  - Market and Limit Closes
  - Place a Bracket Order
  - Protect an Existing Position
  - Update or Cancel TP/SL

<Note> Trading workflows require an [authenticated session](/perps/authenticated-sessions). </Note>

Perps trading changes account exposure on an instrument. An order expresses what the account wants to do, but exposure only changes when the order fills.

An accepted order can rest on the book before it fills.

Use order state to track accepted, resting, modified, canceled, or rejected orders. Use fills and portfolio state to confirm any exposure change.

Open an authenticated session before reading private account state or submitting trading commands. See [Authenticated Sessions](/perps/authenticated-sessions) for the full setup flow.

<Tabs> <Tab title="TypeScript"> Create a `SecureClient`.

<Tab title="Python"> Create an `AsyncSecureClient`.

<Tab title="API"> Use proxy credentials for private reads and signed trading commands.

Start by identifying the Perps instrument you want to trade. Instruments define the market and include the constraints used later when building an order.

<Tabs> <Tab title="TypeScript"> Fetch instruments and select the market you want to trade.

<Tab title="Python"> Fetch instruments and select the market you want to trade.

<Tab title="API"> Fetch instruments and select the market you want to trade.

Before placing an order, decide whether it should open new exposure, increase existing exposure, reduce exposure, or close the position.

The effect of a buy or sell depends on the current position.

| Current position | Buy order               | Sell order             | | ---------------- | ----------------------- | ---------------------- | | No position      | Opens long              | Opens short            | | Long             | Increases long          | Reduces or closes long | | Short            | Reduces or closes short | Increases short        |

To close a position, submit an order in the opposite direction for the current open position size.

<Tabs> <Tab title="TypeScript"> Read the portfolio when the order decision depends on current exposure.

<Tab title="Python"> Read the portfolio when the order decision depends on current exposure.

<Tab title="API"> Read the portfolio when the order decision depends on current exposure.

Place an order when the account is ready to express buy or sell intent. Use an explicit limit price when you need price protection. Use immediate-or-cancel execution when the order should fill immediately or cancel any unfilled quantity.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Choose a Price"> Fetch a ticker when you need a lightweight current-price reference. Fetch the book when the order price depends on spread, depth, or top-of-book liquidity.

<Tab title="Python"> <Steps> <Step title="Choose a Price"> Fetch a ticker when you need a lightweight current-price reference. Fetch the book when the order price depends on spread, depth, or top-of-book liquidity.

<Tab title="API"> <Steps> <Step title="Choose a Price"> Fetch current market data when the order price depends on live prices or available liquidity.

Use take-profit and stop-loss (TP/SL) orders to place conditional exits for a position. A take-profit order exits when price moves in your favor. A stop-loss order exits when price moves against you.

TP/SL orders watch the mark price, not the last traded price. A trigger fires when the mark price touches the trigger price, then submits a reduce-only order to close exposure.

| Position | Take-profit fires when | Stop-loss fires when  | | -------- | ---------------------- | --------------------- | | Long     | Mark rises to trigger  | Mark falls to trigger | | Short    | Mark falls to trigger  | Mark rises to trigger |

For a long position, take-profit triggers usually sit above the current mark and stop-loss triggers usually sit below it. For a short position, the directions are reversed.

Choose how the exit should execute after the trigger fires.

| Close Type | What Happens                                                      | Available For                | | ---------- | ----------------------------------------------------------------- | ---------------------------- | | Market     | The exit executes immediately against available liquidity.        | Bracket orders and positions | | Limit      | The exit places a limit order and can remain open until it fills. | Bracket orders only          |

A resting limit exit does not lock up the position. A more aggressive reduce-only order on the same side (a manual close, or the position's other trigger firing later) takes priority and cancels the resting exit to make room. In particular, a fired stop-loss can displace a resting take-profit exit, so a bracket whose take-profit is already resting keeps a working stop. Closes that execute immediately never cancel a resting exit up front. See [Close a Position](#close-a-position) for the full priority rules.

A bracket order submits one entry order with up to one take-profit and one stop-loss trigger. The triggers stay dormant until the entry fills in full. If the entry is canceled, rejected, or only partially filled, the triggers are canceled too. A bracket protects the completed entry, not a partial fill.

<Note> You cannot attach TP/SL triggers to an order that is already resting on the book. To protect a position from an existing order, wait for the fill and then protect the position. </Note>

<Tabs> <Tab title="TypeScript"> Place a GTC entry order with take-profit and stop-loss triggers.

<Tab title="Python"> Place a GTC entry order with take-profit and stop-loss triggers.

<Tab title="API"> Submit the entry order and its TP/SL children in one `createOrders` operation with `grp` set to `"order"`.

Add TP/SL orders to a position that is already open. Position TP/SL closes the full position at trigger time, so it does not use a fixed quantity.

Position TP/SL has a few placement rules:

<Tabs> <Tab title="TypeScript"> Place TP/SL orders for the full current position.

<Tab title="Python"> Place TP/SL orders for the full current position.

<Tab title="API"> Submit position-scoped TP/SL orders with `grp` set to `"position"`. Use `qty: "0"` so the engine sizes the exit at trigger time.

TP/SL orders cannot be modified in place. To change a trigger price or execution type, cancel the old trigger and create a replacement.

Cancel-then-create is not atomic. Between the cancel and the replacement, the position may be unprotected.

So far, we have used immediate-or-cancel orders. Next, we’ll look at how to control whether an order rests, fills immediately, or only adds liquidity.

Use good-til-canceled orders when the order can rest on the book until it fills or you cancel it.

<Tabs> <Tab title="TypeScript"> Set `timeInForce` to GTC.

<Tab title="Python"> Set `time*in*force` to `gtc`.

<Tab title="API"> Set `tif` to `"gtc"`.

A post-only order is a special type of good-til-canceled order that only adds liquidity. If it would cross the book and take liquidity, it is rejected instead.

<Tabs> <Tab title="TypeScript"> Set `postOnly: true` on a GTC order.

<Tab title="Python"> Set `post_only=True` on a GTC order.

<Tab title="API"> Set `po: true` on a `gtc` order.

Use fill-or-kill orders when the full quantity must fill immediately or cancel. These orders do not rest on the book.

<Tabs> <Tab title="TypeScript"> Set `timeInForce` to FOK.

<Tab title="Python"> Set `time*in*force` to `fok`.

<Tab title="API"> Set `tif` to `"fok"`.

Change the price or total quantity of an existing order without canceling it and creating a new one. The order keeps its identity, direction, and other execution constraints.

You can modify standalone good-til-canceled (GTC) limit orders that are resting on the book, including partially filled orders.

<Tabs> <Tab title="TypeScript"> SDK support is coming soon. </Tab>

<Tab title="Python"> SDK support is coming soon. </Tab>

<Tab title="API"> <Steps> <Step title="Build and Sign the Modification"> Choose whether to identify the order by its exchange order ID or client order ID. Set `p` to the new limit price and `qty` to the new total quantity, including any quantity that has already filled.

The order's cumulative fill is its current total quantity minus its current remaining quantity. The requested new total must be greater than that cumulative fill. On success, the new remaining quantity is:

For example, suppose an order has a total quantity of `10`, a remaining quantity of `6`, and therefore a cumulative fill of `4`. Modifying the total quantity to `7` leaves `3` resting. A requested total of `4` or less is rejected.

The exchange evaluates these values from the live order when it applies the modification. A fill that arrives while the modification is in progress can change the resulting remaining quantity or cause the request to be rejected.

| Rule                  | Behavior                                                                                                 | | --------------------- | -------------------------------------------------------------------------------------------------------- | | Resting order         | The order must be a standalone GTC limit order currently resting on the book.                            | | Order in flight       | An order still moving through creation or taker delay is not yet resting and cannot be modified.         | | Crossing price        | The modified order must remain non-crossing against the live opposite best price when it is applied.     | | TP/SL relationship    | A TP/SL leg or an order with attached or order-scoped TP/SL cannot be modified.                          | | Rejected modification | The rejected modification itself does not alter the live order; separately processed activity still can. |

Queue treatment is determined from the live order state when the modification is applied.

| Modification                        | Queue treatment                           | | ----------------------------------- | ----------------------------------------- | | Same price and lower total quantity | Keeps its existing queue priority.        | | Higher total quantity               | Re-enters at the back of the price level. | | Any price change                    | Re-enters at the back of the price level. | | Same price and same total quantity  | Rejected because it makes no change.      |

Cancel resting orders when they are stale, conflict with updated strategy, or should no longer remain on the book. Canceling a resting order does not close any filled position.

<Tabs> <Tab title="TypeScript"> Cancel stale orders by order ID or by client order ID.

<Tab title="Python"> Cancel stale orders by order ID or by client order ID.

<Tab title="API"> Cancel by order ID with `DELETE /v1/trade/orders`.

Cancel every open order for your account in a single request, for example when pulling quotes during a fast move or shutting down a strategy. Scope the request to one instrument to clear only that book while quotes on other instruments stay live.

A successful response confirms the request was accepted, not that every order is already gone: individual orders can still race with fills or other cancels. Confirm the final state from your open orders.

<Tabs> <Tab title="TypeScript"> Cancel all open orders, or only the open orders on one instrument.

<Tab title="Python"> Cancel all open orders, or only the open orders on one instrument.

<Tab title="API"> Cancel all open orders with `DELETE /v1/trade/orders/all`. Use the same signing flow as [Place Orders](#place-orders) to create `<cancel_signature>`. For hashing, sign the compact operation, not the structured JSON body.

Auto-cancel is a dead man's switch for your open orders. Arm it with a future deadline, and the exchange cancels every open order on your account when that deadline passes. Keep re-arming it with a fresh deadline while your integration runs. If the process crashes or loses connectivity, the re-arms stop, the deadline passes, and your resting orders leave the book with no action from you.

The switch fires once. After it fires, the schedule clears itself, and orders you place afterwards are unprotected until you arm it again. Arming again replaces the current schedule, and the deadline must be at least five seconds in the future. Accounts can trigger auto-cancel a limited number of times per UTC day, so disarm the switch on graceful shutdown instead of letting it fire.

<Tabs> <Tab title="TypeScript"> Arm the switch with `session.armAutoCancel` and keep protection active by re-arming on an interval shorter than the deadline.

<Tab title="Python"> Arm the switch with `session.arm*auto*cancel` and keep protection active by re-arming on an interval shorter than the deadline. `cancel_at` accepts a `datetime` or a Unix timestamp in milliseconds.

<Tab title="API"> Arm the switch with `PATCH /v1/trade/auto-cancel`. Use the same signing flow as [Place Orders](#place-orders) to create `<auto*cancel*signature>`. For hashing, sign the compact operation, not the structured JSON body.

Closing a position is a new order in the opposite direction of the open position. Use the full open position size to close. Use a smaller quantity to reduce instead. Mark close orders reduce-only so they cannot flip the account into new exposure if position state changes before execution.

Reduce-only is a safeguard, not a sizing shortcut. You still choose the quantity: use the full position size to close or a smaller quantity to reduce. An order that would increase exposure or flip the position is rejected.

| Current Position | Reduce-Only Buy   | Reduce-Only Sell  | | ---------------- | ----------------- | ----------------- | | Long             | Rejected          | Reduces or closes | | Short            | Reduces or closes | Rejected          | | No position      | Rejected          | Rejected          |

Resting reduce-only orders on the same instrument share the position as a closing budget, but they never block a close that executes immediately. An IOC, FOK, or market-priced reduce-only order is accepted against the full position size. After a fill, the exchange cancels whole resting reduce-only orders on the same side, least aggressive first, until their remaining exposure fits the reduced position. A close that fills nothing leaves them untouched.

A reduce-only order that would rest competes on price instead: a lower-priced sell or a higher-priced buy outranks a resting reduce-only order and cancels it in full, least aggressive first, until the new order fits, while an equal or worse price keeps the resting order's claim. Any excess that still does not fit is trimmed from the new order, or the order is rejected.

<Tabs> <Tab title="TypeScript"> Find the current position by market symbol and parse its decimal size.

<Tab title="Python"> Find the current position by market symbol and inspect its decimal size.

<Tab title="API"> Fetch the portfolio and inspect the position `size` for the instrument.

Leverage controls how much notional exposure a position can carry relative to its margin. Cross margin uses available account collateral for the position; isolated margin keeps collateral allocated to that position. Some instruments support only isolated margin. Validate leverage against the instrument's maximum and current risk tiers before submitting a change.

Leverage and margin mode resolve independently for each instrument. An explicit per-instrument setting takes precedence over a default assigned to your exchange-managed account group. Without either, leverage defaults to the instrument's maximum and margin mode to isolated. Account configuration reads report the resolved values; updates set explicit values.

Switching margin mode requires no position and no open orders in that instrument, including orders awaiting risk approval or execution. Close the position and cancel all orders before switching. See [Default Leverage and Margin Mode](/perps/learn-about-trading/margin#default-leverage-and-margin-mode) for how inherited settings apply.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Read Current Configuration"> Read the current account configuration before changing leverage.

<Tab title="Python"> <Steps> <Step title="Read Current Configuration"> Read the current account configuration before changing leverage.

<Tab title="API"> <Steps> <Step title="Read Current Configuration"> Read the current account configuration before changing leverage.

Adjust the collateral allocated to an open position when you want to give it more buffer or release collateral that is no longer needed.

<Tabs> <Tab title="TypeScript"> Use `updateMargin` on the authenticated Perps session.

<Tab title="Python"> Use `update_margin` on the authenticated Perps session.

<Tab title="API"> Submit a signed `updateMargin` operation to `PATCH /v1/trade/margin`. Use the same signing flow as [Place Orders](#place-orders), and sign this compact operation for each request:

The amount is a precision-safe decimal string in the instrument's quote asset. A positive value adds isolated margin; a negative value removes it. This workflow applies only to an open position using isolated margin.

For allocation and removal constraints, see [Adjusting Isolated Margin](/perps/learn-about-trading/margin#adjusting-isolated-margin).

Keep local trading state in sync by starting from a local snapshot, applying live updates, and reconciling again whenever the session tells you state may have been missed.

TP/SL orders appear alongside regular orders in open-order and order-history reads. Track their lifecycle in addition to the position and fills they protect.

| Lifecycle State | Meaning                                                         | | --------------- | --------------------------------------------------------------- | | Dormant         | Waiting for a bracket entry order to fill in full.              | | Armed           | Watching the mark price for the trigger.                        | | Triggered       | Fired and submitted the closing order.                          | | Canceled        | Removed by you, by parent cancellation, or by auto-cancel.      | | Cleared         | Removed because the protected position closed or changed sides. |

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Fetch a Startup Snapshot"> Fetch a snapshot when the session starts.

<Tab title="Python"> <Steps> <Step title="Fetch a Startup Snapshot"> Fetch a snapshot when the session starts.

<Tab title="API"> <Steps> <Step title="Fetch a Startup Snapshot"> Use account reads to build the local startup snapshot.

Use the fee schedule when you need to display or account for the default maker and taker trading fees. Fee rates are decimal strings, so `"0.0004"` means `0.04%`.

Default (`$0` tier) rates apply when an account has no tier assignment. The account's actual rate on each fill depends on its current fee tier. See [Fees](/perps/learn-about-trading/fees) for the tier table. Authenticated portfolio reads report the account's current tier; see [Portfolio](/perps/account-management#portfolio).

<Tabs> <Tab title="TypeScript"> Fetch the current Perps fee schedule.

<Tab title="Python"> Fetch the current Perps fee schedule.

<Tab title="API"> Fetch the current Perps fee schedule.

**Examples:**

Example 1 (text):
```text
flowchart TD
  A[Submit order] --> B{Accepted?}
  B -->|No| C[Order rejected]
  B -->|Yes| D{Filled?}
  D -->|Rests| E[Open order]
  D -->|Fills| F[Fill]
  D -->|Partially fills| F
  F -->|Remaining quantity| E
  F --> G[Exposure changes]
  E --> H[Cancel if needed]
```

Example 2 (text):
```text
    import { createSecureClient } from "@polymarket/client";
    import { privateKey } from "@polymarket/client/viem";

    const client = await createSecureClient({
      wallet: process.env.POLYMARKET_WALLET_ADDRESS!,
      signer: privateKey(process.env.PRIVATE_KEY!),
    });
```

Example 3 (text):
```text
Open the Perps session.

```ts theme={null}
const session = await client.openPerpsSession();
```
```

Example 4 (text):
```text
    import os

    from polymarket import AsyncSecureClient

    client = await AsyncSecureClient.create(
        private_key=os.environ["PRIVATE_KEY"],
        wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
    )
```

---

## Overview

**URL:** https://docs.polymarket.com/trading/overview.md

**Contents:**
- Trading Workflow
- Start Trading

Trading connects signed orders on the CLOB with settlement on Polygon. You choose an outcome token, authorize an order with your signer, and submit it to the order book. When the order matches, settlement transfers pUSD and outcome tokens between trading accounts.

Set up your account once, then repeat the remaining steps for each order.

<Steps> <Step title="Set Up Your Account"> Connect a signer to your account wallet, fund it, and grant the required trading approvals. </Step>

<Step title="Choose an Outcome"> Select the outcome token you want to buy or sell and check its current market constraints. </Step>

<Step title="Place an Order"> Choose a price and size, sign the order, and submit it to the CLOB. </Step>

<Step title="Manage the Order"> Monitor fills and cancel any remaining open amount. Matched trades settle on Polygon and update your balances and positions. </Step> </Steps>

<Info> The Exchange operator can match orders and enforce their ordering, but cannot set prices or execute trades that users did not authorize. </Info>

<CardGroup cols={2}> <Card title="Place Your First Order" icon="rocket" href="/trading/quickstart"> Complete the first authenticated trading workflow. </Card>

<Card title="Wallets and Authentication" icon="key" href="/trading/wallets-auth"> Connect a signer to the account wallet that holds funds and positions. </Card>

<Card title="Order Lifecycle" icon="repeat" href="/concepts/order-lifecycle"> Understand how orders move from submission through fills, cancellation, or expiration. </Card>

<Card title="Session Keys" icon="clock" href="/trading/session-keys"> Give a separate signer scoped, time-limited Deposit Wallet access. </Card> </CardGroup>

---

## Combos for Builders

**URL:** https://docs.polymarket.com/trading/combos/builders.md

**Contents:**
- Custodial Integration
  - Request and Execute a Quote
- Non-Custodial Integration
- Handle Outcomes and Errors
  - Check Each Case
- Next Steps

Approved builders can request executable Combo quotes and accept them for their users. The Builder Gateway runs a quote competition, returns the best available quote, and tracks the accepted trade through onchain execution.

You need the builder credentials provided during onboarding, plus authenticated access to the trading account. If you are not registered, [register as a builder](https://builders.polymarket.com/) before continuing.

This guide starts with the custodial model, where the builder controls and signs for one omnibus trading account. If each user signs for their own wallet, follow the [non-custodial guide](#non-custodial-integration) at the end of this page.

<Warning> Keep the Builder API secret on trusted infrastructure. Never expose it in a browser or other untrusted client. </Warning>

In the custodial model, the builder holds Combo positions for users in one omnibus Deposit Wallet and controls the account signer. The same account and builder identity must request and accept each quote.

Choose 2–50 unique, mutually compatible underlying market position IDs as the legs. These are outcome position IDs from [Combo-enabled markets](/trading/combos/market-makers#get-combo-markets), not CLOB token IDs or the derived Combo position IDs. Contradictory legs cannot form a Combo. A BUY request sets the maximum collateral budget, including fees. A SELL request specifies the number of Combo shares to sell.

<Tabs> <Tab title="TypeScript"> Use `requestComboQuote()` on a TypeScript `SecureClient` to request, accept, and track a Combo quote.

<Tab title="Python"> Use `request*combo*quote()` on `AsyncSecureClient` to request, accept, and track a Combo quote. The synchronous `SecureClient` exposes the same methods.

<Tab title="API"> The Direct API gives custodial server-side integrations lower-level control over request signing and order construction. The gateway host is provided during builder onboarding, and its base path is `/v1/builder/rfq`.

In the non-custodial model, each user controls the account signer for their own Deposit Wallet, while the builder provides integration authorization from trusted infrastructure.

<Tabs> <Tab title="TypeScript"> Use `remoteBuilderSigning()` with a TypeScript `SecureClient` so the connected wallet authorizes account actions while your server keeps the Builder API secret.

Custodial and non-custodial accounts share the same quote and execution outcomes. The account model changes who authorizes the trade, not how the RFQ progresses. Keep the RFQ ID until the request reaches a terminal state.

| Case                           | What happened                                                                 | What to do                                                                     | | ------------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | | No executable quote            | The competition ended without a usable quote.                                 | Treat it as a normal market outcome. Retry later or adjust the requested size. | | Acceptance failed              | The maker declined, the deadline passed, or execution could not start.        | Request a fresh quote. Do not reuse an expired quote.                          | | Local wait timed out           | Your client stopped waiting before a durable outcome was available.           | Fetch the RFQ status and continue until it reaches a terminal state.           | | Execution ended without a fill | The RFQ failed, expired, or was canceled.                                     | Inspect the returned error before deciding whether to request another quote.   | | Filled                         | The trade was confirmed onchain.                                              | Record the transaction hash and reconcile the trade and resulting positions.   | | Request failed                 | Authentication, validation, rate limiting, transport, or a dependency failed. | Correct the reported cause; retry only when the request is safe to repeat.     |

No executable quote, failed acceptance, and terminal execution failure are business outcomes. They can be returned successfully by the service and should not be treated as transport failures.

<Tabs> <Tab title="TypeScript"> Use `requestComboQuote()` and its follow-up methods on `SecureClient` to detect each case. Use the original RFQ ID when a local wait times out.

<Tab title="Python"> Use `request*combo*quote()` and its follow-up methods on `AsyncSecureClient` or `SecureClient` to detect each case. Use the original RFQ ID when a local wait times out.

<Tab title="API"> Inspect the response `status` and `error` fields after each Direct API request. Do not use the HTTP status alone to decide whether the trade filled.

<CardGroup cols={2}> <Card title="Collateral Return" icon="coins" href="/trading/combos/collateral-return"> Release pUSD from compatible Combo positions before resolution. </Card>

<Card title="Discover Combo Markets" icon="magnifying-glass" href="/trading/combos/market-makers#get-combo-markets"> Find eligible markets and their leg position IDs. </Card> </CardGroup>

**Examples:**

Example 1 (javascript):
```javascript
Don't have the TypeScript SDK installed? Start with the
[TypeScript SDK guide's wallet integrations](/getting-started/typescript#wallet-integrations),
then come back.

<Steps>
  <Step title="Create a Custodial Client">
    Configure a `SecureClient` with the wallet signer, Deposit Wallet address, and
    Builder API Key. This server-side example keeps the account key and builder
    secret on trusted infrastructure.

    ```ts theme={null}
    import { createSecureClient } from "@polymarket/client";
    import { builderApiKey } from "@polymarket/client/node";
    import { privateKey } from "@polymarket/client/viem";

    const client = await createSecureClient({
      signer: privateKey(process.env.POLYMARKET_PRIVATE_KEY!),
      wallet: process.env.POLYMARKET_DEPOSIT_WALLET!,
      apiKey: builderApiKey({
        key: process.env.POLYMARKET_BUILDER_API_KEY!,
        secret: process.env.POLYMARKET_BUILDER_SECRET!,
        passphrase: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
      }),
    });
    ```
  </Step>

  <Step title="Request a Quote">
    Call `requestComboQuote()` with the leg position IDs and a human-readable
    collateral amount. Amounts and sizes must be positive and have at most six
    decimal places. Combo quote requests currently target the YES side, which the
    SDK supplies by default. The method resolves when the quote competition closes.

    ```ts theme={null}
    import { OrderSide } from "@polymarket/client";

    const result = await client.requestComboQuote({
      legPositionIds: ["<yes-position-id-1>", "<yes-position-id-2>"],
      direction: OrderSide.BUY,
      amount: "10",
    });

    // result: RequestComboQuoteResult
    ```

    If no usable quote is available, `result.quote` is `null` and `result.reason`
    explains the outcome. A winning quote includes its acceptance deadline in
    `result.quote.expiresAt`, as a Unix timestamp in milliseconds. Use that value
    rather than assuming a fixed acceptance window.

    For a SELL quote, pass `direction: OrderSide.SELL` with a human-readable `size`
    instead of `amount`. The returned `quote.netReceive` is the exact collateral
    proceeds after fees.
  </Step>

  <Step title="Accept and Track the Quote">
    Pass the returned quote to `acceptComboQuote()` immediately. After it enters
    execution, call `waitForComboFill()` to wait for a terminal result.

    ```ts theme={null}
    import { RfqStatus } from "@polymarket/client";

    async function acceptAndTrackQuote() {
      if (result.quote === null) {
        console.log(`No quote available: ${result.reason}`);
        return;
      }

      const acceptance = await client.acceptComboQuote(result.quote);

      if (acceptance.status === "failed") {
        console.log(`Quote not accepted: ${acceptance.reason}`);
        return;
      }

      const fill = await client.waitForComboFill({
        rfqId: acceptance.rfqId,
        timeoutMs: 120_000,
      });

      if (fill.status === RfqStatus.Filled) {
        console.log(`Filled: ${fill.txHash}`);
        return;
      }

      console.log(`Execution ended with ${fill.status}`);
    }

    await acceptAndTrackQuote();
    ```

    An acceptance with `status: "executing"` is not yet a confirmed fill. A maker
    decline, expired window, or execution failure is returned as a business outcome.
    A local timeout does not mean the trade failed.
  </Step>
</Steps>
```

Example 2 (text):
```text
Don't have the Python SDK installed? Start with the
[Python SDK guide](/getting-started/python), then come back.

<Steps>
  <Step title="Configure Custodial Credentials">
    Load the Builder API Key on trusted infrastructure. The workflow below uses a
    server-side account key and Deposit Wallet address.

    ```python theme={null}
    import os

    from polymarket import BuilderApiKey


    builder_api_key = BuilderApiKey(
        key=os.environ["POLYMARKET_BUILDER_API_KEY"],
        secret=os.environ["POLYMARKET_BUILDER_SECRET"],
        passphrase=os.environ["POLYMARKET_BUILDER_PASSPHRASE"],
    )
    ```
  </Step>

  <Step title="Request, Accept, and Track the Quote">
    Call `request_combo_quote()` with the leg position IDs and a human-readable
    collateral amount. Amounts and sizes must be positive and have at most six
    decimal places. Combo quote requests currently target the YES side, which the
    SDK supplies by default. The method resolves when the quote competition closes.

    ```python theme={null}
    from decimal import Decimal

    from polymarket import AsyncSecureClient, RfqStatus, TimeoutError


    async with await AsyncSecureClient.create(
        private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
        wallet=os.environ["POLYMARKET_DEPOSIT_WALLET"],
        api_key=builder_api_key,
    ) as client:
        result = await client.request_combo_quote(
            leg_position_ids=["<yes-position-id-1>", "<yes-position-id-2>"],
            direction="BUY",
            amount=Decimal("10"),
        )

        if result.quote is None:
            print(f"No quote available: {result.reason}")
        else:
            try:
                acceptance = await client.accept_combo_quote(result.quote)

                if acceptance.status == "failed":
                    print(f"Quote not accepted: {acceptance.reason}")
                else:
                    fill = await client.wait_for_combo_fill(
                        rfq_id=acceptance.rfq_id,
                        timeout=120.0,
                    )

                    if fill.status is RfqStatus.FILLED:
                        print(f"Filled: {fill.tx_hash}")
                    else:
                        print(f"Execution ended with {fill.status}")
            except TimeoutError:
                status = await client.fetch_rfq_status(rfq_id=result.rfq_id)
                print(f"Current status: {status.status}")
    ```

    If no usable quote is available, `result.quote` is `None` and `result.reason`
    explains the outcome. A winning quote includes its acceptance deadline in
    `result.quote.expires_at`, as a Unix timestamp in milliseconds. Use that value
    rather than assuming a fixed acceptance window.

    For a SELL quote, pass `direction="SELL"` with a human-readable `size` instead
    of `amount`. The returned `quote.net_receive` is the exact collateral proceeds
    after fees.

    An acceptance with `status == "executing"` is not yet a confirmed fill. A maker
    decline, expired window, or execution failure is returned as a business outcome.
    A local timeout does not mean the trade failed. The context manager closes the
    client after the workflow, including after an exception.
  </Step>
</Steps>
```

Example 3 (text):
```text
<Steps>
  <Step title="Sign Request Headers">
    Create and accept requests require both account and builder authentication.
    Status requests require account authentication only.

    | Request                                   | Account headers | Builder headers |
    | ----------------------------------------- | --------------- | --------------- |
    | `POST /requests`                          | Required        | Required        |
    | `POST /requests/{rfq_id}/accept`          | Required        | Required        |
    | `GET /requests/{rfq_id}` after acceptance | Required        | Do not send     |

    The account header set is `POLY_ADDRESS`, `POLY_API_KEY`, `POLY_PASSPHRASE`,
    `POLY_TIMESTAMP`, and `POLY_SIGNATURE`. The builder header set is
    `POLY_BUILDER_API_KEY`, `POLY_BUILDER_PASSPHRASE`,
    `POLY_BUILDER_TIMESTAMP`, and `POLY_BUILDER_SIGNATURE`.

    `POLY_ADDRESS` is the EOA that owns the omnibus account credentials. Both
    `signer_address` and `maker_address` are the builder-controlled Deposit Wallet
    address.

    Compute each signature with HMAC-SHA256, using the base64-decoded secret as the
    key. Sign an uppercase method, a Unix timestamp in seconds, the full request path
    such as `/v1/builder/rfq/requests` without the host or query string, and the exact
    serialized body sent on the wire. Omit the body for `GET` requests. Encode the
    digest as base64url with padding preserved.

    ```text theme={null}
    HMAC-SHA256(
      base64Decode(secret),
      timestamp + HTTP_METHOD + FULL_REQUEST_PATH + REQUEST_BODY
    )
    ```
  </Step>

  <Step title="Create the RFQ">
    Create a BUY RFQ with a collateral budget in 6-decimal base units. The gateway
    holds the request until the quote competition finishes.

    ```http theme={null}
    POST /v1/builder/rfq/requests
    Content-Type: application/json
    POLY_ADDRESS: <account-signer-address>
    POLY_API_KEY: <account-api-key>
    POLY_PASSPHRASE: <account-passphrase>
    POLY_TIMESTAMP: <account-timestamp>
    POLY_SIGNATURE: <account-signature>
    POLY_BUILDER_API_KEY: <builder-api-key>
    POLY_BUILDER_PASSPHRASE: <builder-passphrase>
    POLY_BUILDER_TIMESTAMP: <builder-timestamp>
    POLY_BUILDER_SIGNATURE: <builder-signature>

    {
      "signer_address": "<deposit-wallet-address>",
      "maker_address": "<deposit-wallet-address>",
      "signature_type": 3,
      "leg_position_ids": ["<yes-position-id-1>", "<yes-position-id-2>"],
      "direction": "BUY",
      "side": "YES",
      "requested_size": {
        "unit": "notional",
        "value_e6": "1000000"
      }
    }
    ```

    Use `unit: "notional"` for BUY requests and `unit: "shares"` for SELL
    requests. The `value_e6` value is a string in 6-decimal base units. `side` must
    currently be `"YES"`.

    An executable response includes the RFQ, the winning quote, and an acceptance
    deadline:

    <Accordion title="Create RFQ Response">
      ```json theme={null}
      {
        "rfq_id": "<rfq-id>",
        "status": "AWAITING_REQUESTER_ACCEPTANCE",
        "expires_at": 1773890765500,
        "builder_code": "<builder-code>",
        "request": {
          "rfq_id": "<rfq-id>",
          "maker_address": "<deposit-wallet-address>",
          "requestor_public_id": "<requester-public-id>",
          "leg_position_ids": ["<yes-position-id-1>", "<yes-position-id-2>"],
          "condition_id": "<combo-condition-id>",
          "yes_position_id": "<combo-yes-position-id>",
          "no_position_id": "<combo-no-position-id>",
          "direction": "BUY",
          "side": "YES",
          "requested_size": {
            "unit": "notional",
            "value_e6": "1000000"
          },
          "created_at": 1773890758000
        },
        "quote": {
          "quote_id": "<quote-id>",
          "blended_price_e6": "500000",
          "maker_amount_e6": "966191",
          "taker_amount_e6": "1932381",
          "total_required_e6": "1000000",
          "net_receive_e6": "1932381"
        }
      }
      ```
    </Accordion>

    A terminal result such as no quotes returns HTTP `200` with `status: "FAILED"`
    and an `error` object. `expires_at` and `request.created_at` are Unix timestamps
    in milliseconds. Construct and submit the signed order before `expires_at`; do
    not assume a fixed acceptance window. `total_required_e6` is the exact requester
    balance required: collateral including fees for BUY, or Combo shares for SELL.
    For BUY quotes, `net_receive_e6` is the number of Combo shares received. For SELL
    quotes, it is the exact collateral proceeds after fees; use it instead of
    deriving proceeds from the blended price.
  </Step>

  <Step title="Accept the Quote">
    Build an Exchange v3 requester order from the returned RFQ and quote, sign it
    for the authenticated wallet type, then submit it with both authentication
    sets. Use Polygon chain ID `137` and Exchange v3 contract
    `0xe3333700cA9d93003F00f0F71f8515005F6c00Aa` for the EIP-712 domain.

    Deposit Wallets use `signatureType: 3` and an ERC-7739-wrapped signature. See
    [Authorize the Quote](/trading/combos/market-makers#authorize-the-quote) for the
    Exchange v3 order types and wallet-specific signing paths.

    ```http theme={null}
    POST /v1/builder/rfq/requests/<rfq-id>/accept
    Content-Type: application/json
    POLY_ADDRESS: <account-signer-address>
    POLY_API_KEY: <account-api-key>
    POLY_PASSPHRASE: <account-passphrase>
    POLY_TIMESTAMP: <account-timestamp>
    POLY_SIGNATURE: <account-signature>
    POLY_BUILDER_API_KEY: <builder-api-key>
    POLY_BUILDER_PASSPHRASE: <builder-passphrase>
    POLY_BUILDER_TIMESTAMP: <builder-timestamp>
    POLY_BUILDER_SIGNATURE: <builder-signature>

    {
      "quote_id": "<quote-id>",
      "signed_order": {
        "salt": "<salt>",
        "maker": "<deposit-wallet-address>",
        "signer": "<deposit-wallet-address>",
        "tokenId": "<combo-yes-position-id>",
        "makerAmount": "966191",
        "takerAmount": "1932381",
        "side": 0,
        "signatureType": 3,
        "timestamp": "<unix-seconds>",
        "metadata": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "builder": "<builder-code>",
        "signature": "<order-signature>"
      }
    }
    ```

    For both directions, copy `maker_amount_e6` to `makerAmount` and
    `taker_amount_e6` to `takerAmount`, and use the returned Combo YES position ID
    as `tokenId`. Set `side` to `0` for BUY or `1` for SELL. The order's `builder`
    must equal the returned `builder_code`.

    The response contains the latest known state. If last look is still pending,
    the gateway waits for an update for up to one second before returning. If the
    response still has `status: "AWAITING_MAKER_CONFIRMATION"`, fetch status until
    the maker responds.

    <Accordion title="Accept Quote Response">
      ```json theme={null}
      {
        "rfq_id": "<rfq-id>",
        "status": "EXECUTING",
        "taker_order_hash": "<order-hash>"
      }
      ```
    </Accordion>

    The `taker_order_hash` is the EIP-712 hash of the requester order. A maker
    decline or execution failure still returns HTTP `200`, with `status: "FAILED"`
    and a nested `error` object. Retrying the same authenticated acceptance does not
    execute twice; its response may omit `taker_order_hash`. Use `rfq_id` as the
    stable recovery identifier.
  </Step>

  <Step title="Fetch Status">
    After acceptance, fetch durable status with account headers only.

    ```http theme={null}
    GET /v1/builder/rfq/requests/<rfq-id>
    Accept: application/json
    POLY_ADDRESS: <account-signer-address>
    POLY_API_KEY: <account-api-key>
    POLY_PASSPHRASE: <account-passphrase>
    POLY_TIMESTAMP: <account-timestamp>
    POLY_SIGNATURE: <account-signature>
    ```

    <Accordion title="Status Response">
      ```json theme={null}
      {
        "rfq_id": "<rfq-id>",
        "status": "CONFIRMED",
        "tx_hash": "<transaction-hash>"
      }
      ```
    </Accordion>

    Status reads before acceptance return HTTP `409`. The status response contains
    one top-level `status` plus an optional `tx_hash` or `error`; it does not repeat
    the request or quote. Status can progress through
    `AWAITING_MAKER_CONFIRMATION`, `EXECUTING`, `MINED`, and `RETRYING` before
    reaching a successful `CONFIRMED` or `FILLED` state. `FAILED`, `EXPIRED`, and
    `CANCELED` are terminal states without a fill.
  </Step>
</Steps>
```

Example 4 (javascript):
```javascript
Start with a connected Viem `WalletClient` and the user's Deposit Wallet
address. See the [TypeScript wallet integrations](/getting-started/typescript#wallet-integrations)
if you have not configured the account signer yet.

### Set Up Remote Builder Signing

Combo quote requests require authenticated account access. Create a
`SecureClient` with `remoteBuilderSigning()` so the user's signer and the
builder's signing service authorize their parts of the request separately.

<CodeGroup>
  ```typescript client.ts theme={null}
  import { createSecureClient, remoteBuilderSigning } from "@polymarket/client";
  import { signerFrom } from "@polymarket/client/viem";

  const client = await createSecureClient({
    signer: signerFrom(walletClient),
    wallet: depositWalletAddress,
    apiKey: remoteBuilderSigning({
      url: "/api/builder/sign",
    }),
  });
  ```

  ```typescript server.ts theme={null}
  import { buildHmacSignature } from "@polymarket/client";

  // Handler for POST /api/builder/sign
  export async function handleSignRequest(request: Request): Promise<Response> {
    const { body, method, path } = await request.json();
    const timestamp = Math.floor(Date.now() / 1000);
    const signature = await buildHmacSignature(
      process.env.POLYMARKET_BUILDER_SECRET!,
      timestamp,
      method,
      path,
      body,
    );

    return Response.json({
      POLY_BUILDER_API_KEY: process.env.POLYMARKET_BUILDER_API_KEY!,
      POLY_BUILDER_PASSPHRASE: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
      POLY_BUILDER_SIGNATURE: signature,
      POLY_BUILDER_TIMESTAMP: `${timestamp}`,
    });
  }
  ```
</CodeGroup>

Here, `walletClient` is the connected Viem `WalletClient` and
`depositWalletAddress` is that user's Deposit Wallet. Authenticate calls to
`/api/builder/sign` with your application session. For cookie authentication,
pass `credentials: "include"` when the signing API is cross-origin. For bearer
authentication, pass the token through the `headers` option on
`remoteBuilderSigning()`.

Use a Deposit Wallet already associated with the user. To provision a new
account first, follow [Create New Accounts](/trading/wallets-auth#create-new-accounts).

The signing response gives the browser the Builder key identifier, passphrase,
timestamp, and a signature scoped to that request. The Builder secret never
leaves the signing server.

<Warning>
  Do not sign arbitrary request details from the browser. Bind the application
  session to the expected user and Deposit Wallet, allow only the required
  method and path combinations, and validate account identities in request
  bodies. Protect cookie-backed endpoints from CSRF and rate-limit signing
  requests. Client setup can request signatures for CLOB authentication and
  Deposit Wallet checks before the Combo create and accept requests, so include
  those setup operations in your allowlist. If you parse a body to validate it,
  still sign the original raw `body` string without reserializing it.
</Warning>

### Request and Execute a User-Authorized Quote

Use the same Combo requester methods as the custodial TypeScript flow. The
account identity now comes from the user's signer and Deposit Wallet, while
Builder authentication comes from your signing API.

```ts theme={null}
import { OrderSide, RfqStatus } from "@polymarket/client";

async function requestAndTrackQuote() {
  const result = await client.requestComboQuote({
    legPositionIds: ["<yes-position-id-1>", "<yes-position-id-2>"],
    direction: OrderSide.BUY,
    amount: "10",
  });

  if (result.quote === null) {
    console.log(`No quote available: ${result.reason}`);
    return;
  }

  const acceptance = await client.acceptComboQuote(result.quote);

  if (acceptance.status === "failed") {
    console.log(`Quote not accepted: ${acceptance.reason}`);
    return;
  }

  const fill = await client.waitForComboFill({
    rfqId: acceptance.rfqId,
    timeoutMs: 120_000,
  });

  if (fill.status === RfqStatus.Filled) {
    console.log(`Filled: ${fill.txHash}`);
    return;
  }

  console.log(`Execution ended with ${fill.status}`);
}

await requestAndTrackQuote();
```

The user must approve the requester order before the quote expires. Preserve the
returned quote and retry acceptance before `result.quote.expiresAt` if wallet or
remote signing fails. Keep the RFQ ID to recover status after an interrupted
Gateway response or local timeout.
```

---

## Manage Positions

**URL:** https://docs.polymarket.com/trading/positions/manage.md

**Contents:**
- Split a Position
- Merge Positions
- Redeem Resolved Positions

Manage positions outside the order book by splitting collateral into complete sets of outcome tokens, merging balanced tokens back into collateral, or redeeming winning tokens after resolution.

Choose an operation based on how you want to change your position:

| Operation | Use it when                                                                   | | --------- | ----------------------------------------------------------------------------- | | Split     | You need to convert collateral into a complete set of outcome tokens.         | | Merge     | You hold balanced outcome tokens and want to convert them back to collateral. | | Redeem    | A market has resolved and you want to claim collateral for winning positions. |

Choose the integration surface you will use to submit position operations.

<Tabs> <Tab title="TypeScript"> The examples on this page assume you have a `SecureClient` configured with either a Relayer API key or a Builder API key.

<Tab title="Python"> The examples on this page assume you have an `AsyncSecureClient` configured with either a Relayer API key or a Builder API key.

<Tab title="API"> The examples on this page assume you can authenticate Relayer API requests with either a Relayer API key or a Builder API key. The examples below use a Relayer API key:

<Tab title="Solidity"> The examples on this page use these Polygon contracts:

Splitting converts pUSD into a complete set of outcome tokens. Every 1 pUSD produces 1 YES token and 1 NO token.

Before splitting, ensure you have:

<Tabs> <Tab title="TypeScript"> Call `splitPosition()` on a `SecureClient`. The client identifies the market type from the condition ID and selects the correct collateral adapter.

<Tab title="Python"> Call `split_position()` on an `AsyncSecureClient`. The synchronous `SecureClient` provides the same method. Both clients identify the market type from the condition ID and select the correct collateral adapter.

<Tab title="API"> Build the `splitPosition` call, then execute it as a gasless wallet transaction.

<Tab title="Solidity"> Splitting pUSD through a collateral adapter follows this flow:

Merging converts a complete set of outcome tokens back into pUSD. Every 1 YES token and 1 NO token returns 1 pUSD.

Before merging, ensure you have:

<Tabs> <Tab title="TypeScript"> Call `mergePositions()` on a `SecureClient`. The client identifies the market type, selects the correct collateral adapter, and checks the wallet's mergeable balance.

<Tab title="Python"> Call `merge_positions()` on an `AsyncSecureClient`. The synchronous `SecureClient` provides the same method. Both clients identify the market type, select the correct collateral adapter, and check the wallet's mergeable balance.

<Tab title="API"> Build the `mergePositions` call, then execute it as a gasless wallet transaction.

<Tab title="Solidity"> Merging outcome tokens through a collateral adapter follows this flow:

Redeeming converts outcome tokens into pUSD after a market resolves. Each winning token returns 1 pUSD, while losing tokens return 0.

<Note> There is no redemption deadline. Winning tokens remain redeemable at any time after resolution. </Note>

Before redeeming, ensure you have:

<Tabs> <Tab title="TypeScript"> Call `redeemPositions()` on a `SecureClient`. The client uses the condition ID to select the correct collateral adapter for the market type.

<Tab title="Python"> Call `redeem_positions()` on an `AsyncSecureClient`. The synchronous `SecureClient` provides the same method. Both clients use the condition ID to select the correct collateral adapter for the market type.

<Tab title="API"> Build the `redeemPositions` call for a resolved market, then execute it as a gasless wallet transaction.

<Tab title="Solidity"> Redeeming outcome tokens through a collateral adapter follows this flow:

**Examples:**

Example 1 (text):
```text
<CodeGroup>
  ```ts Relayer API Key theme={null}
  import { createSecureClient, relayerApiKey } from "@polymarket/client";
  import { privateKey } from "@polymarket/client/viem";

  const client = await createSecureClient({
    signer: privateKey(process.env.SIGNER_PRIVATE_KEY),
    wallet: process.env.POLYMARKET_WALLET_ADDRESS,
    apiKey: relayerApiKey({
      key: process.env.POLYMARKET_RELAYER_API_KEY!,
      address: process.env.POLYMARKET_RELAYER_API_KEY_ADDRESS!,
    }),
  });
  ```

  ```ts Builder API Key theme={null}
  import { createSecureClient } from "@polymarket/client";
  import { builderApiKey } from "@polymarket/client/node";
  import { privateKey } from "@polymarket/client/viem";

  const client = await createSecureClient({
    signer: privateKey(process.env.SIGNER_PRIVATE_KEY),
    wallet: process.env.POLYMARKET_WALLET_ADDRESS,
    apiKey: builderApiKey({
      key: process.env.POLYMARKET_BUILDER_API_KEY!,
      secret: process.env.POLYMARKET_BUILDER_SECRET!,
      passphrase: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
    }),
  });
  ```
</CodeGroup>

See [Wallets and
Authentication](/trading/wallets-auth#execute-gasless-transactions) for the
complete wallet setup and Relayer authorization flow.
```

Example 2 (text):
```text
<CodeGroup>
  ```python Relayer API Key theme={null}
  import os

  from polymarket import AsyncSecureClient, RelayerApiKey

  client = await AsyncSecureClient.create(
      private_key=os.environ["SIGNER_PRIVATE_KEY"],
      wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
      api_key=RelayerApiKey(
          key=os.environ["POLYMARKET_RELAYER_API_KEY"],
          address=os.environ["POLYMARKET_RELAYER_API_KEY_ADDRESS"],
      ),
  )
  ```

  ```python Builder API Key theme={null}
  import os

  from polymarket import AsyncSecureClient, BuilderApiKey

  client = await AsyncSecureClient.create(
      private_key=os.environ["SIGNER_PRIVATE_KEY"],
      wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
      api_key=BuilderApiKey(
          key=os.environ["POLYMARKET_BUILDER_API_KEY"],
          secret=os.environ["POLYMARKET_BUILDER_SECRET"],
          passphrase=os.environ["POLYMARKET_BUILDER_PASSPHRASE"],
      ),
  )
  ```
</CodeGroup>

The synchronous `SecureClient` provides the same methods and supports both
API key types.

See [Wallets and
Authentication](/trading/wallets-auth#execute-gasless-transactions) for the
complete wallet setup and Relayer authorization flow.
```

Example 3 (text):
```text
    RELAYER_API_KEY="<relayer_api_key>"
    RELAYER_API_KEY_ADDRESS="<signer_address>"
```

Example 4 (text):
```text
See [Execute Gasless
Transactions](/trading/wallets-auth#execute-gasless-transactions) for the
complete wallet setup and Relayer authorization flow.
```

---

## Collateral Return

**URL:** https://docs.polymarket.com/trading/combos/collateral-return.md

**Contents:**
- How Collateral Return Works
- Return Collateral
- Handle a Truncated Plan
- Understand Residual Positions

Quoting Combos can be capital-intensive because pUSD may remain locked across related positions until every underlying market resolves. Collateral return identifies capital that no longer needs to remain locked and returns it as pUSD, making it available for new quotes while preserving any unmatched exposure.

Collateral return finds compatible Combo positions that offset one another. It decomposes those positions, merges complementary exposure back into pUSD, and leaves the remaining exposure in residual positions.

For example, let `Y(A)` and `N(A)` represent the YES and NO positions for market `A`, and let `A ^ B ^ C` represent a three-leg Combo. Suppose the wallet holds:

The first leg of each Combo can be decomposed:

`Y(A)` and `N(A)` are complementary, so they merge into 1 pUSD per matched share. The two `Y(…)` positions remain in the wallet, preserving its unmatched exposure to the other legs.

The workflow is plan-based: inspect the proposed position changes, execute that exact plan, wait for confirmation, and request another plan when more work remains.

You need a Relayer API key. See [Connect Your Account](/trading/wallets-auth#connect-your-account) to create one before continuing.

<Tabs> <Tab title="TypeScript"> Given a `SecureClient` configured with a Relayer API key, ensure the wallet has the required trading approvals:

<Tab title="Python"> Given an `AsyncSecureClient` configured with a Relayer API key, ensure the wallet has the required trading approvals:

<Tab title="API"> <Note> The following steps show the Deposit Wallet path. For Safe or Proxy Wallet flows, use an SDK or see the reference examples at the end of this tab. </Note>

The service limits how much work one transaction can contain. When more work remains, each plan is one complete, executable chunk—not a partial transaction. Execute and confirm each chunk before requesting the next plan because every new plan depends on the resulting onchain state.

<Tabs> <Tab title="TypeScript"> Use `plan.truncated` to determine whether more work remains after the current plan.

<Tab title="Python"> Use `plan.truncated` to determine whether more work remains after the current plan.

<Tab title="API"> After the submitted transaction confirms, inspect the `truncated` value from the plan that produced it. When it is `true`, request a fresh plan, inspect and sign its wallet action, submit it, and wait for confirmation again. Continue until the confirmed plan has `truncated: false`. </Tab> </Tabs>

Collateral return only removes exposure that can be recombined into collateral. Any unmatched exposure remains in new residual positions. These positions preserve the wallet's remaining economic exposure after the returned pUSD is removed.

For example, complementary exposure to one underlying leg may unlock pUSD while the rest of each Combo remains open. Inspect the created positions before execution and include them in your normal [Combo position sync](/trading/combos/market-makers#list-combo-positions) after confirmation.

**Examples:**

Example 1 (text):
```text
N(A ^ B ^ C)
N(N(A) ^ B ^ C)
```

Example 2 (text):
```text
N(A) + Y(A ^ N(B ^ C))
Y(A) + Y(N(A) ^ N(B ^ C))
```

Example 3 (text):
```text
    import { createSecureClient, relayerApiKey } from "@polymarket/client";
    import { privateKey } from "@polymarket/client/viem";

    const client = await createSecureClient({
      wallet: process.env.POLYMARKET_WALLET_ADDRESS,
      signer: privateKey(process.env.SIGNER_PRIVATE_KEY),
      apiKey: relayerApiKey({
        key: process.env.RELAYER_API_KEY!,
        address: process.env.RELAYER_API_KEY_ADDRESS!,
      }),
    });

    await client.setupTradingApprovals();
```

Example 4 (text):
```text
<Note>
  Collateral return supports Deposit Wallet, Safe Wallet, and Proxy Wallet
  accounts. EOA accounts are not supported.
</Note>

<Steps>
  <Step title="Request a Plan">
    First, request a plan based on the wallet's current Combo positions.

    ```ts theme={null}
    import type { CollateralReturnPlanResponse } from "@polymarket/client";

    const plan: CollateralReturnPlanResponse = await client.planCollateralReturn();
    ```

    <Accordion title="CollateralReturnPlanResponse">
      <CodeGroup>
        ```ts CollateralReturnPlanResponse Type theme={null}
        enum CollateralReturnKnownOperationKind {
          Split = "split",
          Merge = "merge",
          Redeem = "redeem",
          SplitOnCondition = "split_on_condition",
          MergeOnCondition = "merge_on_condition",
          SplitOnEvent = "split_on_event",
          MergeOnEvent = "merge_on_event",
          ConvertOnEvent = "convert_on_event",
          Extract = "extract",
          Inject = "inject",
          ConvertToYesBasket = "convert_to_yes_basket",
          MergeFromYesBasket = "merge_from_yes_basket",
          Compress = "compress",
        }

        type CollateralReturnOperationKind =
          | CollateralReturnKnownOperationKind
          | (string & {});

        type CollateralReturnOperation = {
          kind: CollateralReturnOperationKind;
          conditionId?: ComboConditionId;
          eventId?: EventId;
          positionId?: PositionId;
          conditionIndex: number;
          amount: DecimalString;
        };

        type CollateralReturnPositionAmount = {
          positionId: PositionId;
          amount: DecimalString;
        };

        type CollateralReturnPositionSummary = {
          consumed: CollateralReturnPositionAmount[];
          created: CollateralReturnPositionAmount[];
        };

        type CollateralReturnRouterCall = {
          to: EvmAddress;
          data: HexString;
        };

        type CollateralReturnPlanResponse = {
          planHash: HexString;
          chainId: number;
          wallet: EvmAddress;
          blockNumber: bigint;
          startingPusd: DecimalString;
          netPusdOut: DecimalString;
          finalPusd: DecimalString;
          operations: CollateralReturnOperation[];
          operationCount: number;
          truncated: boolean;
          estimatedCost: number;
          requiredPusdInput: DecimalString;
          requiredPositions: CollateralReturnPositionAmount[];
          positionSummary: CollateralReturnPositionSummary;
          candidatePositionIds: PositionId[];
          routerCall: CollateralReturnRouterCall;
        };
        ```

        ```json CollateralReturnPlanResponse Example theme={null}
        {
          "planHash": "<plan_hash>",
          "chainId": 137,
          "wallet": "<wallet_address>",
          "blockNumber": "74281963",
          "startingPusd": "5.000000",
          "netPusdOut": "1.000000",
          "finalPusd": "6.000000",
          "operations": [
            {
              "kind": "merge_on_condition",
              "conditionId": "<condition_id>",
              "positionId": "<position_id>",
              "conditionIndex": 0,
              "amount": "1.000000"
            }
          ],
          "operationCount": 1,
          "truncated": false,
          "estimatedCost": 240000,
          "requiredPusdInput": "0.000000",
          "requiredPositions": [
            {
              "positionId": "<position_id>",
              "amount": "1.000000"
            }
          ],
          "positionSummary": {
            "consumed": [
              {
                "positionId": "<position_id>",
                "amount": "1.000000"
              }
            ],
            "created": [
              {
                "positionId": "<residual_position_id>",
                "amount": "0.500000"
              }
            ]
          },
          "candidatePositionIds": [
            "<candidate_position_id_1>",
            "<candidate_position_id_2>"
          ],
          "routerCall": {
            "to": "<contract_address>",
            "data": "<calldata>"
          }
        }
        ```
      </CodeGroup>
    </Accordion>
  </Step>

  <Step title="Inspect the Plan">
    Next, inspect the plan before signing. It is an inspectable execution artifact,
    not just a transaction payload. Review its expected return and residual-position
    impact, and apply any application-specific limits.

    | Field                                     | What to inspect                                                      |
    | ----------------------------------------- | -------------------------------------------------------------------- |
    | `startingPusd`, `netPusdOut`, `finalPusd` | The expected pUSD return and resulting wallet balance.               |
    | `requiredPositions`                       | The Combo positions the plan requires.                               |
    | `operations`                              | The ordered position changes.                                        |
    | `positionSummary`                         | The positions consumed and the residual positions created.           |
    | `estimatedCost`                           | The estimated execution cost against any application-specific limit. |
    | `truncated`                               | Whether more work remains after this plan confirms.                  |
    | `routerCall`                              | The exact action that will be submitted.                             |
  </Step>

  <Step title="Execute the Inspected Plan">
    Finally, execute the inspected plan and wait for the transaction to confirm.

    ```ts theme={null}
    const handle = await client.executeCollateralReturnPlan({ plan });
    const outcome = await handle.wait();

    // outcome.transactionHash: TxHash
    ```

    `await handle.wait()` returns after the submitted plan's transaction confirms.
    Request another plan only then, because the next plan is calculated from the
    resulting onchain state.

    <Info>
      If execution fails, discard the plan and request a new one before retrying.
    </Info>
  </Step>
</Steps>
```

---

## How Combos Work

**URL:** https://docs.polymarket.com/trading/combos/overview.md

**Contents:**
- Build With Combos

Combos are multi-leg positions that combine multiple underlying market outcomes into one YES or NO position. Each Combo is defined by its legs and identified by derived YES and NO position IDs.

The request for quote (RFQ) system enables quote-based Combo execution between two participants: Polymarket users (requesters) and market makers (quoters). A user creates a Request, which starts an auction among connected market makers. Market makers compete by submitting Quotes: executable prices they are willing to fill.

<Note> Combo position IDs are complementary to CLOB token IDs. A user can trade the market on the CLOB or can include the market as a leg of a Combo. </Note>

Integrate Combos into market maker systems or builder apps that request executable prices for users.

<CardGroup cols={2}> <Card title="Market Makers" icon="chart-line" href="/trading/combos/market-makers"> Build a market maker integration for pricing and executing Combos. </Card>

<Card title="Builders" icon="arrows-rotate" href="/trading/combos/builders"> Request Combo quotes and execute accepted trades for users. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
sequenceDiagram
    autonumber
    participant Requester as Polymarket User
    participant RFQ as RFQ System
    participant Quoter as Market Maker
    participant Execution as Execution

    Requester->>RFQ: Request a Combo price
    RFQ->>Quoter: Send quote request
    activate Quoter
    Note right of Quoter: 400 ms max
    Quoter->>RFQ: Submit executable price
    deactivate Quoter
    RFQ->>Requester: Return best quote
    activate Requester
    Note left of Requester: 10 seconds max
    Requester->>RFQ: Accept quote
    deactivate Requester
    opt Last Look enabled
        RFQ->>Quoter: Request Last Look confirmation
        activate Quoter
        Note right of Quoter: 1 second max
        Quoter->>RFQ: Confirm fill
        deactivate Quoter
    end
    RFQ->>Execution: Execute accepted Combo
    Execution-->>Requester: Send execution update
    Execution-->>Quoter: Send execution update
    RFQ-->>Quoter: Broadcast confirmed trade
```

---
