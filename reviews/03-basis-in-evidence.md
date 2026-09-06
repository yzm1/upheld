# Regenerating the lock could launder a stale grade, so the basis moved into the evidence

An outside review from a language model. The maintainer obtained it on partial context on 2026-09-05, and the text below is verbatim. It reviewed the third draft of `CHECKER.md`. That draft had 733 lines, rules T15 to T19 and R1 to R3, `ack` in place, and grounds recorded in the lock.

## Taken

- All six changes and the five smaller repairs. The basis moved out of the lock and into the evidence record, with the lock demoted to a cache (T20). The first test an implementation runs: delete the lock, regenerate, and confirm no grade changed.
- Rules for which record a binding may name, and the verdict `supports`, `contradicts` or `could_not_establish` (T16).
- An acknowledged `unresolvable` still exits 5 (T12, T13).
- Evidence lineage through `supersedes` (T21).
- Bindings in a separate file no producer writes (T22).
- Containment folded into T5; migration never invents evidence (T19); `Finding` given a `subject`; the per-status-count remnant removed; the traversal wording corrected; the chain-of-truth diagram adopted.

## Pushed back on, or extended

- A `basis` command, so producers do not reimplement hashing, and R4 requiring runners to use it.
- A contradicting record as an event beside a superseding one. Otherwise a `did_not_fire` could sit unread beside a bound `supports`.
- The hashing profile promoted to the first artifact among the open problems, since a runner and a checker that hash differently disagree about every defense from the first run.

---

<!-- prose-gate:ignore -->

This revision resolves almost all of the previous pass. The architecture is now coherent enough that the remaining defects are **specific loopholes**, not a need to rethink the tool.

I would still **not start implementation yet**, because one remaining issue can defeat the entire ratchet.

## Verdict

The previous major problems are fixed:

* validity / evidence / acknowledgement are explicitly separated;
* promise-level adequacy is no longer invented from defense counts;
* acknowledgement cannot change truth;
* evidence has immutable identity and explicit binding;
* T5 now compares subject scope with validated subject scope rather than test location;
* `mutants` is correctly outside the checker;
* generated registers are permitted without making register generation the checker's job;
* `validate`, `verify`, `ack`, and historical diagnostics now have sensible boundaries.

I see **three implementation blockers**, then several much smaller repairs.

---

# P0 — `generate` can currently erase staleness

This is the largest remaining flaw.

The document says:

> a defense leaves review only when a person changes `accepted_evidence` to the new record.

and correctly concludes that recovery requires:

> **new evidence plus explicit acceptance of that evidence.**

But the lock is described as containing the observed grounds, while `generate` resolves the current tree and writes those grounds afresh.

So consider:

```text
commit A
    ev-23 validates module M
    generate
    lock.subject = hash(A:M)

commit B
    M changes

verify
    hash(B:M) != hash(A:M)
    => review_required           correct

generate --source B             ← no new evidence!

lock.subject = hash(B:M)

verify
    hash(B:M) == lock.subject
    => still_valid              WRONG
```

No evidence was produced. No binding changed. Yet the grade was laundered back to clean merely by regenerating generated state.

That directly contradicts the central rule.

## The correction

**The lock cannot be the authority for what state the accepted evidence validated.**

The accepted evidence must itself carry its **validation basis**.

Something conceptually like:

```json
{
  "evidence_id": "ev-23",
  "defense_id": "TEMP-017:test-1",
  "oracle": "mutation",

  "basis": {
    "defense_assertion": "...hash...",
    "defense_artifacts": {
      "tests/metrics/test_temporal.py::test_subsecond_parse": "...hash..."
    },
    "subject_scope": {
      "scope": "metrics.temporal",
      "hash": "...hash..."
    },
    "environment": {
      "pyproject.toml": "...hash...",
      "uv.lock": "...hash..."
    }
  },

  "source_rev": "abc1234",
  "result": "fired"
}
```

Your current evidence record records **which scope** was validated and **which environment files matter**, but crucially not what their contents/fingerprints were when the oracle actually ran.

That's insufficient.

`verify` must fundamentally compare:

```text
current state
        versus
basis of accepted evidence
```

not:

```text
current state
        versus
last time somebody ran generate
```

The lock can still exist for:

* normalized resolution,
* indexes,
* cached identities,
* reproducibility,
* efficient diff traversal.

But **regenerating the lock must be incapable of changing whether evidence is entitled to its grade**.

I would promote that to a new explicit invariant:

> **An accepted defense is evaluated against the state its accepted evidence actually observed. Regenerating derived state never advances that basis.**

This is the one change I would make before anything else.

---

# P0 — not every existing evidence record is acceptable evidence

T16 presently establishes:

