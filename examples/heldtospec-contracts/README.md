# The hand survey records 44 promises and no accepted evidence

Readers can inspect this heldtospec contracts survey as a real input for Upheld. It covers public contract documents, library code, and CLI tests.

The survey dates from 6 September 2026 at heldtospec `c8c9362`. The target has not been rerun for this document update. The later test result used a different, dirty source state.

| Record | Count | Source |
|---|---:|---|
| Promises | 44 | obligations.register.json |
| Defenses | 78 | 66 test, 7 checker, 3 type, 2 runtime invariant |
| No defense and no gap | 4 | CTR-003, CTR-005, CTR-037, CTR-044 |
| Gaps | 4 | CTR-010, CTR-025, CTR-026, CTR-027 |
| Promises with next questions | 17 | Nonempty next_step |
| Bindings / evidence records | 0 / 0 | Empty committed files |
| Triage bullets | 19 | Recounted from the historical page |

The [serializer](build_register.py) writes choices already present in its source. It is not a scanner. The [original register](obligations.register.json) remains in the historical probe format.

## Five prominent findings concern observable behavior

| Promise | Historical finding | Observation |
|---|---|---|
| CTR-044 | Published example fails its witness | Exit 4; one errored clause |
| CTR-005 | Foreign-key documentation contradicts code | Published metadata-only claim differs from mapper |
| CTR-019 | Ungradeable result contradicts documented exit | Write/check modes exit 0 |
| CTR-021 | Expected verdict disappears after regeneration | Next write drops the field |
| CTR-016 | Verdict checker accepts source-name matches | Comments can satisfy the claimed link |

The [triage](triage.md) includes the smaller findings. H01–H19 in [the todo list](../../TODO.md) preserve their follow-ups. Current target checks must precede any claim that they remain defects.

## The library run does not grade the defenses

The later report records 149 passing library tests at heldtospec `7f9addc`, with four dirty files. It includes dbt execution. The combined CLI attempt exceeded 300 seconds and did not complete.

[The count audit](reconciliation.md) records the revision change and missing run details. Passing tests show observed suite behavior; they cannot establish that those tests detect each promised failure. Every defense remains unbound.

## The review copy exposes unresolved choices

[The review copy](review-register.json) maps the probe data to wire version 0.1. It preserves IDs, descriptions, and empty evidence state. It adds explicit unknown fields and remains unaccepted.

The [schema rules](../../docs/SCHEMA.md) distinguish shape checks from target resolution and evidence validity. Four promises still require a defense or authorized gap decision. The 78 artifact locations and subject scopes need a resolver check against the target before any accepted evidence.

The original type labels also need review: runtime model constraints do not necessarily supply static type guarantees. This page keeps the original counts instead of silently reclassifying them.
