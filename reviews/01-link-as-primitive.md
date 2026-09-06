# The unit of state is the link between a promise and its evidence

An outside review from a language model. The maintainer obtained it on partial context on 2026-09-05, and the text below is verbatim. It reviewed the checker as the conversation had described it, before anyone drafted `CHECKER.md`.

## Taken

- The link between a promise and its evidence as the unit of state.
- Observed events kept apart from what they mean for a grade, with the grade decided conservatively.
- A record of what a grade relied on. The design renamed it grounds and later moved it into the evidence record.
- Two ways to traverse: from a promise, and from a diff.
- Counting links rather than capping them, and review load as churn times fan-out times how easily a grade is undone.
- The governing aim: keep silent stale grades to a minimum, within the time people have to review.
- Time to triage kept separate from time to re-check.
- History never on the routine path.
- `fresh` as a view over other checks rather than a mechanism of its own.
- A boundary drawn on meaning rather than on bytes.
- The fleet as the instrument that measures the design.

## Pushed back on, or extended

- The accepted gap had no place in the model. It is now a `GapAssertion` outside the grade states.
- Section 2's rule that a declared scope cannot be finer than the evidence, and section 7's limit on review time, pull against each other. `CHECKER.md` resolves it: the fix belongs to the oracle rather than the tracker.
- The four-hash record of grounds had no environment part. The design later gained one, then made it declarative.
- "Exact rename detected, identity probably preserved" smuggles in the judgment section 3 forbids.
- The naming discussion was set aside.

---

<!-- prose-gate:ignore -->

Yes. This is the point where the design becomes much sharper.

The key conceptual correction is:

> **The checker does not track artifacts. It tracks the continued validity of assertions relating a promise to evidence.**

Artifacts and Git changes are merely signals that can invalidate those assertions.

That sounds like a wording change, but it changes the data model and the architecture.

## 1. The unit of state is the **link**, not the obligation or artifact

I would make the primitive something like:

```text
Promise
   │
   ├── defense assertion ──> Test T
   │                         validated by mutation M
   │
   ├── defense assertion ──> Type declaration D
   │                         validated by compiler
   │
   └── accepted gap
```

Each defense assertion has its **own validity state**.

That matters when one promise has:

* three tests,
* one type guarantee,
* one accepted hole,

and only one of them has gone stale.

You don't want:

```json
"status": "stale"
```

on the obligation.

You want something closer to:

```json
{
  "promise_id": "TEMporal-017",
  "defense_id": "TEMporal-017:test:subsecond",
  "guarded_by": "test",
  "artifact": "tests/test_temporal.py::test_subsecond_parse",
  "oracle": {
    "kind": "mutation",
    "scope": "metrics.temporal"
  }
}
```

The checker then answers:

> **Do I still have sufficient grounds to believe this defense assertion?**

---

## 2. I would change one sentence in your analysis

This:

> each branch has a different natural granularity, set by its oracle

is almost right.

I'd make it:

> **Each defense assertion has a maximum meaningful precision set by the oracle that validated it.**

Because `guarded_by: test` does not inherently imply module granularity.

A mutation campaign *might* have established:

```text
test X catches mutation Y at expression Z
```

or it might only establish:

```text
this test set kills the relevant mutants in module M
```

The checker shouldn't invent finer precision than the validation evidence supports.

So:

```text
declared granularity ≤ validated granularity
```

If someone records:

```text
foo.rs:317-321
```

but the mutation evidence only ever validated `foo.rs` as a module, those line numbers are decorative precision.

That's something the checker can itself flag.

**`precision_exceeds_evidence`** would be a very good report facet.

---

## 3. The six kinds of "changed" shouldn't become six heuristics

I would resist making the checker clever about deciding:

> local rename → harmless
> assertion removal → harmful

That would quietly turn it into source analysis.

Instead separate:

### Observed event

```text
defense artifact modified
defense artifact missing
defense artifact relocated
subject artifact modified
promise modified
validation expired
```

from:

### Validity consequence

```text
still_valid
review_required
invalid
unresolvable
```

And make consequence intentionally conservative.

For example:

