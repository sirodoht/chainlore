# Draft fact-check: markets and chains, 31 October 2026

Independent checking and substantive corrections by **GPT-6-Astra high**.
The parent verified this review agent's runtime session metadata in
`rollout-2026-10-31T16-37-59-01a192d3-3b2c-70b2-9983-f4a384f5cf21.jsonl`:
`agent_path: /root/review_markets`; `turn_context.model: gpt-6-astra`;
`turn_context.effort: high`. This is a separate checking pass, not the
original drafting pass. Original `written_by` credits are preserved.

Method: opened every retained reference, compared each factual paragraph,
infobox entry, and timeline row with live evidence, searched for material
updates through 2026-10-31, and reread the corrected final files. Footnotes
support explanatory deductions as well as directly quoted facts; no model
memory is treated as evidence. Build and repository checker are run by the
parent on the shared batch before publication.

## Automated market maker — complete

- Opened Uniswap v2 and v3 whitepapers, Curve's 2019 StableSwap paper,
  Uniswap's impermanent-loss help page, and ethereum.org's MEV page.
- Lead and infobox: v3 introduction defines pooled algorithmic liquidity,
  AMMs/CFMMs, LPs and smart-contract implementation; named examples and
  pricing designs are explained in the whitepapers. Fee/inventory trade-off
  is supported by the returns source.
- Pool paragraphs: v2 introduction and price-oracle section establish the
  reserve product, fee qualification, reserve-ratio price, arbitrage and
  manipulation/TWAP distinction.
- Curves: StableSwap explanation/figures establish constant-sum-like
  behaviour near parity and constant-product behaviour under imbalance;
  v3 section 2 explicitly establishes capital concentration, one-asset
  inventory outside range, suspended fees and resumption on re-entry.
- Returns: the existing loss help page did not clearly establish the
  comparison with holding or fee offset. Added the opened primary source
  https://blog.uniswap.org/how-liquidity-provision-in-defi-works, section
  “Evaluating LP rewards and mitigating risks,” to support both points.
- MEV: ethereum.org's sandwich and effects sections support transaction
  ordering and worse execution, without implying all swaps are sandwiched.
- Update search found current v4 hooks developments. Added a concise v4
  architecture paragraph, verified against the opened developer overview:
  https://developers.uniswap.org/docs/protocols/overview. Kept this a concept
  article rather than a catalogue of every product release.
- Final reread: all seven references work and are used; every factual
  paragraph is cited; infobox repeats supported body claims. No unresolved
  factual limitation.

## Liquidation — complete

- Opened all four retained sources: Aave Health Factor & Liquidations,
  Sky Collateral Liquidation, Hyperliquid Liquidations and Auto-deleveraging.
- Lead and infobox are supported by the distinct lending, auction and
  derivatives mechanisms below; no claim that one universal process exists.
- Aave source states the health-factor equation, below-one eligibility,
  changes in collateral/debt, permissionless competition, bonus and partial
  versus full liquidation. The threshold/insolvency distinction follows
  from that equation and its worked example, rather than conflating a
  threshold breach with negative equity.
- Sky overview/instant settlement, price functions, liquidation limits and
  known-risk sections support both auction paragraphs and execution caveat.
- Hyperliquid documentation establishes order-book liquidation, possible
  partial fills, backstop below two-thirds maintenance, separate isolated
  and cross collateral, and ADL of profitable counterparties when account
  or isolated value is negative. No numerical thresholds were added.
- Update searches included Aave and Hyperliquid changes through October
  2026. Search surfaced an Oct 29–31 Aave emergency freeze/unfreeze report,
  flagged to parent for the separately scoped Aave page; this article does
  not promise availability of any market or new borrowing. The existing
  generic mechanisms remain supported by live documentation.
- Final reread: no factual corrections needed. All four references are
  openable and used; each factual paragraph cited; infobox supported.

## Perpetual futures — complete

- Opened all six retained references: Bybit introduction and contract FAQ,
  Hyperliquid funding, robust price indices, liquidation and ADL documents.
- Bybit sources support derivative/no-expiry distinction, long/short
  exposure, margin definitions, position-size risk tiers, isolated/cross
  collateral and fee/funding distinction. The five-times example is direct
  arithmetic from position value divided by margin, explicitly before fees.
- Funding source supports positive/negative payer direction, premium plus
  interest component, hourly settlement and the incentive to converge.
  No guaranteed peg is claimed.
- Robust-price source supports external oracle, composite mark and margin/
  unrealised-PnL uses; liquidation and ADL sources support the difference
  between a mark and executable liquidity, backstop, and counterparty rank.
