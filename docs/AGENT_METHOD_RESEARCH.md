# Start with an opt-in method guide and measure its effect

Readers are engineers deciding how agents should use Upheld during ordinary work. This S11 research report is dated 7 September 2026.

**Build a small, explicitly invoked guide with versioned reference files first.** Add local checks where they can establish facts. Keep the user's configured Codex, Claude, or Copilot CLI as the host. A new server and model training need evidence of a problem that this simpler route cannot solve.

This is a supported choice for a prototype. No comparative Upheld agent trial ran during this research. Official support for loading skills establishes an interface feature; it does not establish better judgments. The [test proposal](AGENT_METHOD_EVALUATION.md) describes how to challenge the choice. S12–S14 in [TODO](../TODO.md) carry the work that follows.

## The search includes evidence review and tests of harmful guidance

We searched primary papers and official documentation on 7 September 2026. Query families covered agent skills and repository instructions; rubric-guided judgments; scientific claim checking and risk-of-bias review; tool-assisted reasoning; and behavioral tests. We followed relevant primary links from those results. The table records the sources that support this decision, including negative findings.

This is a focused research review, without a registered systematic search or exhaustive screening count. Papers describe their tested tasks and models. Provider pages describe interfaces available at retrieval time. The proposed uses below reflect our reading of those sources. We did not reproduce the papers' experiments. New preprints carry less weight than independently repeated results; none supplies an Upheld success rate.

## More guidance can help or harm

