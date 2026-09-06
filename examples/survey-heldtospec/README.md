# The S02 prototype replays a bounded source review

Readers can reproduce a survey packet and inspect candidate claims from heldtospec's public contracts interface. **This run demonstrates the external-agent path and local quote checks.** It establishes no new confirmed defect or discovery-quality score.

The sources come from heldtospec commit `9ccd2766580e83b21f5d7717c7cee222f8fc6c2d`, retrieved on 6 September 2026. GitHub could not resolve the historical survey's `c8c9362` commit. This run therefore remains separate from the earlier 44-promise study. The pinned guides still use the project's Quivra name.

## Pinned sources keep the input inspectable

| Source | Upstream Git blob | Scope |
|---|---|---|
| [Contracts guide](sources/docs/CONTRACTS.md) | `f672f82102becd3f6ef4e582ad06d9dc93cc5138` | Full document |
| [CLI reference](sources/docs/CLI.md) | `a28db493f5ca60848bc4fa411bd73cb531ea0265` | Full document; candidate selection concerns contracts and relevant exit behavior |

The [manifest](manifest.json) records byte hashes and names the excluded source. The copied files match the Git blob hashes returned by the upstream tree. No target code, tests, live help command, or linked external document ran or entered this survey.

## The run preserves judgments without accepting them

The assistant read both guides and supplied [candidate claims](response.json) through the external import path. A model proposed these claims in the chat. No local Codex CLI or independent human reviewer produced them. The source packet retains the task and exact input text.

| Observed result on 6 September 2026 | Value | Meaning |
|---|---:|---|
| Sources ready / reported inspected | 2 / 2 | Submitted inspection notes; no completeness guarantee |
| Explicit excluded source | 1 | General configuration reference |
| Candidate claims | 12 | Selected unaccepted claims with exact quotations |
| Confirmed new findings | 0 | No executable or independent confirmation attempted |
| Defenses graded | 0 | Outside S02 |
| Replay differences | 0 | Same packet and exact candidate IDs after importing the same saved response |

Candidates include extra-column scope, null-limit units, lint without data access, metadata-only references, and verification with no executable checks. Each includes uncertainty and a next question. Their current behavior remains unchecked.

Open the [review page](run/review.html) or inspect the [packet](run/packet.json). The [workflow guide](../../docs/SURVEY_PROTOTYPE.md) contains the replay commands. Replay checks that saved claims survive import. It does not show whether a fresh model run improves on ordinary search.

## Failure tests establish narrow mechanical behavior

The repository suite passed 35 tests on 6 September 2026, including 14 survey tests. They exercise fabricated quotations, bad ranges, changed inputs, path escape, unsupported size, unsafe page content, duplicate submissions, and interrupted adapter recovery. A fake executable tests the Codex process interface.

No Codex executable was installed in this workspace. Live model behavior, effective tool access, missed claims, and total human review time remain unmeasured. Those limits block claims of a working live provider or better survey results.

The sources retain their upstream Apache-2.0 license; see [source credits](../../NOTICE). The source snapshot is evidence input and remains verbatim.
