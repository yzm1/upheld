# A fault challenge now continues through evidence and review

Readers are engineers implementing the next checker slice. **The development probe runs Upheld's README checker, records its fault challenge, and keeps changed grounds stale after regeneration.** Its acceptance is simulated. It creates no human bindings and does not implement the product CLI.

## Run the bounded case from a checkout

Install the packages in `requirements-docs.txt`, then choose a new output path:

```bash
python tools/probe_evidence_lifecycle.py --output /tmp/upheld-lifecycle-new.json
python -m unittest discover -s tests -p 'test_evidence_lifecycle.py'
```

The probe copies the existing `UPH-001` promise, README checker, and its declared inputs into a temporary directory. It runs the checker against clean inputs, a wrong count, the historical false claim, and a missing input. It also weakens the checker to return no findings; that mutant misses the wrong count.

The output retains commands, outputs, times, input hashes, expected outcomes, an evidence record, and a labeled simulated binding. Existing output paths and symlinks are refused. The project's registers, logs, and bindings remain untouched.

## The case distinguishes freshness from a new judgment

| Case | Expected result |
|---|---|
| Candidate with no choice to rely on evidence | open |
| Simulated binding with unchanged grounds | still_valid |
| Changed subject, promise, checker, or declared input | review_required, with the changed ground named |
| Regenerated view after a subject edit | review_required |
| Relocated checker | invalid; relocation is unresolved |
| Missing declared input or evidence | unresolvable |
| Altered evidence bytes retaining their old identity | invalid |

The tests also reject wrong defense IDs, unsupported scopes and profiles, and inconclusive or contradictory records. These checks exercise a closed case. They do not authenticate a producer's claims or establish that arbitrary prose is correct.

## The development profile does not settle product hashing

`development/readme-byte-snapshot/v1` hashes exact file bytes and sorted compact JSON. It separates the claim, defense assertion, artifacts, subject, and declared inputs. A sorted path list detects added or removed fixture files. It rejects symlinks and supports one checker over one README.

The record ID hashes the evidence fields other than the ID itself. The result file uses exclusive creation. This detects changes under the recorded identity; it provides no signed identity, external timestamp, or durable append-only service.

The actual run is a seeded working snapshot. Its source revision names the current checkout commit; its hashes identify the copied working files. Runtime context remains in the evidence's execution fields. Acceptance is a test decision with no human actor claim.

## Product conformance and review cost remain open

C01–C10 still require product hash vectors, commands, execution policy, evidence lineage, and real human binding. The demo has no generic resolver, component graph, circular support rule, or cache. S15–S17 and the independent discovery and upkeep trials remain open.

The [run record](../measurements/lifecycle-2026-09-08/observation.json) reports the local results. It is development data and must stay outside held-out agent trials. Replaying it cannot establish useful findings per reviewer hour.
