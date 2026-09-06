# ConnectLang

<https://github.com/yzm1/ConnectLang>, branch `research-consolidation`, read
2026-09-05 (`master` at `391b52d1`). A dependently-typed language and its
compiler, written in Rust. It is C in the method.

C never ran a survey. It contributes three things.

## Its spec had the artifact column seven months early

`cl/docs/clgc/08_compiler_obligations.md` was first committed on 2026-02-12.
It is a table with the columns `Obligation`, `Description` and `Delivered via`.
Each row is a promise the compiler makes, and each names the pass or the
type-system feature that delivers it. A second table constrains three
optimisations against stale interior pointers: hoisting code out of loops,
reusing repeated calculations, and assigning registers.

"Delivered via" is close to `guarded_by` and is a different thing. It says what
implements a promise. `guarded_by` says what would catch the promise breaking.
The column is one step short, and it predates the three surveys by seven
months.

## Its testing guide is the shape every survey had to unlearn

`cl/docs/development/TESTING_METHODOLOGY.md`, version 1.1, dated 2026-05-01,
has nine audit categories. Eight are kinds of test. Its targets are test files
per crate (three or more for a mature crate), a test-to-code ratio of 1:1 for
critical components, and assertion density. It runs quarterly. It has no
category for a checker, a type, a runtime invariant or an accepted gap. The
README in the same repository promises that "the compiler fences every choice,
so no guarantee is ever silently lost."

Section 6 of that guide, "Language Specification Alignment", reconciles the
spec, the code and the tests three ways. No other repository in the set does
that. It became rule S1 in the method.

## Its compiler runs the type oracle

`cl_air/src/check/proof_obligations.rs`, `cl_air/tests/proof_obligations.rs`,
`cl_termination/tests/spec_annotation_obligations.rs`, and the website
components `CompilerAirMultiObligationTrace.astro` and
`CompilerAirObligationEvidence.astro` together generate proof obligations,
discharge them, and render the discharge as evidence. That is the `type` row
of the method's oracle table, observed rather than proposed.

The message drafted for its agent is `../messages/to-c.md`.
