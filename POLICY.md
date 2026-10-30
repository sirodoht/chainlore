# Editorial policy

How a Chainlore page moves from draft to AI fact-checked to human
reviewed, and what each status promises the reader.

## Statuses

| Status | Front matter | Promise to the reader |
|---|---|---|
| Draft | `status: draft` | Written, but not yet fully fact-checked. May contain errors. |
| AI fact-checked | `status: ai-fact-checked` | Every claim was checked against live sources by an AI that did not write the text. |
| Human reviewed | `status: human-reviewed` | AI fact-checked, then read, spot-checked, and approved by a named person. |

A page moves up one status at a time. Editing a page can move it back
down; see [Losing a status](#losing-a-status).

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
6. Up to date. The check looked for major events up to the check
   date. Matters still in progress are written "as of" that date.
7. Record. The front matter records the check:

        status: ai-fact-checked
        checked: 2026-10-30
        checked_by: Opus 5.5 High

    The commit message lists the errors found and fixed.

## Human reviewed

A page may be marked `human-reviewed` only when all of the following are
true.

1. Already checked. The page is `ai-fact-checked`, and nothing
   substantive has changed since the check.
2. Read in full. A named reviewer has read the whole page and
   confirms that it:

    - is neutral, with no promotional or hostile language;
    - attributes contested claims;
    - leaves out no major event or criticism the reviewer knows of;
    - is clear and correctly structured.

3. Sources checked by the reviewer. The reviewer opens the sources
   themselves, without relying on an AI report, for:

    - every claim in Incidents and controversies;
    - every claim about a named person;
    - every figure in the infobox;
    - at least 10 other references of the reviewer's choosing, spread
      across the page.

    If one sampled reference fails, the reviewer fixes it and checks 10
    more. If two or more fail, the page returns to `draft` for a full
    AI fact-check.

4. No conflict of interest. The reviewer discloses any job, payment,
   or significant holding related to the subject. Anyone employed or paid
   by the subject, or by a direct competitor, may not review its page.
5. Record. The front matter records the review:

        status: human-reviewed
        checked: 2026-10-30
        checked_by: Opus 5.5 High
        reviewed: 2026-11-02
        reviewed_by: Jane Doe

    The commit message names the reviewer and lists anything they changed.

## Losing a status

- Substantive edits move a page back to `draft` until the changed text
  has been fact-checked. Substantive edits are those that add or change a
  claim, date, number, or name, or add or remove a reference. Once the
  changes pass an AI check, the page becomes `ai-fact-checked`. To regain
  `human-reviewed`, a reviewer reviews the changed sections under the
  rules above.
- Non-substantive edits keep the page's status. These include fixing
  typos, formatting, and broken links that point to the same document.
- Age. A check is a snapshot. A page whose `checked` date is more
  than six months old, or whose subject has had a major event since,
  should be checked again. Until then it keeps its status, and readers
  can see the check date.

The `updated` field records the date of the last substantive edit.
