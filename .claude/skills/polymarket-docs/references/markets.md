# Polymarket-Docs_Docs - Markets

**Pages:** 4

---

## Discover Markets

**URL:** https://docs.polymarket.com/market-data/discover-markets.md

**Contents:**
- Events
  - Fetch an Event
  - List Events
- Markets
  - Fetch a Market
  - List Markets
- Series
  - Fetch a Series
  - List Series
- Sports

Find the events and markets your integration needs, from a specific Polymarket link to a broader view of what is active. This data is public and does not require authentication.

An event groups one or more markets under a shared question set. A single-market event asks one yes/no question; a multi-market event splits a broader question into individual outcomes, such as one market per candidate in an election.

Fetch an event when you already know its identifier.

<Tabs> <Tab title="TypeScript"> Call `fetchEvent()` on a `PublicClient` or `SecureClient` to fetch an event by ID.

<Tab title="Python"> Call `get_event()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch an event by ID. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch an event by ID:

List events when you need a browsable or filterable feed.

<Tabs> <Tab title="TypeScript"> Call `listEvents()` on a `PublicClient` or `SecureClient` to page through events.

<Tab title="Python"> Call `list_events()` on an `AsyncPublicClient` or `AsyncSecureClient` to page through events. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> List active events:

A market is a single yes/no question with two outcome token IDs: one for YES and one for NO.

Fetch a market when you already know its identifier.

<Tabs> <Tab title="TypeScript"> Call `fetchMarket()` on a `PublicClient` or `SecureClient` to fetch a market by ID.

<Tab title="Python"> Call `get_market()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch a market by ID. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch a market by ID:

List markets when you need a filterable feed, such as browsing by tag, sport, or liquidity.

<Tabs> <Tab title="TypeScript"> Call `listMarkets()` on a `PublicClient` or `SecureClient` to page through markets.

<Tab title="Python"> Call `list_markets()` on an `AsyncPublicClient` or `AsyncSecureClient` to page through markets. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> List active markets by tag:

After you choose a market, continue to [Market Details](/market-data/market-details) to extract token IDs and trading fields.

A series groups a recurring set of events under one theme. For example, a weekly Fed rate-decision series has one event per meeting, and a season-long league series has one event per matchup.

Fetch a series by ID.

<Tabs> <Tab title="TypeScript"> Call `fetchSeries()` on a `PublicClient` or `SecureClient` to fetch a series by ID.

