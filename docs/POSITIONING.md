# Position Upheld as the map from software promises to defense coverage

Readers are engineers, maintainers, and reviewers deciding whether Upheld solves a problem they have.

**Upheld keeps a machine-readable map of what software must keep true, how it should be defended, how it is actually defended, and where the gaps need attention.**

That sentence is the primary positioning. Evidence, trace freshness, agents, schemas, and change impact support it.

## The problem is not a lack of requirements or tests

Teams already have requirements, tests, types, static checks, runtime guards, contract tests, CI rules, and review practices. The missing view is often the relationship between intent and coverage.

For an important promise, a team may not have one place that answers:

- what exactly must stay true;
- what defense plan would fit the failure mode and project limits;
- which defenses actually exist;
- whether those defenses have been challenged against the right fault;
- what part remains uncovered or uncertain;
- which earlier judgment needs another look after a change.

Upheld makes that comparison explicit and machine-readable.

## The core output is the plan-versus-current gap

A useful Upheld result looks like this:

> Promise: requests outside the allowed tenant cannot read this object.
>
> Preferred defense plan: authorization at the data-access boundary plus an integration test that crosses tenants and a runtime audit signal for denied attempts.
>
> Current defenses: route-level permission test only.
>
> Evidence: the test has not been challenged through the lower-level data path.
>
> Gap: the current defense is narrower than the plan; direct data access remains uncovered.
>
> Next action: move the guard to the shared access boundary and add the cross-tenant challenge.

The value is the visible difference between what should hold the promise and what does.

## Upheld serves design and audit with the same model

For a new application, teams can author promises and defense plans before code exists. Upheld becomes a design aid: decide how each important promise should be made hard to violate.

For an existing application, Upheld can discover promises and current defenses from source, tests, docs, types, configuration, and runtime checks. It then compares the discovered state with reviewed defense plans.

The two paths converge on the same register and report.

## “Best defense” is conditional

Upheld does not advertise one defense kind as universally strongest. It should compare plans under the project's own constraints: failure consequence, scope, bypass paths, feedback speed, runtime cost, upkeep cost, available infrastructure, and independence between defenses.

A type guard may be best for a local representation rule. A property test may be better for a broad input space. An integration check may be necessary for a remote boundary. A runtime invariant may cover failures no build-time mechanism can see. One promise can require several of them together.

When the inputs do not justify one winner, Upheld should show sound alternatives and tradeoffs rather than fabricate certainty.

## What Upheld is not

Upheld is not primarily:

- a requirements editor;
- a generic dependency graph;
- a test-management system;
- a code-coverage dashboard;
- a formal proof system;
- a compliance checklist;
- a service that declares software safe.

It can consume records from requirements tools, Boundver, build graphs, test runners, and other systems. Their data reduces duplicate work. Their review or pass state does not automatically become Upheld evidence.

## The differentiator is assurance coverage, not trace freshness

Doorstop can make requirement links suspect after upstream changes. Boundver can report consumers of changed contracts. Those mechanisms are useful inputs.

Upheld adds the layer that asks whether the linked mechanism is the right defense, whether it can detect or prevent the named fault, what evidence supports it, and what gap remains relative to the desired plan.

The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records this lower-layer split.

## The short forms

**One sentence:** Upheld maps software promises to the defenses that should and do uphold them, then shows the gaps.

**For a new project:** Specify what must stay true and decide how each promise should be defended before implementation drifts away from intent.

**For an existing project:** Discover what the code promises, see what really defends each promise, and expose weak, missing, unproven, or stale coverage.

**For change review:** Revisit only the promise-to-defense judgments whose recorded grounds or design constraints actually changed.

## Product success

Upheld succeeds when it helps a team make a better coverage decision with acceptable review work. Examples include finding an important promise with no defense, showing that a passing test cannot catch the promised fault, recommending a cheaper or stronger defense portfolio, or preserving a good decision across unrelated changes.

A larger register or more warnings are not success by themselves. The [milestone](MILESTONE.md) measures finding quality, defense-plan quality, gap detection, and human review cost.
