---
title: Litecoin
ticker: LTC
category: Layer 1
status: draft
updated: 2026-11-23
written_by: claude-haiku-5-5 (high effort)
---

Litecoin (LTC) is an open-source, proof-of-work cryptocurrency created by Charlie Lee.[^1][^2] It was launched in 2011 as a fork of Bitcoin's codebase with modified parameters.[^3][^4]

| Property | Value |
|---|---|
| Ticker | LTC[^5] |
| Creator | Charlie Lee[^1][^2] |
| Announced | 2011-10-09, on Bitcointalk[^1] |
| Consensus | Scrypt proof of work[^3] |
| Target block time | About 2.5 minutes[^3] |
| Maximum supply | 84 million LTC[^3] |
| Halving interval | Every 840,000 blocks, about four years (secondary source)[^6] |
| Licence | MIT/X11[^7] |
| Privacy extension | MWEB, based on Mimblewimble[^8] |
| Spot ETF | Canary Capital Litecoin ETF (NASDAQ: LTCC), described by the Litecoin Foundation as the first U.S. spot Litecoin ETF[^9] |

## History

The launch announcement is a Bitcointalk thread titled '[ANN] Litecoin - a lite version of Bitcoin. Launched!', and its opening post carries an October 9, 2011 timestamp.[^imp-58-1] The post says that "some of us who joined together on IRC" set out to create an alternative currency similar to Bitcoin, and that they "wanted to make a coin that is silver to Bitcoin's gold".[^imp-58-1] Of the six earlier altcoins the post reviews, it labels three as 'Dead': ixcoin, i0coin and SolidCoin.[^imp-58-1] The post also says Litecoin would begin with 150 premined coins: the genesis block and the first two blocks.[^imp-58-1]

Wikipedia gives October 7, 2011 as the release date, while the forum post is timestamped October 9, 2011, so the exact start date is not settled here.[^imp-34-2] The forum page shows a last edit dated June 25, 2014, so its current wording may differ from the 2011 original.[^imp-34-1]

A TechCrunch report from December 2017 describes Lee as the former director of engineering at Coinbase and as the founder of Litecoin, which he started in 2011.[^imp-57-2]

According to Wikipedia, a weak source for this draft, Dogecoin began merge-mining with Litecoin in September 2014.[^11] Crypto-press reporting says Litecoin activated SegWit in April 2017, and that Bitcoin followed a few months later.[^12]

## Technology

The 2011 launch post pointed readers to a GitHub repository for the source code.[^imp-34-1]

**Proof of work.** Litecoin uses Scrypt proof of work to validate transactions and secure the network.[^3] The launch thread says the developers liked Tenebrix's Scrypt design and thanks ArtForz for the implementation.[^1] The thread compares Litecoin's 2.5-minute average block time with Bitcoin's 10 minutes.[^1] Trezor states that difficulty adjusts every 2,016 blocks, about 3.5 days.[^3]

**Supply.** The maximum supply is 84 million LTC.[^3] A secondary source states that mining rewards halve every 840,000 blocks, approximately every four years.[^6] The smallest unit is the litoshi, equal to 10⁻⁸ LTC.[^3]

**MWEB.** LIP-0003, the draft proposal for MimbleWimble via Extension Blocks, describes an opt-in MimbleWimble transaction format carried through extension blocks. Extension blocks run alongside the main chain's canonical blocks at the same average interval of 2.5 minutes, and users opt in by moving coins into and out of the extension block through an integrating transaction.[^imp-57-3] The same proposal lists David Burkett, Andrew Yang and Charlie Lee as its authors.[^imp-57-3]

Crypto-press reporting says Litecoin reached the 75% network consensus threshold for MWEB activation on May 2, and that MWEB then locked in for activation at block height 2,257,920.[^imp-34-3] The article is dated May 22, 2022, and describes MWEB as an opt-in feature for confidential transactions.[^imp-34-3]

## Governance

The project states that Litecoin is released under the MIT/X11 licence.[^7] Its website also says 'No board, no central bank, no CEO'. This is the project's self-description and has not been independently verified here.[^7]

## Incidents and controversies

**March 2026 MWEB exploit.** The Litecoin developers' postmortem describes a validation flaw in the MWEB implementation. Missing revalidation of MWEB input metadata during block connection allowed a block producer to include an input whose metadata did not match the UTXO being spent, so a small input could support a much larger pegout.[^5] A chain scan showed the exploit had already occurred at block height 3,073,882, pegging out 85,034.47285734 LTC.[^5] The postmortem says the actor later signed a recovery transaction that returned the funds except an agreed 850 LTC bounty, and that no confirmed user funds were ultimately lost. It also acknowledges that the network temporarily relied on emergency miner coordination.[^5]

