---
title: Litecoin
ticker: LTC
category: Layer 1
status: draft
updated: 2026-11-18
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

The launch announcement was posted on Bitcointalk in a thread titled 'Litecoin - a lite version of Bitcoin. Launched!', with a first post timestamped October 9, 2011.[^1] The post says the project was started by people who met on IRC to create an alternative currency similar to Bitcoin, and that it aimed to be 'silver to Bitcoin's gold'.[^1] The post surveys earlier altcoins, several of which it calls dead, and says the coin would begin with 150 premined coins: the genesis block and the first two blocks.[^1]

Bitstamp describes Lee as a computer scientist and entrepreneur best known as the inventor of Litecoin.[^2] Bitstamp also notes that LTC has fallen in crypto market rankings over recent cycles.[^2]

According to Wikipedia, a weak source for this draft, Dogecoin began merge-mining with Litecoin in September 2014.[^11] Crypto-press reporting says Litecoin activated SegWit in April 2017, and that Bitcoin followed a few months later.[^12]

## Technology

**Proof of work.** Litecoin uses Scrypt proof of work to validate transactions and secure the network.[^3] The launch thread says the developers liked Tenebrix's Scrypt design and thanks ArtForz for the implementation.[^1] The thread compares Litecoin's 2.5-minute average block time with Bitcoin's 10 minutes.[^1] Trezor states that difficulty adjusts every 2,016 blocks, about 3.5 days.[^3]

**Supply.** The maximum supply is 84 million LTC.[^3] A secondary source states that mining rewards halve every 840,000 blocks, approximately every four years.[^6] The smallest unit is the litoshi, equal to 10⁻⁸ LTC.[^3]

**MWEB.** The project describes Mimblewimble Extension Blocks (MWEB) as based on the Mimblewimble protocol, promising confidential transactions and efficient pruning.[^8] According to the project, MWEB works alongside the main blockchain while remaining compatible with existing wallets and services.[^8] Crypto-press reporting names David Burkett, a Mimblewimble developer, as leading development of the protocol for Litecoin.[^12] A weak commentary source states that only activity inside MWEB is shielded.[^14]

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
[^14]: [MWEB three years on: what the adoption data actually says about Litecoin privacy — Litecoin.watch](https://litecoin.watch/articles/mweb-three-years-on-what-the-adoption-data-actually-says-about-litecoin-privacy)
[^18]: [Litecoin's 2026 MWEB incidents: what the postmortem establishes — Litecoin.watch](https://litecoin.watch/articles/litecoin-s-first-security-incident-mweb-exploit-triggers-13-block-reorg-and-600k-loss)
