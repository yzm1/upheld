# Upheld maps software obligations to the defenses that should and do uphold them

Upheld is a software assurance tool in development. It records what software must keep true, how best to enforce each obligation under declared project constraints, what actually enforces it now, what evidence supports those defenses, and where the gaps are.

**The survey has a runnable repository prototype. The Upheld CLI remains unbuilt.** The prototype prepares sources, imports candidate judgments, and writes schema 0.1 register proposals. Documentation checks run separately from the planned product commands.

An obligation is a falsifiable condition the software is expected to preserve. Schema 0.1 currently calls this record a `promise`. A defense is a test, rule, type guarantee, runtime check, or other mechanism intended to uphold it. An evidence record describes a run that assessed a defense. A binding records a person's choice to rely on that evidence.

Upheld supports two ways into the same model. A team can **author obligations while specifying or designing an application**, including the intended assurance plan before code exists. It can also **discover obligations and defenses from an existing codebase**. Both paths should converge on the same machine-readable view.

For each obligation, the useful view is:

| Question | Upheld record or result |
|---|---|
| What must stay true? | Obligation / current `promise` record |
| How should we hold it? | Recommended defense pattern or portfolio, with rationale and constraints |
| What holds it now? | Implemented candidate defenses actually present in the system |
| Why should we trust those defenses? | Fault challenges, scoped evidence, and explicit bindings |
| What is missing or weaker than intended? | Assurance gap, uncertainty, stale grounds, or accepted gap |
| What needs attention after change? | Affected obligations and defenses whose grounds need reassessment |

The recommendation is not automatically the implementation, and an implementation is not automatically adequate. Upheld should make the difference visible. A strong result may be “the obligation is best enforced by a type restriction plus an integration check; today it has only a unit test whose fault challenge is unproven.”

Doorstop and Boundver already fingerprint requirement or dependency links and flag them after changes. Upheld does not treat that behavior as its differentiator. Those tools can provide identity, trace, and change context. Upheld uses that context to maintain the obligation-to-assurance view rather than replacing it. [The boundary and adoption bypass](docs/TRACE_FRESHNESS_BOUNDARY.md) explain that split.

The [development lifecycle](docs/EVIDENCE_LIFECYCLE.md) runs an existing checker through a fault challenge and changed-ground review. Acceptance in that case is simulated. [Earlier tools](docs/PRIOR_ART.md) supply precedents; useful findings, recommendation quality, gap detection, and review cost remain product tests.

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

**Fresh evidence does not prove that a software obligation is true.** The checker will compare current files with the grounds recorded by an evidence producer. It will report when those grounds change. The larger product also needs to compare the actual defenses with the recommended assurance plan and keep resulting gaps visible.

## The next milestone tests discovery, defense choice, gaps, and upkeep

The [milestone](docs/MILESTONE.md) pairs a survey and cheap-probe workflow with a small checker run. It measures useful findings and human review work. The next design work also has to test whether Upheld can recommend appropriate defenses, inventory what exists, and surface consequential gaps without pretending there is one universal ranking of defense kinds.

| Piece | Current state | Read next |
|---|---|---|
| Survey | Source packets, external judgments, register proposals, and an experimental Codex adapter | [Run the prototype](docs/SURVEY_PROTOTYPE.md) |
| Defense recommendation | Designed as separate advice; no product recommender | [Design choices](docs/DECISIONS.md) |
| Evidence producers | Specified; no product producer | [Checker and producer rules](docs/CHECKER.md) |
| Checker CLI | Specified; no product commands | [Schemas and compatibility](docs/SCHEMA.md) |
| Documentation checks | Executable repository tools | [Contribution checks](CONTRIBUTING.md) |

## Start with the product model or the next task

- [Design choices](docs/DECISIONS.md) state the obligation-to-assurance product spine.
- [Survey register](docs/SURVEY_REGISTER.md) explains the current machine-readable output and its limits.
- [Trace-freshness boundary](docs/TRACE_FRESHNESS_BOUNDARY.md) keeps established fingerprint/impact behavior in its supporting role.
- [Component design](docs/COMPONENT_REGISTER_DESIGN.md) records the next schema work.
- [Current method](docs/METHOD.md) explains how to assess a defense.
- [Self-audit](docs/SELF_AUDIT.md) applies the method to Upheld and records observed faults and remaining gaps.
- [Agent guide](docs/UPHELD_SKILL.md) explains the opt-in skill prototype and its untested live-client behavior.
- [Todo list](TODO.md) records remaining work and completed decisions.
- [Measured results](measurements/RESULTS.md) separate observed results from pending trials.
- [Earlier drafts](docs/history/README.md) preserve the original arguments and reviews.

Apache-2.0 covers code and documents. See [license terms](LICENSE) and [attribution notice](NOTICE).
