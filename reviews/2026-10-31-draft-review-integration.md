# Draft review integration — 31 October 2026

Coordinator: GPT-6-Astra high.

The 21 assigned drafts received independent reviews, with source coverage and
corrections recorded in the security, markets, and history review records dated
31 October 2026. All 21 are now AI fact-checked. Original writer credits were
preserved. Satoshi Nakamoto was excluded and is byte-for-byte unchanged from
the starting revision, `ac7abdb`.

The catalogue now contains 60 articles: 59 AI fact-checked and one draft
(Satoshi Nakamoto). This is automated fact-checking, not human review.

## Catalogue cleanup

- Alphabetised entries within each existing subject section, preserving their
  titles, descriptions, and placement.
- Normalised three `Decentralised finance` category values to `DeFi`, and two
  `Exchanges` values to `Exchange`, matching the publication category mapping.
- Added the existing Culture and History subjects to that mapping so future
  generated articles can use those subjects without falling into Other topics.
- Preserved check dates, writer/checker credits, statuses, and substantive-edit
  dates during these navigation and category changes.

Validation: static build and checker passed (60 articles, seven supporting
pages); six existing category/publication tests passed. A catalogue audit
confirmed each article appears exactly once, every category matches its index
section, and entries are alphabetised within sections. Full submissions tests
and migration consistency are also required by the final deployment script.

## Related articles

Added 39 See also links across 26 articles, avoiding links already present in
their source articles. The nine articles previously without incoming article
links now have relevant entry points: Bitcoin block size war, BNB Chain,
Inter-Blockchain Communication, Polymarket, The DAO, Three Arrows Capital,
Tornado Cash, TRON, and XRP Ledger. All 60 articles now have at least one
incoming link from another article, excluding catalogue links.

A before/after audit confirmed that this pass changed only See also sections:
all article claims, references, front matter, and the complete Satoshi article
remained unchanged. Related-link sections have no duplicate, self, or missing
article targets. The static build and checker passed again after these changes.
