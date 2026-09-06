# Build the survey around questions cheap probes can settle

Readers are engineers building the first survey workflow. The committed hand survey produced 44 promises and 17 next questions. Its triage page contains 19 finding bullets.

The scanner remains unbuilt. The serializer writes choices already present in its source. [The count audit](../examples/heldtospec-contracts/reconciliation.md) explains why the earlier 18-item count and probe totals cannot support a yield ratio.

## Give the reader a useful finding before explaining the records

The planned first-use path is `upheld survey`. It should collect candidates, run suitable cheap probes, and write a readable review file. A user should reach a finding without manually creating every internal file.

The survey aims to maximize useful new promises and defects within human review capacity. Count confirmed findings, unanswered questions, and review minutes separately.

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

The following choices remain open: repository scripts versus shared adapters; file versus command review; questions versus rules or a model for classification. Measure the cost of each unresolved queue before choosing.

Register generation must preserve stable IDs and reviewed choices, or expose conflicts. The checker never reruns the scanner. The producer declares the files it reads so later checks can report changed inputs.
