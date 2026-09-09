# Position Upheld as the map from software promises to defense coverage

Readers are engineers, maintainers, and reviewers deciding whether Upheld solves a problem they have.

**Upheld keeps a machine-readable map of what software must keep true, which defenses should hold each promise, which defenses do so now, and where gaps need work.**

That is the primary positioning. Evidence, change tracking, agents, and schemas support it.

## Teams already have requirements and tests

Most projects already have requirements, tests, types, static checks, runtime guards, contract tests, CI rules, and review habits. They often lack one view that connects the promise to the coverage.

For an important promise, Upheld should answer:

- what exactly must stay true;
- what defense plan fits the failure mode and project limits;
- which defenses actually exist;
- whether those defenses have faced the right fault;
- what part remains uncovered or uncertain;
- which earlier judgment needs another look after a change.

Upheld stores that comparison in a form people and tools can inspect.

## The core output is the plan-versus-current gap

A useful result looks like this:

> Promise: requests outside the allowed tenant cannot read this object.
>
> Preferred defense plan: authorization at the data-access boundary plus an integration test that crosses tenants and a runtime audit signal for denied attempts.
>
> Current defenses: route-level permission test only.
>
> Evidence: the test has not faced a challenge through the lower-level data path.
>
> Gap: the current defense is narrower than the plan; direct data access remains uncovered.
>
> Next action: move the guard to the shared access boundary and add the cross-tenant challenge.

The value is the visible difference between what should hold the promise and what does.

## The same model serves design and audit

For a new app, teams can write promises and defense plans before code exists. Use Upheld during design to choose defenses that make each important promise hard to violate.

For an existing app, Upheld can find promises and current defenses in source, tests, docs, types, config, and runtime checks. It then compares that current state with reviewed defense plans.

Both routes lead to the same register and gap report.

## “Best defense” depends on the case

Upheld does not advertise one defense kind as universally strongest. Compare plans using the project's own limits: likely harm, scope, bypass paths, feedback speed, runtime cost, upkeep cost, available tools, and independence between defenses.

A type guard may fit a local representation rule. A property test may suit a broad input space. An integration check may be necessary at a remote boundary. A runtime invariant may catch faults that build-time checks cannot see. One promise can need several of them together.

When the facts do not justify one winner, show sound alternatives and tradeoffs.

## What Upheld is not

Upheld is not primarily:

- a requirements editor;
- a generic dependency graph;
- a test manager;
- a code-coverage dashboard;
- a formal proof system;
- a compliance checklist;
- a service that declares software safe.

It can consume records from requirements tools, Boundver, build graphs, test runners, and other systems. Their data can reduce duplicate work. Their review or pass state never becomes Upheld evidence by default.

## The differentiator is the coverage judgment

Doorstop can mark requirement links suspect after upstream changes. Boundver can report consumers of changed contracts. Those are useful inputs.

Upheld asks a different set of questions: Is the linked mechanism the right defense? Can it detect or prevent the named fault? What evidence supports it? What gap remains against the plan?

The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records the lower-layer split.

## The short forms

**One sentence:** Upheld maps software promises to the defenses that should and do uphold them, then shows the gaps.

**For a new project:** Specify what must stay true and choose defenses before code drifts away from intent.

**For an existing project:** Find what the code promises, see what really defends each promise, and expose weak, missing, unproven, or stale coverage.

**For change review:** Revisit only the promise-to-defense judgments whose recorded grounds or design limits changed.

## Product success

Upheld succeeds when it helps a team make a better coverage decision with acceptable review work. Examples include finding a promise with no defense, showing that a passing test cannot catch the promised fault, proposing a cheaper or stronger defense set, or preserving a good decision across unrelated changes.

A larger register or more warnings do not prove success. The [milestone](MILESTONE.md) measures finding quality, plan quality, gap detection, and human review cost.
