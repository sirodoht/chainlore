---
title: Vitalik Buterin
ticker: None
category: Person
status: draft
updated: 2026-10-31
written_by: claude-haiku-5-5 (high effort)
---

Vitalik Buterin is a cryptocurrency developer and writer whom ethereum.org credits with conceiving Ethereum, a blockchain platform that supports smart contracts.[^1][^2] The project describes him as its chief visionary and advocate, and states that Ethereum has no CEO or single controlling party.[^1] This draft has not been fact-checked, and claims from weaker sources are attributed.

Buterin's public work goes well beyond founding Ethereum. He co-authored the EIP-1559 fee-market proposal[^imp-4-1], co-proposed the quadratic funding mechanism with Zoë Hitzig and E. Glen Weyl[^imp-4-2], wrote essays on scaling[^imp-4-3], and made large cryptocurrency donations for COVID-19 relief in India[^imp-4-4]. He was also involved in the aftermath of the 2016 DAO hack[^imp-4-5] and has been a prominent voice in debates over the Ethereum Foundation.[^imp-4-6] The sections below cover each area, with claims attributed to their sources.

| Field | Detail |
| --- | --- |
| Born | 1994, Russia, according to ethereum.org[^1] |
| Raised | Canada[^1] |
| Known for | Conceiving Ethereum and authoring its original whitepaper[^1][^2] |
| Ethereum role | Described as chief visionary and advocate[^1] |
| Blog | vitalik.eth.limo, with source code in a public GitHub repository[^3] |
| Ethereum native currency | ETH, described as Ethereum's native currency[^6] |

## History

According to ethereum.org, Buterin discovered Bitcoin in 2011 and co-founded *Bitcoin Magazine* in 2012.[^1] The same page dates the idea of Ethereum to late 2013.[^1]

Dates for the whitepaper differ across the sources reviewed. The history page says he shared the whitepaper in November 2013.[^1] The whitepaper page describes it as published in 2014, before Ethereum launched, while its metadata description says 2013.[^2] This draft does not resolve the difference.

His blog is at vitalik.eth.limo. Its source is kept in a public GitHub repository under his account, which describes the site as “Vitalik's blog”.[^3]

Ethereum.org names eight co-founders, including Gavin Wood, Joseph Lubin, Jeffrey Wilcke and Mihai Alisie.[^1]

### Early life and education

Forklog reports that Buterin was born on 31 January 1994 in Kolomna, near Moscow, and that he enrolled at the University of Waterloo in 2012.[^imp-4-7] Fortune reports that he quit his freshman year to focus full time on building Ethereum.[^imp-4-8] Forklog also reports that in 2011 he became a writer for Bitcoin Weekly, a portal devoted to the first cryptocurrency.[^imp-4-7] These are secondary reports, and this draft has not checked them against primary records.

## Technology

The 2014 whitepaper describes a blockchain with a built-in, fully fledged Turing-complete programming language. That language is used to create “contracts” that encode arbitrary state transition functions.[^2] The paper treats proof-of-stake as an alternative to proof-of-work, but sets the comparison aside as beyond its scope.[^2]

Ethereum later moved from proof-of-work to proof-of-stake. Ethereum.org dates the shift to September 2022.[^1] The whitepaper page states that “the original whitepaper no longer reflects what Ethereum is today”. It cites that shift, Layer 2 scaling, and the ERC-20 and ERC-721 standards as post-paper developments.[^2]

## Technical and research work

### EIP-1559 fee market

Buterin is listed first among six authors of EIP-1559, “Fee market change for ETH 1.0 chain”. The EIP page marks it as Final and gives a creation date of 13 April 2019.[^imp-4-1] The proposal makes the base fee per gas rise or fall from block to block, depending on how much gas the parent block used compared with its gas target. The base fee is burned, and miners keep only the priority fee.[^imp-4-1]

