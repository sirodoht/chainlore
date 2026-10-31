---
title: Curve
ticker: CRV
category: DeFi
written_by: Unknown
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Curve

Curve is a decentralised exchange protocol using automated market makers
for stablecoins and other assets. Its StableSwap design concentrates
liquidity around the relative prices expected for closely related assets.
Curve also develops crvUSD and the Llamalend lending system, and its
governance uses locked CRV tokens.[^paper][^intro][^vecrv]

| | |
|---|---|
| Type | Exchange and lending protocol |
| StableSwap paper author | Michael Egorov |
| StableSwap paper | 2019-11-10 |
| Governance token | CRV |
| Voting balance | veCRV |
| Stablecoin | crvUSD |

## StableSwap

Egorov's November 2019 paper describes a pricing rule between constant-sum
and constant-product market makers. Near balanced reserves, the curve is
relatively flat, allowing trades with low price impact. As reserves become
more imbalanced, pricing moves toward constant-product behaviour. An
amplification parameter controls that relationship.[^paper]

This design targets liquidity efficiency around an expected price
relationship. It does not establish that a stablecoin remains redeemable
or that two assets must keep the same value. Curve's broader exchange
documentation also covers volatile-asset markets.[^paper][^intro]

On 29 October 2026, Curve announced StableSwap on Stellar mainnet,
describing it as its first deployment outside the Ethereum Virtual
Machine ecosystem. The implementation uses Stellar's Soroban contracts;
the initial web interface was released as a beta.[^stellar]

## Lending and crvUSD

Curve describes crvUSD as a collateralised-debt stablecoin and Llamalend
as a permissionless lending protocol. Both use LLAMMA, which converts
collateral progressively across price bands. Its documentation cautions
that these conversions can incur losses and still lead to full
liquidation; gradual conversion does not eliminate borrower risk.[^intro]

## Governance

Users obtain veCRV voting power by locking CRV for a chosen period, up to
four years. veCRV is not transferable and declines as the lock approaches
expiry. It provides voting power, participation in fee distribution, and
potential boosts to liquidity incentives.[^vecrv]

Gauge-weight votes determine where CRV emissions are distributed. The
governance documentation distinguishes these votes from broader proposals
to change the protocol. For deployments on other EVM networks, governance
decisions can originate on Ethereum and be communicated across chains.[^governance]

## Incidents

Curve pools were exploited in July 2023. A December governance proposal
identified alETH/ETH, pETH/ETH, msETH/ETH, and CRV/ETH as affected pools and
proposed vesting CRV from the community fund to compensate liquidity
providers. It expressly noted that CRV price changes meant the proposed
distribution could not guarantee full compensation in dollar terms.[^compensation]

Curve reported that its curve.fi domain was hijacked on 12 May 2025,
redirecting visitors to a page soliciting wallet signatures. In its
postmortem, the team said the protocol contracts remained operational and
described moving access to curve.finance. This was a website-domain
incident, distinct from a change to the onchain contracts.[^domain]

## Timeline

| Date | Event |
|---|---|
| 2019-11-10 | StableSwap paper dated[^paper] |
| 2020 | veCRV governance model launches[^vecrv] |
| 2023-07 | Several Curve pools exploited[^compensation] |
| 2023-12-17 | Compensation proposal published[^compensation] |
| 2025-05-12 | curve.fi domain hijacked[^domain] |
| 2026-10-29 | Curve announces StableSwap on Stellar mainnet[^stellar] |

## See also

- [Uniswap](uniswap.md)
- [Stablecoin](stablecoin.md)
- [Lido](lido.md)
- [Aave](aave.md)

## References

[^paper]: Egorov, M. (10 November 2019). *StableSwap — efficient mechanism for stablecoin liquidity*. <https://curve.fi/files/stableswap-paper.pdf>
[^intro]: Curve. *What is Curve?* <https://docs.curve.finance/user/introduction>
[^vecrv]: Curve. *What is veCRV?* <https://docs.curve.finance/user/vecrv/what-is-vecrv>
[^governance]: Curve. *DAO and governance overview*. <https://docs.curve.finance/user/dao/overview>
[^compensation]: Curve governance forum (17 December 2023). *Proposal to recompensate LPs affected by Curve pool exploit*. <https://gov.curve.finance/t/proposal-to-recompensate-lps-affected-by-curve-pool-exploit/9825/>
[^domain]: Curve (19 May 2025). *Curve domain incident*. <https://news.curve.finance/curve-domain-incident/>
[^stellar]: Curve (29 October 2026). *Curve is live on Stellar*. <https://news.curve.finance/curve-is-live-on-stellar/>
