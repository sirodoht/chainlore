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
