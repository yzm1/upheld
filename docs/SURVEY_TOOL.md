# Discover useful claims within the reader's review budget

Readers are engineers building the first survey workflow. The committed hand survey produced 44 promises and 17 next questions. Its triage page contains 19 finding bullets.

The scanner remains unbuilt. The serializer writes choices already present in its source. [The count audit](../examples/heldtospec-contracts/reconciliation.md) explains why the earlier 18-item count and probe totals cannot support a yield ratio.

## Give the reader a useful finding before explaining the records

The planned first-use path is `upheld survey`. It should collect candidates, run suitable cheap probes, and write a readable review file. A user should reach a finding without manually creating every internal file.

**Maximize independently reviewed, useful new discoveries within a fixed human attention budget.** Report defects and newly articulated promises separately. Register size supplies no success measure.

The [cross-domain research](SURVEY_RESEARCH.md) compares scientific claim extraction, evidence search, systematic review, interview analysis, and software probes. It recommends fixed rules for source handling and optional language model help with prose. The [backend proposal](SURVEY_BACKENDS.md) lets users configure their own CLI or model API before model-assisted work.

These are S01 design decisions dated 6 September 2026. S02–S10 still own implementation; E01 still owns the registered trial protocol. No trial has established the recommended approach's advantage.

## Count a discovery only after resolving its meaning

| Term | Operational meaning | Required record |
|---|---|---|
| Useful | Changes a named engineering decision, exposes consequential behavior, or creates a justified next action | Consequence and proposed action; reviewer rationale |
| New | Previously unknown at a declared level: reviewer, project, or existing register | Prior-knowledge check and duplicate search; unknown history stays unknown |
| Confirmed defect | A scoped mismatch with an established promise, supported by inspectable evidence | Exact promise, source or bounded run, affected conditions, and reviewer decision |
| Confirmed new promise | A consequential obligation that the responsible reviewer accepts into the project's stated promises | Source or rationale, scope, acceptance, and prior-knowledge result |
| Decision-required | Evidence exposes an unresolved choice about intended behavior | Competing choices, consequence, owner, and next question; no defect credit yet |
| Candidate | A passage, proposed claim, or suspected mismatch awaiting review | Source, context, uncertainty, and next step |

Use new-to-project findings for the primary milestone outcome. Keep new-to-reviewer and newly recorded findings as separate learning measures. A previously known but undocumented obligation does not become new-to-project merely because it enters the register. Unsettled novelty receives no confirmed-new credit.

Count distinct consequential discoveries. Link duplicates and parts of the same claim; splitting a sentence cannot multiply outcome credit. A discovery that exposes both a promise and its violation receives one total credit with both labels. Report each category and their deduplicated union.

Confirmation concerns the surveyed claim. It does not establish the adequacy of its defense or create an evidence binding. The responsible maintainer resolves disputes against the source and run record.

## Discover questions before retrieving their answers

Use two entry paths: systematic discovery across a bounded source collection, and targeted inquiry about an existing claim. Both retain exact sources and review decisions. Targeted search alone cannot establish that the survey found the important questions.

Inventory included, excluded, unreadable, and unsupported sources first. Extract exact passages and explicit declarations before proposing standalone claims. Preserve conditions, exceptions, negation, versions, and whether the text states behavior or requires it.

Search for evidence that supports or challenges each claim. Mark partial support and scope mismatches explicitly. A missing result means no evidence was retrieved within that search; it does not establish that no evidence exists. Ambiguous passages remain reviewable.

## Measure attention and omissions alongside findings

| Measure | Reporting rule |
|---|---|
| Confirmed useful new discoveries | Separate defects and promises; report their deduplicated union and unresolved novelty |
| Human cost | Include setup, source review, dismissal, duplicate handling, probe interpretation, and dispute resolution; record participant roles |
| Yield | Confirmed useful new discoveries divided by all human review hours; report hours and zero findings when yield is zero |
| Time to first useful finding | Include setup; mark trials without a finding explicitly |
| Candidate errors | Sample faithfulness, lost qualifications, unsupported additions, and wrong evidence relationships; report denominators |
| Missed claims | Independently review a declared sample of source passages, including low-ranked and unprocessed material |
| Source reach | Report included sources, processed portions, omissions, and what each source type contributed |
| Remaining work | Count unresolved choices, unreviewed candidates, queue age, and the reason work stopped |
| Machine cost | Report elapsed time, model and tool calls, tokens and spend where available; keep these separate from human time |

Report total person-minutes when several people participate. Record probe runtime separately from human attention. If no useful finding occurs, minutes per finding is undefined; the trial fails the milestone's finding rule.

Reserve part of the review budget for a random audit of the remaining sources and lower-ranked candidates. E01 must fix the allocation and sampling method before each trial. Sample estimates apply only to their declared population; an unknown universe of possible promises has no measurable global recall.

Stop at the registered budget or explicit source boundary. Record the unfinished queue and omissions. Budget exhaustion does not mean the survey is complete.

## Reading and probes answer different questions

| Step | Output | Limit |
|---|---|---|
| Scan public docs, formats, code, and test assertions | Falsifiable candidate with source and subject | A matching name supplies no grade |
| Review skeptically | Confirmed issue, refuted claim, or unresolved question | Unknown does not mean covered |
| Run a bounded probe | Dated observation, command, result, omissions | A promise failure does not grade its defense |
| Ask which mechanism defends the claim | Explicit kind or gap decision | No default kind |
| Serialize reviewed records | Stable IDs and producer inputs | Human bindings remain in a separate file |

The [record schema](SCHEMA.md) keeps source location, subject scope, confidence, required tools, and whether a defect is reachable separate. Subject scope means the code a claim concerns. Artifact locator means the place where its defense resides.

## Preserve the six mechanism choices

Offer test, property, checker, ratchet, type, and runtime invariant. Record an accepted gap separately. For an unfamiliar mechanism, retain its name and explanation through the extension route.

Classifier trials compare item-level judgments using one shared vocabulary. The [two historical studies](../examples/README.md) used different methods. Reproducing either total cannot establish accuracy.

## The first trial decides what to build next

Implement the source scan and cheap-probe path for heldtospec, then try two independent projects. [The milestone](MILESTONE.md) records the trial protocol and success rules.

The minimum review surface and first probe adapters remain open. Compare human search, the non-generative workflow, a direct agent prompt, and the hybrid workflow before expanding infrastructure. Keep source access and attention budgets comparable. Measure defense-category choices separately from claim extraction.

Register generation must preserve stable IDs and reviewed choices, or expose conflicts. The checker never reruns the scanner. The producer declares the files it reads so later checks can report changed inputs.
