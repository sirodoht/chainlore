# Protocols, history and culture fact-check — 31 October 2026

Checker and additional substantive writing: **GPT-6-Astra high**. The parent
verified its actual runtime model and effort, and this sixth checking agent
inherited that configuration without an override. The existing drafts were
written before this checking pass; their historical `written_by: Unknown`
credits are preserved. No human-review credit is asserted.

## Scope and method

Completed an independent claim-by-claim pass over Curve, Ethena, MakerDAO and
Sky, Mt. Gox, Lightning Network, Monero, Non-fungible token, and Memecoin.
Coverage includes each lead, infobox, factual body paragraph, and timeline.
Opened and read every retained reference, including the relevant parts of
long specifications and PDFs. Search snippets alone were not treated as
verification. Reread the final article text and checked corrections and new
paragraphs against the sources before adding checker metadata.

Each factual paragraph has citations. Uncited infobox cells repeat cited
body or lead claims; timeline rows have their own citations. Subject claims
and research conclusions remain attributed. Named wrongdoing is supported by
the relevant party's incident statement, governance record, or the Justice
Department's charging announcement; allegations are not described as verdicts.

The current-event sweep ran through 31 October 2026, using project news,
governance forums, security advisories, release announcements, regulator
pages, trustee notices, and targeted searches. A current-event search is
not a guarantee that every possible event has been discovered. The resulting
status is a dated AI fact-check, not an audit of backing assets or software.

## Claim and source coverage

Reference names below are local to each article. The appendix records the
retained URLs that were opened and read.

### Curve

- Lead and infobox: `paper`, `intro`, and `vecrv` verify protocol scope,
  Michael Egorov, the paper's 10 November 2019 date, CRV/veCRV and crvUSD.
- StableSwap: `paper` verifies the intermediate invariant, amplification,
  balanced-reserve price impact, and imbalance behaviour. `intro` covers
  volatile-asset pools. The explanation does not promise an asset's peg.
- Lending: `intro` covers collateralised crvUSD, permissionless Llamalend,
  LLAMMA conversion bands, conversion losses, and possible full liquidation.
- Governance: `vecrv` verifies nontransferability, locks up to four years,
  decay, fees and boosts. `governance` covers gauge weights and cross-chain
  execution; narrowed the latter wording to EVM deployments.
- Incidents and timeline: `compensation` identifies affected July 2023
  pools and the 17 December compensation proposal, including its dollar-value
  caveat. `domain` verifies the 12 May 2025 domain incident and attributes
  the contracts-unaffected account to Curve.
- Added the 29 October 2026 Stellar deployment from `stellar`, including
  Soroban, beta interface and Curve's own first-non-EVM characterisation.
  Did not turn the future FXSwap audit/deployment plan into a live product.

### Ethena

- Lead, infobox and access: `overview`, `ena`, and the launch summary on
  `launch` verify USDe/sUSDe/ENA roles, the stated February 2024 launch,
  and approved-counterparty direct minting/redemption versus secondary trading.
- `mechanism` verifies approximate notional hedging of volatile collateral
  and the different treatment of stable backing. `overview` describes the
  expanded permitted strategy set; this remains attributed and is not a
  claim about independently verified current weights.
- `rewards` verifies discretionary sUSDe accrual, possible zero distributions
  in negative-revenue periods, and the reserve fund's intended role.
- `ena`, `risks`, and `funding` verify governance parameters, Risk Committee
  remit and the stated funding, liquidation, custody and exchange risks.
- Added `q3`: fee-switch approval and the $7.5 billion 14-day average supply
  threshold. Did not conflate approval with activation, or describe the
  proposal as directing 95% of all gross protocol revenue to buybacks.
- Added the Binance incident context and the reported $8.8 million
  unrealised PnL exposure. `binance-incident` supports the incident;
  `binance-exposure` and `tokenpost` report Ethena's statement. `exchange-risk`
  supports only the custody/settlement mechanism, not the current dollar figure.
  The figure remains attributed reporting and is expressly not a confirmed loss.

### MakerDAO and Sky

- `whitepaper`, `usds`, and `sky-token` cover the lead, protocol identity,
  collateral-backed Dai/USDS, vault risk, shared core accounting and transition.
- `usds` verifies ERC-20, upgradeability and bidirectional 1:1 conversion;
  the article does not turn that ratio into a secondary-market price guarantee.
