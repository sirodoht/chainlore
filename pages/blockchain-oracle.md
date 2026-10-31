---
title: Blockchain oracle
ticker: None
category: Infrastructure
written_by: Unknown
status: draft
updated: 2026-10-31
---

# Blockchain oracle

A blockchain oracle supplies information that a
[smart contract](smart-contract.md) uses but cannot establish from its own
execution alone. Examples include asset prices and reports of external
events. An oracle makes data available for deterministic execution; it
does not make an external claim true merely by recording it on a
blockchain.[^intro]

| | |
|---|---|
| Type | Data infrastructure |
| Uses | Prices, collateral valuation, external events |
| Data sources | External providers or onchain markets |
| Onchain example | Uniswap v2 cumulative prices[^uniswap] |
| Offchain aggregation example | Chainlink Data Feeds[^feeds] |

## The oracle problem

Nodes executing the same transaction must obtain the same result. If each
queried a changing website independently, they could disagree. Oracle
systems instead submit a report that contracts can consume consistently.
The resulting dependency is often called the oracle problem: who supplies
the report, how it is verified, and what happens when it is wrong or
unavailable.[^intro]

## Price feeds

Chainlink describes its Data Feeds as aggregating information from multiple
sources through oracle networks and publishing reports onchain. Lending
applications can use the reported prices to value collateral and settle
positions. The data source, reporting process, and receiving application
are separate parts of that arrangement.[^feeds]

[Uniswap](uniswap.md) v2 provides a different input: prices derived from
trading pools. It accumulates prices over time, allowing an application to
calculate a time-weighted average between observations. Uniswap's
documentation explains that manipulation costs depend on liquidity and the
averaging period. An average can make a short-lived price movement less
influential without guaranteeing an economically correct price.[^uniswap]

## Risks and application responsibilities

Chainlink's integration guidance warns that market concentration, low
liquidity, and variation across trading venues can impair price quality.
It also distinguishes a wrapped or bridged asset from its underlying
asset: a bridge failure may cause their prices to diverge. Applications
must decide whether the feed actually represents the asset being valued.[^quality]

Rollups add an availability issue. Chainlink's sequencer uptime feeds
allow applications to detect an outage and apply a grace period after
recovery. This can prevent liquidations while ordinary users cannot
interact on equal terms. The application still needs to implement the
check and choose suitable parameters.[^sequencer]

## See also

- [Chainlink](chainlink.md)

- [Aave](aave.md)
- [Stablecoin](stablecoin.md)
- [Rollup](rollup.md)
- [Blockchain bridge](blockchain-bridge.md)

## References

[^intro]: ethereum.org. *Oracles*. <https://ethereum.org/en/developers/docs/oracles/>
[^feeds]: Chainlink. *Data Feeds*. <https://docs.chain.link/data-feeds>
[^uniswap]: Uniswap. *Uniswap v2 oracles*. <https://docs.uniswap.org/contracts/v2/concepts/core-concepts/oracles>
[^quality]: Chainlink. *Selecting quality data feeds*. <https://docs.chain.link/data-feeds/selecting-data-feeds>
[^sequencer]: Chainlink. *L2 sequencer uptime feeds*. <https://docs.chain.link/data-feeds/l2-sequencer-feeds>
