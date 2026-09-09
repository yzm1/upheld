# Show useful promise coverage before expanding the checker

Readers are engineers planning the next Upheld release. The next milestone should show the full product flow: find or write promises, choose how to hold them, find what holds them now, show the gap, and keep the result current.

The thresholds below are project choices recorded on 6 September 2026 and extended on 9 September 2026. They are not industry standards or measured baselines.

## Three deliverables make the result observable

| Deliverable | Required demonstration | Completion record |
|---|---|---|
| Promise survey | An unfamiliar engineer reaches real promises and useful findings without hand-authoring six files | Candidate sources, reviewed promises, elapsed time, review minutes |
| Defense plan and gap view | For reviewed promises, propose justified defense plans, inventory current defenses, and show the differences without promoting advice into implementation | Plans, actual defenses, gap classes, reviewer choices |
| Checker slice | Validate, compute basis, run one oracle, append evidence, bind, verify, change a ground, regenerate | Command outputs, actual evidence, expected drift, unchanged stale result after regeneration |

Hash rules and run context need agreement before the checker can produce trustworthy evidence. JSON schemas only check record shape. The historical 44-promise input should expose its four undecided promises during validation.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) exercises a closed README case with simulated acceptance. It is an early conformance check. It does not complete the defense-plan deliverable or the independent trials.

The product demo must reject a mismatched defense, unsupported scope, inconclusive record, and unavailable input. Changed promises, defenses, subjects, and declared inputs must name the affected ground. Cache rebuilds must preserve evidence and human choices.

## Register predictions before the trials

Use two independent public projects: one ordinary mature codebase outside Upheld's source projects, and another in a different language. Record target choice, commit, component, environment, and the engineer's prior knowledge before each trial.

Each discovery trial lasts two hours. Apply the [survey outcome definitions](SURVEY_TOOL.md): a useful finding is a distinct, consequential defect or accepted new promise, confirmed against the target. Primary novelty means new to the project, checked with the maintainer. Unknown novelty remains unresolved. Record duplicates, wrong claims, unresolved questions, probe time, and all human review time, including setup and failed triage.

E01 must register source boundaries, sampled omission checks, reviewers, and comparison arms before execution. The [research comparison plan](SURVEY_RESEARCH.md) includes human search, a non-generative workflow, a direct agent prompt, and the hybrid proposal. Feasibility pilots and controlled method comparisons need separate result claims.

The initial discovery success rule requires at least one confirmed useful finding in each trial and at most 60 human review minutes per finding. A zero-finding trial or a higher review cost triggers a scope review before adding checker features. Small samples limit any general claim.

## Test defense plans against what the code has

The main product question comes after promise discovery: what should hold each promise, what does hold it now, and what gap remains?

Select a reviewed subset with independently prepared defense plans. Reviewers should record acceptable plans before seeing Upheld's advice. The reference answer may include several good plans when tradeoffs differ.

For each promise, score:

- whether the plan covers the full stated scope and conditions;
- whether its rationale matches the failure modes;
- whether it names important bypass paths and remaining unknowns;
- whether it proposes a useful fault challenge;
- whether it respects stated cost, latency, runtime, and infrastructure limits;
- whether it finds a multi-defense set when one mechanism is too narrow;
- whether it finds the current defenses without relying on names alone;
- whether it separates missing, weak, unproven, stale, and deliberately accepted gaps;
- whether the suggested next action would materially improve the state;
- human review minutes needed to accept, modify, or reject the result.

Do not require one universal order of defense kinds. If reviewers disagree between two sound plans, keep the case contested instead of forcing a single label.

A technically stronger plan that violates the project's stated limits is not a better answer. A current defense with no adequate evidence stays visible with an evidence gap.

## Compare upkeep with a simpler fingerprint baseline

Doorstop marks a link suspect when its upstream fingerprint changes. Boundver lists consumers after a declared contract drifts. These tools set a useful lower baseline. [The product boundary](TRACE_FRESHNESS_BOUNDARY.md) explains why.

At least one follow-up must also run against a small tool or fixture that stores named links, records hashes, and lists changed, missing, or affected links. It does not need defense plans, oracles, evidence logs, or bindings.

Ask whether Upheld earns the extra work. Record, for each arm:

- which stale or affected links it surfaced;
- which existing defenses failed a fault challenge;
- which fresh or passing traces led to unsupported claims;
- which gaps appeared only after comparing the plan with current defenses;
- which findings needed another human check and which did not;
- review minutes and queue age;
- cases where a narrower checked scope saved work without hiding impact;
- whether cache rebuilds preserved the person's recorded choice;
- useful next actions that the simpler tool could not give.

A longer report is not a gain. If Upheld does not improve promise coverage or expose consequential gaps that the simpler tool misses, its extra records are not worth the cost for that workflow.

## Recheck the map after a month of changes

Follow the original promises, defense plans, current defenses, and evidence through roughly a month of real work. Report actual elapsed time and relevant changes. If nothing relevant changed, the trial supplies no upkeep result.

Before the follow-up, cap semantic review at 30 minutes per active project-week for these pilot components. Measure missed stale claims, changed plans, correct rechecks, unnecessary reviews, queue age, and time to clear. Any confirmed silent stale result blocks release. Exceeding the review budget triggers narrower oracle scope or workflow revision.

Include both small refactors and large contract changes. Measure distinct review choices and all affected defenses separately. Suppressing real impact to reduce the queue cannot count as an improvement.

Historical replay may test the protocol earlier. Label it as replay and keep its results separate from live follow-up. Do not claim real-world success from seeded drift alone.

## Keep most effort on the survey, defense plan, and trials

| Work | Initial share |
|---|---:|
| Survey, defense plans, gap review, independent trials | 60% |
| Minimal checker demonstration | 30% |
| Status and schema repairs | 10% |

Review the split after the first two trials. These shares guide planning and create no staffing commitment.

Advanced rename tracking, stored indexes, history explanations, broader adapters, and acknowledgment commands wait for evidence of need. [The todo list](../TODO.md) preserves their admission conditions.
