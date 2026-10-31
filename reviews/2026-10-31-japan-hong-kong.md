# Japan Payment Services Act and Hong Kong Stablecoins Ordinance fact-check

Checked 2026-10-31 by **GPT-6-Astra high**, independently of the original
**Opus 5.5 High** writing pass. Original `written_by` credits are preserved.
The checker also performed the substantive corrections recorded here.

Checker attribution comes from the coordinating agent's inspection of the
current session runtime record: thread
`01a1921e-8156-76e1-a4cb-5e96899f237e`, rollout
`/Users/sirodoht/.codex/sessions/2026/10/31/rollout-2026-10-31T13-20-35-01a1921e-8156-76e1-a4cb-5e96899f237e.jsonl`,
whose latest `turn_context` identifies `gpt-6-astra` and effort `high`.
This full-history subagent inherited that configuration without an override.
This is runtime evidence, not an inference from the Codex application name.

Scope: [Japan](../pages/japan-payment-services-act.md) and
[Hong Kong](../pages/hong-kong-stablecoins-ordinance.md) only. UK, Binance,
Satoshi and all other articles were left to other agents. No commits,
deployment or shared automation edits were made by this checker.

## Method and result

Read AGENTS.md and POLICY.md, then both entire articles. Checked lead,
infobox, every factual paragraph and list item, and every timeline row
against live retrieved sources. Opened all 49 retained reference URLs and
read their relevant material; checked every final footnote against the
claim it supports. Searched current regulatory and issuer developments
through 31 October 2026, including FSA legislative records, the HKMA
register, bank announcements and October press coverage. Re-read the
corrected article bodies, tables and timelines after the final substantive
edits. No remaining factual errors were identified in that pass.

The final local citation audit found 23 unique definitions for Japan and
26 for Hong Kong, with no missing definitions, unused definitions or
uncited factual prose paragraphs. The formerly uncited substantive bullet
items now each carry their own footnote. Infobox and timeline entries
repeat supported body claims; Hong Kong timeline dates more precise than
the body have explicit citations. Navigation-only See also items are not
factual assertions.

Both articles now carry `status: ai-fact-checked`, `checked: 2026-10-31`,
and the checker attribution above. The coordinating agent is responsible
for the required combined static build and `scripts/check.py` run after
all parallel edits; those integration results are recorded separately.
This checker did not build into the shared `dist` directory while other
agents were editing.

## Japan: corrections and evidence

- Separated the 2017 crypto-exchange registration regime from the stablecoin
  framework effective in 2023; the original lead incorrectly dated both to
  2017.
- Corrected the Act's enactment to **17 June 2009**, distinguishing
  **24 June promulgation**. The FSA's original order-summary PDF explicitly
  gives both dates. Corrected the infobox and timeline accordingly.
- Distinguished the G7's call for appropriate regulation from the FATF
  recommendation for registration/licensing, rather than attributing the
  latter to both.
- Added references to every 2019-reform and issuer-type bullet.
- Removed a misleading assertion that permitting private stablecoins
  meant Japan chose them instead of pursuing a CBDC.
- Confirmed **1 June 2026** as the effective date of the 2025 amendment and
  its implementing orders. The original article said this could not be
  confirmed. The FSA's 22 May 2026 notice, section 3, states the date.
- Updated the original all-bank-deposit trust-asset requirement with the
  2025 amendment's permission for certain government bonds and cancellable
  term deposits, subject to limits and principal-protection conditions.
- Added the FSA's own 221st-Diet record confirming the July 2026 enactment;
  retained the distinction between enactment and later commencement.
  Described the higher criminal penalties as provisions of the new law,
  not as already-operative penalties.
- Replaced the inaccessible Crypto Briefing re-report with the original
  NADA NEWS interview of JPYC chief executive Noritaka Okabe. Precisely
  described the limit he criticised as applying to issuance/redemption.
  Removed a redundant pre-launch approval forecast now superseded by
  JPYC's actual launch.
- Replaced a Decrypt re-report of the USDC plans with Circle's announcement,
  keeping first-status claims attributed and the March 2025 plans dated.
- Added the banks' **16 October 2026** announcement of their **17–23 July**
  proof of concept. The draft's generic statement that no launch report
  was found missed this material implementation development. Distinguished
  the completed trial from still-planned commercial deployment.
- Repaired source URLs to the successfully opened canonical host/path
  where necessary.

Source coverage, using the footnote identifiers in the final article:

