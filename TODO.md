# D01–D08, S01, and S11 are complete; S02 needs further checks

Readers are engineers choosing the next Upheld task. This list tracks the supplied discussion against the repository, updated 7 September 2026.

Ten tasks are complete: D01–D08 after the [review repairs](docs/RED_TEAM_FIXES.md), plus S01 and S11 research. S02 has a working prototype but remains open after its red-team review. D04, D06, and D08 were reopened and repaired; the original completion claim overstated their checks. The other 58 tasks remain open or deferred. Product commands, evidence producers, and hash rules remain unbuilt.

[The completion record](docs/COMPLETED_D01_D08.md) links the changes and checks. [The original derived list](docs/history/2026-09-06/DERIVED_TODO.md) preserves the full reasoning, dependencies, and sources for the original 64 items. S11 adds research requested on 6 September 2026. S12–S14 carry its follow-ups. The total is 68 tasks.

## Completed work establishes the current rules

| ID | Status | Completed result | Evidence |
|---|---|---|---|
| D01 | Complete | Current status pages distinguish survey, scripts, and unbuilt CLI. | [Artifact](README.md) |
| D02 | Complete | Adopted evidence-check wording and documented its limit. | [Artifact](docs/DECISIONS.md) |
| D03 | Complete | Set deliverables, trial rules, scope, and effort split. | [Artifact](docs/MILESTONE.md) |
| D04 | Complete | Restored omitted rules and reviewed every original ID; recorded deliberate changes. | [Rule review](docs/RULE_REVIEW.md) |
| D05 | Complete | Defined six built-in kinds, separate gaps, and an explicit extension route. | [Artifact](docs/SCHEMA.md) |
| D06 | Complete | Checked nine schemas, source versions, timestamp and exit rules, and required fixtures. | [Artifact](schemas/0.1/) |
| D07 | Complete | Recounted 19 finding bullets; assigned record IDs and preserved unknown probe totals. | [Artifact](examples/heldtospec-contracts/reconciliation.md) |
| D08 | Complete | Recorded README drift, added a status defense, and exercised seeded failures. | [Artifact](examples/upheld-status/README.md) |
| S01 | Complete | Defined useful, new, confirmed, and decision-required outcomes; specified attention and omission measures; compared cross-domain methods and user-configured backends. E01 trial registration remains open. | [Objective](docs/SURVEY_TOOL.md), [research](docs/SURVEY_RESEARCH.md), [backend proposal](docs/SURVEY_BACKENDS.md) |
| S11 | Complete | Compared primary research and official interfaces; chose an opt-in guide prototype; specified trials and follow-ups. No measured benefit or shipped skill is claimed. | [Research](docs/AGENT_METHOD_RESEARCH.md), [test proposal](docs/AGENT_METHOD_EVALUATION.md), [Repo C case](docs/CONNECTLANG_METHOD_CASE.md) |


## Build the survey and small checker together

The [milestone](docs/MILESTONE.md) defines the next trial and proposed effort split. Complete hash rules and run-context policy before relying on product evidence.

Priority P0 means a trust blocker. P1 means the next learning milestone. P2 means follow-on work. Later work needs the stated admission condition.

