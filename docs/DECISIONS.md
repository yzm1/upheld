# Upheld owns the method and the tools

Readers are engineers deciding how to build or adopt Upheld. This record states the current choices and when to revisit them.

## The product maps obligations to intended and actual assurance

Use this sentence: “Upheld records what software must keep true, how it should be upheld, what actually upholds it, and where the assurance gaps are.”

The current schema calls the falsifiable obligation a `promise`. That wire name can remain during schema 0.1. Product discussions should keep the larger purpose visible: a promise record is useful because a team wants to know how the obligation should be enforced, whether that enforcement exists, whether it has earned trust, and what remains uncovered.

Upheld supports both authored and discovered obligations. A team may write obligations while specifying an application, before implementation. A survey may also extract candidate obligations from an existing project. Both paths feed the same assurance model.

For each obligation, preserve four distinct layers:

1. **Obligation.** What must remain true, including scope, conditions, consequence, and uncertainty.
2. **Recommended assurance.** The best justified defense pattern or portfolio under declared constraints.
3. **Actual assurance.** The implemented defenses that currently claim to uphold the obligation, with their scope and evidence.
4. **Gap and attention.** What is absent, weaker than recommended, unproven, stale, unreachable, conflicting, or deliberately accepted as a gap.

The main product view compares layers two and three and makes layer four visible. Evidence and bindings explain why an actual defense may be relied upon; they are part of this model rather than the whole product.

“Continuous assurance” can describe the category after this explanation. It is not a claim that the current repository provides a running service.

## “Best defense” means best under stated constraints

Upheld should help choose how to enforce an obligation. It must not pretend that defense kinds have a universal ranking.

A recommendation may prefer one defense or a portfolio of defenses. The comparison can consider:

- strength of prevention or detection;
- validated scope and coverage;
- known bypass paths and residual uncertainty;
- independence or diversity between defenses;
- feedback latency;
- runtime and maintenance cost;
- required environment or infrastructure;
- reachability and failure consequence;
- ease of adversarial challenge;
- whether the guarantee can move earlier, such as from runtime detection to construction-time prevention.

An “optimal” recommendation is therefore conditional on an objective and constraints. If those inputs are missing, Upheld should expose several justified choices or state that no ranking is established.

A portfolio can be better than one mechanism. For example, a type restriction may prevent invalid local states while an integration check defends a remote boundary. The schema must eventually represent that recommendation without implying that either mechanism already exists.

## Upheld does not own generic trace freshness

Doorstop stamps parent links. Boundver fingerprints declared contracts and reports affected consumers. Requirements-as-code tools and build graphs do related work.

Do not present machine-readable requirement links, reviewed hashes, suspect-link detection, or generic affected-consumer traversal as Upheld's differentiator. [The trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records the comparison and its consequences.

That layer supports the main product. Change context tells Upheld which obligations, defenses, recommendations, or evidence grounds may need another look. It does not define Upheld's purpose.

Use existing systems as inputs where practical. Doorstop or StrictDoc may supply candidate obligations and locators. Boundver or a build graph may supply component topology and affected consumers. Imported review state, passing tests, link stamps, or affected status never become Upheld evidence or bindings.

Implement only enough local hashing and resolution to check Upheld's own evidence records. Build more only if measured workflows need something the existing tools cannot supply.

## The survey and checker belong in a dedicated repository

The survey produces candidate obligations and useful findings. A recommender proposes defense patterns. Evidence producers assess implemented defenses. The checker compares the current tree with recorded evidence. Reports compare intended and actual assurance and surface gaps. These pieces share a record format.

Boundver checks changes to declared contracts. Heldtospec checks data against contracts. Upheld keeps its broader software-obligation scope here. Revisit this choice if adopters consistently find copying the design easier than using the tool.

Python remains the intended language. Apache-2.0 remains the license for code and documents. These choices do not require publishing a package now.

## This repository is the source for new method changes

From 6 September 2026, the [method](METHOD.md) governs new surveys. The [checker rules](CHECKER.md) govern comparisons with evidence. The [record schema](SCHEMA.md) defines fields. The machine schemas define allowed JSON shapes. A conflict between them is a defect to fix, never permission to manufacture evidence.

The original copied documents remain [dated snapshots](history/README.md). This revision preserves all 27 method requirement IDs and all 23 checker/producer IDs. Field changes appear in the schema mapping.

The earlier plan waited for a heldtospec draft before moving authority. New work here no longer waits for that draft. An authenticated read of heldtospec's main tree on 6 September 2026 found no obligation-survey document at the previously named path. The inspected tree was `9ccd2766580e83b21f5d7717c7cee222f8fc6c2d`.

Upheld can establish its own authority now. This task leaves heldtospec files unchanged. Unpushed branch contents remain unknown. If that project restores a copy, it should link here or carry an explicit version. The cost of proceeding now is that a later upstream revision will need a side-by-side review.

## Six defense kinds preserve the observed distinctions

Use test, property, checker, ratchet, type, and runtime invariant. An accepted gap records a separate decision. [The schema table](SCHEMA.md) defines their evidence checks.

An unfamiliar mechanism uses an extension name and a plain description. Until an installed adapter declares support, it cannot receive a binding. This preserves the observation while exposing unsupported work.

The old sketch's five-way vocabulary omitted distinctions already present in the method. A fixed distribution is not a classifier target. Different projects and input sources can have different mixes.

## Keep advice separate from implemented defenses

A recommendation says what mechanism or portfolio may fit an obligation and why. It does not say that mechanism exists. Future schemas need separate records or fields for advice, an implemented defense, a run that challenged it, and the evidence a person chose.

The advice should name scope, bypass paths, a proposed fault challenge, cost, and what remains uncertain. Discovering an existing test does not show that it is adequate or preferable. A recommended type or property defense stays advice until the project implements it.

The comparison between recommendation and reality should produce explicit gap classes. Examples include `no_defense`, `weaker_than_recommended`, `unproven_defense`, `stale_evidence`, `coverage_gap`, `unsupported_environment`, `conflicting_defenses`, and `accepted_gap`. Exact wire names remain schema work.

## Product learning sets the next scope

The [milestone](MILESTONE.md) sets the next deliverables and evaluation rules. The working effort split is 60% survey and trials, 30% checker demonstration, and 10% document repair. These are planning choices; review them after the first trials.

Advanced history, rename handling, indexes, and review acknowledgments wait for an observed need. Hashing remains an explicit blocker before trustworthy product evidence.

## Earlier tools establish the value we must demonstrate

The [prior-art review](PRIOR_ART.md) covers Doorstop, Boundver, ComplianceAsCode, shared control models, and assurance-case upkeep. Fingerprinted links, tests of checks, and structured evidence have precedents. The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) keeps that lower layer in its supporting role.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) exercises one existing checker and a simulated choice to rely on its evidence. Product commands and pilot results remain open. New features must improve obligation coverage decisions, defense choice, gap detection, or review work against a stated baseline.
