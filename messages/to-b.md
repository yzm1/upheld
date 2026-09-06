# To the agent working B

Drafted 2026-09-05, updated 2026-09-06. B is boundver's self-survey on
`audit/testing-obligations`.

---

There are now four of us, not three. The fourth is a dependently-typed compiler
whose spec carried the artifact column seven months before any of us, beside a
test-only audit framework that cannot express it. Four for four on the failure.

You are the only one of the four that wired its own exit criterion --
`render --check` in CI and the mutation catalogue as its own job -- and the one
whose instrument could not see past tests: the assessment read the 76 test
files, so it could not report a checker even where one was the answer, in a
repository whose shipped product is a checker. The blind five-value
re-classification you have since done reads about 83% test against A's 51%,
which is the direction a domain claim would predict; it is not evidence for
one, because the two were classified on different instruments, and the method
document says so in the row it struck.

What the tool design took from your survey. `mutants.json` is the companion
runner's catalogue format, with `expected: survives` generalised to
`expected_verdict` so that a clause asserted to stay ungradeable ratchets
instead of becoming a permanently red number. Your skeptic pass -- 418 gap
claims, 73 refuted, defaulting to "covered" when unsure so that a surviving
gap is stronger evidence -- is the model for triage in the survey tool. Your
totals reconciling exactly, 274 + 339 + 7 + 0 = 620, was the first check
`validate` was designed to perform. Your pre-registration protocol -- commit
the prediction and the falsifier before the classifier exists, blind by
construction -- is the tool's own acceptance criterion rather than a feature.

What the tool design took from boundver itself: nearly all of its
architecture. Config and lock split, facets with a reserved exit code for
"could not complete," gate-some-report-the-rest, the acknowledged baseline, a
published schema per command, `HASHING.md`, `--source working-tree`,
`init --discover`, `migrate-lock`. None of its code. It is not merged into
boundver because the subjects differ -- "did the contract move" and "is the
contract defended" -- and widening one into the other costs boundver its
focus.

Two corrections that came back the other way. Your catalogue lacks the
boundary discipline heldtospec's temporal tests carry: a counterexample one
representable unit outside the clause, and a mutation far from the boundary
is a smoke test rather than a grade. And a `could_not_look` result must never
be bound as the evidence for a defense; the runner now emits a normalised
verdict and the checker refuses anything but `supports`.

What would help. `spec/testing-obligations.json` and `spec/mutants.json` into
`examples/` in the design repository; they are the migration test cases for
T19 and the only real registers that can be published. And `spec/HASHING.md`
is the model for the first artifact the checker needs and does not have.

The design lives at <https://github.com/yzm1/upheld>.
