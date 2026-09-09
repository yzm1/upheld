# Upheld owns the method and the tools

Readers are engineers deciding how to build or adopt Upheld. This record states the current choices and when to revisit them.

## The product tracks evidence for software promises

Use this sentence: “Upheld records what code promises, what evidence defends each promise, and when that evidence needs another check.”

The earlier tagline ended with “whether it still does.” Readers could take that to mean proof of the promise itself. The new sentence names the narrower result. The trade is a longer opening sentence.

“Continuous assurance” can describe the category after that sentence. It is not a claim that the current repository provides a running service.

## Upheld does not own generic trace freshness

Doorstop's suspect-link stamps and Boundver's contract fingerprints establish the lower-level pattern of recording identity, linking downstream work, and surfacing relationships after drift. Requirements-as-code, build graphs, and ALM tools provide related mechanisms.

Upheld must not present machine-readable requirement links, fingerprinted reviewed state, suspect-link detection, or generic affected-consumer traversal as its differentiator. [The trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records the comparison and its consequences.

Upheld's product responsibility begins with justified reliance: the falsifiable promise, an asserted or recommended defense, the reason that mechanism is appropriate, the fault model and oracle that challenge it, the resulting evidence and basis, a person's explicit binding, and changed-ground invalidation that does not claim semantic failure.

Use existing systems as inputs where practical. Doorstop or StrictDoc may supply candidate promises and locators. Boundver or a build graph may supply component topology and impact context. Imported review state, passing tests, link stamps, or affected status never become Upheld evidence or bindings.

Implement only the minimum standalone freshness machinery Upheld needs. Revisit that boundary only if measured workflows require semantics that the existing systems cannot supply.

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

## Recommendations stay separate from implemented defenses

A recommendation about how best to enforce a promise is valuable design advice, not evidence that the mechanism exists. Future schema work must preserve the distinction between a recommended defense pattern, an implemented candidate defense, observed evidence that challenged it, and a person's accepted binding.

A recommendation should carry its rationale, intended scope, bypass paths, proposed fault challenge, cost, and residual uncertainty. Discovering an existing test does not establish that it is adequate or preferable. A recommended type or property defense must not appear in the register as an implemented defense until it actually exists.

## Product learning sets the next scope

The [milestone](MILESTONE.md) sets the next deliverables and evaluation rules. The working effort split is 60% survey and trials, 30% checker demonstration, and 10% document repair. These are planning choices; review them after the first trials.

Advanced history, rename handling, indexes, and review acknowledgments wait for an observed need. Hashing remains an explicit blocker before trustworthy product evidence.

## Earlier tools establish the value we must demonstrate

The [prior-art review](PRIOR_ART.md) covers Doorstop, Boundver, ComplianceAsCode, shared control models, and assurance-case upkeep. Fingerprinted links, tests of checks, and structured evidence have precedents. The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) makes the resulting product split explicit. Upheld combines these ideas around the reasons to rely on a software defense.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) exercises one existing checker and a simulated choice to rely on its evidence. Product commands and pilot results remain open. New features must improve useful findings or review work against a stated baseline, including a simpler fingerprinted-trace baseline where relevant.
