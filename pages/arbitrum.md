---
title: Arbitrum
ticker: ARB
category: Layer 2
status: draft
updated: 2026-10-30
---

# Arbitrum

**Arbitrum** is a family of layer 2 networks that process transactions
off [Ethereum](ethereum.md) and post the results back to it. Its main
network, **Arbitrum One**, is an optimistic rollup: transactions are
assumed valid unless someone proves otherwise with a fraud proof during a
challenge period. Arbitrum was developed by Offchain Labs and is governed
by the Arbitrum DAO through the **ARB** token.[^intro]

| | |
|---|---|
| Type | Optimistic rollup on Ethereum |
| Developer | Offchain Labs |
| Founders | Ed Felten, Steven Goldfeder, Harry Kalodner |
| Mainnet (Arbitrum One) | 2021-08-31 (public) |
| Chain ID | 42161 (One), 42170 (Nova) |
| Gas token | ETH |
| Governance token | ARB |
| Initial ARB supply | 10,000,000,000 |
| Governance | Arbitrum DAO, Security Council |
| Proof system | BoLD interactive fraud proofs |
| Data availability | Ethereum (One); data availability committee (Nova) |
| Smart contracts | EVM; WebAssembly via Stylus (new activations paused since 2026-10-02) |
| Live data | [L2Beat](https://l2beat.com/scaling/projects/arbitrum), [DefiLlama](https://defillama.com/chain/Arbitrum), [Arbiscan](https://arbiscan.io) |

## History

### Research origins

Arbitrum began as research at Princeton University. Its design was
published at the USENIX Security Symposium in 2018 by Harry Kalodner,
Steven Goldfeder, Xiaoqi Chen, S. Matthew Weinberg, and Edward W.
Felten.[^paper] Felten, Goldfeder, and Kalodner founded Offchain Labs in
2018 to build it. In 2021 Offchain Labs raised US$120 million: a US$20
million Series A in April and a US$100 million Series B led by Lightspeed
Venture Partners in August, at a US$1.2 billion valuation.[^funding]

### Launch

Arbitrum One opened to developers on 28 May 2021 and to the public on 31
August 2021. On 9 August 2022 Offchain Labs launched Arbitrum Nova, a
cheaper chain that stores transaction data with a data availability
committee rather than on Ethereum. On 31 August 2022 Arbitrum One moved
to Nitro, a rewrite that runs a fork of Geth for execution and compiles
it to WebAssembly for fraud proofs.

### Token and DAO

The ARB token was created on 16 March 2023 and airdropped to users on 23
March 2023. Its initial allocation was:[^tokenomics]

| Recipient | Share |
|---|---|
| Arbitrum DAO treasury | 35.28% |
| Offchain Labs team, future team, and advisors | 26.94% |
| Investors in Offchain Labs | 17.53% |
| Users (airdrop) | 11.62% |
| Arbitrum Foundation | 7.5% |
| DAOs building on Arbitrum | 1.13% |

The DAO can mint up to 2% of supply per year.[^tokenomics]

### Later upgrades

- **Stylus** (3 September 2024) lets developers write contracts in Rust,
  C, and C++ compiled to WebAssembly, alongside Solidity.[^stylus]
- **BoLD** (12 February 2025) replaced the allowlisted validator set with
  a permissionless dispute protocol that bounds the delay any challenger
  can cause.[^bold][^upgrades]
- **Timeboost** (17 April 2025) introduced an auction for an "express
  lane" that gave the winner a short time advantage in transaction
  ordering. In September 2026, after a constitutional AIP, Arbitrum One
  replaced it with Priority Gas Auctions, which order transactions by the
  priority fee they pay.[^pga][^pga-aip]
- **ArbOS upgrades** continued with ArbOS 40 Callisto (17 June 2025),
  ArbOS 51 Dia (8 January 2026), and ArbOS 61 Elara (20 August
  2026).[^upgrades]

On 2 October 2026 the Security Council paused new Stylus contract
activations on Arbitrum One and Nova, citing a denial-of-service risk in
WebAssembly handling. Existing Stylus contracts keep running.[^stylus-pause]

### Arbitrum chains

Teams can launch their own chains on Arbitrum's software stack. These
were first branded Arbitrum Orbit and are now called Arbitrum chains.
The most prominent is Robinhood Chain, which launched on mainnet on 1
July 2026.[^robinhood]

## Technology

A sequencer, run by Offchain Labs, orders transactions and gives users
fast confirmations. Batches of transactions are posted to Ethereum.
Anyone can submit an assertion about the resulting state; anyone else can
dispute it. Disputes are resolved by an interactive game on Ethereum that
narrows the disagreement down to a single instruction, which Ethereum
then executes. Withdrawals to Ethereum wait for the challenge period,
about a week.[^bold]

Users can bypass the sequencer by submitting transactions directly to a
contract on Ethereum, which guarantees inclusion after a delay if the
sequencer censors them.

L2Beat classifies Arbitrum One as a Stage 1 rollup: its fraud proofs
work, but the Security Council can still override them in an
emergency.[^l2beat]

## Governance

The Arbitrum DAO votes with ARB on Arbitrum Improvement Proposals (AIPs).
Constitutional proposals, which change the protocol or the constitution,
need a higher quorum and pass through delays that give users time to
exit.[^constitution] The Security Council has 12 members, elected in two
cohorts of six, and can act with 9 of 12 signatures in an emergency. The
Arbitrum Foundation, based in the Cayman Islands, supports the
DAO.[^foundation]

## Incidents and controversies

- **AIP-1 (April 2023).** The foundation's first proposal asked the DAO
  to ratify the whole governance framework, including a 750 million ARB
  allocation to the foundation. It emerged that the foundation had
  already moved about 50 million ARB before the vote, lending 40 million
  and converting 10 million to fiat. About 78% of votes in the Snapshot
  poll were against. The foundation first called the vote a
  ratification, then withdrew the proposal and split it into AIP-1.1 and
  AIP-1.2.[^aip1]
- **Sequencer outages.** Because a single sequencer orders transactions,
  outages stop the network. In December 2023 a surge of inscription
  transactions halted Arbitrum One when its batch poster stopped
  posting.[^outage]
- **KelpDAO freeze (April 2026).** On 21 April 2026 the Security Council
  used its emergency powers to freeze about 30,766 ETH linked to an
  exploit of KelpDAO's rsETH token. A DAO vote later backed releasing the
  funds to victims.[^kelp] The episode showed both the protective use and
  the reach of the council's powers.
- **Centralization.** The sequencer is operated by Offchain Labs, and the
  Security Council can upgrade contracts without delay in an emergency.

## Timeline

| Date | Event |
|---|---|
| 2018 | Arbitrum paper published at USENIX Security; Offchain Labs founded |
| 2021-05-28 | Arbitrum One opens to developers |
| 2021-08-31 | Arbitrum One opens to the public; US$100M Series B |
| 2022-08-09 | Arbitrum Nova launches |
| 2022-08-31 | Nitro upgrade |
| 2023-03-23 | ARB airdrop; Arbitrum DAO formed |
| 2023-04 | AIP-1 controversy |
| 2023-12 | Sequencer outage during inscriptions surge |
| 2024-09-03 | Stylus live on mainnet |
| 2025-02-12 | BoLD live on mainnet |
| 2025-04-17 | Timeboost live on Arbitrum One |
| 2026-04-21 | Security Council freezes ETH from KelpDAO exploit |
| 2026-07-01 | Robinhood Chain mainnet |
| 2026-09 | Timeboost replaced by Priority Gas Auctions |
| 2026-10-02 | New Stylus activations paused |

## See also

- [Ethereum](ethereum.md)
- [Hyperliquid](hyperliquid.md), whose original USDC bridge is deployed on Arbitrum

## References

[^intro]: Arbitrum documentation. *A gentle introduction to Arbitrum*. <https://docs.arbitrum.io/get-started/arbitrum-introduction>
[^paper]: Kalodner, H., Goldfeder, S., Chen, X., Weinberg, S. M., and Felten, E. W. (2018). *Arbitrum: Scalable, private smart contracts*. 27th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity18/presentation/kalodner>
[^funding]: TechCrunch (2021). *Offchain Labs raises $120 million to hide Ethereum's shortcomings with Arbitrum scaling product*. <https://techcrunch.com/2021/08/31/offchain-labs-raises-120-million-to-hide-ethereums-shortcomings-with-arbitrum-scaling-product/>
[^tokenomics]: Arbitrum Foundation. *$ARB distribution*. <https://docs.arbitrum.foundation/airdrop-eligibility-distribution>
[^stylus]: Arbitrum (2024). *Arbitrum Stylus is live on mainnet*. <https://blog.arbitrum.io/arbitrum-stylus-mainnet/>
[^bold]: Arbitrum documentation. *A gentle introduction to BoLD*. <https://docs.arbitrum.io/how-arbitrum-works/bold/gentle-introduction>
[^upgrades]: Arbitrum Foundation. *Network upgrades*. <https://docs.arbitrum.foundation/network-upgrades>
[^pga]: Arbitrum documentation. *Priority Gas Auctions*. <https://docs.arbitrum.io/how-arbitrum-works/priority-gas-auction/pga>
[^pga-aip]: Arbitrum DAO forum. *Constitutional AIP: Transition Arbitrum One ordering policy to Priority Gas Auctions (PGA)*. <https://forum.arbitrum.foundation/t/constitutional-aip-transition-arbitrum-one-ordering-policy-to-priority-gas-auctions-pga/30942>
[^stylus-pause]: Crypto Briefing (2026). *Arbitrum pauses new Stylus activations*. <https://cryptobriefing.com/arbitrum-pauses-new-stylus-activations/>
[^robinhood]: Arbitrum (2026). *Robinhood Chain mainnet*. <https://blog.arbitrum.io/robinhood-chain-mainnet/>
[^l2beat]: L2Beat. *Arbitrum One*. <https://l2beat.com/scaling/projects/arbitrum>
[^constitution]: Arbitrum Foundation. *The Constitution of the Arbitrum DAO*. <https://docs.arbitrum.foundation/dao-constitution>
[^foundation]: Arbitrum Foundation. *What is the Arbitrum Foundation?* <https://docs.arbitrum.foundation/what-foundation>
[^aip1]: Decrypt (2023). *Arbitrum declares first DAO vote moot*. <https://decrypt.co/125252/arbitrum-declares-first-dao-vote-moot-cites-chicken-and-the-egg-problem-as-arb-falls>
[^outage]: Dedaub (2023). *Arbitrum sequencer outage*. <https://dedaub.com/blog/arbitrum-sequencer-outage/>
[^kelp]: Decrypt (2026). *Arbitrum DAO votes to unlock $70 million for Kelp DAO exploit relief*. <https://decrypt.co/367238/arbitrum-dao-votes-to-unlock-70-million-for-kelp-dao-exploit-relief>
