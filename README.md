# Upheld maps software promises to the defenses that should and do uphold them

Upheld records what software must keep true, the defense plan it should have, the defenses it has now, and the gaps that need work.

**Schema 0.2 now represents that product model. The full Upheld CLI remains unbuilt.** The survey prototype still writes 0.1 proposals. Version 0.2 adds defense plans, current-defense mappings, accepted gaps, and a derived gap report. The first report tool and repository checks run here.

An obligation is a falsifiable rule that software must preserve. The rest of this README calls it a promise. A defense plan says which mechanism or set of mechanisms should hold that promise under stated project limits. A current defense is a mechanism that really exists. Evidence records what a fault challenge observed. A binding records a person's choice to trust supporting evidence.

Teams can start before or after implementation. They can write promises and defense plans while designing an app, or discover promises and current defenses from an existing codebase. Both routes lead to the same machine-readable view.

| Question | Upheld answer |
|---|---|
| What must stay true? | Promise |
| How should we hold it? | Defense plan, with reasons and limits |
| What holds it now? | Current defenses |
| Why trust those defenses? | Fault challenges, evidence, and bindings |
| What is missing or weak? | Gaps and accepted exceptions |
| What needs another look after change? | Affected promises, plans, defenses, or evidence grounds |

Advice and code stay separate. A plan may call for a type guard plus an integration check while the code has only a unit test. Upheld should show that difference and whether the test has faced the fault it claims to catch.

Read [the positioning](docs/POSITIONING.md) for the short product story and [the product model](docs/PRODUCT_MODEL.md) for the full lifecycle.

## Trace freshness supports the map

Doorstop can mark requirement links suspect after upstream changes. Boundver can report consumers of changed contracts. Upheld can reuse those signals instead of building another general dependency engine.

A changed fingerprint means earlier grounds need review. It does not mean the promise is false or the defense failed. [The trace-freshness boundary](docs/TRACE_FRESHNESS_BOUNDARY.md) records that split.

## Schema 0.2 exposes the plan-versus-current gap

The [schema guide](docs/SCHEMA.md) defines four 0.2 shapes: a register for promises, plans, current defenses, and accepted gaps; evidence records; human bindings; and a derived gap report.

`tools/assurance_report.py` currently derives only gaps justified by recorded mappings, evidence, and bindings. It does not yet choose plans, inspect the live tree for stale evidence, or discover omitted promises.

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

Fresh evidence never proves a promise true. It can justify trusting one defense within a recorded scope. Upheld must still compare that current defense with the plan and keep any gap visible.

## The next milestone tests the whole flow

The [milestone](docs/MILESTONE.md) tests promise discovery or authorship, defense-plan quality, discovery of current defenses, gap finding, evidence quality, and upkeep cost.

| Piece | Current state | Read next |
|---|---|---|
| Product model | Schema 0.2 and design docs | [Product model](docs/PRODUCT_MODEL.md) |
| Survey | Source packets, external judgments, 0.1 proposals, and an experimental Codex adapter | [Run the prototype](docs/SURVEY_PROTOTYPE.md) |
| Defense planner | Record shape and trial plan; agent-guidance route unproven | [Design choices](docs/DECISIONS.md) |
| Gap report | Small 0.2 structural reporter | [Schema guide](docs/SCHEMA.md) |
| Evidence producer and checker | Specified; product commands unbuilt | [Checker design](docs/CHECKER.md) |
| Agent guide | Packaged 0.2 workflow around method 1.4 | [Use the skill](docs/UPHELD_SKILL.md) |

## Start here

- [Positioning](docs/POSITIONING.md): the problem Upheld solves.
- [Product model](docs/PRODUCT_MODEL.md): promise, plan, current defenses, evidence, and gaps.
- [Schema](docs/SCHEMA.md): 0.2 shapes and 0.1 compatibility.
- [Self-application](examples/upheld-self-assurance/README.md): what 0.2 says about Upheld itself.
- [Milestone](docs/MILESTONE.md): how the product claims will be tested.
- [Current method](docs/METHOD.md): how a current defense earns evidence.
- [Prior art](docs/PRIOR_ART.md): what Doorstop, Boundver, and adjacent systems already establish.
- [Todo list](TODO.md): remaining work.

Apache-2.0 covers code and documents. See [license terms](LICENSE) and [attribution notice](NOTICE).
