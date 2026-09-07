# Reply to the obligation survey: what ConnectLang confirms and changes

Originally written 2026-09-06; revised 2026-09-07.

This responds to `OBLIGATION_SURVEY.md` as supplied at SHA-256
`84164ab580ffe40f8c8eeffb511c236884acc6e00931e7236212dadd1620862d`.
It is a design and method response, not a live implementation log, a replacement
language specification, or a completion claim. External-repository results are
attributed reports unless explicitly identified below as locally reproduced.

## Bottom line

The survey is right about the central failure: the unit of assurance is a
falsifiable **obligation**, not a test file, assertion, module, technique, or
coverage score. An artifact is meaningful only if it protects a real promise and
a relevant violation has been shown to contradict the claimed evidence on the
route users will exercise.

That changes how this workstream must be judged, but it does not replace or
shrink its mandate. ConnectLang still has to reconcile research, normative
design, implementation, and observed behavior in both directions; complete the
accepted M0 language and ecosystem needed by its forcing projects; and preserve
implementation-derived improvements where they are better than stale design.
Neither an obligation census nor closure of today's task rows is an M0 exit
criterion by itself.

I would adopt the obligation-first discipline, artifact classification,
explicit unknowns, versioned evidence, and deliberate sensitivity challenges. I
would amend three central claims before making the method authoritative here:

1. Production delivery, defending mechanism, and evidence that the defense can
   discriminate are different relationships and need separate fields.
2. Mutation is a powerful sensitivity instrument, not the only possible oracle
   for a test-backed obligation.
3. The compiler enforcing a language rule is not independent evidence that the
   compiler implements that rule soundly.

## What ConnectLang independently confirms

### The artifact column predates the survey, but the operational join is incomplete

Local Git history confirms that [CLGC chapter 8](clgc/08_compiler_obligations.md)
already contained a per-obligation **Delivered via** column at commit
`b3b1cdf21`, dated 2026-02-12. It names such deliverers as StackMap metadata, a
CSIR transformation, code generation, and a type-system extension. The column's
existence is verified; it does not prove that every named deliverer was complete
or correctly composed.

The later testing methodology did fail to inherit that model. Its old targets
for test files per crate, a 1:1 test-to-code ratio, and assertion density counted
artifacts rather than rigor. Commit `6586e09f1` retired those proxies and changed
the methodology, inventory, checks, and verification wiring to distinguish
delivery, production reachability, evidence, and limits. Therefore the survey's
specific proxy criticism accurately describes the pre-`6586e09f1` state, not
the current prose policy.

The deeper criticism remains current. The thirteen-row
[manual CLGC overlay](development/TEST_INVENTORY_MANUAL_AUDIT.json) records
`delivered_via`, production-wiring observations, evidence descriptions, limits,
and unresolved work, but has no `answered_by` field. The
[primary obligation register](development/COMPILER_OBLIGATIONS.json) has both
`delivered_via` and `answered_by`, but covers a bounded, defect-driven compiler
slice rather than the CLGC register. No single machine-readable CLGC row yet
carries the promise, delivery chain, defending mechanism, observed evidence,
and open state together.

That gap is now owned by
**TEST-OBLIGATION-ARTIFACT-LINKAGE-001/-T**. The resulting path must preserve a
status and next-step state, with an exact next step whenever a row is open. It
must also preserve specified-but-unimplemented promises rather than requiring an
implementing source line before an obligation can exist.

