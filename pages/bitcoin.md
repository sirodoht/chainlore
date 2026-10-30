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

### Precursors

Bitcoin drew on two decades of work on digital cash. David Chaum's
DigiCash, founded in 1989, offered private electronic payments but
depended on a central issuer and went bankrupt in 1998. Adam Back's
Hashcash (1997) introduced a proof-of-work function to deter email
spam.[^hashcash] Wei Dai's b-money (1998) and Nick Szabo's bit gold,
which Szabo says he devised in 1998 and published in 2005, outlined money
created by computational work and recorded by a distributed group of
servers.[^b-money][^bit-gold] In 2004 Hal Finney built reusable proofs of
work (RPOW), which let Hashcash tokens be transferred.[^rpow] None solved
the problem of preventing double spending without a trusted party. The
Bitcoin whitepaper cites both Hashcash and b-money.[^whitepaper]

### Origins

The domain bitcoin.org was registered on 18 August 2008. On 31 October
2008 Satoshi Nakamoto published the whitepaper *Bitcoin: A Peer-to-Peer
Electronic Cash System* to the Cryptography Mailing
List.[^announcement] The genesis block was mined on 3 January 2009. Its
coinbase transaction contains the text "The Times 03/Jan/2009 Chancellor
on brink of second bailout for banks", a headline from *The Times* of
London.[^chainparams][^genesis] The first version of the software was
released days later, and the first transaction between two people, from
Nakamoto to Hal Finney, was included in block 170 on 12 January 2009.

For most of 2009 bitcoin had no market price. In October 2009 the
exchange New Liberty Standard published the first exchange rate, US$1 for
1,309.03 BTC, based on the cost of the electricity used to mine
it.[^nls] In November 2009 Nakamoto and Martti Malmi started a discussion
forum that became Bitcointalk, which for years was the main venue for
development and debate.[^bitcointalk]

On 22 May 2010 Laszlo Hanyecz paid 10,000 BTC for two pizzas, the first
widely known purchase of physical goods with bitcoin. The date is
celebrated as Bitcoin Pizza Day.

### Nakamoto's departure

Nakamoto wrote most of the early code and ran the project until late
2010. Their last post on Bitcointalk was on 12 December
2010.[^last-post] In private correspondence with developer Mike Hearn in
April 2011 they wrote that they had "moved on to other
things".[^hearn-emails] Gavin Andresen, who had taken over day-to-day
leadership of the software, became its lead maintainer.

Analysis of early blocks suggests that a single miner, widely believed to
be Nakamoto, mined roughly one million BTC in 2009 and 2010. Almost none
of those coins have ever moved.[^patoshi]

### Identity of Satoshi Nakamoto

Nakamoto's identity remains unknown. In March 2014 *Newsweek* named Dorian
Nakamoto, a Californian engineer, who denied any involvement. Australian
computer scientist Craig Wright claimed from 2016 to be Nakamoto. On 14
March 2024 the High Court of England and Wales ruled that he is not
Nakamoto and did not write the whitepaper,[^copa] and in its full
judgment in May 2024 found that he had forged documents to support his
claim.[^copa-judgment] In October 2024 the HBO documentary *Money
Electric* suggested that early developer Peter Todd was Nakamoto, which
he denied.[^money-electric] Hal Finney, Nick Szabo, and Adam Back have
also been proposed, and all have denied it. Finney died in August 2014.

### Value overflow incident

On 15 August 2010 a bug allowed block 74,638 to create about 184 billion
BTC.[^cve-2010-5139] A fix was released within about five hours, and the
corrected chain overtook the invalid one at block 74,691.[^overflow] It
is the only time a bug has been exploited to create bitcoin beyond the
supply limit.

### Early growth

Bitcoin first reached parity with the US dollar in February 2011. The
same month Silk Road, a darknet marketplace that accepted only bitcoin,
opened. It gave bitcoin its first sustained real-world use and much of
its early notoriety. The FBI shut it down in October 2013 and arrested
its operator, Ross Ulbricht, who was sentenced to life in prison in
2015[^silk-road] and pardoned by US President Donald Trump on 21 January
2025.

Mining moved from ordinary computer processors to graphics cards in 2010,
and the first mining pool, which shared rewards among many small miners,
found its first block in December 2010.[^slush] In early 2013 the first
application-specific integrated circuits (ASICs) built for Bitcoin
mining shipped.[^avalon] Mining became an industrial activity
concentrated in places with cheap electricity.