| Event                      | Checker can establish                        | Result                   |
| -------------------------- | -------------------------------------------- | ------------------------ |
| test unchanged             | exact evidence object remains                | possibly valid           |
| test changed               | something relevant *may* have changed        | review                   |
| test deleted               | asserted target gone                         | invalid                  |
| exact rename detected      | identity probably preserved                  | relocate, perhaps review |
| subject changed            | proof no longer covers current subject       | review                   |
| promise changed            | evidence established against different claim | review                   |
| oracle deadline elapsed    | evidence expired                             | review                   |
| target cannot be inspected | checker failed to know                       | unknown/error            |

Crucially:

> **The checker does not need to know whether a change was consequential in order to be correct.**

It only needs to refuse to silently preserve a grade where its grounds have changed.

That fits your cost asymmetry beautifully.

---

## 4. This suggests a much better model than `as_of`

The original:

```json
"as_of": "abc1234"
```

is indeed too impoverished.

The baseline needs to say **what exactly was relied upon when the link was accepted**.

Conceptually:

```json
{
  "defense_id": "TEMP-017:test-1",

  "promise": "TEMP-017",

  "defense": {
    "kind": "test",
    "locator": "tests/test_temporal.py::test_subsecond_parse"
  },

  "validation": {
    "oracle": "mutation",
    "scope": "metrics.temporal",
    "result": "caught"
  },

  "baseline": {
    "promise": "...hash...",
    "defense_artifact": "...hash...",
    "subject_scope": "...hash...",
    "oracle_record": "...hash..."
  }
}
```

Not necessarily this literal schema, but this ontology.

Now the checker can say:

```text
TEMP-017:test-1

promise             unchanged
defense artifact    unchanged
subject scope        changed
oracle record        unchanged

=> REVIEW REQUIRED
   validation predates subject change
```

Much more useful than:

```text
stale: true
```

---

# 5. Your two-index observation should become an architectural requirement

Absolutely.

You need the logical equivalents of:

```text
promise → defenses → dependent artifacts
```

and:

```text
artifact → affected defense assertions → promises
```

Those support fundamentally different workflows.

### Obligation-first

```bash
tool status TEMP-017
```

> Is my claim still defended?

### Diff-first

```bash
tool affected HEAD~1..HEAD
```

> I changed these twelve things. Which accepted claims might now require revalidation?

The second is probably the everyday command once deployed across a fleet.

And with your cardinalities, **do not construct this by repeatedly scanning the register**. The lock/baseline should materialize the reverse index.

The register remains canonical; the lock can contain derived structures.

---

## 6. Cardinality should be measured, not "fixed"

I now agree with your reversal on the 100-obligations-per-file observation.

`103` links from one file is not, by itself, pathology.

It could mean:

1. terrible coarse linking; or
2. one central parser/compiler/schema genuinely participates in 103 promises.

Those require opposite responses.

I wouldn't add a rule like:

```text
max_obligations_per_artifact = 20
```

I would report structural metrics:

```text
outdegree artifact → assertions
indegree promise → artifacts
fanout after typical diff
review queue generated per commit
median / p90 / p99 queue size
```

Those are enormously more useful.

The important metric isn't even cardinality alone.

It is approximately:

```text
review load
    = artifact churn
    × dependency fanout
    × invalidation sensitivity
```

A file referenced by 100 promises but changed once every two years is cheap.

A generated schema touched every commit and referenced by 30 promises is expensive.

---

# 7. Which means you found the actual optimization target

Not:

> minimize false-positive stale flags

but:

> **maximize soundness subject to review capacity.**

Or even more concretely:

```text
minimize silent stale assertions
subject to:
    review_queue ≤ operational capacity
```

That's quite a good governing principle for the project.

And because false negatives are durable while false positives self-heal, the sensible default is indeed conservative invalidation.

I would state this normatively in the spec:

> **When the checker cannot establish that previously validated evidence still applies, it MUST NOT preserve the prior validation merely to reduce review volume.**

That prevents future contributors from "improving" it into unsoundness.

---

# 8. One thing I would not bake in: "agent = hundreds"

Your broader conclusion survives, but this should remain an empirical variable.

An agent may *process* hundreds of candidates.

It doesn't necessarily mean it can correctly **revalidate hundreds of semantic promise/evidence relationships** without escalating them.

So distinguish:

```text
queue triage capacity
```