* immutable evidence ID;
* at most one binding;
* referenced record exists.

That's necessary, but not sufficient.

This could currently be structurally legal:

```json
Defense:
{
  "id": "TEMP-017:test-1",
  "guarded_by": "test",
  "accepted_evidence": "ev-99"
}

Evidence:
{
  "evidence_id": "ev-99",
  "defense_id": "SOME-OTHER-DEFENSE",
  "oracle": "compiler",
  "result": "could_not_look"
}
```

There are several compatibility conditions missing.

An accepted evidence record must at least satisfy:

```text
evidence.defense_id == defense.id

oracle is compatible with guarded_by

evidence result is admissible as supporting evidence

validated_subject_scope is broad enough for subject_scope

evidence basis corresponds to the assertion/tree it claims to validate
```

T5 already owns the fourth condition.

The others belong around T16.

### Particularly important: `could_not_look`

The mutation runner correctly distinguishes:

```text
fired
did_not_fire
could_not_look
```

and explicitly says failure to run is never scored as fired.

But nothing currently prevents a defense from binding a `could_not_look` record as its accepted evidence.

I would normalize producer output one level further:

```text
oracle_result: fired
evidence_verdict: supports | contradicts | could_not_establish
```

The checker stays ignorant of pytest/Rust/compiler semantics. Each evidence producer or adapter maps its native result to that small protocol.

Then:

> `accepted_evidence` MUST refer to a record whose normalized verdict supports the grade being asserted.

Otherwise it isn't an answered defense.

---

# P0 — acknowledged `unresolvable` contradicts T12

There is an exact internal contradiction in the exit-code section.

The general rule says:

> exit code is computed from gated **unacknowledged** findings.

And `0` means:

> no gated, unacknowledged finding.

Then `unresolvable`:

> cannot be un-gated ... until a person acknowledges it with a reason.

So:

```text
unresolvable
+ acknowledged
= no gated unacknowledged finding
= exit 0
```

But T12 immediately says:

> per-defense unresolvability ... is not 0.

Both cannot be implemented.

I think T12 is the right rule.

Acknowledgement should do exactly what the earlier section promises:

```text
unresolvable + new
unresolvable + acknowledged
```

Both remain `unresolvable`.

And **both exit 5**.

The acknowledgement changes only what the operator has already seen.

So make one explicit exception to the ordinary gate calculation:

```text
if any unresolvable:
    exit 5
else:
    highest consequence among gated + unacknowledged findings
```

Otherwise you have recreated "could not look → clean" after one human command, which is exactly the distinction the checker was designed to preserve.

---

# P1 — "new evidence exists" isn't yet a sound invalidation event

This is subtler.

Right now any newer evidence record for a defense makes the currently accepted record stale:

> `ev-31` appears → defense enters `review_required`.

And the accepted-evidence ground is actually defined over **the set of evidence records for the defense**, so appending any record moves it.

That is probably too coarse even by your conservative standard.

Suppose:

```text
ev-23: fired
```

is current and valid.

Someone reruns an experiment accidentally with a broken environment:

```text
ev-31: could_not_look
```

Nothing about the grounds supporting `ev-23` changed.

Why should `ev-23` cease to be valid?

Or somebody runs a different oracle over a different scope.

Or an exploratory run is appended.

The existence of more evidence is not itself analogous to the subject changing.

## You need evidence lineage

I'd add either:

```json
"supersedes": "ev-23"
```

or an evidence-series identity:

```json
"series": "TEMP-017:test-1/mutation/main"
```

plus a basis.

Then the checker can distinguish:

```text
another evidence record exists
```

from:

```text
a record explicitly intended to supersede the bound evidence exists
```

and:

```text
new valid evidence contradicts the accepted evidence
```

I would actually rename the facet event from:

> `new evidence available`

to:

> `accepted evidence superseded`

unless you intentionally want *every experiment* to invalidate accepted evidence.

That decision should be explicit.

---

# P1 — generated registers and human acceptance still clash

You've correctly restored generated registers:

> A's seven-minute survey script produces one; the checker fingerprints its inputs and never reruns it.

But evidence acceptance is also defined as:

> a **person changes `accepted_evidence`** in the register.

For a generated register:

```text
survey.py → obligations.register.json
```

a human edits:

```text
accepted_evidence = ev-31
```

then the next legitimate survey regeneration may simply overwrite that decision.

Worse, your provenance check fingerprints the **producer inputs**, so it cannot detect that the generated output has been manually edited away from what the producer would emit.

You need to say where human decisions live for a generated register.

Two defensible solutions:

**A. Cleaner:** acceptance bindings are a separate human-owned overlay.

```text
obligations.register.json       generated or manual
obligations.bindings.json       human judgment
```

