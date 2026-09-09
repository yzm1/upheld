# Trace freshness supports the obligation-to-assurance map

Readers are engineers deciding what Upheld should build instead of reimplement. This note records the 9 September 2026 decision that follows the Doorstop and Boundver review.

**Upheld's main job is to map each software obligation from intent to current assurance.** A team should be able to state what an application must keep true, see the best justified way to enforce that obligation under its constraints, inspect what mechanisms actually enforce it now, and see the gap between those two states. Evidence shows which actual defenses have earned reliance. Change tracking tells the team when part of that assessment needs another look.

Doorstop and Boundver already cover the lower-level pattern of saved fingerprints, linked downstream work, and review after drift. Upheld should reuse that pattern where possible. It should not let that supporting mechanism displace the larger product model.

## The product spine is obligation, intended assurance, actual assurance, and gap

For every obligation, Upheld should keep four views distinct.

| View | Question |
|---|---|
| Obligation | What must remain true, under which conditions and scope? |
| Intended assurance | What defense or defense portfolio would best hold it under the project's stated constraints? |
| Actual assurance | What mechanisms currently claim to hold it, and what evidence supports them? |
| Gap and attention | What is missing, weaker than intended, unproven, stale, conflicting, or deliberately left open? |

The current schema 0.1 calls an obligation a `promise`. That wire name does not change this product model.

This model supports two entry points. A team can author obligations and intended defenses while specifying a new application. It can also survey an existing system to discover obligations and the defenses already present. Both paths should reach the same machine-readable state.

A useful result can therefore say:

> This boundary must reject values outside zero through one. Under the project's constraints, the preferred assurance is a construction-time restriction plus a boundary integration check. The current implementation has only two example tests. Their fault-discrimination evidence is absent. The obligation therefore has an enforcement-strength gap and an evidence gap.

That is the forest. Fingerprints, suspect links, and affected-consumer graphs help keep this result current.

## The model follows the application lifecycle

### While specifying the application

A team writes or imports obligations. It can also record consequence, scope, assumptions, environment, and constraints that matter to assurance choice.

Upheld can then propose one or more defense plans. A proposal can prefer prevention over later detection when that is possible, or combine several mechanisms when one mechanism cannot cover the full obligation.

The recommendation remains advice. It should explain its reason, cost, scope, bypass paths, proposed fault challenge, and remaining unknowns.

### While implementing the application

Upheld finds or links the mechanisms that actually exist. These may be types, tests, properties, static checkers, ratchets, runtime invariants, contract tests, or supported extension kinds.

The actual mechanism may match the recommendation, partially match it, exceed it, or differ for a justified reason. Upheld should record the difference instead of forcing the project into the recommendation.

### While establishing assurance

The project challenges each defense with a suitable oracle and fault model. A passing suite alone does not show that the suite can detect the fault the obligation is about.

Run evidence records what was actually observed and which source, scope, configuration, and environment inputs formed the basis. A person may then choose which compatible evidence to rely on.

### While maintaining the application

Source and contract changes may invalidate some recorded grounds. Existing trace and impact systems can narrow the set that needs review.

Upheld then updates the assurance map. Some defenses remain justified after review. Others need a new run. A recommendation may also change because the application's constraints or architecture changed.

## “Best” assurance is conditional, and often a portfolio

Upheld should help answer “how should we enforce this?” without claiming one global order of techniques.

A recommendation can compare mechanisms using project-specific factors such as:

- prevention strength and detection strength;
- validated scope;
- bypass paths;
- fault consequence;
- feedback time;
- runtime cost;
- maintenance cost;
- required infrastructure;
- independence from other defenses;
- ease of adversarial challenge;
- whether a failure can be made unrepresentable rather than detected later.

If the user supplies priorities or limits, Upheld can rank choices under those inputs. If not, it should present justified alternatives and their tradeoffs.

The unit of recommendation may be a portfolio. A type restriction can prevent a local invalid state while an integration check protects a remote boundary. A runtime invariant may cover failures that build-time checks cannot see. The model should allow the project to state that the obligation needs the combination.

## Gaps are first-class product output

The difference between intended and actual assurance should produce explicit, inspectable gaps.

Examples include:

- no defense exists;
- a defense exists but is weaker or narrower than the recommendation;
- the defense exists but no adequate challenge has shown that it detects the stated fault;
- evidence exists but its tracked grounds changed;
- two defenses overlap while another part of the obligation remains uncovered;
- required infrastructure is unavailable;
- the actual defense differs from the recommendation and the reason has not been reviewed;
- the team deliberately accepted an uncovered area with a recorded reason.

A gap is not always a defect. Some gaps are accepted design choices. The product value is that the choice stays visible and machine-readable instead of disappearing into memory or scattered review comments.

Reports and change review should prioritize gaps by consequence, exposure, reachability, and the cost of resolving uncertainty. A raw count alone is not enough.

## Doorstop and Boundver share the lower-level change shape

Doorstop saves a fingerprint for reviewed requirement content. A child link stores the parent's fingerprint. When the parent changes, Doorstop marks the link suspect until a reviewer clears it.

Boundver saves fingerprints for declared contract facets and stores consumer edges. When a contract fingerprint changes, Boundver can list direct and transitive consumers that may need work.

| Question | Doorstop | Boundver |
|---|---|---|
| What is named? | Requirement item | Component or declared contract |
| What value is saved? | Review stamp or parent-link stamp | Lockfile fingerprint |
| What points downstream? | Requirement trace link | Consumer edge |
| What triggers work? | Item fingerprint differs | Contract facet fingerprint differs |
| What gets reported? | Suspect link or unreviewed item | Direct or transitive affected consumer |
| What happens next? | Review or clear | Inspect impact and run targeted checks |

