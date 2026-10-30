# ChainLore

An encyclopedia of crypto, written with AI from the start.

Data, references, and signal only. No ads, no colours, no token shilling.

## Why

Wikipedia covers crypto poorly. Major protocols such as Hyperliquid and
Arbitrum have no article at all. The crypto sites that do cover them are
mostly price tickers, dashboards, or marketing. ChainLore is the reference
work in between. See [VISION.md](VISION.md).

## Contents

| File | Purpose |
|---|---|
| [VISION.md](VISION.md) | What ChainLore is and what it is not |
| [INDEX.md](INDEX.md) | Every page in the encyclopedia |
| [INSPIRATION.md](INSPIRATION.md) | Existing sites we learn from |
| [pages/](pages/) | The articles, one Markdown file per subject |

## Page conventions

Every page in `pages/` follows the same shape:

1. **Front matter**: title, ticker, category, status, last updated date.
2. **Lead**: one paragraph that says what the subject is.
3. **Infobox**: a two-column table of hard facts.
4. **Body sections**: History, Technology, Token, Governance, Incidents
   and controversies, as applicable.
5. **Timeline**: dated events, oldest first.
6. **See also**: links to other ChainLore pages.
7. **References**: numbered footnotes, preferring primary sources such as
   whitepapers, specifications, official docs, governance proposals, and
   onchain data.

Rules:

- Every factual claim should be traceable to a reference.
- Dates are written as `D Month YYYY` in prose and `YYYY-MM-DD` in tables.
- Figures that change constantly (price, TVL, market cap) are not
  hardcoded into prose. Link to a live source instead.
- Pages with `status: draft` have not been fact-checked against their
  references yet.
- File names are lowercase and hyphenated: `pages/arbitrum.md`.
