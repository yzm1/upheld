# D01–D08 now have checked repository artifacts

Readers can review the completed document and schema work here. The work started from Upheld main at `3cc993edf7810901ce285b013e18fc670e18919a` on 6 September 2026.

**The repository now has current rules, a checked schema, and a repeatable documentation workflow.** Product evidence capture and the Upheld CLI remain open work.

## Each completed task has a concrete result

| Task | Before | After | Review |
|---|---|---|---|
| D01 | Current pages denied the real example existed | Status separates the hand survey, scripts, and unbuilt CLI | [README](../README.md) |
| D02 | Tagline could imply proof of software truth | Opening describes evidence and when it needs checking | [Product choice](DECISIONS.md) |
| D03 | Broad command design dominated next-work choices | Two deliverables, dated trial rules, and an explicit effort split | [Milestone](MILESTONE.md) |
| D04 | Method stored answers on promises; checker used defenses | All 27 method IDs map to per-defense evidence; Upheld owns new changes | [Method](METHOD.md) |
| D05 | Documents disagreed on five versus seven groupings | Six defense kinds, separate gaps, declared extensions, oracle compatibility | [Kind mapping](SCHEMA.md) |
| D06 | Ontology prose lacked schemas | Nine schemas cover first inputs/outputs and the probe format | [Schemas](../schemas/0.1/) |
| D07 | 18-item claim differed from 19 bullets; run revisions differed | Stable finding/run IDs, recounted totals, explicit unresolved probe count | [Count audit](../examples/heldtospec-contracts/reconciliation.md) |
| D08 | Upheld's own status drift had no defense | Small register, status checker, and seeded failure tests; no evidence binding | [Self-check](../examples/upheld-status/README.md) |

The current reference pages are shorter. The original method and checker remain unchanged in [dated snapshots](history/README.md), preserving the longer arguments and source-specific examples. Readers need those snapshots when reviewing the history behind a requirement.

## Checks cover shape, counts, and known failure cases

| Check | Observed result on 6 September 2026 | Limit |
|---|---|---|
| Nine schema compilers and real register checks | Pass | Shape cannot establish evidence validity |
| Original register and review copy | 44 promises, 78 defenses, four expected undecided claims | Target locators and scopes remain unchecked |
| Triage recount | 19 bullets; five odd, six ambiguous, eight missing | Probe total remains unknown |
| Supplied prose-check tests | 29 pass | Heuristics cannot establish clear meaning |
| Repository behavior tests | 10 pass | Synthetic faults test the listed rules only |
| README defense | Clean current input; stale claim and count drift detected | Arbitrary prose needs human review |
| Missing input | Distinct failure-to-inspect result | No product oracle record created |

Run [the contributor checks](../CONTRIBUTING.md) to reproduce these results. The prose checker runs on every current document in the maintained set. Historical copies retain their original wording and content hashes.

The local environment lacked a schema package. Local checks used fastjsonschema 2.21.2 from its source tag at `4f1ed6d9c0462f3522a66f49c8f3dc482300101b`. The CI requirements pin the same version.

## The remaining limits belong to named tasks

P01–P04 still define exact run capture and cross-machine scope. C01 still owes hash rules and agreement vectors. C02 still owes the product validator and all semantic checks. Publishing record shapes does not close those tasks.

The existing heldtospec example remains historical. No heldtospec file changed. Its missing probe logs, dirty-file contents, and incomplete CLI execution remain explicit. H01–H19 require a current target check.
