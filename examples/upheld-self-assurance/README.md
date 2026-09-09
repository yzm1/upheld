# Upheld 0.2 shows its own plan-versus-current gaps

This bounded self-review uses schema 0.2 against Upheld commit `01bdaf0a0ef9bb880c3c42e3156c50800873431b`, dated 9 September 2026. It covers the product model, schema, trace boundary, agent guide, gap reporter, repository gate, and focused tests named in the register.

**The result is five product promises and twelve open gaps.** None is accepted. The evidence log and binding map are empty by design. The author proposed the defense plans; independent reviewers have not graded them.

Read [the register](obligations.register.json) for the plans and current-defense inventory. `tools/assurance_report.py` builds [the gap report](assurance.report.json) from that register plus the empty evidence and binding files.

## The new model asks a larger question

The earlier self-audit found package-checker defects. This pass asks whether Upheld has the defenses its current product design calls for.

| Promise | Current state | Main gaps |
|---|---|---|
| UPH-02-01: plan and current defense stay distinct | Schema 0.2 and focused report tests exist | Both current defenses lack bound supporting evidence |
| UPH-02-02: choose a good defense plan under project limits | The 0.2 skill contains a constraint-aware planner route | Live-client evidence and independent planner trials are missing |
| UPH-02-03: find real defenses and compare them with the plan | The skill contains an inventory route and the gap reporter exists | Both are present but still unproven |
| UPH-02-04: keep prior trust current without manufacturing acceptance | Design rules exist | Product `basis`/`verify` behavior and producer-versus-binding checks are unbuilt |
| UPH-02-05: upgrade/import safely and expose the full workflow through the skill | 0.2 guide and package tests exist | 0.1 upgrade, external trace import, and live client trials are missing; package tests remain unbound |

The report contains six `no_defense` gaps and six `unproven_defense` gaps. The planner and inventory routes already exist in the skill. The open question is whether configured agents carry them out correctly and whether their judgments are good.

A schema, script, skill, or test does not close a plan member merely because the file exists. The reporter requires bound supporting evidence before it marks a mapped member covered.

## The self-review corrected its own register

The first draft briefly listed `skills/upheld/SKILL.md` as a defense of package behavior. That repeated the old delivery-versus-defense mistake. The skill file is package content. It does not check the package promise.

The corrected record maps that plan member to `tests/test_skill_package.py`. The schema defense likewise names the schema together with the repository checker that compiles it.

This matters beyond bookkeeping. Finding “what exists” still requires a judgment about each artifact's role. Names and nearby files do not settle that question.

## The planner needs proof next

Upheld says it should help answer “how should this promise be held?” The repository can represent that answer, and the 0.2 skill gives an agent a procedure for producing it. **The project still lacks demonstrated planner quality.**

The plan therefore calls for both the planner route and independently reviewed trials. The route exists. The trials do not. No bound evidence yet shows that a live client changes its plan when a decisive project limit changes.

Defense inventory has the same shape. The skill tells an agent to read mechanisms and scope instead of trusting names. The gap reporter can compare those mappings. Held-out live-client evidence still needs to show that the inventory is accurate enough to trust.

## Six plan members have no mapped defense

The main missing pieces are:

- independently reviewed planner trials;
- product `basis` and `verify` behavior for changed evidence grounds;
- checks that producers and refresh operations never create bindings;
- a 0.1-to-0.2 upgrade that preserves old records without inventing a plan;
- importers for external requirement and change tools that leave source-tool trust state behind;
- live held-out trials of the packaged skill.

## The report stays derived

The repository gate regenerates `assurance.report.json` from the register, bindings, and evidence. A hand edit to the gap list fails unless the source records justify it.

The same gate also keeps the evidence and binding files empty for this example. Passing CI counts as a development observation; this self-review does not turn it into accepted product evidence.

## Limits

This is an author self-review. It does not show that the five chosen promises are complete, that the plans are best, or that Upheld improves engineering outcomes. The [milestone](../../docs/MILESTONE.md) still owns independent planner, discovery, upkeep, and human-work trials.
