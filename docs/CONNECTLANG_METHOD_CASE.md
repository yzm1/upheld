# Repo C distinguishes delivered behavior from demonstrated defense

Readers are engineers designing the Upheld guide. We reviewed this case on 7 September 2026 using the extended ConnectLang response supplied by the user.

The response helps S11 by exposing a missing question: **does the production path connect the components that the argument relies on?** Component tests and a complete-looking register can coexist with an unwired path.

We inspected the linked commit contents and the supplied response. We did not reproduce ConnectLang's runtime checks. Reported run counts, platform outcomes, and the response author's causal account remain claims by the source author. This case shaped the guide and must stay outside its held-out trial.

## The source changes support narrower claims than the original message

| Source | What was inspected or reported | Consequence for Upheld |
|---|---|---|
| [February obligation register](https://github.com/yzm1/connectlang/commit/b3b1cdf21630559029647c4c3ee7d3512b31654e) | The register names what delivers each promise. | Delivery is a distinct relationship. Its presence does not establish a defending mechanism or evidence that the mechanism detects faults. |
| [Methodology repair](https://github.com/yzm1/connectlang/commit/6586e09f108649bd30b9e6e33eb1509fcbb5f93a) | The patch distinguishes helper APIs from production routing and reopens work previously marked complete. | Read the actual caller path. A useful helper and its tests cannot establish that production uses it. |
| [Root-handling repair](https://github.com/yzm1/connectlang/commit/20a4761e187bc6b9eb7a8c941916066d316650f6) | The patch addresses root handling and native Windows stack unwinding. The response describes a missing live root and an invalid frame-pointer assumption. | Track assumptions across compiler and runtime boundaries. Keep other platforms and paths open where the evidence does not cover them. |
| [Supplied extended response](history/2026-09-07/CONNECTLANG_RESPONSE.md) | Reports removal of a source-string test tied to obsolete prose while retaining runtime tests; distinguishes project completion from audit completion. | Test behavior, preserve the user's project mandate, and avoid treating a clean task list as the project outcome. |

The earlier [message to C](../messages/to-c.md) equated its delivery column too closely with a defense link. It also drew too strong a conclusion from code that handled proof duties. Its dated correction preserves the historical message while withdrawing those inferences.

## Ask separate questions before proposing a defense

A guide should ask what behavior the project requires, what implements it, what detects a fault, and what observed challenge supports that check. It should then trace the calls used by the real program and state the remaining assumptions. These are distinct questions even when the same file appears in several answers.

Published promises lacking implementing code remain candidates. A discrepancy between research, design, and code needs someone to settle the intended behavior; the oldest document does not automatically prevail. An accepted gap records why work remains open. It does not become a defense.

The response also supports fault challenges beyond code edits, independent checks of compiler soundness, and priorities based on consequence, exposure, dependencies, and cost to resolve uncertainty. These are useful guide requirements, without evidence that adding the guide improves an agent's results.

No new defense kind or automatic score for a whole promise follows from this case. The current [method](METHOD.md) already preserves missing-code promises, independent oracles, separate gaps, and fault models beyond code edits. S12 should make those rules easier to apply and ask how the real program uses each part. Any normative change needs its own rule review.

The [snapshot](history/2026-09-07/CONNECTLANG_RESPONSE.md) preserves the supplied file bytes. We recorded its digest in the [snapshot manifest](history/snapshot-hashes.json). The source author's revised date is 7 September 2026; the dates of the cited commits remain those in GitHub. This review makes no claim that Upheld caused the reported repairs.
