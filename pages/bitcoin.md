---
title: Bitcoin
ticker: BTC
category: Layer 1
status: draft
updated: 2026-10-30
---

# Bitcoin

**Bitcoin** (BTC) is a decentralized digital currency and the first
cryptocurrency. It was described in a 2008 whitepaper by the pseudonymous
Satoshi Nakamoto and launched in January 2009. Bitcoin uses proof of work
to order transactions in a public ledger, the blockchain, without a
central authority. Its supply is capped at 21 million BTC.[^whitepaper]

| | |
|---|---|
| Ticker | BTC |
| Type | Cryptocurrency, layer 1 blockchain |
| Creator | Satoshi Nakamoto (pseudonym) |
| Whitepaper | 2008-10-31 |
| Genesis block | 2009-01-03 |
| Consensus | Proof of work (double SHA-256) |
| Target block time | 10 minutes |
| Difficulty adjustment | Every 2,016 blocks |
| Supply cap | 21,000,000 BTC |
| Block subsidy | 3.125 BTC (since 2024-04-20) |
| Smallest unit | 1 satoshi = 0.00000001 BTC |
| Reference client | Bitcoin Core |
| License | MIT |
| Live data | [mempool.space](https://mempool.space) |

## History

### Origins

On 31 October 2008 Satoshi Nakamoto published the whitepaper *Bitcoin: A
Peer-to-Peer Electronic Cash System* to the Cryptography Mailing
List.[^whitepaper] The genesis block was mined on 3 January 2009. Its
coinbase transaction contains the text "The Times 03/Jan/2009 Chancellor
on brink of second bailout for banks", a headline from *The Times* of
London.[^genesis] The first version of the software was released days
later, and the first transaction between two people, from Nakamoto to Hal
Finney, was included in block 170 on 12 January 2009.

On 22 May 2010 Laszlo Hanyecz paid 10,000 BTC for two pizzas, the first
widely known purchase of physical goods with bitcoin. The date is
celebrated as Bitcoin Pizza Day.

Nakamoto stopped participating publicly in late 2010 and was last heard
from in private correspondence in 2011. Their identity remains unknown.

### Value overflow incident

On 15 August 2010 a bug allowed block 74,638 to create about 184 billion
BTC. Developers released a fix within hours, and the chain was
reorganized to exclude the invalid transaction.[^cve-2010-5139]

### Block size war and SegWit

From 2015 to 2017 the community split over how to scale transaction
capacity. One side favoured raising the 1 MB block size limit; the other
favoured Segregated Witness (SegWit) and off-chain layers. SegWit
activated as a soft fork on 24 August 2017 at block
481,824.[^bip141] Earlier that month, on 1 August 2017, a group favouring
larger blocks forked the chain to create Bitcoin Cash.

### Taproot

Taproot, a soft fork adding Schnorr signatures and more private, more
efficient scripts, activated on 14 November 2021 at block
709,632.[^bip340][^bip341]

### Institutional adoption

El Salvador made bitcoin legal tender on 7 September 2021, the first
country to do so. In January 2025 its legislature amended the law to make
acceptance voluntary. On 10 January 2024 the US Securities and Exchange
Commission approved the first spot bitcoin exchange-traded products, which
began trading the next day. On 6 March 2025 a US executive order created a
Strategic Bitcoin Reserve.

## Technology

Transactions are grouped into blocks. Miners compete to find a block
header whose double SHA-256 hash is below a target; the first to do so
earns the block subsidy plus transaction fees. Nodes follow the valid
chain with the most accumulated proof of work. The difficulty target is
recalculated every 2,016 blocks so that blocks arrive about every ten
minutes.

Bitcoin uses an unspent transaction output (UTXO) model and a deliberately
limited, non-Turing-complete scripting language, Script. Since SegWit,
block size is measured in weight units, with a limit of 4 million.

Changes to the protocol are proposed as Bitcoin Improvement Proposals
(BIPs).[^bips] There is no formal governance; changes require broad
adoption by node operators, miners, and users. Most nodes run Bitcoin
Core. Alternative clients include Bitcoin Knots and btcd.

Second-layer systems include the Lightning Network, a network of payment
channels proposed by Joseph Poon and Thaddeus Dryja in
2015.[^lightning]

## Supply

New bitcoin enters circulation only through the block subsidy. The
subsidy started at 50 BTC and halves every 210,000 blocks, about every
four years, so total supply approaches but never exceeds 21 million.

| Halving | Date | Block | Subsidy after |
|---|---|---|---|
| 1 | 2012-11-28 | 210,000 | 25 BTC |
| 2 | 2016-07-09 | 420,000 | 12.5 BTC |
| 3 | 2020-05-11 | 630,000 | 6.25 BTC |
| 4 | 2024-04-20 | 840,000 | 3.125 BTC |
| 5 | about 2028 | 1,050,000 | 1.5625 BTC |

## Incidents and controversies

- **Mt. Gox (2014).** Mt. Gox, then the largest bitcoin exchange, halted
  withdrawals and filed for bankruptcy in February 2014 after losing
  about 850,000 BTC.
- **Block size war (2015–2017).** See [above](#block-size-war-and-segwit).
- **Energy use.** Proof-of-work mining consumes large amounts of
  electricity, a recurring point of criticism.
- **Ordinals and OP_RETURN (2023–2025).** The Ordinals protocol, launched
  in January 2023, made it possible to inscribe arbitrary data in
  transactions, which reopened the debate about what block space is for.
  The debate intensified in 2025 when Bitcoin Core 30 relaxed its default
  limit on `OP_RETURN` data, and some node operators switched to Bitcoin
  Knots in protest.

## Timeline

| Date | Event |
|---|---|
| 2008-08-18 | bitcoin.org domain registered |
| 2008-10-31 | Whitepaper published |
| 2009-01-03 | Genesis block mined |
| 2009-01-12 | First transaction, Nakamoto to Hal Finney (block 170) |
| 2010-05-22 | 10,000 BTC paid for two pizzas |
| 2010-08-15 | Value overflow incident (block 74,638) |
| 2012-11-28 | First halving |
| 2014-02 | Mt. Gox collapses |
| 2017-08-01 | Bitcoin Cash fork |
| 2017-08-24 | SegWit activates (block 481,824) |
| 2021-09-07 | El Salvador makes bitcoin legal tender |
| 2021-11-14 | Taproot activates (block 709,632) |
| 2023-01 | Ordinals launched |
| 2024-01-10 | US SEC approves spot bitcoin ETPs |
| 2024-04-20 | Fourth halving |
| 2025-03-06 | US Strategic Bitcoin Reserve created |

## See also

- [Ethereum](ethereum.md)

## References

[^whitepaper]: Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. <https://bitcoin.org/bitcoin.pdf>
[^genesis]: Genesis block `000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`. <https://mempool.space/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f>
[^cve-2010-5139]: CVE-2010-5139. <https://en.bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures>
[^bip141]: BIP 141: Segregated Witness (Consensus layer). <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>
[^bip340]: BIP 340: Schnorr Signatures for secp256k1. <https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki>
[^bip341]: BIP 341: Taproot: SegWit version 1 spending rules. <https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki>
[^bips]: Bitcoin Improvement Proposals repository. <https://github.com/bitcoin/bips>
[^lightning]: Poon, J. and Dryja, T. (2016). *The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments*. <https://lightning.network/lightning-network-paper.pdf>
