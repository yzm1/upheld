# Upheld — consolidated discussion-derived todo list

Prepared 2026-09-06 against `yzm1/upheld` main at `3cc993edf7810901ce285b013e18fc670e18919a`.

This is a planning deliverable: 64 tracked items, not a claim that their implementation is authorized, complete, or all required for the next milestone. It consolidates the supplied review with the current repository, including the concrete work the review refers to indirectly. No repository files or GitHub issues were changed. Historical heldtospec findings are carried forward for revalidation; its current code was not inspected in this task.

## How to use this list

- **P0:** settle before relying on the first checker evidence, or correct materially misleading status now.
- **P1:** next product-learning milestone; survey work and experiments should run alongside the minimal checker work.
- **P2:** follow-on or historical target-project remediation, after checking whether it remains necessary.
- **Later:** explicitly retained, with an admission condition rather than an implied immediate commitment.
- **New:** action proposed by the supplied discussion. **Existing:** already specified or explicitly pending in the repository. **Derived:** concrete work needed to make those proposals executable. These labels describe provenance, not approval.

All boxes are open work. Existing design decisions are listed separately below so they are not mistaken for absent architecture. A task can close with a documented decision not to implement a proposal, where the item explicitly calls for a decision.

Suggested order: D01–D03 and E01 first; S01–S10 plus E02–E04 as the main discovery track; D04–D07 and P01–P04 before C01–C10 produces trusted evidence; E05–E07 evaluate maintenance and generalization. D08 supplies a self-dogfooding case. H01–H19 belong to heldtospec follow-up. L01–L06 remain later work.

The discussion's suggested **60% survey/probes and real-project experiments, 30% minimal checker, 10% specification/status cleanup** is a proposed allocation, not measured optimal staffing. The aim is to prevent the large checker specification from determining the next milestone by default.

## Source key

Repository links below are pinned to the inspected snapshot. Requirement IDs and section titles provide finer traceability.

| Key | Source |
|---|---|
| DISC | Supplied `Pasted markdown(20260906-110530).md`, the full review beginning “I like Upheld quite a lot.” |
| README | [Repository README](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/README.md) |
| DEC | [Decisions](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/docs/DECISIONS.md) |
| METHOD | [Method](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/docs/METHOD.md) |
| CHECKER | [Checker specification](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/docs/CHECKER.md) |
| SURVEY | [Survey sketch](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/docs/SURVEY_TOOL.md) |
| EX | [Example report](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/examples/heldtospec-contracts/README.md) |
| REG | [44-promise register](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/examples/heldtospec-contracts/obligations.register.json) |
| TRIAGE | [Example triage](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/examples/heldtospec-contracts/triage.md) |
| EXAMPLES | [Example inventory](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/examples/README.md) |
| MEASURE | [Measurements](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/measurements/RESULTS.md) |
| REVIEW-0 | [Survey-agent implications](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/reviews/00-survey-agent-implications.md) |

## What is actually present

The repository contains design documents, four prior reviews, reference notes, a synthetic measurement script, and a hand-authored/script-serialized heldtospec register. It has no package scaffold or implemented Upheld command surface. GitHub issue search returned no issues.

The register contains **44 promises, 78 defenses, four promises with neither defense nor gap, four gaps, 17 promises with `next_step`, zero bindings, and zero evidence records**. The evidence file is zero bytes in the repository tree. Its absence of records is intentional.

The example report records **149 library tests passing** on heldtospec `7f9addc` with four uncommitted files. That is a historical execution report, not an Upheld conformance run or evidence that those tests can detect the promised failures. The register's survey provenance names `c8c9362`, a different revision. The CLI attempt did not complete. These limits must survive consolidation.

The triage report says 18 items, but contains **19 top-level finding bullets: five odd, six ambiguous, eight missing**. It also groups multiple promise IDs in some bullets. The register's 17 `next_step` entries are a different unit. The example describes four probes while the triage summary says five. These are reconciliation tasks, not numbers to normalize silently.

## D — Direction, status, and specification seams (8)

- [ ] **D01 · P0 · Existing + New — Correct the current-status documentation.** Update README status and reading order, EXAMPLES, SURVEY's “nothing tried”/“heldtospec has no register” statements, and the scope of MEASURE's “no real measurements” claims. Distinguish the hand survey, scripts, synthetic performance, historical execution, and unbuilt product. Preserve dated source snapshots where historical wording is intentional; annotate rather than silently rewriting history. **Done when:** current-facing status agrees with the committed artifacts and links to the real example. **Sources:** DISC “accidental dogfooding”; README; EXAMPLES; SURVEY; EX; MEASURE.

