---
title: Cryptocurrency wallet
ticker: None
category: Infrastructure
written_by: Unknown
status: draft
updated: 2026-10-31
---

# Cryptocurrency wallet

A cryptocurrency wallet is software or a device used to manage keys and
authorise transactions on a blockchain. The assets are recorded on the
network; a wallet supplies the means to control them. Receiving addresses,
transaction signing, and communication with the network can be handled by
different components.[^bitcoin]

| | |
|---|---|
| Type | Key management and transaction software or hardware |
| Functions | Receiving addresses, signing, balance display, network access |
| Examples of interfaces | Mobile applications, browser extensions, hardware devices[^ethereum] |
| Recovery standard | BIP-39 mnemonic seeds, where supported[^bip39] |

## Keys, accounts, and custody

For a conventional key-controlled account, a private key authorises
transactions and the receiving address identifies where assets can be sent.
A wallet interface is distinct from the account: compatible software can
access the same account. Ethereum also has contract accounts, whose authority
is defined by program logic rather than a private key belonging to the
contract itself.[^ethereum][^accounts]

Custody describes who can sign. MetaMask's documentation distinguishes
wallets controlled by the user from services that control keys for
customers. A balance displayed by a hosted service therefore involves trust
in that service. A self-managed wallet instead places responsibility for
signing and recovery with its controller.[^custody]

## Storage and recovery

A hardware wallet separates signing from a networked computer. The computer
can prepare and broadcast a transaction while the device retains the signing
keys. Offline signing reduces exposure of those keys to the connected
machine; the user still needs to verify what is being signed.[^bitcoin]

BIP-39, assigned on 10 September 2013, specifies a mnemonic representation
of computer-generated randomness. Its word sequences, commonly called seed
or recovery phrases, produce a seed for a deterministic wallet. An optional
passphrase changes the resulting seed: a different passphrase produces a
different wallet rather than a password error. The specification does not
describe a way to recover forgotten secrets from an address.[^bip39]

## Applications and permissions

Wallets can display balances, send transactions, and connect accounts to
applications. The interface may manage several accounts or networks, but
the account's assets remain part of the relevant blockchain's state.[^ethereum]

On Ethereum, an ERC-20 approval gives another address a token-spending
allowance. This is distinct from transferring tokens immediately. An
application can subsequently use the allowance through `transferFrom`;
understanding that permission is part of understanding the transaction a
wallet presents.[^erc20]

## Timeline

| Date | Event |
|---|---|
| 2013-09-10 | BIP-39 assigned[^bip39] |
| 2015-11-19 | ERC-20 proposed, including token allowances[^erc20] |

## See also

- [MetaMask](metamask.md)

- [Bitcoin](bitcoin.md)
- [Ethereum](ethereum.md)
- [Smart contract](smart-contract.md)

## References

[^bitcoin]: Bitcoin developer documentation. *Wallets*. <https://developer.bitcoin.org/devguide/wallets.html>
[^ethereum]: ethereum.org. *Ethereum wallets*. <https://ethereum.org/en/wallets/>
[^accounts]: ethereum.org. *Ethereum accounts*. <https://ethereum.org/en/developers/docs/accounts/>
[^bip39]: Bitcoin Improvement Proposals. *BIP-39: Mnemonic code for generating deterministic keys*. <https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>
[^erc20]: Vogelsteller, F. and Buterin, V. (2015). *ERC-20: Token Standard*. <https://eips.ethereum.org/EIPS/eip-20>

[^custody]: MetaMask. *What is a self-custodial wallet?* <https://support.metamask.io/start/metamask-is-a-self-custodial-wallet>
