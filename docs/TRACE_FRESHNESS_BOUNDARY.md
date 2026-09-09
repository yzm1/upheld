# Trace freshness supports the promise-to-defense map

Readers are engineers deciding what Upheld should build instead of reimplement. This note records the 9 September 2026 choice that follows the Doorstop and Boundver review.

**Upheld's main job is to map each software promise from intent to current defense.** A team should be able to state what an app must keep true, see the best justified way to hold that promise under its limits, inspect what holds it now, and see the gap. Evidence shows which current defenses have earned trust. Change tracking tells the team when some part of that map needs another look.

Doorstop and Boundver already cover saved fingerprints, downstream links, and review after drift. Upheld should reuse that work where possible. It should keep it underneath the larger product model.

## The product spine is promise, defense plan, current defenses, and gap

| View | Question |
|---|---|
| Promise | What must stay true, under which conditions and scope? |
| Defense plan | What mechanism or set would best hold it under the project's stated limits? |
| Current defenses | What mechanisms now claim to hold it, and what evidence backs them? |
| Gap and next work | What is missing, weaker than planned, unproven, stale, conflicting, or deliberately left open? |

Schema 0.1 calls the first record a `promise`. A team may write these records while designing a new app. It may also survey an existing system and find them after the fact. Both paths should reach the same machine-readable view.

A useful result can say:

> This boundary must reject values outside zero through one. The preferred plan is a type guard plus a boundary integration check. The code has only two example tests, and no fault challenge has shown that they catch an out-of-range value. The map therefore shows both a defense gap and an evidence gap.

Fingerprints, suspect links, and affected-consumer graphs help keep that result current.

## The map follows the software lifecycle

### At design time

A team writes or imports promises and records the scope, assumptions, harm, cost limits, and other facts that matter to defense choice.

Upheld can propose one or more defense plans. A plan may prefer an earlier guard over later detection, or combine several mechanisms when one is too narrow.

The plan remains advice. It should name its reason, cost, scope, bypass paths, proposed fault challenge, and unknowns.

### As code appears

Upheld finds or links the mechanisms that actually exist. These may be types, tests, properties, static checkers, ratchets, runtime invariants, contract tests, or supported extension kinds.

The code may match the plan, match only part of it, exceed it, or choose a sound alternative. Upheld records the difference rather than forcing the project into the original plan.

### When a defense is checked

The project challenges each defense with a suitable oracle and fault model. A passing suite alone does not show that the suite can detect the fault named by the promise.

Run evidence records what was observed and the source, scope, configuration, and tree inputs used by that run. A person may then choose which compatible evidence to trust.

### During upkeep

Source and contract changes may alter recorded grounds. Existing trace and impact tools can narrow the set that needs review.

Some defenses will remain good after review. Others need a new run. The defense plan itself may also change when the architecture, threat model, cost limit, or runtime setting changes.

## “Best” means best under stated limits

Upheld should help answer “how should we hold this?” without giving every defense kind one fixed rank.

A plan can compare:

- whether the mechanism prevents the bad state or detects it later;
- the scope it covers;
- known bypass paths;
- expected harm if it fails;
- feedback speed;
- runtime and upkeep cost;
- tools or runtime access it needs;
- how independent it is from other defenses;
- how easily a meaningful fault can challenge it;
- whether the guard can move earlier in the build or type system.

If the user supplies priorities or hard limits, Upheld can rank plans under those inputs. Otherwise it should present sound options and tradeoffs.

A plan may be a set. A type guard can protect local state while an integration check protects a remote boundary. A runtime invariant can cover faults that build-time checks cannot see.

## Gaps are first-class output

The plan-versus-current comparison should make gaps explicit.

Examples include:

- no defense exists;
- a current defense is weaker or narrower than the plan;
- a defense exists but no suitable fault challenge has tested it;
- evidence exists but its tracked grounds changed;
- two defenses overlap while part of the promise stays uncovered;
- a needed tool or runtime target is unavailable;
- the code differs from the plan and nobody has reviewed the reason;
- the team deliberately leaves part uncovered and records why.

A gap is not always a bug. The value is that the choice stays visible in the data instead of disappearing into memory or old review comments.

Reports should sort gaps by harm, exposure, reachability, and the cost of settling the unknown. A raw count is not enough.

## Doorstop and Boundver share the lower-level change shape

Doorstop saves a fingerprint for reviewed requirement text. A child link stores the parent's fingerprint. When the parent changes, Doorstop marks the link suspect until a reviewer clears it.

Boundver saves fingerprints for declared contract facets and stores consumer edges. When a contract fingerprint changes, Boundver can list direct and transitive consumers that may need work.

