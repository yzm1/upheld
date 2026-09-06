# The mutant runner is a second tool, and the baseline could hide invalid evidence

An outside review from a language model. The maintainer obtained it on partial context on 2026-09-05, and the text below is verbatim. It reviewed the second draft of `CHECKER.md`: 489 lines, rules T1 to T14, `mutants` and `accept` as checker commands, and five per-facet exit codes.

## Taken

- All eight blockers. `mutants` moved to a companion, and T7, T10 and T11 retired in favour of R1 to R3.
- Acknowledging a finding no longer changes its grade, and `accept` became `ack` (T15).
- T5 now compares subject scope with validated subject scope instead of using the artifact locator.
- Version one no longer infers whether a whole promise is adequate; T1 rewritten.
- Every evidence record has an ID that never changes, and a binding names one (T16).
- A config file added, evidence written one record per line, hashing made a rule (T17).
- Environment inputs declared by the oracle rather than read from the machine.
- T6 changed from forbidding a generated register to forbidding the checker from generating one (T18).
- `validate`, `verify` and `ack` given separate phases, and taking on old registers made a rule (T9, T19).
- The history contradiction resolved; the model frozen; the three-way non-impersonation principle adopted.

## Pushed back on, or extended

- The review does not say what the exit code does with a gated finding someone has acknowledged. boundver's model resolves it: the exit code covers the unacknowledged gated subset, and the report always shows the grade. `CHECKER.md` says so.
- A structured runner protocol brings back per-language adapters. The design states that as the runner's cost.
- Per-facet exit codes collapsed to consequence codes, with the facet in the structured output.

---

<!-- prose-gate:ignore -->

This revision has the right center now. I would **not implement it exactly as written yet**, though: the remaining problems are no longer philosophical; they are a handful of schema/lifecycle contradictions that would otherwise get baked into V1.

The strongest parts should stay: the defense assertion as the unit of validity, event ≠ consequence, conservative invalidation, separate grounds, diff-first traversal, and the governing objective of minimizing silent staleness subject to actual review capacity.

## The blockers

| Priority | Problem                                             | Why it matters                                                   |
| -------- | --------------------------------------------------- | ---------------------------------------------------------------- |
| **P0**   | `mutants` makes this two tools                      | Directly violates the product boundary                           |
| **P0**   | Baseline can hide invalid evidence                  | Can recreate the silent-false-valid failure T2 exists to prevent |
| **P0**   | T5 compares the wrong kinds of scope                | Defense location and validation scope are different axes         |
| **P0**   | Evidence acceptance lifecycle is absent             | No defined operation makes a stale defense valid again           |
| **P0**   | Multiple defenses have no composition semantics     | Promise-level status cannot actually be derived                  |
| **P1**   | Config/hash/environment model is incomplete         | Lock reproducibility is currently underspecified/contradictory   |
| **P1**   | Register authorship was narrowed too far            | "Checker doesn't generate it" became "nothing may generate it"   |
| **P1**   | Old-schema/adoption path is internally inconsistent | `validate`, `accept`, T8 and T9 don't quite compose              |

### 1. Remove `mutants` from the checker

This is the clearest architectural correction.

The document says:

> it does not run a test suite

and later defines a command that edits source, executes test commands, restores the tree and records oracle evidence.

Those are not the same responsibility.

I would make:

```text
register checker
    consumes:
        register
        evidence
        tree
    produces:
        validity findings

oracle producers
    mutation runner
    seeded-violation runner
    compiler/type verifier
    ...
    produce:
        evidence records
```

The mutation runner may ship in the same repository or distribution, but it is a **companion evidence producer**, not a checker command.

Then T7, T10 and T11 move into the mutation-runner specification. That leaves the core checker exactly within the positioning:

> It does not produce obligations.
> It does not test code.
> It checks whether recorded evidence is still entitled to the grade the register gives it.

There is another practical sign that the split is needed: `validate` currently checks a mutant catalogue, but **no mutant-catalogue file exists in the Files section**.

Also, T7 is not actually implementable from a raw shell command alone. A nonzero process exit can mean:

* a test assertion caught the mutant,
* compilation failed,
* collection failed,
* configuration was missing,
* the runner crashed.