- Attributed the price-index discussion to Hyperliquid's robust-price
  documentation to avoid implying every builder-deployed market uses the
  same oracle architecture. Update search and live margining/funding documents
  exposed HIP-3 and account-mode differences; the article otherwise avoids
  specific cross-DEX sharing and builder-configuration claims.
- Final reread: all six retained references work and are used; every factual
  paragraph cited; all infobox entries supported by cited body text.

## Polymarket — complete

- Opened all six original references: official Prices & Orderbook, Order
  Lifecycle, pUSD and Resolution documentation; CFTC 2022 enforcement
  release and QCX designated-contract-market register.
- Lead and infobox: event shares, implied probabilities, matching and
  settlement, pUSD/Polygon/USDC, two oracle paths and the QCX legal identity
  all appear in those sources. The price example is direct arithmetic,
  not a claim that a market price is an objective probability.
- Trading: order lifecycle explicitly separates offchain creation/operator
  matching from onchain settlement; pUSD documentation specifies ERC-20,
  Polygon, USDC backing and onchain wrap/unwrap contracts; price page
  specifies midpoint, the over-$0.10 spread exception, and execution at
  actual bids/asks. Kept collateral claims attributed to documentation.
- Corrected resolution overstatement: the documentation includes an
  unknown/50–50 resolution paying $0.50 to each outcome, so $1/$0 settlement
  is now explicitly ordinary binary resolution rather than universal.
  Read the full proposal/challenge/DVM voting and Chainlink TWAP sections.
- CFTC 2022 release directly supports wrongdoing, $1.4m penalty and wind-
  down requirement. Current register confirms QCX designation and original
  9 July 2025 date; neither is extended to all international products.
- October update search found an important state-law development. Added
  the opened Michigan regulator notice of 28 October: agreement to stop
  new sports contracts, close remaining positions by 25 November, and a
  pending appeal. The text attributes the regulator's report and does not
  adopt its contested promotional description of prediction markets.
- Added the 29 October security interruption and company's fix, restoration,
  law-enforcement referral and reimbursement commitment. Opened Reuters'
  full syndicated story on StreetInsider. AP original and Yahoo syndication
  failed to open; neither is cited. Avoided unsupported loss totals,
  assigning blame to a named vendor, or claiming reimbursement completed.
- Final reread verified all eight retained references, all paragraphs and
  the infobox. Incident scope and reimbursement completion remain limited
  to what the company's reported statement establishes as of 31 October;
  no unsupported certainty is introduced.

## Bybit — complete

- Opened all six original references: company history, contract FAQ,
  incident timeline, FBI notice, BlockSec analysis, Austrian FMA notice.
- Lead/infobox/timeline: company history supports 2018 and initial BTCUSD
  inverse perpetual; the timeline identifies Ben Zhou as co-founder and
  documents the ETH wallet; FBI confirms approximately $1.5bn and its
  26 February attribution to North Korea/TraderTraitor for 21 February.
  Attribution is explicitly the FBI's assessment.
- Read the contract FAQ's risk limits, margin modes, initial/maintenance
  margin, fees, liquidation and user-eligibility sections. These support
  both trading paragraphs and geographic/KYC qualification. No maximum
  leverage or universal regional availability is asserted.
- BlockSec's original research supports the malicious wallet-logic upgrade
  and signers' deception. Added Sygnia's opened 16 March 2025 investigation,
  https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/, as later
  forensic corroboration. The paragraph does not allege signer misconduct
  or a generic vulnerability in all Safe contracts.
- Read the company's incident timeline through the Feb 24 recap: partner
  support, deposits, loans and OTC purchases covered its claimed ETH gap;
  withdrawal processing and shortfall coverage are kept as Bybit claims,
  separate from recovering stolen assets.
- FMA May notice confirms decision on 28 May (notice published 30 May),
  Bybit EU GmbH identity and exact authorised categories. Update search
  found and opened the 4 August 2026 FMA licence for Bybit Payments GmbH:
  added a short paragraph and timeline row distinguishing electronic-money
  issuance/payment services from the separate crypto-asset licence.
- Final reread: all eight retained references work and are used; each
  paragraph has support; infobox and five timeline rows repeat cited facts.
  No recovered-funds total or blanket licensing claim is implied.

## BNB Chain — complete

- Opened all eight original references: website, BSC introduction,
  validator overview, Fusion, staking, post-Fusion FAQ, 2022 ecosystem
  incident notice and August 2026 Pasteur announcement.
- Lead/infobox: official chain navigation names BSC/opBNB/Greenfield and
  says Beacon sunset complete. Introduction supports EVM and BNB gas/
  staking; consensus and staking sections establish independent validators,
  PoSA, rotating production and stake-based selection.
