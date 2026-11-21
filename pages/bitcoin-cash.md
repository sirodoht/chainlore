---
title: Bitcoin Cash
ticker: None
category: Layer 1
status: draft
updated: 2026-11-21
written_by: claude-haiku-5-5 (high effort)
---

| Property | Detail |
| --- | --- |
| Type | Hard fork of Bitcoin, incompatible with Bitcoin's rules[^3] |
| Activation time | Unix time 1501590000 (1 August 2017, 12:20 UTC)[^1] |
| Shared history | Through block 478,558; first distinct Bitcoin Cash block is 478,559[^3] |
| Block size rule | Fork block must exceed 1,000,000 bytes; configured limit of at least 8,000,000 bytes[^1] |
| SegWit | Not included[^1][^3] |
| Replay protection | SIGHASH_FORKID signature flag[^1][^3] |
| Later split | Bitcoin SV, 15 November 2018, after block 556,766[^3] |
| Scheduled upgrade | Four CHIP-based changes, activating on mainnet once median time past reaches 1778846400 (15 May 2026, 12:00 UTC)[^2] |

Bitcoin Cash is a cryptocurrency created by a hard fork of Bitcoin on 1 August 2017.[^imp-45-1] The fork arose during the dispute over how to increase Bitcoin's block capacity.[^imp-45-3] Its initial rules supported larger blocks, omitted SegWit and added replay protection, and its shared history with Bitcoin ends at block 478,558.[^imp-45-1][^imp-45-3]

## History

By 2017 Bitcoin's blocks were often full, and the supporters of two approaches disagreed: keeping the base layer small and adding SegWit, or raising the block size limit directly.[^3] According to Degrees of Satoshi, the mining hardware company Bitmain published a user-activated hard fork plan on 14 June 2017 as a response to BIP148, a proposed user-activated soft fork deadline for SegWit.[^3]

Degrees of Satoshi reports that a software implementation called Bitcoin ABC adopted these rules, and that the mining pool ViaBTC said it would list the resulting coin as Bitcoin Cash.[^imp-45-3] The activation time was 1 August 2017 at 12:20 UTC. The chains shared history through block 478,558, and the first distinct Bitcoin Cash block was 478,559.[^imp-45-3] Degrees of Satoshi, citing a CoinDesk report, says ViaBTC mined the first Bitcoin Cash block at about 6:14 p.m. UTC, with a size of 1.915 MB and 6,985 transactions.[^imp-45-3] Bitcoin Cash became tradeable on exchanges shortly after the fork, according to an IRS Chief Counsel memorandum quoted by Degrees of Satoshi.[^imp-45-3]

## Technology

The fork was time-based. It activated once the median time past of the chain tip reached the activation time. The specification says the design moved from a block-height fork to a time-based one because of miner requests.[^1]

The specification required blocks of up to 1,000,000 bytes to follow existing rules. Above that size, it required the user to configure a fork EB value of at least 8,000,000 bytes, citing miners' past willingness to support that size.[^1] The fork block had to exceed 1,000,000 bytes, which the specification says prevents a reorganisation of the forked chain back to the original chain.[^1] Larger blocks were subject to a maximum single-transaction size of 1,000,000 bytes and a signature-operation limit that scales with block size, calculated as 20000 multiplied by the block size rounded up to whole megabytes.[^1]

For replay protection, the specification requires a mandatory signature shift through the hash type, using an adapted BIP143 hash algorithm for protected transactions.[^1] Degrees of Satoshi describes the new SIGHASH_FORKID flag and notes that without replay protection, a payment on one chain could be copied onto the other by anyone who saw it.[^3] SegWit rules were not carried over.[^1][^3]

A specification dated 9 January 2026 lists four changes to take effect on mainnet: CHIP-2024-12 Pay to Script, CHIP-2021-05 Bounded Looping Operations, CHIP-2025-05 Functions, and CHIP-2025-05 Bitwise operations.[^2]

The specification sets mainnet activation at median time past 1778846400, which is 15 May 2026 at 12:00 UTC.[^imp-45-2] The article does not yet cite a source confirming whether mainnet activation took place on that date.

## Governance

The 2017 specification left activation largely to node operators. The client defaulted to forking, the activation time was user-configurable, and setting it to zero disabled the special rules.[^1] Users had to set a fork EB of at least 8,000,000 bytes and a fork MG greater than 1,000,000 bytes at startup. After activation, users could adjust EB and MG.[^1]

The 2026 specification links each proposed change to a CHIP document and a discussion thread on bitcoincashresearch.org, and sets activation by a median-time-past timestamp.[^2]

## Incidents and controversies

Degrees of Satoshi quotes the Bitcoin Cash website as describing the 2017 divide this way: one side favoured keeping blocks small and positioning Bitcoin as a settlement layer, while the other favoured scaling on-chain to preserve Bitcoin's use as everyday electronic cash.[^3] The specification itself describes its requirements as proposed.[^1]

Degrees of Satoshi reports that Bitmain framed its plan as insurance rather than a project, saying the UAHF would “only be launched in response to a successful BIP148 UASF.”[^3]

The November 2018 dispute produced another persistent split, including Bitcoin SV. The chain split on 15 November 2018 after block 556,766, the last block the two sides shared.[^imp-45-3]

## Timeline

| Date | Event |
| --- | --- |
| 2017-06-14 | Bitmain publishes its UAHF contingency plan, according to Degrees of Satoshi[^3] |
| 2017-07-24 | Version 1.6 of the UAHF Technical Specification is dated[^1] |
| 2017-08-01 | Activation time of 12:20 UTC; the ledger splits at block 478,558; first Bitcoin Cash block mined at about 6:14 p.m. UTC[^1][^3] |
| 2018-11-15 | Bitcoin SV split occurs after block 556,766[^3] |
| 2026-01-09 | Version 1 of the 2026-05-15 network upgrade specification is dated[^2] |

## References

[^1]: [UAHF Technical Specification - Bitcoin Cash upgrade specifications](https://upgradespecs.bitcoincashnode.org/uahf-technical-spec/)
[^2]: [2026-05-15 Network Upgrade Specification - Bitcoin Cash upgrade specifications](https://upgradespecs.bitcoincashnode.org/2026-05-15-upgrade/)
[^3]: [Bitcoin Cash: why Bitcoin split on 1 August 2017, and what happened to both sides after](https://www.degreesofsatoshi.com/encyclopedia/bitcoin-cash-fork-2017/)

[^imp-45-1]: [UAHF Technical Specification - Bitcoin Cash upgrade specifications](https://upgradespecs.bitcoincashnode.org/uahf-technical-spec/)
[^imp-45-2]: [2026-05-15 Network Upgrade Specification - Bitcoin Cash upgrade specifications](https://upgradespecs.bitcoincashnode.org/2026-05-15-upgrade/)
[^imp-45-3]: [Bitcoin Cash: why Bitcoin split on 1 August 2017, and what happened to both sides after](https://www.degreesofsatoshi.com/encyclopedia/bitcoin-cash-fork-2017/)
