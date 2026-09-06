<!--
Snapshot of docs/OBLIGATION_CHECKER.md from heldtospec (https://github.com/yzm1/heldtospec), taken 2026-09-06.
Source sha256 prefix 315b3b2bec981985, 897 lines. That file may be revised there; this is the
version the rest of this repository was written against. In this document
"this repository" means heldtospec, and paths such as tools/, tests/ and
src/heldtospec/ are heldtospec paths. Relative links have been redirected.
-->

# Obligation checker

A design for a tool that grades a register, not a codebase.

[OBLIGATION_SURVEY.md](METHOD.md) is the method: how to find what code
promises and record what defends each promise. This file describes the artifact
that keeps such a record honest once it exists.

**Nothing described here is built, and almost nothing here is measured.** Every
number this design would consume from a repository is currently unknown. Read
the open problems before the command surface.

**This document is normative** in the same sense as the method it follows:
requirements are numbered, each carries a strength tied to the evidence behind
it, and each states how a reader detects that an implementation has violated it.
The strength key is the one in
[OBLIGATION_SURVEY.md](METHOD.md#how-to-read-a-requirement) -- a MUST
is earned by an observed defect, a SHOULD by an argument -- with one adjustment
for an unbuilt tool: the defects behind its MUSTs were observed in neighbouring
artifacts, and each requirement names which. Three MUSTs share one defect: T2
forbids manufacturing a false `adequate`, and T15 and T20 close two specific
doors through which a tool would manufacture one anyway.
[Conformance](#conformance) collects them. Three requirements were moved out of
the checker to a companion during revision and carry `R` numbers alongside a
fourth written for the companion directly; the old `T` numbers are retired and
not reused.

## What it is

> A register states what a codebase promises and what defends each promise.
> This checks whether the evidence recorded for each promise is still entitled
> to its grade.

It does not survey, discover obligations, judge whether a change mattered,
produce evidence, or run a test suite. It holds one question and answers it
conservatively.

## The three things that must never impersonate each other

> **Validity is derived. Evidence is recorded. Acknowledgement is recorded.
> None of the three is permitted to stand in for another.**

Everything below is a consequence of that sentence. A checker fails at its one
job in three characteristic ways: by storing a validity it should have
recomputed, by letting an acknowledgement change what is true, or by letting
evidence appear without a record of what produced it.

The chain of truth, in order:

```
an oracle runs
    -> an EvidenceRecord records exactly what it observed, and the fingerprints
       of what it observed
        -> a person binds that record to a defense
            -> the checker compares the current tree against what the bound
               record observed
                -> validity
                    -> a finding, which a person may acknowledge
```

`generate` appears nowhere in that chain. The lock it writes is a cache. It can
be deleted and rebuilt without changing whether any defense is valid, and that
is the first property an implementation is tested for.

## The unit of validity is the defense assertion

The primitive is not the obligation and not the artifact. It is the **claim that
a particular piece of evidence defends a particular promise**.

```
Promise TEMP-017
  |
  +-- defense  ->  a test        bound to evidence ev-23 (mutation, supports)
  +-- defense  ->  a declaration bound to evidence ev-24 (compiler, supports)
  +-- gap      ->  accepted, defended by nothing, outside the model below
```

Each defense carries its own validity. A promise holding three tests and one
type guarantee has four independent validities, and a single `status` field on
the promise cannot express that one of the four has gone stale.

What the promise-level view can say is narrower than an earlier revision
claimed. Three defenses on one promise might each establish it alone, or
establish it only jointly, or form two alternative strategies -- and nothing in
the register says which. So the checker reports **counts** and calls a promise
with any defense in review an **affected promise**. It does not synthesise a
promise-level adequacy grade, because that would be grading the codebase rather
than the register.

> **T1 (SHOULD)** -- The unit of validity is the defense assertion. Validity is
> derived per defense and never stored. Promise views aggregate defense states
> and do not synthesise an adequacy grade unless the register explicitly
> supplies composition semantics.
> *Detected by:* a stored status field on a promise, or a report that calls a
> promise "defended" or "undefended" on the strength of a count.

A defense has one stored state and it is not a validity: it is **answered** when
a binding names an evidence record for it and **open** otherwise. Validity is
derived only for answered defenses. An open defense is a promise someone has
decided how to defend and not yet defended, and the checker has nothing to say
about it beyond counting it. A promise with no defense and no gap is a promise
nobody has decided about, and `validate` names it.

## Invalidation: events and consequences are different layers

The checker observes events. It does not decide what they mean.

| Observed event | What the checker establishes | Consequence |
|---|---|---|
| Defense artifact modified | Something relevant may have changed | `review_required` |
| Defense artifact missing | The asserted target is gone | `invalid` |
| Defense artifact relocated | Identity may be preserved | `review_required` |
| Subject scope modified | The grade predates the current subject | `review_required` |
| Promise or defense assertion modified | Evidence was established against a different claim | `review_required` |
| Bound evidence superseded | A record claiming to replace the bound one exists | `review_required` |
| Bound evidence contradicted | A newer record for the same defense and oracle says the defense fails | `review_required` |
| Declared environment input moved | A file the oracle named as relevant changed | `review_required` |
| Register provenance moved | An input the register's producer declared changed | `review_required` (register-level) |
| Target cannot be inspected | The checker failed to know | `unresolvable` |

`still_valid` is not the consequence of any one event. It is the consequence of
**no event across all grounds**, and it is the only outcome the checker is never
permitted to reach by assumption.

Each event reports under one of eight **facets**, which are the unit of gating
and the name carried in structured output:

| Facet | Events |
|---|---|
| `defense` | artifact modified; artifact relocated |
| `link` | artifact missing |
| `subject` | subject scope modified |
| `promise` | promise or defense assertion modified |
| `evidence` | bound evidence superseded; bound evidence contradicted |
| `environment` | declared environment input moved |
| `provenance` | register provenance moved |
| `unresolvable` | target cannot be inspected |

**The checker does not need to know whether a change was consequential in order
to be correct.** It needs only to refuse to preserve a grade whose grounds have
moved. Distinguishing a renamed local variable from a deleted assertion would
require reading the artifact for meaning, which is the boundary this design
exists to hold.

Relocation is listed as `review_required` rather than as a preserved identity on
purpose. Rename detection is a similarity threshold, and a threshold is a
judgment. When a relocation is detected it is reported under the `defense`
facet; when it is not, it is indistinguishable from a missing artifact and
reports under `link`, which is the conservative direction.

> **T2 (MUST)** -- When the checker cannot establish that previously validated
> evidence still applies, it does not preserve the prior validation. No code
> path maps a changed ground to `still_valid`.
> *Detected by:* reading the consequence mapping for any branch that reaches
> `still_valid` from a non-empty event set.
> *Defect behind it:* in A, a name-matched join assigned `adequate` on grounds
> that did not support it, and grading cut the pass rate from 751 to 234. A
> false `adequate` was the silent, durable direction, and this requirement
> forbids the tool from manufacturing one.
>
> **T3 (SHOULD)** -- The consequence of an event depends only on which ground
> moved and on whether the target resolves. It never depends on the content of
> the change.
> *Detected by:* a consequence mapping that reads artifact bytes for anything
> other than identity, presence and hash.

## The basis lives in the evidence, never in the lock

An earlier revision compared the current tree against grounds recorded in the
lock, and `generate` wrote those grounds afresh from whatever tree it was given.
So:

```
commit A   ev-23 validates module M; generate; lock.subject = hash(A:M)
commit B   M changes; verify: hash(B:M) != lock.subject  -> review_required
           generate --source B                            (no new evidence)
           lock.subject = hash(B:M)
           verify: hash(B:M) == lock.subject             -> still_valid
```

No oracle ran. No binding changed. The grade was laundered back to clean by
regenerating generated state. That is T2 defeated through a third door, after
the consequence mapping and acknowledgement.

The correction is that **the evidence record carries its own basis** -- the
fingerprints of everything the oracle observed at the moment it ran -- and the
checker compares the current tree against that basis, never against anything
`generate` wrote:

```json
{"evidence_id": "ev-23", "defense_id": "TEMP-017:test-1",
 "oracle": "mutation", "oracle_result": "fired", "verdict": "supports",
 "validated_subject_scope": "metrics.temporal",
 "basis": {
   "promise": "sha256:…",
   "defense_assertion": "sha256:…",
   "artifacts": {
     "tests/metrics/test_temporal.py::test_subsecond_parse": "sha256:…"},
   "subject_scope": {"scope": "metrics.temporal", "hash": "sha256:…"},
   "environment": {"pyproject.toml": "sha256:…", "uv.lock": "sha256:…"}},
 "source_rev": "abc1234", "producer": "mutation-runner/0.1",
 "supersedes": null}
```

The lock still exists, for resolution caching, the reverse index, and
reproducibility of both. It is never the authority for what evidence observed.

> **T20 (MUST)** -- An answered defense is evaluated against the basis its bound
> evidence record recorded. Regenerating any derived state never advances that
> basis.
> *Detected by:* deleting the lock, running `generate`, and finding any defense
> whose validity changed. This is the first test an implementation runs.
> *Defect behind it:* T2's, through a third door -- and A's staleness incident,
> under T6, which is what generated state being treated as authority looks like
> in practice. Generated state that can advance the basis reproduces the false
> `adequate` on a schedule.

## Acknowledgement changes novelty, never truth

A finding has two orthogonal dimensions:

```
validity:         still_valid | review_required | invalid | unresolvable
acknowledgement:  new | acknowledged
```

`review_required + acknowledged` is still `review_required`. Acknowledging a
finding says that someone knows; it does not say that the evidence is entitled
to its grade again. The report always shows validity. The baseline partitions
findings into new and acknowledged. The exit code, which is a gate policy and
not a statement of truth, considers only findings that are both gated and
unacknowledged -- with one exception stated under exit codes.

An earlier revision had a command named `accept` that subtracted acknowledged
drift before reporting. Subject changes, then `accept`, then a green CI, with
the evidence still not entitled to its grade: that is the failure T2 exists to
prevent, reached through a side door. The command is renamed `ack` so that it
cannot be read as accepting evidence, and it is forbidden from touching
validity.

> **T15 (MUST)** -- Acknowledgement never changes a defense's consequence and
> never removes a finding from the report. It applies only to findings produced
> by `verify`; a structural defect found by `validate` cannot be acknowledged.
> *Detected by:* any finding absent from a report because it was acknowledged,
> or any acknowledged finding whose consequence differs from its unacknowledged
> form.
> *Defect behind it:* T2's, through a second door. A tool that lets
> acknowledgement clear a finding reproduces the false `adequate` with a human
> signature on it.

## Evidence has identity, a verdict, lineage, and a binding

The evidence file is append-only. Several records can exist for one defense --
a mutation run that fired, a later one that fired, a later one that could not
look, an exploratory run over a different scope. "Attach matching records" does
not say which one supports the grade, and "pick the newest" is wrong because a
newer record can be an accident.

**Identity.** Every record carries an immutable identifier, its oracle, its
producer, its validated subject scope and its basis.

**Verdict.** A producer normalises its native result one level further than
its own three states, so that the checker can stay ignorant of what any test
framework's output means:

```
oracle_result:  fired | did_not_fire | could_not_look     (the runner's states)
verdict:        supports | contradicts | could_not_establish
```

A mutation that fired supports the defense; one that did not fire contradicts
it; one that could not look establishes nothing. A compiler pass supports; a
compile failure of the guarded declaration contradicts; a build that did not
run establishes nothing. Each adapter owns its own mapping. The checker reads
only the verdict, and knows one more thing about oracles: which `guarded_by`
each is compatible with, following the survey document's oracle table -- test
with mutation, checker with seeded violation, type with the compiler, runtime
invariant with fault injection.

**Lineage.** A record may name the record it `supersedes`. A record with no
lineage claim is another observation and nothing more. An earlier revision made
*any* newer record an event, which meant an accidental run with a broken
environment would put a sound defense into review; that is conservatism past
the point of usefulness. The two events are narrower: a record that claims to
supersede the bound one, and a newer record for the same defense and oracle
whose verdict is `contradicts`.

**Binding.** A defense is answered by naming exactly one record, and that
naming is a human decision that lives in its own file, for a reason given
under Files. When `ev-31` appears claiming to supersede `ev-23`, the defense
enters `review_required` and leaves it only when a person changes the binding.
The checker does not write bindings, so there is no command for this; `why`
reports what the newer record is and what rebinding would do. This is the
answer to what makes a stale defense entitled to its grade again: **new
evidence plus explicit acceptance of that evidence**, with the checker deciding
neither.

> **T16 (SHOULD)** -- Every evidence record has an immutable identifier and
> names its oracle, its producer, its validated subject scope, its verdict and
> its basis. A binding names at most one record, which exists, whose
> `defense_id` is the defense being bound, whose oracle is compatible with the
> defense's `guarded_by`, and whose verdict is `supports`.
> *Detected by:* a binding to an absent record, a record for another defense,
> a compiler record on a test-guarded defense, or a `could_not_establish`
> record, passing `validate`.
>
> **T21 (SHOULD)** -- Only a record claiming to supersede the bound one, or a
> newer `contradicts` record for the same defense and oracle, is an event. Other
> records are observations.
> *Detected by:* an exploratory `could_not_establish` record putting a
> `supports`-bound defense into review.

## The grounds record what was relied upon

`as_of: <commit>` is too impoverished to answer anything. A defense assertion
accepted at a moment rested on several things, called its **grounds**. Four are
fingerprinted in the evidence record's basis at the moment the oracle ran and
compared against the tree now. The fifth cannot be in the basis, because a
superseding record does not exist when the oracle runs; it is a property of the
evidence file, checked by scanning it. Either way a report names which one
moved.

| Ground | Mandatory | Checked against | Moves when |
|---|---|---|---|
| Claim | yes | basis | The promise text, or the defense assertion's own fields, are edited |
| Defense artifact | yes | basis | The test, checker or declaration changes. One hash per locator; any one moving is the event |
| Subject scope | yes | basis | The code the promise is about changes |
| Environment | when the oracle declares inputs | basis | A file the oracle named as relevant changes |
| Evidence lineage | yes | the evidence file | A superseding or contradicting record appears |

The environment ground exists because an unchanged test can cease to be
adequate when the implementation, specification, dependencies, target or build
flags move. It
is optional and declarative for a reason that an earlier revision got wrong: if
"environment" meant whatever toolchain happened to be installed, the same tree
on two machines would produce two observations, and nothing would be
comparable. So an oracle **declares which files constitute its relevant
environment** -- a lockfile, a toolchain file, a build configuration -- and
records their fingerprints in its basis like any other ground. An oracle that
declares nothing has no environment ground, and the record says so.

A report then reads:

```
TEMP-017:test-1   bound: ev-23 (mutation, supports, rev abc1234)
  promise             unchanged
  defense artifact    unchanged
  subject scope       changed      basis sha256:9f2c…  now sha256:7d11…
  evidence lineage    unchanged
  environment         unchanged    (pyproject.toml, uv.lock)
  => review required: validation predates subject change
```

> **T4 (SHOULD)** -- Every evidence record's basis fingerprints the claim, the
> defense artifacts and the subject scope separately, plus environment when the
> oracle declares inputs, using the hashing profile the config names. Lineage
> is checked against the evidence file and is not in the basis.
> *Detected by:* a report that can say a defense is stale and cannot say which
> ground moved; an environment ground computed from anything not in the tree;
> or a basis produced with a profile the checker does not recognise.

## Granularity: claimed subject precision is bounded by validated precision

Three scopes are in play and an earlier revision confused two of them:

| Field | Answers | Participates in |
|---|---|---|
| `artifact_locator` | Where is the defending artifact | Identity and change tracking |
| `subject_scope` | What code the promise, and this defense, are about | The granularity and containment checks |
| `validated_subject_scope` | Over what subject the oracle established adequacy | The granularity check |

The first and the second are in different trees and need not be nested. A test
under `tests/metrics/` defending a promise about `metrics.temporal` is the
normal case. Comparing the artifact locator against the validated scope, as the
earlier revision did, compares two coordinate systems.

Two invariants hold between the scopes, and both are checked structurally.
**Containment:** a defense's `subject_scope` lies within its promise's, so that
good mutation evidence over `billing/` cannot be bound to a promise about
`parser/`. **Precision:** a defense may not claim a subject scope narrower than
the one its bound evidence validated. A campaign that established "this test
set kills the relevant mutants in module M" supports a claim about M; it does
not support a claim about lines 317 to 321 of M. Subject scopes are nested
paths -- package, module, symbol, range -- and a claim is narrower when it is
strictly inside.

The consequence is uncomfortable and is stated rather than hidden. Mutation run
at module scope validates at module scope, so every test-branch defense graded
by that campaign is pinned to the module, and any change anywhere in the module
puts all of them into review. That is correct, and it is expensive.

**The fix belongs to the oracle, not to the tracker.** Where module-scoped
invalidation produces more review than capacity allows, the answer is to run
mutation at finer scope and record grades there. Finer locators over coarse
evidence buy nothing; finer evidence is the only thing that legitimately narrows
a blast radius. This is also the only sanctioned way to satisfy the capacity
constraint in the governing objective below, since the obvious ways are
forbidden by T2, T15 and T20.

> **T5 (SHOULD)** -- A defense's `subject_scope` lies within its promise's
> `subject_scope`, and is not strictly inside the `validated_subject_scope` of
> its bound evidence. `validate` reports violations of the first as
> `scope_outside_promise` and of the second as `precision_exceeds_evidence`.
> The artifact locator participates in neither.
> *Detected by:* a defense scoped outside its promise, or a range-scoped claim
> over module-scoped evidence, passing `validate`; or an implementation that
> compares the artifact locator against anything.

## Two traversals

Two questions need two indexes:

- **Promise first.** Which recorded defenses of this promise are still current?
- **Diff first.** These twelve things changed; which bound evidence no longer
  matches the tree?

The second is the everyday operation once a register is large. The lock may
hold a materialised reverse index for it, and this design does not require one.
Measured here on a synthetic register of ten thousand promises and 21,650
defenses -- an order of magnitude beyond any that exists -- a full load took
about 110 milliseconds and building the reverse index in memory about 11. The
index is a convenience, not a requirement, until a real register makes it one.

## Ontology

Frozen before any code, because these are the things that must not impersonate
each other.

```
Promise                                   # judgment
    id, text, subject_scope

DefenseAssertion                          # judgment
    id, promise_id, guarded_by,
    artifact_locator(s), subject_scope

GapAssertion                              # judgment
    promise_id, reason

EvidenceRecord                            # immutable observation
    evidence_id, defense_id, oracle,
    oracle_result, verdict,
    validated_subject_scope, basis,
    source_rev, producer, supersedes

EvidenceBinding                           # human acceptance decision
    defense_id -> evidence_id

CurrentObservation                        # derived from the tree; never stored
    grounds as they are now

Validity                                  # derived; never stored
    compare(CurrentObservation, bound EvidenceRecord.basis)

Finding                                   # derived; never persisted as truth
    subject (defense:<id> | register),
    facet, consequence, acknowledgement

Acknowledgement                           # human knowledge of a finding
    finding fingerprint, reason, who, when

Lock                                      # cache; never the authority
    resolved artifacts, reverse index,
    register provenance fingerprints

Config                                    # operational policy; not methodology
    gated facets, hashing profile version,
    resolver versions, schema version
```

A `GapAssertion` is not a `DefenseAssertion`. It carries no evidence claim, so
there is nothing for the checker to invalidate, and it sits outside the four
validity states. It appears in reports as what it is.

## Files

| File | Written by | Holds |
|---|---|---|
| `obligations.config.json` | a person | Operational policy: gated facets, hashing profile version, resolver and schema versions |
| `obligations.register.json` | a person, or a producer the register names | Promises, defenses, gaps |
| `obligations.bindings.json` | a person | Which evidence record each answered defense is bound to |
| `obligations.evidence.jsonl` | oracle producers, append-only | Immutable evidence records with their bases |
| `obligations.lock.json` | `generate` | Cache: resolutions, reverse index, register provenance fingerprints |
| `obligations.baseline.json` | `ack` | Acknowledged finding fingerprints with reasons |

All six are committed; the lock may be absent, in which case `verify` builds
what it needs in memory. Evidence is a line-delimited file because appending an
immutable record to a JSON array means rewriting its terminator, which is
hostile to merges for no benefit.

**Bindings are a separate file because the register may be generated.** An
earlier revision said the register is never generated, which forbids A's
register from existing: it is produced by a seven-minute script over the tree.
The non-goal was always narrower -- **the checker never creates, infers or
edits the register** -- and a repository-specific survey tool emitting one is
the normal case. But a generated register that people also edit is a file with
two authors and no rule about who wins: the next legitimate regeneration
overwrites the binding a person made, and provenance fingerprinting of the
producer's *inputs* cannot see that the *output* was hand-edited. So the human
decision lives where no producer writes. A generated register declares its
producer and its inputs; the lock fingerprints those inputs; when they move,
`verify` reports a register-level `provenance` finding and never reruns the
producer. This is what an earlier `fresh` command was for.

The config, the committed lock, the acknowledged baseline, the published output
schemas and the requirement that hashing be specified rather than assumed are
taken from boundver, which solved the same structural problem for declared
contracts one level down.

> **T6 (MUST)** -- The checker never creates, infers or edits the register or
> the bindings. The lock, when present, is never hand-edited, and on a clean
> tree `generate` reproduces it byte for byte.
> *Detected by:* running `generate` on a clean tree and diffing; any checker
> command that writes to the register or the bindings.
> *Defect behind it:* A's survey documenting that generated state goes stale
> silently was staged for commit while its own regeneration was still running,
> and the committed copy predated a finding the fresh copy contained. Generated
> state that anything can edit by hand cannot be told apart from generated state
> that is merely old -- which is why, under T20, generated state is also never
> the authority.
>
> **T22 (SHOULD)** -- Bindings live in a file that no producer writes.
> *Detected by:* regenerating a generated register and finding a binding gone.
>
> **T17 (SHOULD)** -- The hashing profile is specified in a normative document
> the config names by version, and every evidence producer computes its basis
> with the same profile. It settles at least: tree versus working tree; path
> normalisation; line-ending equivalence; symlinks; ordering of collections;
> canonical serialisation of the promise text and the defense assertion; the
> sentinel for missing versus unreadable; how a range or symbol is hashed; and
> how the profile itself is versioned.
> *Detected by:* two conforming implementations, or a producer and the checker,
> disagreeing about whether the same defense drifted. No such document exists
> yet. Because the basis now lives in the evidence, this is the first artifact
> an implementation needs, and it is listed under open problems for that
> reason.
>
> **T18 (SHOULD)** -- A register with a producer declares the producer and its
> inputs; the lock fingerprints them; `verify` reports their drift as a
> register-level finding and never reruns the producer.
> *Detected by:* a generated register whose inputs changed producing a clean
> `verify`, or a checker command that invokes a producer.

## Commands

`validate` -- reads the config, the register, the bindings and the evidence
file; touches no tree; never consults the baseline. It enumerates **every**
structural defect it finds and exits 1 if there are any, rather than stopping
at the first: schema; required fields; `guarded_by` present and in the enum
with no default; a promise with no defense and no gap; a binding that violates
T16 -- absent record, wrong defense, incompatible oracle, verdict other than
`supports`; `scope_outside_promise`; `precision_exceeds_evidence`. The binding
check is the cheapest vacuity check available and the one a register is most
likely to fail on its first run. For a register in an older schema, `validate`
emits a migration patch it does not apply.

`basis --defense <id> --source <rev>` -- computes the grounds for one defense
against a tree, with the config's hashing profile, and prints them. This is the
one command that exists for producers: an evidence producer calls it at run
time to obtain the basis it records, so that no producer reimplements hashing.
It writes nothing.

`generate --source <rev>` -- builds the cache: resolves every locator, builds
the reverse index, fingerprints the register's declared provenance inputs,
writes the lock. Records; never judges; never the authority.

`verify --source <rev>` -- requires the current source, the register, the
bindings and the evidence file; uses the lock if present; does not require
traversable history. For each answered defense it computes the current grounds
and compares them against the bound record's basis; classifies into events;
maps events to consequences; marks each finding new or acknowledged against the
baseline; reports all of them. The exit code is computed as stated under exit
codes.

`affected <range>` -- the diff-first traversal. Requires only the two
endpoints.

`ack <finding-fingerprint> --reason <text>` -- records that a person has seen a
`verify` finding. It writes the baseline and nothing else. It cannot acknowledge
a `validate` finding.

`why <id>` -- explains one result: which ground moved, what the bound record's
basis said and what the tree says now, what superseding or contradicting record
exists if any, and what rebinding would do. This is the one command permitted
to walk history, because it runs on one identifier at a time, and it degrades
to "history unavailable" on a shallow checkout rather than failing.
Reconstructing fine-grained identity from history was measured on this
repository at over two minutes for a single seventeen-line range across 1,262
commits, so history is a diagnostic and never in the path of routine
verification.

`report` -- counts. The number of defenses in `review_required` is printed
before the number of promises, because the second measures how much has been
noticed and the first measures how much is still moving. Open defenses and gaps
are each counted separately from both.

There is no `mutants`. An earlier revision had one, in a document that also
said the tool runs no test suite. It edits source, executes test commands and
records oracle results, which are an evidence producer's responsibilities, and
the companion section below holds them.

> **T8 (MUST)** -- `guarded_by` is required on every defense and has no default.
> `validate` reports its absence as a defect rather than assuming a value.
> *Detected by:* an entry with the field absent passing `validate`.
> *Defect behind it:* four repositories, four times, every survey classified
> every obligation as a test when nothing forced the question. An enum with a
> default gets the default.
>
> **T9 (SHOULD)** -- `validate` enumerates every structural defect before
> exiting, so that a register with six hundred missing fields receives one
> finding class with six hundred instances and exit 1, not an exception at the
> first. `verify` requires inputs that passed `validate`. Nothing is
> acknowledged by either.
> *Detected by:* a `validate` run that stops before enumerating all defects;
> or a baseline file appearing after any command other than `ack`.
>
> **T19 (SHOULD)** -- For a register in a previous schema version, `validate`
> emits a migration patch and does not apply it. Migration never manufactures
> evidence: an old `status: answered` defense with no deterministically
> identifiable real evidence record migrates to open, with a diagnostic saying
> why.
> *Detected by:* an old-schema register producing a bare failure, a rewritten
> register, or a binding to a record with no producer. Two of the two registers
> that exist today are in the older shape, which makes this an adoption
> requirement rather than a convenience.

## Exit codes

`validate` exits 0, 1 for any structural defect, or 2 when it could not read
its inputs. `verify` assumes inputs that passed `validate`. The facet is in the
structured output, not the exit code; with eight facets, per-facet exit codes
would be theatre, and a shell gate needs only to know what kind of thing
happened.

```
if any finding is unresolvable:            exit 5    (acknowledged or not)
else:  highest consequence among gated, unacknowledged findings
```

| Code | Meaning |
|---:|---|
| 0 | No gated, unacknowledged finding, and nothing unresolvable |
| **2** | **The check itself could not run** -- no tree, unreadable inputs. Never for a per-defense condition |
| 3 | At least one gated, unacknowledged `review_required` finding |
| 4 | At least one gated, unacknowledged `invalid` finding |
| 5 | At least one `unresolvable` finding, acknowledged or not |

`unresolvable` is the one facet where acknowledgement does not reach the exit
code. An earlier revision let a person acknowledge one and thereby turn it into
a clean exit, which recreated "could not look, therefore fine" behind one human
command -- the exact distinction the checker exists to preserve. Acknowledging
an unresolvable finding still records that someone has seen it; it does not
make a target the checker could not inspect into one it could. The way to a
clean exit is to repair the register so that the target resolves, or to record
the gap as what it is. Code 2 is reserved for the run failing as a whole, so
that "the tool could not run", "the tool ran and could not see some things",
and "the tool ran and found nothing" are three different exits. Absent history
is not a reason for code 2; `verify` does not use it.

Gate some facets and report the rest. A ratchet that gates everything on its
first day is reverted on its second. `provenance` and `environment` move on
every dependency bump and start as report-only.

> **T12 (MUST)** -- A target the checker could not inspect is never folded into
> a clean result. Whole-run failure and per-defense unresolvability are distinct
> exits, and neither is 0, and no acknowledgement changes that.
> *Detected by:* a run over a register naming a missing file that exits 0,
> before or after `ack`.
> *Defect behind it:* the four-clause checker definition in the survey document,
> every clause of which came from a defect in a checker that was already
> shipping.
>
> **T13 (SHOULD)** -- Gating is configurable per facet in the config, except
> that `unresolvable` is always gated. A facet not gated is still reported.
> *Detected by:* a configuration that can silence a facet rather than un-gate
> it, or one that can un-gate `unresolvable`.
>
> **T14 (SHOULD)** -- Every command's output conforms to a published schema,
> and the facet and subject of every finding are in that output.
> *Detected by:* a command whose output has no schema file, or a finding whose
> subject cannot be told apart between a defense and the register.

## Companion: the mutation runner

The checker consumes evidence; something else produces it. Mutation runners,
seeded-violation runners and compiler verifiers are **evidence producers**. They
may ship in the same distribution. They are not checker commands, and the
checker's positioning -- it runs no test suite -- is a statement about the
checker. Only the mutation runner is specified below. A seeded-violation runner
-- the checker branch's oracle, and the one that has actually been run in this
repository -- appends records the same way with `oracle: seeded_violation`, and
its specification is owed.

A mutation runner reads a catalogue and appends evidence records. Each
catalogue entry names a file, a search string that must occur exactly once, a
replacement, the clause it exercises, its distance from that clause's boundary,
and an `expected_verdict`. The last generalises B's `expected: survives`: a
clause asserted to stay ungradeable, with its reason, ratchets instead of
becoming a permanently red number a team learns to ignore.

The runner cannot classify from a shell exit code. A non-zero exit can mean an
assertion caught the mutant, compilation failed, collection failed,
configuration was missing, or the runner itself crashed -- and distinguishing
the first from the rest is the entire point. So the runner needs a **structured
result protocol**, satisfied by an adapter per test framework, which is where
the per-language cost of this design lives. The checker stays language-neutral
because the adapters absorb it; that is a cost, and it is stated here rather
than hidden in the checker's claims.

Before it mutates anything, the runner obtains the basis for the defense it is
about to grade by calling the checker's `basis` command against the tree it is
running on, and records that basis verbatim in the evidence record it appends.
A record without a basis is not evidence the checker can compare against
anything, and T20 cannot be met without this.

The catalogue carries a discipline the runner can require but not supply: a
counterexample sits one representable unit outside the clause it exercises. A
mutation far from the boundary is a smoke test, not a grade. This repository's
own temporal tests are the model -- two rows one unit apart must find no gap,
three units apart must find one.

| File | Written by | Holds |
|---|---|---|
| `mutants.catalogue.json` | a person | Entries as above |

> **R1 (MUST)** -- The runner classifies each entry from a structured result
> into fired, did not fire, or could not look, and maps that to a verdict of
> `supports`, `contradicts` or `could_not_establish`. A run that failed to
> start, to compile, or to collect is never scored as fired.
> *Detected by:* a catalogue whose test command cannot start -- a missing
> environment variable is enough -- and any entry reported as fired or
> `supports`.
> *Defect behind it:* an audit in A that counted red as caught scored exactly
> that as a pass.
>
> **R2 (SHOULD)** -- The runner restores the tree on every exit path.
> *Detected by:* a dirty tree after a run that errored.
>
> **R3 (SHOULD)** -- Every catalogue entry records the distance between its
> mutation and the boundary of the clause it exercises, and the runner reports
> entries that do not.
> *Detected by:* an entry with no stated distance being run.
>
> **R4 (SHOULD)** -- Every evidence record the runner appends carries a basis
> obtained from the checker's `basis` command against the tree the run
> observed, and names the record it supersedes when it is a rerun of the same
> defense and oracle.
> *Detected by:* a record with no basis, or a basis whose profile version the
> config does not name. This is a SHOULD by the strength rule and a
> precondition of T20 in practice.

## The governing objective

Not the minimisation of false alarms. The objective is:

> Minimise silent stale assertions, subject to the review queue remaining
> within the capacity that actually reviews it.

False alarms cost a look and self-correct. A silently preserved grade is durable
and invisible. That asymmetry is why T2, T15 and T20 forbid the three obvious
ways of satisfying the constraint -- laxer invalidation, acknowledgement that
clears, and regeneration that advances the basis -- and why the only sanctioned
way is the one under granularity: narrower evidence. When the queue exceeds
capacity the tool is reporting a fact about the oracle, and the tool is not
where the fix goes.

Capacity itself is two numbers, not one. An agent can cheaply triage a queue of
hundreds into the few that need semantic review; the few are the throughput
limit. Both should be measured rather than assumed.

## What it is not

It performs no survey and discovers no obligations. It produces no evidence,
runs no test suite, and replaces no compiler, coverage tool or mutation engine.
It supplies the repository-level signal that says which of their results are
still believed.

The boundary is semantic rather than physical. An earlier formulation said the
tool does not read source, which is false the moment it hashes a scope:

> The checker may inspect declared artifacts to establish identity, presence and
> change. It does not inspect them to infer obligations, defenses, or semantic
> consequences.

T3 is that sentence as a requirement.

## Open problems

**No hashing document exists, and it is now the first artifact.** T17 names
what one must settle. Because the basis lives in the evidence record, a producer
and the checker that hash differently disagree about every defense from the
first run, so this is not a conformance nicety but the precondition of the core
comparison. It is unwritten.

**The two documents disagree about the schema.** The survey document's field
table stores `satisfied_by` and `status` on the obligation. This design stores
neither there, and adds `subject_scope` and `artifact_locator` to the defense
and moves the binding to its own file. The survey document is the one with two
registers already shaped like it, and it has to move; T19 is how existing
registers follow.

**The granularity and capacity constraints are unreconciled.** Evidence-set
granularity makes invalidation coarse; capacity makes it need to be narrow.
Which binds is an empirical question about churn, and no measurement exists.

**Gaps may need a revisit condition.** A `GapAssertion` has nothing the checker
can invalidate, which is the correct V1 answer. If experience shows accepted
gaps silently outliving the decision that accepted them, a `revisit_on` field
is the smallest addition. It is not designed until that is observed.

**Nothing has been built, and nothing has been measured from a register.** Two
measurements exist and both are about the tool's own mechanics: the cost of
walking history for one range, and the cost of loading and indexing a synthetic
register. Every number the design would consume from a repository -- degree
distributions, churn, queue size -- is still unknown, because no repository yet
produces it.

## What deploying it would measure

The fleet is the measurement apparatus, not merely the beneficiary. A
deliberately conservative first version, deployed across repositories that keep
registers, would produce what the design needs and cannot currently obtain:

- promise and defense-assertion counts
- degree distributions in both directions
- churn of linked artifacts
- invalidations per commit and per week, by event kind
- the fraction auto-resolved, the fraction needing semantic review
- queue age and time to clear

Then the question "is symbol-level identity worth building" becomes answerable.
Hypothetically: if conservative module-level invalidation raises five hundred
candidates and four hundred and ninety are mechanically resolved, finer tracking
is wasted work; if a handful of high-churn files generate most of the unresolved
queue, finer evidence is warranted exactly there and nowhere else. Neither
number is real.

Designing the granularity system before those numbers exist is the same error
the method warns about elsewhere: a confident deduction standing where a cheap
probe was available.

## Conformance

Twenty-three requirements: nineteen on the checker and four on the companion
runner. Seven are MUST, each earned by a defect observed in a neighbouring
artifact and named where the requirement appears; three of the seven share
T2's defect and close doors through which it would recur. Sixteen are SHOULD.
None is MAY. `T7`, `T10` and `T11` are retired; their content is `R1` to `R3`.

| | Requirement | Strength |
|---|---|---|
| **T1** | The unit of validity is the defense assertion; promise views aggregate and do not synthesise adequacy | SHOULD |
| **T2** | A changed ground never maps to `still_valid` | MUST |
| **T3** | Consequences depend on which ground moved, never on the content of the change | SHOULD |
| **T4** | Every evidence basis fingerprints claim, artifacts and subject scope separately, plus environment when declared, with the named profile; lineage is checked against the evidence file | SHOULD |
| **T5** | A defense's subject scope lies within its promise's and is not narrower than its evidence validated; the locator participates in neither | SHOULD |
| **T6** | The checker never creates, infers or edits the register or the bindings; the lock, when present, is reproducible and never hand-edited | MUST |
| **T8** | `guarded_by` required, no default | MUST |
| **T9** | `validate` enumerates every defect before exiting; nothing is acknowledged except by `ack` | SHOULD |
| **T12** | Uninspectable targets are never folded into a clean exit, before or after acknowledgement | MUST |
| **T13** | Gating is per facet in config; `unresolvable` is always gated; ungated facets are still reported | SHOULD |
| **T14** | Every command's output has a published schema carrying facet and subject | SHOULD |
| **T15** | Acknowledgement never changes a consequence or removes a finding; it applies to `verify` findings only | MUST |
| **T16** | Evidence records are immutable, identified and carry a verdict and basis; a binding names one existing, matching, compatible, `supports` record | SHOULD |
| **T17** | The hashing profile is specified normatively and versioned, and producers use it | SHOULD |
| **T18** | A generated register declares its producer and inputs; their drift is reported; the producer is never rerun | SHOULD |
| **T19** | `validate` emits a migration patch for old-schema registers, does not apply it, and never manufactures evidence | SHOULD |
| **T20** | An answered defense is evaluated against its bound evidence's recorded basis; regenerating derived state never advances it | MUST |
| **T21** | Only a superseding record or a contradicting one for the same defense and oracle is an event | SHOULD |
| **T22** | Bindings live in a file no producer writes | SHOULD |
| **R1** | Three-state classification from a structured result, mapped to a verdict | MUST |
| **R2** | The tree is restored on every exit path | SHOULD |
| **R3** | Every catalogue entry records its distance from the clause boundary | SHOULD |
| **R4** | Every record carries a basis from the checker's `basis` command and names what it supersedes | SHOULD |

Since nothing is built, no implementation is scored here. The first one will
be, in this table, before it is used -- and the first thing it is tested for is
T20's detection.

## Provenance

| Element | Source |
|---|---|
| Config and lock split, facets with exit codes, acknowledged baseline, published output schemas (T13, T14), a specified hashing profile (T17) | boundver, read directly |
| Three-state classification from a structured result (R1) | A, from a defect in a shipping audit |
| Generated state guarded and never the authority (T6, T20) | A, from the staleness incident recorded in the survey document |
| A register with a producer (T18) | A, whose register is produced by a script |
| Boundary discipline: a counterexample one representable unit outside the clause (R3) | This repository's own temporal tests |
| `expected_verdict`, generalised from `expected: survives` | B's mutant catalogue |
| Environment as a ground | C |
| `guarded_by` with no default (T8) | All four repositories, by exhibiting the failure |
| Defense assertion as the unit of validity (T1); event and consequence as separate layers (T3); declared granularity bounded by validated granularity; triage capacity distinct from validation capacity | A first external review, untested against any repository |
| Acknowledgement orthogonal to validity (T15); evidence identity and binding (T16); the three scopes (T5); declarative environment (T4); the checker rather than the register as the subject of T6; the runner as a companion (R1 to R3); the three-way non-impersonation principle; gaps outside the model | A second external review, untested against any repository |
| The basis in the evidence rather than the lock (T20); binding admissibility and the normalised verdict (T16); `unresolvable` beyond acknowledgement (T12, T13); evidence lineage (T21); bindings as a separate file (T22); containment (T5); migration never manufacturing evidence (T19); `Finding.subject`; the chain of truth | A third external review, untested against any repository |
| The fix for coarse evidence belongs to the oracle rather than the tracker; per-language adapters as the runner's stated cost; exit codes by consequence rather than by facet; the `basis` command and R4; contradiction as an event alongside supersession; the hashing profile as the first artifact | This document |

The last four rows have no repository behind them.