- [ ] **D02 · P1 · New — Decide and apply accurate product positioning.** Evaluate the proposed promise/evidence/re-establishment wording and “continuous assurance” description. Explain the survey, evidence producers, and checker as distinct pieces. **Done when:** the entry-point description clearly says what Upheld establishes, avoids implying proof of promise truth, and does not imply freshness alone guarantees adequacy. Exact slogan remains a choice. **Sources:** DISC “killer idea”; CHECKER “What it is”.

- [ ] **D03 · P1 · New — Make the next milestone a product-learning milestone.** Record the minimal end-to-end checker slice and the survey/probe workflow as its two deliverables, with the two-hour discovery trial and maintenance trial as evaluation gates. Make the effort allocation explicit and revisable. **Done when:** the milestone has observable outcomes and a scope boundary that excludes the deferred command surface. **Sources:** DISC “effort is inverted”, “What I would build now”, final allocation.

- [ ] **D04 · P0 · Existing — Reconcile METHOD with CHECKER and establish the document handoff.** Resolve obligation-level `status`/`satisfied_by`/`answered_by` versus defense assertions, bindings, and derived validity. Preserve useful survey metadata rather than dropping it during schema cleanup. Coordinate the documented handoff from heldtospec's evolving method snapshot and clarify which document is authoritative. **Done when:** field placement and terms agree, legacy fields have explicit mappings, and current normative text no longer depends on an unseen revision elsewhere. **Sources:** README Status; DEC “No move”; CHECKER Open problems; METHOD O1–O10.

- [ ] **D05 · P0 · Derived — Resolve taxonomy and oracle compatibility before freezing schemas.** METHOD describes seven groupings and an open vocabulary; SURVEY still uses a five-way framing; CHECKER's examples cover four defense kinds and separate accepted gaps. Preserve property and ratchet distinctions or explicitly justify a mapping; define how unfamiliar mechanisms are represented and validated without defaulting to test. Specify compatible evidence producers for each supported kind. **Done when:** a candidate classified as property, ratchet, runtime invariant, accepted gap, or unfamiliar mechanism has an honest end-to-end representation. **Sources:** METHOD “What answers an obligation”, O2/O9; SURVEY Ask; CHECKER T8/T16. This is an additional consolidation finding, not an explicitly named defect in DISC.

- [ ] **D06 · P0 · Existing + Derived — Publish versioned input/output schemas and a probe-format compatibility policy.** Cover register, config, bindings, evidence, and outputs for the first commands. Explicitly map the example's nested defenses and descriptive fields in `0.1-probe`. Do not assume “follows the ontology” means final-schema compliant. **Done when:** the example can be structurally assessed with specific diagnostics; format changes are reviewable and do not create evidence. **Depends on:** D04–D05, P01–P03. **Sources:** CHECKER T14/T16/T19; EX Schema decisions; REG.

- [ ] **D07 · P1 · Derived — Reconcile the survey's counts and observation provenance.** Give each triage finding and probe a stable identity; reconcile 18 versus 19 bullets, four versus five probes, 17 open next steps, and the revision difference between survey and test execution. Mark unresolved records as unknown. **Done when:** every published aggregate can be reproduced from identified records and the two revisions are explained or explicitly unresolved. **Sources:** TRIAGE; EX; REG. This task is necessary before treating the reported ratios as product evidence.

- [ ] **D08 · P1 · New + Existing — Preserve and dogfood the README-drift incident.** Add a dated case describing the obsolete “no register” claim after the example existed. Survey Upheld itself after the heldtospec workflow; include a falsifiable promise about repository-status accuracy, with its source, scope, candidate defense, and honest evidence state. **Done when:** the historical example is preserved and a repeatable defense can detect an intentionally reintroduced stale status claim. A human/editorial check is acceptable initially if labeled honestly. **Sources:** DISC dogfooding; DEC “No register for this repository”.

## S — Survey, cheap probes, and first use (10)

- [ ] **S01 · P1 · New — Add the survey's governing objective.** State: maximize useful newly discovered promises/defects subject to human triage capacity. Define useful, new, confirmed, and decision-required separately. **Done when:** the survey plan measures findings and attention cost rather than rewarding register size. **Depends on:** E01 for the operational protocol. **Sources:** DISC experiment; CHECKER governing objective.

- [ ] **S02 · P1 · Existing — Turn the hand survey into a repeatable scanner workflow.** Start with a component boundary and language-neutral sources: published docs, specifications, configuration/contract schemas, CLI help, and public API documentation. Emit falsifiable candidates with source locations, rationale, uncertainty, and next question. **Done when:** heldtospec's component can be rescanned by a documented procedure whose judgment and serialization steps are distinguishable. Do not credit `build_register.py` as an automated scanner. **Sources:** SURVEY Scan/What to build first; METHOD P1/O1–O6; EX Producer.

