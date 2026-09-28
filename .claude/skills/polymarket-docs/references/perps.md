# Polymarket-Docs_Docs - Perps

**Pages:** 21

---

## Perps Changelog

**URL:** https://docs.polymarket.com/changelog/perps.md

Notable changes to the Polymarket Perps API.

<Update label="Sep 27, 2026" description="Required fill fields, rewards date params, and instrument close-only statuses"> No breaking changes to order placement, cancellation, or authentication. Fill objects gain three required fields, and `GET /v1/account/rewards` now rejects `start*timestamp` / `end*timestamp` with `400`. Parsers should accept two new terminal order statuses and two new instrument fields for delisting. TWAP controls, position share-card snapshots, display symbols, and the builder-codes read surface are usable. TWAP order entry, chase limits, GTD, partial TP/SL closes, builder attribution, trailing stops, and synthetic pricing ship switched off. Expect one WebSocket reconnect and a short cancel-only window.

The market-maker gateway is briefly unavailable while its pods roll, so WebSocket connections to the MM gateway drop once and need to reconnect. The exchange is in cancel-only mode for the duration: cancels, liquidations, deposits, withdrawals, and funding keep working; new orders are rejected until the window closes. While cancel-only is on, a cancel that races an order's acceptance is answered `order*in*flight`; held cancels resume when the window closes. </Update>

<Update label="Sep 21, 2026" description="Reversal margin at worst executable price, rounded volume strings, and daily reward rows"> No breaking changes to order placement, cancellation, authentication, or market data. Orders that flip a position now reserve margin at the worst executable price, so some reversals that used to pass can return `insufficient_margin`. Volume, notional, and candle strings are correctly rounded, and daily liquidity and open-interest reward rows appear after 12:05 UTC. Trailing stop-loss, TWAP, and good-till-date are in this build but not enabled. Expect one WebSocket reconnect and a short cancel-only window.

The market-maker gateway is briefly unavailable while its pods roll, so WebSocket connections to the MM gateway drop once and need to reconnect. The exchange is in cancel-only mode for the duration: cancels, liquidations, deposits, withdrawals, and funding keep working; new orders are rejected until the window closes. While cancel-only is on, a cancel that races an order's acceptance is answered `order*in*flight`; held cancels resume when the window closes. </Update>

<Update label="Sep 17, 2026" description="Held cancels during accept, 503 on engine timeouts, and reduce-only displacement"> No breaking changes to order placement, authentication, or market data. Cancels that arrive while an order is still being accepted now succeed, several cancel and account routes return `503` instead of `500` when the engine times out, a more aggressive reduce-only order can displace your own less aggressive resting reduce-only orders, and isolated-margin accounts get a stricter check when a ladder could reverse a position. Market makers should see fewer connection errors on the MM REST host. Expect one WebSocket reconnect and a short cancel-only window.

The market-maker gateway is briefly unavailable while its pods roll, so WebSocket connections to the MM gateway drop once and need to reconnect. The exchange is in cancel-only mode for the duration: cancels, liquidations, deposits, withdrawals, and funding keep working; new orders are rejected until the window closes. While cancel-only is on, a cancel that races an order's acceptance is answered `order*in*flight` as before; held cancels resume when the window closes. </Update>

<Update label="Sep 15, 2026" description="Trading-key internal transfers within account groups; Retry-After on internal-transfer 503s"> No breaking changes. Trading keys can now move collateral between accounts in the same exchange-managed account group. Owner-signed internal transfers are unchanged.

<Update label="Sep 15, 2026" description="Gateway pod identity: x-pmp-pod response header and pod field on auth acknowledgements"> No changes to request shapes, authentication inputs, or existing response fields. Responses gain correlation metadata identifying the gateway pod that produced them, so your request logs can be matched against exchange logs.

<Update label="Sep 14, 2026" description="Non-paginated history routes reject cursor; 50-level book and leaderboard account-value sort"> No breaking changes to order placement, cancellation, authentication, or market data. Fourteen history and info routes now reject a `cursor` query parameter they used to ignore. Order-path latency should come back down after the September 8 increase, exact order lookups should return far fewer `503`s, and the index price for Hyperliquid-sourced instruments is corrected. Optional: a 50-level order book channel and an account-value sort on the leaderboard. Expect one WebSocket reconnect on the market-maker gateway during the maintenance window.

The market-maker gateway is briefly unavailable while its pods roll, so WebSocket connections to the MM gateway drop once and need to reconnect. The exchange is in cancel-only mode for the duration: cancels, liquidations, deposits, withdrawals, and funding keep working; new orders are rejected until the window closes. This release also moves the matching engine's sequencer to the new build, so plan for one reconnect and a short cancel-only period. </Update>

<Update label="Sep 8, 2026" description="Cancel-by-coid grace window, stricter filter validation, and faster rejected-order lookups"> Cancel-by-coid grace window, stricter filter validation, and faster rejected-order lookups. No breaking changes.

The market-maker gateway rolls pod by pod during the window, so MM WebSocket connections will drop once and need to reconnect. The exchange is in cancel-only mode for the duration: cancels, liquidations, deposits, withdrawals, and funding continue; new orders are rejected until the window closes. </Update>

<Update label="Sep 4, 2026" description="OI reward eligibility threshold increased to $5M"> The OI reward eligibility threshold is now $5M of combined daily average gross OI per rewards entity, up from $1M. Accounts without an entity mapping qualify independently. The 6% APR rate and calculation on the account's full daily average gross OI across all instruments are unchanged. </Update>

<Update label="Sep 2, 2026" description="Exchange statistics endpoint added"> Added `GET /v1/info/exchange-stats`, a public endpoint returning aggregate statistics for all pUSD-quoted perpetual markets over a required `[start*timestamp, end*timestamp)` window of up to 31 days: matched USD volume, gross positive maker and taker trading fees (rebates, incentives, and referral payments excluded), and one-sided open interest in USD notional with its sample time, taken from the latest complete sample before the window end — both null when no complete sample is available. Responses are cached for five minutes; a request costs weight 10, and a request served from cache costs 1. </Update>

<Update label="Sep 1, 2026" description="Concurrent WebSocket posts and HTTP overload shedding"> Concurrent WebSocket posts and HTTP overload shedding. No breaking changes.

The public gateway fleet moves to dedicated hardware during this window. WebSocket connections drop once; standard reconnects cover it. </Update>

<Update label="Aug 24, 2026" description="Response timestamps, rejection references, and liquidation metadata"> Rejections and acknowledgements now carry inspectable timing, every WebSocket push is stamped with engine event time, and backstop liquidation fills include optional metadata.

| Field         | Meaning              | | ------------- | -------------------- | | Request `ts`  | Client send time     | | `arts`        | Gateway arrival time | | Item `ts`     | Engine decision time | | Envelope `ts` | Server send time     | | `ets`         | Engine event time    | </Update>

<Update label="Aug 16, 2026" description="Current position fills endpoint added"> Added `GET /v1/info/position-fills`, a public endpoint returning every fill in a registered account's current open position cycle for one instrument. A cycle begins when the position opens from flat or flips direction, and a multi-leg flip stays in one cycle. Pages of up to 100 fills are linked by an opaque `cursor` returned alongside the data; the cursor is validated against the live position on every page and returns `400` if the position changed mid-pagination. `GET /v1/account/fills` has returned the same opaque `cursor` field since Jul 24 — passing the last fill's trade ID as `cursor` still works there. </Update>

<Update label="Aug 14, 2026" description="Equity and PnL history honour the requested interval"> `GET /v1/account/equity` and `GET /v1/account/pnl` now bucket the returned series by the `interval` query parameter. Previously the parameter was validated but ignored: every accepted value returned the same fixed-granularity series (per minute for equity, per hour for PnL), and long windows were truncated at 1000 rows instead of aggregated. Each equity point is now the last sample in its interval bucket; each PnL point is the PnL realized inside its bucket — not a running total — and empty buckets are omitted. Buckets are aligned to the Unix epoch, points keep real sample timestamps, and the 1000-entry cap now counts buckets, so a coarser interval covers a longer window before `more` is set. Responses for the finest intervals (`1m` equity, `1h` PnL) are unchanged. </Update>

<Update label="Aug 13, 2026" description="Deposit and withdrawal history amounts are always decimal token units"> `GET /v1/account/deposits` and `GET /v1/account/withdrawals` now serialize every `amount` (and withdrawal `fee`) in decimal token units, e.g. `"10"` for 10 pUSD. Previously, deposit rows in `pending` or `removed` status reported raw on-chain base units (`"10000000"` for the same 10 pUSD), and pending withdrawal rows could serve base-unit amounts and fees as well, so rows for the same transfer disagreed on units across statuses. Clients that divided pending amounts by `10^decimals` to compensate must drop that conversion. Confirmed rows and the WebSocket `deposits` and `withdrawals` channels are unchanged — they were already decimal. Signed operation inputs (`POST /v1/account/withdraw`) still take base-unit amounts matching the EIP-712 signature. </Update>

<Update label="Aug 11, 2026" description="Fill history flags maker fills executed under liquidation"> `GET /v1/account/fills` and account trade history previously reported `liquidation: false` on every maker fill, even when the maker's own account was under liquidation on the instrument — while the WebSocket `fills` channel already reported `liq: true` for the same fill. The two surfaces now agree: any maker or taker fill on an instrument in the account's active liquidation scope reports `liquidation: true`. Rows written before the change are unaffected. Such maker legs are also excluded from leaderboard win counts. </Update>

<Update label="Aug 10, 2026" description="Fills gain an adl flag; liq no longer set on ADL counterparty legs"> Fill entries now carry a required boolean `adl` field on both the WebSocket `fills` channel and `GET /v1/account/fills`, set on both legs of an auto-deleveraging match. Behavior change: the counterparty leg of an ADL match previously reported `liq: true` on the WebSocket `fills` channel; it now reports `liq: false`. `liq` marks only the leg whose own position is being liquidated. Clients that detect forced closes via `liq` alone will no longer see ADL counterparty fills — check `adl` as well. </Update>

<Update label="Aug 8, 2026" description="Position deleveraged notification added"> Added the <code>position\_deleveraged</code> notification, sent to the counterparty of an auto-deleveraging match when its profitable position is closed or reduced to settle a liquidation on the other side. Delivered on the WebSocket <code>notifications</code> channel and in the notifications history. </Update>

<Update label="Aug 7, 2026" description="Exchange info reports engine version and cancel-only state"> `GET /v1/info/exchange` now includes `engine*version`, the engine release version of the build serving the response. The response also documents `cancel*only`, which reports whether the exchange is in cancel-only (maintenance) mode; the flag has been returned since maintenance mode shipped on Jul 15. </Update>

<Update label="Aug 6, 2026" description="Portfolio margin summary includes available order margin"> The portfolio response and <code>portfolio</code> WebSocket channel now include <code>margin.available\*order\*margin</code>: the collateral available for additional order initial margin after existing exposure, open orders, orders and isolated-margin additions awaiting risk processing, and pending withdrawals or transfers. </Update>

<Update label="Jul 6, 2026" description="Cancel all orders added"> Added <code>DELETE /v1/trade/orders/all</code> to cancel all open orders in one request, optionally scoped to a single instrument. Available in the SDKs as <code>cancelAllOrders</code> (TypeScript) and{" "} <code>cancel\*all\*orders</code> (Python). </Update>

<Update label="Jun 11, 2026" description="Cancel responses include order IDs"> Cancel responses now include `oid` and `coid` fields. </Update>

<Update label="Jun 10, 2026" description="Taker delay added for immediately matching orders"> Added a 20ms taker delay for orders that immediately match on entry. </Update>

<Update label="Jun 9, 2026" description="Reduce-only orders added"> Added the reduce-only field to order submission and order updates. </Update>

<Update label="Jun 8, 2026" description="Auto-cancel and rate-limit updates"> <ul> <li> Added <code>PATCH /v1/trade/auto-cancel</code> to arm or clear a dead man's switch that cancels all open orders at a specified time. </li>

**Examples:**

Example 1 (text):
```text
`GET /v1/account/fills`, `GET /v1/info/fills`, `GET /v1/info/trades`,
and the WebSocket `fills` channel now includes `settlement` (boolean
— `true` only for a position closed by instrument settlement),
`builder_fee` (string, `"0"` until builder codes are enabled), and
`total_fee` (string — exchange fee plus builder fee). `pnl` is
unchanged: realized PnL before fees; subtract `total_fee` once for
the net result. Strict schema validators must add the three fields.
```

