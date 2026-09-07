# Prepare a source packet and review proposed claims

Readers are engineers running the S02 prototype from this repository. **The prototype collects source documents and validates submitted candidate claims.** A person or an external agent supplies the judgments. An experimental Codex adapter can request them from a user-configured CLI.

The prototype does not execute probes, grade defenses, or write accepted register entries. The packaged Upheld CLI remains unbuilt. Python 3.10 or later runs this script without extra packages.

## Replay the heldtospec example from the repository root

Choose a new output directory outside the source folder:

```bash
python tools/survey.py prepare \
  --root examples/survey-heldtospec/sources \
  --manifest examples/survey-heldtospec/manifest.json \
  --run /tmp/upheld-survey-replay
python tools/survey.py import \
  --run /tmp/upheld-survey-replay \
  --response examples/survey-heldtospec/response.json \
  --reviewer replay
python tools/survey.py report --run /tmp/upheld-survey-replay
python tools/survey.py compare \
  --left examples/survey-heldtospec/run \
  --right /tmp/upheld-survey-replay
```

Open `/tmp/upheld-survey-replay/review.html`. The page shows original quotations, full source context, proposed meanings, uncertainty, and next questions. This replay imports prior judgments. It measures no new discovery yield. [The run report](../examples/survey-heldtospec/README.md) records what actually ran.

## Make a new survey boundary explicit

Copy the example manifest and name the repository, revision, component boundary, and selected files. An optional `source_notice` marks historical names or commands in the review page. Each included file needs its SHA-256 digest. Excluded entries need a reason. The script checks file bytes against the manifest; repository and revision labels remain declarations by the person preparing it.

The manifest defines the entire source boundary. Files outside that list remain outside the survey. Include known exclusions explicitly when readers need to see them. Missing files, changed hashes, unsupported formats, and oversized documents remain visible in the inventory.

The first collector accepts whole UTF-8 text documents up to 64 KiB each. It preserves tables, examples, and headings as text. It does not parse images or follow document links. The complete packet must fit within 16 MiB. Narrow the declared boundary when it exceeds those limits; never silently trim a document.

Preparation saves the source text, source hashes, collector hash, instructions, and response schema in `packet.json`. Its content digest identifies the packet. Existing run directories cause an error. Prepare a new directory for changed inputs.

## Supply judgments through the same response format

Give `packet.json` to a reviewer or existing agent session. Request a JSON response matching `response-schema.json`. The committed response demonstrates the format. State which sources the reviewer inspected and explain a zero-candidate result. Each reviewer declares whole-document or partial reading and describes unread portions. These are reviewer assertions; the tool cannot prove their completeness.

For each candidate, retain its claim, subject, conditions, kind, rationale, uncertainty, and next question. Include a separate check of whether the proposed meaning preserves the source. References must quote complete source lines exactly. Related passages can supply additional references.

Import rejects unknown fields, invented locations, altered quotations, wrong packet IDs, and malformed replies. It does not mechanically verify meaning. Reviewer names and inspection notes are submitted assertions, not authenticated facts. An accepted import means the candidate passed structural and quotation checks.

Each import creates a new attempt record. Rejected attempts retain diagnostics; prior valid submissions remain available. Reports group exact duplicates and leave differing claims visible. Source inspection status means a reviewer reported reading it; it does not establish complete claim coverage.

## Configure Codex explicitly before requesting judgments

Create a private JSON config with `executable`, `model`, `timeout_seconds`, and `allow_unverified_agent`. Use your installed executable and chosen model. The adapter requires `allow_unverified_agent: true` after you review its limits. Otherwise use external import. No model account or credentials belong in the repository.

```bash
python tools/survey.py codex \
  --run /tmp/upheld-survey-replay \
  --config /path/to/your/codex-survey.json
```

The adapter uses the documented [Codex non-interactive interface](https://developers.openai.com/codex/noninteractive). It sends the packet through stdin and requests a schema-constrained final response. It records the CLI version, model, arguments, elapsed time, and failures. Spend remains unknown.

It requests a read-only sandbox in a temporary working directory and preserves existing user policies and login. It does not certify the installed agent's permissions or disable every configured external connection. Review that setup before use. A local CLI can send source material to a remote model.

This adapter is experimental. Tests exercise its process interface with a fake executable; a real Codex run and permission checks remain pending. Automated cancellation currently requires a Unix-compatible host. Setup and extraction share the time budget. The process monitor stops output that exceeds 1 MiB; polling can overshoot that threshold. Timeout or failure leaves unfinished sources open. Raw agent logs are not retained because they can contain private details.

## Compare runs without merging human decisions

`compare` reports changed source hashes and exact candidate additions or removals. It does not infer renamed claims or reconcile accepted choices. `report` regenerates the readable page from the packet and attempt files. A changed packet digest blocks resume.

Successful commands exit zero. Invalid input, unavailable setup, and rejected replies exit two. These statuses concern the prototype workflow; they carry no evidence grade.

S03 adds code-aware sources; S04 adds richer skeptical triage; S05 adds bounded probes. S08 owns accepted-decision preservation, and S09 owns first-use packaging and live adapter checks. [S11 research](AGENT_METHOD_RESEARCH.md) is complete. [S12 supplies the guide package](UPHELD_SKILL.md); S13 and S14 own reviewed cases and live client trials.