The authors argue that burning the base fee ensures only ETH can pay transaction fees, strengthens ETH's economic role, and reduces risks associated with miner extractable value (MEV). They also argue that keeping the base fee away from miners removes any incentive for them to manipulate it.[^imp-4-1] These are the authors' own rationales, not independent findings.

### Scaling and layer 2 essays

After the Dencun upgrade, Buterin wrote that rollups would need to “scale internally” to handle more activity, for example through parallelization. The Block reported this, and described Dencun's EIP-4844 as aimed at drastically reducing transaction fees for layer 2 networks.[^imp-4-3]

In February 2026 CoinDesk reported that a new Buterin post reflected a renewed focus on scaling Ethereum's base layer, after several years in which much of the ecosystem's scaling strategy centred on layer 2 rollups.[^imp-4-9] In a separate critique reported by Unchained, he argued that the original idea of layer 2 networks as secure extensions of Ethereum “no longer makes sense”. This is his view, not a settled finding.[^imp-4-10]

## Governance

- Ethereum.org says Ethereum has no CEO, board, or single controlling party. It describes the network as community-governed, with the non-profit Ethereum Foundation providing support.[^1]
- The same page says Buterin “remains respected in the community”, but that decisions are made through group agreement rather than by any single person.[^1]
- CoinDesk reported on 21 January 2025 that Buterin was going “on offense” amid a major leadership shake-up at the Foundation.[^4]
- The Block reported, citing a Foundation blog post, that executive director Aya Miyaguchi was “stepping up” as president. The headline notes Buterin's promise of leadership changes. The excerpt reviewed gives no exact date.[^5]

### Ethereum Foundation restructuring (2026)

On 24 May 2026 Buterin published a roughly 1,500-word post on X about the Ethereum Foundation's restructuring. The Block reported that he framed it as his personal view, not a board position.[^imp-4-6] He said the Foundation is choosing “longevity over breadth”, will sell less ETH, and will focus on censorship and capture resistance, open source, privacy and security. He also said his own power within the organisation “will continue to decrease, which is honestly what I want.”[^imp-4-6]

The Block also reported that the Foundation holds roughly 0.16% of all ETH, and that Buterin described it as “one node, with a defined purpose, alongside other nodes” rather than the centre of Ethereum.[^imp-4-6] Buterin said he had been “regularly” hearing from community members who felt the Foundation's actions did not match its rhetoric of decentralization and privacy.[^imp-4-6] At least eight senior Foundation contributors have left or announced plans to leave in 2026, including five in May.[^imp-4-6] Former Foundation developer Dankrad Feist proposed raising $1 billion for a separate Ethereum advocacy organisation “more economically aligned” with ETH.[^imp-4-6] The account here rests on Buterin's own post as reported by The Block, and no independent audit of the Foundation is cited.

## Philanthropy and public goods

Buterin co-authored the quadratic funding proposal with Zoë Hitzig and E. Glen Weyl. Gitcoin's documentation dates the original paper to 2018, while a 2020 academic paper cites the same work as 2019.[^imp-4-2][^imp-4-11] Gitcoin Grants has used the mechanism to match small donations to open-source projects.[^imp-4-12] Gitcoin describes its program as the largest and longest-running deployment of quadratic funding, having distributed over $60 million to more than 3,700 projects. That is Gitcoin's self-reported claim and has not been checked independently here.[^imp-4-2]

In May 2021 Buterin donated Shiba Inu tokens to the India Covid-Crypto Relief Fund. CNN reported that he transferred more than 50 trillion SHIB coins, a donation its headline valued at $1 billion, and that he also sent 500 ether, about $1.9 million, to the fund.[^imp-4-4] CNN reported that the SHIB had initially been gifted to him and sent to his public wallet by the coin's founders.[^imp-4-4] After the donation the coin's value fell, and CNN reported it was off about 30% the following Thursday, according to Coinbase.[^imp-4-4] A Bloomberg report, relayed by Benzinga, said only about $20 million of the donation had been paid out at that point, with another $20 million in the pipeline.[^imp-4-13]

