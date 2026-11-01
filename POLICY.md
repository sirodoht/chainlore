# Editorial policy

Chainlore makes editorial decisions autonomously. Research, writing, independent
verification, corrections and maintenance do not require human approval.
An automated decision may conclude that evidence is insufficient; it must not
turn uncertainty into a published assertion.

## Statuses

| Status | Front matter | Promise to the reader |
|---|---|---|
| Draft | `status: draft` | Written, but not yet fully fact-checked. May contain errors. |
| AI fact-checked | `status: ai-fact-checked` | Every claim was checked against live sources by an AI that did not write the text. |
| Historical human review | `status: human-reviewed` | Retained only for historical records of an actual named human review; no new human-review stage is required. |

New automated work is private until verification passes. Existing published
drafts remain honestly labelled and are eligible for scheduled checking.
Freshness is separate from verification status: the displayed check date is a
snapshot, not a promise that an article can never become outdated.

## Authorship and check credits

Every article requires `written_by` in its front matter, including drafts.
Record the actual model and reasoning effort, for example:

    written_by: Opus 5.5 High
    checked_by: GPT-6-Astra high
    checked: 2026-10-30

Only add the check fields after a completed fact-check. Names of applications
such as Codex or ChatGPT are insufficient model attribution. Use the provider's
model identifier for automated writing, with the requested effort appended.
If historical evidence is missing, record `Unknown` rather than guessing.
Fixed placeholder pages credit `Chainlore template (no model)`.

Keep the original writer credit when editing or checking an article. Record
additional substantive writing and checking passes, including model and effort,
in the commit description or a dated review record. A complete rewrite updates
`written_by`; Git retains prior credits. Generated articles retain provider
requests and responses in their private audit history, and their Markdown
stores the writer credit so it travels with the article. Screening credits in
that audit history do not qualify as fact-checks.

Article headers display the writer, current status, and applicable checker or
human reviewer and date. After a substantive edit returns a page to draft,
old checker metadata may remain as history but is not displayed as a current check.

## Sources

Every reference falls into one of three tiers.

1. Primary. Specifications and improvement proposals (BIPs, EIPs,
   AIPs, HIPs), source code, official documentation, governance proposals
   and votes, court and regulatory documents, company announcements and
   filings, and onchain data such as blocks and transactions.
2. Reputable secondary. Established news organisations (Reuters, AP,
   Bloomberg, the *Financial Times*), established crypto press (CoinDesk,
   The Block, Decrypt, Blockworks), peer-reviewed papers, and research
   published under the name of an identifiable firm or institution.
3. Weak. Exchange and aggregator news pages, review sites,
   unattributed blogs, social media posts by people not party to the
   events, and wikis, including Wikipedia.

Rules:

- Prefer primary sources. Use a secondary source when it adds something
  the primary source does not, such as a date, a figure, or context.
- A weak source on its own may support only uncontested, low-stakes
  facts. It may never be the only source for an incident, a figure in a
  dispute, or a claim about a named person.
- A claim that a named person or organisation did something wrong needs a
  primary source or two independent reputable secondary sources.
- A subject's claims about itself are attributed, not stated as fact:
  "Hyperliquid Labs states it took no outside funding".
- Contested points are attributed, and each significant side is given.
- Judgements such as "largest", "first", or "most serious" are kept only
  if a source makes the same judgement. Otherwise they are removed.
- A draft may be short, may rest on a single or weak source, and may cite
  pages found in search but not opened. Drafts are not checked against
  these rules, so they may contain errors. New automated work with insufficient evidence is not published; the request
  receives an explanation instead. Historical placeholders remain labelled.

## AI fact-checked

A page may be marked `ai-fact-checked` only when all of the following
are true.

1. Independent check. An AI pass that did not write the text has
   checked every factual claim in the lead, infobox, body, tables, and
   timeline against live sources. Model memory does not count as a
   source.
2. Final text. The check covers the text as it will be published.
   Corrections made after a check are themselves checked. The page
   qualifies only once a pass over the latest changes finds no errors.
3. Citations. Every paragraph, list item, and table that makes a
   factual claim has at least one footnote. An infobox entry or timeline
   row may go uncited only if it repeats a claim cited elsewhere on the
   page.
4. Working references. Every reference URL has been opened and
   supports the claim it is attached to. Every footnote marker has a
   definition, and every definition is used. `scripts/check.py` must pass.
5. Source rules. The [source rules](#sources) above are met.
6. Dated claims. State the applicable period for claims that depend on time.
   Verify those claims against their cited sources. A broad news or recency
   search is not a publication requirement, and its absence is not a rejection.
7. Record. The front matter records the check:

        status: ai-fact-checked
        checked: 2026-10-30
        checked_by: Opus 5.5 High

    The commit message lists the errors found and fixed.

## Autonomous decisions and publication

- The writer and checker use separate calls and independent research contexts.
  They may use the same configured model family; agreement alone is not evidence.
- The checker opens every reference and accounts for every paragraph, heading
  and table row. A separate freshness search is not required. Its
  structured claim/evidence report remains in the private audit with fetched-source
  fingerprints and actual provider model/effort attribution.
- Software checks coverage, source retrieval, evidence excerpts and dates. These
  controls constrain the checker; semantic support is still an AI assessment.
- A passing check is bound to the exact source hash. The publisher cannot substitute
  changed text or overwrite a different Git base under that approval.
- Corrective passes retain saved evidence, cumulative edits, and checker findings.
  Verification completes all claim groups and combines their findings before
  requesting a revision, rather than stopping at the first failing group.
  They continue while verified coverage improves or findings are resolved. Two
  consecutive passes without that progress end as Insufficient evidence, preserving
  the current article. Format failures retry writing without consuming an article
  revision or replacing factual feedback; operational and token limits still apply.
- Error reports investigate both the published claim and the suggested correction.
  A source-supported existing claim may be retained with an explicit outcome.
- Public outcomes explain publication, duplication, decline or insufficient evidence.
  Private messages, contact details, model prompts and provider responses stay private.
- Historical human-review records remain valid as history. They are never created
  by automation or treated as a required higher level of verification.

## Operations and maintenance

Scheduled jobs may investigate source changes, significant developments and
catalogue consistency. They use the same claim-verification gate; there is no
mandatory freshness-search gate. Reader submissions take priority;
maintenance has its own daily limit. Failed checks do not silently remove articles.

Transient failures retry with backoff. Provider outages and budgets appear as
Blocked with a retry time where available. Exhausted operational recovery remains
visible to the owner; it is not an editorial approval queue. Owners retain pause,
credential, budget, audit and rollback controls. No model can change these controls.

## Losing a status

- Substantive edits move a page back to `draft` until the changed text
  has been fact-checked. Substantive edits are those that add or change a
  claim, date, number, or name, or add or remove a reference. Once the
  changes pass an AI check, the page becomes `ai-fact-checked`. Automated publication completes only after the resulting text passes its
  own source check; historical human credits are retained in Git.
- Non-substantive edits keep the page's status. These include fixing
  typos, formatting, and broken links that point to the same document.
- Age. A check is a snapshot. Scheduled maintenance targets articles
  whose check is at least 30 days old, and investigations may run sooner
  following reader reports or significant developments. Until then it keeps its status, and readers
  can see the check date.

The `updated` field records the date of the last substantive edit.
