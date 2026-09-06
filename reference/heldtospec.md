# heldtospec

<https://github.com/yzm1/heldtospec>. The method and the checker design come
from here, so "this repository" in both means heldtospec. Apache-2.0. Read at
commit `830a1ea` and later.

## Its contract compiler handled promises in three tiers and named one

`contract_to_checks` in `src/heldtospec/contracts/mapper.py`, line 89:
"Translate enforceable schema, SLA, and expression promises into checks." The
word *enforceable* admits a remainder. The whole function shows three tiers.

| Tier | What happens | Examples |
|---|---|---|
| Enforced: the promise becomes a check | `nullable`, `unique`, `allowed_values`, `min`, `max`, `regex`, the schema, freshness, `min_rows`, `max_null_percentage`, `checks[].expr` | The loop body |
| Known unenforceable: a `logger.warning` | `sla.quality.min_validity`, with the message "NOT enforced"; a check naming a metric with no expected value, "so it cannot fail"; a check with neither | Lines 229, 251 and 260 |
| Silently dropped: nothing | `ColumnDefinition.references`, the foreign key, at `models.py:48`. No code in the package read it | None |

The middle tier is a gap the code found and then reported to a log that
scrolls past. The bottom tier is a gap nobody decided on. Line 251 was already
a vacuity detector, and nobody had called it one. On 6 September 2026 the
repository shipped `contract prove`, which grades every clause by seeding a
fault. `../examples/heldtospec-contracts/README.md` records the survey of that
component.

## Its temporal tests show the boundary discipline

`tests/metrics/test_what_a_temporal_setting_actually_means.py`, lines 74 to
90. For every unit the parser accepts, two rows one unit apart under a two-unit
frequency must find no gap. Three units apart under a one-unit frequency must
find one. Both directions, every unit. The docstring names the shape the test
replaces: "the control flow is held and the amounts are free." This is rule R3
in the checker design.

## Its own mutation tool runs nowhere

`tools/mutate.py` produces the 38-module mutation table in
`docs/TESTING_STRATEGY.md`. No workflow and no hook names it. `[tool.mutmut]`
in `pyproject.toml` covers `redaction.py` alone. Nobody has installed the
pre-commit hook. The repository was 410 commits ahead of `origin/main` when
the method first counted, 424 on the next whole read, and 468 on 6 September
2026.

## It has no register, so it is the survey tool's first target

`docs/TESTING_STRATEGY.md` is what the method produced here, and it is prose.
The method's self-score, kept in `../docs/history/2026-09-06/METHOD.md`, marks
every register rule unreachable for that reason. The sources to scan, in
expected order of yield: the contract format, CLI help, docstrings on the
public surface, and 5,127 test functions across 543 files.

## It ran the seeded-violation measurement

The method reports rule V5 met here: ten datasets in one afternoon, and a
published guarantee the repository defended with nothing. It is the only
branch oracle anyone in the set has run. The seeded-violation runner is the
companion that still needs a spec.
