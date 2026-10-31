---
title: Arbitrum
ticker: ARB
category: Layer 2
written_by: Opus 5.5 High
status: ai-fact-checked
checked: 2026-10-30
checked_by: GPT-6-Astra high
updated: 2026-10-30
---

# Arbitrum

**Arbitrum** is a family of layer 2 networks that process transactions
off [Ethereum](ethereum.md) and post the results back to it. Its main
network, **Arbitrum One**, is an optimistic [rollup](rollup.md): transactions are
assumed valid unless someone proves otherwise with a fraud proof during a
challenge period. Arbitrum was developed by Offchain Labs and is governed
by the Arbitrum DAO through the **ARB** token.[^intro][^governance-intro]

| | |
|---|---|
| Type | Optimistic rollup on Ethereum |
| Developer | Offchain Labs |
| Founders | Ed Felten, Steven Goldfeder, Harry Kalodner |
| Mainnet (Arbitrum One) | 2021-08-31 (public) |
| Chain ID | 42161 (One), 42170 (Nova)[^chain-info] |
| Gas token | ETH |
| Governance token | ARB |
| Initial ARB supply | 10,000,000,000 |
| Governance | Arbitrum DAO, Security Council |
| Proof system | BoLD interactive fraud proofs |
| Challenge period | About 6.4 days |
| Data availability | Ethereum (One and, since September 2026, Nova)[^governance-intro] |
| Smart contracts | EVM; WebAssembly via Stylus (new activations paused since 2026-10-02) |
| Live data | [L2Beat](https://l2beat.com/scaling/projects/arbitrum), [DefiLlama](https://defillama.com/chain/Arbitrum), [Arbiscan](https://arbiscan.io) |

## History

### Research origins

Arbitrum began as research at Princeton University. Ed Felten was a
professor of computer science there and had served as Deputy US Chief
Technology Officer in the Obama White House, appointed in
2015.[^felten] Steven Goldfeder was a co-author of the textbook *Bitcoin
and Cryptocurrency Technologies*,[^textbook] and Harry Kalodner was a
doctoral student working on blockchain analysis.[^blocksci][^introducing]

The design was published at the USENIX Security Symposium in 2018 by
Kalodner, Goldfeder, Xiaoqi Chen, S. Matthew Weinberg, and
Felten.[^paper] The 2018 paper described a system in which a small set
of managers ran a contract off-chain and any one of them could challenge
a false claim about its result on-chain.[^introducing] Felten,
Goldfeder, and Kalodner co-founded Offchain Labs to build it.[^public-launch] By
2019 they had adapted the design into an optimistic rollup, in which
anyone, not only a fixed set of managers, can challenge.[^rollup-2019]

Offchain Labs announced US$120 million in funding at a US$1.2 billion
valuation in August 2021.[^public-launch] This included April’s US$20 million
Series A and August’s US$100 million Series B, led by Lightspeed.[^funding] In October 2022 it
acquired Prysmatic Labs, the developer of Prysm, one of Ethereum's main
consensus clients.[^prysmatic]

### Launch

After an open public testnet in October 2020,[^testnet] Arbitrum One
opened to developers in May 2021 and to the public on 31 August
2021.[^public-launch] Fraud proofs worked from launch, but only an
allowlisted set of validators could post them.[^bold-testnet]

In June 2022 Offchain Labs paused "Arbitrum Odyssey", a promotional
campaign, after the traffic it generated pushed up fees on the
network.[^odyssey]

On 9 August 2022 Offchain Labs launched Arbitrum Nova, a cheaper chain
built on AnyTrust technology.[^nova-launch] Under AnyTrust, a data
availability committee holds the transaction data; the protocol assumes
at least two committee members are honest.[^anytrust] Reddit used Nova for
Community Points,[^nova-launch] which it discontinued in November
2023.[^reddit] According to the governance documentation, Nova began posting
its data to Ethereum in September 2026, leaving the committee
dormant.[^governance-intro]

On 31 August 2022 Arbitrum One moved to Nitro, a rewrite that runs a
fork of Geth for execution and compiles it to WebAssembly for fraud
proofs. Nitro also compressed the transaction data it posted to
Ethereum.[^compression][^intro][^tokenomics]

### Token and DAO

The ARB token and DAO were announced on 16 March 2023; the user airdrop
opened on 23 March. The distribution following governance proposals
AIP-1.1 and AIP-1.2 was:[^aip1-clarification][^tokenomics]

| Recipient | Share |
|---|---|
| Arbitrum DAO treasury | 35.28% |
| Offchain Labs team, future team, and advisors | 26.94% |
| Investors in Offchain Labs | 17.53% |
| Users (airdrop) | 11.62% |
| Arbitrum Foundation | 7.5% |
| DAOs building on Arbitrum | 1.13% |

The DAO can mint up to 2% of supply per year. Tokens allocated to the
team and investors were locked for one year and then unlocked monthly
over three years, starting in March 2024.[^tokenomics][^vesting]

The DAO took control of Arbitrum One and Nova's upgrade keys at
launch.[^constitution] Within weeks its first proposal, AIP-1, became a
controversy (see [below](#incidents-and-controversies)). The first
Security Council election began in September 2023.[^sc-elections]

### Incentive programmes and treasury

Much of the DAO's activity has been spending its treasury. The
Short-Term Incentive Program (STIP), approved in September 2023,
budgeted up to 50 million ARB for applications on Arbitrum.[^stip] It was
followed by further incentive programmes in 2024.[^stip-bridge]

In June 2024 the DAO approved the Gaming Catalyst Program, a 225 million
ARB fund for games on Arbitrum, run by Arbitrum Gaming
Ventures.[^gcp] On 2 July 2026 the DAO approved a wind-down plan.
The plan stopped new investments outside the existing portfolio and
proposed returning about 143.7 million ARB. By 21 July the implementation
updates recorded returns of 129.17 million ARB and US$7 million in USDC.
As of 30 October 2026 the wind-down remained in progress.[^agv-wind-down][^agv-updates]

Arbitrum One’s net base-fee revenue goes to the DAO treasury. Priority
fees under Priority Gas Auctions are divided between the DAO (97%) and
the Arbitrum Developer Guild (3%).[^gas]

### Later upgrades

- **Atlas** (March 2024) let Arbitrum post data to Ethereum as blobs
  after Ethereum's Dencun upgrade, cutting fees sharply.[^atlas]
- **Stylus** (3 September 2024) lets developers write contracts in Rust,
  C, and C++ compiled to WebAssembly, alongside Solidity.[^stylus]
- **BoLD** (12 February 2025) replaced the allowlisted validator set with
  a permissionless dispute protocol that bounds the delay any challenger
  can cause.[^bold][^upgrades]
- **Timeboost** (April 2025) introduced an auction for an "express
  lane" that gave the winner a short time advantage in transaction
  ordering. In September 2026, after a constitutional AIP, Arbitrum One
  replaced it with Priority Gas Auctions, which order transactions by the
  priority fee they pay.[^pga][^pga-live]
- **ArbOS upgrades** continued with ArbOS 40 Callisto (17 June 2025),
  ArbOS 51 Dia (8 January 2026), and ArbOS 61 Elara (20 August
  2026).[^upgrades]

On 2 October 2026 the Security Council paused new Stylus contract
activations on Arbitrum One and Nova, citing a denial-of-service risk in
WebAssembly handling. Existing active contracts can run until their
activation expires, and can extend it before expiry. Expired contracts
cannot reactivate while the pause remains in place.[^stylus-pause][^stylus-notice]

### Arbitrum chains

Teams can launch their own chains on Arbitrum's software stack. These
were first branded Arbitrum Orbit, announced in March 2023,[^orbit] and
are now called Arbitrum chains. A chain can settle to Arbitrum One as a
layer 3, or directly to Ethereum, and since January 2024 can use its own
gas token.[^custom-gas] Under the Arbitrum Expansion Program, launched by
the Arbitrum Foundation in January 2024, chains that settle anywhere
other than Arbitrum One or Nova pay 10% of their net protocol revenue
to the Arbitrum ecosystem.[^aep][^aep-launch]

Examples include Xai, a gaming chain,[^xai] and ApeChain, built for the
ApeCoin community.[^apechain] On 30 June 2025 Robinhood began issuing
tokenized stocks to European customers on Arbitrum One,[^robinhood-stocks]
and on 1 July 2026 it launched Robinhood Chain, an Arbitrum chain of its
own.[^robinhood]

## Technology

### Transaction flow

A sequencer receives transactions, orders them,
and publishes the order in a real-time feed, giving users confirmation
in well under a second. A batch poster compresses batches of
transactions and posts them to Ethereum, as blobs where possible. Once
the batch is finalized on Ethereum, its order cannot change, even
though its result has not yet been proven.[^sequencer]

Users can bypass the sequencer by submitting transactions directly to a
contract on Ethereum, called the delayed inbox. If the sequencer does
not include them within at most about 24 hours, anyone can force them
into the chain. This protects users from censorship but not from
delay.[^sequencer]

Arbitrary messages and token deposits from Ethereum to Arbitrum can use
"retryable tickets", which can be re-executed if they fail the first
time.[^retryables] Messages from Arbitrum to Ethereum, such as
withdrawals, can be executed on Ethereum only after the challenge period
has passed.[^bold]

### Execution

Nitro runs a modified version of Geth, an Ethereum execution client.[^intro] A layer
called ArbOS handles what is specific to Arbitrum, such as pricing the
cost of posting data to Ethereum and processing cross-chain messages.
Execution base fees respond to gas usage against targets measured over
multiple time windows.[^gas]

Stylus adds a second virtual machine that runs WebAssembly. Stylus and
EVM contracts can call each other. Programs that do heavy computation
can use less execution gas in Stylus, according to its documentation.[^stylus-intro]

### Proving

Validators run the same code and post assertions to Ethereum about the
resulting state. Each assertion requires a bond. If an assertion is
wrong, another validator can challenge it. The two sides then bisect
their disagreement, round by round, until it narrows to a single
instruction, which a contract on Ethereum executes to decide who is
right. A challenge period is about 6.4 days. Under an adversarial
challenge, BoLD’s stated upper bound is two challenge periods plus a
two-day Security Council grace period; 6.4 days is therefore not a
guarantee for every withdrawal.[^bold]

Before BoLD, an attacker could in principle delay a correct assertion by
challenging it repeatedly with different identities. BoLD lets a single
honest party defend the correct state against any number of challengers
within a fixed time.[^bold]

As of 30 October 2026, L2Beat classifies Arbitrum One as a Stage 1 rollup: its fraud proofs
work, but the Security Council can still override them in an
emergency.[^l2beat]

## Governance

The Arbitrum DAO votes with ARB on Arbitrum Improvement Proposals (AIPs).
Token holders can delegate their votes. Proposals are
usually discussed on the DAO forum, tested in an off-chain Snapshot poll,
and then put to a binding on-chain vote.[^constitution]

Constitutional proposals, which change the protocol or the constitution,
need a higher quorum and pass through delays that give users time to
exit before a change takes effect.[^constitution] Non-constitutional
proposals, such as treasury grants, need a lower quorum.[^constitution]

The Security Council has 12 members, elected in two cohorts of six, one
every six months. It can act immediately with 9 of 12 signatures in an
emergency, and can make non-emergency upgrades with 9 of 12 signatures
subject to the normal delays.[^constitution][^l2beat] The Arbitrum
Foundation, based in the Cayman Islands, supports the DAO.[^foundation]

## Incidents and controversies

- **AIP-1 (April 2023).** The foundation's first proposal asked the DAO
  to ratify the whole governance framework, including a 750 million ARB
  allocation to the foundation. The foundation acknowledged that some
  funds had already been used, including conversion to stablecoins,
  and said it had intended the vote as ratification. AIP-1 was replaced
  by AIP-1.1 and AIP-1.2.[^aip1-clarification][^tokenomics]
- **Bridge bug (2022).** In September 2022 a white-hat researcher
  disclosed a bug in Nitro's bridge that could have allowed deposits to
  be stolen. It was fixed before it was exploited, and the researcher
  received a 400 ETH bounty.[^bounty][^bounty-report]
- **Sequencer outages.** Because a single sequencer orders transactions,
  an outage interrupts the normal transaction path. Users retain the
  delayed-inbox route.[^sequencer] In December 2023 a surge of inscription
  transactions halted Arbitrum One when its batch poster stopped
  posting.[^outage]
- **KelpDAO freeze (April 2026).** On 21 April 2026 the Security Council
  used its emergency powers to freeze about 30,766 ETH linked to an
  exploit of KelpDAO’s rsETH token.[^kelp-council] A non-binding Snapshot
  poll in May supported releasing the funds for relief; the poll itself
  did not authorize the transfer.[^kelp]
- **Binance-related freeze (October 2026).** On 30 October the Security
  Council reported freezing 8,425 ETH and about 74.56 million ARB linked
  to the Binance exploit. As of that date, moving the funds required
  further Arbitrum governance action.[^binance-council]
- **Centralization.** The December 2023 outage report describes Offchain Labs as
  the sequencer operator. The Security Council can upgrade contracts without delay in an
  emergency.[^outage][^constitution]
- **Token-holder revenue.** Fees accrue to the DAO treasury rather than
  being automatically distributed to ARB holders.[^gas]

## Timeline

| Date | Event |
|---|---|
| 2018 | Arbitrum paper published at USENIX Security |
| 2020-10 | Open public testnet |
| 2021-05 | Arbitrum One opens to developers |
| 2021-08-31 | Arbitrum One opens to the public |
| 2022-06 | Arbitrum Odyssey paused |
| 2022-08-09 | Arbitrum Nova launches |
| 2022-08-31 | Nitro upgrade |
| 2022-09 | Bridge bug disclosed; 400 ETH bounty announced |
| 2022-10 | Offchain Labs acquires Prysmatic Labs |
| 2023-03-16 | Arbitrum Orbit announced |
| 2023-03-23 | ARB airdrop; Arbitrum DAO formed |
| 2023-04 | AIP-1 controversy |
| 2023-09 | First Security Council election begins |
| 2023-12 | Sequencer outage during inscriptions surge |
| 2024-01 | Arbitrum Expansion Program launched |
| 2024-03 | Atlas upgrade: blob support |
| 2024-06 | Gaming Catalyst Program approved |
| 2024-09-03 | Stylus live on mainnet |
| 2025-02-12 | BoLD live on mainnet |
| 2025-04 | Timeboost live on Arbitrum One |
| 2025-06-30 | Robinhood launches tokenized stocks on Arbitrum One |
| 2026-04-21 | Security Council freezes ETH from KelpDAO exploit |
| 2026-07-01 | Robinhood Chain mainnet |
| 2026-07-02 | DAO votes to wind down the Gaming Catalyst Program |
| 2026-09 | Timeboost replaced by Priority Gas Auctions |
| 2026-10-02 | New Stylus activations paused |
| 2026-10-30 | Security Council freezes Binance-exploit-linked funds |

## See also

- [Ethereum](ethereum.md)
- [Hyperliquid](hyperliquid.md)

## References

[^intro]: Arbitrum documentation. *A gentle introduction to Arbitrum*. <https://docs.arbitrum.io/get-started/arbitrum-introduction>
[^felten]: The White House (2015). *The White House names Dr. Ed Felten as Deputy U.S. Chief Technology Officer*. <https://obamawhitehouse.archives.gov/blog/2015/05/11/white-house-names-dr-ed-felten-deputy-us-chief-technology-officer>
[^textbook]: Narayanan, A., Bonneau, J., Felten, E., Miller, A., and Goldfeder, S. (2016). *Bitcoin and Cryptocurrency Technologies*. Princeton University Press. <https://collaborate.princeton.edu/en/publications/bitcoin-and-cryptocurrency-technologies-a-comprehensive-introduct/>
[^blocksci]: Kalodner, H. et al. (2020). *BlockSci: Design and applications of a blockchain analysis platform*. USENIX Security 2020. <https://www.usenix.org/conference/usenixsecurity20/presentation/kalodner>
[^paper]: Kalodner, H., Goldfeder, S., Chen, X., Weinberg, S. M., and Felten, E. W. (2018). *Arbitrum: Scalable, private smart contracts*. 27th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity18/presentation/kalodner>
[^introducing]: Kalodner, H. (2018). *Introducing Arbitrum, a new layer 2 solution*. Ethereum Research. <https://ethresear.ch/t/introducing-arbitrum-a-new-layer-2-solution/3825>
[^rollup-2019]: Felten, E. (2019). *How Arbitrum Rollup works*. Offchain Labs. <https://medium.com/offchainlabs/how-arbitrum-rollup-works-39788e1ed73f>
[^funding]: TechCrunch (2021). *Offchain Labs raises $120 million to hide Ethereum's shortcomings with Arbitrum scaling product*. <https://techcrunch.com/2021/08/31/offchain-labs-raises-120-million-to-hide-ethereums-shortcomings-with-arbitrum-scaling-product/>
[^prysmatic]: The Block (2022). *Offchain Labs acquires Ethereum software team Prysmatic Labs*. <https://www.theblock.co/post/176548/offchain-labs-acquires-ethereum-software-team-prysmatic-labs>
[^testnet]: Offchain Labs (2020). *Arbitrum Rollup testnet: full-featured and open to all*. <https://medium.com/offchainlabs/arbitrum-rollup-testnet-full-featured-and-open-to-all-da3255b562ea>
[^bold-testnet]: Arbitrum. *Arbitrum BOLD testnet live: the next step in decentralization*. <https://blog.arbitrum.io/arbitrum-bold-testnet-live-the-next-step-in-decentralization/>
[^odyssey]: The Block (2022). *Arbitrum fees rose higher than Ethereum mainnet for several hours*. <https://www.theblock.co/post/154762/arbitrum-fees-rose-higher-than-ethereum-mainnet-for-several-hours>
[^anytrust]: Arbitrum documentation. *AnyTrust protocol*. <https://docs.arbitrum.io/how-arbitrum-works/deep-dives/anytrust-protocol>
[^reddit]: Reddit staff (2023). *Sunsetting Community Points beta*. <https://www.reddit.com/r/CryptoCurrency/comments/17a33ql/serious_sunsetting_community_points_beta_and/>
[^compression]: Arbitrum Research. *Compression in Nitro*. <https://research.arbitrum.io/t/compression-in-nitro/20>
[^tokenomics]: Arbitrum Foundation. *$ARB distribution*. <https://docs.arbitrum.foundation/airdrop-eligibility-distribution>
[^sc-elections]: Arbitrum Foundation. *Security Council elections 101*. <https://blog.arbitrum.foundation/security-council-elections-101/>
[^stip]: Arbitrum DAO. *Short-Term Incentive Program* (on-chain proposal). <https://www.tally.xyz/gov/arbitrum/proposal/92535731414466076465748260699234569033779695239254902723866669906112586724812>
[^stip-bridge]: Arbitrum DAO forum. *Double down on STIP successes (STIP-Bridge)*. <https://forum.arbitrum.foundation/t/double-down-on-stip-successes-stip-bridge/22353>
[^gcp]: Cointelegraph (2024). *Arbitrum DAO approves $215M gaming ecosystem fund proposal*. <https://cointelegraph.com/news/arbitrum-gaming-catalyst-program-215m-investment>
[^agv-wind-down]: Arbitrum DAO forum. *AGV wind-down: structured transition and return of capital to the DAO treasury*. <https://forum.arbitrum.foundation/t/agv-wind-down-structured-transition-return-of-capital-to-the-dao-treasury/31012>
[^atlas]: Arbitrum documentation. *ArbOS 20 Atlas*. <https://docs.arbitrum.io/run-arbitrum-node/arbos-releases/arbos20>
[^stylus]: Arbitrum (2024). *Arbitrum Stylus is live on mainnet*. <https://blog.arbitrum.io/arbitrum-stylus-mainnet/>
[^bold]: Arbitrum documentation. *A gentle introduction to BoLD*. <https://docs.arbitrum.io/how-arbitrum-works/bold/gentle-introduction>
[^upgrades]: Arbitrum Foundation. *Network upgrades*. <https://docs.arbitrum.foundation/network-upgrades>
[^pga]: Arbitrum documentation. *Priority Gas Auctions*. <https://docs.arbitrum.io/how-arbitrum-works/priority-gas-auction/pga>
[^stylus-pause]: Arbitrum Security Council (2026). *Emergency action, 2 October 2026*. <https://forum.arbitrum.foundation/t/security-council-emergency-action-2-10-2026/31530>
[^orbit]: Arbitrum Foundation (2023). *Launch of Arbitrum Orbit*. <https://www.prnewswire.com/news-releases/the-arbitrum-foundation-announces-launch-of-arbitrum-orbit-layer-3-chains-for-all-301773505.html>
[^custom-gas]: The Block (2024). *Arbitrum Orbit custom gas tokens*. <https://www.theblock.co/post/270370/arbitrum-orbit-custom-gas-tokens>
[^aep]: Arbitrum Foundation. *Calculate AEP fees*. <https://docs.arbitrum.foundation/calculate-aep-fees>
[^xai]: The Block (2023). *Gaming-focused layer 3 Xai set to launch on Arbitrum*. <https://www.theblock.co/post/234647/gaming-focused-layer-3-xai-arbitrum-launch>
[^apechain]: Arbitrum. *ApeChain's bold move to Arbitrum*. <https://blog.arbitrum.io/apechains-bold-move-to-arbitrum-a-game-changing-partnership-2/>
[^robinhood-stocks]: Robinhood (2025). *Robinhood launches stock tokens*. <https://robinhood.com/newsroom/robinhood-launches-stock-tokens-reveals-layer-2-blockchain-and-expands-crypto-suite-in-eu-and-us-with-perpetual-futures-and-staking/>
[^robinhood]: Arbitrum (2026). *Robinhood Chain mainnet*. <https://blog.arbitrum.io/robinhood-chain-mainnet/>
[^sequencer]: Arbitrum documentation. *Sequencer*. <https://docs.arbitrum.io/how-arbitrum-works/deep-dives/sequencer>
[^retryables]: Arbitrum documentation. *Parent to child chain messaging*. <https://docs.arbitrum.io/how-arbitrum-works/deep-dives/l1-to-l2-messaging>
[^gas]: Arbitrum documentation. *Gas and fees*. <https://docs.arbitrum.io/how-arbitrum-works/deep-dives/gas-and-fees>
[^stylus-intro]: Arbitrum documentation. *A gentle introduction to Stylus*. <https://docs.arbitrum.io/stylus/gentle-introduction>
[^l2beat]: L2Beat. *Arbitrum One*. <https://l2beat.com/scaling/projects/arbitrum>
[^constitution]: Arbitrum Foundation. *The Constitution of the Arbitrum DAO*. <https://docs.arbitrum.foundation/dao-constitution>
[^foundation]: Arbitrum Foundation. *What is the Arbitrum Foundation?* <https://docs.arbitrum.foundation/what-foundation>
[^bounty]: The Block (2022). *Arbitrum announces 400 ETH bug bounty payout*. <https://www.theblock.co/post/171585/arbitrum-announces-400-eth-bug-bounty-payout>
[^outage]: Dedaub (2023). *Arbitrum sequencer outage*. <https://dedaub.com/blog/arbitrum-sequencer-outage/>
[^kelp]: Decrypt (2026). *Arbitrum DAO votes to unlock $70 million for Kelp DAO exploit relief*. <https://decrypt.co/367238/arbitrum-dao-votes-to-unlock-70-million-for-kelp-dao-exploit-relief>
[^governance-intro]: Arbitrum Foundation. *Introduction to DAO governance*. <https://docs.arbitrum.foundation/gentle-intro-dao-governance>
[^chain-info]: Arbitrum documentation. *Chain information*. <https://docs.arbitrum.io/chain-info>
[^public-launch]: Offchain Labs (2021). *Arbitrum One public launch and funding*. <https://www.prnewswire.com/news-releases/offchain-labs-rolls-out-arbitrum-one-ethereum-scaling-solution-to-the-public-and-announces-120m-in-funding-301365642.html>
[^nova-launch]: Offchain Labs (2022). *Nova is open to the public*. <https://medium.com/offchainlabs/its-time-for-a-new-dawn-nova-is-open-to-the-public-a081df1e4ad2>
[^vesting]: Arbitrum Foundation. *Token supply*. <https://docs.arbitrum.foundation/token-supply>
[^agv-updates]: Arbitrum DAO (2026). *AGV wind-down process updates*. <https://forum.arbitrum.foundation/t/agv-windown-process-updates/31084>
[^pga-live]: Arbitrum (2026). *Competing for transaction priority on Arbitrum*. <https://blog.arbitrum.io/competing-for-transaction-priority-on-arbitrum/>
[^stylus-notice]: Arbitrum documentation. *Stylus activation pause notice*. <https://docs.arbitrum.io/notices/stylus-activation-pause-notice>
[^aep-launch]: Arbitrum Foundation (2024). *Arbitrum Expansion Program and Developer Guild*. <https://forum.arbitrum.foundation/t/the-arbitrum-expansion-program-and-developer-guild/20722>
[^aip1-clarification]: Arbitrum Foundation (2023). *Clarity around the ratification of AIP-1*. <https://forum.arbitrum.foundation/t/clarity-around-the-ratification-of-aip-1/12864>
[^bounty-report]: 0xriptide (2022). *Hackers in Arbitrum’s inbox*. <https://medium.com/@0xriptide/hackers-in-arbitrums-inbox-ca23272641a2>
[^kelp-council]: Arbitrum Security Council (2026). *Emergency action, 21 April 2026*. <https://forum.arbitrum.foundation/t/security-council-emergency-action-21-04-2026/30803>
[^binance-council]: Arbitrum Security Council (2026). *Emergency action, 30 October 2026*. <https://forum.arbitrum.foundation/t/security-council-emergency-action-30-10-2026/31625>