<Tab title="Python"> Call `get_series()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch a series by ID. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch a series by ID:

<Tabs> <Tab title="TypeScript"> Call `listSeries()` on a `PublicClient` or `SecureClient` to page through series.

<Tab title="Python"> Call `list_series()` on an `AsyncPublicClient` or `AsyncSecureClient` to page through series. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> List active weekly series:

Sports metadata maps a sport to its Polymarket tags and market types. Use it to browse sports markets by league, look up the valid market types for filtering, find events associated with a game, or resolve team rosters.

<Tabs> <Tab title="TypeScript"> Call `listSports()` on a `PublicClient` or `SecureClient` to list supported sports.

<Tab title="Python"> Call `get_sports()` on an `AsyncPublicClient` or `AsyncSecureClient` to list supported sports. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> List supported sports:

Every sports market carries a market type that tells you which line it prices: a moneyline (which team wins), a spread (win by how much), or a total (over/under a combined score). Fetch the valid values, then pass one or more of them when listing markets to filter.

<Tabs> <Tab title="TypeScript"> Call `fetchSportsMarketTypes()` on a `PublicClient` or `SecureClient` to list the supported market types. When present, a market reports its type in `sports.sportsMarketType`.

<Tab title="Python"> Call `get*sports*market*types()` on an `AsyncPublicClient` or `AsyncSecureClient` to list the supported market types. The synchronous `PublicClient` and `SecureClient` provide the same method. Each market reports its type in `sports.sports*market_type` when present.

<Tab title="API"> List supported sports market types. When present, a market reports its type in `sportsMarketType`:

A sports game's markets can be split across a main event and companion events. Depending on the game, companion events may cover player props, half-time and second-half results, exact score, or additional lines grouped under a more-markets event. Their slugs extend the main event's slug with a suffix such as `-player-props`, `-halftime-result`, or `-more-markets`.

Append a known suffix when you need one companion event. To discover current companion events, use the listing workflow instead of guessing each suffix.

<Tabs> <Tab title="TypeScript"> Call `fetchEvent()` on a `PublicClient` or `SecureClient`. To fetch only the more-markets event, append `-more-markets` to the main event's slug.

<Tab title="Python"> Call `get_event()` on an `AsyncPublicClient` or `AsyncSecureClient`. To fetch only the more-markets event, append `-more-markets` to the main event's slug. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> To fetch only the more-markets event, append `-more-markets` to the main event's slug:

Sports event responses identify which team is designated home and which is designated away. Use this value when aligning Polymarket data with an external sports feed.

<Tabs> <Tab title="TypeScript"> Use `PublicClient.fetchEvent()` or `SecureClient.fetchEvent()` to identify the teams.

<Tab title="Python"> Use `AsyncPublicClient.get*event()` or `AsyncSecureClient.get*event()` to identify the teams.

<Tab title="API"> Fetch the event by slug to identify its home and away teams.

<Warning> Home and away assignments can change after markets are created, especially when games are rescheduled or moved. If you plan to submit quotes in Combos, check [Common Footguns](/trading/combos/market-makers#common-footguns). </Warning>

<Tabs> <Tab title="TypeScript"> Call `listTeams()` on a `PublicClient` or `SecureClient` to page through teams.

<Tab title="Python"> Call `list_teams()` on an `AsyncPublicClient` or `AsyncSecureClient` to page through teams. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> List teams in a league:

Search returns matching events, tags, and profiles for a free-text query in one call. Use it for a search bar or a "jump to market" input.

<Tabs> <Tab title="TypeScript"> Call `search()` on a `PublicClient` or `SecureClient` to search Polymarket.

<Tab title="Python"> Call `search()` on an `AsyncPublicClient` or `AsyncSecureClient` to search Polymarket. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Search Polymarket:

Tags group events and markets by categories, leagues, people, and themes. Each tag can link to multiple ranked related tags, forming a directed graph rather than a strict tree. Use these relationships to expand discovery from one topic to adjacent topics.

Browse the available tags, for example to build a category filter.

<Tabs> <Tab title="TypeScript"> Call `listTags()` on a `PublicClient` or `SecureClient` to page through tags.

<Tab title="Python"> Call `list_tags()` on an `AsyncPublicClient` or `AsyncSecureClient` to page through tags. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> List tags:

Fetch a tag by slug to resolve its numeric ID. You'll need that ID for the `tagId`/`tagIds` filters used earlier in Events and Markets.

<Tabs> <Tab title="TypeScript"> Call `fetchTag()` on a `PublicClient` or `SecureClient` to fetch a tag by slug.

<Tab title="Python"> Call `get_tag()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch a tag by slug. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch a tag by slug:

Get the relationship records that link a tag to related tags, useful for building "you might also like" surfaces. Each record is a lightweight pointer (a rank and the two numeric tag IDs), not a full tag object.

<Tabs> <Tab title="TypeScript"> Call `fetchRelatedTags()` on a `PublicClient` or `SecureClient` to fetch a tag's relationship records.

<Tab title="Python"> Call `get*related*tags()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch a tag's relationship records. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch a tag's relationship records:

Get the full `Tag` objects for a tag's related tags in one call, skipping the extra round trip to fetch each related tag by ID.

<Tabs> <Tab title="TypeScript"> Call `fetchRelatedTagResources()` on a `PublicClient` or `SecureClient` to fetch the related tag objects.

<Tab title="Python"> Call `get*related*tag_resources()` on an `AsyncPublicClient` or `AsyncSecureClient` to fetch the related tag objects. The synchronous `PublicClient` and `SecureClient` provide the same method.

<Tab title="API"> Fetch the related tag objects:

**Examples:**

Example 1 (text):
```text
    const event = await client.fetchEvent({ id: "90177" });

    // event: Event
```

Example 2 (text):
```text
You can also fetch an event by its Polymarket URL or slug:

<CodeGroup>
  ```ts URL theme={null}
  const event = await client.fetchEvent({
    url: "https://polymarket.com/event/will-the-us-confirm-that-aliens-exist-before-2027",
  });
  ```

  ```ts Slug theme={null}
  const event = await client.fetchEvent({
    slug: "will-the-us-confirm-that-aliens-exist-before-2027",
  });
  ```
</CodeGroup>

