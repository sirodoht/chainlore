---
title: Ethena
ticker: ENA
category: DeFi
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Ethena

Ethena is the protocol behind USDe, a token designed to track the dollar
using backing assets and hedging strategies. Ethena calls USDe a synthetic
dollar and distinguishes it from fiat-backed stablecoins such as
[USDC](usdc.md) and [Tether](tether.md). Its related tokens include sUSDe,
which represents staked USDe, and ENA, its governance token.[^overview][^ena]

| | |
|---|---|
| Type | Synthetic-dollar protocol |
| Dollar token | USDe |
| Staked dollar token | sUSDe |
| Governance token | ENA |
| Public USDe launch | February 2024, according to Ethena[^launch] |
| Direct minting and redemption | Approved counterparties, subject to checks[^overview] |

## Backing and hedging

Ethena's technical explanation describes matching volatile backing assets
with short futures positions of approximately equal notional value. The
intention is for gains on one side to offset losses on the other, limiting
exposure to the asset's price direction. Stable backing assets do not
require the same hedge. A dollar target is therefore supported by portfolio
management and market infrastructure rather than solely by cash reserves.[^mechanism]

As of 31 October 2026, Ethena's overview describes a wider range of revenue
strategies, including crypto and non-crypto basis trades, lending, and
tokenised real-world assets. These are the protocol's descriptions of its
permitted approach; they should not be read as an independently verified
statement of current portfolio weights.[^overview]

## Access and sUSDe

The protocol distinguishes trading USDe in secondary markets from direct
minting and redemption by approved counterparties. This distinction matters
when comparing the market price available to a holder with the protocol's
mint-and-redeem mechanism.[^overview]

Users staking USDe receive sUSDe. Ethena describes rewards as discretionary:
distributions increase the USDe value represented by each sUSDe token.
Its documentation says periods of negative protocol revenue can result in
no reward distribution, with the reserve fund intended to absorb losses.
That intended buffer is not a guarantee of a fixed return or of
loss-free backing.[^rewards]

## Governance and risks

Ethena documents ENA as the token governing parameters including backing
composition, new strategies, future revenue allocation, and the membership
and remit of the Risk Committee. ENA and sUSDe therefore represent different
roles within the system.[^ena]

An October 2026 governance update reported approval of a fee-switch
proposal linking ENA buybacks to USDe supply milestones. Activation was
conditional on a 14-day average USDe supply of at least $7.5 billion;
approval alone did not establish that this threshold had been met.[^q3]

The protocol's risk documentation lists funding, liquidation, custody,
exchange failure, and backing-asset risks. It specifically acknowledges
that negative perpetual-futures funding can require Ethena to pay rather
than receive funding. A hedge against price direction does not remove
those operating costs or dependencies.[^risks][^funding]

Following Binance's disclosure of the 29 October 2026 hot-wallet breach,
AMBCrypto and TokenPost reported Ethena's statement that its unrealised
profit-and-loss exposure to Binance was about $8.8 million. This was
reported exposure, not a confirmed loss. Ethena's risk documentation says
its backing assets remain with off-exchange custodians, while unsettled
profit and loss creates exposure to an exchange failure.[^binance-incident][^binance-exposure][^tokenpost][^exchange-risk]

## See also

- [Stablecoin](stablecoin.md)
- [MakerDAO and Sky](makerdao-sky.md)
- [Curve](curve.md)
- [Hyperliquid](hyperliquid.md)
- [Perpetual futures](perpetual-futures.md)

## References

[^overview]: Ethena. *Ethena overview*. <https://docs.ethena.fi/overview/ethena-overview.md>
[^mechanism]: Ethena. *How USDe works*. <https://docs.ethena.fi/overview/how-usde-works.md>
[^launch]: Ethena. *Website, Introducing Ethena Pay summary*. <https://ethena.fi/>
[^rewards]: Ethena. *Rewards mechanism*. <https://docs.ethena.fi/protocol-overview/rewards-mechanism.md>
[^ena]: Ethena. *ENA*. <https://docs.ethena.fi/overview/ena.md>
[^risks]: Ethena. *Risks*. <https://docs.ethena.fi/protocol-overview/risks.md>
[^funding]: Ethena. *Funding risk*. <https://docs.ethena.fi/protocol-overview/risks/funding-risk.md>
[^q3]: Blockworks Advisory (13 October 2026). *Ethena's July–September 2026 governance update*. Ethena governance forum. <https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857>
[^binance-incident]: Binance (30 October 2026). *Security incident update*. <https://www.binance.com/en/support/announcement/detail/d3306d9dca5243548c813b605e1d1751>
[^binance-exposure]: Njiri, B. (30 October 2026). *'Our collateral resides off-exchange': Ethena downplays $8.8M Binance exposure*. AMBCrypto. <https://ambcrypto.com/our-collateral-resides-off-exchange-ethena-downplays-8-8m-binance-exposure/>
[^tokenpost]: Kim, J. (30 October 2026). *Ethena puts USDe's unrealized Binance exposure at $8.8 million*. TokenPost. <https://www.tokenpost.com/news/business/45230>
[^exchange-risk]: Ethena. *Exchange failure risk*. <https://docs.ethena.fi/protocol-overview/risks/exchange-failure-risk>