- [ ] **S03 · P1 · Existing + Derived — Add test/code sources and audit source-selection bias.** Mine test assertions for candidate promises/defenses, and inspect declarations, constraints, errors, and signatures through a first language adapter. Retain cross-file promises and do not infer adequate defense from a matching name. **Done when:** the survey records what each source adds and checks the documented undercount of shape/type-related promises. **Sources:** SURVEY Scan; EX distribution; DISC real-repository value.

- [ ] **S04 · P1 · Existing — Build skeptical triage with explicit uncertainty.** Separate confirmed problems, mechanically answerable questions, probe candidates, classification decisions, accepted gaps, and unresolved observations. Record why a gap claim was refuted rather than silently hiding it. **Done when:** the example queue has an auditable disposition per item and unknowns cannot be converted into verified coverage by a default. **Sources:** SURVEY Raise; TRIAGE. The historical skeptic's “default covered” instruction is study context, not a safe product truth rule.

- [ ] **S05 · P1 · New + Existing — Build the cheap-probe stage before investing heavily in a classifier.** Turn the example's documentation examples, boundary inputs, persistence round trips, and CLI exit checks into repeatable bounded probes. Record inputs, command, result, elapsed time, execution limitations, and linked candidates. **Done when:** the first queue can be mechanically reduced with a measured cost per resolved item. Findings about a promise remain distinct from evidence grading a defense. **Depends on:** P01–P04 for durable observation format. **Sources:** DISC effort inversion; TRIAGE conclusion; EX empty-evidence explanation.

- [ ] **S06 · P1 · Existing — Implement classification without a preselected defense.** Ask whether the promise ranges over the whole surface, chosen/generated inputs, time, static representability, or runtime, and whether an authorized person has accepted a gap. Keep missing-environment and deployment-reachability facts separate from mechanism. **Done when:** the interface cannot silently turn uncertainty, unavailable infrastructure, or every new row into `test`. **Depends on:** D05. **Sources:** SURVEY Ask; METHOD O2/O9/O10; CHECKER T8.

- [ ] **S07 · P1 · Existing — Define document-to-subject mapping and usable locators.** Preserve where a promise is made separately from what code it concerns. For `path::function` locators whose class was not confirmed, either resolve the full identifier or report the limitation. Decide an honest initial scope/resolver precision and ask for human judgment where needed. **Done when:** supported locators resolve deterministically and scope containment can be checked without pretending the artifact locator is subject scope. **Sources:** SURVEY final open question; EX Schema decisions; CHECKER T5/T17.

- [ ] **S08 · P1 · Existing + Derived — Make register generation preserve human decisions.** Define stable candidate/promise/defense identities, how reviewed classifications and gaps survive rescans, and who writes each artifact. Declare generator identity and inputs; maintain bindings separately. **Done when:** a second survey run retains reviewed decisions or surfaces an explicit conflict, leaves bindings intact, and never emits accepted evidence merely because it found a defense. **Sources:** SURVEY producer boundary; CHECKER T6/T18/T22; DISC progressive internal model. Human review persistence beyond bindings is a derived implementation need.

- [ ] **S09 · P1 · New — Deliver a one-command first-use path.** Provide the proposed `upheld survey` experience or a documented prototype equivalent that discovers candidates, runs appropriate cheap probes, and emits a readable triage artifact. Manufacture required internal structure progressively; show missing prerequisites as actionable steps. **Done when:** a first-time engineer can reach a useful finding without manually authoring six ontology files. Counts distinguish candidates, unbound defenses, findings, and confirmed evidence; the review's sample “104 well supported” is illustrative, not a valid evidence claim. **Sources:** DISC onboarding; SURVEY open questions.

- [ ] **S10 · P1 · New + Existing — Choose the minimum review surface and measure its usability.** Start with a readable file plus structured records if adequate; decide file versus CLI/review UI based on observed friction. Expose the source, observation, unresolved question, and next action; measure time to first finding and human review minutes. **Done when:** a new user can resolve a triage item and resume a rescan without understanding the whole checker ontology. **Sources:** SURVEY triage open question; DISC onboarding/experiment. A hosted application is not implied.

## P — Execution provenance distinct from tree basis (4)

- [ ] **P01 · P0 · New — Specify an execution-provenance object or equivalent linked run record.** Decide mandatory versus optional fields for source revision and dirty-tree identity, exact command, producer/tool versions, toolchain, target, configuration/feature flags, exercised scope, result, omissions, and run timestamp/duration. **Done when:** the recorded observation can be identified beyond a Git SHA and absent fields have explicit meaning. **Sources:** DISC provenance seam; REVIEW-0; METHOD V3. The review proposes an object, not a settled schema.

