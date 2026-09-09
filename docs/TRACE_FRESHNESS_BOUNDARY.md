# Fingerprints and affected links are prior art; Upheld starts at the defense

Readers are engineers deciding what Upheld should build instead of reimplement. This note records the 9 September 2026 decision that follows the Doorstop and Boundver review.

**Doorstop and Boundver already cover the basic pattern of saved fingerprints, linked downstream work, and review after drift.** Upheld should build above that pattern. It should explain why a mechanism can uphold a promise, how to challenge that mechanism, what a real run observed, which record a person chose to rely on, and which changed inputs force another review.

Doorstop and Boundver remain different products. Doorstop manages requirements. Boundver tracks declared contract drift and affected consumers. Their overlap shows which lower-level work Upheld can reuse.

## Doorstop and Boundver share the same lower-level shape

Doorstop saves a fingerprint for reviewed requirement content. A child link stores the parent's fingerprint. When the parent changes, Doorstop marks the link suspect until a reviewer clears it.

Boundver saves fingerprints for declared contract facets. It also stores consumer edges. When a contract fingerprint changes, Boundver can list direct and transitive consumers that may need work.

| Question | Doorstop | Boundver |
|---|---|---|
| What is named? | Requirement item | Component or declared contract |
| What value is saved? | Review stamp or parent-link stamp | Lockfile fingerprint |
| What points downstream? | Requirement trace link | Consumer edge |
| What triggers work? | Item fingerprint differs | Contract facet fingerprint differs |
| What gets reported? | Suspect link or unreviewed item | Direct or transitive affected consumer |
| What happens next? | Review or clear | Inspect impact and run targeted checks |

Doorstop centers on requirements and document review. Boundver separates exact, behavior, boundary, and compatibility changes across component contracts. Neither tool says that a linked test, type, checker, or other mechanism is a good defense merely because the link is fresh.

A product that stores promise-to-artifact links, hashes them, and requests review after changes would therefore rebuild established behavior. Upheld needs to add something above that layer.

## Keep change tracking and defense review separate

Treat the design as two layers that can work together.

### Layer 1 tracks names, files, hashes, and downstream links

This layer answers concrete questions:

- Which named item are we talking about?
- Which file or symbol resolves to it now?
- What bytes or contract value did the previous check record?
- Which declared links depend on it?
- Which consumers may need work after a change?
- Is a target missing or unavailable?

Doorstop, Boundver, build graphs, requirements tools, and source resolvers already answer parts of these questions. Upheld may keep a small local version for standalone use. It should avoid growing another general dependency engine without measured need.

### Layer 2 tests whether a defense supports reliance

This is Upheld's core work:

- What falsifiable promise are we trying to uphold?
- Which mechanism claims to defend it?
- Why does that mechanism fit this promise and scope?
- Which bypass paths or failure modes remain?
- Which fault model and oracle can challenge the mechanism?
- What did a real run observe?
- Which files, claim text, configuration, and environment files formed that run's basis?
- Which evidence record did a person choose to rely on?
- Have any of those inputs changed?

A fresh trace can still point to a weak defense. A stale trace can still point to a defense that remains good after review. Upheld must keep those cases apart.

## A changed hash means review the old grounds again

Trace tools often give a change signal more meaning than it deserves.

When a tracked input changes, Upheld should say:

> The earlier evidence used different grounds. Recheck before reusing the person's earlier choice.

It should not claim that the promise is false. It should not claim that the defense failed unless a run observed such a failure.

The reverse rule matters too. If the selected profile produces the same fingerprint, Upheld knows only that those tracked inputs match the earlier basis. The matching hash does not rerun the defense, authenticate the producer, prove complete coverage, or prove the promise.

Imported Doorstop `suspect` state and Boundver `affected` output therefore stay as change context. Neither becomes an evidence verdict.

## Refreshing hashes must never create a person's choice

Doorstop offers useful review commands, including ways to clear suspect links. That convenience exposes a trap for Upheld: a metadata refresh must never look like a fresh decision to rely on evidence.

Keep these rules:

1. Regenerating hashes, indexes, locators, manifests, or a lock never advances an evidence record's basis.
2. Resolving a moved artifact may repair its locator; it does not create a new run.
3. Clearing an imported suspect flag does not create an Upheld binding.
4. If Upheld later supports batch binding, a person must explicitly choose named evidence records or findings. The record must show that action.
5. Importers and evidence producers never write human bindings.

The disposable lock and immutable evidence log serve different purposes. The lock helps Upheld resolve current files. The evidence log preserves what a past run actually claimed.

## Keep stable record names separate from paths and hashes

Requirements tools repeatedly face rename and link-maintenance problems. Boundver also separates component names from the source snapshot it checks.

Upheld should keep four things distinct:

