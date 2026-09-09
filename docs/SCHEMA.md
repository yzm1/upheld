# Version 0.2 separates the defense plan from the defenses that exist

Readers are engineers producing or consuming Upheld JSON. **Schema 0.2 represents the whole promise-to-defense map: what must stay true, what should hold it, what holds it now, what evidence supports those defenses, and which gaps need attention.**

The schemas under [schemas/0.2](../schemas/0.2/) define the new register, evidence, bindings, and derived assurance report. Version 0.1 remains supported as the first published wire format. Product commands are still unbuilt, so 0.1 command-output schemas remain the only published `validate`, `basis`, and `verify` shapes for now.

A breaking record change uses a new schema version. Upgrading a file never creates a defense, recommendation, evidence record, or human choice that was not present in the source.

## The register holds intent and current implementation

Version 0.2 renames the top-level `promises` array to `obligations`. Each obligation carries its source, scope, constraints, recommended defense plans, actual defenses, and accepted exceptions.

| Record | Question it answers |
|---|---|
| obligation | What must remain true? |
| `recommended_assurance` | Which defense plan or plans fit the stated objective and limits? |
| plan member | Which mechanism should cover which part of the obligation, and how should it be challenged? |
| `actual_defenses` | Which mechanisms really exist in the project now? |
| evidence | What did a real challenge of an actual defense observe? |
| binding | Which supporting evidence did a person choose to rely on? |
| accepted gap | Which known shortfall did a person deliberately leave open? |
| assurance report | What does the recorded plan-versus-current comparison expose now? |

Advice and implementation are different record types. A recommended type check does not become an actual defense until the project implements it. A discovered unit test does not become recommended merely because it exists.

## A defense plan is conditional and may contain several mechanisms

`recommended_assurance.plans` can hold a preferred plan and alternatives. A plan records its objective, the project limits considered, its tradeoffs, and remaining unknowns.

Each plan member records:

- a defense kind;
- intended scope;
- why that mechanism fits;
- known bypass paths;
- the fault challenge that should test it;
- required environment;
- optional cost notes;
- residual uncertainty.

`portfolio_logic` says whether all members are required, any member is sufficient, the members are layered, or a custom rule applies. This lets one obligation call for a type restriction plus an integration check without pretending either mechanism covers the other one's scope.

The built-in defense kinds remain `test`, `property`, `checker`, `ratchet`, `type`, and `runtime_invariant`. An extension kind still begins with `x-` and supplies a mechanism description.

## Actual defenses map back to the plan without being forced to match it

Each actual defense records the real artifact, scope, kind, environment, and implementation state. `recommendation_member_ids` links the current mechanism to the plan members it is meant to implement.

An empty mapping is allowed. It means the project has a defense whose place in the chosen plan has not been reviewed. A generated report can surface that as `divergence_unreviewed` rather than silently deleting or promoting the defense.

`implementation_state` is `present`, `partial`, `disabled`, or `unknown`. A partial or disabled implementation remains visible and can create a plan-coverage gap.

## Derived gaps belong in a report; accepted gaps belong in the register

The register stores only deliberate accepted exceptions under `accepted_gaps`. Open gaps are derived from the current plan, actual defense mappings, bindings, and evidence.

[The assurance report schema](../schemas/0.2/assurance-report.schema.json) currently names these derived gap kinds:

- `no_plan`;
- `no_defense`;
- `weaker_than_recommended`;
- `unproven_defense`;
- `stale_evidence`;
- `coverage_gap`;
- `unsupported_environment`;
- `divergence_unreviewed`;
- `conflicting_defenses`;
- `accepted_gap`;
- `unknown`.

The first reporter implements only the gap classes it can justify from recorded structure, mappings, bindings, and evidence. It must not infer semantic coverage that the records do not establish.

An accepted gap stays visible in the report. Acceptance changes the gap's status and review instruction; it does not convert the gap into a defense or evidence.

## Evidence still belongs only to an actual defense

Version 0.2 evidence keeps the 0.1 separation between observation and human acceptance. The main wire change is that the basis hashes the `obligation` rather than the older `promise` field.

The basis still records:

- the hashing profile;
- obligation fingerprint;
- defense assertion fingerprint;
- artifact fingerprints;
- validated subject scope;
- declared environment files.

Execution context still records either an explicit unknown state or the producer's account of command, time, duration, toolchain, target, configuration, dirty-tree state, and omissions.

A supporting record must match the actual defense and its oracle. A binding still maps one defense ID to one evidence ID. Producers never write bindings.

## Version 0.2 does not rank defense kinds globally

The schema records the objective and constraints behind a recommendation because “best” depends on the project. Cost, latency, failure consequence, infrastructure, bypass paths, and the need for independent defenses can change the preferred plan.

The wire format therefore stores the reasoning inputs and alternatives rather than a universal score such as `type > property > test`.

## Version 0.1 remains readable and migrates without inventing intent

Version 0.1 remains under [schemas/0.1](../schemas/0.1/). It separates claims, candidate defenses, evidence, and bindings, but has no first-class defense-plan model.

A future 0.1-to-0.2 migration must preserve these rules:

| Version 0.1 | Version 0.2 | Migration rule |
|---|---|---|
| `promises` | `obligations` | Preserve IDs and claim text. |
| `the_test_that_would_catch_it` | `falsifier` | Preserve the prose. |
| `defenses` | `actual_defenses` | Preserve real mechanisms; initialize recommendation mappings empty unless separately reviewed. |
| `gap` | `accepted_gaps` | Preserve the recorded choice and unknown actor/time honestly. |
| no defense-plan field | `recommended_assurance` | Set status to `unknown`; never infer a preferred plan from existing tests. |
| evidence `basis.promise` | evidence `basis.obligation` | Preserve the fingerprint value when the obligation text and hash profile are unchanged. |
| `surveyed_on` | `recorded_on` | Preserve the date and name the producer mode. |

Migration does not turn an existing defense into a recommendation. It does not create evidence from `last_actually_ran`, and it does not bind any evidence.

## Version 0.1 compatibility rules still apply to old records

The heldtospec probe remains `0.1-probe`. The review-copy and survey-register tools still emit 0.1 until their 0.2 migration work is implemented. Existing 0.1 fixtures, diagnostics, and command-output schemas remain checked by the repository.

The historical 0.1 rules remain important:

- every actual defense has an explicit mechanism kind;
- a compiler's acceptance cannot establish its own soundness;
- a test or property needs a justified fault challenge before binding;
- a checker must distinguish clean, violated, and unable-to-inspect states;
- execution context and evidence basis answer different questions;
- unchanged hashes do not establish that the original defense judgment was sound.

## The first 0.2 reporter is deliberately narrow

`tools/assurance_report.py` compares a selected plan with actual defense mappings. With bindings and evidence supplied, it can distinguish a mapped present defense with supporting evidence from one that is merely present.

It currently derives `no_plan`, `no_defense`, `weaker_than_recommended`, `unproven_defense`, and `divergence_unreviewed`, while keeping accepted exceptions visible. It does not yet calculate stale evidence from the live tree, prove scope composition, rank recommendations, or discover omitted obligations.

Those limits are product work, not reasons to blur the record types.