**April 2026 disruption and reorg.** The postmortem says a later attempt used the same exploit path. Upgraded nodes rejected the bad block, but the handling of mutated MWEB block data left some upgraded mining nodes unable to mine normally. Unupgraded miners extended an invalid 13-block chain, which was later reorged out after upgraded miners coordinated on the valid chain.[^5] Litecoin Core 0.21.5.4, released April 25, addressed this failure mode.[^5]

**Third-party effects.** According to the postmortem, the attacker swapped 11,000 LTC for 7.78814476 BTC through NEAR Intents and 10 LTC for 0.00719957 BTC through THORChain. After the reorg those LTC were no longer on the valid chain. Exact third-party transaction IDs and final loss amounts were still being collected.[^5]

**Source caveat.** A commentary site argues that a reported $600,000 figure is not an established final loss.[^18]

## Timeline

| Date | Event |
|---|---|
| 2011-10-09 | Launch announcement posted on Bitcointalk.[^1] |
| 2014-09 | Dogecoin begins merge-mining with Litecoin (weak source).[^11] |
| 2017-04 | SegWit activated on Litecoin, per crypto-press reporting.[^12] |
| 2024-10-15 | Canary Capital files its S-1 application with the SEC.[^9] |
| 2026-03-19 | Developers identify the MWEB validation flaw; chain scan confirms the exploit at block 3,073,882.[^5] |
| 2026-03-24 | Recovery transaction mined, returning funds except the 850 LTC bounty.[^5] |
| 2026-03-25 | Rebalancing peg-in mined at block 3,078,098.[^5] |
| 2026-04-25 | Second attempt leads to a 13-block invalid chain, later reorged out; Litecoin Core 0.21.5.4 released.[^5] |

## References

[^1]: [Litecoin - a lite version of Bitcoin. Launched! (Bitcointalk announcement thread)](https://bitcointalk.org/index.php?topic=47417.0)
[^2]: [Who is Charlie Lee? - People Profiles](https://www.bitstamp.net/learn/people-profiles/charlie-lee/)
[^3]: [Litecoin: what it is and how it works with Trezor](https://trezor.io/learn/supported-assets/other-cryptocurrencies/litecoin-what-it-is-and-how-it-works-with-trezor)
[^4]: [litecoin/README.md at master · litecoin-project/litecoin · GitHub](https://github.com/litecoin-project/litecoin/blob/master/README.md)
[^5]: [Litecoin MWEB Security Incident Postmortem](https://litecoin.com/news/litecoin-mweb-security-incident-postmortem)
[^6]: [Litecoin (LTC)](https://chainquiry.com/projects/litecoin/)
[^7]: [Learn about Litecoin](https://litecoin.com/what-is-litecoin)
[^8]: [mweb](https://litecoin.com/projects/mweb)
[^9]: [Litecoin Spot ETF Now Trading (NASDAQ: LTCC)](https://litecoin.com/news/litecoin-spot-etf-approved)
[^11]: [Litecoin](https://en.wikipedia.org/wiki/Litecoin)
[^12]: [Litecoin Activates MimbleWimble Extension Blocks (MWEB)](https://cryptopotato.com/litecoin-activates-mimblewimble-extension-blocks-mweb/)
[^18]: [Litecoin's 2026 MWEB incidents: what the postmortem establishes — Litecoin.watch](https://litecoin.watch/articles/litecoin-s-first-security-incident-mweb-exploit-triggers-13-block-reorg-and-600k-loss)

[^imp-34-1]: [Litecoin - a lite version of Bitcoin. Launched! (Bitcointalk announcement thread)](https://bitcointalk.org/index.php?topic=47417.0)
[^imp-34-2]: [Litecoin - Wikipedia](https://en.wikipedia.org/wiki/Litecoin)
[^imp-34-3]: [Litecoin Activates MimbleWimble Extension Blocks (MWEB) - CryptoPotato](https://cryptopotato.com/litecoin-activates-mimblewimble-extension-blocks-mweb/)

[^imp-57-2]: [Litecoin founder Charlie Lee has sold all of his LTC | TechCrunch](https://techcrunch.com/2017/12/20/litecoin-charlie-lee-conflict-of-interest/amp)
[^imp-57-3]: [LIP-0003: MimbleWimble via Extension Blocks (Litecoin Improvement Proposal, Draft)](https://github.com/litecoin-project/lips/blob/master/lip-0003.mediawiki)

[^imp-58-1]: [Bitcointalk announcement thread, opening post: Litecoin - a lite version of Bitcoin. Launched!](https://bitcointalk.org/index.php?topic=47417.0)
