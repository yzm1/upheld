# Compare current files with the evidence a person accepted

Readers are engineers implementing the checker. A defense assertion links a mechanism to a software promise. An evidence record holds an oracle run. A binding selects that record for one defense.

The product commands remain unbuilt. This revision keeps the 19 checker rules and four producer rules from the [original design](history/2026-09-06/CHECKER.md). Their strength and supporting defects remain unchanged.

**Compare current files to derive a result. Record what an oracle observed. Record when a person saw a finding.** None may replace another.

## Each defense keeps its own result

An open defense has no binding. An answered defense names one supporting record. Compare its current grounds with that record's basis: the fingerprints of the claim, defense, subject, and declared environment files.

| Facet | Observed event | Result |
|---|---|---|
| defense | Artifact changed or a relocation was detected | review_required |
| link | Artifact is missing | invalid |
| subject | Code covered by the evidence changed | review_required |
| promise | Promise or defense assertion changed | review_required |
| evidence | Bound record superseded, or later same-defense/same-oracle record contradicts it | review_required |
| environment | A declared tree input changed | review_required |
| provenance | A register producer's declared input changed | Register-level review_required |
| unresolvable | Target cannot be inspected | unresolvable |

No changed ground permits `still_valid`. Undetected relocation looks like a missing artifact. The checker checks whether targets exist, which targets they are, and their bytes; it does not decide whether a change matters semantically.

A gap records a choice to leave a promise undefended. It has no evidence grade. Promise reports give counts; they do not infer whole-promise adequacy from separate defenses.

## Scope describes what the oracle assessed

The artifact locator names the file or symbol containing the defense. Subject scope names the code the promise and defense concern. Validated subject scope names what the oracle actually assessed.

A defense's subject must lie within its promise's subject. It cannot claim narrower precision than the evidence supports. Do not compare artifact location with either subject. If broad evidence creates excessive review, rerun the oracle at a narrower scope.

## The evidence record owns its basis

The lock is a disposable cache. Deleting or regenerating it cannot advance an evidence record's grounds. The checker only reads evidence, the register, and bindings. It never reruns a producer.

Evidence records are immutable and append-only. A binding names one existing record for the same defense, with a compatible oracle and a `supports` verdict. A later inconclusive run alone does not invalidate it. A record that explicitly supersedes or contradicts it does.

Declared setup files use reproducible fingerprints. Runtime context belongs in a separate run field. The [schema](SCHEMA.md) reserves honest unknown values; P01–P04 in the todo list still owe the complete execution policy.

Hash profile v0.1 is not yet specified. Before implementation, settle working-tree semantics, path normalization, line endings, symlinks, ordering, claim serialization, missing/unreadable inputs, scope hashing, and versioning. Then publish executable agreement vectors.

## Commands separate structure, observation, and acknowledgment

| Command | Reads and reports | Writes |
|---|---|---|
| validate | All structural defects, bindings, compatibility, scopes; no tree or baseline | Nothing; may emit an unapplied migration patch |
| basis | One defense's grounds at the requested source | Output only |
| generate | Reproducible resolutions and indexes | Optional lock only |
| verify | Validated inputs, current tree, bound basis, lineage, provenance | Output only |
| affected | Diff between two endpoints and affected defenses | Output only |
| why | Grounds and records for one identifier; optional history | Output only |
| report | Defense states, open defenses, gaps, and affected promises | Output only |
| ack | One verify finding's fingerprint and reason | Baseline only |

Routine checks work without history or a lock. History in `why` may degrade to “history unavailable.” Migration never converts a legacy answered label into evidence; it emits a patch and diagnostic.

Every command needs a published output schema before release. Version 0.1 currently specifies outputs for `validate`, `basis`, and `verify`. The other commands remain deferred and may not claim conformance to T14 yet.

## Exit codes preserve failures to inspect

Validation exits 0 for valid structure, 1 for structural defects, or 2 for unreadable inputs. First check that the input structure is valid; structural defects retain exit 1.

| Verify exit | Meaning |
|---|---|
| 0 | No gated, new finding and no unresolvable target |
| 2 | Whole check cannot run |
| 3 | Gated, new review_required finding |
| 4 | Gated, new invalid finding |
| 5 | Any unresolvable target, even if acknowledged |

Exit 5 takes precedence over per-defense results. Otherwise use the highest consequence among gated, new findings. Recording that a person saw a finding changes whether it counts as new at the gate. Reports retain every finding and its current result. Structural defects cannot be acknowledged.

The config chooses gated facets, but always gates unresolvable. Environment and register provenance start as report-only. The full eight-facet report remains visible.

## Evidence producers execute the oracle

