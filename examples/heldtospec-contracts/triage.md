# Triage

The queue the survey tool's second step would produce: the odd, the ambiguous,
the missing. Forty-four promises produced eighteen items. That ratio is the
first measurement of the queue SURVEY_TOOL.md says decides what to build next.

## Odd

Things that are not wrong and are not what a reader expects.

- **CTR-016.** A checker that guards "every actionable verdict is produced by
  a test" by string-matching the constant's name in the suite's source. The
  link is by name, which the method names as the failure it grades hardest.
- **CTR-018.** `accepted:` keys are unchecked free strings inside a model
  family that forbids unknown keys everywhere else. Fails safe, misleads the
  author.
- **CTR-003.** Two duration parsers in one package with different grammars:
  `contracts/mapper.py::parse_duration` takes s/m/h/d and a bare number;
  `metrics/temporal.py` takes w/d/h/m/s/ms/us/ns. A contract author reading
  the metrics docs will write `1w` and get a `ValueError`.
- **CTR-014, CTR-043.** Two doc-versus-code sweeps, each with a static
  exemption list. An entry added to the list escapes the sweep by construction.
  The lists are small and visible; the pattern is worth naming.
- **CTR-017.** A plain YAML contract can never be answered by `type`, because
  the store is unknown without ODCS servers. Correct, and it means the
  five-way distribution for YAML contracts has a structural zero in one cell.

## Ambiguous

Things where the reading did not settle whether a defense exists.

- **CTR-002.** The `[0, 1]` bound on `max_null_percentage` is a `Field`
  constraint. No test submits 50. Is the type the only defense, and is that
  enough?
- **CTR-009.** The additive-compatibility half -- an extra column passes -- is
  in the doc and in no test found. The failing half is covered three ways.
- **CTR-011.** `_cell` escaping is narrated in the docstring with the defect
  it fixed. No test found submits a pipe.
- **CTR-032.** The `own & run.absent` branch has no test named for it. A
  sibling branch is covered.
- **CTR-041.** Missing-file exit code is asserted for `prove`. The handler
  comment for `verify` says the same claim once passed for the wrong reason.
- **CTR-038.** dbt is on PATH here, so the execution half of the adapter can
  run in this environment. Whether it has run anywhere is unknown.

## Missing

Promises that are made and defended by nothing, or that nobody made.

- **CTR-005.** `CONTRACTS.md:91` says `references` is not enforced. It is. The
  page is in the nav; the sweep does not cover it.
- **CTR-044.** The example contract in the same page fails its own witness.
- **CTR-019.** Exit 4 on ungradeable: documented in two places, implemented in
  neither, tested by nothing.
- **CTR-021.** `expected_verdict` is erased by the next write. Documented as
  the mechanism that stops findings becoming noise; tested for its comparison
  semantics; not tested for survival.
- **CTR-012.** The init-to-verify round trip. The workflow test says in its
  own docstring that it stops short.
- **CTR-037.** The parser's error shapes.
- **Nobody made this one:** `prove` is applied to no contract in its own
  repository. No committed `soundness.json`, no example contract. The gate
  exists and gates nothing.
- **Nobody made this one either:** `last_actually_ran`. 468 commits, zero CI
  runs, no hook. One local run of the library half for this survey: 149
  passed. The CLI half timed out and has no known execution.

## What the queue says

Eighteen items from forty-four promises, in one sitting, on a component whose
tests were written by an agent applying the same method. Nine are the kind an
agent resolves mechanically -- grep for a test, run a probe. Five needed a
probe that took minutes and returned a finding each. Four are decisions.

If that ratio holds, the survey tool's second step is a probe runner, not a
classifier: the expensive thing was not deciding what kind of defense a promise
had, it was checking whether a documented behaviour was true.