- `liquidation` verifies declining-price auctions and immediate settlement
  versus the older capital-locking bidding model.
- `launch` verifies the 9 September 2024 proposal and historical 24,000:1
  initial ratio. `sky-token` verifies the completed SKY governance transition
  and delayed-conversion penalty; no stale penalty percentage was introduced.
- `governance` covers Chief/Pause/executable proposals. `savings` supports
  sUSDS, variable savings and aggregate-surplus funding, rather than a fixed return.
- `black-thursday` verifies the March 2020 congestion/oracle/liquidation
  account, zero/low bids, vault-holder losses and recapitalisation. The
  compensation poll remains a proposal record, not proof of compensation.
- Checked current Sky news and voting pages, including September penalty
  proposals and October announcements. No factual body correction was needed;
  this was a full pass, not metadata-only validation. A proposed governance
  change was not assumed executed merely because its template existed.

### Mt. Gox

- `filing` verifies operator, Japanese jurisdiction, 25 February closure,
  preliminary 750,000 customer plus 100,000 company BTC figures and cash
  discrepancies. The Bitcoin-bug explanation is explicitly preliminary.
- `recovery` verifies the 7 March discovery and 20 March announcement of
  approximately 200,000 BTC, with the revised roughly 650,000 missing estimate.
- `doj` verifies the two defendants' names, 2023 charging date, alleged
  2011–May 2014 theft and roughly 647,000 BTC. Preserved indictment versus guilt.
- `repayment` verifies the trustee, initial July 2024 BTC/BCH distributions
  and procedural conditions. `deadline` verifies the 16 October 2026 notice,
  the three repayment categories, 31 October 2027 Japan-time deadline and
  exceptions to the description of largely completed repayments.
- Checked the trustee's current official homepage for later notices. The
  existing lead, infobox and timeline correctly reflected the latest extension;
  no body correction was needed after the full pass.

### Lightning Network

- `paper` verifies the lead, authors, January 2016 draft date, offchain
  channels, onchain enforcement, monitoring and response obligations.
- `bolts` verifies funding, commitment/revocation states, cooperative and
  unilateral closure, routing/HTLCs, invoice information and interoperability.
- `liquidity` verifies directional balances, route capacity and rebalancing.
  `beta` verifies 15 March 2018, lnd 0.4-beta, mainnet support and early-use cautions.
- `watchtower` verifies opt-in configuration and separate-machine/network
  guidance; the text does not claim monitoring solves liquidity limitations.
- Added `invoice-bug`: 21 September 2026 disclosure, cancelled-payment invoice
  mismatch and possible delivery of goods without payment. Verified the
  distinct lnd 0.19.0-beta fix of 22 May 2025 and tapd 0.5.1 trigger fix.
  Did not confuse disclosure date with patch date or imply one patch covered
  every affected combined deployment.
- Added `wavelength`: 23 October mainnet alpha, Ark-like settlement, node/channel
  abstraction for end users, Bitcoin support and future stablecoin work.

### Monero

- `about` and `spec` verify April 2014/CryptoNote origins, community leadership
  change, XMR, proof of work, RandomX and the two-minute target.
- `spec` verifies ring signatures, stealth addresses, RingCT, probabilistic
  sender privacy, Dandelion++ limits and remote-node IP exposure. `faq` verifies
  commitment-based balance validation without disclosure of transaction amounts.
- Corrected the absolute 0.6 XMR/block claim in the infobox and monetary
  paragraph: `spec` states block-size penalties. `faq` verifies the
  9 June 2022 tail-emission start and continuing supply. The final text
  distinguishes the base subsidy from realised issuance.
- `research` verifies Hammad/Victor's 2024 wallet-bug and transaction-pattern
  heuristics; retained the limitation against generalising to all transactions.
- Checked current official releases, including 0.18.5.4 on 16 October,
  and `upgrade-plan`. The final text reports the current published ring-signature
  specification and the developer plan's explicit nonbinding qualification;
  it does not assert an activation date or equate testing with mainnet activation.

### Non-fungible token

- `ethereum` and `report` cover the definition, uses and distinction between
  a token record and its associated rights. `721`, `1155`, and `royalties`
  verify the standards and infobox proposal dates.
