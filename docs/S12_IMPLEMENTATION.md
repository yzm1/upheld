# S12 supplies an exportable guide; live client trials remain open

Readers are engineers reviewing the S12 result. Date: 7 September 2026. The [research and design](S12_DESIGN.md) and [author-led red team](S12_RED_TEAM.md) preceded the skill and packager.

**The guide now covers the five agreed tasks and exports explicit-only packages for Codex, Claude, and Copilot.** Its bundled method retains all 27 rule IDs and strengths. Follow the [use guide](UPHELD_SKILL.md) to export a folder. No account settings or installed skills were changed during this work.

No supported client executable was available here. Packaging checks and the author walkthrough below do not establish agent compliance, live loading, or better judgments. S13, E01, and S14 remain open for those observations.

The later [self-audit](SELF_AUDIT.md) found that these checks missed a wrong source commit and an empty package. Version 0.1.1 repairs those defects and separates failure to inspect. The dated results below describe 0.1.0.

## File checks expose drift without claiming behavior

| Observed check on 7 September 2026 | Result and limit |
|---|---|
| Portable source through the supplied skill validator | Passed. The validator checks frontmatter and scaffold errors. Its accepted fields are narrower than current client extensions; it checks the portable source only. |
| Export each client profile, then move it to a fresh directory | Passed file verification and local-link checks after the move. No reference depends on the original checkout at runtime. Optional external source links still need network access. |
| Change a bundled rule from MUST to SHOULD | Export refused before writing output. The check compares the generated reference with the reviewed source. |
| Change method text and update only the review hash | Export refused until its pinned source changes too. This keeps an old source commit from silently labeling new text. |
| Change, remove, or add an exported file | Manifest checks rejected each altered package. These are file-integrity checks, with no publisher or behavior guarantee. |
| Export into an existing folder | Refused and preserved its sentinel file. |
| Broken, escaping, or symlinked source reference | Refused. The package cannot depend on that unsafe reference. |
| Client controls and permission grants | Tests inspect explicit-only fields and absence of tool grants. Actual host enforcement remains untested. |
| Repository test suite | All 46 tests passed, including eight new packaging tests. No model calls occur in these tests. |

The documentation gate also checks skill prose and links and refuses a stale method copy. It retains the existing schema, rule, and source-snapshot checks. A passing gate does not grade a defense.

## The author walkthrough preserves the limits of known examples

We read the guide against existing source material after writing it. This is an author review in the same context that designed the skill. It is neither a fresh agent trial nor independent outcome review.

| Input and route | Supported result | Remaining check |
|---|---|---|
| [Repo C case](CONNECTLANG_METHOD_CASE.md), defense challenge | Delivery artifacts and helper checks do not establish a connected production defense. The guide asks for the actual call path and retains untested platform scope. | A new client must apply that distinction to an unseen case without being given its answer. |
| [heldtospec register](../examples/heldtospec-contracts/obligations.register.json), CTR-005, record proposal | The saved row describes a conflict between public prose and code, has no defenses, and proposes a next check. It remains a historical candidate for current reinspection. | Read current heldtospec sources before asserting the defect still exists. |
| [heldtospec evidence](../examples/heldtospec-contracts/obligations.evidence.jsonl) and [bindings](../examples/heldtospec-contracts/obligations.bindings.json), probe reading | The evidence file is empty and the binding map is empty. The reported historical suite result supplies no accepted defense evidence. | Obtain a justified fault challenge and actual run record before proposing acceptance. |

During implementation review, the shared `.agents/skills` location exposed a cross-client risk: a Codex-only policy would not control Copilot. Every export now carries the Claude/Copilot flag, and Codex also gets its own policy file. Live parsing remains part of S14.

PR #5's stale S11 sentence is corrected in the [prototype guide](SURVEY_PROTOTYPE.md). S12 closes the package deliverable. It does not close the independent corpus, registered trials, or live support gates.