In 2011 Amir Taaki published BIP 1, which established the Bitcoin
Improvement Proposal process, since revised by BIP 2 and
BIP 3.[^bip1] In April 2012 pay-to-script-hash (P2SH, BIP 16) activated,
allowing multisignature addresses that begin with
"3".[^bip16][^bip13] In September 2012 a group of early supporters
founded the Bitcoin Foundation, a non-profit that funded core
development for several years.[^bitcoin-foundation]

Regulators began to respond. In March 2013 the US Financial Crimes
Enforcement Network issued guidance that bitcoin exchangers and
administrators were money transmitters.[^fincen] New York introduced the
BitLicense in 2015.[^bitlicense] In April 2017 Japan recognised bitcoin
as a legal means of payment.[^japan]

### Block size war and SegWit

In 2010 Nakamoto added a 1 MB limit on block size, widely understood as
a temporary anti-spam measure. By 2015 blocks were filling up and fees
were rising, and the community split over how to scale. One side,
including Andresen and Hearn, favoured raising the limit with a hard
fork. The other, including most Bitcoin Core developers, favoured keeping
blocks small so that ordinary users could run full nodes, and moving
activity to off-chain layers.

In August 2015 Hearn and Andresen released Bitcoin XT, a client that
would have raised the limit to 8 MB.[^bip101] It failed to win miner
support, as did Bitcoin Classic in 2016. In January 2016 Hearn left the
project, declaring the experiment had failed.[^hearn-resolution]

Segregated Witness (SegWit), proposed in 2015, moved signature data out
of the part of the block counted against the limit. This raised capacity
and fixed transaction malleability without a hard fork. Miners were slow
to signal for it. In May 2017 a group of companies and miners agreed the
New York Agreement, known as SegWit2x: activate SegWit, then raise the
limit to 2 MB with a hard fork within six months.[^segwit2x] Separately,
users backed BIP 148, a "user-activated soft fork" under which their
nodes would reject blocks not signalling SegWit from 1 August
2017.[^bip148]

SegWit activated as a soft fork on 24 August 2017 at block
481,824.[^bip141][^chainparams][^segwit-activation] Earlier that month,
on 1 August 2017, a group favouring larger blocks forked the chain to
create Bitcoin Cash. The SegWit2x hard fork was called off in November
2017.[^segwit2x] Bitcoin Cash itself split in November 2018, when
supporters of Craig Wright created Bitcoin SV.[^bsv] The outcome
established that changes to Bitcoin's consensus rules need the support of
users running nodes, not only miners and businesses.

### Lightning Network

The Lightning Network, proposed by Joseph Poon and Thaddeus Dryja in
2015, lets two parties open a payment channel by locking bitcoin in a
shared output and then exchange many payments off-chain, settling only
the final balance on the blockchain.[^lightning] Payments can be routed
across a network of channels. SegWit's malleability fix made it
practical, and the first implementations were released for mainnet use
in March 2018.[^lnd]

### Taproot

Taproot, a soft fork adding Schnorr signatures and more private, more
efficient scripts, activated on 14 November 2021 at block
709,632.[^bip340][^bip341] It was the first major upgrade since SegWit.
The change itself had broad support, though the activation method was
debated. Taproot addresses begin with "bc1p".[^bip350]

### Mining migration

In mid-2021 China banned cryptocurrency mining. Global hashrate fell 38%
in June 2021 as miners shut down or moved abroad, and by August 2021 the
United States had the largest share of hashrate, at 35.4%.[^cambridge]

### Institutional adoption

The Cboe and CME began trading bitcoin futures in December
2017.[^cboe] In August 2020 MicroStrategy, a US software company, began
buying bitcoin as its main treasury reserve asset, and it has continued
to buy since; it rebranded as Strategy in February 2025 and is the
largest corporate holder.[^strategy] In February 2021 Tesla announced it
had bought US$1.5 billion of bitcoin.[^tesla]

El Salvador made bitcoin legal tender on 7 September 2021, the first
country to do so. On 29 January 2025, under an agreement with the
International Monetary Fund, its legislature amended the law to make
acceptance voluntary and to end tax payments in bitcoin.[^el-salvador]

