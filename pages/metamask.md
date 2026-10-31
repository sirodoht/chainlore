---
title: MetaMask
ticker: None
category: Infrastructure
written_by: Unknown
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# MetaMask

MetaMask is a [cryptocurrency wallet](cryptocurrency-wallet.md) originally developed
within Consensys. It provides browser-extension and mobile interfaces for
managing accounts and connecting to blockchain applications. Created by
Aaron Davis and Dan Finlay, it launched as a browser extension in July
2016.[^origins][^history][^connect]

| | |
|---|---|
| Type | Self-custodial wallet |
| Original creators | Aaron Davis, Dan Finlay |
| Original developer | Consensys |
| Initial release | July 2016 |
| Interfaces | Browser extension, mobile application |
| Recovery | Secret Recovery Phrase; supported login-based recovery arrangements[^recovery] |

## History and application access

MetaMask's account of its origins describes Davis and Finlay working on
browser-based software before building the wallet. Consensys's historical
timeline places the browser-extension launch in July 2016. The project
provided an interface between an ordinary web browser and Ethereum
applications.[^origins][^history]

Its current developer documentation describes MetaMask Connect as a
connection layer for both the extension and mobile application, with EVM
and Solana integrations. It can connect directly to an installed extension
or use a QR code or mobile deep link. Connecting an application to a wallet
is an interface operation; it does not transfer custody to the application
by itself.[^connect][^custody]

On 9 September 2026, Consensys Software Inc. announced a plan to separate
its consumer business from its protocol and institutional operations.
The existing company would adopt the MetaMask name, while a new Consensys
company would house the latter operations. The announcement expected the
reorganisation to be completed by the end of 2026.[^reorganisation]

## Accounts, recovery, and permissions

MetaMask describes itself as self-custodial: its provider cannot recover
funds when the means of access are lost. Its recovery documentation
distinguishes the Secret Recovery Phrase, which derives wallet accounts,
from the password that protects access on a device. Supported social-login
setups use encrypted, split recovery material and require both the login
account and the MetaMask password.[^custody][^recovery]

Security alerts assess requests using information such as the application
URL, network identifier, and proposed transaction. MetaMask says this data
is shared with its security partners, while recovery phrases and private
keys are not. Alerts inform a user's decision but do not necessarily block
the transaction.[^alerts]

## Incidents and controversies

In April 2023 Consensys disclosed unauthorised access to a third-party
customer-support ticketing provider. It estimated about 7,000 users were
affected among people who submitted personal information between
1 August 2021 and 10 February 2023. Consensys said the incident did not
compromise the security of the wallet extension or mobile application;
the exposure concerned support-ticket data. This distinction matters
because self-custody does not eliminate risks from associated support
services.[^support]

In a notice first issued on 30 September and updated on 1 October 2026,
MetaMask disclosed an incident affecting part of its infrastructure. It
said it had worked with partners to exit affected staking validators as a
precaution, and that its investigation had found no indication that wallets
or customer funds had been affected. The cited update described continuing
containment and verification, rather than a final account of the incident.[^infrastructure]

## Timeline

| Date | Event |
|---|---|
| 2016-07 | Browser extension launches[^history] |
| 2022-07-14 | Founders' retrospective published[^origins] |
| 2023-04-14 | Support-provider incident disclosed[^support] |
| 2026-09-09 | Corporate separation plan announced[^reorganisation] |
| 2026-09-30 | Infrastructure incident disclosed[^infrastructure] |

## See also

- [Non-fungible token](nft.md)
- [Ethereum](ethereum.md)
- [Solana](solana.md)
- [Smart contract](smart-contract.md)
- [Hyperliquid](hyperliquid.md)
- [Account abstraction](account-abstraction.md)

## References

[^origins]: MetaMask (14 July 2022). *How did MetaMask come to life? The origin story, revealed*. <https://metamask.io/news/how-did-metamask-come-to-life-the-origin-story-revealed>
[^history]: Consensys. *Eight years of evolution: the history of Ethereum and Consensys*. <https://consensys.com/blog/eight-years-of-evolution-the-history-of-ethereum-and-consensys>
[^connect]: MetaMask. *MetaMask Connect*. <https://docs.metamask.io/metamask-connect/>
[^custody]: MetaMask. *What is a self-custodial wallet?* <https://support.metamask.io/start/metamask-is-a-self-custodial-wallet>
[^recovery]: MetaMask. *User guide: Secret Recovery Phrase, password, and private keys*. <https://support.metamask.io/start/user-guide-secret-recovery-phrase-password-and-private-keys/>
[^alerts]: MetaMask. *How to manage security alerts to protect your wallet*. <https://support.metamask.io/configure/wallet/security-alerts/>
[^support]: Consensys (14 April 2023). *FAQ: customer support data security incident*. <https://consensys.com/blog/faq-customer-support-data-security-incident>
[^reorganisation]: Consensys (9 September 2026). *Consensys Software Inc. to become two independent companies*. <https://consensys.com/blog/consensys-software-inc-to-become-two-independent-companies-metamask-the-consumer-platform-and-consensys-the-protocols-and-institutional-infrastructure-company>
[^infrastructure]: MetaMask (1 October 2026, including 30 September notice). *User update*. <https://metamask.com/news/user-update>
