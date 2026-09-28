# Polymarket-Docs_Docs - Market-Data

**Pages:** 5

---

## Real-Time Data

**URL:** https://docs.polymarket.com/market-data/realtime-data.md

**Contents:**
- Market Stream
- Sports Stream
  - Period Values
  - Game Status Values
- Reference Prices
  - Historical Snapshot
  - Crypto Prices
  - Equity Prices
    - Supported Equity Symbols
    - Market Hours

Use Polymarket's real-time feeds to react as market conditions and related data change. They keep the public market data your application depends on current without repeated polling. For authenticated order and trade updates, see [Real-Time Order Updates](/trading/realtime-order-updates).

Use the market stream to keep your application in sync with changes to a market's order book and trading state.

<Tabs> <Tab title="TypeScript"> Given a `PublicClient` or `SecureClient`, subscribe to the `market` topic with one or more token IDs:

<Tab title="Python"> Given an `AsyncPublicClient` or `AsyncSecureClient`, subscribe to the market stream with a `MarketSpec` containing one or more token IDs:

<Tab title="API"> Connect to the market WebSocket:

Use the sports stream to keep live game information current alongside sports markets. Updates arrive when a game goes live, its score or period changes, or it ends. NFL and CFB updates can also reflect possession changes.

<Warning> Sports data is provided for informational purposes only. It may be delayed, contain errors, or omit recent events. Polymarket does not provide trading or investment advice, and this data should not be used as the basis for a trading decision. </Warning>

<Tabs> <Tab title="TypeScript"> Given a `PublicClient` or `SecureClient`, subscribe to the `sports` topic to receive every game update:

<Tab title="Python"> Given an `AsyncPublicClient` or `AsyncSecureClient`, subscribe with a `SportsSpec` to receive every game update:

<Tab title="API"> Connect to the sports WebSocket:

The meaning and format of a period depend on the sport:

| Values                 | Meaning                              | | ---------------------- | ------------------------------------ | | `1H`, `2H`             | First or second half                 | | `1Q`, `2Q`, `3Q`, `4Q` | Quarter                              | | `HT`                   | Halftime                             | | `FT`                   | Full time in regulation              | | `FT OT`                | Full time after overtime             | | `FT NR`                | Full time with no result             | | `End 1`, `End 2`, …    | End of an MLB inning                 | | `1/3`, `2/3`, `3/3`    | Map number in a best-of-three series | | `1/5`, `2/5`, …        | Map number in a best-of-five series  |

Status values vary by sport and are case-sensitive:

| Sport       | Values                                                                                                                         | | ----------- | ------------------------------------------------------------------------------------------------------------------------------ | | NFL         | `Scheduled`, `InProgress`, `Final`, `F/OT`, `Suspended`, `Postponed`, `Delayed`, `Canceled`, `Forfeit`, `NotNecessary`         | | NHL         | `Scheduled`, `InProgress`, `Final`, `F/OT`, `F/SO`, `Suspended`, `Postponed`, `Delayed`, `Canceled`, `Forfeit`, `NotNecessary` | | MLB         | `Scheduled`, `InProgress`, `Final`, `Suspended`, `Delayed`, `Postponed`, `Canceled`, `Forfeit`, `NotNecessary`                 | | NBA and CBB | `Scheduled`, `InProgress`, `Final`, `F/OT`, `Suspended`, `Postponed`, `Delayed`, `Canceled`, `Forfeit`, `NotNecessary`         | | CFB         | `Scheduled`, `InProgress`, `Final`, `F/OT`, `Suspended`, `Postponed`, `Delayed`, `Canceled`, `Forfeit`                         | | Soccer      | `Scheduled`, `InProgress`, `Break`, `Suspended`, `PenaltyShootout`, `Final`, `Awarded`, `Postponed`, `Canceled`                | | Esports     | `not_started`, `running`, `finished`, `postponed`, `canceled`                                                                  | | Tennis      | `scheduled`, `inprogress`, `suspended`, `finished`, `postponed`, `cancelled`                                                   |

Stream crypto, equity, and time-weighted average reference prices through Polymarket. Authenticate, select the symbols you need, and process historical prices and live updates.

<Note> Reference price subscriptions require authentication. Existing RTDS integrations should follow the [migration guide](/migrate/rtds-to-polybolt). </Note>

