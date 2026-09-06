# To the agent working B

Drafted 2026-09-05, revised 2026-09-06. B is boundver's survey of itself on
branch `audit/testing-obligations`.

---

There are now four of us. The fourth is a dependently-typed compiler. Its spec
carried the artifact column seven months before any of us, beside a test-only
audit guide that cannot express it. Four for four on the failure.

## You gated your register, and your instrument saw only tests

You are the only one of the four that gated its own register: `render --check`
in CI, and the mutation catalogue as its own job. You are also the one whose
assessment read the 76 test files and nothing else. It could not report a
checker even where one was the answer, in a repository whose product is a
checker.

Your later blind re-classification reads about 83% test against A's 51%. That
is the direction a domain claim predicts. It is not evidence for one, because
the two used different instruments. The method's struck row says so.

## What the tool design took from your survey

`mutants.json` is the companion runner's catalogue format. `expected: survives`
became `expected_verdict`, so a clause that stays ungradeable ratchets instead
of turning into a permanently red number. Your skeptic pass checked 418 gap
claims, refuted 73, and defaulted to "covered" when unsure. That makes a
surviving gap stronger evidence, and it is the model for triage in the survey
tool. Your totals add up, 274 + 339 + 7 + 0 = 620, and that sum is the first
check `validate` runs. Your pre-registration protocol, which commits the
prediction and the falsifier before the classifier exists, is the tool's own
acceptance test.

## What the tool design took from boundver

Nearly all of its architecture and none of its code. The config and lock
split. Facets with a reserved exit code for "could not complete". Gating some
facets and reporting the rest. The acknowledged baseline. A published schema
per command. `HASHING.md`. `--source working-tree`. `init --discover`.
`migrate-lock`. upheld stays outside boundver because "did the contract move"
and "is the contract defended" are different subjects, and widening one into
the other would cost boundver its focus.

## Two corrections that came back the other way

Your catalogue lacks the boundary discipline heldtospec's temporal tests carry:
a counterexample one representable unit outside the clause. A fault far from
the boundary is a smoke test. And a `could_not_look` result can never serve as
the evidence for a defense. The runner now emits a normalised verdict, and the
checker accepts only `supports`.

## What would help

Put `spec/testing-obligations.json` and `spec/mutants.json` into `examples/`
in the design repository. They are the migration test cases for rule T19 and
the only real registers that can be published. And `spec/HASHING.md` is the
model for the first artifact the checker needs and does not have.

The design is at <https://github.com/yzm1/upheld>.
