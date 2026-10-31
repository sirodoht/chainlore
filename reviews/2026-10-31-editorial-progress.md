# Remove the freshness gate and preserve correction progress

The owner requested removal of mandatory freshness checks and forward progress
instead of repeated terminal outcomes. Verification now checks the article's
claims against fetched references without requiring a broad recency search.
Missing search results and a false legacy `freshness_checked` flag do not fail a
report. Saved source evidence does not expire at midnight; each new report must
still record its actual completion date. Source rules, coverage, exact quotes,
candidate hashes and publication-base checks remain enforced.

The Liquidation checker identified missing table footnotes, an overbroad
"usually" claim, and a formula attached to the wrong reference. The writer had
been forbidden from replacing tables. Citation-only table replacements are now
allowed while preserving all other table characters and facts. Writers receive
the previous cumulative patch and candidate as context, with the original article
remaining the exact edit base.

Correction passes reuse fetched checker evidence and retain factual feedback.
Truncated or malformed writer responses retry from that saved context with a
32,000-token output allowance; they do not consume a factual revision or replace
checker findings with a formatting error. Saved unprocessed writer responses are
validated after restart before another paid call. Repeated format failures remain
operational blocks, never unsupported-claim decisions.

The former absolute two-revision limit is replaced by a limit on two consecutive
passes without improvement in verified coverage or issue resolution. Total
revision counts and token usage remain in the audit. The existing 4M daily and
3M per-submission budgets remain unchanged. A guarded recovery command resumes
historically exhausted corrections from saved evidence and actionable findings;
it never grants publication approval.
