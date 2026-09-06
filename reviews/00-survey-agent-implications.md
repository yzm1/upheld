<!--
Source: the agent revising docs/OBLIGATION_SURVEY.md in heldtospec, after
incorporating replies from A, B and C. Relayed by the maintainer, 2026-09-05.
Reviewed: the first draft of CHECKER.md (the one with `fresh` and `mutants` as
checker commands).

Accepted: freshness conditional on generator cost (X2 restated as a ratio);
three-state mutant classification from the engine's native result; boundary
discipline (one representable unit outside the clause); needs_environment
orthogonal to mechanism; expected_verdict generalised from expected: survives;
pre-registration as the tool's own acceptance protocol.

Pushed back on: "everything the replies added is either a field on the register
or a discipline on the person running it, and neither needs a shared binary to
exist." Deriving fired / did-not-fire / could-not-look from a runner's native
output is code, per runner, and getting it wrong is the bug A found. That
finding earns the runner more, not less.
-->

# What this means for the tool

The replies change its scope, its schema, and one of its acceptance criteria.

Its subject just got smaller, and that's good. Two of the three struck rows were analysis claims — the domain distribution, the ranking formula. Neither was ever the tool's job. What survived and got stronger is entirely mechanical: seeded-violation grading with three-state results. The tool's centre of gravity moves from score toward mutants, which was already one of the two earned commands.

fresh needs C's provenance list, and a hash won't do. "An unchanged test can cease to be adequate when the implementation, specification, dependencies, target or build flags change." Record source revision and dirty-tree state, command, toolchain/target/configuration, exercised scope, result, omissions, run time. And the semantics: invalidation means reassessment required, not proof of a regression — a distinct exit state from "found a difference."

X2's correction removes a command. I proposed fresh as a cheap alternative to regeneration. B's generator is sub-second, so there regenerate-and-compare is the guard and a cached freshness check adds an invalidation problem for no saving. So fresh is conditional on the generator being expensive — it belongs behind a measurement of the generator, not in the default set. That's one of two earned commands turning out to be earned only in one of the two repos that built it.

mutants needs the three-state result and boundary discipline. A's finding — an audit counting red as caught scores a missing environment variable as a pass — is a bug the tool would have shipped. It must classify into fired / did-not-fire / could-not-look, from the engine's own native result. And heldtospec's spec adds what B's catalogue lacks: the counterexample must sit one representable unit outside the clause. A mutation far from the boundary is a smoke test, not a grade.

Two schema changes. needs_environment as its own field, orthogonal to the mechanism — otherwise the tool's own classification eats doable work in the direction that hides it. And expected_verdict, which heldtospec took from boundver's expected: survives and generalised: the grader asserts a clause stays ungradeable, so the honest remainder ratchets instead of becoming a permanently red number teams learn to ignore.

The strongest single steal is B's pre-registration protocol, and it applies to the tool's own acceptance rather than to its features. Commit the prediction and the falsifier before the classifier exists; resolve the falsifier to specific IDs and grade each decisive-or-arguable before results; commit the reliability rule with a publication threshold; blind by construction, not by instruction. B's first run failed and they took the strict reading of their own ambiguous rule because the loose one was the one they preferred. Nothing in the tool design catches that; only the protocol does.

And the honest bottom line on (b) is unchanged but for a different reason. mutants is now earned three times over rather than twice. fresh is earned once — in the repo with the seven-minute generator. Everything the replies added is either a field on the register or a discipline on the person running it, and neither needs a shared binary to exist.
