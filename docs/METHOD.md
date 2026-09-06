# Grade the defense before relying on its evidence

Readers are engineers surveying a codebase. Upheld records falsifiable software promises and the mechanisms intended to defend them.

This is method version 1.2, dated 6 September 2026. It keeps all 27 rule IDs from version 1.0. The [original snapshot](history/2026-09-06/METHOD.md) keeps each defect, reason, and historical self-score. The tables below govern new records. MUST marks a rule earned by an observed defect. SHOULD marks a reasoned rule that still needs stronger support.

**Reading a test can establish a candidate link. A run that detects a stated fault can grade that defense.** Neither observation proves the whole promise.

## Separate discovery from the choice of defense

Complete the reading pass before writing tests. A run with an independent oracle, such as a seeded fault or a complete artifact list, can combine discovery and repair. An oracle is the check that decides the observed result independently of the author's judgment.

Read public documents, specifications, configuration formats, source, and tests. Record where a promise is made separately from the code it concerns. Check cross-file claims as carefully as local claims.

| ID | Strength | Rule and check |
|---|---|---|
| P1 | SHOULD | Finish reading before writing unless an independent oracle controls the pass. Inspect the run sequence. |
| P2 | MUST | Label name-matched links `not_yet_read`. They never establish adequate coverage. Sample links and read the named artifacts. |
| P3 | MUST | Run an available cheap probe before recording a claim about external behavior as evidence. Link its observation. |
| S1 | SHOULD | Enumerate promises published outside source and map them to the relevant code. Record published clauses with no implementation as promises. Inspect public surfaces for omissions. |

## Record claims and decisions separately

A promise holds the claim and survey notes. A defense assertion links a mechanism to that promise. A gap holds a reason to leave it undefended. An evidence record holds what a run observed. A binding names the evidence a person accepts for one defense.

An answered defense has a binding. The checker compares current files with that record to decide whether its grounds still hold. A promise has no stored answer or adequacy status. Reports count open defenses, gaps, unresolved choices, and next questions separately.

| ID | Strength | Rule and check |
|---|---|---|
| O1 | SHOULD | Promise `text` states what could be false. Ask which observation would refute it. |
| O2 | MUST | Every defense has an explicit `guarded_by` mechanism with no default. An unfamiliar kind needs an extension name and description. A gap is a separate decision. |
| O3 | MUST | Every promise has prose in `the_test_that_would_catch_it`; that prose outranks technique tags. The field can describe a check other than a test. |
| O4 | SHOULD | `confidence` separates `verified` reading with a quotation from `suspected` shape matches. It describes discovery, not defense adequacy. |
| O5 | SHOULD | Unresolved survey questions carry `next_step` with the question that would settle them. |
| O6 | SHOULD | `evidence_tier` records whether a link rests on read text, unread behavior, an exact structural join, or fuzzy naming. |
| O7 | SHOULD | Record the artifact on its defense and the observed revision and basis on its evidence. An artifact name alone is insufficient. |
| O8 | SHOULD | Reassess a bound defense when relevant grounds change. The checker derives this result; no promise status changes. |
| O9 | MUST | Record environment needs separately from the defense kind, in `needs_environment`. |
| O10 | MUST | Record reachability as live, latent, impossible, or unknown. A latent promise carries `armed_by`, the condition that makes it reachable. Its defense guards that condition and fails when it becomes true. Split mixed live and latent claims. |

O7 and O8 remain proposed mechanisms without product execution evidence. Their wire fields replace the old promise-level `satisfied_by` and `status`. [The schema mapping](SCHEMA.md) preserves legacy survey notes.

## Match the evidence check to the mechanism

The six built-in kinds are test, property, checker, ratchet, type, and runtime invariant. A property samples generated inputs. A ratchet compares behavior over time. A type guarantee prevents a violation through static checking. A model that rejects bad values at runtime needs a check that actually runs.

[The compatibility table](SCHEMA.md) names the accepted oracle families. Gaps are decisions, and warnings alone do not establish acceptance.

| ID | Strength | Rule and check |
|---|---|---|
| V1 | MUST | Choose the kind from the mechanism, regardless of its file or workflow location. |
| V2 | MUST | A checker fails on a present defect or ratchets against a baseline; enumerates results; distinguishes clean, violated, and unable to inspect; and actually runs at the intended occasion. |
| V3 | MUST | Record actual execution time as `last_actually_ran` from a run, with unknowns explicit. A workflow declaration supplies no timestamp. |
| V4 | MUST | Bind a test or property defense only after an oracle discriminates a fault under a stated model. A passing suite alone cannot supply this record. |
| V5 | MUST | Bind a checker only after a seeded violation differs from both a clean input and failure to inspect. |
| V6 | SHOULD | Bind a runtime invariant only after fault injection exercises it. No supporting run was present in the source survey. |

Fault discrimination needs a justified fault model. Replayed defects, corrupted artifacts, and injected faults can qualify; mutation is the default. A timeout, build failure, or unscheduled check cannot count as detection. Record an unscheduled check as absent.

A compiler's own acceptance cannot establish its soundness. Type defenses need an independent authority, such as a checked proof or a reference implementation. No type-defense oracle was exercised in the source survey.

Read or probe library behavior before calling two cases equivalent. A small probe can settle a library behavior that reading alone leaves uncertain. Fuzzy links remain candidates until an independent check supports them.

## Measure useful findings and the work to review them

The survey aims to discover useful new promises and defects within the time people can spend reviewing them. The checker aims to minimize silently stale assertions within that capacity. [The milestone](MILESTONE.md) defines the first measurements.

| ID | Strength | Rule and check |
|---|---|---|
| H1 | SHOULD | Report unresolved `next_step` count as prominently as promise count. |
| X1 | MUST | Derive the exit criterion from code and recheck it against a machine-readable baseline. Inspect both the baseline and its actual execution. |
| X2 | MUST | Check generated survey state at each intended occasion. Use regenerate-and-compare when cheap; otherwise measure and use a cheaper guard. |
| D1 | SHOULD | Each deliberately absent feature names the condition that would justify adding it. |
| Rp1 | MUST | Each quantitative claim names its repository and date. |
| Rp2 | MUST | Label single observations and unrun claims where they occur. |
| Rp3 | MUST | Read the whole report before sharing it. A diff can hide contradictions elsewhere. |

Requirements describe the instrument. Meeting the rules alone establishes neither useful findings nor safe software. Write down expected results before trials. Write expectations and models from the contract before running the implementation. A static screen selects work to inspect and cannot grade it. State how source choice and different category rules limit the findings. Matching category totals does not establish correct labels. Open-thread counts measure unresolved work; movement requires dated comparisons. Rp3 requires human review and has no mechanical proof.

## Current evidence covers one hand survey

The [heldtospec example](../examples/heldtospec-contracts/README.md) has 44 promises and zero accepted evidence records. Its historical library run reports 149 passing tests. The CLI run did not complete. Those runs do not establish that the survey meets every rule.

The [Upheld status case](../examples/upheld-status/README.md) has a repeatable README check and an unbound defense. The product still needs hash rules and a way to create evidence records. Historical self-scores in the snapshot refer to heldtospec at their recorded revision.

[The rule review](RULE_REVIEW.md) maps each original requirement to the current rules and records deliberate changes.