<Accordion title="Output: Event">
  <CodeGroup>
    ```ts Event Type theme={null}
    type Market = {
      id: string;
      slug?: string | null;
      question?: string | null;
      conditionId: string | null;
      outcomes: {
        yes: { tokenId: string | null };
        no: { tokenId: string | null };
      };
    };

    type Event = {
      id: string;
      slug?: string | null;
      title?: string | null;
      markets: Market[];
    };
    ```

    ```json Event Example theme={null}
    {
      "id": "90177",
      "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
      "title": "Will the US confirm that aliens exist by...?",
      "markets": [
        {
          "id": "703257",
          "slug": "will-the-us-confirm-that-aliens-exist-before-2027-789-924-249",
          "question": "Will the US confirm that aliens exist before 2027?",
          "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
          "outcomes": {
            "yes": {
              "tokenId": "107505882767731489358349912513945399560393482969656700824895970500493757150417"
            },
            "no": {
              "tokenId": "7305630249804085635496399869905769372294302716159034447326228509068694952392"
            }
          }
        },
        "..."
      ]
    }
    ```
  </CodeGroup>
</Accordion>
```

Example 3 (text):
```text
    event = await client.get_event(id="90177")

    # event: Event
```

Example 4 (text):
```text
You can also fetch an event by its Polymarket URL or slug:

<CodeGroup>
  ```python URL theme={null}
  event = await client.get_event(
      url="https://polymarket.com/event/will-the-us-confirm-that-aliens-exist-before-2027",
  )
  ```

  ```python Slug theme={null}
  event = await client.get_event(
      slug="will-the-us-confirm-that-aliens-exist-before-2027",
  )
  ```
</CodeGroup>

<Accordion title="Output: Event">
  <CodeGroup>
    ```python Event Type theme={null}
    class MarketOutcome:
        token_id: str | None

    class MarketOutcomes:
        yes: MarketOutcome
        no: MarketOutcome

    class Market:
        id: str
        slug: str | None
        question: str | None
        condition_id: str | None
        outcomes: MarketOutcomes

    class Event:
        id: str
        slug: str | None
        title: str | None
        markets: tuple[Market, ...]
    ```

    ```json Event Example theme={null}
    {
      "id": "90177",
      "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
      "title": "Will the US confirm that aliens exist by...?",
      "markets": [
        {
          "id": "703257",
          "slug": "will-the-us-confirm-that-aliens-exist-before-2027-789-924-249",
          "question": "Will the US confirm that aliens exist before 2027?",
          "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
          "outcomes": {
            "yes": {
              "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417"
            },
            "no": {
              "token_id": "7305630249804085635496399869905769372294302716159034447326228509068694952392"
            }
          }
        },
        "..."
      ]
    }
    ```
  </CodeGroup>
</Accordion>
```

---

## Markets & Events

**URL:** https://docs.polymarket.com/concepts/markets-events.md

**Contents:**
- Markets
  - Market Example
- Events
  - Single-Market Events
  - Multi-Market Events
- Identifying Markets
- Sports Markets
- Next Steps

Every prediction on Polymarket is structured around two core concepts: **markets** and **events**. Understanding how they relate is essential for building on the platform.

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event-market.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=4c62bd08a405868307cdd6799b368ca5" alt="" className="dark:hidden" width="1540" height="952" data-path="images/core-concepts/event-market.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/event-market.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=2eb5c9b0f8a2afe52bc2e717b7b796a2" alt="" className="hidden dark:block" width="1540" height="952" data-path="images/dark/core-concepts/event-market.png" /> </Frame>

A **market** is the fundamental tradable unit on Polymarket. Each market represents a single binary question with Yes/No outcomes.

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=0c9a264aec9a22ce5a20c4cc7980806d" alt="" className="dark:hidden" width="1540" height="952" data-path="images/core-concepts/event.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/event.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=912e41bebfe8c1a43ef53b89685ca3d2" alt="" className="hidden dark:block" width="1540" height="952" data-path="images/dark/core-concepts/event.png" /> </Frame>

| Identifier       | Description                                                              | | ---------------- | ------------------------------------------------------------------------ | | **Condition ID** | Unique identifier for the market's condition in the CTF contracts        | | **Question ID**  | Hash of the market question used for resolution                          | | **Token IDs**    | ERC1155 token IDs used for trading on the CLOB — one for Yes, one for No |

<Note> Markets can only be traded via the CLOB if `enableOrderBook` is `true`. Some markets may exist onchain but not be available for order book trading. </Note>

A simple market might be:

This creates two outcome tokens:

An **event** is a container that groups one or more related markets together. Events provide organizational structure and enable multi-outcome predictions.

When an event contains just one market, it creates a simple market pair. The event and market are essentially equivalent.

When an event contains two or more markets, it groups related binary questions under one event. Some multi-market events represent mutually exclusive outcomes.

Polymarket links these mutually exclusive markets as a [negative-risk group](/concepts/negative-risk). Exactly one market in the group resolves Yes, while every other market resolves No.

Every market and event has a unique **slug** that appears in the Polymarket URL:

You can use slugs to fetch specific markets or events from the API:

Specifically for sports markets, outstanding limit orders are **automatically cancelled** once the game begins, clearing the order book at the official start time. However, game start times can shift — if a game starts earlier than scheduled, orders may not be cleared in time. Always monitor your orders closely around game start times.

<CardGroup cols={2}> <Card title="Prices & Orderbook" icon="chart-line" href="/concepts/prices-orderbook"> Learn how prices are determined and how the order book works. </Card>

<Card title="Fetching Market Data" icon="code" href="/market-data/overview"> Start querying markets and events from the API. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
Event: Will Bitcoin reach $100,000 by December 2024?
└── Market: Will Bitcoin reach $100,000 by December 2024? (Yes/No)
```

