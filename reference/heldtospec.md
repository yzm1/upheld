# heldtospec

<https://github.com/yzm1/heldtospec> -- the repository the method and the
checker design were written in. "This repository" in both documents means this
one. Apache-2.0. Read at commit `830a1ea` and after.

## The three-tier example

`src/heldtospec/contracts/mapper.py`, `contract_to_checks()`, line 89:
"Translate enforceable schema, SLA, and expression promises into checks." The
word *enforceable* concedes a remainder. Reading the whole function:

| Tier | What happens | Where |
|---|---|---|
| Enforced, becomes a check | nullable, unique, allowed_values, min/max, regex, schema, freshness, min_rows, max_null_percentage, `checks[].expr` | the loop body |
| Known unenforceable, `logger.warning` | `sla.quality.min_validity` ("NOT enforced"); a check naming a metric with no expected value ("so it cannot fail"); a check with neither | lines 229, 251, 260 |
| Silently dropped, nothing | `ColumnDefinition.references` (`# FK: dataset.column`), `models.py:48`, read by no code anywhere in the package | -- |

The middle tier is `accepted` discovered and reported through a channel that
scrolls past. The bottom tier is `accepted` with nobody accepting it. Line 251
is a vacuity detector nobody called one.

## Boundary discipline

`tests/metrics/test_what_a_temporal_setting_actually_means.py`, lines 74-90:
for every unit the parser accepts, two rows one unit apart with a two-unit
frequency must find no gap, and three units apart with a one-unit frequency
must find one. Both directions, per unit. The docstring names the shape it
replaces: "the control flow is held and the amounts are free." This is R3 in
the checker design.

## The instrument, undefended

`tools/mutate.py` produces the 38-module mutation table in
`docs/TESTING_STRATEGY.md` and is named by no workflow and no hook.
`[tool.mutmut]` in `pyproject.toml` is scoped to `redaction.py` alone. The
pre-commit hook is not installed. The repository was 410 commits ahead of
`origin/main` when the method document first said so and 424 when the document
was next read whole.

## The method's output

`docs/TESTING_STRATEGY.md` is what the method produced when run here. It is
prose. heldtospec has no register, and the method document's self-score marks
every register requirement unreachable for that reason. It is the first
repository the survey tool should be run against; sources in order of expected
yield are the contract format, CLI help, docstrings on the public surface, and
5,127 test functions across 543 files.

## The seeded-violation measurement

The method document reports V5 met here: ten datasets, one afternoon, and a
published guarantee the repository defends with nothing. It is the one branch
oracle that has actually been run anywhere in the set, and the seeded-violation
runner is the companion whose specification is owed.