On 10 January 2024 the US Securities and Exchange Commission approved
the first spot bitcoin exchange-traded products, which began trading the
next day.[^sec-etf] On 6 March 2025 a US executive order declared it US
policy to establish a Strategic Bitcoin Reserve.[^sbr]

### Market history

Bitcoin's price has moved in boom-and-bust cycles that have roughly
tracked the halvings.

| Date | Milestone |
|---|---|
| 2011-02 | Reaches US$1 |
| 2013-11 | Passes US$1,000 |
| 2017-12 | Peaks near US$20,000 |
| 2021-11-10 | Peaks near US$69,000 |
| 2022 | Falls below US$16,000 after the collapses of Terra, Celsius, and FTX |
| 2024-12 | Passes US$100,000 |
| 2025-10-06 | All-time high, about US$126,000[^ath] |

On 10 October 2025 a market-wide crash caused the largest single day of
liquidations in crypto history.[^oct-2025] For current prices, see live
data sources.

## Technology

### Blocks and mining

Transactions are grouped into blocks. Miners compete to find a block
header whose double SHA-256 hash is below a target; the first to do so
earns the block subsidy plus transaction fees. Nodes follow the valid
chain with the most accumulated proof of work. The difficulty target is
recalculated every 2,016 blocks so that blocks arrive about every ten
minutes. Newly mined coins cannot be spent for 100 blocks.[^maturity]

Because changing a past block would require redoing its proof of work
and that of every later block, the deeper a transaction is buried, the
harder it is to reverse. A common convention treats six confirmations,
about an hour, as final for large payments.

### Transactions and scripts

Bitcoin uses an unspent transaction output (UTXO) model. Each transaction
spends earlier outputs and creates new ones; a wallet's balance is the
sum of the outputs it can spend. The conditions for spending an output
are written in Script, a deliberately limited, non-Turing-complete
language. Since SegWit, block size is measured in weight units, with a
limit of 4 million.

Address formats have changed as the protocol has
evolved:[^bip13][^bip173][^bip350]

| Prefix | Type | Introduced |
|---|---|---|
| `1` | Pay-to-public-key-hash (P2PKH) | 2009 |
| `3` | Pay-to-script-hash (P2SH) | 2012 |
| `bc1q` | Native SegWit (bech32) | 2017 |
| `bc1p` | Taproot (bech32m) | 2021 |

### Nodes and development

Unconfirmed transactions wait in each node's memory pool, or mempool, and
miners generally choose those paying the highest fee per unit of weight.
When demand for block space is high, fees rise.

Changes to the protocol are proposed as Bitcoin Improvement Proposals
(BIPs).[^bips] There is no formal governance; changes require broad
adoption by node operators, miners, and users. Most nodes run Bitcoin
Core, which was called Bitcoin-Qt until 2014.[^core-rebrand] Alternative
clients include Bitcoin Knots and btcd. Development is funded by grants
and donations from companies and non-profits rather than by a single
foundation or a pre-mined token.

## Supply

New bitcoin enters circulation only through the block subsidy. The
subsidy started at 50 BTC and halves every 210,000 blocks, about every
four years, so total supply approaches but never exceeds 21
million.[^max-money] The last fraction of a bitcoin is expected to be
mined around 2140, after which miners will be paid only in fees.

| Halving | Date | Block | Subsidy after |
|---|---|---|---|
| 1 | 2012-11-28 | 210,000 | 25 BTC |
| 2 | 2016-07-09 | 420,000 | 12.5 BTC |
| 3 | 2020-05-11 | 630,000 | 6.25 BTC |
| 4 | 2024-04-20 | 840,000 | 3.125 BTC |
| 5 | about 2028 | 1,050,000 | 1.5625 BTC |

Coins sent to lost keys or unspendable outputs are permanently removed
from use, so the usable supply is lower than the number of coins mined.

## Incidents and controversies

