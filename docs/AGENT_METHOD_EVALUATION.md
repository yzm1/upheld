# Test whether Upheld improves judgments before adopting the guide

Readers are engineers planning the first agent-method trial. This proposal is dated 7 September 2026. It completes the test-design portion of S11; E01 remains open until exact cases, tools, models, budgets, and scoring rules are committed before running.

No runs or human ratings are reported here. Sample sizes and release conditions below are project proposals, without a claim of statistical power. The [research report](AGENT_METHOD_RESEARCH.md) explains their basis.

## Compare the same agent under controlled conditions

| Arm | Added Upheld support | Question |
|---|---|---|
| A | None beyond the ordinary task prompt | What does this agent already do? Preserve all existing project and safety instructions. |
| B | Full current method supplied as context | Does merely providing the method help? |
| C | Compact guide and worked examples, with fixed reference content supplied | Does the proposed guide help with tools and source access held constant? |
| D | C's core with detailed references loaded on demand | Does selective loading save work without losing rules? |
| E | D plus executable Upheld support | What do the added checks contribute? |
| F | E's guidance and supported checks within the S02 survey workflow | Does orchestration improve discovery or review enough to justify its cost? |

Use fresh sessions and matched task inputs. Hold model version, host, source access, ordinary tools, permissions, and budget constant within each comparison. D changes reference delivery; E deliberately changes executable support. Report those differences. Compare F only on discovery tasks it actually supports; report unsupported tasks separately, without inventing an orchestration result.

First use cases used to build the guide to repair the guide and verify scoring. Then register and run A/B/C on held-out cases. Register D/E/F as a second comparison on a fresh held-out set after their tools work. Include A and C as repeated controls in that stage. Do not select the best prompt using held-out answers or claim all arms were compared in the first stage.

Start with the user's configured CLI. Repeat the selected comparison on other configured clients before claiming portability. Separate explicit invocation from automatic triggering; unsupported client features are reported as such. No paid runs or account changes occur as part of S11 research.

## Prepare cases whose answers can be challenged

Propose 24 held-out cases per stage, split equally across software changes, scientific evidence review, and reproducible data analysis. Two runs per arm give 144 runs for the first three-arm stage. These counts are planning choices dated above. E01 may revise them before any trial after estimating actual cost.

Use source-grounded cases with permission to retain the needed materials. Scientific cases should include claims supported, contradicted, or left unresolved by supplied literature. Analysis cases should use published data and scripts with reproducible results. Software cases need pinned code and relevant documents. Choose exact artifacts under S13; this proposal supplies no invented case results.

Balance known faults, adequate defenses, missing evidence, conflicting sources, and intended-behavior decisions. Cover discovery, change review, defense challenge, probe interpretation, and record proposals. Include work without a register. Keep sources and expected answers in separate stores so agents cannot read the scoring material.

Repo C and the heldtospec examples already shaped Upheld. Use them for development only. Exclude the same fault, adjacent revisions, and paraphrased answers from the held-out set. Existing public benchmarks may be familiar to models; disclose this limit and include newly reviewed source combinations. Split by project or source family, rather than scattering near-duplicates across both sets.

Two reviewers should independently write expected findings and their source support before seeing agent output. A third reviewer resolves disagreements where possible; contested cases retain an unresolved label. Record reviewer expertise and conflicts. If independent reviewers are unavailable, label the run a guide-building exercise and keep the adoption decision open.

## Score useful decisions and their costs separately

| Measure | Rule fixed before running |
|---|---|
| Judgment correctness | Review each material conclusion against sources and the expected check. Mark correct, incorrect, appropriately unresolved, or unscorable. |
| Missed issues | Count missed known findings over all eligible known findings. Retain severity and domain; do not use the agent's own list as the denominator. |
| Unsupported conclusions | Count material claims without sufficient support, including wrong scope and invented observations. Report per output and per claim so verbosity cannot hide errors. |
| Useful discoveries | Count distinct, independently confirmed findings that change a decision or next action. New valid discoveries can extend the answer set only through blinded review of all arms. |
| Human work | Time source inspection, triage, corrections, disagreement resolution, and follow-up. Include rejected suggestions and empty runs. |
| Operating cost | Record elapsed time, tool calls, tokens where exposed, and actual billed cost where available. Keep unavailable cost fields unknown. |
| Main task success | Check whether the requested change or review was completed and whether the original project scope was preserved. |
| Method adherence | Audit rule use separately. High adherence cannot compensate for wrong judgments or wasted effort. |

Blind reviewers to the arm where feasible; normalize presentation without deleting substantive content. Randomize output order. A model judge may help triage, but cannot be the sole outcome judge. Log whether the reviewer accepts, edits, or rejects a suggestion; acceptance alone does not establish correctness.

Pair comparisons by case. Report case-level differences and uncertainty intervals, with source families as the grouping unit where cases are related. Repeated runs are not independent new cases. Show domain results, critical failures, and contested labels beside aggregate results. A small pilot can establish feasibility or expose harm; it cannot establish broad superiority.

## Register limits and stop rules before running

Commit case hashes, source revisions, permitted retrieval, model and host versions, guide hashes, tool versions, prompts, permission settings, run order, repetitions, time and spend limits, and scoring instructions under E01. Record whether clients expose sampling controls; repeated settings do not guarantee identical results.

Estimate cost using early runs before setting a hard total budget. Stop at that budget and publish the incomplete denominator. Count timeouts, malformed outputs, and tool failures as observed outcomes. Permit a replacement only for a documented infrastructure fault under a rule written before the trial; retain the original attempt and its cost.

A fabricated execution, unrequested evidence binding, or change that abandons the user's required scope blocks adoption of that tested guide version. Zero observed critical failures provides limited evidence; it does not prove absence. For the pilot, adopt only when paired results show useful gains without an unresolved increase in serious errors and reviewers can sustain the measured workload. Agree a numerical review-time ceiling under E01 after early timing and before held-out runs. Do not choose it from favorable results.

Automatic triggering needs a separate relevant/irrelevant task set. Count missed invocations, unnecessary audits, and added work. Scope this set and its acceptable error rates before running it. Explicit invocation can remain the supported mode if automatic triggering does not help.

Publish all arms, failed attempts, changes from the registered plan, and unresolved judgments. E07 then records whether to keep, revise, defer, or stop each interface. Research completion never substitutes for those observations.