| Sources opened | Coverage checked |
|---|---|
| `act` — official Japanese Law Translation, explicitly the 2020 version | Act number, purpose, original business categories, crypto-asset definition and exclusions, exchange-service definition, registration, delegation to FSA and Local Finance Bureaus; infobox text-version qualification |
| `fsa-2009` — FSA order-summary PDF | 17 June enactment and 24 June promulgation; background and timeline |
| `fsa-slides` — 7 December 2022 FSA presentation | Mt. Gox and Coincheck context and attributed loss figures, G7/FATF distinctions, 2016/2019/2022 reforms, 95% offline custody, trust/user protections, fiat and algorithmic stablecoin categories, issuer routes and original backing rules, intermediary proposals explicitly dated to 2022 |
| `fsa-2017` — FSA registration screening PDF | 1 April 2017 start, Local Finance Bureau process, 11 registered and 19 under examination at September end |
| `kl-gates` — named law-firm analysis | 2018 inspections and study meetings, 31 May/7 June 2019 dates, terminology, custody, derivatives, tokenised rights and unfair-trading changes, absence of insider-trading prohibition at that stage |
| `cc-2022` — Clifford Chance analysis | Diem/Terra context, electronic-payment-instrument scope, issuer restrictions, no DLT requirement, algorithmic exclusions and historically proposed treatment of foreign coins |
| `fsa-wr540` | 2022 promulgation and 2023 finalisation/commencement; criminal-proceeds-law status and travel rule |
| `fsa-wr642`, `fsa-wr688` | 2025 law and cross-border collection, May 2026 orders and foreign trust-beneficial-interest expansion |
| `fsa-2026-orders` | Actual June 2026 commencement, intermediary registration and permissible backing changes |
| `chambers` | New intermediary category, stablecoin/crypto classification, Type II issuance/redemption cap; used as explanatory legal analysis, not a replacement for the newer FSA commencement notice |
| `amt-2026` | April bill approval/submission, four-pillars description, FIEA migration and crypto-only deletions, remaining subordinate legislation and compliance costs |
| `fsa-221`, `adnkronos`, `coindesk-jul` | July 15 enactment (primary corroboration), upper-house approval, new penalties and insider-trading rules; reported future commencement and tax timetable remain attributed forecasts |
| `block-jpyc` | August registration, October 27 launch, company's backing claim and The Block's first-status description |
| `nada-jpyc` | Original October 27 interview: circulation below internal goal, issuance/redemption friction; no volatile circulation balance retained |
| `block-sbi-usdc`, `circle-usdc` | March 4 registration announcement, March 12 beta, planned March 26 full service and exchange plans; first-status attributed to issuers |
| `block-jpysc` | June 24 launch, issuer/distributor roles, attributed first status, lack of funds-transfer-type limits and initial account restriction |
| `block-megabanks`, `megabanks-june` | June 10 trust structure and FY2026 commercial target; November 2025 regulatory test support |
| `megabanks-oct` | October 16 release, July 17–23 trial, statutory trust-beneficiary-right structure, participating firms and cross-border use case; practical deployment still prospective |

