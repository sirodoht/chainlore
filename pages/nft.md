---
title: Non-fungible token
ticker: None
category: Culture
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Non-fungible token

A non-fungible token, or NFT, is a blockchain token with an individual
identity rather than interchangeable units. NFTs can represent digital
collectibles, game items, tickets, and other records. On [Ethereum](ethereum.md),
[smart contracts](smart-contract.md) track token ownership and transfers;
the rights associated with a token depend on the application and its
terms.[^ethereum][^report]

| | |
|---|---|
| Abbreviation | NFT |
| Common Ethereum standards | ERC-721; ERC-1155 |
| ERC-721 proposal date | 2018-01-24[^721] |
| ERC-1155 proposal date | 2018-06-17[^1155] |
| Royalty-information standard | ERC-2981[^royalties] |

## Standards and ownership records

ERC-721 specifies how a contract identifies each token, records its owner,
and authorises transfers. A token ID is meaningful together with its
contract address on a given chain: two collections can use the same number
for different tokens. The standard includes individual approvals and operator approval
covering an owner's tokens.[^721]

ERC-1155 supports multiple token types within one contract, including both
fungible and non-fungible assets. Its batch operations allow several token
IDs and amounts to be transferred together. It is therefore a broader
multi-token interface, rather than a requirement that every unit in a
contract be unique.[^1155]

## Metadata and the underlying asset

ERC-721's optional metadata extension provides a token URI that can point
to a description and image resource. This separates the onchain token
record from the material it references. A token can remain transferable
while an external server changes or stops providing the associated
content.[^721][^report]

The 2024 joint report by the US Copyright Office and Patent and Trademark
Office distinguishes ownership of the token from copyright in an associated
work. Buying an NFT does not automatically transfer copyright; a valid
agreement may separately transfer or license rights. A record of a token's
provenance also does not, by itself, establish that its issuer had the
right to use someone else's work.[^report]

## Uses and royalties

Ethereum's documentation lists art, games, event attendance, credentials,
access controls, and domain names among NFT applications. In these uses,
other software interprets the token record and supplies the relevant
experience or entitlement.[^ethereum]

ERC-2981 standardises how a contract reports a royalty recipient and amount
for a proposed sale price. It does not itself force every marketplace to
pay that royalty. The specification describes royalty payment as voluntary,
so reporting royalty information and enforcing a payment are separate
functions.[^royalties]

## Risks

Ethereum's documentation identifies phishing, contract vulnerabilities,
and exposed private keys as NFT security risks. Transfer permissions also
matter: an approved operator can exercise the authority granted by the
contract. These risks concern the token account even when the artwork or
other associated item is stored elsewhere.[^ethereum][^721]

## See also

- [Cryptocurrency wallet](cryptocurrency-wallet.md)
- [MetaMask](metamask.md)
- [Memecoin](memecoin.md)

## References

[^ethereum]: Ethereum.org. *Non-fungible tokens*. <https://ethereum.org/en/nft/>
[^721]: Entriken, W. et al. (24 January 2018). *ERC-721: Non-fungible token standard*. <https://eips.ethereum.org/EIPS/eip-721>
[^1155]: Radomski, W. et al. (17 June 2018). *ERC-1155: Multi token standard*. <https://eips.ethereum.org/EIPS/eip-1155>
[^royalties]: Burks, Z. et al. (15 September 2020). *ERC-2981: NFT royalty standard*. <https://eips.ethereum.org/EIPS/eip-2981>
[^report]: US Copyright Office and USPTO (12 March 2024). *Non-fungible tokens and intellectual property: a report to Congress*. <https://copyright.gov/policy/nft-study/Joint-USPTO-USCO-Report-on-NFTs-and-Intellectual-Property.pdf>