| Question | Doorstop | Boundver |
|---|---|---|
| What is named? | Requirement item | Component or declared contract |
| What value is saved? | Review stamp or parent-link stamp | Lockfile fingerprint |
| What points downstream? | Requirement trace link | Consumer edge |
| What triggers work? | Item fingerprint differs | Contract facet fingerprint differs |
| What gets reported? | Suspect link or unreviewed item | Direct or transitive affected consumer |
| What happens next? | Review or clear | Inspect impact and run targeted checks |

Doorstop centers on requirement text and document review. Boundver separates exact, behavior, boundary, and compatibility drift across component contracts. Neither says that a linked test, type, checker, or other mechanism is a good defense merely because the link is fresh.

A tool that only stores promise-to-artifact links, hashes them, and asks for review after changes would rebuild known behavior. Upheld should consume that signal as one input to the larger map.

## A changed hash asks for a recheck; it does not prove failure

When a tracked input changes, Upheld should say:

> The earlier evidence used different grounds. Recheck before reusing the earlier binding.

It should not claim that the promise is false. It should not claim that the defense failed unless a run observed such a failure.

The reverse rule matters too. If the selected profile produces the same fingerprint, Upheld knows only that those tracked inputs match the earlier basis. The matching hash does not rerun the defense, authenticate the producer, prove full coverage, or prove the promise.

Imported Doorstop `suspect` state and Boundver `affected` output therefore stay as change context. Neither becomes an evidence verdict.

## Refreshing metadata must never create trust

Doorstop offers useful review commands, including ways to clear suspect links. Upheld must keep a metadata refresh separate from a fresh human choice.

1. Rebuilding hashes, indexes, locators, manifests, or a lock never advances an evidence record's basis.
2. Resolving a moved artifact may repair its locator; it does not create a new run.
3. Clearing an imported suspect flag does not create an Upheld binding.
4. If Upheld later supports batch binding, a person must explicitly choose named evidence records or findings.
5. Importers and evidence producers never write human bindings.

The lock helps resolve current files. The evidence log preserves what a past run claimed.

## Keep stable IDs separate from files, hashes, and human choices

Upheld should keep these four things apart:

- the stable promise or defense ID;
- the current file, symbol, or resolver result;
- the current fingerprint or evidence basis;
- the person's review or binding choice.

A rename can keep the same record ID. A byte-identical replacement can come from a different source. A guessed rename must not keep evidence current merely to shrink the queue.

The same rule applies to the defense plan. A changed code file does not automatically change the best plan. A changed promise, threat model, cost limit, architecture, or runtime setting may.

## Existing trace tools provide an adoption bypass

Teams that already maintain requirement or dependency graphs should not recreate them before trying Upheld.

Useful inputs include:

- Doorstop or StrictDoc records as candidate promises and source locators;
- Doorstop parent links and suspect flags as trace-change context;
- Boundver components, contract facets, and affected consumers as component-change context;
- build-system affected targets as scheduling data;
- ReqIF or other requirement records as candidate promise sources.

A source tool may say `reviewed`, `suspect`, `affected`, or `passing`. Upheld records those facts as context. They do not become Upheld evidence or a human binding.

A practical path is:

1. reuse stable IDs the project already has;
2. import or write promises and project limits;
3. record or generate defense plans;
4. find the defenses that actually exist;
5. compare plan and current state and show gaps;
6. challenge current defenses and append evidence;
7. bind evidence only after explicit review;
8. use existing change tools to narrow later rechecks where their scope is trustworthy.

A team should be able to use Upheld alongside Doorstop, StrictDoc, Boundver, or its build graph.

## Test the whole product

The trials must test more than stale-link handling. Given a reviewed set of promises, ask whether Upheld can:

- propose suitable defense plans under stated limits;
- find current defenses without promoting name matches;
- find important gaps between the plan and the code;
- separate missing, weak, unproven, and stale coverage;
- suggest a useful next action;
- keep review time within the project's budget.

For upkeep, compare with a simpler tool that stores named links, records fingerprints, and lists changed, missing, or affected links.

If Upheld cannot improve a choice or reveal an important gap that the simpler tool misses, the extra records are not worth their cost for that workflow.

## Product claims must match the whole purpose

Do not claim novelty for requirements as code, machine-readable trace links, stored reviewed fingerprints, suspect-link detection, or generic affected-consumer traversal.

State the product problem clearly: **a machine-readable map from software promises to the defense plan, current defenses, evidence, and gaps, kept current as the app changes.**

The [prior-art review](PRIOR_ART.md) records the sources. The [component design](COMPONENT_REGISTER_DESIGN.md) applies the lower-layer boundary to S15-S17. The [decisions](DECISIONS.md) state the full product model.
