# Polymarket-Docs_Docs - Other

**Pages:** 19

---

## Contracts

**URL:** https://docs.polymarket.com/resources/contracts.md

**Contents:**
- Core Trading Contracts
- Combos Contracts
- Collateral Contracts
- Wallet Factory Contracts
- Resolution Contracts
- Security
  - Audits
  - Bug Bounty
- Source Code

All Polymarket contracts are deployed on **Polygon mainnet** (Chain ID: 137). This is the single source of truth for all contract addresses used across the platform.

| Contract                               | Address                                                                                                                    | | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | | CTF Exchange                           | [`0xE111180000d2663C0091e4f400237545B87B996B`](https://polygonscan.com/address/0xE111180000d2663C0091e4f400237545B87B996B) | | Neg Risk CTF Exchange                  | [`0xe2222d279d744050d28e00520010520000310F59`](https://polygonscan.com/address/0xe2222d279d744050d28e00520010520000310F59) | | Neg Risk Adapter (CLOB v1, deprecated) | [`0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296`](https://polygonscan.com/address/0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296) | | Conditional Tokens (CTF)               | [`0x4D97DCd97eC945f40cF65F87097ACe5EA0476045`](https://polygonscan.com/address/0x4D97DCd97eC945f40cF65F87097ACe5EA0476045) |

| Contract                    | Address                                                                                                                    | | --------------------------- | -------------------------------------------------------------------------------------------------------------------------- | | PositionManager (proxy)     | [`0x006F54F7f9A22e0000CC2AB60031000000ae9fEF`](https://polygonscan.com/address/0x006F54F7f9A22e0000CC2AB60031000000ae9fEF) | | PositionManager (impl)      | [`0x30c038F0Dae8dcC3E6AD51D016F50821D32Cb87e`](https://polygonscan.com/address/0x30c038F0Dae8dcC3E6AD51D016F50821D32Cb87e) | | BinaryModule (proxy)        | [`0x1000008dD9001B968442c1000017eaE6E0dA00Ba`](https://polygonscan.com/address/0x1000008dD9001B968442c1000017eaE6E0dA00Ba) | | BinaryModule (impl)         | [`0x492FEc596eC347459E1Ebe30b9245EB3B49B1BBa`](https://polygonscan.com/address/0x492FEc596eC347459E1Ebe30b9245EB3B49B1BBa) | | NegRiskModule (proxy)       | [`0x200000900045e3B6259600682756002200028933`](https://polygonscan.com/address/0x200000900045e3B6259600682756002200028933) | | NegRiskModule (impl)        | [`0xA61e7ca374F721D5b9FD5b0FEe6Fb90f27d448d7`](https://polygonscan.com/address/0xA61e7ca374F721D5b9FD5b0FEe6Fb90f27d448d7) | | CombinatorialModule (proxy) | [`0x30000034706C7d8e12009DAB006Be20000c031A8`](https://polygonscan.com/address/0x30000034706C7d8e12009DAB006Be20000c031A8) | | CombinatorialModule (impl)  | [`0xb529b2430d78868422C47934d9d61cC9D0C53dBb`](https://polygonscan.com/address/0xb529b2430d78868422C47934d9d61cC9D0C53dBb) | | Exchange (proxy)            | [`0xe3333700cA9d93003F00f0F71f8515005F6c00Aa`](https://polygonscan.com/address/0xe3333700cA9d93003F00f0F71f8515005F6c00Aa) | | Exchange (impl)             | [`0x7345C6842b244926125ed4054905cAc49620B5dc`](https://polygonscan.com/address/0x7345C6842b244926125ed4054905cAc49620B5dc) | | AutoRedeemer (proxy)        | [`0xa1200000d0002264C9a1698e001292D00E1b00af`](https://polygonscan.com/address/0xa1200000d0002264C9a1698e001292D00E1b00af) | | AutoRedeemer (impl)         | [`0x64860bFD14fCcaAc09cd36f347784a9616AfB66C`](https://polygonscan.com/address/0x64860bFD14fCcaAc09cd36f347784a9616AfB66C) |

| Contract                       | Address                                                                                                                    | | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | | pUSD — CollateralToken (proxy) | [`0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB`](https://polygonscan.com/address/0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB) | | pUSD — CollateralToken (impl)  | [`0x6bBCef9f7ef3B6C592c99e0f206a0DE94Ad0925f`](https://polygonscan.com/address/0x6bBCef9f7ef3B6C592c99e0f206a0DE94Ad0925f) | | CollateralOnramp               | [`0x93070a847efEf7F70739046A929D47a521F5B8ee`](https://polygonscan.com/address/0x93070a847efEf7F70739046A929D47a521F5B8ee) | | CollateralOfframp              | [`0x2957922Eb93258b93368531d39fAcCA3B4dC5854`](https://polygonscan.com/address/0x2957922Eb93258b93368531d39fAcCA3B4dC5854) | | PermissionedRamp               | [`0xebC2459Ec962869ca4c0bd1E06368272732BCb08`](https://polygonscan.com/address/0xebC2459Ec962869ca4c0bd1E06368272732BCb08) | | CtfCollateralAdapter           | [`0xAdA100Db00Ca00073811820692005400218FcE1f`](https://polygonscan.com/address/0xAdA100Db00Ca00073811820692005400218FcE1f) | | NegRiskCtfCollateralAdapter    | [`0xadA2005600Dec949baf300f4C6120000bDB6eAab`](https://polygonscan.com/address/0xadA2005600Dec949baf300f4C6120000bDB6eAab) |

| Contract                 | Address                                                                                                                    | | ------------------------ | -------------------------------------------------------------------------------------------------------------------------- | | Deposit Wallet Factory   | [`0x00000000000Fb5C9ADea0298D729A0CB3823Cc07`](https://polygonscan.com/address/0x00000000000Fb5C9ADea0298D729A0CB3823Cc07) | | Deposit Wallet Beacon    | [`0x7A18EDfe055488A3128f01F563e5B479D92ffc3a`](https://polygonscan.com/address/0x7A18EDfe055488A3128f01F563e5B479D92ffc3a) | | Gnosis Safe Factory      | [`0xaacfeea03eb1561c4e67d661e40682bd20e3541b`](https://polygonscan.com/address/0xaacfeea03eb1561c4e67d661e40682bd20e3541b) | | Polymarket Proxy Factory | [`0xaB45c5A4B0c941a2F231C04C3f49182e1A254052`](https://polygonscan.com/address/0xaB45c5A4B0c941a2F231C04C3f49182e1A254052) |

| Contract              | Address                                                                                                                    | | --------------------- | -------------------------------------------------------------------------------------------------------------------------- | | UMA Adapter           | [`0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74`](https://polygonscan.com/address/0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74) | | UMA Optimistic Oracle | [`0xCB1822859cEF82Cd2Eb4E6276C7916e692995130`](https://polygonscan.com/address/0xCB1822859cEF82Cd2Eb4E6276C7916e692995130) |

CTF Exchange V2 has been audited by two independent firms:

| Auditor    | Report                                                                                                                                                                  | | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | Quantstamp | [CTF Exchange V2 — Quantstamp — March 2026](https://github.com/Polymarket/ctf-exchange-v2/blob/main/audits/CTF%20Exchange%20V2%20-%20Quantstamp%20-%20March%202026.pdf) | | Cantina    | [CTF Exchange V2 — Cantina — March 2026](https://github.com/Polymarket/ctf-exchange-v2/blob/main/audits/CTF%20Exchange%20V2%20-%20Cantina%20-%20March%202026.pdf)       |

Security vulnerabilities can be reported through the [Cantina bug bounty program](https://cantina.xyz/bounties/ff945ca2-2a6e-4b83-b1b6-7a0cd3b94bea).

<CardGroup cols={1}> <Card title="CTF Exchange V2" icon="github" href="https://github.com/Polymarket/ctf-exchange-v2"> Order matching and settlement contracts </Card> </CardGroup>

---

## Error Codes

**URL:** https://docs.polymarket.com/resources/error-codes.md

**Contents:**
- Global Errors
- Order Book
  - GET book
  - POST books
- Pricing
  - GET price
  - POST prices
  - GET midpoint
  - POST midpoints
  - GET spread

All CLOB API errors return a JSON object with a single `error` field:

These errors can occur on **any authenticated endpoint**.

<ResponseField name="401" type="Unauthorized"> `Unauthorized/Invalid api key` — Your API key is missing, expired, or invalid. Ensure you're sending all required [authentication headers](/getting-started/api#authentication). </ResponseField>

<ResponseField name="401" type="Unauthorized"> `Invalid L1 Request headers` — Your L1 authentication headers (HMAC signature) are malformed or the signature doesn't match. See [Authentication](/getting-started/api#authentication). </ResponseField>

<ResponseField name="503" type="Service Unavailable"> `Trading is currently disabled. Check polymarket.com for updates` — The exchange is temporarily paused. No orders (including cancels) are accepted. </ResponseField>

<ResponseField name="429" type="Too Many Requests"> `Too Many Requests` — You've exceeded the [rate limit](/api-reference/rate-limits). Back off and retry with exponential backoff. </ResponseField>

Errors from the order book endpoints.

<ResponseField name="400" type="Bad Request"> `Invalid token id` — The `token_id` query parameter is missing or not a valid token ID. </ResponseField>

<ResponseField name="404" type="Not Found"> `No orderbook exists for the requested token id` </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid payload` — The request body is malformed or missing required fields. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Payload exceeds the limit` — Too many token IDs in a single request. Reduce the batch size. </ResponseField>

Errors from price, midpoint, and spread endpoints.

<ResponseField name="400" type="Bad Request"> `Invalid token id` — The `token_id` parameter is missing or invalid. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid side` — The `side` parameter must be `BUY` or `SELL`. </ResponseField>

<ResponseField name="404" type="Not Found"> `No orderbook exists for the requested token id` </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid payload` — The request body is malformed or missing required fields. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid side` — The `side` field must be `BUY` or `SELL`. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Payload exceeds the limit` — Too many token IDs in a single request. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid token id` — The `token_id` parameter is missing or invalid. </ResponseField>

<ResponseField name="404" type="Not Found"> `No orderbook exists for the requested token id` </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid payload` — The request body is malformed or missing required fields. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Payload exceeds the limit` — Too many token IDs in a single request. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid token id` — The `token_id` parameter is missing or invalid. </ResponseField>

<ResponseField name="404" type="Not Found"> `No orderbook exists for the requested token id` </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid payload` — The request body is malformed or missing required fields. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Payload exceeds the limit` — Too many token IDs in a single request. </ResponseField>

Errors from order placement endpoints.

<ResponseField name="400" type="Bad Request"> `Invalid order payload` — The request body is malformed, missing required fields, or contains invalid values. </ResponseField>

<ResponseField name="400" type="Bad Request"> `the order owner has to be the owner of the API KEY` — The `maker` address in the order doesn't match the address associated with your API key. </ResponseField>

<ResponseField name="400" type="Bad Request"> `the order signer address has to be the address of the API KEY` </ResponseField>

<ResponseField name="400" type="Bad Request"> `'{address}' address banned` — This address has been banned from trading. </ResponseField>

<ResponseField name="400" type="Bad Request"> `'{address}' address in closed only mode` </ResponseField>

<ResponseField name="503" type="Service Unavailable"> `Trading is currently cancel-only. New orders are not accepted, but cancels are allowed.` — The exchange is in cancel-only mode. You can cancel existing orders but cannot place new orders. </ResponseField>

<ResponseField name="503" type="Service Unavailable"> `post-only mode: only post-only orders and cancels are allowed` — The exchange is in post-only mode. You can cancel orders and place orders with `postOnly: true`; non-post-only orders are rejected. The response includes `code: "post*only*mode"` and `retry*after*seconds`, and the same retry delay is also sent in the `Retry-After` HTTP header. </ResponseField>

The retry delay is also sent in the `Retry-After` HTTP header.

All errors from `POST /order` apply, plus:

<ResponseField name="400" type="Bad Request"> `Too many orders in payload: {N}, max allowed: {M}` — The batch contains more orders than the maximum allowed per request. </ResponseField>

Per-order errors are returned in the `200` response array, with individual error messages for each failed order.

In post-only mode, non-post-only orders in a batch return per-order errors:

These errors are returned when an order passes initial validation but fails during processing. They appear in the response body of `POST /order` and `POST /orders`.

<ResponseField name="400" type="Bad Request"> `invalid post-only order: order crosses book` — A post-only (maker) order would immediately match. Adjust the price so it rests on the book. </ResponseField>

<ResponseField name="400" type="Bad Request"> `order {id} is invalid. Price ({price}) breaks minimum tick size rule: {tick}` — The order price doesn't align with the market's tick size. Use [`GET /tick-size`](/api-reference/market-data/get-tick-size) to check the valid tick size. </ResponseField>

<ResponseField name="400" type="Bad Request"> `order {id} is invalid. Size ({size}) lower than the minimum: {min}` — The order size is below the market minimum. </ResponseField>

<ResponseField name="400" type="Bad Request"> `order {id} is invalid. Duplicated.` </ResponseField>

<ResponseField name="400" type="Bad Request"> `order {id} crosses the book` </ResponseField>

<ResponseField name="400" type="Bad Request"> `not enough balance / allowance` — Insufficient pUSD balance or token allowance. Make sure the account holds enough pUSD and grant the exchange allowances with [Set Up Trading Approvals](/trading/wallets-auth#set-up-trading-approvals). </ResponseField>

<ResponseField name="400" type="Bad Request"> `invalid expiration` — The order expiration timestamp is in the past or invalid. </ResponseField>

<ResponseField name="400" type="Bad Request"> `order canceled in the CTF exchange contract` </ResponseField>

<ResponseField name="400" type="Bad Request"> `order match delayed due to market conditions` </ResponseField>

<ResponseField name="400" type="Bad Request"> `order couldn't be fully filled. FOK orders are fully filled or killed.` — A Fill-or-Kill order could not be completely filled by available liquidity. The entire order is rejected. </ResponseField>

<ResponseField name="400" type="Bad Request"> `no orders found to match with FAK order. FAK orders are partially filled or killed if no match is found.` — A Fill-and-Kill order found no matching orders at all. At least one match is required. </ResponseField>

<ResponseField name="400" type="Bad Request"> `the market is not yet ready to process new orders` </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `order timed out` — The exchange could not process the order before the request deadline. This typically happens during bursts of concurrent order submissions from the same account. The order was rejected before reaching the order book and can be safely resubmitted. </ResponseField>

Internal matching engine errors that may surface during order execution.

<ResponseField name="425" type="Too Early"> The matching engine is restarting. Retry with exponential backoff. See [Matching Engine Restarts](/trading/matching-engine) for restart handling. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `there are no matching orders` </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `FOK orders are filled or killed` — A Fill-or-Kill order could not be fully satisfied. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `the trade contains rounding issues` </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `the price of the taker's order has a discrepancy greater than allowed with the worst maker order` </ResponseField>

Errors from order cancellation endpoints.

<ResponseField name="400" type="Bad Request"> `Invalid order payload` — The request body is malformed. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid orderID` — The provided order ID is not a valid format. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid order payload` — The request body is malformed. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Too many orders in payload, max allowed: {N}` — Too many order IDs in a single cancellation request. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid orderID` — One or more order IDs are not valid. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid order payload` — The request body is malformed or contains invalid filter parameters. </ResponseField>

Errors from order query endpoints.

<ResponseField name="400" type="Bad Request"> `Invalid orderID` — The order ID in the URL path is not valid. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `Internal server error` — An unexpected error occurred while fetching the order. </ResponseField>

<ResponseField name="400" type="Bad Request"> `invalid order params payload` — The query parameters are malformed or contain invalid values. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `Internal server error` — An unexpected error occurred while fetching orders. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid trade params payload` — The query parameters are malformed or contain invalid values. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `Internal server error` — An unexpected error occurred while fetching trades. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid token id` — The `token_id` parameter is missing or invalid. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `Internal server error` — An unexpected error occurred while fetching the last trade price. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid payload` — The request body is malformed or missing required fields. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Payload exceeds the limit` — Too many token IDs in a single request. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid market` — The condition ID is not a valid format. </ResponseField>

<ResponseField name="404" type="Not Found"> `market not found` — No market exists with this condition ID. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid token id` — The token ID is not valid. </ResponseField>

<ResponseField name="404" type="Not Found"> `market not found` — No market found for this token ID. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid token id` — The token ID is not valid. </ResponseField>

<ResponseField name="404" type="Not Found"> `market not found` — No market found for this token ID. </ResponseField>

<ResponseField name="400" type="Bad Request"> Filter validation errors — One or more query parameters (`market`, `startTs`, `endTs`, `fidelity`) are invalid. </ResponseField>

<ResponseField name="400" type="Bad Request"> `startTs is required` — The `startTs` query parameter is missing. </ResponseField>

<ResponseField name="400" type="Bad Request"> `asset*id is required` — The `asset*id` query parameter is missing. </ResponseField>

<ResponseField name="400" type="Bad Request"> `invalid fidelity: {val}` — The `fidelity` parameter must be one of: `1m`, `5m`, `15m`, `30m`, `1h`, `4h`, `1d`, `1w`. </ResponseField>

<ResponseField name="400" type="Bad Request"> `limit cannot exceed 1000` — Reduce the `limit` parameter to 1000 or below. </ResponseField>

<ResponseField name="400" type="Bad Request"> `startTs is required` — The `startTs` query parameter is missing. </ResponseField>

<ResponseField name="400" type="Bad Request"> `either market or asset*id must be provided` — You must specify either a `market` (condition ID) or `asset*id` (token ID). </ResponseField>

<ResponseField name="400" type="Bad Request"> `limit cannot exceed 1000` — Reduce the `limit` parameter to 1000 or below. </ResponseField>

<ResponseField name="401" type="Unauthorized"> `Invalid L1 Request headers` — L1 authentication headers are missing or invalid. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Could not create api key` </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `Could not retrieve API keys` — An unexpected error occurred while fetching your API keys. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `Could not delete API key` — An unexpected error occurred while deleting the API key. </ResponseField>

<ResponseField name="401" type="Unauthorized"> `Invalid L1 Request headers` — L1 authentication headers are missing or invalid. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Could not derive api key!` </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `could not create builder api key` — Builder API key creation failed. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `could not get builder api keys` — An unexpected error occurred while fetching builder API keys. </ResponseField>

<ResponseField name="400" type="Bad Request"> `invalid revoke builder api key body` — The request body is malformed. </ResponseField>

<ResponseField name="400" type="Bad Request"> `invalid revoke builder api key headers` — Required authentication headers are missing. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `could not revoke the builder api key: {key}` — An unexpected error occurred while revoking the key. </ResponseField>

<ResponseField name="400" type="Bad Request"> `invalid builder trade params` — The query parameters are malformed or contain invalid values. </ResponseField>

<ResponseField name="500" type="Internal Server Error"> `could not fetch builder trades` — An unexpected error occurred while fetching builder trades. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid asset type` — The `asset_type` parameter is not a recognized asset type. </ResponseField>

<ResponseField name="400" type="Bad Request"> `Invalid signature*type` — The `signature*type` parameter must be `EOA`, `POLY*PROXY`, or `GNOSIS*SAFE`. </ResponseField>

| Status | Meaning               | Common Causes                                                                                                | | ------ | --------------------- | ------------------------------------------------------------------------------------------------------------ | | `400`  | Bad Request           | Invalid parameters, malformed payload, business logic violation                                              | | `401`  | Unauthorized          | Missing or invalid API key, bad HMAC signature, expired timestamp                                            | | `404`  | Not Found             | Market doesn't exist, order not found, token ID not recognized                                               | | `425`  | Too Early             | Matching engine is restarting — retry with backoff. See [Matching Engine Restarts](/trading/matching-engine) | | `429`  | Too Many Requests     | Rate limit exceeded — implement exponential backoff                                                          | | `500`  | Internal Server Error | Unexpected server error — retry with backoff                                                                 | | `503`  | Service Unavailable   | Exchange paused, or order placement blocked by cancel-only / post-only mode                                  |

<Note> The CLOB API has an internal override: any error message containing `"not found"` returns `404`, `"unauthorized"` returns `401`, and `"context canceled"` returns `400`, regardless of the original status code. </Note>

**Examples:**

Example 1 (text):
```text
{
  "error": "<message>"
}
```

Example 2 (text):
```text
{
  "error": "post-only mode: only post-only orders and cancels are allowed",
  "code": "post_only_mode",
  "retry_after_seconds": 79
}
```

Example 3 (text):
```text
[
  {
    "errorMsg": "post-only mode: only post-only orders and cancels are allowed",
    "orderID": "",
    "takingAmount": "",
    "makingAmount": "",
    "status": "",
    "success": true
  },
  {
    "errorMsg": "post-only mode: only post-only orders and cancels are allowed",
    "orderID": "",
    "takingAmount": "",
    "makingAmount": "",
    "status": "",
    "success": true
  }
]
```

---

## Polymarket 101

**URL:** https://docs.polymarket.com/polymarket-101.md

**Contents:**
- Self-Custody
- How Polymarket Works
  - Prices Are Probabilities
  - Collateral and Tokens
  - Trading
  - Resolution
- Why Blockchain
- Smart Wallets
  - Deployments
- Getting Started

Polymarket is a prediction market platform where users trade on the outcomes of real-world events. Instead of betting against a house, you trade shares with other users in an open, peer-to-peer market. Prices reflect the market's collective belief in the probability of an event occurring.

The platform is non-custodial, meaning you always control your funds. All trades are settled through smart contracts on the blockchain, ensuring transparent and trustless operation.

Polymarket operates on a non-custodial model. You maintain full control of your funds at all times.

<Warning> Keep your private key safe and never share it with anyone. If you lose your private key, you lose access to your funds. If you signed up via Magic Link or have a proxy wallet, recovery may be possible through [recovery.polymarket.com](https://recovery.polymarket.com). </Warning>

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/polymarket-101.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=059e9831d1c51b99996d9747c0139d49" alt="Polymarket Overview" className="dark:hidden" width="1526" height="952" data-path="images/core-concepts/polymarket-101.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/polymarket-101.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=4e929eca98a2bb83ef7421f7bbaf9f1d" alt="Polymarket Overview" className="hidden dark:block" width="1526" height="952" data-path="images/dark/core-concepts/polymarket-101.png" /> </Frame>

Every share on Polymarket is priced between `$0.00` and `$1.00`. The price represents the market's belief in the probability of that outcome occurring.

For example, if "Yes" shares for an event are trading at `$0.65`, the market believes there's approximately a `65%` chance the event will happen.

Polymarket uses pUSD (Polymarket USD) as collateral. Every Yes/No pair is fully backed:

Shares are represented as tokens using the [Gnosis Conditional Token Framework](https://github.com/gnosis/conditional-tokens-contracts/) (ERC1155 standard), enabling seamless onchain trading and settlement.

Polymarket uses a peer-to-peer order book (CLOB) for trading. You trade directly with other users, not against the house.

| Action  | When to Use                           | Profit Scenario           | | ------- | ------------------------------------- | ------------------------- | | Buy Yes | You think the probability is too low  | Event occurs              | | Buy No  | You think the probability is too high | Event does not occur      | | Sell    | Lock in gains or limit losses         | Price moves in your favor |

When an event concludes, markets are resolved through the **UMA Optimistic Oracle**:

This community-driven process ensures fair and accurate market resolution.

Polymarket is built on **Polygon**, a blockchain network, for several key reasons:

Polymarket uses smart wallets so users can trade without manually submitting every onchain transaction. New API users use deposit wallets. Existing Safe and Proxy users can continue using their current wallet.

Deposit wallets hold the user's pUSD and outcome tokens on Polygon and validate orders through ERC-1271. Safe and Proxy wallets remain supported for existing users and integrations.

Using smart wallets allows Polymarket to provide an improved UX where multi-step transactions can be executed atomically and transactions can be relayed by Polymarket's relayer. If you are a developer looking to programmatically access positions accumulated through an existing Polymarket account, continue using that account's current smart wallet type.

Each smart-wallet user has their own wallet address. See [Contracts](/resources/contracts) for all deployed factory and trading contract addresses on Polygon.

Ready to start trading?

<CardGroup cols={2}> <Card title="Trading Quickstart" icon="rocket" href="/trading/quickstart"> Set up your account and make your first trade. </Card>

<Card title="Explore Markets" icon="chart-line" href="https://polymarket.com"> Browse active prediction markets on Polymarket. </Card> </CardGroup>

---

## TypeScript SDK

**URL:** https://docs.polymarket.com/getting-started/typescript.md

**Contents:**
- Quickstart
- Pagination
- Types
- Error Handling
- Wallet Integrations
- Realtime Subscriptions
- Next Steps

The `@polymarket/client` NPM package is the official TypeScript SDK for building Polymarket integrations. With this SDK client you can fetch market data, subscribe to real-time data, submit orders, redeem positions and many other actions.

<CardGroup cols={2}> <Card title="GitHub" icon="github" href="https://github.com/Polymarket/ts-sdk"> View the TypeScript SDK source. </Card>

<Card title="NPM Package" icon="npm" href="https://www.npmjs.com/package/@polymarket/client"> Install `@polymarket/client@latest`. </Card> </CardGroup>

See the [SDK Changelog](/changelog/sdks#typescript) for recent TypeScript releases.

<Steps> <Step title="Install the SDK"> Install the SDK with your preferred package manager.

<Step title="Create a Public Client"> Create a `PublicClient` to access publicly available Polymarket data.

<Step title="Fetch Active Markets"> Fetch a page of active markets to discover trading opportunities.

SDK list methods use a consistent paginator interface. Iterate with `for await` to retrieve every page, or fetch one page at a time when you need to control pacing.

`page.nextCursor` is an opaque SDK cursor. Store it as-is if you want to resume a scan later, and omit it when starting from the first page.

SDK methods return typed responses, and their public types are exported from `@polymarket/client`.

The SDK also uses branded types for identifiers, decimal values, timestamps, and EVM addresses so TypeScript can distinguish values that would otherwise all be strings.

Each SDK action exposes a matching error guard. Use it to handle documented errors for that action and rethrow anything unexpected.

Create a `SecureClient` when your integration needs to trade or access account data. Pass the signer adapter for your wallet library to `createSecureClient()`.

<Tabs> <Tab title="Viem"> Install the Viem adapter alongside the SDK.

<Tab title="Privy"> Install the Privy adapter and server SDK alongside the Polymarket SDK.

<Tab title="Ethers v5"> Install the Ethers v5 adapter and its aliased dependency alongside the SDK.

Continue to [Wallets and Authentication](/trading/wallets-auth) to configure the account wallet and gasless transactions.

The SDK can combine updates from multiple realtime feeds into a single stream of events.

Call `subscribe()` with one or more subscription specs. Public streams are available on both `PublicClient` and `SecureClient`. A `SecureClient` also provides private streams for the connected account.

const tokenId = "<token_id>";

const stream = await client.subscribe([ { topic: "market", tokenIds: [tokenId] }, { topic: "sports" }, ]);

for await (const event of stream) { // event: //   | MarketBookEvent //   | MarketPriceChangeEvent //   | MarketLastTradePriceEvent //   | MarketTickSizeChangeEvent //   | SportsEvent

Narrow `event.topic` before handling a specific event shape. The examples show a few streams; see [Real-Time Data](/market-data/realtime-data), [Real-Time Order Updates](/trading/realtime-order-updates), and [Perps Realtime Updates](/perps/realtime-updates) for feed-specific options.

<CardGroup cols={2}> <Card title="Read Market Data" icon="chart-line" href="/market-data/overview"> Discover markets and work with prices, order books, and historical data. </Card>

<Card title="Subscribe to Real-Time Updates" icon="radio" href="/market-data/realtime-data"> Stream market and account updates as they happen. </Card>

<Card title="Place Your First Order" icon="rocket" href="/trading/quickstart"> Set up an account and complete your first authenticated trade. </Card>

<Card title="Use Session Keys" icon="key" href="/trading/session-keys"> Grant scoped, time-limited Deposit Wallet access to a separate signer. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
<CodeGroup>
  ```bash npm theme={null}
  npm install @polymarket/client@latest
  ```

  ```bash bun theme={null}
  bun add @polymarket/client@latest
  ```

  ```bash pnpm theme={null}
  pnpm add @polymarket/client@latest
  ```

  ```bash yarn theme={null}
  yarn add @polymarket/client@latest
  ```
</CodeGroup>
```

Example 2 (text):
```text
    import { createPublicClient } from "@polymarket/client";

    const client = createPublicClient();
```

Example 3 (text):
```text
    const pages = client.listMarkets({
      closed: false,
      pageSize: 5,
    });

    const firstPage = await pages.firstPage();

    for (const market of firstPage.items) {
      // market: Market
    }
```

Example 4 (text):
```text
const pages = client.listMarkets({
  closed: false,
  pageSize: 10,
});

for await (const page of pages) {
  for (const market of page.items) {
    // market: Market
  }
}
```

---

## Python SDK

**URL:** https://docs.polymarket.com/getting-started/python.md

**Contents:**
- Quickstart
- Async and Sync Interfaces
- Pagination
- Types
- Error Handling
- Secure Client
- Realtime Subscriptions
- DataFrames and Jupyter
- Next Steps

The `polymarket-client` package is the official Python SDK for building Polymarket integrations.

<CardGroup cols={2}> <Card title="GitHub" icon="github" href="https://github.com/Polymarket/py-sdk/"> View the Python SDK source. </Card>

<Card title="PyPI Package" icon="python" href="https://pypi.org/project/polymarket-client/"> Install `polymarket-client` from PyPI. </Card> </CardGroup>

See the [SDK Changelog](/changelog/sdks#python) for recent Python releases.

<Steps> <Step title="Install the SDK"> Install the SDK with your preferred package manager.

<Step title="Create a Public Client"> Create an `AsyncPublicClient` to access publicly available Polymarket data.

<Step title="Fetch Active Markets"> Fetch a page of active markets to discover trading opportunities.

Public clients access public data. [Secure clients](#secure-client) add trading and account access. Both client types are available in async and sync forms.

| Interface | Public data         | Trading and account data | | --------- | ------------------- | ------------------------ | | Async     | `AsyncPublicClient` | `AsyncSecureClient`      | | Sync      | `PublicClient`      | `SecureClient`           |

Async clients fit services, bots, and applications that already run an event loop. Sync clients are convenient for scripts and notebooks.

from polymarket import AsyncPublicClient

async with AsyncPublicClient() as client: pages = client.list*markets(closed=False) first*page = await pages.first_page()

<Note> Some features, including realtime subscriptions, are async-only because they rely on long-lived streams. </Note>

SDK list methods use a consistent paginator interface. Iterate over the paginator to retrieve every page, or fetch one page at a time when you need to control pacing.

pages = client.list*markets(closed=False, page*size=10)

async for page in pages: for market in page.items:

When page boundaries do not matter, iterate over every item directly.

async for market in pages.iter_items():

`page.next_cursor` is an opaque SDK cursor. Store it as-is if you want to resume a scan later, and omit it when starting from the first page.

pages = client.list*markets(closed=False, page*size=10) page = await pages.first_page()

if page.next*cursor: second*page = await pages.from*cursor(page.next*cursor).first_page()

SDK methods return typed models, and their public types are exported from `polymarket`.

The SDK also uses distinct types for domain identifiers and EVM addresses. Precision-sensitive values use `decimal.Decimal`, while dates and timestamps use Python's `datetime` types.

All SDK exceptions inherit from `PolymarketError`. Catch specific exceptions when your application can respond to them, then catch the base exception as a fallback.

Create an `AsyncSecureClient` or `SecureClient` when your integration needs to trade or access account data. The Python SDK creates the signer from a local private key.

from polymarket import AsyncSecureClient

async with await AsyncSecureClient.create( private*key=os.environ["POLYMARKET*PRIVATE_KEY"], ) as client: ...

Continue to [Wallets and Authentication](/trading/wallets-auth) to configure the account wallet and gasless transactions.

The Python SDK can combine updates from multiple realtime feeds into a single stream of events.

<Note> Realtime subscriptions are available only through `AsyncPublicClient` and `AsyncSecureClient`. `PublicClient` and `SecureClient` do not implement `subscribe()`. </Note>

Call `subscribe()` with one or more subscription specs. Both `AsyncPublicClient` and `AsyncSecureClient` support public streams, while `AsyncSecureClient` also provides private streams for the connected account.

from polymarket.streams import MarketSpec, SportsSpec

token*id = "<token*id>"

async with await client.subscribe( [MarketSpec(token*ids=[token*id]), SportsSpec()], ) as stream: async for event in stream:

Narrow `event.topic` before handling a specific event shape. The examples show a few streams; see [Real-Time Data](/market-data/realtime-data), [Real-Time Order Updates](/trading/realtime-order-updates), and [Perps Realtime Updates](/perps/realtime-updates) for feed-specific options.

Convert pages and paginators directly to a [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html), [Polars DataFrame](https://docs.pola.rs/py-polars/html/reference/dataframe/), or [Apache Arrow Table](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html). Install the `pandas`, `polars`, or `arrow` package extra for the format you use; the `quant` extra installs all three.

pages = client.list*markets(closed=False) df = await pages.to*pandas(limit=100)

Paginator conversions require an explicit limit. Pass `limit=None` to retrieve every item.

Common SDK objects also render as compact cards in [Jupyter](https://docs.jupyter.org/en/stable/) notebooks. Return an object as the last expression in a cell to display it.

<CardGroup cols={2}> <Card title="Read Market Data" icon="chart-line" href="/market-data/overview"> Discover markets and work with prices, order books, and historical data. </Card>

<Card title="Subscribe to Real-Time Updates" icon="radio" href="/market-data/realtime-data"> Stream market and account updates as they happen. </Card>

<Card title="Place Your First Order" icon="rocket" href="/trading/quickstart"> Set up an account and complete your first authenticated trade. </Card>

<Card title="Use Session Keys" icon="key" href="/trading/session-keys"> Grant scoped, time-limited Deposit Wallet access to a separate signer. </Card> </CardGroup>

**Examples:**

Example 1 (text):
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
```

Example 2 (text):
```text
    from polymarket import AsyncPublicClient


    async with AsyncPublicClient() as client:
        ...
```

Example 3 (text):
```text
    import asyncio

    from polymarket import AsyncPublicClient


    async def main() -> None:
        async with AsyncPublicClient() as client:
            pages = client.list_markets(closed=False)
            first_page = await pages.first_page()

            for market in first_page.items:
                # market: Market
                ...


    asyncio.run(main())
```

Example 4 (text):
```text
  from polymarket import PublicClient


  with PublicClient() as client:
      pages = client.list_markets(closed=False)
      first_page = pages.first_page()
```

---

## Taker Rebate Program

**URL:** https://docs.polymarket.com/programs/taker-rebates.md

**Contents:**
- How Tiers Work
  - Example 1: A Normal Taker Trade
  - Example 2: Why Price Matters
- Category Weights
- Tiers and Rebates
  - Example: Your Rebate Starts When You Reach the Tier
- Rebates
- Level-Up Bonuses
- Your Tier on Your Profile
- Notes

<Note> The Taker Rebate Program goes live on **Thursday, May 28, 2026**. </Note>

Polymarket Tiers reward you for trading as a **taker**. The more taker volume you do, the higher your tier, the bigger the rebate you earn back on every trade you make from that point on. Every **taker** trade earns **Weighted Volume (wV)**. Your tier is based on your Weighted Volume over the last 30 days, and rebates are paid every day in pUSD.

There are seven tiers, from **Bronze** to **Obsidian**. Your tier shows on your profile, and the first time you reach a new tier you get a one-time bonus.

Your tier is set by how much **Weighted Volume (wV)** you earn over the last 30 days. You earn Weighted Volume on your taker trades. Three things decide how much you earn:

You buy 1,000 shares of a Politics market at 40¢, and the order fills right away (a taker trade).

Two trades, both \$50 in size, both in Crypto (weight 2.3):

Both trades count, and your Weighted Volume from every trade adds up over 30 days to set your tier.

| Category                           | Weight                         | | ---------------------------------- | ------------------------------ | | Sports                             | 1.0                            | | Politics, Finance, Mentions, Tech  | 1.3                            | | Economics, Culture, Weather, Other | 1.7                            | | Crypto                             | 2.3                            | | Geopolitics                        | 0 (free to trade, earns no wV) |

<Note> Category weights are set by Polymarket and may change over time. </Note>

Once your 30-day Weighted Volume passes a tier's threshold, you unlock that tier's rebate. The higher your tier, the bigger your rebate. Your rebate applies to your trades from the moment you reach the tier, going forward.

| Tier | Name     | 30-day wV Needed    | Rebate | Level-Up Bonus | | :--: | -------- | ------------------- | :----: | :------------: | |   0  | None     | Under \$2,000       |   0%   |      None      | |   1  | Bronze   | \$2,000             |   3%   |      \$10      | |   2  | Silver   | \$20,000            |   8%   |      \$50      | |   3  | Gold     | \$200,000           |   18%  |      \$250     | |   4  | Platinum | \$1,000,000         |   32%  |     \$1,500    | |   5  | Diamond  | \$4,000,000         |   44%  |     \$7,500    | |   6  | Obsidian | \$10,000,000 and up |   50%  |    \$25,000    |

The day you reach **Gold**, the 18% Gold rebate turns on for every trade you make from then on.

If you keep climbing and hit **Diamond**, your rebate moves up to 44%, and again it applies only to your trades going forward.

Your tier updates every day based on your last 30 days of Weighted Volume. Moving up takes effect at the next daily update.

The first time you reach a new tier, you get a one-time bonus in pUSD:

| Tier     | Bonus    | | -------- | -------- | | Bronze   | \$10     | | Silver   | \$50     | | Gold     | \$250    | | Platinum | \$1,500  | | Diamond  | \$7,500  | | Obsidian | \$25,000 |

For example, the first time you climb from Silver to Gold, you get \$250 added to your account, on top of your normal rebates.

Your tier shows on your Polymarket profile and on the leaderboards. As you climb from Bronze to Obsidian, your badge updates to match your current tier.

<AccordionGroup> <Accordion title="Do maker trades count toward my tier"> No. Only taker trades earn Weighted Volume and count toward your tier. Maker fills are rewarded separately through the [Maker Rebates Program](/programs/maker-rebates). </Accordion>

<Accordion title="When does my rebate start applying"> Your rebate applies to trades from the moment you reach a tier, going forward. There is no backfill on earlier trades. </Accordion>

<Accordion title="When are rebates paid"> Rebates are paid once a day at midnight UTC in pUSD, directly to your account. You must accrue at least **\$1** in rebates before a payout is issued. </Accordion>

<Accordion title="How often does my tier update"> Your tier is recalculated daily based on your last 30 days of Weighted Volume. Tier changes take effect at the next daily update. </Accordion>

<Accordion title="What happens if I slow down trading"> Your tier moves down after a short grace period if your 30-day Weighted Volume drops below your current tier's threshold. </Accordion>

<Accordion title="Which markets earn Weighted Volume"> All fee-enabled categories earn Weighted Volume at the weight shown in the table above. Geopolitical and world events markets are free to trade and earn no Weighted Volume. </Accordion>

<Accordion title="Are third-party integrations using omnibus wallets eligible"> No. Third-party integrations using omnibus wallets are not eligible for the Taker Rebate Program. </Accordion> </AccordionGroup>

**Examples:**

Example 1 (text):
```text
wV = Trade Size × (1 − Entry Price) × Category Weight × Bonuses
```

---

## Tiers

**URL:** https://docs.polymarket.com/programs/builders/tiers.md

**Contents:**
- Feature Definitions
- Tier Comparison
- Unverified
- Verified
- Partner
- How to Upgrade
- Contact
- FAQ

The Builder Program uses a tiered system to manage rate limits while rewarding high-performing integrations. Higher tiers unlock increased limits, weekly rewards, and priority support.

| Feature                     | Description                                                                                | | --------------------------- | ------------------------------------------------------------------------------------------ | | **Daily Relayer Txn Limit** | Maximum Relayer transactions per day for deposit wallet, Safe, and Proxy wallet operations | | **API Rate Limits**         | Rate limits for non-relayer endpoints (CLOB, Gamma, etc.)                                  | | **Gasless Trading**         | Gas fees subsidized for supported smart-wallet operations                                  | | **Order Attribution**       | Orders tracked and attributed to your Builder profile                                      | | **Builder Fees**            | Builders who route orders can charge fees and monetize on flow                             | | **Leaderboard Visibility**  | Visibility on the [Builder Leaderboard](https://builders.polymarket.com/)                  | | **Telegram Channel**        | Private Builders channel for announcements and support                                     | | **Engineering Support**     | Direct access to engineering team                                                          | | **Marketing Support**       | Promotion via official Polymarket social accounts                                          | | **Priority Access**         | Early access to new features and products                                                  |

| Feature                     | Unverified |  Verified  |  Partner  | | --------------------------- | :--------: | :--------: | :-------: | | **Daily Relayer Txn Limit** |   100/day  | 10,000/day | Unlimited | | **API Rate Limits**         |  Standard  |  Standard  |  Highest  | | **Gasless Trading\***       |     Yes    |     Yes    |    Yes    | | **Order Attribution**       |     Yes    |     Yes    |    Yes    | | **Builder Fees**            |     Yes    |     Yes    |    Yes    | | **Leaderboard Visibility**  |      —     |     Yes    |    Yes    | | **Telegram Channel**        |      —     |     Yes    |    Yes    | | **Engineering Support**     |      —     |  Standard  |  Elevated | | **Marketing Support**       |      —     |  Standard  |  Elevated | | **Priority Access**         |      —     |      —     |    Yes    |

<Card title="100 Relay transactions/day" icon="seedling"> The default tier for all new builders. Start immediately with no approval required. </Card>

**How to get started:**

**What's included:**

<Card title="10,000 Relay transactions/day" icon="badge-check"> For builders who need higher throughput. Requires manual approval. </Card>

Contact us at [builder@polymarket.com](mailto:builder@polymarket.com) with:

**Unlocks over Unverified:**

<Card title="Unlimited Relay transactions/day" icon="handshake"> Enterprise tier for high-volume integrations and strategic partners. </Card>

**Unlocks over Verified:**

<Steps> <Step title="Build and Launch"> Start with the Unverified tier and build your integration. </Step>

<Step title="Generate Volume"> Route orders through Polymarket and demonstrate consistent usage. </Step>

<Step title="Apply for Verification"> Email [builder@polymarket.com](mailto:builder@polymarket.com) with your builder key and use case. </Step>

<Step title="Get Approved"> The Polymarket team reviews applications and responds within a few business days. </Step> </Steps>

Ready to upgrade or have questions?

<Card title="builder@polymarket.com" icon="envelope" href="mailto:builder@polymarket.com"> Email us with your Builder API Key and use case details. </Card>

<AccordionGroup> <Accordion title="How do I know if I am verified"> Verification is displayed in your [Builder Profile](https://polymarket.com/settings?tab=builder) settings. </Accordion>

<Accordion title="What happens if I exceed my daily limit"> Relayer requests beyond your daily limit will be rate-limited and return an error. Consider upgrading to Verified or Partner tier if you're hitting limits. </Accordion>

<Accordion title="What if I just need more daily Relay transaction limits for my own wallet"> If you're not routing orders for other users (wallets), you can get unlimited daily Relay transactions by obtaining a [Relayer API key](https://polymarket.com/settings?tab=api-keys). </Accordion> </AccordionGroup>

---

## Maker Rebates Program

**URL:** https://docs.polymarket.com/programs/maker-rebates.md

**Contents:**
- Why Maker Rebates
- How Maker Rebates Work
  - Eligibility
  - Payment
- Funding
- Fee-Curve Weighted Rebates
- Taker Fee Structure
  - Fee Tables (100 Shares)
  - Fee Precision
- Which Markets Are Eligible

Polymarket charges taker fees across multiple market categories. Fees are determined by the protocol at match time and fund a **Maker Rebates** program that pays daily pUSD rebates to liquidity providers.

Deeper liquidity means tighter spreads, lower price impact, more reliable fills, and greater resilience during volatility. Maker Rebates incentivize **consistent, competitive quoting** so everyone gets a better trading experience.

Place orders that add liquidity to the book and get filled (i.e., your liquidity is taken by another trader).

Rebates are paid daily in pUSD, directly to your wallet. A minimum accrued rebate of **\$1 pUSD** is required for a payout.

Maker Rebates are funded by taker fees collected in eligible markets. A percentage of these fees are redistributed to makers who keep the markets liquid. The rebate percentage differs by market type.

| Category        | Maker Rebate | Distribution Method | | --------------- | ------------ | ------------------- | | Crypto          | 20%          | Fee-curve weighted  | | Sports          | 15%          | Fee-curve weighted  | | Finance         | 25%          | Fee-curve weighted  | | Politics        | 25%          | Fee-curve weighted  | | Economics       | 25%          | Fee-curve weighted  | | Culture         | 25%          | Fee-curve weighted  | | Weather         | 25%          | Fee-curve weighted  | | Other / General | 25%          | Fee-curve weighted  | | Mentions        | 25%          | Fee-curve weighted  | | Tech            | 25%          | Fee-curve weighted  | | Geopolitics     | —            | Fee-free            |

<Note> Polymarket collects taker fees in eligible markets across all fee-enabled categories. The rebate percentage is at the sole discretion of Polymarket and may change over time. </Note>

Rebates are distributed using the **same formula as taker fees**. This ensures makers are rewarded proportionally to the fee value their liquidity generates.

For each filled maker order:

Where **C** = number of shares traded and **p** = price of the shares. The fee parameters differ by market type:

| Category        | Taker Fee Rate | Maker Fee Rate | | --------------- | -------------- | -------------- | | Crypto          | 0.07           | 0              | | Sports          | 0.05           | 0              | | Finance         | 0.04           | 0              | | Politics        | 0.04           | 0              | | Economics       | 0.05           | 0              | | Culture         | 0.05           | 0              | | Weather         | 0.05           | 0              | | Other / General | 0.05           | 0              | | Mentions        | 0.04           | 0              | | Tech            | 0.04           | 0              | | Geopolitics     | 0              | 0              |

Totals are calculated per market, so you only compete with other makers in the same market.

Taker fees are calculated in pUSD and vary based on the share price. The fee amount in pUSD is symmetric around 50% probability — a trade at 30¢ incurs the same dollar fee as a trade at 70¢.

<Frame> <div className="p-3 bg-white rounded-xl"> <iframe title="Fee Curves" aria-label="Line chart" id="datawrapper-chart-dJ74e" src="https://datawrapper.dwcdn.net/dJ74e/" scrolling="no" frameborder="0" width={700} style={{ width: "0", minWidth: "100% !important", border: "none" }} height="450" data-external="1" /> </div> </Frame>

For detailed fee tables for each market category, see the [Fees](/trading/fees) page.

Fees are rounded to 5 decimal places. The smallest fee charged is 0.00001 pUSD. Anything smaller rounds to zero, so very small trades near the extremes may incur no fee at all.

The following market categories have taker fees enabled and are eligible for maker rebates: Crypto, Sports, Finance, Politics, Economics, Culture, Weather, Tech, Mentions, and Other / General.

To confirm whether fees apply to a specific market, see [Trading Fees](/market-data/market-details#trading-fees) in Market Details.

<AccordionGroup> <Accordion title="How do I qualify for maker rebates"> Place orders that add liquidity to the book and get filled (i.e., your liquidity is taken by another trader). </Accordion>

<Accordion title="When are rebates paid">Daily, in pUSD. You must accrue at least \$1 in rebates before a payout is issued.</Accordion>

<Accordion title="How are rebates calculated"> Rebates are proportional to your share of executed maker liquidity in each eligible market. Totals are calculated per market, so you only compete with other makers in the same market. </Accordion>

<Accordion title="Where does the rebate pool come from"> Taker fees collected in eligible markets are allocated to the maker rebate pool and distributed daily. </Accordion>

<Accordion title="Which markets have fees enabled"> Crypto, Sports, Finance, Politics, Economics, Culture, Weather, Tech, Mentions, and Other / General markets. </Accordion> </AccordionGroup>

**Examples:**

Example 1 (text):
```text
fee_equivalent = C × feeRate × p × (1 - p)
```

Example 2 (text):
```text
rebate = (your_fee_equivalent / total_fee_equivalent) * rebate_pool
```

---

## Positions & Tokens

**URL:** https://docs.polymarket.com/concepts/positions-tokens.md

**Contents:**
- Outcome Tokens
  - Split
  - Trade
  - Merge
  - Redeem
  - Position Value
- Profit and Loss
  - Example - Buying Yes at 0.40
  - Holding Rewards
  - Example - Selling Before Resolution

Every prediction on Polymarket is represented by **outcome tokens**. When you trade, you're buying and selling these tokens. Your **position** is simply your balance of tokens for a given market.

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/token-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=cad279109c43c68c541123c2d348c4c5" alt="" className="dark:hidden" width="1596" height="952" data-path="images/core-concepts/token-lifecycle.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/token-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=204d16c1d89892a3c8573060aa04780e" alt="" className="hidden dark:block" width="1596" height="952" data-path="images/dark/core-concepts/token-lifecycle.png" /> </Frame>

Each market has exactly two outcome tokens:

| Token   | Redeems for | If...                    | | ------- | ----------- | ------------------------ | | **Yes** | \$1.00      | The event occurs         | | **No**  | \$1.00      | The event does not occur |

Tokens are **ERC1155** assets on Polygon, using the [Gnosis Conditional Token Framework](https://github.com/gnosis/conditional-tokens-contracts/) (CTF). This means they're fully onchain and function as standard ERC1155 tokens.

<Note> Outcome tokens are always fully backed. Every Yes/No pair in existence is backed by exactly `$1` of pUSD collateral locked in the CTF contract. </Note>

Convert pUSD into outcome tokens. Splitting \$1 creates 1 Yes token and 1 No token.

Use this when you want to:

Buy or sell tokens on the order book. This is how most users acquire positions.

You can sell your position at any time before resolution.

Convert a complete set of tokens back into pUSD. Merging requires equal amounts of Yes and No tokens.

Use this when you want to:

After a market resolves, exchange winning tokens for pUSD.

| Outcome             | Yes tokens     | No tokens      | | ------------------- | -------------- | -------------- | | Event occurs        | Worth \$1 each | Worth \$0      | | Event doesn't occur | Worth \$0      | Worth \$1 each |

The value of your position depends on the current market price:

If you hold 100 Yes tokens and Yes is trading at \$0.75:

Your profit depends on how the market resolves compared to your entry price.

| Scenario            | Outcome  | Return | Profit                    | | ------------------- | -------- | ------ | ------------------------- | | Event occurs        | Yes wins | \$1.00 | +\$0.60 per token (150%)  | | Event doesn't occur | No wins  | \$0.00 | -\$0.40 per token (-100%) |

Polymarket pays a **4.00% annualized** Holding Reward based on your total position value in eligible markets. Your total position value is randomly sampled once each hour, and the reward is distributed daily. The rate is variable and subject to change at Polymarket's discretion.

You can lock in profits or cut losses by selling before the market resolves:

**Examples:**

Example 1 (text):
```text
$100 pUSD → 100 Yes tokens + 100 No tokens
```

Example 2 (text):
```text
100 Yes tokens + 100 No tokens → $100 pUSD
```

Example 3 (text):
```text
100 winning tokens → $100 pUSD
```

Example 4 (text):
```text
Position value = Token balance × Current price
```

---

## Prices & Orderbook

**URL:** https://docs.polymarket.com/concepts/prices-orderbook.md

**Contents:**
- Prices Are Probabilities
  - Example
- The Order Book
- Order Types
  - Market Orders
  - Limit Orders
- How Trades Work
- Price Discovery
- Next Steps

Polymarket uses a **Central Limit Order Book (CLOB)** for trading. Prices aren't set by Polymarket—they emerge from supply and demand as users trade with each other.

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/orderbook.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=119174bcaaeb3b9abbd4c2d94b7bdae6" alt="" className="dark:hidden" width="1540" height="952" data-path="images/core-concepts/orderbook.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/orderbook.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=b940f4b5f28ab6ed5845dda2bfe03edb" alt="" className="hidden dark:block" width="1540" height="952" data-path="images/dark/core-concepts/orderbook.png" /> </Frame>

Every share on Polymarket is priced between `$0.00` and `$1.00`. The price directly represents the market's belief in the probability of that outcome.

| Price  | Implied Probability | | ------ | ------------------- | | \$0.25 | 25% chance          | | \$0.50 | 50% chance          | | \$0.75 | 75% chance          |

<Note> The displayed price is the **midpoint** of the bid-ask spread. If the spread is wider than \$0.10, the last traded price is shown instead. </Note>

If the best bid for "Yes" is `$0.34` and the best ask is `$0.40`:

You won't necessarily trade at `$0.37`—you'll pay the ask (`$0.40`) when buying or receive the bid (`$0.34`) when selling.

The order book is a list of all open buy and sell orders for a market. It has two sides:

| Side | Description                                                 | | ---- | ----------------------------------------------------------- | | Bids | Buy orders—the highest prices traders are willing to pay    | | Asks | Sell orders—the lowest prices traders are willing to accept |

The **spread** is the gap between the highest bid and lowest ask. Tighter spreads mean more liquid markets.

Execute immediately at the best available price. Use when you want instant execution and are willing to pay the spread.

Execute only at your specified price or better. Use when you want price control and are willing to wait.

<Note> All orders on Polymarket are technically limit orders. A "market order" is simply a limit order priced to execute immediately against resting orders. </Note>

Polymarket's CLOB is **hybrid-decentralized**:

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/trade-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=2acec8befdfbba57fb554170f7d5813c" alt="" className="dark:hidden" width="1540" height="952" data-path="images/core-concepts/trade-lifecycle.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/trade-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=d18b22ad7629820ad554dda8cb83ec18" alt="" className="hidden dark:block" width="1540" height="952" data-path="images/dark/core-concepts/trade-lifecycle.png" /> </Frame>

This design gives you the speed of centralized matching with the security of onchain settlement. You always maintain custody of your funds.

When a new market launches, there's no initial price. The first price emerges when:

When matched, `$1.00` is converted into 1 Yes token and 1 No token, each going to their respective buyers.

<Note> Polymarket's orderbook has **no trading size limits** — it matches willing buyers and sellers of any amount. However, large orders may move the price significantly. Always check orderbook depth before trading in size. </Note>

<CardGroup cols={2}> <Card title="Positions & Tokens" icon="coins" href="/concepts/positions-tokens"> Learn about outcome tokens and how positions work. </Card>

<Card title="Order Lifecycle" icon="arrows-spin" href="/concepts/order-lifecycle"> Understand what happens from order placement to settlement. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
Displayed price = ($0.34 + $0.40) / 2 = $0.37 (37% probability)
```

---

## Overview

**URL:** https://docs.polymarket.com/index.md

export const IconCard = ({icon, title, description, href, color}) => { return <a className="group flex flex-col p-5 border border-gray-200 dark:border-zinc-800 rounded-2xl hover:border-gray-300 dark:hover:border-zinc-700 hover:bg-gray-50 dark:hover:bg-zinc-900/50 transition-all duration-200" href={href}> <div className="flex items-center justify-center w-10 h-10 rounded-lg mb-4" style={{ backgroundColor: color ? `${color}1A` : "#2E5CFF15" }}> <img src={"/images/icons/" + icon + ".svg"} /> </div> <h3 className="text-base font-semibold text-gray-900 dark:text-zinc-50"> {title} </h3> <p className="mt-1.5 text-sm text-gray-500 dark:text-zinc-400"> {description} </p> </a>; };

<a href="https://docs.polymarket.us" target="_blank" className="group flex items-center gap-3 mx-4 md:mx-24 mt-6 px-5 py-3.5 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 hover:border-blue-500 transition-all duration-200 no-underline"> <span className="text-2xl">🇺🇸</span>

<span className="text-sm text-gray-600 dark:text-zinc-400"> Looking for{" "}

<span className="ml-auto text-sm font-medium text-gray-500 dark:text-zinc-400 group-hover:translate-x-0.5 transition-transform duration-200"> Visit US Docs → </span> </a>

<svg className=" absolute stroke-black dark:stroke-white opacity-30 dark:opacity-40 top-0 right-0 md:w-[700px] md:h-[700px] w-[300px] h-[300px] pointer-events-none rotate-[-10deg] translate-x-20 md:translate-x-60 -translate-y-0 " width="1000" height="1205" viewBox="0 0 422 509" fill="none" xmlns="http://www.w3.org/2000/svg"> <path opacity="0.2" d="M399.991 0.832159C406.26 0.015159 410.64 0.654158 414.152 3.32016C417.675 5.99616 419.479 10.0462 420.389 16.3012C421.3 22.5692 421.302 30.9462 421.302 42.1872V465.86C421.302 477.11 421.3 485.492 420.389 491.76C419.479 498.015 417.675 502.06 414.153 504.727C410.631 507.394 406.251 508.037 399.984 507.222C394.49 506.507 387.627 504.683 378.742 502.199L374.809 501.096L27.221 403.558C20.692 401.727 15.839 400.366 12.144 398.847C8.461 397.332 5.977 395.678 4.16 393.287C2.344 390.897 1.42201 388.062 0.960008 384.108C0.496008 380.141 0.500001 375.102 0.500001 368.323V139.725C0.500001 132.946 0.500996 127.907 0.966996 123.939C1.431 119.985 2.353 117.149 4.161 114.759L4.16 114.758C5.977 112.368 8.461 110.715 12.144 109.2C15.839 107.68 20.692 106.32 27.221 104.489L374.809 6.95216C385.638 3.91716 393.71 1.65116 399.991 0.832159ZM374.342 290.988L86.543 371.765L84.828 372.246L86.543 372.728L374.342 453.504L374.978 453.682V290.81L374.342 290.988ZM46.789 173.266L46.807 334.782V335.441L47.441 335.264L335.205 254.505L336.92 254.023L335.205 253.542L47.424 172.784L46.789 172.605V173.266ZM374.342 54.5442L86.543 135.32L84.828 135.802L86.543 136.283L374.342 217.06L374.978 217.237V54.3652L374.342 54.5442Z" /> </svg>

<div className="relative overflow-hidden"> <div className="relative z-10 pb-18 pt-8 max-w-6xl mx-auto "> <h1 className="block text-3xl px-4  md:px-24 font-semibold text-gray-900 dark:text-zinc-50 tracking-tight"> Polymarket Documentation </h1>

<div className="max-w-6xl mx-auto px-4  md:px-24 mt-10"> <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center"> <div> <h2 className="text-xl font-semibold text-gray-900 dark:text-zinc-50"> Developer Quickstart </h2>

<div className="max-w-6xl mx-auto px-4  md:px-24 pb-12"> <div className="grid grid-cols-1 sm:grid-cols-3 gap-4"> <IconCard icon="medal" title="Builder Program" description="Build apps on Polymarket and earn rewards for driving volume" href="https://builders.polymarket.com" />

**Examples:**

Example 1 (text):
```text
<span className="font-semibold text-gray-800 dark:text-zinc-200">
  Polymarket US
</span>

{" "}

documentation?
```

Example 2 (text):
```text
<div className="max-w-2xl px-4  md:px-24 mt-4 text-lg text-gray-500 dark:text-zinc-500">
  Build on the world's largest prediction market. APIs, SDKs, and tools for prediction market developers.
</div>
```

Example 3 (text):
```text
    <p className="mt-3 text-gray-500 dark:text-zinc-400 max-w-2xl">
      Make your first API request in minutes. Learn the basics of the
      Polymarket platform, fetch market data, place orders, and redeem
      winning positions.
    </p>

    <div className="mt-6">
      <a href="/trading/quickstart" className="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-primary rounded-full hover:bg-indigo-700 transition-colors">
        Place Your First Order →
      </a>
    </div>
  </div>

  <div className="lg:pt-1">
    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { createPublicClient } from "@polymarket/client";

      const client = createPublicClient();

      const pages = client.listMarkets({ closed: false });
      const { items: markets } = await pages.firstPage();
      ```

      ```python Python theme={null}
      from polymarket import AsyncPublicClient

      async with AsyncPublicClient() as client:
          markets = client.list_markets(closed=False)

          async for market in markets.iter_items():
              print(market.question)
      ```

      ```bash API theme={null}
      curl -G "https://gamma-api.polymarket.com/markets/keyset" \
        --data-urlencode "closed=false" \
        --data-urlencode "limit=5"
      ```
    </CodeGroup>
  </div>
</div>

<div className="mt-12">
  <h2 className="text-2xl font-semibold text-gray-900 dark:text-zinc-50">
    Get Familiar with Polymarket
  </h2>

  <p className="mt-2 text-gray-500 dark:text-zinc-400 max-w-2xl">
    Learn how Polymarket works, explore the concepts behind markets and
    trading, or choose how to integrate.
  </p>

  <div className="mt-8">
    <CardGroup cols={3}>
      <Card title="Polymarket 101" icon="lightbulb" href="/polymarket-101">
        Learn how prediction markets work and how to use Polymarket.
      </Card>

      <Card title="Core Concepts" icon="book" href="/concepts/markets-events">
        Understand markets and events, prices and order books, positions,
        orders, and resolution.
      </Card>

      <Card title="SDKs & APIs" icon="code" href="/getting-started/sdks-apis">
        Choose the integration approach that best fits your application.
      </Card>
    </CardGroup>
  </div>
</div>

<div className="my-12 ">
  <a href="https://builders.polymarket.com" target="_blank">
    <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/banner.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=d83f2f21e8474e998d8ba0f45810d978" alt="Banner" className="w-full rounded-2xl" width="2394" height="549" data-path="images/banner.png" />
  </a>
</div>
```

Example 4 (text):
```text
  <IconCard icon="quiz" title="Help Desk" description="Get support, report issues, and find answers to common questions" href="https://help.polymarket.com" />

  <IconCard icon="sensor" title="Status" description="Check API uptime, service health, and incident reports" href="https://status.polymarket.com" />
</div>
```

---

## Resolution

**URL:** https://docs.polymarket.com/concepts/resolution.md

**Contents:**
- Resolution Rules
- After Resolution
  - Redeeming Tokens
- Clarifications
- Resolution Timeline
- Contract Addresses
- Resources
- Next Steps

When the outcome of an event becomes known, the market is **resolved**. Resolution determines which outcome won, allowing holders of winning tokens to redeem them for \$1 each. Losing tokens become worthless.

Polymarket uses the **UMA Optimistic Oracle** for decentralized, permissionless resolution. Anyone can propose an outcome, and anyone can dispute it if they believe it's incorrect.

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/resolution-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=6726569af3efd6f4fda54528c8eb0d0a" alt="" className="dark:hidden" width="1722" height="952" data-path="images/core-concepts/resolution-lifecycle.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/resolution-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=36e91c655f7f50b18dea3a23b44f8c23" alt="" className="hidden dark:block" width="1722" height="952" data-path="images/dark/core-concepts/resolution-lifecycle.png" /> </Frame>

Every market has pre-defined resolution rules that specify:

<Warning> Always read the resolution rules before trading. The market title describes the question, but the **rules** define how it resolves. </Warning>

<Steps> <Step title="Proposal"> Anyone can propose a resolution by:

<Step title="Challenge Period"> After a proposal, there's a **2-hour challenge period** where anyone can dispute the outcome.

<Step title="Dispute - If Challenged"> To dispute a proposal:

<Step title="UMA Vote"> After the debate period, UMA token holders vote on the correct outcome. The voting process takes approximately 48 hours.

Once a market resolves:

After resolution, redeem through the CTF collateral adapter to exchange winning tokens for pUSD. The adapter burns your ERC1155 outcome tokens through the CTF contract, receives the released USDC.e collateral, wraps it into pUSD, and returns pUSD to your wallet.

In rare cases, unforeseen circumstances require clarification of the rules after trading begins. Polymarket may issue an **"Additional context"** update that proposers and voters should consider during resolution.

<Tip> If you believe a clarification is needed, request it in the [Polymarket Discord](https://discord.com/invite/polymarket) `#market-review` channel. </Tip>

| Phase                       | Duration    | | --------------------------- | ----------- | | Challenge period            | 2 hours     | | Debate period (if disputed) | 24-48 hours | | UMA voting (if disputed)    | \~48 hours  |

**Undisputed resolution**: \~2 hours after proposal

**Disputed resolution**: 4-6 days total

| Contract               | Address                                      | Network         | | ---------------------- | -------------------------------------------- | --------------- | | **UmaCtfAdapter v3.0** | `0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49` | Polygon Mainnet | | **UmaCtfAdapter v2.0** | `0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74` | Polygon Mainnet | | **UmaCtfAdapter v1.0** | `0xCB1822859cEF82Cd2Eb4E6276C7916e692995130` | Polygon Mainnet |

<CardGroup cols={2}> <Card title="Positions & Tokens" icon="coins" href="/concepts/positions-tokens"> Learn how to redeem winning tokens after resolution. </Card>

<Card title="Markets & Events" icon="calendar" href="/concepts/markets-events"> Understand how markets are structured. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
1. Selecting the winning outcome
2. Posting a bond (typically \$750 pUSD)
3. Submitting the proposal to the UMA Oracle

If the proposal is correct and undisputed, the proposer receives their bond back plus a reward.

<Warning>
  If you propose incorrectly or too early, you lose your entire bond. Only
  propose if you're confident in the outcome and understand the process.
</Warning>
```

Example 2 (text):
```text
* **If no dispute**: The proposal is accepted and the market resolves
* **If disputed**: A new proposal round begins. If the second proposal is also disputed, the resolution escalates to UMA's DVM (Data Verification Mechanism) for a token holder vote.

There are three possible resolution flows:

1. **No dispute** — Propose then Resolve (fastest, \~2 hours)
2. **One dispute** — Propose, Challenge, second Propose, Resolve (second proposal accepted)
3. **Two disputes** — Propose, Challenge, second Propose, second Challenge, Resolve via DVM vote
```

Example 3 (text):
```text
1. Post a counter-bond (same amount as proposer, typically \$750)
2. The dispute triggers a new proposal round, or if already in the second round, a debate period

During the **24-48 hour debate period**, evidence can be submitted in UMA's Discord channels (`#evidence-rationale` and `#voting-discussion`).
```

Example 4 (text):
```text
| Outcome           | Result                                 | Bond Distribution                                                                                        |
| ----------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Proposer wins** | Original proposal accepted             | Proposer gets bond back + half of disputer's bond                                                        |
| **Disputer wins** | Proposal rejected, new proposal needed | Disputer gets bond back + half of proposer's bond                                                        |
| **Too Early**     | Event hasn't concluded yet             | Disputer gets bond back + half of proposer's bond                                                        |
| **Unknown/50-50** | Neither outcome applicable (rare)      | Market resolves 50/50 — each token redeems for \$0.50; disputer gets bond back + half of proposer's bond |
```

---

## Migrate from old SDKs to Unified SDKs

**URL:** https://docs.polymarket.com/migrate/clob-sdk-to-unified-sdk.md

**Contents:**
- Install the Unified SDK

Migrate from the previous CLOB, relayer, and builder-signing clients to the unified SDK.

<Tabs> <Tab title="TypeScript"> The examples below map previous client capabilities to `@polymarket/client`. The SDK also covers the Gamma API and Data API. Migrating direct Gamma and Data calls can simplify application code and give you normalized, typed models that work seamlessly with the SDK's trading and account workflows.

<Tab title="Python"> The examples below map previous client capabilities to `polymarket-client`. The SDK also covers the Gamma API and Data API. Migrating direct Gamma and Data calls can simplify application code and give you normalized, typed models that work seamlessly with the SDK's trading and account workflows.

<Tab title="Rust"> A unified Rust SDK is in progress. Until it is available, use `polymarket*client*sdk_v2` `0.7.0`, the current Rust SDK.

**Examples:**

Example 1 (javascript):
```javascript
Remove the previous CLOB, relayer, and builder-signing packages used by your
integration. Then install the unified SDK and your wallet library.

<CodeGroup>
  ```bash npm theme={null}
  npm uninstall @polymarket/clob-client-v2 @polymarket/builder-relayer-client @polymarket/builder-signing-sdk
  npm install @polymarket/client@latest viem
  ```

  ```bash pnpm theme={null}
  pnpm remove @polymarket/clob-client-v2 @polymarket/builder-relayer-client @polymarket/builder-signing-sdk
  pnpm add @polymarket/client@latest viem
  ```

  ```bash Yarn theme={null}
  yarn remove @polymarket/clob-client-v2 @polymarket/builder-relayer-client @polymarket/builder-signing-sdk
  yarn add @polymarket/client@latest viem
  ```

  ```bash Bun theme={null}
  bun remove @polymarket/clob-client-v2 @polymarket/builder-relayer-client @polymarket/builder-signing-sdk
  bun add @polymarket/client@latest viem
  ```
</CodeGroup>

<Info>
  The unified SDK includes signer adapters for Viem, Privy, and Ethers v5, so
  you can connect your wallet library without implementing CLOB-specific
  signing. See [Wallet
  Integrations](/getting-started/typescript#wallet-integrations) for setup
  examples.
</Info>

## Client and Wallet Setup

### Create a Public Client

`PublicClient` provides unauthenticated market discovery and data reads.
`createPublicClient` uses production by default and does not require a host or
chain ID.

```ts Before theme={null}
import { ClobClient } from "@polymarket/clob-client-v2";

const client = new ClobClient({
  host: "https://clob.polymarket.com",
  chain: 137,
});
```

```ts After theme={null}
import { createPublicClient } from "@polymarket/client";

const client = createPublicClient();
```

### Create an Authenticated Client

`SecureClient` adds authenticated trading, account, and wallet actions.
`createSecureClient` derives or creates CLOB credentials, resolves the account
wallet, and configures the correct signing flow.

```ts Before theme={null}
import { ClobClient, SignatureTypeV2 } from "@polymarket/clob-client-v2";

const tempClient = new ClobClient({
  host: "https://clob.polymarket.com",
  chain: 137,
  signer,
});
const credentials = await tempClient.createOrDeriveApiKey();

const client = new ClobClient({
  host: "https://clob.polymarket.com",
  chain: 137,
  signer,
  creds: credentials,
  signatureType: SignatureTypeV2.POLY_1271,
  funderAddress: process.env.POLYMARKET_WALLET_ADDRESS,
});
```

```ts After theme={null}
import { type ApiKeyCreds, createSecureClient } from "@polymarket/client";
import { privateKey } from "@polymarket/client/viem";

const client = await createSecureClient({
  wallet: process.env.POLYMARKET_WALLET_ADDRESS,
  signer: privateKey(process.env.POLYMARKET_PRIVATE_KEY),
});
```

Omit `wallet` to use the default Deposit Wallet flow.

### Resume With Existing Credentials

Read credentials from an authenticated client, store them securely, and pass
them to a new client to resume with the same API key. The signer and wallet must
identify the account that owns the credentials.

```ts Before theme={null}
import { ClobClient, SignatureTypeV2 } from "@polymarket/clob-client-v2";

const credentials = client.creds;
if (!credentials) throw new Error("Client has no credentials");

// Store the credentials securely.

const resumedClient = new ClobClient({
  host: "https://clob.polymarket.com",
  chain: 137,
  signer,
  creds: credentials,
  signatureType: SignatureTypeV2.POLY_1271,
  funderAddress: process.env.POLYMARKET_WALLET_ADDRESS,
});
```

```ts After theme={null}
import { createSecureClient } from "@polymarket/client";
import { privateKey } from "@polymarket/client/viem";

const credentials = client.credentials;

// Store the credentials securely.

const resumedClient = await createSecureClient({
  wallet: process.env.POLYMARKET_WALLET_ADDRESS,
  signer: privateKey(process.env.POLYMARKET_PRIVATE_KEY),
  // Restore the type if loading from storage erased it.
  credentials: credentials as ApiKeyCreds,
});
```

### Revoke the Current API Key

Ending authentication revokes the current API key, invalidates the
`SecureClient`, and returns a `PublicClient`.

```ts Before theme={null}
await client.deleteApiKey();
```

```ts After theme={null}
const publicClient = await client.endAuthentication();
```

### Configure Builder API Keys

`SecureClient` accepts Builder authorization for gasless wallet actions.
Migrate local or remote Builder signing to the matching helper.

**Local Builder API key**

Keep local Builder credentials on the server. The Node.js entrypoint generates
the required HMAC headers.

```ts Before theme={null}
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
  localBuilderCreds: {
    key: process.env.POLYMARKET_BUILDER_API_KEY!,
    secret: process.env.POLYMARKET_BUILDER_SECRET!,
    passphrase: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
  },
});

const relayer = new RelayClient(
  "https://relayer-v2.polymarket.com",
  137,
  walletClient,
  builderConfig,
);
```

```ts After theme={null}
import { createSecureClient } from "@polymarket/client";
import { builderApiKey } from "@polymarket/client/node";
import { privateKey } from "@polymarket/client/viem";

const client = await createSecureClient({
  signer: privateKey(process.env.POLYMARKET_PRIVATE_KEY),
  apiKey: builderApiKey({
    key: process.env.POLYMARKET_BUILDER_API_KEY!,
    secret: process.env.POLYMARKET_BUILDER_SECRET!,
    passphrase: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
  }),
});
```

**Remote Builder Signing**

Keep Builder credentials behind your signing endpoint. The client sends the
same `{ method, path, body }` request and applies the same Builder headers, so
the endpoint contract does not change.

```ts Before theme={null}
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
  remoteBuilderConfig: {
    url: "https://example.com/api/builder/sign",
    token: process.env.BUILDER_SIGNING_TOKEN,
  },
});

const relayer = new RelayClient(
  "https://relayer-v2.polymarket.com",
  137,
  walletClient,
  builderConfig,
);
```

```ts After theme={null}
import { createSecureClient, remoteBuilderSigning } from "@polymarket/client";

const client = await createSecureClient({
  signer,
  apiKey: remoteBuilderSigning({
    url: "https://example.com/api/builder/sign",
    headers: {
      Authorization: `Bearer ${process.env.BUILDER_SIGNING_TOKEN}`,
    },
  }),
});
```

On the signing server, replace `BuilderConfig.generateBuilderHeaders` with
`buildHmacSignature`. Keep your existing caller authentication and
authorization around this handler.

```ts Before theme={null}
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
  localBuilderCreds: {
    key: process.env.POLYMARKET_BUILDER_API_KEY!,
    secret: process.env.POLYMARKET_BUILDER_SECRET!,
    passphrase: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
  },
});

export async function POST(request: Request): Promise<Response> {
  const { body, method, path } = await request.json();
  const headers = await builderConfig.generateBuilderHeaders(
    method,
    path,
    body,
  );

  return Response.json(headers);
}
```

```ts After theme={null}
import { buildHmacSignature } from "@polymarket/client";

export async function POST(request: Request): Promise<Response> {
  const { body, method, path } = await request.json();
  const timestamp = Math.floor(Date.now() / 1000);

  return Response.json({
    POLY_BUILDER_API_KEY: process.env.POLYMARKET_BUILDER_API_KEY!,
    POLY_BUILDER_PASSPHRASE: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
    POLY_BUILDER_SIGNATURE: await buildHmacSignature(
      process.env.POLYMARKET_BUILDER_SECRET!,
      timestamp,
      method,
      path,
      body,
    ),
    POLY_BUILDER_TIMESTAMP: `${timestamp}`,
  });
}
```

### Configure Relayer API Keys

`SecureClient` configures Relayer API keys directly. Pass the key and its
associated address to `relayerApiKey` when reconnecting an existing account.

```ts theme={null}
import { createSecureClient, relayerApiKey } from "@polymarket/client";
import { privateKey } from "@polymarket/client/viem";

const client = await createSecureClient({
  wallet: process.env.POLYMARKET_WALLET_ADDRESS,
  signer: privateKey(process.env.POLYMARKET_PRIVATE_KEY),
  apiKey: relayerApiKey({
    key: process.env.POLYMARKET_RELAYER_API_KEY!,
    address: process.env.POLYMARKET_RELAYER_API_KEY_ADDRESS!,
  }),
});
```

### Deploy a Deposit Wallet

Creating a `SecureClient` without a `wallet` derives the signer's Deposit Wallet
address and deploys it when needed. Use one of the Builder authorization
strategies above to authorize the deployment.

```ts Before theme={null}
const deployment = await relayer.deployDepositWallet();
await deployment.wait();
```

```ts After theme={null}
import { createSecureClient } from "@polymarket/client";
import { builderApiKey } from "@polymarket/client/node";
import { privateKey } from "@polymarket/client/viem";

const client = await createSecureClient({
  signer: privateKey(process.env.POLYMARKET_PRIVATE_KEY),
  apiKey: builderApiKey({
    key: process.env.POLYMARKET_BUILDER_API_KEY!,
    secret: process.env.POLYMARKET_BUILDER_SECRET!,
    passphrase: process.env.POLYMARKET_BUILDER_PASSPHRASE!,
  }),
});

const depositWalletAddress = client.account.wallet;
```

## Market Discovery

### Fetch a Market

Both `PublicClient` and `SecureClient` provide `fetchMarket` for reads by Gamma
market ID, slug, or Polymarket URL.

```ts Before theme={null}
const market = await client.getMarket("CONDITION_ID");
```

```ts After theme={null}
const market = await client.fetchMarket({ slug: "MARKET_SLUG" });
```

If you only have a condition ID, filter `listMarkets` and fetch its first page.

```ts theme={null}
const page = await client
  .listMarkets({ conditionIds: ["CONDITION_ID"] })
  .firstPage();

const market = page.items[0];
```

### List Markets

Both `PublicClient` and `SecureClient` provide `listMarkets`, which returns a
paginator and accepts filters directly.

```ts Before theme={null}
const page = await client.getMarkets();
const markets = page.data;
```

```ts After theme={null}
const pages = client.listMarkets({ closed: false, pageSize: 20 });
const page = await pages.firstPage();
const markets = page.items;
```

`getSimplifiedMarkets` does not need a separate replacement. Unified market
models are normalized for SDK use. Sampling-market reads should migrate to
`listCurrentRewards`, which lists the active reward configurations.

```ts Before theme={null}
const markets = await client.getSamplingMarkets();
const page = await client.getSamplingSimplifiedMarkets();
```

```ts After theme={null}
const pages = client.listCurrentRewards();
const page = await pages.firstPage();
```

## Market Data

### Read Trading Parameters

Both `PublicClient` and `SecureClient` return tick size and negative-risk status
on the unified market model. Order methods also resolve them automatically, so
you no longer pass either value when placing an order.

```ts Before theme={null}
const tickSize = await client.getTickSize("TOKEN_ID");
const negRisk = await client.getNegRisk("TOKEN_ID");
```

```ts After theme={null}
const page = await client
  .listMarkets({ clobTokenIds: ["TOKEN_ID"] })
  .firstPage();

const market = page.items[0];
const tickSize = market?.trading.minimumTickSize;
const negRisk = market?.state.negRisk;
```

### Read CLOB Market Details

Both `PublicClient` and `SecureClient` return the normalized market model for
public product data. Its trading fields replace the compact CLOB market response
and standalone fee reads.

```ts Before theme={null}
const info = await client.getClobMarketInfo("CONDITION_ID");
const feeRateBps = await client.getFeeRateBps("TOKEN_ID");
const feeExponent = await client.getFeeExponent("TOKEN_ID");
```

```ts After theme={null}
const page = await client
  .listMarkets({ conditionIds: ["CONDITION_ID"] })
  .firstPage();

const market = page.items[0];
const feeSchedule = market?.trading.feeSchedule;
```

### Fetch Order Books

Both `PublicClient` and `SecureClient` provide single and batch order book reads
with camelCase request fields.

```ts Before theme={null}
const book = await client.getOrderBook("TOKEN_ID");
const books = await client.getOrderBooks([
  { token_id: "TOKEN_ID_1" },
  { token_id: "TOKEN_ID_2" },
]);
```

```ts After theme={null}
const book = await client.fetchOrderBook({ tokenId: "TOKEN_ID" });
const books = await client.fetchOrderBooks([
  { tokenId: "TOKEN_ID_1" },
  { tokenId: "TOKEN_ID_2" },
]);
```

### Fetch Prices

Both `PublicClient` and `SecureClient` provide single and batch price reads with
`OrderSide` and camelCase request fields.

```ts Before theme={null}
import { Side } from "@polymarket/clob-client-v2";

const price = await client.getPrice("TOKEN_ID", Side.BUY);
const prices = await client.getPrices([
  { token_id: "TOKEN_ID_1", side: Side.BUY },
  { token_id: "TOKEN_ID_2", side: Side.SELL },
]);
```

```ts After theme={null}
import { OrderSide } from "@polymarket/client";

const price = await client.fetchPrice({
  tokenId: "TOKEN_ID",
  side: OrderSide.BUY,
});
const prices = await client.fetchPrices([
  { tokenId: "TOKEN_ID_1", side: OrderSide.BUY },
  { tokenId: "TOKEN_ID_2", side: OrderSide.SELL },
]);
```

### Fetch Midpoints

Both `PublicClient` and `SecureClient` provide `fetchMidpoint` and
`fetchMidpoints` for single and batch reads.

```ts Before theme={null}
const midpoint = await client.getMidpoint("TOKEN_ID");
const midpoints = await client.getMidpoints([
  { token_id: "TOKEN_ID_1" },
  { token_id: "TOKEN_ID_2" },
]);
```

```ts After theme={null}
const midpoint = await client.fetchMidpoint({ tokenId: "TOKEN_ID" });
const midpoints = await client.fetchMidpoints([
  { tokenId: "TOKEN_ID_1" },
  { tokenId: "TOKEN_ID_2" },
]);
```

### Fetch Spreads

Both `PublicClient` and `SecureClient` provide single and batch spread reads
with the same request pattern.

```ts Before theme={null}
const spread = await client.getSpread("TOKEN_ID");
const spreads = await client.getSpreads([
  { token_id: "TOKEN_ID_1" },
  { token_id: "TOKEN_ID_2" },
]);
```

```ts After theme={null}
const spread = await client.fetchSpread({ tokenId: "TOKEN_ID" });
const spreads = await client.fetchSpreads([
  { tokenId: "TOKEN_ID_1" },
  { tokenId: "TOKEN_ID_2" },
]);
```

### Fetch Last Trade Prices

Both `PublicClient` and `SecureClient` provide singular and batch methods for
last-trade prices.

```ts Before theme={null}
const lastTrade = await client.getLastTradePrice("TOKEN_ID");
const lastTrades = await client.getLastTradesPrices([
  { token_id: "TOKEN_ID_1" },
  { token_id: "TOKEN_ID_2" },
]);
```

```ts After theme={null}
const lastTrade = await client.fetchLastTradePrice({ tokenId: "TOKEN_ID" });
const lastTrades = await client.fetchLastTradePrices([
  { tokenId: "TOKEN_ID_1" },
  { tokenId: "TOKEN_ID_2" },
]);
```

### Fetch Price History

Both `PublicClient` and `SecureClient` provide price history. Pass all parameters
in one request object; the response uses camelCase fields and typed timestamps.

```ts Before theme={null}
const history = await client.getPricesHistory({
  market: "TOKEN_ID",
  interval: "1d",
  fidelity: 60,
});
```

```ts After theme={null}
import { PriceHistoryInterval } from "@polymarket/client";

const history = await client.fetchPriceHistory({
  tokenId: "TOKEN_ID",
  interval: PriceHistoryInterval.ONE_DAY,
  fidelity: 60,
});
```

### Estimate a Market Order Price

Both `PublicClient` and `SecureClient` provide market-order price estimates. The
request distinguishes collateral spent for buys from shares sold for sells.

```ts Before theme={null}
const price = await client.calculateMarketPrice(
  "TOKEN_ID",
  Side.BUY,
  100,
  OrderType.FAK,
);
```

```ts After theme={null}
const price = await client.estimateMarketPrice({
  tokenId: "TOKEN_ID",
  side: OrderSide.BUY,
  amount: 100,
});
```

### List Recent Market Trades

Both `PublicClient` and `SecureClient` provide the public trade paginator, which
replaces the previous market-events response.

```ts Before theme={null}
const trades = await client.getMarketTradesEvents("CONDITION_ID");
```

```ts After theme={null}
const pages = client.listTrades({ market: ["CONDITION_ID"] });
const page = await pages.firstPage();
const trades = page.items;
```

## Orders

### Place a Limit Order

`SecureClient` resolves tick size, negative-risk status, fees, and signing
details before it submits a limit order.

```ts Before theme={null}
const response = await client.createAndPostOrder(
  {
    tokenID: "TOKEN_ID",
    price: 0.52,
    size: 10,
    side: Side.BUY,
  },
  { tickSize: "0.01", negRisk: false },
  OrderType.GTC,
);
```

```ts After theme={null}
const response = await client.placeLimitOrder({
  tokenId: "TOKEN_ID",
  price: 0.52,
  size: 10,
  side: OrderSide.BUY,
});
```

Set `expiration` for a GTD order and `postOnly: true` for a post-only order.

### Place a Market Order

`SecureClient` places market orders. Buys specify collateral to spend, while
sells specify shares to sell.

```ts Before theme={null}
const response = await client.createAndPostMarketOrder(
  {
    tokenID: "TOKEN_ID",
    amount: 10,
    userUSDCBalance: 10,
    side: Side.BUY,
  },
  { tickSize: "0.01", negRisk: false },
  OrderType.FAK,
);
```

```ts After theme={null}
const response = await client.placeMarketOrder({
  tokenId: "TOKEN_ID",
  amount: 10,
  maxSpend: 10,
  side: OrderSide.BUY,
  orderType: OrderType.FAK,
});
```

`userUSDCBalance` becomes `maxSpend`. The previous field supplied the account
balance used to adjust the order for fees; the unified SDK instead accepts the
maximum total USD to spend. Set `maxSpend` equal to `amount` when the amount
should include fees, or omit it to pay applicable fees on top.

### Sign Without Posting

`SecureClient` provides order-type-specific creation methods when signing and
submission need to happen separately.

```ts Before theme={null}
const signedOrder = await client.createOrder(
  {
    tokenID: "TOKEN_ID",
    price: 0.52,
    size: 10,
    side: Side.BUY,
  },
  { tickSize: "0.01", negRisk: false },
);

const response = await client.postOrder(signedOrder, OrderType.GTC);
```

```ts After theme={null}
const signedOrder = await client.createLimitOrder({
  tokenId: "TOKEN_ID",
  price: 0.52,
  size: 10,
  side: OrderSide.BUY,
});

const response = await client.postOrder(signedOrder);
```

Use `createMarketOrder` instead when preparing an FAK or FOK market order.

### Post Several Orders

`SecureClient` provides `postOrders`. Order type and post-only behavior are part
of each signed order, so the method accepts the signed orders directly.

```ts Before theme={null}
const response = await client.postOrders([
  { order: firstOrder, orderType: OrderType.GTC },
  { order: secondOrder, orderType: OrderType.GTC },
]);
```

```ts After theme={null}
const response = await client.postOrders([firstOrder, secondOrder]);
```

### Attribute an Order to a Builder

`SecureClient` attaches the builder code to each order.

```ts Before theme={null}
const response = await client.createAndPostOrder(
  {
    tokenID: "TOKEN_ID",
    price: 0.52,
    size: 10,
    side: Side.BUY,
    builderCode: process.env.POLYMARKET_BUILDER_CODE,
  },
  { tickSize: "0.01", negRisk: false },
);
```

```ts After theme={null}
const response = await client.placeLimitOrder({
  tokenId: "TOKEN_ID",
  price: 0.52,
  size: 10,
  side: OrderSide.BUY,
  builderCode: process.env.POLYMARKET_BUILDER_CODE,
});
```

### Cancel Orders

`SecureClient` provides the cancel methods. They now accept camelCase request
objects, while `cancelAll` remains parameterless.

```ts Before theme={null}
await client.cancelOrder("ORDER_ID");
await client.cancelOrders(["ORDER_ID_1", "ORDER_ID_2"]);
await client.cancelAll();
await client.cancelMarketOrders({
  market: "CONDITION_ID",
  asset_id: "TOKEN_ID",
});
```

```ts After theme={null}
await client.cancelOrder({ orderId: "ORDER_ID" });
await client.cancelOrders({ orderIds: ["ORDER_ID_1", "ORDER_ID_2"] });
await client.cancelAll();
await client.cancelMarketOrders({
  market: "CONDITION_ID",
  tokenId: "TOKEN_ID",
});
```

### Fetch an Order

`SecureClient` fetches an order by ID using a request object.

```ts Before theme={null}
const order = await client.getOrder("ORDER_ID");
```

```ts After theme={null}
const order = await client.fetchOrder({ orderId: "ORDER_ID" });
```

### List Open Orders

`SecureClient` provides `listOpenOrders`, which returns a paginator. Filters and
response fields use camelCase.

```ts Before theme={null}
const orders = await client.getOpenOrders({
  market: "CONDITION_ID",
  asset_id: "TOKEN_ID",
});
```

```ts After theme={null}
const pages = client.listOpenOrders({
  market: "CONDITION_ID",
  tokenId: "TOKEN_ID",
});
const orders = [];
for await (const page of pages) {
  orders.push(...page.items);
}
```

### Check Order Scoring

`SecureClient` provides `fetchOrderScoring` for one order and
`fetchOrdersScoring` for several.

```ts Before theme={null}
const scoring = await client.isOrderScoring({ orderId: "ORDER_ID" });
const batch = await client.areOrdersScoring({
  orderIds: ["ORDER_ID_1", "ORDER_ID_2"],
});
```

```ts After theme={null}
const scoring = await client.fetchOrderScoring({ orderId: "ORDER_ID" });
const batch = await client.fetchOrdersScoring({
  orderIds: ["ORDER_ID_1", "ORDER_ID_2"],
});
```

## Account Activity and Balances

### List Account Trades

`SecureClient` replaces both previous account trade-history methods with one
paginator.

```ts Before theme={null}
const trades = await client.getTrades({ market: "CONDITION_ID" });
const page = await client.getTradesPaginated({ market: "CONDITION_ID" });
```

```ts After theme={null}
const pages = client.listAccountTrades({ market: "CONDITION_ID" });
const firstPage = await pages.firstPage();

const trades = [];
for await (const page of pages) {
  trades.push(...page.items);
}
```

### List Builder Trades

Both `PublicClient` and `SecureClient` provide public builder trade history,
filtered by builder code.

```ts Before theme={null}
const trades = await client.getBuilderTrades();
```

```ts After theme={null}
const pages = client.listBuilderTrades({
  builderCode: process.env.POLYMARKET_BUILDER_CODE,
});
const page = await pages.firstPage();
const trades = page.items;
```

### Read and Drop Notifications

`SecureClient` provides notification methods with action-oriented names and
camelCase request fields.

```ts Before theme={null}
const notifications = await client.getNotifications();
await client.dropNotifications({ ids: [1, 2] });
```

```ts After theme={null}
const notifications = await client.fetchNotifications();
await client.dropNotifications({ ids: ["1", "2"] });
```

### Refresh Balances and Allowances

`SecureClient` manages balances and allowances while placing orders. It detects
a missing allowance, completes the required approval, refreshes the balance and
allowance, and retries the order.

```ts Before theme={null}
await client.updateBalanceAllowance({
  asset_type: AssetType.COLLATERAL,
});

const balance = await client.getBalanceAllowance({
  asset_type: AssetType.COLLATERAL,
});
```

```ts After theme={null}
const response = await client.placeLimitOrder({
  tokenId: "TOKEN_ID",
  price: 0.52,
  size: 10,
  side: OrderSide.BUY,
});
```

## Positions

The unified methods build and submit the wallet transactions. You no longer
need to encode contract calls or pass transaction arrays to `execute`.

### Split a Position

`SecureClient` splits collateral into a complete set of YES and NO outcome
tokens.

```ts Before theme={null}
const splitTx = {
  to: CTF_COLLATERAL_ADAPTER_ADDRESS,
  data: collateralAdapterInterface.encodeFunctionData("splitPosition", [
    PUSD_ADDRESS,
    ethers.constants.HashZero,
    conditionId,
    [1, 2],
    ethers.utils.parseUnits("1", 6),
  ]),
  value: "0",
};

const split = await relayer.execute([splitTx], "Split position");
await split.wait();
```

```ts After theme={null}
const split = await client.splitPosition({
  conditionId,
  amount: 1_000_000n,
});

await split.wait();
```

### Merge Positions

`SecureClient` merges balanced YES and NO tokens back into collateral.

```ts Before theme={null}
const mergeTx = {
  to: CTF_COLLATERAL_ADAPTER_ADDRESS,
  data: collateralAdapterInterface.encodeFunctionData("mergePositions", [
    PUSD_ADDRESS,
    ethers.constants.HashZero,
    conditionId,
    [1, 2],
    ethers.utils.parseUnits("1", 6),
  ]),
  value: "0",
};

const merge = await relayer.execute([mergeTx], "Merge positions");
await merge.wait();
```

```ts After theme={null}
const merge = await client.mergePositions({
  conditionId,
  amount: "max",
});

await merge.wait();
```

### Redeem Resolved Positions

`SecureClient` redeems winning outcome tokens for collateral after resolution.

```ts Before theme={null}
const redeemTx = {
  to: CTF_COLLATERAL_ADAPTER_ADDRESS,
  data: collateralAdapterInterface.encodeFunctionData("redeemPositions", [
    PUSD_ADDRESS,
    ethers.constants.HashZero,
    conditionId,
    [1, 2],
  ]),
  value: "0",
};

const redeem = await relayer.execute([redeemTx], "Redeem positions");
await redeem.wait();
```

```ts After theme={null}
const redeem = await client.redeemPositions({ conditionId });
await redeem.wait();
```

## Service Status

Neither `PublicClient` nor `SecureClient` requires these calls. The unified
clients manage request timing internally.

```ts Before theme={null}
await client.getOk();
const timestamp = await client.getServerTime();
```

```ts After theme={null}
// No client call is required for request timestamp synchronization.
```
```

Example 2 (python):
```python
Public clients provide unauthenticated market discovery and data reads.
Secure clients add authenticated trading, account, and wallet actions.
Python provides async and sync versions of each, so choose the interface
that matches your application's execution model.

| Interface | Clients                                  | Best for                                             |
| --------- | ---------------------------------------- | ---------------------------------------------------- |
| Async     | `AsyncPublicClient`, `AsyncSecureClient` | Services, bots, and applications using an event loop |
| Sync      | `PublicClient`, `SecureClient`           | Scripts, notebooks, and synchronous applications     |

The examples below use the async clients.

<Note>
  Some features are available only through the async clients due to their
  streaming nature.
</Note>

## Install the Unified SDK

Remove the previous CLOB, relayer, and builder-signing packages. Then install the
unified SDK.

<CodeGroup>
  ```bash uv theme={null}
  uv remove py-clob-client-v2 py-builder-relayer-client py-builder-signing-sdk
  uv add polymarket-client
  ```

  ```bash pip theme={null}
  pip uninstall -y py-clob-client-v2 py-builder-relayer-client py-builder-signing-sdk
  pip install polymarket-client
  ```

  ```bash Poetry theme={null}
  poetry remove py-clob-client-v2 py-builder-relayer-client py-builder-signing-sdk
  poetry add polymarket-client
  ```
</CodeGroup>

## Client and Wallet Setup

### Create a Public Client

`AsyncPublicClient` provides unauthenticated market discovery and data reads.
Production is the default environment.

```python Before theme={null}
from py_clob_client_v2.client import ClobClient

client = ClobClient("https://clob.polymarket.com", chain_id=137)
```

```python After theme={null}
from polymarket import AsyncPublicClient

client = AsyncPublicClient()
```

### Create an Authenticated Client

`AsyncSecureClient` adds authenticated trading, account, and wallet actions.
`create` derives or creates CLOB credentials, resolves the account wallet, and
configures signing.

```python Before theme={null}
import os

from py_clob_client_v2.client import ClobClient
from py_clob_client_v2.order_utils.model import SignatureTypeV2

temporary_client = ClobClient(
    "https://clob.polymarket.com",
    chain_id=137,
    key=os.environ["POLYMARKET_PRIVATE_KEY"],
)
credentials = temporary_client.create_or_derive_api_key()

client = ClobClient(
    "https://clob.polymarket.com",
    chain_id=137,
    key=os.environ["POLYMARKET_PRIVATE_KEY"],
    creds=credentials,
    signature_type=SignatureTypeV2.POLY_1271,
    funder=os.environ["POLYMARKET_WALLET_ADDRESS"],
)
```

```python After theme={null}
import os

from polymarket import AsyncSecureClient

client = await AsyncSecureClient.create(
    private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
    wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
)
```

Omit `wallet` to use the default Deposit Wallet flow.

### Resume With Existing Credentials

Read credentials from an authenticated client, store them securely, and pass
them to a new client to resume with the same API key. The private key and wallet
must identify the account that owns the credentials.

```python Before theme={null}
import os

from py_clob_client_v2.client import ClobClient
from py_clob_client_v2.order_utils.model import SignatureTypeV2

credentials = client.creds
if credentials is None:
    raise RuntimeError("Client has no credentials")

# Store the credentials securely.

resumed_client = ClobClient(
    "https://clob.polymarket.com",
    chain_id=137,
    key=os.environ["POLYMARKET_PRIVATE_KEY"],
    creds=credentials,
    signature_type=SignatureTypeV2.POLY_1271,
    funder=os.environ["POLYMARKET_WALLET_ADDRESS"],
)
```

```python After theme={null}
import os

from polymarket import AsyncSecureClient

credentials = client.credentials

# Store the credentials securely.

resumed_client = await AsyncSecureClient.create(
    private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
    wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
    credentials=credentials,
)
```

### Revoke the Current API Key

Ending authentication revokes the current API key, invalidates the
`AsyncSecureClient`, and returns an `AsyncPublicClient`.

```python Before theme={null}
client.delete_api_key()
```

```python After theme={null}
public_client = await client.end_authentication()
```

### Configure Builder API Keys

`AsyncSecureClient` accepts a `BuilderApiKey` for gasless wallet actions. Keep
the key, secret, and passphrase on the server.

```python Before theme={null}
import os

from py_builder_relayer_client.client import RelayClient
from py_builder_signing_sdk.config import BuilderConfig
from py_builder_signing_sdk.sdk_types import BuilderApiKeyCreds

builder_config = BuilderConfig(
    local_builder_creds=BuilderApiKeyCreds(
        key=os.environ["POLYMARKET_BUILDER_API_KEY"],
        secret=os.environ["POLYMARKET_BUILDER_SECRET"],
        passphrase=os.environ["POLYMARKET_BUILDER_PASSPHRASE"],
    )
)

relayer = RelayClient(
    "https://relayer-v2.polymarket.com",
    137,
    os.environ["POLYMARKET_PRIVATE_KEY"],
    builder_config,
)
```

```python After theme={null}
import os

from polymarket import AsyncSecureClient, BuilderApiKey

client = await AsyncSecureClient.create(
    private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
    api_key=BuilderApiKey(
        key=os.environ["POLYMARKET_BUILDER_API_KEY"],
        secret=os.environ["POLYMARKET_BUILDER_SECRET"],
        passphrase=os.environ["POLYMARKET_BUILDER_PASSPHRASE"],
    ),
)
```

### Configure Relayer API Keys

`AsyncSecureClient` configures Relayer API keys directly. Pass the key and its
associated address when reconnecting an existing account.

```python theme={null}
import os

from polymarket import AsyncSecureClient, RelayerApiKey

client = await AsyncSecureClient.create(
    private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
    wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
    api_key=RelayerApiKey(
        key=os.environ["POLYMARKET_RELAYER_API_KEY"],
        address=os.environ["POLYMARKET_RELAYER_API_KEY_ADDRESS"],
    ),
)
```

### Deploy a Deposit Wallet

Creating an `AsyncSecureClient` without a `wallet` derives the signer's Deposit
Wallet address and deploys it when needed. Use Builder authorization to
authorize the deployment.

```python Before theme={null}
deployment = relayer.deploy_deposit_wallet()
deployment.wait()
```

```python After theme={null}
import os

from polymarket import AsyncSecureClient, BuilderApiKey

client = await AsyncSecureClient.create(
    private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
    api_key=BuilderApiKey(
        key=os.environ["POLYMARKET_BUILDER_API_KEY"],
        secret=os.environ["POLYMARKET_BUILDER_SECRET"],
        passphrase=os.environ["POLYMARKET_BUILDER_PASSPHRASE"],
    ),
)

deposit_wallet_address = client.wallet
```

## Market Discovery

### Fetch a Market

Both `AsyncPublicClient` and `AsyncSecureClient` provide `get_market` for reads
by Gamma market ID, slug, or Polymarket URL.

```python Before theme={null}
market = client.get_market("CONDITION_ID")
```

```python After theme={null}
market = await client.get_market(slug="MARKET_SLUG")
```

If you only have a condition ID, filter `list_markets` and fetch its first page.

```python theme={null}
pages = client.list_markets(condition_ids=["CONDITION_ID"])
page = await pages.first_page()
market = page.items[0]
```

### List Markets

Both `AsyncPublicClient` and `AsyncSecureClient` provide `list_markets`, which
returns an async paginator and accepts filters directly.

```python Before theme={null}
page = client.get_markets()
markets = page["data"]
```

```python After theme={null}
pages = client.list_markets(closed=False, page_size=20)
page = await pages.first_page()
markets = page.items
```

Simplified-market reads do not need a separate replacement. Sampling-market
reads migrate to `list_current_rewards`, which lists active reward
configurations.

```python Before theme={null}
markets = client.get_sampling_markets()
page = client.get_sampling_simplified_markets()
```

```python After theme={null}
pages = client.list_current_rewards()
page = await pages.first_page()
```

## Market Data

### Read Trading Parameters

Both `AsyncPublicClient` and `AsyncSecureClient` return tick size and
negative-risk status on the market model. Order methods also resolve them
automatically.

```python Before theme={null}
tick_size = client.get_tick_size("TOKEN_ID")
neg_risk = client.get_neg_risk("TOKEN_ID")
fee_rate_bps = client.get_fee_rate_bps("TOKEN_ID")
```

```python After theme={null}
market = await client.get_market(slug="MARKET_SLUG")
tick_size = market.trading.minimum_tick_size
neg_risk = market.state.neg_risk
fee_schedule = market.trading.fee_schedule
```

### Read CLOB Market Details

Both `AsyncPublicClient` and `AsyncSecureClient` return the typed market model.
Its trading fields replace the compact CLOB market response.

```python Before theme={null}
details = client.get_clob_market_info("CONDITION_ID")
tick_size = details["mts"]
neg_risk = details["nr"]
fee_details = details["fd"]
```

```python After theme={null}
market = await client.get_market(slug="MARKET_SLUG")
tick_size = market.trading.minimum_tick_size
neg_risk = market.state.neg_risk
fee_schedule = market.trading.fee_schedule
```

### Fetch Order Books

Both `AsyncPublicClient` and `AsyncSecureClient` provide single and batch order
book reads.

```python Before theme={null}
from py_clob_client_v2 import BookParams

book = client.get_order_book("TOKEN_ID")
books = client.get_order_books(
    [BookParams(token_id="TOKEN_ID_1"), BookParams(token_id="TOKEN_ID_2")]
)
```

```python After theme={null}
book = await client.get_order_book(token_id="TOKEN_ID")
books = await client.get_order_books(token_ids=["TOKEN_ID_1", "TOKEN_ID_2"])
```

### Fetch Prices

Both `AsyncPublicClient` and `AsyncSecureClient` provide single and batch price
reads with typed requests.

```python Before theme={null}
from py_clob_client_v2 import BookParams, Side

price = client.get_price("TOKEN_ID", Side.BUY)
prices = client.get_prices(
    [
        BookParams(token_id="TOKEN_ID_1", side=Side.BUY),
        BookParams(token_id="TOKEN_ID_2", side=Side.SELL),
    ]
)
```

```python After theme={null}
from polymarket import PriceRequest

price = await client.get_price(token_id="TOKEN_ID", side="BUY")
prices = await client.get_prices(
    requests=[
        PriceRequest(token_id="TOKEN_ID_1", side="BUY"),
        PriceRequest(token_id="TOKEN_ID_2", side="SELL"),
    ]
)
```

### Fetch Midpoints

Both `AsyncPublicClient` and `AsyncSecureClient` provide single and batch
midpoint reads.

```python Before theme={null}
from py_clob_client_v2 import BookParams

midpoint = client.get_midpoint("TOKEN_ID")
midpoints = client.get_midpoints(
    [BookParams(token_id="TOKEN_ID_1"), BookParams(token_id="TOKEN_ID_2")]
)
```

```python After theme={null}
midpoint = await client.get_midpoint(token_id="TOKEN_ID")
midpoints = await client.get_midpoints(token_ids=["TOKEN_ID_1", "TOKEN_ID_2"])
```

### Fetch Spreads

Both `AsyncPublicClient` and `AsyncSecureClient` provide single and batch spread
reads.

```python Before theme={null}
from py_clob_client_v2 import BookParams

spread = client.get_spread("TOKEN_ID")
spreads = client.get_spreads(
    [BookParams(token_id="TOKEN_ID_1"), BookParams(token_id="TOKEN_ID_2")]
)
```

```python After theme={null}
spread = await client.get_spread(token_id="TOKEN_ID")
spreads = await client.get_spreads(token_ids=["TOKEN_ID_1", "TOKEN_ID_2"])
```

### Fetch Last Trade Prices

Both `AsyncPublicClient` and `AsyncSecureClient` provide singular and batch
methods for last-trade prices.

```python Before theme={null}
from py_clob_client_v2 import BookParams

last_trade = client.get_last_trade_price("TOKEN_ID")
last_trades = client.get_last_trades_prices(
    [BookParams(token_id="TOKEN_ID_1"), BookParams(token_id="TOKEN_ID_2")]
)
```

```python After theme={null}
last_trade = await client.get_last_trade_price(token_id="TOKEN_ID")
last_trades = await client.get_last_trade_prices(
    token_ids=["TOKEN_ID_1", "TOKEN_ID_2"]
)
```

### Fetch Price History

Both `AsyncPublicClient` and `AsyncSecureClient` provide price history. Pass the
parameters as keyword arguments; the response contains typed points.

```python Before theme={null}
from py_clob_client_v2 import PricesHistoryParams

history = client.get_prices_history(
    PricesHistoryParams(market="TOKEN_ID", interval="1d", fidelity=60)
)
```

```python After theme={null}
history = await client.get_price_history(
    token_id="TOKEN_ID",
    interval="1d",
    fidelity=60,
)
```

### Estimate a Market Order Price

Both `AsyncPublicClient` and `AsyncSecureClient` provide market-order price
estimates. Buys specify collateral spent, while sells specify shares sold.

```python Before theme={null}
from py_clob_client_v2 import OrderType, Side

buy_price = client.calculate_market_price(
    "TOKEN_ID", Side.BUY, 10, OrderType.FOK
)
sell_price = client.calculate_market_price(
    "TOKEN_ID", Side.SELL, 5, OrderType.FOK
)
```

```python After theme={null}
buy_price = await client.estimate_market_price(
    token_id="TOKEN_ID", side="BUY", amount=10, order_type="FOK"
)
sell_price = await client.estimate_market_price(
    token_id="TOKEN_ID", side="SELL", shares=5, order_type="FOK"
)
```

### List Recent Market Trades

Both `AsyncPublicClient` and `AsyncSecureClient` provide the public trade
paginator, which replaces the previous market-events response.

```python Before theme={null}
trades = client.get_market_trades_events("CONDITION_ID")
```

```python After theme={null}
pages = client.list_trades(market=["CONDITION_ID"])
page = await pages.first_page()
trades = page.items
```

## Orders

### Place a Limit Order

`AsyncSecureClient` resolves tick size, negative-risk status, fees, and signing
details before submitting a limit order.

```python Before theme={null}
from py_clob_client_v2 import OrderArgs, Side

response = client.create_and_post_order(
    OrderArgs(
        token_id="TOKEN_ID",
        price=0.52,
        size=10,
        side=Side.BUY,
    )
)
```

```python After theme={null}
response = await client.place_limit_order(
    token_id="TOKEN_ID",
    price=0.52,
    size=10,
    side="BUY",
)
```

### Place a Market Order

`AsyncSecureClient` places market orders. Buys specify collateral to spend,
while sells specify shares to sell.

```python Before theme={null}
from py_clob_client_v2 import MarketOrderArgs, OrderType, Side

response = client.create_and_post_market_order(
    MarketOrderArgs(
        token_id="TOKEN_ID",
        amount=10,
        user_usdc_balance=10,
        side=Side.BUY,
    ),
    order_type=OrderType.FOK,
)
```

```python After theme={null}
response = await client.place_market_order(
    token_id="TOKEN_ID",
    side="BUY",
    amount=10,
    max_spend=10,
    order_type="FOK",
)
```

`user_usdc_balance` becomes `max_spend`. The previous field supplied the
account balance used to adjust the order for fees; the unified SDK instead
accepts the maximum total USD to spend. Set `max_spend` equal to `amount` when
the amount should include fees, or omit it to pay applicable fees on top.

### Sign Without Posting

`AsyncSecureClient` provides order-type-specific creation methods when signing
and submission need to happen separately.

```python Before theme={null}
from py_clob_client_v2 import MarketOrderArgs, OrderArgs, Side

limit_order = client.create_order(
    OrderArgs(token_id="TOKEN_ID", price=0.52, size=10, side=Side.BUY)
)
market_order = client.create_market_order(
    MarketOrderArgs(token_id="TOKEN_ID", amount=10, side=Side.BUY)
)
```

```python After theme={null}
limit_order = await client.create_limit_order(
    token_id="TOKEN_ID",
    price=0.52,
    size=10,
    side="BUY",
)
market_order = await client.create_market_order(
    token_id="TOKEN_ID",
    side="BUY",
    amount=10,
)
```

### Post Several Orders

`AsyncSecureClient` provides `post_orders`. Order type and post-only behavior
are part of each signed order, so the method accepts signed orders directly.

```python Before theme={null}
from py_clob_client_v2 import OrderType, PostOrdersV2Args

responses = client.post_orders(
    [
        PostOrdersV2Args(order=first_order, orderType=OrderType.GTC),
        PostOrdersV2Args(order=second_order, orderType=OrderType.GTC),
    ]
)
```

```python After theme={null}
responses = await client.post_orders([first_order, second_order])
```

### Attribute an Order to a Builder

`AsyncSecureClient` attaches the builder code to each order.

```python Before theme={null}
from py_clob_client_v2 import OrderArgs, Side

response = client.create_and_post_order(
    OrderArgs(
        token_id="TOKEN_ID",
        price=0.52,
        size=10,
        side=Side.BUY,
        builder_code="BUILDER_CODE",
    )
)
```

```python After theme={null}
response = await client.place_limit_order(
    token_id="TOKEN_ID",
    price=0.52,
    size=10,
    side="BUY",
    builder_code="BUILDER_CODE",
)
```

### Cancel Orders

`AsyncSecureClient` provides explicit methods for cancelling one order,
several orders, all orders, or orders for a market.

```python Before theme={null}
from py_clob_client_v2 import OrderMarketCancelParams, OrderPayload

client.cancel_order(OrderPayload(orderID="ORDER_ID"))
client.cancel_orders(["ORDER_ID_1", "ORDER_ID_2"])
client.cancel_market_orders(OrderMarketCancelParams(market="CONDITION_ID"))
client.cancel_all()
```

```python After theme={null}
await client.cancel_order(order_id="ORDER_ID")
await client.cancel_orders(order_ids=["ORDER_ID_1", "ORDER_ID_2"])
await client.cancel_market_orders(market="CONDITION_ID")
await client.cancel_all()
```

### Fetch an Order

`AsyncSecureClient` fetches an order by ID using a keyword argument.

```python Before theme={null}
order = client.get_order("ORDER_ID")
```

```python After theme={null}
order = await client.get_order(order_id="ORDER_ID")
```

### List Open Orders

`AsyncSecureClient` provides `list_open_orders`, which returns an async
paginator.

```python Before theme={null}
from py_clob_client_v2 import OpenOrderParams

orders = client.get_open_orders(
    OpenOrderParams(market="CONDITION_ID", asset_id="TOKEN_ID")
)
```

```python After theme={null}
pages = client.list_open_orders(market="CONDITION_ID", token_id="TOKEN_ID")
orders = [order async for order in pages.iter_items()]
```

### Check Order Scoring

`AsyncSecureClient` provides `get_order_scoring` for one order and
`get_orders_scoring` for several.

```python Before theme={null}
from py_clob_client_v2 import OrderScoringParams, OrdersScoringParams

scoring = client.is_order_scoring(OrderScoringParams(orderId="ORDER_ID"))
batch = client.are_orders_scoring(
    OrdersScoringParams(orderIds=["ORDER_ID_1", "ORDER_ID_2"])
)
```

```python After theme={null}
scoring = await client.get_order_scoring(order_id="ORDER_ID")
batch = await client.get_orders_scoring(
    order_ids=["ORDER_ID_1", "ORDER_ID_2"]
)
```

## Account Activity and Balances

### List Account Trades

`AsyncSecureClient` replaces both previous account trade-history methods with one
async paginator.

```python Before theme={null}
from py_clob_client_v2 import TradeParams

trades = client.get_trades(TradeParams(market="CONDITION_ID"))
page = client.get_trades_paginated(TradeParams(market="CONDITION_ID"))
```

```python After theme={null}
pages = client.list_account_trades(market="CONDITION_ID")
first_page = await pages.first_page()

trades = [trade async for trade in pages.iter_items()]
```

### List Builder Trades

Both `AsyncPublicClient` and `AsyncSecureClient` provide public builder trade
history, filtered by builder code.

```python Before theme={null}
from py_clob_client_v2 import BuilderTradeParams

page = client.get_builder_trades(
    BuilderTradeParams(builder_code="BUILDER_CODE")
)
trades = page["trades"]
```

```python After theme={null}
pages = client.list_builder_trades(builder_code="BUILDER_CODE")
page = await pages.first_page()
trades = page.items
```

### Read and Drop Notifications

`AsyncSecureClient` provides notification methods with keyword arguments and
typed responses.

```python Before theme={null}
from py_clob_client_v2 import DropNotificationParams

notifications = client.get_notifications()
client.drop_notifications(DropNotificationParams(ids=[1, 2]))
```

```python After theme={null}
notifications = await client.get_notifications()
await client.drop_notifications(ids=["1", "2"])
```

### Refresh Balances and Allowances

`AsyncSecureClient` reads balances and manages missing allowances while placing
orders. It completes the required approval, refreshes the allowance, and
retries the order.

```python Before theme={null}
from py_clob_client_v2 import AssetType, BalanceAllowanceParams

params = BalanceAllowanceParams(asset_type=AssetType.COLLATERAL)
client.update_balance_allowance(params)
balance = client.get_balance_allowance(params)
```

```python After theme={null}
balance = await client.get_balance_allowance(asset_type="COLLATERAL")
response = await client.place_limit_order(
    token_id="TOKEN_ID",
    price=0.52,
    size=10,
    side="BUY",
)
```

## Positions

The unified methods build and submit wallet transactions. You no longer need to
encode contract calls or pass transaction arrays to `execute`.

### Split a Position

`AsyncSecureClient` splits collateral into a complete set of YES and NO outcome
tokens.

```python Before theme={null}
from py_builder_relayer_client.models import Transaction

split_tx = Transaction(
    to=CTF_COLLATERAL_ADAPTER_ADDRESS,
    data=collateral_adapter.encode_abi(
        "splitPosition",
        args=[PUSD_ADDRESS, bytes(32), CONDITION_ID, [1, 2], 1_000_000],
    ),
    value="0",
)

split = relayer.execute([split_tx], "Split position")
split.wait()
```

```python After theme={null}
split = await client.split_position(
    condition_id="CONDITION_ID",
    amount=1_000_000,
)
await split.wait()
```

### Merge Positions

`AsyncSecureClient` merges balanced YES and NO tokens back into collateral.

```python Before theme={null}
from py_builder_relayer_client.models import Transaction

merge_tx = Transaction(
    to=CTF_COLLATERAL_ADAPTER_ADDRESS,
    data=collateral_adapter.encode_abi(
        "mergePositions",
        args=[PUSD_ADDRESS, bytes(32), CONDITION_ID, [1, 2], 1_000_000],
    ),
    value="0",
)

merge = relayer.execute([merge_tx], "Merge positions")
merge.wait()
```

```python After theme={null}
merge = await client.merge_positions(
    condition_id="CONDITION_ID",
    amount="max",
)
await merge.wait()
```

### Redeem Resolved Positions

`AsyncSecureClient` redeems winning outcome tokens for collateral after
resolution.

```python Before theme={null}
from py_builder_relayer_client.models import Transaction

redeem_tx = Transaction(
    to=CTF_COLLATERAL_ADAPTER_ADDRESS,
    data=collateral_adapter.encode_abi(
        "redeemPositions",
        args=[PUSD_ADDRESS, bytes(32), CONDITION_ID, [1, 2]],
    ),
    value="0",
)

redeem = relayer.execute([redeem_tx], "Redeem positions")
redeem.wait()
```

```python After theme={null}
redeem = await client.redeem_positions(condition_id="CONDITION_ID")
await redeem.wait()
```

## Service Status

Neither `AsyncPublicClient` nor `AsyncSecureClient` requires these calls. The
unified clients manage request timing internally.

```python Before theme={null}
client.get_ok()
timestamp = client.get_server_time()
```

```python After theme={null}
# No client call is required for request timestamp synchronization.
```
```

Example 3 (rust):
```rust
See the [GitHub repository](https://github.com/Polymarket/rs-clob-client-v2) and
the [`polymarket_client_sdk_v2` package on crates.io](https://crates.io/crates/polymarket_client_sdk_v2)
for the complete API and examples.

## Install the Rust SDK

Enable the `clob` feature for authentication and trading:

```bash theme={null}
cargo add polymarket_client_sdk_v2@0.7.0 --features clob
```

## Trade From a Deposit Wallet

The Rust SDK supports the CLOB order path for an existing Deposit Wallet. It
does not include a client for deploying Deposit Wallets or submitting wallet
batches; use the Direct API workflows for those actions.

Pass the deployed Deposit Wallet as the funder and use
`SignatureType::Poly1271` when authenticating. This example refreshes the
collateral allowance cache, then places a GTC limit buy:

```rust theme={null}
use std::str::FromStr as _;

use alloy::signers::Signer as _;
use alloy::signers::local::LocalSigner;
use polymarket_client_sdk_v2::clob::types::request::UpdateBalanceAllowanceRequest;
use polymarket_client_sdk_v2::clob::types::{
    AssetType, OrderType, Side, SignatureType,
};
use polymarket_client_sdk_v2::clob::{Client, Config};
use polymarket_client_sdk_v2::types::{Address, Decimal, U256};
use polymarket_client_sdk_v2::{POLYGON, PRIVATE_KEY_VAR};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let host = "https://clob-v2.polymarket.com";
    let signer = LocalSigner::from_str(&std::env::var(PRIVATE_KEY_VAR)?)?
        .with_chain_id(Some(POLYGON));
    let deposit_wallet = Address::from_str(&std::env::var("DEPOSIT_WALLET")?)?;

    let client = Client::new(host, Config::default())?
        .authentication_builder(&signer)
        .funder(deposit_wallet)
        .signature_type(SignatureType::Poly1271)
        .authenticate()
        .await?;

    client
        .update_balance_allowance(
            UpdateBalanceAllowanceRequest::builder()
                .asset_type(AssetType::Collateral)
                .build(),
        )
        .await?;

    let response = client
        .limit_order()
        .token_id(U256::from_str(&std::env::var("TOKEN_ID")?)?)
        .side(Side::Buy)
        .price(Decimal::from_str("0.40")?)
        .size(Decimal::from_str("100")?)
        .order_type(OrderType::GTC)
        .build_sign_and_post(&signer)
        .await?;

    println!("order_id={} status={}", response.order_id, response.status);
    Ok(())
}
```

## Handle Matching Engine Restarts

Rebuild and re-sign an order before each retry because `SignedOrder` is
consumed when it is submitted. Treat HTTP `425` as temporary and retry with
exponential backoff:

```rust theme={null}
use polymarket_client_sdk_v2::error::{Kind, StatusCode};

let mut delay = std::time::Duration::from_secs(1);

for _ in 0..10 {
    let order = client.limit_order()
        .token_id(token_id).price(price).size(size).side(side)
        .build().await?;
    let signed = client.sign(&signer, order).await?;

    match client.post_order(signed).await {
        Ok(response) => return Ok(response),
        Err(err) if err.kind() == Kind::Status => {
            if let Some(status) = err.downcast_ref::<polymarket_client_sdk_v2::error::Status>() {
                if status.status_code == StatusCode::from_u16(425).unwrap() {
                    eprintln!("Engine restarting, retrying in {delay:?}...");
                    tokio::time::sleep(delay).await;
                    delay = (delay * 2).min(std::time::Duration::from_secs(30));
                    continue;
                }
            }
            return Err(err);
        }
        Err(err) => return Err(err),
    }
}
```

See [Matching Engine Restarts](/trading/matching-engine) for the restart window,
post-only period, and restricted-mode responses.
```

---

## Order Lifecycle

**URL:** https://docs.polymarket.com/concepts/order-lifecycle.md

**Contents:**
- How Orders Work
- Order Types
  - Post-Only Orders
- Order Statuses
- Trade Statuses
- Maker vs Taker
- Cancellation
- Requirements
- Next Steps

Every trade on Polymarket follows a specific lifecycle. Orders are created offchain, matched by an operator, and settled onchain through smart contracts. This hybrid approach combines the speed of centralized matching with the security of blockchain settlement.

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/order-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=4db07008193421bfe359afe44b5f604e" alt="" className="dark:hidden" width="2336" height="952" data-path="images/core-concepts/order-lifecycle.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/order-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=5a0f3eba2f20c44471bae05c0670de4a" alt="" className="hidden dark:block" width="2336" height="952" data-path="images/dark/core-concepts/order-lifecycle.png" /> </Frame>

All orders on Polymarket are **limit orders**. A limit order specifies the price you're willing to pay (or accept) and the quantity you want to trade.

<Note> "Market orders" are simply limit orders with a price set to execute immediately against the best available resting orders. </Note>

Orders are **EIP712-signed messages**. When you place an order, you sign a structured message with your private key. This signature authorizes the Exchange contract to execute the trade on your behalf, without ever taking custody of your funds.

| Type    | Behavior                                                      | Use Case                 | | ------- | ------------------------------------------------------------- | ------------------------ | | **GTC** | Good Till Cancelled — rests on book until filled or cancelled | Standard limit orders    | | **GTD** | Good Till Date — auto-expires at specified time               | Time-limited orders      | | **FOK** | Fill Or Kill — fill entirely or cancel immediately            | All-or-nothing execution | | **FAK** | Fill And Kill — fill what's available, cancel the rest        | Partial fills acceptable |

Post-only orders will only rest on the book. If a post-only order would match immediately (cross the spread), it's rejected instead of executed. This guarantees you're always the maker, never the taker.

<Steps> <Step title="Create and Sign"> Your client creates an order object containing:

<Step title="Submit to CLOB"> The signed order is submitted to the Central Limit Order Book (CLOB) operator. The operator validates:

<Step title="Match or Rest"> **If the order is marketable** (your buy price ≥ lowest ask, or your sell price ≤ highest bid), it matches against resting orders. Some markets apply a short taker delay before matching:

<Step title="Settlement"> When orders match, the operator submits the trade to the blockchain. The Exchange contract:

<Step title="Confirmation"> The trade achieves finality on Polygon. Your token balances update and the trade appears in your history. </Step> </Steps>

When you place an order, it receives one of these statuses:

| Status      | Description                                                                                                             | | ----------- | ----------------------------------------------------------------------------------------------------------------------- | | `live`      | Order is resting on the book                                                                                            | | `matched`   | Order matched immediately                                                                                               | | `delayed`   | Marketable order accepted into an asynchronous delay window on configured seconds-delay markets, such as sports markets | | `unmatched` | Marketable order placed on the book after the delay expired without a match                                             |

After matching, trades progress through these statuses:

| Status      | Terminal | Description                                            | | ----------- | -------- | ------------------------------------------------------ | | `MATCHED`   | No       | Trade matched, sent to executor for onchain submission | | `MINED`     | No       | Transaction mined into the blockchain                  | | `CONFIRMED` | Yes      | Trade achieved finality, successful                    | | `RETRYING`  | No       | Transaction failed, being retried                      | | `FAILED`    | Yes      | Trade failed permanently                               |

| Role      | Description                     | When                                                  | | --------- | ------------------------------- | ----------------------------------------------------- | | **Maker** | Adds liquidity to the book      | Your order rests and is later matched                 | | **Taker** | Removes liquidity from the book | Your order matches immediately against resting orders |

Price improvement always benefits the taker. If you place a buy order at `$0.55` and it matches against a resting sell at `$0.52`, you pay `$0.52`.

You can cancel orders at any time before they're matched via the CLOB API, except while a marketable order is in a pending delay window.

Partial fills cannot be cancelled: only the unfilled portion of an order can be cancelled.

Before placing orders, ensure:

| Requirement         | Description                                        | | ------------------- | -------------------------------------------------- | | **Balance**         | Sufficient pUSD (for buys) or tokens (for sells)   | | **Allowance**       | Approve the Exchange contract to spend your assets | | **API Credentials** | Valid API key for authenticated endpoints          |

<Info> Order size is limited by your available balance minus any amounts reserved by existing open orders.

$$ \text{maxOrderSize} = \text{balance} - \sum(\text{openOrderSize} - \text{filledAmount}) $$ </Info>

<CardGroup cols={2}> <Card title="Resolution" icon="gavel" href="/concepts/resolution"> Learn how markets are resolved and winning tokens redeemed. </Card>

<Card title="Trading Guide" icon="book" href="/trading/quickstart"> Start placing orders with our step-by-step guide. </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
* Token ID (which outcome you're trading)
* Side (buy or sell)
* Price and size
* Expiration time
* Timestamp (in milliseconds, used for order uniqueness)

You sign this order with your private key, creating an EIP712 signature.
```

Example 2 (text):
```text
* Signature is valid
* You have sufficient balance
* You have set the required allowances
* Price meets minimum tick size requirements
```

Example 3 (text):
```text
* **Taker delay:** used on selected crypto and finance up/down markets. The order is held for 250 ms, then validation runs again and the order is matched or placed on the book. The API waits for this hold and returns the final order result. To check a specific market, call the public CLOB endpoint `GET https://clob.polymarket.com/clob-markets/{condition_id}` and look for `itode: true`.
* **Sports/game delay:** enabled on configured sports markets around live game conditions. The order waits for the market's configured delay window before matching.

During either delay, the order is pending and cannot be canceled. If the market, balance, allowance, or risk checks fail when the delay expires, the order is rejected instead of matching.

**If the order is not marketable**, it rests on the book waiting for a counterparty. It remains open until:

* Another order matches against it
* You cancel it
* It expires (GTD orders only)
```

Example 4 (text):
```text
* Verifies both signatures
* Transfers tokens from seller to buyer
* Transfers pUSD from buyer to seller

Settlement is **atomic**: either the entire trade succeeds or nothing happens.
```

---

## Predictions Changelog

**URL:** https://docs.polymarket.com/changelog/predictions.md

<Update label="Sep 15, 2026" description="PolyBolt WebSocket: real-time prices on one socket">

<Update label="Sep 4, 2026" description="Data API v2 release">

<Update label="Aug 17, 2026" description="Crypto taker delay reduced to 50ms">

<Update label="Aug 14, 2026" description="5-minute crypto markets moved to a 60-second Chainlink TWAP">

<Update label="Aug 10, 2026" description="Data API: per-outcome redemption activity, position fee basis fields, and event artwork fallback">

<Update label="Aug 7, 2026" description="Chainlink TWAP resolution for crypto up/down markets">

<Update label="Jul 17, 2026" description="Latency improvements and order response changes — Friday July 24, 04:00 UTC">

<Update label="Jul 14, 2026" description="Relayer: deprecating CLOB v1 Neg Risk Adapter">

<Update label="Jul 10, 2026" description="Sports taker fee and maker rebate update">

<Update label="Jul 2, 2026" description="World Cup markets decimalized to a 0.0025 (0.25¢) tick size">

<Update label="Jun 25, 2026" description="Bridge API: optional X-Builder-Code header">

<Update label="Jun 15, 2026" description="CLOB DELETE /orders maximum batch size reduced to 1000">

<Update label="Jun 1, 2026" description="Increased CLOB order rate limits"> Raised burst and sustained rate limits for several CLOB trading endpoints.

See [Rate Limits](/api-reference/rate-limits) for the full table. </Update>

<Update label="May 18, 2026" description="Data API: builderCode added to /v1/builders/leaderboard and /v1/builders/volume">

<Update label="May 14, 2026" description="GET /markets/keyset maximum limit reduced to 100">

<Update label="Apr 28, 2026" description="CLOB V2 is live on production"> Polymarket's CLOB V2 upgrade is live on `https://clob.polymarket.com`.

<Update label="Apr 21, 2026" description="Relayer API: POST /submit returns immediately without transactionHash">

<Update label="Apr 17, 2026" description="CLOB V2: upgrades go live April 28 at ~11:00 UTC, with ~1 hour of downtime"> Polymarket is shipping a coordinated upgrade: **new Exchange contracts, a rewritten CLOB backend, and a new collateral token (pUSD)**.

**Exchange upgrades go live April 28, 2026 at \~11:00 UTC with \~1 hour of downtime.** All integrations must migrate to the V2 SDK before the cutover — there will be no backward compatibility after go-live.

**Full walkthrough:** [Migrating to CLOB V2](/v2-migration). Follow [Discord](https://discord.gg/polymarket), Telegram, and [status.polymarket.com](https://status.polymarket.com) for the exact start time.

**Historical pre-cutover note:** before go-live, integrations could test against `https://clob-v2.polymarket.com`. As of April 28, V2 runs on `https://clob.polymarket.com`.

**What you need to do**

**During the window:** Trading will be paused for \~1 hour on April 28 starting around 11:00 UTC. The SDK's hot-swap mechanism will auto-refresh the client when V2 goes live — no manual action needed if you're on the latest SDK. </Update>

<Update label="Apr 13, 2026" description="Bridge API: added support link for bridging issues">

<Update label="Apr 10, 2026" description="New keyset pagination endpoints for markets and events">

<Update label="Apr 9, 2026" description="GET /markets: closed defaults to false">

<Update label="April 8, 2026" description="Increased API Rate Limits"> Increased burst and sustained rate limits for several CLOB trading endpoints.

See [Rate Limits](/api-reference/rate-limits) for the full table. </Update>

<Update label="Mar 31, 2026" description="REST API Fee Fields Update">

<Update label="Mar 30, 2026" description="Fee Structure V2">

<Update label="Mar 17, 2026" description="March Madness: $2M+ in Liquidity Rewards">

**Daily reward rates for markets (subject to change):**

**48 hours before GameStartTime:**

**From game live to game completion (note: rewards are expressed in daily rates):**

**From game live to halftime (note: rewards are expressed in daily rates):**

<Update label="Mar 1, 2026" description="Taker Fees & Maker Rebates: All Crypto Markets">

<Update label="Feb 12, 2026" description="5-Minute Crypto Markets">

<Update label="Feb 11, 2026" description="Taker Fees & Maker Rebates: NCAAB and Serie A">

<Update label="Jan 28, 2026" description="Bridge API: Withdrawal Endpoint">

<Update label="Jan 16, 2026" description="Docs Update: RTDS documentation">

<Update label="Jan 16, 2026" description="Docs Update: Maker Rebates Program">

<Update label="Jan 6, 2026" description="New API Features">

<Update label="Jan 5, 2026" description="Taker Fees & Maker Rebates">

<Update label="Sept 24, 2025" description="Polymarket Real-Time Data Socket (RTDS) official release">

<Update label="September 15, 2025" description="WSS price_change event update">

<Update label="August 26, 2025" description="Updated /trades and /activity endpoints">

<Update label="August 21, 2025" description="Batch Orders Increase">

<Update label="July 23, 2025" description="Get Book(s) update">

<Update label="June 3, 2025" description="New Batch Orders Endpoint">

<Update label="June 3, 2025" description="Change to /data/trades">

<Update label="May 28, 2025" description="Websocket Changes">

<Update label="May 28, 2025" description="New FAK Order Type"> We’re excited to introduce a new order type soon to be available to all users: Fill and Kill (FAK). FAK orders behave similarly to the well-known Fill or Kill (FOK) orders, but with a key difference:

<Update label="May 15, 2025" description="Increased API Rate Limits"> All API users will enjoy increased rate limits for the CLOB endpoints.

**Examples:**

Example 1 (text):
```text
For complete documentation, see [Market Data](/market-data/overview).
```

Example 2 (text):
```text
* Please see [Real-Time Data](/market-data/realtime-data) for details.
```

Example 3 (text):
```text
* `limit`: 500
* `offset`: 1,000
```

Example 4 (text):
```text
* `min_order_size`
  * type: string
  * description: Minimum price increment.
* `neg_risk`
  * type: boolean
  * description: Boolean indicating whether the market is neg\_risk.
* `tick_size`
  * type: string
  * description: Minimum price increment.
```

---

## Polymarket USD

**URL:** https://docs.polymarket.com/concepts/pusd.md

**Contents:**
- Why pUSD
- Key facts
- Wrapping — USDC.e → pUSD
  - Example
- Unwrapping — pUSD → USDC.e
- Next steps

**pUSD** (Polymarket USD) is the collateral token used for all trading on Polymarket. It's a standard ERC-20 token on Polygon, backed by USDC. The smart contract — which enables the withdrawal functionality — enforces the backing. No algorithmic peg, no fractional reserve.

<Note> **Day to day, nothing changes.** You load funds, see a balance, trade, and withdraw. pUSD is the technical settlement layer underneath the same experience you're used to. </Note>

The protocol settles all trading activity in native USDC, providing a more capital efficient, scalable, and institutionally aligned settlement standard as the platform continues to grow.

pUSD is a standard ERC-20 wrapper that represents a USDC claim. Wrapping and unwrapping are enforced onchain by the `CollateralOnramp` and `CollateralOfframp` contracts.

|                |                         | | -------------- | ----------------------- | | Token standard | ERC-20                  | | Network        | Polygon mainnet         | | Decimals       | 6                       | | Backing        | USDC (enforced onchain) | | Transferable   | Yes — standard ERC-20   |

pUSD is designed to function within Polymarket. There are no current plans to list it on external exchanges.

See the [Contracts](/resources/contracts) page for all collateral-related contract addresses.

Use the **CollateralOnramp** to wrap USDC.e into pUSD.

import { createWalletClient, createPublicClient, http, parseAbi, parseUnits, } from "viem"; import { polygon } from "viem/chains"; import { privateKeyToAccount } from "viem/accounts";

const account = privateKeyToAccount(process.env.PRIVATE_KEY as `0x${string}`); const walletClient = createWalletClient({ account, chain: polygon, transport: http() }); const publicClient = createPublicClient({ chain: polygon, transport: http() });

const ONRAMP = "0x93070a847efEf7F70739046A929D47a521F5B8ee" as const; const USDCE = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174" as const; // USDC.e on Polygon

const amount = parseUnits("100", 6); // 100 USDC.e

// 1. Approve the Onramp to spend your USDC.e const approveHash = await walletClient.writeContract({ address: USDCE, abi: parseAbi(["function approve(address spender, uint256 amount) returns (bool)"]), functionName: "approve", args: [ONRAMP, amount], }); await publicClient.waitForTransactionReceipt({ hash: approveHash });

// 2. Wrap USDC.e → pUSD const wrapHash = await walletClient.writeContract({ address: ONRAMP, abi: parseAbi(["function wrap(address *asset, address *to, uint256 _amount)"]), functionName: "wrap", args: [USDCE, account.address, amount], }); await publicClient.waitForTransactionReceipt({ hash: wrapHash });

Use the **CollateralOfframp** to unwrap pUSD back into USDC.e.

<CardGroup cols={2}> <Card title="Contracts" icon="file-contract" href="/resources/contracts"> All Polymarket contract addresses and audits </Card>

<Card title="Bridge" icon="arrow-right-arrow-left" href="/trading/bridge/deposit"> Deposit from other chains — auto-wraps to pUSD </Card> </CardGroup>

**Examples:**

Example 1 (text):
```text
function wrap(address _asset, address _to, uint256 _amount) external
```

Example 2 (text):
```text
  from web3 import Web3

  ONRAMP = "0x93070a847efEf7F70739046A929D47a521F5B8ee"
  USDCE = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"

  amount = 100 * 10**6  # 100 USDC.e

  # 1. Approve the Onramp to spend your USDC.e
  usdce = w3.eth.contract(address=USDCE, abi=[{
      "name": "approve", "type": "function",
      "inputs": [{"name": "spender", "type": "address"},
                 {"name": "amount", "type": "uint256"}],
      "outputs": [{"type": "bool"}],
  }])
  usdce.functions.approve(ONRAMP, amount).transact({"from": address})

  # 2. Wrap USDC.e → pUSD
  onramp = w3.eth.contract(address=ONRAMP, abi=[{
      "name": "wrap", "type": "function",
      "inputs": [{"name": "_asset", "type": "address"},
                 {"name": "_to", "type": "address"},
                 {"name": "_amount", "type": "uint256"}],
      "outputs": [],
  }])
  onramp.functions.wrap(USDCE, address, amount).transact({"from": address})
```

Example 3 (text):
```text
function unwrap(address _asset, address _to, uint256 _amount) external
```

---

## Builder Fees

**URL:** https://docs.polymarket.com/programs/builders/fees.md

**Contents:**
- How It Works
- Registration
  - Fee Rate Limits
  - Rate Change Policy
- Fee Calculation
  - Platform Fees
  - Builder Fees
  - Balance Checks
- Onchain Attribution
  - V2 Order Struct

CLOB V2 introduces a fee layer that lets builders earn a fee on every order routed through their application. When a builder attaches their unique **builder code** to an order and that order matches, a **builder fee** is collected alongside any platform fee.

Builder fees are flat percentages of trade notional, configured by each builder within enforced limits. They're additive — they stack on top of platform fees, never replace them.

<Note> New to the Builder Program? Start with [Builder Program](/programs/builders/overview). This page covers the fee layer specifically. </Note>

<Frame> <img src="https://mintcdn.com/polymarket-292d1b1b/lWwKl4XdsXxYugaA/images/core-concepts/builder-fee.png?fit=max&auto=format&n=lWwKl4XdsXxYugaA&q=85&s=9287dc95f24f07bcb9f33c4d7d6ed0f2" alt="" className="dark:hidden" width="2068" height="952" data-path="images/core-concepts/builder-fee.png" />

<img src="https://mintcdn.com/polymarket-292d1b1b/lWwKl4XdsXxYugaA/images/dark/core-concepts/builder-fee.png?fit=max&auto=format&n=lWwKl4XdsXxYugaA&q=85&s=31b5e9be53b16738ad9f2b833b1eb02a" alt="" className="hidden dark:block" width="2068" height="952" data-path="images/dark/core-concepts/builder-fee.png" /> </Frame>

Builder fees and platform fees are independent. What the user pays depends on the market config and whether a builder code is attached:

| Market               | Builder code attached | User pays                  | | -------------------- | --------------------- | -------------------------- | | No platform fee      | No                    | Nothing                    | | No platform fee      | Yes                   | Builder fee only           | | Platform fee enabled | No                    | Platform fee only          | | Platform fee enabled | Yes                   | Platform fee + builder fee |

Builder fees never replace platform fees — they're always additive.

<Warning> Polymarket reserves the right to revoke your ability to charge a builder fee in its sole discretion, for any reason or no reason, including but not limited to instances where fees are determined to have been collected through fraudulent, deceptive, misleading, automated, self-referred, or other non-bona fide trading activity. </Warning>

Register for a builder code through your Polymarket account.

<Steps> <Step title="Create a Builder Profile"> Open polymarket.com → Settings → [Builders](https://polymarket.com/settings?tab=builder) and set up your builder profile. </Step>

<Step title="Set Your Fee Rates"> Configure two rates on your profile:

<Step title="Copy Your Builder Code"> Your profile is assigned a `bytes32` builder code. [Attach it to every order you submit](/trading/place-orders#builder-attribution). </Step> </Steps>

| Parameter      | Default    | Maximum       | | -------------- | ---------- | ------------- | | Taker fee rate | 0 bps (0%) | 100 bps (1%)  | | Maker fee rate | 0 bps (0%) | 50 bps (0.5%) | | Granularity    | —          | 1 bp (0.01%)  |

Fee rate changes are gated so users can see them coming:

Platform fees use a dynamic per-market formula:

Where `C` is the trade size, `p` is the order price, and `feeRate` is a per-market parameter. Platform fees are currently taker-only and are not configurable by builders.

Builder fees are a flat percentage of notional:

**Example.** A 1,000 pUSD taker buy routed through a builder charging 100 bps (1%) taker fee:

The maker and taker sides of a single trade can have different builder codes and different rates. If Builder A (0.3% maker) posts the resting order and Builder B (0.8% taker) submits the matching order, each earns their respective fee from their respective side.

The account must have enough pUSD to cover the trade and all applicable platform and builder fees. For market buys, [set an all-in spending limit](/trading/place-orders#cap-market-buy-spending) so the order amount is adjusted for fees before signing.

Builder attribution is part of the signed V2 order struct — not an offchain label. The `builder` field appears in every `OrderFilled` event emitted by the CTF Exchange V2 contract.

The `builder` field is a `bytes32` matching your registered builder code.

When a user places an order with your `builderCode` attached:

Collected builder fees are distributed to the wallet associated with your builder profile.

Polymarket may disable a builder code at any time — for violations of the Builder Program terms, abusive fee practices, or platform integrity concerns. Orders carrying a disabled code will be rejected by the CLOB.

Builder profiles and fee rates are publicly queryable. This is intentional — it lets users and third parties see what a builder charges before using their app.

**Examples:**

Example 1 (text):
```text
* **Taker Fee Rate** — charged on taker orders routed through your app
* **Maker Fee Rate** — charged on maker orders routed through your app
```

Example 2 (text):
```text
platform_fee = C × feeRate × p × (1 - p)
```

Example 3 (text):
```text
builder_fee = notional × builder_fee_rate_bps / 10000
```

Example 4 (text):
```text
builder_fee = 1000 × 100 / 10000 = 10 pUSD
```

---

## Referral Program

**URL:** https://docs.polymarket.com/programs/referral-program.md

**Contents:**
- Eligibility
- How to Refer
- Rewards
  - The Caps
  - Example
- Payouts
- Notes
- FAQ

<Note> These updated Referral Program terms take effect on **Thursday, May 28, 2026**. </Note>

Refer traders to Polymarket and earn a share of the net trading fees they generate, paid every day in pUSD.

To start earning, you need at least **\$10,000** in lifetime trading volume on Polymarket.

Share any market or profile page using the share button on that page. When someone clicks your link and signs up, they become your referral.

To count, a new user must sign up within **30 days** of clicking your link.

You earn a share of the **net** trading fees your referrals generate.

| Type              | Reward                      | | ----------------- | --------------------------- | | Direct referral   | **10%** of net trading fees | | Indirect referral | **5%** of net trading fees  |

<Note> Net trading fees are what Polymarket keeps after the referred user's own tier rebate. The more rebate they earn, the more of their fees go back to them rather than into your referral reward. </Note>

Referral rewards are bounded two ways. Rewards on a referral end at whichever of these comes first:

You refer a new trader. From their very first trade and through every tier up to **Gold**, you earn **10%** of the net fees from their trades, paid daily. If they trade actively early on, this is when you earn the most. Your rewards on that referral end once they reach **Platinum** or hit 30 days, whichever happens first.

<AccordionGroup> <Accordion title="Who can earn referral rewards"> Any Polymarket user with at least \$10,000 in lifetime trading volume. You can share links before reaching the threshold, but rewards only begin once you cross it. </Accordion>

<Accordion title="What is the difference between direct and indirect referrals"> A direct referral is someone you personally refer. An indirect referral is someone referred by one of your referrals. You earn 10% of net fees from direct referrals and 5% from indirect referrals. </Accordion>

<Accordion title="What does net fees mean"> Net fees are what Polymarket keeps after the referred user's own tier rebate. Your referral reward is a percentage of that net amount. </Accordion>

<Accordion title="When do my referral rewards stop"> Rewards on a referral start with their first trade and end at whichever of these comes first: the referral reaches the Platinum tier, or 30 days from their sign-up. </Accordion>

<Accordion title="When am I paid"> Rewards are paid once a day at midnight UTC in pUSD, directly to your account. </Accordion>

<Accordion title="What is not allowed"> Self-referrals, referring accounts you control, and inauthentic trading are not allowed. Polymarket may disqualify referrals and claw back rewards for activity that breaks the Terms of Service. </Accordion>

<Accordion title="Are third-party integrations using omnibus wallets eligible"> No. Third-party integrations using omnibus wallets are not eligible for the Referral Program. </Accordion> </AccordionGroup>

---

## SDK Changelog

**URL:** https://docs.polymarket.com/changelog/sdks.md

<Tabs> <Tab title="TypeScript">

<Tab title="Python">

**Examples:**

Example 1 (python):
```python
* Added authenticated PolyBolt crypto, 60-second TWAP, and equity price streams through `SecureClient.subscribe(...)`, with history snapshots, exact decimal prices, shared connections, and automatic reconnects. Use `prices.crypto`, `prices.crypto.twap`, or `prices.equity`; crypto symbols must be canonical USD pairs such as `btcusd`. Rejections expose a machine-readable `RequestRejectedError.code`. Event sequence numbers are scoped to each channel and connection and reset on reconnect. Legacy price topics remain deprecated, with removal planned one month after this release. Migrating Binance prices changes USDT quotes to USD; 30-second TWAP has no replacement. See the [SDK migration guide](/migrate/rtds-to-polybolt#migrate-sdks-to-polybolt).

Given an authenticated `SecureClient`, migrate a crypto subscription as follows:

```diff theme={null}
const stream = await client.subscribe([
-  { topic: "prices.crypto.chainlink", symbols: ["btc/usd"] },
+  { topic: "prices.crypto", symbols: ["btcusd"] },
]);
```

* Added explicit `EIP712Domain` types to authentication, Deposit Wallet order and batch, and Perps signing payloads for signers that require complete typed data.
* Exported `OrderPostStatus` from `@polymarket/client` so callers can compare accepted order statuses without importing the bindings package.

### `0.10.0`

* Breaking change: trade, activity, position, and Combo feeds now use server cursors and automatically retry transient rate limits. Restart scans with a new first page; previously saved cursors are not reusable. Replace `market` filters with `conditionId` and top-level `start`/`end` with `window`. Time windows accept epoch seconds or `Date` values; `window: "full"` requests full history. Condition filters accept at most 20 distinct IDs.

```diff theme={null}
const pages = client.listActivity({
  user,
-  market: [conditionId],
-  start,
-  end,
+  conditionId: [conditionId],
+  window: { start, end },
});
```

* Breaking change: `listPositions(...)` now covers open, redeemable, and closed positions. Replace `listClosedPositions(...)` with `status: PositionStatus.Closed`, and `listMarketPositions(...)` with a public client's `listPositions({ conditionId })`. Market-holder results are individual positions rather than groups by outcome. The default `Open` status includes redeemable positions.

```diff theme={null}
+import { PositionStatus } from "@polymarket/client";

-const pages = client.listClosedPositions({ user });
+const pages = client.listPositions({ user, status: PositionStatus.Closed });
```

* Breaking change: secure `listPositions(...)` always selects the authenticated wallet and rejects `user: null`. Use a public client to list a market's holders.

```diff theme={null}
-const pages = secureClient.listPositions({ user: null, market: [conditionId] });
+const pages = publicClient.listPositions({ conditionId });
```

* Breaking change: position rows expose `currentSize`, `currentPrice`, `totalSize`, and explicit fee-exclusive entry economics. Money, size, price, and PnL values use decimal strings; `entryFeesUsdc` is disclosed separately and must not be deducted from `entryCostUsdc` again. Optional feed metadata now uses `undefined` for absent values, and returned timestamps use epoch milliseconds.

```diff theme={null}
-const shares = position.size;
-const price = position.curPrice;
-const bought = position.totalBought;
+const shares = position.currentSize;
+const price = position.currentPrice;
+const bought = position.totalSize;
```

* Breaking change: request vocabularies now use exported enums, including `SortDirection`, `TradeFilterType`, `PositionFilterType`, `PositionSortBy`, `ComboPositionSortBy`, and `TipSide`. Replace the removed `Side` type with `OrderSide`.

```diff theme={null}
-import type { Side } from "@polymarket/client";
+import { OrderSide } from "@polymarket/client";

-const side: Side = "BUY";
+const side = OrderSide.BUY;
```

* Added migration activity through `ActivityType.MIGRATION` and `MigrationActivity`, plus tip activity through `ActivityType.TIP` and `TipSide`. Combo positions now support `ComboPositionStatus.Redeemable` as a sole status filter.
* Breaking change: Combo activity includes `positionId` on every row and removes `transactionAt`, `logIndex`, and `moduleId`. Use `timestamp` for the activity time.

```diff theme={null}
-const occurredAt = activity.transactionAt;
+const occurredAt = activity.timestamp;
```

* Breaking change: `listMarketHolders(...)` now returns a paginator. Pass `conditionIds` and `pageSize`; `minBalance` is measured in display shares. Optional `includePnl` adds gross holdings and position economics for one condition ID with a page size of at most 100. Merge outcome groups across pages by `assetId`.

```diff theme={null}
-const holders = await client.listMarketHolders({ market: [conditionId], limit: 10 });
+const pages = client.listMarketHolders({ conditionIds: [conditionId], pageSize: 10 });
+const firstPage = await pages.firstPage();
+const holders = firstPage.items;
```

* Breaking change: `fetchPortfolioValue(...)` returns one `PortfolioValue` with a decimal-string `value`, and accepts `conditionIds` instead of `market`. Position and portfolio reads also canonicalize Polymarket Protocol V2 condition IDs.

```diff theme={null}
-const [portfolio] = await client.fetchPortfolioValue({ user, market: [conditionId] });
+const portfolio = await client.fetchPortfolioValue({ user, conditionIds: [conditionId] });
```

* Added `fetchUserStats(...)`, `fetchUserPnl(...)`, and `fetchUserVolume(...)` for account analytics, with authenticated-wallet defaults on secure clients. Breaking change: replace `fetchTradedMarketCount(...)` with the exact distinct-market count on `fetchUserStats(...)`. It returns `null` for an unknown user.

```diff theme={null}
-const count = (await client.fetchTradedMarketCount({ user })).traded;
+const stats = await client.fetchUserStats({ user });
+const count = stats?.tradedMarketCount ?? null;
```

* Breaking change: replace `fetchPriceHistory(...)` with cursor-paginated `listPriceHistory(...)`. Pass `assetId` and exactly one time selection: `interval`, `start` with optional `end`, or `asOf`. Replace minute-based `fidelity` with `bucketSeconds`; omit it for automatic resolution. Explicit ranges span at most 15 days. Each point includes a decimal-string price, epoch-millisecond timestamp, and `resolutionSeconds`.

```diff theme={null}
+import { PriceHistoryInterval } from "@polymarket/client";

-const history = await client.fetchPriceHistory({ assetId, interval: "1d", fidelity: 60 });
+const pages = client.listPriceHistory({
+  assetId,
+  interval: PriceHistoryInterval.OneDay,
+  bucketSeconds: 3600,
+});
+const firstPage = await pages.firstPage();
+const history = firstPage.items;
```

* Breaking change: replace `listOpenInterest(...)` with `fetchOpenInterest(...)` and pass `conditionIds` for selected markets. Values represent priced gross open interest in USDC.

```diff theme={null}
-const openInterest = await client.listOpenInterest({ market: [conditionId] });
+const openInterest = await client.fetchOpenInterest({ conditionIds: [conditionId] });
```

* Breaking change: `fetchEventLiveVolume(...)` accepts `eventIds` and returns cumulative taker volume in shares, with market rows in `markets` and a decimal-string `takerVolumeTotal`.

```diff theme={null}
-const volume = await client.fetchEventLiveVolume({ id: eventId });
+const volume = await client.fetchEventLiveVolume({ eventIds: [eventId] });
```

* Breaking change: builder rankings now return cursor-paginated `BuilderStanding` rows. Builder volume returns complete `BuilderVolumePoint` date buckets; `bucketLimit` bounds buckets rather than builder rows. Replace `timePeriod` with `window` for rankings or `interval` for volume. Use `BuilderVolumeInterval.Year` for yearly buckets.

```diff theme={null}
+import { BuilderVolumeInterval, LeaderboardWindow } from "@polymarket/client";

-const pages = client.listBuilderLeaderboard({ timePeriod: "MONTH" });
-const volume = await client.fetchBuilderVolume({ timePeriod: "MONTH" });
+const pages = client.listBuilderLeaderboard({ window: LeaderboardWindow.Month });
+const volume = await client.fetchBuilderVolume({ interval: BuilderVolumeInterval.Month });
```

* Breaking change: trader rankings use cursor pagination, `window`, and `sortBy`; the list no longer accepts `user` or `userName` filters. Use `fetchTraderLeaderboardStanding({ user })` for one wallet's standing. Added `listBiggestWinners(...)` with market and Combo variants.

```diff theme={null}
+import { LeaderboardWindow, TraderLeaderboardSort } from "@polymarket/client";

-const pages = client.listTraderLeaderboard({ timePeriod: "MONTH", orderBy: "PNL" });
+const pages = client.listTraderLeaderboard({
+  window: LeaderboardWindow.Month,
+  sortBy: TraderLeaderboardSort.Pnl,
+});
```

* Added `fetchResolutions(...)` for resolution lifecycle lookups by question, condition, or event, with typed timestamps, transaction metadata, payouts, and finality. Unset values are omitted.
* Combo leg markets now preserve `question`, `groupItemTitle`, `sportsMarketType`, `line`, and `outcomes`. Trade activity tolerates unknown outcome metadata.

### `0.9.0`

* Order estimation, preparation, creation, and placement now accept protocol-neutral `assetId` values. Structured Polymarket Protocol V2 position IDs select Polymarket Protocol V2 routing automatically, while `tokenId` remains available as a deprecated alias.
* Added `fetchTradingApprovalsState(...)` for reading a wallet's missing trading approvals without a signer or transaction workflow. Malformed approval-check responses now raise `UnexpectedResponseError`.
* Markets and events now expose their protocol through `version`, and markets expose Combo eligibility through `market.state.comboStatus`. Combo status values introduced after this release pass through as strings.
* Secure account reads now reject invalid request values and `user: null` with `UserInputError` instead of silently selecting the wallet or throwing an untyped error.
* Session Key authorization and revocation submissions now allow up to five minutes for relayer validation and broadcast.
* Breaking change: `revokeSessionKey(...)` now resolves to `void` once the Session Key leaves the active registry. The backend continues canceling orders and finalizing the on-chain revocation asynchronously. See [Revoke a Session Key](/trading/session-keys#revoke-a-session-key).

```diff theme={null}
-const revocation = await secureClient.revokeSessionKey({
+await secureClient.revokeSessionKey({
  address: sessionKeyAddress,
});
```

* Team entries on event and team-list responses now preserve their `ordering` value.
* Breaking change: removed legacy AMM fields from market and event models, along with the `marketMakerAddresses` filter on `listMarkets(...)`. Responses that still contain the removed fields continue to parse, but those values are ignored. Use the supported CLOB metrics where applicable.

```diff theme={null}
-const volume = market.metrics.volumeAmm;
+const volume = market.metrics.volumeClob;
```

### `0.8.1`

* `client.authorizeSessionKey(...)` no longer accepts `validUntil`. This is a breaking change. Each Session Key authorization expires after 180 days. Revoke a Session Key to end access sooner.

```diff theme={null}
const authorization = await client.authorizeSessionKey({
  address: sessionKeyAddress,
-  validUntil: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),
});
```

### `0.8.0`

* Added protocol-neutral `assetId` and `conditionId` fields to CLOB reads, filters, realtime events, and Data API responses. The deprecated `tokenId`, `tokenIds`, and `market` aliases still work.
* Position lifecycle methods now split, merge, and redeem ordinary Polymarket Protocol V2 positions. Redemption by position ID supports binary, negative-risk, and Combo positions.
* `setupTradingApprovals()` and `prepareTradingApprovals()` now include the Polymarket Protocol V2 binary and negative-risk modules.
* Combo market discovery now exposes whether a market is `pending` and excludes pending markets when selecting live RFQ legs.
* Live volume reads now return `null` for empty market identifiers.
* Renamed the low-level CTF and Router transaction builders and their error guards to contract-specific names. This is a breaking change for callers that import them directly.

```diff theme={null}
import {
-  mergePositionsCall,
-  mergeV2Call,
-  redeemV2Call,
-  splitPositionCall,
-  splitV2Call,
+  ctfMergePositionsCall,
+  ctfSplitPositionCall,
+  routerMergeCall,
+  routerRedeemCall,
+  routerSplitCall,
} from "@polymarket/client";
```

### `0.7.0`

* Added scoped Deposit Wallet session keys through `client.authorizeSessionKey(...)`, `client.fetchSessionKeys()`, and `client.revokeSessionKey(...)`. Secure clients can use an authorized session signer for ordinary operations. Scopes default to `ALL`; known scopes are enumerated while newer scope strings remain usable.
* Account notifications now use a `NotificationType`-discriminated union with a typed payload for every supported kind. `fetchNotifications(...)` omits kinds unknown to this SDK version and rejects a response when a recognized kind has a malformed payload.
* `RateLimitError.rateLimit` now carries the `Poly-RateLimit-*` state returned with a rejection. Pass `onRateLimitUpdate` when creating a client to receive per-signer bucket, remaining, reset, tier, and warning updates from any response that reports them.
* Order estimation, preparation, creation, and placement now accept Polymarket Protocol V2 position IDs and route them through Exchange V3 signing and trading approvals. Existing token-ID orders remain supported.
* `listComboPositions(...)` now accepts either one status or an array of statuses.
* `RequestRejectedError.restriction` distinguishes matching-engine restarts from post-only mode, and `retryAfter` falls back to the response body's `retry_after_seconds` value when the header is absent. Batch post-only rejections now use the `post_only_mode` order error code.
* Order preparation now tolerates insignificant floating-point drift on valid tick-grid prices and uses exact fixed-point amount calculations. CLOB salts that cannot round-trip through a JavaScript number are rejected before submission.
* Breaking change: deprecated `CtfConditionId` type, use ConditionId\` instead.

```diff theme={null}
-import type { CtfConditionId } from "@polymarket/client";
+import type { ConditionId } from "@polymarket/client";
```

### `0.6.0`

* Added requester-side Combos RFQ support through `client.requestComboQuote(...)`, `client.acceptComboQuote(...)`, and `client.waitForComboFill(...)`. You can also call `fetchRfqStatus` from `@polymarket/client/actions`. Authenticate requests with `builderApiKey(...)` or `remoteBuilderSigning(...)`. Winning quotes can be stored as JSON, and SELL quotes include the exact post-fee `netReceive`. No-quote, decline, and expiry outcomes return values. Gateway rejections throw `RfqRequestRejectedError`.
* Market outcomes now include a nullable Polymarket Protocol V2 `positionId` alongside the CLOB `tokenId`. New code should use the protocol-neutral `ConditionId`, `ConditionIdSchema`, `OptionalConditionIdSchema`, and `toConditionId`. The CTF-named aliases and market-level `positionIds` array remain available for compatibility but are deprecated.
* Breaking change: `client.fetchLastTradePrice(...)` now returns `LastTradePrice | null`. It returns `null` when the token has not traded. `client.fetchLastTradePrices(...)` leaves untraded tokens out of the response, so match results by `tokenId` instead of array position.

```diff theme={null}
-const price = (await client.fetchLastTradePrice({ tokenId })).price;
+const lastTrade = await client.fetchLastTradePrice({ tokenId });
+const price = lastTrade?.price ?? null;
```

### `0.5.0`

* Added a Perps dead man's switch: `session.armAutoCancel()` schedules a one-shot cancel-all, `session.disarmAutoCancel()` clears it, and `session.fetchAutoCancelStatus()` reports the current deadline and daily trigger usage. Arming after the daily limit raises `AutoCancelDailyLimitError`.
* Perps funding history and realtime funding events now include a required `id`, typed as `PerpsFundingPaymentId`.
* Fixed `session.placeOrder()` missing private order updates that arrive before the command acknowledgement. When the caller omits a client order ID, the SDK now generates one before submitting the order.

### `0.4.0`

* Added `PerpsSession.updateMargin`, which adjusts isolated margin for an instrument position. Positive `amount` values add margin; negative values remove it.
* Repeated order preparation now caches market configuration and platform and builder fees. If cached tick data rejects a limit or protected market price, the SDK fetches current metadata once before returning the input error.
* Unprotected market orders now derive depth, price, tick size, and exchange selection from one live order book response. `maxSpend` remains an estimated all-in spend target based on recently resolved fees, not a hard cap.
* `AcceptedOrderResponse.orderId` is now typed as `OrderId`.
* Breaking TypeScript type change: `OrderBook.tickSize` is now a numeric `TickSizeValue` instead of a `DecimalString`.

```diff theme={null}
-const isOneCentTick = orderBook.tickSize === "0.01";
+const isOneCentTick = orderBook.tickSize === 0.01;
```

### `0.3.0`

* Added typed 30-second and 60-second Chainlink TWAP realtime subscriptions. `subscribe` validates subscription input when called: an unsupported TWAP window throws `UserInputError` before the connection opens.
* Added Perps account notifications: `session.listNotifications()`, `session.fetchUnreadNotificationsCount()`, `session.markNotificationsRead()`, and a `notifications` session WebSocket channel with typed `notification` events.
* Perps fills pagination now uses the API-native cursor and adds a `sort` direction option (newest first by default). Previously issued SDK-encoded fills cursors no longer work.
* Added the `DEPOSIT`, `WITHDRAWAL`, and `TAKER_REBATE` activity types. `listActivity` now returns all activity types by default, including deposits and withdrawals.
* `RequestRejectedError` and `RateLimitError` now expose `retryAfter` from the `Retry-After` response header.
* Fixes:
  * Open order `createdAt` and `expiresAt` now parse epoch-seconds wire timestamps correctly instead of treating them as milliseconds.
  * RFQ quote rejections now carry the granular Combos quote-validation error codes instead of a generic validation failure.
  * Deposit Wallet gasless and Collateral Return submits now self-heal nonce mismatches: when the relayer rejects a batch and reports the on-chain nonce, the SDK re-signs the batch with that nonce and resubmits it once.
  * Cursor-paginated reads no longer report the per-page item count as `Page.totalCount`. Use `page.items.length` instead.

### `0.2.0`

* Added `client.waitForOrderFillSettlement(order)`, which waits until every fill in an order response reaches a terminal settlement outcome and returns the settlement transaction hashes. Matched order responses are no longer guaranteed to include `transactionsHashes`; use this method to obtain hashes reliably.
* `ClobTrade.status` is now typed with the shared `TradeStatus` enum instead of a plain string.
* Added Collateral Return support: `planCollateralReturn` returns an inspectable plan and `executeCollateralReturnPlan` signs and submits it for Deposit Wallet, Safe, and Proxy accounts, returning a transaction handle.
* Added `isolatedOnly` to `PerpsInstrument`, indicating whether the instrument supports only isolated margin.
* Added volume-based fee tiers to the Perps fee schedule: each `PerpsFeeScheduleEntry` carries a `tiers` array of `PerpsFeeTier` values, including negative maker rebate rates.
* Perps withdrawal statuses are now forward-compatible: known statuses are enumerated in `PerpsKnownWithdrawalStatus`, which adds `failed`, and statuses introduced after a release flow through as plain strings instead of failing the response parse.
* Deprecated the `PerpsWithdrawalStatus` value alias; migrate enum member access:

```diff theme={null}
-if (withdrawal.status === PerpsWithdrawalStatus.Confirmed) {
+if (withdrawal.status === PerpsKnownWithdrawalStatus.Confirmed) {
```

* Fixed offset-paginated list methods silently stopping after the first page when `pageSize` reached the server's limit cap. `pageSize` is now validated per endpoint and values above the cap are rejected with `UserInputError`. A full page reports `hasMore: true`; when a collection ends exactly on a page boundary, the final page is empty.
* Limit and protected market order prices must be a multiple of the market tick size. Off-grid prices (for example `0.007` on a `0.005` tick market) are now rejected client-side instead of by the exchange after signing.

### `0.1.0`

* Graduated the SDK to the stable 0.x release line, marked Perps APIs as experimental, and removed deprecated compatibility APIs.
* Added Perps support for reduce-only orders, account stats, cancel-all, TP/SL metadata and placement, batched fill and trade frames, and stricter order request validation.
* Added `conditionId` aliases to CLOB order book, open order, trade, and builder trade models while keeping `market` available as a deprecated alias.
* Typed CLOB cancellation results with branded `OrderId` values for `canceled` and `notCanceled` keys.

### `0.1.0-beta.18`

* `setupTradingApprovals` and `prepareTradingApprovals` no longer request approvals for the retired CLOB v1 Neg Risk Adapter.
* Streams drop unknown or unreadable WebSocket frames instead of closing the connection. RFQ quoter sessions no longer fail with `TransportError` on an unrecognized frame; a caller waiting on an unreadable acknowledgement fails through its acknowledgement timeout instead.
* Removed `RfqKnownInboundMessageSchema` from `@polymarket/bindings`; each RFQ inbound message schema declares its own object shape directly.

### `0.1.0-beta.17`

* RFQ quoter sessions now keep running when the server introduces new error codes. `RfqErrorCode` is an open type: known codes are enumerated in `RfqKnownErrorCode`, and unrecognized codes flow through rejection errors as plain strings.
* Deprecated the `RfqErrorCode` value alias; migrate enum member access:

```diff theme={null}
-if (error.code === RfqErrorCode.RateLimited) {
+if (error.code === RfqKnownErrorCode.RateLimited) {
```

* Added `ConnectionLostError` carrying the WebSocket close `code` and `reason`. Losing an RFQ session connection now rejects in-flight operations and fails the session iterator with it, instead of ending the event loop silently. Closing the session still ends iteration cleanly.
* Streamed market and user events normalize empty-string optional decimal fields (for example a trade's `feeRateBps` or a price change's `bestBid` and `bestAsk`) to `null`.
* Batch price reads (`fetchPrices`, `fetchMidpoints`, `fetchSpreads`) return `TokenId`-keyed records of branded decimal strings.
* Perps sessions handle fills and trades frames that batch multiple entries.

### `0.1.0-beta.16`

* Added `RESOLVED_PARTIAL` to `ComboPositionStatus` so Combo positions that resolve at a fractional payout (for example a voided leg) parse correctly instead of failing validation.

### `0.1.0-beta.15`

* Combo activity now parses the canonical `type` field returned by the Data API, instead of deriving lifecycle actions from legacy fields.

### `0.1.0-beta.14`

* Added SDK pagination for Combo lifecycle activity and server-cursor pagination for Combo positions.
* Added Combo position sync request fields and exposed `outcome` and `redeemable` on Combo positions.
* Branded Combo activity row IDs.
* Breaking beta change: Combo activity and position fields now use `wallet`, `amount`, and `payout`; Combo activity rows no longer expose `moduleKind`.

```diff theme={null}
-activity.userAddress
-activity.amountUsdc
-redeemActivity.payoutUsdc
-position.userAddress
+activity.wallet
+activity.amount
+redeemActivity.payout
+position.wallet
```

### `0.1.0-beta.13`

* Added `listMarketClarifications` for reading market clarification text with SDK-owned pagination and market, event, state, question, and transaction filters.
* Fixed legacy Proxy wallet gasless execution and added live Safe and Proxy wallet coverage.
* Resolve closed markets when preparing market position redemptions.
* Gasless transaction handles now wait for relayer transactions to reach confirmed state before resolving.

### `0.1.0-beta.12`

* Require GTD limit order expirations to be at least 3 minutes in the future.

### `0.1.0-beta.11`

* Support CLOB order tick sizes `0.005` and `0.0025`.
* Pagination request cursors now infer the branded pagination cursor type.

### `0.1.0-beta.10`

* Preserve already-deployed legacy UUPS Deposit Wallets when `createSecureClient` resolves the default wallet, while new Deposit Wallet deployments use the beacon factory path.

### `0.1.0-beta.9`

* Added `PriceHistoryInterval` and `SearchSort` exports, preserved `groupItemTitle` on normalized markets, and published `expectPrivateKey` from `@polymarket/types`.

### `0.1.0-beta.8`

* RFQ quoter sessions now emit typed `trade` events for confirmed Combos fills.
* RFQ rejection errors now expose `errorId` values and parse `INVALID_SIGNATURE` and `INTERNAL_ERROR` codes.

### `0.1.0-beta.7`

* Added `parentEventId` to `Event` so child events can link back to their parent event.
* Added `maxPrice` and `minPrice` protection fields to market order requests.
* Handle legacy multi-outcome markets more safely: `listMarkets` skips markets that cannot be represented by the binary market model, and `fetchMarket` returns a typed SDK error for unsupported markets.
* Normalize empty-string order and activity fields to SDK values: decimal amounts become `"0"`, missing maker order fee rates become `null`, and missing trade or position market icons become `null`.
* Parse Combo trade activity rows with an `isCombo` discriminated union.
* Support new Combos RFQ websocket error codes for balance, allowance, and pre-execution reservation failures.
* Broad user websocket subscriptions now omit market filters so all-market streams receive trade events.
* Retry rejected JSON-RPC `eth_call` batches by splitting them into smaller batches.

### `0.1.0-beta.6`

* Point Combos RFQ endpoints at the production domains: `combos-rfq-api.polymarket.com` (REST) and `combos-rfq-gateway-quoter.polymarket.com` (quoter WebSocket).

### `0.1.0-beta.5`

* Added `listComboMarkets` for fetching the Combo market catalog with typed bindings and SDK-owned pagination. See [Combos](/trading/combos/overview).
* Parse RFQ quote rejections that use the `SUBMISSION_WINDOW_CLOSED` gateway error code.

### `0.1.0-beta.4`

* Added Combos support for multi-leg RFQ positions. See [Combos](/trading/combos/overview).
* Reject whitespace-only search queries and trim leading or trailing search input.
* `ConditionId` is now deprecated in favor of `CtfConditionId`; existing
  `ConditionId` exports remain available as deprecated aliases.

### `0.1.0-beta.3`

**Secure client setup now defaults to the Deposit Wallet flow**

`createSecureClient` can now derive and use the signer's deterministic Deposit
Wallet when you omit `wallet`. If you already know which Polymarket wallet you
want to use, keep passing `wallet`.

```diff theme={null}
const secureClient = await createSecureClient({
-  wallet: "YOUR_POLYMARKET_WALLET_ADDRESS",
   signer,
});
```

If you want to keep account selection explicit, no change is required:

```ts theme={null}
const secureClient = await createSecureClient({
  wallet: "YOUR_POLYMARKET_WALLET_ADDRESS",
  signer,
});
```

**`setupTradingApprovals()` now waits internally**

You no longer need to wait on the returned handle. Call the method once before
trading; it is safe to call again if approvals are already set.

```diff theme={null}
-const handle = await secureClient.setupTradingApprovals();
-await handle.wait();
+await secureClient.setupTradingApprovals();
```

**Gasless setup helpers are deprecated**

You no longer need to call `isGaslessReady()` or `setupGaslessWallet()` in the
normal setup path. Create the secure client, then set up trading approvals.

```diff theme={null}
-const ready = await secureClient.isGaslessReady();
-
-if (!ready) {
-  secureClient = await secureClient.setupGaslessWallet();
-}
-
 await secureClient.setupTradingApprovals();
```

### `0.1.0-beta.2`

First beta release of the unified TypeScript SDK. Install the beta package with
your package manager:

```bash theme={null}
pnpm add @polymarket/client@beta
```
```

Example 2 (python):
```python
* Added authenticated PolyBolt crypto, 60-second TWAP, and equity price streams through `AsyncSecureClient.subscribe(...)`, with history snapshots, exact decimal prices, automatic reconnects, typed price events, and isolated filter rejections. Use `CryptoPriceSpec`, `CryptoTwapPriceSpec`, or `EquityPriceSpec` from `polymarket.streams`; crypto symbols must be canonical USD pairs such as `btcusd`, while equity prices use the instrument's quote currency. Legacy price specs remain deprecated. Migrating Binance prices changes USDT quotes to USD; 30-second TWAP has no replacement. See the [SDK migration guide](/migrate/rtds-to-polybolt#migrate-sdks-to-polybolt).

Given an authenticated `AsyncSecureClient`, migrate a crypto subscription as follows:

```diff theme={null}
-from polymarket.streams import CryptoPricesSpec
+from polymarket.streams import CryptoPriceSpec

stream = await client.subscribe([
-    CryptoPricesSpec(topic="prices.crypto.chainlink", symbols=["btc/usd"]),
+    CryptoPriceSpec(symbols=["btcusd"]),
])
```

* Protected market BUY orders round shares so they can cross at `max_price` while preserving the cap across tick-size refinements. When rounding cannot preserve the cap, the SDK refreshes market metadata once before rejecting the order.
* `list_markets(...)` sorts `order="volume"` and `order="liquidity"` numerically. Previously saved cursors with these sort fields are incompatible; restart from the first page after upgrading.

```diff theme={null}
pages = client.list_markets(order="volume")
-page = await pages.from_cursor(saved_cursor).first_page()
+page = await pages.first_page()
```

### `0.10.0`

* Breaking change: trade, activity, position, and Combo reads now use server cursors. Restart scans from the first page when upgrading from `0.9.0`. Replace `market` filters with `condition_id`. Time bounds accept epoch seconds or timezone-aware `datetime` values. Use `full_history=True` without `start` or `end` to request full history. Position reads remain unbounded by default, including holdings without an activity timestamp.

```diff theme={null}
pages = client.list_activity(
    user=user,
-    market=[condition_id],
+    condition_id=[condition_id],
)
```

* Breaking change: `list_positions(...)` replaces `list_closed_positions(...)` and `list_market_positions(...)`. Use `status="CLOSED"` for closed positions and `status="REDEEMABLE"` for redeemable positions. For a market's holders, use a public client's `list_positions(condition_id=condition_id)`. Secure clients default to the authenticated wallet. Market position results are individual `Position` rows.

```diff theme={null}
-pages = client.list_closed_positions(user=user)
+pages = client.list_positions(user=user, status="CLOSED")
```

* Breaking change: position rows now expose `current_size`, `current_price`, `total_size`, and explicit entry costs and fees. Prices, sizes, PnL, and percentages use `Decimal`. `entry_cost_usdc` excludes fees. Do not subtract `entry_fees_usdc` from it again.

```diff theme={null}
-shares = position.size
-price = position.cur_price
-bought = position.total_bought
+shares = position.current_size
+price = position.current_price
+bought = position.total_size
```

* Breaking change: replace `get_market_holders(...)` with the paginated `list_market_holders(...)`. Pass `condition_ids` and `page_size`. Merge outcome groups across pages by `asset_id`. `include_pnl=True` adds position economics for one condition with a maximum page size of 100.

```diff theme={null}
-holders = await client.get_market_holders(market=[condition_id], limit=10)
+pages = client.list_market_holders(condition_ids=[condition_id], page_size=10)
+page = await pages.first_page()
+holders = page.items
```

* Breaking change: `get_portfolio_value(...)` returns one `PortfolioValue` instead of a tuple. Portfolio and open-interest filters now use `condition_ids`.

```diff theme={null}
-values = await client.get_portfolio_values(user=user, market=[condition_id])
-value = values[0].value
+portfolio = await client.get_portfolio_value(user=user, condition_ids=[condition_id])
+value = portfolio.value

-interest = await client.get_open_interests(market=[condition_id])
+interest = await client.get_open_interests(condition_ids=[condition_id])
```

* Added `get_user_stats(...)`, `get_user_pnl(...)`, and `get_user_volume(...)` for wallet analytics. Breaking change: replace `get_traded_market_count(...)` with `UserStats.traded_market_count`. Statistics return `None` when unavailable. Secure clients default these reads to the authenticated wallet.

```diff theme={null}
-count = (await client.get_traded_market_count(user=user)).traded
+stats = await client.get_user_stats(user=user)
+count = stats.traded_market_count if stats is not None else None
```

* Breaking change: replace `get_price_history(...)` with the paginated `list_price_history(...)`. Use `asset_id`, `start`/`end`, and `bucket_seconds` instead of `token_id`, `start_ts`/`end_ts`, and minute-based `fidelity`. Select an interval, a window of at most 15 days, or an exact `as_of` timestamp. Price points now expose `timestamp`, `price`, and `resolution_seconds`.

```diff theme={null}
-points = await client.get_price_history(asset_id=asset_id, interval="1d", fidelity=1)
+pages = client.list_price_history(asset_id=asset_id, interval="1d", bucket_seconds=60)
+page = await pages.first_page()
+points = page.items
```

* Breaking change: trader and builder leaderboards now take lowercase `window` values. Trader sorting uses `sort_by`. Use `get_trader_leaderboard_standing(user=...)` for an individual wallet's rankings. Added `list_biggest_winners(...)` for winning market and Combo positions.

```diff theme={null}
-pages = client.list_trader_leaderboard(time_period="DAY", order_by="PNL")
+pages = client.list_trader_leaderboard(window="day", sort_by="PNL")

-pages = client.list_builder_leaderboard(time_period="DAY")
+pages = client.list_builder_leaderboard(window="day")
```

* Breaking change: `get_builder_volumes(...)` returns `BuilderVolumePoint` calendar buckets. Use `interval` and `bucket_limit`, which counts dates rather than rows.

```diff theme={null}
-volumes = await client.get_builder_volumes(time_period="DAY")
+volumes = await client.get_builder_volumes(interval="day", bucket_limit=30)
```

* Breaking change: `get_event_live_volume(...)` accepts integer `event_ids` and returns one combined `LiveVolume`. Read `taker_volume_total` for total shares and `markets` for the breakdown.

```diff theme={null}
-volumes = await client.get_event_live_volumes(id=str(event_id))
+volume = await client.get_event_live_volume(event_ids=[event_id])
```

* Added `get_resolutions(...)` for resolution status and payouts by question, conditions, or events. Resolution payouts preserve their values through serialization and parsing.
* Breaking change: Combo position sorting now uses separate `sort_by` and `sort_direction` arguments. Status filters accept multiple values, except `"REDEEMABLE"`, which must be used alone. Update bounds accept epoch seconds or timezone-aware `datetime` values.

```diff theme={null}
-pages = client.list_combo_positions(user=user, sort="current_value_desc")
+pages = client.list_combo_positions(user=user, sort_by="CURRENT_VALUE", sort_direction="DESC")
```

* Added typed migration and tip activity and public activity/status enums. Breaking change: Combo activity now exposes `position_id` and uses `timestamp` instead of `transaction_at`. `log_index` and `module_id` are removed.

```diff theme={null}
-occurred_at = activity.transaction_at
+occurred_at = activity.timestamp
```

* Data reads now retry short-lived rate limits. Invalid filters, time bounds, event IDs, and cursor inputs raise `UserInputError`. Malformed response identities raise `UnexpectedResponseError`.
* Fixed UTC interpretation of date-only timestamps, preservation of full position history and zero-valued Combo update bounds, and dataframe exports containing both enum and string activity values.

### `0.9.0`

* Added protocol-neutral `asset_id` and `condition_id` fields across CLOB reads, filters, realtime events, and Data API responses. Pass a CTF token ID or Polymarket Protocol V2 position ID through `asset_id`; the deprecated `token_id`, `token_ids`, and `market` aliases remain available for compatibility.
* Order estimation, creation, and placement now route Polymarket Protocol V2 position IDs through Exchange V3, and `setup_trading_approvals()` includes the Polymarket Protocol V2 binary and negative-risk modules.
* Position lifecycle methods now split and merge ordinary Polymarket Protocol V2 positions. `merge_multiple_positions(...)` accepts Polymarket Protocol V2 `position_id` requests, and `redeem_positions(position_id=...)` redeems a resolved Polymarket Protocol V2 position.

### `0.8.0`

* Markets and events now expose their protocol through `version`, and markets expose Combo eligibility through `market.state.combo_status`. Combo status values introduced after this release pass through as strings.
* Team entries on event and team-list responses now preserve their `ordering` value.
* Breaking change: `revoke_session_key(...)` now returns `None` once the Session Key leaves the active registry. The SDK retries transient registry reads, while the backend continues canceling orders and finalizing the on-chain revocation asynchronously. See [Revoke a Session Key](/trading/session-keys#revoke-a-session-key).

```diff theme={null}
-transaction = await secure_client.revoke_session_key(
+await secure_client.revoke_session_key(
    address=session_key_address,
)
```

* Session Key authorization and revocation submissions now allow up to five minutes for relayer validation and broadcast.

### `0.7.1`

* `authorize_session_key(...)` no longer accepts `valid_until`. This is a breaking change. Each Session Key authorization expires after 180 days. Revoke a Session Key to end access sooner.

```diff theme={null}
authorization = await secure_client.authorize_session_key(
    address=session_key_address,
-    valid_until=datetime.now(UTC) + timedelta(days=30),
)
```

### `0.7.0`

* Added scoped Deposit Wallet session keys through `authorize_session_key(...)`, `fetch_session_keys()`, and `revoke_session_key(...)` on secure clients. Secure clients can use an authorized session signer for ordinary operations. Scopes default to `ALL`; known scopes are enumerated while newer scope strings remain usable.
* `RateLimitError.rate_limit` now carries the `Poly-RateLimit-*` state returned with a rejection. Pass `on_rate_limit_update` when creating a client to receive per-signer rate-limit updates from any response that reports them.
* Added `get_trading_approvals_state(...)` to public and secure clients so applications can inspect missing ERC-20 and ERC-1155 approvals without submitting transactions.
* `RequestRejectedError.restriction` now distinguishes matching-engine restarts, cancel-only mode, and post-only mode. `retry_after` falls back to the response body's `retry_after_seconds` value when the header is absent.
* Breaking change: account notifications are now a `NotificationType`-discriminated union whose payloads are typed Pydantic models instead of arbitrary mappings. Narrow on `notification.type`, then read payload fields as attributes.

```diff theme={null}
-if notification.type == 2:
-    order_id = notification.payload["order_id"]
+if notification.type == NotificationType.ORDER_FILL:
+    order_id = notification.payload.order_id
```

### `0.6.0`

* Added requester-side Combos RFQ support to `SecureClient` and `AsyncSecureClient` through `request_combo_quote(...)`, `accept_combo_quote(...)`, `wait_for_combo_fill(...)`, and `fetch_rfq_status(...)`. Pass a Builder API key through `api_key=`. `ComboQuote` values can be serialized, and SELL quotes include the exact post-fee `net_receive`. No-quote, decline, expiry, and terminal failure outcomes return values. Gateway rejections raise `RfqRequestRejectedError`.
* Breaking change: `get_last_trade_price(...)` now returns `LastTradePrice | None`. Untraded tokens return `None` instead of a `Decimal("0.5")` placeholder. `get_last_trade_prices(...)` leaves untraded tokens out of the response, so match results by `token_id` instead of array position.

```diff theme={null}
-price = client.get_last_trade_price(token_id=token_id).price
+last_trade = client.get_last_trade_price(token_id=token_id)
+price = last_trade.price if last_trade is not None else None
```

### `0.5.0`

* Added a Perps dead man's switch: `session.arm_auto_cancel()` schedules a one-shot cancel-all, `session.disarm_auto_cancel()` clears it, and `session.fetch_auto_cancel_status()` reports the current deadline and daily trigger usage. Arming after the daily limit raises `AutoCancelDailyLimitError`.
* Perps funding history and realtime funding events now include a required `id`, typed as `PerpsFundingPaymentId`.
* Fixed `session.place_order()` missing private order updates that arrive before the command acknowledgement. When the caller omits a client order ID, the SDK now generates one before submitting the order.
* Order placement now caches market configuration and platform and builder fees, reducing repeated metadata reads while refreshing stale tick data before returning an input error.

### `0.4.0`

* Added async `PerpsSession.update_margin`, which adjusts isolated margin for an instrument position. Positive `amount` values add margin; negative values remove it.
* `AcceptedOrder.order_id` is now typed as `OrderId`.

### `0.3.0`

* Added typed 30-second and 60-second Chainlink TWAP realtime subscriptions.
* Added Perps account notifications: `session.list_notifications()` with the account's `unread` count on each page, `session.mark_notifications_read()`, and a `notifications` session WebSocket channel with typed `notification` events.
* Perps fills pagination now uses the API-native cursor, and `list_fills` accepts a `sort` direction (newest first by default).
* Added the `DEPOSIT`, `WITHDRAWAL`, and `TAKER_REBATE` activity types. `list_activity` now returns all activity types by default, including deposits and withdrawals.
* `RequestRejectedError` now exposes `retry_after` from the `Retry-After` response header or a `retry_after_seconds` response field.
* Fixes:
  * RFQ quote rejections now carry the granular Combos quote-validation error codes instead of a generic validation failure.
  * Deposit Wallet gasless and Collateral Return submits now self-heal nonce mismatches: when the relayer rejects a batch and reports the on-chain nonce, the SDK re-signs the batch with that nonce and resubmits it once.
  * Collateral Return operation `event_id` values are now typed as `EventId`.

### `0.2.0`

* Added `wait_for_order_fill_settlement`, which waits until every fill in an order response reaches a terminal settlement outcome and returns the settlement transaction hashes.
* Added Collateral Return support to secure clients: `plan_collateral_return` returns an inspectable plan and `execute_collateral_return_plan` signs and submits it for Deposit Wallet, Safe, and Proxy accounts, returning a transaction handle.
* Added `isolated_only` to Perps instruments, indicating whether the instrument supports only isolated margin.
* Added volume-based fee tiers to the Perps fee schedule, including negative maker rebate rates, typed with `PerpsFeeTier`.
* Perps withdrawal statuses are now forward-compatible: known statuses are enumerated in `PerpsKnownWithdrawalStatus`, which adds `failed`, and statuses introduced after a release flow through as plain strings instead of failing the response parse. `list_withdrawals` accepts `withdrawal_status="failed"`.
* Fixed offset-paginated reads silently stopping after the first page when `page_size` reached the server's limit cap. `page_size` is now validated per endpoint and values above the cap raise `UserInputError`. A full page reports `has_more=True`; when a collection ends exactly on a page boundary, the final page is empty.
* CLOB cursor-paginated reads no longer report the per-page row count as `Page.total_count`; it was never the total across pages. Use the page items instead:

```diff theme={null}
-count = page.total_count
+count = len(page.items)
```

* Open orders with no expiration now parse `expires_at` as `None`. GTC orders report a zero expiration, which previously parsed as the Unix epoch.

### `0.1.0`

* Graduated the SDK to the stable 0.x release line, marked Perps APIs as experimental, and removed deprecated beta compatibility APIs.
* Added `condition_id` aliases to CLOB models while keeping `market` available as a deprecated alias.
* Typed CLOB cancellation result IDs with `OrderId`.
* Streams drop unknown or unreadable WebSocket frames instead of closing the connection.
* Limit and market order helpers reject prices that are not a multiple of the market tick size.

### `0.1.0b21`

* `setup_trading_approvals` no longer requests approvals for the retired CLOB v1 Neg Risk Adapter.

### `0.1.0b20`

* RFQ quoter sessions now keep running when the server introduces new error codes: unrecognized codes are carried on rejection errors as plain strings, while known codes stay typed through the `RfqErrorCode` enum.
* Added `ConnectionLostError` carrying the WebSocket close `code` and `reason`. Losing an RFQ session connection now raises it from in-flight operations and the session iterator, instead of a generic `TransportError`. Closing the session still ends iteration cleanly.
* Optional decimal fields on streamed market and user events treat empty strings as absent (for example a trade's `fee_rate_bps` or a price change's `best_bid` and `best_ask`).
* Batch price reads return `TokenId`-keyed maps.
* Perps streams handle fill and trade frames that batch multiple entries.

### `0.1.0b19`

* Added `RESOLVED_PARTIAL` to `ComboPositionStatus` so Combo positions that resolve at a fractional payout (for example a voided leg) parse correctly instead of failing validation.

### `0.1.0b18`

* Combo activity now parses the canonical `type` field returned by the Data API, instead of deriving lifecycle actions from legacy fields.

### `0.1.0b17`

* Added SDK pagination for Combo lifecycle activity and server-cursor pagination for Combo positions.
* Added typed overloads for market, event, and tag lookups, mutually-exclusive lookup arguments, and `redeem_positions`.
* Added trade time filters.
* Hardened Combo pagination filters and branded Combo activity IDs.
* Breaking beta change: Combo activity and position fields now use `wallet`, `amount`, and `payout`; Combo activity rows no longer expose `module_kind`.

```diff theme={null}
-activity.user_address
-activity.amount_usdc
-redeem_activity.payout_usdc
-position.user_address
+activity.wallet
+activity.amount
+redeem_activity.payout
+position.wallet
```

### `0.1.0b16`

* Fixed Deposit Wallet trading setup approvals to use the current Protocol V2 auto-redeem operator.

### `0.1.0b15`

* Added support for Perps.

### `0.1.0b14`

* Added builder API key management for creating, fetching, and revoking builder API keys.
* Added support for merging multiple positions in one request.
* Added runnable Python SDK examples for common integration workflows.
* Resolve closed markets when redeeming positions.
* Gasless transaction handles now wait for relayer transactions to reach confirmed state before resolving.

### `0.1.0b13`

* Require GTD limit order expirations to be at least 3 minutes in the future.

### `0.1.0b12`

* Support CLOB order tick sizes `0.005` and `0.0025`.

### `0.1.0b11`

* Preserve already-deployed legacy UUPS Deposit Wallets when secure clients resolve the default wallet, while new Deposit Wallet deployments use the beacon factory path.
* Retry rejected JSON-RPC batches by splitting them into smaller batches.
* Added typed Gamma search sort fields for search requests.

### `0.1.0b10`

* Preserve `group_item_title` on market responses so grouped market titles remain available after normalization.

### `0.1.0b9`

* RFQ quoter sessions now emit typed `RfqTradeEvent` events for confirmed Combos fills.
* RFQ rejection errors now expose `error_id` values and parse `INVALID_SIGNATURE` and `INTERNAL_ERROR` codes.

### `0.1.0b8`

* Added `parent_event_id` to `Event` so child events can link back to their parent event.
* Added `max_price` and `min_price` protection fields to market order requests.
* Handle legacy multi-outcome market listings more safely by omitting markets that cannot be represented by the binary market model.
* Normalize empty-string trade and position market icons to `None`.
* Parse Combo trade activity rows correctly.
* Support new Combos RFQ error codes for balance, allowance, and pre-execution reservation failures.
* Broad user websocket subscriptions now omit market filters so all-market streams receive trade events.

### `0.1.0b7`

* Point Combos RFQ endpoints at the production domains: `combos-rfq-api.polymarket.com` (REST) and `combos-rfq-gateway-quoter.polymarket.com` (quoter WebSocket).

### `0.1.0b6`

* Added `list_combo_markets` for fetching the Combo market catalog with SDK pagination. See [Combos](/trading/combos/overview).
* Parse RFQ quote rejections that use the `SUBMISSION_WINDOW_CLOSED` gateway error code.

### `0.1.0b5`

* Added Combos support for multi-leg RFQ positions. See [Combos](/trading/combos/overview).
* Added notebook-friendly model display for Jupyter workflows.
* `ConditionId` is now deprecated in favor of `CtfConditionId`; existing
  `ConditionId` exports remain available as deprecated aliases.

### `0.1.0b4`

* Added dataframe conversion support for SDK models and response collections.

**Secure client setup now defaults to the Deposit Wallet flow**

`AsyncSecureClient.create` can now derive and use the signer's deterministic
Deposit Wallet when you omit `wallet`. If you already know which Polymarket
wallet you want to use, keep passing `wallet`.

```diff theme={null}
secure_client = await AsyncSecureClient.create(
    private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
-    wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
)
```

If you want to keep account selection explicit, no change is required:

```python theme={null}
secure_client = await AsyncSecureClient.create(
    private_key=os.environ["POLYMARKET_PRIVATE_KEY"],
    wallet=os.environ["POLYMARKET_WALLET_ADDRESS"],
)
```

**`setup_trading_approvals()` now waits internally**

You no longer need to wait on the returned handle. Call the method once before
trading; it is safe to call again if approvals are already set.

```diff theme={null}
-handle = await secure_client.setup_trading_approvals()
-await handle.wait()
+await secure_client.setup_trading_approvals()
```

**Gasless setup helpers are deprecated**

You no longer need to call `is_gasless_ready()` or `setup_gasless_wallet()` in
the normal setup path. Create the secure client, then set up trading approvals.

```diff theme={null}
-ready = await secure_client.is_gasless_ready()
-
-if not ready:
-    secure_client = await secure_client.setup_gasless_wallet()
-
 await secure_client.setup_trading_approvals()
```

### `0.1.0b1`

First beta release of the unified Python SDK. Install the beta package with your
package manager:

```bash theme={null}
uv add polymarket-client
```
```

---
