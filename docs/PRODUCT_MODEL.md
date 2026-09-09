# Upheld keeps a living map from software obligations to defense coverage

Readers are engineers deciding what Upheld is for before choosing a command or schema field.

**Upheld should let a team answer five questions about an app: What must stay true? How should we hold it? What holds it now? Why do we trust those defenses? What gap needs work?** The same map should stay useful from early design through later changes.

Schema 0.2 uses `obligations` for the falsifiable conditions the software must preserve. Version 0.1 called the same core record a `promise`.

## One map supports new designs and existing code

Upheld has two entry paths.

**Design first.** A team can write obligations before code exists. It can record scope, assumptions, harm, cost limits, runtime limits, and other facts that affect defense choice. Upheld can then help form a defense plan before the feature is built.

**Audit first.** A team can scan an existing project for obligations and defenses already present in docs, code, tests, types, config, and runtime checks. Upheld can then compare that current state with a stronger or cheaper defense plan.

The two paths meet in the same data. A discovered obligation may later become an explicit design rule. An authored defense plan may later acquire real code and evidence.

## Each obligation has a desired state and a current state

| Part | Core question |
|---|---|
| Obligation | What must stay true? |
| Defense plan | What mechanism or set of mechanisms should hold it under the project's limits? |
| Current defenses | What mechanisms actually exist now? |
| Evidence and binding | Which current defenses have faced a meaningful fault challenge, and which evidence did a person choose to trust? |
| Gap | What is missing, weak, unproven, stale, conflicting, or deliberately left open? |

The plan and the current state must remain separate. Advice does not become code because Upheld proposed it. A test does not become a good defense because Upheld found it.

Schema 0.2 makes this split explicit. `recommended_assurance` holds candidate plans and the selected plan. `actual_defenses` holds mechanisms that exist. `accepted_gaps` holds deliberate exceptions. The assurance report derives open gaps from those records plus evidence and bindings.

The main report should make the comparison easy to read. A user should be able to move from “this obligation has a gap” to the exact reason and the next useful action.

## The best defense depends on the project

Upheld should help find the best justified plan under stated limits. It should not give every defense kind one fixed rank.

A plan can compare mechanisms by:

- how much of the bad state they prevent or detect;
- which scope they cover;
- known bypass paths;
- expected harm if they fail;
- feedback speed;
- runtime and upkeep cost;
- tools or targets they need;
- how independent they are from other defenses;
- whether a meaningful fault can challenge them;
- whether a later check can move into an earlier guard.

When the user gives hard limits or priorities, those inputs define the trade. Without them, Upheld should present sound options rather than invent a single winner.

A plan may need several defenses. For example, a type guard can protect local state while an integration check covers a remote service. A runtime invariant can catch faults that no build-time rule can see.

## Gaps are a primary output

Upheld should make the difference between the plan and current state explicit.

Useful gap classes include:

- no plan exists yet;
- no implementation matches a recommended defense;
- current defense is partial, disabled, weaker, or narrower than the plan;
- current defense exists but has no bound supporting evidence;
- evidence is stale because tracked grounds changed;
- part of the obligation has no coverage;
- a needed tool or target is unavailable;
- code uses a different defense and the reason has not been reviewed;
- several defenses conflict or leave a hole between them;
- the team accepted an uncovered part and recorded why.

Some gaps are bugs. Some are design debt. Some are accepted tradeoffs. The common value is that they remain visible in one machine-readable map.

Open gaps should normally be derived, not copied into the canonical register by hand. Accepted exceptions are different: a person can record them in the register, and reports keep them visible as accepted gaps.

A gap view should help order work by harm, exposure, reachability, and the effort needed to settle the unknown. A raw gap count is not enough.

## Evidence answers whether a current defense earned trust

A current defense is a fact about the implementation. Evidence is a fact about a run that challenged that defense. A binding is a person's choice to rely on compatible supporting evidence.

These are separate because a passing suite can exist without testing the fault named by the obligation. Upheld should ask what fault would show that the defense is inadequate and whether the defense can tell that fault from a valid state.

Evidence therefore supports the current-defense side of the map. It is not the whole product.

## Change tracking keeps the map current

When code, an obligation, a defense, or a tracked input changes, Upheld needs to know which parts of the map may need another look.

Doorstop, Boundver, build graphs, and other tools already solve parts of this lower-level job. Upheld can import their change signals where practical. A changed fingerprint means that old grounds need review. It does not mean the obligation is false.

The [trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) records that lower-layer split and the rules for importing those signals safely.

## A small user workflow should expose the whole model

A useful first-use flow can be simple:

1. choose a component or feature;
2. write or discover its obligations;
3. review a proposed defense plan;
4. inspect the defenses Upheld found in the code;
5. see the plan-versus-current gaps;
6. challenge important current defenses;
7. bind evidence only when a person chooses to trust it;
8. revisit only the affected parts after later changes.

A user should not need to understand every internal file before getting this view.

## Product success is better coverage with manageable work

Upheld should be judged by whether it helps teams make better choices about how obligations are held.

Useful gains include finding obligations that were never defended, finding tests that cannot catch the promised fault, suggesting a stronger or cheaper defense plan, showing uncovered scope, preserving good evidence across unrelated changes, and directing review only where recorded grounds changed.

The [positioning](POSITIONING.md) states this in user-facing terms. The [schema](SCHEMA.md) defines the 0.2 record split. The [milestone](MILESTONE.md) turns these goals into trials. The [component design](COMPONENT_REGISTER_DESIGN.md) carries the map into multi-component and cross-project work. The [method](METHOD.md) defines how a current defense earns evidence.
