---
title: Polymarket
ticker: None
category: DeFi
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Polymarket

Polymarket is a prediction-market platform where participants trade
positions tied to event outcomes. Prices are commonly read as implied
probabilities: a share priced at $0.60 corresponds to a market-implied
60% chance of its outcome. Settlement follows the market's resolution
rules, rather than a trader's interpretation of its headline.[^prices][^resolution]

| | |
|---|---|
| Type | Prediction-market platform |
| International platform architecture | Offchain matching, onchain settlement |
| Documented collateral | pUSD on Polygon, backed by USDC |
| Documented resolution sources | UMA; Chainlink TWAP for up-down markets |
| US exchange | QCX LLC doing business as Polymarket US[^us] |

## Trading and collateral

The international platform uses a hybrid order book. Orders are created
offchain, matched by an operator, and settled through smart contracts.
Blockchain settlement therefore coexists with an operator responsible
for matching; it does not imply that every part of a trade happens
through a permissionless onchain order book.[^orders]

As of October 2026, Polymarket's documentation identifies pUSD as its
collateral token on Polygon. It describes pUSD as an ERC-20 token backed
by USDC, with wrapping and withdrawal functions enforced by collateral
contracts. A balance used for trading should consequently be distinguished
from a direct balance of native USDC in a wallet.[^collateral]

The displayed price is normally the midpoint between the best bid and
ask; the documentation says it uses the last trade when the spread is
wider than ten cents. A displayed probability is therefore not
necessarily the price at which a trader can buy or sell the desired
quantity. Available bids, asks, and depth determine execution.[^prices]

## Resolution

A market's rules specify its resolution source, end date, and treatment
of ambiguous cases. In an ordinary binary resolution, winning shares
redeem for $1 and losing shares become worthless. The documentation also
allows an unknown or 50–50 resolution in which each outcome token redeems
for $0.50. An apparently straightforward question may require a particular
announcement or data source.[^resolution]

The documented UMA process allows a proposer to post a bond and nominate
an outcome, followed by a challenge period. Disputed cases can reach
UMA token-holder voting. Polymarket separately documents Chainlink
time-weighted average prices for up-down markets, so it would be
incorrect to describe every market as using the same resolution
path.[^resolution]

## Regulation and the US exchange

On 3 January 2022, the US Commodity Futures Trading Commission settled
charges against Blockratize, doing business as Polymarket. The CFTC found
that it had offered event-based binary options without the required
registration or designation. The order imposed a $1.4 million penalty
and required non-compliant markets to be wound down.[^cftc]

That historical order should be read separately from the later US
exchange. As of October 2026, the CFTC's register lists QCX LLC, doing
business as Polymarket US, as a designated contract market, with an
original designation date of 9 July 2025. The register identifies the
specific legal entity; it does not establish that every product or
international service carrying the Polymarket name has the same
regulatory status.[^us]

On 28 October 2026, Michigan's gaming regulator announced that Polymarket
US had agreed to stop offering new sports-related event contracts to
Michigan customers and close remaining positions by 25 November. The
regulator said Polymarket's appeal of an earlier injunction ruling
remained pending. As of 31 October, federal designation had therefore
not eliminated disputes over state gambling regulation.[^michigan]

## October 2026 security incident

On 29 October 2026, Polymarket temporarily halted trading after a security
incident involving a third-party provider. Reuters reported the company's
statement that it had fixed the issue, restored trading, referred the
incident to UK law enforcement, and would reimburse affected traders.
That statement was a reimbursement commitment, not confirmation that all
reimbursements had been completed as of 31 October.[^security]

## See also

- [Blockchain oracle](blockchain-oracle.md)
- [Chainlink](chainlink.md)
- [USDC](usdc.md)
- [Smart contract](smart-contract.md)

## References

[^prices]: Polymarket documentation. *Prices & Orderbook*. <https://docs.polymarket.com/concepts/prices-orderbook>
[^orders]: Polymarket documentation. *Order Lifecycle*. <https://docs.polymarket.com/concepts/order-lifecycle>
[^collateral]: Polymarket documentation. *Polymarket USD*. <https://docs.polymarket.com/concepts/pusd>
[^resolution]: Polymarket documentation. *Resolution*. <https://docs.polymarket.com/concepts/resolution>
[^cftc]: CFTC (2022-01-03). *CFTC Orders Event-Based Binary Options Markets Operator to Pay $1.4 Million Penalty*. <https://www.cftc.gov/PressRoom/PressReleases/8478-22>
[^us]: CFTC. *Designated Contract Markets: QCX LLC d/b/a Polymarket US*. <https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations/49571>

[^michigan]: Michigan Gaming Control Board (2026-10-28). *Polymarket backs down as Michigan's relentless crackdown on unlicensed sports betting continues*. <https://www.michigan.gov/mgcb/news/2026/10/28/polymarket-backs-down-in-michigan>
[^security]: Reuters (2026-10-29), republished by StreetInsider. *Polymarket resumes trading after third-party security breach, to reimburse users*. <https://new.streetinsider.com/Reuters/Polymarket%2Bresumes%2Btrading%2Bafter%2Bthird-party%2Bsecurity%2Bbreach,%2Bto%2Breimburse%2Busers/27256837.html>