- [ ] **P02 · P0 · New — Define what `verify` can and cannot establish about runtime context.** Keep T4's recomputable tree inputs distinct from producer-recorded execution context. Explain how unpinned interpreter/compiler versions, flags, or environment can limit applicability, and when a declared tree input should pin them. **Done when:** “tree basis unchanged” does not imply an independently checked execution environment, and cross-machine comparisons follow a documented policy. **Sources:** DISC same-SHA scenario; CHECKER T4/T17.

- [ ] **P03 · P0 · Derived — Reconcile dirty-tree capture with the actual oracle observation.** Define `basis --source` behavior for a commit versus a working tree, tracked/untracked relevant inputs, and source changes during a run. Ensure the recorded basis describes the intended original defense/subject and the seeded change is recorded separately. **Done when:** two dirty trees at the same SHA are distinguishable, and a run cannot attach clean-commit grounds to dirty source it actually observed. **Depends on:** P01–P02; informs C01/C03/C04. **Sources:** DISC provenance example; EX four dirty files; CHECKER R4/T17.

- [ ] **P04 · P1 · Existing + New — Record actual execution and omissions without upgrading their meaning.** Capture `last_actually_ran` from run records, including skipped, absent, timed-out, and unavailable work. Preserve the library/CLI split and dbt execution in the example. **Done when:** a declared workflow, a passing suite, and a completed adequacy oracle are three distinguishable facts in reports. **Sources:** METHOD V3; TRIAGE last_actually_ran; EX execution and empty evidence.

## C — Minimal trustworthy checker vertical slice (10)

- [ ] **C01 · P0 · Existing + New — Write hashing profile v0.1 and executable conformance vectors.** Settle tree/working-tree semantics, path normalization, line endings, symlinks, collection order, canonical claim/assertion serialization, missing versus unreadable inputs, range/symbol handling or explicit lack of support, and profile versioning. Build the tiny implementation needed to test the specification. **Done when:** producer and verifier paths agree on canonical fixtures and the vectors expose disagreements rather than merely repeat one helper's output. **Depends on:** D06, P02–P03. **Sources:** CHECKER T17; DISC vertical slice 1.

- [ ] **C02 · P0 · Existing + New — Implement `validate` and run it on the real 44-promise register.** Enumerate structural defects, required fields/no default kind, identifier/reference and binding admissibility, scope containment, and precision claims. Publish output and exit behavior. **Done when:** malformed fixtures yield all applicable diagnostics and the real example is honestly reported. In particular CTR-003/005/037/044 have neither defense nor gap and should be findings under the existing specification; do not force a clean exit by inventing acceptance. **Depends on:** D05–D06. **Sources:** CHECKER T5/T8/T9/T14/T16; DISC vertical slice 2; REG summary.

- [ ] **C03 · P0 · Existing + New — Implement `basis` for the first supported source/scope profile.** Compute the claim, defense assertion, artifact, subject, and declared environment grounds independently and include the named profile. **Done when:** a producer invokes the command and carries its output verbatim, with unsupported/unreadable inputs reported honestly. **Depends on:** C01–C02. **Sources:** CHECKER T4/T17/R4; DISC vertical slice 3.

- [ ] **C04 · P1 · Existing + New — Build one tiny evidence producer and its structured adapter.** Choose one seeded violation or mutation with a known defense and a boundary-adjacent counterexample. Distinguish fired, did-not-fire, and could-not-look from structured execution results; do not treat every nonzero exit as a caught defect. Restore the original tree on errors and interruption without discarding pre-existing user edits. **Done when:** real detection, survival, startup/collection failure, and cleanup each demonstrate the correct behavior. **Depends on:** C03, P01–P04. **Sources:** CHECKER R1–R4; DISC vertical slice 4. The full companion runner is L05.

- [ ] **C05 · P1 · New + Existing — Produce the first real immutable EvidenceRecord.** Record the actual oracle outcome, identity, defense, validated scope, basis, execution provenance, and lineage if applicable. Keep failed/inconclusive observations honest. **Done when:** an append-only record from C04 exists and validates; it is not reconstructed from the historical 149-pass run. **Depends on:** C04. **Sources:** CHECKER T16/R4; DISC vertical slice 5.

