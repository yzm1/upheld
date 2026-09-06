# ConnectLang

<https://github.com/yzm1/ConnectLang> -- branch `research-consolidation`, read
2026-09-05 (`master` at `391b52d1`). A dependently-typed language and compiler
in Rust. C in the method document.

C ran no survey. It contributes three things.

## An obligation table with an artifact column, seven months early

`cl/docs/clgc/08_compiler_obligations.md`, first committed 2026-02-12. A
normative table `| Obligation | Description | Delivered via |` -- stack maps,
type descriptors, safepoint insertion, barrier insertion, domain-typed pointers,
root liveness, no stale derived pointers -- each row naming the pass or
type-system extension that discharges it. A second table constrains LICM, CSE
and register allocation against stale interior pointers.

"Delivered via" is not `guarded_by`: it records what implements an obligation,
not what would catch it breaking. It is one column away, and it predates the
three surveys by seven months.

## A test-only audit framework in the same repository

`cl/docs/development/TESTING_METHODOLOGY.md`, v1.1, 2026-05-01. Nine audit
categories, eight of them kinds of test. Targets: test file count per crate
(3+ for mature crates), test-to-code ratio (1:1 for critical components),
assertion density. Quarterly execution. No category for a checker, a type, a
runtime invariant, or an accepted gap -- in a compiler whose README promises
"the compiler fences every choice, so no guarantee is ever silently lost."

Section 6, "Language Specification Alignment," reconciles specification,
implementation and tests three ways. None of the other repositories has it. It
is S1 in the method.

## The type oracle, running

`cl_air/src/check/proof_obligations.rs`, `cl_air/tests/proof_obligations.rs`,
`cl_termination/tests/spec_annotation_obligations.rs`, and the website
components `CompilerAirMultiObligationTrace.astro` and
`CompilerAirObligationEvidence.astro`. The compiler generates proof
obligations, discharges them, and renders the discharge as evidence. That is
the `type` row of the method's oracle table, observed rather than proposed.

## The message drafted for its agent

`../messages/to-c.md`.
