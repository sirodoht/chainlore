---
title: Hyperliquid
ticker: HYPE
category: Layer 1
status: draft
updated: 2026-10-30
---

# Hyperliquid

**Hyperliquid** is a layer 1 blockchain built to run a fully onchain
order book exchange for perpetual futures and spot trading. It has two
execution environments secured by one consensus: **HyperCore**, which
runs the order books, margining, and liquidations, and **HyperEVM**, an
EVM environment that is part of the same chain rather than a separate
one.[^overview][^hyperevm] Its native token is **HYPE**. Hyperliquid was
built by Hyperliquid Labs, which states it took no outside venture
funding.[^contributors]

| | |
|---|---|
| Ticker | HYPE |
| Type | Layer 1 blockchain, perpetual futures exchange |
| Developer | Hyperliquid Labs |
| Founders | Jeff Yan, iliensinc (pseudonym) |
| Consensus | HyperBFT |
| Execution | HyperCore (order books), HyperEVM |
| HyperEVM chain ID | 999 |
| Token genesis | 2024-11-29 |
| HYPE max supply | 1,000,000,000 |
| Quote asset | USDC, natively issued on Hyperliquid |
| Funding payments | Hourly |
| Outside funding | None (per Hyperliquid Labs) |
| Live data | [DefiLlama](https://defillama.com/protocol/hyperliquid), [Hyperscreener](https://hyperscreener.asxn.xyz/home) (third party) |

## History

### Founding

Hyperliquid was founded by Jeff Yan and a pseudonymous co-founder known
as iliensinc. Yan studied mathematics and computer science at Harvard
University and briefly worked as an algorithm developer at Hudson River
Trading, a high-frequency trading firm, before moving into
crypto.[^fortune][^efc] From 2020 the team did proprietary market making
in crypto, through a firm called Chameleon
Trading.[^contributors][^coinbureau] Hyperliquid Labs has stayed small,
with about a dozen people, and has not raised money from outside
investors.[^fortune]

The team set out to build an exchange with the speed and features of a
centralized exchange but with every order and trade recorded onchain.
Yan has said the collapse of the centralized exchange FTX in November
2022 convinced him it was the right time to build a decentralized
exchange.[^fortune] Hyperliquid opened as a closed alpha in February
2023 and launched fully later that year.[^decrypt-explainer] The first
versions ran on the Tendermint consensus engine; in 2024 the team
replaced it with its own, HyperBFT.[^despread]

### Growth

Hyperliquid's trading volume grew through 2023 and 2024. In 2025 it was
the largest decentralized exchange for perpetual futures by open
interest, and for most of the year by volume, ahead of earlier venues
such as dYdX and GMX, a perpetual futures exchange that started on
[Arbitrum](arbitrum.md). In late 2025 newer exchanges, including Aster
and Lighter, briefly matched or passed its daily volume, partly through
incentive programmes.[^aster] Large, active traders account for much of
Hyperliquid's activity, and some of their leveraged positions, being
public onchain, are followed closely on social media.

### Points and token genesis

A points program for traders began on 1 November 2023. Points were
distributed weekly in two phases: 1 million a week until May 2024, and
700,000 a week from late May to November 2024.[^points] On 29 November
2024 the Hyper Foundation's token genesis event distributed 31% of
HYPE's supply to points holders, with no allocation to private
investors.[^genesis][^genesis-block] The airdrop went to about 94,000
addresses and was one of the largest by value in crypto at the
time.[^airdrop] Core contributors' tokens were locked for one year and
began unlocking in late November 2025.[^unlock]

| Recipient | Share |
|---|---|
| Future emissions and community rewards | 38.888% |
| Genesis distribution (airdrop) | 31% |
| Core contributors | 23.8% |
| Hyper Foundation budget | 6% |
| Community grants | 0.3% |
| HIP-2 liquidity | 0.012% |

Native staking of HYPE opened on 30 December 2024.[^staking-launch] The
absence of venture investors and the size of the airdrop were widely
discussed as a contrast to token launches funded by venture capital.

### HyperEVM, stablecoins, and builder markets

HyperEVM launched on mainnet on 18 February 2025.[^hyperevm-launch] It
let developers deploy Ethereum-style smart contracts on the same chain
as the exchange. On 30 April 2025 contracts gained the ability to read
HyperCore state, such as prices and positions, and on 5 July 2025 to send
actions to HyperCore, such as placing orders.[^galaxy] Lending markets,
liquid staking tokens for HYPE, and other applications were built on it.

On 14 February 2025 Unit, a tokenization protocol built on Hyperliquid,
began offering spot trading of native BTC, deposited from the Bitcoin
network, and later added other assets such as ETH and SOL.[^unit]

On 14 September 2025 validators, with about 70% of stake, voted to award
the USDH stablecoin ticker to Native Markets.[^usdh] Two days later
Circle launched native USDC on Hyperliquid, which replaced the original
bridge from Arbitrum as the main way USDC enters the chain.[^circle][^usdc]
On 14 May 2026 Coinbase became the official deployer of USDC treasury on
Hyperliquid, and USDH began to be phased out.[^coinbase]

On 13 October 2025 HIP-3 went live, letting anyone who stakes 500,000
HYPE deploy their own perpetual futures markets.[^hip3-launch] Builders
used it to list markets that other exchanges did not, including
perpetuals on equities and other traditional assets.[^hip3-equities] On
2 May 2026 HIP-4 added outcome markets, a form of prediction
market.[^hip4-launch]

### Supply burn

The Assistance Fund converts trading fees into HYPE. In December 2025
validators voted to recognize the HYPE held by the fund as burned,
removing it from total and circulating supply.[^fees][^burn-vote]

### Exchange-traded products

In May 2026 the first US spot HYPE exchange-traded products began
trading, including 21Shares' THYP and Bitwise's BHYP.[^etf]

## Technology

### Consensus

HyperBFT is a Byzantine fault tolerant consensus protocol derived from
HotStuff. Validators stake HYPE, and their voting power is proportional
to the HYPE staked with them, including HYPE delegated by other holders.
Validators that respond too slowly can be jailed by a vote of other
validators, which removes them from consensus and stops rewards to their
delegators. Blocks are final as soon as they are produced, with no
probabilistic waiting period.[^overview][^staking]

### HyperCore

HyperCore keeps the full order book onchain: every order, cancellation,
trade, and liquidation is a transaction, ordered by consensus. Trades are
final in the block in which they are matched. Traders can use cross
margin, which shares collateral across positions, or isolated margin,
which limits losses to the collateral assigned to one
position.[^margining]

Perpetual futures have no expiry. To keep their price close to the
underlying asset, traders on one side pay the other a funding rate every
hour.[^funding] Validators publish oracle prices about every three
seconds, calculated as a weighted median of prices on centralized
exchanges. Oracle prices are used to calculate funding, and are one
input to the mark price, which also draws on Hyperliquid's own order
book and decides when positions are liquidated.[^oracle]

When a position falls below its maintenance margin it is liquidated,
first by closing it with market orders on the order book and, if equity
keeps falling, by transferring it to HLP. If an account's value turns
negative, auto-deleveraging closes profitable positions on the other
side.[^liquidations][^adl]

Hyperliquid Improvement Proposals (HIPs) define its main
features:[^hips]

- **HIP-1**: a native token standard for spot assets on HyperCore.
- **HIP-2**: "Hyperliquidity", automated market making for HIP-1 tokens.
- **HIP-3**: permissionless perpetual futures markets deployed by
  builders who stake HYPE.
- **HIP-4**: outcome markets.

### Vaults

The **Hyperliquidity Provider (HLP)** vault is a community-owned vault
that makes markets and takes over liquidated positions. Depositors share
its profit and loss. Deposits are locked for four days.[^hlp]

Anyone can also create a vault and trade with other people's deposits.
The vault leader must keep at least 5% of the vault's capital and
receives 10% of its profits.[^vault-leaders]

### Fees and the Assistance Fund

Trading fees are tiered by 14-day volume and lower for traders who stake
HYPE. Front-ends built on Hyperliquid can add their own fee through
"builder codes".[^builder-codes] The **Assistance Fund** converts trading
fees to HYPE automatically as part of chain execution. HYPE in the fund
is treated as burned.[^fees]

### HyperEVM

HyperEVM produces two kinds of blocks: small blocks about every second,
with a 2 million gas limit, for ordinary transactions, and large blocks
about every minute, with a 30 million gas limit, for contract
deployments and other heavy transactions. Its gas token is HYPE.
Contracts can read HyperCore state through precompiles and send actions
to HyperCore through a system contract called CoreWriter.[^galaxy]

### USDC

USDC is issued natively on Hyperliquid through Circle's Cross-Chain
Transfer Protocol. A legacy bridge on Arbitrum, whose withdrawals are
signed by Hyperliquid's validators, holds a small and shrinking share of
USDC on HyperCore.[^usdc]

## Governance

HYPE holders do not vote on proposals directly, but can influence votes
by choosing which validator to delegate to. Decisions such as delisting
markets, awarding tickers, and changing the supply of HYPE are taken by
validators, voting in proportion to their stake. The Hyper Foundation
runs several validators and holds a large share of staked
HYPE.[^foundation-stake][^delegation] Major features are specified as
HIPs; the software is written and shipped by Hyperliquid Labs.

## Incidents and controversies

- **North Korea concerns (December 2024).** Security researchers flagged
  addresses linked to North Korean hackers trading on the platform,
  prompting record outflows. The team said no exploit had
  occurred.[^dprk]
- **ETH whale liquidation (March 2025).** On 12 March 2025 a trader with
  a roughly 50x ETH long worth about US$300 million withdrew collateral
  and unrealized profit, leaving the position just above liquidation.
  When it was liquidated HLP took it over and lost about US$4 million.
  Hyperliquid then cut maximum leverage to 40x on BTC and 25x on
  ETH.[^whale]
- **JELLY delisting (March 2025).** On 26 March 2025 a trader
  manipulated the price of the thinly traded JELLYJELLY token and left
  HLP holding a large short. Validators delisted the market and settled
  it at US$0.0095, turning a potential loss of about US$10 million for
  HLP into a gain of about US$700,000. Critics said the intervention
  showed that a small validator set could override market
  outcomes.[^jelly]
- **API outage (July 2025).** On 29 July 2025 Hyperliquid's API stopped
  serving requests for about 40 minutes, leaving traders unable to manage
  positions. Hyperliquid reimbursed affected users about US$2
  million.[^outage][^outage-refund]
- **Validator centralization.** The validator set is small compared with
  other major layer 1s. In 2025 five Hyper Foundation validators held
  more than half of all stake.[^validators]
- **October 2025 liquidations.** During the market crash of 10–11
  October 2025, about US$10 billion of positions were liquidated on
  Hyperliquid, and it triggered cross-margin auto-deleveraging of
  profitable positions for the first time in over two years.[^oct-2025]
- **POPCAT (November 2025).** On 12 November 2025 a trader using 19
  wallets opened large long positions in the POPCAT memecoin, supported
  by a large buy order. When the trader withdrew the order, the price
  fell, the positions were liquidated into HLP, and the vault lost about
  US$4.9 million.[^popcat]
- **Transparency of positions.** Because every position is public,
  traders with large positions can be targeted by others trying to push
  prices to their liquidation levels.[^whale-hunting] Critics, including
  Binance founder Changpeng Zhao, have argued that perpetual futures
  exchanges should hide positions; Yan has defended the transparency.

## Timeline

| Date | Event |
|---|---|
| 2023-02 | Closed alpha opens |
| 2023-11-01 | Points program begins |
| 2024 | HyperBFT replaces Tendermint |
| 2024-11-29 | HYPE token genesis; 31% airdropped |
| 2024-12 | North Korea-linked trading flagged |
| 2024-12-30 | Native HYPE staking opens |
| 2025-02-14 | Unit brings native BTC spot trading |
| 2025-02-18 | HyperEVM mainnet |
| 2025-03-12 | ETH whale liquidation costs HLP about US$4M |
| 2025-03-26 | JELLY market delisted by validators |
| 2025-04-30 | HyperEVM contracts can read HyperCore state |
| 2025-07-05 | HyperEVM contracts can send actions to HyperCore |
| 2025-07-29 | API outage; users reimbursed about US$2M |
| 2025-09-14 | USDH ticker awarded to Native Markets |
| 2025-09-16 | Native USDC launches on Hyperliquid |
| 2025-10-10 | About US$10B liquidated; auto-deleveraging triggered |
| 2025-10-13 | HIP-3 live |
| 2025-11-12 | POPCAT manipulation costs HLP about US$4.9M |
| 2025-11-29 | Core contributor tokens begin unlocking |
| 2025-12 | Assistance Fund HYPE recognized as burned |
| 2026-05-02 | HIP-4 outcome markets live |
| 2026-05 | US spot HYPE ETPs begin trading |
| 2026-05-14 | Coinbase becomes official USDC deployer; USDH phased out |

## See also

- [Arbitrum](arbitrum.md), home of Hyperliquid's legacy USDC bridge
- [Ethereum](ethereum.md)

## References

[^overview]: Hyperliquid documentation. *HyperCore overview*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/overview>
[^hyperevm]: Hyperliquid documentation. *HyperEVM*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperevm>
[^contributors]: Hyperliquid documentation. *Core contributors*. <https://hyperliquid.gitbook.io/hyperliquid-docs/about-hyperliquid/core-contributors>
[^fortune]: Fortune (2026). *How a Harvard grad helped make Hyperliquid the biggest new player in crypto*. <https://fortune.com/2026/01/12/hyperliquid-jeff-yan-defi-perpetuals-perps-exchange-defi/>
[^efc]: eFinancialCareers. *Jeffrey Yan*. <https://www.efinancialcareers.com/news/jeffrey-yan>
[^coinbureau]: Coin Bureau. *Hyperliquid review*. <https://coinbureau.com/review/hyperliquid-review>
[^decrypt-explainer]: Decrypt. *What is Hyperliquid?* <https://decrypt.co/341605/what-hyperliquid-decentralized-exchange-blockchain>
[^despread]: Despread Research. *Hyperliquid: The Perpetual DEX Endgame*. <https://research.despread.io/report-hyperliquid/>
[^aster]: Decrypt (2025). *Aster vs Hyperliquid: Binance chain DEX perps volume derails the hype train*. <https://decrypt.co/341065/aster-vs-hyperliquid-binance-chain-dex-perps-volume-derails-the-hype-train>
[^points]: Hyperliquid documentation. *Points*. <https://hyperliquid.gitbook.io/hyperliquid-docs/points>
[^genesis]: Hyper Foundation (2024). HYPE genesis announcement, 28 November 2024. <https://x.com/HyperFND/status/1862007773191708760>
[^genesis-block]: The Block (2024). *Hyperliquid plans to launch HYPE token in Nov. 29 genesis event*. <https://www.theblock.co/post/328631/hyperliquid-plans-to-launch-hype-token-in-nov-29-genesis-event>
[^airdrop]: Blockworks (2024). *Hyperliquid could have the most valuable airdrop ever*. <https://blockworks.co/news/hyperliquid-most-valuable-airdrop>
[^unlock]: The Block (2025). *HYPE tokens unstaked for Hyperliquid Labs' first allocation*. <https://www.theblock.co/news/defi/2025-12-29-hype-tokens-unstaked-for-hyperliquid-labs-first-allocation-383880>
[^staking-launch]: The Block (2024). *HYPE token staking goes live on the Hyperliquid mainnet*. <https://www.theblock.co/post/332592/hype-token-staking-goes-live-on-the-hyperliquid-mainnet>
[^hyperevm-launch]: The Block (2025). HyperEVM mainnet launch. <https://www.theblock.co/post/341424>
[^galaxy]: Galaxy Research (2025). *Hyperliquid's L1 begins to find its footing*. <https://www.galaxy.com/insights/research/hyperliquids-l1-begins-to-find-its-footing>
[^unit]: The Defiant (2025). *Hyperliquid debuts Unit on-chain BTC trading*. <https://thedefiant.io/news/defi/hyperliquid-debuts-unit-on-chain-btc-trading-hype-token-surges-above-28-9fb7cbde>
[^usdh]: The Block (2025). USDH ticker vote. <https://www.theblock.co/post/370570>
[^circle]: The Block (2025). *Circle launches USDC natively on Hyperliquid*. <https://www.theblock.co/post/370946/circle-launches-usdc-natively-on-hyperliquid>
[^usdc]: Hyperliquid documentation. *USDC*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/usdc>
[^coinbase]: The Block (2026). Coinbase becomes Hyperliquid's official USDC deployer. <https://theblock.co/post/401233/coinbase-hyperliquid-official-deployer-usdc>
[^hip3-launch]: The Block (2025). HIP-3 mainnet launch. <https://www.theblock.co/post/374306>
[^hip3-equities]: Blockworks (2025). *HIP-3 brings equity perps to crypto*. <https://blockworks.com/news/hip-3-equity-perps>
[^hip4-launch]: The Block (2026). HIP-4 permissionless deployment. <https://theblock.co/post/408875/hyperliquid-hip-4-permissionless-deployment>
[^fees]: Hyperliquid documentation. *Fees*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees>
[^burn-vote]: The Block (2025). *Hyper Foundation proposes zeroing out Hyperliquid's assistance fund*. <https://www.theblock.co/post/383091/hyper-foundation-proposes-removing-1-billion-hype-tokens-from-circulating-supply-by-zeroing-out-hyperliquids-assistance-fund>
[^etf]: The Block (2026). *Hyperliquid ETFs see $22.3 million in early inflows*. <https://www.theblock.co/news/markets/2026-05-20-hyperliquid-etfs-22-3-million-early-inflows-analysts-point-organic-interest-402028>
[^staking]: Hyperliquid documentation. *Staking*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking>
[^margining]: Hyperliquid documentation. *Margining*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining>
[^funding]: Hyperliquid documentation. *Funding*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding>
[^oracle]: Hyperliquid documentation. *Robust price indices*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/robust-price-indices>
[^liquidations]: Hyperliquid documentation. *Liquidations*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations>
[^adl]: Hyperliquid documentation. *Auto-deleveraging*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/auto-deleveraging>
[^hips]: Hyperliquid documentation. *Hyperliquid Improvement Proposals*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals>
[^hlp]: Hyperliquid documentation. *Protocol vaults*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults/protocol-vaults>
[^vault-leaders]: Hyperliquid documentation. *For vault leaders*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults/for-vault-leaders>
[^builder-codes]: Hyperliquid documentation. *Builder codes*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/builder-codes>
[^foundation-stake]: Crypto Briefing (2025). *Hyper Foundation controls 49% of staked HYPE*. <https://cryptobriefing.com/hyper-foundation-staked-hype-centralization/>
[^delegation]: Hyperliquid documentation. *Delegation program*. <https://hyperliquid.gitbook.io/hyperliquid-docs/validators/delegation-program>
[^dprk]: The Block (2024). *Hyperliquid sees record outflows following North Korea hack concerns*. <https://www.theblock.co/post/332298/hyperliquid-sees-record-outflows-following-north-korea-hack-concerns>
[^whale]: The Block (2025). *HLP vault loss after Hyperliquid whale liquidation*. <https://www.theblock.co/post/345866/hype-drop-hlp-vault-loss-hyperliquid-whale-liquidation>
[^jelly]: Decrypt (2025). *Hyperliquid delists Solana meme coin after liquidation crisis*. <https://decrypt.co/311713/hyperliquid-delists-solana-meme-coin-liquidation-crisis>
[^outage]: The Block (2025). *Hyperliquid plans automated refunds after outage*. <https://www.theblock.co/post/364861/hyperliquid-outage-refund>
[^outage-refund]: Cointelegraph (2025). *Hyperliquid reimburses $2M to crypto traders after outage*. <https://cointelegraph.com/news/hyperliquid-reimburses-2m-crypto-traders-outage>
[^validators]: Blockworks (2025). *Hyperliquid decentralization and its validators*. <https://blockworks.com/news/hyperliquid-decentralization-validator-put>
[^oct-2025]: crypto.news (2025). *Hyperliquid launches HIP-3 as HYPE rebounds after $10B liquidation wave*. <https://crypto.news/hyperliquid-launches-hip-3-as-hype-rebounds-after-10b-liquidation-wave/>
[^popcat]: The Block (2025). *Hyperliquid pauses deposits and withdrawals amid POPCAT trading scheme speculation*. <https://www.theblock.co/post/378606/hyperliquid-pauses-deposits-withdrawals-popcat-trading-scheme-speculation>
[^whale-hunting]: Cointelegraph (2025). *Traders targeting Hyperliquid whales' significant positions to trigger liquidations: 10x Research*. <https://cointelegraph.com/news/traders-targeting-hyperliquid-whales-significant-positions-trigger-liquidations-10x-research>
