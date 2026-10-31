---
title: Blockchain bridge
ticker: None
category: Infrastructure
written_by: Unknown
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Blockchain bridge

A blockchain bridge is a system for transferring information or representing
assets across different blockchain networks. It provides a way for activity
on one chain to cause a corresponding action on another. Bridges can connect
separate layer 1 networks or a base chain and a
[rollup](rollup.md).[^intro]

| | |
|---|---|
| Type | Cross-chain infrastructure |
| Uses | Asset transfers and messages |
| Example issuer transfer system | Circle's CCTP[^cctp] |
| Example proposed message interface | ERC-5164[^messages] |
| Security dependencies | Verification, contracts, operators, underlying chains[^intro] |

## Assets and messages

A token representing an asset on another chain is not the original asset
on its original ledger. Ethereum's bridge guide uses wrapped bitcoin to
illustrate this distinction: the Ethereum token and native bitcoin belong
to separate networks. The mechanism connecting them introduces its own
custody and redemption assumptions.[^intro]

Not all transfers require a wrapped token or a liquidity pool. Circle's
Cross-Chain Transfer Protocol burns native [USDC](usdc.md) on a source chain
and mints native USDC on a destination chain. Circle documents this as an
issuer-supported burn-and-mint design, distinct from moving a claim backed
by tokens held in a bridge pool.[^cctp]

Bridges can also carry instructions. ERC-5164 proposes interfaces for
dispatching a message on one chain and executing it on another. Its
security requirements include identifying the source chain and sender
and preventing a message from being executed more than once. A common
interface does not prescribe a single verification mechanism for every
implementation. As of 31 October 2026, the proposal is listed as Last Call,
rather than a final standard.[^messages]

## Trust and failures

Ethereum's bridge guide distinguishes systems relying on external operators
from systems that minimise additional trust through verification. It also
recognises intermediate designs. Contract errors, failures of the underlying
chains, and dishonest or compromised operators can affect transfers.[^intro]

For bridges attached to rollups, upgrade permissions and exit mechanisms
are material parts of the design. L2Beat's framework examines whether
privileged actors can block or falsify withdrawals and whether users can
leave before upgrades. A working proof mechanism alone does not describe
all of those powers.[^stages]

## Incidents

On 2 February 2022, an attacker exploited Wormhole's Solana-side verification
process to mint 120,000 wrapped ETH without the corresponding backing.
CertiK's transaction analysis describes a forged message accepted after a
fake account bypassed verification; some of the resulting tokens were then
redeemed for ETH on Ethereum. The incident illustrates how a bridge's
verification failure can create unbacked claims across networks.[^wormhole]

## See also

- [Binance](binance.md)
- [Ethereum](ethereum.md)
- [Solana](solana.md)
- [Arbitrum](arbitrum.md)
- [Smart contract](smart-contract.md)

## References

[^intro]: ethereum.org. *Introduction to blockchain bridges*. <https://ethereum.org/en/bridges/>
[^cctp]: Circle. *Cross-Chain Transfer Protocol*. <https://developers.circle.com/cctp>
[^messages]: Ethereum Improvement Proposals. *ERC-5164: Cross-Chain Execution*. <https://eips.ethereum.org/EIPS/eip-5164>
[^stages]: L2Beat. *Stages framework*. <https://l2beat.com/stages>
[^wormhole]: CertiK (1 August 2022). *Wormhole bridge exploit incident analysis*. <https://www.certik.com/blog/1kDYgyBcisoD2EqiBpHE5l-wormhole-bridge-exploit-incident-analysis>
