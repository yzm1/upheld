# Upheld 0.2 exposes its own plan-versus-current gaps

This bounded self-application uses schema 0.2 against Upheld commit `01bdaf0a0ef9bb880c3c42e3156c50800873431b`, dated 9 September 2026. It covers the product model, positioning, schema, trace boundary, agent guide, gap reporter, repository gate, and focused tests named in the register.

**The result is five product obligations and twelve open assurance gaps.** None is accepted. The evidence log and binding map are intentionally empty. The proposed defense plans are author-generated and have not been independently reviewed.

Read [the register](obligations.register.json) for the intended plans and current-defense inventory. [The derived report](assurance.report.json) is generated from that register plus the empty evidence and binding files.

## The new model changes what the self-review says

The earlier self-audit found concrete package-checker defects. This pass asks a larger question: does Upheld itself have the defenses that its current product design says should exist?

| Obligation | Current state | Main gaps |
|---|---|---|
| UPH-02-01: plan and implementation stay distinct | Schema 0.2 and focused report tests exist | Both current defenses remain unbound and therefore unproven under Upheld's own evidence rules |
| UPH-02-02: recommend a good defense plan under constraints | The 0.2 skill contains a constraint-aware recommendation route | The agent-guidance implementation is unproven in a live client, and independent recommendation-quality trials are missing |
| UPH-02-03: inventory real defenses and compare them with the plan | The skill contains an inventory route and the structural gap reporter exists | Both are present but unproven under the recorded evidence model |
| UPH-02-04: keep assurance current without manufacturing trust | Design rules exist | Product `basis`/`verify` behavior and producer-versus-binding integration are still unbuilt |
| UPH-02-05: migrate/import safely and expose the full workflow through the skill | 0.2 guide and package tests exist | 0.1 migration, external trace import, and live client trials are missing; package behavior remains unbound |

The derived report contains twelve open gaps: six `no_defense` gaps and six `unproven_defense` gaps. This distinction matters. The recommendation and inventory workflows are not absent; the skill already describes them. What is missing is evidence that configured agents carry out those workflows correctly and that the resulting judgments are good.

A present schema, script, skill, or test does not close a plan member merely because it exists. The reporter requires bound supporting evidence before treating a mapped implementation as covered.

## The most important product gap is validation of the planner

Upheld's positioning says it should help answer “how should this obligation be held?” The repository can now represent that answer, and the 0.2 skill gives an agent a procedure for producing it. **What the project does not yet have is demonstrated recommendation quality.**

The defense plan therefore calls for both the agent-guidance implementation and independently reviewed recommendation trials. The first exists; the second does not. The present route also has no bound evidence showing that a live client changes its recommendation appropriately when a decisive project constraint changes.

Actual-defense discovery has the same shape. The 0.2 skill tells an agent to read mechanisms and scope rather than trust names, and the gap reporter can compare those mappings once supplied. That is an implementation, but no held-out live-client evidence yet shows that the inventory is accurate enough to rely on.

## The largest literal implementation gaps sit lower in the lifecycle

Six plan members have no mapped implementation in this bounded review. The consequential ones are:

- independently reviewed recommendation-quality trials;
- product `basis` and `verify` behavior for changed evidence grounds;
- integration tests proving producers and refresh operations never manufacture bindings;
- a 0.1-to-0.2 migration that preserves existing records without inventing a defense plan;
- importers for external requirement and change tools that do not import their trust state;
- live held-out trials of the packaged skill.

These are better descriptions of the current implementation gap than “the recommender does not exist.”

## Evidence remains deliberately strict

The schema, reporter, package tests, and agent guidance are real implementation, but this example does not create product evidence from those facts. Tests running in CI are development observations. Upheld 0.2 still requires a compatible evidence record and explicit binding before a current defense closes a plan member.

That strict result is useful here: it prevents the project from calling its own new model “assured” simply because the model's tests pass.

## The report is derived, not curated

`tools/assurance_report.py` produces the committed report from the register, bindings, and evidence. Repository checks compare the generated result with `assurance.report.json` using the recorded generation time.

Changing a plan member, actual-defense mapping, binding, or supporting evidence must therefore change the report or fail the repository gate. Open gaps are not a second hand-maintained source of truth.

## Limits

This is an author self-application, not an independent evaluation. It does not establish that the five selected obligations are complete, that the proposed plans are optimal, or that Upheld improves engineering outcomes. It deliberately excludes broad heldtospec re-survey, research reproduction, and live agent trials.

The [milestone](../../docs/MILESTONE.md) still owns independent recommendation-quality, discovery, maintenance, and human-work measurements.
