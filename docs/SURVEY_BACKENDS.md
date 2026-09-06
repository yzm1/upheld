# Let users bring their existing agent to the survey

Readers are engineers designing the survey's model interface. **Require an explicit backend choice before sending survey material to a model.** Offer a local path without a generative model and optional adapters for user-configured agent CLIs.

This proposal dates from 6 September 2026. The interface remains unbuilt. Official documentation supports the capabilities below. Codex, Claude, and Copilot executables were unavailable in this workspace; no adapter or paid model call ran.

## Keep interpretation optional and evidence handling local

Upheld should own source inventory, stable source spans, reviewed choices, and validated output. A language model may propose standalone claims, search questions, and evidence relationships. Its output remains a candidate until review.

The non-generative path should collect exact passages, explicit schema rules, and rule matches. It should support term search, duplicate grouping, human claim editing, and imported probe results. Classic relevance ranking can follow once enough reviewer labels exist. Learned text encoders are a separate optional dependency, even when they do not generate prose.

This path trades broader automatic interpretation for predictable source handling and lower setup cost. Its quality depends on source coverage, useful review order, precise rules, and clear questions. Measure those benefits against ordinary human search before adding a model.

## Native CLI adapters are the first implementation candidate

| User choice | Documented interface | Adapter responsibility |
|---|---|---|
| [Codex](https://developers.openai.com/codex/noninteractive) | Non-interactive execution, JSON event output, schema-constrained final output | Set and verify read-only operation; distinguish events from final records; validate locally |
| [Claude Code](https://code.claude.com/docs/en/headless) | Print mode, JSON or streamed output, JSON schema output | Decode its output envelope; respect existing permissions and hooks; validate locally |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-programmatic-reference) | Programmatic prompts and tool controls | Validate returned content locally; test effective permissions and supported output for the installed version |
| Other executable | User-specified executable and argument list | Admit through a versioned capability check; report unsupported behavior explicitly |
| [OpenRouter](https://openrouter.ai/docs/guides/features/structured-outputs) | Model API; structured output depends on the selected model and provider | Use the user's API key; restrict eligible endpoints; package source evidence and validate responses |

A CLI adapter reuses the user's CLI login through that process. It must not copy credentials from the agent's files. Upheld needs no model account. Settings should identify the executable, argument list, chosen model, time budget, and output limit; keep secrets in environment references.

Launch executables directly without a shell. Preserve the user's existing policies. A read-only scan must not gain rights to edit the repository or run arbitrary probes. An adapter that cannot enforce the required limits must remain unavailable for unattended use. Tool approval flags alone do not establish a sandbox.

At setup, check the installed version and run a small capability fixture. Check login, output parsing, stopping behavior, permitted tools, and reported costs where supported. Report unknown costs as unknown. This fixture belongs to implementation; documentation review cannot pass it.

## Treat agent protocols and model APIs as different options

[Agent Client Protocol](https://agentclientprotocol.com/get-started/agents) offers a shared connection interface, with adapters for some agents. [Copilot's Agent Client Protocol server](https://docs.github.com/en/copilot/reference/copilot-cli-reference/acp-server) is documented as public preview. Protocol support does not make login, tool policy, or structured output identical.

Start with the smallest native adapters needed for the pilots. Evaluate Agent Client Protocol as a way to reduce adapter code after those interfaces work. Keep its use optional and versioned while capabilities differ.

OpenRouter supplies model responses rather than a configured coding agent. Upheld must supply the evidence packet and any permitted tool workflow. Use [provider routing controls](https://openrouter.ai/docs/guides/routing/provider-selection) to constrain endpoints and required parameters. Disable unrequested provider fallback by default.

Explain which material leaves the machine before enabling a backend. A local CLI can still use remote inference. Record selected endpoints and apply the user's [data-handling requirements](https://openrouter.ai/docs/guides/privacy/data-collection); do not promise privacy merely because the user supplied the key.

## Failures must leave a resumable review queue

| Event | Required behavior |
|---|---|
| Missing CLI or authentication | Explain setup failure; allow the non-generative path |
| Timeout, cancellation, or budget exhaustion | Preserve completed candidates and mark unfinished sources |
| Invalid output or invented source locator | Reject the affected result; retain diagnostics and original input |
| Conflicting model judgments | Preserve disagreement for review; do not silently choose a defense |
| Source text contains agent instructions | Treat it as evidence data; it cannot authorize tools or change policies |
| Rescan changes an accepted claim | Expose a conflict; preserve the human decision and evidence binding |

Use separate permissions for reading evidence and executing probes. Require bounded execution and an actual run record for any probe. Neither successful model output nor a completed survey creates accepted evidence. The existing checker consumes reviewed records and never reruns the model.

S02 owns the repeatable scan and capability fixtures; S04 owns uncertain review outcomes; S08 owns preserved choices; S09 owns setup and first use. These tasks remain open. [S01's research](SURVEY_RESEARCH.md) supplies the rationale and comparison plan.
