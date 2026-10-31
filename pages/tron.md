---
title: TRON
ticker: TRX
category: Layer 1
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# TRON

TRON is a blockchain for transfers and smart contracts, with TRX as its
native resource and governance asset. Its delegated-proof-of-stake system
elects 27 block producers called Super Representatives. The network
meters transaction data and contract computation through separate
resources called Bandwidth and Energy.[^sr][^resources]

| | |
|---|---|
| Native asset | TRX |
| Founder | Justin Sun[^history] |
| Mainnet launch | 31 May 2018, according to TRON's history[^history] |
| Consensus | Delegated proof of stake |
| Active block producers | 27 Super Representatives |
| Contract execution | TRON Virtual Machine, or TVM[^resources] |

## Resources and staking

Bandwidth accounts for the size of a transaction stored onchain. Energy
accounts for computation performed by the TVM during a contract call.
Transactions can consume available resources or fall back on burning TRX
to pay the applicable resource charges. A token transfer that invokes a
contract therefore has different resource requirements from a simple
native-asset transfer.[^resources]

Stake 2.0 became active on 7 April 2023. Under the resource configuration
described in TRON's documentation as of October 2026, staking TRX provides
Bandwidth or Energy together with TRON Power, the weight used in
Super Representative elections. Resource entitlements are proportional
to the relevant network-wide stake, rather than a permanently fixed
amount of computation per TRX.[^stake]

## Governance

Candidates are ranked by votes at maintenance updates, normally six hours
apart. The top 27 produce blocks; the next 100 occupy the Super
Representative Partner tier. Producing blocks, receiving voting rewards,
and having an approval count toward a governance proposal are distinct
roles. Protocol parameters, including rewards, can change through
onchain proposals.[^sr]

This design makes the distribution of votes and control of elected
producers relevant to governance. Holding TRX alone does not make an
account a block producer: the account must participate in the staking,
voting, or candidacy mechanisms appropriate to its role.[^sr][^stake]

## Stablecoin use

Tether announced its TRON integration in March 2019, using the TRC-20
token format for USDT. The integration allows the issued stablecoin to
interact with TRON contracts and applications; USDT remains a different
asset from TRX.[^tether]

Circle announced in February 2024 that it was ending support for USDC on
TRON and immediately stopped minting there. It offered Circle Mint
customers a transition period through February 2025. Circle attributed
the decision to its company-wide risk assessment, illustrating that an
issuer's support for a chain can change independently of the chain's
continued operation.[^circle]

## Regulatory proceedings

The US Securities and Exchange Commission brought proceedings involving
Sun and related companies in 2023. Its amended complaint alleged, among
other matters, that Rainberry facilitated wash trading in TRX during
2018–2019. These were the regulator's allegations, not admissions by the
defendants.[^sec]

In March 2026 the SEC proposed a settlement under which Rainberry would
pay $10 million, without admitting or denying the settled allegations,
and the remaining claims against the TRON defendants would be dismissed
with prejudice. The court entered final judgment on 9 March, ordering
Rainberry to pay that penalty. The penalty was imposed on Rainberry,
not on holders of TRX.[^sec][^judgment]

## See also

- [Tether](tether.md)
- [USDC](usdc.md)
- [Proof of stake](proof-of-stake.md)
- [Smart contract](smart-contract.md)

## References

[^sr]: TRON developer documentation. *Super Representatives*. <https://developers.tron.network/docs/super-representatives>
[^resources]: TRON developer documentation. *Resource Model*. <https://developers.tron.network/docs/resource-model>
[^history]: TRON. *About TRON: milestones*. <https://tron.network/about>
[^stake]: TRON developer documentation. *Stake 2.0 overview*. <https://developers.tron.network/docs/staking-on-tron-network>
[^tether]: Tether (2019-03-04). *USDT Introduced to TRON Blockchain*. <https://tether.io/news/usdt-introduced-to-tron-blockchain/>
[^circle]: Circle (2024-02-21). *Circle is Discontinuing Support for USDC on the TRON Blockchain*. <https://www.circle.com/blog/circle-is-discontinuing-support-for-usdc-on-the-tron-blockchain>
[^sec]: SEC (2026-03-05). *Litigation Release No. 26496*. <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26496>
[^judgment]: US District Court, Southern District of New York (2026-03-09). *SEC v. Sun et al.*, No. 1:23-cv-02433, document 98, final judgment. <https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv02433/596044/98/>
