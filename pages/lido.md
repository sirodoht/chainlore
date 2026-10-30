---
title: Lido
ticker: LDO
category: DeFi
status: ai-fact-checked
checked: 2026-10-30
checked_by: Opus 5.5 High
updated: 2026-10-30
---

# Lido

**Lido** is a liquid staking protocol for [Ethereum](ethereum.md). Users
deposit ETH and receive stETH, a token that represents their staked ETH
and the rewards it earns, and that can be traded or used in other
applications while the ETH stays staked. Lido allocates deposits to
validators run by node operators, charges a 10% fee on staking rewards,
and is governed by the Lido DAO through the **LDO** token. Lido has also
offered staking on other networks, all of which it has since wound
down.[^intro][^block-2020]

| | |
|---|---|
| Type | Liquid staking protocol |
| Founders | Konstantin Lomashuk, Vasiliy Shapovalov |
| Launch | December 2020 (Ethereum) |
| Staking tokens | stETH (rebasing), wstETH (non-rebasing wrapper) |
| Protocol fee | 10% of staking rewards |
| Governance token | LDO |
| LDO supply | 1,000,000,000 (fixed at launch) |
| Governance | Lido DAO (Aragon), with dual governance since 2025 |
| stETH contract | `0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84` |
| LDO contract | `0x5a98fcbea516cf06857215779fd812ca3bef1b32`[^contracts] |
| Former networks | Terra, Kusama, Polkadot, Solana, Polygon |
| Live data | [Lido](https://lido.fi/ethereum), [DefiLlama](https://defillama.com/protocol/lido) |

## History

### Founding and launch

Lido was founded by Konstantin Lomashuk and Vasiliy Shapovalov, who had
earlier created the staking provider P2P Validator (p2p.org).[^forklog-paradigm][^coindesk-lomashuk]
Lomashuk also runs the venture firm cyber.Fund with another Lido
co-founder.[^coindesk-lomashuk]

Lido was built for the period when ETH staked on the Beacon Chain could
not be withdrawn, giving stakers a transferable token representing their
locked ETH.[^block-2020][^forklog-what]
A testnet ran on Goerli from late November 2020, and in December 2020
Lido raised US$2 million from Semantic Ventures, ParaFi Capital, Terra,
KR1, Stakefish, Staking Facilities and others, with angel investments
from Rune Christensen, Stani Kulechov and Kain Warwick.[^block-2020] The
staking service opened on 19 December 2020, and the stETH contract was
deployed that month.[^forklog-what][^etherscan]

The LDO governance token went live on 5 January 2021 (see
[Token](#token)).[^ldo] In April 2021 LDO holders approved selling 100
million LDO from the treasury, 10% of supply, to the investment firm
Paradigm and partners for 21,600 ETH; Paradigm paid 15,120 ETH for its
70 million in May.[^paradigm-proposal][^paradigm-snapshot][^forklog-paradigm][^forklog-paradigm-paid]
In March 2022 Andreessen Horowitz announced a US$70 million investment,
paid partly by buying LDO from existing holders.[^techcrunch]

### Other networks

By March 2022 Lido offered liquid staking on
Solana, Kusama and [Terra](terra.md), and planned to launch on Polygon
that month; by June 2022 it also supported Polkadot.[^techcrunch][^forklog-what]
Lido on Terra ended in May 2022 after Terra's collapse.[^forklog-what]

The other deployments were later sunset:

- **Polkadot and Kusama.** In March 2023 MixBytes, which developed both
  deployments, said it would stop supporting them, citing low adoption
  and "unmet financial expectations". New deposits stopped on 15 March
  2023 and the Polkadot deployment ended on 1 August 2023.[^dot-ksm]
- **Solana.** P2P Validator, which had developed Lido on Solana since
  March 2022, asked the DAO either to fund continued development or to
  close it. LDO holders voted to close it, and staking stopped on 16
  October 2023. Front-end support for unstaking ended in February
  2024.[^solana]
- **Polygon.** Shard Labs proposed in November 2024 to sunset Lido on
  Polygon, citing low adoption and weak economics. A Snapshot vote ending
  on 28 November 2024 approved the sunset, with 58 million LDO in favour.
  New staking stopped on 16 December 2024, and front-end support ended
  on 16 June 2025.[^polygon][^polygon-sunset]

### Withdrawals and Lido v2

Until Ethereum's Shapella upgrade activated on 12 April 2023, staked ETH
could not be withdrawn, and stETH holders who wanted ETH had to sell on
the market.[^shapella][^coinshares] Lido announced v2 in February 2023. It added
withdrawals, letting holders redeem stETH for ETH at a 1:1 ratio through
a request-and-claim queue. It also added a Staking Router that lets the
protocol use several "modules", each with its own operator set and
rules.[^v2-intro] LDO holders approved the upgrade in an Aragon vote
that concluded on 15 May 2023, and withdrawal requests opened that day.[^block-v2]

### New operator modules

Under the Staking Router, the DAO added modules meant to widen the
operator set beyond the curated list:

- **Simple DVT** went live on mainnet on 16 April 2024 after an Aragon
  vote in February. It uses distributed validator technology from Obol
  and SSV Network, in which several operators jointly run one validator,
  similar to a multisig. Lido said the module would bring in solo and
  community stakers alongside professional operators.[^simple-dvt]
- **The Community Staking Module (CSM)** launched on mainnet on 25
  October 2024 as Lido's first permissionless module. Anyone can run
  validators by posting an ETH bond, set at 2.4 ETH for a first validator
  once the module left its early-adoption phase in January 2025. Lido
  reported that more than 330 operators had joined by then.[^csm]

In July 2026 an on-chain vote approved a "Lido Core" upgrade that
introduced Curated Module v2, Staking Router v3 and CSM v3.[^h1-2026]
After a Snapshot vote, Simple DVT's 72 regular clusters were wound down
and their operators offered a route into CSM.[^core-upgrade] In October 2026
a second CSM instance for high-balance (0x02) validators went
live.[^csm-0x02]

### Lido Alliance and Lido v3

In a Snapshot vote closing on 23 May 2024, LDO holders approved the Lido
Alliance, a framework proposed by Steakhouse Financial under which the
DAO endorses and supports Ethereum-aligned protocols that share its
focus on security.[^alliance] By April 2025 the alliance had
onboarded three members: Mellow, Drop and Bolt.[^alliance-q1]

Lido v3 was announced in February 2025 and launched on mainnet on 30
January 2026, after testnets and a soft launch.[^block-v3][^v3] It added
stVaults: separate vaults in which an owner chooses node operators, fees
and other settings, and can mint stETH against the staked ETH.
Launch partners included node operators P2P.org and Chorus One, and the
layer 2 network Linea, which used a vault to stake bridged
ETH.[^block-v3][^v3]

### Recent developments

In August 2025 Lido cut about 15% of contributor roles across Lido Labs,
Lido Ecosystem and the Lido Alliance. Shapovalov said the decision "was
about costs — not performance".[^block-layoff] He also said that "Lido
failed to ride the wave of restaking", and set out a plan to win
institutional stakers.[^dlnews-share]

In December 2025 LDO holders voted on GOOSE-3, a strategy for 2026 that
included expanding Lido Earn, a set of yield vaults, and new revenue
sources beyond staking. Some forum members questioned that
direction.[^goose3] Lido reported that its 2025 revenue fell 23% from
2024, which it attributed to net staking outflows, lower staking yields
and competition.[^block-revenue]

From November 2025 the DAO debated using treasury funds to buy back
LDO, and a second proposal followed in March 2026 after the token reached
an all-time low.[^dlnews-buyback] The DAO approved a one-off LDO
Accumulation Program on 13 April 2026 and adopted an automated
mechanism, NEST, which converts part of any staking revenue above an
annualised baseline of US$40 million into LDO.[^nest] Lido's H1 2026 report said NEST
buybacks were not expected soon at current ETH prices.[^h1-2026]

### Regulation

On 5 August 2025 the US Securities and Exchange Commission's Division of
Corporation Finance issued a staff statement saying that, in its view,
liquid staking as it described it, including the issue and redemption of
staking receipt tokens, does not involve the offer or sale of
securities. The statement has no legal force, depends on the facts it
assumes, and does not cover providers that decide how much to stake,
guarantee rewards, or offer extra yield.[^sec]

On 16 October 2025 VanEck filed to register a VanEck Lido Staked Ethereum
ETF that would have held stETH.[^vaneck-s1] It withdrew the filing on 14 October
2026, saying it did not intend to proceed; no shares were ever
sold.[^vaneck] A WisdomTree exchange-traded product in Europe that stakes
through Lido launched in December 2025.[^block-revenue][^h1-2026]

## Technology

### stETH and wstETH

When a user deposits ETH, Lido mints stETH one-for-one. stETH is a
rebasing token: each day an oracle reports validator balances, and every
holder's stETH balance changes to reflect rewards or penalties, without
any transfer. Internally, each holder owns a fixed number of "shares" of
the pool, and the stETH value of a share changes with each report. If
validators are slashed, balances can fall.[^tokens-guide]

Because some applications cannot handle balances that change on their
own, Lido also issues wstETH, a wrapper whose balance stays fixed while
the amount of stETH each token represents increases.[^tokens-guide]

Since v2, holders can exit through Lido itself by requesting a
withdrawal. The protocol fills the request from incoming deposits or by
asking operators to exit validators, then burns the stETH. Lido normally
runs in "turbo" mode; a "bunker" mode slows withdrawals in severe
conditions so that early leavers do not gain at
the expense of those who stay.[^v2-intro][^block-v2]

### Node operators

Lido does not run validators itself. The DAO's 10% fee on staking
rewards is split between node operators and the DAO treasury.[^intro]
The original curated operator set was chosen in onboarding rounds: a
sub-governance group of operators reviewed applications and recommended
candidates, and the DAO made the final decision.[^lnosg] Under Curated
Module v2, a Curated Module Committee assigns approved operators to
groups that determine how much stake each receives, while the CSM
modules remain open to anyone who posts a bond.[^staking-modules]

## Governance

The Lido DAO is an Aragon organisation in which voting power is
proportional to LDO holdings. Proposals are discussed on the Lido
research forum, often polled on Snapshot, and enacted by on-chain Aragon
votes. Routine, uncontentious actions go through Easy Track, a lighter
process meant to reduce voter fatigue and gas costs.[^lido-dao][^alliance]

### Token

LDO is an ERC-20 token with a fixed supply of 1 billion, all minted at
launch. The announced allocation was:[^ldo]

| Recipient | Share |
|---|---|
| DAO treasury | 36.32% |
| Investors | 22.18% |
| Initial Lido developers | 20% |
| Founders and future employees | 15% |
| Validators and signature holders | 6.5% |

Allocations to insiders were locked for one year and then vested over a
second year. A 0.4% airdrop went to early stakers.[^ldo] LDO gives
voting rights but no claim on fees; a DAO forum member described it in
2026 as "merely votes, not dividend-paying shares".[^dlnews-buyback]

### Dual governance

Dual governance was proposed on the Lido forum in June 2022. The author
argued that LDO holders' interests differ from those of stakers, and that
a captured DAO could use upgrades to steal funds or control the validator
set.[^dg-proposal] Under the version deployed in 2025, approved
decisions wait in a timelock. stETH holders can oppose them by locking
stETH, wstETH or withdrawal requests in an escrow. If the locked amount
reaches 1% of Lido's staked ETH, execution is delayed, by between 5 and
45 days depending on the level of opposition. At 10%, a "rage quit"
blocks execution until objecting holders have withdrawn. A Tiebreaker
Committee of outside members can break a prolonged deadlock.[^dg-101]
The on-chain vote enabling the system passed with 53.6 million LDO in
favour, just above the 50 million quorum, and concluded on 30 June
2025.[^block-dg]

## Incidents and controversies

- **stETH discount (June 2022).** Before withdrawals were possible, the
  only way to turn stETH into ETH quickly was to sell it, mostly through
  a Curve pool. After the lender Celsius paused withdrawals in June 2022,
  the pool became about 80% stETH and 20% ETH.[^kaiko] Wallets linked to
  the hedge fund Three Arrows Capital sold more than 56,000 stETH, and
  on 14 June stETH traded at almost a 7% discount to ETH.[^block-3ac]
  Analysts at CoinShares said that without withdrawals there was no
  arbitrage to hold the price near ETH.[^coinshares] Lido described the
  price as an "exchange rate" rather than a peg and said every stETH was
  backed by ETH. Jacob Blish, its head of business development, said the
  team had not expected the leverage built up after stETH was added to
  [Aave](aave.md).[^fortune-steth]
- **Share of staked ETH (2022 onward).** Ethereum Foundation researcher
  Danny Ryan argued in 2022 that a single liquid staking protocol above
  thresholds such as one third, one half or two thirds of stake could
  extract outsized profits or censor transactions. He recommended that
  "Lido and similar LSD products self-limit", and that capital
  allocators avoid protocols holding more than 25% of staked
  ETH.[^ryan] When Shapovalov opened a forum discussion in May 2022, Lido
  held slightly over 30% of stake. Supporters of a cap cited the risk of
  governance capture; opponents argued that capped stake would flow to
  centralised exchanges, which Lido had been founded to
  counter.[^self-limit-forum] A Snapshot vote ending on 1 July 2022
  rejected self-limiting by about 80.5 million LDO to
  156,000.[^self-limit-snapshot]
  Lido's development in the following years focused on dual governance
  and community staking, which Shapovalov said in 2025 improved Lido's
  image but did little for growth.[^dlnews-share] Its share was about
  28% in January 2025, 23.9% on 1 January 2026 and 21.2% on 30 June
  2026.[^coindesk-lomashuk][^h1-2026]
- **Kelp DAO exploit (April 2026).** After an exploit of Kelp DAO's
  rsETH token, deposits in Lido's EarnETH vault fell sharply. Lido said
  first-loss cover fully compensated depositors and no user funds were
  lost. The DAO also joined an industry effort, DeFi United, committing
  up to 2,500 stETH towards the rsETH shortfall.[^h1-2026]

## Timeline

| Date | Event |
|---|---|
| 2020-12-15 | US$2M funding round reported |
| 2020-12-19 | Staking service opens on Ethereum |
| 2021-01-05 | LDO token goes live |
| 2021-04-06 | Sale of 100M LDO to Paradigm and partners approved |
| 2022-03-03 | Andreessen Horowitz investment announced |
| 2022-05 | Terra deployment ends after Terra's collapse |
| 2022-05-21 | Forum discussion on limiting Lido's share opens |
| 2022-06 | stETH discount during Celsius and Three Arrows crises |
| 2022-06-10 | Dual governance first proposed |
| 2022-07-01 | Snapshot vote rejects self-limiting |
| 2023-04-12 | Shapella upgrade enables Ethereum withdrawals |
| 2023-05-15 | Lido v2: withdrawals and Staking Router |
| 2023-08-01 | Lido on Polkadot ends |
| 2023-10-16 | Lido on Solana stops accepting stake |
| 2024-04-16 | Simple DVT module live |
| 2024-05-23 | Lido Alliance approved |
| 2024-10-25 | Community Staking Module live |
| 2024-11-28 | Vote to sunset Lido on Polygon |
| 2025-01 | CSM becomes fully permissionless |
| 2025-06-16 | Front-end support for Lido on Polygon ends |
| 2025-06-30 | Dual governance vote concludes |
| 2025-08 | Lido announces 15% staff reduction |
| 2025-08-05 | SEC staff statement on liquid staking |
| 2025-10-16 | VanEck files for Lido staked ETH ETF |
| 2025-12 | GOOSE-3 strategy vote |
| 2026-01-30 | Lido v3 and stVaults live on mainnet |
| 2026-04-13 | LDO Accumulation Program approved |
| 2026-04 | Kelp DAO exploit; Lido joins DeFi United |
| 2026-07 | Lido Core upgrade: Curated Module v2, CSM v3 |
| 2026-10-14 | VanEck withdraws ETF filing |
| 2026-10 | 0x02 CSM module live |

## See also

- [Ethereum](ethereum.md)
- [Aave](aave.md), where stETH is used as collateral
- [Terra](terra.md), an early Lido deployment
- [Solana](solana.md), an early Lido deployment

## References

[^intro]: Lido documentation. *Lido documentation home*. <https://docs.lido.fi/>
[^block-2020]: The Block (2020). *Eth2 staking protocol Lido raises $2 million in new funding*. <https://www.theblock.co/linked/87761/eth2-staking-protocol-lido-raises-2-million-funding>
[^forklog-paradigm]: ForkLog (2021). *Paradigm hedge fund and partners to buy 10% of Lido tokens*. <https://forklog.com/en/paradigm-hedge-fund-and-partners-to-buy-10-of-lido-tokens/>
[^coindesk-lomashuk]: CoinDesk (2025). *Lido co-founder teases "Second Foundation" for Ethereum amid community backlash*. <https://www.coindesk.com/tech/2025/01/22/lido-co-founder-teases-second-foundation-for-ethereum-amid-community-backlash>
[^block-layoff]: The Block (2025). *Lido lays off 15% of workforce for "long-term sustainability," cofounder says*. <https://www.theblock.co/post/365369/lido-lay-off>
[^dlnews-share]: DL News (2025). *Lido eyes "low-risk staking" to boost flagging market share*. <https://www.dlnews.com/articles/regulation/lido-eyes-low-risk-staking-to-boost-flagging-market-share/>
[^paradigm-proposal]: Lido research forum (2021). *Proposal: LDO treasury diversification*. <https://research.lido.fi/t/proposal-ldo-treasury-diversification/458>
[^paradigm-snapshot]: Lido DAO Snapshot (2021). *Proposal: LDO Treasury Diversification*. <https://snapshot.org/#/lido-snapshot.eth/proposal/QmTR46STEjdRwmCKJjDThXXekKJHbhuiUHaXqDJqry3KqK>
[^forklog-paradigm-paid]: ForkLog (2021). *Paradigm transfers 15,120 ETH to Lido DAO under token buyback agreement*. <https://forklog.com/en/news/paradigm-transfers-15120-eth-to-lido-dao-under-token-buyback-agreement>
[^forklog-what]: ForkLog (2022). *What is Lido?* <https://forklog.com/en/what-is-lido/>
[^etherscan]: Etherscan. *Lido: stETH Token*. <https://etherscan.io/address/0xae7ab96520de3a18e5e111b5eaab095312d7fe84>
[^contracts]: Lido documentation. *Deployed contracts*. <https://docs.lido.fi/deployed-contracts/>
[^ldo]: Lido (2021). *Introducing LDO: the Lido DAO governance token*. <https://blog.lido.fi/introducing-ldo/>
[^techcrunch]: TechCrunch (2022). *A16z backs decentralized liquid crypto staking platform Lido*. <https://techcrunch.com/2022/03/03/lido-raises-the-stakes-for-crypto-defi-investors-with-new-capital/>
[^dot-ksm]: Lido research forum (2023). *Sunsetting of Lido on Polkadot and Kusama*. <https://research.lido.fi/t/sunsetting-of-lido-on-polkadot-and-kusama/4067>
[^solana]: Lido (2023). *Lido on Solana sunset*. <https://blog.lido.fi/sunset-lido-on-solana/>
[^polygon]: Lido research forum (2024). *Reevaluation of Lido on Polygon state*. <https://research.lido.fi/t/reevaluation-of-lido-on-polygon-state/8848>
[^polygon-sunset]: Lido (2024). *Lido on Polygon sunset*. <https://blog.lido.fi/lido-on-polygon-sunset/>
[^shapella]: Ethereum Foundation (2023). *Shapella mainnet announcement*. <https://blog.ethereum.org/2023/03/28/shapella-mainnet-announcement>
[^v2-intro]: Lido (2023). *Introducing Lido V2: next step in decentralization*. <https://blog.lido.fi/introducing-lido-v2/>
[^block-v2]: The Block (2023). *Lido Finance passes vote to activate withdrawals on Ethereum with v2 upgrade*. <https://www.theblock.co/post/230811/lido-finance-ethereum-withdrawals-upgrade>
[^simple-dvt]: Lido (2024). *Simple DVT: a new phase for Lido on Ethereum*. <https://blog.lido.fi/simpledvt-new-phase-for-lido-on-ethereum/>
[^csm]: Lido (2025). *CSM goes fully permissionless*. <https://blog.lido.fi/csm-goes-fully-permissionless/>
[^core-upgrade]: Lido (2026). *A new Lido Core upgrade for protocol sustainability and a leaner Ethereum*. <https://blog.lido.fi/a-new-lido-core-upgrade-for-protocol-sustainability-and-a-leaner-ethereum/>
[^csm-0x02]: Lido (2026). *Introducing 0x02 CSM: a permissionless path to running higher-balance validators*. <https://blog.lido.fi/introducing-0x02-csm-a-permissionless-path-to-running-higher-balance-validators/>
[^h1-2026]: Lido DAO (2026). *GOOSE-2026 report, H1 2026*. <https://lido.fi/ldo-hub/reports/h1-2026>
[^alliance]: Lido research forum (2024). *Lido Alliance: an Ethereum-aligned ecosystem*. <https://research.lido.fi/t/lido-alliance-an-ethereum-aligned-ecosystem/7475>
[^alliance-q1]: Lido research forum (2025). *Q1 2025 Lido Alliance update*. <https://research.lido.fi/t/q1-2025-lido-alliance-update/9880>
[^block-v3]: The Block (2026). *Lido rolls out stVaults on mainnet with Day 1 users including Linea, Nansen and several institutional stakers*. <https://www.theblock.co/post/387769/lido-stvaults-mainnet>
[^v3]: Lido (2026). *Lido V3 is live: modular infrastructure for a new paradigm of Ethereum staking*. <https://blog.lido.fi/lido-v3-is-live-modular-infrastructure-for-a-new-paradigm-of-ethereum-staking/>
[^goose3]: Lido research forum (2025). *[Lido Labs] GOOSE-3: Lido's next chapter*. <https://research.lido.fi/t/lido-labs-goose-3-lido-s-next-chapter/10927>
[^block-revenue]: The Block (2026). *Lido revenue dropped 23% last year as users withdrew funds and yields declined*. <https://www.theblock.co/post/394947/lido-revenue-dropped-23-last-year-users-withdrew-funds-yields-declined>
[^dlnews-buyback]: DL News (2026). *Lido jumps from all-time low as DAO debates $20m buyback programme*. <https://www.dlnews.com/articles/defi/lido-jumps-from-all-time-low-as-dao-debates-buyback-programme/>
[^nest]: Lido (2026). *LDO automated buybacks: overview*. <https://blog.lido.fi/ldo-automated-buybacks-overview/>
[^sec]: US Securities and Exchange Commission, Division of Corporation Finance (2025). *Statement on certain liquid staking activities*. <https://www.sec.gov/newsroom/speeches-statements/corpfin-certain-liquid-staking-activities-080525>
[^vaneck]: VanEck Digital Assets (2026). *VanEck Lido Staked Ethereum ETF: Form RW (application for withdrawal)*. SEC EDGAR. <https://www.sec.gov/Archives/edgar/data/0002091159/000209115926000005/vanecklidostakedethereumet.htm>
[^vaneck-s1]: VanEck Lido Staked Ethereum ETF (2025). *Form S-1 registration statement*. SEC EDGAR. <https://www.sec.gov/Archives/edgar/data/2091159/000162828025045249/vanecklidostakedethereumet.htm>
[^tokens-guide]: Lido documentation. *Lido tokens integration guide*. <https://docs.lido.fi/guides/lido-tokens-integration-guide>
[^lnosg]: Lido research forum (2021). *Node Operator Sub Governance & new node operator application process*. <https://research.lido.fi/t/node-operator-sub-governance-new-node-operator-application-process/344>
[^staking-modules]: Lido documentation. *Staking modules*. <https://docs.lido.fi/staking-modules/>
[^lido-dao]: Lido documentation. *Lido DAO*. <https://docs.lido.fi/lido-dao>
[^dg-proposal]: Lido research forum (2022). *LDO+stETH dual governance*. <https://research.lido.fi/t/ldo-steth-dual-governance/2382>
[^dg-101]: Lido (2025). *Dual Governance 101: explainer*. <https://blog.lido.fi/dual-governance-101-explainer/>
[^block-dg]: The Block (2025). *Lido DAO votes to enable dual governance, giving stakers veto power*. <https://www.theblock.co/post/360212>
[^kaiko]: Kaiko Research (2022). *Celsius reaches boiling point*. <https://marketing.kaiko.com/celsius-reaches-boiling-point>
[^block-3ac]: The Block (2022). *Lido staked ether selloff continues as larger holder unloads 56,000 stETH*. <https://theblock.co/news/defi/2022-06-14-lido-staked-ether-selloff-continues-as-larger-holder-unloads-56000-steth-151894>
[^coinshares]: CoinShares (2022). *Is the decoupling of Lido's staked ETH another stablecoin collapse?* <https://coinshares.com/de/resources/research/is-the-decoupling-of-lidos-staked-eth-another-stablecoin-collapse>
[^fortune-steth]: Fortune (2022). *Ethereum staking, Lido Finance and the crypto hedge fund crisis* (by Ian Allison, CoinDesk). <https://fortune.com/crypto/2022/06/17/ethereum-staking-lido-finance-crypto-derivative-hedge-fund-three-arrows-celsius>
[^ryan]: Ryan, D. (2022). *The risks of LSD*. <https://notes.ethereum.org/@djrtwo/risks-of-lsd>
[^self-limit-forum]: Lido research forum (2022). *Should Lido on Ethereum be limited to some fixed % of stake?* <https://research.lido.fi/t/should-lido-on-ethereum-be-limited-to-some-fixed-of-stake/2225>
[^self-limit-snapshot]: Lido DAO Snapshot (2022). *Should Lido consider self-limiting?* <https://snapshot.org/#/lido-snapshot.eth/proposal/0x10abedcc563b66b1adee60825e78c387105110fa4a1e7354ab57bc9cc1e675c2>
