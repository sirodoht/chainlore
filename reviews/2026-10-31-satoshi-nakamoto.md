# Satoshi Nakamoto independent fact-check — 2026-10-31

Article: `pages/satoshi-nakamoto.md`.
Checker: **GPT-6-Astra high**, a separate agent that did not write the
expanded article. Model and effort were inherited from the parent session,
whose configuration was verified by the parent. The expansion and this
pass's substantive corrections are credited to GPT-6-Astra high; the
historical `written_by: Unknown` remains unchanged.

## Scope and outcome

Read AGENTS.md and POLICY.md. Checked the lead, all infobox entries, every
body paragraph, all timeline rows, and every reference against live
sources. Opened all 16 original reference URLs successfully and the three
added references, for **19 of 19 final references**. Re-read the final
article and checked the corrected wording and additions against the
opened sources before setting `status: ai-fact-checked`,
`checked: 2026-10-31`, and `checked_by: GPT-6-Astra high`.

The parent agent, also GPT-6-Astra high, independently opened the three
new references and checked the reviewer's additions and corresponding
timeline rows. The court judgment confirms the March order, its duration,
permission requirement and May reasons; The Block confirms the documentary's
release and hypothesis; WIRED confirms the reported denials and skepticism.
No further article corrections were needed. This second check covers the
substantive material first written during the independent review.

The article has **2,073 body words**, compared with 1,004 before expansion
(front matter and reference definitions excluded; footnote markers and
Markdown link destinations removed; word tokens retain internal apostrophes
and hyphens). This is approximately 2.06 times the original length.

## Corrections and updates

- Clarified that the Dai correspondence linked to a draft, including in
  the timeline; the draft itself was not included in the message.
- Replaced the claim of an anonymity promise with qualified anonymity
  language, matching the Malmi correspondence.
- Clarified that the overflow recovery instructions appear in the edited
  announcement itself, rather than a separate follow-up.
- Shortened the release discussion to keep aggregate source use within
  the source budget without losing its core historical details.
- Added the later civil restraint order from an approved court judgment.
  Distinguished the order date from publication of the reasons.
- Added the competing *Finding Satoshi* hypothesis and reported denials,
  preserving the unresolved status of the pseudonym.

## Source coverage

The identifiers below correspond to the article's reference definitions.
All final URLs were opened, and the relevant passages were inspected.

| Reference | Coverage checked |
|---|---|
| announcement | Announcement and title |
| paper | Design, incentives, security assumptions, privacy, bibliography |
| release | Archive timestamp and release details |
| genesis | Versioned source, timestamp parameters, embedded message, output |
| finney | First-person retrospective and early participation |
| development | Release post and limits of its protections |
| hearn | Dated exchange, contract explanation, withdrawal |
| judgment | Court findings and chronology, especially paragraph 7 |
| identity | Attributed reporting and denial |
| dai | Email headers, citation request, draft link |
| discussion | Finney exchange and development account |
| malmi | Emails 93, 124, 197 and 200 |
| overflow | Original post and visible edit date |
| wikileaks | Post 148 and its timestamp |
| contempt | Operative order and chronology |
| holdings | Research method, estimate and explicit uncertainty |
| restraint | Approved judgment, paragraphs 1, 5 and 97 |
| documentary | Hypothesis, publication and unresolved identity |
| skepticism | Continuing disagreement and attributed family denials |

The National Archives endpoint for the added judgment was inaccessible to
the browser tool, and a separate mirror timed out. The cited S3 mirror of
the approved judgment opened successfully; the article identifies it as a
mirror. Those failed endpoints are not cited as verified references.

## Freshness, sourcing and limits

Searched for significant developments through 31 October 2026 concerning
identity claims, Wright proceedings, and attributed holdings. The search
prompted the additions above; it did not produce a verified identification
or justify treating attributed mining estimates as authenticated current
holdings. The article distinguishes messages written under the pseudonym,
judicial findings about a claimant, and hypotheses about other people.
The unresolved identity discussion is explicitly dated.

Checked citations and source tiers. Named-person wrongdoing is supported
by court documents. Correspondents' recollections and research conclusions
remain attributed. All factual paragraphs and timeline rows have citations;
the uncited “Known for” infobox entry repeats cited text.

A conservative count charging each entire cited paragraph and each cited
table row to every attached source gives a maximum of 182 words per source;
the WIRED source uses 49 of its 100-word allowance. All other sources stay
within their 200-word allowance. Direct quotation is limited to brief
titles and the embedded genesis message, within the quotation limit.

## Validation

- Static build passed: 61 articles, 7 supporting pages, 246 timeline pages,
  588 events, **0 rows skipped**.
- Checker passed: **314 HTML pages**, including statuses, links, assets,
  IDs and citation anchors.
- `git diff --check` passed.

Used the existing repository virtual environment's Python interpreter to
run `scripts/build.py` and `scripts/check.py` in the review checkout. The
initial `uv run --locked` attempts were blocked by default-cache permissions
and then restricted-network dependency downloads; the existing environment
provided the required dependencies. No automation or attribution recovery
code changed, so submissions tests and migration checks were not required.