Use lowercase symbols. See the [PolyBolt overview](/api-reference/live-data/overview#supported-symbols) for crypto and TWAP lists, and the equity catalog below for equity symbols.

Each new subscription provides a snapshot of the preceding two minutes of prices and live updates. Seed local state from the snapshot, then apply the latest price. Applications that only need live prices can ignore the snapshot.

Stream crypto reference prices in USD to keep prices current alongside related markets.

<Tabs> <Tab title="TypeScript"> Call `client.subscribe` with an authenticated `SecureClient` from `@polymarket/client` 0.11.0 or later. See [Wallet Integrations](/getting-started/typescript#wallet-integrations) to create the client.

<Tab title="Python"> Call `client.subscribe` with an authenticated `AsyncSecureClient` from `polymarket-client` 0.11.0 or later. Complete [Secure Client setup](/getting-started/python#secure-client) first, and run this example inside an async function.

<Tab title="API"> Connect to PolyBolt and authenticate before subscribing to crypto prices.

Stream reference prices for stocks, ETFs, forex pairs, precious metals, and commodities.

<Tabs> <Tab title="TypeScript"> Call `client.subscribe` to subscribe to the `prices.equity` topic and your chosen symbols with an authenticated `SecureClient`.

<Tab title="Python"> Call `client.subscribe` to subscribe to the `prices.equity` topic and your chosen symbols with an authenticated `AsyncSecureClient`.

<Tab title="API"> Reuse the authenticated connection from the [Crypto Prices](#crypto-prices) API example and send this frame to subscribe to AAPL:

| Asset class     | Supported symbols                                                                                               | | --------------- | --------------------------------------------------------------------------------------------------------------- | | Stocks          | `aapl`, `tsla`, `msft`, `googl`, `amzn`, `meta`, `nvda`, `nflx`, `pltr`, `open`, `rklb`, `abnb`, `coin`, `hood` | | ETFs            | `qqq`, `spy`, `ewy`, `vxx`                                                                                      | | Forex           | `eurusd`, `gbpusd`, `usdcad`, `usdjpy`, `usdkrw`                                                                | | Precious metals | `xauusd`, `xagusd`                                                                                              | | Commodities     | `wti`, `cc`, `ngd`                                                                                              |

When the market for an asset is closed, the stream continues with its last known price and marks that value as carried forward. During market hours, prices can update up to five times per second for each feed.

A time-weighted average price (TWAP) represents an asset's price across a lookback window. Stream Chainlink-computed crypto TWAPs with a fixed 60-second window through Polymarket.

<Tabs> <Tab title="TypeScript"> Call `client.subscribe` to subscribe to the `prices.crypto.twap` topic and your chosen symbols with an authenticated `SecureClient`.

<Tab title="Python"> Call `client.subscribe` to subscribe to the `prices.crypto.twap` topic and your chosen symbols with an authenticated `AsyncSecureClient`.

<Tab title="API"> Reuse the authenticated connection from the [Crypto Prices](#crypto-prices) API example and send this frame to subscribe to the 60-second BTC/USD TWAP:

<Warning> Live comment and reaction streaming is being retired without a replacement streaming channel. Check below for the corresponding fetch method. </Warning>

<Tabs> <Tab title="TypeScript"> Create a public client and call `client.listComments()` to list comments for an event. This method does not provide live comment or reaction events.

<Tab title="Python"> Create a public client and call `client.list_comments()` to list comments for an event. This method does not provide live comment or reaction events.

<Tab title="API"> Use `GET /comments` on the Gamma API to list comments for an event. This request does not provide live comment or reaction events.

**Examples:**

Example 1 (text):
```text
    const tokenId = "<token_id>";

    const stream = await client.subscribe([
      {
        topic: "market",
        tokenIds: [tokenId],
      },
    ]);

    for await (const event of stream) {
      switch (event.type) {
        case "book":
          // event: MarketBookEvent
          break;
        case "price_change":
          // event: MarketPriceChangeEvent
          break;
        case "last_trade_price":
          // event: MarketLastTradePriceEvent
          break;
        case "tick_size_change":
          // event: MarketTickSizeChangeEvent
          break;
      }
    }
```

Example 2 (text):
```text
<Accordion title="Standard Market Events">
  #### Order Book

  <CodeGroup>
    ```ts MarketBookEvent Type theme={null}
    type OrderBookLevel = {
      price: DecimalString;
      size: DecimalString;
    };

    type MarketBookEvent = {
      topic: "market";
      type: "book";
      payload: {
        market: string;
        tokenId: TokenId;
        bids: OrderBookLevel[];
        asks: OrderBookLevel[];
        hash?: string | null;
        timestamp?: string | null;
        minOrderSize?: DecimalString | null;
        tickSize?: DecimalString | null;
        negRisk?: boolean | null;
        lastTradePrice?: DecimalString | null;
      };
    };
    ```

    ```json MarketBookEvent Example theme={null}
    {
      "topic": "market",
      "type": "book",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "bids": [{ "price": "0.08", "size": "33343.4" }],
        "asks": [{ "price": "0.09", "size": "163939.58" }],
        "hash": "0xabc123…",
        "timestamp": "1782753357257"
      }
    }
    ```
  </CodeGroup>

  #### Price Change

  <CodeGroup>
    ```ts MarketPriceChangeEvent Type theme={null}
    type PriceChange = {
      tokenId: TokenId;
      price: DecimalString;
      size: DecimalString;
      side: OrderSide;
      hash?: string | null;
      bestBid?: DecimalString | null;
      bestAsk?: DecimalString | null;
    };

    type MarketPriceChangeEvent = {
      topic: "market";
      type: "price_change";
      payload: {
        market: string;
        priceChanges: PriceChange[];
        timestamp?: string | null;
      };
    };
    ```

    ```json MarketPriceChangeEvent Example theme={null}
    {
      "topic": "market",
      "type": "price_change",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "priceChanges": [
          {
            "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
            "price": "0.08",
            "size": "33343.4",
            "side": "BUY",
            "hash": "56621a121a47ed9333273e21c83b660cff37ae50",
            "bestBid": "0.08",
            "bestAsk": "0.09"
          }
        ],
        "timestamp": "1782753357257"
      }
    }
    ```
  </CodeGroup>

  #### Last Trade Price

  <CodeGroup>
    ```ts MarketLastTradePriceEvent Type theme={null}
    type MarketLastTradePriceEvent = {
      topic: "market";
      type: "last_trade_price";
      payload: {
        market: string;
        tokenId: TokenId;
        price: DecimalString;
        size?: DecimalString | null;
        feeRateBps?: DecimalString | null;
        side: OrderSide;
        timestamp?: string | null;
        transactionHash?: string | null;
      };
    };
    ```

    ```json MarketLastTradePriceEvent Example theme={null}
    {
      "topic": "market",
      "type": "last_trade_price",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "price": "0.08",
        "size": "219.217767",
        "feeRateBps": "0",
        "side": "SELL",
        "timestamp": "1782753357257",
        "transactionHash": "0xeeefff…"
      }
    }
    ```
  </CodeGroup>

  #### Tick Size Change

  <CodeGroup>
    ```ts MarketTickSizeChangeEvent Type theme={null}
    type MarketTickSizeChangeEvent = {
      topic: "market";
      type: "tick_size_change";
      payload: {
        market: string;
        tokenId: TokenId;
        oldTickSize?: DecimalString | null;
        newTickSize: DecimalString;
        timestamp?: string | null;
      };
    };
    ```

    ```json MarketTickSizeChangeEvent Example theme={null}
    {
      "topic": "market",
      "type": "tick_size_change",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "oldTickSize": "0.01",
        "newTickSize": "0.001",
        "timestamp": "1782753357257"
      }
    }
    ```
  </CodeGroup>
</Accordion>

Enable `customFeatureEnabled` to include top-of-book and market lifecycle
updates:

```ts theme={null}
const stream = await client.subscribe([
  {
    topic: "market",
    tokenIds: [tokenId],
    customFeatureEnabled: true,
  },
]);

for await (const event of stream) {
  switch (event.type) {
    case "book":
      // event: MarketBookEvent
      break;
    case "price_change":
      // event: MarketPriceChangeEvent
      break;
    case "last_trade_price":
      // event: MarketLastTradePriceEvent
      break;
    case "tick_size_change":
      // event: MarketTickSizeChangeEvent
      break;
    case "best_bid_ask":
      // event: MarketBestBidAskEvent
      break;
    case "new_market":
      // event: NewMarketEvent
      break;
    case "market_resolved":
      // event: MarketResolvedEvent
      break;
  }
}
```

<Accordion title="Additional Market Events">
  #### Best Bid and Ask

  <CodeGroup>
    ```ts MarketBestBidAskEvent Type theme={null}
    type MarketBestBidAskEvent = {
      topic: "market";
      type: "best_bid_ask";
      payload: {
        market: string;
        tokenId: TokenId;
        bestBid?: DecimalString | null;
        bestAsk?: DecimalString | null;
        spread?: DecimalString | null;
        timestamp?: string | null;
      };
    };
    ```

    ```json MarketBestBidAskEvent Example theme={null}
    {
      "topic": "market",
      "type": "best_bid_ask",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "bestBid": "0.08",
        "bestAsk": "0.09",
        "spread": "0.01",
        "timestamp": "1782753357257"
      }
    }
    ```
  </CodeGroup>

  #### New Market

  <CodeGroup>
    ```ts NewMarketEvent Type theme={null}
    type NewMarketEvent = {
      topic: "market";
      type: "new_market";
      payload: {
        id: string;
        question?: string | null;
        market: string;
        slug?: string | null;
        description?: string | null;
        tokenIds?: TokenId[] | null;
        outcomes?: string[] | null;
        eventMessage?: {
          id: string;
          ticker?: string | null;
          slug?: string | null;
          title?: string | null;
          description?: string | null;
        } | null;
        timestamp?: string | null;
        tags?: string[] | null;
        conditionId?: CtfConditionId | null;
        active?: boolean | null;
        clobTokenIds?: string[] | null;
        sportsMarketType?: string | null;
        line?: DecimalString | null;
        gameStartTime?: IsoDateTimeString | null;
        orderPriceMinTickSize?: DecimalString | null;
        groupItemTitle?: string | null;
        takerBaseFee?: DecimalString | null;
        feesEnabled?: boolean | null;
        feeSchedule?: unknown;
      };
    };
    ```

    ```json NewMarketEvent Example theme={null}
    {
      "topic": "market",
      "type": "new_market",
      "payload": {
        "id": "123456",
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "question": "Will the US confirm that aliens exist before 2027?",
        "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
        "tokenIds": [
          "107505882767731489358349912513945399560393482969656700824895970500493757150417",
          "7305630249804085635496399869905769372294302716159034447326228509068694952392"
        ],
        "outcomes": ["Yes", "No"],
        "active": true,
        "timestamp": "1782753357257"
      }
    }
    ```
  </CodeGroup>

  #### Market Resolved

  <CodeGroup>
    ```ts MarketResolvedEvent Type theme={null}
    type MarketResolvedEvent = {
      topic: "market";
      type: "market_resolved";
      payload: {
        id: string;
        market: string;
        tokenIds?: TokenId[] | null;
        winningTokenId?: TokenId | null;
        winningOutcome?: string | null;
        eventMessage?: {
          id: string;
          ticker?: string | null;
          slug?: string | null;
          title?: string | null;
          description?: string | null;
        } | null;
        timestamp?: string | null;
        tags?: string[] | null;
      };
    };
    ```

    ```json MarketResolvedEvent Example theme={null}
    {
      "topic": "market",
      "type": "market_resolved",
      "payload": {
        "id": "123456",
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "tokenIds": [
          "107505882767731489358349912513945399560393482969656700824895970500493757150417",
          "7305630249804085635496399869905769372294302716159034447326228509068694952392"
        ],
        "winningTokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "winningOutcome": "Yes",
        "timestamp": "1782753357257"
      }
    }
    ```
  </CodeGroup>
</Accordion>
```