| ID | Priority | Task | Completion condition |
|---|---|---|---|
| S02 | P1 | Finish live adapter checks and independently assess the implemented source-review prototype | Demonstrate the configured real CLI and effective permissions; independently review source passages for missed or distorted claims. The source/import path and replay work, but those results do not complete the agreed assessment. See [red-team findings](docs/S02_RED_TEAM.md). |
| S12 | P1 | Build the opt-in Upheld guide and versioned references | Preserve all method IDs and strengths, source limits, independent evidence, and project scope. Cover discovery without a register, change review, defense challenge, probe reading, and record proposals. Include the reviewed Repo C example. A source-text instruction cannot authorize a run or binding. No benefit claim before E01 trials. |
| S13 | P1 | Prepare independently reviewed agent-method cases | Pin real sources across software, scientific evidence, and reproducible analysis; separate expected answers from agent inputs. Two reviewers record judgments and disagreements. Exclude Repo C, heldtospec, and related answers from held-out cases. Meet the [test proposal](docs/AGENT_METHOD_EVALUATION.md) before registering E01. |
| S14 | P1 | Exercise configured clients and compare added support | After S12–S13, record real skill loading, effective permissions, missing-tool behavior, cancellation, and cost for each claimed client. Run the E01-registered comparisons and publish failures, useful findings, misses, and human work. Test automatic triggering separately. Add a server only for a demonstrated need unmet by local commands. Feed the decision into E07. |
| S03 | P1 | Add test/code sources and audit source-selection bias | the survey records what each source adds and checks the documented undercount of shape/type-related promises. |
| S04 | P1 | Build skeptical triage with explicit uncertainty | the example queue has an auditable disposition per item and unknowns cannot be converted into verified coverage by a default. |
| S05 | P1 | Build the cheap-probe stage before investing heavily in a classifier | the first queue can be mechanically reduced with a measured cost per resolved item. Findings about a promise remain distinct from evidence grading a defense. |
| S06 | P1 | Implement classification without a preselected defense | the interface cannot silently turn uncertainty, unavailable infrastructure, or every new row into `test`. |
| S07 | P1 | Define document-to-subject mapping and usable locators | supported locators resolve deterministically and scope containment can be checked without pretending the artifact locator is subject scope. |
| S08 | P1 | Make register generation preserve human decisions | a second survey run retains reviewed decisions or surfaces an explicit conflict, leaves bindings intact, and never emits accepted evidence merely because it found a defense. |
| S09 | P1 | Deliver a one-command first-use path | a first-time engineer can reach a useful finding without manually authoring six ontology files. Complete live adapter checks for authentication, output, effective permissions, cancellation, and costs before claiming provider readiness. Counts distinguish candidates, unbound defenses, findings, and confirmed evidence; the review's sample “104 well supported” is illustrative, not a valid evidence claim. |
| S10 | P1 | Choose the minimum review surface and measure its usability | a new user can resolve a triage item and resume a rescan without understanding the whole checker ontology. |
| P01 | P0 | Specify an execution-provenance object or equivalent linked run record | the recorded observation can be identified beyond a Git SHA and absent fields have explicit meaning. |
| P02 | P0 | Define what `verify` can and cannot establish about runtime context | “tree basis unchanged” does not imply an independently checked execution environment, and cross-machine comparisons follow a documented policy. |
| P03 | P0 | Reconcile dirty-tree capture with the actual oracle observation | two dirty trees at the same SHA are distinguishable, and a run cannot attach clean-commit grounds to dirty source it actually observed. |
| P04 | P1 | Record actual execution and omissions without upgrading their meaning | a declared workflow, a passing suite, and a completed adequacy oracle are three distinguishable facts in reports. |
| C01 | P0 | Write hashing profile v0.1 and executable conformance vectors | producer and verifier paths agree on canonical fixtures and the vectors expose disagreements rather than merely repeat one helper's output. |
| C02 | P0 | Implement `validate` and run it on the real 44-promise register | malformed fixtures yield all applicable diagnostics and the real example is honestly reported. In particular CTR-003/005/037/044 have neither defense nor gap and should be findings under the existing specification; do not force a clean exit by inventing acceptance. |
| C03 | P0 | Implement `basis` for the first supported source/scope profile | a producer invokes the command and carries its output verbatim, with unsupported/unreadable inputs reported honestly. |
| C04 | P1 | Build one tiny evidence producer and its structured adapter | real detection, survival, startup/collection failure, and cleanup each demonstrate the correct behavior. |
| C05 | P1 | Produce the first real immutable EvidenceRecord | an append-only record from C04 exists and validates; it is not reconstructed from the historical 149-pass run. |
| C06 | P1 | Demonstrate explicit evidence binding | the checker consumes a valid binding, rejects mismatched/inconclusive records, and neither scanner nor producer silently writes acceptance. |
| C07 | P1 | Implement the minimal `verify` path and honest output | unchanged grounds produce the expected result and all implemented finding classes have structured output. |
| C08 | P1 | Demonstrate invalidation and evidence-lineage behavior | moved grounds never produce `still_valid`; lineage invalidates only as specified; unrelated inconclusive observations do not automatically invalidate a supporting binding. |
| C09 | P0 release gate | Prove regeneration cannot restore validity | no stale defense becomes current, binding decisions survive, and any cache that is implemented is reproducible. Start with this acceptance test before implementing caching. |
| C10 | P1 | Package the reproducible demonstration and score its conformance honestly | another engineer can reproduce it, a run record exists, and the CHECKER conformance table distinguishes passed, unsupported, and deferred requirements. |
| E01 | P1 | Pre-register the evaluation protocol | discovery yield, error rates, and human effort cannot be redefined after the run to flatter it. |
| E02 | P1 | Select two independent pilot targets | the pair challenges both shared development habits and language assumptions; no claim of universality follows from two examples. |
| E03 | P1 | Run the two-hour discovery experiment on both targets | the findings have evidence and the denominators include unsuccessful triage effort. |
| E04 | P1 | Evaluate classifier choices with matched instruments | a chosen method outperforms a relevant baseline or its limits are stated. Matching A's distribution alone is insufficient; METHOD already warns that A/B instruments differ. |
| E05 | P1 | Run the maintenance follow-up after real development | maintenance burden is measured against actual changed grounds and oracle reassessment, not simply “number of hashes changed.” |
| E06 | P1 | Measure granularity, fanout, and review capacity | evidence supports a decision about finer oracle scopes; do not narrow tracking below validated precision to reduce counts. |
| E07 | P1 | Feed results back into the method and milestone | the next roadmap explicitly says what to keep, change, defer, or stop based on the pilots. |
| H01 | P2 | CTR-005: align public contract documentation with implementation | the documented behavior agrees with current executable behavior and the relevant documentation is checked. |
| H02 | P2 | CTR-044: repair and execute the published example | the copied example passes its intended witness and a regression check executes it. |
| H03 | P2 | CTR-019: decide ungradeable-clause exit semantics | write and check modes have focused assertions for ungradeable results and neither silently contradicts documentation. |
| H04 | P2 | CTR-021: preserve expected verdicts and reasons across writes | `expected_verdict` and its rationale survive legitimate regeneration or a conflict is reported. |
| H05 | P2 | CTR-016: replace name matching with execution evidence | comments and assertions that a verdict is absent cannot satisfy “the suite produced this verdict,” and the replacement has a seeded violation. |
| H06 | P2 | CTR-018: validate accepted-kind names | a misspelled acceptance key produces a clear error rather than silent nonacceptance. |
| H07 | P2 | CTR-003: settle duration grammar and defend it | contract duration units, bare values, unsupported inputs, and relevant boundaries have behavior-backed coverage. Unifying the parsers is not presumed necessary. |
| H08 | P2 | CTR-002: verify the fraction boundary and classify its defense accurately | the defense kind/oracle match the actual mechanism, and the decision about additional tests is explicit. |
| H09 | P2 | CTR-009: cover additive compatibility's passing half | both promised compatibility directions are defended. |
| H10 | P2 | CTR-010: correct the stale documented field count | prose and model agree and the intentional gap remains a separately justified decision. |
| H11 | P2 | CTR-011: exercise `_cell` escaping | an execution asserts the intended escaped rendering, not merely the docstring describing the old fix. |
| H12 | P2 | CTR-012: complete init-to-verify execution | the user-facing initialization path produces an artifact that completes verification with the intended result. |
| H13 | P2 | CTR-014/043: review documentation sweep coverage and exemptions | deliberately adding an unsupported statement or exemption cannot silently evade the intended assurance. |
| H14 | P2 | CTR-032: establish `own & run.absent` branch coverage | the branch has an observed result and absent execution is not confused with a quiet check. |
| H15 | P2 | CTR-037: locate or add parser-error-shape defenses | public error cases are asserted behaviorally, with no reliance on a source comment alone. |
| H16 | P2 | CTR-038: reconcile dbt execution status | the dated completed run is linked and the remaining need for a current rerun is separate from the historical fact. Do not keep “never run” as an unqualified task. |
| H17 | P2 | CTR-041: verify every promised missing-file CLI result | each claimed path has an assertion of its actual output/exit, and the test cannot pass through the wrong handler. |
| H18 | P2 | Give `contract prove` a real in-repository subject and gate | `prove` actually gates a promise in its own repository and the first successful run is recorded. |
| H19 | P2 | Complete and record the missing execution path | library and CLI execution have separate dated records, the intended automation has actually fired, and skipped/timeouts remain visible. |
| L01 | Later | `affected` and traversal conveniences | it answers the measured workflow need with correct endpoints and outputs. |
| L02 | Later | `why` and history diagnostics | shallow/unavailable history degrades to an explicit limitation without breaking correctness. |
| L03 | Later | Sophisticated rename/symbol tracking and materialized indexing | measured cost/queue reduction justifies the complexity without preserving validity on guessed identity. |
| L04 | Later decision | `ack` and baseline ergonomics | T12/T13/T15 hold before and after acknowledgment, with fingerprint behavior specified. |
| L05 | Later | Broader adapters, migration, and the complete companion runner | each added scope has an observed adoption need and meaningful conformance evidence. |
| L06 | Later | Gap revisit conditions | a concrete observed gap-drift case motivates the trigger and the field does not masquerade as evidence validity. |

