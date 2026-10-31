---
title: Lightning Network
ticker: None
category: Layer 2
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Lightning Network

The Lightning Network is a payment-channel network used to transfer
[bitcoin](bitcoin.md) without recording every payment individually on
Bitcoin's blockchain. Participants update channel balances offchain and
can settle through onchain transactions. Joseph Poon and Thaddeus Dryja
described the design in a paper whose January 2016 draft sets out channels,
routed payments, and enforcement using Bitcoin transactions.[^paper]

| | |
|---|---|
| Type | Payment-channel network |
| Settlement asset covered here | Bitcoin |
| Paper authors | Joseph Poon and Thaddeus Dryja |
| Interoperability specifications | BOLTs[^bolts] |
| lnd mainnet beta announcement | 2018-03-15[^beta] |

## Channels and settlement

A channel begins with a funding transaction. Its participants exchange
signed commitments representing how funds can be distributed. Updating
the balance replaces the earlier commitment; the protocol includes a
revocation mechanism to discourage publication of an obsolete state.
Participants can close cooperatively or use an onchain unilateral close
when cooperation fails.[^bolts]

This design keeps routine balance updates away from the global ledger,
while retaining onchain enforcement. It also creates obligations: channel
participants must retain appropriate state and respond to attempts to
settle using revoked commitments. The paper treats monitoring and the
ability to publish transactions within the required time as part of the
security model.[^paper]

## Routing and liquidity

Payments can cross several channels rather than requiring a direct channel
between every sender and recipient. Hashed timelock contracts make a
payment conditional on revealing a secret before a deadline, with a timeout
path if it does not complete. Lightning invoices describe payment requests,
including information such as an amount and expiry.[^bolts]

A channel's total capacity is different from the amount its participants
can send in a particular direction. Outbound liquidity supports sending;
inbound liquidity supports receiving. A payment needs an available route
with sufficient liquidity, so a large aggregate network capacity does not
guarantee that a particular payment will succeed. Lightning Labs documents
rebalancing and channel management as operational tasks for node
operators.[^liquidity]

## Implementations and operational limits

The BOLT specifications define interoperability between implementations.
Lightning Labs announced lnd 0.4-beta on 15 March 2018, its first release
with Bitcoin mainnet support. It targeted developers and technical users
and recommended experimenting with small amounts during that early
phase.[^bolts][^beta]

On 23 October 2026, Lightning Labs announced the mainnet alpha of
Wavelength, a toolkit connecting wallets to Lightning through an Ark-like
settlement layer. Its design lets end users make Lightning payments
without operating their own Lightning nodes or channels; the announcement
covered Bitcoin, with stablecoin support described as future work.[^wavelength]

Watchtowers can monitor for channel breaches while a user's node is
offline. In lnd, the watchtower service must be enabled and configured;
Lightning Labs recommends a separate machine and network for resilience.
It is a monitoring mechanism, not a substitute for available liquidity or
reliable node operation.[^watchtower][^liquidity]

In a disclosure published on 21 September 2026, Lightning Labs described
an invoice-accounting flaw affecting lnd's invoice HTLC interceptor.
A cancelled payment could be recorded as settled, potentially causing an
operator to release goods without receiving payment. The lnd defect was
fixed in version 0.19.0-beta, released on 22 May 2025. A separate trigger
in tapd was patched in version 0.5.1; the disclosure said both fixes were
needed for full protection in the affected combined setup.[^invoice-bug]

## See also

- [Cryptocurrency wallet](cryptocurrency-wallet.md)
- [Smart contract](smart-contract.md)
- [Rollup](rollup.md)
- [Bitcoin block size war](bitcoin-block-size-war.md)

## References

[^paper]: Poon, J. and Dryja, T. (14 January 2016). *The Bitcoin Lightning Network: scalable off-chain instant payments*, draft 0.5.9.2. <https://lightning.network/lightning-network-paper.pdf>
[^bolts]: Lightning specifications. *BOLT #0: Introduction and index*. <https://github.com/lightning/bolts/blob/master/00-introduction.md>
[^beta]: Osuntokun, O. (15 March 2018). *Announcing our first Lightning mainnet release, lnd 0.4-beta!*. <https://lightning.engineering/posts/2018-03-15-lnd-beta/>
[^liquidity]: Lightning Labs. *Understanding liquidity*. <https://docs.lightning.engineering/the-lightning-network/liquidity/understanding-liquidity>
[^watchtower]: Lightning Labs. *Configuring watchtowers*. <https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower>
[^wavelength]: Lightning Labs (23 October 2026). *Wavelength mainnet launch*. <https://lightning.engineering/posts/2026-10-23-wavelength-mainnet-launch/>
[^invoice-bug]: Lightning Labs (21 September 2026). *LND/TAPD: cancelled HTLC marked settled*. <https://security.lightning.engineering/2026/09/21/lnd-tapd-cancelled-htlc-marked-settled.html>
