# Real survey counts exist; product upkeep remains unmeasured

Readers deciding what to build can use the measurements below. The historical observations below date from 5–6 September 2026. The historical reports supply no raw oracle records.

## The hand survey provides counts and reported outcomes

| Measure | Observation | Source and limit |
|---|---:|---|
| Promises | 44 | Committed heldtospec register at Upheld `3cc993e` |
| Candidate defenses | 78 | Links from reading; zero bindings |
| Next questions | 17 | Nonempty `next_step` entries |
| Triage bullets | 19 | Five odd, six ambiguous, eight missing |
| Reported passing library tests | 149 | Later execution at heldtospec `7f9addc` with four dirty files |

[The reconciliation](../examples/heldtospec-contracts/reconciliation.md) separates these units and records missing probe details. No human-cost or discovery-yield estimate is justified by these counts.

## Synthetic loading does not justify a stored index

The [synthetic script](synthetic_register.py) creates 10,000 promises and 21,650 defenses, about 12.2 MB. These synthetic inputs do not represent a surveyed project.

| Operation | 5 September | 6 September |
|---|---:|---:|
| JSON load | 108 ms | 481 ms |
| Build reverse index | 11 ms | 21 ms |
| Query 12 changed files | 0.07 ms; 469 defenses | 0.08 ms; 500 defenses |

The original reports used one Linux container under unknown concurrent load. The second sample used its own fixed seed for changed files. These results support starting without a stored index; they do not measure product verification cost.

## History reconstruction was too slow for routine checks

A heldtospec history query over a seventeen-line range exceeded 120 seconds at 1,262 commits. The background run eventually returned one commit. This is the historical result recorded at Upheld `3cc993e`.

Keep history out of routine verification. An optional explanation command can use it later and report unavailable history explicitly.

## Discovery and upkeep trials still need runs

[The milestone](../docs/MILESTONE.md) defines two-hour discovery trials and a month of follow-up. Record review time, missed stale assertions, unnecessary reviews, queue age, and subject-scope cost. No result for those trials exists yet.

## The 7 September self-audit records local fault challenges

[The self-audit](../docs/SELF_AUDIT.md) records package failures and repairs with explicit run context. These new local runs supply no accepted product evidence or independently measured agent benefit.