- **Value overflow (2010).** See [above](#value-overflow-incident).
- **March 2013 chain split.** On 11 March 2013 a database limit in
  version 0.7 of the software made it reject a large block, block 225,430,
  that version 0.8 accepted, splitting the chain in two. Developers asked
  miners to return to version 0.7, and the split was resolved within
  hours.[^bip50]
- **Mt. Gox (2014).** Mt. Gox, then the largest bitcoin exchange, halted
  withdrawals and filed for bankruptcy on 28 February 2014, reporting
  about 850,000 BTC missing. In March 2014 it said it had found about
  200,000 BTC in an old wallet.[^mtgox] Repayments to creditors began in
  December 2023, and repayments in bitcoin followed in July
  2024.[^mtgox-yen][^mtgox-btc]
- **Bitfinex hack (2016).** In August 2016 about 120,000 BTC was stolen
  from the exchange Bitfinex. In February 2022 US authorities arrested
  two people in connection with laundering the funds and seized about
  94,000 BTC.[^bitfinex]
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
| 2009-10 | First exchange rate published |
| 2010-05-22 | 10,000 BTC paid for two pizzas |
| 2010-08-15 | Value overflow incident (block 74,638) |
| 2010-12-12 | Nakamoto's last forum post |
| 2011-02 | Parity with US dollar; Silk Road opens |
| 2012-04 | P2SH activates |
| 2012-11-28 | First halving |
| 2013-03-11 | Chain split between versions 0.7 and 0.8 |
| 2013-10 | Silk Road shut down |
| 2014-02-28 | Mt. Gox files for bankruptcy |
| 2016-08 | Bitfinex hack |
| 2017-08-01 | Bitcoin Cash fork; BIP 148 takes effect |
| 2017-08-24 | SegWit activates (block 481,824) |
| 2017-12 | Bitcoin futures launch on Cboe and CME |
| 2018-11 | Bitcoin Cash splits; Bitcoin SV created |
| 2020-08 | MicroStrategy begins buying bitcoin |
| 2021-06 | China's mining ban; hashrate falls 38% |
| 2021-09-07 | El Salvador makes bitcoin legal tender |
| 2021-11-14 | Taproot activates (block 709,632) |
| 2023-01 | Ordinals launched |
| 2023-12 | Mt. Gox begins repaying creditors |
| 2024-01-10 | US SEC approves spot bitcoin ETPs |
| 2024-03-14 | UK High Court rules Craig Wright is not Satoshi Nakamoto |
| 2024-04-20 | Fourth halving |
| 2024-07 | Mt. Gox begins bitcoin repayments |
| 2025-01-21 | Ross Ulbricht pardoned |
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
[^hashcash]: Back, A. (2002). *Hashcash: A Denial of Service Counter-Measure*. <http://www.hashcash.org/papers/hashcash.pdf>
[^b-money]: Dai, W. (1998). *b-money*. Satoshi Nakamoto Institute. <https://nakamotoinstitute.org/library/b-money/>
[^bit-gold]: Szabo, N. (2005). *Bit Gold*. Satoshi Nakamoto Institute. <https://nakamotoinstitute.org/library/bit-gold/>
[^rpow]: Finney, H. (2004). *RPOW: Reusable Proofs of Work*. Satoshi Nakamoto Institute. <https://nakamotoinstitute.org/finney/rpow/>
[^announcement]: Nakamoto, S. (2008). *Bitcoin P2P e-cash paper*. Cryptography Mailing List, 31 October 2008. <https://www.metzdowd.com/pipermail/cryptography/2008-October/014810.html>
[^chainparams]: Bitcoin Core source, `src/kernel/chainparams.cpp` (genesis timestamp text, `SegwitHeight`). <https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp>
[^genesis]: Genesis block `000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`. <https://mempool.space/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f>
[^nls]: BullionStar. *Dawn of Bitcoin price discovery 2009–2011: the very early Bitcoin exchanges*. <https://www.bullionstar.com/blogs/ronan-manly/dawn-of-bitcoin-price-discovery-2009-2011-the-very-early-bitcoin-exchanges>
[^bitcointalk]: Bitcoin Wiki. *BitcoinTalk*. <https://en.bitcoin.it/wiki/BitcoinTalk>
[^last-post]: Nakamoto, S. (2010). *Added some DoS limits, removed safe mode (0.3.19)*. Bitcointalk, 12 December 2010. <https://satoshi.nakamotoinstitute.org/posts/bitcointalk/543/>
[^hearn-emails]: Motherboard (2017). *Former Bitcoin developer shares early Satoshi Nakamoto emails*. <https://vice.com/en/article/7xx9gb/former-bitcoin-developer-shares-early-satoshi-nakamoto-emails>
[^patoshi]: Lerner, S. D. (2013). *The Well Deserved Fortune of Satoshi Nakamoto*. <https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/>
[^copa]: *COPA v Wright*, High Court of England and Wales, judgment. <https://www.judiciary.uk/wp-content/uploads/2024/07/COPA-v-Wright-Judgment.pdf>
[^copa-judgment]: *COPA v Wright* [2024] EWHC 1198 (Ch), 20 May 2024. <https://caselaw.nationalarchives.gov.uk/ewhc/ch/2024/1198>
[^money-electric]: The Block (2024). *HBO documentary suggests Peter Todd is Bitcoin creator Satoshi Nakamoto, who denies it online*. <https://www.theblock.co/post/320144/hbo-documentary-suggests-peter-todd-is-bitcoin-creator-satoshi-nakamoto-who-denies-it-online>
[^cve-2010-5139]: CVE-2010-5139. <https://en.bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures>
[^overflow]: Bitcoin Wiki. *Value overflow incident*. <https://en.bitcoin.it/wiki/Value_overflow_incident>
[^silk-road]: NPR (2015). *Silk Road founder sentenced to life in prison*. <https://www.npr.org/2015/05/29/410601330/silk-road-founder-sentenced-to-life-in-prison>
[^slush]: Bitcoin Wiki. *Slush Pool*. <https://en.bitcoin.it/wiki/Slush_Pool>
[^avalon]: Bitcoin Magazine (2013). *Avalon ships Bitcoin's first consumer ASICs*. <https://bitcoinmagazine.com/articles/avalon-ships-bitcoins-first-consumer-asics-1358905223>
[^bip1]: BIP 1: BIP Purpose and Guidelines. <https://github.com/bitcoin/bips/blob/master/bip-0001.mediawiki>
[^bip13]: BIP 13: Address Format for pay-to-script-hash. <https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki>
[^bip16]: BIP 16: Pay to Script Hash. <https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki>
[^bitcoin-foundation]: Bitcoin Wiki. *Bitcoin Foundation*. <https://en.bitcoin.it/wiki/Bitcoin_Foundation>
[^fincen]: FinCEN (2013). *Application of FinCEN's Regulations to Persons Administering, Exchanging, or Using Virtual Currencies* (FIN-2013-G001). <https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering>
[^bitlicense]: New York State Department of Financial Services. *Virtual currency businesses*. <https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses>
[^japan]: CoinDesk (2017). *Japan's bitcoin law goes into effect tomorrow*. <https://www.coindesk.com/markets/2017/03/31/japans-bitcoin-law-goes-into-effect-tomorrow>
[^bip101]: BIP 101: Increase maximum block size. <https://github.com/bitcoin/bips/blob/master/bip-0101.mediawiki>
[^hearn-resolution]: Hearn, M. (2016). *The resolution of the Bitcoin experiment*. <https://mikehearn.medium.com/the-resolution-of-the-bitcoin-experiment-dabb30201f7>
[^segwit2x]: Bitcoin Wiki. *SegWit2x*. <https://en.bitcoin.it/wiki/SegWit2x>
[^bip148]: BIP 148: Mandatory activation of segwit deployment. <https://github.com/bitcoin/bips/blob/master/bip-0148.mediawiki>
[^bip141]: BIP 141: Segregated Witness (Consensus layer). <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>
[^segwit-activation]: Bitcoin Magazine (2017). *Segregated Witness activates on Bitcoin: what to expect*. <https://bitcoinmagazine.com/technical/segregated-witness-activates-bitcoin-what-expect>
[^bsv]: Decrypt (2018). *Bitcoin Cash hard fork*. <https://decrypt.co/2018/11/15/bitcoin-cash-hard-fork/>
[^lightning]: Poon, J. and Dryja, T. (2016). *The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments*. <https://lightning.network/lightning-network-paper.pdf>
[^lnd]: Lightning Labs (2018). *lnd v0.4-beta release notes*. <https://github.com/lightningnetwork/lnd/releases/tag/v0.4-beta>
[^bip340]: BIP 340: Schnorr Signatures for secp256k1. <https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki>
[^bip341]: BIP 341: Taproot: SegWit version 1 spending rules. <https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki>
[^bip350]: BIP 350: Bech32m format for v1+ witness addresses. <https://github.com/bitcoin/bips/blob/master/bip-0350.mediawiki>
[^cambridge]: Cambridge Judge Business School (2021). *New data reveals timeline of China's bitcoin mining exodus*. <https://www.jbs.cam.ac.uk/2021/new-data-reveals-timeline-of-chinas-bitcoin-mining-exodus/>
[^cboe]: Cboe (2017). *Cboe Bitcoin Futures product launch date*. <https://cdn.cboe.com/resources/schedule_update/2017/Cboe-Bitcoin-Futures-Product-Launch-Date-and-December-Transaction-Fee-Waiver.pdf>
[^strategy]: Strategy (2025). *MicroStrategy is now Strategy*. <https://software.strategy.com/news/microstrategy-is-now-strategy_02-05-2025>
[^tesla]: Bloomberg (2021). *Tesla holds fast to its pioneering investment in bitcoin*. <https://www.bloomberg.com/news/articles/2021-10-20/tesla-holds-fast-to-its-pioneering-investment-in-bitcoin>
[^el-salvador]: The Block (2025). *El Salvador passes bill to revise bitcoin adoption strategy per IMF deal*. <https://www.theblock.co/post/337885/el-salvador-passes-bill-to-revise-bitcoin-adoption-strategy-per-imf-deal-reuters>
[^sec-etf]: Gensler, G. (2024). *Statement on the Approval of Spot Bitcoin Exchange-Traded Products*. US SEC. <https://www.sec.gov/newsroom/speeches-statements/gensler-statement-spot-bitcoin-011023>
[^sbr]: The White House (2025). *Establishment of the Strategic Bitcoin Reserve and United States Digital Asset Stockpile*. <https://www.whitehouse.gov/presidential-actions/2025/03/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile/>
[^ath]: KuCoin News (2026). *Bitcoin's $126,210 all-time high turns one year old*. <https://www.kucoin.com/news/flash/bitcoin-s-126-210-all-time-high-turns-one-year-old>
[^oct-2025]: investingLive (2026). *One year after crypto's $20 billion liquidation day*. <https://investinglive.com/cryptocurrency/one-year-after-crypto-s-20-billion-liquidation-day-the-lesson-for-bitcoin-traders/>
[^maturity]: Bitcoin Core source, `src/consensus/consensus.h` (`COINBASE_MATURITY`). <https://github.com/bitcoin/bitcoin/blob/master/src/consensus/consensus.h>
[^bip173]: BIP 173: Base32 address format for native v0-16 witness outputs. <https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki>
[^core-rebrand]: Bitcoin Core 0.9.0 release notes. <https://bitcoin.org/en/release/v0.9.0>
[^bips]: Bitcoin Improvement Proposals repository. <https://github.com/bitcoin/bips>
[^bip50]: BIP 50: March 2013 Chain Fork Post-Mortem. <https://github.com/bitcoin/bips/blob/master/bip-0050.mediawiki>
[^mtgox]: CNBC (2014). *Mt. Gox says it found 200,000 bitcoins in forgotten wallet*. <https://www.cnbc.com/2014/03/20/mtgox-says-it-found-200000-bitcoins-in-forgotten-wallet.html>
[^mtgox-yen]: The Block (2023). *Mt. Gox reportedly starts repaying some creditors via PayPal*. <https://www.theblock.co/post/269212/mt-gox-reportedly-starts-repaying-some-creditors-via-paypal>
[^mtgox-btc]: The Block (2024). *Mt. Gox starts making repayment in bitcoin and bitcoin cash*. <https://www.theblock.co/post/303614/mt-gox-starts-making-repayment-in-bitcoin-and-bitcoin-cash-trustee>
[^bitfinex]: Bloomberg (2022). *DOJ seizes $3.6 billion in bitcoin stolen in 2016 Bitfinex hack*. <https://www.bloomberg.com/news/articles/2022-02-08/doj-seizes-3-6-billion-in-bitcoin-stolen-in-2016-bitfinex-hack>
[^core30]: Bitcoin Core 30.0 release notes. <https://bitcoincore.org/en/releases/30.0/>
[^bip110]: CoinDesk (2026). *Controversial bitcoin fork BIP-110 mines two blocks, then stops*. <https://www.coindesk.com/tech/2026/08/09/controversial-bitcoin-fork-bip-110-mines-two-blocks-then-stops>
