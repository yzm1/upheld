# The rule review restores omitted operational instructions

Readers are Upheld maintainers reviewing the shortened rules. This review compares the dated originals with the current method and checker on 6 September 2026.

The initial rewrite preserved identifiers but lost operational clauses. The repairs below restore those clauses and state deliberate changes. Historical examples remain in the unchanged source snapshots. This review records what each rule requires. The product still has no grade.

## Every original rule has a current disposition

Original sources: [method](history/2026-09-06/METHOD.md) and [checker](history/2026-09-06/CHECKER.md). Current sources: [method](METHOD.md) and [checker](CHECKER.md). Every rule retains its original MUST or SHOULD strength.

| ID | Disposition and retained meaning |
|---|---|
| P1 | Preserved: reading precedes repair unless an independent oracle controls the pass. |
| P2 | Restored: no link found differs from confirmed absence; name matching gives no numerical coverage bound. |
| P3 | Preserved: cheap external-behavior probes run before claims become evidence. |
| O1 | Renamed name to text; the claim remains falsifiable. |
| O2 | Moved mechanism to each defense; accepted becomes a gap. Extensions remain explicit. |
| O3 | Preserved: prose falsifier outranks technique tags. |
| O4 | Preserved: verified means read and quoted, distinct from suspected discovery. |
| O5 | Preserved: unresolved questions carry a next step that can settle them. |
| O6 | Preserved: evidence tier records dependence beyond read text; unknown is explicit. |
| O7 | Moved artifact to defense and revision to evidence. Still proposed without product execution. |
| O8 | Moved reassessment to derived defense results. Run context stays separate from stable basis. |
| O9 | Moved environment needs to each defense, separate from mechanism. |
| O10 | Restored: guard the arming condition and split live/latent claims. Unknown reachability is explicit. |
| V1 | Preserved: classify by mechanism rather than directory. |
| V2 | Restored absent execution as distinct from a quiet result; all four checker requirements remain. |
| V3 | Preserved: actual run timestamp, with unknown explicit; no workflow boolean. |
| V4 | Restored justified fault models and alternative fault sources. Timeouts and build failures are not detection. |
| V5 | Preserved: seeded violation differs from clean and failure to inspect. |
| V6 | Preserved: runtime fault injection remains proposed and unexercised in the source. |
| H1 | Preserved equal prominence of unresolved counts; restored the limit on claiming movement. |
| X1 | Preserved: source-derived criterion and an executed machine-readable baseline comparison. |
| X2 | Preserved: measure cost before choosing regeneration or a cheaper freshness guard. |
| S1 | Restored explicit recording of published clauses with no implementation. |
| D1 | Preserved: each deliberate absence carries the condition for reconsidering it. |
| Rp1 | Preserved: quantitative claims name their repository and date. |
| Rp2 | Preserved: single observations and unrun claims carry limits where used. |
| Rp3 | Restored explicit reliance on human whole-document review; no mechanical proof. |
| T1 | Explicit scope choice: version 0.1 defers the original composition exception; promise reports give counts. |
| T2 | Preserved: changed grounds never yield still_valid. |
| T3 | Preserved: consequences use changed grounds and resolution, without semantic guesses. |
| T4 | Preserved: separate fingerprints with a named profile, plus evidence lineage. |
| T5 | Preserved: promise containment, validated precision, and independent locator. |
| T6 | Restored the ban on hand-edited locks; register and binding writes remain forbidden. |
| T8 | Preserved: guarded_by is required without a default. |
| T9 | Preserved: enumerate structural defects; verify requires valid inputs; only ack acknowledges. |
| T12 | Preserved: uninspectable targets cannot yield clean, including after acknowledgment. |
| T13 | Preserved: configurable facets, mandatory unresolvable gate, all facets reported. |
| T14 | Explicit staging: schemas precede each command release; only three outputs currently have schemas. |
| T15 | Preserved: acknowledgment changes neither result nor visibility and applies only to verify. |
| T16 | Preserved: immutable identified evidence; bindings require existing matching compatible supports records. |
| T17 | Preserved: a specified versioned hash profile shared with producers; still deferred. |
| T18 | Preserved: declared producer inputs, reported drift, no rerun by checker. |
| T19 | Preserved: unapplied migration patch and no invented evidence; review-copy tool is a limited precursor. |
| T20 | Preserved: bound evidence owns basis and regeneration cannot advance it. |
| T21 | Preserved: explicit supersession or newer same-defense/same-oracle contradiction only. |
| T22 | Preserved: producers never write bindings. |
| R1 | Preserved: structured three-state outcomes; startup, compile, and collection failures cannot support. |
| R2 | Preserved: restore the tree on every exit, including preexisting edits. |
| R3 | Preserved: record boundary distance and report missing distances. |
| R4 | Preserved: basis comes from the checker and a rerun names superseded evidence. |

## Supporting explanations also constrain interpretation

The current method restores independent type oracles, expected results drawn from the contract, and static screening as a reading aid. The schema document clarifies that the compiler family cannot establish soundness through compiler acceptance alone. Fault-family labels also cannot exclude the replay and injection options allowed by V4.

The old artifact/revision and stored-status fields now split across defenses, evidence, and bindings. This deliberate change lets one promise have several separately assessed defenses. Accepted gaps stay distinct from missing defenses. Unknown imported facts remain visible rather than becoming invented observations.

## Text checks require review but cannot perform it

The [review manifest](rule-review.json) fixes the reviewed document bytes and each rule's strength. Editing a rule document requires a new comparison and an explicit manifest update in the same change. Update this review when meaning changes. Hashes cannot establish that the replacement wording is correct.

The tests downgrade T2 and reverse T20 without updating the manifest; both must fail. A reviewer can still approve a bad rule and update its hash. That remaining risk requires human review, including Rp3. The manifest makes an unreviewed edit visible; it never grades semantic equivalence.

## Method 1.3 clarifies the source and judgment boundaries

The S02 review on 6 September 2026 keeps all 27 method rule IDs and their strengths. P1's reading pass now has an explicit source boundary and visible omissions. O4's quoted reading remains distinct from faithful meaning and established behavior. The oracle explanation requires a separately justified criterion; a second answer from the same model cannot count as independent evidence.

The prose on measured results now links S01's outcome definitions and includes omitted sources and total review effort. The evidence section adds the S02 replay and states what it cannot establish. These edits clarify scope and reporting; they do not relax V4, V5, type-defense authority, or human acceptance.
