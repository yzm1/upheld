# Show useful findings before expanding the checker

Readers are engineers planning the next Upheld release. The next milestone delivers a survey workflow and a small example that keeps evidence honest.

The thresholds below are project choices recorded on 6 September 2026. They are not industry standards or measured baselines.

## Two deliverables make the result observable

| Deliverable | Required demonstration | Completion record |
|---|---|---|
| Survey and cheap probes | An unfamiliar engineer reaches a real finding without hand-authoring six files | Candidate sources, confirmed finding, elapsed time, review minutes |
| Checker slice | Validate, compute basis, run one oracle, append evidence, bind, verify, change a ground, regenerate | Command outputs, actual evidence, expected drift, unchanged stale result after regeneration |

Hash rules and run context need agreement before the checker can produce trustworthy evidence. JSON schemas only check record shape. The historical 44-promise input should expose its four undecided promises during validation.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) exercises a closed README case with simulated acceptance. It is an early conformance check. It does not complete either deliverable or the independent trials.

The product demonstration must reject a mismatched defense, unsupported scope, inconclusive record, and unavailable input. Changed claims, checks, subjects, and declared inputs must name the affected ground. Regeneration must preserve evidence and choices. Track unsupported lineage and component cases explicitly.

## Register predictions before the trials

Use two independent public projects: one ordinary mature codebase outside Upheld's source projects, and another in a different language. Record target choice, commit, component, environment, and the engineer's prior knowledge before each trial.

Each discovery trial lasts two hours. Apply the [survey outcome definitions](SURVEY_TOOL.md): a useful finding is a distinct, consequential defect or accepted new promise, confirmed against the target. Primary novelty means new to the project, checked with the maintainer. Unknown novelty remains unresolved. Record duplicates, wrong claims, unresolved questions, probe time, and all human review time, including setup and failed triage. The maintainer adjudicates disputed findings against the source and run record.

E01 must register source boundaries, sampled omission checks, reviewers, and comparison arms before execution. The [research comparison plan](SURVEY_RESEARCH.md) includes human search, a non-generative workflow, a direct agent prompt, and the hybrid proposal. Feasibility pilots and controlled method comparisons need separate result claims.

The initial success rule requires at least one confirmed useful finding in each trial and at most 60 human review minutes per finding. A zero-finding trial or a higher review cost triggers a scope review before adding checker features. Small samples limit any general claim.

When testing categories, compare per-item choices against independently reviewed labels. Use the same categories and include abstentions. Category totals alone cannot pass the trial.

## Recheck evidence after a month of changes

Follow the original evidence through roughly a month of real development. Report actual elapsed time and relevant changes. If nothing relevant changed, the trial supplies no upkeep result.

Before the follow-up, cap semantic review at 30 minutes per active project-week for these pilot components. Measure missed stale assertions, correct reassessments, unnecessary reviews, queue age, and time to clear. Any confirmed silent stale result blocks release. Exceeding the review budget triggers narrower oracle scope or workflow revision.

Include both small refactors and large contract changes. Measure distinct review decisions and all affected defenses separately. Suppressing real impact to reduce the queue cannot count as an improvement.

Historical replay may test the protocol earlier. Label it as replay and keep its results separate from live follow-up. Do not claim real-world success from seeded drift alone.

## Keep most effort on the survey and trials

| Work | Initial share |
|---|---:|
| Survey, probes, independent trials | 60% |
| Minimal checker demonstration | 30% |
| Status and schema repairs | 10% |

Review the allocation after the first two trials. These shares guide planning and create no staffing commitment.

Advanced rename tracking, stored indexes, history explanations, broader adapters, and acknowledgment commands wait for evidence of need. [The todo list](../TODO.md) preserves their admission conditions.
