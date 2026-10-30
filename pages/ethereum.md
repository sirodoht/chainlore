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
Since September 2022 it has used proof of stake.[^history]

| | |
|---|---|
| Ticker | ETH |
| Type | Smart contract platform, layer 1 blockchain |
| Proposed by | Vitalik Buterin |
| Whitepaper | 2013-11-27 |
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

Vitalik Buterin described Ethereum in a whitepaper circulated on 27
November 2013 and announced it publicly in January 2014.[^history][^whitepaper]
Gavin Wood wrote the formal specification, the Yellow Paper, published
on 1 April 2014.[^yellowpaper] The founders also included Charles
Hoskinson, Anthony Di Iorio, Mihai Alisie, Joseph Lubin, Amir Chetrit,
and Jeffrey Wilcke.

A public crowdsale from 22 July to 2 September 2014 raised about 31,500
BTC, then worth about US$18 million.[^crowdsale] The network launched
with the Frontier release on 30 July 2015.

### The DAO and Ethereum Classic

The DAO, an investment fund run by smart contract, raised about 12.7
million ETH in 2016. On 17 June 2016 an attacker exploited a reentrancy
bug and drained about 3.6 million ETH. On 20 July 2016, at block
1,920,000, the network hard-forked to return the funds to their owners.
A minority that rejected the fork kept running the original chain, which
became Ethereum Classic (ETC).[^dao][^history]

### Move to proof of stake

The Beacon Chain, a separate proof-of-stake chain, launched on 1 December
2020. On 15 September 2022, in an upgrade called the Merge, Ethereum's
original execution chain switched its consensus to the Beacon Chain and
stopped using proof of work. The change cut the network's energy use by
about 99.95%.[^merge] Staked ETH became withdrawable with the Shapella
upgrade on 12 April 2023.[^history]

### Rollup-centric roadmap

In October 2020 Buterin proposed that Ethereum scale mainly through layer
2 rollups, such as [Arbitrum](arbitrum.md), rather than on the base layer
itself.[^rollup-roadmap] Later upgrades followed that plan. Dencun (March
2024) added "blobs", a cheaper data type for rollups
(EIP-4844).[^eip4844] Pectra (May 2025) raised blob capacity (EIP-7691)
and let ordinary accounts delegate to smart contract code
(EIP-7702).[^eip7702] Fusaka (3 December 2025) introduced PeerDAS
(EIP-7594), which lets nodes verify blob data by sampling it rather than
downloading all of it.[^fusaka]

Fusaka also allowed blob capacity to be raised by small
"blob-parameter-only" (BPO) forks without a full upgrade. BPO1 (9
December 2025) raised the target and maximum blobs per block from 6/9 to
10/15, and BPO2 (7 January 2026) raised them to 14/21.[^fusaka]

The next named upgrade, Glamsterdam, includes enshrined proposer-builder
separation (EIP-7732) and block-level access lists (EIP-7928). It went
live on the Sepolia testnet on 6 October 2026.[^glamsterdam] Its
deployment to the Hoodi testnet, planned for 26 October, was postponed
after auditors flagged risks to existing contracts in two of its
proposals. As of 30 October 2026 it has no mainnet date.[^glamsterdam-delay]

### Exchange-traded products

The US SEC approved exchange rule changes for spot ether exchange-traded
products on 23 May 2024.[^etf-approval] They began trading on 23 July
2024.[^etf-trading] On 6 October 2025 Grayscale's ether funds began
staking, the first US-listed spot crypto ETPs to do so.[^etf-staking]

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
several independent clients is a deliberate design goal.[^clients]

Protocol changes are proposed as Ethereum Improvement Proposals (EIPs)
and agreed in public All Core Developers calls.[^eips]

## Incidents and controversies