Key newly added primary sources:
[FSA commencement notice](https://www.fsa.go.jp/news/r7/sonota/20260522/20260522.html),
[FSA 2009 dates](https://www.fsa.go.jp/news/21/kinyu/20091207-1/1-1.pdf),
[FSA Diet record](https://www.fsa.go.jp/common/diet/221/index.html),
[October megabank release](https://www.bk.mufg.jp/global/newsroom/news2026/pdf/newse1016_1.pdf).

## Hong Kong: corrections and evidence

- Checked the full gazetted ordinance, particularly sections 2–17 and
  Schedules 2 and 7. Replaced an unsupported claim of a 10 September 2026
  consolidated-text version with the actual gazetted text and its
  publication identity.
- Clarified that the issuance perimeter is issuance **in the course of
  business**, including HKD-referenced offshore issuance. Marketing targets
  the **Hong Kong public**, even if conducted elsewhere.
- Completed the statutory stablecoin definition with electronic
  transfer/storage/trading, unit-of-account/store-of-value and the
  alternative of a similar information repository to a distributed ledger.
- Tied applicant company status to the Companies Ordinance definition.
- Added the crucial requirement that issuance must not be prohibited by
  section 8 for the professional-investor offering exception to apply.
- Added the approved equivalent-financial-resources alternative to the
  capital infobox. Corrected the other-business-consent rule: it applies
  to non-authorised-institution licensees, rather than automatically to
  banks. Included the stablecoin manager in fit-and-proper requirements.
- Clarified when the transitional undertaking takes effect (upon provisional
  licensing) and the closing-down exception.
- Replaced secondary sources for first reading, the joint venture,
  counterfeit-token warning, HSBC naming and HSBC launch with primary
  LegCo, HKMA and issuer material. Kept The Block for HashKey's reported
  first mint/redemption, which adds detail to the issuer release.
- Replaced a false **3 October 2025** warning date with **24 September**,
  derived from the SCMP's 25 September report of the Wednesday statement.
  Removed the weak CoinCentral source and the unnecessary named-issuer
  allegation; retained only what the visible SCMP report supports.
- Removed unsupported assertions about firms' responses to the FT report
  and unverified confirmations. Kept the underlying reporting explicitly
  attributed to the FT's unnamed sources via The Block.
- Removed the volatile HSBC reserve snapshot and inaccessible-source-only
  technology/deposit-protection/attestation assertions. Replaced them with
  HSBC's directly verifiable launch scope and prospective bank-app and
  investment integrations.
- Replaced an unqualified absence-of-news claim with what the HKMA register
  actually showed on the check date: two licensees. Removed an inference
  about yuan-coin licensing that the entity register alone cannot establish.
- Named the author of the investingLive criticism and kept it explicitly
  as commentary. Added direct citations to every substantive requirements
  bullet and to the more precise early timeline dates.

Source coverage, using final-article footnote identifiers:

| Sources opened | Coverage checked |
|---|---|
| `ord` — LegCo copy of the government gazetted ordinance | Definitions and exclusions (sections 2–4), jurisdiction and marketing (5), licensing/applicants (8, 14–17), offering and professional exception (9), advertising (10), fraud/penalties (8–11); minimum criteria and bank exceptions (Schedule 2); transitional timing and undertakings (Schedule 7) |
| `gia-commence`, `commencement` | May 30 gazettal, June 6 notice, August 1 commencement, L.N. 125 identity and statutory power; professional-investor specification |
| `pr-2025-05` | May 21 passage, legislative purpose, retail-offering and advertising statements |
| `hkma-page` | 2022/2023 discussion-paper chronology, regulatory scope and guideline description |
| `pr-2023-12` | December 27 consultation and sandbox announcement, proposal scope and February 29 deadline |
| `pr-2024-03` | March 12 sandbox launch and purpose |
| `pr-2024-07-sandbox` | July 18 participants, no public funds initially, scam warning |
| `pr-2024-07-concl` | July 17 conclusions, 108 responses and majority support |
| `legco-bill` | Actual December 18 first-reading date |
| `pr-2025-07` | July 29 final guidelines/licensing note, August 1 gazette publication, August/September contact/application dates, no licences yet |
| `pr-2025-08` | August 14 HKMA/SFC market-hype warning, quoted Yue stance and initial licensing expectations |
| `pr-0410`, `insight-2026`, `register` | April 10 grants/effectiveness; 36 applications, selection criteria, Anchorpoint venture partners, policy on further grants; FRS01/FRS02 and April 23 register revision shown at October 31 access |
| `hsbc-pr` | HSBC's April plans for second-half issuance, apps and uses |
| `anchorpoint-launch`, `block-hkdap` | August 12 institutional/professional beta, conditional end-2026 retail ambition, reported HashKey mint/redemption |
| `hkma-fake` | April 28 warning, misleading HKDAP/HSBC tickers and issuers' confirmation that neither had issued regulated coins then |
| `hsbc-name`, `hsbc-launch` | September 30 naming, October 23 PayMe launch, phased wallet activation, 3.3m eligible user base as stated by HSBC, P2P/merchant use, later bank-app/tokenised-fund plans |
| `block-ft` | October 2025 FT account of PBoC/CAC instructions, explicitly sourced and unconfirmed as an announced order; 77 expressions of interest |
| `scmp-yuan` | September 25 publication and Wednesday warning, no licences and offshore-yuan social-media claims; only visible article text used |
| `ledger`, `standard-yue` | July Yue caution about euphoria, initial few licences and share-price bubbles |
| `investinglive-launch` | Eamonn Sheridan's attributed concern about a closed system adding little to PayMe balances |

Key primary replacements:
[Gazetted ordinance](https://www.legco.gov.hk/yr2025/english/ord/2025ord017-e.pdf),
[commencement notice](https://www.legco.gov.hk/yr2025/english/subleg/negative/2025ln125-e.pdf),
[HKMA warning](https://www.hkma.gov.hk/eng/news-and-media/scam-alert/2026/04/20260428-5/),
[Anchorpoint launch](https://anchorpoint.hk/uploads/2026/08/Anchorpoint-commences-institutional-rollout-of-HKDAP-via-Beta-Access-1.pdf),
[HSBC launch](https://www.about.hsbc.com.hk/news-and-media/hsbc-redcoin-launches-today).

## Access and temporal limits

The web reader returned empty or blocked results for some public primary
pages, notably Japan's translated Act, some FSA/HKMA pages, and the LegCo
ordinance PDF. Their substantive text was retrieved directly through
public HTTP requests and read. The LegCo file was successfully downloaded
with system `curl` (269 pages, approximately 1.45 MB), parsed and inspected;
its text matched the gazetted text initially accessible through a mirror.
The mirror is not a retained reference. The e-Legislation landing page
opened but did not expose the statute to the text reader; the article's
legal footnote therefore points to the accessible LegCo government PDF.

The SCMP source exposed its date and the three relevant introductory
paragraphs; no claim depends on unseen paywalled material. References that
could not be opened usefully and were replaceable were removed. The July
Japan law's exact commencement remained unconfirmed in this pass, so the
article preserves that limitation and attributes 2027/2028 expectations to
contemporaneous reporting. Issuer statements and prospective product
launches remain attributed and dated. No human-review status is claimed.

Final local verification: `git diff --check` passed for the two articles and
this review record. Metadata/writer-credit and reference-set assertions
passed. Final article SHA-256 digests at handoff:

- Japan: `552c4334b99686ab253e462c37252a33c6842b8a45a67cf6f624f9a92e42f49e`
- Hong Kong: `46cd701eab16f69d5c7bbe224631a860fc68390c3c3cb4e0265d6ef8f4f12dfc`
