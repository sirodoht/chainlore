---
title: Vitalik Buterin
ticker: None
category: Person
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
written_by: claude-haiku-5-5 (high effort)
---

Vitalik Buterin is a cryptocurrency developer and writer whom ethereum.org credits with conceiving Ethereum, a blockchain platform that supports smart contracts.[^1][^2]

Buterin's public work goes well beyond founding Ethereum. He co-authored the EIP-1559 fee-market proposal[^imp-4-1], co-proposed the quadratic funding mechanism with Zoë Hitzig and E. Glen Weyl[^imp-4-2], wrote essays on scaling[^blobs], and made a large cryptocurrency donation for COVID-19 relief in India[^imp-4-14]. He was also involved in the aftermath of the 2016 DAO hack[^dao-attack] and has been a prominent voice in debates over the Ethereum Foundation.[^imp-4-6]

| Field | Detail |
| --- | --- |
| Born | 1994, Russia, according to ethereum.org[^1] |
| Raised | Canada[^1] |
| Known for | Conceiving Ethereum and authoring its original whitepaper[^1][^2] |
| Blog | vitalik.eth.limo, with source code in a public GitHub repository[^3] |

## History

Buterin discovered Bitcoin in 2011. A University of Waterloo biography dates his co-founding of *Bitcoin Magazine* to September 2011 and his Ethereum whitepaper to November 2013.[^waterloo-bio]

Ethereum.org's history also dates the first sharing of the whitepaper to November 2013; the version hosted on its whitepaper page is described as published in 2014.[^1][^2]

His blog is at vitalik.eth.limo. Its source is kept in a public GitHub repository under his account, which describes the site as “Vitalik's blog”.[^3]

Ethereum.org names eight co-founders, including Gavin Wood, Joseph Lubin, Jeffrey Wilcke and Mihai Alisie.[^1]

### Early life and education

The University of Waterloo reports that Buterin studied computer science there and worked as a research assistant for cryptographer Ian Goldberg. It says he received a $100,000 Thiel Fellowship in 2014 and subsequently left Waterloo to work on Ethereum full time.[^waterloo]

## Technology

The 2014 whitepaper describes a blockchain with a built-in, fully fledged Turing-complete programming language. That language is used to create “contracts” that encode arbitrary state transition functions.[^2] The paper treats proof-of-stake as an alternative to proof-of-work, but sets the comparison aside as beyond its scope.[^2]

Ethereum later moved from proof-of-work to proof-of-stake in September 2022. Ethereum.org cautions that the original whitepaper is a historical document rather than a description of the present network.[^1][^2]

## Technical and research work

### EIP-1559 fee market

Buterin is listed first among six authors of EIP-1559, “Fee market change for ETH 1.0 chain”. The EIP page marks it as Final and gives a creation date of 13 April 2019.[^imp-4-1] The proposal makes the base fee per gas rise or fall from block to block, depending on how much gas the parent block used compared with its gas target. In the proposal's proof-of-work setting, the base fee was burned and miners received the priority fee rather than the base fee.[^imp-4-1]

The authors argue that burning the base fee ensures only ETH can pay transaction fees, strengthens ETH's economic role, and reduces risks associated with miner extractable value (MEV). They also argue that keeping the base fee away from miners removes any incentive for them to manipulate it.[^imp-4-1] These are the authors' own rationales, not independent findings.

### Scaling and layer 2 essays

After the Dencun upgrade, Buterin wrote in March 2024 that rollups needed to scale their own execution as well as benefiting from Ethereum's cheaper data space. He identified parallel execution, storage, and their interactions as engineering challenges for rollups.[^blobs]

In February 2026 CoinDesk reported that a new Buterin post reflected a renewed focus on scaling Ethereum's base layer, after several years in which much of the ecosystem's scaling strategy centred on layer 2 rollups.[^imp-4-9]

### Private API payments

In October 2026, the Ethereum Foundation announced zkAPI, an implementation of a private API-payment design by Buterin and Davide Crapis. The announcement describes separating a user's payment identity from metered API requests with zero-knowledge proofs, while acknowledging that network metadata and request content can still reveal links between sessions.[^zkapi]

## Governance

Ethereum.org describes the network as community-governed and says it has no CEO or single controlling party. The Ethereum Foundation is a supporting organisation, distinct from the network.[^1]

In January 2025, CoinDesk reported that Buterin was directing a Foundation leadership reorganisation. In February, executive director Aya Miyaguchi announced that she would move to the role of president.[^4][^aya]

