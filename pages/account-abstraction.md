---
title: Account abstraction
ticker: None
category: Infrastructure
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# Account abstraction

Account abstraction allows blockchain accounts to use programmable
validation rules. In Ethereum, this expands beyond the traditional
model in which an externally owned account authorises transactions
through a private-key signature. It can support alternative signing
policies, recovery arrangements, and different ways to pay transaction
fees.[^4337][^roadmap]

| | |
|---|---|
| Purpose | Programmable account authorisation |
| ERC-4337 mechanism | UserOperations, bundlers, and an EntryPoint |
| Optional fee sponsor | Paymaster |
| EIP-7702 mechanism | Code delegation by an externally owned account |
| Pectra activation | 7 May 2025 |

## Programmable policies

A wallet can require extra approvals for a large transfer, restrict
transactions to selected destinations, or provide backup keys for
recovery. These are examples of policies that account code can enforce;
account abstraction does not give every wallet the same recovery or
permission system. Ethereum's roadmap describes such flexibility as a
way to improve both security and usability.[^roadmap]

Batching can combine related actions, such as approving a token and
then spending it, in one atomic transaction. Sponsorship allows another
party to cover fees, while restricted permissions can let an application
perform a narrow set of actions without receiving unrestricted account
control.[^7702]

## ERC-4337

ERC-4337 defines a route to account abstraction that does not require
changes to Ethereum's consensus rules. A user submits a UserOperation,
an instruction object processed by supporting infrastructure. A
bundler includes one or more operations in a regular transaction that
calls the EntryPoint contract.[^4337]

The account's code validates the operation. An optional paymaster can
sponsor its execution, with fees charged against a deposit held through
the EntryPoint. Sponsorship changes who pays; execution still consumes
gas. Bundlers validate operations before including them, and the
specification addresses denial-of-service risks from account and
paymaster behaviour.[^4337]

## EIP-7702

EIP-7702 takes a complementary approach: an externally owned account
can authorise delegation to contract code while retaining its address.
The delegation persists beyond the transaction that installs it and
can be replaced or cleared with another valid authorisation. Its
specified uses include batching, sponsored fees, and restricted
sub-keys.[^7702]

Ethereum activated EIP-7702 in the Pectra upgrade on 7 May 2025.
ERC-4337 and EIP-7702 are distinct mechanisms: the former describes
operation processing through contracts and bundlers, while the latter
changes the protocol to permit account-code delegation.[^pectra][^4337][^7702]

## Security considerations

Programmable authority also makes the chosen code security-critical.
EIP-7702 warns that a poorly implemented delegate can give an attacker
near-complete control of an account. Its security discussion includes
replay protection and signing the intended transaction parameters.
Additional features therefore need correct implementation and clear
authorisation; installing delegation alone does not provide a recovery
policy or make an account safe.[^7702]

## See also

- [Cryptocurrency wallet](cryptocurrency-wallet.md)
- [Safe](safe.md)
- [Multisignature wallet](multisignature-wallet.md)
- [Ethereum](ethereum.md)

## References

[^4337]: Buterin, V., et al. *ERC-4337: Account Abstraction Using Alt Mempool*. <https://eips.ethereum.org/EIPS/eip-4337>
[^7702]: Buterin, V., Wilson, S., Dietrichs, A., and lightclient. *EIP-7702: Set Code for EOAs*. <https://eips.ethereum.org/EIPS/eip-7702>
[^roadmap]: Ethereum documentation. *Account abstraction*. <https://ethereum.org/roadmap/account-abstraction/>
[^pectra]: Ethereum documentation. *Pectra*. <https://ethereum.org/roadmap/pectra/>
