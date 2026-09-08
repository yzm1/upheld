# The survey writes a schema 0.1 register for review

Readers are engineers who want a machine-readable record of software promises and their defenses. **The `register` command turns a saved source review into the existing JSON format.** A person or a configured agent still supplies the source judgments.

This first export retains unknown enforcement. The source-review format has no defense records, so the exporter leaves each defense list empty. It creates no accepted gaps, evidence, or bindings. A binding is a person's choice to rely on a particular evidence record.

## Export the recorded example to a new file

From the repository root:

```bash
python -m pip install -r requirements-docs.txt
python tools/survey.py register \
  --run examples/survey-heldtospec/run \
  --out /tmp/heldtospec-proposed.register.json
```

The command checks the result against [schema 0.1](../schemas/0.1/register.schema.json) before writing. The example produces twelve proposed promises and no defenses. [The committed output](../examples/survey-register/obligations.register.json) comes from this command. It reuses the saved judgments; it measures no new discovery yield.

Choose an existing output folder and a new filename outside the input run. An existing file or symlink causes an error. The exporter publishes the complete file in one step. A failed publish leaves the prior file intact.

## Each promise keeps its source and its limits

| Field | Exported value |
|---|---|
| `text` | Submitted claim plus its conditions and limits |
| `subject_scope` | The reviewer's stated subject; path containment remains unchecked |
| `source`, `published_in`, `detail` | Source paths, line ranges, and exact quotes |
| `confidence` | `suspected`; matching a quote does not establish its meaning |
| `evidence_tier` | `read`; the source was available to the reviewer |
| `reachability` | `unknown`; no executable path was checked |
| `defenses` | Empty; the source review did not assess them |
| `the_test_that_would_catch_it` | Explicitly unknown |
| `next_step` | The submitted next question |
| `metadata.survey` | Original candidate, uncertainty, source hashes, and reviewer links |

An ambiguous item remains a question under the register's `metadata.survey.questions`. It does not become a promise. Inferred claims remain suspected. Different claims stay separate even when they cite the same source. Exact duplicates share a record while retaining each distinct submitted reply.

The register also carries the reading boundary, inventory, and inspection notes. Missing and excluded files remain visible. Partial reading stays partial. Even a reviewed zero-claim result has no whole-project coverage claim.

## Exported IDs identify proposals with unchanged content

The exporter derives each ID from the declared repository and exact candidate content. Repeated export of the same saved run produces the same bytes with the same exporter. Editing a claim or its source can change its ID. S08 still owns matching those edits to reviewed records.

The exporter checks saved response hashes and checks the raw reply against its parsed copy. It then rechecks the source quotations. These checks detect inconsistent saved data. They do not authenticate the named reviewer, repository, or revision.

It reads at most 1,000 attempt files and 16 MiB of attempt data. The output must fit within 16 MiB. Exceeding a limit causes an error. No partial register counts as a successful export.

## Existing decisions remain untouched

The exporter creates a new proposal. It never edits an earlier register or bindings file. A reviewer can compare the proposal with their maintained register. Automatic reconciliation remains S08 work; the command does not claim that an unchanged ID preserves a human decision across edited claims.

The [source workflow](SURVEY_PROTOTYPE.md) shows preparation and import. The [component design](COMPONENT_REGISTER_DESIGN.md) specifies the next schema work. Proposed tests and observed defenses need separate fields in that work; a recommendation must never appear as an existing defense.

## Red-team checks cover failure and preservation

The [export tests](../tests/test_survey_register.py) exercise altered saved replies, conflicting claims, missing sources, partial reading, ambiguity, empty runs, output limits, and overwrite attempts. [The repair record](SURVEY_REGISTER_REVIEW.md) describes what these checks establish and what remains open.
