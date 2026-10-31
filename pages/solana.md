---
title: Solana
ticker: SOL
category: Layer 1
written_by: Opus 5.5 High
status: ai-fact-checked
checked: 2026-10-30
checked_by: Opus 5.5 High
updated: 2026-10-30
---

# Solana

**Solana** is a proof-of-stake layer 1 blockchain designed for high
throughput and low fees, with smart contracts (called programs) that can
run in parallel. It was conceived in 2017 by Anatoly Yakovenko, whose
design used a technique he called Proof of History to order transactions
before validators vote on them. Its main network launched as a "mainnet
beta" in March 2020. Its native token, SOL, pays transaction fees and is
staked to validators.[^fidelity][^whitepaper]

| | |
|---|---|
| Type | Proof-of-stake layer 1 blockchain |
| Developers | Solana Labs, Anza, Jump Crypto (Firedancer), Jito |
| Founders | Anatoly Yakovenko, Raj Gokal |
| Mainnet beta | 2020-03-16 |
| Consensus | Alpenglow (since 2026-10-21); previously Tower BFT with Proof of History |
| Native token | SOL |
| Genesis supply | 500,000,000 SOL |
| Maximum supply | None (inflationary issuance) |
| Slot time | 200 ms (since 2026-10-09) |
| Validator clients | Agave, Jito-Solana, Harmonic Salsa; Firedancer (not supported under Alpenglow as of October 2026) |
| Live data | [Solana Explorer](https://explorer.solana.com), [DefiLlama](https://defillama.com/chain/Solana), [CoinGecko](https://www.coingecko.com/en/coins/solana) |

## History

### Origins

Yakovenko moved from Ukraine to the United States as a child and worked
at Qualcomm for nearly 13 years, including on distributed systems, leaving
in 2016. According to Fortune, the idea for Proof of History came to him
in 2017 while he and a friend were mining cryptocurrency to offset the
cost of hardware they were building for deep learning: he realised that
the passage of time could itself serve as a data structure for ordering
events. The project was first named Loom and was renamed after a
similarly named Ethereum project appeared. Raj Gokal joined as a co-founder at the end of 2017; Greg
Fitzgerald and Stephen Akridge, also former Qualcomm engineers, were
early co-founders.[^fortune-origins]

Yakovenko set out the design in the whitepaper *Solana: A new
architecture for a high performance blockchain*. It proposed Proof of
History as "a proof for verifying order and passage of time between
events", to be used alongside a proof-of-stake consensus algorithm to
reduce messaging between nodes, and estimated that up to 710,000
transactions per second were possible on a 1 Gbps
network.[^whitepaper] According to the US Securities
and Exchange Commission (SEC), Solana Labs, Inc. was founded in 2018 by
Yakovenko and Gokal and is headquartered in San
Francisco.[^sec-coinbase]

### Funding and token sales

The SEC stated that between May 2018 and early March 2020 Solana Labs
sold about 177 million SOL through Simple Agreements for Future Tokens,
raising over US$23 million in offerings Solana Labs said were exempt
from registration. In
March 2020 it sold about 8 million SOL in a Dutch auction on CoinList at
US$0.22 each, raising about US$1.76 million.[^sec-coinbase][^coinlist]
In July 2019 Solana announced a US$20 million round led by Multicoin
Capital,[^recap-2019] and on 9 June 2021 Solana Labs announced a
US$314,159,265 private token sale led by Andreessen Horowitz and
Polychain Capital, open only to offshore investors. Alameda Research and
Jump Trading were among the participants.[^private-sale]

SOL had a genesis supply of 500 million tokens. Fidelity Digital Assets,
citing Crypto.com data, gives the initial allocation
as:[^fidelity]

| Recipient | SOL |
|---|---|
| Community reserve | 194,500,000 |
| Seed round investors | 81,200,000 |
| Founding sale | 64,600,000 |
| Founding team | 63,900,000 |
| Solana Foundation | 52,300,000 |
| Validator sale | 25,900,000 |
| Strategic sale | 9,400,000 |
| CoinList auction | 8,200,000 |

The SEC complaint instead cites Solana Labs as having stated that 12.5% of
the initial supply went to its founders and 12.5% to the Solana
Foundation.[^sec-coinbase]

### Foundation and mainnet beta

The Solana Foundation, a Swiss non-profit, was created in June 2019 to
oversee governance and coordination of the protocol.[^recap-2019] On 8
April 2020 Solana Labs transferred 167 million SOL to it.[^sec-coinbase]
Mainnet beta launched on 16 March 2020.[^helius-inflation]

Weeks later, users found an account holding more than 13 million SOL.
The foundation said on 27 April 2020 that it had lent 11,365,067 SOL to a
market maker without disclosing the loan during the CoinList auction and
Binance listing, and apologised.[^market-maker] On 22 May 2020 it removed
that amount from the token supply, and the tokens were burned on 25 May
2020.[^supply-removal] Inflationary staking rewards were activated
on 10 February 2021.[^helius-inflation]

### FTX and Alameda

FTX and Alameda Research were closely tied to the early Solana
ecosystem. In July 2020 they created the Serum Foundation and launched
Serum, an order-book exchange on Solana.[^serum] The Solana Foundation
sold Alameda and FTX more than 50 million SOL between August 2020 and
January 2021, most of it locked and unlocking monthly until 2027 or 2028,
and Solana Labs sold Alameda a further 7.5 million SOL in February
2021.[^ftx-facts]

When FTX and Alameda filed for bankruptcy in November 2022 (see
[FTX](ftx.md)), SOL fell sharply, and Fortune reported an analyst's view
that its close association with Sam Bankman-Fried was weighing on it.
Yakovenko said Solana Labs held no assets on FTX.[^fortune-ftx] The
Solana Foundation disclosed about US$1 million in cash on FTX, together
with FTX shares and FTT and SRM tokens held there. It also said that
wrapped assets issued through Sollet, a custodial bridge, worth about
US$40 million had an unknown backing.[^ftx-facts]

### Solana Labs, Anza and client diversity

The validator client was originally developed by Solana Labs. On 2
March 2024 Anza, a firm of former Solana Labs executives and engineers,
forked that client into a new repository and named it
Agave.[^anza-fork] Jump Crypto has been building
Firedancer, an independent client written in C, since 2022; a first
version went live on testnet in October 2023.[^firedancer-jump][^bp23][^fidelity]
A hybrid version, Frankendancer, reached mainnet in September
2024,[^theblock-frankendancer] and the Solana Foundation announced that
Firedancer was live on mainnet in December 2025.[^firedancer-live] The Jito Foundation maintains Jito-Solana,
a fork of the validator that it describes as an MEV client, and Jito
offers transaction bundles used by traders seeking maximal extractable
value (MEV).[^jito][^jito-docs]

### Saga and consumer products

In June 2022 Solana Mobile, a subsidiary of Solana Labs, announced Saga,
an Android phone built by OSOM with a secure element for storing keys,
priced at US$1,000.[^saga-reveal] It went on general sale on 8 May
2023.[^fortune-saga]

### Memecoins and pump.fun

Pump.fun, launched in January 2024, lets anyone create a Solana token in
a few clicks.[^gizmodo-pump] It paused its livestreaming feature on 25
November 2024, citing moderation problems, amid criticism of stunts and threats made
on streams.[^gizmodo-stream] In July 2025 it
raised US$600 million in 12 minutes in a public sale of its token,
plus about US$720 million privately.[^fortune-pump] In January 2025 the
launch of a memecoin by Donald Trump drove a surge in
Solana activity; Coinbase users saw delayed Solana withdrawals, which
Coinbase attributed to its own systems.[^fortune-trump]

### Exchange-traded products

On 28 October 2025 Bitwise began trading BSOL on the NYSE, which it
described as the first US spot Solana exchange-traded product; it
intended to stake all of the fund's SOL.[^bitwise] Grayscale launched a Solana fund around
the same time, followed in November 2025 by VanEck, Canary Capital and
Fidelity.[^coindesk-fsol]

### Regulation

In June 2023 the SEC alleged in its complaint against Coinbase that SOL
was offered and sold as a security.[^sec-coinbase] The SEC dismissed that
case in February 2025, saying the dismissal was not a judgement on the
merits.[^sec-dismissal] On 17 March 2026 the SEC issued an interpretation,
with guidance from the Commodity Futures Trading Commission, that listed SOL among
its examples of digital commodities, which it does not treat as
securities.[^sec-interp]

### 2026 upgrades

In 2026 several protocol changes reached mainnet. The block limit rose
from 60 million to 100 million compute units on 29 July 2026.[^cu-blocks]
Slot times were cut from 400 to 200 milliseconds in four steps, the last
on 9 October 2026.[^slots] Alpenglow replaced Tower BFT on 21 October
2026 (see [Consensus](#consensus)). A proposal to double the rate at
which inflation declines, SIMD-0550, was merged into the improvement
document repository on 23 July 2026 and went to a stake-weighted vote in
August 2026.[^simd-0550-pr][^simd-0550-forum]

## Technology

### Accounts and execution

Solana separates programs from the accounts that hold data and balances.
Each transaction lists every account it will read or write. Sealevel, the
runtime, uses these lists to run transactions that do not touch the same
accounts in parallel.[^sealevel]

### Leaders, Gulf Stream and Turbine

Validators take turns as leader according to a schedule known in
advance. Gulf Stream uses this to forward transactions straight to
upcoming leaders instead of keeping a shared mempool, and transactions
reference a recent block hash so that they expire if not
included.[^gulf-stream] Turbine spreads a block across the network by
splitting it into small pieces called shreds, adding erasure-coded
redundancy, and relaying them through a stake-weighted tree of
validators.[^turbine][^turbine-anza]

### Consensus

Under the original design, the leader ran a sequential hash chain, Proof
of History, recording transactions into it to prove their order and the
time elapsed.[^whitepaper] Tower BFT, a variant of practical Byzantine
fault tolerance, used that chain as a clock: each vote locked a
validator out of voting for conflicting forks for a period that doubled
with each later vote.[^tower-bft] Votes were sent as on-chain
transactions, and finality took about 12.8 seconds.[^alpenglow]

Alpenglow, specified in SIMD-0326 by Quentin Kniep, Kobi Sliwinski and
Roger Wattenhofer, replaces this layer. It finalises a block in one round of
voting if 80% of stake votes for it, or in two rounds with 60%. It is
designed to tolerate 20% adversarial stake plus a further 20% offline,
whereas Tower BFT needed a supermajority of more than two-thirds of
stake to confirm a block.[^simd-0326][^alpenglow] Validators approved it
in a stake-weighted vote whose result CoinDesk reported on 2 September
2025, with 98.27% of the stake that
voted in favour and 52% of stake taking part.[^coindesk-alpenglow] Its first phase,
Votor, activated at epoch 1064 on 21 October 2026, targeting finality of
about 150 milliseconds. Validators now exchange votes directly and
aggregate them into certificates, vote transactions no longer appear in
blocks, and Proof of History no longer paces block production. Each
voting validator pays a flat fee of 0.8 SOL per epoch, which is burned.
The second phase, Rotor, will replace Turbine and was not scheduled as
of October 2026. Firedancer was not supported for the switchover, and
validators had to run an Agave-based client: Agave, Jito-Solana or
Harmonic Salsa.[^alpenglow]

## Token and fees

Every transaction pays a base fee of 5,000 lamports per signature, of
which half is burned and half goes to the block-producing validator.
Users can add a priority fee, priced per compute unit, to be scheduled
sooner.[^fees] Priority fees were originally also half burned. Under
SIMD-0096, approved by validators in 2024 with 77.7% of votes, they go
entirely to the validator; critics noted that validators voted on a
change that benefited them.[^fidelity][^fees] Fidelity Digital Assets
noted that this reduced the amount of SOL burned to near
zero.[^fidelity]

New SOL is issued as staking rewards. The schedule began at 8% a year
and falls by 15% each year until it reaches a long-term rate of
1.5%.[^helius-inflation][^anza-inflation] SIMD-0550 proposes raising the
rate of decline to 30% a year, which its authors estimate would reach
1.5% in about 2.8 years instead of 5.7.[^simd-0550-forum]

## Governance

Protocol changes are proposed as Solana Improvement Documents (SIMDs),
discussed off-chain, and implemented by the client teams. Changes with
economic effects, such as SIMD-0096 and Alpenglow, have been put to
stake-weighted votes.[^fidelity][^coindesk-alpenglow] Fidelity Digital Assets described the
system as one in which validators cast the votes, and noted the
criticism that SOL holders who do not stake are not
represented.[^fidelity] By August 2026 holders who stake directly could
override their validator's vote on a proposal.[^simd-0550-forum]

## Incidents and controversies

- Outages. On 14 September 2021 the network was offline for about 17
  hours after bots flooded it with transactions during a token
  offering.[^outage-2021] On 30 April 2022 consensus stalled for about
  seven hours after bots sent millions of transactions per second to
  mint NFTs.[^outage-2022-04] On 1 June 2022 a bug in durable nonce
  transactions halted block production for four and a half
  hours.[^outage-2022-06] On 30 September 2022 a misconfigured validator
  producing duplicate blocks triggered a consensus bug, and production
  stopped for about eight hours.[^outage-2022-09][^fortune-outage] In
  each case validators coordinated a restart of the
  network.[^outage-2021][^outage-2022-06]
- Degradation in February 2023. On 25 February 2023 block-forwarding services
  repeatedly re-sent an unusually large block, overwhelming Turbine;
  validators restarted the cluster with downgraded software.[^outage-2023]
- Outage in February 2024. On 6 February 2024 a bug in the program
  cache halted finalisation for about five hours.[^outage-2024]
- Wormhole bridge (February 2022). An attacker exploited a
  signature-verification flaw in the Solana side of the Wormhole bridge
  to mint about 120,000 wrapped ETH without backing, worth about US$326
  million.[^halborn][^theblock-wormhole] Jump Crypto replaced the 120,000 ETH the next
  day.[^theblock-wormhole]
- Slope wallet (August 2022). On 2 August 2022 attackers drained
  9,231 wallets of about US$4.1 million in assets. The Solana Foundation
  said the affected keys had been created or imported in Slope's mobile
  wallet, which had sent private key material to an application
  monitoring service, and that the Solana protocol was not
  involved.[^slope]
- Securities status. The SEC alleged in 2023 that SOL was a security,
  dropped the case in 2025, and listed SOL as a digital commodity in
  2026.[^sec-coinbase][^sec-dismissal][^sec-interp]

## Timeline

| Date | Event |
|---|---|
| 2017 | Yakovenko conceives Proof of History |
| 2019-06 | Solana Foundation created |
| 2020-03-16 | Mainnet beta launches |
| 2020-03-23 | CoinList auction of 8M SOL |
| 2020-07 | Serum launched by FTX and Alameda |
| 2021-06-09 | US$314M private token sale announced |
| 2021-09-14 | Network offline for about 17 hours |
| 2022-02 | Wormhole bridge exploit |
| 2022-04-30 | Outage during NFT mint |
| 2022-06-01 | Outage from durable nonce bug |
| 2022-08-02 | Slope wallet drain |
| 2022-09-30 | Outage from duplicate-block bug |
| 2022-11 | FTX and Alameda collapse |
| 2023-05-08 | Saga goes on general sale |
| 2023-06-06 | SEC complaint against Coinbase names SOL |
| 2023-10 | Firedancer live on testnet |
| 2024-01 | Pump.fun launches |
| 2024-02-06 | Five-hour outage |
| 2024-03-02 | Anza forks the validator as Agave |
| 2025-01 | Trump memecoin launch drives activity |
| 2025-02-27 | SEC dismisses Coinbase case |
| 2025-07 | Pump.fun token sale |
| 2025-09 | Alpenglow approved by validator vote |
| 2025-10-28 | Bitwise BSOL begins trading |
| 2025-12 | Firedancer live on mainnet |
| 2026-03-17 | SEC interpretation lists SOL as a digital commodity |
| 2026-07-29 | Block limit raised to 100M compute units |
| 2026-08 | Stake-weighted vote on SIMD-0550 |
| 2026-10-09 | Slot time reduced to 200 ms |
| 2026-10-21 | Alpenglow activates on mainnet |

## See also

- [Memecoin](memecoin.md)
- [Blockchain bridge](blockchain-bridge.md)

- [Ethereum](ethereum.md)
- [FTX](ftx.md), an early backer whose collapse affected Solana
- [USDC](usdc.md) and [Tether](tether.md), both issued natively on Solana
- [Hyperliquid](hyperliquid.md)

## References

[^fidelity]: Fidelity Digital Assets (2025). *Coin Report: Solana (SOL)*. <https://www.fidelitydigitalassets.com/sites/g/files/djuvja3256/files/acquiadam/FDA_US_UK_SolanaCoinReport_1205025.2.0.pdf>
[^whitepaper]: Yakovenko, A. *Solana: A new architecture for a high performance blockchain* (v0.8.13). Solana Foundation. <https://github.com/solana-foundation/solana-com/blob/main/apps/docs/public/solana-whitepaper.pdf>
[^fortune-origins]: Fortune (2022). *How Anatoly Yakovenko's crypto startup Solana Labs is building what investors think will be a core layer of Web3*. <https://fortune.com/2022/04/12/solana-anatoly-yakovenko-blockchain-cryptocurrency-ethereum-proof-of-history/>
[^sec-coinbase]: US Securities and Exchange Commission (2023). *SEC v. Coinbase, Inc. and Coinbase Global, Inc.*, complaint, 23 Civ. 4738 (S.D.N.Y.). <https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-102.pdf>
[^coinlist]: Solana (2020). *Solana raises 1.76 million in sold out CoinList auction*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/solana-raises-1-76-million-in-sold-out-coinlist-auction.mdx>
[^recap-2019]: Solana (2019). *Solana in 2019: Growth, development, and the road to mainnet*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/solana-in-2019--growth--development--and-the-road-to-mainnet.mdx>
[^private-sale]: Solana Labs (2021). *Solana Labs completes a $314.15M private token sale led by Andreessen Horowitz and Polychain Capital*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/solana-labs-completes-a-314-15m-private-token-sale-led-by-andreessen-horowitz-and-polychain-capital.mdx>
[^market-maker]: Solana Foundation (2020). *Solana will reduce its token supply to account for market making allocation*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/solana-will-reduce-its-token-supply-to-account-for-market-making-allocation.mdx>
[^supply-removal]: Solana Foundation (2020). *Solana Foundation permanently removes ◎11.365M from token supply*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/solana-foundation-permanently-removes--11-365m-from-token-supply.mdx>
[^helius-inflation]: Helius (2024). *Solana issuance and inflation schedule*. <https://www.helius.dev/blog/solana-issuance-inflation-schedule>
[^serum]: Solana (2020). *FTX chooses Solana for Serum: A high-speed, non-custodial decentralized derivatives exchange*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/ftx-chooses-solana-for-serum--a-high-speed--non-custodial-decentralized-derivatives-exchange.mdx>
[^ftx-facts]: Solana Foundation (2022). *Solana ecosystem facts related to FTX bankruptcy*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/solana-facts-ftx-bankruptcy.mdx>
[^fortune-ftx]: Fortune (2022). *How will the Binance-FTX drama affect Solana? Here's what we know so far*. <https://fortune.com/crypto/2022/11/09/how-will-the-binance-ftx-drama-affect-solana-heres-what-we-know-so-far/>
[^anza-fork]: Anza (2024). *Learn more about the Solana Labs to Agave fork*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/solana-labs-anza-fork.mdx>
[^firedancer-jump]: Jump Crypto. *Firedancer*. <https://jumpcrypto.com/firedancer/>
[^bp23]: Solana Foundation (2023). *Day 1 at Breakpoint: Firedancer, AWS, Google Cloud, and more!* <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/breakpoint-2023-day-1-firedancer-aws-google-cloud.mdx>
[^theblock-frankendancer]: The Block (2024). *Jump Crypto's Frankendancer client launches on Solana mainnet; Firedancer on testnet*. <https://www.theblock.co/post/317490/jump-frankendancer-launches-on-solana-mainnet>
[^firedancer-live]: Solana Foundation (2025). *Firedancer validator client goes live on Mainnet*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/links/firedancer-mainnet-live.mdx>
[^jito]: Jito Foundation. *jito-solana* (source repository). <https://github.com/jito-foundation/jito-solana>
[^jito-docs]: Jito documentation. *Jito*. <https://docs.jito.wtf/>
[^saga-reveal]: Solana Mobile (2022). *Solana Mobile debuts Saga, a flagship Android phone for web3*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/saga-reveal.mdx>
[^fortune-saga]: Fortune (2023). *The Solana Saga is here. Should you spend $1,000 on the newest crypto smartphone?* <https://fortune.com/crypto/2023/05/08/solana-saga-new-crypto-smartphone/>
[^gizmodo-pump]: Gizmodo (2024). *Pump.fun is all of the internet's worst impulses on one site*. <https://gizmodo.com/pump-fun-is-all-of-the-internets-worst-impulses-on-one-site-2000529483>
[^gizmodo-stream]: Gizmodo (2024). *Pump.fun shuts down its bonkers live streaming service*. <https://gizmodo.com/pump-fun-shuts-down-its-bonkers-live-streaming-service-2000530104>
[^fortune-pump]: Fortune (2025). *Popular crypto site Pump.fun raised $600 million in 12 minutes*. <https://fortune.com/crypto/2025/07/18/pump-fun-memecoin-raise-ico-era-600-million-1-3-billion/>
[^fortune-trump]: Fortune (2025). *Solana battles Coinbase outages as SOL hits new high*. <https://fortune.com/crypto/2025/01/22/solana-battles-coinbase-outages-sol-crypto-hits-new-high/>
[^bitwise]: Bitwise (2025). *Bitwise launches BSOL, first spot Solana ETP in US*. <https://bitwiseinvestments.com/newsroom/bitwise-launches-bsol-first-spot-solana-etp-in-us>
[^coindesk-fsol]: CoinDesk (2025). *Fidelity launches FSOL fund, bringing major Wall Street name to Solana ETFs*. <https://www.coindesk.com/markets/2025/11/18/fidelity-launches-fsol-fund-bringing-major-wall-street-name-to-solana-etfs>
[^sec-dismissal]: US Securities and Exchange Commission (2025). *SEC announces dismissal of civil enforcement action against Coinbase*. <https://www.sec.gov/newsroom/press-releases/2025-47>
[^sec-interp]: US Securities and Exchange Commission (2026). *Commission interpretation on the application of the federal securities laws to certain crypto assets*, Release No. 33-11412. <https://www.sec.gov/files/rules/interp/2026/33-11412.pdf>
[^cu-blocks]: Solana Foundation (2026). *100M CU blocks*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/upgrades/100m-cu-blocks.mdx>
[^slots]: Solana Foundation (2026). *Reduced slot times*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/upgrades/reduced-slot-times.mdx>
[^simd-0550-pr]: Solana Improvement Documents. *SIMD-0550: Double disinflation* (pull request #550). <https://github.com/solana-foundation/solana-improvement-documents/pull/550>
[^simd-0550-forum]: Solana Developer Forum (2026). *SIMD-0550: Proposal to double disinflation*. <https://forum.solana.com/t/simd-0550-proposal-to-double-disinflation/4874>
[^sealevel]: Solana (2019). *Sealevel: Parallel processing thousands of smart contracts*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/sealevel---parallel-processing-thousands-of-smart-contracts.mdx>
[^gulf-stream]: Solana (2019). *Gulf Stream: Solana's mempool-less transaction forwarding protocol*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/gulf-stream--solana-s-mempool-less-transaction-forwarding-protocol.mdx>
[^turbine]: Solana (2019). *Turbine: Solana's block propagation protocol solves the scalability trilemma*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/turbine---solana-s-block-propagation-protocol-solves-the-scalability-trilemma.mdx>
[^turbine-anza]: Anza documentation. *Turbine block propagation*. <https://docs.anza.xyz/consensus/turbine-block-propagation>
[^tower-bft]: Solana (2019). *Tower BFT: Solana's high performance implementation of PBFT*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/tower-bft--solana-s-high-performance-implementation-of-pbft.mdx>
[^alpenglow]: Solana Foundation (2026). *Alpenglow*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/upgrades/alpenglow.mdx>
[^simd-0326]: Kniep, Q., Sliwinski, K., and Wattenhofer, R. (2025). *SIMD-0326: Alpenglow*. <https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0326-alpenglow.md>
[^coindesk-alpenglow]: CoinDesk (2025). *Solana set for major overhaul after 98% votes to approve historic 'Alpenglow' upgrade*. <https://www.coindesk.com/tech/2025/09/02/solana-set-for-major-overhaul-after-98-votes-to-approve-historic-alpenglow-upgrade>
[^fees]: Solana documentation. *Fee structure*. <https://github.com/solana-foundation/solana-com/blob/main/apps/docs/content/docs/en/core/fees/fee-structure.mdx>
[^anza-inflation]: Anza documentation. *State-validation protocol-based rewards*. <https://docs.anza.xyz/implemented-proposals/ed_overview/ed_validation_client_economics/ed_vce_state_validation_protocol_based_rewards>
[^outage-2021]: Solana Foundation (2021). *9-14 network outage initial overview*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/9-14-network-outage-initial-overview.mdx>
[^outage-2022-04]: Solana Foundation (2022). *04-30-22 Solana mainnet beta outage report and mitigation*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/04-30-22-solana-mainnet-beta-outage-report-mitigation.mdx>
[^outage-2022-06]: Solana Foundation (2022). *06-01-22 Solana mainnet beta outage report*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/06-01-22-solana-mainnet-beta-outage-report-2.mdx>
[^outage-2022-09]: Solana Foundation (2022). *09-30-22 Solana mainnet beta outage report*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/09-30-22-solana-mainnet-beta-outage-report.mdx>
[^fortune-outage]: Fortune (2022). *Solana back online after another outage. Here's what happened*. <https://fortune.com/crypto/2022/10/01/solana-back-online-after-latest-outage/>
[^outage-2023]: Solana Foundation (2023). *02-25-23 Solana mainnet beta outage report*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/02-25-23-solana-mainnet-beta-outage-report.mdx>
[^outage-2024]: Anza (2024). *02-06-24 Solana mainnet beta outage report*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/02-06-24-solana-mainnet-beta-outage-report.mdx>
[^halborn]: Halborn (2022). *Explained: The Wormhole hack (February 2022)*. <https://www.halborn.com/blog/post/explained-the-wormhole-hack-february-2022>
[^theblock-wormhole]: The Block (2022). *Wormhole replenishes its blockchain bridge after $325 million exploit*. <https://www.theblock.co/post/132909/wormhole-replenishes-its-blockchain-bridge-after-325-million-exploit>
[^slope]: Solana Foundation (2022). *8/2/2022 Slope wallet incident update*. <https://github.com/solana-foundation/solana-com/blob/main/apps/media/content/posts/8-2-2022-application-wallet-incident.mdx>
