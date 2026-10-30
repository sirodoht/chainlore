---
title: Uniswap
ticker: UNI
category: DeFi
status: draft
updated: 2026-10-30
---

# Uniswap

**Uniswap** is a decentralised exchange protocol that lets users swap
tokens against pools of liquidity held in smart contracts, rather than
against an order book. Prices are set by a formula, and anyone can add
tokens to a pool and earn a share of its trading fees. Uniswap launched on
[Ethereum](ethereum.md) in November 2018 and has since been deployed on
many other networks. It was created by Hayden Adams, is developed by
Uniswap Labs, and is governed by holders of the UNI token.[^history][^whitepaper-v1][^uni]

| | |
|---|---|
| Type | Decentralised exchange, automated market maker |
| Developer | Uniswap Labs (Universal Navigation Inc.) |
| Founder | Hayden Adams |
| Launch (v1) | 2018-11-02 |
| Versions | v1 (2018), v2 (2020), v3 (2021), v4 (2025) |
| Governance token | UNI |
| Initial UNI supply | 1,000,000,000 |
| Governance | Uniswap Governance, organised since 2025 as DUNI, a Wyoming DUNA |
| Licence | v4 core: Business Source License 1.1; v3 core: GPL-2.0-or-later since 2023 |
| Own network | Unichain (mainnet 2025-02-11) |
| Other products | UniswapX, Uniswap web app and wallet |
| Live data | [DefiLlama](https://defillama.com/protocol/uniswap), [Uniswap explorer](https://app.uniswap.org/explore) |

## History

### Origins

Hayden Adams was laid off from a job as a mechanical engineer at Siemens
on 6 July 2017. Karl Floersch, then working on Ethereum research at the
Ethereum Foundation, encouraged him to learn smart contract development
and suggested he build an automated market maker. Adams has said the
design was inspired by posts by Vitalik Buterin on on-chain market
makers. He credits Alan Lu of Gnosis with first conceiving of "x\*y=k"
market makers on Ethereum.[^history] In his June 2017 post "On path
independence", Buterin described the constant product design as his
favourite and credited it to Martin Köppelmann.[^path-independence]

In April 2018 Floersch introduced him to Buterin, who suggested
writing the contracts in Vyper and applying for an Ethereum Foundation
grant.[^history] The foundation's Wave III grants, announced in August
2018, gave Uniswap US$100,000 for a "DEX framework".[^ef-grants] With
the grant, Adams contracted Runtime Verification to formally verify and
audit the contracts.[^history] Adams later became chief executive of Uniswap
Labs.[^wells-coindesk]

### v1 and v2

Uniswap v1 went live on Ethereum mainnet on 2 November 2018, the last
day of the Devcon 4 conference in Prague, with about US$30,000 of
liquidity from a single provider.[^history] Each v1 exchange contract
paired one ERC-20 token with ether, so a swap between two tokens was
routed through ETH.[^whitepaper-v1]

Uniswap Labs announced v2 on 23 March 2020 and deployed it on 18 May
2020.[^v2-announce][^v2-launch] v2 allowed pools between any two ERC-20
tokens, added price oracles and "flash swaps", in which a user can
receive tokens and pay for them later in the same transaction, and
included a protocol fee that was switched off at launch.[^v2-announce]

### SushiSwap and the UNI token

SushiSwap, a copy of Uniswap with an added token, launched on 28 August
2020. It paid SUSHI tokens to users who deposited their Uniswap
liquidity tokens, and on 9 September 2020 moved more than US$800 million
of that liquidity out of Uniswap's pools.[^sushi-theblock][^sushi-coindesk]
The episode became known as a "vampire attack".[^vampire]

On 16 September 2020 Uniswap introduced UNI, with 1 billion tokens
minted at genesis. Of these, 15% were airdropped to past users,
including 400 UNI to each of 251,534 addresses that had used the
protocol before 1 September 2020. A liquidity mining programme ran from
18 September to 17 November 2020 on four ETH pools.[^uni]

| Recipient | Share |
|---|---|
| Community (airdrop, liquidity mining, treasury) | 60% |
| Team and future employees | 21.266% |
| Investors | 18.044% |
| Advisors | 0.69% |

Team, investor and advisor tokens vested over four years. After four
years, up to 2% of supply a year may be minted.[^uni]

### v3

Uniswap Labs announced v3 on 23 March 2021 and deployed it on Ethereum
on 5 May 2021.[^v3-announce][^v3-launch] Its main change was
concentrated liquidity: providers choose a price range for their funds,
and each position is represented by a non-fungible token. Uniswap Labs
claimed this could make capital up to 4,000 times more efficient than in
v2. v3 also introduced three fee tiers (0.05%, 0.30% and 1%) and
cheaper oracles.[^v3-announce] A 0.01% tier was added by a governance
vote in late 2021.[^prop-9][^unification]

The v3 core contracts were released under the Business Source License
1.1, which limits commercial and production use of the code for a
period. Uniswap Labs described it as "effectively a time-delayed
GPL-2.0-or-later license".[^v3-announce] The licence set a change date
of 1 April 2023 at the latest, after which the code converts to GPL.[^v3-licence]

### Uniswap Labs and the Uniswap Foundation

In October 2022 Uniswap Labs raised US$165 million in a Series B round
led by Polychain Capital.[^series-b] The Uniswap Foundation was set up
in 2022, building on a grants programme begun in 2021. Its co-founders are Devin Walsh and Ken
Ng.[^uf-about]

In July 2023 Uniswap Labs introduced UniswapX (see
[below](#uniswapx)).[^uniswapx] On 17 October 2023 it began charging a
0.15% fee on some swaps made through its web app and wallet, separate
from the protocol fee controlled by governance.[^interface-fee] On 10
April 2024 it raised the fee to 0.25% and extended it to most
pairs.[^interface-fee-hike]

### v4 and Unichain

Uniswap Labs published the design of v4 in June 2023.[^v4-vision] It
went live on 31 January 2025, initially on 12 networks, including
Ethereum, Arbitrum, [Base](base.md), OP Mainnet, Polygon and BNB
Chain.[^v4-launch-uf][^v4-launch-theblock]

Unichain, Uniswap Labs' own layer 2 network in the
[Optimism](optimism.md) Superchain, launched on 11 February 2025.
Uniswap Labs states that it launched as a Stage 1 rollup with one-second
blocks and permissionless fault proofs.[^unichain]

### UNIfication and the fee switch

On 10 November 2025 Hayden Adams of Uniswap Labs and Devin Walsh and Ken
Ng of the Uniswap Foundation proposed "UNIfication". It would turn on
protocol fees and use them to burn UNI, starting with v2 pools and the
v3 pools that make up most liquidity provider fees on Ethereum. On v2,
the provider fee would fall from 0.30% to 0.25%, with 0.05% going to the
protocol. Unichain's net sequencer fees, after an Optimism share of 15%,
would also go to the burn. The proposal also included a retroactive burn
of 100 million UNI from the treasury, an end to Uniswap Labs' interface,
wallet and API fees, the transfer of most Foundation staff to Labs, and
an annual growth budget of 20 million UNI paid to Labs.[^unification]
Adams said the fee switch had been delayed "in great part due to a
hostile regulatory environment".[^unification-theblock]

The on-chain vote ended on 25 December 2025 with more than 125 million
UNI in favour and 742 against.[^unification-passed][^unification-coindesk]
The proposal was executed on 29 December 2025, sending 100 million UNI
to a burn address and enabling v2 and v3 protocol fees.[^prop-93]

### 2026

Governance extended protocol fees in a series of votes. In March 2026 it
enabled fees on all v3 pools on Ethereum and on v2 and v3 pools on eight
more networks.[^prop-94][^proposals] On 1 July 2026 Uniswap deployed v2,
v3 and v4 on Robinhood Chain, which is built on [Arbitrum](arbitrum.md)
technology. Later that month governance enabled fees there and turned
on v4 protocol fees for the first time, on seven
networks.[^v4-fees-theblock][^prop-100]

Uniswap Labs also launched Earn, a lending product built on Morpho, in
July 2026.[^earn] On 22 October 2026 aggregator hooks, which let v4 route trades through other exchanges such
as Curve and PancakeSwap and charge a protocol fee on them, went live on
Ethereum, Base and Robinhood Chain.[^aggregator-hooks]

## Technology

### Constant product market maker

Each Uniswap v1 and v2 pool holds reserves of two tokens and keeps the
product of the reserves constant (x × y = k). A trader who adds one token
to the pool must take out enough of the other to keep the product
unchanged, so each trade moves the price, and larger trades move it
more.[^whitepaper-v1] Arbitrageurs trade whenever the pool price differs
from prices elsewhere, which keeps it in line with the market.[^returns]

Liquidity providers deposit both tokens and receive liquidity tokens
representing their share of the pool. In v1 and v2 a 0.3% fee on every
trade is added to the pool and shared pro rata among
providers.[^whitepaper-v1][^returns]

### Liquidity provider risk

When prices move, arbitrage changes the mix of tokens in a pool, and a
provider's share can end up worth less than if they had simply held the
tokens. Uniswap's documentation calls this impermanent loss, because it
disappears if the price returns to where it was when the liquidity was
added. It gives examples: a 1.5-fold price change leads to a loss of
about 2% compared with holding, and a 5-fold change to about 25.5%. Fees
can offset the loss, and the documentation notes that providers do
better when prices move back and forth than when they move steadily in
one direction.[^returns]

### Oracles

From v2, each pool records a running sum of its price, measured at the
start of each block before any trades. Other contracts can read this sum
at two times and compute a time-weighted average price (TWAP). To
manipulate it, an attacker has to move the price at the end of a block
and hold it there, and usually loses money to arbitrageurs. Uniswap's
documentation states that the cost rises roughly in line with the pool's
liquidity.[^oracles] v3 kept TWAPs, reduced their gas cost, and allowed
averages to be computed over roughly the previous nine
days.[^v3-announce]

### v4: singleton and hooks

In v4 all pools live in a single "singleton" contract. Uniswap Labs estimated this cuts the cost of
creating a pool by 99%. Under "flash accounting", only net balances are
settled at the end of a transaction. v4 also restores native ETH and
allows any fee level, including dynamic fees.[^v4-vision]

Hooks are external contracts that a pool can call at points such as
before or after a swap or a change in liquidity. They let developers add
features such as dynamic fees, custom pricing curves or automatic
rebalancing of positions. Each pool
can use its own hook, set when the pool is created.[^v4-vision][^v4-launch-uf] According
to The Block, v4 went through nine audits and a security competition,
and had a US$15.5 million bug bounty.[^v4-launch-theblock] Like v3 before
it, v4 was released under the Business Source License, with exceptions
grantable by governance.[^v4-vision][^v4-launch-uf]

### UniswapX

UniswapX, released on 17 July 2023, is a separate protocol in which
users sign orders off-chain and third-party "fillers" compete to execute
them through a Dutch auction, using Uniswap pools, other venues or their
own inventory. Fillers pay the gas. Uniswap Labs states that this
protects users from sandwich attacks and returns value that would
otherwise go to arbitrage. The contracts are open source under the
GPL.[^uniswapx]

## Governance

UNI holders govern the protocol. They can spend the treasury, set and
switch on protocol fees, and mint new UNI up to 2% a year. To vote,
holders must delegate their voting power to an
address.[^governance] Binding votes take place on-chain through
a GovernorBravo contract, which limits each proposal to 10 actions, so
large changes are split across several votes.[^prop-94][^prop-100] A
proposal needs 40 million UNI in favour to reach
quorum.[^prop-93]

In September 2025 governance voted to register as
DUNI, a Wyoming Decentralized Unincorporated Nonprofit Association
(DUNA). The proposal described the aim as limiting the personal
liability of participants and allowing governance to sign contracts and
meet tax obligations. It transferred US$16.5 million worth of UNI to
DUNI for legal defence and tax compliance, and was executed on 12
September 2025.[^duni-vote][^duni-theblock]

v2 was built with a fee switch that would send 0.05% of each trade to
the protocol, but it stayed off for years, partly over fears that
liquidity providers would leave and partly over legal, tax and
securities concerns.[^vote-delay][^fee-switch-2022] In 2024 the Uniswap
Foundation delayed a vote on a new fee mechanism after "a stakeholder
raised a new issue".[^vote-delay]

## Incidents and controversies

- **SushiSwap migration (2020).** SushiSwap's founder, the pseudonymous
  Chef Nomi, converted SUSHI tokens to ether on 6 September 2020,
  leading to accusations of an exit scam. Control passed to Sam
  Bankman-Fried of [FTX](ftx.md), who ran the migration of Uniswap
  liquidity.[^sushi-theblock] CoinDesk reported that day that Uniswap had
  nonetheless ended up with more liquidity than when SushiSwap was
  announced.[^sushi-coindesk]
- **Interface fees (from 2023).** The interface fee was set by Uniswap
  Labs, not by governance. Adams said it was separate from the protocol
  fee switch and that users could avoid it by using other interfaces,
  aggregators or the contracts directly.[^interface-fee] The
  UNIfication proposal said Labs' interface, wallet and API fees "will
  be set to zero".[^unification][^unification-passed]
- **SEC investigation (2024–2025).** On 10 April 2024 Uniswap Labs
  disclosed a Wells notice from the US Securities and Exchange
  Commission, warning that its staff planned to recommend enforcement
  action.[^fighting] Its executives said the notice concerned acting as
  an unregistered securities broker and exchange. Adams said he was
  "ready to fight".[^wells-coindesk] On 25 February 2025 Uniswap Labs
  announced that the SEC had closed the investigation with no
  action.[^sec-closed] The Wall Street Journal reported the same, citing
  sources, amid other SEC closures under acting chair Mark
  Uyeda.[^sec-closed-theblock]
- **CFTC settlement (2024).** On 4 September 2024 the Commodity Futures
  Trading Commission settled charges that Uniswap Labs had illegally
  offered leveraged retail commodity transactions through leveraged
  tokens traded on the protocol and its web interface. Uniswap Labs agreed to pay a US$175,000 civil
  penalty and to cease and desist. The CFTC said it reduced the penalty
  because the company cooperated.[^cftc]
- **UNIfication criticism (2025).** CoinDesk Research argued that the
  lower v2 provider fee could push liquidity providers to rival
  exchanges paying higher fees, and that buybacks alone might not make
  UNI attractive.[^coindesk-research] Another CoinDesk analysis noted that
  merging Foundation work into Labs might "alienate some DAO
  purists".[^coindesk-proposal]

## Timeline

| Date | Event |
|---|---|
| 2018-11-02 | Uniswap v1 launches at Devcon 4 |
| 2020-05-18 | Uniswap v2 deployed |
| 2020-09-09 | SushiSwap migrates over US$800M of Uniswap liquidity |
| 2020-09-16 | UNI launched and airdropped |
| 2021-05-05 | Uniswap v3 deployed |
| 2023-07-17 | UniswapX launched |
| 2023-10-17 | 0.15% interface fee begins |
| 2024-04-10 | SEC Wells notice disclosed; interface fee raised to 0.25% |
| 2024-09-04 | CFTC settlement |
| 2025-01-31 | Uniswap v4 live on 12 networks |
| 2025-02-11 | Unichain mainnet |
| 2025-02-25 | Uniswap Labs announces SEC closed its investigation |
| 2025-11-10 | UNIfication proposed |
| 2025-12-29 | UNIfication executed; 100M UNI burned |
| 2026-03-07 | Protocol fees extended to all Ethereum v3 pools and more networks |
| 2026-07-01 | Uniswap deployed on Robinhood Chain |
| 2026-07-27 | v4 protocol fees activated on seven networks |
| 2026-10-22 | Aggregator hooks live on Ethereum, Base and Robinhood Chain |

## See also

- [Ethereum](ethereum.md)
- [Arbitrum](arbitrum.md), whose technology Robinhood Chain uses
- [Optimism](optimism.md), whose OP Stack Unichain uses
- [Base](base.md), one of the networks where v4 launched
- [FTX](ftx.md), whose chief executive ran the SushiSwap migration

## References

[^history]: Adams, H. (2019). *A short history of Uniswap*. Uniswap Labs. <https://blog.uniswap.org/uniswap-history>
[^path-independence]: Buterin, V. (2017). *On path independence*. <https://vitalik.eth.limo/general/2017/06/22/marketmakers.html>
[^ef-grants]: Ethereum Foundation (2018). *Ethereum Foundation grants update – Wave III*. <https://blog.ethereum.org/2018/08/17/ethereum-foundation-grants-update-wave-3>
[^whitepaper-v1]: Uniswap. *Uniswap whitepaper* (v1, HackMD). <https://hackmd.io/@HaydenAdams/HJ9jLsfTz>
[^v2-announce]: Uniswap Labs (2020). *Uniswap v2 overview*. <https://blog.uniswap.org/uniswap-v2>
[^v2-launch]: Uniswap Labs (2020). *Uniswap v2 mainnet launch*. <https://blog.uniswap.org/launch-uniswap-v2>
[^sushi-theblock]: The Block (2020). *SushiSwap initiates migration of over $800M in liquidity funds from Uniswap*. <https://www.theblock.co/post/77324/sushiswap-initiates-migration-of-over-800m-in-liquidity-funds-from-uniswap>
[^sushi-coindesk]: CoinDesk (2020). *SushiSwap migration ushers in era of 'protocol politicians'*. <https://www.coindesk.com/tech/2020/09/09/sushiswap-migration-ushers-in-era-of-protocol-politicians>
[^vampire]: CoinDesk (2021). *'Continuous vampire attack': The AMM wars are getting interesting with Integral*. <https://www.coindesk.com/tech/2021/03/29/continuous-vampire-attack-the-amm-wars-are-getting-interesting-with-integral>
[^uni]: Uniswap Labs (2020). *Introducing UNI*. <https://blog.uniswap.org/uni>
[^v3-announce]: Uniswap Labs (2021). *Introducing Uniswap v3*. <https://blog.uniswap.org/uniswap-v3>
[^v3-launch]: Uniswap Labs (2021). *Uniswap v3 mainnet launch*. <https://blog.uniswap.org/launch-uniswap-v3>
[^prop-9]: Uniswap Governance. *Add 1 Basis Point Fee Tier* (proposal 9). <https://vote.uniswapfoundation.org/proposals/9>
[^v3-licence]: Uniswap Labs. *v3-core LICENSE* (Business Source License 1.1). GitHub. <https://raw.githubusercontent.com/Uniswap/v3-core/main/LICENSE>
[^series-b]: Uniswap Labs (2022). *Bringing Web3 to everyone*. <https://blog.uniswap.org/bringing-web3-to-everyone>
[^uf-about]: Uniswap Foundation. *About*. <https://www.uniswapfoundation.org/about>
[^uniswapx]: Uniswap Labs (2023). *Introducing the UniswapX protocol*. <https://blog.uniswap.org/uniswapx-protocol>
[^interface-fee]: The Block (2023). *Uniswap to charge 0.15% to swap certain tokens on web interface and wallet*. <https://www.theblock.co/post/257798/uniswap-to-charge-0-15-to-swap-certain-tokens-on-web-interface-and-wallet>
[^interface-fee-hike]: The Block (2024). *Uniswap Labs hikes swap fee to .25% from .15% on trades through interface*. <https://www.theblock.co/post/288170/uniswap-labs-hikes-swap-fee-to-25-from-15-on-trades-through-interface>
[^v4-vision]: Uniswap Labs (2023). *Our vision for Uniswap v4*. <https://blog.uniswap.org/uniswap-v4>
[^v4-launch-uf]: Uniswap Foundation (2025). *Uniswap v4: supercharging DeFi across chains*. <https://uniswapfoundation.org/blog/uniswap-v4-supercharging-defi-across-chains>
[^v4-launch-theblock]: The Block (2025). *Uniswap V4 goes live, with swaps rolling out across the next few days*. <https://www.theblock.co/post/338223>
[^unichain]: Uniswap Labs (2025). *Unichain mainnet is here*. <https://blog.uniswap.org/unichain-mainnet-is-here>
[^duni-vote]: Uniswap Governance. *Establish Uniswap Governance as "DUNI," a Wyoming DUNA* (proposal 90). <https://vote.uniswapfoundation.org/proposals/90>
[^duni-theblock]: The Block (2025). *Uniswap community votes on Wyoming legal entity to support offchain operations*. <https://www.theblock.co/post/369433/uniswap-votes-legal-entity>
[^unification]: Adams, H., Ng, K., and Walsh, D. (2025). *UNIfication*. Uniswap Labs. <https://blog.uniswap.org/unification>
[^unification-theblock]: The Block (2025). *UNI token soars 30% as Uniswap Labs and Foundation propose fee switch activation*. <https://www.theblock.co/news/defi/2025-11-10-uni-token-soars-26-uniswap-labs-foundation-propose-fee-switch-activation-378257>
[^unification-passed]: The Block (2025). *Uniswap governance passes major 'UNIfication' proposal; 100 million token burn imminent*. <https://www.theblock.co/post/383742/uniswap-passes-unification-proposal>
[^unification-coindesk]: CoinDesk (2025). *Uniswap's UNI token burn, protocol fee 'UNIfication' proposal backed overwhelmingly by voters*. <https://www.coindesk.com/business/2025/12/26/uniswap-s-token-burn-protocol-fee-proposal-backed-overwhelmingly-by-voters>
[^prop-93]: Uniswap Governance. *UNIfication* (proposal 93). <https://vote.uniswapfoundation.org/proposals/93>
[^prop-94]: Uniswap Governance. *Protocol Fee Expansion: Vote 1* (proposal 94). <https://vote.uniswapfoundation.org/proposals/94>
[^proposals]: Uniswap Governance. Proposals. <https://vote.uniswapfoundation.org/proposals>
[^v4-fees-theblock]: The Block (2026). *UNI burn poised to grow as Uniswap governance votes on v4 fees and Robinhood Chain expansion*. <https://www.theblock.co/news/defi/2026-07-18-uni-burn-poised-to-grow-as-uniswap-governance-votes-on-v4-fees-and-robinhood-chain-expansion-408836>
[^prop-100]: Uniswap Governance. *Activate v4 Protocol Fees (Part 1/2)* (proposal 100). <https://vote.uniswapfoundation.org/proposals/100>
[^earn]: The Block (2026). *Uniswap launches 'Earn' with Morpho to let users earn yield on idle crypto assets*. <https://www.theblock.co/news/defi/2026-07-31-uniswap-morpho-earn-yield-gauntlet-vaults-410286>
[^aggregator-hooks]: The Block (2026). *Uniswap's aggregator hooks go live on Ethereum, Base and Robinhood Chain*. <https://www.theblock.co/news/defi/2026-10-22-uniswaps-aggregator-hooks-go-live-ethereum-base-robinhood-chain-421932>
[^returns]: Uniswap documentation. *Understanding returns* (v2). <https://developers.uniswap.org/docs/protocols/v2/concepts/understanding-returns>
[^oracles]: Uniswap documentation. *Oracles* (v2). <https://developers.uniswap.org/llms.mdx/docs/protocols/v2/concepts/oracles>
[^governance]: Uniswap documentation. *Governance overview*. <https://developers.uniswap.org/docs/ecosystem/governance/overview>
[^vote-delay]: CoinDesk (2024). *Uniswap vote delay shows DeFi stakeholders aren't all in it together*. <https://www.coindesk.com/tech/2024/06/03/uniswap-vote-delay-shows-defi-stakeholders-arent-all-in-it-together>
[^fee-switch-2022]: Decrypt (2022). *Unpacking Uniswap's 'fee switch'*. <https://decrypt.co/105823/unpacking-uniswaps-fee-switch>
[^fighting]: Uniswap Labs (2024). *Fighting for DeFi*. <https://blog.uniswap.org/fighting-for-defi>
[^wells-coindesk]: CoinDesk (2024). *DeFi exchange Uniswap receives enforcement notice from the SEC*. <https://www.coindesk.com/policy/2024/04/10/defi-exchange-uniswap-receives-enforcement-notice-from-the-sec>
[^sec-closed]: Uniswap Labs (2025). *A win for DeFi: SEC closes investigation into Uniswap Labs*. <https://blog.uniswap.org/a-win-for-defi>
[^sec-closed-theblock]: The Block (2025). *SEC drops Uniswap Labs investigation as agency continues crypto-friendly push*. <https://www.theblock.co/post/343353/sec-drops-uniswap-labs-investigation-as-agency-continues-crypto-friendly-push-wsj>
[^cftc]: Commodity Futures Trading Commission (2024). *CFTC issues order against Uniswap Labs for offering illegal digital asset derivatives trading* (release 8961-24). <https://www.cftc.gov/PressRoom/PressReleases/8961-24>
[^coindesk-research]: Diwan, S. (2025). *Uniswap's UNIfication proposal: buybacks and competitive risk*. CoinDesk Research. <https://www.coindesk.com/research/uniswap-s-unification-proposal-buybacks-and-competitive-risk>
[^coindesk-proposal]: CoinDesk (2025). *What Uniswap's latest proposal really means for UNI token buyers*. <https://www.coindesk.com/markets/2025/11/12/what-uniswap-s-latest-proposal-really-means-for-uni-token-buyers>
