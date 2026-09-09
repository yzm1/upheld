# Earlier tools sharpen the value Upheld must demonstrate

Readers are engineers choosing Upheld's next features. **Other tools already fingerprint trace links and test enforcement checks.** Upheld must show useful findings and manageable review work before claiming an advantage.

This review began on 8 September 2026 and was sharpened on 9 September. It checks primary sources, Doorstop code, and Boundver's current design. It does not claim that either project influenced the other or that Upheld's proposed combination is unique. The product checker remains unbuilt.

## Doorstop and Boundver solve the same lower layer

Doorstop saves a stamp for reviewed requirement content and another stamp on a parent link. When the parent changes, the link becomes suspect. Boundver saves fingerprints for declared contracts and follows consumer edges when those fingerprints change.

| Question | Doorstop | Boundver |
|---|---|---|
| What is named? | Requirement item | Component or declared contract |
| What is saved? | Review or parent-link stamp | Lockfile fingerprint |
| What points downstream? | Requirement trace link | Consumer edge |
| What triggers work? | Item fingerprint differs | Contract facet fingerprint differs |
| What gets reported? | Suspect link / unreviewed item | Direct or transitive affected consumer |
| What happens next? | Review or clear | Inspect impact and run targeted checks |

They remain different products. Doorstop centers on requirements and document review. Boundver classifies exact, behavior, boundary, and compatibility drift across component contracts.

The overlap still matters. A tool that stores promise-to-artifact links, hashes them, and requests review after change would mostly rebuild established behavior. [The trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) says where Upheld should start instead: explain why a defense fits, challenge it, record the run, record the person's choice, and recheck the inputs behind that choice.

## Each precedent supplies a concrete lesson

| Source | What it does | What Upheld should do |
|---|---|---|
| [Doorstop item code](https://github.com/doorstop-dev/doorstop/blob/1f5756390bdeeff58fc22e30d5c5a56bb1a81c16/doorstop/core/item.py) | Stores item-review and parent-link stamps separately. Clearing a link does not run a defense. | Keep source change, review need, and observed failure separate. Do not claim novelty for suspect links. |
| [Doorstop defaults](https://github.com/doorstop-dev/doorstop/blob/1f5756390bdeeff58fc22e30d5c5a56bb1a81c16/doorstop/settings.py) | Can initialize review/link state during normal use. | A saved hash does not prove that a person deliberately accepted anything. Refresh must not create a binding. |
| [Doorstop custom validators](https://github.com/doorstop-dev/doorstop/blob/1f5756390bdeeff58fc22e30d5c5a56bb1a81c16/docs/api/scripting.md) | Compares stored reference hashes with current files. | Saving a hash and checking it later do not show that the linked check is good. |
| [Boundver source](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/docs/WHY_BOUNDVER.md) | Fingerprints contract facets and reports direct and transitive consumers. It does not prove compatibility or consumer safety. | Reuse component and change data without treating an edge or unchanged hash as evidence. |
| [ComplianceAsCode test guide](https://complianceascode.readthedocs.io/en/latest/tests/README.html#rule-based-testing) | Creates good and bad states and checks scanner results. | Ask whether the defense can tell a stated fault from a valid state. |
| [NIST component model](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/) and [assessment results](https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/assessment-results/) | Separates reusable control descriptions from scoped runs and evidence. | Keep advice, implemented defenses, runs, and a person's choice distinct. |
| [ExplicitCase maintenance guide](https://download.fortiss.org/public/projects/af3/help/assuranceCases/maintenance.html) | Propagates possible impact; engineers judge the actual effect. | Say which input changed without claiming that the promise is false. |

Doorstop's changelog dates review and link clearance to 2014. Its ordinary item fingerprint omits parent-link stamps, so one direct link can become suspect without making every descendant link suspect.

Bulk review can be a real human choice. The dangerous case is a refresh that silently turns new hashes into acceptance. Preserved evidence bytes still depend on the producer, inputs, and expected result.

## The cited studies support narrower claims

| Study | Supported result and limit |
|---|---|
| [Compliance as Code, March 2026 preprint](https://arxiv.org/html/2603.01520v1) | Fleiss' kappa was 0.18 on a 500-rule sample. Ordered, single-category mapping likely contributed to disagreement. This did not measure defense efficacy. |
| [Requirements quality and trace recovery, June 2026 preprint](https://arxiv.org/html/2606.11834v1) | Effects varied across five methods and two datasets. Test the actual sources; broad claims remain uncertain. |
| [Traceability mapping review, 2021](https://arxiv.org/abs/2108.02133) | Creating and maintaining links is a recurring cost. This paper cannot support the separately described 2023 practitioner study. |

No reviewed source establishes a universal ranking of defense kinds. Judge a proposed check by its scope, bypass paths, faults, expected result, cost, and what remains unknown. A large queue can also reflect a large real change.

## Prior art changes what Upheld should build and test

1. **A fresh link does not prove a good defense.** A suspect or affected link only says that earlier work may need another look.
2. **Advice is not code.** Store a proposed defense separately from an implemented one.
3. **Import rather than duplicate.** Doorstop, StrictDoc, Boundver, build graphs, and external requirements tools can supply candidate promises, stable IDs, locators, and affected links. Their review state does not become evidence or a binding.
4. **Do not rebuild generic graph traversal by default.** Consume Boundver-style topology where available. Add an Upheld support link only when its conditions and grounds are explicit.
5. **Test against the simpler tool.** Maintenance pilots must include an ordinary fingerprinted-link baseline. Upheld's extra records have to earn their review cost.

The [method](METHOD.md) already requires a reason for each defense choice and keeps unknowns visible. The [checker rules](CHECKER.md) separate unchanged inputs from a sound original judgment. The [milestone](MILESTONE.md) now includes the simpler fingerprint baseline.

The [component design](COMPONENT_REGISTER_DESIGN.md) and [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) carry these limits into the next schema work.
