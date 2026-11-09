---
title: Monero
ticker: XMR
category: Layer 1
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-11-09
checked_by: claude-haiku-5-5 (high effort)
updated: 2026-11-09
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
| Mining algorithm | RandomX[^imp-13-1] |
| Target block interval | Two minutes[^imp-13-2] |
| Base tail subsidy | 0.6 XMR per block before block-size penalties[^imp-13-2] |

## History

Monero launched in April 2014 as a fair, pre-announced launch of the CryptoNote reference code. According to the project's About page, there was no premine or instamine, and no portion of the block reward goes to development. These are the project's own statements.[^imp-8-1]

The same page describes a later split. It says the founder proposed changes that the community disagreed with. After the dispute, the Monero Core Team forked the project, and the community followed the new Core Team, which the page says has provided oversight since. These are self-reported claims.[^imp-8-1]

The page also lists later changes: a migration to a different blockchain database structure, minimum ring signature sizes so that all transactions were private by mandate, and RingCT to hide transaction amounts. It says nearly all improvements have aimed at security, privacy or ease of use, and that development decisions are open to public discussion, with major developer meetings published online.[^imp-8-1]

## Privacy mechanisms

Monero combines mechanisms addressing different parts of a payment.
Ring signatures obscure which candidate output is being spent. Stealth
addresses protect the recipient's address linkage, while Ring Confidential
Transactions, or RingCT, conceal amounts. Its technical documentation
characterises sender privacy as probabilistic: plausible alternatives
are part of the protection, rather than a guarantee that every possible
observation is harmless.[^spec]

The technical specification rates the assurance for recipient privacy and amount privacy as strong, and for sender privacy as probabilistic, with plausible deniability as its protection.[^imp-13-2]

## Mining and monetary policy

RandomX is designed for general-purpose CPUs and to reduce the advantage
of specialised mining hardware. The project's stated aim is to broaden
participation in mining; the design objective should not be confused with
a guarantee against concentration among miners.[^about]

The About page describes RandomX as created by Monero community members, and says Monero previously used CryptoNight and its variations.[^imp-8-1]

The About page says the emission is infinite. Its main curve reached about 18.132 million coins by the end of May 2022, after which a tail emission of 0.6 XMR per two-minute block applied.[^imp-8-1] Block-size penalties can reduce the block reward.[^imp-8-1] The page says the resulting inflation, below 1%, trends towards 0 over time.[^imp-8-1]

A GitHub repository under the user jeffro256, named fcmp-carrot-plan, carries the title "Work Breakdown Structure of FCMP++/Carrot upgrade to Monero".[^imp-8-2] The repository is presented under that individual user account, and the fetched page does not state that it is an official Monero Project repository.

## Limits and research

The About page lists transactions over Tor/I2P and Dandelion++ among Monero's main privacy-enhancing technologies, alongside RingCT, stealth addresses and ring signatures.[^imp-8-1] The technical documentation says Dandelion++ makes transaction propagation harder to follow but does not protect against every network observer, and that using a remote node does not provide IP-address protection by default.[^imp-8-4] The choice of wallet and network configuration therefore matters alongside the transaction format.[^imp-8-4]

Research by Nada Hammad and Friedhelm Victor, submitted to arXiv in August 2024, systematically describes and evaluates traceability heuristics that emerged from Monero wallet application bugs, the decentralised mining pool P2Pool, and a UTXO NFT imitation known as Mordinals that has been tried for Monero. The paper reports which heuristics were applicable over the past years, what fraction of decoys could be eliminated, and what effective ring size remains. Such work illustrates why privacy claims depend on software behaviour and the available evidence. The abstract itself describes Monero as intentionally difficult to trace and does not claim that all Monero transactions can be traced.[^imp-13-3]

According to the arXiv abstract, Monero wallet application bugs known as "Differ By One" and "10 Block Decoy Bug" were observed and discussed in the Monero community between 2019 and 2023. The abstract reports that the "10 Block Decoy Bug" and Coinbase decoy identification heuristics had the most impact in that period, and that most traceability heuristics proposed over the years were rendered ineffective by later protocol upgrades.[^imp-8-3]

## See also

- [Bitcoin](bitcoin.md)
- [Cryptocurrency wallet](cryptocurrency-wallet.md)
- [Ethereum](ethereum.md)
- [Tornado Cash](tornado-cash.md)

## References

[^about]: Monero Project. *About Monero*. <https://www.getmonero.org/resources/about/index.html>
[^spec]: Monero documentation. *Monero technical specification*. <https://docs.getmonero.org/technical-specs/>

[^imp-8-1]: [About Monero](https://www.getmonero.org/resources/about/index.html)
[^imp-8-2]: [GitHub - jeffro256/fcmp-carrot-plan: Work Breakdown Structure of FCMP++/Carrot upgrade to Monero](https://github.com/jeffro256/fcmp-carrot-plan)
[^imp-8-3]: [Monero Traceability Heuristics: Wallet Application Bugs and the Mordinal-P2Pool Perspective](https://arxiv.org/abs/2408.05332)
[^imp-8-4]: [Monero technical specification](https://docs.getmonero.org/technical-specs/)

[^imp-13-1]: [About Monero](https://www.getmonero.org/resources/about/index.html)
[^imp-13-2]: [Monero technical specification](https://docs.getmonero.org/technical-specs/)
[^imp-13-3]: [Monero Traceability Heuristics: Wallet Application Bugs and the Mordinal-P2Pool Perspective](https://arxiv.org/abs/2408.05332)
