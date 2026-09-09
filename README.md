# Upheld maps software obligations to the defenses that should and do uphold them

Upheld is a software tool for keeping important software claims covered. It records what must stay true, the best defense plan under the project's limits, what defenses exist now, what the checks showed, and what gaps remain.

**The survey has a runnable repository prototype. The Upheld CLI remains unbuilt.** The prototype prepares sources, imports candidate judgments, and writes schema 0.1 register proposals. Documentation checks run separately from the planned product commands.

An obligation is a falsifiable rule the software is expected to keep. Schema 0.1 calls this record a `promise`. A defense is a test, rule, type guarantee, runtime check, or other mechanism meant to uphold it. An evidence record describes a run that assessed a defense. A binding records a person's choice to rely on that evidence.

Teams can enter the model in two ways. They can write promises while designing a new app and record the desired defense plan before code exists. They can also discover promises and defenses from an existing codebase. Both paths should reach the same machine-readable view.

For each promise, the useful view is:

| Question | Upheld record or result |
|---|---|
| What must stay true? | Obligation / current `promise` record |
| How should we hold it? | Recommended defense pattern or portfolio, with rationale and constraints |
| What holds it now? | Implemented candidate defenses actually present in the system |
| Why should we trust those defenses? | Fault challenges, scoped evidence, and explicit bindings |
| What is missing or weaker than intended? | Assurance gap, uncertainty, stale grounds, or accepted gap |
| What needs attention after change? | Affected obligations and defenses whose grounds need reassessment |

Advice and reality stay separate. A plan may call for a type restriction plus an integration check while the code has only a unit test. Upheld should show that difference and whether the existing test has ever faced the fault it claims to catch.

Doorstop and Boundver already fingerprint requirement or dependency links and flag them after changes. Upheld can use those signals for identity, trace, and change context. [The boundary and adoption bypass](docs/TRACE_FRESHNESS_BOUNDARY.md) explain the split.

The [development lifecycle](docs/EVIDENCE_LIFECYCLE.md) runs an existing checker through a fault challenge and changed-ground review. Acceptance in that case is simulated. [Earlier tools](docs/PRIOR_ART.md) supply precedents; useful findings, defense-plan quality, gap finding, and review cost remain product tests.

## The committed example has no graded defenses

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

**Fresh evidence does not prove that a promise is true.** The checker will compare current files with the grounds recorded by an evidence producer. It will report when those grounds change. The larger product must also compare the defense plan with the defenses that exist and keep the gaps visible.

## The next milestone tests promises, defense choice, gaps, and upkeep

The [milestone](docs/MILESTONE.md) pairs source review and cheap probes with a small checker run. It also tests whether Upheld can propose useful defense plans, find what the project has now, and expose important gaps without assuming one universal rank for defense kinds.

| Piece | Current state | Read next |
|---|---|---|
| Survey | Source packets, external judgments, register proposals, and an experimental Codex adapter | [Run the prototype](docs/SURVEY_PROTOTYPE.md) |
| Defense recommendation | Designed as separate advice; no product recommender | [Design choices](docs/DECISIONS.md) |
| Evidence producers | Specified; no product producer | [Checker and producer rules](docs/CHECKER.md) |
| Checker CLI | Specified; no product commands | [Schemas and compatibility](docs/SCHEMA.md) |
| Documentation checks | Executable repository tools | [Contribution checks](CONTRIBUTING.md) |

## Start with the product model or the next task

- [Product model](docs/PRODUCT_MODEL.md) gives the whole promise-to-defense-to-gap workflow.
- [Design choices](docs/DECISIONS.md) records the rules that follow from that model.
- [Survey register](docs/SURVEY_REGISTER.md) explains the current machine-readable output and its limits.
- [Trace-freshness boundary](docs/TRACE_FRESHNESS_BOUNDARY.md) keeps fingerprint and impact work in its supporting role.
- [Component design](docs/COMPONENT_REGISTER_DESIGN.md) records the next schema work.
- [Current method](docs/METHOD.md) explains how to assess a defense.
- [Self-audit](docs/SELF_AUDIT.md) applies the method to Upheld and records observed faults and remaining gaps.
- [Agent guide](docs/UPHELD_SKILL.md) explains the opt-in skill prototype and its untested live-client behavior.
- [Todo list](TODO.md) records remaining work and completed decisions.
- [Measured results](measurements/RESULTS.md) separate observed results from pending trials.
- [Earlier drafts](docs/history/README.md) preserve the original arguments and reviews.

Apache-2.0 covers code and documents. See [license terms](LICENSE) and [attribution notice](NOTICE).
