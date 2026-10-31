# Coverage expansion: 31 October 2026

This writing pass adds the subjects proposed in the coverage review and
replaces the generated Binance and Satoshi Nakamoto pages with maintained
Git sources. Each batch is committed and pushed separately.

## Attribution and status

The writing runtime identifies itself only as based on GPT-6; the exact
model variant and reasoning-effort setting are not exposed in the session.
New and rewritten articles therefore use `written_by: Unknown` rather than
guessing an exact attribution. This is also the attribution record for the
substantive writing in this pass. Existing author credits are preserved.

All new and rewritten articles remain drafts. Research and an author review
are not an independent AI fact-check under POLICY.md. Existing articles
receive navigation links without changes to their factual wording or
review dates.

## Foundation batch

- Cryptocurrency wallet: distinguish keys, accounts, custody, recovery,
  and token allowances, using Bitcoin documentation, BIP-39, and Ethereum
  documentation and standards.
- Smart contract: execution, permissions, proxy upgrades, and failure
  modes, using Ethereum documentation, Solidity guidance, and ERCs.
- Rollup: separate optimistic and validity proofs, sequencing, data
  publication, and administrative powers. L2Beat stages are not presented
  as a guarantee against bugs.
- Blockchain bridge: distinguish representations of assets, issuer
  burn-and-mint transfers, and cross-chain messages and their trust models.
- Blockchain oracle: distinguish agreement on execution from data quality,
  with external feeds, onchain prices, and sequencer availability.

Sources were opened during research on 31 October 2026. The article
footnotes identify the sources used. Frequently changing market figures
are omitted. Static builds and link/citation checks run for each batch.

## Organisations batch

Added Coinbase, MetaMask, and MakerDAO and Sky. Sources include company
announcements, regulator statements, protocol documentation, and governance
records. The Coinbase dismissal is not described as a merits ruling;
MetaMask's support-ticket incident is distinguished from a wallet compromise;
and the Maker compensation poll is not described as an executed payment.
Added navigation from Base, USDC, Hyperliquid, wallets, and stablecoins.

## Protocol batch

Added Chainlink, Curve, and Ethena, with reciprocal links from the oracle,
exchange, staking, and stablecoin coverage. Used protocol specifications,
operator documentation, and governance records. Curve's compensation
proposal is not treated as proof of completed payments. Ethena's current
strategy descriptions and discretionary rewards are attributed to Ethena.

## Bitcoin history and privacy batch

Added Mt. Gox, Lightning Network, and Monero. Mt. Gox uses the trustee's
16 October 2026 extension to October 2027 and separates initial loss
estimates, recovered coins, and criminal allegations. Lightning distinguishes
channel capacity from directional liquidity. Monero describes probabilistic
privacy and published limitations rather than promising untraceability.

## Culture batch

Added NFTs and memecoins. Distinguished token ownership from intellectual
property rights, royalty reporting from payment enforcement, and memecoin
labels from legal classification. Included the March 2026 SEC framework
and attributed manipulation findings to the relevant research dataset.

## Existing live article rewrites

Re-fetched both public Markdown pages before rewriting. Satoshi had changed
from a placeholder into an automated draft during the work. The previous
public writer credits were `claude-haiku-5-5` for Binance and
`claude-haiku-5-5 (high effort)` for Satoshi. These complete replacements
use the attribution recorded above and preserve the live slugs.

Binance now cites company incident disclosures, regulatory notices, the
criminal case, the separate SEC dismissal, and the clemency warrant. The
FCA action is scoped to Binance Markets Limited. The October 2026 account
reflects update #2 and attributes provisional figures and recovery promises.
Removed weak-source allegations that could not support the earlier wording.

Satoshi now uses the original paper and mailing-list archive, recipient-
published correspondence, and the court judgment. The archive timestamps
the release announcement on 8 January 2009 EST. Removed speculative
wealth estimates and unsupported motives; separated identity claims from
established documentary history.

## Final validation

The static build produces 39 articles and seven supporting pages. The
checker passes all 46 HTML pages. A separate audit confirms that all 18
new or rewritten articles appear in the index, have incoming article
links, link to other articles, and have no missing or unused footnote
definitions. Git whitespace checks pass. Deployment uses the repository's
existing release, backup, test, and health-check workflow.

## Satoshi article expansion

Expanded the existing Satoshi Nakamoto article at the owner's request,
from 510 to 1,004 words excluding front matter and references. Preserved
its original text and writer credit, adding the double-spending problem,
the whitepaper's privacy limitations, the genesis block, the experimental
launch, Hal Finney's participation, and development before withdrawal.

Additional writer: Unknown. This session is described as based on GPT-6;
the exact model variant and reasoning effort are not supplied. This is
an expansion, not a replacement of the original writer attribution or
an independent fact-check. The article remains a draft.

Opened the existing primary sources and three additional primary sources
on 31 October 2026: Bitcoin Core's versioned genesis-block code, Finney's
first-person retrospective, and Nakamoto's 0.3.19 release post. The genesis
date is the UTC date of the timestamp encoded in Bitcoin Core. Added
citations beside the new claims and two timeline entries. Static build,
local-link and citation-anchor checks passed for all 46 HTML pages.