Example 3 (text):
```text
    from polymarket.streams import MarketSpec

    token_id = "<token_id>"

    async with await client.subscribe(
        MarketSpec(token_ids=[token_id]),
    ) as stream:
        async for event in stream:
            if event.type == "book":
                ...  # event: MarketBookEvent
            elif event.type == "price_change":
                ...  # event: MarketPriceChangeEvent
            elif event.type == "last_trade_price":
                ...  # event: MarketLastTradePriceEvent
            elif event.type == "tick_size_change":
                ...  # event: MarketTickSizeChangeEvent
```

Example 4 (python):
```python
<Accordion title="Standard Market Events">
  #### Order Book

  <CodeGroup>
    ```python MarketBookEvent Type theme={null}
    class OrderBookLevel:
        price: Decimal
        size: Decimal

    class MarketBookPayload:
        market: str
        token_id: TokenId
        bids: tuple[OrderBookLevel, ...]
        asks: tuple[OrderBookLevel, ...]
        hash: str | None
        timestamp: datetime | None
        min_order_size: Decimal | None
        tick_size: Decimal | None
        neg_risk: bool | None
        last_trade_price: Decimal | None

    class MarketBookEvent:
        topic: Literal["market"]
        type: Literal["book"]
        payload: MarketBookPayload
    ```

    ```json MarketBookEvent Example theme={null}
    {
      "topic": "market",
      "type": "book",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "bids": [{ "price": "0.08", "size": "33343.4" }],
        "asks": [{ "price": "0.09", "size": "163939.58" }],
        "hash": "0xabc123…",
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>

  #### Price Change

  <CodeGroup>
    ```python MarketPriceChangeEvent Type theme={null}
    class PriceChange:
        token_id: TokenId
        price: Decimal
        size: Decimal
        side: Literal["BUY", "SELL"]
        hash: str | None
        best_bid: Decimal | None
        best_ask: Decimal | None

    class MarketPriceChangePayload:
        market: str
        price_changes: tuple[PriceChange, ...]
        timestamp: datetime | None

    class MarketPriceChangeEvent:
        topic: Literal["market"]
        type: Literal["price_change"]
        payload: MarketPriceChangePayload
    ```

    ```json MarketPriceChangeEvent Example theme={null}
    {
      "topic": "market",
      "type": "price_change",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "price_changes": [
          {
            "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
            "price": "0.08",
            "size": "33343.4",
            "side": "BUY",
            "hash": "56621a121a47ed9333273e21c83b660cff37ae50",
            "best_bid": "0.08",
            "best_ask": "0.09"
          }
        ],
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>

  #### Last Trade Price

  <CodeGroup>
    ```python MarketLastTradePriceEvent Type theme={null}
    class MarketLastTradePricePayload:
        market: str
        token_id: TokenId
        price: Decimal
        size: Decimal | None
        side: Literal["BUY", "SELL"]
        fee_rate_bps: Decimal | None
        transaction_hash: str | None
        timestamp: datetime | None

    class MarketLastTradePriceEvent:
        topic: Literal["market"]
        type: Literal["last_trade_price"]
        payload: MarketLastTradePricePayload
    ```

    ```json MarketLastTradePriceEvent Example theme={null}
    {
      "topic": "market",
      "type": "last_trade_price",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "price": "0.08",
        "size": "219.217767",
        "side": "SELL",
        "fee_rate_bps": "0",
        "transaction_hash": "0xeeefff…",
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>

  #### Tick Size Change

  <CodeGroup>
    ```python MarketTickSizeChangeEvent Type theme={null}
    class MarketTickSizeChangePayload:
        market: str
        token_id: TokenId
        old_tick_size: Decimal | None
        new_tick_size: Decimal
        timestamp: datetime | None

    class MarketTickSizeChangeEvent:
        topic: Literal["market"]
        type: Literal["tick_size_change"]
        payload: MarketTickSizeChangePayload
    ```

    ```json MarketTickSizeChangeEvent Example theme={null}
    {
      "topic": "market",
      "type": "tick_size_change",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "old_tick_size": "0.01",
        "new_tick_size": "0.001",
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>
</Accordion>

Enable `custom_feature_enabled` to include top-of-book and market lifecycle
updates:

```python theme={null}
async with await client.subscribe(
    MarketSpec(token_ids=[token_id], custom_feature_enabled=True),
) as stream:
    async for event in stream:
        if event.type == "book":
            ...  # event: MarketBookEvent
        elif event.type == "price_change":
            ...  # event: MarketPriceChangeEvent
        elif event.type == "last_trade_price":
            ...  # event: MarketLastTradePriceEvent
        elif event.type == "tick_size_change":
            ...  # event: MarketTickSizeChangeEvent
        elif event.type == "best_bid_ask":
            ...  # event: MarketBestBidAskEvent
        elif event.type == "new_market":
            ...  # event: NewMarketEvent
        elif event.type == "market_resolved":
            ...  # event: MarketResolvedEvent
```

<Accordion title="Additional Market Events">
  #### Best Bid and Ask

  <CodeGroup>
    ```python MarketBestBidAskEvent Type theme={null}
    class MarketBestBidAskPayload:
        market: str
        token_id: TokenId
        best_bid: Decimal | None
        best_ask: Decimal | None
        spread: Decimal | None
        timestamp: datetime | None

    class MarketBestBidAskEvent:
        topic: Literal["market"]
        type: Literal["best_bid_ask"]
        payload: MarketBestBidAskPayload
    ```

    ```json MarketBestBidAskEvent Example theme={null}
    {
      "topic": "market",
      "type": "best_bid_ask",
      "payload": {
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "best_bid": "0.08",
        "best_ask": "0.09",
        "spread": "0.01",
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>

  #### New Market

  <CodeGroup>
    ```python NewMarketEvent Type theme={null}
    class MarketEventMessage:
        id: str
        ticker: str | None
        slug: str | None
        title: str | None
        description: str | None

    class NewMarketPayload:
        id: str
        market: str
        question: str | None
        slug: str | None
        description: str | None
        token_ids: tuple[TokenId, ...] | None
        outcomes: tuple[str, ...] | None
        event_message: MarketEventMessage | None
        timestamp: datetime | None
        tags: tuple[str, ...] | None
        condition_id: CtfConditionId | None
        active: bool | None
        clob_token_ids: tuple[str, ...] | None
        sports_market_type: str | None
        line: Decimal | None
        game_start_time: datetime | None
        order_price_min_tick_size: Decimal | None
        group_item_title: str | None
        taker_base_fee: Decimal | None
        fees_enabled: bool | None
        fee_schedule: object | None

    class NewMarketEvent:
        topic: Literal["market"]
        type: Literal["new_market"]
        payload: NewMarketPayload
    ```

    ```json NewMarketEvent Example theme={null}
    {
      "topic": "market",
      "type": "new_market",
      "payload": {
        "id": "123456",
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "question": "Will the US confirm that aliens exist before 2027?",
        "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
        "token_ids": [
          "107505882767731489358349912513945399560393482969656700824895970500493757150417",
          "7305630249804085635496399869905769372294302716159034447326228509068694952392"
        ],
        "outcomes": ["Yes", "No"],
        "active": true,
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>

  #### Market Resolved

  <CodeGroup>
    ```python MarketResolvedEvent Type theme={null}
    class MarketResolvedPayload:
        id: str
        market: str
        token_ids: tuple[TokenId, ...] | None
        winning_token_id: TokenId | None
        winning_outcome: str | None
        event_message: MarketEventMessage | None
        timestamp: datetime | None
        tags: tuple[str, ...] | None

    class MarketResolvedEvent:
        topic: Literal["market"]
        type: Literal["market_resolved"]
        payload: MarketResolvedPayload
    ```

    ```json MarketResolvedEvent Example theme={null}
    {
      "topic": "market",
      "type": "market_resolved",
      "payload": {
        "id": "123456",
        "market": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
        "token_ids": [
          "107505882767731489358349912513945399560393482969656700824895970500493757150417",
          "7305630249804085635496399869905769372294302716159034447326228509068694952392"
        ],
        "winning_token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
        "winning_outcome": "Yes",
        "timestamp": "2026-06-29T17:15:57.257000Z"
      }
    }
    ```
  </CodeGroup>
</Accordion>
```

---

## Analytics

**URL:** https://docs.polymarket.com/market-data/public-analytics.md

**Contents:**
- Market Activity
  - Recent Trades
  - Open Interest
  - Market Holders
  - Event Live Volume
  - Market Resolution
- Trader Leaderboard
- Biggest Winners
- Builder Analytics
  - Builder Leaderboard

Use these reads to understand where trading activity is concentrated and how traders and integrations perform over time.

The examples below assume you already have a market object. To find or fetch one, see [**Discover Markets**](/market-data/discover-markets).

<Tabs> <Tab title="TypeScript"> Given a market, read its condition and event IDs:

<Tab title="Python"> Given a market, read its condition and event IDs:

<Tab title="API"> Given a market object, its condition and event IDs are available in these fields:

Review the trades recently matched in a market, including their side, price, size, outcome, wallet, and timestamp.

<Tabs> <Tab title="TypeScript"> Call `listTrades()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `list_trades()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> List recent trades for a market:

Measure the value currently held in outstanding positions for one or more markets.

<Tabs> <Tab title="TypeScript"> Call `fetchOpenInterest()` on a `PublicClient` or `SecureClient`. Pass up to 20 condition IDs, or omit `conditionIds` for the single global figure (served as `conditionId: null`).

<Tab title="Python"> Call `get*open*interests()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Fetch open interest for a market:

Find the largest public holders for each outcome token in a market.

<Tabs> <Tab title="TypeScript"> Call `listMarketHolders()` on a `PublicClient` or `SecureClient` and walk the cursor pages. `pageSize` applies separately to each outcome token, so merge groups by `assetId` across pages. Set `includePnl: true` (one condition ID, page size at most 100) to add position economics to every holder row.

<Tab title="Python"> Call `list*market*holders()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> List the largest holders for a market:

Summarize activity across an event and break the volume down by market.

<Tabs> <Tab title="TypeScript"> Call `fetchEventLiveVolume()` on a `PublicClient` or `SecureClient`. Pass one or more event IDs; a list spans events and returns one combined result.

<Tab title="Python"> Call `get*event*live_volume()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Fetch live volume for an event:

Check a market's resolution progress.

<Tabs> <Tab title="TypeScript"> Call `fetchResolutions()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `get_resolutions()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Fetch resolution progress for the market:

Compare trader volume and profit and loss over a selected period.

<Tabs> <Tab title="TypeScript"> Call `listTraderLeaderboard()` on a `PublicClient` or `SecureClient`. `window` defaults to one day, `category` to overall, and `sortBy` to PnL. Tied traders share a rank and the next rank skips.

<Tab title="Python"> Call `list*trader*leaderboard()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> List the trader leaderboard for a time period. The board ranks by PnL by default; pass `sort_by=VOLUME` for the volume board:

Compare individual winning positions by their profit at resolution.

<Tabs> <Tab title="TypeScript"> Call `listBiggestWinners()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `list*biggest*winners()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> List the largest wins resolved in the last day:

Evaluate the reach of a builder integration through its attributed trading activity.

Compare builders by attributed volume and active users.

<Tabs> <Tab title="TypeScript"> Call `listBuilderLeaderboard()` on a `PublicClient` or `SecureClient`.

<Tab title="Python"> Call `list*builder*leaderboard()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> List the builder leaderboard for a time period:

Track attributed builder volume and active users over time.

<Tabs> <Tab title="TypeScript"> Call `fetchBuilderVolume()` on a `PublicClient` or `SecureClient`. `interval` picks the bucket width and `bucketLimit` counts the most recent complete buckets (at most 90); every builder active in a bucket gets one row.

<Tab title="Python"> Call `get*builder*volumes()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Fetch builder volume over time. Each row is one builder's volume in one time bucket, with the builder's rank within that bucket; `limit` counts the most recent buckets:

**Examples:**

Example 1 (text):
```text
    const conditionId = market.conditionId;
    const eventId = market.events[0].id;
```

Example 2 (text):
```text
    condition_id = market.condition_id
    event_id = market.events[0].id
```

Example 3 (text):
```text
    {
      "conditionId": "<condition_id>",
      "events": [{ "id": "<event_id>" }]
    }
```

Example 4 (text):
```text
Assign the identifiers for the requests below:

```bash theme={null}
CONDITION_ID="<condition_id>"
EVENT_ID="<event_id>"
```
```

---

## Prices and Order Books

**URL:** https://docs.polymarket.com/market-data/prices-order-books.md

**Contents:**
- Order Book
  - Fetch an Order Book
  - Fetch Multiple Order Books
- Best Market Price
  - Fetch a Price
  - Fetch Multiple Prices
- Midpoint Price
  - Fetch a Midpoint
  - Fetch Multiple Midpoints
- Spread

Each Polymarket outcome is represented by a token traded on the CLOB. Its price reflects what traders are willing to pay for that outcome, while its order book shows the resting bids and asks.

The examples below assume you already have a market object from which to read the outcome token IDs. To find or fetch one, see [**Discover Markets**](/market-data/discover-markets).

<Tabs> <Tab title="TypeScript"> Given a market, read its outcome token IDs:

<Tab title="Python"> Given a market, read its outcome token IDs:

<Tab title="API"> Given a market object, its outcome token IDs are stored as a JSON-encoded array:

Retrieve the resting bids and asks for one outcome token. Bids are ordered by ascending price and asks by descending price, so the best bid and ask are the last entries in their respective arrays. Each response also includes a `hash` for the order-book state. Compare it with the previous response's hash to determine whether the book changed between reads.

<Tabs> <Tab title="TypeScript"> Call `fetchOrderBook()` on a `PublicClient` or `SecureClient` to fetch an outcome's order book.

<Tab title="Python"> Call `get*order*book()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch an outcome's order book. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch an outcome's order book:

Batch order-book reads return the resting bids and asks for several outcomes in one request.

<Info>Maximum 500 items per request.</Info>

<Tabs> <Tab title="TypeScript"> Call `fetchOrderBooks()` on a `PublicClient` or `SecureClient` to fetch several order books in one request.

<Tab title="Python"> Call `get*order*books()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch several order books in one request. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch several order books in one request:

Read the best available execution price for an outcome and side. `BUY` returns the lowest ask, which is the price you would pay to buy. `SELL` returns the highest bid, which is the price you would receive when selling.

<Tabs> <Tab title="TypeScript"> Call `fetchPrice()` on a `PublicClient` or `SecureClient` to fetch the best price for one side. For a `BUY`, the method returns the lowest ask.

<Tab title="Python"> Call `get_price()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch the best price for one side. For a `BUY`, the method returns the lowest ask. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch the lowest ask available to a buyer:

Batch price reads return the best market price for several outcome-and-side pairs in one request. Use them when the same view or calculation needs more than one outcome.

<Info>Maximum 500 items per request.</Info>

<Tabs> <Tab title="TypeScript"> Call `fetchPrices()` on a `PublicClient` or `SecureClient` to fetch several prices in one request.

<Tab title="Python"> Call `get_prices()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch several prices in one request. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch several prices in one request:

The midpoint is the average of the best bid and best ask. It provides a reference price between the two sides of the order book.

<Tabs> <Tab title="TypeScript"> Call `fetchMidpoint()` on a `PublicClient` or `SecureClient` to fetch the midpoint.

<Tab title="Python"> Call `get_midpoint()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch the midpoint. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch the midpoint:

Fetch midpoint prices for several outcomes in one request.

<Info>Maximum 500 items per request.</Info>

<Tabs> <Tab title="TypeScript"> Call `fetchMidpoints()` on a `PublicClient` or `SecureClient` to fetch several midpoints.

<Tab title="Python"> Call `get_midpoints()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch several midpoints. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch several midpoints in one request:

The spread is the difference between the best ask and best bid. A narrower spread indicates that the two sides of the order book are closer together.

<Tabs> <Tab title="TypeScript"> Call `fetchSpread()` on a `PublicClient` or `SecureClient` to fetch the spread.

<Tab title="Python"> Call `get_spread()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch the spread. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch the spread:

Batch spread reads return the bid-ask spread for several outcomes in one request.

<Info>Maximum 500 items per request.</Info>

<Tabs> <Tab title="TypeScript"> Call `fetchSpreads()` on a `PublicClient` or `SecureClient` to fetch several spreads in one request.

<Tab title="Python"> Call `get_spreads()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch several spreads in one request. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch several spreads in one request:

Use the last trade price to see where an outcome most recently traded.

<Tabs> <Tab title="TypeScript"> Call `fetchLastTradePrice()` on a `PublicClient` or `SecureClient` to fetch the last trade.

<Tab title="Python"> Call `get*last*trade_price()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch the last trade. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch the last trade:

Fetch the most recent matched trade for several outcomes in one request.

<Info>Maximum 500 items per request.</Info>

<Tabs> <Tab title="TypeScript"> Call `fetchLastTradePrices()` on a `PublicClient` or `SecureClient` to fetch several last trades.

<Tab title="Python"> Call `get*last*trade_prices()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch several last trades. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch several last trade prices in one request:

Tokens that have never traded are omitted from the multi-token response.

Read historical prices for an outcome token over a selected time period.

<Tabs> <Tab title="TypeScript"> Call `listPriceHistory()` on a `PublicClient` or `SecureClient`. Choose a relative window, an explicit time range, or a point in time.

<Tab title="Python"> Call `list*price*history()` on an existing `AsyncPublicClient` or `AsyncSecureClient`.

<Tab title="API"> Pass `token*id` and exactly one time form: `interval` for a relative window, `start` (with optional `end`, epoch seconds, at most 15 days) for an absolute range, or `as*of` for a point-in-time read. `bucket_seconds` sets the bucket width in seconds; deeper pages come from `?cursor=`.

**Examples:**

Example 1 (text):
```text
    const yesTokenId = market.outcomes.yes.tokenId!;
    const noTokenId = market.outcomes.no.tokenId!;
```

Example 2 (text):
```text
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
Parse the array, then select the outcome you want to read:

```bash theme={null}
TOKEN_ID="<yes_token_id>"
```
```

---

## Overview

**URL:** https://docs.polymarket.com/market-data/overview.md

**Contents:**
- Understand the Data Model
- Choose a Workflow

Market data starts with identifying the event, market, or outcome your application cares about. The pages in this section take you from that choice to the data your application needs.

On Polymarket, an event groups one or more markets. Each market is a tradable question with YES and NO outcomes, and each outcome has its own token ID. Use the token ID for the outcome whose price or order book you want to read.

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=0c9a264aec9a22ce5a20c4cc7980806d" alt="" className="dark:hidden" width="1540" height="952" data-path="images/core-concepts/event.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/event.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=912e41bebfe8c1a43ef53b89685ca3d2" alt="" className="hidden dark:block" width="1540" height="952" data-path="images/dark/core-concepts/event.png" /> </Frame>

<Steps> <Step title="Discover an event"> Browse active events, search by topic, or fetch an event directly from its Polymarket URL. </Step>

<Step title="Select a market"> Inspect the event's markets and choose the specific question your app cares about. </Step>

<Step title="Choose an outcome"> Choose YES or NO and keep its token ID. You'll use it to read prices, access the order book, and place orders. </Step>

<Step title="Read or stream data"> Use the identifiers you've collected to retrieve or stream the market data your application needs. </Step> </Steps>

If you are new to Polymarket market data, start with [Discover Markets](/market-data/discover-markets).

<CardGroup cols={2}> <Card title="Discover Markets" icon="magnifying-glass" href="/market-data/discover-markets"> Find the events and markets your application cares about. </Card>

<Card title="Get Market Details" icon="list-tree" href="/market-data/market-details"> Understand a market's outcomes, status, trading constraints, fees, and other properties. </Card>

<Card title="Prices and Order Books" icon="chart-line" href="/market-data/prices-order-books"> Understand current pricing and liquidity, or inspect how prices have changed. </Card>

<Card title="Analytics" icon="chart-column" href="/market-data/public-analytics"> Analyze market activity and compare trader and builder performance. </Card>

<Card title="Real-Time Data" icon="radio" href="/market-data/realtime-data"> Keep your application current as markets and related data change. </Card>

<Card title="Chainlink TWAP Prices" icon="clock" href="/market-data/realtime-data#twap-prices"> Stream Chainlink-computed 60-second time-weighted crypto prices. </Card> </CardGroup>

---

## Market Details

**URL:** https://docs.polymarket.com/market-data/market-details.md

**Contents:**
- Market Identifiers
- Market Outcomes
- Market Status
  - Identify Augmented Negative Risk
- Trading Constraints
- Trading Fees
- Liquidity Reward Settings
- Market Timing
- Liquidity and Activity

The market object represents a prediction market. Alongside its question and outcomes, it describes the market's current state and provides the information an integration needs to read prices, follow activity, or trade.

The examples below assume you already have a market object. To find or fetch one, see [Discover Markets](/market-data/discover-markets).

<Tabs> <Tab title="TypeScript"> Let's say you fetched a market with `fetchMarket()` on a `PublicClient` or `SecureClient`:

<Tab title="Python"> Let's say you fetched a market with `get_market()` on an `AsyncPublicClient` or `AsyncSecureClient`:

<Tab title="API"> Let's say you fetched a market from the Gamma API:

A market has three identifiers, each used in a different context:

| Identifier   | Use it for                                                            | | ------------ | --------------------------------------------------------------------- | | Market ID    | Fetching a known market by its Gamma ID.                              | | Market slug  | Fetching a known market or linking to its human-readable page.        | | Condition ID | Public analytics, positions, and some trading or lifecycle workflows. |

<Tabs> <Tab title="TypeScript"> Read the identifiers from the market object:

<Tab title="Python"> Read the identifiers from the market object:

<Tab title="API"> Read the identifiers from the Gamma response:

Each market has YES and NO outcomes. Each outcome includes a label, current price, and CLOB token ID. The token ID connects the market to order book and trading requests.

<Tabs> <Tab title="TypeScript"> Read both outcomes from `market.outcomes`:

<Tab title="Python"> Read both outcomes from `market.outcomes`:

<Tab title="API"> Gamma returns the outcome labels, prices, and CLOB token IDs as JSON-encoded arrays:

Market status tells you whether a market is currently available for trading. Check it before relying on live prices or submitting an order, since a market may exist before its order book opens and remain discoverable after it closes. It also indicates whether the market belongs to a [negative-risk group](/concepts/negative-risk), where only one of several mutually exclusive markets can resolve YES.

<Tabs> <Tab title="TypeScript"> Read market status from `market.state`:

<Tab title="Python"> Read market status from `market.state`:

<Tab title="API"> Read the corresponding fields from the Gamma response:

Negative-risk membership is a market-level property, but augmented negative risk is configured on the event. After confirming that the market's `negRisk` value is `true`, fetch its event and check that augmented negative risk is enabled:

<Tabs> <Tab title="TypeScript"> Fetch the event referenced by the market, then check its trading configuration:

<Tab title="Python"> Fetch the event referenced by the market, then check its trading configuration:

<Tab title="API"> Read the event ID from the market's `events` array, then fetch that event:

See [Augmented Negative Risk](/concepts/negative-risk#augmented-negative-risk) for how named outcomes, placeholders, and Other behave.

Every market enforces a minimum price increment, also known as the **tick size**, and a minimum order size. The minimum price increment defines the grid of prices you can submit; an order price must be a multiple of the active value. Orders smaller than the minimum order size are rejected.

| Minimum price increment | Step size | Example prices               | | ----------------------- | --------- | ---------------------------- | | `0.1`                   | 10¢       | `0.1`, `0.5`, `0.9`          | | `0.01`                  | 1¢        | `0.01`, `0.50`, `0.99`       | | `0.005`                 | 0.5¢      | `0.005`, `0.500`, `0.995`    | | `0.0025`                | 0.25¢     | `0.0025`, `0.5000`, `0.9975` | | `0.001`                 | 0.1¢      | `0.001`, `0.500`, `0.999`    | | `0.0001`                | 0.01¢     | `0.0001`, `0.5000`, `0.9999` |

<Note> The `0.0025` (0.25¢) increment applies only to World Cup *to advance*, *moneyline*, *spreads*, and *totals* markets. Always read the active value from the market rather than assuming a fixed increment. </Note>

Read the active constraints for a market in your integration:

<Tabs> <Tab title="TypeScript"> Read the market's trading constraints:

<Tab title="Python"> Read the market's trading constraints:

<Tab title="API"> Read the corresponding fields from the Gamma response:

Some markets charge trading fees. The fee schedule determines how fees vary with price, which side pays them, and what share is returned to makers.

<Tabs> <Tab title="TypeScript"> Read the market's fee configuration:

<Tab title="Python"> Read the market's fee configuration:

<Tab title="API"> Read the corresponding fields from the Gamma response:

Liquidity reward settings determine which resting orders can qualify for incentives and how much funding is available. An order must meet the market's minimum qualifying size and remain within its maximum qualifying spread. See [Liquidity Rewards](/programs/liquidity-rewards) for the scoring methodology.

<Tabs> <Tab title="TypeScript"> Read liquidity reward settings from `market.rewards`:

<Tab title="Python"> Read liquidity reward settings from `market.rewards`:

<Tab title="API"> Read the corresponding fields from the Gamma response:

Market timing places a market within its expected schedule. Markets include start and end dates, while sports markets may also include the scheduled start time of the game.

<Tabs> <Tab title="TypeScript"> Read timing data from the market's state, trading configuration, and sports metadata:

<Tab title="Python"> Read timing data from the market's state, trading configuration, and sports metadata:

<Tab title="API"> Read the corresponding fields from the Gamma response:

See [Place Orders](/trading/place-orders#place-a-market-order) for the implications of trading on a market with a configured delay.

Liquidity, volume, and recent price activity describe how actively a market trades. Use them to compare markets or monitor changes over time.

<Tabs> <Tab title="TypeScript"> Read the market's liquidity, volume, and price summary:

<Tab title="Python"> Read the market's liquidity, volume, and price summary:

<Tab title="API"> Read the corresponding fields from the Gamma response:

**Examples:**

Example 1 (text):
```text
    const market = await client.fetchMarket({
      slug: "will-the-us-confirm-that-aliens-exist-before-2027-789-924-249",
    });
    // market: Market
```

Example 2 (text):
```text
    market = await client.get_market(
        slug="will-the-us-confirm-that-aliens-exist-before-2027-789-924-249",
    )
    # market: Market
```

Example 3 (text):
```text
    curl "https://gamma-api.polymarket.com/markets/slug/will-the-us-confirm-that-aliens-exist-before-2027-789-924-249"
```

Example 4 (text):
```text
    const marketId = market.id;
    const slug = market.slug;
    const conditionId = market.conditionId;
```

---
