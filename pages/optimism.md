---
title: Optimism
ticker: OP
category: Layer 2
status: draft
updated: 2026-10-30
---

# Optimism

**Optimism** is a layer 2 project that runs OP Mainnet, an optimistic
rollup on [Ethereum](ethereum.md), and develops the OP Stack, open-source
software that other teams use to launch their own rollups. Transactions on
OP Mainnet are executed off Ethereum and posted back to it, and are assumed
valid unless challenged with a fault proof. The software is built mainly by
OP Labs, and the network is governed by the Optimism Collective through the
**OP** token.[^op-stack-intro][^fp-explainer][^collective]

| | |
|---|---|
| Type | Optimistic rollup on Ethereum (OP Mainnet); rollup software framework (OP Stack) |
| Developer | OP Labs PBC (formerly Optimism PBC); Optimism Foundation |
| Founding team | Jinglan (Jing) Wang, Karl Floersch, Ben Jones, Kevin Ho, Mark Tyneway, Kelvin Fichter[^coindesk-wang] |
| Mainnet | 2021-01-15 (limited); open to all deployers 2021-12-16 |
| Chain ID | 10[^connect] |
| Gas token | ETH |
| Governance token | OP |
| Initial OP supply | 4,294,967,296 (2^32) |
| Governance | Optimism Collective (Token House and Citizens' House); Security Council |
| Proof system | Permissionless fault proofs (since 2024-06-10) |
| Withdrawal delay | About 7 days |
| Data availability | Ethereum (blobs since March 2024) |
| L2Beat stage | Stage 1 |
| Live data | [L2Beat](https://l2beat.com/scaling/projects/op-mainnet), [Optimistic Etherscan](https://optimistic.etherscan.io) |

## History

### Plasma Group and founding

Optimism grew out of Plasma Group, a non-profit research organisation
working on Ethereum scaling. CoinDesk reports that Jinglan Wang and Karl
Floersch, a former Ethereum Foundation researcher, set it up, and that the
group moved from Plasma designs to optimistic rollups as demand for cheap
transactions grew. It lists the founding team as Wang, Ben Jones, Floersch,
Mark Tyneway, Kelvin Fichter and Kevin Ho.[^coindesk-wang] Plasma Group
shut down on its first anniversary and donated its remaining funds to
Gitcoin. Its members founded Optimism, a public benefit corporation, in
December 2019, with Wang as chief executive.[^seed]

### Funding

In January 2020 the new company raised a US$3.5 million seed round from
Paradigm and IDEO CoLab Ventures.[^seed] Andreessen Horowitz (a16z) led a
US$25 million Series A, announced on 23 February 2021. a16z's post named
Jing, Karl and Ben as the core team and traced the work to "the team's
research at Plasma".[^a16z][^series-a] On 17 March 2022 Optimism announced
a US$150 million Series B co-led by Paradigm and a16z at a US$1.65 billion
valuation.[^series-b][^series-b-decrypt]

### Soft launch and the OVM

Optimism opened a limited mainnet, then called Optimistic Ethereum, on 15
January 2021, with Synthetix as its first application. The team said it
would hold upgrade keys for at least the first six months and warned users
to expect outages and bugs.[^soft-launch][^preliminary] Contract deployment
was restricted to an allowlist of approved projects.[^paradigm-ovm]

The first design, the Optimistic Virtual Machine (OVM), was not a copy of
the EVM. Contracts were compiled with a modified Solidity compiler that
replaced some opcodes with calls to OVM equivalents and banned others, so
not all Ethereum contracts could run unchanged.[^paradigm-ovm]

### Regenesis and EVM equivalence

On 11 November 2021 Optimism carried out its final "regenesis", restarting
the chain from a new genesis state with an upgrade that made it EVM
equivalent. Transactions from before that date are not part of the current
chain.[^regenesis][^synthetix] The upgrade also removed the OVM's fraud
proof system; OP Mainnet would not have working fault proofs again until
June 2024.[^l2beat] On 16 December 2021 Optimism removed its allowlist,
letting anyone deploy contracts.[^whitelist]

### OP token and the Collective

On 26 April 2022 Optimism announced the Optimism Collective, a governance
structure with two co-equal houses. Optimism PBC was renamed OP Labs PBC,
and a new Optimism Foundation, led by Wang and Jones, was formed to steward
the Collective.[^collective] The OP token launched on 31 May 2022 with an
airdrop of about 214 million OP, 5% of the initial supply.[^token-live]
The initial allocation was:[^allocation]

| Recipient | Share |
|---|---|
| Ecosystem Fund | 25% |
| Retroactive Public Goods Funding | 20% |
| User airdrops | 19% |
| Core contributors | 19% |
| Investors | 17% |

Further airdrops followed, starting with 11.7 million OP to more than
300,000 addresses on 9 February 2023.[^airdrop-2] In 2026 the Foundation
proposed re-designating the remaining user airdrop allocation as a
"Strategic Ecosystem Fund".[^budget-y5]

### Retroactive Public Goods Funding

Retroactive Public Goods Funding (later Retro Funding) rewards projects
after they have shown impact; the Collective's founding pact rests on what
Optimism calls "the axiom of impact=profit".[^collective] The first round
allocated US$1 million. Later rounds allocated 10 million OP (round 2), 30 million OP
to 501 recipients (round 3, announced 11 January 2024), and between about
2 and 10 million OP each in rounds 4 to 7.[^retro-numbers][^retro-2][^retro-3]
In January 2026 the Foundation paused Retro Funding for at least a year;
by August 2026 about 81 million OP of the 859 million allocated had been
committed.[^season-9][^budget-y5]

### Bedrock and the OP Stack

On 17 October 2022 Optimism introduced the OP Stack, a modular framework for
building rollups, and described a future "Superchain" of interconnected
chains sharing it. Bedrock, a rewrite of the OP Mainnet codebase, was to be
its first release; Optimism says it is about a hundredth the size of the
original OVM code.[^op-stack-intro] OP Mainnet migrated to Bedrock on 6
June 2023, with several hours of planned downtime. The Foundation stated the
upgrade would lower fees and make the bridge more secure.[^bedrock][^upgrades]

Later network upgrades included Ecotone (14 March 2024), which moved data
posting to Ethereum blobs; Granite (11 September 2024); Holocene (9 January
2025); Isthmus (9 May 2025); Jovian (2 December 2025); and Karst (8 July
2026).[^upgrades]

### Base and the Superchain

Coinbase built its Base network on the OP Stack and launched it in August
2023. Base agreed to send the Collective the greater of 2.5% of its
sequencer revenue or 15% of its net sequencer revenue, and could earn up to
about 118 million OP over six years, with its voting power capped at 9% of
votable supply.[^welcoming-base] The "Law of Chains", published in July
2023, set out principles for chains that opt into Superchain
governance.[^law-of-chains]

Other chains that joined the Superchain include Unichain, World Chain,
Soneium and Ink.[^dlnews-base] Ronin announced a migration to an OP Stack
layer 2 in 2025, and OKX moved its X Layer network from Polygon CDK to the
OP Stack.[^ronin][^xlayer] Optimism states that 54 mainnet chains were
built on the OP Stack as of October 2026.[^ecosystem-2026]

### Fault proofs and decentralisation

Permissionless fault proofs went live on OP Mainnet on 10 June 2024,
allowing anyone to propose and challenge state claims used to prove
withdrawals. L2Beat then classed OP Mainnet as Stage 1.[^fault-proofs][^l2beat]
In August 2024 fault proofs were disabled as a precaution after a bug was
found, and withdrawals fell back to permissioned proposals; they were
re-enabled with the Granite upgrade.[^l2beat]

The Security Council began signing OP Mainnet upgrades on 9 February 2024,
initially in a 2-of-2 multisig with the Optimism Foundation.[^security-council]
Optimism stated in September 2026 that the council has 13 voting members
and a 75% signing threshold.[^facts-2026]

### Base's departure and restructuring (2025–2026)

In November 2025 Wang wrote that the team "did too much and focused too
little", and said the project had cut staff, unified execution under one
entity and would focus on the OP Stack and enterprise
customers.[^new-era] On 29 January 2026 Optimism launched OP Enterprise,
a set of infrastructure and support tiers, including fully managed
hosting by OP Labs, for companies running OP Stack chains.[^op-enterprise]

On 8 January 2026 the Foundation proposed spending 50% of incoming
Superchain revenue on monthly OP purchases for a year, with the tokens
returned to the treasury.[^buyback-proposal] Token holders approved it on
28 January 2026 with about 84% support; purchases began in February
through over-the-counter swaps.[^buyback-vote] The Foundation reported
buying more than 9 million OP by August 2026.[^budget-y5]

On 18 February 2026 Base announced it would move from the OP Stack to its
own codebase, base/base, and said it planned to replace Optimism's proof
system with its own.[^decrypt-base]
The Foundation confirmed that Base's revenue share would not continue and
that Base would not receive the unvested part of its OP grant; Base remained
a customer of OP Enterprise.[^forum-base][^dlnews-base] DL News reported
that Base had contributed 8,387 ETH, 41% of the Collective's lifetime
revenue, and 90% of its revenue in January 2026.[^dlnews-base] On 12
March 2026 OP Labs laid off 20 employees, about a fifth of its staff; Wang
said the cut was "not about finances".[^layoffs]

### Interoperability

Optimism's plan for the Superchain includes native message passing between
OP Stack chains. Interop ships in the Lagoon network upgrade. As of October
2026, OP Labs documentation targets a first two-chain interop set of OP
Mainnet and Unichain in December 2026, subject to governance
approval.[^lagoon][^interop-prep]

## Technology

A single sequencer orders OP Mainnet transactions and posts them to
Ethereum, using blobs since March 2024. The operator can be changed through
a contract controlled by the Foundation. Users can force transactions
through Ethereum if the sequencer censors them, with a delay of up to 12
hours.[^l2beat]

Since Bedrock, the OP Stack separates a consensus-layer client (op-node)
from an execution client (such as op-reth), following the split Ethereum
adopted for The Merge.[^op-stack-intro][^interop-prep]

Withdrawals to Ethereum must be proven against a state proposal submitted
through the DisputeGameFactory contract. Anyone can submit or challenge a
proposal. Disputes are resolved by an interactive bisection game that ends
in a one-step proof of a single MIPS instruction on Ethereum; Cannon is the
fault proof virtual machine used for this. The system is designed to support further proof
systems, including zero-knowledge proofs.[^fp-explainer][^fault-proofs]
L2Beat lists a challenge period of 3.5 days followed by a 3.5-day execution
delay.[^l2beat]

L2Beat classes OP Mainnet as Stage 1, not Stage 2, because the Security
Council can act outside provable bugs and because upgrades give users less
than 30 days to exit. Emergency upgrades can be executed immediately.[^l2beat]

## Governance

The Token House votes with OP, directly or by delegation, on protocol
upgrades, treasury grants and other proposals. Most votes need a quorum of
30% of votable OP supply.[^gov-faq] The Citizens' House is a one-person,
one-vote body whose members hold non-transferable badges; its first version
launched in December 2022 to vote on Retro Funding.[^collective][^retro-2]
The upgrade process in Optimism's documentation includes a veto period in
which the Citizens' House can block upgrades approved by the Token
House.[^upgrades]

The Optimism Foundation is a Cayman Islands foundation company governed by
a board of directors and a supervisor. Governance can vote to remove
directors and block changes to its documents that reduce token holders'
rights.[^gov-faq] In 2026 the Foundation said it intended to turn the
Collective "from experiment to organization", including a possible new
legal entity such as a DUNA.[^season-9]

## Incidents and controversies

- **Wintermute loss (June 2022).** The Foundation sent 20 million OP to an
  address supplied by the market maker Wintermute, which was the address of
  a Wintermute multisig on Ethereum that had not been deployed on Optimism.
  Wintermute took responsibility. An unknown attacker gained control of
  the address on Optimism and took the tokens, then sold 1 million and sent
  1 million to Vitalik Buterin's address. Wintermute bought back the tokens sold.
  On 10 June 2022 the attacker returned 17 million OP.[^wintermute-decrypt][^wintermute-return]
- **Airdrop launch (May 2022).** Some users claimed OP early by calling the
  contract while the team was still testing, and some users reported
  being shown as ineligible after earlier being eligible.[^coindesk-airdrop]
- **ETH duplication bug (2022).** On 2 February 2022 the researcher Jay
  Freeman (saurik) reported a bug in which `SELFDESTRUCT` could duplicate
  ETH. He found no evidence of malicious use. Optimism paid a bounty of
  US$2,000,042, and forks of its code were also patched.[^saurik]
- **Fault proof suspension (August 2024).** Fault proofs were disabled for
  several weeks after a bug was found, as described [above](#fault-proofs-and-decentralisation).[^l2beat]
- **Lost early data.** OP Labs states that data directories holding event
  logs and transaction status for January to July 2021 were deleted in
  error in August 2023. Balances were unaffected.[^lost-data]
- **Fraud proofs removed (2021–2024).** From the November 2021 regenesis to
  June 2024, OP Mainnet ran without working fault proofs.[^l2beat]
- **Token grants.** CoinDesk reported criticism from competitors that
  Optimism did not disclose how much OP was set aside for chains joining
  the Superchain.[^coindesk-wang]
- **Base revenue and OP Enterprise.** After Base's departure, the delegate
  GFXlabs argued that Base was now paying OP Labs while token holders
  received nothing. The Foundation said OP Enterprise revenue goes to the
  Foundation and that it was exploring using it for buybacks.[^forum-base]

## Timeline

| Date | Event |
|---|---|
| 2019-12 | Optimism founded by former Plasma Group members |
| 2020-01 | US$3.5M seed round from Paradigm and IDEO CoLab Ventures |
| 2021-01-15 | Limited mainnet launch with Synthetix |
| 2021-02-23 | US$25M Series A led by a16z |
| 2021-11-11 | Final regenesis; EVM equivalence |
| 2021-12-16 | Deployment allowlist removed |
| 2022-02-02 | ETH duplication bug reported |
| 2022-03-17 | US$150M Series B |
| 2022-04-26 | Optimism Collective announced; Optimism PBC renamed OP Labs |
| 2022-05-31 | OP token and first airdrop |
| 2022-06-10 | Attacker returns 17M of 20M OP from Wintermute address |
| 2022-10-17 | OP Stack introduced |
| 2022-12-06 | Citizens' House v0.1 announced |
| 2023-06-06 | Bedrock upgrade |
| 2023-07-25 | Law of Chains published |
| 2023-08 | Base launches on the OP Stack |
| 2024-01-11 | Retro Funding round 3 results: 30M OP |
| 2024-02-09 | Security Council begins signing upgrades |
| 2024-03-14 | Ecotone upgrade: blob data |
| 2024-06-10 | Permissionless fault proofs; Stage 1 |
| 2024-08 | Fault proofs temporarily disabled |
| 2024-09-11 | Granite upgrade |
| 2026-01-28 | OP buyback programme approved |
| 2026-01-29 | OP Enterprise launched |
| 2026-02-18 | Base announces move off the OP Stack |
| 2026-03-12 | OP Labs lays off about 20 staff |
| 2026-07-08 | Karst upgrade |

## See also

- [Ethereum](ethereum.md)
- [Arbitrum](arbitrum.md), a competing optimistic rollup
- [Base](base.md), built on the OP Stack until 2026
- [Uniswap](uniswap.md), whose Unichain is built on the OP Stack

## References

[^op-stack-intro]: Optimism (2022). *Introducing the OP Stack*. <https://optimism.io/blog/introducing-the-op-stack>
[^fp-explainer]: Optimism documentation. *Fault proofs explainer*. <https://docs.optimism.io/op-stack/fault-proofs/explainer>
[^collective]: Optimism (2022). *Introducing the Optimism Collective*. <https://optimism.io/blog/introducing-the-optimism-collective>
[^coindesk-wang]: CoinDesk (2024). *Optimism's Jing Wang and the widely adopted OP Stack*. <https://www.coindesk.com/tech/2024/12/10/optimism-s-jing-wang-and-the-widely-adopted-op-stack>
[^connect]: Optimism documentation. *Connecting to OP Mainnet*. <https://docs.optimism.io/op-mainnet/network-information/connecting-to-op>
[^seed]: The Block (2020). *Plasma Group researchers raise $3.5M from Paradigm and IDEO to start new company*. <https://www.theblock.co/post/53017>
[^a16z]: Dixon, C. and Simpson, A. (2021). *Investing in Optimism*. a16z crypto. <https://a16zfrontier.com/posts/announcement/investing-in-optimism/>
[^series-a]: The Block (2021). *Ethereum scaling startup Optimism raises $25 million Series A led by a16z*. <https://www.theblock.co/linked/96004/ethereum-optimism-scaling-a16z-funding>
[^series-b]: Gunderson Dettmer (2022). *Optimism raises $150M Series B financing*. <https://www.gunder.com/en/news-insights/client-news/optimism-raises-150m-series-b-financing>
[^series-b-decrypt]: Decrypt (2022). *Ethereum startup Optimism hits $1.6 billion valuation after raising $150M*. <https://decrypt.co/95371/ethereum-startup-optimism-1-6-billion-valuation>
[^soft-launch]: The Block (2021). *Optimism's Ethereum-based scaling solution has soft launched on mainnet*. <https://www.theblock.co/post/91524/optimisms-ethereum-based-scaling-solution-has-soft-launched-on-mainnet>
[^preliminary]: The Block (2021). *Ethereum's layer 2 scaling solution Optimism plans to release its preliminary mainnet on January 15*. <https://www.theblock.co/linked/89907/>
[^paradigm-ovm]: Konstantopoulos, G. and Hasu (2021). *How does Optimism's rollup really work?* Paradigm. <https://paradigm.xyz/2021/01/how-does-optimism-s-rollup-really-work>
[^regenesis]: Optimism documentation. *Accessing pre-regenesis history*. <https://docs.optimism.io/op-mainnet/pre-bedrock-history/regenesis-history>
[^synthetix]: Synthetix (2021). *SNXweave weekly recap 14*. <https://blog.synthetix.io/snxweave-weekly-recap-14/>
[^l2beat]: L2Beat. *OP Mainnet*. <https://l2beat.com/scaling/projects/op-mainnet>
[^whitelist]: ForkLog (2021). *Optimism opens access to its Ethereum L2 solution for all developers*. <https://forklog.com/en/optimism-opens-access-to-its-ethereum-l2-solution-for-all-developers/>
[^token-live]: The Block (2022). *Optimism's governance token officially goes live*. <https://www.theblock.co/post/149464/optimisms-governance-token-officially-goes-live>
[^allocation]: Optimism Foundation (2023). *Treasury appropriation proposal: Foundation Year 2 budget*. Optimism governance forum. <https://gov.optimism.io/t/treasury-appropriation-proposal-foundation-year-2-budget/5979>
[^airdrop-2]: Optimism (2023). *OP Drop #2*. <https://optimism.io/blog/op-drop-2>
[^budget-y5]: Optimism Foundation (2026). *Collective Year 4 budget update and Year 5 budget outlook*. Optimism governance forum. <https://gov.optimism.io/t/collective-year-4-budget-update-and-year-5-budget-outlook/10796>
[^retro-numbers]: Optimism governance forum (2025). *RetroPGF/RF evolution & numbers*. <https://gov.optimism.io/t/retropgf-rf-evolution-numbers/10128>
[^retro-2]: Optimism (2022). *Introducing the Citizens' House: 10M OP to public goods*. <https://optimism.io/blog/introducing-the-citizens-house-10m-op-to-public-goods>
[^retro-3]: Optimism (2024). *Announcing RetroPGF round 3 recipients*. <https://optimism.io/blog/announcing-retropgf-round-3-recipients>
[^season-9]: Optimism (2026). *Season 9: from experiment to organization*. <https://optimism.io/blog/season-9-from-experiment-to-organization>
[^bedrock]: The Block (2023). *Optimism plans mainnet Bedrock upgrade for June 6*. <https://www.theblock.co/post/230898/optimism-mainnet-bedrock-upgrade>
[^upgrades]: Optimism documentation. *Network upgrades*. <https://docs.optimism.io/op-stack/protocol/network-upgrades>
[^welcoming-base]: Optimism (2023). *Welcoming Base*. <https://optimism.io/blog/welcoming-base>
[^law-of-chains]: Optimism (2023). *Introducing the Law of Chains*. <https://optimism.io/blog/introducing-the-law-of-chains>
[^dlnews-base]: DL News (2026). *Optimism token price plunges as Base leaves Superchain*. <https://www.dlnews.com/articles/defi/optimism-token-price-plunges-as-base-leaves-superchain/>
[^ronin]: Optimism (2025). *Ronin is coming home to Ethereum with Optimism's OP Stack*. <https://optimism.io/blog/ronin-is-coming-home-to-ethereum-with-optimism-s-op-stack>
[^xlayer]: Optimism (2025). *OKX migrates XLayer to the OP Stack*. <https://optimism.io/blog/okx-migrates-xlayer-to-the-op-stack>
[^ecosystem-2026]: Optimism (2026). *OP Stack ecosystem overview: chains, apps, and stats (2026)*. <https://optimism.io/blog/op-stack-ecosystem-overview-2026>
[^fault-proofs]: Optimism (2024). *Permissionless fault proofs and Stage 1 arrive to the OP Stack*. <https://optimism.io/blog/permissionless-fault-proofs-and-stage-1-arrive-to-the-op-stack>
[^security-council]: Optimism (2024). *Introducing the Optimism Collective's Security Council*. <https://optimism.io/blog/introducing-the-optimism-collective-s-security-council>
[^facts-2026]: Optimism (2026). *Optimism: governance, sequencer & enterprise facts (2026)*. <https://optimism.io/blog/optimism-governance-sequencer-enterprise-facts>
[^new-era]: The Block (2025). *Optimism co-founder outlines new era amid brutal token price decline*. <https://www.theblock.co/post/380702/optimism-co-founder-outlines-new-era-amid-brutal-token-price-decline>
[^op-enterprise]: Optimism (2026). *Introducing OP Enterprise*. <https://optimism.io/blog/introducing-op-enterprise>
[^buyback-proposal]: Optimism (2026). *OP token buybacks*. <https://optimism.io/blog/op-token-buybacks>
[^buyback-vote]: The Block (2026). *OP token holders approve buyback plan redirecting 50% of Optimism protocol revenue to OTC swaps*. <https://www.theblock.co/post/387660/op-token-holders-approve-buyback-plan-50-optimism-protocol-revenue-otc-swaps>
[^decrypt-base]: Decrypt (2026). *Morning Minute: Base breaks up with Optimism*. <https://decrypt.co/358722/morning-minute-base-breaks-up-with-optimism>
[^forum-base]: Optimism governance forum (2026). *Base, the Superchain, and governance: questions that merit answers*. <https://gov.optimism.io/t/base-the-superchain-and-governance-questions-that-merit-answers/10612>
[^layoffs]: The Block (2026). *Optimism's OP Labs cuts 20% of staff to 'do fewer things well'*. <https://www.theblock.co/news/ecosystems/2026-03-12-optimism-op-labs-layoff-393339>
[^lagoon]: Optimism documentation. *Lagoon*. <https://docs.optimism.io/op-stack/protocol/hardforks/lagoon>
[^interop-prep]: Optimism documentation. *Prepare for interop on OP Mainnet and Unichain*. <https://docs.optimism.io/notices/interop-prep>
[^gov-faq]: Optimism documentation. *FAQs* (governance). <https://docs.optimism.io/governance/gov-faq>
[^wintermute-decrypt]: Decrypt (2022). *Ethereum layer-2 solution Optimism loses 20 million tokens in interlayer snafu*. <https://decrypt.co/102377/ethereum-layer-2-solution-optimism-loses-20-million-tokens-in-interlayer-snafu>
[^wintermute-return]: The Block (2022). *Hacker returns 17 million OP tokens*. <https://www.theblock.co/post/151344/hacker-returns-17-million-op-tokens>
[^coindesk-airdrop]: CoinDesk (2022). *Optimism tokens claimed by some users ahead of official airdrop announcement*. <https://www.coindesk.com/markets/2022/05/31/optimism-tokens-claimed-by-users-ahead-of-official-airdrop-announcement/>
[^saurik]: Freeman, J. (2022). *Attacking an Ethereum L2 with unbridled Optimism*. <https://www.saurik.com/optimism.html>
[^lost-data]: Optimism documentation. *Lost pre-regenesis data*. <https://docs.optimism.io/op-mainnet/pre-bedrock-history/lost-pre-regenesis-data>