In January 2022 CoinDesk reported that CryptoRelief, the Indian fund that received the original donation, was returning the sum, which Buterin would use for “higher-risk higher-reward” projects. CoinDesk reported the returned amount as $100 million in USDC.[^imp-4-14]

### Public statements

Fortune reported that in 2022 Buterin called Putin's attack on Ukraine a “crime against the Ukrainian and Russian people.”[^imp-4-8] In March 2026 he framed Ethereum as “sanctuary technology” rather than just a smart-contract platform, according to Crypto Times.[^imp-4-15]

## Incidents and controversies

**eth.limo hijack attempt.** Reports say that on April 17 (the year is not stated in the excerpts reviewed) an attacker impersonated an eth.limo team member to trick registrar EasyDNS into running an account recovery process. EasyDNS accepted responsibility for the breach.[^7] The attacker sought to redirect traffic through the eth.limo wildcard domain. Reports said this could affect more than 2 million ENS .eth domains, including vitalik.eth.limo.[^8] Buterin shared a direct IPFS link to his blog as a safe alternative and asked users to wait for an all-clear from the eth.limo team before resuming normal access.[^9] According to CoinCentral, the attacker never obtained eth.limo's DNSSEC signing keys.[^10] The excerpt reviewed presents Buterin as affected by the attack and warning users, not as accused of wrongdoing.[^9]

**Nerayoff allegations (2023 onward).** In November 2023, Steven Nerayoff, a crypto advisor, publicly accused Buterin and Joseph Lubin of sabotaging crypto and engaging in fraudulent ICOs. He also alleged secret dealings with government officials to create a favourable regulatory environment for ETH.[^11] These are Nerayoff's allegations. CCN wrote that the ETHgate recording, which shows Nerayoff warning Buterin about potential legal trouble, “isn't quite the bombshell Nerayoff promised”. CCN also wrote that “for now, Nerayoff's claims remain unsubstantiated”.[^12] The sources reviewed do not document a court filing or a formal response from Buterin.[^12]

**Foundation remarks (January 2025).** CoinDesk's 21 January 2025 report says Buterin labelled some inflammatory X posts about the head of the Ethereum Foundation as “pure evil”. This draft could read only the article's metadata, not its body.[^4]

**Sandwich attack.** A Long Beach News report, a weak source, says a bot known as jaredfromsubway.eth targeted a small token swap by Buterin on April 30. The report describes him as a vocal critic of maximal extractable value (MEV).[^13]

### The DAO hack and the 2016 hard fork

The DAO, a smart-contract fund on Ethereum, raised more than $160 million worth of ether from about 11,000 investors. In June 2016 someone found a vulnerability in its code and drained about 3.6 million ETH.[^imp-4-5][^imp-4-16] CoinDesk's retrospective says Buterin had not been directly involved with The DAO, but became part of the bailout effort.[^imp-4-17]

Buterin's post of 20 July 2016 announced a completed hard fork. Block 1920000 executed an irregular state change that moved about 12 million ETH from the “Dark DAO” and “Whitehat DAO” contracts into a WithdrawDAO recovery contract. The post said roughly 85% of miners were mining on the fork and that about 4.5 million ETH had been sent to DAO token holders.[^imp-4-18]

The fork was divisive. CBC reports that Buterin expected most users to move to the reset platform, but a small group kept using the old chain, calling it Ethereum Classic and arguing that he had no right to reset the platform.[^imp-4-5] CoinDesk later described the decision as “the most controversial decision in Ethereum's history.”[^imp-4-17] Unclaimed DAO funds, estimated at around 75,000 ETH, are overseen by curators that include Buterin and Griff Green, according to Crypto Briefing.[^imp-4-16]

## Timeline