Example 2 (text):
```text
`end_timestamp`.** They were previously ignored; they now return
`400` with `invalid start_timestamp` / `invalid end_timestamp`. Use
`date`, `start_date`, and `end_date`.
```

Example 3 (text):
```text
`instrument_settled`.** Operators can put an instrument into
close-only — orders that would increase exposure are rejected with
`instrument_close_only`, resting increase-exposure orders are
canceled with that status, reduce-only trading continues — and later
settle and delist it. Remaining positions close at the trailing
30-minute time-weighted index average with no fee; remaining orders
cancel with `instrument_settled`; further orders are rejected with
`instrument_settled`. Settlement fills arrive as normal fills with
`settlement: true`. Nothing is delisted by this release. Add the
statuses now so strict parsers do not fail the first time it happens.
```

Example 4 (text):
```text
(boolean, always present) and `settlement` (object with `sequence`,
`timestamp`, `price`, `insurance_debit`; present only after
settlement). Instruments may also carry an optional `display_symbol`;
`symbol` is unchanged.
```

---

## Authenticated Sessions

**URL:** https://docs.polymarket.com/perps/authenticated-sessions.md

**Contents:**
- Set Up Perps Access
- Session Lifecycle
- Resume a Session

An authenticated session is a two-way authenticated communication channel with the Perps system that allows your app to place orders, read private Perps account data, and receive private real-time updates.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Create a Secure Client"> Create a `SecureClient` for the Polymarket wallet that owns the Perps account, using the signer that controls it.

<Tab title="Python"> <Steps> <Step title="Create a Secure Client"> Create an `AsyncSecureClient` for the Polymarket wallet that owns the Perps account, using the signer that controls it.

