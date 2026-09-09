# Version 0.2 separates the defense plan from current defenses

Readers are engineers producing or consuming Upheld JSON. **Schema 0.2 stores the full promise-to-defense map: what must stay true, what should hold it, what holds it now, what the checks showed, and which gaps need work.**

The files under [schemas/0.2](../schemas/0.2/) define the register, evidence, bindings, and gap report. Version 0.1 remains readable. The repository still lacks the full product commands, so only 0.1 publishes command output shapes for `validate`, `basis`, and `verify`.

A breaking wire change gets a new version. An upgrade never invents a defense plan, current defense, evidence record, or human choice.

## The register stores the plan and current state

Version 0.2 renames the top-level `promises` array to `obligations`. Product prose can still say promise. Each record carries source, scope, project limits, defense plans, current defenses, and accepted gaps.

| Record | Question it answers |
|---|---|
| obligation | What must remain true? |
| `recommended_assurance` | Which plan fits the stated goals and limits? |
| plan member | Which mechanism should cover which part, and how should we challenge it? |
| `actual_defenses` | Which mechanisms exist now? |
| evidence | What did a real challenge observe? |
| binding | Which supporting record did a person choose to trust? |
| accepted gap | Which known shortfall did a person choose to leave open? |
| gap report | What does the plan-versus-current comparison expose now? |

Advice and current code use different fields. A suggested type guard does not become a current defense until the project builds it. Finding a unit test does not make it part of the preferred plan.

## A plan can use several mechanisms

`recommended_assurance.plans` can hold one preferred plan and alternatives. Each plan names its goal, project limits, tradeoffs, and remaining unknowns.

Each member names its defense kind, target scope, reason, known bypass paths, fault challenge, needed tools or target, optional cost notes, and remaining unknowns.

`portfolio_logic` says whether all members are required, any member can suffice, members form layers, or a custom rule applies. One promise can therefore call for a type guard plus an integration check without claiming either covers the other's scope.

The built-in kinds remain `test`, `property`, `checker`, `ratchet`, `type`, and `runtime_invariant`. An extension kind begins with `x-` and supplies a plain mechanism name.

## Current defenses map back to plan members

Each current defense names the real artifact, scope, kind, needed tools, and state. `recommendation_member_ids` links it to the plan members it claims to implement.

The schema allows an empty mapping. That means nobody has reviewed where the defense fits in the selected plan. The gap report can flag it as `divergence_unreviewed`.

`implementation_state` is `present`, `partial`, `disabled`, or `unknown`. Partial or disabled code stays visible and can leave a plan gap.

## The report derives open gaps

The register stores deliberate accepted gaps under `accepted_gaps`. The reporter derives open gaps from the selected plan, current-defense mappings, bindings, and evidence.

[The report schema](../schemas/0.2/assurance-report.schema.json) names `no_plan`, `no_defense`, `weaker_than_recommended`, `unproven_defense`, `stale_evidence`, `coverage_gap`, `unsupported_environment`, `divergence_unreviewed`, `conflicting_defenses`, `accepted_gap`, and `unknown`.

The first reporter emits only the classes its inputs justify. It must not guess semantic coverage. Accepted gaps remain visible; acceptance changes their status, not their meaning.

## Evidence belongs to a current defense

Version 0.2 keeps observation separate from human choice. Its main wire change is `basis.obligation`, replacing `basis.promise`.

The basis records the hash profile, promise fingerprint, defense-assertion fingerprint, artifact fingerprints, checked subject scope, and declared setup files. Run context records either an explicit unknown state or the producer's account of command, time, duration, toolchain, target, config, dirty-tree state, and omissions.

A supporting record must match the current defense and oracle. A binding maps one defense ID to one evidence ID. Producers never write bindings.

## The schema does not give defense kinds a global rank

The plan stores goals and project limits because “best” depends on the case. Cost, delay, likely harm, available tools, bypass paths, and the need for independent checks can change the preferred plan.

The wire format stores those facts and alternatives instead of a score such as `type > property > test`.

## Version 0.1 upgrades without inventing a plan

Version 0.1 remains under [schemas/0.1](../schemas/0.1/). A future 0.1-to-0.2 tool must preserve IDs, claim text, current defenses, accepted gaps, dates, and evidence fingerprints.

It must set the new plan state to `unknown` unless a separate review supplies a plan. It must leave plan-member mappings empty unless someone reviewed them. It must never create evidence from `last_actually_ran` or create a binding.

The current review-copy and survey-register tools still write 0.1. Existing 0.1 fixtures and checks remain part of CI until the upgrade path exists.

## The first gap reporter stays narrow

`tools/assurance_report.py` compares a selected plan with current-defense mappings. If bindings and evidence are present, it can tell a mapped defense with supporting evidence from one that merely exists.

Today it derives `no_plan`, `no_defense`, `weaker_than_recommended`, `unproven_defense`, and `divergence_unreviewed`, while keeping accepted gaps visible. It does not yet check the live tree for stale evidence, prove that several members cover a whole promise, rank plans, or find omitted promises.