- **1994:** Born in Russia, according to ethereum.org.[^1]
- **2011:** Discovers Bitcoin, according to ethereum.org.[^1]
- **2012:** Co-founds *Bitcoin Magazine*, according to ethereum.org.[^1]
- **Late 2013:** Conceives Ethereum. The history page says he shared the whitepaper in November 2013.[^1]
- **January 2014:** Announces the Ethereum concept publicly at the North American Bitcoin Conference in Miami.[^1]
- **July–August 2014:** Crowdfunding raises 31,000 BTC, reported as worth about $18 million at the time, in return for ether.[^1]
- **April 2015:** Olympic testnet launches.[^1]
- **30 July 2015:** Mainnet genesis block is mined.[^1]
- **14 March 2016:** Homestead, the first planned upgrade, follows.[^1]
- **September 2022:** Ethereum shifts to proof-of-stake.[^1]
- **21 January 2025:** CoinDesk reports on Buterin's “pure evil” remarks amid a Foundation leadership shake-up.[^4]

## References

[^1]: [History of Ethereum: founder, launch and ownership | ethereum.org](https://ethereum.org/ethereum-history-founder-and-ownership/)
[^2]: [Ethereum Whitepaper | ethereum.org](https://ethereum.org/whitepaper/)
[^3]: [GitHub - vbuterin/blog](https://github.com/vbuterin/blog)
[^4]: [Ethereum's Vitalik Buterin Goes on Offense Amid Major Leadership Shake-up](https://www.coindesk.com/tech/2025/01/21/ethereum-s-vitalik-buterin-goes-on-offense-amid-major-leadership-shake-up)
[^5]: [Ethereum Foundation's Aya Miyaguchi 'stepping up' as president as Vitalik Buterin promises leadership changes](https://www.theblock.co/post/343301/ethereum-foundations-aya-miyaguchi-stepping-up-as-president-as-vitalik-buterin-promises-leadership-changes)
[^6]: [Who is Vitalik Buterin? - Bitstamp Learn Center](https://www.bitstamp.net/en-gb/learn/people-profiles/who-is-vitalik-buterin/)
[^7]: [EasyDNS accepts responsibility for eth.limo hijack, its first social engineering breach in 28 years](https://www.theblock.co/post/398005/easydns-accepts-responsibility-for-eth-limo-hijack-its-first-social-engineering-breach-in-28-years)
[^8]: [eth.limo domain hijacked; EasyDNS admits first social engineering attack in 28 years](https://www.gate.com/news/detail/ethlimo-domain-hijacked-easydns-admits-first-social-engineering-attack-in-20445355)
[^9]: [Vitalik Buterin Warns Users After eth.limo DNS Hijack](https://tech.yahoo.com/cybersecurity/articles/vitalik-buterin-warns-users-eth-085725655.html)
[^10]: [The Attack on eth.limo Shows Why Crypto Websites Are Still Vulnerable to Old-School Hacking - CoinCentral](https://coincentral.com/the-attack-on-eth-limo-shows-why-crypto-websites-are-still-vulnerable-to-old-school-hacking/)
[^11]: [Ethereum Insider Says Vitalik Buterin and Joseph Lubin Sabotaged Crypto, Engaged in Fraudulent ICOs](https://thecryptobasic.com/2023/11/14/ethereum-insider-says-vitalik-buterin-and-joseph-lubin-sabotaged-crypto-engaged-in-fraudulent-icos/)
[^12]: [Who is Steven Nerayoff and What Does ETHgate Recording Mean for Ethereum and Buterin?](https://www.ccn.com/news/ethgate-who-is-steven-nerayoff-ethereum/)
[^13]: [Vitalik Buterin Sandwich Attack by JaredfromSubway Bot](https://thelongbeachnews.com/jaredfromsubway-bot-front-runs-vitalik-buterins-4-token-swap-with-1-million-in-volume)

[^imp-4-1]: [EIP-1559: Fee market change for ETH 1.0 chain](https://eips.ethereum.org/EIPS/eip-1559)
[^imp-4-2]: [Quadratic Funding](https://gitcoin.co/mechanisms/quadratic-funding)
[^imp-4-3]: [Vitalik Buterin emphasizes need for parallelization, internal scaling in Ethereum rollups](https://www.theblock.co/post/285539/vitalik-buterin-emphasizes-need-for-parallelization-internal-scaling-in-ethereum-rollups)
[^imp-4-4]: [Ethereum co-founder Vitalik Buterin donates $1 billion of Shiba Inu coin to India Covid relief](https://www.cnn.com/2021/05/13/business/ethereum-shiba-inu-india-covid-donation/index.html)
[^imp-4-5]: [How a $64M hack changed the fate of Ethereum, Bitcoin's closest competitor](https://www.cbc.ca/news/science/ethereum-hack-blockchain-fork-bitcoin-1.3719009)
[^imp-4-6]: [Vitalik Buterin says Ethereum Foundation will be a 'smaller ship,' sell less ETH amid researcher exodus](https://www.theblock.co/post/402435/vitalik-buterin-says-ethereum-foundation-will-be-a-smaller-ship-sell-less-eth-amid-researcher-exodus)
[^imp-4-7]: [Who is Vitalik Buterin?](https://forklog.com/en/who-is-vitalik-buterin/)
[^imp-4-8]: [ethereum founder vitalik buterin biography and net worth](https://fortune.com/2022/02/24/ethereum-founder-vitalik-buterin-biography-and-net-worth)
[^imp-4-9]: [Ethereum news: Vitalik Buterin reveals his bold new plan to fix the network's scaling problem](https://www.coindesk.com/tech/2026/02/27/vitalik-buterin-reveals-his-bold-new-plan-to-fix-ethereum-s-scaling-problem)
[^imp-4-10]: [Vitalik Rethinks Ethereum's L2 Playbook, Calls for Shift Toward Native Rollups - Unchained](https://unchainedcrypto.com/vitalik-buterin-calls-for-rethink-of-ethereum-layer-2s-as-native-rollups-take-center-stage/)
[^imp-4-11]: [Quadratic Funding and Matching Funds Requirements](https://arxiv.org/pdf/2010.01193)
[^imp-4-12]: [Gitcoin quadratic funding · Polity Atlas](https://polityatlas.org/experiments/gitcoin-quadratic-funding)
[^imp-4-13]: [Ethereum Co-Founder Donated $1B Shiba Inu To Aid India In COVID-19 Battle — Money Reaching The People Is A Lot Less](https://benzinga.com/markets/cryptocurrency/21/07/22190225/ethereum-co-founder-donated-1b-shiba-inu-to-aid-india-in-covid-19-battle-money-reaching-th)
[^imp-4-14]: [Buterin to Use Returned $100M From SHIB Donation for COVID Projects Worldwide](https://www.coindesk.com/business/2022/01/28/buterin-to-use-returned-100m-from-shib-donation-for-covid-projects-worldwide)
[^imp-4-15]: [Vitalik Buterin Signals New Era for Ethereum With Foundation Mandate](https://www.cryptotimes.io/2026/03/13/vitalik-buterin-signals-new-era-for-ethereum-with-foundation-mandate/)
[^imp-4-16]: [The DAO exploit marks its 10th anniversary, a hack that drained 3.6M ETH and split Ethereum in two](https://cryptobriefing.com/dao-exploit-10th-anniversary-ethereum/)
[^imp-4-17]: [CoinDesk Turns 10: 2016 - How The DAO Hack Changed Ethereum and Crypto](https://www.coindesk.com/consensus-magazine/2023/05/09/coindesk-turns-10-how-the-dao-hack-changed-ethereum-and-crypto)
[^imp-4-18]: [Hard Fork Completed | Ethereum Foundation Blog](https://blog.ethereum.org/2016/07/20/hard-fork-completed)