Example 2 (text):
```text
Event: Who will win the 2024 Presidential Election?
├── Market: Donald Trump? (Yes/No)
├── Market: Joe Biden? (Yes/No)
├── Market: Kamala Harris? (Yes/No)
└── Market: Other? (Yes/No)
```

Example 3 (text):
```text
https://polymarket.com/event/fed-decision-in-october
                              └── slug: fed-decision-in-october
```

Example 4 (text):
```text
# Fetch event by slug
curl "https://gamma-api.polymarket.com/events?slug=fed-decision-in-october"
```

---

## Negative Risk Markets

**URL:** https://docs.polymarket.com/concepts/negative-risk.md

**Contents:**
- How It Works
  - Example
- Contract Addresses
- Augmented Negative Risk
  - How Placeholders Work
  - Trading Rules for Augmented Neg Risk
- Technical Details
  - Conversion Mechanics
- Next Steps

**Negative risk** is a mechanism for multi-outcome events where only one outcome can win. It enables capital-efficient trading by allowing positions across all outcomes within an event to be related through a **conversion** operation.

In a standard multi-outcome event, each market is independent. If you want to bet against one outcome, you must buy that outcome's No tokens—but those No tokens have no relationship to the other outcomes.

Negative risk changes this. In a neg risk event:

Consider an event: "Who will win the 2024 Presidential Election?" with three outcomes:

| Outcome | Your Position | | ------- | ------------- | | Trump   | —             | | Harris  | —             | | Other   | 1 No          |

With negative risk, that 1 No on "Other" can be converted into:

| Outcome | After Conversion | | ------- | ---------------- | | Trump   | 1 Yes            | | Harris  | 1 Yes            | | Other   | —                |

This is capital-efficient because betting against one outcome is economically equivalent to betting *for* all other outcomes.

Neg risk markets use different contracts than standard markets:

See [Contracts](/resources/contracts) for the Neg Risk Adapter and Neg Risk CTF Exchange addresses.

Standard negative risk requires the complete set of outcomes to be known at market creation. But sometimes new outcomes emerge after trading begins (e.g., a new candidate enters a race).

**Augmented negative risk** solves this with:

| Outcome Type             | Description                                                   | | ------------------------ | ------------------------------------------------------------- | | **Named outcomes**       | Known outcomes (e.g., "Trump", "Harris")                      | | **Placeholder outcomes** | Reserved slots that can be clarified later (e.g., "Person A") | | **Explicit Other**       | Catches any outcome not explicitly named                      |

<Warning> Only trade on **named outcomes**. Placeholder outcomes should be ignored until they are named or until resolution occurs. The Polymarket UI does not display unnamed outcomes. </Warning>

The conversion operation is atomic and happens through the Neg Risk Adapter:

<CardGroup cols={2}> <Card title="Markets & Events" icon="calendar" href="/concepts/markets-events"> Understand how multi-market events are structured. </Card>

<Card title="Positions & Tokens" icon="coins" href="/concepts/positions-tokens"> Learn about token operations like split, merge, and redeem. </Card> </CardGroup>

---

## Markets

**URL:** https://docs.polymarket.com/perps/learn-about-trading/markets.md

**Contents:**
- Instruments
- Price Feeds