Doorstop centers on requirements and document review. Boundver separates exact, behavior, boundary, and compatibility changes across component contracts. Neither tool says that a linked test, type, checker, or other mechanism is a good defense merely because the link is fresh.

A product that stores obligation-to-artifact links, hashes them, and requests review after changes would therefore rebuild established behavior. Upheld should consume that signal as one input to the larger assurance map.

## A changed hash means review the old grounds again

When a tracked input changes, Upheld should say:

> The earlier evidence used different grounds. Recheck before reusing the earlier binding.

It should not claim that the obligation is false. It should not claim that the defense failed unless a run observed such a failure.

The reverse rule matters too. If the selected profile produces the same fingerprint, Upheld knows only that those tracked inputs match the earlier basis. The matching hash does not rerun the defense, authenticate the producer, prove complete coverage, or prove the obligation.

Imported Doorstop `suspect` state and Boundver `affected` output therefore stay as change context. Neither becomes an evidence verdict.

## Refreshing metadata must never create acceptance

Doorstop offers useful review commands, including ways to clear suspect links. That convenience exposes a trap for Upheld: refreshing metadata must never look like a fresh decision to rely on evidence.

Keep these rules:

1. Regenerating hashes, indexes, locators, manifests, or a lock never advances an evidence record's basis.
2. Resolving a moved artifact may repair its locator; it does not create a new run.
3. Clearing an imported suspect flag does not create an Upheld binding.
4. If Upheld later supports batch binding, a person must explicitly choose named evidence records or findings. The record must show that action.
5. Importers and evidence producers never write human bindings.

The disposable lock and immutable evidence log serve different purposes. The lock helps Upheld resolve current files. The evidence log preserves what a past run actually claimed.

## Keep identity, location, current basis, and decision separate

Upheld should keep four things distinct:

- the stable obligation or defense ID;
- the current file, symbol, or resolver result;
- the current fingerprint or evidence basis;
- the person's review or binding choice.

A rename can keep the same record ID. A byte-identical replacement can come from a different source. A guessed rename must not keep evidence current merely to shrink the review queue.

The same rule applies to recommendations. A changed implementation does not automatically change the preferred assurance plan. A changed requirement, threat model, cost limit, architecture, or deployment environment may.

## Existing trace tools provide an adoption bypass

Teams that already maintain requirements or dependency graphs should not recreate them before trying Upheld.

Useful inputs include:

- Doorstop or StrictDoc requirements as candidate obligations and source locators;
- Doorstop parent links and suspect flags as trace-change context;
- Boundver components, contract facets, and affected consumers as component-change context;
- build-system affected targets as scheduling data;
- ReqIF or other requirements-management records as candidate obligation sources.

The import rule stays strict. A source tool may say `reviewed`, `suspect`, `affected`, or `passing`. Upheld records those facts as input context. They do not become Upheld evidence or a human binding.

A practical adoption path is:

1. reuse stable IDs that the project already maintains;
2. import or author obligations and constraints;
3. record or generate recommended assurance plans;
4. inventory the defenses that actually exist;
5. compare intended and actual assurance and surface gaps;
6. challenge actual defenses and append evidence;
7. bind evidence only after explicit review;
8. use existing change tools to narrow later rechecks where their scope is trustworthy.

A team should be able to use Upheld alongside Doorstop, StrictDoc, Boundver, or its build graph.

## Component records need several kinds of edge

S15-S17 must distinguish these relations:

- **membership**: a claim or artifact belongs to a component;
- **dependency or consumer**: a change may affect another component;
- **source trace**: an obligation came from or points to another record or artifact;
- **support**: one claim or mechanism supplies stated grounds for another claim under named conditions.

The first three help select work. They supply no evidence by themselves. A support edge is stronger and needs a reason, scope, conditions, and defenses that Upheld can inspect.

Boundver can supply component topology. Doorstop or StrictDoc can supply requirement trace links. Upheld should add support semantics where needed and use both to maintain the intended-versus-actual assurance view.

## Test the whole product, not only stale-link handling

Upheld should not compare itself only with manual work or no tool. Doorstop and Boundver make a stronger maintenance baseline possible.

But the evaluation also has to test the earlier stages of the product spine. Given a reviewed set of obligations, measure whether Upheld can:

- propose suitable defense plans under stated constraints;
- identify actual defenses without promoting mere name matches;
- detect consequential differences between recommended and actual assurance;
- distinguish missing, weak, unproven, and stale assurance;
- suggest a useful next action;
- keep review time within the project's budget.

For the maintenance phase, compare with a simple tool that stores named links, records fingerprints, and lists changed, missing, or affected relationships.

If Upheld cannot improve decisions or reveal consequential gaps that the simpler baseline misses, the extra records are not worth the cost for that workflow.

## Product claims must match the whole purpose

Do not claim novelty for requirements as code, machine-readable trace links, stored reviewed fingerprints, suspect-link detection, or generic affected-consumer traversal.

Do claim the product problem clearly: **a machine-readable map from software obligations to intended assurance, actual assurance, evidence, and gaps, maintained as the application evolves.**

The [prior-art review](PRIOR_ART.md) records the sources. The [component design](COMPONENT_REGISTER_DESIGN.md) applies the lower-layer boundary to S15-S17. The [decisions](DECISIONS.md) state the full product model.
