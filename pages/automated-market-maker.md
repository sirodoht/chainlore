---
title: Automated market maker
ticker: None
category: Decentralised finance
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# Automated market maker

An automated market maker, or AMM, offers trades against pooled assets
using an algorithm. In decentralised finance, a [smart
contract](smart-contract.md) can hold the pool and execute its pricing
rules. [Uniswap](uniswap.md) is one implementation; AMM describes a class
of market mechanisms rather than a particular exchange or token.[^v3]

| | |
|---|---|
| Abbreviation | AMM |
| Liquidity suppliers | Liquidity providers, or LPs |
| Example designs | Constant product, StableSwap, concentrated liquidity |
| Examples | Uniswap and [Curve](curve.md) |
| Main LP trade-off | Trading fees against inventory exposure and losses |

## Pools and prices

The constant-product design used by Uniswap v2 relates two token reserves
through an invariant commonly written as `x × y = k`. Swaps add one asset
and remove the other, moving the quoted price as the reserve ratio
changes. Fees mean the product need not remain literally unchanged across
a completed trade.[^v2]

Arbitrage traders buy where an asset is cheaper and sell where it is more
expensive. Their trades help align an AMM's price with other markets. This
is different from the contract receiving an authoritative external price:
the pool's immediately observable price can itself be manipulated. The
Uniswap v2 design therefore includes a mechanism for constructing
time-weighted price observations.[^v2]

## Different liquidity curves

Curve's 2019 StableSwap paper describes a design intended for assets with
similar prices. Near a balanced pool it behaves more like a constant-sum
market, allowing trades with relatively little price movement. As reserves
become imbalanced, it moves toward constant-product behaviour. The curve
can improve trading around the expected exchange rate, but its equations
also allow the market price to move away from that rate.[^stableswap]

Uniswap v3 introduced concentrated liquidity, allowing an LP to choose a
price interval for a position. Within that interval, a given deposit can
support more trading depth than if spread across all prices. Outside it,
the position becomes entirely one of its two assets and stops earning
trading fees until the price re-enters the interval.[^v3]

## Returns and risks

An LP's inventory changes as others trade. The resulting position can be
worth less than simply holding the original tokens, a difference commonly
called impermanent loss. Closing the position can realise that difference;
the word “impermanent” is not a promise that the loss will disappear.
Trading fees may offset losses, but do not guarantee that they will.[^loss]

For traders, transaction ordering is another risk. A sandwich strategy
places transactions before and after a victim's swap, exploiting the
price movement and leaving the victim with worse execution. AMM trading
is consequently connected to [maximal extractable value](mev.md), as well
as to liquidity and pricing.[^mev]

## See also

- [Uniswap](uniswap.md)
- [Curve](curve.md)
- [Blockchain oracle](blockchain-oracle.md)
- [Maximal extractable value](mev.md)

## References

[^v2]: Adams, H., Zinsmeister, N., and Robinson, D. (2020). *Uniswap v2 Core*. <https://app.uniswap.org/whitepaper.pdf>
[^v3]: Adams, H. et al. (2021). *Uniswap v3 Core*. <https://app.uniswap.org/whitepaper-v3.pdf>
[^stableswap]: Egorov, M. (2019). *StableSwap — efficient mechanism for Stablecoin liquidity*. <https://curve.fi/files/stableswap-paper.pdf>
[^loss]: Uniswap Labs. *What is Impermanent Loss?* <https://support.uniswap.org/hc/en-us/articles/20904453751693-What-is-Impermanent-Loss>
[^mev]: ethereum.org. *Maximal extractable value (MEV)*. <https://ethereum.org/en/developers/docs/mev/>
