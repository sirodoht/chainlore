---
title: Liquidation
ticker: None
category: Decentralised finance
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# Liquidation

In crypto lending and derivatives, liquidation is the process used to
reduce or close a position when it no longer meets its collateral
requirements. A lending protocol may sell or transfer pledged assets to
repay debt, while a derivatives venue may close a leveraged position.
The trigger and execution rules depend on the particular system.[^aave][^hyperliquid]

| | |
|---|---|
| Lending example | Repay debt in exchange for collateral |
| Derivatives example | Close positions below maintenance margin |
| Pricing dependency | Oracle or mark-price rules |
| Execution mechanisms | Direct repayment, order book, or auction |
| Remaining risk | A shortfall can survive unsuccessful liquidation |

## Lending positions

Aave expresses a borrower's collateral buffer through a health factor:
collateral value, adjusted by liquidation thresholds, divided by debt
value. A value below one makes a position eligible for liquidation.
This can follow a fall in collateral prices, an increase in debt value,
or other changes to the position.[^aave]

An Aave liquidator repays debt and receives collateral plus a liquidation
bonus. The process is permissionless and competitive. The permitted
repayment fraction depends on the position and protocol rules; it is
not always a complete sale of all the borrower's assets. Aave's
documentation describes both partial and full-liquidation cases.[^aave]

The threshold is not identical to insolvency. A position can cross its
liquidation threshold while collateral is still worth more than its
debt, because the threshold incorporates a buffer. Liquidation aims to
act before further price changes or execution costs consume that
buffer.[^aave]

## Auctions

Sky's documented collateral-liquidation system transfers an unsafe
vault's collateral and debt into the liquidation process, then auctions
collateral for DAI. Its Liquidation 2.0 design uses descending-price
auctions with immediate settlement, rather than requiring bidders to
leave funds locked until an auction ends.[^sky]

Auction design creates additional dependencies. The initial price,
price-decay function, and limits on concurrent debt liquidation affect
how quickly assets can sell. Sky's documentation lists risks from prices
falling too rapidly or too slowly, oracle inputs, and governance changes
that affect auctions already underway.[^sky]

## Derivatives positions

Hyperliquid first attempts to close an under-margined account's positions
through market orders. Orders may fill partially, and a backstop
liquidator can take over if equity deteriorates further. Isolated and
cross-margin positions expose different pools of collateral to that
process.[^hyperliquid]

Liquidation does not itself guarantee that all debt is recovered. In
Hyperliquid's documented auto-deleveraging process, a negative account
or isolated-position value can lead to positions on the profitable
opposing side being closed. This allocates the remaining shortfall
through specified trading rules.[^adl]

## Execution risk

Eligibility, price measurement, and successful execution are separate
steps. Aave liquidators compete to submit transactions after oracle or
position changes; Sky auctions require buyers; an order-book liquidation
requires available counterparties. A protocol's mathematical collateral
test cannot alone ensure that the required trade will clear at the
price used in that test.[^aave][^sky][^hyperliquid]

## See also

- [Aave](aave.md)
- [MakerDAO and Sky](makerdao-sky.md)
- [Perpetual futures](perpetual-futures.md)
- [Maximal extractable value](mev.md)

## References

[^aave]: Aave. *Health Factor & Liquidations*. <https://aave.com/help/borrowing/liquidations>
[^sky]: Sky Protocol documentation. *Collateral Liquidation*. <https://developers.skyeco.com/protocol/vaults/collateral-liquidation/>
[^hyperliquid]: Hyperliquid documentation. *Liquidations*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations>
[^adl]: Hyperliquid documentation. *Auto-deleveraging*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/auto-deleveraging>