**B. Fewer files:** a generated register's producer MUST consume a human-owned binding/decision input and round-trip those bindings unchanged.

I prefer A architecturally, although I appreciate that it adds a sixth committed artifact.

What I would not leave unspecified is "generated file which humans also edit."

---

# P1 — one old-schema sentence survived

`validate` still says it checks:

> "per-status counts reconciling with the entry total"

But the new model deliberately has no stored validity status. A defense is merely:

```text
answered = accepted_evidence exists
open     = otherwise
```

So this looks like residue from the old schema.

Delete the per-status-count check unless there is some other status catalogue not described in the ontology.

---

# P1 — migration must never "manufacture" evidence

The migration section says an old `status: answered` entry has no evidence link, so migration must:

> "manufacture one or leave the defense open."

The first option violates your strongest new principle:

> evidence is recorded; it may not impersonate something that was never produced.

Migration cannot manufacture evidence.

The rule should simply be:

> An old answered defense without a deterministically identifiable real evidence record migrates to **open**, with a migration diagnostic explaining why.

That is conservative and honest.

---

# P1 — register-level findings don't fit the `Finding` ontology

You now have:

```text
Register provenance moved
→ review_required (register-level)
```

which is sensible.

But `Finding` is defined as:

```text
Finding
    defense_id, facet, consequence, acknowledgement
```

so a register-level finding has nowhere to live.

Make the subject explicit:

```text
Finding
    subject
    facet
    consequence
    acknowledgement

subject =
    defense:<id>
  | register
```

Potentially later:

```text
producer:<id>
run
```

but V1 only needs `defense | register`.

---

# P1 — `subject_scope` exists twice without a relationship

The ontology has:

```text
Promise
    id, text, subject_scope

DefenseAssertion
    ...
    subject_scope
```

That might be intentional, but the invariant is unstated.

At minimum:

```text
defense.subject_scope ⊆ promise.subject_scope
```

should probably be structurally validated.

Otherwise this is legal:

```text
Promise:
    promise about parser/

Defense:
    subject_scope = billing/
```

with perfectly good mutation evidence over `billing/`.

T5 says the evidence supports the defense's claimed precision, but nobody checks that the defense's claimed subject has anything to do with the promise's declared subject.

I would not force equality because a broad promise may have several defenses over subscopes.

Containment is enough for V1.

---

# Two wording fixes

These are small but worth doing because this is normative prose.

The "Two traversals" section still describes promise-first as:

> **"Is this claim still defended?"**

But T1 explicitly says the checker cannot answer that without composition semantics.

Change it to:

> **Promise first:** Which recorded defenses of this promise are still current?

And `accepted evidence` is now being used for two different concepts:

1. the bound evidence record;
2. the "accepted evidence ground," currently the set of all records.

I would rename the latter. Once supersession is modeled, the grounds become much clearer anyway.

---

# The deeper correction I would make to the model

With the first issue fixed, I think the ontology becomes:

```text
Promise
    judgment

DefenseAssertion
    judgment

EvidenceRecord
    immutable observation
    + validation basis

EvidenceBinding
    human acceptance decision
    defense → evidence

CurrentObservation
    derived from current tree

Validity
    compare(CurrentObservation, EvidenceRecord.basis)

Acknowledgement
    human knowledge of a finding

Lock
    cache / normalized resolution / indexes
    NEVER the authority for evidence applicability
```

That gives a very clean causal chain:

```text
oracle ran
    ↓
EvidenceRecord records exactly what it saw
    ↓
human binds that evidence to a defense
    ↓
checker compares today's state with what that evidence saw
    ↓
Validity
    ↓
finding may be acknowledged
```

And crucially:

```text
generate
```

occurs nowhere in that chain of truth.

It can be deleted and recreated freely without changing whether a defense is valid.

**That is the property I would test first in the checker itself.**

---

## What can genuinely remain open after this

The existing open problems around:

* granularity vs review capacity,
* whether gaps eventually need `revisit_on`,
* fleet cardinality/churn measurements,

really can remain open. The document is right that deployment should answer them rather than more armchair design.

The hashing document is also correctly identified as **unfinished implementation specification**, not another ontology problem. It needs to exist before conformance means much, but you already know exactly why.

So I would do **one more revision before coding**, centered on:

1. move accepted-ground authority from lock → evidence validation basis;
2. define admissible/compatible evidence binding;
3. resolve acknowledged `unresolvable`;
4. define evidence supersession rather than "any newer record";
5. resolve generated-register vs human-binding ownership;
6. clean the five smaller schema remnants above.

After that, I think continuing to design instead of shipping the fleet V1 would start becoming the error the document itself warns against.

<!-- /prose-gate:ignore -->