At the published checkpoint `18847f7a7`, the primary register contained twenty
open rows: eighteen classified `test`, two `checker`, and none classified
`type`, `runtime invariant`, or `accepted`. That is not a compiler-wide artifact
census. It is a selected implementation-defect sample and cannot confirm or
refute the prediction that a full language/compiler census will have a much
larger type/checker share. A small CLGC trace measured one explicitly
type-delivered top-level row out of seven; its denominator and limits are
recorded in the
[measurement report](plans/2026-09-05_obligation_evidence_measurement.md#observed-register-and-denominator).

### ConnectLang has its own source-text counterexample

The user's report that another repository found 214 assertion-bearing tests
which pinned source text rather than behavior has not been independently
reproduced here. Its lesson is nevertheless testable, and ConnectLang supplies a
smaller direct instance.

During the GC replay, a compiler-contract test failed because it required
obsolete liveness prose. The implementation behavior had not regressed. Commit
`20a4761e1` removed that source-substring test and retained the two real runtime
tests. [GC-M0-CONTRACT-EVIDENCE-001](../crates/cl_mem/TASKS.md) records the
distinction and the remaining executable owners. Likewise,
[STD-SOURCE-HYGIENE-GATE-001/-T](../../std/TASKS.md) explicitly records that its
530 source-shape checks do not satisfy compiler or runtime obligations.

The rule should therefore be explicit: a source-text assertion is behavioral
evidence only when the accepted promise is itself textual or structural. For a
semantic or runtime promise, it may prove repository shape or point to a
candidate artifact; it does not prove the behavior.

### Existing artifacts did not prove their composition

The GC root chain provides a separate counterexample. The specification named
liveness, stack-map metadata, code generation, and root walking; component
controls existed. Following one concrete promise through the actual JIT/runtime
route still found that an ordinary live local was not represented at an
allocating call and that Windows frames were being interpreted through an
invalid frame-pointer assumption. The first moving-object witness failed before
the composed repair.

The subsequent work added exact relocation and Windows unwind challenges, but
did not turn them into universal GC completion evidence: non-Windows discovery,
AOT publication, view/derived-address provenance, and other root families remain
separate obligations. The experiment and its scope are retained in the
[measurement record](plans/2026-09-05_obligation_evidence_measurement.md#exact-new-root-lifetime-counterexample-to-execute),
not summarized here as an ever-changing status log.

This is stronger than “the right artifacts have tests.” It demonstrates that
the obligation is held only if every required producer/consumer boundary is
connected and the composed route rejects or survives the relevant fault.

### The proof-obligation and website contribution is real but bounded

The [website evidence component](../../website/src/components/CompilerAirObligationEvidence.astro)
makes source snippets and a stored diagnostic inspectable; rendering it does not
run the compiler. The Cargo-discovered golden test definition can invoke the
built `clc`, but the original static trace did not execute that test and must not
be described as an observed run.

Similarly,
[proof_obligations.rs](../crates/cl_air/src/check/proof_obligations.rs) contains
useful type/runtime/proof-required vocabulary and component-level controls, but
it is not the production elaborator's refinement router. The exact deferred
proof-hint/diagnostic integration remains separately tracked. These artifacts
are valuable because they make a branch of the intended model concrete, not
because their presence certifies the live language route.

## What the cross-repository findings establish

The supplied survey reports four repositories: a service monorepo, a versioning
library, ConnectLang, and the originating data-quality library. I independently
checked the ConnectLang history and artifacts above. I did not receive or inspect
revisions of the other repositories, so their distributions, mutation totals,
and the reported 214 source-text tests remain attributed to the survey or the
user rather than presented as ConnectLang measurements.

Within that boundary, the convergence is important:

- multiple efforts started from test taxonomies and later needed an artifact
  axis resembling `answered_by`;
- a repository can have many assertions, test files, or apparently reached
  modules while the asserted behavior is free;
- a workflow declaration and a review cadence do not prove that evidence ran on
  the current revision; and
- measurement itself discovers obligations that a reading pass missed.

The reported distributions do **not** yet establish a domain law. The survey
itself says only one repository received a full artifact classification; another
instrument could see only tests, and ConnectLang was not classified as a whole.
The preregistered prediction of a high type/checker share should remain a
prediction until a comparable census exists.

## Amendments needed for ConnectLang

### Separate promise, delivery, defense, and evidence

One row should be able to answer these distinct questions:

| Field | Question |
| --- | --- |
| `name` / authority | What accepted promise can be false, and who or what makes it normative? |
| `delivered_via` | Which production artifacts jointly implement it, including an explicit missing link? |
| `answered_by` | What kind of mechanism defends or deliberately accepts the obligation? |
| challenge | What plausible wrong behavior should contradict that mechanism? |
| observed evidence | What actually ran, at what revision/configuration, and what distinguished? |
| status / `next_step` | What remains unresolved, and what exact action can resolve it? |

The current version-one vocabulary permits exactly one of `type`, `checker`,
`test`, `runtime invariant`, or `accepted`. Those are useful groupings, but the
schema must not pretend joint or newly discovered mechanisms fit one label.
Until a tested schema extension exists, joint defenses should be represented by
explicitly linked obligations and their production chain retained in
`delivered_via`.

`accepted` also needs care: it is an authorized decision not to defend a
promise, not a technical enforcement mechanism. A warning or silent omission is
not acceptance unless an owner made that decision explicitly.

### Require sensitivity, without making one tool the definition

The survey is correct that passing tests alone are insufficient. It overreaches
when V4 makes mutation the only admissible oracle for every test-backed row.
Mutation demonstrates sensitivity to the selected operators; it does not prove
that the operator set models the obligation, that a missing consumer was
exercised, or that a timeout/build failure was a semantic kill.

The governing rule should be: do not call evidence protective until a justified
violation has been observed to contradict it while an appropriate valid control
still passes. Targeted mutation is one strong way to do that. A replay of the
original defect, a deliberately corrupted artifact, a seeded checker fixture,
fault injection, differential checking, or a bounded reference model can also
be discriminating evidence. Record the fault model and retain survivors or
inconclusive outcomes rather than turning mutation score into another proxy.

### Do not use the compiler as its own soundness oracle

For a language user's program, a type rule can make a violation unrepresentable.
For this repository, the compiler implementing that rule is part of the system
under test. Its acceptance is therefore not independent proof of its own
soundness. Exact invalid-program rejections, valid controls, independent models
or differential checks where practical, checked proof artifacts, and consumed
native results answer different parts of that claim. Trusted assumptions and
unsupported routes must remain explicit.

### Treat provenance and freshness as evidence state, not truth

An artifact path plus a timestamp is insufficient. Evidence should identify the
source revision and dirty-tree state where applicable, command, toolchain,
target/configuration, exercised route, result, omissions, and run time. A changed
source, dependency, flag, or target should require reassessment; it is not by
itself proof of a regression. Updating a hash is not a substitute for replaying
the semantic challenge.

A quarterly survey is a cadence, not a gate. A gate needs a machine-readable
baseline and something that actually re-evaluates or invalidates it. Conversely,
cheap deterministic regeneration can be preferable to a second freshness cache;
“strictly cheaper than regeneration” is not a universal requirement.

### Let research and specification reveal missing code

An obligation survey that starts only from implementation cannot see a promised
feature for which no code exists. ConnectLang cannot require every row to quote
an implementing source line: mature research conclusions, normative design,
published behavior, CLI help, and forcing-project requirements can be the
authority while `delivered_via` honestly records a missing implementation.

Nor can an old design automatically win a disagreement. Research may have moved
past it, and implementation may embody a better coherent decision. The work is
to adjudicate the contract, promote the better decision into the normative
corpus, and then repair every other layer against it.

### Use heuristics as queues, not verdicts

The survey's “untested count is a trustworthy floor” does not follow when fuzzy
matching can miss protected obligations. Report `no link found` separately from
confirmed absence. File reach, assertion density, source-string occurrence, and
name similarity can prioritize reading; none should remove an obligation from
the worklist.

Historical defect frequency is useful evidence, but it cannot govern priority
as “frequency times absent technique.” A first memory-safety failure may have a
historical count of zero. Prior agents' attention also biases the count. Priority
must include consequence, exposure, forcing-project dependency, missing
production links, and the cost of resolving uncertainty.

## Effect on the project mandate

For each consequential M0 slice, I will use the survey as follows:

1. Establish the accepted promise and unresolved design questions before
   selecting a convenient implementation or test. Include promises with no code.
2. Trace exact identities and effects through the supported compiler, runtime,
   standard-library, server/database, tooling, and forcing-project route that
   depends on them.
3. State a plausible wrong behavior before measuring. Execute the smallest
   discriminating challenge and a valid control; deepen it with mutation or fault
   injection where that adds information.
4. Repair the actual delivery boundary, retain the regression or seeded fault,
   and reconcile research, design, implementation, tests, examples, and tasks in
   both directions.
5. Record exact evidence and remaining limits, commit and push coherent batches,
   and run `just verify-full` before closing owning tasks.

This does not freeze discovery until a repository-wide census is complete. The
LeopardCL and other forcing projects are expected to expose new M0 obligations.
It also does not permit hard accepted M0 features to drift into later milestones
because they are difficult, or pull unrelated M1+ machinery into M0 because it
is interesting.

## What ConnectLang can give back

ConnectLang contributes more than a confirmation of `answered_by`:

- its February compiler-obligation table already recorded the multi-artifact
  **delivery** side;
- its three-way specification/implementation/test reconciliation exposes
  promises with no implementation, which a code-only survey cannot see;
- its proof-obligation and website artifacts make the type branch concrete while
  also exposing the difference between rendered evidence and execution;
- its retired liveness source guard is a local counterexample to treating source
  assertions as semantic tests; and
- its GC root-chain experiment shows that individually plausible artifacts and
  tests do not establish their composition.

The durable rule is therefore:

> Name the promise, identify every production artifact that delivers it, name
> the mechanism meant to defend it, and make a relevant violation contradict
> the claimed evidence on the route people will use.

That is the standard this workstream will apply. The survey sharpens the method;
the outcome remains a coherent, actually usable M0 language and ecosystem.
