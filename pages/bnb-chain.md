---
title: BNB Chain
ticker: BNB
category: Layer 1
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# BNB Chain

BNB Chain is a blockchain ecosystem that includes BNB Smart Chain (BSC),
opBNB, and the Greenfield storage network. BSC supports Ethereum Virtual
Machine-compatible smart contracts and uses BNB for execution fees and
staking. The ecosystem also previously included BNB Beacon Chain, whose
functions were migrated through the Chain Fusion programme.[^ecosystem][^bsc][^fusion]

| | |
|---|---|
| Native asset | BNB |
| Smart-contract base chain | BNB Smart Chain |
| BSC consensus | Proof of Staked Authority |
| Other components | opBNB and BNB Greenfield |
| Retired component | BNB Beacon Chain |

## Execution and validators

BSC is a separate blockchain with its own validators, even though its
execution environment supports Ethereum tooling. Its consensus combines
stake-based validator selection with a limited set of authorities taking
turns to produce blocks. EVM compatibility does not mean that Ethereum
validators secure BSC transactions.[^bsc]

As of October 2026, the validator documentation describes daily elections
for 45 active validators: 21 Cabinets and 24 Candidates. Each epoch draws
18 from the first group and three from the second to form the
21-validator consensus set. Staking rank therefore influences both
selection and participation; “45 active validators” does not mean all
45 produce blocks in every epoch.[^validators]

## Chain Fusion

Chain Fusion moved Beacon Chain functionality to BSC and retired Beacon
Chain. Native staking on BSC allows delegators to stake without first
moving BNB to the older network. The current architecture should therefore
be distinguished from earlier descriptions of two simultaneously active
chains dividing execution from staking and governance.[^fusion][^staking]

The post-Fusion documentation describes the shutdown of Beacon Chain
transaction processing and its normal cross-chain communication with BSC.
Recovery of eligible remaining assets uses a separate migration process.
It explicitly warns that BEP-2 or BEP-8 assets not bound or mirrored to BSC
cannot be recovered through that process.[^recovery]

## Security incidents and upgrades

In an October 2022 incident, an attacker exploited BSC Token Hub, the
bridge between Beacon Chain and BSC. BNB Chain's account reported
2 million BNB withdrawn through forged proofs. The team said it contacted
validators individually to coordinate a suspension of BSC. The incident
demonstrated both a bridge-verification failure and the network's ability
to coordinate an emergency halt.[^incident]

BNB Chain's August 2026 upgrade announcement described Fermi as having
reduced BSC's block interval to 0.45 seconds, followed by Osaka/Mendel
changes intended to improve operation at that pace. It scheduled Pasteur
for 25 August, with changes to bridge signature verification, validator
key rotation, and block utilisation. The announcement's throughput
figures were testnet benchmarks, not measurements of ordinary mainnet
traffic.[^pasteur]

## Governance and dependencies

The validator set, staking rules, and bridge verification are separate
parts of the system's security. Fast blocks and compatibility with
Ethereum applications do not remove those dependencies. The 2022 bridge
incident and later verification upgrades provide concrete examples of
why application users must distinguish execution compatibility from
consensus and cross-chain trust.[^bsc][^incident][^pasteur]

## See also

- [Binance](binance.md)
- [Ethereum](ethereum.md)
- [Proof of stake](proof-of-stake.md)
- [Blockchain bridge](blockchain-bridge.md)

## References

[^ecosystem]: BNB Chain. *BNB Chain website*, chain navigation and Beacon Chain sunset status. <https://www.bnbchain.org/en>
[^bsc]: BNB Chain documentation. *BSC introduction*. <https://docs.bnbchain.org/bnb-smart-chain/introduction/>
[^validators]: BNB Chain documentation. *BSC Validator Overview*. <https://docs.bnbchain.org/bnb-smart-chain/validator/overview/>
[^fusion]: BNB Chain documentation. *BNB Chain Fusion*. <https://docs.bnbchain.org/bc-fusion/>
[^staking]: BNB Chain documentation. *Staking*. <https://docs.bnbchain.org/bc-fusion/validators/staking/>
[^recovery]: BNB Chain documentation. *Post-Fusion FAQ*. <https://docs.bnbchain.org/bc-fusion/post-fusion/faq/>
[^incident]: BNB Chain (2022-10-07). *BNB Chain Ecosystem Update*. <https://www.bnbchain.org/en/blog/bnb-chain-ecosystem-update>
[^pasteur]: BNB Chain (2026-08-14). *Pasteur Hardfork Arrives on BSC Mainnet on August 25*. <https://www.bnbchain.org/en/blog/pasteur-hardfork-arrives-on-bsc-mainnet-on-august-25>
