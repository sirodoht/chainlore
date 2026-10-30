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
by the Arbitrum DAO through the **ARB** token.[^docs]

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
| Smart contracts | EVM; WebAssembly via Stylus |
| Live data | [L2Beat](https://l2beat.com/scaling/projects/arbitrum), [DefiLlama](https://defillama.com/chain/arbitrum), [Arbiscan](https://arbiscan.io) |

## History

### Research origins

Arbitrum began as research at Princeton University. Its design was
published at the USENIX Security Symposium in 2018 by Harry Kalodner,
Steven Goldfeder, Xiaoqi Chen, S. Matthew Weinberg, and Edward W.
Felten.[^paper] Felten, Goldfeder, and Kalodner founded Offchain Labs in
2018 to build it. In August 2021 Offchain Labs raised a US$120 million
Series B.

### Launch

Arbitrum One opened to developers on 28 May 2021 and to the public on 31
August 2021. On 9 August 2022 Offchain Labs launched Arbitrum Nova, a
cheaper chain that stores transaction data with a data availability
committee rather than on Ethereum. On 31 August 2022 Arbitrum One moved
to Nitro, a rewrite that runs a fork of Geth for execution and compiles
it to WebAssembly for fraud proofs.

### Token and DAO

The ARB token launched on 23 March 2023 with an airdrop to users. Its
initial allocation was:[^tokenomics]

| Recipient | Share |
|---|---|
| Arbitrum DAO treasury | 42.78% |
| Offchain Labs team, future team, and advisors | 26.94% |
| Investors in Offchain Labs | 17.53% |
| Users (airdrop) | 11.62% |
| DAOs building on Arbitrum | 1.13% |

The DAO's constitution lets it mint up to 2% of supply per year.[^constitution]

### Later upgrades

- **Stylus** (September 2024) lets developers write contracts in Rust,
  C, and C++ compiled to WebAssembly, alongside Solidity.
- **BoLD** (February 2025) replaced the allowlisted validator set with a
  permissionless dispute protocol that bounds the delay any challenger
  can cause.
- **Timeboost** (April 2025) introduced an auction for an "express lane"
  that gives the winner a short time advantage in transaction ordering.

Teams can also launch their own chains on Arbitrum's stack, known as
Arbitrum Orbit chains.

## Technology

A sequencer, run by Offchain Labs, orders transactions and gives users
fast confirmations. Batches of transactions are posted to Ethereum.
Anyone can submit an assertion about the resulting state; anyone else can
dispute it. Disputes are resolved by an interactive game on Ethereum that
narrows the disagreement down to a single instruction, which Ethereum
then executes. Withdrawals to Ethereum wait for the challenge period,
about a week.

Users can bypass the sequencer by submitting transactions directly to a
contract on Ethereum, which guarantees inclusion after a delay if the
sequencer censors them.

L2Beat classifies Arbitrum One as a Stage 1 rollup: its fraud proofs
work, but the Security Council can still override them in an
emergency.[^l2beat]

## Governance

The Arbitrum DAO votes with ARB on Arbitrum Improvement Proposals (AIPs).
Constitutional proposals, which change the protocol or the constitution,
need a higher threshold and pass through delays that give users time to
exit.[^constitution] The Security Council has 12 members, elected in two
cohorts, and can act with 9 of 12 signatures in an emergency. The
Arbitrum Foundation, based in the Cayman Islands, supports the DAO.

## Incidents and controversies

- **AIP-1 (April 2023).** The foundation's first proposal asked the DAO
  to ratify a budget of 750 million ARB. It emerged that the foundation
  had already begun moving tokens before the vote. The proposal failed,
  and the foundation resubmitted it as two separate proposals.
- **Sequencer outages.** Because a single sequencer orders transactions,
  outages stop the network. One in December 2023 was caused by a surge of
  inscription transactions.
- **Centralization.** The sequencer is operated by Offchain Labs, and the
  Security Council can upgrade contracts without delay in an emergency.

## Timeline

| Date | Event |
|---|---|
| 2018 | Arbitrum paper published at USENIX Security; Offchain Labs founded |
| 2021-05-28 | Arbitrum One opens to developers |
| 2021-08-31 | Arbitrum One opens to the public; US$120M Series B |
| 2022-08-09 | Arbitrum Nova launches |
| 2022-08-31 | Nitro upgrade |
| 2023-03-23 | ARB token and airdrop; Arbitrum DAO formed |
| 2023-04 | AIP-1 controversy |
| 2024-09 | Stylus live on mainnet |
| 2025-02 | BoLD live on mainnet |
| 2025-04 | Timeboost live on Arbitrum One |

## See also

- [Ethereum](ethereum.md)
- [Hyperliquid](hyperliquid.md), whose USDC bridge is deployed on Arbitrum

## References

[^docs]: Arbitrum documentation. <https://docs.arbitrum.io>
[^paper]: Kalodner, H., Goldfeder, S., Chen, X., Weinberg, S. M., and Felten, E. W. (2018). *Arbitrum: Scalable, private smart contracts*. 27th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity18/presentation/kalodner>
[^tokenomics]: Arbitrum Foundation. *$ARB distribution*. <https://docs.arbitrum.foundation/airdrop-eligibility-distribution>
[^constitution]: Arbitrum Foundation. *The Constitution of the Arbitrum DAO*. <https://docs.arbitrum.foundation/dao-constitution>
[^l2beat]: L2Beat. *Arbitrum One*. <https://l2beat.com/scaling/projects/arbitrum>
