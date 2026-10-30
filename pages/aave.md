---
title: Aave
ticker: AAVE
category: DeFi
status: ai-fact-checked
checked: 2026-10-30
checked_by: Opus 5.5 High
updated: 2026-10-30
---

# Aave

**Aave** is a decentralised lending protocol. Users supply crypto assets
to shared pools to earn interest, and borrow from those pools against
collateral worth more than the loan; positions whose health factor falls
below 1 can be liquidated.[^v3-docs] It grew out of ETHLend, a
peer-to-peer lending platform founded by Stani Kulechov, and is
governed by the Aave DAO, whose members vote with the AAVE
token.[^aci-2020][^ethlend-ico][^governance-docs]

| | |
|---|---|
| Type | Lending protocol |
| Founder | Stani Kulechov |
| Developer | Aave Labs |
| Predecessor | ETHLend (2017) |
| Launch | 2020-01-09 (Aave Protocol v1, Ethereum) |
| Current versions | V3 (2022), V4 (2026) |
| Governance token | AAVE (ERC-20), migrated from LEND at 100 LEND per AAVE |
| Total AAVE supply | 16,000,000 |
| Stablecoin | GHO |
| Governance | Aave DAO |
| Live data | [DefiLlama](https://defillama.com/protocol/aave), [Aave app](https://app.aave.com), [Aave governance forum](https://governance.aave.com), [Etherscan](https://etherscan.io/token/0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9) |

## History

### ETHLend

Stani Kulechov holds a Master of Laws degree from the University of
Helsinki.[^kulechov] He founded ETHLend, which by late 2017 let borrowers
lock ERC-20 tokens as collateral and borrow Ether from individual
lenders. Its LEND token was sold in a presale that reached a 2,000 ETH
cap in September 2017 and a public sale that began on 25 November 2017;
Finance Magnates reported that the public sale raised US$10 million
in its first half-hour.[^ethlend-ico]

In September 2018 Aave was established as the parent company of
ETHLend. When the Aave Protocol launched, ETHLend stopped taking new
loans and stayed open only so that existing users could close their
positions.[^aci-2020]

### Aave Protocol v1 and flash loans

The Aave Protocol launched on Ethereum on 9 January 2020. Instead of
matching individual lenders and borrowers, it pooled deposits into
reserves that borrowers drew from. It also offered flash loans,
which need no collateral.[^aci-2020] A flash loan must be
repaid, with a fee, before the transaction ends; otherwise the whole
transaction is reverted.[^flash-docs]

### Token migration and V2

On 2 October 2020 LEND holders began migrating to a new token, AAVE, at
100 LEND per AAVE. The total supply of AAVE was set at 16 million: 13
million for the migration and 3 million for an Aave Ecosystem Reserve
controlled by governance.[^migration] The migration contract
stayed open until the 2025 Aavenomics proposal moved to close it,
reclaiming about 320,000 unclaimed AAVE.[^aavenomics-block]

Version 2 launched in early December 2020. It represented debts as
tokens, which allowed native credit delegation (lending one's borrowing
power to another address), and let users trade collateral or repay loans
with it. It added batch flash loans and a reserve factor that directs
part of borrowers' interest to the DAO. A planned flash-loan-based tool
was to let users move from V1 to V2 without closing positions.[^v2]

### V3

The Aave Companies launched V3 on 16 March 2022 on six networks, with
Ethereum to follow later. Its main additions were Portals, efficiency
mode and isolation mode (see [Technology](#technology)).[^v3-launch]

On 5 January 2022 Aave had launched Aave Arc, a permissioned version of
the protocol for institutions. Fireblocks was the first "whitelister",
vetting participants under know-your-customer checks, and approved 30
institutions at launch.[^arc]

### Lens Protocol

On 18 May 2022 Aave launched Lens Protocol, a social graph on Polygon in
which profiles and content are held as NFTs in users' wallets, so that
any app can build on them.[^lens-launch] On 20 January 2026 Lens
announced that Mask Network would take over its
stewardship.[^lens-mask]

### GHO

GHO, a US dollar stablecoin, went live on Ethereum on 15 July 2023
after a DAO vote. Users mint it by borrowing against collateral they
have supplied to Aave, and the interest it earns goes to the DAO
treasury.[^gho-block] Contracts approved by governance, called
facilitators, can mint and burn GHO up to a cap that governance sets for
each one.[^gho-docs]

### Horizon

Aave Labs launched Horizon on 26 August 2025. It is a separate,
licensed instance of the protocol, forked from V3.3, in which qualified
institutions borrow stablecoins against tokenised real-world assets.
Only holders approved by the issuers of those assets can supply them,
but anyone can supply the USDC, RLUSD and GHO that is lent out.
Launch collateral came from Superstate and Centrifuge.[^horizon-blog][^horizon-docs]

### Aavenomics and buybacks

In March 2025 Marc Zeller of the Aave Chan Initiative (ACI), a
governance service provider, proposed "Aavenomics". Its main parts were
weekly AAVE buybacks run by a new Aave Finance Committee, a new
bad-debt backstop called Umbrella, and directing some GHO revenue to
AAVE stakers.[^aavenomics-block] On 9 April 2025 token holders approved
a first US$4 million of buybacks, with over 99% in
favour.[^buyback-ct] Aave's documentation describes the later
programme as having a US$50 million annual budget. The tokens it buys
go to the Ecosystem Reserve rather than being burned.[^token-docs]
TokenLogic proposed on 22 April 2026 to pause the buybacks, which had
stopped on 19 April after the rsETH incident (see
[below](#incidents-and-controversies)).[^buyback-pause]

### V4

Aave V4 went live on Ethereum on 30 March 2026 after an Aave Labs
proposal passed a Snapshot vote and an on-chain AIP. It launched with
three liquidity hubs (Core, Prime and Plus), conservative caps, and a
Protocol Security Council able to pause and freeze markets while the
code hardened. Audits were by Trail of Bits, Blackthorn and
ChainSecurity.[^v4-activation] Aave Labs reported more than US$100
million in V4 deposits by May 2026.[^al-may]

### Deployments

Aave runs as separate instances on many networks. When the protocol
froze markets on 29 October 2026, the freeze covered V3 reserves on 16
networks and V4 reserves on four.[^binance-response] Some smaller
instances have been retired, such as V3 on Scroll in April
2026.[^al-april] The AAVE token itself is bridged to Arbitrum, Base,
Optimism and Polygon.[^token-docs]

## Technology

In V3, suppliers receive aTokens, interest-bearing tokens whose balance
grows as borrowers pay interest. Borrowers' debts are tracked with debt
tokens. Interest rates follow utilisation, the share of a pool that is
lent out: they rise slowly up to an optimal point and steeply above it.
A position whose health factor (collateral value against debt) falls
below 1 can be partly repaid by a liquidator, who receives collateral
at a discount.[^v3-docs] V3 sets the flash loan fee at 0.05% at
deployment, adjustable by governance.[^flash-docs]

V3 introduced three features:

- Efficiency mode (eMode) gives a higher loan-to-value ratio when
  collateral and debt are in the same category of correlated assets,
  such as dollar stablecoins.[^v3-docs] CoinDesk reported loan-to-value
  ratios of up to 98% in some cases at launch.[^v3-launch]
- Isolation mode let governance list riskier assets as collateral under
  a debt ceiling and limited what could be borrowed against them. V3.7
  removed it, replacing it with isolated eMode categories, in which only
  that category's collateral counts.[^v3-docs]
- Portals let approved bridges burn aTokens on one network and mint
  them on another.[^v3-launch]

V4 replaces separate pools with a hub-and-spoke design. Liquidity hubs
hold shared liquidity and give each spoke a limit for borrowing and
supplying. Spokes are the modules users deal with; each sets its own
risk parameters and can be added or removed without moving liquidity.
Borrowers pay a risk premium based on the quality of their collateral.
Liquidators repay only enough debt to bring a position back to a target
health factor, and their bonus grows as the health factor
falls.[^v4-docs]

### Safety Module and Umbrella

By mid-October 2020, AAVE holders could stake in the Safety Module
and earn AAVE rewards. Once the module was activated, up to 30% of the
staked assets could be used to cover a shortfall in the protocol.[^migration] Umbrella,
proposed by BGD Labs in March 2025, lets users stake aTokens and GHO
instead. If a pool has bad debt in an asset, stakes in that asset are
burned automatically to cover it, without a governance
vote.[^umbrella-arfc][^umbrella-docs] Umbrella is live on Ethereum for
USDC, USDT, WETH and GHO and is gradually replacing the Safety Module.
Staked AAVE stays active during the transition, and its slashing is to
be disabled once Umbrella is large enough.[^umbrella-docs]

## Governance

Holders of AAVE, staked AAVE (stkAAVE) and supplied AAVE (aAAVE) can
vote or delegate. Ethereum holds voting power, but voting can take place
on lower-cost networks such as Polygon and Avalanche. In the standard
process, a proposal is discussed on the forum as an Aave Request for
Comments (ARFC), passes a binding Snapshot vote, and is then submitted
on-chain as an Aave Improvement Proposal (AIP). Most AIPs use a short
executor with a 1-day timelock. Changes to the token or to governance
itself use a long executor with a 10-day vote and a 7-day
timelock.[^governance-docs]

Routine changes are made by stewards: service providers given limited
powers to adjust parameters such as caps and interest rates without a
full vote.[^governance-docs] Separate guardian multisigs can freeze
markets in emergencies.[^binance-response]

Much of the DAO's work is done by paid service providers. Gauntlet
managed risk from 2020 until February 2024, when its co-founder John
Morrow said it could no longer work with the DAO because of
"inconsistent guidelines and unwritten objectives" among large
stakeholders. Zeller said the ACI still supported having two risk
providers, and argued that Gauntlet was using the dispute to justify
seeking other business.[^gauntlet] Chaos Labs, a risk manager since
November 2022,[^chaos-decrypt] announced on 6 April 2026 that it was
leaving. It cited departing contributors, V4's wider risk scope, and
three years of running the engagement at a loss. Kulechov replied that
the DAO had declined Chaos Labs' requests to be the sole risk provider
and to expand its oracle role, though it had been willing to roughly
double the budget.[^chaos-forum] As of October 2026 Aave's documentation
names LlamaRisk as the risk service provider and Aave Labs as the
technical service provider.[^governance-docs]

## Incidents and controversies

- CRV short attempt (November 2022). Avraham Eisenberg, who had
  earlier exploited Mango Markets, borrowed tens of millions of CRV on
  Aave against USDC collateral. Blockchain analysts read this as an
  attempt to short the token. CRV's price then rose sharply, and his
  position was liquidated, leaving Aave with about US$1.6 million of
  bad debt.[^crv-coindesk][^crv-decrypt] Llama and Gauntlet
  proposed covering it from Gauntlet's insolvency fund and the
  treasury.[^crv-block]
- wstETH oracle error (March 2026). On 10 March 2026 a mismatch between
  two settings in the CAPO oracle, which caps the price reported for
  wstETH, priced it about 2.85% below the market rate. About 10,938
  wstETH across 34 accounts on Ethereum Core and Prime was wrongly
  liquidated. Chaos Labs, which wrote the post-mortem, said no bad debt
  arose.[^capo-block] An AIP to refund users from the treasury was
  executed in late March.[^capo-reimb]
- rsETH exploit (April 2026). On 18 April 2026 an attacker forged a
  message on Kelp's LayerZero bridge, releasing 116,500 unbacked rsETH.
  The attacker deposited 89,567 rsETH on Aave and borrowed against it.
  Aave's contracts were not compromised. Guardians froze rsETH and then
  WETH on several markets, and service providers modelled bad debt of
  about US$124 million to US$230 million.[^rseth-report] TokenLogic
  proposed that the treasury contribute 25,000 ETH, alongside
  donations and a credit facility from Mantle, in a "DeFi United"
  recovery effort.[^rseth-funding] The attacker's positions were
  liquidated on 6 May 2026. By 10 May WETH had been unfrozen on all
  active markets, with rsETH still frozen as a
  precaution.[^weth-unfreeze][^al-may]
- Binance hot wallet hack (October 2026). Binance said a hack on 29
  October 2026 affected about US$6.3 billion in assets.[^binance-ct] A
  wallet linked to the attacker supplied 60 million USDT to Aave and
  borrowed 19,762 WETH. Guardian multisigs then froze 175 V3 reserves
  on 16 networks and 117 V4 reserves on four networks; Horizon stayed
  open. LlamaRisk said the position was over-collateralised and did not
  put suppliers at risk.[^binance-response] As supplier withdrawals
  pushed the largest stablecoin pools to 92–100% utilisation, LlamaRisk
  proposed temporary cuts to their Slope2 interest-rate parameter[^binance-caps]
  and lower borrow and draw caps ahead of a staged unfreeze.[^binance-draw]
  As of 30 October 2026 the markets remain frozen.[^binance-response]
- Aave Labs and the DAO (2025–2026). In December 2025 a delegate found
  that fees from a new CoW Swap integration in Aave Labs' interface went
  to Aave Labs rather than the DAO. Zeller said Aave Labs, "in the
  pursuit of their own monetization", had redirected Aave user volume to
  competitors. Aave Labs said the interface it operated sat entirely outside
  the protocol the DAO stewards, and that the DAO governed the protocol's
  smart contracts.[^cow-forum][^cow-tl] Aave Labs then put to a Snapshot
  vote a proposal, written by Ernesto Boado of BGD Labs, to move the
  brand's domains, social accounts and code repositories under DAO
  control.
  Boado said it had been submitted without his knowledge; Aave Labs said
  the rules did not require his permission.[^brand-block] The vote
  failed, with over 55% against and over 41%
  abstaining.[^brand-ct]
- Funding dispute and departures (2026). In February 2026 Aave Labs
  proposed the "Aave Will Win" framework. It would send all revenue from
  Aave-branded products to the DAO, make V4 the core of the protocol,
  create a foundation to hold the trademarks, and fund Aave Labs. The
  temperature check passed on 1 March with 52.58% in favour. Zeller
  argued that without votes from addresses linked to Aave Labs it would
  have failed.[^aww-temp] On 12 April 2026 the DAO approved US$25
  million and 75,000 AAVE for Aave Labs, with about 75%
  support.[^aww-funding] BGD Labs, which had maintained V3, left on 1
  April 2026, objecting to plans to deprecate V3.[^bgd] The ACI said on
  3 March 2026 that it would wind down over four months, arguing that
  Labs-linked addresses had voted on their own budget.[^aci-exit]

## Timeline

| Date | Event |
|---|---|
| 2017-11-25 | ETHLend public LEND token sale begins |
| 2018-09 | Aave established as parent of ETHLend |
| 2020-01-09 | Aave Protocol v1 launches on Ethereum with flash loans |
| 2020-10-02 | LEND to AAVE migration begins |
| 2020-12 | Aave V2 launches |
| 2022-01-05 | Aave Arc launches |
| 2022-03-16 | Aave V3 launches on six networks |
| 2022-05-18 | Lens Protocol launches on Polygon |
| 2022-11-22 | CRV short attempt leaves bad debt |
| 2023-07-15 | GHO goes live on Ethereum |
| 2024-02-21 | Gauntlet announces departure |
| 2025-03-04 | Aavenomics proposal published |
| 2025-04-09 | First AAVE buyback approved |
| 2025-08-26 | Horizon launches |
| 2025-12 | CoW Swap fee dispute; brand-ownership vote fails |
| 2026-01-20 | Lens stewardship passes to Mask Network |
| 2026-02-20 | BGD Labs announces departure |
| 2026-03-01 | "Aave Will Win" temperature check passes |
| 2026-03-03 | ACI announces departure |
| 2026-03-10 | wstETH CAPO oracle error |
| 2026-03-30 | Aave V4 live on Ethereum |
| 2026-04-06 | Chaos Labs announces departure |
| 2026-04-12 | DAO approves Aave Labs funding |
| 2026-04-18 | rsETH exploit; rsETH markets frozen |
| 2026-05-10 | WETH unfreeze completed |
| 2026-10-29 | Markets frozen after Binance hack |

## See also

- [Ethereum](ethereum.md)
- [Arbitrum](arbitrum.md), whose Security Council froze ETH from the rsETH exploit
- [Uniswap](uniswap.md)
- [Lido](lido.md), issuer of the wstETH involved in the March 2026 oracle error
- [USDC](usdc.md) and [Tether](tether.md)

## References

[^kulechov]: The Block. *Stani Kulechov* (profile). <https://www.theblock.co/profile/350181/stani-kulechov>
[^ethlend-ico]: Finance Magnates (2017). *ETHLend's LEND token raises over $10 million in 30 minutes*. <https://www.financemagnates.com/thought-leadership/ethlends-lend-token-raises-10-million-30-minutes/>
[^aci-2020]: Alternative Credit Investor (2020). *ETHLend winds down loanbook in favour of Aave 'flash loans'*. <https://alternativecreditinvestor.com/2020/01/22/ethlend-winds-down-loanbook-in-favour-of-aave-flash-loans/>
[^flash-docs]: Aave documentation. *Aave V3 flash loans*. <https://aave.com/docs/aave-v3/guides/flash-loans>
[^migration]: Eichholz, L. (2020). *AAVE token: an analysis of migration and staking*. Glassnode. <https://research.glassnode.com/aave-token-analysis-migration-staking/>
[^aavenomics-block]: The Block (2025). *Aave contributor presents 'most important proposal in our history,' token price jumps 8%*. <https://www.theblock.co/post/344488/aave-contributor-presents-most-important-proposal-in-our-history-token-price-jumps-8>
[^v2]: Cointelegraph (2020). *DeFi project Aave unlocks collateral with version 2 release*. <https://cointelegraph.com/news/defi-project-aave-unlocks-collateral-with-version-2-release>
[^v3-launch]: CoinDesk (2022). *DeFi platform Aave launches V3 with cross-chain swaps front and center*. <https://coindesk.com/tech/2022/03/16/defi-platform-aave-lauches-v3-with-cross-chain-swaps-front-and-center/>
[^v3-docs]: Aave documentation. *Aave V3 overview*. <https://aave.com/docs/aave-v3/overview>
[^arc]: The Block (2022). *Aave launches permissioned DeFi platform Aave Arc, Fireblocks becomes first whitelister*. <https://www.theblock.co/post/129277/aave-arc-permissioned-defi-platform-fireblocks-first-whitelister>
[^lens-launch]: Decrypt (2022). *Aave launches decentralized, NFT-based Twitter rival on Polygon*. <https://decrypt.co/100764/aave-launches-decentralized-nft-based-twitter-rival-on-polygon>
[^lens-mask]: The Block (2026). *Mask Network takes over Lens Protocol with goal to build 'products people actually use'*. <https://www.theblock.co/post/386293/mask-network-takes-over-lens-protocol-with-goal-to-build-products-people-actually-use>
[^gho-block]: The Block (2023). *Aave DAO deploys GHO stablecoin on Ethereum mainnet*. <https://www.theblock.co/post/239688/aave-dao-deploys-gho-stablecoin-on-ethereum-mainnet>
[^gho-docs]: Aave documentation. *GHO stablecoin*. <https://aave.com/docs/ecosystem/gho>
[^horizon-blog]: Aave Labs (2025). *Aave Horizon launches*. <https://aave.com/blog/horizon-launch>
[^horizon-docs]: Aave documentation. *Aave Horizon RWA market*. <https://aave.com/docs/aave-v3/horizon>
[^buyback-ct]: Cointelegraph (2025). *AAVE soars 13% as buyback proposal passes among tokenholders*. <https://cointelegraph.com/news/aave-buyback-proposal-passes-among-holders>
[^token-docs]: Aave documentation. *AAVE token*. <https://aave.com/docs/ecosystem/aave>
[^buyback-pause]: TokenLogic (2026). *[ARFC] Pause AAVE buybacks*. Aave governance forum. <https://governance.aave.com/t/arfc-pause-aave-buybacks/24686>
[^v4-activation]: Aave Labs (2026). *[ARFC] Aave V4 activation on Ethereum mainnet*. Aave governance forum. <https://governance.aave.com/t/arfc-aave-v4-activation-on-ethereum-mainnet/24293>
[^v4-docs]: Aave documentation. *Aave V4 overview*. <https://aave.com/docs/aave-v4>
[^al-april]: Aave Labs (2026). *AL development update, April 2026*. Aave governance forum. <https://governance.aave.com/t/al-development-update-april-2026/24821>
[^al-may]: Aave Labs (2026). *AL development update, May 2026*. Aave governance forum. <https://governance.aave.com/t/al-development-update-may-2026/25013>
[^umbrella-arfc]: BGD Labs (2025). *[ARFC] Aave Umbrella activation*. Aave governance forum. <https://governance.aave.com/t/arfc-aave-umbrella-activation/21521>
[^umbrella-docs]: Aave documentation. *Aave Umbrella*. <https://aave.com/docs/aave-v3/umbrella>
[^governance-docs]: Aave documentation. *Aave governance*. <https://aave.com/docs/ecosystem/governance>
[^gauntlet]: Morrow, J. (2024). *Gauntlet is leaving Aave*. Aave governance forum. <https://governance.aave.com/t/gauntlet-is-leaving-aave/16700>
[^chaos-decrypt]: Decrypt (2026). *Aave token falls near 2-year low as risk management firm becomes latest to depart*. <https://decrypt.co/363566/aave-token-near-2-year-low-risk-management-firm-departs>
[^chaos-forum]: Goldberg, O. (2026). *Chaos Labs is leaving Aave*. Aave governance forum. <https://governance.aave.com/t/chaos-labs-is-leaving-aave/24386>
[^crv-coindesk]: CoinDesk (2022). *Mango exploiter gets liquidated after roiling Aave using $20M of borrowed Curve tokens*. <https://coindesk.com/markets/2022/11/22/mango-exploiter-gets-liquidated-after-roiling-aave-using-20m-of-borrowed-curve-tokens>
[^crv-decrypt]: Decrypt (2022). *Aave feeling the squeeze even after failed attempt by Mango hacker*. <https://decrypt.co/115596/aave-feeling-the-squeeze-even-after-failed-attempt-by-mango-hacker>
[^crv-block]: The Block (2022). *Llama and Gauntlet submit proposal to cover $1.6 million in bad debt on Aave*. <https://www.theblock.co/post/189606/llama-and-gauntlet-submit-proposal-to-cover-1-6-million-in-bad-debt-on-aave>
[^capo-block]: The Block (2026). *Aave suffers oracle glitch, triggering $26 million in unfair wstETH liquidations*. <https://www.theblock.co/post/393121/aave-oracle-glitch-wsteth>
[^capo-reimb]: TokenLogic (2026). *[Direct to AIP] wstETH CAPO oracle incident user reimbursement*. Aave governance forum. <https://governance.aave.com/t/direct-to-aip-wsteth-capo-oracle-incident-user-reimbursement/24275>
[^rseth-report]: LlamaRisk et al. (2026). *rsETH incident report (April 20, 2026)*. Aave governance forum. <https://governance.aave.com/t/rseth-incident-report-april-20-2026/24580>
[^rseth-funding]: TokenLogic (2026). *[ARFC] rsETH incident funding update*. Aave governance forum. <https://governance.aave.com/t/arfc-rseth-incident-funding-update/24740>
[^weth-unfreeze]: LlamaRisk (2026). *[Direct to AIP] WETH unfreeze and LTV restoration across Aave V3 instances*. Aave governance forum. <https://governance.aave.com/t/direct-to-aip-weth-unfreeze-and-ltv-restoration-across-aave-v3-instances/24878>
[^binance-ct]: Cointelegraph (2026). *Binance hit by $6.3B hack, the largest in cryptocurrency history*. <https://cointelegraph.com/news/binance-linked-wallet-faces-possible-exploit-blockchain-researcher-warns>
[^binance-response]: LlamaRisk (2026). *Binance hot wallet exploit: Aave's response*. Aave governance forum. <https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954>
[^binance-caps]: LlamaRisk (2026). *Risk Stewards: temporary Slope2 reductions on Aave V3 and Aave V4 / 2026.10.30*. Aave governance forum. <https://governance.aave.com/t/risk-stewards-temporary-slope2-reductions-on-aave-v3-and-aave-v4-2026-10-30/25955>
[^binance-draw]: LlamaRisk (2026). *Risk Stewards: borrow and draw cap reductions on Aave V3 and Aave V4 / 2026.10.30*. Aave governance forum. <https://governance.aave.com/t/risk-stewards-borrow-and-draw-cap-reductions-on-aave-v3-and-aave-v4-2026-10-30/25960>
[^cow-forum]: EzR3aL et al. (2025). *Aave CowSwap integration – tokenholder questions*. Aave governance forum. <https://governance.aave.com/t/aave-cowswap-integration-tokenholder-questions/23530>
[^cow-tl]: TokenLogic (2025). *Velora & CowSwap integration analysis*. Aave governance forum. <https://governance.aave.com/t/velora-cowswap-integration-analysis/23620>
[^brand-block]: The Block (2025). *'A hostile takeover attempt': Aave Labs' unilateral push to vote on brand-rights proposal sparks community outcry*. <https://www.theblock.co/post/383464/aave-labs-vote-sparks-community-outcry>
[^brand-ct]: Cointelegraph (2025). *Aave founder says $15M token buy wasn't used in controversial DAO vote*. <https://cointelegraph.com/news/aave-founder-tokens-influence-failed-dao-vote>
[^aww-temp]: The Block (2026). *'Aave will win' proposal clears temp check with 52.6% backing on revenue shift, V4 plan*. <https://www.theblock.co/post/391693/aave-proposal-clears-temp-check-vote>
[^aww-funding]: The Block (2026). *Aave DAO approves $25 million Aave Labs funding grant in binding 'Aave Will Win' vote*. <https://www.theblock.co/post/397138/aave-dao-approves-25-million-aave-labs-funding-grant-in-binding-aave-will-win-vote>
[^bgd]: BGD Labs (2026). *BGD. Leaving Aave*. Aave governance forum. <https://governance.aave.com/t/bgd-leaving-aave/24122>
[^aci-exit]: Zeller, M. (2026). *ACI is leaving Aave*. Aave governance forum. <https://governance.aave.com/t/aci-is-leaving-aave/24205>
