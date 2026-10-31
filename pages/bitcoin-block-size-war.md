---
title: Bitcoin block size war
ticker: None
category: History
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Bitcoin block size war

The Bitcoin block size war was a dispute over how to increase Bitcoin's
transaction capacity and who could authorise changes to its rules.
Proposals in 2015–2017 ranged from larger blocks through a hard fork
to Segregated Witness and payment-channel scaling. The disagreements
concerned both technical limits and the authority of miners, businesses,
developers, and users.[^bip101][^roadmap][^opposition]

| | |
|---|---|
| Central issue | Capacity, verification costs, and rule changes |
| Larger-block proposal | BIP 101 |
| Soft-fork upgrade | Segregated Witness, BIP 141 |
| Bitcoin Cash split | 1 August 2017 |
| SegWit activation | 24 August 2017 |
| SegWit2x suspension | November 2017 |

## Competing priorities

Gavin Andresen's June 2015 BIP 101 proposed replacing the one-megabyte
limit with an initial eight-megabyte limit and scheduled growth. Its
motivation was to prevent limited transaction capacity from constraining
Bitcoin adoption. The specification proposed a hard fork, requiring
participating software to accept blocks that older rules would
reject.[^bip101]

Gregory Maxwell's December 2015 roadmap emphasised the cost of
independent validation. He argued that excessive resource requirements
could force users to trust intermediaries, while insufficient capacity
could also make direct access too expensive. His proposed approach
combined efficiency improvements, SegWit, and mechanisms such as
payment channels.[^roadmap]

## SegWit and activation

BIP 141 separates witness data, including signatures, from the
traditional transaction structure while committing to it within the
block. Its block-weight rule discounts witness bytes and caps weight
at four million units. This increases effective capacity without being
a simple fourfold increase in the number of transactions. It also
addresses transaction malleability for supported transactions, helping
protocols that depend on stable transaction identifiers.[^bip141]

Activation itself became contentious. BIP 148 specified that enforcing
nodes would reject blocks without the required SegWit signal from
1 August 2017 until lock-in, subject to its activation conditions.
BIP 91 offered miner coordination using an 80% threshold to require
that signal. SegWit ultimately activated on 24 August 2017 at block
481,824.[^bip148][^bip91][^activation]

## The forks and agreements

The May 2017 New York Agreement, published by Digital Currency Group,
combined support for SegWit with a two-megabyte hard fork within six
months. Bitcoin.org opposed the resulting SegWit2x proposal and argued
that miner support could not alone redefine Bitcoin. Its objections
included coin naming, replay risks, and treatment of customer
balances.[^nya][^opposition]

Bitcoin Cash split from Bitcoin on 1 August 2017. Its project website
presents that split as a decision to pursue onchain scaling for
low-cost everyday payments. It became a separate network rather than
an agreed change applied to all Bitcoin users.[^cash]

The SegWit2x hard-fork effort was suspended in November 2017. In a
contemporaneous statement, BitPay's Stephen Pair said its participation
had aimed to reconcile the community, but that proceeding amid division
would be harmful; he subsequently recorded supporters suspending the
effort. The outcome left SegWit active on Bitcoin and Bitcoin Cash
following a separate scaling path.[^pair][^activation][^cash]

## See also

- [Bitcoin](bitcoin.md)
- [Lightning Network](lightning-network.md)
- [Proof of work](proof-of-work.md)

## References

[^bip101]: Andresen, G. (2015). *BIP 101: Increase maximum block size*. <https://bips.dev/101/>
[^roadmap]: Maxwell, G. (2015-12-07). *Capacity increases Roadmap for the Bitcoin system*. <https://bitcoincore.org/en/2015/12/07/roadmap/>
[^bip141]: Lombrozo, E., Lau, J., and Wuille, P. *BIP 141: Segregated Witness (Consensus layer)*. <https://bips.dev/141/>
[^bip148]: Shaolin Fry (2017). *BIP 148: Mandatory activation of segwit deployment*. <https://bips.dev/148/>
[^bip91]: Hilliard, J. (2017). *BIP 91: Reduced threshold Segwit MASF*. <https://bips.dev/91/>
[^activation]: Blockstream (2017-10-12). *The Status of SegWit at Blockstream*. <https://blog.blockstream.com/en-the-status-of-segwit-at-blockstream/>
[^nya]: Digital Currency Group (2017-05-23). *Bitcoin Scaling Agreement at Consensus 2017*. <https://dcgco.medium.com/bitcoin-scaling-agreement-at-consensus-2017-133521fe9a77>
[^opposition]: Bitcoin.org (2017). *Bitcoin.org to denounce “Segwit2x”*. <https://bitcoin.org/en/posts/denounce-segwit2x>
[^cash]: Bitcoin Cash. *Peer-to-Peer Electronic Cash*, project history. <https://bitcoincash.org/>
[^pair]: Pair, S. (2017-11-08). *Segwit2x Should Be Canceled*, including subsequent update. <https://medium.com/@spair/segwit2x-should-be-canceled-b7399c767d34>
