---
title: Tornado Cash
ticker: TORN
category: Infrastructure
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Tornado Cash

Tornado Cash is a cryptocurrency privacy protocol that uses smart-contract
pools and zero-knowledge proofs to obscure the relationship between
deposits and withdrawals. Its documentation describes deposits from one
address and withdrawals to another without publicly identifying the
matching deposit. Its sanctions history and criminal cases against
developers concern different legal questions.[^protocol][^appeal][^doj]

| | |
|---|---|
| Function | Transaction privacy |
| Proof technology | zk-SNARKs |
| Classic pool design | Fixed-denomination deposits |
| Governance token | TORN |
| US sanctions removal | 21 March 2025 |
| Roman Storm retrial | Scheduled for 26 April 2027 under an August 2026 order |

## How the pools work

In the Classic design, depositing creates a private note and a public
commitment recorded in a pool's Merkle tree. A withdrawal uses a
zero-knowledge proof to demonstrate entitlement without revealing which
deposit it spends. A public nullifier hash prevents the same entitlement
from being used twice.[^protocol]

Privacy also depends on the surrounding activity. The project's
documentation identifies pool participation, timing, and withdrawal-fee
payment as relevant factors. A relayer can submit a withdrawal and pay
its gas, reducing the need to fund the receiving address from a linked
account. The cryptographic proof alone therefore does not guarantee
that observers cannot infer a relationship between transactions.[^protocol]

TORN is an ERC-20-compatible governance token. The project's token
documentation describes holders making proposals and voting. Governance
participation is separate from proving ownership of a deposit in a
Classic privacy pool.[^token][^protocol]

## US sanctions and the civil challenge

OFAC sanctioned Tornado Cash in 2022, citing illicit use, including
laundering associated with North Korean hackers. Users challenged
whether the agency's statutory authority extended to its immutable
contracts. On 26 November 2024, the Fifth Circuit held in *Van Loon v.
Department of the Treasury* that the immutable contracts at issue were
not property subject to blocking under the International Emergency
Economic Powers Act.[^appeal]

Treasury announced removal of the economic sanctions against Tornado
Cash on 21 March 2025. That delisting addressed the sanctions designation;
it was not an acquittal of developers in separate criminal
proceedings.[^delisting][^doj]

## Criminal proceedings

On 6 August 2025, a US jury convicted co-founder Roman Storm of
conspiracy to operate an unlicensed money-transmitting business,
according to the Justice Department. Jurors did not reach verdicts on
the money-laundering and sanctions-conspiracy counts. Storm sought
acquittal, arguing that prosecutors had not proved he intended to help
criminals misuse the software.[^doj][^retrialreport]

As of 31 October 2026, the retrial is scheduled for 26 April 2027 under
Judge Katherine Polk Failla's 25 August 2026 order. The order cited
Storm's pending acquittal motion and the need for time to consider
post-trial motions and prepare. The unresolved counts should not be
described as convictions.[^retrial]

In the Netherlands, a court convicted developer Alexey Pertsev of money
laundering on 14 May 2024 and imposed a 64-month prison sentence. He
appealed; The Block reported the filing after confirmation from a court
spokesperson. In October 2026, Decrypt reported that he had been released
to electronic monitoring pending appeal.
This was a separate prosecution under Dutch law, not the US sanctions
challenge.[^dutch][^dutchappeal][^october]

## See also

- [Zero-knowledge proof](zero-knowledge-proof.md)
- [Ethereum](ethereum.md)
- [Smart contract](smart-contract.md)
- [Monero](monero.md)

## References

[^protocol]: Tornado Cash documentation. *How Does Tornado Cash Work?* <https://raw.githubusercontent.com/tornadocash/docs/en/general/how-does-tornado.cash-work.md>
[^token]: Tornado Cash documentation. *TORN*. <https://raw.githubusercontent.com/tornadocash/docs/en/general/torn.md>
[^appeal]: US Court of Appeals for the Fifth Circuit (2024-11-26). *Van Loon v. Department of the Treasury*, No. 23-50669. <https://www.govinfo.gov/content/pkg/USCOURTS-ca5-23-50669/pdf/USCOURTS-ca5-23-50669-0.pdf>
[^delisting]: US Treasury (2025-03-21). *Tornado Cash Delisting*. <https://home.treasury.gov/news/press-releases/sb0057>
[^doj]: US Department of Justice (2025-08-06). *Founder Of Tornado Cash Crypto Mixing Service Convicted Of Knowingly Transmitting Criminal Proceeds*. <https://www.justice.gov/usao-sdny/pr/founder-tornado-cash-crypto-mixing-service-convicted-knowingly-transmitting-criminal>
[^retrialreport]: Reguerra, E. (2026-08-26). *Tornado Cash developer Roman Storm's retrial delayed to April 2027*. Cointelegraph. <https://cointelegraph.com/news/roman-storm-retrial-delayed-april-2027>
[^retrial]: US District Court, Southern District of New York (2026-08-25). *United States v. Storm*, No. 23 Cr. 430, docket 300, order. <https://storage.courtlistener.com/recap/gov.uscourts.nysd.604938/gov.uscourts.nysd.604938.300.0.pdf>
[^dutch]: Anti Money Laundering Centre (2024-06-13). *Ontwikkelaar van Cryptomixer Tornado Cash veroordeeld voor witwassen*, discussing ECLI:NL:RBOBR:2024:2069. <https://www.amlc.nl/ontwikkelaar-van-cryptomixer-tornado-cash-veroordeeld-voor-witwassen/>
[^dutchappeal]: The Block (2024-05-16). *Tornado Cash developer Alexey Pertsev appeals conviction*. <https://www.theblock.co/news/regulation/2024-05-16-tornado-cash-alexey-pertsev-appeals-conviction-294906>

[^october]: Decrypt (2026-10-07). *Prosecutors Cite Bitcoin Fog Ruling Against Roman Storm's Venue Challenge*. <https://decrypt.co/380260/prosecutors-cite-bitcoin-fog-ruling-against-roman-storms-venue-challenge>
