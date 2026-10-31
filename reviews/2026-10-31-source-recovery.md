# Recover incomplete independent source collection

The Liquidation submission's revised candidate reached a truncated checker response
before a live freshness search ran. Report-only recovery then lacked tools to fill
that gap and treated the resulting insufficient report as a factual revision.

Verification now checks actual fetched reference contents and live search-result
blocks before generating claim reports. Missing evidence receives targeted source
calls: search first, then up to four missing references per call. Existing fetched
documents remain saved. Collection is bounded by 12 calls, three consecutive calls
without progress, and the existing per-run/daily budgets. No source failure grants
approval or consumes an article revision. Group reports are regenerated if new
source collection is needed, preserving superseded reports for audit.

Guarded recovery can reopen an automated insufficient outcome with the explicit
`--reopen-incomplete-sources` flag. It rejects factual claim errors, changed
candidates, old evidence, and later paid work. The old decision and failed check
remain; the new check receives no publication approval and retains revision counts.

Regression tests cover truncated source collection, missing references, tool errors,
crash recovery, genuine checker findings, and guarded reopening of the wrong outcome.
