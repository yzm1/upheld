# Upheld maps software obligations to the defenses that should and do uphold them

Upheld keeps a machine-readable map of what software must keep true, how it should be defended, how it is actually defended, and where the gaps need attention.

**Schema 0.2 now represents that product model. The full Upheld CLI remains unbuilt.** The existing survey prototype still emits 0.1 proposals; 0.2 adds defense plans, actual-defense mappings, accepted exceptions, and a derived assurance report. Documentation checks and the first report generator run in this repository.

An obligation is a falsifiable rule the software is expected to preserve. A defense plan says which mechanism or portfolio should uphold it under stated project limits. An actual defense is a mechanism that really exists. Evidence records what a challenge of an actual defense observed. A binding records a person's choice to rely on supporting evidence.

Teams can enter the model in two ways. They can author obligations and defense plans while designing a new app, before code exists. They can also discover obligations and current defenses from an existing codebase. Both paths should reach the same machine-readable view.

| Question | Upheld record or result |
|---|---|
| What must stay true? | Obligation |
| How should we hold it? | Recommended defense plan or portfolio, with rationale and constraints |
| What holds it now? | Actual defenses present in the system |
| Why should we trust those defenses? | Fault challenges, scoped evidence, and explicit bindings |
| What is missing or weaker than intended? | Derived assurance gaps plus deliberate accepted exceptions |
| What needs attention after change? | Affected obligations, plans, defenses, or evidence grounds |

Advice and reality stay separate. A plan may call for a type restriction plus an integration check while the code has only a unit test. Upheld should show that difference and whether the existing test has ever faced the fault it claims to catch.

[The positioning](docs/POSITIONING.md) gives the short product story. [The product model](docs/PRODUCT_MODEL.md) explains the lifecycle and record roles.

## Trace freshness is useful plumbing, not the product

Doorstop can make requirement links suspect after upstream changes. Boundver can report consumers of changed contracts. Upheld can consume those signals for identity, trace, and change context instead of rebuilding a second general dependency engine.

A changed fingerprint means that earlier grounds need another look. It does not mean the obligation is false or the defense failed. [The trace-freshness boundary](docs/TRACE_FRESHNESS_BOUNDARY.md) records that split.

## Schema 0.2 exposes the plan-versus-current gap

The [schema guide](docs/SCHEMA.md) defines four current 0.2 shapes:

- assurance register: obligations, constraints, defense plans, actual defenses, and accepted gaps;
- evidence: observations tied to actual defenses and their grounds;
- bindings: explicit human choices to rely on evidence;
- assurance report: derived open and accepted gaps.

`tools/assurance_report.py` currently derives only gaps justified by recorded structure, mappings, evidence, and bindings. It does not yet recommend plans, inspect the live tree for stale evidence, or discover omitted obligations.

## The committed 0.1 survey remains historical input

The heldtospec survey covers one contracts component. Its records date from 6 September 2026; they do not describe that project's current state.

| Committed record | Count | What it establishes |
|---|---:|---|
| Promises | 44 | Claims the survey recorded |
| Candidate defenses | 78 | Links based on reading |
| Promises awaiting a defense or gap decision | 4 | Unresolved choices |
| Accepted gaps | 4 | Recorded reasons to leave claims undefended |
| Bound evidence records | 0 | No defense has an accepted grade |
| Library tests reported passing | 149 | One historical suite run; CLI run incomplete |

Sources: [survey records](examples/heldtospec-contracts/README.md) and [reconciled counts](examples/heldtospec-contracts/reconciliation.md).

Fresh evidence never proves an obligation true. It can justify relying on a particular defense within a recorded scope. The larger product must also compare that current defense with the intended plan and keep the remaining gap visible.

## The next milestone tests the whole flow

The [milestone](docs/MILESTONE.md) now tests obligation authorship/discovery, defense-plan quality, discovery of actual defenses, gap detection, evidence quality, and upkeep cost.

| Piece | Current state | Read next |
|---|---|---|
| Product model | Schema 0.2 and design docs | [Product model](docs/PRODUCT_MODEL.md) |
| Survey | Source packets, external judgments, 0.1 proposals, and an experimental Codex adapter | [Run the prototype](docs/SURVEY_PROTOTYPE.md) |
| Defense recommendation | Record shape and evaluation plan; no product recommender | [Design choices](docs/DECISIONS.md) |
| Assurance report | Small 0.2 structural gap reporter | [Schema guide](docs/SCHEMA.md) |
| Evidence producers | Specified; no product producer | [Checker and producer rules](docs/CHECKER.md) |
| Checker CLI | Specified; no product commands | [Checker design](docs/CHECKER.md) |
| Agent guide | Packaged 0.2 workflow around method 1.4 | [Use the skill](docs/UPHELD_SKILL.md) |

## Start here

- [Positioning](docs/POSITIONING.md) — what problem Upheld solves and what it is not.
- [Product model](docs/PRODUCT_MODEL.md) — obligation, defense plan, current defenses, evidence, and gaps.
- [Schema](docs/SCHEMA.md) — 0.2 machine-readable shapes and 0.1 compatibility.
- [Milestone](docs/MILESTONE.md) — how the product claims will be tested.
- [Current method](docs/METHOD.md) — how a current defense earns evidence.
- [Prior art](docs/PRIOR_ART.md) — what Doorstop, Boundver, and adjacent systems already establish.
- [Todo list](TODO.md) — remaining implementation and evaluation work.

Apache-2.0 covers code and documents. See [license terms](LICENSE) and [attribution notice](NOTICE).