- Validator overview directly confirms daily top-45 elections, 21 Cabinets
  plus 24 Candidates, and the per-epoch 18+3 consensus set. Kept it as a
  dated documentation description rather than a live independent node census.
- Fusion/staking support functional migration, retirement and direct BSC
  delegation. FAQ supports shutdown and unrecoverable unbound BEP2/BEP8.
  Update search found a material recovery change: opened phase-3 notice
  https://docs.bnbchain.org/announce/token-recovery-sunset-phase3/ and added
  1 July hosted-tool discontinuation, local replacement and retained
  approval-server signature. Avoided repeating the guide's internally
  conflicting claim that signatures never leave the device, since its
  actual workflow sends signed data to an approval server.
- 2022 incident notice is primary evidence of the Token Hub exploit,
  forged proof, 2m BNB and validator-coordinated halt. Numbers are attributed
  to BNB Chain and are not converted into an unsupported final loss value.
- August announcement supports Fermi 0.45s, Osaka/Mendel, Pasteur components
  and testnet-only performance figures. Opened September post-Pasteur
  follow-up to confirm actual 25 August activation, rather than leaving
  an obsolete scheduling-only account.
- Opened October Jenner announcement and release notes. They differ in
  scheduling detail: the earlier announcement says late October/testnet
  and late November/mainnet; v1.8.1 release notes specify Chapel testnet
  and explicitly do not schedule mainnet. Added only the supported release
  scope and feature categories, not a completed mainnet activation or
  unverified testnet activation. Full release notes URL is retained.
- Final reread: all eleven references work and are used; all factual
  paragraphs cited; infobox supported. Roadmap/current-network distinction
  and documentation age are explicit where material.

## TRON — complete

- Opened all eight original references: Super Representatives, Resource
  Model, history page, Stake 2.0, Tether integration, Circle discontinuation,
  SEC release and Justia judgment landing page.
- History page returned only a JavaScript placeholder on open, despite
  searchable cached excerpts. Replaced it with opened TRON DAO Q3 2026
  research for founder and current protocol context; added the opened
  contemporaneous 31 May 2018 launch announcement on TRON's Medium
  publication to retain the precise launch date. Did not equate mainnet
  software launch with the later June token migration/Independence Day.
- Lead/infobox/resources: current developer pages confirm TRX, DPoS, top
  27 SRs, TVM, Bandwidth transaction bytes, Energy computation, and the
  TRX-burn fallback. Stake page confirms 7 April 2023 activation, current
  simultaneous resource+TP award, and proportional resource entitlement.
- Governance: SR roles table distinguishes top 27 from ranks 28–127,
  six-hour maintenance, block production, rewards and counted approvals.
  The staking/voting/candidacy explanation follows those separate roles.
- October update search and opened Q3 report support the added attributed
  Proposal 107/Pyrrho/secp256r1 paragraph. No chain-volume, user-count or
  ETF-performance claims were imported from promotional reporting.
- Tether announcement supports March 2019/TRC20 integration; Circle's
  February 2024 announcement supports immediate minting stop, transition
  through February 2025, and its attributed company-wide risk assessment.
- SEC litigation release supports 2023 filing, amended wash-trading
  allegations concerning 2018–2019, March 2026 settlement terms and no
  admission/denial. Justia's docket description confirms 9 March judgment
  and $10m Rainberry penalty, but its PDF could not be reliably extracted
  in this tool session (local download hit a challenge page). Opened the
  full judgment text reproduced by Midpage instead:
  https://app.midpage.ai/document/securities-and-exchange-commission-v--96f6dfdc-03ed-4f22-934c-03ab4bfbb366.
  Its opening/sections II and IV explicitly confirm no-admission settlement,
  penalty and dismissal with prejudice. Added that working reference and
  made final disposition explicit for Rainberry's remaining specified
  claims and all claims against Sun/TRON Foundation/BitTorrent Foundation.
  Court-text mirror is evidence of the primary judgment, not an AI legal
  summary. No exoneration or admission of guilt is inferred.
- Final reread: all ten retained references open and support their use;
  every factual paragraph cited and all six infobox entries verified.
  Original inaccessible history URL was removed, not silently certified.

## Final handoff

All seven assigned articles have completed final-text checking. The first
three were reported by the parent as built, checked and committed in
`9a5f2c3`. The remaining four are ready for the same batch validation.
No build, shared catalogue edits, commits or pushes were performed by this
review agent. The record documents additional substantive writing and
checking by GPT-6-Astra high; all original writer fields remain unchanged.