| Primary source and date | What it establishes | Transfer and limit |
|---|---|---|
| [Evaluating AGENTS.md](https://arxiv.org/html/2602.11988v1), February 2026 preprint | Tested repository context files across coding agents; added context tended to reduce task success and increase cost. Agents followed instructions and explored more. | Measure unnecessary work and task success. Following the method is insufficient. Repository navigation guidance differs from an explicitly requested judgment procedure. |
| [SkillsBench](https://arxiv.org/html/2602.12670v1), February 2026 preprint | Curated skills helped on average across diverse artifact tasks, with substantial task variation. Skills can bundle scripts and resources alongside prose. | Compare guide text with tools held constant. The inspected version has inconsistent task totals and headline gains across sections; do not reuse its headline effect as an expected Upheld gain. Curated bundles do not isolate the effect of instructions. |
| [G-Eval](https://aclanthology.org/2023.emnlp-main.153/), December 2023 | Criteria, generated evaluation steps, and forms improved agreement with human ratings on summarization and dialogue tasks. The paper also reports concern about preference for model-generated text. | Use explicit review questions and inspectable answers. Human agreement on text quality does not establish that a software defense works. |
| [Prometheus](https://arxiv.org/abs/2310.08491), October 2023 preprint | A trained evaluator applies supplied rubrics and reference answers. | A useful comparator for custom criteria, but training and reference answers add costs absent from a portable guide. Defer training until simpler methods fail on reviewed cases. |
| [Self-correction study](https://arxiv.org/abs/2310.01798), October 2023, and [key-condition checking](https://aclanthology.org/2024.emnlp-main.714/), November 2024 | The former finds failures of reasoning correction without external feedback; the latter improves correction using a specific prompting procedure. | Self-review can generate better questions. It does not create independent execution evidence. Neither result warrants a universal claim about all models. |
| [ReAct](https://arxiv.org/abs/2210.03629), October 2022 | Interleaving reasoning with actions lets an agent obtain external information and feedback on studied tasks. | Separate source lookup, proposed checks, actual observations, and conclusions. A tool result still needs a justified connection to the claim. |
| [CheckList](https://aclanthology.org/2020.acl-main.442/), July 2020 | Tests organized by capability and behavior expose failures that aggregate accuracy can hide. | Test missing sources, conflicting claims, irrelevant triggers, and failed probes separately. A clean aggregate score must not hide invented evidence. |

The differing results from context-file studies and SkillsBench help us choose what to test. They test different instructions, bundles, tasks, and agents. Averaging their scores would hide those differences. Upheld needs matched comparisons of its own guide, including cases where the correct response is to leave working behavior alone.

## Evidence-review tools supply a better model than an audit checklist

| Primary source and date | What the tool or method does | Proposed Upheld transfer |
|---|---|---|
| [Cochrane risk-of-bias guidance](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-08), accessed 7 September 2026 | Uses questions about the study to propose a judgment; assessors may override defaults with reasons. | Ask for source-backed answers before a conclusion. Preserve unanswered questions and human reasons. Its medical rules and overall rating scheme do not become Upheld rules. |
| [RobotReviewer user study](https://abstracts.cochrane.org/2019-santiago/using-robotreviewer-assist-humans-conducting-risk-bias-assessments-randomized-user), 2019 conference abstract | Compared manual review with machine-suggested judgments and highlighted passages. Reviewers could change both. Assisted review was quicker in this study. | Present claim, passage, and editable judgment together. Measure review time and corrections. Acceptance of a suggestion does not establish its independent correctness; the abstract is limited evidence. |
| [SciFact](https://aclanthology.org/2020.emnlp-main.609/), November 2020; [working code and data](https://github.com/allenai/scifact) | Separates finding relevant abstracts, selecting evidence sentences, and deciding whether they support or refute a scientific claim. | Score source retrieval separately from claim judgment. A correct quotation can still support the wrong conclusion. Include evidence-insufficient cases. |
| [SciFact-Open](https://aclanthology.org/2022.findings-emnlp.347/), December 2022 | Studies claim checking against a much larger literature collection, using pooled candidate evidence and human labels. | Test bounded packets and open retrieval separately. Failure to find support in a packet is a search limit, not proof that no support exists. |
| [Goal Structuring Notation standard](https://scsc.uk/resources/citation_r1386.html), version 3, 2021 | Defines a notation and guidance for constructing and reviewing engineering arguments. | Make the reasoning connecting a claim to evidence visible. A well-formed argument remains open to challenge. A diagram is optional; the underlying links matter. |

These examples support a procedure with reviewable intermediate answers. For Upheld, the key questions are: What is promised? What would refute it? What implements it? What detects a violation? What observed check shows that detection works? Which production connections and assumptions remain untested?

[Repo C's extended response](CONNECTLANG_METHOD_CASE.md) supplies a real example of those distinctions. A compiler helper and its local tests existed while a production path remained unwired. That case informs the guide; it cannot independently demonstrate the guide's benefit.

## Existing clients can host the first version

| Interface and official source, checked 7 September 2026 | Supported use | Decision |
|---|---|---|
| [Agent Skills format](https://agentskills.io/specification) | A folder contains a guide, metadata, and optional references or scripts; clients can load detail as needed. | Use a portable core and pinned references. Keep essential evidence limits in the core so a missed reference cannot silently authorize stronger claims. |
| [Codex skills](https://learn.chatgpt.com/docs/build-skills) | Packages task instructions, resources, and optional scripts. | First candidate host through the user's configured CLI. Actual loading, permissions, and behavior still need S14 checks. |
| [Claude Code skills](https://code.claude.com/docs/en/skills) | Supports skills and controls over invocation, including `disable-model-invocation`. | Begin with explicit invocation. Provider-specific settings belong in a small installation note; they are not portable security controls. |
| [Copilot skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) and [setup](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | Loads relevant skill instructions and bundled resources. | Check the exact CLI or editor surface separately. Shared format does not imply identical triggering or tool permissions. |
| Local commands and structured files | Upheld already has a [survey prototype](SURVEY_PROTOTYPE.md); product evidence commands remain unbuilt. | Reuse source packets and checked imports where applicable. Add deterministic checks only for facts they can establish. |
| [Model Context Protocol tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools), versioned specification | Exposes callable operations with structured inputs and results. | Defer a server. Add one only if tested clients need a shared tool service that local commands cannot reasonably supply. Tool exposure does not teach the method by itself. |

A reference pack alone is the lowest-cost control. A skill adds discoverable entry instructions. Retrieved references reduce initial context but can be missed. A structured procedure makes omissions easier to inspect but can force irrelevant work. Executable checks establish bounded facts at a maintenance cost. Survey orchestration adds source collection and review state but also setup work. The trial compares these effects rather than treating each added layer as progress.

The user keeps their existing agent account and CLI settings. An OpenRouter-style backend remains optional under [S01's backend proposal](SURVEY_BACKENDS.md). It must provide its own host workflow and tool permissions; a model endpoint alone does not implement skill loading.

## The guide must preserve the method's evidence limits

The minimum core should define promise, delivery, defense, gap, observed evidence, and human binding. A binding is a person's acceptance of evidence for one defense. It must preserve source boundaries, uncertainty, the project's intended scope, and the difference between proposing a check and observing one.

The following audit covers all 27 IDs in [method 1.3](METHOD.md). It changes no normative rule or strength. Detailed record and oracle rules stay in versioned references. An oracle is a separately justified criterion for the expected result.

| Method IDs | Guidance an agent needs | Check beyond prose |
|---|---|---|
| P1, P2, P3, S1 | Read a declared scope; expose unread sources; retain promises lacking code; probe behavior before recording it as evidence. | Source manifests, read logs, and actual probe records. Logs alone do not prove understanding. |
| O1, O3, O5 | State a refutable claim, the check that would catch it, and the next unresolved question. | Human review of meaning and relevance. |
| O2, O9, V1 | Choose the mechanism from behavior; keep gaps and environment needs separate. | Schema checks can reject absent fields; reviewers must assess the choice. |
| O4, O6, O7 | Separate quoted reading, candidate links, and observed evidence with its revision. | Quote and locator checks; run and revision capture. Matching bytes do not prove faithful interpretation. |
| O8, O10 | Reassess changed grounds; distinguish live, latent, impossible, and unknown reachability. | Future basis checks and probes of enabling conditions; conservative unknowns where unsupported. |
| V2, V3, V4, V5, V6 | Require actual execution and a justified fault model; distinguish clean, violated, and unable to inspect. | Real checks against faults, clean cases, and inspection failures. A compiler cannot establish its own soundness through acceptance alone. |
| H1, X1, X2, D1 | Show unresolved work; use code-derived exit criteria; check intended occasions; name deferred-feature triggers. | Baselines and observed scheduled runs. These product checks remain unbuilt where the TODO says so. |
| Rp1, Rp2, Rp3 | Date and source numbers, label unrun claims, and read the full report before sharing. | Source audit and whole-report review; a prose checker cannot establish that a human reviewed it. |

Use task-specific routes: discover promises without requiring a register; review a change against affected promises; challenge a defense; interpret a probe; or propose records for review. Each route returns a bounded result and unresolved questions. It must not turn a small code edit into an unsolicited full-project survey.

Each proposed finding should carry the task boundary, source locator and revision, relevant quotation, claim, delivery path, candidate defense, concise justification, counterevidence, uncertainty, and next check. Include actual run links only when available. Record proposals separately from accepted bindings. Support ordinary prose when no register exists; add structured export only when the user needs it.

## Failure behavior is part of the interface

| Failure | Required response and trial challenge |
|---|---|
| Stale or conflicting guidance | Show the method version and conflict. Preserve higher-priority instructions and the user's project mandate; seek a decision on unresolved intended behavior. Test an old reference beside a newer rule. |
| Source text gives the agent commands | Treat retrieved passages as evidence to inspect. Test a source that asks for evidence fabrication or unrequested writes; host permissions remain authoritative. |
| Tool is absent or cannot inspect | Report the missing capability and next step. Test missing executables, denied access, timeouts, and malformed results. |
| Quote is accurate but conclusion is wrong | Retain exceptions and opposing passages. Test narrowed conditions, wrong revisions, and irrelevant quotations. |
| Local component works but production chain does not | Trace the required calls and assumptions. Use Repo C for teaching and different cases for measurement. |
| Agent invents a run or accepts its own proposal | Require an actual linked observation; keep human acceptance separate. Any such failure blocks release of that tested version. |
| Checklist completion displaces the project goal | Keep original deliverables visible. Test a suggestion to defer an essential feature merely to make the register clean. |

## S11 closes research; the benefit remains unmeasured

We will prototype the compact guide, preserve the full method as a comparator, and test added tools separately. S12 implements the guide; S13 prepares independently reviewed cases; S14 checks real clients and the staged comparison. E01 must register exact trials before execution. If the guide adds review work without useful findings, shorten it or stop shipping it. If tools account for the gains, ship those tools without claiming the prose caused them.

On 7 September 2026, `python tools/check_docs.py` passed for all 38 current documents, including links, schemas, snapshot hashes, and the supplied prose checks. This verifies document checks only. It does not show that agents make better calls.
