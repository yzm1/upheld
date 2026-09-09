# Upheld tracks the evidence behind software promises

Upheld is a software assurance tool in development. It records what code promises, what evidence defends each promise, and when that evidence needs another check.

**The survey has a runnable repository prototype. The Upheld CLI remains unbuilt.** The prototype prepares sources, imports candidate judgments, and writes schema 0.1 register proposals. Documentation checks run separately from the planned product commands.

A promise is a claim that can be false. A defense is a test, rule, type guarantee, or other mechanism intended to uphold it. An evidence record describes a run that assessed a defense. A binding records a person's choice to rely on that evidence.

Fingerprinting a requirement or dependency link and flagging it after change is established prior art in tools such as Doorstop and Boundver. Upheld does not treat that trace-freshness layer as its differentiator. Its added responsibility is to record **why a defense is worth relying on, how that defense was challenged, what was actually observed, what a person accepted, and when the grounds for that acceptance change**. [The boundary and adoption bypass](docs/TRACE_FRESHNESS_BOUNDARY.md) explain how existing trace and impact systems can feed Upheld instead of being replaced.

The [development lifecycle](docs/EVIDENCE_LIFECYCLE.md) runs an existing checker through a fault challenge and changed-ground review. Acceptance in that case is simulated. [Earlier tools](docs/PRIOR_ART.md) supply precedents; useful findings and review cost remain the product tests.

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

**Fresh evidence does not prove that a software promise is true.** The checker will compare current files with the grounds recorded by an evidence producer. It will report when those grounds change.

## The next milestone tests discovery and upkeep

The [milestone](docs/MILESTONE.md) pairs a survey and cheap-probe workflow with a small checker run. It measures useful findings and human review work.

| Piece | Current state | Read next |
|---|---|---|
| Survey | Source packets, external judgments, register proposals, and an experimental Codex adapter | [Run the prototype](docs/SURVEY_PROTOTYPE.md) |
| Evidence producers | Specified; no product producer | [Checker and producer rules](docs/CHECKER.md) |
| Checker CLI | Specified; no product commands | [Schemas and compatibility](docs/SCHEMA.md) |
| Documentation checks | Executable repository tools | [Contribution checks](CONTRIBUTING.md) |

## Start with the method or the next task

- [Survey register](docs/SURVEY_REGISTER.md) explains the machine-readable output and its limits.
- [Trace-freshness boundary](docs/TRACE_FRESHNESS_BOUNDARY.md) separates established fingerprint/impact behavior from Upheld's assurance layer.
- [Component design](docs/COMPONENT_REGISTER_DESIGN.md) records the next schema work.
- [Current method](docs/METHOD.md) explains how to assess a defense.
- [Self-audit](docs/SELF_AUDIT.md) applies the method to Upheld and records observed faults and remaining gaps.
- [Agent guide](docs/UPHELD_SKILL.md) explains the opt-in skill prototype and its untested live-client behavior.
- [Todo list](TODO.md) records remaining work and completed decisions.
- [Design choices](docs/DECISIONS.md) explain the product boundary and the source of each rule.
- [Measured results](measurements/RESULTS.md) separate observed results from pending trials.
- [Earlier drafts](docs/history/README.md) preserve the original arguments and reviews.

Apache-2.0 covers code and documents. See [license terms](LICENSE) and [attribution notice](NOTICE).
