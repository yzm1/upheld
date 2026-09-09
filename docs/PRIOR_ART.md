# Earlier tools sharpen the value Upheld must demonstrate

Readers are engineers choosing Upheld's next features. **Fingerprint-based trace links and tests of enforcement checks have established precedents.** Upheld must demonstrate useful findings and manageable review work before claiming an advantage.

This review, dated 8 September 2026 and sharpened on 9 September 2026, checks primary sources, Doorstop code, and Boundver's current design. It is a focused comparison. It establishes no historical influence between projects and no claim that the proposed combination is unique. The product checker remains unbuilt.

## Doorstop and Boundver meet at the trace-freshness layer

Doorstop's suspect-link mechanism and Boundver's contract-drift mechanism have the same lower-level shape: record an identity for something previously accepted, retain a relationship to downstream work, and surface that relationship when the recorded identity no longer matches.

| Primitive | Doorstop | Boundver |
|---|---|---|
| Named object | Requirement item | Component or declared contract |
| Recorded identity | Review or parent-link stamp | Lockfile fingerprint |
| Relationship | Requirement trace link | Consumer edge |
| Change signal | Item fingerprint differs | Contract facet fingerprint differs |
| Downstream result | Suspect link / unreviewed item | Direct or transitive affected consumer |
| Follow-up | Review or clear | Inspect impact and run targeted checks |

They are not the same product. Doorstop is requirements-centric; Boundver classifies exact, behavior, boundary, and compatibility drift across declared component contracts. The important conclusion is narrower: **fingerprinted trace freshness and generic affected-relationship propagation are established prior art.** If Upheld only stored promise-to-artifact links, hashed them, and requested review when they changed, it would largely reimplement this layer.

The architectural consequence is recorded in [the trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md): Upheld may consume or minimally reproduce identity and impact context, but its differentiating responsibility begins with the reason to rely on a defense, the challenge of that defense, scoped evidence, explicit acceptance, and honest invalidation of changed grounds.

## Each precedent supplies a concrete design lesson

| Source | Established behavior | Upheld consequence |
|---|---|---|
| [Doorstop item code](https://github.com/doorstop-dev/doorstop/blob/develop/doorstop/core/item.py) | Item review and parent-link clearance store fingerprints separately. Clearing a link does not run a defense. | Separate source changes, a need for review, and an observed failure. Do not claim novelty for suspect-link detection. |
| [Doorstop defaults](https://github.com/doorstop-dev/doorstop/blob/develop/doorstop/settings.py) | Validation can initialize review/link state as part of ordinary workflow. | A recorded hash alone cannot establish deliberate human acceptance. Refresh must not manufacture a binding. |
| [Doorstop custom validators](https://github.com/doorstop-dev/doorstop/blob/develop/docs/api/scripting.md) | A documented extension compares stored reference hashes with current files. | Capturing a hash and checking it later are separate capabilities; neither grades enforcement adequacy. |
| [Boundver source](https://github.com/yzm1/boundver/blob/main/docs/WHY_BOUNDVER.md) | Fingerprints declared contract facets and reports direct and transitive consumers of changed contracts. It explicitly does not prove compatibility or consumer safety. | Reuse component and change context without treating a dependency or unchanged fingerprint as evidence. |
| [ComplianceAsCode test guide](https://complianceascode.readthedocs.io/en/latest/tests/README.html#rule-based-testing) | Creates compliant and noncompliant states and checks scanner decisions. | Test whether the defense distinguishes a stated fault from a valid state. |
| [NIST component model](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/) and [assessment results](https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/assessment-results/) | Separate reusable control descriptions from scoped assessments, observations, and evidence. | Keep recommended defenses, implemented defenses, observed runs, and choices to rely on them distinct. |
| [ExplicitCase maintenance guide](https://download.fortiss.org/public/projects/af3/help/assuranceCases/maintenance.html) | Propagates potential impact; engineers judge actual effects. | Report which ground changed without inferring that the promise is false or the defense is necessarily inadequate. |

Doorstop's changelog dates review and clearance to 2014. Its ordinary item fingerprint omits parent-link stamps. A change can therefore make a direct link suspect without making every descendant link suspect.

Bulk review can record a legitimate explicit choice. The failure to prevent is silent acceptance during refresh. Preserved evidence bytes still require trust in the producer, inputs, and expected result.

## The cited studies support narrower claims

| Study | Supported result and limit |
|---|---|
| [Compliance as Code, March 2026 preprint](https://arxiv.org/html/2603.01520v1) | Fleiss' kappa was 0.18 on a 500-rule validation sample. Ordered, single-category mapping likely contributed to disagreement. This did not measure defense efficacy. |
| [Requirements quality and trace recovery, June 2026 preprint](https://arxiv.org/html/2606.11834v1) | Effects varied across five methods and two datasets. Evaluate actual sources; broad generalization remains uncertain. |
| [Traceability mapping review, 2021](https://arxiv.org/abs/2108.02133) | Establishing and maintaining links is a recurring cost. This is the paper cited in the supplied report; it cannot substantiate the separately described 2023 practitioner study. |

Neither the reviewed evidence nor the current pilot data establishes a universal ordering of defense kinds. Judge each proposed check by its scope, bypass paths, faults, expected result, cost, and residual uncertainty. A large queue alone cannot establish poor quality: a large real change can affect many defenses.

## Prior art changes both architecture and evaluation

The comparison implies five concrete constraints.

1. **Freshness is not adequacy.** A suspect or affected relationship says previous grounds need attention; it does not say the promise is false or the defense is bad.
2. **Recommendation is not implementation.** A proposed defense pattern needs its own state and must not appear as an existing defense.
3. **Import rather than duplicate.** Doorstop, StrictDoc, Boundver, build graphs, and ALM exports can supply candidate obligations, stable IDs, locators, and impact context. Their review state does not become evidence or acceptance.
4. **Generic dependency traversal is not an Upheld moat.** Component work should consume Boundver-style topology where available and add semantic support only when Upheld can state the conditions and grounds.
5. **Evaluate against the simple baseline.** Maintenance pilots must compare Upheld with ordinary fingerprinted trace/suspect-link behavior, not only with manual work or no tool. Upheld's extra ontology has to earn its review cost.

## The method and trials now carry these conclusions

The [method](METHOD.md) requires reasons for a defense choice and preserves uncertainty. The [checker rules](CHECKER.md) separate fresh grounds from a sound original judgment. The [milestone](MILESTONE.md) measures useful findings, misses, false links, and review time.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) exercises an existing README checker with seeded faults and simulated acceptance. Component ownership, shared claims, and unsupported cycles remain in [the component design](COMPONENT_REGISTER_DESIGN.md). The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) now constrains that work so it does not grow into a second generic dependency engine.
