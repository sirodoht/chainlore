# Verification cutoff and budget recovery — 31 October 2026

The Liquidation correction stopped because its independent checker reached
`max_tokens` after opening 13 sources. The old workflow treated the incomplete
report as a substantive failure, discarded the draft checkpoint and requested
fresh research. That next call exceeded the original per-run reservation cap.

The repair retains the exact candidate and independent fetched-source context.
At most two report-only calls can finish the assessment without more tool calls
or writing. A completed report must still satisfy every evidence, coverage, date
and exact-source publication requirement. Interrupted output cannot become approval
or a factual verdict. Old audit records remain intact during recovery.

Completed calls now settle to reported usage including cache tokens; unknown-cost
calls retain estimates. Server-tool calls reserve additional sampling headroom.
The per-run admission limit increases from 500,000 to 1,000,000 tokens; the daily
limit stays 2,000,000. Estimates are explicitly not provider-enforced cost ceilings.
Public blockers no longer claim recovery attempts were exhausted when a budget
prevented the next call.

Validation covers saved-evidence recovery, crash resumption without duplicate calls,
partial-output refusal, bounded attempts, stale-evidence refusal, real findings,
usage settlement and overruns, cache input, unknown usage and exact budget messages.

Provider behavior references:
- https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools
