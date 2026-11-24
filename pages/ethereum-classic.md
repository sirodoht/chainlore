---
title: Ethereum Classic
ticker: ETC
category: Layer 1
status: draft
updated: 2026-11-24
written_by: claude-haiku-5-5 (high effort)
---

| Field | Detail |
| --- | --- |
| Ticker | ETC[^5] |
| Consensus | Proof of work[^3][^4] |
| Fork block | 1920000, reported in a post dated 2016-07-20[^1] |
| Mining at fork completion | Roughly 85% of miners mining the fork, per the Ethereum Foundation post[^1] |
| Proposal process | Ethereum Classic Improvement Proposals (ECIPs)[^4][^5] |
| Notable incident | 51% attack on 2020-07-31[^3] |

## History

The Ethereum Foundation's post dated 20 July 2016 reported that block 1920000 contained an irregular state change. It transferred about 12 million ETH from the “Dark DAO” and “Whitehat DAO” contracts into the WithdrawDAO recovery contract. The post said roughly 85% of miners were mining the fork at completion.[^1]

The post said the recovery contract was returning ether to DAO token holders, with about 4.5 million ETH sent so far and about 463,000 ETH under the control of the curator.[^1]

Users who wanted to follow the unchanged chain were told to run with the --oppose-dao-fork flag and to guard against transaction replay attacks.[^1]

The Ethereum Classic website republishes the Foundation's post. It describes its content as user-generated and solely for informational purposes, and states there is “no official anything” in Ethereum Classic.[^2] The sources reviewed do not describe a formal organisational relationship between Ethereum Classic and the Ethereum Foundation beyond this reprint.[^1][^2]

## Technology

Ethereum Classic uses proof-of-work mining, so the security of its history depends on the mining power an attacker can obtain.[^3][^4] Bitquery describes proof-of-work finality as probabilistic rather than certain.[^3]

ECIP-1100, titled Modified Exponential Subjective Scoring (MESS), was created on 2020-09-09. Its stated motivation was that low hashrate had caused Ethereum Classic's consensus algorithms to yield inconvenient and undesirable finality rates.[^4]

- The proposal described a subjective rule for choosing between chain segments. It used a cubic curve to require a proposed segment to exceed the local segment by a time-dependent total difficulty ratio.[^4]
- The proposal stated that the rule falls outside the existing consensus protocol, so it would need consistent implementation across clients.[^4]
- The ECIP page records that ECIP-1100 was replaced with ECBP-1110 in January 2024.[^4]

## Governance

Protocol proposals are published as Ethereum Classic Improvement Proposals (ECIPs). Proposals are grouped by category, and each proposal page shows a status; the ECIP-1100 page, for example, lists the category ECBP and the status Replaced.[^imp-60-6]

A May 2026 community call discussed Olympia, a proposal described by a speaker as routing transaction fees into a treasury. Speakers described the proposal as contested and said there was no clear consensus behind it.[^5]

The call page states that F2Pool and 2Miners signed the nolympia.dev petition against Olympia, joining Antpool, and that these pools put roughly 80% of ETC hashrate on record opposing it.[^imp-60-8] The petition page lists F2Pool, 2Miners and Antpool among its signers.[^imp-60-7] The call page attributes the 80% figure to trustpool.cc, which was not checked for this article.[^imp-60-8]

## Incidents and controversies

### 51% attack, 31 July 2020

On 31 July 2020, one miner mined more than 3,500 blocks in secret, forming a fork that ran from block 10904146 to block 10907740. The miner kept the blocks private and then broadcast them. Because the secret chain carried more work, the network accepted it, replacing 12 hours of history.[^3]

- Bitquery reports that the attacker needed more than half of the network's mining power to sustain the attack for 12 hours.[^3]
- Bitquery estimates the rented hash power cost about 17.5 BTC, or about $170,000 at the time.[^3]
- Bitquery concludes the attack was deliberate and that the miner rented hash power from outside sources.[^3]
- Some transfers made in the 12-hour window are missing from the new chain, and honest miners lost rewards for blocks mined during the attack.[^3]

Node software did not respond the same way. According to Bitquery, Geth and Hyperledger Besu nodes accepted the attacker's blocks, while Open Ethereum nodes stayed on the old chain, which split the network.[^3]

## Timeline

| Date | Event |
| --- | --- |
| 2016-07-20 | The Ethereum Foundation post reports the completed hard fork. Block 1920000 moved about 12 million ETH from the Dark DAO and Whitehat DAO contracts into the WithdrawDAO recovery contract.[^1] |
| 2020-07-31 | One miner replaces 12 hours of Ethereum Classic history with a secret chain of more than 3,500 blocks.[^3] |
| 2020-09-09 | ECIP-1100 (MESS) is created.[^4] |
| 2024-01 | ECIP-1100 is replaced with ECBP-1110.[^4] |

## References

[^1]: [Hard Fork Completed | Ethereum Foundation Blog](https://blog.ethereum.org/2016/07/20/hard-fork-completed)
[^2]: [The DAO Hard Fork Completed - Ethereum Classic](https://ethereumclassic.org/blog/2016-07-20-new-ethereum-dao-hard-fork-completed/)
[^3]: [Ethereum Classic 51% Chain Attack July 31, 2020 - Bitquery](https://bitquery.io/blog/ethereum-classic-51-chain-attack-july-31-2020)
[^4]: [MESS (Modified Exponential Subjective Scoring)](https://ecips.ethereumclassic.org/ECIPs/ecip-1100)
[^5]: [ETCCC 52 - Nolympia](https://cc.ethereumclassic.org/calls/52/)

[^imp-60-6]: [MESS (Modified Exponential Subjective Scoring)](https://ecips.ethereumclassic.org/ECIPs/ecip-1100)
[^imp-60-7]: [Nolympia - Petition against the Olympia Treasury proposal for Ethereum Classic](https://nolympia.dev/)
[^imp-60-8]: [ETCCC 52 - Nolympia](https://cc.ethereumclassic.org/calls/52/)