Yet precisely distinguishing the first from the others is the whole point of T7. The companion oracle therefore needs a **structured runner protocol**, not merely `test_command → exit code`.

---

## 2. Baseline must never change validity

This is the most dangerous bug.

Currently:

```text
verify
→ classify events
→ map consequences
→ subtract baseline
→ gate/report
```

and `accept` writes drift to that baseline.

But suppose:

```text
subject changed
→ review_required
→ accept
→ baseline removes finding
→ CI becomes clean
```

The evidence is still **not entitled to its grade**. Someone merely acknowledged that fact.

You need two orthogonal dimensions:

```text
validity:
    still_valid
    review_required
    invalid
    unresolvable

acknowledgement:
    new
    acknowledged
```

Therefore:

```text
review_required + new
review_required + acknowledged
```

are both still `review_required`.

The baseline changes **novelty**, never **truth**.

I would change the normative rule to something like:

> **T? (MUST)** — Baseline acknowledgement never changes a defense's consequence. It partitions current findings into acknowledged and unacknowledged findings; it does not remove them from the current validity state.

And I would strongly consider renaming:

```text
accept
```

to:

```text
ack
acknowledge
ack-drift
```

because **accept** sounds dangerously like "accept this evidence as valid."

This amendment is required by the document's own governing objective.

---

## 3. T5 currently compares two different coordinate systems

This needs a substantive rewrite.

These are different:

```text
defense locator
tests/test_temporal.py::test_subsecond_parse
```

and:

```text
validated subject scope
metrics.temporal
```

The first answers:

> **Where is the defensive artifact?**

The second answers:

> **Over what subject was its adequacy established?**

They need not be nested. They often aren't even in the same directory tree.

So these should be explicit separate fields:

```text
artifact_locator
subject_scope
validated_subject_scope
```

Then the intended invariant is something like:

> The **claimed subject precision** must not exceed the precision supported by the accepted evidence.

Not:

> the defense locator must not sit inside the evidence scope.

The current T5 therefore should not merely be tweaked; its operands need changing.

This also gives you a useful structural invariant:

```text
artifact_locator       → identity/change tracking
subject_scope          → what the promise concerns
validated_subject_scope→ what the oracle actually established
```

Only the last two participate in the granularity comparison.

---

# 4. I would withdraw "promise-level status is derived" for V1

The first half of T1 is right:

> state belongs to the defense assertion.

The second half is not yet justified:

> promise-level status is derived.

Derived **how**?

Suppose P has:

```text
test A
test B
type guarantee C
```

There are at least three possible meanings:

```text
A OR B OR C
```

Any one independently establishes P.

Or:

```text
A AND B AND C
```

They jointly establish P.

Or:

```text
(A AND B) OR C
```

There are two alternative defense strategies.

Your many-to-many measurements make this non-theoretical.

If one of twenty linked artifacts goes stale, the checker can say with certainty:

> this defense assertion moved

but it cannot necessarily say:

> this promise is no longer defended

without composition semantics.

That latter statement begins to grade the codebase rather than the register.

### V1 answer

Don't solve Boolean defense algebra yet.

Report:

```text
TEMP-017
    3 defense assertions
    2 still_valid
    1 review_required
```

and call TEMP-017 an **affected promise**, not an invalid promise.

I would rewrite T1:

> **The unit of validity is the defense assertion. Validity is derived for each defense assertion and is never stored. Promise views aggregate defense states but do not synthesize an adequacy grade unless the register explicitly supplies composition semantics.**

That is even more faithful to:

> This grades the register, not the codebase.

---

# 5. The evidence lifecycle needs one missing concept: **accepted evidence identity**

The evidence file is append-only and `generate` currently "attaches matching evidence records."

"Matching" is doing far too much work.

Imagine:

```text
ev-17   mutation     fired
ev-23   mutation     fired
ev-31   mutation     could_not_look
```

Which one supports the defense?

And the document explicitly says a newer oracle record can itself cause `review_required`. So "pick latest" clearly isn't correct.

Each evidence record needs immutable identity:

```json
{
  "evidence_id": "ev-23",
  "defense_id": "TEMP-017:test-1",
  "oracle": "mutation",
  "validated_subject_scope": "...",
  "result": "fired",
  "..."
}
```

and the defense assertion needs an explicit binding:

```json
"accepted_evidence": "ev-23"
```

Then:

```text
ev-31 appears
```

does not silently replace `ev-23`.

It may produce:

```text
new_evidence_available
→ review_required
```

and the assertion becomes current again only after the accepted binding changes.

Importantly, **baseline acknowledgement cannot perform this operation**.

This finally answers the lifecycle question the current document does not:

> What actually makes a stale assertion entitled to its grade again?

Answer:

> **new evidence plus explicit acceptance of that evidence.**

The checker itself still never decides that the semantic relationship is adequate.

---

# 6. The file architecture is missing a file it claims to have

The provenance explicitly says you copied **"Config and lock split"** from boundver.

But the file table contains:

```text
register
evidence
lock
baseline
```

No config.

Yet T13 says gating is configurable.

I think this should simply become:

```text
obligations.config.json
obligations.register.json
obligations.evidence.jsonl
obligations.lock.json
obligations.baseline.json
```

Config holds operational policy, not methodology:

```text
gated facets
locator/resolver versions
hashing profile
environment-input recipes
perhaps schema compatibility
```

The register remains judgment.

Also, if evidence really is **append-only**, I would use `.jsonl`, not `.json`. Appending immutable records to a JSON array means rewriting the array terminator and is unnecessarily merge-hostile.

---

# 7. `HASHING.md` needs to come back

This design now depends more heavily on hashing than boundver does:

> five independently named grounds determine whether evidence stays entitled.

But "hash it" is not a specification.

You need the thing you originally identified in boundver as already solved:

```text
HASHING.md
```

normatively referenced.

It has to settle at least:

* Git tree vs working tree,
* path normalization,
* CRLF/LF,
* symlinks,
* executable bit if relevant,
* collection ordering,
* canonical JSON hashing,
* what part of a promise constitutes the promise ground,
* missing vs unreadable sentinels,
* hashing of ranges/symbols,
* versioning of the hashing algorithm.

Otherwise two compliant implementations can disagree about whether the same evidence expired.

And because this document calls itself normative, that is not an implementation detail.

---

# 8. Environment currently contradicts reproducible locks

You say:

> the lock is a pure function of register + evidence + tree

and T6 requires regenerating it identically on a clean tree.

But the fifth ground includes:

> toolchain, target, build flags or pinned dependencies.

If "toolchain" means whatever happens to be installed on the machine, then:

```text
same tree
same register
same evidence
different machine
→ different lock
```

T6 fails.

So environment cannot mean arbitrary ambient process state.

The clean model is:

> **An oracle declares which environment inputs were relevant to its evidence. Those inputs are themselves deterministically fingerprintable.**

For example:

```json
"environment_inputs": [
  "rust-toolchain.toml",
  "Cargo.lock"
],
"target": "x86_64-unknown-linux-gnu",
"flags": ["..."]
```

Then evidence records what environment it ran under, while the checker can recompute whether the **declared relevant inputs** have moved.

Until that exists, I would actually weaken T4:

> four mandatory grounds plus an oracle-declared context/environment ground when defined.

"Report-only" does not solve nondeterminism in lock generation.

---

# 9. T6 overcorrected on register generation

This is important because it subtly changes the original methodology.

The real non-goal was:

> **this tool never produces obligations.**

That does **not** imply:

> no program may produce the register.

Your original description explicitly allowed a person or a repository-specific script written by that person to build the survey artifact.

But T6 now says:

> "The register is never generated."

That's a different policy.

I'd change it to:

> **The checker never creates, infers, or edits the register.**

A repository-specific survey tool may still emit one.

This matters for `fresh`, too.

The correct conclusion is not:

> generated registers are forbidden, therefore no freshness problem exists.

It is:

> **freshness is not a separate checker mechanism. If a register has a producer, its producer/input provenance is another declared dependency whose drift the checker can report.**

So you can still legitimately have **no `fresh` command** while retaining the original useful capability.

Manual register:

```text
no producer provenance
```

Generated register:

```text
producer: survey.py
inputs: [...]
as_of fingerprints: [...]
```

Input movement becomes a register-provenance finding.

The checker still never reruns the expensive survey.

---

# 10. `validate` / `verify` / `accept` need cleaner phase separation

At present:

* T8 says missing `guarded_by` makes `validate` fail.
* T9 says a nonconforming register produces a complete report rather than stopping.
* `verify` assumes validation passed.
* the adoption prose then discusses `accept` in the same scenario as a register missing `guarded_by`.

These are easy to reconcile:

```text
validate
    always enumerates every structural defect
    exits 1 if any exist
    never consults baseline

verify
    requires valid inputs
    checks temporal validity/drift

ack
    acknowledges verify findings only
    cannot acknowledge malformed schema
```

So a legacy register missing 600 `guarded_by` fields gets:

```text
1 finding class
600 enumerated instances
exit 1
```

rather than an early exception.

That's what T9 is really trying to require.

And because you already know two real registers use the old schema, **migration is a V1 adoption requirement**, not merely an open problem. Since the checker must not rewrite the register, it can emit a migration report/patch without applying it.

---

## 11. One smaller history contradiction

The document very correctly says:

> history is diagnostic and never in routine verification.

But exit code 2 later lists "no history" among reasons `verify` itself cannot run.

Those positions should be reconciled.

I would make:

```text
verify
    requires current source + lock
    does not require traversable history

affected <range>
    requires the requested endpoints

why
    optionally uses history
    degrades to "history unavailable" if shallow/missing
```

A shallow CI checkout should be able to answer:

> the recorded artifact differs

even if it cannot answer:

> in which historical commit did it first differ?

---

# What I think the V1 ontology should now be

Not a full schema, but I would freeze these concepts before coding:

```text
Promise
    id
    text
    subject_scope

DefenseAssertion
    id
    promise_id
    guarded_by
    artifact_locator(s)
    accepted_evidence_id

EvidenceRecord          # immutable
    evidence_id
    defense_id
    oracle
    validated_subject_scope
    oracle_result
    relevant_environment
    producer/version

Lock                    # generated
    resolved artifacts
    promise ground
    defense-artifact ground(s)
    subject ground
    accepted-evidence ground
    environment/context ground
    reverse index if worthwhile

Finding                  # derived, never persisted as truth
    defense_id
    facet
    consequence
    acknowledgement

Baseline
    exact finding fingerprint
    acknowledgement metadata
    reason
```

And I'd make this sentence normative:

> **Validity is derived. Evidence is recorded. Acknowledgement is recorded. None of those three is allowed to impersonate another.**

That is the missing invariant tying the whole design together.

## `accepted` gaps

I would **not block V1 on inventing an oracle for them**.

They are not defense assertions. Say so.

Represent:

```text
GapAssertion
    promise_id
    reason
```

Show them in reports, but keep them outside:

```text
still_valid
review_required
invalid
unresolvable
```

If experience shows they need expiration, add:

```text
revisit_on
review_after
```

later.

Right now the document correctly notices that they have no invalidation mechanism, but the simplest answer may be that **the checker has nothing to invalidate because there is no evidence claim there**.

---

# What I would actually do next

I would make these changes **before writing implementation code**:

1. split the mutation oracle from the checker;
2. replace T5's locator/scope comparison;
3. make baseline acknowledgement orthogonal to validity;
4. remove promise-level adequacy status from V1;
5. give evidence immutable IDs and explicit accepted bindings;
6. restore `config` + normative hashing;
7. make environment deterministic/declarative;
8. change T6 from "register never generated" to "checker never generates register";
9. cleanly separate validate/verify/ack;
10. update the survey schema at the same time.

After those, I would consider the design **ready for a deliberately simple fleet V1**. The remaining questions about cardinality, churn, reverse-index persistence, symbol granularity, and agent throughput genuinely should then be learned by deployment rather than designed in advance—as the document itself argues.

The architecture has converged substantially; the main danger now is no longer under-design. It is accidentally letting **acknowledgement, evidence production, or promise-level inference** creep across the very boundary the tool was created to enforce.

<!-- /prose-gate:ignore -->
