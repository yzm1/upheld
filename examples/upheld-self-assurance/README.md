# Upheld 0.2 exposes its own plan-versus-current gaps

This bounded self-application uses schema 0.2 against Upheld commit `01bdaf0a0ef9bb880c3c42e3156c50800873431b`, dated 9 September 2026. It covers the product model, positioning, schema, trace boundary, agent guide, gap reporter, repository gate, and focused tests named in the register.

**The result is five reviewed product obligations and twelve open assurance gaps.** None is accepted. The evidence log and binding map are intentionally empty. The proposed defense plans are author-generated and have not been independently reviewed.

Read [the register](obligations.register.json) for the intended plans and current-defense inventory. [The derived report](assurance.report.json) is generated from that register plus the empty evidence and binding files.

## The new model changes what the self-review says

The earlier self-audit found concrete package-checker defects. This pass asks a larger question: does Upheld itself have the defenses that its current product design says should exist?

| Obligation | Current state | Main gaps |
|---|---|---|
| UPH-02-01: plan and implementation stay distinct | Schema 0.2 and focused report tests exist | Both current defenses remain unbound and therefore unproven under Upheld's own evidence rules |
| UPH-02-02: recommend a good defense plan under constraints | No recommender or independent recommendation trial exists | Two `no_defense` gaps |
| UPH-02-03: inventory real defenses and compare them with the plan | Structural gap reporter exists | Code-aware defense inventory is missing; the reporter itself has no bound evidence |
| UPH-02-04: keep assurance current without manufacturing trust | Design rules exist | Product `basis`/`verify` behavior and producer-versus-binding integration are still unbuilt |
| UPH-02-05: migrate/import safely and expose the full workflow through the skill | 0.2 guide and package tests exist | 0.1 migration, external trace import, and live client trials are missing; package behavior remains unbound |

The derived report contains twelve open gaps: seven `no_defense` gaps and five `unproven_defense` gaps. A present schema, script, skill, or test does not close a gap merely because it exists. The reporter requires bound supporting evidence before treating a mapped plan member as covered.

## The most important product gap is now obvious

Upheld's positioning says it should help answer “how should this obligation be held?” The repository can now represent that answer, but **it cannot yet produce it as a product capability**.

The missing recommender is therefore not an optional convenience. It is one of the largest gaps between the new positioning and the implementation. Its defense plan calls for both a constraint-aware planner and independently reviewed recommendation trials. Neither exists in the audited snapshot.

The next missing layer is actual-defense discovery. The 0.2 skill tells an agent not to trust names alone, and the gap reporter can compare mappings once supplied, but no 0.2 code-aware inventory path yet earns that mapping.

## Evidence remains deliberately strict

The schema, reporter, and package tests have real implementation, but this example does not create product evidence from those facts. Tests running in CI are observations about development work. Upheld 0.2 still requires a compatible evidence record and explicit binding before a current defense closes a plan member.

That strict result is useful here: it prevents the project from calling its own new model “assured” simply because the model's tests pass.

## The report is derived, not curated

`tools/assurance_report.py` produces the committed report from the register, bindings, and evidence. Repository checks compare the generated result with `assurance.report.json` using the recorded generation time.

Changing a plan member, actual-defense mapping, binding, or supporting evidence must therefore change the report or fail the repository gate. Open gaps are not a second hand-maintained source of truth.

## Limits

This is an author self-application, not an independent evaluation. It does not establish that the five selected obligations are complete, that the proposed plans are optimal, or that Upheld improves engineering outcomes. It deliberately excludes broad heldtospec re-survey, research reproduction, and live agent trials.

The [milestone](../../docs/MILESTONE.md) still owns independent recommendation-quality, discovery, maintenance, and human-work measurements.
