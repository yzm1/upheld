# S02 works as a prototype but needs live and independent checks

Readers are engineers deciding whether to merge or rely on the S02 survey. This review covers the prototype, its example, and method version 1.2 on 6 September 2026. **The earlier S02 completion claim was too strong.** The task is open again until the agreed live adapter and independent source-review checks run.

The review used the source, failure tests, pinned example, current method, and original rule mapping. It did not run a real model CLI or independently measure discovery yield. Passing tests cannot settle those limits.

| Finding | Severity | Before | Repair and remaining limit |
|---|---|---|---|
| Adapter output could grow unchecked during execution | High | Final file size was checked after exit; logs and version output had no size guard | Monitor both output routes during the process and share one time budget across setup and extraction. Tests force excessive logs and final files. Polling can overshoot the threshold |
| Read-only mode did not establish safe external-tool behavior | High | The adapter requested a sandbox but could inherit external connections; invocation lacked an explicit acknowledgment of that limit | Require explicit opt-in to the unverified agent and retain the warning. This does not certify permissions; live checks remain a blocker to claiming readiness |
| Source inspection could conceal partial reading | Medium | One note marked a source inspected without a required extent | Require whole-document or partial reading and an unread-portion description. Reject partial reading that claims no unread portions. These remain reviewer assertions |
| Accurate source lines were difficult for an agent to supply | Medium | Packets supplied whole text but no numbered lines | Include numbered lines alongside the unchanged source; exact quote checks still decide structural validity |
| Historical naming leaked into current presentation | Medium | Current prose repeated the obsolete project name; the page showed old commands without a clear source notice | Use heldtospec in current prose. Add a visible historical-source notice and label verbatim quotes. Preserve source bytes so evidence remains faithful |
| Methodology left bounded reading and model self-checks ambiguous | Medium | Reading scope was unstated; source quotes could be mistaken for established meaning | Method 1.3 defines a reading boundary, separates quoted text from meaning, and requires separately justified oracle criteria |
| Replay was insufficient to close the agreed work | High | S02 was complete despite absent live checks and independent review | Reopen S02. Keep the working prototype and passing replay; require the missing checks before closure |

## The method retains its evidence requirements

All 27 method rule IDs and strengths remain unchanged. P1 now applies to a declared reading boundary with visible omissions. O4's source reading cannot establish a faithful rewrite or true behavior by itself. Repeating the same model's answer does not supply independent evidence.

The method now links S01's outcome definitions and describes the prototype replay's limited meaning. Fault discrimination, type-defense authority, and human binding requirements remain intact. [The rule review](RULE_REVIEW.md) records the changes, and its manifest pins the reviewed text.

## Tests demonstrate the repairs without claiming survey accuracy

The repository suite passed 38 tests on 6 September 2026. Seventeen concern the survey, including new cases for output floods, explicit adapter opt-in, and concealed partial reading. The original example remains preserved; the updated replay reuses its judgments and verifies the unchanged sources.

Independent source labels, meaningful omission rates, real CLI behavior, external-tool limits, and actual review effort remain unknown. The new prototype checks also remain ordinary test results with no accepted Upheld evidence binding.