- **The DAO fork (2016).** See [above](#the-dao-and-ethereum-classic).
- **Parity multisig (2017).** In July 2017 a bug in the Parity wallet let
  an attacker steal about 150,000 ETH.[^parity] In November 2017 a user
  accidentally triggered a second bug that froze about 514,000 ETH
  permanently.
- **Bybit hack (2025).** On 21 February 2025 attackers stole about US$1.5
  billion in ETH and staked ETH from the exchange Bybit's Ethereum
  multisig cold wallet, the largest crypto theft on record. The FBI
  attributed it to North Korea.[^bybit]
- **Staking centralization.** A large share of staked ETH is held through
  a few liquid staking providers and exchanges, which raises concerns
  about concentration of validator power.

## Timeline

| Date | Event |
|---|---|
| 2013-11-27 | Whitepaper circulated |
| 2014-04-01 | Yellow Paper published |
| 2014-07-22 | Crowdsale begins |
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
| 2025-02-21 | Bybit hack |
| 2025-05-07 | Pectra upgrade |
| 2025-10-06 | First US spot ether ETPs begin staking |
| 2025-12-03 | Fusaka upgrade (PeerDAS) |
| 2025-12-09 | BPO1: blobs raised to 10/15 |
| 2026-01-07 | BPO2: blobs raised to 14/21 |
| 2026-10-06 | Glamsterdam live on Sepolia testnet |

## See also

- [Bitcoin](bitcoin.md)
- [Arbitrum](arbitrum.md)

## References

[^history]: ethereum.org. *The history of Ethereum*. <https://ethereum.org/en/history/>
[^whitepaper]: Buterin, V. *Ethereum Whitepaper*. <https://ethereum.org/en/whitepaper/>
[^yellowpaper]: Wood, G. *Ethereum: A Secure Decentralised Generalised Transaction Ledger*. <https://ethereum.github.io/yellowpaper/paper.pdf>
[^crowdsale]: Ethereum Foundation (2014). *Launching the Ether Sale*. <https://blog.ethereum.org/2014/07/22/launching-the-ether-sale>
[^dao]: *The DAO*. Wikipedia. <https://en.wikipedia.org/wiki/The_DAO>
[^merge]: ethereum.org. *The Merge*. <https://ethereum.org/en/roadmap/merge/>
[^rollup-roadmap]: Buterin, V. (2020). *A rollup-centric ethereum roadmap*. <https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698>
[^eip1559]: EIP-1559: Fee market change for ETH 1.0 chain. <https://eips.ethereum.org/EIPS/eip-1559>
[^eip4844]: EIP-4844: Shard Blob Transactions. <https://eips.ethereum.org/EIPS/eip-4844>
[^eip7702]: EIP-7702: Set Code for EOAs. <https://eips.ethereum.org/EIPS/eip-7702>
[^fusaka]: Ethereum Foundation (2025). *Fusaka Mainnet Announcement*. <https://blog.ethereum.org/2025/11/06/fusaka-mainnet-announcement>
[^glamsterdam]: Ethereum Foundation (2026). *Glamsterdam Testnet Announcement*. <https://blog.ethereum.org/2026/09/17/glamsterdam-testnet-announcement>
[^glamsterdam-delay]: CoinDesk (2026). *Ethereum delays Glamsterdam test after security devs flag risk to existing contracts*. <https://www.coindesk.com/tech/2026/10/23/ethereum-delays-glamsterdam-test-after-security-devs-flag-risk-to-existing-contracts>
[^etf-approval]: Fortune (2024). *SEC completes abrupt U-turn to approve Ethereum ETFs*. <https://www.fortune.com/crypto/2024/05/23/sec-completes-abrupt-u-turn-to-approve-ethereum-etfs-in-politically-driven-move>
[^etf-trading]: Baker McKenzie (2024). *Ethereum ETFs to start trading today in the United States*. <https://blockchain.bakermckenzie.com/2024/07/23/ethereum-etfs-to-start-trading-today-in-the-united-states/>
[^etf-staking]: Grayscale (2025). Press release, 6 October 2025. <https://www.sec.gov/Archives/edgar/data/1725210/000119312525231048/press_release_10.6.2025.htm>
[^parity]: OpenZeppelin (2017). *On the Parity Wallet Multisig Hack*. <https://www.openzeppelin.com/news/on-the-parity-wallet-multisig-hack-405a8c12e8f7>
[^bybit]: BleepingComputer (2025). *FBI confirms Lazarus hackers were behind $1.5B Bybit crypto heist*. <https://www.bleepingcomputer.com/news/security/fbi-confirms-lazarus-hackers-were-behind-15b-bybit-crypto-heist/>
[^clients]: ethereum.org. *Nodes and clients*. <https://ethereum.org/en/developers/docs/nodes-and-clients/>
[^eips]: Ethereum Improvement Proposals. <https://eips.ethereum.org>
