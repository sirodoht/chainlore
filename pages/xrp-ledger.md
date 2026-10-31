---
title: XRP Ledger
ticker: XRP
category: Layer 1
written_by: GPT-6-Astra high
status: draft
updated: 2026-10-31
---

# XRP Ledger

The XRP Ledger, or XRPL, is a public ledger for payments and asset
exchange, with XRP as its native cryptocurrency. Its validators reach
agreement through a consensus protocol based on trusted validator lists,
rather than competing through mining. The ledger includes an integrated
decentralised exchange.[^consensus][^dex]

| | |
|---|---|
| Native asset | XRP |
| Launch | June 2012[^history] |
| Initial supply | 100 billion XRP[^xrp] |
| Consensus trust structure | Unique Node Lists, or UNLs |
| Protocol changes | Validator-voted amendments |

## Origins and XRP

XRPL's published history identifies David Schwartz, Jed McCaleb, and
Arthur Britto as the engineers who began developing the ledger in 2011.
It launched in June 2012. The company later known as Ripple was formed
afterward; the network, its native asset, and the company are distinct
subjects despite their closely connected histories.[^history]

The initial ledger created 100 billion XRP. Its founders allocated
80 billion to the company, and Ripple later placed a substantial portion
of its holdings into on-ledger escrow. This initial distribution differs
from a system that creates new native coins as mining rewards.[^xrp]

Transaction fees are denominated in XRP and destroyed rather than paid
to validators. Required fees can increase under load, so the existence of
a small reference fee is not a guarantee that every transaction can be
processed immediately at that amount.[^fees]

## Consensus and validator lists

Servers exchange proposals about candidate transactions, then validate
the resulting ledger state. Each server considers votes from its Unique
Node List: validators that, collectively, it trusts not to collude.
This is a selection of whose statements count, rather than a vote weighted
by how much XRP each holder owns.[^structure]

Operators can configure their lists, but the lists need substantial
overlap for servers to agree reliably on the same history. Recommended
list publishers simplify that coordination. XRPL's documentation
acknowledges that publishers have significant influence over which
validators are widely trusted, even though publishing a list is separate
from validating individual transactions.[^unl]

## Exchange and issued assets

The ledger's exchange supports offers to trade XRP and issued tokens.
An offer may execute immediately, remain partially open, or be consumed
by a later trade or cross-currency payment. Auto-bridging can route a
token-to-token exchange through XRP when that produces a better
rate.[^dex]

Issued assets can have issuer-controlled features, including freezes and
authorised trust lines. Those controls concern the particular issued
asset; they should not be confused with XRP's status as the ledger's
native currency. Using a common ledger does not make every token's
issuer obligations identical.[^dex][^xrp]

## Protocol governance

Changes affecting transaction processing are introduced through
amendments implemented in node software. Validators vote on activation;
the documentation specifies more than 80% support maintained for two
weeks. Once enabled, an amendment applies to later ledger versions,
and reversing its effect requires another amendment.[^amendments]

A feature's presence in source code or a software release therefore
does not by itself establish that it is active on mainnet. Validator
votes and the amendment's activation status are part of that
distinction.[^amendments]

## See also

- [Bitcoin](bitcoin.md)
- [Proof of stake](proof-of-stake.md)
- [Automated market maker](automated-market-maker.md)
- [Stablecoin](stablecoin.md)

## References

[^history]: XRP Ledger documentation. *History*. <https://xrpl.org/about/history>
[^xrp]: XRP Ledger documentation. *What is XRP and Why Is It Valuable?* <https://xrpl.org/docs/introduction/what-is-xrp>
[^consensus]: XRP Ledger documentation. *Consensus Protocol*. <https://xrpl.org/docs/concepts/consensus-protocol>
[^structure]: Cohen, D., Schwartz, D., and Britto, A. *Consensus Structure*. <https://xrpl.org/docs/concepts/consensus-protocol/consensus-structure>
[^unl]: XRP Ledger documentation. *Unique Node List (UNL)*. <https://xrpl.org/docs/concepts/consensus-protocol/unl>
[^fees]: XRP Ledger documentation. *Transaction Cost*. <https://xrpl.org/docs/concepts/transactions/transaction-cost>
[^dex]: XRP Ledger documentation. *Decentralized Exchange (DEX)*. <https://xrpl.org/docs/concepts/tokens/decentralized-exchange>
[^amendments]: XRP Ledger documentation. *Amendments*. <https://xrpl.org/docs/concepts/networks-and-servers/amendments>
