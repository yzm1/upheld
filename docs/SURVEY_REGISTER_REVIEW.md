# Canonical export preserves unknowns and existing files

Readers are engineers reviewing the new survey output. **The exporter fixes the missing path from saved source judgments to schema 0.1.** It leaves semantic review and enforcement discovery open.

## The design addresses the output gap

The old workflow stopped at candidate replies and a readable page. The new `register` command writes a file that passes the existing register schema. It preserves source quotes, conditions, and open questions. It reports unknown defenses without creating accepted gaps or evidence.

The trade is explicit: a schema-valid record can still contain a poor claim. The output calls every proposed promise suspected. Reading, code inspection, and a check of actual enforcement remain separate work.

## Adversarial cases now have explicit outcomes

| Challenge | Required outcome | Check |
|---|---|---|
| Matching quote with omitted limits | Retain the submitted limits in promise text | Qualifier export test |
| Parsed reply edited after import | Reject disagreement with the saved raw reply | Saved-input test |
| Ambiguous item | Keep a question without creating a promise | Ambiguity test |
| Two incompatible rewrites | Retain both as suspected claims | Conflict test |
| Missing file or partial reading | Retain the unresolved source and unread extent | Scope test |
| No valid reply | Fail without producing a register | Empty-run test |
| Reviewed reply with no claims | Retain the review record and unknown coverage | Zero-claim test |
| Existing human-edited output | Fail and preserve its bytes | Overwrite test |
| Repeated export | Produce the same bytes with the same inputs and exporter | Repeat test |
| Changed claim | Keep the old file intact; do not infer an ID match | Edited-claim test |
| Output or publish failure | Leave no partial output or temporary file | Failure test |

The [test file](../tests/test_survey_register.py) implements these cases. They establish narrow program behavior. They do not assess a model's claim quality or establish a defense grade.

## Replay no longer relabels an old response

A packet includes the collector's code hash. Editing the collector changes the packet ID even when source bytes stay the same. The old replay test expected equal IDs across that change. It now checks the unchanged source bytes and validates the saved reply against its original packet.

The workflow guide exports directly from the recorded run. A new packet needs a reply naming that packet. Historical source files and attempt records stay unchanged.

## Enforcement discovery and repeated-review merging remain open

The current reply format contains no actual or proposed defenses. Export therefore cannot claim to have searched for them. S06–S07 retain defense kinds and usable locators. S08 retains matching and reconciling edited claims. S02 and S14 retain live client and independent review checks.

Component ownership, cross-project references, and cycle support belong to S15–S17. [The agreed design](COMPONENT_REGISTER_DESIGN.md) records their source basis and acceptance cases. None of those tasks closes merely because this export passes a schema check.

## The local checks passed on 8 September 2026

The full repository suite passed 57 tests, including eleven new export tests. The recorded heldtospec run produced twelve suspected promises, zero ambiguity items, and zero defenses. The documentation checks compare that output with a fresh export and validate it against schema 0.1.

These are local checks of a recorded run. No live model call, defense probe, or accepted evidence record was produced by this change.