- [ ] **C06 · P1 · New + Existing — Demonstrate explicit evidence binding.** Have a reviewer select the matching compatible `supports` record in the separate binding artifact. Explain what is being accepted and retain the unbound/open state elsewhere. **Done when:** the checker consumes a valid binding, rejects mismatched/inconclusive records, and neither scanner nor producer silently writes acceptance. **Depends on:** C05. **Sources:** CHECKER T16/T22; DISC vertical slice 6.

- [ ] **C07 · P1 · Existing + New — Implement the minimal `verify` path and honest output.** Validate inputs first, recompute grounds against the bound record, retain per-defense results, and distinguish changed, missing, and uninspectable targets. Implement the applicable facet/exit rules, including whole-run failure versus per-defense unresolvability. Report gaps and open defenses separately; no promise-level adequacy inferred from counts. **Done when:** unchanged grounds produce the expected result and all implemented finding classes have structured output. **Depends on:** C06. **Sources:** CHECKER T1–T4/T9/T12–T14/T20; DISC vertical slice 7. State unsupported later behavior explicitly rather than claiming full conformance.

- [ ] **C08 · P1 · New + Existing — Demonstrate invalidation and evidence-lineage behavior.** Change the test, subject source, promise text, defense assertion, and declared environment input separately. Delete an artifact; exercise an uninspectable target. Append superseding and contradicting records, and an unrelated/inconclusive observation. **Done when:** moved grounds never produce `still_valid`; lineage invalidates only as specified; unrelated inconclusive observations do not automatically invalidate a supporting binding. **Depends on:** C07. **Sources:** CHECKER T2/T4/T12/T21; DISC vertical slice 8.

- [ ] **C09 · P0 release gate · New + Existing — Prove regeneration cannot restore validity.** After C08 makes a defense stale, delete/rebuild disposable state and rescan/regenerate supported generated artifacts without a new oracle or changed binding. Preserve register semantics when testing cache invariance; a changed claim is itself a changed ground. **Done when:** no stale defense becomes current, binding decisions survive, and any cache that is implemented is reproducible. Start with this acceptance test before implementing caching. **Depends on:** C07–C08. **Sources:** CHECKER T6/T20/T22; DISC vertical slice 9.

- [ ] **C10 · P1 · Derived — Package the reproducible demonstration and score its conformance honestly.** Add only the scaffold, CLI entry points, fixtures, and execution job needed for validate → basis → producer → record → binding → verify → drift → regeneration. Use the supplied example with known diagnostics plus a legitimate minimal valid fixture where necessary. **Done when:** another engineer can reproduce it, a run record exists, and the CHECKER conformance table distinguishes passed, unsupported, and deferred requirements. **Depends on:** C02–C09. **Sources:** DEC Language/no scaffold; CHECKER Conformance; DISC vertical slice. Publishing a package is not required to complete this demonstration.

## E — Independent experiments and product measurements (7)

- [ ] **E01 · P1 · New + Existing — Pre-register the evaluation protocol.** Define the two-hour discovery test, what counts as a novel useful finding, how truth is adjudicated, review-cost accounting, and what result would falsify the product hypothesis. Record predictions and decisive/arguable cases before seeing outcomes. **Done when:** discovery yield, error rates, and human effort cannot be redefined after the run to flatter it. **Sources:** DISC experiment; REVIEW-0 pre-registration; METHOD “Predict the oracle”.

- [ ] **E02 · P1 · New — Select two independent pilot targets.** Choose an ordinary moderately mature OSS project outside Upheld's ancestry and a second target in a substantially different language/ecosystem. Record selection reasons, component boundaries, revisions, and environmental requirements. **Done when:** the pair challenges both shared development habits and language assumptions; no claim of universality follows from two examples. **Sources:** DISC monocultural evidence concern.

- [ ] **E03 · P1 · New — Run the two-hour discovery experiment on both targets.** Have a competent engineer unfamiliar with the codebase use the prototype; record prior knowledge, time to first finding, unique confirmed findings, useful newly articulated promises, false/duplicate claims, automatic/probe resolution, and human minutes per useful finding. **Done when:** the findings have evidence and the denominators include unsuccessful triage effort. **Depends on:** E01–E02 and usable S02–S10; a fully implemented checker is not a prerequisite. **Sources:** DISC experiment and survey priority.

- [ ] **E04 · P1 · Existing + Derived — Evaluate classifier choices with matched instruments.** If accessible, use A's 1,578 classified obligations and B's 620/blind reclassification; preserve private data boundaries and document access limitations. Compare questions, rules, and model assistance on a shared taxonomy, with item-level judgments, abstention, confusion patterns, and review cost. **Done when:** a chosen method outperforms a relevant baseline or its limits are stated. Matching A's distribution alone is insufficient; METHOD already warns that A/B instruments differ. **Depends on:** D05/S06/E01. **Sources:** SURVEY Ask; EXAMPLES; METHOD distribution discussion. No private corpus publication is implied.

