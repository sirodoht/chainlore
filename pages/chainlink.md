---
title: Chainlink
ticker: LINK
category: Infrastructure
written_by: GPT-6-Astra high
status: draft
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-11-25
---

# Chainlink

Chainlink is infrastructure for connecting [smart contracts](smart-contract.md)
to data and services through [oracle](blockchain-oracle.md) networks.
Its original whitepaper, by Steve Ellis, Ari Juels, and Sergey Nazarov,
described a system combining offchain node software with onchain
aggregation. Chainlink announced its Ethereum mainnet launch on
30 May 2019.[^paper][^launch]

| | |
|---|---|
| Type | Oracle infrastructure |
| Original whitepaper | 2017-09-04 |
| Mainnet launch announcement | 2019-05-30 |
| Token | LINK |
| Token standard on Ethereum | ERC-677[^token] |
| Example service | Data Feeds[^feeds] |

## History and design

The 2017 paper proposed distributing oracle work across nodes and sources
to reduce dependence on a single provider. It distinguished the
blockchain's agreement about execution from the separate task of obtaining
external information. The 2019 launch announcement applied this model on
Ethereum.[^paper][^launch]

Chainlink's Data Feeds publish reports such as asset prices, reserve
information, and interest rates. Its documentation describes aggregation
from multiple sources and use in collateral valuation and settlement.
The specific feed determines what is measured; a contract must select
and interpret the relevant report.[^feeds]

By 2026, Chainlink also offered the Cross-Chain Interoperability Protocol
(CCIP) and the Chainlink Runtime Environment (CRE). Its 21 October quarterly
review reported that CCIP 2.0 had gone live in the third quarter and
described CRE coordinating institutional workflows across blockchain
systems.[^q3]

## Offchain reporting

With Offchain Reporting, oracle nodes exchange observations over a
peer-to-peer network and sign an aggregated report. A node submits the
report to an onchain contract, which verifies signatures from the required
quorum. This reduces the number of blockchain transactions compared with
having every node publish its observation separately. Other nodes can
attempt transmission if the scheduled sender fails.[^ocr]

## LINK and service payments

Chainlink documents LINK as the payment and compensation token for its
services. Its payment-abstraction mechanism can accept other forms of
payment and convert them into LINK. The token extends ERC-20 with ERC-677
functionality, including a data payload accompanying a transfer. Token
ownership should be distinguished from the operation of a particular oracle
network.[^token]

## Risks and integration

Chainlink's feed-selection guidance says all feeds have inherent risks.
Thin trading, concentration on one venue, congestion, and changes to an
asset's backing can affect the usefulness of a reported price. Developers
remain responsible for choosing a suitable source and configuring their
application's risk parameters. Aggregation does not remove the need for
those decisions.[^quality]

## Timeline

| Date | Event |
|---|---|
| 2017-09-04 | First Chainlink whitepaper dated[^paper] |
| 2019-05-30 | Ethereum mainnet launch announced[^launch] |
| 2026-10-21 | Quarterly review reports CCIP 2.0 live[^q3] |

### Further milestones, 2021–2025

| Date | Event |
|---|---|
| 2021-04-15 | Chainlink 2.0 whitepaper dated[^imp-64-2] |
| 2021-08-05 | Chainlink Automation announced as live on Ethereum mainnet and open to the public[^imp-64-3] |
| 2022-12-06 | Staking v0.1 early access live on Ethereum mainnet, with general access scheduled for 2022-12-08 and an initial 25M LINK cap[^imp-64-4] |
| 2023-07-17 | CCIP entered Mainnet Early Access on Avalanche, Ethereum, Optimism and Polygon[^imp-64-5] |
| 2025-05-18 | Chainlink's whitepaper index lists an OCR3 paper dated this day, describing it as major scaling, performance and programmability upgrades[^imp-64-2] |

## See also

- [Ethereum](ethereum.md)
- [Aave](aave.md)
- [Blockchain bridge](blockchain-bridge.md)

## References

[^paper]: Ellis, S., Juels, A. and Nazarov, S. (4 September 2017). *ChainLink: a decentralized oracle network*. <https://research.chain.link/whitepaper-v1.pdf>
[^launch]: Nazarov, S. (30 May 2019). *Chainlink: connected consensus on Ethereum*. <https://chain.link/blog/chainlink-connected-consensus-on-ethereum>
[^feeds]: Chainlink. *Data Feeds*. <https://docs.chain.link/data-feeds>
[^ocr]: Chainlink. *Offchain Reporting*. <https://docs.chain.link/architecture-overview/off-chain-reporting>
[^token]: Chainlink. *LINK token contracts*. <https://docs.chain.link/resources/link-token-contracts>
[^quality]: Chainlink. *Selecting quality data feeds*. <https://docs.chain.link/data-feeds/selecting-data-feeds>
[^q3]: Chainlink (21 October 2026). *Chainlink quarterly review: Q3, 2026*. <https://chain.link/blog/quarterly-review-q3-2026>

[^imp-64-2]: [Chainlink 2.0 and the future of Decentralized Oracle Networks](https://chain.link/whitepaper)
[^imp-64-3]: [Chainlink Automation Is Now Live on Mainnet](https://chain.link/blog/chainlink-automation-is-now-live-on-mainnet)
[^imp-64-4]: [Chainlink Staking v0.1 Early Access Is Now Live](https://chain.link/blog/chainlink-staking-early-access-now-live)
[^imp-64-5]: [CCIP Officially Launches on Mainnet](https://blog.chain.link/ccip-mainnet-early-access/)
