# Article attribution

- Every article must have `written_by` in its front matter. Record the actual
  writer model and reasoning effort (for example, `Opus 5.5 High`), not an app
  name such as Codex or ChatGPT. Use `Unknown` when historical evidence is absent;
  never infer a past model from the current configuration.
- Preserve the original writer credit during edits and fact-checks. Credit
  additional substantive writing passes, with model and effort, in the Git
  commit description or a dated file in `reviews/`. For a complete rewrite,
  update `written_by`; Git retains the earlier attribution.
- A completed fact-check must record `checked_by` (actual model and effort)
  and `checked` (date), following POLICY.md. Record the pass and corrections in
  the commit description or `reviews/`. Editing metadata alone is not a new
  fact-check and must not change the check date.
- Historical human review uses `reviewed_by` and `reviewed`; no human approval
  is required by the autonomous workflow. Automated request/output
  screening is not fact-checking and must never populate checker credits.
- Run the static build and checker after article metadata changes. When
  changing automation or attribution recovery, also run the submissions tests
  and the migration consistency check described in README.md.

# Article timelines

- Article timelines must be Markdown tables with `Date` as the first column
  heading. Write dates as `2018`, `2018-09`, `2018-09-26` or `2023-03-10–13`,
  only as precisely as the sources support. Other formats are silently left out
  of `/timeline/`.
- After building, confirm the build reports 0 rows skipped.
