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
central authority.[^whitepaper] Its supply is capped at 21 million
BTC.[^max-money]

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
List.[^announcement] The genesis block was mined on 3 January 2009. Its
coinbase transaction contains the text "The Times 03/Jan/2009 Chancellor
on brink of second bailout for banks", a headline from *The Times* of
London.[^chainparams][^genesis] The first version of the software was
released days later, and the first transaction between two people, from
Nakamoto to Hal Finney, was included in block 170 on 12 January 2009.

On 22 May 2010 Laszlo Hanyecz paid 10,000 BTC for two pizzas, the first
widely known purchase of physical goods with bitcoin. The date is
celebrated as Bitcoin Pizza Day.

Nakamoto stopped participating publicly in late 2010 and was last heard
from in private correspondence in 2011. Their identity remains unknown.
Australian computer scientist Craig Wright claimed for years to be
Nakamoto; on 14 March 2024 the High Court of England and Wales ruled that
he is not.[^copa]

### Value overflow incident

On 15 August 2010 a bug allowed block 74,638 to create about 184 billion
BTC.[^cve-2010-5139] A fix was released within about five hours, and the
corrected chain overtook the invalid one at block 74,691.[^overflow]

### Block size war and SegWit

From 2015 to 2017 the community split over how to scale transaction
capacity. One side favoured raising the 1 MB block size limit; the other
favoured Segregated Witness (SegWit) and off-chain layers. SegWit
activated as a soft fork on 24 August 2017 at block
481,824.[^bip141][^chainparams][^segwit-activation] Earlier that month,
on 1 August 2017, a group favouring larger blocks forked the chain to
create Bitcoin Cash.

### Taproot

Taproot, a soft fork adding Schnorr signatures and more private, more
efficient scripts, activated on 14 November 2021 at block
709,632.[^bip340][^bip341]

### Mining migration

In mid-2021 China banned cryptocurrency mining. Global hashrate fell 38%
in June 2021 as miners shut down or moved abroad, and by August 2021 the
United States had the largest share of hashrate, at 35.4%.[^cambridge]

### Institutional adoption

El Salvador made bitcoin legal tender on 7 September 2021, the first
country to do so. On 29 January 2025, under an agreement with the
International Monetary Fund, its legislature amended the law to make
acceptance voluntary and to end tax payments in bitcoin.[^el-salvador]

On 10 January 2024 the US Securities and Exchange Commission approved
the first spot bitcoin exchange-traded products, which began trading the
next day.[^sec-etf] On 6 March 2025 a US executive order declared it US
policy to establish a Strategic Bitcoin Reserve.[^sbr]

Public companies also hold bitcoin as a treasury asset. The largest is
Strategy, formerly MicroStrategy.

### Market

Bitcoin reached an all-time high of about US$126,000 on 6 October 2025.
On 10 October 2025 a market-wide crash caused the largest single day of
liquidations in crypto history.[^oct-2025] For current prices, see live
data sources.

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
four years, so total supply approaches but never exceeds 21
million.[^max-money]

| Halving | Date | Block | Subsidy after |
|---|---|---|---|
| 1 | 2012-11-28 | 210,000 | 25 BTC |
| 2 | 2016-07-09 | 420,000 | 12.5 BTC |
| 3 | 2020-05-11 | 630,000 | 6.25 BTC |
| 4 | 2024-04-20 | 840,000 | 3.125 BTC |
| 5 | about 2028 | 1,050,000 | 1.5625 BTC |

## Incidents and controversies

- **Mt. Gox (2014).** Mt. Gox, then the largest bitcoin exchange, halted
  withdrawals and filed for bankruptcy on 28 February 2014, reporting
  about 850,000 BTC missing. In March 2014 it said it had found about
  200,000 BTC in an old wallet.[^mtgox]