A companion runner obtains basis before seeding a fault. It records that basis verbatim, the fault, structured result, normalized verdict, and any superseded record. It restores the original tree on every exit path, preserving existing edits.

A failing process can mean detection, failure to collect tests, missing setup, or a crash. Only the adapter's structured result can distinguish them. The adapter reports `supports`, `contradicts`, or `could_not_establish`.

A mutation catalog entry names file, unique search text, replacement, exercised clause, boundary distance, and expected verdict. The counterexample should sit one representable unit outside the promised boundary. A distant fault only establishes a weaker smoke check.

## All 23 requirements retain their identifiers

The earlier T7, T10, and T11 numbers remain retired. The fourth column says how a reader detects a violation, compressed from the [source snapshot](history/2026-09-06/CHECKER.md), which also keeps the defect behind each MUST.

| ID | Strength | Rule | Detected by |
|---|---|---|---|
| T1 | SHOULD | Derive validity per defense. Promise views count states without inferring adequacy. | A stored status on a promise, or a report that calls a promise defended from a count. |
| T2 | MUST | A changed ground never maps to still_valid. | Any consequence path that reaches `still_valid` from a non-empty event set. |
| T3 | SHOULD | Consequences depend on the changed ground and resolution, never semantic interpretation. | A consequence rule that reads artifact bytes beyond identity, presence and hash. |
| T4 | SHOULD | Fingerprint claim, artifacts, subject, and declared environment separately with the named profile. Check lineage in the evidence log. | A stale report that cannot name the ground; an environment ground from outside the tree; an unknown profile. |
| T5 | SHOULD | Defense scope lies within its promise and claims no finer precision than validated scope. Locator is separate. | A defense scoped outside its promise, or finer than its evidence, passing `validate`. |
| T6 | MUST | Checker never edits register or bindings. Regenerating a clean-tree lock reproduces its bytes. | `generate` on a clean tree changes the lock; any command writes the register or bindings. |
| T8 | MUST | Every defense supplies guarded_by with no default. | An entry without `guarded_by` passing `validate`. |
| T9 | SHOULD | Validate lists all structural defects before exit. Verify requires valid inputs. Only ack writes a baseline. | `validate` stops at the first defect; a baseline appears after any command except `ack`. |
| T12 | MUST | Uninspectable targets never yield a clean exit, even after acknowledgment. Whole-run failure stays distinct. | A register naming a missing file exits 0, before or after `ack`. |
| T13 | SHOULD | Gate per facet; always gate unresolvable; report ungated facets. | Config can silence a facet, or un-gate `unresolvable`. |
| T14 | SHOULD | Every released command has a published output schema with finding facet and subject. | A released command without a schema, or a finding whose subject the output cannot tell apart. |
| T15 | MUST | Acknowledgment changes neither consequence nor visibility. It applies only to verify findings. | A finding missing from a report after `ack`, or changing consequence after `ack`. |
| T16 | SHOULD | Immutable evidence has identity, verdict, scope, producer, and basis. Bind only matching, compatible supports records. | A binding to an absent, foreign, incompatible or `could_not_establish` record passing `validate`. |
| T17 | SHOULD | Specify and version the hashing profile; producers share it. | Two implementations, or producer and checker, disagreeing on whether one defense drifted. |
| T18 | SHOULD | Generated registers name producer and inputs. Report input drift without rerunning the producer. | A generated register's inputs change and `verify` stays clean; any command runs a producer. |
| T19 | SHOULD | Emit an unapplied migration patch for old records. Never manufacture evidence. | An old register yielding a bare failure, a rewritten file, or a binding with no producer. |
| T20 | MUST | Compare with bound evidence basis. Regeneration never advances it. | Delete the lock, run `generate`, and any grade changes. Run this first. |
| T21 | SHOULD | Only explicit supersession or a later same-defense/same-oracle contradiction is an evidence event. | An inconclusive record putting a `supports`-bound defense into review. |
| T22 | SHOULD | No producer writes the bindings file. | Regenerating a register removes a binding. |
| R1 | MUST | Use structured results for fired, did_not_fire, and could_not_look; normalize them honestly. | A run that cannot start reporting `fired` or `supports`. |
| R2 | SHOULD | Restore the original tree on every exit path. | A dirty tree after a failed run. |
| R3 | SHOULD | Record and report the fault's distance from the clause boundary. | An entry with no stated distance running. |
| R4 | SHOULD | Obtain basis from the checker and name superseded evidence on a rerun. | A record with no basis, or a profile the config does not name. |

The first product test must demonstrate T20. The current documentation tools exercise record shape and a status check; they do not implement these commands.
