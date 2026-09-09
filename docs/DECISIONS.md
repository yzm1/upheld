# Upheld owns the method and the tools

Readers are engineers deciding how to build or adopt Upheld. This record states the current choices and when to revisit them.

## The product maps obligations to planned and current defenses

Use this sentence: “Upheld records what software must keep true, how it should be upheld, what actually upholds it, and where the gaps are.”

Schema 0.2 calls the falsifiable rule an `obligation`. Version 0.1 called it a `promise`. For each obligation, a team needs the desired defense plan, the defenses that exist now, the evidence behind them, and the gap between plan and reality.

Teams may write obligations while designing a new app. A survey may also find candidate obligations in an existing project. Both paths feed the same machine-readable view.

| Layer | What it records |
|---|---|
| Obligation | What must stay true, with scope, conditions, consequence, and unknowns |
| Defense plan | The best justified mechanism or set of mechanisms under stated project limits |
| Current defenses | Mechanisms that actually exist and claim to uphold the obligation |
| Gap and next work | Missing, weak, unproven, stale, conflicting, or deliberately uncovered parts |

Evidence and bindings explain why a current defense may be trusted. They support this map; they do not replace it.

“Continuous assurance” can describe the category after this explanation. It does not claim that the current repository provides a running service.

## “Best defense” means best under stated project limits

Upheld should help choose how to enforce an obligation. Defense kinds have no global rank.

A plan may use one mechanism or several. The comparison can consider strength, scope, bypass paths, cost, feedback speed, required environment, independence from other defenses, failure consequence, and whether a meaningful fault can challenge the mechanism.

If the user supplies priorities or limits, Upheld can rank plans under those inputs. If key inputs are missing, show justified options and tradeoffs instead of forcing a rank.

A set of defenses can be better than one. A type restriction may guard local state while an integration check covers a remote boundary. Schema 0.2 represents plan members and whether they are required together, alternatives, or layers.

## Upheld does not own generic trace freshness

Doorstop stamps parent links. Boundver fingerprints declared contracts and reports affected consumers. Requirements-as-code tools and build graphs do related work.

Do not present machine-readable requirement links, reviewed hashes, suspect-link detection, or generic affected-consumer traversal as Upheld's differentiator. [The trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records the comparison and its limits.

That lower layer helps route work. A change signal tells Upheld which obligations, defense plans, current defenses, or evidence grounds may need another look. It does not define the product.

Use existing systems as inputs where practical. Doorstop or StrictDoc may supply candidate obligations and locators. Boundver or a build graph may supply component topology and affected consumers. Imported review state, passing tests, link stamps, or affected status never become Upheld evidence or bindings.

Implement only enough local hashing and resolution to check Upheld's own records. Build more only if real use shows a missing capability.

## The survey, planner, checker, and reports belong together

The survey finds candidate obligations and useful faults. The planner proposes defense patterns. Evidence producers test current defenses. The checker compares current files with recorded evidence. Reports compare the plan with what the code has and show the gaps.

Boundver checks changes to declared contracts. Heldtospec checks data against contracts. Upheld keeps its broader obligation-and-defense scope here.

Python remains the intended language. Apache-2.0 remains the license for code and documents.

## Schema 0.2 is the current product model

[Schema 0.2](SCHEMA.md) now separates `recommended_assurance`, `actual_defenses`, evidence, bindings, and accepted gaps. Open plan-versus-current gaps belong in a derived assurance report rather than being hand-maintained as canonical state.

The first reporter derives only gaps justified by the recorded structure and evidence. It does not yet rank plans, discover omitted obligations, inspect the live tree for stale evidence, or prove composition across plan members.

Version 0.1 remains a supported compatibility format. Its survey exporter and older examples continue to work until migration is implemented. Migration must never infer a preferred plan from existing tests or create acceptance.

## This repository is the source for new method changes

From 6 September 2026, the [method](METHOD.md) governs new surveys and evidence judgments. The [checker rules](CHECKER.md) govern comparisons with evidence. The [record schema](SCHEMA.md) defines fields. A conflict between them is a defect to fix, never permission to invent evidence.

The original copied documents remain [dated snapshots](history/README.md). This revision preserves all 27 method rule IDs and all 23 checker/producer IDs.

## Six defense kinds preserve the useful differences

Use test, property, checker, ratchet, type, and runtime invariant. An accepted gap is a separate choice. [The schema](SCHEMA.md) defines their record shapes and evidence expectations.

An unfamiliar mechanism uses an extension name and a plain description. Until an installed adapter declares support, it cannot receive a binding.

## Keep advice separate from current defenses

Schema 0.2 now enforces the central distinction. `recommended_assurance` holds plans and plan members. `actual_defenses` holds mechanisms that exist. Evidence belongs to actual defenses. Bindings remain human choices.

Advice names scope, bypass paths, a proposed fault challenge, cost, and what remains unknown. Finding an existing test does not show that it is adequate or preferable. A suggested type or property defense stays in the plan until the project implements it.

The assurance report currently names `no_plan`, `no_defense`, `weaker_than_recommended`, `unproven_defense`, `stale_evidence`, `coverage_gap`, `unsupported_environment`, `divergence_unreviewed`, `conflicting_defenses`, and `accepted_gap`. The first implementation derives only the subset it can justify.

## Product learning sets the next scope

The [milestone](MILESTONE.md) sets the next deliverables and trial rules. The next high-value gaps are a real defense recommender, a 0.2 survey/migration path, live evidence production and verification, and imports from existing trace/change systems.

Advanced history, rename handling, indexes, and review acknowledgments still wait for observed need. Hashing remains a blocker before trustworthy product evidence.

## Earlier tools set the bar Upheld must clear

The [positioning](POSITIONING.md) states the user problem. The [prior-art review](PRIOR_ART.md) covers Doorstop, Boundver, ComplianceAsCode, shared control models, and safety-case upkeep. The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) keeps that lower layer in its supporting role.

New work must improve obligation coverage, defense choice, gap finding, or review cost against a stated baseline. The self-assurance example applies this same standard to Upheld rather than treating schema work as proof of the product.
