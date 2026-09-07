# Ship a small method guide that works from a copied folder

Readers are engineers building the first Upheld skill. Research and design date: 7 September 2026. This document precedes implementation. The [design challenge](S12_RED_TEAM.md) records the review and resulting changes.

**Use one portable core, bundled rule references, and a packager that adds explicit-only controls for the selected client.** Keep the skill outside automatic discovery paths in this repository. Users choose whether and where to install it. The package needs no new account, remote service, or product evidence command.

S12 delivers the guide and checks its packaging. S14 must still demonstrate live loading and behavior in each configured client. No supported client executable is available in this workspace. S13 and E01 remain responsible for independently reviewed cases and trials that measure benefit.

## Research narrows the design beyond S11

The [S11 report](AGENT_METHOD_RESEARCH.md) covers empirical skill studies, scientific claim review, and rubric-guided reasoning. This follow-up searches primary documentation for authoring, invoking, distributing, and testing the actual package. Searches on 7 September 2026 included “agent skills evaluating skills,” “skill creator best practices,” and each client's invocation controls. We inspected official specifications and practical examples, including their limitations. This is a focused review, without an exhaustive literature-screening claim.

| Primary source, checked 7 September 2026 | Finding | Design consequence |
|---|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | The core uses a named folder, frontmatter, and optional supporting files. Tool pre-approval is experimental and varies by client. | Keep the core portable. Omit tool grants; existing host permissions remain in force. |
| [Authoring guidance](https://agentskills.io/skill-creation/best-practices) | Concise instructions and selective reference loading reduce irrelevant context; references should have clear read conditions. | Keep task scope and evidence limits in the entrypoint. Load the full rules before grading a defense or proposing formal records. |
| [Skill evaluation guide](https://agentskills.io/skill-creation/evaluating-skills) | Uses realistic requests, fresh contexts, a no-skill control, and separately recorded outputs and costs. It permits refining assertions after early outputs. | Use that loop for development. Freeze scoring before held-out trials under E01; keep expected answers outside the shipped skill. |
| [Description testing](https://agentskills.io/skill-creation/optimizing-descriptions) | Triggering depends on the description; both missed and irrelevant triggers matter. | Name the Upheld review request precisely. Explicit-only use is the agreed starting mode; automatic triggering remains a separate S14 trial. |
| [Codex skill controls](https://learn.chatgpt.com/docs/build-skills) | `agents/openai.yaml` can set `allow_implicit_invocation: false`. | The Codex package includes that policy and an explicit `$upheld` prompt. |
| [Claude Code skill controls](https://code.claude.com/docs/en/skills) | `disable-model-invocation` controls automatic use. `allowed-tools` grants permission rather than limiting all tools. | Add the explicit-only field to the Claude package. Do not advertise a read-only sandbox supplied by the skill. |
| [Copilot CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) | Documents the explicit-only field and several discovery locations. Surface and configuration affect loading. | Add that field to the Copilot package. Document the exact intended location, with live support still untested. |
| [Agent evaluation practice](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), January 2026 | Describes tasks, repeated trials, graders, traces, and outcome checks as distinct parts of agent evaluation. | Package checks establish file properties. Agent judgment and task outcome require a different trial and independent review. |

Provider documentation is evidence about intended interfaces. It supplies no Upheld performance result. The local skill validator also accepts a narrower frontmatter set than current Claude and Copilot documentation. Validate the portable source with it; test rendered client controls separately. Do not modify the validator to hide the difference.

## The user gets help with a decision, without adopting a register first

The first user is an engineer already using an agent to review code or investigate a claim. The useful result is a supported finding or a smaller, well-defined next check. It should remain useful when the project has no Upheld files.

| Choice | Benefit | Cost and rejected alternative |
|---|---|---|
| One core plus generated client packages | Fix guidance once; preserve the same method across hosts. | A small packaging script needs tests. Three hand-maintained copies would drift. |
| Local rule reference pinned to the source commit | Reading rules works after copying the folder and without network access. | Bundled text adds size. Live retrieval alone could fail or silently change the method. |
| Conditional full-rule reading | Short reviews need little setup; evidence judgments can inspect exact rules. | Agent compliance remains uncertain. Putting all rules in the entrypoint would impose that cost on every request. |
| Prose record proposals first | Users can review claims without trusting an exporter. | Formal export still needs current schemas and product checks. No automatic evidence or binding writer ships here. |
| Explicit client choice, fresh output directory | Packaging does not discover or modify accounts, project rules, or existing installs. | Installation remains a deliberate local step. Automatic global installation would widen this task. |
| No runtime scripts in the skill | Existing agent tools can inspect sources and run authorized probes. | The guide cannot enforce its own judgments or permissions. New execution tools need a measured use under S14. |

There is no added service fee or separate model dependency. Actual agent cost remains unknown until live trials. Record tokens, elapsed time, and review effort before judging whether the guide earns its cost. A larger package or a cleaner report is insufficient evidence of value.

## Keep the core short and the rules exact

The entrypoint defines promise, delivery, defense, evidence, and binding. It preserves the user's scope, identifies unread sources, and prohibits promotion of a proposal into an observed result. Its task routes cover discovery, change review, defense challenge, probe reading, and proposed records.

Bundle the normative portion of the current method, preserving all 27 rule IDs, strengths, and surrounding qualifications. Rewrite external links to the pinned source revision. This deliberate copy is the method the skill teaches; it is generated from the maintained document rather than edited separately. Keep the Repo C lesson in a small worked reference, clearly attributed and excluded from held-out tests.

The packager checks the reference against the maintained source before export and records file hashes in the output manifest. Hashes detect drift relative to this checkout. They do not authenticate a publisher or prove that the method is current online. A missing or conflicting reference limits the result to provisional findings.

## Implement only after the design challenge

Write the core and worked reference, generate the rule reference, and add a standard-library packager. It must reject existing output paths and unsafe source links, preserve copied bytes, and produce client-specific controls without broad permissions. Add meaningful tests for drift, relocation, output refusal, and package contents. Include maintained skill prose and links in the documentation gate.

Use the existing Repo C and heldtospec material for an author walkthrough, with its contaminated context stated. A walkthrough cannot close S14 or support a gain claim. Close S12 only with the package, observed structural checks, walkthrough limits, and concrete install instructions. The [red-team record](S12_RED_TEAM.md) must precede those files and remain linked after fixes.
