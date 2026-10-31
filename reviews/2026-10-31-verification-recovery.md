# Verification cutoff and budget recovery — 31 October 2026

The Liquidation correction stopped because its independent checker reached
`max_tokens` after opening 13 sources. The old workflow treated the incomplete
report as a substantive failure, discarded the draft checkpoint and requested
fresh research. That next call exceeded the original per-run reservation cap.

The repair retains the exact candidate and independent fetched-source context.
Groups of at most four units receive at most two report-only attempts each,
without more tool calls or writing. Approval requires complete combined coverage. A completed report must still satisfy every evidence, coverage, date
and exact-source publication requirement. Interrupted output cannot become approval
or a factual verdict. Old audit records remain intact during recovery.

Completed calls now settle to reported usage including cache tokens; unknown-cost
calls retain estimates. Server-tool calls reserve additional sampling headroom.
The per-run admission limit increases from 500,000 to 1,500,000 tokens; the daily
limit stays 2,000,000. Estimates are explicitly not provider-enforced cost ceilings.
Public blockers no longer claim recovery attempts were exhausted when a budget
prevented the next call.

Validation covers saved-evidence recovery, crash resumption without duplicate calls,
partial-output refusal, bounded attempts, stale-evidence refusal, real findings,
usage settlement and overruns, cache input, unknown usage and exact budget messages.

Provider behavior references:
- https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools


The first live whole-report retry also exhausted its 32,000-token output allowance.
Report recovery therefore uses small claim groups with independent checkpoints.
The earlier whole-report attempt remains in the audit and usage ledger. The final
per-job limit is 1,500,000 tokens to accommodate the measured recovery cost; the
shared daily limit remains unchanged. Partial group results cannot publish an article.

A live non-publishing probe of the first four units completed with `end_turn`, no
validation errors and one completed group. The overall check correctly remained
pending. The probe asserted that both candidate and fetched sources exactly matched
material already sent to the same checker in the authorized recovery; no contact
fields or submission text were included. Production state was not changed by it.