export const PerpsInstrumentsTable = () => { const collapsedRowCount = 10; const instrumentsUrl = "https://api.perpetuals.polymarket.com/v1/info/instruments"; const [instruments, setInstruments] = useState([]); const [error, setError] = useState(null); const [showAll, setShowAll] = useState(false); const [loading, setLoading] = useState(true); const [requestId, setRequestId] = useState(0); useEffect(() => { const controller = new AbortController(); const fetchInstruments = async () => { setLoading(true); setError(null); try { const response = await fetch(instrumentsUrl, { cache: "no-store", signal: controller.signal }); if (!response.ok) { throw new Error(`Request failed with status ${response.status}`); } const data = await response.json(); if (!Array.isArray(data)) { throw new Error("The instruments response was not a list"); } setInstruments([...data].sort((first, second) => first.instrument*id - second.instrument*id)); } catch (requestError) { if (requestError.name !== "AbortError") { setError(requestError); } } finally { if (!controller.signal.aborted) { setLoading(false); } } }; fetchInstruments(); return () => controller.abort(); }, [requestId]); if (loading) { return <div className="not-prose rounded-xl border border-gray-200 p-4 text-sm text-gray-600 dark:border-zinc-800 dark:text-gray-400" role="status"> Loading available instruments… </div>; } if (error) { return <div className="not-prose rounded-xl border border-red-200 p-4 text-sm text-red-700 dark:border-red-900 dark:text-red-300" role="alert"> <p>Could not load the available instruments.</p> <button className="mt-3 rounded-md border border-red-300 px-3 py-1.5 font-medium hover:bg-red-50 dark:border-red-800 dark:hover:bg-red-950" onClick={() => setRequestId(current => current + 1)} type="button"> Try again </button> </div>; } const visibleInstruments = showAll ? instruments : instruments.slice(0, collapsedRowCount); return <div className="not-prose rounded-xl border border-gray-200 dark:border-zinc-800"> <div className="overflow-x-auto"> <table className="w-full table-fixed text-left text-sm"> <colgroup> <col className="w-10" /> <col /> <col /> <col /> <col /> </colgroup> <thead className="border-b border-gray-200 bg-gray-50 text-gray-700 dark:border-zinc-800 dark:bg-zinc-900 dark:text-gray-300"> <tr> <th className="w-10 px-2 py-3 font-medium" scope="col"> ID </th> <th className="px-4 py-3 font-medium" scope="col"> Symbol </th> <th className="px-4 py-3 font-medium" scope="col"> Category </th> <th className="px-4 py-3 font-medium" scope="col"> Base Asset </th> <th className="px-4 py-3 font-medium" scope="col"> Max Leverage </th> </tr> </thead> <tbody className="divide-y divide-gray-200 dark:divide-zinc-800"> {visibleInstruments.map(instrument => <tr key={instrument.instrument*id}> <td className="w-10 min-w-0 px-2 py-3 text-gray-600 dark:text-gray-400"> {instrument.instrument*id} </td> <td className="whitespace-nowrap px-4 py-3 font-mono text-gray-900 dark:text-gray-100"> {instrument.symbol} </td> <td className="whitespace-nowrap px-4 py-3 font-mono text-gray-900 dark:text-gray-100"> {instrument.category} </td> <td className="whitespace-nowrap px-4 py-3 font-mono text-gray-900 dark:text-gray-100"> {instrument.base*asset} </td> <td className="whitespace-nowrap px-4 py-3 text-gray-600 dark:text-gray-400"> {instrument.max*leverage}x </td> </tr>)} </tbody> </table> </div> {instruments.length > collapsedRowCount && <div className="border-t border-gray-200 px-4 py-3 dark:border-zinc-800"> <button aria-expanded={showAll} className="font-medium text-gray-700 hover:text-gray-950 dark:text-gray-300 dark:hover:text-white" onClick={() => setShowAll(current => !current)} type="button"> {showAll ? "Show fewer" : `Show all ${instruments.length} instruments`} </button> </div>} </div>; };

Polymarket Perps markets track underlying assets across indices, commodities, crypto assets, and equities. Each market has its own trading parameters.

Perps markets are represented by instruments, which are the listed perpetual contracts available to trade.

<PerpsInstrumentsTable />

Each instrument also includes details that shape how it trades:

<Note> Market parameters can change as markets evolve. Builders should read live instrument details from [Market Data](/perps/market-data#fetch-instruments) before submitting orders. </Note>

Each market tracks an underlying market through external price feeds. Those feeds drive the [Index Price](/perps/learn-about-trading/index-price), and the Index Price helps anchor the [Mark Price](/perps/learn-about-trading/mark-price).

---