- **Block size war (2015–2017).** See [above](#block-size-war-and-segwit).
- **Energy use.** Proof-of-work mining consumes large amounts of
  electricity, a recurring point of criticism.
- **Ordinals and OP_RETURN (2023–2026).** The Ordinals protocol, launched
  in January 2023, made it possible to inscribe arbitrary data in
  transactions, which reopened the debate about what block space is for.
  The debate intensified in October 2025 when Bitcoin Core 30 raised its
  default limit on `OP_RETURN` data to 100,000 bytes and allowed multiple
  `OP_RETURN` outputs.[^core30] Some node operators switched to Bitcoin
  Knots in protest. On 8 August 2026 nodes enforcing BIP-110, a
  Knots-backed soft fork to restrict data in transactions, split from
  the main chain at block 961,632. With little miner support, the
  minority chain mined two blocks and then stopped.[^bip110]

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
| 2014-02-28 | Mt. Gox files for bankruptcy |
| 2017-08-01 | Bitcoin Cash fork |
| 2017-08-24 | SegWit activates (block 481,824) |
| 2021-06 | China's mining ban; hashrate falls 38% |
| 2021-09-07 | El Salvador makes bitcoin legal tender |
| 2021-11-14 | Taproot activates (block 709,632) |
| 2023-01 | Ordinals launched |
| 2024-01-10 | US SEC approves spot bitcoin ETPs |
| 2024-03-14 | UK High Court rules Craig Wright is not Satoshi Nakamoto |
| 2024-04-20 | Fourth halving |
| 2025-01-29 | El Salvador makes bitcoin acceptance voluntary |
| 2025-03-06 | US executive order on a Strategic Bitcoin Reserve |
| 2025-10-06 | All-time high, about US$126,000 |
| 2025-10-10 | Largest liquidation day in crypto history |
| 2025-10 | Bitcoin Core 30 relaxes OP_RETURN limits |
| 2026-08-08 | BIP-110 minority chain splits off and stalls |

## See also

- [Ethereum](ethereum.md)

## References

[^whitepaper]: Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. <https://bitcoin.org/bitcoin.pdf>
[^max-money]: Bitcoin Core source, `src/consensus/amount.h` (`MAX_MONEY`). <https://github.com/bitcoin/bitcoin/blob/master/src/consensus/amount.h>
[^announcement]: Nakamoto, S. (2008). *Bitcoin P2P e-cash paper*. Cryptography Mailing List, 31 October 2008. <https://www.metzdowd.com/pipermail/cryptography/2008-October/014810.html>
[^chainparams]: Bitcoin Core source, `src/kernel/chainparams.cpp` (genesis timestamp text, `SegwitHeight`). <https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp>
[^genesis]: Genesis block `000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`. <https://mempool.space/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f>
[^copa]: *COPA v Wright*, High Court of England and Wales, judgment. <https://www.judiciary.uk/wp-content/uploads/2024/07/COPA-v-Wright-Judgment.pdf>
[^cve-2010-5139]: CVE-2010-5139. <https://en.bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures>
[^overflow]: Bitcoin Wiki. *Value overflow incident*. <https://en.bitcoin.it/wiki/Value_overflow_incident>
[^bip141]: BIP 141: Segregated Witness (Consensus layer). <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>
[^segwit-activation]: Bitcoin Magazine (2017). *Segregated Witness activates on Bitcoin: what to expect*. <https://bitcoinmagazine.com/technical/segregated-witness-activates-bitcoin-what-expect>
[^bip340]: BIP 340: Schnorr Signatures for secp256k1. <https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki>
[^bip341]: BIP 341: Taproot: SegWit version 1 spending rules. <https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki>
[^cambridge]: Cambridge Judge Business School (2021). *New data reveals timeline of China's bitcoin mining exodus*. <https://www.jbs.cam.ac.uk/2021/new-data-reveals-timeline-of-chinas-bitcoin-mining-exodus/>
[^el-salvador]: The Block (2025). *El Salvador passes bill to revise bitcoin adoption strategy per IMF deal*. <https://www.theblock.co/post/337885/el-salvador-passes-bill-to-revise-bitcoin-adoption-strategy-per-imf-deal-reuters>
[^sec-etf]: Gensler, G. (2024). *Statement on the Approval of Spot Bitcoin Exchange-Traded Products*. US SEC. <https://www.sec.gov/newsroom/speeches-statements/gensler-statement-spot-bitcoin-011023>
[^sbr]: The White House (2025). *Establishment of the Strategic Bitcoin Reserve and United States Digital Asset Stockpile*. <https://www.whitehouse.gov/presidential-actions/2025/03/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile/>
[^oct-2025]: investingLive (2026). *One year after crypto's $20 billion liquidation day*. <https://investinglive.com/cryptocurrency/one-year-after-crypto-s-20-billion-liquidation-day-the-lesson-for-bitcoin-traders/>
[^mtgox]: CNBC (2014). *Mt. Gox says it found 200,000 bitcoins in forgotten wallet*. <https://www.cnbc.com/2014/03/20/mtgox-says-it-found-200000-bitcoins-in-forgotten-wallet.html>
[^core30]: Bitcoin Core 30.0 release notes. <https://bitcoincore.org/en/releases/30.0/>
[^bip110]: CoinDesk (2026). *Controversial bitcoin fork BIP-110 mines two blocks, then stops*. <https://www.coindesk.com/tech/2026/08/09/controversial-bitcoin-fork-bip-110-mines-two-blocks-then-stops>
[^bips]: Bitcoin Improvement Proposals repository. <https://github.com/bitcoin/bips>
[^lightning]: Poon, J. and Dryja, T. (2016). *The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments*. <https://lightning.network/lightning-network-paper.pdf>
