---
title: Multisignature wallet
ticker: None
category: Infrastructure
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# Multisignature wallet

A multisignature wallet requires a specified number of authorised
signatures to approve spending or another action. A two-of-three policy,
for example, accepts any two of three designated signers. The policy can
support shared custody, organisational approval, or recovery without
making one key sufficient to move the funds.[^bip11]

| | |
|---|---|
| Common abbreviation | Multisig |
| Policy notation | M-of-N |
| Bitcoin implementation | Spending conditions in scripts |
| Smart-contract implementation | Owner list and signature threshold |
| Operational concern | Signer independence and transaction verification |

## Bitcoin scripts

BIP 11, assigned in October 2011, specified a standard form for
M-of-N-signature Bitcoin transactions. Its motivating examples included
wallet protection services and escrow. A threshold below the full number
of keys permits some signers to be unavailable; requiring every signer
offers no such tolerance.[^bip11]

BIP 16 introduced pay-to-script-hash, which lets a sender pay to a hash
of spending conditions rather than supplying the full conditions when
making the payment. The redeemer provides the script and evidence
needed to satisfy it. P2SH can represent multisignature conditions,
but is a general script mechanism rather than a synonym for
multisig.[^bip16]

Coordinating signatures also requires a way to exchange transaction
information. BIP 174 defines the Partially Signed Bitcoin Transaction
format, or PSBT. It carries the information needed by signers and can
combine partial signatures across software or devices, including offline
signers. A PSBT coordinates authorisation; it does not remove the need
to inspect the proposed transaction.[^psbt]

## Contract accounts

An Ethereum smart-contract wallet can maintain an owner list and enforce
a signature threshold in code. Safe's documented design supports
changing both owners and the threshold through authorised operations.
The account itself is a contract, so its authority is determined by its
code and configuration rather than a single account private
key.[^safe]

Additional execution paths can modify the security model. Safe modules,
for example, can authorise actions under their own rules after being
enabled. Safe warns that a malicious module can take over an account.
Evaluating the displayed owner threshold alone is therefore insufficient
for an account with enabled extensions.[^modules]

## Failure modes

Multiple approvals protect against some individual-key failures, but
cannot establish that the approved action is desirable. BlockSec's
analysis of the February 2025 Bybit incident describes multiple signers
being deceived into approving a malicious wallet upgrade. Valid
signatures were part of the attack path.[^bybit]

The incident illustrates the distinction between independent keys and
independent checks. Signers who all rely on the same misleading interface
can approve the same harmful instruction. Wallet security consequently
depends on what each signer verifies as well as how many signatures the
contract or script requires.[^bybit]

## See also

- [Cryptocurrency wallet](cryptocurrency-wallet.md)
- [Bitcoin](bitcoin.md)
- [Smart contract](smart-contract.md)
- [Bybit](bybit.md)

## References

[^bip11]: Andresen, G. (2011). *BIP 11: M-of-N Standard Transactions*. <https://bips.dev/11/>
[^bip16]: Andresen, G. (2012). *BIP 16: Pay to Script Hash*. <https://bips.dev/16/>
[^psbt]: Chow, A. (2017). *BIP 174: Partially Signed Bitcoin Transaction Format*. <https://bips.dev/174/>
[^safe]: Safe documentation. *Smart Account Concepts*. <https://docs.safe.global/advanced/smart-account-concepts>
[^modules]: Safe documentation. *Safe Modules*. <https://docs.safe.global/advanced/smart-account-modules>
[^bybit]: BlockSec (2025-02-25). *Bybit $1.5B Hack: In-Depth Analysis of the Malicious Safe Wallet Upgrade Attack*. <https://blocksec.com/blog/bybit-1-5-b-hack-in-depth-analysis-of-the-malicious-safe-wallet-upgrade-attack>
