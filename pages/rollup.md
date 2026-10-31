---
title: Rollup
ticker: None
category: Infrastructure
written_by: Unknown
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Rollup

A rollup is a blockchain scaling system that executes transactions outside
a base chain and publishes data and state commitments to that chain.
Ethereum rollups use Ethereum to settle results while sharing the cost of
publishing information across a batch of transactions. Optimistic and
validity rollups differ in how those results are verified.[^optimistic][^zk]

| | |
|---|---|
| Type | Layer 2 scaling architecture |
| Main verification families | Optimistic rollups with fault proofs; validity rollups |
| Data publication on Ethereum | Calldata or blobs[^optimistic][^zk] |
| Operational roles | Sequencing, proposing state, challenging or proving |
| Risk framework | L2Beat stages and project risk assessments[^stages] |

## Verification

An optimistic rollup accepts proposed results subject to a challenge
period. A challenger can dispute an invalid state transition using a fault
or fraud proof. Security depends on the ability to detect and challenge
bad results. Canonical withdrawals generally wait for the relevant dispute
period to finish.[^optimistic]

A validity rollup supplies a cryptographic proof that a proposed state
transition follows its execution rules. Its settlement contract verifies
that proof before accepting the transition. Systems often called
zero-knowledge or ZK rollups use this approach, but proving correctness does
not by itself make transaction data private. Their published data can
remain public.[^zk]

## Sequencing and data availability

A sequencer orders transactions and may give users an early confirmation.
That response is distinct from final settlement on the base chain. Rollup
designs differ in whether users can force inclusion through Ethereum and
what happens when an operator stops responding.[^optimistic][^stages]

EIP-4844 introduced blob-carrying transactions as a data-publication
mechanism. Blob data is separate from normal EVM execution data, and its
fee market is distinct from ordinary execution gas. Blobs support cheaper
data publication; they are not a substitute for the rollup's proof system
or a promise of permanent archival storage.[^blobs][^zk]

## Governance and risks

An administrator may retain power to change settlement contracts or proof
systems. An emergency council may also bypass ordinary upgrade delays.
Those powers affect whether users have time to exit an unwanted change,
even where the underlying verification design is sound.[^stages]

L2Beat describes its stages as a measure of decentralisation and trust
minimisation. It explicitly distinguishes that measure from security
against bugs: a system controlled entirely by code can still have unsafe
code. A project's stage should therefore be read alongside its individual
risk analysis.[^stages]

## Timeline

| Date | Event |
|---|---|
| 2022-02-25 | EIP-4844 created[^blobs] |
| 2023-06 | L2Beat introduces its stages framework[^stages] |

## See also

- [Lightning Network](lightning-network.md)
- [Ethereum](ethereum.md)
- [Arbitrum](arbitrum.md)
- [Optimism](optimism.md)
- [Base](base.md)
- [Blockchain bridge](blockchain-bridge.md)
- [Zero-knowledge proof](zero-knowledge-proof.md)

## References

[^optimistic]: ethereum.org. *Optimistic rollups*. <https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/>
[^zk]: ethereum.org. *Zero-knowledge rollups*. <https://ethereum.org/en/developers/docs/scaling/zk-rollups/>
[^blobs]: Buterin, V. et al. (2022). *EIP-4844: Shard Blob Transactions*. <https://eips.ethereum.org/EIPS/eip-4844>
[^stages]: L2Beat. *Stages framework*. <https://l2beat.com/stages>