<Tab title="API"> Start by registering new proxy credentials for an existing Polymarket account. If you do not have one yet, create an account at [polymarket.com](https://polymarket.com) first.

Open an authenticated session to start trading, read private Perps account data, and receive private real-time updates.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Listen for Session Events"> After opening a Perps session, iterate over it to receive private real-time updates.

<Tab title="Python"> <Steps> <Step title="Listen for Session Events"> After opening a Perps session, iterate over it to receive private real-time updates.

<Tab title="API"> <Steps> <Step title="Authenticate a WebSocket Connection"> Connect to the Perps WebSocket production URL.

Resume a session when stored credentials are still valid and a Perps workflow needs to continue in a new runtime context.

<Tabs> <Tab title="TypeScript"> Read `session.credentials` after opening a session and store the object in secure credential storage.

<Tab title="Python"> Read `session.credentials` after opening a session and store the object in secure credential storage.

<Tab title="API"> Resume an API session by reusing stored proxy credentials while they are still valid.

**Examples:**

Example 1 (text):
```text
        import { createSecureClient } from "@polymarket/client";
        import { privateKey } from "@polymarket/client/viem";

        const client = await createSecureClient({
          wallet: process.env.POLYMARKET_WALLET_ADDRESS!,
          signer: privateKey(process.env.PRIVATE_KEY!),
        });
```

Example 2 (text):
```text
    <Note>
      This example uses Viem for wallet signing. See the [TypeScript tooling
      guide](/getting-started/typescript#wallet-integrations) for other wallet library
      integrations.
    </Note>
  </Step>

  <Step title="Open a Perps Session">
    Open a Perps session. By default, delegated Perps credentials expire after one
    week.

    ```ts theme={null}
    const session = await client.openPerpsSession();
    ```

    You can also set the session lifetime and label explicitly. `expiresIn` is
    measured in milliseconds.

    ```ts theme={null}
    const session = await client.openPerpsSession({
      expiresIn: 7 * 24 * 60 * 60 * 1000,
      label: "trading-app",
    });
    ```
  </Step>
</Steps>
```

Example 3 (text):
```text
        import os

        from polymarket import AsyncSecureClient

        client = await AsyncSecureClient.create(
            private_key=os.environ["PRIVATE_KEY"],
            wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
        )
```

Example 4 (text):
```text
  </Step>

  <Step title="Open a Perps Session">
    Open a Perps session. By default, delegated Perps credentials expire after one
    week.

    ```python theme={null}
    session = await client.open_perps_session()
    ```

    You can also set the session lifetime and label explicitly. `expires_in` is a
    `timedelta`.

    ```python theme={null}
    from datetime import timedelta

    session = await client.open_perps_session(
        expires_in=timedelta(days=7),
        label="trading-app",
    )
    ```
  </Step>
</Steps>
```

---

## Realtime Updates

**URL:** https://docs.polymarket.com/perps/realtime-updates.md

**Contents:**
- Best Bid and Offer
- Order Book
- Trades
- Tickers
- Statistics
- Candles

Stream public market data as prices, books, trades, candles, tickers, and market statistics change.

<Note> Private order, fill, and account-state reconciliation is covered in [Reconcile Trade State](/perps/trading#reconcile-trade-state). </Note>

Start with the stream that matches the view you are building. Subscribe to the updates you need, read events while the view is active, then stop the stream when the view no longer needs live data.

<Tabs> <Tab title="TypeScript"> Subscribe from a `PublicClient` or `SecureClient` and iterate over the merged event stream.

<Tab title="Python"> Subscribe from an `AsyncPublicClient` or `AsyncSecureClient` and iterate over the merged event stream.

<Tab title="API"> Connect to the Perps WebSocket production URL.

Use best bid and offer updates for top-of-book quotes.

<Tabs> <Tab title="TypeScript"> Subscribe to best bid and offer updates for one instrument.

<Tab title="Python"> Subscribe to best bid and offer updates for one instrument.

<Tab title="API"> Subscribe to best bid and offer updates for one instrument.

Use order book updates for depth across bid and ask price levels.

<Tabs> <Tab title="TypeScript"> Subscribe to order book updates for one instrument.

<Tab title="Python"> Subscribe to order book updates for one instrument.

<Tab title="API"> Subscribe to order book updates for one instrument.

Use trades to update recent-print lists, last-trade displays, or execution-based analytics.

<Tabs> <Tab title="TypeScript"> Subscribe to public trade updates for one instrument.

<Tab title="Python"> Subscribe to public trade updates for one instrument.

<Tab title="API"> Subscribe to public trade updates for one instrument.

Use ticker updates for the current mark, index, last price, open interest, and funding state.

<Tabs> <Tab title="TypeScript"> Subscribe to ticker updates for one instrument or all active instruments.

<Tab title="Python"> Subscribe to ticker updates for one instrument or all active instruments.

<Tab title="API"> Subscribe to ticker updates for one instrument or all active instruments.

Use statistics for 24-hour volume, opening price, and the rolling kline window.

<Tabs> <Tab title="TypeScript"> Subscribe to 24-hour statistics for one instrument or all active instruments.

<Tab title="Python"> Subscribe to 24-hour statistics for one instrument or all active instruments.

<Tab title="API"> Subscribe to 24-hour statistics for one instrument or all active instruments.

Use candles to update charts with live OHLCV data.

<Tabs> <Tab title="TypeScript"> Subscribe to candle updates for one instrument and interval.

<Tab title="Python"> Subscribe to candle updates for one instrument and interval.

<Tab title="API"> Subscribe to candle updates for one instrument and interval.

**Examples:**

Example 1 (text):
```text
    import { createPublicClient } from "@polymarket/client";

    const client = createPublicClient();

    const stream = await client.subscribe([
      { topic: "perps.bbo", instrumentId: 1 },
      { topic: "perps.trades", instrumentId: 1 },
    ]);

    for await (const event of stream) {
      switch (event.type) {
        case "bbo":
          // event: PerpsBboEvent
          break;
        case "trade":
          // event: PerpsTradeEvent
          break;
      }

      if (shouldClose) {
        await stream.close();
      }
    }
```

Example 2 (text):
```text
The stream yields typed events for each subscription and can be closed when the
live view no longer needs updates.
```

Example 3 (text):
```text
    from polymarket import AsyncPublicClient
    from polymarket.streams import PerpsBboSpec, PerpsTradesSpec

    client = AsyncPublicClient()

    stream = await client.subscribe(
        [
            PerpsBboSpec(instrument_id=1),
            PerpsTradesSpec(instrument_id=1),
        ]
    )

    async for event in stream:
        if event.type == "bbo":
            # event: PerpsBboEvent
            pass
        elif event.type == "trade":
            # event: PerpsTradeEvent
            pass

        if should_close:
            await stream.close()
```

Example 4 (text):
```text
The stream yields typed events for each subscription and can be closed when the
live view no longer needs updates.
```

---

## FAQ

**URL:** https://docs.polymarket.com/perps/faq.md

**Contents:**
- General
- Trading and Orders
- Pricing, Mark, Index, and Funding
- Margin and Leverage
- Liquidation
- Fees
- API and Integration
- Sessions

Common questions about Polymarket Perps.

<AccordionGroup> <Accordion title="What is Polymarket Perps?"> Polymarket Perps is a perpetual futures exchange offering continuous exposure to equities, indices, commodities, and other underlyings. Positions have no expiry. A funding rate keeps the contract price tethered to the underlying's spot price over time. </Accordion>

<Accordion title="Which instruments can I trade?"> Fetch the current product list, symbols, underlyings, reference feeds, and leverage settings from [`GET /v1/info/instruments`](/perps/market-data#fetch-instruments). </Accordion>

<Accordion title="Is the exchange on-chain or off-chain?"> Hybrid. Order matching, margin, and funding run off-chain for low latency. Deposits and withdrawals settle on Polygon, and the exchange periodically posts state-root commitments on-chain so off-chain activity stays verifiable. </Accordion>

<Accordion title="Does the perp trade 24/7, even when the underlying market is closed?"> Yes. The order book, matching, funding, margin checks, and liquidations all run continuously. What changes outside of regular hours is the set of external feeds used to compute Index and Mark. </Accordion>

<Accordion title="Do Polymarket Perps expire?"> No. Perpetual futures have no expiration date. A Perps position stays open until you close it or it is force-closed by liquidation. </Accordion>

<Accordion title="Are perps and perpetual futures the same thing?"> Yes. "Perps" is trader shorthand for "perpetual futures." Both refer to the same derivative contract: a futures-style instrument with no expiry, anchored to the underlying's spot price through periodic funding. </Accordion>

<Accordion title="How are Perps different from Polymarket prediction markets?"> Polymarket's prediction markets settle Yes or No shares at \$1 or \$0 based on a discrete event outcome. Perps are continuous: there is no event resolution and no \$0/\$1 settlement. Instead you take a long or short position whose value moves with the underlying asset's price, subject to funding payments and margin requirements like any perpetual futures contract. </Accordion> </AccordionGroup>

<AccordionGroup> <Accordion title="What order types are supported?"> Limit and market-style orders are supported with GTC, IOC, and FOK time-in-force values. GTC orders can be tagged post-only, which rejects the order if it would take liquidity. Closing orders can be tagged reduce-only, which prevents the order from increasing exposure. See [Configure Order Behavior](/perps/trading#configure-order-behavior) and [Close a Position](/perps/trading#close-a-position). </Accordion>

<Accordion title="Why was my order rejected when my balance looks fine?"> Pre-trade margin uses the worst-case position size from your existing exposure plus all resting orders on each side, not just the current position.

<Accordion title="What is self-trade prevention?"> Self-trade prevention is on by default for every order and runs in CancelMaker mode: when a taker would match against a resting order on the same account, the conflicting resting maker is canceled and the taker continues matching against other makers. It is not an API setting. There is no way to turn it off or change its mode. Accounts that Polymarket has grouped as one entity count as the same account for this check. See [Self-Trade Prevention](/perps/learn-about-trading/self-trade-prevention). </Accordion> </AccordionGroup>

<AccordionGroup> <Accordion title="What's the difference between Mark Price, Index Price, and last trade price?">

<Accordion title="What happens to Mark when external feeds go down?"> Each Mark candidate degrades gracefully to the Index. If the order book mid is missing, the candidate falls back to Index. If there are no recent trades or quotes, the candidate falls back to Index. If external mark feeds are unavailable, the candidate falls back to Index. In the worst case, all candidates converge to Index and Mark tracks Index directly. </Accordion>

<Accordion title="How is funding calculated and when does it settle?"> A premium index is sampled every 5 seconds by walking the book for 1,000 quote-asset notional on each side. Samples are averaged over a 1-hour charge window, run through an 8-hour formula with a fixed interest leg and clamp, divided by 8, and capped at +/-4% per hour. Settlement happens once per window. Longs pay shorts when the rate is positive, and shorts pay longs when negative. The protocol takes no cut. </Accordion>

<Accordion title="Can I see funding pressure between settlements?"> Yes. A rolling 5-second premium sample and its implied 8-hour rate are published continuously through public market data. You can also read funding history with [`GET /v1/info/funding`](/perps/market-data#list-funding-history). </Accordion> </AccordionGroup>

<AccordionGroup> <Accordion title="What's the difference between cross and isolated margin?">

<Accordion title="What is the maximum leverage?"> For crypto, SP500, Oil, Gold and Silver we offer up to 20x leverage, RWA in general up to 10x leverage. </Accordion>

<Accordion title="What are leverage tiers and why does my margin go up as my position grows?"> Tiers cap the maximum leverage available as position notional grows. Building a larger position requires lowering your leverage setting, which raises the initial margin rate on your entire position — the cap is not applied bracket by bracket. Tiers affect initial margin only; the maintenance margin rate is flat per market. Fetch live tier values from [`GET /v1/info/instruments`](/perps/market-data#fetch-instruments). </Accordion>

<Accordion title="How is maintenance margin set?"> The maintenance margin rate is flat per market: `MMR = 0.5 / max_leverage`, independent of position size and of your leverage setting — for example, 2.5% on a 20x market. It equals half the initial margin rate at maximum leverage, so a max-leverage position is liquidated only after losing roughly half of its posted margin; at lower leverage the buffer between entry margin and liquidation is larger. </Accordion>

<Accordion title="What happens between margin call and liquidation?"> Three states are evaluated continuously.

<Accordion title="Can I withdraw collateral while I have an open position?"> Yes, but withdrawals must leave the greater of existing collateral reservations and 10% of total open-position notional at Mark Price. Orders awaiting risk checks also reserve margin. A \$100 position at 20x needs \$5 initial margin but a \$10 withdrawal reserve, excluding fees and other obligations. See [Withdrawal Margin Requirements](/perps/learn-about-trading/margin#withdrawal-margin-requirements) for the formula and example. </Accordion> </AccordionGroup>

<AccordionGroup> <Accordion title="When am I liquidated?"> Liquidation occurs when account equity falls below maintenance margin. Cross and isolated positions are checked independently: each isolated position has its own equity and maintenance margin, while cross uses the account's combined equity and combined maintenance margin. See [Margin and Liquidation](/perps/concepts#margin-and-liquidation). </Accordion>

<Accordion title="Why does my liquidation price move when I haven't changed anything?"> For cross positions, the liquidation price depends on available balance: everything in the cross account that is not this position's own equity. Mark moves on other cross positions, size changes, or collateral changes can all shift the liquidation price for every cross position simultaneously. </Accordion>

<Accordion title="What happens during liquidation?"> The affected scope is flagged and new orders on it are blocked. Cross blocks the whole account. Isolated blocks just that instrument. The system closes positions with reduce-only IOC orders, rate-limited per account, re-evaluating margin between fills. Cross liquidation closes one position at a time across cycles. If equity recovers above the recovery initial margin, the flag clears. </Accordion>

<Accordion title="What is the insurance fund and when does it step in?"> When equity falls below two-thirds of maintenance margin, order-book liquidation is unlikely to recover value, so the system absorbs the position directly into the insurance-fund account along with its margin. For cross backstop, the system absorbs all cross positions plus quote balance. </Accordion>

<Accordion title="Are there extra fees on liquidation fills?"> Yes. While flagged, every fill pays an additional liquidation fee rate on top of the maker or taker rate.

</Accordion> </AccordionGroup>

<AccordionGroup> <Accordion title="What are the current maker and taker fees?"> Fees are tiered by trailing 30-day trading volume. New accounts start at the \$0 tier and move up as their volume crosses each threshold. Fee tiers are re-evaluated every UTC day.

</Accordion> </AccordionGroup>

<AccordionGroup> <Accordion title="What's the difference between my main wallet and the proxy?"> Your main wallet signs the one-time create-proxy request and never trades directly. The returned proxy address and secret are what you use day to day: the proxy private key signs trade requests, and the `(proxy, secret)` pair authenticates private REST and WebSocket reads. This isolates the trading key from the wallet that holds funds. See [Set Up Authentication](/perps/authenticated-sessions#set-up-authentication). </Accordion>

<Accordion title="What address identifies my Perps account?"> Your account is keyed by your EOA base address, the externally-owned account that signs `createProxy`, not a Safe smart-contract wallet address. Even if you use a Safe wallet elsewhere on Polymarket, your Perps balances, positions, and history are all tracked against the underlying EOA. Use that EOA when looking up your account or referencing it in support requests. </Accordion>

<Accordion title="How do I avoid clock-skew rejections?"> Each signed request must include a fresh `ts` request timestamp in milliseconds and `salt`. Reused or stale values are rejected. Sync against `GET /v1/info/time` and do not sign requests far in the past or future. The optional `expa` field caps the validity window. </Accordion>

<Accordion title="How do deposits and withdrawals work?"> Deposits and withdrawals are the only operations that move assets in or out of the exchange. Both settle on Polygon. Deposits credit equity as soon as the engine sees them. Withdrawals are signed off-chain and must satisfy the [withdrawal margin requirements](/perps/learn-about-trading/margin#withdrawal-margin-requirements), including the 10% notional floor. See [Fund Your Account](/perps/fund-your-account). </Accordion>

<Accordion title="Are there geographic restrictions on order placement?"> Yes. Order placement is not permitted from the United States, Canada, Cuba, Iran, North Korea, Syria, Crimea, Donetsk, or Luhansk. Builders are responsible for verifying user location before submitting orders. </Accordion> </AccordionGroup>

<AccordionGroup> <Accordion title="What do market sessions actually change?"> Sessions affect which set of external feeds is used to compute Index Price and Mark Price. They do not change funding, margin, leverage tiers, order matching, or liquidation triggers. Those run identically around the clock. </Accordion>

<Accordion title="What's the difference between Disrupted and Halted?">

</Accordion> </AccordionGroup>

**Examples:**

Example 1 (text):
```text
    WorstCaseSize = max(|Position + OpenBuys|, |Position - OpenSells|)
```

Example 2 (text):
```text
If `Equity < IM_required` for that worst case, the order is rejected even though current equity is comfortable.
```

Example 3 (text):
```text
* Mark Price is the price the system uses for margin, PnL, liquidation, and funding.
* Last trade price is the price of the most recent fill on the local book. It is not used for margining.

See [Prices](/perps/concepts#prices).
```

Example 4 (text):
```text
* Cross margin shares account collateral across all cross positions. Unrealized PnL on one position can offset margin on another, but a liquidation evaluates and can unwind the whole cross account.

The web app opens new positions in isolated mode by default. Cross is opt-in through the API using leverage configuration, and only for instruments that allow it: some markets are isolated-only and reject cross margin. Instrument data shows which margin modes each market supports. See [Update Leverage](/perps/trading#update-leverage) and [Fetch Instruments](/perps/market-data#fetch-instruments).
```

---

## Place Your First Trade

**URL:** https://docs.polymarket.com/perps/place-your-first-trade.md

This guide walks through the shortest safe path to a first Perps trade. You will set up a Perps account, add collateral, and place a small buy order.

You need a Polymarket account with pUSD available before you start. Create one at [polymarket.com](https://polymarket.com).

<Note> Building directly against the API? Start with [Authenticated Sessions](/perps/authenticated-sessions), then use [Fund Your Account](/perps/fund-your-account) and [Trading](/perps/trading). </Note>

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Install the SDK"> Install the Unified TypeScript SDK with the package manager of your choice.

<Tab title="Python"> <Steps> <Step title="Install the SDK"> Install the Unified Python SDK with the package manager of your choice.

**Examples:**

Example 1 (javascript):
```javascript
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
      guide](/getting-started/typescript#wallet-integrations) for other wallet library
      integrations.
    </Note>
  </Step>

  <Step title="Create a Secure Client">
    Create a `SecureClient` with the wallet and signer that owns the Perps account.
    Include a Relayer API key so the SDK can submit gasless transactions.

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

    Create a [Relayer API key](https://polymarket.com/settings?tab=api-keys) from
    polymarket.com → Settings → API Keys.
  </Step>

  <Step title="Fund the Account">
    Set up the approvals required for Perps collateral deposits, then deposit pUSD
    from the user's Polymarket wallet into the Perps account. The minimum Perps
    deposit is 10 pUSD. Amounts use raw pUSD base units, so 10 pUSD is
    `10_000_000n`.

    ```ts theme={null}
    await client.setupTradingApprovals();

    const deposit = await client.depositToPerps({
      amount: 10_000_000n,
    });

    await deposit.wait();
    ```

    `deposit.wait()` confirms that the chain transaction settled. Perps may take a
    moment to credit the account after that. See [Fund Your
    Account](/perps/fund-your-account) for the full funding workflow.
  </Step>

  <Step title="Open a Perps Session">
    Open a Perps session for private reads and trading.

    ```ts theme={null}
    const session = await client.openPerpsSession();
    ```
  </Step>

  <Step title="Choose a Market">
    Fetch the available Perps instruments and choose the market you want to trade.

    ```ts theme={null}
    const instruments = await client.fetchPerpsInstruments();
    const instrument = instruments.find(
      (instrument) => instrument.symbol === "SP500-USD",
    );

    if (instrument === undefined) {
      throw new Error("Instrument not found.");
    }
    ```
  </Step>

  <Step title="Place the Order">
    Place a long buy order for `1` quantity unit of `SP500-USD` with an explicit
    limit price of `100` USD per quantity unit and immediate-or-cancel execution.

    ```ts theme={null}
    import { OrderSide, PerpsTimeInForce } from "@polymarket/client";

    const order = await session.placeOrder({
      instrumentId: instrument.id,
      side: OrderSide.BUY,
      quantity: "1",
      price: "100",
      timeInForce: PerpsTimeInForce.IOC,
    });

    // order.id: PerpsOrderId
    ```

    The returned order includes the accepted order state. See
    [Trading](/perps/trading) for direction, order behavior, cancellation, and state
    reconciliation.
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
    Create an `AsyncSecureClient` with the wallet and signer that owns the Perps
    account. Include a Relayer API key so the SDK can submit gasless transactions.

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

    Create a [Relayer API key](https://polymarket.com/settings?tab=api-keys) from
    polymarket.com → Settings → API Keys.
  </Step>

  <Step title="Fund the Account">
    Set up the approvals required for Perps collateral deposits, then deposit pUSD
    from the user's Polymarket wallet into the Perps account. The minimum Perps
    deposit is 10 pUSD. Amounts use raw pUSD base units, so 10 pUSD is `10_000_000`.

    ```python theme={null}
    await client.setup_trading_approvals()

    deposit = await client.deposit_to_perps(amount=10_000_000)

    await deposit.wait()
    ```

    `deposit.wait()` confirms that the chain transaction settled. Perps may take a
    moment to credit the account after that. See [Fund Your
    Account](/perps/fund-your-account) for the full funding workflow.
  </Step>

  <Step title="Open a Perps Session">
    Open a Perps session for private reads and trading.

    ```python theme={null}
    session = await client.open_perps_session()
    ```
  </Step>

  <Step title="Choose a Market">
    Fetch the available Perps instruments and choose the market you want to trade.

    ```python theme={null}
    instruments = await client.fetch_perps_instruments()
    instrument = next(
        (item for item in instruments if item.symbol == "SP500-USD"),
        None,
    )

    if instrument is None:
        raise RuntimeError("Instrument not found.")
    ```
  </Step>

  <Step title="Place the Order">
    Place a long buy order for `1` quantity unit of `SP500-USD` with an explicit
    limit price of `100` USD per quantity unit and immediate-or-cancel execution.

    ```python theme={null}
    result = await session.place_order(
        instrument_id=instrument.id,
        side="BUY",
        quantity="1",
        price="100",
        time_in_force="ioc",
    )

    # result.order.id: PerpsOrderId
    ```

    The returned order includes the accepted order state. See
    [Trading](/perps/trading) for direction, order behavior, cancellation, and state
    reconciliation.
  </Step>
</Steps>
```

---

## Self-Trade Prevention

**URL:** https://docs.polymarket.com/perps/learn-about-trading/self-trade-prevention.md

**Contents:**
- How it works
- Account groups

Self-trade prevention (STP) stops your orders from filling against your own resting orders. It runs on the matching engine for every order, it is not an order parameter, and it cannot be disabled or changed per order.

Before a taker matches, the engine checks whether the resting maker it would hit belongs to the same party. Every order submitted through the API runs in **CancelMaker** mode: the conflicting resting order is canceled and the taker keeps matching against the rest of the book. The canceled resting order is reported with status `stp_cancelled`, the same status you see in the order tables under [Trading](/perps/trading).

The engine also implements **CancelTaker** and **CancelBoth** modes, which are used internally by the exchange and are not available to API orders.

STP acts on resting orders that are eligible to match. A resting order priced outside the instrument's mark-relative price band cannot be matched by anyone, so a crossing order of yours does not cancel it; it stays on the book, keeps its margin reserved, and counts toward your open-order limit until you cancel it or the mark moves back into range.

Polymarket can group several accounts that are controlled by one entity, for example a market maker running separate accounts for separate strategies. Groups are assigned by Polymarket on request. There is no public API to create, inspect, or change them, and group membership is never visible to other users or in public endpoints.

For STP, **accounts in a group count as the same party**. An order from one member that would match another member's resting order cancels that resting order and continues matching against the rest of the book, exactly as if both orders were on one account. Resting take-profit and stop-loss exits behave like any other resting order of yours: a group-mate's crossing order cancels them just as your own would, and a canceled exit does not re-arm.

Grouping changes nothing else about how the accounts trade. Balances, margin, positions, liquidation, rate limits, open-order limits and auto-cancel remain strictly per account. Two things do follow group membership besides STP:

any member with no explicit per-instrument setting, including future listings. Your own explicit settings always take precedence. See [Margin](/perps/learn-about-trading/margin).

trading key registered to one member can move collateral to another member of the same group. Owner keys are never restricted by groups, and withdrawals always require the owner key.

When Polymarket changes a group's membership, orders that were being matched at that instant are re-evaluated by the engine against the new membership before any result is published, so a fill or cancellation can never be based on stale membership. You do not see a distinct error for this; the order simply resolves under the new membership.

To have accounts grouped, contact Polymarket with the list of accounts that belong to the entity.

---

## Concepts

**URL:** https://docs.polymarket.com/perps/concepts.md

**Contents:**
- Instruments
- Perps Accounts
- Prices
- Orders And Fills
- Trading Positions
- Margin And Liquidation
- Funding Payments
- Realtime Account State

Perps trading depends on how order fills create or change positions, how prices affect account equity, and how collateral supports trading risk. The concepts below describe the moving parts that determine what an account can trade and when a position is at risk.

An instrument identifies a Perps market: a tradable perpetual contract that tracks an underlying asset such as the S\&P 500 Index, gold, or bitcoin. Each instrument carries the information needed to identify the market and the rules for trading it.

| Attribute           | Meaning                                                                                        | | ------------------- | ---------------------------------------------------------------------------------------------- | | ID                  | The instrument identifier used in market data and orders                                       | | Symbol              | A short market label, such as `SP500-USD`, `GOLD-USD`, or `BTC-USD`                            | | Underlying asset    | The asset or index the market tracks, such as the S\&P 500 Index, gold, or bitcoin             | | Collateral asset    | The asset used to fund Perps accounts and support open positions. Polymarket Perps use pUSD.   | | Trading constraints | Market-specific rules such as price precision, quantity precision, order limits, and leverage. |

A Perps account is tied to a signer account. The signer account controls private actions such as trading and withdrawals.

The Perps account holds the state created by those actions: collateral, open positions, orders, fills, and history. Later sections explain how those pieces change as orders execute, prices move, and funding payments settle.

Perps accounts are funded through onchain collateral deposits.

<Note> If you're building on Perps, delegated credentials let your app act for the Perps account without using the owner key for every private action. See [Authenticated Sessions](/perps/authenticated-sessions). </Note>

A Perps market has two broad categories of prices: execution prices and calculated prices. Execution prices come from trades in the order book. Calculated prices are produced by Polymarket and used for reference, margin, and liquidation checks.

This separation matters because one small or isolated trade should not be able to change an account's risk state or trigger liquidation by itself.

| Price        | Category         | Meaning                                                    | Used for                                            | | ------------ | ---------------- | ---------------------------------------------------------- | --------------------------------------------------- | | Traded price | Execution price  | The price of an executed order book fill                   | Trade history and execution records                 | | Index price  | Calculated price | Polymarket's estimate of the underlying asset's fair value | Reference price and price anchoring                 | | Mark price   | Calculated price | The price used to value positions                          | Unrealized PnL, margin checks, and liquidation risk |

Calculated prices are computed from external price feeds. The feed set can change with market sessions, such as regular hours, overnight trading, and weekends, while funding, margin, and liquidation rules stay the same around the clock. See [Market Sessions](/perps/learn-about-trading/market-sessions).

Orders are requests to trade in a Perps market. They can execute immediately or rest in the order book until another order matches them.

The order book is the list of resting buy and sell orders for a market. A fill is an executed match between orders in that book.

<Note> Fills update Perps account state; they are not separate onchain transactions. </Note>

Limit orders are useful when the trade needs an explicit price. If the order does not fill immediately, it can rest in the book where it can be inspected, modified, or cancelled.

Once an order fills, it changes the account's position in that market. A position is what the account currently holds: long exposure, short exposure, or no open exposure.

| Position | Benefits when           | Loses when              | | -------- | ----------------------- | ----------------------- | | Long     | The tracked asset rises | The tracked asset falls | | Short    | The tracked asset falls | The tracked asset rises |

A fill that adds to the account's current side increases exposure. A fill against the current side reduces exposure. When the position size reaches zero, the position is closed. If losses exceed what the account can support, the position can also be liquidated.

Perps accounts use collateral to support open positions. Margin checks compare the account's current value against the collateral required to open, increase, or maintain those positions.

Margin checks use these terms:

| Term               | Meaning                                                                                       | | ------------------ | --------------------------------------------------------------------------------------------- | | Collateral         | Funds available to support positions and withdrawals                                          | | Account equity     | The current value of the account after open-position gains, losses, fees, and funding effects | | Initial margin     | Collateral required to open or increase a position                                            | | Maintenance margin | Minimum collateral required to keep a position open                                           | | Liquidation        | Forced position closing when account equity falls below maintenance margin                    |

Account equity moves as the mark price changes and as account debits or credits settle. It can move up or down even before a position is closed.

<Tip> If you're building on Perps, monitor account equity to decide when to reduce exposure, add collateral, or stop placing new orders. </Tip>

At a high level, account equity is the account's collateral plus open-position gains or losses, minus amounts owed.

If account equity falls below maintenance margin, the account is at risk of liquidation. Liquidation closes exposure to prevent losses from exceeding the account's collateral.

**Funding payments** help keep a Perps market close to its index price. They are not order-book trades; they are account debits or credits applied to open positions over time.

<Note> Funding payments are different from collateral deposits. Deposits add collateral to a Perps account; funding payments are debits or credits between long and short positions. </Note>

| Market state                    | Typical payment direction | | ------------------------------- | ------------------------- | | Market trades above index price | Longs pay shorts          | | Market trades below index price | Shorts pay longs          |

A funding payment credited to the account increases account equity. A funding payment owed by the account reduces account equity.

The **funding rate** is the rate used to calculate these payments. Public market data shows funding rates over time, while private account history shows the funding payments applied to an account.

If you're building on Perps, realtime account state helps your integration keep a local view in sync.

Integrations often keep a local view of account state so they can react quickly to fills, risk changes, and collateral movements. Realtime updates help keep that local view in sync.

| State change          | Why it matters                                                 | | --------------------- | -------------------------------------------------------------- | | Order update          | A resting order opened, changed, filled, or cancelled          | | Fill                  | A trade executed and changed the account's position or balance | | Portfolio update      | Account equity, margin, or position state changed              | | Funding payment       | A funding debit or credit changed account state                | | Deposit or withdrawal | Collateral moved into or out of the account                    |

Realtime streams can reconnect or detect gaps. When that happens, the integration should resync by refetching the account state it depends on before trusting the local view again.

**Examples:**

Example 1 (text):
```text
flowchart LR
    A[Submit order] --> B{Matches now?}
    B -->|Yes| C[Fill updates account]
    B -->|No| D[Order rests in book]
    D --> E[Later fill or cancel]
    E --> C
```

Example 2 (text):
```text
Account equity = collateral + unrealized PnL - amounts owed
```

---

## Overview

**URL:** https://docs.polymarket.com/perps/learn-about-trading/overview.md

Perps markets follow a small set of system rules. This section explains how those rules work so you can anticipate how positions are valued, when they are at risk, and why account balances change.

<CardGroup cols={2}> <Card title="Architecture" icon="sitemap" href="/perps/learn-about-trading/architecture"> How offchain matching and onchain settlement fit together. </Card>

<Card title="Markets" icon="list" href="/perps/learn-about-trading/markets"> Available Perps markets and the parameters that shape trading. </Card>

<Card title="Fees" icon="percent" href="/perps/learn-about-trading/fees"> What each fill costs and how the volume-based fee tiers work. </Card>

<Card title="Margin" icon="scale-balanced" href="/perps/learn-about-trading/margin"> Equity, initial margin, maintenance margin, and margin states. </Card>

<Card title="Liquidation Mechanics" icon="triangle-exclamation" href="/perps/learn-about-trading/liquidation-mechanics"> How liquidation is detected, executed, and backstopped. </Card>

<Card title="Funding" icon="repeat" href="/perps/learn-about-trading/funding"> How funding rates are computed and settled against open positions. </Card>

<Card title="Mark Price" icon="chart-line" href="/perps/learn-about-trading/mark-price"> How the price used for margin, PnL, and liquidation is computed. </Card>

<Card title="Index Price" icon="crosshairs" href="/perps/learn-about-trading/index-price"> How the underlying's fair value is sourced and aggregated. </Card>

<Card title="Market Sessions" icon="clock" href="/perps/learn-about-trading/market-sessions"> How session state affects pricing feed selection. </Card>

<Card title="Geographic Restrictions" icon="globe" href="/api-reference/perps/geographic-restrictions"> Where order placement is restricted. </Card> </CardGroup>

---

## Notifications

**URL:** https://docs.polymarket.com/perps/notifications.md

**Contents:**
- Read Notifications
- Stream Notifications
- Mark Notifications Read
- Backfill Missed Notifications
- Notification Types

Notifications turn a Perps account's activity into a ready-to-display feed of position changes, canceled orders, and liquidation events. They are the same events that drive the notification bell in the Polymarket app.

Read recent notifications to render the feed, then stream the live channel to keep it fresh. Mark notifications read as the user catches up. Notifications summarize activity for display. To reconcile order, fill, and position state, use [Reconcile Trade State](/perps/trading#reconcile-trade-state) instead.

<Note> Notifications require an [authenticated session](/perps/authenticated-sessions). </Note>

Start with a read to render the feed. It returns the account's notifications newest first, together with the unread count for the badge.

<Tabs> <Tab title="TypeScript"> Fetch the first page of notifications.

<Tab title="Python"> Fetch the first page of notifications.

<Tab title="API"> Fetch the account's notifications, newest first.

Subscribe to the live channel to append new notifications and bump the unread badge without polling.

<Tabs> <Tab title="TypeScript"> Notification events arrive on the session stream alongside the other private session updates.

<Tab title="Python"> Notification events arrive on the session stream alongside the other private session updates.

<Tab title="API"> Authenticate the WebSocket connection first, then subscribe to the `notifications` channel.

Read state drives the unread count. Mark notifications read when the user views them, either one by one or everything up to the newest one they have seen. Read state is scoped to the account, so a session can only mark its own notifications read.

<Tabs> <Tab title="TypeScript"> Mark specific notifications read by id, or mark everything up to an entry read.

<Tab title="Python"> Mark specific notifications read by id, or mark everything up to an entry read.

<Tab title="API"> Mark specific notifications read by id, or mark everything at or before a cursor read.

The live channel can miss notifications. A reconnect leaves a gap, and under load the server can drop frames. The notifications read closes these gaps. Pass a sequence lower bound and it returns every notification from that point forward, so the feed catches up with stored history.

Anchor the bound at the sequence of the last notification you processed, not at the sequence of the signal that told you to resync. The bound is inclusive and one event can emit several notifications that share one sequence, so the backfill re-covers the boundary. Deduplicate merged results by notification `id`, which is identical across the read and the live channel.

<Tabs> <Tab title="TypeScript"> Track the sequence of the last notification event you processed. When the session signals a `resync`, run the backfill from that anchor.

<Tab title="Python"> Track the sequence of the last notification event you processed. When the session signals a `resync`, run the backfill from that anchor.

<Tab title="API"> <Steps> <Step title="Track the Last Processed Frame"> Keep the `sq` of the last notifications data frame you processed. When the server drops frames under load, it sends a `resync` control frame instead. Its `sq` is the highest sequence among the dropped notifications.

Every notification carries a `type` and a small type-specific payload.

<Tabs> <Tab title="TypeScript"> The `PerpsNotificationType` and `PerpsNotificationOrderType` enums export the `type` and `orderType` values shown in the examples below.

<Tab title="Python"> The `PerpsNotificationType` and `PerpsNotificationOrderType` type aliases list the `type` and `order_type` values.

<Tab title="API"> Notifications report these `type` values.

**Examples:**

Example 1 (text):
```text
    const page = await session.listNotifications().firstPage();
    // page.items: PerpsNotificationEntry[]
```

Example 2 (text):
```text
Each entry pairs one notification with its read state, and `readAt` stays
`null` until the notification is marked read. The read is paginated, so iterate
it to walk older history.

```ts theme={null}
for await (const page of session.listNotifications()) {
  // page.items: PerpsNotificationEntry[]
}
```

For the unread badge, fetch the count directly.

```ts theme={null}
const unread = await session.fetchUnreadNotificationsCount();
```

<Accordion title="Output: PerpsNotificationEntry[]">
  <CodeGroup>
    ```ts Type theme={null}
    type PerpsNotificationEntry = {
      notification: PerpsNotification;
      readAt: number | null;
      timestamp: number;
    };
    ```

    ```json Example theme={null}
    [
      {
        "notification": {
          "id": "0a5d8f1e-3b2c-5e4a-9f8b-1c2d3e4f5a6b",
          "type": "position_opened",
          "instrumentId": 1,
          "side": "long",
          "size": "0.01",
          "avgPrice": "65000",
          "leverage": 5,
          "orderType": "market"
        },
        "readAt": null,
        "timestamp": 1767225600000
      }
    ]
    ```
  </CodeGroup>
</Accordion>
```

Example 3 (text):
```text
    page = await session.list_notifications().first_page()
    # page.items: tuple[PerpsNotificationEntry, ...]
    # page.unread: int
```

Example 4 (text):
```text
Each entry pairs one notification with its read state, and `read_at` stays
`None` until the notification is marked read. The page also carries the
account's `unread` count for the badge. The read is paginated, so iterate it to
walk older history.

```python theme={null}
async for page in session.list_notifications():
    # page.items: tuple[PerpsNotificationEntry, ...]
    pass
```

<Accordion title="Output: tuple[PerpsNotificationEntry, ...]">
  ```json theme={null}
  [
    {
      "notification": {
        "id": "0a5d8f1e-3b2c-5e4a-9f8b-1c2d3e4f5a6b",
        "type": "position_opened",
        "instrument_id": 1,
        "side": "long",
        "size": "0.01",
        "avg_price": "65000",
        "leverage": 5,
        "order_type": "market"
      },
      "read_at": null,
      "timestamp": 1767225600000
    }
  ]
  ```
</Accordion>
```

---

## Liquidation Mechanics

**URL:** https://docs.polymarket.com/perps/learn-about-trading/liquidation-mechanics.md

**Contents:**
- Trigger
- While Liquidating
- Execution
  - Target Selection
  - Order Shape
- Recovery
- Insurance-Fund Backstop
- Auto-Deleveraging
  - Counterparty Selection
  - Execution Price

When a trader's equity drops below maintenance margin, the system closes the position before it becomes insolvent. Normal liquidations route through the order book as reduce-only immediate-or-cancel orders. If the breach is severe, the position is absorbed directly by the insurance fund — or, when the fund cannot safely take it on, closed against opposite-side traders through auto-deleveraging.

An account or isolated position is at risk when:

Liquidation starts when `MarginRatio < 1.0`, which means `Equity < MM`.

Cross and isolated positions are checked independently:

Margin health is re-evaluated continuously, so the system reacts as soon as a new Mark Price, fill, or deposit moves the account across the threshold.

When liquidation starts, the affected scope is flagged:

Order submissions from the account are rejected while the flag is set. The system also cancels the account's resting orders inside the same scope before it places the first liquidation order: cross liquidation cancels resting orders on every cross-margined market but leaves isolated markets untouched, while isolated liquidation cancels only the orders on the affected market.

These cancels race in-flight executions, so a resting order can still fill in the moment between the flag being set and its cancel applying. Any maker or taker fill on an instrument in the account's active liquidation scope reports `liquidation: true` in the account's fill history and `liq: true` on the WebSocket `fills` channel.

The system closes flagged positions with reduce-only immediate-or-cancel orders. These orders execute immediately against available liquidity and cancel any unfilled quantity. Margin health is re-evaluated between orders, so partial fills that restore the account naturally stop the process.

Cross liquidation closes one position at a time. After each fill settles, the system re-evaluates and picks again from the remaining cross positions, so a trader with multiple cross positions is unwound across several cycles rather than all at once.

Isolated liquidation closes the flagged position in full.

Liquidation orders are IOC, reduce-only, and market-priced. They sweep whatever liquidity is resting on the book at the moment they land. There is no protective spread off Mark.

When a liquidating account's equity recovers to or above its recovery initial margin, the flag clears and normal order submission resumes.

If a position is fully closed during liquidation, the flag is also cleared because the market no longer has a position to liquidate.

If equity falls far enough below maintenance margin that order-book liquidation is unlikely to recover value, the system skips the order book and absorbs the position into the insurance fund.

Once absorbed, the insurance fund holds the position and manages it like any other account.

The margin that leaves the trader's account with an absorption is recorded as a cash transfer, separate from fills, funding, and deposits. Retrieve it with [Get Account Backstop Transfers](/api-reference/get-account-backstop-transfers) to reconcile balance changes after a backstop liquidation.

The backstop only fires when the fund can take the position on and remain healthy itself — its equity after absorbing must stay at or above its own maintenance margin. When it cannot, the system auto-deleverages instead.

If a breach is severe enough for the backstop but the insurance fund cannot safely absorb the position, the system force-closes it directly against traders holding the opposite side. This is auto-deleveraging (ADL): no order-book matching, no draw on the insurance fund.

An isolated liquidation deleverages the affected market only. A cross liquidation deleverages every open cross position the account holds.

For each affected market, opposite-side positions are ranked by:

cross equity for a cross position, or over the position's own equity for an isolated position.

The most profitable, most leveraged counterparties rank first. The system works down the queue, reducing each counterparty in turn, until the liquidated position is fully closed. A counterparty position is only ever reduced — never flipped to the other side or increased. Accounts that are themselves liquidating, and the insurance fund, are never selected.

While a counterparty is being deleveraged, its new orders on that market are rejected, exactly as during liquidation. The block clears automatically once the deleveraging completes.

price — the price at which its isolated margin is exactly exhausted.

started, not the live mark.

Both legs settle at this price, and each side's realized PnL is credited to its quote balance.

`adl: true`. The `liq` flag marks only the leg whose own position is being liquidated, so it stays `false` on the counterparty leg.

market, side, size closed, execution price, and realized PnL.

The liquidating account pays an extra liquidation fee on every fill while flagged, on top of its normal maker or taker rate.

Liquidation fee rates vary by market. If you're integrating Perps, read current values from [Market Data](/perps/market-data#fetch-instruments).

Auto-deleveraging fills bypass the order book and carry no fee for either side.

**Examples:**

Example 1 (text):
```text
MarginRatio = Equity / MaintenanceMargin
```

Example 2 (text):
```text
AdlIndex = ProfitRatio * Notional / Equity
```

Example 3 (text):
```text
FillFee = Notional * (MakerOrTakerRate + LiquidationFeeRate)
```

---

## Fees

**URL:** https://docs.polymarket.com/perps/learn-about-trading/fees.md

**Contents:**
- Fee Calculation
- Fee Metrics
- Fee Accounting

Perps trading fees are tiered by an account's trailing 30-day trading volume. Higher-volume accounts pay lower taker fees, and the top tier earns a maker rebate instead of paying a maker fee.

For each fill, the fee is calculated on the notional value of the trade:

Fees are denominated in the instrument's quote asset (pUSD). The rate applied to a fill is set by the account's current volume tier.

| 30-Day Volume ≥ | Taker   | Maker    | | --------------- | ------- | -------- | | \$0             | 0.0400% | 0.0125%  | | \$1M            | 0.0370% | 0.0100%  | | \$5M            | 0.0350% | 0.0080%  | | \$25M           | 0.0300% | 0.0050%  | | \$100M          | 0.0270% | 0.0020%  | | \$500M          | 0.0250% | 0.0000%  | | \$1B            | 0.0200% | -0.0050% |

New accounts start at the \$0 tier and move up as trailing 30-day volume crosses each threshold. Fee tiers are re-evaluated every UTC day.

A negative maker fee is a rebate: the maker receives the rebate amount, and the fee recipient's internal ledger is debited by the same amount.

<Note> A subset of accounts created during the Perps beta are temporarily on the top-tier fee schedule regardless of trailing 30-day volume. Standard volume-based tiering applies to these accounts once the transition period ends. </Note>

If you're integrating Perps, read the current fee schedule from [Trading Fees](/perps/trading#trading-fees) and your account's current tier from the [portfolio](/perps/account-management#portfolio).

Trailing 7-day activity metrics are available for visibility. They are a rolling view of recent activity and do not, on their own, determine the volume tier used to set fees.

| Metric              | Meaning                                                                        | | ------------------- | ------------------------------------------------------------------------------ | | Total volume        | Total Perps trading volume                                                     | | Taker volume        | Perps volume that removed liquidity                                            | | Maker volume        | Perps volume that added liquidity                                              | | Account maker share | Account maker volume divided by total exchange volume                          | | Entity maker share  | Entity maker volume divided by total exchange volume, when the account has one |

These metrics are cached by UTC day and may be stale by up to 24 hours.

If you're integrating Perps, read account metrics from [Account Stats](/perps/account-management#account-stats).

Every fill's fee flows through a single fee-recipient account on the internal ledger:

**Examples:**

Example 1 (text):
```text
Fee = abs(Price * Quantity) * Rate
```

---

## Index Price

**URL:** https://docs.polymarket.com/perps/learn-about-trading/index-price.md

**Contents:**
- Feed Sources
- Feed Selection
- Aggregation

Index Price is Polymarket's estimate of the underlying asset's fair value. It is computed from external price feeds, aggregated to resist stale or anomalous inputs, and published every 200 milliseconds per market.

Index Price can use feeds from external sources such as:

The system selects different feeds based on the current market session so it can use the most accurate feed set for each market. See [Market Sessions](/perps/learn-about-trading/market-sessions).

Index Price is computed as a weighted average across the selected feeds after dropping stale prices and filtering outliers. This prevents any single stale or anomalous feed from moving the Index.

The same aggregation approach is used to build the [C3 candidate in Mark Price](/perps/learn-about-trading/mark-price), using a separate mark feed set.

---

## Referral Program

**URL:** https://docs.polymarket.com/perps/referral-program.md

**Contents:**
- How It Works
- Rewards
- Invite limits and unlocks
- Payouts
- Find and Track Your Code
- Perps vs. Prediction Market Referrals

Refer traders to Polymarket Perps and earn a share of the trading fees they pay. Each account has one Perps referral code. Share your Perps link, and when a new trader opens Perps through it, your code is applied to their account automatically.

<Note> The program's mechanics, attribution rules, invite limits, and other terms may change as the Perps referral program expands. </Note>

Every Perps account has one referral code. Your referral code and your Perps invite code are the same string, so the same link invites traders and credits you for the referral.

When someone opens Perps through your link, your code is applied to their account automatically. You start earning on the trading fees they generate after they are attributed to your code.

A referral code can be applied only once. An account keeps the first code it is given and cannot switch to a different code later. You also cannot apply your own code.

You earn **20% of the trading fees** paid by every Perps trader you refer. There is no cap on how much a single referred trader can earn you.

| Detail        | Perps referral program                              | | ------------- | --------------------------------------------------- | | Reward        | 20% of trading fees paid by referred Perps traders  | | Recipient     | The referrer                                        | | Trader bonus  | No separate bonus is paid to the trader you invite  | | Per-user cap  | No cap on how much one referred trader can earn you | | Payout timing | Weekly                                              |

Each account can refer up to 25 people before volume-based tiers apply. <br />Your code starts with 10 available invites and automatically expands to a total limit of 25 after those 10 invites (with active users) are used. From there, you can unlock a total limit of 100 invites at \$100,000 in combined eligible Perps volume, 250 at \$500,000, and 500 at \$1,000,000.

Eligible volume includes your own Perps trading volume and volume generated by your direct referrals after they are attributed to your code. Indirect referrals do not count. The tier numbers are total invite limits, not additional invites.

If you use every invite in your current tier, your code cannot accept another referral until you unlock the next tier. The maximum standard limit is 500 invites.

Referral earnings are paid out weekly. You can see referral payouts in your Perpetuals portfolio history.

Your referral code is available from your profile and on Perps market pages, so you can copy and share it while you trade. The Perps referrals dashboard shows:

The Perps referral program is separate from the prediction market referral program. They use different codes and track earnings independently.

Referring a Perps trader does not affect your prediction market referrals, and a prediction market referral does not affect your Perps referrals. Each program shows up in its own place.

**Examples:**

Example 1 (text):
```text
https://polymarket.com/perps?c={code}
```

---

## Errors

**URL:** https://docs.polymarket.com/perps/errors.md

**Contents:**
- Service Unavailable
  - Transient Overload (`503`)
  - Recover an Isolated-Margin Adjustment
- Order Placement Errors
- Modify Order Errors
- Order Cancellation Errors
- Auto-Cancel Errors
- Update Leverage Errors
- Isolated Margin Adjustment Errors

The API returns descriptive error messages when a request is rejected. Use the HTTP status and response body to decide whether to retry or correct the request.

The API returns `503 Service Unavailable` for temporary overload or a response timeout on operations that support safe retries.

A `503` does not prove that the request did not execute. A load-shed rejection happens before dispatch, but an engine response timeout can occur after the request was admitted.

| Operation                                                                                       | Retry Action                                                                                        | | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | | Reads and idempotent state updates, such as setting leverage                                    | Retry with backoff.                                                                                 | | Signed balance changes, such as isolated-margin adjustments, withdrawals, or internal transfers | Resend only the exact original signed request. Do not generate a new signature, salt, or timestamp. |

indeterminate outcome. Follow the operation's recovery guidance before retrying.

For `PATCH /v1/trade/margin`, `amt` is a signed delta, not a replacement balance. After a `503`, retry only the exact original signed payload. A newly signed request is a separate adjustment and can apply the delta again.

A `signature*already*used` rejection means the original signed request was ingested; it does not confirm that the adjustment succeeded. Its decision may still be pending or may have rejected the adjustment.

`GET /v1/account/portfolio` reports committed state without a per-request outcome. Neither an unchanged balance nor a matching delta proves what happened: the request may still be pending, or another adjustment may explain the change.

Do not sign another adjustment for the same account until the original outcome has been confirmed out of band. No public endpoint currently reports that request's terminal outcome.

| Error                                          | Condition                                          | | ---------------------------------------------- | -------------------------------------------------- | | `invalid signature`                            | EIP-712 signature verification or timestamp failed | | `signature expired`                            | Signature older than 5 minutes                     | | `account not found for proxy`                  | Signer proxy not linked to any account             | | `no orders provided`                           | Empty order array                                  | | `FOK orders cannot be post-only`               | FOK + `post*only=true`                             | | `IOC orders cannot be post-only`               | IOC + `post*only=true`                             | | `GTC orders require a price`                   | GTC without price                                  | | `price cannot be zero`                         | Price = 0                                          | | `client order id cannot be all zeros`          | Client order ID is all zeros                       | | `price exceeds allowed decimal places`         | Too many decimal places in price                   | | `price exceeds allowed significant figures`    | More than 5 significant figures in price           | | `quantity must be positive`                    | Quantity is zero or negative                       | | `quantity exceeds allowed decimal places`      | Too many decimal places in quantity                | | `quantity exceeds allowed significant figures` | More than 5 significant figures in quantity        | | `command expired`                              | `exp*ms` is in the past                            | | `command expiry too far in future`             | `exp*ms` is more than 5 seconds from now           |

Modify Order returns one result per requested order. A rejected modification does not change the live order, although a separately processed fill or cancellation can still change its state.

| Error                              | Condition                                                                                  | | ---------------------------------- | ------------------------------------------------------------------------------------------ | | `modify*already*pending`           | Another modification for the same order is still in progress.                              | | `modify*no*op`                     | The requested price and total quantity equal the live order values.                        | | `modify*limit*reached`             | The order has already reached 10,000 successful modifications.                             | | `modify*would*cross`               | The modified order would lock or cross the live opposite best price.                       | | `duplicate*order*in*batch`         | An earlier item in the same batch resolved to the same order ID.                           | | `order*not*modifiable`             | The order is not an eligible standalone resting GTC limit order.                           | | `order*has*tpsl`                   | The order is a TP/SL leg or has attached or order-scoped TP/SL.                            | | `modify*quantity*not*above*filled` | The requested new total quantity is less than or equal to the live cumulative fill.        | | `order*unknown`                    | The client order ID does not resolve to an order owned by the account.                     | | `order*not*in*orderbook`           | The order ID is unknown, terminal, owned by another account, or otherwise not disclosable. | | `order*in*flight`                  | The order is still in creation or taker delay and is not yet resting.                      | | `invalid*command`                  | A per-item price, quantity, or notional validation failed before sequencing.               |

Shared account, instrument, margin, position, reduce-only, and rate-limit errors can also reject a modification under the same conditions as a new order.

A cancel sent while an order is awaiting risk checks succeeds immediately, unless the account is being liquidated. The canceled order will not enter the order book.

A cancel sent while the order's accept is still on its way to the matching engine does not fail: the exchange holds one such cancel, applies it as soon as the accept completes, and answers with the final outcome — success once the order is removed, or `order*already*terminal` if the order filled or was rejected first. If the exchange disables this behavior, is in cancel-only maintenance mode, or the account is being liquidated, such a cancel returns `order*in*flight` instead.

| Error                      | Condition                                                                                                                                                               | | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | `order*not*found`          | Order doesn't exist                                                                                                                                                     | | `order*not*pending*engine` | An earlier cancel for the same order is already queued or in flight                                                                                                     | | `order*not*in*orderbook`   | Order is not in the active book                                                                                                                                         | | `order*in*flight`          | Order is not yet cancellable: in taker delay, the account is being liquidated, or acceptance is in flight while held cancels are disabled or cancel-only mode is active | | `order*already*terminal`   | Order filled, was canceled, or was rejected before this cancel                                                                                                          |

Returned when arming the auto-cancel switch with `PATCH /v1/trade/auto-cancel`. Disarming skips these checks and is always allowed. A deadline already in the past is rejected earlier with a plain `400` message.

| Error                             | Condition                                                                      | | --------------------------------- | ------------------------------------------------------------------------------ | | `auto*cancel*deadline*too*soon`   | Deadline is less than 5 seconds in the future                                  | | `auto*cancel*daily*limit*reached` | Account already triggered auto-cancel the maximum number of times this UTC day | | `auto*cancel*in_flight`           | A previous trigger is still cancelling the account's open orders               |

`auto*cancel*in_flight` is transient. Arming succeeds once the engine finishes the earlier cancellation.

Returned when a leverage or margin-mode update is rejected. Leverage must be positive; a zero leverage is rejected earlier with a plain `400` validation message. A disabled instrument is not rejected merely because it is disabled.

| Error                  | Condition                                                                                                                                                                                           | | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | `instrument*not*found` | The instrument ID has never been listed                                                                                                                                                             | | `invalid*leverage`     | The requested leverage exceeds the instrument's maximum                                                                                                                                             | | `position*exists`      | A margin-mode switch was requested while a position is open in the instrument                                                                                                                       | | `open*orders*exist`    | A margin-mode switch was requested while orders exist in the instrument, including orders awaiting risk approval or execution                                                                       | | `blp*leverage*locked`  | The account is subscribed to the Backstop Liquidity Provider program for the instrument, even if the update re-submits the unchanged pair; unsubscribe before pinning or changing its configuration |

These stable identifiers are returned when an isolated margin adjustment is rejected after sequencing.

Gateway signature validation can reject a stale or future-skewed timestamp earlier as `invalid signature`; that request never reaches sequencing.

| Error                                | Condition                                                                   | | ------------------------------------ | --------------------------------------------------------------------------- | | `position*not*found`                 | The target open position does not exist                                     | | `invalid*margin*mode`                | The target position is not using isolated margin                            | | `invalid*margin*amount`              | The amount is zero, over-precise, or cannot be represented safely           | | `insufficient*margin`                | An addition exceeds available, unreserved collateral                        | | `account*liquidating`                | Cross liquidation is active, or the target isolated position is liquidating | | `margin*below*required*initial`      | A removal would leave position equity below current required initial margin | | `invalid*margin*signature*timestamp` | Sequencer found the timestamp over five minutes old or one minute ahead     | | `signature*already*used`             | The exact signed margin request has already been ingested                   |

**Examples:**

Example 1 (text):
```text
{
  "status": "err",
  "error": "service_unavailable"
}
```

---

## Funding

**URL:** https://docs.polymarket.com/perps/learn-about-trading/funding.md

**Contents:**
- How Funding Works
  - Premium Index
  - Funding Rate
  - Payment
  - Interval
- Parameters

Unlike futures contracts, perpetuals have no expiry date. Funding is the mechanism that keeps the perpetual price anchored to the underlying's fair value. When the perpetual trades above Index, longs pay shorts. When it trades below Index, shorts pay longs.

Funding runs continuously across all sessions, regardless of whether the underlying reference market is open. This keeps the convergence incentive active and prevents positions from being left unanchored from fair value.

Funding is computed in three stages:

Every 5 seconds, the protocol takes one snapshot per market of how far the book has drifted from Index. It walks the book for a fixed quote notional on each side.

If one side of the book cannot fill the notional because it is too thin or empty, that side falls back to Index, which zeros its contribution.

The impact price difference and premium index are:

A positive premium means the perpetual is trading rich versus Index. A negative premium means it is trading cheap.

At the end of each charge window, premium samples are averaged, passed through the 8-hour funding formula, divided by 8 to get an hourly rate, and capped.

At the end of each charge window, every open position in the market settles a funding payment proportional to position size and the hourly rate.

| Condition                             | Longs   | Shorts  | | ------------------------------------- | ------- | ------- | | Hourly rate > 0, perp rich vs Index   | Pay     | Receive | | Hourly rate \< 0, perp cheap vs Index | Receive | Pay     |

Funding is a direct transfer between longs and shorts. The protocol takes no cut. Settlement credits or debits the quote balance, and realized funding is tracked separately from trading PnL.

The charge window is 1 hour. Samples are averaged over the hour, and the hourly rate is applied once at the end.

Between settlements, rolling premium samples and implied rates are published so traders can see funding pressure build in real time.

| Parameter        | Default                   | Description                               | | ---------------- | ------------------------- | ----------------------------------------- | | Sample interval  | 5 seconds                 | Cadence of premium index samples          | | Impact notional  | 1,000 quote notional      | Quote notional used for impact VWAP       | | Interest leg     | 0.01% per 8 hours         | Fixed component in the 8-hour formula     | | Interest clamp   | +/-0.05%                  | Symmetric clamp on interest minus premium | | Funding scale    | 1.0 crypto; 0.5 otherwise | Multiplier applied to the 8-hour formula  | | Charge window    | 1 hour                    | Interval between funding settlements      | | Funding rate cap | 4% per hour               | Maximum absolute hourly funding rate      |

**Examples:**

Example 1 (text):
```text
bid_impact = VWAP of top bids filling 1,000 quote notional
ask_impact = VWAP of top asks filling 1,000 quote notional
```

Example 2 (text):
```text
IPD = max(bid_impact - Index, 0) - max(Index - ask_impact, 0)
PremiumIndex = IPD / Index
```

Example 3 (text):
```text
mean_P = average of PremiumIndex samples over the window
scale = 1.0 for crypto markets; 0.5 otherwise
F_8h = scale * (mean_P + clamp(0.0001 - mean_P, +/-0.0005))
FR_hour = clamp(F_8h / 8, +/-0.04)
```

---

## Market Data

**URL:** https://docs.polymarket.com/perps/market-data.md

**Contents:**
- Fetch Instruments
- Fetch Tickers
- Fetch the Order Book
- List Candles
- Fetch Mark Price History
- List Trades
- List Funding History

Use market data to understand what can be traded, where the market is trading now, and how activity has changed over time.

<Tabs> <Tab title="TypeScript"> The TypeScript examples on this page use a `PublicClient`. The same market-data methods are also available on `SecureClient` instances.

<Tab title="Python"> The Python examples on this page use an `AsyncPublicClient`. The same market-data methods are also available on `AsyncSecureClient` instances.

<Tab title="API"> Use the Perps REST API production URL.

Fetch instruments before your integration lets users choose or submit orders for a Perps market. Instrument data gives you the constraints needed to validate that workflow.

<Tabs> <Tab title="TypeScript"> Fetch the available instruments.

<Tab title="Python"> Fetch the available instruments.

<Tab title="API"> Fetch the available instruments.

Use tickers when you need a lightweight view of where one or more markets are trading now.

<Tabs> <Tab title="TypeScript"> Fetch one ticker when you already know which instrument your integration is tracking.

<Tab title="Python"> Fetch one ticker when you already know which instrument your integration is tracking.

<Tab title="API"> Fetch all tickers to build a market list or refresh a dashboard.

Ticker snapshots are refreshed in the background and may be up to ten seconds old. When the gateway cannot guarantee that bound — for example while its data store is unavailable — the endpoint returns `503 Service Unavailable` rather than stale prices. Treat a `503` as transient and retry with backoff.

Use the order book before choosing an order price or size. It shows available liquidity at the requested depth.

<Tabs> <Tab title="TypeScript"> Choose how many price levels to request. Supported depths are `10`, `100`, `500`, and `1000`. When omitted, the SDK requests `100` levels.

<Tab title="Python"> Choose how many price levels to request. Supported depths are `10`, `100`, `500`, and `1000`. When omitted, the SDK requests `100` levels.

<Tab title="API"> Fetch the order book for an instrument. Supported depths are `10`, `100`, `500`, and `1000`; when omitted, the API uses `100`.

Use candles when your workflow needs time-bucketed price history for charts, backtests, or trading signals.

<Tabs> <Tab title="TypeScript"> The SDK paginates candle history. When `start` is omitted, it starts from the past 24 hours.

<Tab title="Python"> The SDK paginates candle history. When `start` is omitted, it starts from the past 24 hours.

<Tab title="API"> Fetch candles for an instrument and interval. `start*timestamp` is required; `end*timestamp` is optional. The API returns at most 1000 candles per request.

Mark price history shows how an instrument's mark price changed over time. Each data point contains the last mark price recorded for an interval, independent of whether trades occurred during that interval.

<Tabs> <Tab title="API"> Fetch bucketed mark prices for an instrument and interval. `start*timestamp` is required; `end*timestamp` is optional. The API returns at most 1000 points per request.

Use public trades when recent executions matter more than aggregated candles. This is useful for trade tape views and execution analysis.

<Tabs> <Tab title="TypeScript"> The SDK paginates trade history, including cursor handling and boundary deduplication.

<Tab title="Python"> The SDK paginates trade history, including cursor handling and boundary deduplication.

<Tab title="API"> Fetch recent public trades for an instrument. `start*timestamp` and `end*timestamp` are optional. The API returns at most 100 trades per request.

Use funding-rate history when estimating carry costs or explaining why Perps prices differ from the index over time.

<Tabs> <Tab title="TypeScript"> The SDK paginates funding-rate history.

<Tab title="Python"> The SDK paginates funding-rate history.

<Tab title="API"> Fetch historical funding rates for an instrument. `start*timestamp` and `end*timestamp` are optional. The API returns at most 100 funding-rate entries per request.

**Examples:**

Example 1 (text):
```text
    import { createPublicClient } from "@polymarket/client";

    const client = createPublicClient();
```

Example 2 (text):
```text
    from polymarket import AsyncPublicClient

    client = AsyncPublicClient()
```

Example 3 (text):
```text
    https://api.perpetuals.polymarket.com
```

Example 4 (text):
```text
    const instruments = await client.fetchPerpsInstruments();
    // instruments: PerpsInstrument[]
```

---

## Overview

**URL:** https://docs.polymarket.com/perps/overview.md

**Contents:**
- How Perps Work
- Building on Perps
- Next Steps

Polymarket [Perps](https://polymarket.com/perps) are perpetual contracts that track an underlying asset such as an index, commodity, crypto asset, or equity. Perps trade continuously and do not expire, so traders can open, manage, and close leveraged positions without waiting for a market resolution event.

A Perps trade starts as an order in the order book. When it fills, it becomes a position whose value changes as the tracked market moves, until the trader closes it or the system closes it because the account can no longer support the risk.

<CardGroup cols={2}> <Card title="Prices" icon="chart-line"> A Perps market has a traded price from the order book and reference prices used by the system. The index price tracks the underlying asset, while the mark price is used for account equity, margin checks, and liquidation risk. </Card>

<Card title="Trading Positions" icon="arrow-right-arrow-left"> Trading a Perps market creates or changes a position. A long position benefits when the tracked asset rises, and a short position benefits when it falls. Orders trade through the order book; fills update the account's position, balance, and history. </Card>

<Card title="Margin And Liquidation" icon="shield"> Perps require collateral to support open positions. That collateral is the account's margin: the buffer that covers losses while a position is open. If account equity falls too far relative to the required margin, the position can be liquidated to close exposure. </Card>

<Card title="Funding Payments" icon="repeat"> Funding payments keep the contract price close to the index price. When a market trades above its index price, long positions generally pay short positions. When it trades below its index price, shorts generally pay longs. </Card> </CardGroup>

If you are here to see what you can build on top of Polymarket Perps, common use cases include:

<CardGroup cols={3}> <Card title="Concepts" icon="book" href="/perps/concepts"> Learn the shared terms used across Perps docs. </Card>

<Card title="Learn About Trading" icon="book-open" href="/perps/learn-about-trading/overview"> Understand the market mechanics behind Perps. </Card>

<Card title="Place Your First Trade" icon="bolt" href="/perps/place-your-first-trade"> Build a first end-to-end Perps trading flow. </Card> </CardGroup>

---

## Account Management

**URL:** https://docs.polymarket.com/perps/account-management.md

**Contents:**
- Review Account Health
  - Balances
  - Portfolio
  - Account Stats
- Reconcile Orders and Fills
  - Open Orders
  - Orders
  - Fills
- Reconcile Funding and Transfers
  - Funding Payments

Use account reads to turn Perps activity into a reliable local view of account health, trading history, and performance.

<Note> Account management workflows require an [authenticated session](/perps/authenticated-sessions). </Note>

Start with the account's current collateral and exposure when showing portfolio health or checking whether a trade fits the account's risk state.

Use balances to show collateral by asset and account value.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use the portfolio to show open positions, margin usage, withdrawable collateral, and liquidation state.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use account stats to review trailing 7-day trading activity such as volume and maker share. Stats are cached by UTC day and may be stale by up to 24 hours. See [Fee Metrics](/perps/learn-about-trading/fees#fee-metrics) for what each metric means.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use order state and fills to connect submitted orders with resting liquidity, executions, fees, and exposure changes.

Use open orders to show what is still resting on the book.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use orders to inspect the latest known state for submitted orders.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use fills to reconcile executions, fees, realized PnL, and exposure changes.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Funding, deposits, and withdrawals explain collateral changes that did not come from order fills. Use [Fund Your Account](/perps/fund-your-account) for deposit and withdrawal submission workflows.

Use funding payments to explain periodic funding debits or credits for a market.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use deposits to reconcile collateral added to the Perps account.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use withdrawals to reconcile collateral leaving the Perps account.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use equity and PnL history to explain how the account's value changed over time.

Use equity history to chart account value over time. Each point is the last equity sample in its `interval` bucket, stamped with that sample's own timestamp. A coarser interval lets each 1000-point page cover a longer window before `more` is set.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

Use PnL history to chart account profit and loss over the same interval. Each point is the PnL realized inside its `interval` bucket — not a running total — and buckets in which nothing was realized are omitted, so the series is sparse.

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

**Examples:**

Example 1 (text):
```text
const balances = await session.fetchBalances();
```

Use this shape to render collateral balances and account value by asset.

<Accordion title="Output: PerpsBalance[]">
  <CodeGroup>
    ```ts PerpsBalance Type theme={null}
    type PerpsBalance = {
      asset: string;
      balance: string;
      value: string;
    };

    type Output = PerpsBalance[];
    ```

    ```json PerpsBalance Example theme={null}
    [
      {
        "asset": "pUSD",
        "balance": "1000",
        "value": "1000"
      }
    ]
    ```
  </CodeGroup>
</Accordion>
```

Example 2 (text):
```text
balances = await session.fetch_balances()
```

Use this shape to render collateral balances and account value by asset.

<Accordion title="Output: tuple[PerpsBalance, ...]">
  ```json theme={null}
  [
    {
      "asset": "pUSD",
      "balance": "1000",
      "value": "1000"
    }
  ]
  ```
</Accordion>
```

Example 3 (text):
```text
curl "https://api.perpetuals.polymarket.com/v1/account/balances" \
  -H "polymarket-proxy: <proxy_address>" \
  -H "polymarket-secret: <proxy_secret>"
```

Use this shape to render collateral balances and account value by asset.

<Accordion title="Output: Balances">
  ```json theme={null}
  [
    {
      "asset": "pUSD",
      "balance": "1000",
      "value": "1000"
    }
  ]
  ```
</Accordion>
```

Example 4 (text):
```text
const portfolio = await session.fetchPortfolio();
```

Use this shape to render positions, margin usage, and liquidation state.

<Accordion title="Output: PerpsPortfolio">
  <CodeGroup>
    ```ts PerpsPortfolio Type theme={null}
    type PerpsPortfolio = {
      positions: Array<{
        instrumentId: number;
        symbol: string;
        size: string;
        entryPrice: string;
        leverage: number;
        cross: boolean;
        initialMargin: string;
        maintenanceMargin: string;
        positionValue: string;
        liquidationPrice: string;
        unrealizedPnl: string;
        returnOnEquity: string;
        cumulativeFunding: string;
      }>;
      margin: {
        totalAccountValue: string;
        totalInitialMargin: string;
        totalMaintenanceMargin: string;
        totalPositionValue: string;
      };
      withdrawable: string;
      inLiquidation: boolean;
      timestamp: number;
    };

    type Output = PerpsPortfolio;
    ```

    ```json PerpsPortfolio Example theme={null}
    {
      "positions": [
        {
          "instrumentId": 1,
          "symbol": "BTC-PERP",
          "size": "0.01",
          "entryPrice": "65000",
          "leverage": 5,
          "cross": false,
          "initialMargin": "130",
          "maintenanceMargin": "65",
          "positionValue": "650",
          "liquidationPrice": "52000",
          "unrealizedPnl": "0",
          "returnOnEquity": "0",
          "cumulativeFunding": "0"
        }
      ],
      "margin": {
        "totalAccountValue": "1000",
        "totalInitialMargin": "130",
        "totalMaintenanceMargin": "65",
        "totalPositionValue": "650"
      },
      "withdrawable": "870",
      "inLiquidation": false,
      "timestamp": 1767000000000
    }
    ```
  </CodeGroup>
</Accordion>
```

---

## Fund Your Account

**URL:** https://docs.polymarket.com/perps/fund-your-account.md

**Contents:**
- Deposit Collateral
- Withdraw Collateral
- Review Funding History

Fund the Perps account with pUSD before placing orders. Deposits move pUSD from the user's Polymarket wallet into the Perps account. Withdrawals move available pUSD back to the authenticated wallet.

Deposit pUSD when the account needs collateral for opening or maintaining Perps positions.

<Tabs> <Tab title="TypeScript"> <Steps> <Step title="Create a Secure Client"> Create a `SecureClient` for the wallet that will fund the Perps account. If you already have a Polymarket wallet, pass it as `wallet` and include a Relayer API key so the SDK can submit gasless transactions. If you are creating a wallet programmatically, use a Builder API key so the SDK can create the Deposit Wallet for that signer.

<Tab title="Python"> <Steps> <Step title="Create a Secure Client"> Create an `AsyncSecureClient` for the wallet that will fund the Perps account. If you already have a Polymarket wallet, pass it as `wallet` and include a Relayer API key so the SDK can submit gasless transactions. If you are creating a wallet programmatically, use a Builder API key so the SDK can create the Deposit Wallet for that signer.

<Tab title="API"> <Steps> <Step title="Check Deposit Approval"> Before depositing, the Polymarket wallet must approve the Perps deposit contract to spend pUSD. If the approval is already in place, skip the approval call.

Withdraw pUSD when the account has available collateral that should return to the authenticated wallet.

Withdrawals must satisfy the [withdrawal margin requirements](/perps/learn-about-trading/margin#withdrawal-margin-requirements), including the 10% reserve against open-position notional. Collateral available for trading can therefore exceed collateral available for withdrawal.

<Tabs> <Tab title="TypeScript"> Request a withdrawal to the authenticated wallet. Amounts use raw pUSD base units, so 10 pUSD is `10*000*000n`.

<Tab title="Python"> Request a withdrawal to the authenticated wallet. Amounts use raw pUSD base units, so 10 pUSD is `10*000*000`.

<Tab title="API"> <Steps> <Step title="Build the Withdrawal Operation"> Create a `withdraw` operation with the account signer, pUSD token, raw token amount, and destination wallet. For withdrawals, `amount` is the raw pUSD token amount, so 10 pUSD is `10000000`.

Use deposit and withdrawal history to reconcile collateral movements after your integration submits funding requests.

See [Authenticated Sessions](/perps/authenticated-sessions) for how to create an authenticated session for private account history reads.

<Tabs> <Tab title="TypeScript"> List deposit or withdrawal history from an authenticated Perps session.

<Tab title="Python"> List deposit or withdrawal history from an authenticated Perps session.

<Tab title="API"> List deposit history.

**Examples:**

Example 1 (text):
```text
    <CodeGroup>
      ```ts Existing Account theme={null}
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

      ```ts New Programmatic Wallet theme={null}
      import { createSecureClient } from "@polymarket/client";
      import { builderApiKey } from "@polymarket/client/node";
      import { privateKey } from "@polymarket/client/viem";

      const client = await createSecureClient({
        signer: privateKey(process.env.PRIVATE_KEY!),
        apiKey: builderApiKey({
          key: process.env.BUILDER_API_KEY!,
          secret: process.env.BUILDER_SECRET!,
          passphrase: process.env.BUILDER_PASSPHRASE!,
        }),
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Set Up Deposit Approvals">
    Set up the approvals required for Perps collateral deposits. The SDK skips work
    that is already complete.

    ```ts theme={null}
    await client.setupTradingApprovals();
    ```
  </Step>

  <Step title="Deposit Collateral">
    Deposit pUSD from the user's Polymarket wallet into the Perps account. Make sure
    the wallet has pUSD before depositing. The minimum Perps deposit is 10 pUSD.
    Amounts use raw pUSD base units, so 10 pUSD is `10_000_000n`.

    ```ts theme={null}
    const deposit = await client.depositToPerps({
      amount: 10_000_000n,
    });

    const receipt = await deposit.wait();
    // receipt.transactionHash: TxHash
    ```

    `deposit.wait()` confirms that the chain transaction settled. Perps may take a
    moment to credit the account after that.
  </Step>

  <Step title="Verify the Deposit">
    Open a Perps session and read account state after the deposit settles.

    ```ts theme={null}
    const session = await client.openPerpsSession();

    try {
      const portfolio = await session.fetchPortfolio();
      const pages = session.listDeposits();
      const deposits = await pages.firstPage();
    } finally {
      await session.close();
    }
    ```

    Use `portfolio.withdrawable` to check collateral available for withdrawal and
    `deposits.items` to reconcile deposit history. The `withdrawable` value already
    accounts for the [10% notional reserve](/perps/learn-about-trading/margin#withdrawal-margin-requirements).
  </Step>
</Steps>
```

Example 2 (text):
```text
    <CodeGroup>
      ```python Existing Account theme={null}
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

      ```python New Programmatic Wallet theme={null}
      import os

      from polymarket import AsyncSecureClient, BuilderApiKey

      client = await AsyncSecureClient.create(
          private_key=os.environ["PRIVATE_KEY"],
          api_key=BuilderApiKey(
              key=os.environ["BUILDER_API_KEY"],
              secret=os.environ["BUILDER_SECRET"],
              passphrase=os.environ["BUILDER_PASSPHRASE"],
          ),
      )
      ```
    </CodeGroup>
  </Step>

  <Step title="Set Up Deposit Approvals">
    Set up the approvals required for Perps collateral deposits. The SDK skips work
    that is already complete.

    ```python theme={null}
    await client.setup_trading_approvals()
    ```
  </Step>

  <Step title="Deposit Collateral">
    Deposit pUSD from the user's Polymarket wallet into the Perps account. Make sure
    the wallet has pUSD before depositing. The minimum Perps deposit is 10 pUSD.
    Amounts use raw pUSD base units, so 10 pUSD is `10_000_000`.

    ```python theme={null}
    deposit = await client.deposit_to_perps(amount=10_000_000)

    receipt = await deposit.wait()
    # receipt.transaction_hash: TransactionHash
    ```

    `deposit.wait()` confirms that the chain transaction settled. Perps may take a
    moment to credit the account after that.
  </Step>

  <Step title="Verify the Deposit">
    Open a Perps session and read account state after the deposit settles.

    ```python theme={null}
    session = await client.open_perps_session()

    try:
        portfolio = await session.fetch_portfolio()
        pages = session.list_deposits()
        deposits = await pages.first_page()
    finally:
        await session.close()
    ```

    Use `portfolio.withdrawable` to check collateral available for withdrawal and
    `deposits.items` to reconcile deposit history. The `withdrawable` value already
    accounts for the [10% notional reserve](/perps/learn-about-trading/margin#withdrawal-margin-requirements).
  </Step>
</Steps>
```

Example 3 (text):
```text
        pUSD.approve(PerpsDepositContract, maxUint256)
```

Example 4 (text):
```text
    Use these contract addresses when building the approval call.

    | Contract               | Address                                      |
    | ---------------------- | -------------------------------------------- |
    | pUSD collateral token  | `0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB` |
    | Perps deposit contract | `0xDCa4af75705dbB50f62437045afF9921947917d2` |

    <Note>
      The following steps show the Deposit Wallet batch path. If you are trading
      with a Safe or Poly Proxy wallet, use an SDK that handles the wallet-specific
      transaction flow for you.
    </Note>
  </Step>

  <Step title="Build the Deposit Call">
    Create the Perps deposit call. Deposit amounts use pUSD base units, so 10 pUSD
    is `10000000`.

    ```solidity theme={null}
    function deposit(address token, uint256 amount, address to);
    ```

    Encode the deposit calldata with these arguments.

    | Argument | Value                                        |
    | -------- | -------------------------------------------- |
    | `token`  | `0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB` |
    | `amount` | `10000000`                                   |
    | `to`     | Signer address for the Polymarket account.   |

    Build the final ordered call list. Include the approval call first only when
    approval is needed.

    <CodeGroup>
      ```json Without Approval theme={null}
      [
        {
          "target": "0xDCa4af75705dbB50f62437045afF9921947917d2",
          "value": "0",
          "data": "<deposit_calldata>"
        }
      ]
      ```

      ```json With Approval theme={null}
      [
        {
          "target": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
          "value": "0",
          "data": "<approve_calldata>"
        },
        {
          "target": "0xDCa4af75705dbB50f62437045afF9921947917d2",
          "value": "0",
          "data": "<deposit_calldata>"
        }
      ]
      ```
    </CodeGroup>
  </Step>

  <Step title="Fetch a Relayer Nonce">
    Fetch a fresh `WALLET` nonce before submitting the Deposit Wallet batch.

    ```bash theme={null}
    curl -G "https://relayer-v2.polymarket.com/v1/account/transactions/params" \
      -H "RELAYER_API_KEY: $RELAYER_API_KEY" \
      -H "RELAYER_API_KEY_ADDRESS: $RELAYER_API_KEY_ADDRESS" \
      --data-urlencode "address=<polymarket_account_signer_address>" \
      --data-urlencode "type=WALLET"
    ```

    The response includes the nonce to sign with the batch.

    ```json theme={null}
    {
      "address": "<polymarket_account_signer_address>",
      "nonce": "<wallet_nonce>"
    }
    ```
  </Step>

  <Step title="Build the Deposit Wallet Batch">
    Build the EIP-712 `Batch` typed data for the Deposit Wallet. Use the final
    ordered call list from the previous step, and omit the approval call when
    allowance is already sufficient. Set `deadline` to a Unix timestamp in seconds
    after which the relayer should reject the batch.

    ```json theme={null}
    {
      "domain": {
        "name": "DepositWallet",
        "version": "1",
        "chainId": 137,
        "verifyingContract": "<polymarket_wallet_address>"
      },
      "primaryType": "Batch",
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
      "message": {
        "wallet": "<polymarket_wallet_address>",
        "nonce": "<wallet_nonce>",
        "deadline": "<unix_seconds>",
        "calls": [
          {
            "target": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
            "value": "0",
            "data": "<approve_calldata>"
          },
          {
            "target": "0xDCa4af75705dbB50f62437045afF9921947917d2",
            "value": "0",
            "data": "<deposit_calldata>"
          }
        ]
      }
    }
    ```

    Sign this typed data with the signer for the Polymarket account.
  </Step>

  <Step title="Submit the Deposit Transaction">
    Submit the signed batch to the Relayer API. Use the same ordered call list you
    signed in the previous step.

    ```bash theme={null}
    curl -X POST "https://relayer-v2.polymarket.com/submit" \
      -H "Content-Type: application/json" \
      -H "RELAYER_API_KEY: $RELAYER_API_KEY" \
      -H "RELAYER_API_KEY_ADDRESS: $RELAYER_API_KEY_ADDRESS" \
      -d '{
        "type": "WALLET",
        "from": "<polymarket_account_signer_address>",
        "to": "0x00000000000Fb5C9ADea0298D729A0CB3823Cc07",
        "nonce": "<wallet_nonce>",
        "signature": "<wallet_batch_signature>",
        "metadata": "Deposit pUSD to Perps",
        "depositWalletParams": {
          "depositWallet": "<polymarket_wallet_address>",
          "deadline": "<unix_seconds>",
          "calls": [
            {
              "target": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
              "value": "0",
              "data": "<approve_calldata>"
            },
            {
              "target": "0xDCa4af75705dbB50f62437045afF9921947917d2",
              "value": "0",
              "data": "<deposit_calldata>"
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

  <Step title="Poll the Deposit Transaction">
    Poll the relayer transaction until it reaches `STATE_CONFIRMED` before relying
    on the deposited collateral.

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

    Perps may take a moment to credit the account after the onchain transaction
    settles. Treat `STATE_FAILED` and `STATE_INVALID` as terminal failures.
  </Step>
</Steps>
```

---

## Market Sessions

**URL:** https://docs.polymarket.com/perps/learn-about-trading/market-sessions.md

**Contents:**
- What Sessions Affect
- What Sessions Do Not Affect
- Categories
- How the Category Is Determined

Perps trade 24/7, but the underlying markets do not. Liquidity and external price feed availability vary by time of day and day of week. Sessions are the system's categorization of these conditions.

Sessions affect one thing: which set of external feeds is used to compute [Index Price](/perps/learn-about-trading/index-price) and the [C3 candidate in Mark Price](/perps/learn-about-trading/mark-price).

Each category can use its own feed set. For example, primary venue feeds may be used during regular hours and after-hours venue feeds may be used overnight. If the current category has no dedicated feed set, the system falls back to the overnight feed set.

Sessions do not change:

Those systems run identically around the clock.

Each market has a schedule that defines its time windows and exceptions. The system evaluates the schedule on time boundaries to produce the current category. When the category changes, subsequent Index and Mark updates use the feed set assigned to the new category.

---

## Architecture

**URL:** https://docs.polymarket.com/perps/learn-about-trading/architecture.md

**Contents:**
- Offchain Matching
- Onchain Components
- State Root Commitments
- Data Flow

Polymarket Perps is a hybrid exchange: matching happens offchain for speed, while custody and settlement live on Polygon. Exchange state is periodically committed onchain so offchain activity remains verifiable.

When a trader places an order, the matching engine maintains the order book, applies risk checks, matches orders, and updates balances, positions, margin, and funding offchain. This gives the exchange its latency profile because matching does not wait on block times.

Orders are authorized by the trader, so the system can only act on trades the trader approved.

The following operations are onchain and settle on Polygon:

credit their Perps account.

Deposits and withdrawals are the only way assets enter or leave the exchange. Trading itself does not produce per-trade onchain transactions.

The exchange periodically commits its trading state onchain in the form of state root commitments. A state root summarizes the offchain ledger at a point in time, including account balances, and lets observers verify that reported exchange state matches what Polymarket has committed to Polygon.

crediting their Perps account.

---