- [ ] **E05 · P1 · New — Run the maintenance follow-up after real development.** Revisit original evidence after roughly a month of activity; a historical replay may pilot the protocol but must be labeled as such. Adjudicate correct reassessment, missed stale assertions, needless reviews, and human work. **Done when:** maintenance burden is measured against actual changed grounds and oracle reassessment, not simply “number of hashes changed.” **Depends on:** E03 and an operational C07. **Sources:** DISC follow-up experiment.

- [ ] **E06 · P1 · Existing + New — Measure granularity, fanout, and review capacity.** Collect promise/defense counts, degree in both directions, artifact churn, invalidations by event/commit/week, auto-resolved versus semantic-review fractions, queue age, and time to clear. Identify high-churn/high-fanout sources of unresolved work. **Done when:** evidence supports a decision about finer oracle scopes; do not narrow tracking below validated precision to reduce counts. **Depends on:** E05; can start instrumentation earlier. **Sources:** CHECKER deployment metrics/T5/governing objective; MEASURE; DISC maintenance burden.

- [ ] **E07 · P1 · New + Derived — Feed results back into the method and milestone.** Record unfamiliar defense mechanisms, scope assumptions that failed, source-coverage gaps, probe yield, onboarding friction, and costs. Keep repository-specific findings attributed; promote requirements according to the method's evidence-strength rule. **Done when:** the next roadmap explicitly says what to keep, change, defer, or stop based on the pilots. **Depends on:** E03–E06. **Sources:** DISC different-ecosystem trial and resist new checker features; METHOD requirement-strength discipline.

## H — Concrete heldtospec follow-ups recovered from the example (19)

These are **historical, not reverified-current defects**. Begin each by checking the target revision now in use and any landed fix. Close only with current evidence or a documented decision. Prepare any upstream report as a draft unless sending it is separately authorized. Preserve the original survey as a dated observation.

- [ ] **H01 · P2 · Existing — CTR-005: align public contract documentation with implementation.** Recheck `references` enforcement and cover `references`, `--reference`, `--strict`, and `accepted:` accurately. **Done when:** the documented behavior agrees with current executable behavior and the relevant documentation is checked. **Sources:** REG CTR-005; EX finding 2; TRIAGE Missing.

- [ ] **H02 · P2 · Existing — CTR-044: repair and execute the published example.** Decide whether `created_at` belongs in the schema or the freshness clause should be removed, according to intended behavior. **Done when:** the copied example passes its intended witness and a regression check executes it. **Sources:** REG CTR-044; EX finding 1.

- [ ] **H03 · P2 · Existing — CTR-019: decide ungradeable-clause exit semantics.** Implement the documented exit-4 rule or correct the contract and docstring deliberately. **Done when:** write and check modes have focused assertions for ungradeable results and neither silently contradicts documentation. **Sources:** REG CTR-019; EX finding 3.

- [ ] **H04 · P2 · Existing — CTR-021: preserve expected verdicts and reasons across writes.** Choose a separate human-authored expectations file or explicit preservation semantics; test a second generated write. **Done when:** `expected_verdict` and its rationale survive legitimate regeneration or a conflict is reported. **Sources:** REG CTR-021; EX finding 4; CHECKER T22 analogy.

- [ ] **H05 · P2 · Existing — CTR-016: replace name matching with execution evidence.** Instrument actual emitted verdicts or an equivalent behavioral oracle. **Done when:** comments and assertions that a verdict is absent cannot satisfy “the suite produced this verdict,” and the replacement has a seeded violation. **Sources:** REG CTR-016; EX finding 5.

- [ ] **H06 · P2 · Existing — CTR-018: validate accepted-kind names.** Check keys against supported clause kinds and expose typos. **Done when:** a misspelled acceptance key produces a clear error rather than silent nonacceptance. **Sources:** REG CTR-018; TRIAGE Odd.

- [ ] **H07 · P2 · Existing — CTR-003: settle duration grammar and defend it.** Document which parser contracts use and deliberately decide whether the two grammars should align. **Done when:** contract duration units, bare values, unsupported inputs, and relevant boundaries have behavior-backed coverage. Unifying the parsers is not presumed necessary. **Sources:** REG CTR-003; TRIAGE Odd.

- [ ] **H08 · P2 · Existing — CTR-002: verify the fraction boundary and classify its defense accurately.** Probe out-of-range values such as 50 and the 0/1 boundaries; inspect whether the mechanism is runtime model validation rather than compiler-enforced unrepresentability. **Done when:** the defense kind/oracle match the actual mechanism, and the decision about additional tests is explicit. **Sources:** REG CTR-002; TRIAGE Ambiguous; METHOD type definition. The classification check is a derived seam, not a confirmed new defect.

