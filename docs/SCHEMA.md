# Version 0.1 separates claims, observations, and acceptance

Readers are engineers producing or consuming Upheld JSON. The schemas under [schemas/0.1](../schemas/0.1/) define record shape. They check fields and types. They cannot decide whether evidence still applies.

This is the first published wire version, dated 6 September 2026. A breaking change requires a new schema version. Hashing is still unresolved; a structurally valid hash string establishes no agreed hash semantics.

## Each file has one writer

| File | Writer | Contents |
|---|---|---|
| register | Survey producer or person | Promises, nested defenses, optional gaps, producer inputs |
| config | Person | Gate choices, schema/hash/resolver versions, adapter declarations |
| evidence, one JSON object per line | Oracle producer | Immutable observation with basis and execution context |
| bindings | Person | Defense ID to accepted evidence ID |
| lock, when implemented | generate | Disposable cached resolutions and indexes |
| baseline, when implemented | ack | Finding fingerprint, reason, actor, and time |

This version publishes four input schemas and outputs for `validate`, `basis`, and `verify`. Lock and baseline formats remain deferred with their commands. Producers never write bindings.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) embeds records of these shapes under a named test profile. Its binding is explicitly simulated. Schema validation cannot establish human acceptance, producer trust, or agreed product hash behavior.

## The promise carries survey notes; each defense carries its kind

| Earlier field | Version 0.1 location | Rule |
|---|---|---|
| name | Promise text | Preserve the falsifiable claim |
| answered_by | Defense guarded_by | No default; accepted becomes a separate gap |
| satisfied_by | Defense locator plus evidence source_rev and basis | A named file cannot manufacture a record |
| status | Removed from promise | Binding presence defines answered; verify derives validity |
| source / published_in | Promise | Where the claim is made |
| subject_scope | Promise and defense | What code the claim concerns |
| confidence / detail | Promise | Reading confidence and quotation |
| evidence_tier | Promise | Read, unread_dependence, structural, fuzzy, or unknown |
| why / the_test_that_would_catch_it / next_step | Promise | Consequence, falsifier, unresolved question |
| needs_environment | Defense | Separate requirements for running it |
| reachability / armed_by | Promise | Latent requires an arming condition |
| last_actually_ran | Defense, derived from a cited run | Timestamp or explicit unknown; no boolean |

Each defense has an ID, promise ID, kind, locator, scope, reason for its kind, and environment needs. A promise without a defense or gap remains representable so `validate` can report `promise_without_defense_or_gap`.

A gap requires a reason. Actor and time may be unknown in imported records. Unknown authors remain visible. A gap creates no evidence. Additional survey notes use `metadata`; unknown top-level fields fail shape checks.

## Built-in kinds have explicit evidence checks

| guarded_by | Mechanism | Compatible oracle family |
|---|---|---|
| test | Chosen cases and asserted outcomes | mutation |
| property | Generated inputs checked against an oracle | mutation |
| checker | Rule over a declared surface | seeded_violation |
| ratchet | Rule over releases or recorded behavior | seeded_transition |
| type | Static guarantee makes the violation unrepresentable | compiler |
| runtime_invariant | Check or alarm during execution | fault_injection |

The `compiler` family names the type-defense adapter; compiler acceptance alone never supports a binding. Its oracle needs an independent authority. The `mutation` family also permits a replayed defect or injected fault under a justified model. Family names do not establish that an oracle is adequate.

A ratchet's seeded transition must show a forbidden change, an allowed change, and a failure to inspect. A runtime model check cannot use the compiler family merely because a model declares types.

An unfamiliar mechanism uses `x-` followed by its name and supplies `mechanism`. Configuration may declare its oracle and adapter. Naming an adapter does not install it. Before binding, the checker must confirm that it supports the declared pair. Otherwise it reports `unsupported_oracle`. Never fall back to test.

## Basis and execution context answer different questions

The basis records the hash profile, promise, defense assertion, artifact fingerprints, subject scope fingerprint, and declared environment files. Only tree inputs belong in the environment map.

Execution context records the producer's account of the run. Version 0.1 requires an explicit recorded or unknown state. An unknown state carries a reason. Recorded context includes command, time, duration, toolchain, target, configuration, dirty-tree account, and omissions. This shape leaves source capture and cross-machine scope to P01–P04; it does not certify reproducibility.

Supporting records must match the bound defense and oracle. The checker also checks fixed IDs, scope boundaries, profile support, and the order of records. Checking shape alone cannot establish those links.

## The probe format remains a preserved source

The heldtospec input uses `0.1-probe`, nested defenses, and an empty binding map. [Its compatibility schema](../schemas/0.1/probe-register.schema.json) validates that historical shape. It is distinct from the new format.

The [review-copy tool](../tools/prepare_probe_review.py) writes a version 0.1 candidate to a chosen new path. It rejects unsupported source versions and validates the source shape before writing. Producer inputs name the supplied source path. It retains IDs, claims, locators, gaps, and notes. It adds explicit unknown context. It never changes the original or creates evidence. The generated [review copy](../examples/heldtospec-contracts/review-register.json) remains unaccepted.

| Expected diagnostic | Count | Meaning |
|---|---:|---|
| promise_without_defense_or_gap | 4 | CTR-003, CTR-005, CTR-037, CTR-044 |
| artifact_resolution_unchecked | 78 | No target checkout or resolver run in this task |
| scope_containment_unchecked | 78 | Locators and scope strings have not established containment |
| supporting_evidence_absent | 78 | All defenses remain open |

The repository checks compare shape and counts against this table. They do not implement the full `validate` command. Migration from other older schemas remains T19 work.

## Schema checks reject two previously accepted contradictions

Timestamp fields require date-time strings or their already supported unknown state. A verify result with an unresolvable finding or positive unresolvable count requires exit 5. These corrections enforce the documented version 0.1 contract; they add no new record fields. Producers relying on the earlier permissive schemas must correct invalid records.

The example checks require the two current evidence files and empty bindings. Future examples may hold evidence. Full cross-record and output-count consistency checks remain C02 work.
