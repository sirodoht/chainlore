# Draft article fact-checks — 31 October 2026

Scope: the 24 draft articles requested for checking, excluding Satoshi
Nakamoto, which the user assigned separately. Six subagents divided the
work, running in waves because the session permitted three concurrent
subagents alongside the coordinating agent.

Checker and corrective-writing attribution: **GPT-6-Astra high**. The
coordinator verified `gpt-6-astra` and `high` in the active session's
`turn_context`; all six full-history subagents inherited that configuration
without overrides. Original `written_by` credits are preserved. These are
AI checks under POLICY.md, not human reviews.

## Coverage records

Each linked report records the live-source pass, factual corrections,
current-event search, final-text verification and source-access limits.

| Review record | Articles |
|---|---|
| [Foundations and exchanges](2026-10-31-foundations.md) | Binance; blockchain bridge; blockchain oracle; Chainlink; Coinbase; cryptocurrency wallet; MetaMask; rollup; smart contract |
| [Stablecoin](2026-10-31-stablecoin.md) | Stablecoin |
| [Japan and Hong Kong](2026-10-31-japan-hong-kong.md) | Japan Payment Services Act; Hong Kong Stablecoins Ordinance |
| [US laws](2026-10-31-us-laws.md) | CLARITY Act; GENIUS Act |
| [Europe and UK](2026-10-31-europe-uk.md) | MiCA; UK cryptoasset regime |
| [Protocols, history and culture](2026-10-31-protocols-history-culture.md) | Curve; Ethena; MakerDAO and Sky; Mt. Gox; Lightning Network; Monero; NFT; memecoin |

## Main corrections

- US legislation: corrected reserve eligibility, offering thresholds and
  exceptions; added Treasury's September interim final rule and the
  Federal Reserve proposal; corrected the Senate calendar and preserved
  the distinction between CLARITY's differing texts.
- MiCA and UK: corrected notification periods and exemption conditions,
  added October regulatory developments, and distinguished consultations,
  negotiating positions and future supervision from operative rules.
- Japan and Hong Kong: corrected enactment/commencement dates, Japan's
  permissible backing changes, and Hong Kong's licensing and bank exceptions.
- Stablecoins: corrected issuer identities, wind-downs, redemption mechanics,
  incident chronology and reported loss figures; replaced weak or
  inaccessible sources and narrowed unsupported claims.
- Technical and protocol articles: clarified account delegation, rollup
  proofs, bridge-standard status, Monero's base subsidy, and the distinction
  between proposals, approvals, software patches and live deployments.
- Current developments: added verified updates for Coinbase, MetaMask,
  Chainlink, Curve, Lightning and Ethena, retaining attribution and
  uncertainty where an investigation or implementation remains unfinished.

## Integration review

The coordinator reviewed the article changes and individual review records,
checked shared regulatory claims for consistency, and assisted with primary
sources where publishers' ordinary URLs were inaccessible. In particular,
the OCC was undergoing maintenance; official GovInfo text supports the
GENIUS rule, and an archived original OCC decision supports World Liberty
Trust Company's preliminary conditional approval. These limitations are
recorded in the individual reports.

A final cross-article query raised the 29 October Binance incident. It was
already covered in Binance's draft and retained in the checked article.
The coordinator independently reopened and read Binance's [30 October
update #2](https://www.binance.com/en/support/announcement/detail/d3306d9dca5243548c813b605e1d1751),
then reread the existing lead and incident section. The approximate $6.3
billion loss, reported $3 billion frozen, more than $6.34 billion reserved,
withdrawal suspension, continuing deposits and preliminary investigation
are supported. The article attributes the figures and commitments to the
company and does not present recovery or investigation as complete. No
additional Binance edit was needed for that query.

The coordinator also added the EBA's October USDC significance decision
and the UK's proposed stablecoin tax changes to the general stablecoin
article after reading the full primary texts. The stablecoin review's
integration addendum records those three additional references and the
recheck of the final wording. USDC's separate article was outside the
requested draft scope.

## Combined validation

All 24 requested articles now have `status: ai-fact-checked`,
`checked: 2026-10-31`, and `checked_by: GPT-6-Astra high`.

- `.venv/bin/python scripts/build.py` passed: 39 articles and seven
  supporting pages built.
- `.venv/bin/python scripts/check.py` passed: all 46 generated HTML pages
  have valid statuses, local links, assets, IDs and citation anchors.
- A separate audit of the 24 requested articles found 470 reference
  entries, with no missing, unused or duplicate footnote definitions and
  no uncited factual prose candidates. Table/list coverage was also
  checked in the individual editorial passes.
- All 24 files differ from the pre-check snapshot. Every original writer
  credit matches that snapshot: 17 `Unknown` and seven `Opus 5.5 High`.
  The former remain unknown because this check does not establish their
  historical writer models.
- The tracked article diff contains exactly the 24 requested files;
  Satoshi is absent. All six review records are present.
- `git diff --check` passed.

These integration results complete the build/check steps left pending in
the individual handoff records. The check is a snapshot as of 31 October
2026; source-access and attribution limits are retained in those records.

The editorial scope excludes automation and attribution-recovery code.
Commit, push and deployment follow separately under the user's publication
instruction.