- [ ] **H09 · P2 · Existing — CTR-009: cover additive compatibility's passing half.** Find existing execution evidence or add a focused case where an extra column is permitted. **Done when:** both promised compatibility directions are defended. **Sources:** REG CTR-009; TRIAGE Ambiguous.

- [ ] **H10 · P2 · Existing — CTR-010: correct the stale documented field count.** Reconcile the paragraph describing three fields with the added `accepted` field. **Done when:** prose and model agree and the intentional gap remains a separately justified decision. **Sources:** REG CTR-010. This item is easy to lose because it is in `next_step` but not a named triage bullet.

- [ ] **H11 · P2 · Existing — CTR-011: exercise `_cell` escaping.** Locate or add the missing pipe-containing input case. **Done when:** an execution asserts the intended escaped rendering, not merely the docstring describing the old fix. **Sources:** REG CTR-011; TRIAGE Ambiguous.

- [ ] **H12 · P2 · Existing — CTR-012: complete init-to-verify execution.** Extend or supplement the workflow that deliberately stops short. **Done when:** the user-facing initialization path produces an artifact that completes verification with the intended result. **Sources:** REG CTR-012; TRIAGE Missing.

- [ ] **H13 · P2 · Existing — CTR-014/043: review documentation sweep coverage and exemptions.** Ensure the navigable contract page is included; inspect both static exemption lists and make each bypass visible and justified. **Done when:** deliberately adding an unsupported statement or exemption cannot silently evade the intended assurance. **Sources:** REG CTR-014; TRIAGE Odd CTR-014/043. Shares the documentation repair with H01; does not duplicate its completion.

- [ ] **H14 · P2 · Existing — CTR-032: establish `own & run.absent` branch coverage.** Determine whether an existing test actually reaches it, and add one if needed. **Done when:** the branch has an observed result and absent execution is not confused with a quiet check. **Sources:** REG CTR-032; TRIAGE Ambiguous.

- [ ] **H15 · P2 · Existing — CTR-037: locate or add parser-error-shape defenses.** Search the referenced historical readable-load-errors change and the wider suite before adding duplicates. **Done when:** public error cases are asserted behaviorally, with no reliance on a source comment alone. **Sources:** REG CTR-037; TRIAGE Missing.

- [ ] **H16 · P2 · Existing — CTR-038: reconcile dbt execution status.** The triage calls execution unknown, while the later example report says the 149-test run included the dbt execution half. **Done when:** the dated completed run is linked and the remaining need for a current rerun is separate from the historical fact. Do not keep “never run” as an unqualified task. **Sources:** REG CTR-038; TRIAGE Ambiguous; EX execution.

- [ ] **H17 · P2 · Existing — CTR-041: verify every promised missing-file CLI result.** Check the relevant lint/verify/prove/docs paths, including the documented prior false-positive test. **Done when:** each claimed path has an assertion of its actual output/exit, and the test cannot pass through the wrong handler. **Sources:** REG CTR-041; TRIAGE Ambiguous.

- [ ] **H18 · P2 · Existing — Give `contract prove` a real in-repository subject and gate.** Commit an appropriate example contract and soundness artifact, then wire and execute the intended check. **Done when:** `prove` actually gates a promise in its own repository and the first successful run is recorded. **Sources:** TRIAGE “Nobody made this one”; EX execution. Coordinate with H02 where the same example is suitable.

- [ ] **H19 · P2 · Existing — Complete and record the missing execution path.** Recheck current CI/hook execution instead of repeating historical “468 commits/zero runs” as a current fact. Diagnose the CLI startup/metric-discovery timeout enough to complete the intended suite, or report a bounded unresolved limitation. **Done when:** library and CLI execution have separate dated records, the intended automation has actually fired, and skipped/timeouts remain visible. **Sources:** TRIAGE last_actually_ran; EX execution; METHOD V3.

## L — Explicitly later work and admission conditions (6)

- [ ] **L01 · Later · Existing — `affected` and traversal conveniences.** Add diff-first ergonomics once real users need them and the minimal verifier works. Keep history out of routine verification. **Done when admitted:** it answers the measured workflow need with correct endpoints and outputs. **Sources:** CHECKER Two traversals; DISC explicit deferral.

- [ ] **L02 · Later · Existing — `why` and history diagnostics.** Add explanatory history only when basic ground-difference output proves insufficient. **Done when admitted:** shallow/unavailable history degrades to an explicit limitation without breaking correctness. **Sources:** CHECKER Commands; MEASURE history experiment; DISC explicit deferral.

