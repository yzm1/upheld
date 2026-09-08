# Prepare a source packet and review proposed claims

Readers are engineers running the S02 prototype from this repository. **The prototype collects source documents and writes candidate claims to a schema 0.1 register.** A person or an external agent supplies the judgments. An experimental Codex adapter can request them from a user-configured CLI.

The prototype does not execute probes, grade defenses, or write accepted register entries. The packaged Upheld CLI remains unbuilt. Python 3.10 or later runs the source and import commands without extra packages. Register export uses the validator in `requirements-docs.txt`.

## Replay the heldtospec example from the repository root

Use the recorded run to produce a new register file:

```bash
python -m pip install -r requirements-docs.txt
python tools/survey.py register \
  --run examples/survey-heldtospec/run \
  --out /tmp/heldtospec-proposed.register.json
```

Open the JSON file and the saved [source review](../examples/survey-heldtospec/run/review.html). The export reuses saved judgments. It measures no new discovery yield. [The output guide](SURVEY_REGISTER.md) explains fields, unknown defenses, and unresolved questions.

The recorded packet pins the collector code that produced it. A changed collector creates a different packet ID. Freshly prepared packets need replies that name their own IDs; an old reply remains tied to its original packet.

## Make a new survey boundary explicit

Copy the example manifest and name the repository, revision, component boundary, and selected files. An optional `source_notice` marks historical names or commands in the review page. Each included file needs its SHA-256 digest. Excluded entries need a reason. The script checks file bytes against the manifest; repository and revision labels remain declarations by the person preparing it.

The manifest defines the entire source boundary. Files outside that list remain outside the survey. Include known exclusions explicitly when readers need to see them. Missing files, changed hashes, unsupported formats, and oversized documents remain visible in the inventory.

The first collector accepts whole UTF-8 text documents up to 64 KiB each. It preserves tables, examples, and headings as text. It does not parse images or follow document links. The complete packet must fit within 16 MiB. Narrow the declared boundary when it exceeds those limits; never silently trim a document.

Preparation saves the source text, source hashes, collector hash, instructions, and response schema in `packet.json`. Its content digest identifies the packet. Existing run directories cause an error. Prepare a new directory for changed inputs.

For a new source review, prepare the packet outside the source folder:

```bash
python tools/survey.py prepare \
  --root /path/to/repository \
  --manifest /path/to/survey-manifest.json \
  --run /tmp/new-upheld-survey
```

## Supply judgments through the same response format

Give `packet.json` to a reviewer or existing agent session. Request a JSON response matching `response-schema.json`. The committed response demonstrates the format. State which sources the reviewer inspected and explain a zero-candidate result. Each reviewer declares whole-document or partial reading and describes unread portions. These are reviewer assertions; the tool cannot prove their completeness.

For each candidate, retain its claim, subject, conditions, kind, rationale, uncertainty, and next question. Include a separate check of whether the proposed meaning preserves the source. References must quote complete source lines exactly. Related passages can supply additional references.

Import rejects unknown fields, invented locations, altered quotations, wrong packet IDs, and malformed replies. It does not mechanically verify meaning. Reviewer names and inspection notes are submitted assertions, not authenticated facts. An accepted import means the candidate passed structural and quotation checks.

Each import creates a new attempt record. Rejected attempts retain diagnostics; prior valid submissions remain available. Reports group exact duplicates and leave differing claims visible. Source inspection status means a reviewer reported reading it; it does not establish complete claim coverage.

Import the reply, then write the canonical register:

```bash
python tools/survey.py import \
  --run /tmp/new-upheld-survey \
  --response /path/to/reply.json \
  --reviewer local-review
python tools/survey.py register \
  --run /tmp/new-upheld-survey \
  --out /tmp/new-upheld-proposed.register.json
```

## Configure Codex explicitly before requesting judgments

Create a private JSON config with `executable`, `model`, `timeout_seconds`, and `allow_unverified_agent`. Use your installed executable and chosen model. The adapter requires `allow_unverified_agent: true` after you review its limits. Otherwise use external import. No model account or credentials belong in the repository.

```bash
python tools/survey.py codex \
  --run /tmp/new-upheld-survey \
  --config /path/to/your/codex-survey.json
```

The adapter uses the documented [Codex non-interactive interface](https://developers.openai.com/codex/noninteractive). It sends the packet through stdin and requests a schema-constrained final response. It records the CLI version, model, arguments, elapsed time, and failures. Spend remains unknown.

It requests a read-only sandbox in a temporary working directory and preserves existing user policies and login. It does not certify the installed agent's permissions or disable every configured external connection. Review that setup before use. A local CLI can send source material to a remote model.

This adapter is experimental. Tests exercise its process interface with a fake executable; a real Codex run and permission checks remain pending. Automated cancellation currently requires a Unix-compatible host. Setup and extraction share the time budget. The process monitor stops output that exceeds 1 MiB; polling can overshoot that threshold. Timeout or failure leaves unfinished sources open. Raw agent logs are not retained because they can contain private details.

## Compare runs without merging human decisions

`compare` reports changed source hashes and exact candidate additions or removals. It does not infer renamed claims or reconcile accepted choices. `report` regenerates the readable page from the packet and attempt files. A changed packet digest blocks resume.

Successful commands exit zero. Invalid input, unavailable setup, and rejected replies exit two. These statuses concern the prototype workflow; they carry no evidence grade.

S03 adds code-aware sources; S04 adds richer skeptical triage; S05 adds bounded probes. S08 owns accepted-decision preservation, and S09 owns first-use packaging and live adapter checks. [S11 research](AGENT_METHOD_RESEARCH.md) is complete. [S12 supplies the guide package](UPHELD_SKILL.md); S13 and S14 own reviewed cases and live client trials.
