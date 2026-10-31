---
title: MetaMask
ticker: None
category: Infrastructure
written_by: Unknown
status: draft
updated: 2026-10-31
---

# MetaMask

MetaMask is a [cryptocurrency wallet](cryptocurrency-wallet.md) developed
within Consensys. It provides browser-extension and mobile interfaces for
managing accounts and connecting to blockchain applications. Created by
Aaron Davis and Dan Finlay, it launched as a browser extension in July
2016.[^origins][^history][^connect]

| | |
|---|---|
| Type | Self-custodial wallet |
| Original creators | Aaron Davis, Dan Finlay |
| Developer | Consensys |
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

## Timeline

| Date | Event |
|---|---|
| 2016-07 | Browser extension launches[^history] |
| 2022-07-14 | Founders' retrospective published[^origins] |
| 2023-04-14 | Support-provider incident disclosed[^support] |

## See also

- [Ethereum](ethereum.md)
- [Solana](solana.md)
- [Smart contract](smart-contract.md)
- [Hyperliquid](hyperliquid.md)

## References

[^origins]: MetaMask (14 July 2022). *How did MetaMask come to life? The origin story, revealed*. <https://metamask.io/news/how-did-metamask-come-to-life-the-origin-story-revealed>
[^history]: Consensys. *Eight years of evolution: the history of Ethereum and Consensys*. <https://consensys.com/blog/eight-years-of-evolution-the-history-of-ethereum-and-consensys>
[^connect]: MetaMask. *MetaMask Connect*. <https://docs.metamask.io/metamask-connect/>
[^custody]: MetaMask. *What is a self-custodial wallet?* <https://support.metamask.io/start/metamask-is-a-self-custodial-wallet>
[^recovery]: MetaMask. *How to secure your Secret Recovery Phrase and password*. <https://support.metamask.io/privacy-and-security/what-is-a-secret-recovery-phrase-and-how-to-keep-your-crypto-wallet-secure>
[^alerts]: MetaMask. *How to manage security alerts to protect your wallet*. <https://support.metamask.io/privacy-and-security/how-to-turn-on-security-alerts/>
[^support]: Consensys (14 April 2023). *FAQ: customer support data security incident*. <https://consensys.com/blog/faq-customer-support-data-security-incident>