### Ethereum Foundation restructuring (2026)

On 24 May 2026, The Block reported Buterin's explanation of the Foundation's restructuring. He presented it as his personal view, not the board's position. He said the Foundation would prioritise long-term sustainability, reduce ETH sales, and concentrate on censorship and capture resistance, open source, privacy, and security. He also said he wanted his own influence within the organisation to decline.[^imp-4-6]

The report placed those remarks in the context of departures: at least eight senior contributors had left or announced plans to leave during 2026 by the time of publication, including five in May. The account describes Buterin's proposed direction amid a governance debate, rather than an independently audited outcome.[^imp-4-6]

## Philanthropy and public goods

Buterin co-authored the quadratic funding proposal with Zoë Hitzig and E. Glen Weyl; their preprint was submitted in September 2018. The mechanism uses the square of the sum of the square roots of contributions to determine funding, giving broad participation weight beyond the size of individual donations. Gitcoin describes using quadratic funding in its grants programme.[^qf-paper][^imp-4-2]

In May 2021 Buterin donated about 50 trillion Shiba Inu tokens to the India-focused CryptoRelief fund. CoinDesk's later account valued the donation at about $1.2 billion at the time and said the tokens had been sent to him unsolicited by their creators. That was a market valuation of tokens, not a claim that the fund immediately received the same amount in spendable dollars.[^imp-4-14]

In January 2022 CoinDesk reported that CryptoRelief planned to return $100 million in USDC to Buterin for COVID-related science and relief projects worldwide. This was a portion of the original donation, not its entire headline valuation.[^imp-4-14]

## Incidents and controversies

**eth.limo hijack attempt.** In April 2026, registrar EasyDNS acknowledged that a social-engineering attack had tricked it into a bogus account recovery for eth.limo, the gateway used by Buterin's blog. EasyDNS said DNSSEC-aware resolvers rejected the changed nameserver responses. The Block reported that Buterin warned readers to avoid eth.limo links, shared an IPFS alternative, and subsequently confirmed that the incident was resolved.[^easydns][^7]

**Foundation remarks (January 2025).** CoinDesk reported that Buterin condemned inflammatory posts targeting Miyaguchi during the leadership dispute, including threats and calls for bullying.[^4]

### The DAO hack and the 2016 hard fork

The DAO, an investment organisation on Ethereum, raised approximately 12 million ETH, valued at about $150 million at the time, according to the SEC's investigation. In June 2016, an exploit diverted ether into a child DAO. Buterin's contemporaneous notice described the recursive-call vulnerability and proposed an initial soft-fork response.[^dao-report][^dao-attack]

Buterin's post of 20 July 2016 announced a completed hard fork. Block 1,920,000 executed an irregular state change that moved about 12 million ETH from the “Dark DAO” and “Whitehat DAO” contracts into a WithdrawDAO recovery contract. The post said roughly 85% of miners were mining on the fork and that about 4.5 million ETH had been sent to DAO token holders.[^imp-4-18]

The fork was divisive. Ethereum's history records that some participants rejected intervention in an application-level failure and continued the non-fork chain as Ethereum Classic. In June 2026, The Block reported that Buterin was among the curators overseeing a security endowment funded by more than 75,000 ETH from unclaimed recovery assets.[^fork-history][^dao-fund]

## Timeline

- **1994:** Born in Russia, according to ethereum.org.[^1]
- **2011:** Discovers Bitcoin and co-founds *Bitcoin Magazine*, according to Waterloo's biography.[^waterloo-bio]
- **November 2013:** Shares the Ethereum whitepaper.[^waterloo-bio]
- **January 2014:** Announces the Ethereum concept publicly at the North American Bitcoin Conference in Miami.[^1]
- **9 May 2015:** Announces the Olympic pre-release testnet.[^olympic]
- **30 July 2015:** Ethereum's mainnet launches.[^1]
- **20 July 2016:** Announces completion of the DAO recovery fork.[^imp-4-18]
- **September 2022:** Ethereum shifts to proof-of-stake.[^1]

## References

