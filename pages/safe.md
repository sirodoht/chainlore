---
title: Safe
ticker: SAFE
category: Infrastructure
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# Safe

Safe is a smart-account protocol for Ethereum and compatible networks,
formerly called Gnosis Safe. Its contract-based accounts can require
multiple owners to approve transactions and can support additional
rules through extensions. Safe's history dates the Gnosis Safe product
to 2018 and its separation from Gnosis to 2022.[^history][^accounts]

| | |
|---|---|
| Earlier name | Gnosis Safe |
| Account type | Smart-contract account |
| Standard authorisation | Owners and signature threshold |
| Extensions | Modules and guards |
| Governance token | SAFE |

## Accounts and owners

Safe's account documentation describes an owner list and a threshold:
the minimum number of owner signatures needed for ordinary transaction
execution. A three-owner account can, for example, require two approvals.
Authorised operations can replace owners or change the threshold. The
Safe account itself has no private key; its owners supply the
credentials checked by the contract.[^accounts]

This makes the account distinct from the wallets used to sign for it.
A hardware wallet may control an owner address, while the Safe contract
holds assets and applies the approval policy. Safe's own history
emphasises that Safe is a smart-account system rather than a hardware
wallet.[^history]

## Modules and guards

A module adds an execution route governed by its own logic. Safe's
documentation describes uses including recurring payments, spending
allowances, and recovery. Once enabled, a module can execute through the
module interface without collecting the ordinary owner-signature
threshold for each operation. Safe warns that a malicious module can
take control of an account; extension permissions therefore matter
alongside its owner list.[^modules]

A guard performs checks before and after a Safe transaction. It can
reject a proposed operation or check the resulting state. This also
creates an availability risk: a defective guard can block execution.
Safe's documentation explicitly calls for attention to guard audits and
recovery mechanisms.[^guards]

## Development and governance

According to Safe's account of its development, the project grew out
of a wallet built for Gnosis, introduced the Gnosis Safe smart account
in 2018, and formed a separate ecosystem and SafeDAO in 2022. SAFE is
the ecosystem's governance token. As of October 2026, the Foundation
also describes SAFE staking as securing its Safenet transaction-security
network.[^history][^token]

## Transaction-verification risk

The February 2025 theft from Bybit involved a malicious upgrade to a
Safe wallet. BlockSec's transaction analysis describes several signers
being deceived into authorising the operation. The incident illustrates
that collecting valid signatures does not ensure that signers correctly
understand the action they approve.[^bybit]

## See also

- [Multisignature wallet](multisignature-wallet.md)
- [Account abstraction](account-abstraction.md)
- [Smart contract](smart-contract.md)
- [Bybit](bybit.md)

## References

[^history]: Safe Foundation. *History of Safe*. <https://safefoundation.org/blog/history-of-safe>
[^accounts]: Safe documentation. *Smart Account Concepts*. <https://docs.safe.global/advanced/smart-account-concepts>
[^modules]: Safe documentation. *Safe Modules*. <https://docs.safe.global/advanced/smart-account-modules>
[^guards]: Safe documentation. *Safe Guards*. <https://docs.safe.global/advanced/smart-account-guards>
[^token]: Safe Foundation. *Safe Token*. Accessed 2026-10-31. <https://safefoundation.org/token>
[^bybit]: BlockSec (2025-02-25). *Bybit $1.5B Hack: In-Depth Analysis of the Malicious Safe Wallet Upgrade Attack*. <https://blocksec.com/blog/bybit-1-5-b-hack-in-depth-analysis-of-the-malicious-safe-wallet-upgrade-attack>