- [ ] **L03 · Later · Existing + New — Sophisticated rename/symbol tracking and materialized indexing.** Admit only after E06 identifies a real bottleneck or unresolved review concentration. First improve validated oracle scope where coarse evidence is the cause. **Done when admitted:** measured cost/queue reduction justifies the complexity without preserving validity on guessed identity. **Sources:** CHECKER T5/Two traversals/Open problems; DISC don't optimize traversal.

- [ ] **L04 · Later decision · Existing + New — `ack` and baseline ergonomics.** The discussion says “perhaps even ack” should wait; decide based on pilot review load. If introduced, preserve finding visibility and validity, forbid acknowledging structural defects, and keep unresolvable nonzero regardless of acknowledgment. **Done when admitted:** T12/T13/T15 hold before and after acknowledgment, with fingerprint behavior specified. **Sources:** DISC tentative deferral; CHECKER baseline/exit requirements.

- [ ] **L05 · Later · Existing — Broader adapters, migration, and the complete companion runner.** Expand beyond the initial language/probe only after the pilots demonstrate demand. Obtain authorized legacy examples for T19; emit reviewable migration patches without applying them or manufacturing evidence. Specify and test the full seeded-violation/mutation catalog behavior, boundary metadata, expectations, and additional structured adapters. **Done when admitted:** each added scope has an observed adoption need and meaningful conformance evidence. **Sources:** CHECKER T19/R1–R4; EXAMPLES; SURVEY adapter question. Basic `0.1-probe` compatibility remains D06/C02, not deferred here.

- [ ] **L06 · Later · Existing — Gap revisit conditions.** Keep accepted gaps outside validity initially. Design `revisit_on` only if pilots show accepted decisions outliving their assumptions. **Done when admitted:** a concrete observed gap-drift case motivates the trigger and the field does not masquerade as evidence validity. **Sources:** CHECKER Open problems. This preserves an existing unresolved question rather than adding an immediate feature from DISC.

## Already decided in the design — implement and verify, do not redesign by default

| Discussion point | Current specification | Work that remains |
|---|---|---|
| Validity belongs to the defense assertion | T1 | C07; no aggregate promise adequacy without composition semantics |
| Changed grounds cannot retain a grade | T2–T4 | C07–C08 |
| Evidence basis is the authority; lock is disposable | T20 | C03/C07/C09 |
| Acknowledgment records awareness, never truth | T15 | Preserve now; implement L04 only when admitted |
| Cannot inspect is not a clean result | T12–T13 | C04/C07–C08 |
| Evidence has identity, verdict, lineage, explicit binding | T16/T21/T22 | C05–C08 |
| Generators do not own human bindings | T6/T22 | S08/C09 |
| Three scopes are distinct; claimed precision is bounded | T5 | S07/C02 |
| Producer executes the oracle; checker consumes records | Companion R1–R4 | C04, later L05 |
| Scale/indexing are not demonstrated blockers | Synthetic measurements; no required materialized index | E06 before L03 |

These are settled specifications, not implemented protections. Conversely, the real register and historical library run are completed observations, not still-pending “first survey” or “run anything” tasks.

## Coverage of the supplied discussion

| Discussion section | Consolidated work |
|---|---|
| Product idea and positioning | D02–D03, S01 |
| Preserve epistemic discipline | P01–P04, C01–C10, invariant table |
| Real defects and triage yield | D07, S04–S05, H01–H19 |
| Survey is underdesigned | S02–S10, E03–E04 |
| Adoption complexity | S08–S10, D06 |
| Execution provenance seam | P01–P04, C01/C03 |
| Monocultural evidence | E01–E04/E07 |
| README dogfooding | D01/D08 |
| Ten-step vertical slice | C01–C09, then survey emphasis S02–S10; packaged by C10 |
| Defer checker conveniences | L01–L05 |
| Discovery yield and maintenance burden | E01/E03/E05–E06 |
| Proposed effort allocation | D03 and suggested order |

The review's numeric ratings are opinions, not acceptance tests. Its open-source-readiness score does not itself derive a new licensing, trademark, website, or launch-program backlog. Apache-2.0 and NOTICE already exist. Such work can be planned separately when release scope is requested.

## Completion rule for this backlog

Close an item only with a linked decision, artifact, or dated observation satisfying its completion condition. Mark designed, implemented, exercised, and measured separately. Refresh target revisions before implementation, retain historical observations, and report unresolved tasks by their actual question. Checking off this planning list does not establish that Upheld's promises are defended; its own evidence and maintenance measurements must do that.
