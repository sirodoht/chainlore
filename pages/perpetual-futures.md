---
title: Perpetual futures
ticker: None
category: Infrastructure
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Perpetual futures

Perpetual futures, often called perpetual contracts or perps, are
derivatives that provide long or short exposure without a scheduled
expiry. Crypto venues use periodic funding payments to encourage their
prices to track the referenced asset. Holding a perpetual position is
different from buying the underlying asset outright.[^intro][^funding]

| | |
|---|---|
| Type | Derivative |
| Scheduled expiry | None |
| Price-alignment mechanism | Funding payments |
| Collateral concepts | Initial and maintenance margin |
| Examples | [Bybit](bybit.md) and [Hyperliquid](hyperliquid.md) |

## Margin and leverage

Initial margin is the collateral needed to open a position; maintenance
margin is the requirement for keeping it open. Leverage expresses the
relationship between exposure and collateral. For example, $1,000 of
margin supporting $5,000 of exposure represents five-times leverage,
before fees and other adjustments. Maximum leverage can vary by asset
and position size.[^contracts]

Isolated margin assigns collateral to a particular position. Cross
margin shares eligible collateral across positions in an account. These
arrangements change which balances absorb losses and how liquidation is
calculated. They do not change the fact that the contract can lose value
as its reference market moves.[^contracts]

## Funding

Funding transfers value between the long and short sides at specified
intervals. A positive rate generally means longs pay shorts, while a
negative rate reverses the direction. Hyperliquid's documented mechanism
combines an interest component with a premium component and settles
funding hourly; other venues can use different intervals and
formulas.[^funding]

Funding is intended to make persistent price divergence costly for the
side trading at a premium. It is an incentive, not a contractual promise
that the perpetual always trades at the spot price. A quoted funding
rate is also distinct from a venue's fee for executing a trade.[^funding][^contracts]

## Reference prices

The last traded price, oracle price, and mark price serve different
purposes. Hyperliquid’s robust-price documentation describes an external
price oracle for funding and a separate composite mark for margin and
unrealised profit or loss. This design uses external venues
and local market information to reduce sensitivity to isolated
trades.[^prices]

A mark is an input to the risk engine, not a guarantee that a large order
can execute at that price. Hyperliquid initially attempts liquidations
through its order book; available liquidity determines whether those
orders fill. If that process cannot restore sufficient margin, a
backstop mechanism may take over the position.[^liquidation]

## Loss allocation

When a deficit remains, some systems can close profitable opposing
positions through auto-deleveraging. Hyperliquid documents a ranking
based on profit and leverage to select affected accounts. Such rules
matter even to a trader whose own position is profitable: managing one
account's margin does not remove the venue's broader settlement
dependencies.[^adl]

## See also

- [Liquidation](liquidation.md)
- [Hyperliquid](hyperliquid.md)
- [Bybit](bybit.md)
- [Blockchain oracle](blockchain-oracle.md)

## References

[^intro]: Bybit. *Introduction to USDT Perpetual and Expiry Contracts*. <https://www.bybit.com/en/help-center/article/Introduction-to-USDT-Perpetual-Expiry-Contract>
[^contracts]: Bybit. *FAQ — USDT Perpetual and Expiry Contracts*. <https://www.bybitglobal.com/en/help-center/article/FAQ-USDT-Perpetual-and-Expiry-Contracts>
[^funding]: Hyperliquid documentation. *Funding*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding>
[^prices]: Hyperliquid documentation. *Robust price indices*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/robust-price-indices>
[^liquidation]: Hyperliquid documentation. *Liquidations*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations>
[^adl]: Hyperliquid documentation. *Auto-deleveraging*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/auto-deleveraging>