from:

```text
validation capacity
```

An agent can cheaply reduce:

```text
327 invalidations
```

to perhaps:

```text
281 obviously preserved relocations
31 mechanically revalidated
15 need semantic review
```

That is a huge win.

But those final 15 may still be the real throughput limit.

So fleet instrumentation should measure at least:

```text
generated
auto-resolved
agent-reviewed
human-reviewed
accepted
rejected
time-to-clear
```

Then you will actually know.

---

# 9. The `git log -L` result is more important than it looks

It doesn't merely rule out one implementation technique.

It says:

> **Reconstructing fine-grained identity retrospectively from Git history cannot be in the hot path.**

That's a strong architectural constraint.

The tool should maintain state prospectively:

```text
known locator
known content fingerprint
known containing artifact
known validation scope
known commit/tree
```

and compare snapshots.

History can be an optional diagnostic tool, never required for routine validity checking.

This is another argument for the boundver-style committed lock.

---

# 10. I think `fresh` is no longer really a separate conceptual feature

Earlier we had:

```text
verify
fresh
mutants
```

But underneath, they're all the same operation.

They ask:

> **Has something changed that invalidates the grounds on which an assertion was accepted?**

For generated evidence:

```text
inputs changed → generated result potentially expired
```

For mutation evidence:

```text
subject changed → mutation grade potentially expired
```

For test location:

```text
defense target disappeared → assertion broken
```

So `fresh` may remain a convenient CLI command, but the **engine should have one invalidation model**.

Something like:

```text
Assertion
Validation
Dependencies
Baseline
Invalidation
```

Then `fresh` is just a projection over assertions whose oracle is generation/freshness.

---

# 11. This also preserves your original scope boundary

Importantly, none of this requires the tool to discover promises.

And it need not understand Python, Rust, JavaScript, etc.

It can know:

```text
this declared scope changed
```

without knowing:

```text
what this function means
```

That distinction should be explicit:

> **The checker may inspect declared artifacts to establish identity, presence and change. It does not inspect them to infer obligations, defenses, or semantic consequences.**

That's a better formulation than the absolute:

> "It does not read source."

because once you hash or locate source scopes, literally speaking it *does* consume source bytes.

The semantic prohibition is what you actually care about.

---

# 12. Fleet adoption now makes sense immediately

And not mainly because four copies are wasteful.

You found a considerably stronger justification:

> **The fleet is the measurement apparatus for designing the checker.**

Deploy the deliberately conservative/simple form first and collect:

```text
per repository:
    number of promises
    number of defense assertions
    promise ↔ artifact degree distributions
    linked-artifact churn
    invalidations / commit
    invalidations / week
    invalidations by event kind
    auto-resolved fraction
    queue age
    revalidation disposition
    oracle/granularity distribution
```

Then the question:

> "Do we need symbol/range-level identity?"

becomes answerable.

If conservative file-level invalidation generates 500 candidates but agents reduce 490 mechanically, **don't build fine-grained tracking**.

If 40 highly-churned files generate 90% of unresolved work, then selectively introduce finer locators there.

That is a much better evolutionary path than designing the perfect granularity system in advance.

---

## The design principle I would now put near the top of V2

I think you've uncovered something strong enough to promote to first-class doctrine:

> **A register does not claim that an artifact exists. It claims that evidence supports a promise. The checker preserves that claim only while the grounds on which it was accepted remain intact. Changes are invalidation signals, not judgments about meaning.**
>
> **When those grounds change, the cheap error is to ask for review. The expensive error is to silently preserve a claim that may no longer be true.**

And that gives the tool an even cleaner one-sentence description than we had before:

> **It checks whether the evidence recorded for each promise is still entitled to its grade.**

Still no survey.
Still no obligation discovery.
Still no code reasoning.
Still no testing framework.

But the internal model is now substantially more rigorous than **"hash the files and see what moved."**

Also: this makes **Promisebook** somewhat less attractive to me than it was one turn ago. The central object is not really a book *of promises*; it is a **register of claims about their defenses**. Before settling the name, I would now search the vocabulary around **register / attestation / warrant / assurance / evidence / defense**, because the ontology you've just exposed gives us a much better naming target.

<!-- /prose-gate:ignore -->