## S11 researches agents using Upheld as a method

Give agents knowledge of Upheld so they can judge promises, defenses, and evidence during ordinary work. Treat this direction as a peer to Upheld invoking an agent. The user requested this research on 6 September 2026. Build on [S01's research](docs/SURVEY_RESEARCH.md) and [backend proposal](docs/SURVEY_BACKENDS.md); coordinate experiment design with E01.

Match S01's research quality: inspect primary papers, official interfaces, and working examples. Search across domains, including scientific evidence review, fact-checking, review rubrics, and tools that teach agents a method. State search scope, evidence strength, transfer limits, and unknowns. Separate documented features, research results, and proposed transfers; do not rank systems using incompatible benchmarks.

| Research question | Required result |
|---|---|
| How do existing tools apply a supplied method? | Compare skills, project instructions, retrieved reference material, structured workflows, and callable tools across multiple domains |
| What Upheld knowledge changes judgment? | Define the minimum guidance on promises, defense kinds, evidence, uncertainty, gaps, and acceptance; identify which rules need executable checks |
| Which tasks benefit? | Cover discovering promises, reviewing changes, challenging defenses, interpreting probe results, and proposing records, including work without an existing register |
| How should agents access Upheld? | Compare a portable skill and reference pack, local commands and structured files, and a tool protocol such as Model Context Protocol; justify the smallest useful interface |
| Which claims may an agent make? | Specify inspectable sources, reasoning, uncertainty, and next checks; keep model judgments, actual executions, human acceptance, and verified evidence distinct |
| What happens when guidance fails? | Examine stale instructions, conflicting project rules, unsupported tools, misleading source instructions, fabricated evidence, and inappropriate certainty |
| How do we test the added value? | Propose matched comparisons of the same agent without guidance, with an Upheld skill, with executable support, and within the orchestrated survey |

The comparison must measure judgment correctness, missed issues, unsupported conclusions, useful discoveries, human review cost, and operating cost. Use independent outcome review and source-grounded cases beyond software vocabulary. Control source access, model, available tools, and budgets. Distinguish proposed experiments from completed runs.

Close S11 with a dated research report, a supported interface decision, and explicit implementation follow-ups with acceptance criteria. Register concrete trials under E01 before running them. Do not assume a skill, server, or orchestration layer is necessary before comparing the alternatives.

## Historical target findings need a fresh check

H01–H19 describe heldtospec at the recorded survey date. Check its current source before treating any item as an unresolved defect. The later library run already addressed part of H16; its record still needs linking at defense scope.

Close a task with a dated artifact, decision, or observed check. Keep designed, implemented, exercised, and measured states distinct. A completed planning task does not grade a software defense.
