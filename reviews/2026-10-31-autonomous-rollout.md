# Autonomous editorial rollout — 31 October 2026

This changes application workflow and editorial policy. It does not retroactively
fact-check or relabel the existing article catalogue.

Publication requires a separate checker context with live search, every reference
opened, complete unit coverage, supporting excerpts, no unresolved findings and
an approval tied to the exact source. Concurrent source changes invalidate that
approval. Model judgment remains necessary for semantic support.

Real-provider acceptance tests ran in a separate private database on Brick, with
production and the worker disabled, shadow mode enabled, and no publication remote:

- Supported historical statement: passed (private replay check 3).
- Same statement with a deliberately incorrect year: failed (check 4), with an
  unsupported unit and unresolved checker findings.
- Actual returned checker: `claude-haiku-5-5 (high effort)`.
- Both tests retrieved the cited source and performed fresh web searches.
- Neither test could publish, change a production submission, or send email.

The first two checks exposed incomplete title classification and a JSON code-fence
format mismatch. Both withheld approval. The checker prompt now requires evidence
for the title and no unresolved issues; the parser accepts only a whole JSON object
or a single enclosing JSON fence, without surrounding prose. The final positive
and negative fixtures passed their expected outcomes.

Automated tests additionally cover unchanged-source publication, rejected altered
hashes, missing or contradictory evidence, partial checker responses, correction
routing, revision limits, source conflicts, shadow publication prevention, budget
reservations, queue controls, reader priority and maintenance deduplication.

Operational limits: two corrective research/revision passes, three automatic
recovery attempts, up to three delayed account recovery probes, 10 new jobs/day,
one scheduled maintenance job/day, 2,000,000 reserved tokens/day and 500,000/run.
These conservative token reservations include tool allowances and failed calls;
they are not a currency invoice. Owner configuration can change the budget limits.


Post-deployment inspection confirmed that two earlier improvement-writing failures
were complete `end_turn` responses wrapped in JSON fences. The same strict parser
now handles both writing and verification responses. Surrounding prose, incomplete
objects, non-object JSON and interrupted responses remain rejected. No historical
private response text was published or used to assign new verification credit.
