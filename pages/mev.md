---
title: Maximal extractable value
ticker: None
category: Infrastructure
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Maximal extractable value

Maximal extractable value, or MEV, is value obtainable through control of
transaction inclusion and ordering beyond ordinary block rewards and
transaction fees. The earlier term “miner extractable value” reflected
proof-of-work block production; the broader name also applies when
validators produce blocks.[^overview]

| | |
|---|---|
| Abbreviation | MEV |
| Earlier terminology | Miner extractable value |
| Examples | Arbitrage, liquidations, sandwich trades |
| Ethereum infrastructure example | MEV-Boost[^boost] |
| Research milestone | *Flash Boys 2.0*, April 2019[^paper] |

## Where it comes from

Transactions can change the opportunity available to the next transaction.
A searcher may buy a token on one exchange and sell it on another, or
compete to liquidate an undercollateralised loan. Searchers identify these
opportunities and submit transactions, sharing some proceeds with the
parties that include them.[^overview]

These activities have different consequences. Arbitrage can bring prices
into alignment and liquidations can help lending systems remain solvent.
Other ordering strategies worsen execution for users. MEV therefore
includes both useful market operations and extraction at someone else's
expense.[^overview]

## Research and consensus risks

Philip Daian and co-authors documented trading bots and competitive fee
bidding in their 2019 paper *Flash Boys 2.0*. They described priority gas
auctions, in which participants compete for favourable ordering, and
analysed how transaction-ordering revenue can create incentives to
destabilise consensus.[^paper]

That research connects application-level trading to blockchain security.
When the value available from changing a block's contents is sufficiently
large, it may change the economic incentive to extend the existing chain.
The paper's analysis is a warning about incentive structures, rather than
a claim that every profitable trade causes a reorganisation.[^paper]

## Builders, proposers, and private transactions

Flashbots' MEV-Boost software lets Ethereum validators obtain candidate
blocks from a competitive builder market. Builders assemble transactions
and offer a payment to the proposing validator. This separates the task
of constructing a block from the validator's opportunity to propose it;
MEV-Boost is middleware used by validators, rather than the definition of
Ethereum consensus itself.[^boost]

Flashbots also operates Protect, a transaction-submission service. Its
documentation says it sends transactions through a private mempool to
hide them from public frontrunning and sandwich bots, and can return some
MEV or excess fees to users. These are service features, not a guarantee
that all possible ordering losses have been eliminated.[^protect]

Private submission introduces choices about who receives transaction
information. Protect's settings allow different sharing arrangements
with builders and searchers. Its documentation explains that broader
sharing can improve inclusion speed or refund opportunities while
requiring trust in additional recipients. A private route therefore needs
to be assessed by its actual data-sharing rules.[^settings]

## See also

- [Automated market maker](automated-market-maker.md)
- [Ethereum](ethereum.md)
- [Aave](aave.md)
- [Uniswap](uniswap.md)

## References

[^overview]: ethereum.org. *Maximal extractable value (MEV)*. <https://ethereum.org/developers/docs/mev/>
[^paper]: Daian, P. et al. (2019). *Flash Boys 2.0: Frontrunning, Transaction Reordering, and Consensus Instability in Decentralized Exchanges*. <https://arxiv.org/abs/1904.05234>
[^boost]: Flashbots. *MEV-Boost overview*. <https://docs.flashbots.net/flashbots-mev-boost/introduction>
[^protect]: Flashbots. *MEV Protection Overview*. <https://docs.flashbots.net/flashbots-protect/overview>
[^settings]: Flashbots. *Protect settings guide*. <https://docs.flashbots.net/flashbots-protect/settings-guide>
