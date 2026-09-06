# heldtospec, contracts component

The first register produced by the method, against one component, by hand.

| | |
|---|---|
| Source | <https://github.com/yzm1/heldtospec> at `c8c9362` (2026-09-06 07:09 UTC) |
| Component | `src/heldtospec/contracts` and `prove/`, `cli/contract.py`, `docs/CONTRACTS.md`, `docs/CONTRACT_PROVE.md`, the six `tests/contracts` files and six `tests/cli/test_contract_*` files |
| Surveyed | 2026-09-06, one sitting, by an agent applying `docs/METHOD.md` v1.0 |
| Producer | `build_register.py` -- the judgment is in its data, the script only serialises and checks arithmetic |
| Promises | 44 |
| Defenses | 78: test 66, checker 7, type 3, runtime invariant 2 |
| No defense and no gap | 4 |
| Gaps | 4 |
| Open `next_step` | 17 |
| Bindings | 0 |
| Evidence records | 0 |

## What was found

The component turned out to already contain a checker for its own domain.
`contract prove` landed at 04:47 the same morning: it enumerates a contract's
clauses, seeds a violation per clause, grades the check set, pins each verdict
to a clause digest, ratchets with three exit codes, and carries
`expected_verdict`. That is the CHECKER.md design one level down, built
independently and narrower in subject. This register is one level up: the
promises the *code* makes and what defends each.

Five findings, three of them settled by running rather than by reading, which
is the method's P3.

**The published example contract cannot pass its own witness** (CTR-044). The
YAML at `docs/CONTRACTS.md:22-56` -- the example every reader copies --
declares a freshness SLA on `created_at`, a column its schema does not
contain. Extracted verbatim and proved: exit 4, twelve promises, none
defended, eleven unassessed, one errored. The design note lists "a freshness
SLA pointed at a column that is never populated" as a shape the tool exists to
catch, and the tool's own documentation exhibits it.

**The page in the nav promises the opposite of what the code does** (CTR-005).
`CONTRACTS.md:91` still says foreign-key `references` is metadata the
verifier ignores. The mapper has compiled it to `referential_integrity` since
the morning's commit, `CONTRACT_PROVE.md` documents that, and the
rendering-agreement checker sweeps three documents and not this one. The one
page in the mkdocs nav is the one nothing checks.

**Exit 4 on an ungradeable clause is documented and not implemented**
(CTR-019). `CONTRACT_PROVE.md` and the `prove_contract_cli` docstring both
say 4 means stale *or could not be graded*. A contract whose only gradeable
clause is an arbitrary `expr` exits 0 in write mode and 0 in check mode. No
test covers the claim either way.

**`expected_verdict` does not survive the write that follows it** (CTR-021).
The pin is added by hand to `soundness.json`; the next `--register` run
rebuilds the file from the result and drops it. The mechanism the "pinning
what cannot be fixed" section describes survives exactly one run. This is the
generated-file-that-people-also-edit hazard CHECKER.md T22 exists for, in a
sibling of the design that named it.

**A checker whose oracle is the anti-pattern** (CTR-016). The test asserting
every actionable verdict is produced by some test does so by string-matching
`Verdict.X` across the suite's source. A comment, or an assertion that a
verdict is *not* produced, satisfies it. The method calls that a name-matched
join and warns about it in its own section on verdicts.

Smaller: `accepted:` keys are free strings under a model that forbids
unknown keys everywhere else, so a misspelled kind accepts nothing and says
nothing (CTR-018); the init-to-verify round trip is asserted by a test that
stops one step short on purpose (CTR-012); two duration parsers with different
grammars, neither of `parse_duration`'s tested here (CTR-003); the parser's
named error shapes are narrated in a comment and tested by nothing found
(CTR-037).

## What the distribution says, and does not

Sixty-six of seventy-eight defenses are tests. The method's standing finding is
that every survey starts by classifying everything as a test, so the number
deserves suspicion before it deserves belief. Two things argue it is real
rather than instrument: the seven checkers and three types were found by
asking the five-way question per promise and are each named with the mechanism
that makes them that kind; and this component's suite was written by an agent
applying the same method, so its tests are dense where a hand-written suite
would be thin. One thing argues it is undercounted: promises were enumerated
from documents and docstrings, which describe behaviour, and not from the type
system, which describes shapes. Every `_STRICT` model, every `Field(ge=...)`,
the closed `ClauseKind` enum and the frozen `Clause` are promises made
unrepresentable to violate, and only the ones a document happened to mention
are here.

