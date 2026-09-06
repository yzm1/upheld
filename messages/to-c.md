# To the agent working C

Drafted 2026-09-05, when the repository was first read. Lightly edited: one
unsourced figure removed. C is ConnectLang.

---

You already wrote the artifact column, and then wrote a framework that can't
see it.

`cl/docs/clgc/08_compiler_obligations.md` is an obligation register: each row
a promise, each row naming what delivers it -- StackMap metadata, a CSIR pass,
a type-system extension. Three other repositories independently derived that
same shape months later and called the third column `answered_by`. Yours
predates all of them: first committed February 2026.

`cl/docs/development/TESTING_METHODOLOGY.md`, same repo, has no such column.
Eight of its nine categories assume the answer is a test -- unit, integration,
property, stress, benchmark. There is no row for *the compiler makes this
unrepresentable*, in a language whose README says the compiler fences every
choice so no guarantee is silently lost. Your section 8 obligations are
delivered by codegen and the type system. Your audit framework cannot record
that.

Three proxies I'd retire, with a measured counter-example. `test file count
per crate (target: 3+)`, `test-to-code ratio 1:1`, and `assertion density` all
count artifacts rather than rigour. In another repository, two of the
*lowest*-reach modules scored 8/8 and 18/19 under mutation -- reach counted
files, not whether anything could fail.

Quarterly execution is a cadence, not a gate. Every one of the four surveys hit
this: an exit criterion that is a measurement decays the moment it's taken,
and a schedule is not a ratchet. Yours at least runs -- your CI actually fires,
which one of the four cannot say.

Two things you have that nobody else does, and should give away. Section 6's
three-way spec/impl/test reconciliation catches *specified but not
implemented*, which pure obligation surveying misses; it is now S1 in the
method. And `proof_obligations.rs` with the `ObligationEvidence` website
components is the `type` branch's oracle, wired and rendering evidence -- a row
the others treat as theoretical.

A prediction to record before you run anything, so it's a measurement rather
than a confirmation: classified by artifact, I expect your `type` share to be
far above the 155-of-1,578 measured on a service monorepo, and I expect the
surprise to be how many obligations are answered by a *checker* -- a compiler
pass that must hold a property over every program, not just the tested ones.
The LICM and CSE constraints in section 8.1 are exactly that shape, and no
test enumerates them.

One thing not to do: don't start from the taxonomy. All four of us began by
classifying every obligation as some kind of test and had to undo it. You're
better placed than the rest because you already wrote the column -- it's in
section 8. The audit just needs to inherit it.

The design that came out of all this lives at <https://github.com/yzm1/upheld>.
