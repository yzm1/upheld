# Upheld tracks the evidence behind software promises

Upheld is a software assurance tool in development. It records what code promises, what evidence defends each promise, and when that evidence needs another check.

**The survey has a runnable repository prototype. The Upheld CLI remains unbuilt.** The prototype prepares sources and imports candidate judgments. Documentation checks run separately from the planned product commands.

A promise is a claim that can be false. A defense is a test, rule, type guarantee, or other mechanism intended to uphold it. An evidence record describes a run that assessed a defense. A binding records a person's choice to rely on that evidence.

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
| Survey | Source-packet prototype, external judgment import, and experimental Codex adapter | [Run the prototype](docs/SURVEY_PROTOTYPE.md) |
| Evidence producers | Specified; no product producer | [Checker and producer rules](docs/CHECKER.md) |
| Checker CLI | Specified; no product commands | [Schemas and compatibility](docs/SCHEMA.md) |
| Documentation checks | Executable repository tools | [Contribution checks](CONTRIBUTING.md) |

## Start with the method or the next task

- [Current method](docs/METHOD.md) explains how to assess a defense.
- [Self-audit](docs/SELF_AUDIT.md) applies the method to Upheld and records observed faults and remaining gaps.
- [Agent guide](docs/UPHELD_SKILL.md) explains the opt-in skill prototype and its untested live-client behavior.
- [Todo list](TODO.md) records remaining work and completed decisions.
- [Design choices](docs/DECISIONS.md) explain the product boundary and the source of each rule.
- [Measured results](measurements/RESULTS.md) separate observed results from pending trials.
- [Earlier drafts](docs/history/README.md) preserve the original arguments and reviews.

Apache-2.0 covers code and documents. See [license terms](LICENSE) and [attribution notice](NOTICE).
