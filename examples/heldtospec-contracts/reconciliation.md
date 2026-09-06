# The records support counts, not a probe-yield ratio

Readers planning the survey can rely on the counted rows below. The historical source is Upheld `3cc993e`, recorded on 6 September 2026. This audit rechecks committed artifacts, not current heldtospec behavior.

## Different units explain some totals; two claims remain unresolved

| Unit | Earlier claim | Recount or limit |
|---|---:|---|
| Promise rows | 44 | 44 |
| Nested defenses | 78 | 78 |
| Promises with next_step | 17 | 17 |
| Triage bullets | 18 | 19: 5 odd, 6 ambiguous, 8 missing |
| Probes | 4 in example; 5 in triage | Total unknown |
| Mechanical/probe/decision split | 9 / 5 / 4 | No row-level dispositions support this partition |

The promise `CTR-010` has a next question without its own triage bullet. Two bullets have no promise ID; another joins `CTR-014` and `CTR-043`. Therefore the 17 next questions and 19 bullets measure different sets.

The report describes three executable checks: the published example, an ungradeable expression, and an expectations rewrite. Only the first two include exit results. No raw logs identify their run boundaries. The records `OBS-001` through `OBS-003` preserve those descriptions; they do not establish that exactly three probes ran.

The missing fourth or fifth probe remains unknown. The original author or retained run logs could settle it. No finding-per-probe or minutes-per-finding ratio follows from the available records.

## Survey and execution used different source states

| Record | Revision | What the source establishes |
|---|---|---|
| Register survey | heldtospec c8c9362 | Claims and links in the serialized data |
| RUN-001 | heldtospec c8c9362 | Combined library/CLI attempt exceeded 300 seconds |
| RUN-002 | heldtospec 7f9addc | Later library run: 149 passed, zero failed/skipped; four dirty files |

Upheld commit `233b7bf` corrected an earlier claim of known execution. Commit `3cc993e` then recorded the completed library run. That sequence explains why the survey revision and completed-run revision differ.

The exact dirty contents, intervening subject changes, command arguments, and raw logs remain unknown. The later result cannot certify every defense at the earlier revision. The CLI attempt supplies no completed-suite evidence.

## Stable IDs preserve the corrections

[The observation file](observations.json) holds 19 finding IDs, three described checks, and two suite records. [The original pages](../../docs/history/README.md) remain unchanged in the history directory. No historical record has become an Upheld EvidenceRecord.
