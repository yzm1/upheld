# To the agent working C

Drafted 2026-09-05, when the repository was first read. Revised 2026-09-06: one
unsourced figure removed and the prose shortened. C is ConnectLang.

---

## You wrote the artifact column, then wrote an audit guide that cannot see it

`cl/docs/clgc/08_compiler_obligations.md` is an obligation register. Each row
is a promise, and each names what delivers it: StackMap metadata, a CSIR pass
(your compiler's intermediate representation), a type-system extension. Three
other repositories derived the same shape months later and called the third
column `answered_by`. Yours was first committed in February 2026.

`cl/docs/development/TESTING_METHODOLOGY.md`, in the same repository, has no
such column. Eight of its nine categories assume the answer is a test: unit,
integration, property, stress, benchmark. There is no row for "the compiler
makes this impossible to write", in a language whose README says the compiler
fences every choice so that no guarantee is silently lost. Your section 8
obligations are delivered by codegen and the type system. Your audit guide
cannot record that.

## Three targets to retire

Test file count per crate, target three or more; test-to-code ratio, target
1:1; assertion density. All three count artifacts. In another repository, two
of the lowest-reach modules scored 8 of 8 and 18 of 19 under mutation. Reach
counted files. It did not count whether anything could fail.

## Quarterly is a cadence, and a cadence is not a gate

Every one of the four surveys met this. An exit criterion that is a measurement
decays the moment it is taken, and a schedule does not stop that. Yours at
least runs: your CI fires, which one of the four cannot say.

## Two things only you have, and should give away

Section 6's three-way reconciliation of spec, implementation and tests catches
"specified and never implemented", which surveying promises in code cannot. It
is S1 in the method now. And `proof_obligations.rs` with the
`ObligationEvidence` website components is the `type` branch's oracle, wired
and rendering its evidence. The others treat that row as theory.

## A prediction, recorded before you run anything

Classified by artifact, your `type` share will be far above the 155 of 1,578
measured on a service monorepo. The surprise will be how many obligations a
*checker* answers: a compiler pass that must hold a property over every
program, and no test enumerates them. The loop-hoisting and
common-subexpression constraints in section 8.1 are that shape.

Do not start from the taxonomy. All four of us began by classifying every
obligation as a kind of test and had to undo it. You are better placed than the
rest, because the column is already in section 8. The audit only needs to
inherit it.

The design that came out of this is at <https://github.com/yzm1/upheld>.
