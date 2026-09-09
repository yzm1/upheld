# Upheld owns the method and the tools

Readers are engineers deciding how to build or adopt Upheld. This record states the current choices and when to revisit them.

## The product maps promises to planned and current defenses

Use this sentence: “Upheld records what software must keep true, how it should be upheld, what actually upholds it, and where the gaps are.”

Schema 0.1 calls the falsifiable rule a `promise`. Product work should keep the wider purpose clear: for each promise, a team needs the desired defense plan, the defenses that exist now, the evidence behind them, and the gap between plan and reality.

Teams may write promises while designing a new app. A survey may also find candidate promises in an existing project. Both paths feed the same machine-readable view.

| Layer | What it records |
|---|---|
| Promise | What must stay true, with scope, conditions, consequence, and unknowns |
| Defense plan | The best justified mechanism or set of mechanisms under stated project limits |
| Current defenses | Mechanisms that actually exist and claim to uphold the promise |
| Gap and next work | Missing, weak, unproven, stale, conflicting, or deliberately uncovered parts |

Evidence and bindings explain why a current defense may be trusted. They support this map; they do not replace it.

“Continuous assurance” can describe the category after this explanation. It does not claim that the current repository provides a running service.

## “Best defense” means best under stated project limits

Upheld should help choose how to enforce a promise. Defense kinds have no global rank.

A plan may use one mechanism or several. The comparison can consider the factors below.

| Factor | Question |
|---|---|
| Strength | Does it prevent the bad state, detect it, or only sample for it? |
| Scope | Which part of the promise does it cover? |
| Bypass | How can the bad state still escape the mechanism? |
| Cost | What does it cost to run and maintain? |
| Speed | How quickly does it report a fault? |
| Environment | What tools, services, targets, or runtime access does it need? |
| Independence | Does it fail for the same reason as another defense? |
| Challenge | Can we seed or replay a meaningful fault and see it fire? |
| Earlier guard | Can a runtime check move into a type, build rule, or other earlier guard? |

If the user supplies priorities or limits, Upheld can rank plans under those inputs. If key inputs are missing, show justified options and the tradeoffs instead of forcing a rank.

A set of defenses can be better than one. A type restriction may guard local state while an integration check covers a remote boundary. Future schema work must let the plan state that both are needed without implying that either already exists.

## Upheld does not own generic trace freshness

Doorstop stamps parent links. Boundver fingerprints declared contracts and reports affected consumers. Requirements-as-code tools and build graphs do related work.

Do not present machine-readable requirement links, reviewed hashes, suspect-link detection, or generic affected-consumer traversal as Upheld's differentiator. [The trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records the comparison and its limits.

That lower layer helps route work. A change signal tells Upheld which promises, defense plans, current defenses, or evidence grounds may need another look. It does not define the product.

Use existing systems as inputs where practical. Doorstop or StrictDoc may supply candidate promises and locators. Boundver or a build graph may supply component topology and affected consumers. Imported review state, passing tests, link stamps, or affected status never become Upheld evidence or bindings.

Implement only enough local hashing and resolution to check Upheld's own records. Build more only if real use shows a missing capability.

## The survey, planner, checker, and reports belong together

The survey finds candidate promises and useful faults. The planner proposes defense patterns. Evidence producers test current defenses. The checker compares current files with recorded evidence. Reports compare the plan with what the code has and show the gaps.

Boundver checks changes to declared contracts. Heldtospec checks data against contracts. Upheld keeps its broader promise-and-defense scope here. Revisit this choice if adopters consistently find copying the design easier than using the tool.

Python remains the intended language. Apache-2.0 remains the license for code and documents. These choices do not require publishing a package now.

## This repository is the source for new method changes

From 6 September 2026, the [method](METHOD.md) governs new surveys. The [checker rules](CHECKER.md) govern comparisons with evidence. The [record schema](SCHEMA.md) defines fields. The machine schemas define allowed JSON shapes. A conflict between them is a defect to fix, never permission to invent evidence.

The original copied documents remain [dated snapshots](history/README.md). This revision preserves all 27 method rule IDs and all 23 checker/producer IDs. Field changes appear in the schema mapping.

The earlier plan waited for a heldtospec draft before moving authority. New work here no longer waits for that draft. An authenticated read of heldtospec's main tree on 6 September 2026 found no obligation-survey document at the previously named path. The inspected tree was `9ccd2766580e83b21f5d7717c7cee222f8fc6c2d`.

Upheld can now own its current method. This task leaves heldtospec files unchanged. Unpushed branch contents remain unknown. If that project restores a copy, it should link here or carry an explicit version. A later upstream revision will then need a side-by-side review.

## Six defense kinds preserve the useful differences

Use test, property, checker, ratchet, type, and runtime invariant. An accepted gap is a separate choice. [The schema table](SCHEMA.md) defines their evidence checks.

An unfamiliar mechanism uses an extension name and a plain description. Until an installed adapter declares support, it cannot receive a binding. This keeps unsupported work visible.

The old sketch's five-way vocabulary omitted differences already present in the method. A fixed mix is not a classifier target. Different projects can need different mixes.

## Keep advice separate from current defenses

Advice says what mechanism or set may fit a promise and why. It does not say that mechanism exists. Future schema work needs separate fields or records for the plan, a current defense, a run that challenged it, and the evidence a person chose.

Advice should name scope, bypass paths, a proposed fault challenge, cost, and what remains unknown. Finding an existing test does not show that it is adequate or preferable. A suggested type or property defense stays in the plan until the project implements it.

The plan-versus-current comparison should produce explicit gap classes. Examples include `no_defense`, `weaker_than_recommended`, `unproven_defense`, `stale_evidence`, `coverage_gap`, `unsupported_environment`, `conflicting_defenses`, and `accepted_gap`. Exact wire names remain schema work.

## Product learning sets the next scope

The [milestone](MILESTONE.md) sets the next deliverables and trial rules. The working effort split is 60% survey and trials, 30% checker demo, and 10% document repair. Review that split after the first trials.

Advanced history, rename handling, indexes, and review acknowledgments wait for an observed need. Hashing remains a blocker before trustworthy product evidence.

## Earlier tools set the bar Upheld must clear

The [prior-art review](PRIOR_ART.md) covers Doorstop, Boundver, ComplianceAsCode, shared control models, and safety-case upkeep. Fingerprinted links, tests of checks, and structured evidence all have precedents. The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) keeps that lower layer in its supporting role.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) exercises one existing checker and a simulated choice to rely on its evidence. Product commands and pilot results remain open. New work must improve promise coverage, defense choice, gap finding, or review cost against a stated baseline.
