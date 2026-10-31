---
title: Bitcoin
ticker: BTC
category: Layer 1
written_by: Opus 5.5 High
status: ai-fact-checked
checked: 2026-10-30
checked_by: GPT-6-Astra high
updated: 2026-10-30
---

# Bitcoin

**Bitcoin** (BTC) is a decentralized digital currency and the first
decentralized cryptocurrency.[^faq] It was described in a 2008 whitepaper by the pseudonymous
Satoshi Nakamoto and launched in January 2009. Bitcoin uses proof of work
to order transactions in a public ledger, the blockchain, without a
central authority.[^whitepaper] Its supply is capped at 21 million
BTC under its issuance rules.[^halvings]

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
| Smallest unit | 1 satoshi = 0.00000001 BTC[^max-money] |
| Reference client | Bitcoin Core |
| License | MIT[^max-money] |
| Live data | [mempool.space](https://mempool.space) |

## History

### Precursors

Bitcoin drew on two decades of work on digital cash. David Chaum's
DigiCash offered private electronic payments and filed for bankruptcy
in 1998.[^digicash] Adam Back's
Hashcash (1997) introduced a proof-of-work function to deter email
spam.[^hashcash] Wei Dai's b-money (1998) and Nick Szabo's bit gold,
published in 2005, outlined money
created by computational work and recorded by a distributed group of
servers.[^b-money][^bit-gold] Hal Finney's reusable proofs of work (RPOW) let proof-of-work tokens
be transferred through a trusted server that prevented double spending.[^rpow] The
Bitcoin whitepaper cites both Hashcash and b-money.[^whitepaper]

### Origins

The domain bitcoin.org was registered on 18 August 2008.[^domain] On 31 October
2008 Satoshi Nakamoto published the whitepaper *Bitcoin: A Peer-to-Peer
Electronic Cash System* to the Cryptography Mailing
List.[^announcement] The genesis block was mined on 3 January 2009. Its
coinbase transaction contains the text "The Times 03/Jan/2009 Chancellor
on brink of second bailout for banks", a headline from *The Times* of
London.[^chainparams][^genesis] The first version of the software was
released on 8 January 2009.[^release01] A 10 BTC payment from Nakamoto
to Hal Finney was included in block 170 on 12 January 2009.[^first-tx][^finney]

For most of 2009 bitcoin had no market price. In October 2009 the
exchange New Liberty Standard published the first exchange rate, US$1 for
1,309.03 BTC, based on the cost of the electricity used to mine
it.[^nls] A discussion forum that became Bitcointalk opened in November
2009.[^bitcointalk]

On 22 May 2010 Laszlo Hanyecz reported exchanging 10,000 BTC for two
pizzas on the Bitcoin forum.[^pizza]

### Nakamoto's departure

Nakamoto's last post on Bitcointalk was on 12 December
2010.[^last-post] In private correspondence with developer Mike Hearn in
April 2011 they wrote that they had "moved on to other
things" and that the project was in the hands of Gavin Andresen and
other contributors.[^hearn-emails]

In 2013 researcher Sergio Demian Lerner estimated that one early miner
had accumulated roughly one million BTC. He suggested it was Nakamoto,
but explicitly stated that the attribution was uncertain.[^patoshi]

### Identity of Satoshi Nakamoto

Nakamoto’s identity remains unknown.[^faq] Craig Wright claimed to be
Nakamoto. On 14
March 2024 the High Court of England and Wales ruled that he is not
Nakamoto and did not write the whitepaper,[^copa-judgment] and in its full
judgment in May 2024 found that he had forged documents to support his
claim.[^copa-judgment] In October 2024 the HBO documentary *Money
Electric* suggested that early developer Peter Todd was Nakamoto, which
he denied.[^money-electric]

### Value overflow incident

On 15 August 2010 a bug allowed block 74,638 to create about 184 billion
BTC.[^overflow] Nakamoto committed a fix on the same day. The patched
software rejected the overflow transaction.[^overflow-fix]

### Early growth

Bitcoin reached parity with the US dollar in 2011.[^price-history] Silk
Road, a darknet marketplace using bitcoin, operated from 2011 until
October 2013, when authorities shut it down and arrested Ross Ulbricht.
He was sentenced to life imprisonment in 2015[^silk-road] and pardoned by
US President Donald Trump on 21 January 2025.[^pardon]

Mining hardware progressed from general-purpose processors to graphics
cards and then to application-specific integrated circuits (ASICs) around
2013.[^avalon] Mining pools let participants combine their computing
power and share rewards. Slush announced his pool in late
2010.[^slush]

In 2011 Amir Taaki published BIP 1, which established the Bitcoin
Improvement Proposal process, since revised by BIP 2 and
BIP 3.[^bip1][^bip3] In April 2012 pay-to-script-hash (P2SH, BIP 16) activated,
allowing multisignature addresses that begin with
"3".[^bip16][^bip13] In September 2012 a group of early supporters
launched the Bitcoin Foundation to promote Bitcoin’s
use.[^bitcoin-foundation]

Regulators began to respond. In March 2013 the US Financial Crimes
Enforcement Network issued guidance that bitcoin exchangers and
administrators generally qualified as money transmitters unless an
exception applied; ordinary users did not qualify merely by using
virtual currency.[^fincen] New York introduced the
BitLicense in 2015.[^bitlicense] In April 2017 Japan recognised bitcoin
as a legal means of payment.[^japan]

### Block size war and SegWit

Bitcoin’s pre-SegWit consensus rules limited blocks to 1 MB. In 2015
Gavin Andresen proposed BIP 101, which would have increased the limit
to 8 MB initially, followed by further growth. It was not adopted by
Bitcoin.[^bip101]

Segregated Witness (SegWit), proposed in 2015, moved signature data out
of the part of the block counted against the limit. This raised capacity
and addressed signature-related transaction malleability without a hard
fork.[^bip141] A separate 2017 proposal, SegWit2x, combined SegWit with a
planned block-size hard fork.[^segwit2x] Separately,
users backed BIP 148, a "user-activated soft fork" under which their
nodes would reject blocks not signalling SegWit from 1 August
2017.[^bip148]

SegWit activated as a soft fork on 24 August 2017 at block
481,824.[^bip141][^chainparams][^segwit-activation] Earlier that month,
on 1 August 2017, a group favouring larger blocks forked the chain to
create Bitcoin Cash.[^bch] The SegWit2x organizers suspended their hard
fork in November 2017, citing insufficient consensus.[^segwit2x]

### Lightning Network

The Lightning Network, described by Joseph Poon and Thaddeus Dryja in a
2016 paper, lets two parties open a payment channel by locking bitcoin in a
shared output and then exchange many payments off-chain, settling only
the final balance on the blockchain.[^lightning] Payments can be routed
across a network of channels. SegWit's malleability fix made it
practical.[^bip141] Lightning Labs released a mainnet-enabled beta of
its lnd implementation in March 2018.[^lnd]

### Taproot

Taproot, a soft fork adding Schnorr signatures and more private, more
efficient scripts, activated on 14 November 2021 at block
709,632.[^bip340][^bip341][^taproot-block] Taproot addresses begin with
"bc1p".[^bip350]

### Mining migration

China restricted cryptocurrency mining in mid-2021. A Cambridge report
published that July documented the preceding decline in China’s share of
global hashrate, from 75.5% in September 2019 to 46% in April 2021, and
described the subsequent relocation of mining equipment.[^cambridge]

### Institutional adoption

The Cboe and CME began trading bitcoin futures in December
2017.[^cboe][^cme] In August 2020 MicroStrategy, a US software company, began
buying bitcoin as its main treasury reserve asset.[^strategy-treasury]
It rebranded as Strategy in February 2025.[^strategy] In February 2021 Tesla announced it
had bought US$1.5 billion of bitcoin.[^tesla]

El Salvador made bitcoin legal tender on 7 September 2021, the first
country to do so.[^el-salvador-imf] In January 2025, under an agreement with the
International Monetary Fund, its legislature amended the law to make
acceptance voluntary.[^el-salvador]

On 10 January 2024 the US Securities and Exchange Commission approved
the listing and trading of spot bitcoin exchange-traded products.[^sec-etf] On 6 March 2025 a US executive order declared it US
policy to establish a Strategic Bitcoin Reserve.[^sbr]

### Market history

Selected price milestones are listed below. Prices vary by trading
venue.[^price-history]

| Date | Milestone |
|---|---|
| 2011 | Reaches US$1[^price-history] |
| 2013-11 | Passes US$1,000[^price-history] |
| 2017-12 | Reaches roughly US$19,200 on the cited price series[^price-history] |
| 2021-11 | Peaks near US$69,000[^price-history] |
| 2024-12 | Passes US$100,000[^price-history] |
| 2025-10-06 | Reaches about US$126,000[^ath] |

During the 10–11 October 2025 sell-off, CoinDesk Research reported over
US$19 billion in market-wide liquidations over 24 hours.[^oct-2025] For current prices, see live
data sources.

## Technology

### Blocks and mining

Transactions are grouped into blocks. Miners compete to find a block
header whose double SHA-256 hash does not exceed a target. A miner whose
valid block becomes part of the accepted chain earns the block subsidy
plus transaction fees. Nodes follow the valid
chain with the most accumulated proof of work. The difficulty target is
recalculated every 2,016 blocks so that blocks arrive about every ten
minutes.[^blockchain-guide] Newly mined coins cannot be spent for 100 blocks.[^maturity]

Because changing a past block would require redoing its proof of work
and that of every later block, the deeper a transaction is buried, the
harder it is to reverse. A common convention treats six confirmations,
about an hour on average, as sufficient for some payments, although
Bitcoin does not provide absolute finality.[^payment-guide]

### Transactions and scripts

Bitcoin uses an unspent transaction output (UTXO) model. Each transaction
spends earlier outputs and creates new ones; a wallet's balance is the
sum of the outputs it can spend. The conditions for spending an output
are written in Script, a deliberately limited, non-Turing-complete
language. Since SegWit, block size is measured in weight units, with a
limit of 4 million.[^transactions-guide][^bip141]

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
When demand for block space is high, fees can rise.[^transactions-guide][^block-assembly][^mempool]

Changes to the protocol are proposed as Bitcoin Improvement Proposals
(BIPs).[^bips] There is no formal governance; changes require broad
adoption by node operators, miners, and users.[^faq] Bitcoin Core was
called Bitcoin-Qt until 2014.[^core-rebrand] As of 30 October 2026 its
latest release is 32.1, published on 27 October; 32.0 was tagged but never
fully released.[^core321][^core321-date]

## Supply

New bitcoin enters circulation only through the block subsidy. The
subsidy started at 50 BTC and halves every 210,000 blocks, about every
four years, so total supply approaches but never exceeds 21
million.[^halvings] The last fraction of a bitcoin is expected to be
mined around 2140, after which miners will be paid only in fees.[^halvings]

Halving dates and subsidies:[^halvings]

| Halving | Date | Block | Subsidy after |
|---|---|---|---|
| 1 | 2012-11-28 | 210,000 | 25 BTC |
| 2 | 2016-07-09 | 420,000 | 12.5 BTC |
| 3 | 2020-05-11 | 630,000 | 6.25 BTC |
| 4 | 2024-04-20 | 840,000 | 3.125 BTC |
| 5 | about 2028 | 1,050,000 | 1.5625 BTC |

Coins whose private keys are irretrievably lost cannot be spent. This
reduces the usable supply without changing the recorded
issuance.[^faq]

## Incidents and controversies

- **Value overflow (2010).** See [above](#value-overflow-incident).[^overflow][^overflow-fix]
- **March 2013 chain split.** On 11 March 2013 a database limit in
  version 0.7 of the software made it reject a large block, block 225,430,
  that version 0.8 accepted, splitting the chain in two. Developers asked
  miners to return to version 0.7, and the split was resolved within
  hours.[^bip50]
- **Mt. Gox (2014).** Mt. Gox closed its website and sought civil
  rehabilitation in February 2014, reporting
  about 850,000 BTC missing.[^mtgox-filing] In March 2014 it said it had found about
  200,000 BTC in an old wallet.[^mtgox] Creditors reported receiving
  cash repayments in December 2023; bitcoin repayments began in July
  2024.[^mtgox-yen][^mtgox-btc]
- **Bitfinex hack (2016).** In August 2016 about 120,000 BTC was stolen
  from the exchange Bitfinex. In February 2022 US authorities arrested
  two people in connection with laundering the funds and seized about
  94,000 BTC.[^bitfinex]
- **Block size war (2015–2017).** See [above](#block-size-war-and-segwit).[^bip101][^bip148][^segwit2x]
- **Binance hot-wallet incident (October 2026).** Binance reported that
  its hot wallets were compromised on 29 October, with about US$6.3
  billion in assets stolen, including BTC and ETH. As of 30 October,
  Binance said its investigation was ongoing and withdrawals remained
  suspended.[^binance-incident]
- **Energy use.** Proof-of-work mining consumes large amounts of
  electricity. Cambridge publishes estimates of the network's
  electricity consumption in its Bitcoin Electricity Consumption
  Index.[^energy]
- **Ordinals and OP_RETURN (2023–2026).** Ordinals inscriptions store
  content in Taproot script-path spends.[^ordinals] Casey Rodarmor
  announced their mainnet readiness in January 2023.[^ordinals-history]
  This became part of a broader debate about data in transactions.[^bip110]
  The debate intensified in October 2025 when Bitcoin Core 30 raised its
  default relay and mining policy limit on `OP_RETURN` data to 100,000 bytes and allowed multiple
  `OP_RETURN` outputs.[^core30] Some node operators switched to Bitcoin
  Knots in protest. On 8 August 2026 nodes enforcing BIP-110, a
  Knots-backed soft fork to restrict data in transactions, split from
  the main chain at block 961,632. With little miner support, the
  minority chain had mined two blocks and stalled when CoinDesk reported
  on it on 9 August.[^bip110]

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
| 2011 | Parity with US dollar; Silk Road operates |
| 2012-04 | P2SH activates |
| 2012-11-28 | First halving |
| 2013-03-11 | Chain split between versions 0.7 and 0.8 |
| 2013-10 | Silk Road shut down |
| 2014-02 | Mt. Gox seeks civil rehabilitation |
| 2016-08 | Bitfinex hack |
| 2017-08-01 | Bitcoin Cash fork; BIP 148 takes effect |
| 2017-08-24 | SegWit activates (block 481,824) |
| 2017-12 | Bitcoin futures launch on Cboe and CME |
| 2020-08 | MicroStrategy begins buying bitcoin |
| 2021 | China’s mining crackdown |
| 2021-09-07 | El Salvador makes bitcoin legal tender |
| 2021-11-14 | Taproot activates (block 709,632) |
| 2023 | Ordinals inscriptions |
| 2023-12 | Mt. Gox begins repaying creditors |
| 2024-01-10 | US SEC approves spot bitcoin ETPs |
| 2024-03-14 | UK High Court rules Craig Wright is not Satoshi Nakamoto |
| 2024-04-20 | Fourth halving |
| 2024-07 | Mt. Gox begins bitcoin repayments |
| 2025-01-21 | Ross Ulbricht pardoned |
| 2025-01 | El Salvador makes bitcoin acceptance voluntary |
| 2025-03-06 | US executive order on a Strategic Bitcoin Reserve |
| 2025-10-06 | Reaches about US$126,000 |
| 2025-10-10–11 | Market-wide liquidation cascade |
| 2025-10 | Bitcoin Core 30 relaxes OP_RETURN limits |
| 2026-08-08 | BIP-110 minority chain splits off |
| 2026-10-27 | Bitcoin Core 32.1 released |
| 2026-10-29 | Binance reports multi-asset hot-wallet theft |

## See also

- [Lightning Network](lightning-network.md)
- [Monero](monero.md)
- [Mt. Gox](mt-gox.md)
- [Cryptocurrency wallet](cryptocurrency-wallet.md)

- [Ethereum](ethereum.md)

## References

[^whitepaper]: Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. <https://bitcoin.org/bitcoin.pdf>
[^max-money]: Bitcoin Core source, `src/consensus/amount.h` (`MAX_MONEY`). <https://github.com/bitcoin/bitcoin/blob/master/src/consensus/amount.h>
[^hashcash]: Back, A. (2002). *Hashcash: A denial of service counter-measure*. <https://cdn.nakamotoinstitute.org/docs/hashcash.pdf>
[^b-money]: Dai, W. (1998). *b-money*. Satoshi Nakamoto Institute. <https://nakamotoinstitute.org/library/b-money/>
[^bit-gold]: Szabo, N. (2005). *Bit Gold*. Satoshi Nakamoto Institute. <https://nakamotoinstitute.org/library/bit-gold/>
[^rpow]: Finney, H. *RPOW: Reusable Proofs of Work*. Satoshi Nakamoto Institute. <https://nakamotoinstitute.org/finney/rpow/>
[^announcement]: Nakamoto, S. (2008). *Bitcoin P2P e-cash paper*. Cryptography Mailing List, 31 October 2008. <https://www.metzdowd.com/pipermail/cryptography/2008-October/014810.html>
[^chainparams]: Bitcoin Core source, `src/kernel/chainparams.cpp` (genesis timestamp text, `SegwitHeight`). <https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp>
[^genesis]: Blockchain.com. *Bitcoin block 0*. <https://www.blockchain.com/explorer/blocks/btc/0>
[^nls]: BullionStar. *Dawn of Bitcoin price discovery 2009–2011: the very early Bitcoin exchanges*. <https://www.bullionstar.com/blogs/ronan-manly/dawn-of-bitcoin-price-discovery-2009-2011-the-very-early-bitcoin-exchanges>
[^bitcointalk]: Bitcoin Wiki. *BitcoinTalk*. <https://en.bitcoin.it/wiki/BitcoinTalk>
[^last-post]: Nakamoto, S. (2010). *Added some DoS limits, removed safe mode (0.3.19)*. Bitcointalk, 12 December 2010. <https://satoshi.nakamotoinstitute.org/posts/bitcointalk/543/>
[^hearn-emails]: Nakamoto, S. and Hearn, M. (2011). *Holding coins in an unspendable state*. Correspondence published by Hearn. <https://plan99.net/~mike/satoshi-emails/thread5.html>
[^patoshi]: Lerner, S. D. (2013). *The Well Deserved Fortune of Satoshi Nakamoto*. <https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/>
[^copa-judgment]: *COPA v Wright* [2024] EWHC 1198 (Ch), 20 May 2024. <https://caselaw.nationalarchives.gov.uk/ewhc/ch/2024/1198>
[^money-electric]: The Block (2024). *HBO documentary suggests Peter Todd is Bitcoin creator Satoshi Nakamoto, who denies it online*. <https://www.theblock.co/post/320144/hbo-documentary-suggests-peter-todd-is-bitcoin-creator-satoshi-nakamoto-who-denies-it-online>
[^overflow]: Bitcoin developers (2010). *Strange block 74638*. Incident discussion. <https://bitcointalk.org/index.php?topic=822.0>
[^silk-road]: US Department of Justice (2015). *Ross Ulbricht sentenced to life in prison*. <https://www.justice.gov/usao-sdny/pr/ross-ulbricht-aka-dread-pirate-roberts-sentenced-manhattan-federal-court-life-prison>
[^slush]: Braiins (2020). *Hashing history: the story of Braiins*. <https://braiins.com/blog/hashing-history-the-story-of-braiins>
[^avalon]: Braiins (2020). Interview with Jan Čapek on mining hardware and software. <https://braiins.com/blog/jan-capek-braiins-its-time-to-give-back-the-control-over-mining-software-to-miners>
[^bip1]: BIP 1: BIP Purpose and Guidelines. <https://github.com/bitcoin/bips/blob/master/bip-0001.mediawiki>
[^bip13]: BIP 13: Address Format for pay-to-script-hash. <https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki>
[^bip16]: BIP 16: Pay to Script Hash. <https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki>
[^bitcoin-foundation]: Andresen, G. (2012). *Bitcoin Foundation announcement*. <https://bitcointalk.org/index.php?topic=113400.0>
[^fincen]: FinCEN (2013). *Application of FinCEN's Regulations to Persons Administering, Exchanging, or Using Virtual Currencies* (FIN-2013-G001). <https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering>
[^bitlicense]: New York State Department of Financial Services. *Virtual currency businesses*. <https://www.dfs.ny.gov/apps_and_licensing/virtual_currency_businesses>
[^japan]: CoinDesk (2017). *Japan's bitcoin law goes into effect tomorrow*. <https://www.coindesk.com/markets/2017/03/31/japans-bitcoin-law-goes-into-effect-tomorrow>
[^bip101]: BIP 101: Increase maximum block size. <https://github.com/bitcoin/bips/blob/master/bip-0101.mediawiki>
[^segwit2x]: CoinDesk (2017). *Bitcoin hard fork suspended for lack of consensus*. <https://www.coindesk.com/markets/2017/11/08/2x-called-off-bitcoin-hard-fork-suspended-for-lack-of-consensus>
[^bip148]: BIP 148: Mandatory activation of segwit deployment. <https://github.com/bitcoin/bips/blob/master/bip-0148.mediawiki>
[^bip141]: BIP 141: Segregated Witness (Consensus layer). <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>
[^segwit-activation]: Blockchain.com. *Bitcoin block 481824*. <https://www.blockchain.com/explorer/blocks/btc/481824>
[^lightning]: Poon, J. and Dryja, T. (2016). *The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments*. <https://lightning.network/lightning-network-paper.pdf>
[^lnd]: Lightning Labs (2018). *lnd v0.4-beta release notes*. <https://github.com/lightningnetwork/lnd/releases/tag/v0.4-beta>
[^bip340]: BIP 340: Schnorr Signatures for secp256k1. <https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki>
[^bip341]: BIP 341: Taproot: SegWit version 1 spending rules. <https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki>
[^bip350]: BIP 350: Bech32m format for v1+ witness addresses. <https://github.com/bitcoin/bips/blob/master/bip-0350.mediawiki>
[^cambridge]: Cambridge Judge Business School (2021). *New data reveals timeline of China's bitcoin mining exodus*. <https://www.jbs.cam.ac.uk/2021/new-data-reveals-timeline-of-chinas-bitcoin-mining-exodus/>
[^cboe]: Cboe (2017). *Cboe Bitcoin Futures product launch date*. <https://cdn.cboe.com/resources/schedule_update/2017/Cboe-Bitcoin-Futures-Product-Launch-Date-and-December-Transaction-Fee-Waiver.pdf>
[^strategy]: Strategy (2025). *MicroStrategy is now Strategy*. <https://software.strategy.com/news/microstrategy-is-now-strategy_02-05-2025>
[^tesla]: Tesla (2021). *2020 Form 10-K*. <https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm>
[^el-salvador]: The Block (2025). *El Salvador passes bill to revise bitcoin adoption strategy per IMF deal*. <https://www.theblock.co/post/337885/el-salvador-passes-bill-to-revise-bitcoin-adoption-strategy-per-imf-deal-reuters>
[^sec-etf]: Gensler, G. (2024). *Statement on the Approval of Spot Bitcoin Exchange-Traded Products*. US SEC. <https://www.sec.gov/newsroom/speeches-statements/gensler-statement-spot-bitcoin-011023>
[^sbr]: The White House (2025). *Establishment of the Strategic Bitcoin Reserve and United States Digital Asset Stockpile*. <https://www.whitehouse.gov/presidential-actions/2025/03/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile/>
[^ath]: CoinDesk (2025). *How October was the most destructive month in recent memory for at least some crypto traders*. <https://www.coindesk.com/markets/2025/10/27/how-october-was-the-most-destructive-month-in-recent-memory-for-crypto-traders>
[^oct-2025]: CoinDesk Research (2025). *The $19 billion liquidation that shook crypto*. <https://www.coindesk.com/research/market-spotlight-the-19-billion-liquidation-that-shook-crypto>
[^maturity]: Bitcoin Core source, `src/consensus/consensus.h` (`COINBASE_MATURITY`). <https://github.com/bitcoin/bitcoin/blob/master/src/consensus/consensus.h>
[^bip173]: BIP 173: Base32 address format for native v0-16 witness outputs. <https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki>
[^core-rebrand]: Bitcoin Core 0.9.0 release notes. <https://bitcoin.org/en/release/v0.9.0>
[^bips]: Bitcoin Improvement Proposals repository. <https://github.com/bitcoin/bips>
[^bip50]: BIP 50: March 2013 Chain Fork Post-Mortem. <https://github.com/bitcoin/bips/blob/master/bip-0050.mediawiki>
[^mtgox]: Mt. Gox (2014). *Notice concerning bitcoin balances, 20 March*. <https://www.mtgox.com/img/pdf/20140320-btc-announce.pdf>
[^mtgox-yen]: The Block (2023). *Mt. Gox reportedly starts repaying some creditors via PayPal*. <https://www.theblock.co/post/269212/mt-gox-reportedly-starts-repaying-some-creditors-via-paypal>
[^mtgox-btc]: The Block (2024). *Mt. Gox starts making repayment in bitcoin and bitcoin cash*. <https://www.theblock.co/post/303614/mt-gox-starts-making-repayment-in-bitcoin-and-bitcoin-cash-trustee>
[^bitfinex]: US Department of Justice (2022). *Two arrested for alleged conspiracy to launder stolen cryptocurrency*. <https://www.justice.gov/opa/pr/two-arrested-alleged-conspiracy-launder-45-billion-stolen-cryptocurrency>
[^core30]: Bitcoin Core 30.0 release notes. <https://bitcoincore.org/en/releases/30.0/>
[^bip110]: CoinDesk (2026). *Controversial bitcoin fork BIP-110 mines two blocks, then stops*. <https://www.coindesk.com/tech/2026/08/09/controversial-bitcoin-fork-bip-110-mines-two-blocks-then-stops>
[^faq]: Bitcoin.org. *Frequently asked questions*. <https://bitcoin.org/en/faq>
[^halvings]: Bitcoin.org. *Halving history and issuance schedule*. <https://bitcoin.org/en/halving>
[^digicash]: Wired (1998). *DigiCash outta cash*. <https://www.wired.com/1998/11/digicash-outta-cash/>
[^domain]: Bitcoin.org (2018). *Bitcoin.org is 10 years old*. <https://bitcoin.org/en/posts/ten-year-anniversary>
[^release01]: Nakamoto, S. (2009). *Bitcoin v0.1 released*. <https://satoshi.nakamotoinstitute.org/emails/cryptography/16/>
[^first-tx]: Blockchain.com. *Transaction f4184fc5…*. <https://www.blockchain.com/explorer/transactions/BTC/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16>
[^finney]: Finney, H. (2013). *Bitcoin and me*. <https://bitcointalk.org/index.php?topic=155054.0>
[^pizza]: Hanyecz, L. (2010). *Pizza for bitcoins?* <https://bitcointalk.org/index.php?topic=137.0>
[^overflow-fix]: Nakamoto, S. (2010). *Fix for block 74638 overflow output transaction*. <https://github.com/bitcoin/bitcoin/commit/d4c6b90ca3f9b47adb1b2724a0c3514f80635c84>
[^pardon]: US Department of Justice (2025). *Ulbricht pardon warrant, 21 January*. <https://www.justice.gov/pardon/media/1386096/dl>
[^bip3]: BIP 3. *Updated BIP process*. <https://bitcoin.org/bip/3/>
[^bch]: BitGo documentation. *Bitcoin Cash fork notes*. <https://specs.bitgo.com/coins/bitcoin-cash>
[^cme]: CME (2017). *Initial listing of the Bitcoin futures contract*. <https://www.cmegroup.com/notices/clearing/2017/12/Chadv17-468.html>
[^strategy-treasury]: Strategy. *The Bitcoin strategy*. <https://software.strategy.com/video/the-bitcoin-strategy-futureproofing-an-organization-with-the-worlds-hardest-money>
[^price-history]: CoinDesk. *Bitcoin price history*. <https://www.coindesk.com/price/bitcoin>
[^blockchain-guide]: Bitcoin developer guide. *Block chain*. <https://developer.bitcoin.org/devguide/block_chain.html>
[^payment-guide]: Bitcoin developer guide. *Payment processing*. <https://developer.bitcoin.org/devguide/payment_processing.html>
[^transactions-guide]: Bitcoin developer guide. *Transactions*. <https://developer.bitcoin.org/devguide/transactions.html>
[^core321]: Bitcoin Core. *32.1 release notes*. <https://bitcoincore.org/en/releases/32.1/>
[^core321-date]: Bitcoin Core (2026). *32.1 released, 27 October*. <https://bitcoincore.org/en/2026/10/27/release-32.1/>
[^ordinals]: Ordinal Theory Handbook. *Inscriptions*. <https://docs.ordinals.com/inscriptions.html>
[^taproot-block]: Blockchain.com. *Bitcoin block 709632*. <https://www.blockchain.com/explorer/blocks/btc/709632>
[^energy]: Cambridge Centre for Alternative Finance. *Cambridge Bitcoin Electricity Consumption Index*. <https://ccaf.io/cbnsi/cbeci>
[^block-assembly]: Bitcoin Core source. *Block assembly*. <https://raw.githubusercontent.com/bitcoin/bitcoin/master/src/node/miner.cpp>
[^mempool]: Bitcoin Core. *getrawmempool RPC documentation*. <https://bitcoincore.org/en/doc/30.0.0/rpc/blockchain/getrawmempool/>
[^ordinals-history]: Rodarmor, C. (2024). *How Ordinals Came to Be*. <https://casey.github.io/blog/how-ordinals-came-to-be/>
[^el-salvador-imf]: IMF (2025). *El Salvador: Selected Issues*, Country Report 25/68. <https://www.imf.org/-/media/files/publications/cr/2025/english/1slvea2025003-print-pdf.pdf>
[^binance-incident]: Binance (2026). *Security Incident Update #2, 30 October*. <https://www.binance.com/en/support/announcement/detail/d3306d9dca5243548c813b605e1d1751>

[^mtgox-filing]: Mt. Gox (2014). *Announcement regarding an application for commencement of a procedure of civil rehabilitation, 28 February*. <https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf>
