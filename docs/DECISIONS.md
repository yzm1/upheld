# Upheld owns the method and the tools

Readers are engineers deciding how to build or adopt Upheld. This record states the current choices and when to revisit them.

## The product maps promises to planned and current defenses

Use this sentence: “Upheld records what software must keep true, how it should be upheld, what actually upholds it, and where the gaps are.”

Schema 0.2 calls the falsifiable rule an `obligation`; version 0.1 called it a `promise`. After that wire distinction, use the simpler word promise in product prose.

For each promise, keep four things visible:

| Part | What it records |
|---|---|
| Promise | What must stay true, with scope, conditions, harm, and unknowns |
| Defense plan | The best justified mechanism or set of mechanisms under stated project limits |
| Current defenses | Mechanisms that actually exist and claim to uphold the promise |
| Gap and next work | Missing, weak, unproven, stale, conflicting, or deliberately uncovered parts |

Evidence and bindings explain why a current defense may earn trust. They support this map; they do not replace it.

Teams may write promises while designing a new app. A survey may find candidate promises in an existing project. Both routes feed the same records.

## “Best defense” depends on the project

Defense kinds have no global rank. A plan may use one mechanism or several.

Compare choices by strength, scope, bypass paths, cost, feedback speed, required tools, independence from other defenses, likely harm, and whether a meaningful fault can challenge the mechanism.

If the user supplies priorities or hard limits, rank plans under those inputs. If key inputs are missing, show sound options and tradeoffs instead of forcing a winner.

A type guard may protect local state while an integration check covers a remote boundary. Schema 0.2 can record whether plan members work together, offer alternatives, or form layers.

## Trace freshness routes work; it does not define Upheld

Doorstop stamps parent links. Boundver fingerprints declared contracts and reports affected consumers. Requirements tools and build graphs do related work.

Do not present requirement links, reviewed hashes, suspect-link checks, or generic consumer traversal as Upheld's differentiator. [The trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records the split.

A change signal tells Upheld which promises, plans, current defenses, or evidence grounds may need another look. It does not say the promise is false.

Use existing systems as inputs where practical. Doorstop or StrictDoc may supply candidate promises and locators. Boundver or a build graph may supply component topology and affected consumers. Their reviewed, passing, suspect, or affected state never becomes Upheld evidence or a binding.

Build only enough local hashing and resolution to check Upheld's own records. Add more when real use proves the need.

## The survey, planner, checker, and reports belong together

The survey finds candidate promises and useful faults. The planner proposes defense plans. Evidence producers test current defenses. The checker compares current files with recorded grounds. Reports compare the plan with what the code has and show the gaps.

Boundver checks changes to declared contracts. Heldtospec checks data against contracts. Upheld keeps the broader promise-and-defense problem here.

Python remains the intended language. Apache-2.0 remains the license.

## Schema 0.2 is the current product model

[Schema 0.2](SCHEMA.md) separates `recommended_assurance`, `actual_defenses`, evidence, bindings, and accepted gaps. The gap report derives open plan-versus-current gaps instead of asking people to copy them into the register.

The first reporter only derives what the recorded mappings and evidence support. It does not yet rank plans, find omitted promises, inspect the live tree for stale evidence, or prove that several plan members cover a whole promise.

Version 0.1 remains readable. Its survey exporter and older examples keep working until the 0.2 upgrade path exists. That upgrade must not infer a preferred plan from existing tests or create human acceptance.

## The method remains authoritative for evidence judgments

From 6 September 2026, the [method](METHOD.md) governs survey and evidence judgments. The [checker rules](CHECKER.md) govern comparisons with recorded grounds. The [schema](SCHEMA.md) defines wire fields. A conflict between them is a defect to fix, never permission to invent evidence.

The dated snapshots remain under [history](history/README.md). The current method keeps all 27 rule IDs, and the checker design keeps all 23 checker and producer IDs.

## Keep the six built-in defense kinds

Use test, property, checker, ratchet, type, and runtime invariant. An accepted gap is a separate choice. An unfamiliar mechanism uses an `x-` name and a plain description.

Plans and current defenses remain different records. Finding a test does not show that it is the best defense. A suggested type or property guard stays in the plan until the project builds it.

## The next work must close product gaps

The [milestone](MILESTONE.md) sets the trial rules. The highest-value open work is: test the planner against independently reviewed cases; add a 0.1-to-0.2 upgrade path; run real evidence and checker commands; and import useful trace/change data without importing trust state.

Advanced history, rename handling, indexes, and review acknowledgments still wait for observed need. Hash rules remain a blocker for trustworthy product evidence.

The [positioning](POSITIONING.md) states the user problem. The [prior-art review](PRIOR_ART.md) sets the lower baseline. The [self-application](../examples/upheld-self-assurance/README.md) applies the new model to Upheld and keeps its own open gaps visible.