- `721` verifies ownership, individual/operator approvals, optional token URI
  metadata and address-plus-ID identity. Added the explicit chain scope,
  matching the specification's identifier discussion.
- `1155` verifies mixed fungible/non-fungible types and batch transfers.
- `report` verifies offchain availability/mutability, separate copyright
  ownership/licensing and the limits of provenance. `royalties` verifies
  royalty-information signalling rather than compulsory payment.
- `ethereum`/`721` cover phishing, keys, contract risks and operator authority.
  Checked current SEC materials alongside the March 2024 report; did not add
  a categorical securities-law conclusion about every NFT.

### Memecoin

- `staff` verifies the social/market definition and scope of the February 2025
  staff analysis. `doge` verifies the attributed founders, 6 December 2013,
  Doge inspiration and Reddit tipping history.
- Read the full `research` paper, not only its abstract: corrected the citation
  to named authors and its stated ACM CCS 2026 venue; supplied exact
  14 January 2024–14 January 2026 dataset dates. Platform inputs and all five
  manipulation classes are supported. Results remain limited to the paper's
  data and methods, not assertions that every coin or participant is fraudulent.
- `cftc` and added `cftc-release` verify the mechanism and 2018 advisory date.
  Removed an uncited inventory-accumulation detail from the description.
- `staff` and `response` verify the staff statement's nonbinding status,
  exclusions, other fraud authority and Crenshaw's criticism. `interpretation`
  verifies the March 2026 taxonomy and asset/investment-contract distinction.
- Swept current regulator materials, including the August 2026 Regulation
  Crypto Assets proposal and October SEC updates. Did not treat a proposal
  as a final blanket exemption or expand narrow exemptions to all memecoins.

## Access and evidentiary limits

Ethena's original X statement was not independently retrieved. AMBCrypto's
article has a named reporter and reviewer and reproduces the quoted exposure
statement. TokenPost has a separate named reporter and distinguishes unrealised
exposure from loss, noting the absent measurement time and methodology.
These are separate published reports corroborating that statement's reported
content, not demonstrated independent measurements or proof that their sourcing
was editorially independent. No such independence is claimed in the article.
The primary risk documentation cannot authenticate the current exposure figure.
CryptoBriefing's related page returned an access error and is not retained.

Binance's incident announcement was successfully opened and read during the
source pass, including its 30 October update. Later repeat opens redirected
to the announcements index. Its retained URL therefore has intermittent access
behaviour; the earlier substantive retrieval, separately rechecked by the parent,
supports the incident reference. No claim is based on the empty index response.

Ethena's exchange-failure `.md` endpoint initially failed; the retained
non-`.md` URL returned the substantive documentation and was read. A Moody's
rating page returned no readable body; no claim in the articles relies on it.
PDFs were read as extracted text, including the trustee notices and relevant
Copyright Office report pages. Dynamic project documents represent the versions
retrieved on the check date; no reserve audit, code execution, or transaction-level
reproduction of academic research was performed.

## Verification and handoff

All eight articles now record `ai-fact-checked`, `checked: 2026-10-31`, and
`checked_by: GPT-6-Astra high`; historical writer credits are unchanged.
The final citation-marker audit found no missing, unused or duplicate
definitions. The parent is responsible for the combined static build and
`scripts/check.py` after integration, as required by AGENTS.md and POLICY.md.
This agent did not commit, deploy, run the shared build, or edit other articles.

## Opened reference inventory

The following entries mirror the final article reference lists. Each was
opened and its supporting content read during this pass, with the access
qualifications above.

### curve

- `paper`: Egorov, M. (10 November 2019). *StableSwap — efficient mechanism for stablecoin liquidity*. <https://curve.fi/files/stableswap-paper.pdf>
- `intro`: Curve. *What is Curve?* <https://docs.curve.finance/user/introduction>
- `vecrv`: Curve. *What is veCRV?* <https://docs.curve.finance/user/vecrv/what-is-vecrv>
- `governance`: Curve. *DAO and governance overview*. <https://docs.curve.finance/user/dao/overview>
- `compensation`: Curve governance forum (17 December 2023). *Proposal to recompensate LPs affected by Curve pool exploit*. <https://gov.curve.finance/t/proposal-to-recompensate-lps-affected-by-curve-pool-exploit/9825/>
- `domain`: Curve (19 May 2025). *Curve domain incident*. <https://news.curve.finance/curve-domain-incident/>
- `stellar`: Curve (29 October 2026). *Curve is live on Stellar*. <https://news.curve.finance/curve-is-live-on-stellar/>

