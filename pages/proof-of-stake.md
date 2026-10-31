---
title: Proof of stake
ticker: None
category: Infrastructure
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# Proof of stake

Proof of stake is an approach to blockchain consensus in which validators
commit cryptocurrency as stake. [Ethereum](ethereum.md) uses staked ETH
to support block proposals and votes, with rewards for participation and
penalties for specified failures. Its design provides an example of proof
of stake; the label alone does not specify every network's rules.[^pos]

| | |
|---|---|
| Abbreviation | PoS |
| Ethereum consensus asset | ETH |
| Ethereum participants | Validators |
| Related approach | [Proof of work](proof-of-work.md) |
| Ethereum transition | 15 September 2022[^merge] |

## Ethereum's design

Ethereum validators check proposed blocks and issue votes called
attestations. Time is divided into slots, with a proposer selected for a
slot and committees assigned voting duties. The voting process helps
establish both the current chain head and longer-term agreement on its
history.[^pos]

Checkpoint votes representing at least two-thirds of the active stake
support justification and finalisation. Finality means that producing
conflicting finalised histories entails a substantial slashable violation;
it does not mean computers can no longer fail. A sufficiently large
non-participating share can interrupt finality.[^pos]

Slashing penalises particular contradictory signed messages, including
double proposals and conflicting attestations. Ordinary missed duties and
offline penalties are different from slashing. Correlated offences can
make losses more severe than an isolated offence.[^pos]

## Checkpoints and trust

Ethereum uses weak-subjectivity checkpoints to help a node joining or
returning to the network identify the accepted history. A recent trusted
checkpoint provides an anchor; the node then verifies the chain forward
from that state. This addresses the problem of alternative histories
signed by validators whose old stake is no longer available to
penalise.[^weak]

The checkpoint must come from a source the operator trusts, and can be
cross-checked against independent nodes or explorers. It is a different
function from an ordinary finalised block: the node rejects histories
inconsistent with its chosen checkpoint, while conflicting finalised
blocks indicate a consensus failure.[^weak]

## Pools and liquid staking

Staking pools let people participate through a service or contract rather
than operate a validator themselves. A liquid staking token represents a
claim associated with that arrangement. Ethereum's protocol rewards the
validators; it does not directly recognise the holder of a pool token as
a validator.[^pools]

Pool users inherit validator penalties and add dependencies on contracts,
operators, and governance. A liquid token can also trade below the value
of its underlying stake, especially when redemptions are delayed or market
liquidity is thin. The ability to sell a token is therefore distinct from
the ability to redeem the underlying ETH immediately.[^pools]

## Ethereum's transition

The Merge joined Ethereum's existing execution system to the Beacon
Chain's proof-of-stake consensus in September 2022. It ended proof-of-work
mining on Ethereum. The change did not itself substantially increase
transaction capacity or directly lower gas fees; those were separate
scaling objectives.[^merge]

## See also

- [Ethereum](ethereum.md)
- [Proof of work](proof-of-work.md)
- [Lido](lido.md)
- [Solana](solana.md)

## References

[^pos]: ethereum.org. *Proof-of-stake (PoS)*. <https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/>
[^weak]: ethereum.org. *Weak subjectivity*. <https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/weak-subjectivity/>
[^pools]: ethereum.org. *Liquid and pooled staking*. <https://ethereum.org/en/staking/pools/>
[^merge]: ethereum.org. *The Merge*. <https://ethereum.org/en/roadmap/merge/>
