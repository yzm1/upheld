# The review failures now have checks and explicit limits

Readers are Upheld maintainers reviewing repairs to the merged D01–D08 work. The starting tree is main at `185ed61dc78221d193a6058583077c3226a1c043`, dated 6 September 2026. It includes the later detection-column and writing-checker repairs.

The initial completion report overstated its checks. D04, D06, and D08 required another pass. The changes below repair the reproduced failures. The product CLI and full semantic validator remain unbuilt.

## Each failure has a specific repair

| Review finding | Before | Repair and check |
|---|---|---|
| RT01: forced completion | Reopening D06 failed the gate | Unique IDs, recognized statuses, and closure links replace fixed task totals. Reopened and new tasks pass. |
| RT02: lost meaning | O10 named an arming condition without guarding it | Current method restores the guard and other omitted clauses. [Rule review](RULE_REVIEW.md) covers each original ID. |
| RT02: silent rule edits | T2 downgrade and T20 reversal passed | Reviewed document hashes and exact strengths require explicit updates; both probes fail. |
| RT03: false status count | Changing 149 library tests to 999 passed | All six factual README counts have checked sources and changed-count tests. |
| RT04: false source format | Unsupported versions became 0.1-probe | Converter checks source version and shape before writing, and requires the actual source path. |
| RT05: incomplete fixtures | Missing evidence files and dangling bindings passed | Both current examples require their evidence files and empty bindings. Future examples may contain evidence. |
| Timestamp shape | Arbitrary text passed as execution time | Date-time format checks accept actual timestamps or the supported unknown state. |
| Verify output | An unresolvable target could accompany exit zero | Unresolvable findings or counts require exit 5, including acknowledged findings. |
| Optimized Python | Optimization removed gate assertions | Explicit checks run under normal Python and `python -O`. |

## Checks establish bounded results

The [regression tests](../tests/test_red_team.py) use deliberate synthetic inputs. They create no product evidence and never bind a defense. Run them with the existing [contributor commands](../CONTRIBUTING.md).

Rule hashes require a visible review step. They cannot judge whether a reviewer approved bad semantics. The full task-list prose still needs review when statuses change; accepting a Reopened row does not automatically rewrite the surrounding report.

The converter creates a review copy only. Its source path describes the supplied input; it does not certify source bytes or execution context. Fixture checks cover the two explicitly unbound examples. General evidence-link checks, exact output-count agreement, and evidence validity remain C02 work.

The historical 149-pass run remains a reported observation with missing raw logs. Checking its README count against that record creates no new execution evidence.

## The original probes now separate bad inputs from honest corrections

The [local run record](../measurements/red-team-2026-09-06.json) records the repeated probes on 6 September 2026. The unchanged tree and D06 reopening pass both commands. The false count, T2 downgrade, T20 reversal, missing evidence file, and dangling binding fail the documentation gate. Optimized Python also rejects the wrong count. Both schema counterexamples now fail.

The baseline passes all 21 repository tests and 31 supplied prose-check tests. All 30 current documents pass the writing checks. These results cover the repair tree and synthetic probes; they do not establish that a product oracle ran.

## D04, D06, and D08 close with narrower claims

D04 closes the documented rule mapping and restored instructions. D06 closes the published record shapes and supported review conversion. D08 closes the listed README claims and known stale wording. None closes the product validator or establishes software adequacy.

The historical snapshots remain unchanged. The supplied writing skill retains the newer changes already on main. This repair changes no skill files.
