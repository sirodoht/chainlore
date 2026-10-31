---
title: Bybit
ticker: None
category: Exchange
written_by: GPT-6-Astra high
status: ai-fact-checked
checked: 2026-10-31
checked_by: GPT-6-Astra high
updated: 2026-10-31
---

# Bybit

Bybit is a cryptocurrency exchange whose products include perpetual and
expiry contracts. The company's history dates its launch to 2018 and
identifies a BTCUSD inverse perpetual as its initial contract. Its
exchange operations also involve custody of customer assets, including
the Ethereum wallet targeted in a major theft in February 2025.[^about][^contracts][^timeline]

| | |
|---|---|
| Type | Cryptocurrency exchange |
| Launch | 2018, according to Bybit |
| Co-founder | Ben Zhou[^timeline] |
| Product example | USDT perpetual and expiry contracts |
| EU crypto-service entity | Bybit EU GmbH |
| Major security incident | February 2025 theft, approximately $1.5 billion[^fbi] |

## Trading and margin

Bybit's contract documentation distinguishes trading fees from funding
payments. Perpetual contracts exchange funding between long and short
positions at scheduled intervals, while expiry contracts have a
settlement date. Maximum leverage varies by instrument and position
size; the exchange applies risk limits and maintenance-margin
requirements.[^contracts]

The choice of margin mode changes which balances support a position.
Isolated margin allocates collateral to an individual position, whereas
cross margin uses eligible balances across the trading account.
Liquidation rules and mark prices are therefore important to the
operation of these products. A trader's last execution price is not
necessarily the reference used to trigger liquidation.[^contracts]

## The February 2025 theft

On 21 February 2025, assets worth approximately $1.5 billion were stolen
from Bybit. In a public notice five days later, the FBI attributed the
theft to North Korea and identified the activity as TraderTraitor.
The attribution is the FBI's assessment.[^fbi]

BlockSec's technical analysis describes a malicious upgrade of the Safe
multisignature wallet used by Bybit. Signers were deceived into approving
a transaction that changed wallet logic, allowing the attacker to take
control and drain the assets. The attack illustrates how multiple
signatures can still authorise a malicious action if signers rely on
misleading transaction information.[^analysis][^forensics]

Bybit's published timeline states that it processed withdrawals during
the response and covered the resulting ETH shortfall through partner
support, deposits, loans, and purchases. Those are the company's account
of its response. Restoring an exchange's available assets is a different
measure from recovering the original stolen funds.[^timeline]

## Entities and regulation

Austria's Financial Market Authority granted Bybit EU GmbH authorisation
under the EU's Markets in Crypto-Assets Regulation on 28 May 2025. The
notice lists custody, exchange for money or other crypto-assets,
placement, and transfer services. It is an authorisation for a named
entity and specified services, rather than a blanket approval of every
Bybit-branded product worldwide.[^fma]

Bybit's international derivatives documentation separately restricts
access by jurisdiction and requires identity verification. Availability
of a website or a familiar brand name consequently does not establish
that the same contract is available through every regional
entity.[^contracts]

The FMA separately licensed Bybit Payments GmbH as an electronic-money
institution on 4 August 2026, authorising electronic-money issuance and
specified payment services. This is a different legal entity and licence
from Bybit EU GmbH's crypto-asset service authorisation.[^payments][^fma]

## Timeline

| Date | Event |
|---|---|
| 2018 | Bybit launches |
| 2025-02-21 | Ethereum wallet theft |
| 2025-02-26 | FBI publishes its North Korea attribution |
| 2025-05-28 | Austrian authorisation for Bybit EU GmbH |
| 2026-08-04 | Austrian electronic-money licence for Bybit Payments GmbH |

## See also

- [Binance](binance.md)
- [Coinbase](coinbase.md)
- [Cryptocurrency wallet](cryptocurrency-wallet.md)
- [MiCA](mica.md)

## References

[^about]: Bybit. *About Bybit*, company history. <https://www.bybit.global/en/promo/global/aboutus>
[^contracts]: Bybit Help Center. *FAQ — USDT Perpetual and Expiry Contracts*. <https://www.bybitglobal.com/en/help-center/article/FAQ-USDT-Perpetual-and-Expiry-Contracts>
[^timeline]: Bybit. *Bybit Security Incident: Timeline of Events and FAQs*. <https://www.bybit.global/en/learn/this-week-in-bybit/bybit-security-incident-timeline>
[^fbi]: FBI (2025-02-26). *North Korea Responsible for $1.5 Billion Bybit Hack*. <https://www.ic3.gov/PSA/2025/PSA250226>
[^analysis]: BlockSec (2025-02-25). *Bybit $1.5B Hack: In-Depth Analysis of the Malicious Safe Wallet Upgrade Attack*. <https://blocksec.com/blog/bybit-1-5-b-hack-in-depth-analysis-of-the-malicious-safe-wallet-upgrade-attack>
[^fma]: Austrian Financial Market Authority (2025-05-30). *Granting of Authorisation Bybit EU GmbH*. <https://www.fma.gv.at/en/granting-of-authorisation-bybit-eu-gmbh/>

[^forensics]: Sygnia (2025-03-16). *Bybit — What We Know So Far*. <https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/>
[^payments]: Austrian Financial Market Authority (2026-08-04). *Konzessionserteilung Bybit Payments GmbH*. <https://www.fma.gv.at/konzessionserteilung-bybit-payments-gmbh/>