[^1]: [History of Ethereum: founder, launch and ownership | ethereum.org](https://ethereum.org/ethereum-history-founder-and-ownership/)
[^2]: [Ethereum Whitepaper | ethereum.org](https://ethereum.org/whitepaper/)
[^3]: [GitHub - vbuterin/blog](https://github.com/vbuterin/blog)
[^4]: [Ethereum's Vitalik Buterin Goes on Offense Amid Major Leadership Shake-up](https://www.coindesk.com/tech/2025/01/21/ethereum-s-vitalik-buterin-goes-on-offense-amid-major-leadership-shake-up)
[^7]: [EasyDNS accepts responsibility for eth.limo hijack, its first social engineering breach in 28 years](https://www.theblock.co/post/398005/easydns-accepts-responsibility-for-eth-limo-hijack-its-first-social-engineering-breach-in-28-years)
[^imp-4-1]: [EIP-1559: Fee market change for ETH 1.0 chain](https://eips.ethereum.org/EIPS/eip-1559)
[^imp-4-2]: [Quadratic Funding](https://gitcoin.co/mechanisms/quadratic-funding)
[^imp-4-6]: [Vitalik Buterin says Ethereum Foundation will be a 'smaller ship,' sell less ETH amid researcher exodus](https://www.theblock.co/post/402435/vitalik-buterin-says-ethereum-foundation-will-be-a-smaller-ship-sell-less-eth-amid-researcher-exodus)
[^imp-4-9]: [Ethereum news: Vitalik Buterin reveals his bold new plan to fix the network's scaling problem](https://www.coindesk.com/tech/2026/02/27/vitalik-buterin-reveals-his-bold-new-plan-to-fix-ethereum-s-scaling-problem)
[^imp-4-14]: [Buterin to Use Returned $100M From SHIB Donation for COVID Projects Worldwide](https://www.coindesk.com/business/2022/01/28/buterin-to-use-returned-100m-from-shib-donation-for-covid-projects-worldwide)
[^imp-4-18]: [Hard Fork Completed | Ethereum Foundation Blog](https://blog.ethereum.org/2016/07/20/hard-fork-completed)

[^waterloo-bio]: University of Waterloo (2019-03-25). *Vitalik Buterin — Cryptocurrencies and Blockchains: Combining Mechanism Design and Computation*. <https://cs.uwaterloo.ca/events/dls-vitalik-buterin-cryptocurrencies-blockchains>
[^waterloo]: University of Waterloo (2024-07-10). *Vitalik Buterin at Waterloo*. <https://cs.uwaterloo.ca/news/vitalik-buterin-waterloo>
[^blobs]: Buterin, V. (2024-03-28). *Ethereum has blobs. Where do we go from here?* <https://vitalik.eth.limo/general/2024/03/28/blobs.html>
[^zkapi]: Ethereum Foundation (2026-10-01). *Introducing zkAPI: private usage credits for any API*. <https://blog.ethereum.org/en/2026/10/01/introducing-zkapi>
[^aya]: Miyaguchi, A. (2025-02-25). *A new chapter in the infinite garden*. Ethereum Foundation. <https://blog.ethereum.org/2025/02/25/aya-announcement>
[^qf-paper]: Buterin, V., Hitzig, Z., and Weyl, E. G. (2018). *A Flexible Design for Funding Public Goods*. <https://arxiv.org/abs/1809.06421>
[^easydns]: EasyDNS (2026-04-18). *We screwed up and we own it: The eth.limo sh*tshow is on us*. <https://easydns.com/blog/2026/04/18/we-screwed-up-and-we-own-it-the-eth-limo-shtshow-is-on-us/>
[^dao-report]: SEC (2017-07-25). *Report of Investigation: The DAO*, Release No. 81207. <https://www.sec.gov/litigation/investreport/34-81207.pdf>
[^dao-attack]: Buterin, V. (2016-06-17). *CRITICAL UPDATE Re: DAO Vulnerability*. Ethereum Foundation. <https://blog.ethereum.org/2016/06/17/critical-update-re-dao-vulnerability>
[^fork-history]: Ethereum.org. *Timeline of all Ethereum forks*, DAO fork. <https://ethereum.org/ethereum-forks/>
[^dao-fund]: The Block (2026-06-18). *The DAO hack at 10: From $50 million exploit to a $130 million Ethereum security fund*. <https://www.theblock.co/news/ecosystems/2026-06-18-ethereum-130-million-security-fund-the-dao-hack-10-years-405248>
[^olympic]: Buterin, V. (2015-05-09). *Olympic: Frontier Pre-Release*. Ethereum Foundation. <https://blog.ethereum.org/2015/05/09/olympic-frontier-pre-release>
