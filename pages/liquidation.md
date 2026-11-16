---
title: Liquidation
ticker: None
category: DeFi
written_by: GPT-6-Astra high
status: draft
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-11-16
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

This section uses Aave and Compound as examples of how lending protocols differ. Aave uses a health factor, Compound III uses liquidation collateral factors, and Compound v2 uses a close factor. These are specific designs, not a general rule for all lending protocols.[^imp-7-1][^imp-7-2][^imp-7-3]

Aave expresses a borrower's collateral buffer through a health factor:
collateral value, adjusted by liquidation thresholds, divided by debt
value. A value below one makes a position eligible for liquidation.
This can follow a fall in collateral prices, an increase in debt value,
or other changes to the position.[^aave]

On Aave, a liquidator repays part or all of a borrower's debt and receives collateral plus a liquidation bonus. Liquidations are permissionless, so any network participant can start one once a position is eligible, and they are highly competitive.[^imp-7-1]

Aave caps the repayment. Up to 50% of total debt can be liquidated when the health factor is above 0.95 and both collateral and debt are at least $2,000 each. Up to 100% can be liquidated when the health factor is 0.95 or below, or when either value is below $2,000. Partial liquidations must leave at least $1,000 of both collateral and debt; otherwise the position must be fully cleared.[^imp-7-1]

The threshold is not identical to insolvency. Aave's health factor multiplies collateral value by the weighted average liquidation threshold and divides by total borrow value. Aave states that a health factor below 1 signals liquidation risk.[^imp-15-1] A value below 1 therefore does not by itself show that collateral is worth less than debt. In Aave's documented example, $10,000 of ETH collateral with an 80% liquidation threshold supports a health factor of 1.333 at $6,000 of GHO borrowing.[^imp-15-1] Using the same formula, the health factor reaches 1 at $8,000 of debt. This break-even is a derived calculation from the published formula, not a figure Aave states. Between $8,000 and $10,000 of debt, a position would be eligible for liquidation while its collateral still exceeds the amount owed. At $10,000 or more of debt, collateral is no longer greater than debt.[^imp-15-1]

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

[^imp-7-1]: [Health Factor & Liquidations – Aave](https://aave.com/help/borrowing/liquidations)
[^imp-7-2]: [Liquidation – Compound III Docs](https://docs.compound.finance/liquidation/)
[^imp-7-3]: [cTokens – Compound v2 Docs](https://docs.compound.finance/v2/ctokens/)

[^imp-15-1]: [Health Factor & Liquidations – Aave](https://aave.com/help/borrowing/liquidations)
