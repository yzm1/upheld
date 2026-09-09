# Upheld owns the method and the tools

Readers are engineers deciding how to build or adopt Upheld. This record states the current choices and when to revisit them.

## The product tracks evidence for software promises

Use this sentence: “Upheld records what code promises, what evidence defends each promise, and when that evidence needs another check.”

The earlier tagline ended with “whether it still does.” Readers could take that to mean proof of the promise itself. The new sentence names the narrower result. The trade is a longer opening sentence.

“Continuous assurance” can describe the category after that sentence. It is not a claim that the current repository provides a running service.

## Upheld does not own generic trace freshness

Doorstop stamps parent links. Boundver fingerprints declared contracts and reports affected consumers. Requirements-as-code tools and build graphs do related work.

Do not present machine-readable requirement links, reviewed hashes, suspect-link detection, or generic affected-consumer traversal as Upheld's differentiator. [The trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records the comparison and its consequences.

Upheld starts after that signal. It records a falsifiable promise, the mechanism claimed to defend it, why that mechanism fits, how to challenge it, what a run observed, which record a person chose to rely on, and which changed inputs force another review.

Use existing systems as inputs where practical. Doorstop or StrictDoc may supply candidate promises and locators. Boundver or a build graph may supply component topology and affected consumers. Imported review state, passing tests, link stamps, or affected status never become Upheld evidence or bindings.

Implement only enough local hashing and resolution to check Upheld's own evidence records. Build more only if measured workflows need something the existing tools cannot supply.

## The survey and checker belong in a dedicated repository

The survey produces candidate promises and useful findings. Evidence producers assess defenses. The checker compares the current tree with recorded evidence. These pieces share a record format.

Boundver checks changes to declared contracts. Heldtospec checks data against contracts. Upheld keeps its broader software-promise scope here. Revisit this choice if adopters consistently find copying the design easier than using the tool.

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

A recommendation says what mechanism may fit a promise and why. It does not say that mechanism exists. Future schemas need separate records or fields for advice, an implemented defense, a run that challenged it, and the evidence a person chose.

The advice should name scope, bypass paths, a proposed fault challenge, cost, and what remains uncertain. Discovering an existing test does not show that it is adequate or preferable. A recommended type or property defense stays advice until the project implements it.

## Product learning sets the next scope

The [milestone](MILESTONE.md) sets the next deliverables and evaluation rules. The working effort split is 60% survey and trials, 30% checker demonstration, and 10% document repair. These are planning choices; review them after the first trials.

Advanced history, rename handling, indexes, and review acknowledgments wait for an observed need. Hashing remains an explicit blocker before trustworthy product evidence.

## Earlier tools establish the value we must demonstrate

The [prior-art review](PRIOR_ART.md) covers Doorstop, Boundver, ComplianceAsCode, shared control models, and assurance-case upkeep. Fingerprinted links, tests of checks, and structured evidence have precedents. The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) makes the product split explicit. Upheld combines these ideas around the reasons to rely on a software defense.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) exercises one existing checker and a simulated choice to rely on its evidence. Product commands and pilot results remain open. New features must improve useful findings or review work against a stated baseline, including a simpler fingerprinted-trace baseline where relevant.
