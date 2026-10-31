---
title: Hyperliquid
ticker: HYPE
category: Layer 1
written_by: Opus 5.5 High
status: ai-fact-checked
checked: 2026-10-30
checked_by: GPT-6-Astra high
updated: 2026-10-30
---

# Hyperliquid

**Hyperliquid** is a layer 1 blockchain built to run a fully onchain
order book exchange for perpetual futures and spot trading. It has two
execution environments secured by one consensus: **HyperCore**, which
runs the order books, margining, and liquidations, and **HyperEVM**, an
EVM environment that is part of the same chain rather than a separate
one.[^overview][^hyperevm] Its native token is **HYPE**. Hyperliquid was
built by Hyperliquid Labs, which states that development has been
self-funded without external capital.[^hyper101]

| | |
|---|---|
| Ticker | HYPE |
| Type | Layer 1 blockchain, perpetual futures exchange |
| Developer | Hyperliquid Labs |
| Founders | Jeff Yan, iliensinc (pseudonym) |
| Consensus | HyperBFT |
| Execution | HyperCore (order books), HyperEVM |
| HyperEVM chain ID | 999[^evm-dev] |
| Token genesis | 2024-11-29 |
| HYPE max supply | 1,000,000,000[^genesis-block] |
| Main collateral asset | USDC, natively issued on Hyperliquid[^usdc] |
| Funding payments | Hourly[^contracts] |
| Outside funding | None, according to Hyperliquid Labs[^hyper101] |
| Live data | [DefiLlama](https://defillama.com/protocol/hyperliquid), [Hyperscreener](https://hyperscreener.asxn.xyz/home) (third party) |

## History

### Founding

Hyperliquid was founded by Jeff Yan and the pseudonymous iliensinc.
Hyperliquid's documentation describes them as Harvard classmates and
says the team began proprietary crypto market making in 2020.[^contributors]
Yan has said that FTX's collapse in November 2022 prompted the team to
commit to building a decentralized exchange. Hyperliquid opened its
closed alpha in February 2023 and its full mainnet in August that
year.[^decrypt-explainer] It initially used Tendermint consensus;
DeSpread's December 2024 research dates the introduction of HyperBFT
to May 2024.[^despread]

### Growth

DeSpread recorded monthly trading volume of US$77 billion and open
interest of US$3.37 billion for November 2024.[^despread] Competition
grew in 2025: in September, Decrypt reported that Aster had helped BNB
Chain overtake Hyperliquid in 24-hour perpetuals volume. That was a
comparison over one day, rather than a full-year ranking.[^aster]

### Points and token genesis

A points program for traders began on 1 November 2023. Points were
distributed weekly in two phases: 1 million a week until May 2024, and
700,000 a week from late May to November 2024.[^points] On 29 November
2024 HYPE launched with 31% of its maximum supply allocated to eligible
users, and no allocation to private investors.[^genesis-block][^staking-launch]
More than 94,000 addresses were eligible; not all allocated tokens had
been claimed when Blockworks reported on it in December.[^airdrop] Core contributors' tokens were locked for one year and
began unlocking in late November 2025.[^unlock]

The major allocations announced at genesis were:[^genesis-block]

| Recipient | Share |
|---|---|
| Future emissions and community rewards | Approximately 38.8% |
| Genesis distribution (airdrop) | 31% |
| Core contributors | 23.8% |
| Hyper Foundation budget | 6% |

Native staking of HYPE opened on 30 December 2024.[^staking-launch]

### HyperEVM, stablecoins, and builder markets

HyperEVM launched on mainnet on 18 February 2025.[^galaxy] It
let developers deploy Ethereum-style smart contracts on the same chain
as the exchange. On 30 April 2025 contracts gained the ability to read
HyperCore state, such as prices and positions, and on 5 July 2025 to send
actions to HyperCore, such as placing orders.[^galaxy]

Unit provides deposits and withdrawals between Hyperliquid and other
blockchains, including Bitcoin, Ethereum, and Solana. Users can trade
those deposited assets on Hyperliquid's spot order book and withdraw
them back to their native chain.[^unit-docs]

On 14 September 2025 validators selected Native Markets for the USDH
stablecoin ticker by a two-thirds supermajority of staked HYPE; the
Hyper Foundation abstained.[^usdh] On 16 September Circle launched
native USDC and CCTP V2 on HyperEVM, with direct HyperCore support still
planned at that point.[^circle] On 14 May 2026 Coinbase announced that
it was becoming USDC's treasury deployer under Hyperliquid's Aligned
Quote Asset framework. It said USDH markets would be phased out, with
Native Markets continuing conversions and redemptions during the
transition.[^coinbase]

HIP-3 was scheduled for activation on 13 October 2025 and supports
builder-deployed perpetual markets backed by a 500,000 HYPE stake.[^hip3-launch][^hips]
These include equity perpetuals.[^hip3-equities] HIP-4 outcome markets
launched on 2 May 2026 in a limited initial release.[^hip4-launch]

On 16 September 2026 Payward announced plans to offer US clients
Hyperliquid perpetuals through its regulated entities. As of 30 October
2026, the planned deployment remained subject to regulatory approval;
Hyperliquid had announced permissioned-market functionality on
testnet.[^payward][^payward-update]

On 29 October 2026 Intercontinental Exchange and Trade[XYZ] announced
an agreement to bring Trade[XYZ]'s Hyperliquid markets into a regulated
US market and clearing structure. The announced plan was subject to
regulatory approvals.[^ice]

### Supply burn

The Assistance Fund converts trading fees into HYPE. In December 2025
the Hyper Foundation proposed recognizing the fund's HYPE as burned,
through a stake-weighted validator vote.[^burn-vote] As of 30 October
2026 the protocol documentation treats HYPE in the fund as burned and
removed from total and circulating supply.[^fees]

### Exchange-traded products

In May 2026 US spot HYPE exchange-traded products began
trading, including 21Shares' THYP and Bitwise's BHYP.[^etf]

## Technology

### Consensus

HyperBFT is a Byzantine fault tolerant consensus protocol derived from
HotStuff. Validators stake HYPE, and their voting power is proportional
to the HYPE staked with them, including HYPE delegated by other holders.
Validators that respond too slowly can be jailed by a vote of other
validators, which removes them from consensus and stops rewards to their
delegators. The protocol assumes that more than two-thirds of stake is
honest; honest nodes agree on the ordered list of committed consensus
rounds.[^overview][^staking]

### HyperCore

HyperCore keeps the full order book onchain: every order, cancellation,
trade, and liquidation is a transaction, ordered by consensus. Trades are
final in the block in which they are matched.[^about] Traders can use cross
margin, which shares collateral across positions, or isolated margin,
which separates a position's collateral from other isolated or cross
positions.[^margining]

Perpetual futures have no expiry.[^contracts] To keep their price close to the
underlying asset, traders on one side pay the other a funding rate every
hour.[^funding] For validator-operated perpetuals, validators publish oracle prices about every three
seconds, calculated as a weighted median of prices on centralized
exchanges. Oracle prices are used to calculate funding, and are one
input to the mark price, which also draws on Hyperliquid's own order
book and decides when positions are liquidated.[^oracle]

When a position falls below its maintenance margin it is liquidated,
first by closing it with market orders on the order book and, if equity
keeps falling, by transferring it to HLP. If an account's value turns
negative, auto-deleveraging closes profitable positions on the other
side.[^liquidations][^adl]

Hyperliquid Improvement Proposals (HIPs) specify protocol features:

- **HIP-1**: a native token standard for spot assets on HyperCore.[^hip1]
- **HIP-2**: "Hyperliquidity", automated market making for HIP-1 tokens.[^hip2]
- **HIP-3**: permissionless perpetual futures markets deployed by
  builders who stake HYPE.[^hips]
- **HIP-4**: fully collateralized outcome contracts with bounded settlement
  values, without leverage or liquidations.[^hip4]

### Vaults

The **Hyperliquidity Provider (HLP)** vault is a community-owned vault
that makes markets and takes over liquidated positions. Depositors share
its profit and loss. Withdrawals are locked for four days after the most recent deposit.[^hlp]

The documentation for legacy user vaults allows a leader to trade with
other people's deposits. The leader must retain at least 5% of vault
capital and receives a 10% profit share.[^vault-leaders]

### Fees and the Assistance Fund

Trading fees are tiered by 14-day volume and lower for traders who stake
HYPE.[^fees] Front-ends built on Hyperliquid can add their own fee through
"builder codes".[^builder-codes] The **Assistance Fund** converts trading
fees to HYPE automatically as part of chain execution. HYPE in the fund
is treated as burned.[^fees]

### HyperEVM

As of 30 October 2026, HyperEVM's documentation specifies small blocks
about every second, with a 3 million gas limit, for ordinary transactions, and large blocks
about every minute, with a 30 million gas limit, for contract
deployments and other heavy transactions.[^dual-blocks] Its gas token is
HYPE.[^evm-dev] Contracts can read HyperCore state through precompiles
and send actions to HyperCore through a system contract called
CoreWriter.[^corewriter]

### USDC

USDC is natively minted on Hyperliquid through Circle's contracts on
HyperEVM. CCTP provides a transfer route from Arbitrum to HyperCore.
As of 30 October 2026, Hyperliquid's documentation says the legacy
Arbitrum bridge holds less than 10% of HyperCore's USDC supply.[^usdc]

## Governance

HYPE holders delegate stake to validators.[^staking] Validators make
stake-weighted decisions, including market-deployer slashing and the
selection of stablecoin tickers.[^hips][^usdh] The Hyper Foundation
also operates a delegation program for validators.[^delegation]
Hyperliquid Labs leads core development.[^hyper101]

## Incidents and controversies

- **North Korea concerns (December 2024).** MetaMask researcher Taylor
  Monahan identified addresses she suspected were controlled by North
  Korean hackers. About US$250 million in net outflows followed in one
  day. Hyperliquid said it had found no exploit or loss of user
  funds.[^dprk][^dprk-followup]

- **ETH whale liquidation (March 2025).** On 12 March 2025 a trader with
  an ETH long worth about US$300 million withdrew collateral
  and unrealized profit, leaving the position just above liquidation.
  When it was liquidated HLP took it over and lost about US$4 million.
  Hyperliquid then cut maximum leverage to 40x on BTC and 25x on
  ETH.[^whale]
- **JELLY delisting (March 2025).** On 26 March 2025 validators delisted
  JELLY perpetuals after suspicious trading left HLP exposed to a large
  short position. The market was settled at US$0.0095. Hyperliquid said
  it would compensate users other than flagged addresses; critics
  argued that overriding settlement prices undermined the exchange's
  claimed decentralization.[^jelly][^validators]

- **API outage (July 2025).** On 29 July 2025 Hyperliquid's API stopped
  serving requests normally for 37 minutes, leaving traders unable to manage
  positions. Hyperliquid reimbursed affected users about US$2
  million.[^outage][^outage-refund]
- **Validator centralization (March 2025).** In its analysis of the
  JELLY intervention, Blockworks reported that five Hyper Foundation
  validators controlled more than half of the stake. This is a dated
  observation, not a measurement of the current validator set.[^validators]
- **October 2025 liquidations.** During the 10–11 October market crash,
  Hyperliquid's perpetuals open interest fell from about US$14 billion
  to US$6 billion, according to CoinDesk Research.[^oct-2025]

- **POPCAT (November 2025).** On 12 November Hyperliquid paused deposits
  and withdrawals. The Block reported an analyst's account that a trader
  had used 19 wallets and withdrawn a large POPCAT buy order, leaving
  HLP with about US$4.9 million in losses. The report described the
  manipulation explanation as speculation.[^popcat]
- **Transparency of positions.** In March 2025, 10x Research's Markus
  Thielen argued that public position data could help groups of traders
  coordinate attempts to trigger large traders' liquidations.[^whale-hunting]
- **US congressional inquiry (September 2026).** On 29 September the
  House Oversight Committee requested information from Hyperliquid Labs
  about identity checks, geographic restrictions, and suspicious trading,
  including a short position preceding an October 2025 tariff
  announcement. Hyperliquid Labs told The Block it was reviewing the
  request. The letter requested information; it was not a finding of
  wrongdoing.[^oversight][^oversight-response]

## Timeline

| Date | Event |
|---|---|
| 2023-02 | Closed alpha opens |
| 2023-11-01 | Points program begins |
| 2024 | HyperBFT replaces Tendermint |
| 2024-11-29 | HYPE token genesis; 31% allocated for the airdrop |
| 2024-12 | Researcher raises concerns about suspected North Korean-linked accounts |
| 2024-12-30 | Native HYPE staking opens |
| 2025-02-18 | HyperEVM mainnet |
| 2025-03-12 | ETH whale liquidation costs HLP about US$4M |
| 2025-03-26 | JELLY market delisted by validators |
| 2025-04-30 | HyperEVM contracts can read HyperCore state |
| 2025-07-05 | HyperEVM contracts can send actions to HyperCore |
| 2025-07-29 | API outage; later reimbursements total about US$2M |
| 2025-09-14 | USDH ticker awarded to Native Markets |
| 2025-09-16 | Native USDC launches on HyperEVM |
| 2025-10-10–11 | Open interest falls from about US$14B to US$6B during market crash |
| 2025-10-13 | Scheduled HIP-3 activation |
| 2025-11-12 | Deposits and withdrawals paused amid reported POPCAT losses |
| 2025-11-29 | Core contributor tokens begin unlocking |
| 2025-12 | Foundation proposes recognizing Assistance Fund HYPE as burned |
| 2026-05-02 | HIP-4 outcome markets live |
| 2026-05 | US spot HYPE ETPs begin trading |
| 2026-05-14 | Coinbase announces USDC treasury role and planned USDH phase-out |
| 2026-09-16 | Payward announces plans for US markets, subject to approval |
| 2026-09-29 | House Oversight Committee requests information |
| 2026-10-29 | ICE and Trade[XYZ] announce US market plan, subject to approval |

## See also

- [MetaMask](metamask.md)

- [Arbitrum](arbitrum.md)
- [Ethereum](ethereum.md)
- [Perpetual futures](perpetual-futures.md)
- [Liquidation](liquidation.md)

## References

[^overview]: Hyperliquid documentation. *HyperCore overview*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/overview>
[^hyperevm]: Hyperliquid documentation. *HyperEVM*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperevm>
[^contributors]: Hyperliquid documentation. *Core contributors*. <https://hyperliquid.gitbook.io/hyperliquid-docs/about-hyperliquid/core-contributors>
[^decrypt-explainer]: Decrypt. *What is Hyperliquid?* <https://decrypt.co/341605/what-hyperliquid-decentralized-exchange-blockchain>
[^despread]: Despread Research. *Hyperliquid: The Perpetual DEX Endgame*. <https://research.despread.io/report-hyperliquid/>
[^aster]: Decrypt (2025). *Aster vs Hyperliquid: Binance chain DEX perps volume derails the hype train*. <https://decrypt.co/341065/aster-vs-hyperliquid-binance-chain-dex-perps-volume-derails-the-hype-train>
[^points]: Hyperliquid documentation. *Points*. <https://hyperliquid.gitbook.io/hyperliquid-docs/points>
[^genesis-block]: The Block (2024). *Hyperliquid plans to launch HYPE token in Nov. 29 genesis event*. <https://www.theblock.co/post/328631/hyperliquid-plans-to-launch-hype-token-in-nov-29-genesis-event>
[^airdrop]: Blockworks (2024). *Hyperliquid could have the most valuable airdrop ever*. <https://blockworks.co/news/hyperliquid-most-valuable-airdrop>
[^unlock]: The Block (2025). *HYPE tokens unstaked for Hyperliquid Labs' first allocation*. <https://www.theblock.co/news/defi/2025-12-29-hype-tokens-unstaked-for-hyperliquid-labs-first-allocation-383880>
[^staking-launch]: The Block (2024). *HYPE token staking goes live on the Hyperliquid mainnet*. <https://www.theblock.co/post/332592/hype-token-staking-goes-live-on-the-hyperliquid-mainnet>
[^galaxy]: Galaxy Research (2025). *Hyperliquid's L1 begins to find its footing*. <https://www.galaxy.com/insights/research/hyperliquids-l1-begins-to-find-its-footing>
[^usdh]: The Block (2025). Native Markets wins USDH ticker vote. <https://www.theblock.co/news/ecosystems/2025-09-14-native-markets-team-wins-hyperliquid-usdh-stablecoin-bid-eyes-test-phase-within-days-370570>
[^circle]: Circle (2025). Circle and USDC Expansion with Hyperliquid. <https://www.circle.com/blog/circle-and-usdc-expansion-with-hyperliquid>
[^usdc]: Hyperliquid documentation. *USDC*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/usdc>
[^coinbase]: Coinbase (2026). Coinbase and Hyperliquid: Aligning Markets on Hyperliquid to USDC. <https://www.coinbase.com/blog/coinbase-and-hyperliquid-aligning-markets-on-hyperliquid-to-usdc>
[^hip3-launch]: The Block (2025). Hyperliquid to activate HIP-3 upgrade. <https://www.theblock.co/news/ecosystems/2025-10-13-hyperliquid-activate-hip-3-upgrade-374306>
[^hip3-equities]: Blockworks (2025). *HIP-3 brings equity perps to crypto*. <https://blockworks.com/news/hip-3-equity-perps>
[^hip4-launch]: The Block (2026). Hyperliquid rolls out validator-governed prediction markets. <https://www.theblock.co/news/ecosystems/2026-05-26-hyperliquid-validator-prediction-markets-402511>
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
[^delegation]: Hyperliquid documentation. *Delegation program*. <https://hyperliquid.gitbook.io/hyperliquid-docs/validators/delegation-program>
[^dprk]: The Block (2024). *Hyperliquid sees record outflows following North Korea hack concerns*. <https://www.theblock.co/post/332298/hyperliquid-sees-record-outflows-following-north-korea-hack-concerns>
[^whale]: The Block (2025). *HLP vault loss after Hyperliquid whale liquidation*. <https://www.theblock.co/post/345866/hype-drop-hlp-vault-loss-hyperliquid-whale-liquidation>
[^jelly]: Decrypt (2025). *Hyperliquid delists Solana meme coin after liquidation crisis*. <https://decrypt.co/311713/hyperliquid-delists-solana-meme-coin-liquidation-crisis>
[^outage]: The Block (2025). *Hyperliquid plans automated refunds after outage*. <https://www.theblock.co/post/364861/hyperliquid-outage-refund>
[^outage-refund]: Cointelegraph (2025). *Hyperliquid reimburses $2M to crypto traders after outage*. <https://cointelegraph.com/news/hyperliquid-reimburses-2m-crypto-traders-outage>
[^validators]: Blockworks (2025). *Hyperliquid decentralization and its validators*. <https://blockworks.com/news/hyperliquid-decentralization-validator-put>
[^oct-2025]: CoinDesk Research (2025). The $19 Billion Liquidation That Shook Crypto. <https://www.coindesk.com/research/market-spotlight-the-19-billion-liquidation-that-shook-crypto>
[^popcat]: The Block (2025). *Hyperliquid pauses deposits and withdrawals amid POPCAT trading scheme speculation*. <https://www.theblock.co/post/378606/hyperliquid-pauses-deposits-withdrawals-popcat-trading-scheme-speculation>
[^whale-hunting]: Cointelegraph (2025). *Traders targeting Hyperliquid whales' significant positions to trigger liquidations: 10x Research*. <https://cointelegraph.com/news/traders-targeting-hyperliquid-whales-significant-positions-trigger-liquidations-10x-research>
[^evm-dev]: Hyperliquid documentation. HyperEVM developer guide. <https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/hyperevm>
[^dual-blocks]: Hyperliquid documentation. Dual-block architecture. <https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/hyperevm/dual-block-architecture>
[^corewriter]: Hyperliquid documentation. Interacting with HyperCore. <https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/hyperevm/interacting-with-hypercore>
[^about]: Hyperliquid documentation. About Hyperliquid. <https://hyperliquid.gitbook.io/hyperliquid-docs/about-hyperliquid>
[^unit-docs]: Unit documentation. About Unit. <https://docs.hyperunit.xyz/>
[^payward]: Payward (2026). Payward Intends to Bring Onchain Perpetual Futures to US Clients. <https://www.payward.com/press-release/payward-hyperliquid-onchain-perpetual-futures>
[^payward-update]: The Block (2026). Hyperliquid says Kraken parent Payward to be first CFTC-regulated HIP-3 deployer. <https://www.theblock.co/news/markets/2026-10-26-hyperliquid-payward-kraken-cftc-regulated-hip-3-deployer-431787>
[^oversight]: House Oversight Committee (2026). Letter to Hyperliquid Labs, 29 September. <https://oversight.house.gov/wp-content/uploads/2026/09/Hyperliquid-Letter-9.29.26.pdf>
[^oversight-response]: The Block (2026). Comer presses Crypto.com, Hyperliquid and PredictIt on identity checks and suspicious trades. <https://www.theblock.co/news/regulation/2026-09-29-comer-presses-crypto-com-hyperliquid-predictit-identity-checks-suspicious-trades-417192>
[^dprk-followup]: CoinDesk (2026). North Korean-linked trading on Hyperliquid; background on December 2024 concerns. <https://www.coindesk.com/business/2026/08/31/north-korean-hackers-are-moving-tens-of-millions-on-hyperliquid-as-trump-pushes-to-onshore-the-crypto-platform>
[^hip1]: Hyperliquid documentation. HIP-1. <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-1-native-token-standard>
[^hip2]: Hyperliquid documentation. HIP-2. <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-2-hyperliquidity>
[^hip4]: Hyperliquid documentation. HIP-4. <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-4-outcome-markets>
[^hyper101]: Hyperliquid documentation. *Hyperliquid 101*. <https://hyperliquid.gitbook.io/hyperliquid-docs/about-hyperliquid/hyperliquid-101-for-non-crypto-audiences>
[^contracts]: Hyperliquid documentation. *Contract specifications*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/contract-specifications>
[^ice]: Intercontinental Exchange (2026). *Intercontinental Exchange and Trade[XYZ] to Bring Hyperliquid-Based Perpetual Markets Onshore*. <https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-and-TradeXYZ-to-Bring-Hyperliquid-Based-Perpetual-Markets-Onshore/default.aspx>
