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
execution environments that share one consensus: **HyperCore**, which
runs the order books, margining, and liquidations, and **HyperEVM**, a
general-purpose EVM chain. Its native token is **HYPE**. Hyperliquid was
built by Hyperliquid Labs, which states it took no outside venture
funding.[^docs]

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
| HYPE total supply | 1,000,000,000 |
| Margin collateral | USDC, bridged from [Arbitrum](arbitrum.md) |
| Outside funding | None (per Hyperliquid Labs) |
| Live data | [Hyperliquid stats](https://stats.hyperliquid.xyz), [DefiLlama](https://defillama.com) |

## History

### Founding

Hyperliquid was founded by Jeff Yan, previously a high-frequency trader,
and a pseudonymous co-founder known as iliensinc. Before Hyperliquid the
team ran a crypto market-making firm, Chameleon Trading. The exchange
launched in 2023.

### Points and token genesis

A points program for traders began in November 2023. On 29 November
2024 the token genesis event distributed 31% of HYPE's supply to points
holders, with no allocation to private investors.[^tokenomics] The
airdrop was one of the largest by value in crypto at the time.

| Recipient | Share |
|---|---|
| Future emissions and community rewards | 38.888% |
| Genesis distribution (airdrop) | 31% |
| Core contributors | 23.8% |
| Hyper Foundation budget | 6% |
| Community grants | 0.3% |
| HIP-2 liquidity | 0.012% |

### HyperEVM and builder markets

HyperEVM launched on mainnet in February 2025. In September 2025
validators voted to award the USDH stablecoin ticker to Native Markets.
In October 2025 HIP-3 went live, letting anyone who stakes enough HYPE
deploy their own perpetual futures markets on HyperCore.

## Technology

HyperBFT is a Byzantine fault tolerant consensus protocol derived from
HotStuff. Validators stake HYPE.

HyperCore keeps the full order book onchain: every order, cancellation,
trade, and liquidation is a transaction. Hyperliquid Improvement
Proposals (HIPs) define its main features:[^docs]

- **HIP-1**: a native token standard for spot assets on HyperCore.
- **HIP-2**: "Hyperliquidity", automated market making for HIP-1 tokens.
- **HIP-3**: permissionless perpetual futures markets deployed by
  builders who stake HYPE.

The **Hyperliquidity Provider (HLP)** vault is a community-owned vault
that makes markets and takes over liquidated positions. Depositors share
its profit and loss.

The **Assistance Fund** receives trading fees and uses them to buy HYPE
on the market.

Users deposit USDC through a bridge contract on Arbitrum. Withdrawals
are signed by Hyperliquid's validators.

## Incidents and controversies

- **North Korea concerns (December 2024).** Security researchers flagged
  addresses linked to North Korean hackers trading on the platform. The
  team said no exploit had occurred.
- **ETH whale liquidation (March 2025).** On 12 March 2025 a trader
  closed a highly leveraged ETH long in a way that pushed losses onto
  HLP, costing the vault about US$4 million. Hyperliquid then lowered
  maximum leverage on BTC and ETH.
- **JELLY delisting (March 2025).** On 26 March 2025 a trader
  manipulated the price of the thinly traded JELLYJELLY token and left
  HLP holding a large short. Validators delisted the market and settled
  it at a price favourable to HLP. Critics said the intervention showed
  that a small validator set could override market outcomes.
- **Validator centralization.** The validator set is small compared with
  other major layer 1s, and the Hyper Foundation has held a large share
  of stake.
- **October 2025 liquidations.** During the market crash of 10–11
  October 2025, Hyperliquid processed record liquidations and triggered
  auto-deleveraging of profitable positions.

## Timeline

| Date | Event |
|---|---|
| 2023 | Exchange launches |
| 2023-11 | Points program begins |
| 2024-11-29 | HYPE token genesis; 31% airdropped |
| 2024-12 | North Korea-linked trading flagged |
| 2025-02 | HyperEVM mainnet |
| 2025-03-12 | ETH whale liquidation costs HLP about US$4M |
| 2025-03-26 | JELLY market delisted by validators |
| 2025-09 | USDH ticker awarded to Native Markets |
| 2025-10 | HIP-3 live; record liquidations on 10–11 October |

## See also

- [Arbitrum](arbitrum.md)
- [Ethereum](ethereum.md)

## References

[^docs]: Hyperliquid documentation. <https://hyperliquid.gitbook.io/hyperliquid-docs>
[^tokenomics]: Hyperliquid Labs. *HYPE genesis announcement*, 29 November 2024. Allocation also in the Hyperliquid documentation. <https://hyperliquid.gitbook.io/hyperliquid-docs>