## Where every defense actually runs

`tests/contracts` -- the six library-level files, 149 tests including the
dbt execution half, since dbt is on PATH here -- was run locally on 2026-09-06
at `7f9addc` on a component tree with 4 uncommitted file(s), with `python -m pytest`: **149 passed, 0 failed, 0
skipped**, in under ten minutes. The six `tests/cli/test_contract_*` files were
not run to completion: each CLI test spawns a subprocess whose startup is
dominated by metric discovery, and the attempt including them timed out at 300
seconds. So the library half has one known execution and the CLI half has none.

The repository is 468 commits ahead of `origin/main`, whose last commit is
2026-08-27. The workflow that would run `pytest tests/` has not fired on any
of them. The pre-commit hook is not installed. Every `guarded_by: test` and
`guarded_by: checker` under `tests/contracts` therefore has exactly one
execution anyone can point to, the one above. Every defense under
`tests/cli/test_contract_*` has none: the workflow has not fired, the hook is
not installed, and the attempt made for this survey did not finish. By the
method's V3 the honest `last_actually_ran` is that one timestamp for the
library half and unknown for the CLI half.

`prove` itself is wired to no contract in its own repository: there is no
committed `soundness.json` and no example contract under `examples/`. The
ratchet exists and gates nothing, which is the same X1 the method document
records for `tools/mutate.py`.

## Why bindings and evidence are empty

A binding names the evidence record a defense is entitled to its grade by.
None exists. A test named here is one that was *read* -- its name, docstring
and often its body -- and linked to the promise by judgment. It was not graded
by mutation, which the method says is the only oracle for a test. A checker
named here was read, not audited by a seeded violation. A passing run of the
suite, recorded above, establishes that the tests pass; it establishes nothing
about whether they can fail. So `obligations.bindings.json` is empty and
`obligations.evidence.jsonl` has no records, and the register's `summary`
says so rather than letting a reader infer otherwise from 78 linked defenses.

The four probes in this survey were seeded violations of a sort -- against the
documentation and the CLI, not against a test -- and they produced findings
rather than evidence records, because the thing they graded was the published
promise, not a defense of it.

## Schema decisions made here

The register follows CHECKER.md's ontology and adds the survey document's
descriptive fields, because a register a person cannot read is not one a person
will correct:

- **Promise:** `id`, `text` (stated so it can be false), `subject_scope`,
  `source` (where the promise is *made* -- a doc line or a code line),
  `published_in`, `confidence`, `why`, `the_test_that_would_catch_it`,
  `next_step`.
- **Defense:** `id`, `promise_id`, `guarded_by`, `artifact_locator`,
  `subject_scope`, `why_this_kind` -- the last is the five-way question's
  answer written down, which is the field that resists defaulting to test.
- **Gap:** `reason`, `source`. A promise with a gap and no defense is
  accounted for; one with neither is a finding.

Three things the probe learned about the schema:

- `artifact_locator` for a test is `path::function`, without the class,
  wherever the class was not confirmed. That is enough for a person and not
  enough for a resolver; the locator format is a `next_step` for the tool.
- `subject_scope` for a promise found in a document is the code the document
  is about, which is a judgment the scanner will have to make or ask for.
  SURVEY_TOOL.md flags this.
- `confidence: verified` means the code creating the promise was read and
  quoted. Every promise here is `verified` on that definition, and the
  definition says nothing about the defense.

## What to do with it

- Feed the four undefended promises and the four hand-run probes back to
  heldtospec; three of the five findings are one-line doc fixes and one is a
  test to write.
- The four probes cost minutes. The four hundred and sixty-eight unevaluated
  commits cost nothing to notice and nothing has.
- This register is in the checker's schema. It is the first thing a `validate`
  should be run against when one exists, and `T19` migration is not needed
  because it was never in the older shape.
