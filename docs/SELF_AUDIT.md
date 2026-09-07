# Upheld's own fault checks found three defects in its package checker

Readers are engineers assessing whether Upheld follows its method. This bounded self-review covers Upheld at merged commit `ee5b075cd918fb8068233e54579d8bb9c9145d39`, plus the repairs in this change, on 7 September 2026.

**The package checker accepted an uninspected source identity and an empty package, and confused damage with failure to inspect.** Version 0.1.1 fixes those defects. The [before observation](../measurements/self-audit-2026-09-07/before.json) matched two of six predeclared expectations. The [final observation](../measurements/self-audit-2026-09-07/final.json) matches all six. These are local fault challenges, without accepted product evidence or a claim that the whole project is defended.

## The reading pass covers current instruments and published product promises

The first pass read the public promises, method, package and survey code, documentation checks, package tests, and CI wiring. We extended the test reading when the full suite exposed a fixture that lacked Git history. Repairs used the predeclared fault checks. [The source list](../measurements/self-audit-2026-09-07/sources.json) pins the declared boundary and records omissions. We applied the new guide in this conversation; this is not a fresh-client or independent-agent trial.

The review includes published promises with no implementing code. It does not re-survey the heldtospec or ConnectLang repositories, reproduce research papers, inspect all historical reviews, test live agent accounts, or implement the remaining product milestone. Those exclusions remain visible because a bounded pass cannot establish project-wide coverage.

## Observed failures changed the implementation

| Finding | Before repair | Repair and observed challenge |
|---|---|---|
| UPH-002: the named commit must contain the bundled method | A real commit with different method bytes, and an unavailable commit, both produced references without inspection. PR #6's review identified the missing comparison. | Read the named Git object and compare its bytes. Reject a mismatch; report unavailable history separately. CI fetches history so this check can actually run. |
| UPH-003: verification requires the known package files | A folder containing only a manifest with an empty file map passed. | Require the supported manifest fields, client, version, source identity shape, and complete file set before comparing hashes. The empty-package probe now fails. |
| UPH-004: clean, violated, and unable to inspect remain distinct | A changed file and a missing package both exited 1. | Return structured results with exits 0, 1, and 2. The clean, altered-file, and unavailable-package probes produce their expected states. |

The source-pin test also protects against a maintenance mistake: updating local hashes while leaving the named commit stale. It checks the commit itself. A Git source check adds a real dependency: export from a source archive or shallow clone without that commit cannot complete. Package verification after export remains independent of Git history.

Manifest hashes still do not authenticate a publisher. A person who replaces a package and its manifest can supply different matching hashes. The promise is a known package shape and consistent file bytes, with this limit stated in the use guide.

## The register separates delivery, candidate defenses, and observations

[The new self-register](../examples/upheld-self-audit/obligations.register.json) records ten promises, including seven about current instruments and three about future product behavior. Every row has a source quotation, a refuting check, reachability, and a next step. The existing [README status case](../examples/upheld-status/README.md) remains a separate record.

Six rows have candidate defenses. Four still have no candidate defense: live agent behavior and the three future product promises. All ten retain unresolved next steps. The [binding map](../examples/upheld-self-audit/obligations.bindings.json) and evidence file remain empty. Passing tests and fault observations cannot create human acceptance.

| Current promise | What supports the current reading | What remains unresolved |
|---|---|---|
| Source identity, package files, and result states | The recorded faults discriminate old and repaired behavior. | Product basis and compatible evidence production remain unbuilt. |
| Refusing existing output | A regression test checks a sentinel file after attempted export. | This run did not inject concurrent filesystem changes or write failures. |
| Exact survey quotations | Tests submit fabricated quotes, wrong ranges, and unknown sources through the importer. | A matching quote can still misrepresent meaning; independent source review remains S02 work. |
| Preserving method rules | The generated reference matches the normative source; changed text fails the gate. | Byte equality cannot grade the quality of those rules. |
| Agent respects evidence limits | The guide states those limits and the package carries invocation controls. | Real-client behavior is untested under S14; prose instructions are not a demonstrated defense. |
| Changed grounds, immutable evidence, and binding authority | The checker and schema documents state these promises. | C01–C09 and P01–P04 still need code and observations. A schema fixture cannot substitute for that execution. |

## Applying the method exposes what this review cannot close

| Method rules | Applied here | Limit |
|---|---|---|
| P1–P3, S1 | Read the declared sources, include missing-code promises, state expectations, then run cheap probes before claiming behavior. | No whole-project coverage or unseen discovery claim. |
| O1–O7, O9–O10 | Record refutable claims, explicit mechanisms, quoted sources, run links, environment needs, reachability, and next questions. | Candidate links remain unbound; observations have local run context rather than product basis. |
| O8 | Keep changed grounds visible and record repaired file hashes. | No product command reassessed a binding. |
| V1–V5 | Separate the package checker from tests of that checker; exercise clean, faulty, and unavailable inputs. Record actual local runs. | Only the stated fault model was challenged. Other tests passing does not grade every defense. |
| V6 | No runtime invariant was graded. | Fault injection for runtime invariants remains outside this pass. |
| H1, D1 | Report unresolved work alongside the promise count and link conditions for future features. | The user’s product mandate remains unchanged. |
| X1–X2 | Keep predeclared results in machine-readable observations and check generated rules in CI. | The new PR's CI result is separate from local results; routine product upkeep is still unbuilt. |
| Rp1–Rp3 | Date and source the observations, label single runs, and review the full report. | This is an author review; it does not claim independent human review. |

## Repeat the fault challenge without manufacturing acceptance

From a checkout with the pinned source history available:

```bash
python tools/probe_self_audit.py --output /tmp/upheld-new-observation.json
python tools/check_docs.py
python -m unittest discover -s tests -p 'test_*.py'
```

The probe uses temporary source fixtures, leaves the project files untouched, and rejects an existing observation path. Its records include times, source hashes, Python and platform details, dirty-tree status, expected results, and actual outputs. They are development observations rather than product evidence records. The [validation record](../measurements/self-audit-2026-09-07/validation.json) records the separate repository checks.

The next work is to independently review survey omissions and agent behavior under S02 and S13–S14, then build and challenge the product evidence path under C01–C09. A green package check must not close those tasks.
