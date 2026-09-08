# The merge review repairs three defects and limits the new demo

Readers are maintainers reviewing PRs 7 and 8 on 8 September 2026. The combined changes preserve the self-audit and canonical survey output. They apply the prior-art lessons and add an evidence lifecycle probe.

## Each reported defect has a regression check

| Review finding | Repair and check |
|---|---|
| A valid saved reply could disappear after its status changed to rejected. | Export verifies the raw response, hash, result fields, and failure before skipping it. Tests include two valid submissions, edited rejection fields, and a failure before a reply arrives. |
| The self-audit's no-evidence claim could become false while document checks passed. | The fixture guard checks its empty log and bindings. Missing logs, populated logs, and unexpected bindings fail. |
| A probe invoked outside its selected checkout crashed while recording hashes. | The record hashes the invoking script separately. A regression runs the probe from another directory against the selected checkout. |
| Both PRs changed the checked artifact list. | The resolved list validates both examples and preserves the survey's reproducible-export check. |

## The added lifecycle keeps acceptance explicitly simulated

The [demo](EVIDENCE_LIFECYCLE.md) uses the existing README checker. Its challenge distinguishes the working checker from a weakened mutant. Tests cover changed grounds, stale regenerated views, bad evidence IDs, incompatible records, added files, missing inputs, and preserved output.

An initial acceptance test used the full repository where only a closed fixture was supported. It could have failed for the wrong reason. The repaired tests first establish a fresh fixture, then change one condition. A later record with altered evidence bytes cannot keep its earlier identity.

The demo creates no human acceptance and no product command. The [prior-art review](PRIOR_ART.md) narrows the novelty claims. Method 1.4 keeps all rule IDs and strengths. Product hashing, lineage, component support, and independent trials remain open.

## The validation record separates local checks from hosted checks

The [local validation record](../measurements/lifecycle-2026-09-08/validation.json) names the tested source and check outcomes. The [observation](../measurements/lifecycle-2026-09-08/observation.json) records actual fault runs and expected lifecycle results. Hosted checks must pass for the final PR commits before merge.

These results establish behavior within the tested cases. They do not establish model quality, independent human agreement, signed evidence, or review cost in another project.
