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
| Outside funding | None (per Hyperliquid Labs) |
| Live data | [DefiLlama](https://defillama.com/protocol/hyperliquid), [Hyperscreener](https://hyperscreener.asxn.xyz/home) (third party) |

## History

### Founding

Hyperliquid was founded by Jeff Yan, previously a high-frequency trader,
and a pseudonymous co-founder known as iliensinc. Before Hyperliquid the
team did proprietary market making in crypto from 2020, through a firm
called Chameleon Trading.[^contributors][^coinbureau] The exchange
opened as a closed alpha in February 2023 and launched fully later that
year.[^decrypt-explainer]

### Points and token genesis

A points program for traders began on 1 November 2023.[^points] On 29
November 2024 the Hyper Foundation's token genesis event distributed 31%
of HYPE's supply to points holders, with no allocation to private
investors.[^genesis][^genesis-block] The airdrop was one of the largest
by value in crypto at the time. Core contributors' tokens were locked for
one year and began unlocking in late November 2025.[^unlock]

| Recipient | Share |
|---|---|
| Future emissions and community rewards | 38.888% |
| Genesis distribution (airdrop) | 31% |
| Core contributors | 23.8% |
| Hyper Foundation budget | 6% |
| Community grants | 0.3% |
| HIP-2 liquidity | 0.012% |

### HyperEVM, stablecoins, and builder markets

HyperEVM launched on mainnet on 18 February 2025.[^hyperevm-launch]

On 14 September 2025 validators, with about 70% of stake, voted to award
the USDH stablecoin ticker to Native Markets.[^usdh] Two days later
Circle launched native USDC on Hyperliquid, which replaced the original
bridge from [Arbitrum](arbitrum.md) as the main way USDC enters the
chain.[^circle][^usdc] On 14 May 2026 Coinbase became the official
deployer of USDC treasury on Hyperliquid, and USDH began to be phased
out.[^coinbase]

On 13 October 2025 HIP-3 went live, letting anyone who stakes 500,000
HYPE deploy their own perpetual futures markets.[^hip3-launch] On 2 May
2026 HIP-4 added outcome markets, a form of prediction
market.[^hip4-launch]

### Supply burn

The Assistance Fund converts trading fees into HYPE. In December 2025
validators voted to recognize the HYPE held by the fund as burned,
removing it from total and circulating supply.[^fees][^burn-vote]

### Exchange-traded products

In May 2026 the first US spot HYPE exchange-traded products began
trading, including 21Shares' THYP and Bitwise's BHYP.[^etf]

## Technology

HyperBFT is a Byzantine fault tolerant consensus protocol derived from
HotStuff. Validators stake HYPE.[^overview]

HyperCore keeps the full order book onchain: every order, cancellation,
trade, and liquidation is a transaction. Hyperliquid Improvement
Proposals (HIPs) define its main features:[^hips]

- **HIP-1**: a native token standard for spot assets on HyperCore.
- **HIP-2**: "Hyperliquidity", automated market making for HIP-1 tokens.
- **HIP-3**: permissionless perpetual futures markets deployed by
  builders who stake HYPE.
- **HIP-4**: outcome markets.

The **Hyperliquidity Provider (HLP)** vault is a community-owned vault
that makes markets and takes over liquidated positions. Depositors share
its profit and loss.[^hlp]

The **Assistance Fund** converts trading fees to HYPE automatically as
part of chain execution. HYPE in the fund is treated as
burned.[^fees]

USDC is issued natively on Hyperliquid through Circle's Cross-Chain
Transfer Protocol. A legacy bridge on Arbitrum, whose withdrawals are
signed by Hyperliquid's validators, holds a small and shrinking share of
USDC on HyperCore.[^usdc]

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
- **Validator centralization.** The validator set is small compared with
  other major layer 1s. In 2025 five Hyper Foundation validators held
  more than half of all stake.[^validators]
- **October 2025 liquidations.** During the market crash of 10–11
  October 2025, about US$10 billion of positions were liquidated on
  Hyperliquid, and it triggered cross-margin auto-deleveraging of
  profitable positions for the first time in over two years.[^oct-2025]

## Timeline

| Date | Event |
|---|---|
| 2023-02 | Closed alpha opens |
| 2023-11-01 | Points program begins |
| 2024-11-29 | HYPE token genesis; 31% airdropped |
| 2024-12 | North Korea-linked trading flagged |
| 2025-02-18 | HyperEVM mainnet |
| 2025-03-12 | ETH whale liquidation costs HLP about US$4M |
| 2025-03-26 | JELLY market delisted by validators |
| 2025-09-14 | USDH ticker awarded to Native Markets |
| 2025-09-16 | Native USDC launches on Hyperliquid |
| 2025-10-10 | About US$10B liquidated; auto-deleveraging triggered |
| 2025-10-13 | HIP-3 live |
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
[^coinbureau]: Coin Bureau. *Hyperliquid review*. <https://coinbureau.com/review/hyperliquid-review>
[^decrypt-explainer]: Decrypt. *What is Hyperliquid?* <https://decrypt.co/341605/what-hyperliquid-decentralized-exchange-blockchain>
[^points]: Hyperliquid documentation. *Points*. <https://hyperliquid.gitbook.io/hyperliquid-docs/points>
[^genesis]: Hyper Foundation (2024). HYPE genesis announcement, 28 November 2024. <https://x.com/HyperFND/status/1862007773191708760>
[^genesis-block]: The Block (2024). *Hyperliquid plans to launch HYPE token in Nov. 29 genesis event*. <https://www.theblock.co/post/328631/hyperliquid-plans-to-launch-hype-token-in-nov-29-genesis-event>
[^unlock]: The Block (2025). *HYPE tokens unstaked for Hyperliquid Labs' first allocation*. <https://www.theblock.co/news/defi/2025-12-29-hype-tokens-unstaked-for-hyperliquid-labs-first-allocation-383880>
[^hyperevm-launch]: The Block (2025). HyperEVM mainnet launch. <https://www.theblock.co/post/341424>
[^usdh]: The Block (2025). USDH ticker vote. <https://www.theblock.co/post/370570>
[^circle]: The Block (2025). *Circle launches USDC natively on Hyperliquid*. <https://www.theblock.co/post/370946/circle-launches-usdc-natively-on-hyperliquid>
[^usdc]: Hyperliquid documentation. *USDC*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/usdc>
[^coinbase]: The Block (2026). Coinbase becomes Hyperliquid's official USDC deployer. <https://theblock.co/post/401233/coinbase-hyperliquid-official-deployer-usdc>
[^hip3-launch]: The Block (2025). HIP-3 mainnet launch. <https://www.theblock.co/post/374306>
[^hip4-launch]: The Block (2026). HIP-4 permissionless deployment. <https://theblock.co/post/408875/hyperliquid-hip-4-permissionless-deployment>
[^fees]: Hyperliquid documentation. *Fees*. <https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees>
[^burn-vote]: The Block (2025). *Hyper Foundation proposes zeroing out Hyperliquid's assistance fund*. <https://www.theblock.co/post/383091/hyper-foundation-proposes-removing-1-billion-hype-tokens-from-circulating-supply-by-zeroing-out-hyperliquids-assistance-fund>
[^etf]: The Block (2026). *Hyperliquid ETFs see $22.3 million in early inflows*. <https://www.theblock.co/news/markets/2026-05-20-hyperliquid-etfs-22-3-million-early-inflows-analysts-point-organic-interest-402028>
[^hips]: Hyperliquid documentation. *Hyperliquid Improvement Proposals*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals>
[^hlp]: Hyperliquid documentation. *Protocol vaults*. <https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults/protocol-vaults>
[^dprk]: The Block (2024). *Hyperliquid sees record outflows following North Korea hack concerns*. <https://www.theblock.co/post/332298/hyperliquid-sees-record-outflows-following-north-korea-hack-concerns>
[^whale]: The Block (2025). *HLP vault loss after Hyperliquid whale liquidation*. <https://www.theblock.co/post/345866/hype-drop-hlp-vault-loss-hyperliquid-whale-liquidation>
[^jelly]: Decrypt (2025). *Hyperliquid delists Solana meme coin after liquidation crisis*. <https://decrypt.co/311713/hyperliquid-delists-solana-meme-coin-liquidation-crisis>
[^validators]: Blockworks (2025). *Hyperliquid decentralization and its validators*. <https://blockworks.com/news/hyperliquid-decentralization-validator-put>
[^oct-2025]: crypto.news (2025). *Hyperliquid launches HIP-3 as HYPE rebounds after $10B liquidation wave*. <https://crypto.news/hyperliquid-launches-hip-3-as-hype-rebounds-after-10b-liquidation-wave/>
