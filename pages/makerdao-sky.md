---
title: MakerDAO and Sky
ticker: SKY; formerly MKR
category: DeFi
written_by: Unknown
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# MakerDAO and Sky

Sky is the stablecoin protocol and governance ecosystem formerly known as
MakerDAO. Its products include Dai and USDS, tokens designed to track the
US dollar through collateral and protocol mechanisms. The project adopted
the Sky name in 2024 and introduced USDS and the SKY governance token as
part of that transition.[^whitepaper][^sky-token]

| | |
|---|---|
| Type | Stablecoin and collateralised lending protocol |
| Earlier name | MakerDAO |
| Stablecoins | Dai, USDS |
| Governance token | SKY; previously MKR |
| Dai–USDS converter | 1:1 in either direction[^usds] |
| Savings token | sUSDS[^savings] |

## Collateral and stablecoins

The Maker whitepaper describes Dai as a collateral-backed asset created
through the protocol rather than a claim on a single issuer's dollar bank
account. Vaults record collateral and debt, with risk parameters determining
when a position becomes subject to liquidation. USDS represents a
collateralised balance in the same core accounting system.[^whitepaper]

Sky's USDS documentation specifies an ERC-20 token with an upgradeable
implementation and a converter between Dai and USDS. Conversion at a
fixed protocol ratio is distinct from a guarantee that either token always
trades at one dollar on external markets.[^usds][^whitepaper]

The liquidation system sells collateral to cover unsafe debt. Its
Liquidation 2.0 design uses declining-price auctions with immediate
settlement, replacing the earlier arrangement in which bids tied up
capital until an auction ended or a bidder was outbid.[^liquidation]

## Sky transition and governance

The September 2024 launch proposals specified USDS, savings USDS, and SKY,
including a Dai–USDS converter and an initial ratio of 24,000 SKY per MKR.
These proposals are historical records of the transition, not a statement
of every conversion condition today.[^launch]

Sky's August 2026 explanation says SKY has replaced MKR for governance
and describes a delayed-upgrade penalty affecting late MKR conversions.
The technical governance documentation identifies voting, delayed
execution, and one-time executable proposals as distinct components.
Holders' voting power therefore interacts with contracts that implement
the approved changes.[^sky-token][^governance]

Sky.money describes the Sky Savings Rate as variable and funded from
aggregate protocol surplus. sUSDS represents participation in that savings
mechanism; it is not a fixed-rate promise or exposure to one specific
collateral position.[^savings]

## Incidents and risks

During the March 2020 market crash, network congestion and high gas costs
interfered with oracle updates and liquidation bidding. A subsequent Maker
governance poll recorded auctions clearing for zero Dai or far below market
value, losses to vault holders, and recapitalisation of protocol losses.
The poll discussed compensation; its existence alone does not establish
that a compensation programme was implemented.[^black-thursday]

## Timeline

| Date | Event |
|---|---|
| 2020-03 | Market crash disrupts liquidations[^black-thursday] |
| 2024-09-09 | Sky token and product launch parameters proposed[^launch] |
| 2026-08-18 | Sky publishes explanation of completed governance-token transition[^sky-token] |

## See also

- [Stablecoin](stablecoin.md)
- [USDC](usdc.md)
- [Aave](aave.md)
- [Blockchain oracle](blockchain-oracle.md)

## References

[^whitepaper]: Maker/Sky. *Whitepaper*. <https://makerdao.com/da/whitepaper/>
[^usds]: Sky Protocol documentation. *USDS*. <https://developers.skyeco.com/protocol/tokens/usds/>
[^liquidation]: Sky Protocol documentation. *Collateral liquidation*. <https://developers.skyeco.com/protocol/vaults/collateral-liquidation/>
[^launch]: Maker Governance (9 September 2024). *Sky Protocol Launch Season — token and product launch parameter proposal*. <https://vote.makerdao.com/polling/QmTySKwi>
[^sky-token]: Sky.money (18 August 2026). *Understanding the SKY token*. <https://sky.money/blog/understanding-the-sky-token>
[^governance]: Sky Protocol documentation. *Governance overview*. <https://developers.skyeco.com/protocol/governance/ovreview/>
[^savings]: Sky.money. *Sky Savings Rate and product descriptions*. <https://sky.money/>
[^black-thursday]: Maker Governance (6 April 2020). *Vault compensation poll*. <https://vote.makerdao.com/polling/QmWC4qey>