- the stable record ID;
- the current file, symbol, or resolver result;
- the current fingerprint or evidence basis;
- the person's review or binding choice.

A rename can keep the same record ID. A byte-identical replacement can come from a different source. A guessed rename must not keep evidence current merely to shrink the review queue.

S15-S17 should preserve this split for component and cross-project records.

## Advice about enforcement stays separate from implemented defenses

Upheld may eventually suggest how best to defend a promise. For example, a closed numeric boundary may suit a type restriction, a property check, or a few boundary cases better than a broad integration test.

That advice is useful before the mechanism exists. The machine-readable model therefore needs separate states for:

- **recommended defense pattern** — advice with a reason, intended scope, bypass paths, proposed fault challenge, cost, and remaining unknowns;
- **implemented defense** — a real mechanism that the project claims upholds the promise;
- **run evidence** — a recorded challenge of that mechanism with a justified oracle;
- **binding** — the evidence record a person chose to rely on.

A recommendation must never enter the register as an implemented defense. Finding an existing test also does not show that the test is adequate or preferable.

S06 should therefore produce reviewable advice: why the mechanism fits, where it can be bypassed, how to challenge it, and what remains unknown. Merely naming `test`, `property`, `checker`, `type`, `ratchet`, or `runtime_invariant` is insufficient.

## Existing trace tools provide an adoption bypass

Teams that already maintain requirements or dependency graphs should not recreate them before trying Upheld.

Useful inputs include:

- Doorstop or StrictDoc requirements as candidate promises and source locators;
- Doorstop parent links and suspect flags as trace-change context;
- Boundver components, contract facets, and affected consumers as component-change context;
- build-system affected targets as scheduling data;
- ReqIF or other requirements-management records as candidate promise sources.

The import rule stays strict. A source tool may say `reviewed`, `suspect`, `affected`, or `passing`. Upheld records those facts as input context. They do not become Upheld evidence or a human binding.

A practical adoption path is:

1. reuse stable IDs that the project already maintains;
2. import candidate promises, locators, and links;
3. add Upheld defense records only where the project wants stronger assurance;
4. challenge those defenses and append run evidence;
5. bind evidence only after explicit review;
6. use the existing change tool to narrow later rechecks where its scope is trustworthy.

A team should be able to use Upheld alongside Doorstop, StrictDoc, Boundver, or its build graph.

## Component records need several kinds of edge

S15-S17 must distinguish these relations:

- **membership**: a claim or artifact belongs to a component;
- **dependency or consumer**: a change may affect another component;
- **source trace**: a promise came from or points to another record or artifact;
- **support**: one claim or mechanism supplies stated grounds for another claim under named conditions.

The first three can help select work. They supply no evidence by themselves. A support edge is stronger and needs a reason, scope, conditions, and defenses that Upheld can inspect.

Boundver can supply component topology. Doorstop or StrictDoc can supply requirement trace links. Upheld should add support semantics where needed instead of copying those graphs into a new generic graph model.

For example, a combined view could report:

- Boundver says component B consumes A's changed public contract;
- Upheld says B relies on guarantee G from A under conditions C;
- a run recorded evidence for G against versions V and W;
- the contract change touches one tracked input behind that evidence;
- Upheld requests another review before reusing the binding.

The consumer edge narrows the search. The Upheld records explain why the relationship matters.

## Test Upheld against the simpler baseline

Upheld should not compare itself only with manual work or no tool. Doorstop and Boundver make a stronger baseline possible.

At least one follow-up should compare Upheld with a simple tool that stores named links, records fingerprints, and lists changed, missing, or affected links.

Then ask whether Upheld's extra records earn their cost. Useful gains include:

- finding a linked defense that cannot detect the promised fault;
- avoiding a false conclusion from a passing suite;
- keeping changed inputs separate from observed failure;
- using checked scope to avoid unrelated review work;
- suggesting a stronger defense with a clear fault challenge;
- preserving the person's binding when caches regenerate;
- giving a useful next action that the simpler tool cannot give.

If Upheld cannot improve a decision or expose a risky ambiguity that the simpler baseline misses, the extra records are not worth the cost for that workflow.

## Product claims must match this boundary

Do not claim novelty for:

- requirements as code;
- machine-readable trace links;
- requirement-to-test or requirement-to-code links;
- stored reviewed fingerprints;
- suspect-link detection;
- generic affected-consumer traversal.

Upheld must instead demonstrate value around the defense itself: why it fits, how a fault challenge tests it, what a scoped run observed, which evidence a person chose, and which changed inputs make that choice unsafe to reuse without review.

The [prior-art review](PRIOR_ART.md) records the sources. The [component design](COMPONENT_REGISTER_DESIGN.md) applies this boundary to S15-S17. The [decisions](DECISIONS.md) make it a product rule.