### ethena

- `overview`: Ethena. *Ethena overview*. <https://docs.ethena.fi/overview/ethena-overview.md>
- `mechanism`: Ethena. *How USDe works*. <https://docs.ethena.fi/overview/how-usde-works.md>
- `launch`: Ethena. *Website, Introducing Ethena Pay summary*. <https://ethena.fi/>
- `rewards`: Ethena. *Rewards mechanism*. <https://docs.ethena.fi/protocol-overview/rewards-mechanism.md>
- `ena`: Ethena. *ENA*. <https://docs.ethena.fi/overview/ena.md>
- `risks`: Ethena. *Risks*. <https://docs.ethena.fi/protocol-overview/risks.md>
- `funding`: Ethena. *Funding risk*. <https://docs.ethena.fi/protocol-overview/risks/funding-risk.md>
- `q3`: Blockworks Advisory (13 October 2026). *Ethena's July–September 2026 governance update*. Ethena governance forum. <https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857>
- `binance-incident`: Binance (30 October 2026). *Security incident update*. <https://www.binance.com/en/support/announcement/detail/d3306d9dca5243548c813b605e1d1751>
- `binance-exposure`: Njiri, B. (30 October 2026). *'Our collateral resides off-exchange': Ethena downplays $8.8M Binance exposure*. AMBCrypto. <https://ambcrypto.com/our-collateral-resides-off-exchange-ethena-downplays-8-8m-binance-exposure/>
- `tokenpost`: Kim, J. (30 October 2026). *Ethena puts USDe's unrealized Binance exposure at $8.8 million*. TokenPost. <https://www.tokenpost.com/news/business/45230>
- `exchange-risk`: Ethena. *Exchange failure risk*. <https://docs.ethena.fi/protocol-overview/risks/exchange-failure-risk>

### makerdao-sky

- `whitepaper`: Maker/Sky. *Whitepaper*. <https://makerdao.com/da/whitepaper/>
- `usds`: Sky Protocol documentation. *USDS*. <https://developers.skyeco.com/protocol/tokens/usds/>
- `liquidation`: Sky Protocol documentation. *Collateral liquidation*. <https://developers.skyeco.com/protocol/vaults/collateral-liquidation/>
- `launch`: Maker Governance (9 September 2024). *Sky Protocol Launch Season — token and product launch parameter proposal*. <https://vote.makerdao.com/polling/QmTySKwi>
- `sky-token`: Sky.money (18 August 2026). *Understanding the SKY token*. <https://sky.money/blog/understanding-the-sky-token>
- `governance`: Sky Protocol documentation. *Governance overview*. <https://developers.skyeco.com/protocol/governance/ovreview/>
- `savings`: Sky.money. *Sky Savings Rate and product descriptions*. <https://sky.money/>
- `black-thursday`: Maker Governance (6 April 2020). *Vault compensation poll*. <https://vote.makerdao.com/polling/QmWC4qey>

### mt-gox

- `filing`: MtGox (28 February 2014). *Announcement regarding an application for commencement of a procedure of civil rehabilitation*. <https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf>
- `recovery`: MtGox (20 March 2014). *Announcement regarding the balance of Bitcoin held by the company*. <https://www.mtgox.com/img/pdf/20140320-btc-announce.pdf>
- `doj`: US Department of Justice (9 June 2023). *Russian nationals charged with hacking one cryptocurrency exchange and illicitly operating another*. <https://www.justice.gov/archives/opa/pr/russian-nationals-charged-hacking-one-cryptocurrency-exchange-and-illicitly-operating-another>
- `repayment`: Rehabilitation trustee (5 July 2024). *Notice regarding repayment in Bitcoin and Bitcoin Cash*. <https://www.mtgox.com/img/pdf/20240705_01_announcement_en.pdf>
- `deadline`: Rehabilitation trustee (16 October 2026). *Notice concerning change of repayments deadline*. <https://www.mtgox.com/img/pdf/20261016_b3a13e0f-55f6-4653-913b-be80762390e8_announcement_en.pdf>

### lightning-network

