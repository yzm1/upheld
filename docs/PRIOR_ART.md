# Earlier tools sharpen the value Upheld must demonstrate

Readers are engineers choosing Upheld's next features. **Fingerprint-based trace links and tests of enforcement checks have established precedents.** Upheld must demonstrate useful findings and manageable review work before claiming an advantage.

This review, dated 8 September 2026, checks primary sources and Doorstop 3.2 code. It is a focused comparison. It establishes no historical influence between projects and no claim that the proposed combination is unique. The product checker remains unbuilt.

## Each precedent supplies a concrete design lesson

| Source | Established behavior | Upheld consequence |
|---|---|---|
| [Doorstop 3.2 item code](https://github.com/doorstop-dev/doorstop/blob/b4f7f623010f131f5fde37212dde61019ffcf720/doorstop/core/item.py) | Item review and parent-link clearance store fingerprints separately. Clearing a link does not run a defense. | Separate source changes, a need for review, and an observed failure. |
| [Doorstop defaults](https://github.com/doorstop-dev/doorstop/blob/b4f7f623010f131f5fde37212dde61019ffcf720/doorstop/settings.py) | Validation initializes new reviews and link stamps by default. | A recorded hash alone cannot establish deliberate human acceptance. |
| [Doorstop custom validators](https://github.com/doorstop-dev/doorstop/blob/b4f7f623010f131f5fde37212dde61019ffcf720/docs/api/scripting.md) | A documented extension compares stored reference hashes with current files. | Capturing a hash and checking it later are separate capabilities. |
| [Boundver source](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/README.md) | Reports direct and transitive consumers of changed declared contracts. | Reuse component and change context without treating a dependency as evidence. |
| [ComplianceAsCode test guide](https://complianceascode.readthedocs.io/en/latest/tests/README.html#rule-based-testing) | Creates compliant and noncompliant states and checks scanner decisions. | Test whether the defense distinguishes a stated fault from a valid state. |
| [NIST component model](https://pages.nist.gov/OSCAL/learn/concepts/layer/implementation/component-definition/) and [assessment results](https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/assessment-results/) | Separate reusable control descriptions from scoped assessments, observations, and evidence. | Keep proposed defenses, observed runs, and choices to rely on them distinct. |
| [ExplicitCase maintenance guide](https://download.fortiss.org/public/projects/af3/help/assuranceCases/maintenance.html) | Propagates potential impact; engineers judge actual effects. | Report which ground changed without inferring that the promise is false. |

Doorstop's [changelog](https://github.com/doorstop-dev/doorstop/blob/b4f7f623010f131f5fde37212dde61019ffcf720/CHANGELOG.md) dates review and clearance to 2014. Its ordinary item fingerprint omits parent-link stamps. A change can therefore make a direct link suspect without making every descendant link suspect.

Bulk review can record a legitimate explicit choice. The failure to prevent is silent acceptance during refresh. Preserved evidence bytes still require trust in the producer, inputs, and expected result.

## The cited studies support narrower claims

| Study | Supported result and limit |
|---|---|
| [Compliance as Code, March 2026 preprint](https://arxiv.org/html/2603.01520v1) | Fleiss' kappa was 0.18 on a 500-rule validation sample. Ordered, single-category mapping likely contributed to disagreement. This did not measure defense efficacy. |
| [Requirements quality and trace recovery, June 2026 preprint](https://arxiv.org/html/2606.11834v1) | Effects varied across five methods and two datasets. Evaluate actual sources; broad generalization remains uncertain. |
| [Traceability mapping review, 2021](https://arxiv.org/abs/2108.02133) | Establishing and maintaining links is a recurring cost. This is the paper cited in the supplied report; it cannot substantiate the separately described 2023 practitioner study. |

Neither the reviewed evidence nor the current pilot data establishes a universal ordering of defense kinds. Judge each proposed check by its scope, bypass paths, faults, expected result, cost, and residual uncertainty. A large queue alone cannot establish poor quality: a large real change can affect many defenses.

## The method and trials now carry these conclusions

The [method](METHOD.md) requires reasons for a defense choice and preserves uncertainty. The [checker rules](CHECKER.md) separate fresh grounds from a sound original judgment. The [milestone](MILESTONE.md) measures useful findings, misses, false links, and review time.

The [development lifecycle](EVIDENCE_LIFECYCLE.md) exercises an existing README checker with seeded faults and simulated acceptance. Component ownership, shared claims, and unsupported cycles remain in [the component design](COMPONENT_REGISTER_DESIGN.md). Their file layout and support rules still need the S15 schema work.
