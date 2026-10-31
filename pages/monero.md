---
title: Monero
ticker: XMR
category: Layer 1
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Monero

Monero is a proof-of-work cryptocurrency designed to conceal transaction
participants and amounts on its public blockchain. Its native currency is
XMR. The project's history dates its launch to April 2014, using the
CryptoNote reference code, followed by a community-led change in project
leadership.[^about][^spec]

| | |
|---|---|
| Currency | XMR |
| Launch | April 2014 |
| Consensus | Proof of work |
| Mining algorithm | RandomX[^about] |
| Target block interval | Two minutes[^spec] |
| Base tail subsidy | 0.6 XMR per block before block-size penalties[^spec][^faq] |

## Privacy mechanisms

Monero combines mechanisms addressing different parts of a payment.
Ring signatures obscure which candidate output is being spent. Stealth
addresses protect the recipient's address linkage, while Ring Confidential
Transactions, or RingCT, conceal amounts. Its technical documentation
characterises sender privacy as probabilistic: plausible alternatives
are part of the protection, rather than a guarantee that every possible
observation is harmless.[^spec]

The network must still enforce spending rules. The project's FAQ explains
that cryptographic commitments allow verification that transaction values
balance without publicly revealing the individual amounts. Hiding amounts
therefore does not mean abandoning validation of the currency's accounting
rules.[^faq]

## Mining and monetary policy

RandomX is designed for general-purpose CPUs and to reduce the advantage
of specialised mining hardware. The project's stated aim is to broaden
participation in mining; the design objective should not be confused with
a guarantee against concentration among miners.[^about]

Monero's tail emission began on 9 June 2022, with a base subsidy of
0.6 XMR per block and a target interval of
two minutes. Block-size penalties can reduce the subsidy. Continuing
issuance alongside transaction fees means there is no fixed terminal
supply, while a constant base subsidy represents a declining percentage
of the growing supply.[^faq][^spec]

As of 31 October 2026, the published technical specification still
describes ring signatures. A developer work plan for the proposed
FCMP++/Carrot upgrade explicitly labels its estimated schedule as
nonbinding; it is not an activation commitment.[^spec][^upgrade-plan]

## Limits and research

Blockchain privacy and network privacy are separate concerns. Monero's
technical documentation says Dandelion++ makes transaction propagation
harder to follow, but does not protect against every network observer.
Using a remote node does not provide IP-address protection by default.
The choice of wallet and network configuration therefore matters alongside
the transaction format.[^spec]

Research by Hammad and Victor in 2024 examined tracing heuristics
arising from wallet bugs and identifiable transaction patterns. The paper
studied when these heuristics applied and how they could reduce the number
of plausible decoys. Such work illustrates why privacy claims depend on
software behaviour and the available evidence; it does not establish that
all Monero transactions can be traced.[^research]

## See also

- [Bitcoin](bitcoin.md)
- [Cryptocurrency wallet](cryptocurrency-wallet.md)
- [Ethereum](ethereum.md)
- [Tornado Cash](tornado-cash.md)

## References

[^about]: Monero Project. *About Monero*. <https://www.getmonero.org/resources/about/index.html>
[^spec]: Monero documentation. *Monero technical specification*. <https://docs.getmonero.org/technical-specs/>
[^faq]: Monero Project. *Frequently asked questions*. <https://www.getmonero.org/get-started/faq/>
[^research]: Hammad, N. and Victor, F. (2024). *Monero traceability heuristics: wallet application bugs and the Mordinal-P2Pool perspective*. <https://arxiv.org/abs/2408.05332>
[^upgrade-plan]: Jeffro256. *FCMP++/Carrot implementation plan*. <https://github.com/jeffro256/fcmp-carrot-plan>
