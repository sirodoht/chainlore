---
title: Inter-Blockchain Communication
ticker: None
category: Infrastructure
written_by: GPT-6-Astra high
status: ai-fact-checked
checked_by: GPT-6-Astra high
checked: 2026-10-31
updated: 2026-10-31
---

# Inter-Blockchain Communication

Inter-Blockchain Communication, or IBC, is a protocol for passing
verifiable messages between blockchains. It separates the transport and
authentication of messages from the applications that interpret them.
Applications include token transfers and interchain accounts. The
project dates the original version, now called IBC Classic, to March
2021.[^classic]

| | |
|---|---|
| Abbreviation | IBC |
| Original version | IBC Classic |
| Verification mechanism | Onchain clients of other chains |
| Message carriers | Offchain relayers |
| Token-transfer standard | ICS-20 |
| Later development | IBC v2 and Eureka |

## Clients and relayers

In IBC Classic, each participating chain maintains a client representing
the other chain. The client tracks consensus information and verifies
proofs against it. Connections link clients; channels link particular
applications using those connections. This lets multiple applications
share underlying verification infrastructure.[^clients]

Relayers observe chains and submit transactions carrying messages and
proofs. They also deliver client updates and the handshakes used to
establish communication. The receiving chain verifies the evidence:
correctness does not rest on accepting a relayer's unsupported statement
that an event occurred. Relayers nevertheless matter for liveness,
because messages do not deliver themselves.[^clients]

## Packets and applications

The transport layer handles packets, acknowledgements, and timeouts,
while applications decide what the packet contents mean. A token-transfer
application and an interchain-account application can use the same
underlying protocol without assigning the same meaning to their
messages.[^classic]

ICS-20 specifies fungible-token transfers. In a basic outward transfer,
tokens are escrowed on their source chain and corresponding vouchers
are created on the receiving chain. Returning along that path burns the
vouchers and releases the escrowed tokens. The denomination records the
transfer path, so the route is part of the asset's representation rather
than an incidental detail.[^ics20]

ICS-20 also defines refund handling when a transfer fails or times out.
An error acknowledgement or a valid timeout triggers application logic
to return the relevant tokens. This is a protocol process requiring
verification and execution; it is not an assurance that every transfer
will complete instantly.[^ics20]

## IBC v2 and Eureka

IBC v2 simplifies the protocol while retaining client-based
verification. Cosmos's technical account describes Eureka as a product
combining IBC v2, Skip:Go, and the Cosmos Hub to connect Ethereum and
Cosmos networks. It uses an Ethereum client on the Hub and proofs of
Cosmos Hub consensus verification on Ethereum. The product and the
underlying messaging standard are distinct.[^eureka]

As of 31 October 2026, the project's published history reports expansion
to further EVM environments during 2026, together with Interchain
Fungible Tokens (IFT) and General Message Passing (GMP). These extend
asset-transfer options and contract calls across networks; ICS-20 remains
the specific token-transfer standard described above.[^history][^ics20]

## Security assumptions

Proof verification shifts trust away from relayer honesty toward the
connected chains and their client implementations. A client verifies
according to its particular consensus and proof rules; choosing a
connection therefore also means accepting those assumptions. Relayers'
ability to submit evidence of counterparty misbehaviour is another part
of the design, rather than a substitute for sound consensus and client
code.[^clients][^eureka]

## See also

- [Blockchain bridge](blockchain-bridge.md)
- [Zero-knowledge proof](zero-knowledge-proof.md)
- [Ethereum](ethereum.md)

## References

[^classic]: IBC. *How IBC Classic Works*. <https://ibcprotocol.dev/how-ibc-classic-works>
[^clients]: Interchain Developer Academy. *Transport, Authentication, and Ordering Layer — Clients*. <https://ida.interchain.io/academy/3-ibc/4-clients>
[^ics20]: Interchain Standards. *ICS-20: Fungible Token Transfer*. <https://github.com/cosmos/ibc/tree/main/spec/app/ics-020-fungible-token-transfer>
[^eureka]: Cosmos. *IBC Eureka Technical Walkthrough*. <https://cosmos.network/blog/ibc-eureka-technical-walkthrough>
[^history]: IBC. *About the Inter-Blockchain Communication Protocol*. Accessed 2026-10-31. <https://ibcprotocol.dev/about>
