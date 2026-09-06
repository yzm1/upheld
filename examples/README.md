# Examples

Real registers this design has to accept, migrate, and be evaluated against.
None is in this repository yet.

## A -- a service monorepo (private)

About 1,578 obligations, classified by a person as 803 test, 620 checker,
155 type. Produced by `ci/survey/extract.py` in about seven minutes.
Thirty-nine checkers, twenty-one wired to nothing. Grading a name-matched join
cut the pass rate from 751 to 234, leaving 517 too loosely linked to trust.

Private. Whether any of it is placed here is the maintainer's decision. Without
it, the largest evaluation set for the survey tool's classifier stays outside
this repository.

## B -- boundver's self-survey

`spec/testing-obligations.json`: 620 obligations. Totals: asserted 274,
examples_only 339, nothing_found 7, unassessed 0; high_risk 368. A skeptic pass
over 418 gap claims refuted 73 and confirmed 345. `spec/mutants.json`: 119
mutants, each with `file`, `search`, `replace`, `tests`, `obligations`, and
`expected: survives` with a reason where a fault is unobservable.

On branch `audit/testing-obligations` at `73db758` in the boundver repository,
unpushed at the time of writing. To be added here by the maintainer.

Both partitions reconcile exactly -- 274 + 339 + 7 + 0 = 620 and 73 + 345 =
418 -- which is the property the checker's `validate` was first designed to
check, before the schema stopped storing status at all.

## What they are for

- **T19 migration.** Both are in the older schema: status on the obligation, no
  evidence binding. They are the migration test cases, and the rule is that
  migration never manufactures evidence -- an old `answered` with no real
  record migrates to open, with a diagnostic.
- **Classifier evaluation.** A classifier that cannot reproduce A's
  distribution from promise text is biased. B's assessment read only its test
  files, so its distribution is its instrument; it is the harder case, and it
  has since been re-classified blind on the five-value axis.
- **Bindings as a separate file.** Neither register has one. Migration creates
  the file empty, and every previously answered defense is open until a person
  binds real evidence to it.

## Not examples

- ConnectLang ran no survey. Its obligation table is in
  `../reference/connectlang.md`.
- heldtospec has no register. It is the first target for the survey tool.
