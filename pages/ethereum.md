---
title: Ethereum
ticker: ETH
category: Layer 1
status: draft
updated: 2026-10-30
---

# Ethereum

**Ethereum** is a decentralized blockchain with a built-in virtual
machine, the Ethereum Virtual Machine (EVM), that runs general-purpose
programs called smart contracts. Its native currency is **ether** (ETH).
It was proposed by Vitalik Buterin in 2013 and launched on 30 July 2015.
Since September 2022 it has used proof of stake.[^whitepaper]

| | |
|---|---|
| Ticker | ETH |
| Type | Smart contract platform, layer 1 blockchain |
| Proposed by | Vitalik Buterin |
| Whitepaper | 2013 |
| Mainnet launch | 2015-07-30 |
| Consensus | Proof of stake (since 2022-09-15) |
| Slot time | 12 seconds |
| Minimum validator stake | 32 ETH |
| Supply cap | None; base fees are burned (EIP-1559) |
| Smallest unit | 1 wei = 10<sup>-18</sup> ETH |
| Chain ID | 1 |
| Main languages | Solidity, Vyper |
| Steward | Ethereum Foundation (Zug, Switzerland) |
| Live data | [Etherscan](https://etherscan.io), [ultrasound.money](https://ultrasound.money) |

## History

### Founding

Vitalik Buterin described Ethereum in a whitepaper circulated in late
2013 and announced it publicly in January 2014. Gavin Wood wrote the
formal specification, the Yellow Paper, in 2014.[^yellowpaper] The
founders also included Charles Hoskinson, Anthony Di Iorio, Mihai Alisie,
Joseph Lubin, Amir Chetrit, and Jeffrey Wilcke.

A public crowdsale from July to September 2014 raised about 31,500 BTC,
then worth about US$18 million. The network launched with the Frontier
release on 30 July 2015.

### The DAO and Ethereum Classic

The DAO, an investment fund run by smart contract, raised about 12 million
ETH in 2016. On 17 June 2016 an attacker exploited a reentrancy bug and
drained about 3.6 million ETH. On 20 July 2016, at block 1,920,000, the
network hard-forked to return the funds to their owners. A minority that
rejected the fork kept running the original chain, which became Ethereum
Classic (ETC).

### Move to proof of stake

The Beacon Chain, a separate proof-of-stake chain, launched on 1 December
2020. On 15 September 2022, in an upgrade called the Merge, Ethereum's
original execution chain switched its consensus to the Beacon Chain and
stopped using proof of work. The Ethereum Foundation estimated the change
cut the network's energy use by about 99.95%. Staked ETH became
withdrawable with the Shapella upgrade on 12 April 2023.

### Rollup-centric roadmap

In October 2020 Buterin proposed that Ethereum scale mainly through layer
2 rollups, such as [Arbitrum](arbitrum.md), rather than on the base layer
itself.[^rollup-roadmap] Later upgrades followed that plan. Dencun (March
2024) added "blobs", a cheaper data type for rollups
(EIP-4844).[^eip4844] Pectra (May 2025) raised blob capacity and let
ordinary accounts delegate to smart contract code
(EIP-7702).[^eip7702] Fusaka (December 2025) introduced PeerDAS, which
lets nodes verify blob data by sampling it rather than downloading all of
it.

### Exchange-traded products

The US SEC approved exchange rule changes for spot ether exchange-traded
products on 23 May 2024. They began trading on 23 July 2024.

## Technology

Ethereum uses an account model. Externally owned accounts are controlled
by private keys; contract accounts are controlled by their code. Every
operation in the EVM costs gas, paid in ETH.

Since the London upgrade in August 2021 (EIP-1559), each block has a base
fee that is burned and an optional priority fee paid to the block
proposer.[^eip1559] As a result ETH supply can shrink when network
activity is high.

Consensus is Gasper, which combines the Casper FFG finality gadget with
the LMD-GHOST fork-choice rule. Time is split into 12-second slots and
32-slot epochs. A node runs two pieces of software: an execution client
(such as Geth, Nethermind, Besu, Erigon, or Reth) and a consensus client
(such as Prysm, Lighthouse, Teku, Nimbus, Lodestar, or Grandine). Having
several independent clients is a deliberate design goal.

Protocol changes are proposed as Ethereum Improvement Proposals (EIPs)
and agreed in public All Core Developers calls.[^eips]

## Incidents and controversies

- **The DAO fork (2016).** See [above](#the-dao-and-ethereum-classic).
- **Parity multisig (2017).** In July 2017 a bug in the Parity wallet let
  an attacker steal about 150,000 ETH. In November 2017 a user
  accidentally triggered a second bug that froze about 514,000 ETH
  permanently.
- **Staking centralization.** A large share of staked ETH is held through
  a few liquid staking providers and exchanges, which raises concerns
  about concentration of validator power.

## Timeline

| Date | Event |
|---|---|
| 2013 | Whitepaper circulated |
| 2014-07 | Crowdsale begins |
| 2015-07-30 | Mainnet launch (Frontier) |
| 2016-03-14 | Homestead upgrade |
| 2016-06-17 | The DAO exploited |
| 2016-07-20 | DAO hard fork; Ethereum Classic continues original chain |
| 2020-12-01 | Beacon Chain launches |
| 2021-08-05 | London upgrade (EIP-1559) |
| 2022-09-15 | The Merge: switch to proof of stake |
| 2023-04-12 | Shapella: staking withdrawals enabled |
| 2024-03-13 | Dencun: blobs (EIP-4844) |
| 2024-07-23 | US spot ether ETPs begin trading |
| 2025-05-07 | Pectra upgrade |
| 2025-12 | Fusaka upgrade (PeerDAS) |

## See also

- [Bitcoin](bitcoin.md)
- [Arbitrum](arbitrum.md)

## References

[^whitepaper]: Buterin, V. *Ethereum Whitepaper*. <https://ethereum.org/en/whitepaper/>
[^yellowpaper]: Wood, G. *Ethereum: A Secure Decentralised Generalised Transaction Ledger*. <https://ethereum.github.io/yellowpaper/paper.pdf>
[^rollup-roadmap]: Buterin, V. (2020). *A rollup-centric ethereum roadmap*. <https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698>
[^eip1559]: EIP-1559: Fee market change for ETH 1.0 chain. <https://eips.ethereum.org/EIPS/eip-1559>
[^eip4844]: EIP-4844: Shard Blob Transactions. <https://eips.ethereum.org/EIPS/eip-4844>
[^eip7702]: EIP-7702: Set Code for EOAs. <https://eips.ethereum.org/EIPS/eip-7702>
[^eips]: Ethereum Improvement Proposals. <https://eips.ethereum.org>