- `paper`: Poon, J. and Dryja, T. (14 January 2016). *The Bitcoin Lightning Network: scalable off-chain instant payments*, draft 0.5.9.2. <https://lightning.network/lightning-network-paper.pdf>
- `bolts`: Lightning specifications. *BOLT #0: Introduction and index*. <https://github.com/lightning/bolts/blob/master/00-introduction.md>
- `beta`: Osuntokun, O. (15 March 2018). *Announcing our first Lightning mainnet release, lnd 0.4-beta!*. <https://lightning.engineering/posts/2018-03-15-lnd-beta/>
- `liquidity`: Lightning Labs. *Understanding liquidity*. <https://docs.lightning.engineering/the-lightning-network/liquidity/understanding-liquidity>
- `watchtower`: Lightning Labs. *Configuring watchtowers*. <https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower>
- `wavelength`: Lightning Labs (23 October 2026). *Wavelength mainnet launch*. <https://lightning.engineering/posts/2026-10-23-wavelength-mainnet-launch/>
- `invoice-bug`: Lightning Labs (21 September 2026). *LND/TAPD: cancelled HTLC marked settled*. <https://security.lightning.engineering/2026/09/21/lnd-tapd-cancelled-htlc-marked-settled.html>

### monero

- `about`: Monero Project. *About Monero*. <https://www.getmonero.org/resources/about/index.html>
- `spec`: Monero documentation. *Monero technical specification*. <https://docs.getmonero.org/technical-specs/>
- `faq`: Monero Project. *Frequently asked questions*. <https://www.getmonero.org/get-started/faq/>
- `research`: Hammad, N. and Victor, F. (2024). *Monero traceability heuristics: wallet application bugs and the Mordinal-P2Pool perspective*. <https://arxiv.org/abs/2408.05332>
- `upgrade-plan`: Jeffro256. *FCMP++/Carrot implementation plan*. <https://github.com/jeffro256/fcmp-carrot-plan>

### nft

- `ethereum`: Ethereum.org. *Non-fungible tokens*. <https://ethereum.org/en/nft/>
- `721`: Entriken, W. et al. (24 January 2018). *ERC-721: Non-fungible token standard*. <https://eips.ethereum.org/EIPS/eip-721>
- `1155`: Radomski, W. et al. (17 June 2018). *ERC-1155: Multi token standard*. <https://eips.ethereum.org/EIPS/eip-1155>
- `royalties`: Burks, Z. et al. (15 September 2020). *ERC-2981: NFT royalty standard*. <https://eips.ethereum.org/EIPS/eip-2981>
- `report`: US Copyright Office and USPTO (12 March 2024). *Non-fungible tokens and intellectual property: a report to Congress*. <https://copyright.gov/policy/nft-study/Joint-USPTO-USCO-Report-on-NFTs-and-Intellectual-Property.pdf>

### memecoin

- `doge`: Dogecoin. *The history of Dogecoin*. <https://dogecoin.com/dogepedia/articles/history-of-dogecoin/>
- `staff`: SEC Division of Corporation Finance (27 February 2025). *Staff statement on meme coins*. <https://www.sec.gov/newsroom/speeches-statements/staff-statement-meme-coins>
- `cftc`: CFTC (2018). *Customer advisory: beware virtual currency pump-and-dump schemes*. <https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/beware_virtual_currency_pump_dump.html>
- `research`: Szwajcok, N. et al. (September 2026). *Meme coin factories: uncovering large-scale manipulations on pump.fun*. Author version of an ACM CCS 2026 paper. <https://arxiv.org/html/2609.10246v1>
- `response`: Crenshaw, C. (27 February 2025). *Response to staff statement on meme coins: what does it meme?*. <https://www.sec.gov/newsroom/speeches-statements/crenshaw-response-staff-statement-meme-coins-022725>
- `interpretation`: SEC (17 March 2026). *SEC clarifies the application of federal securities laws to crypto assets*. <https://www.sec.gov/newsroom/press-releases/2026-30-sec-clarifies-application-federal-securities-laws-crypto-assets>
- `cftc-release`: CFTC (15 February 2018). *CFTC issues customer advisory on cryptocurrency pump-and-dump schemes*. <https://www.cftc.gov/PressRoom/PressReleases/7697-18>

Total: 56 retained article reference entries.
