# Trace freshness is prior art; Upheld owns justified reliance

Readers are engineers deciding what Upheld should build rather than reimplement. This design note is dated 9 September 2026 and follows the focused prior-art review of Doorstop and Boundver.

**Do not treat fingerprinted requirement links, suspect-link detection, or generic consumer-impact propagation as Upheld's differentiator.** Doorstop and Boundver already establish that design family. Upheld begins where a project needs to say why a mechanism should uphold a promise, what observation demonstrated that mechanism, what a person chose to rely on, and whether the grounds for that choice still apply.

This is a product-boundary decision, not a claim that Doorstop and Boundver are the same product. Doorstop is a requirements-management system. Boundver is a contract-drift and consumer-impact tool. Their overlap identifies an established lower layer that Upheld can consume instead of owning by default.

## Doorstop's suspect links and Boundver share the same primitive

Doorstop stores a fingerprint for reviewed item content and a stamp on a link to its parent. A changed parent fingerprint makes that link suspect until it is explicitly cleared. Boundver stores fingerprints for declared contract facets and a consumer graph; changed contract identity can produce direct and transitive affected consumers.

| General primitive | Doorstop | Boundver |
|---|---|---|
| Stable named object | Requirement item | Component or declared contract |
| Recorded prior identity | Review stamp or link stamp | Lockfile fingerprint |
| Relationship | Requirement trace link | Consumer edge |
| Change event | Item fingerprint differs | Contract facet fingerprint differs |
| Downstream result | Link becomes suspect / item unreviewed | Consumer becomes affected |
| Human or workflow action | Review or clear | Inspect impact, run targeted checks, update reviewed baseline |

The centers of gravity still differ. Doorstop is requirements-centric and its stamps support document review. Boundver distinguishes exact, behavior, boundary, and compatibility drift and routes change through a declared consumer graph. Neither relationship, by itself, establishes that a test, type, checker, or other mechanism is an adequate defense of a software promise.

Therefore the minimal idea "store a promise, link it to an artifact, fingerprint the relationship, and request review when it changes" is established prior art. If Upheld stopped there, it would mostly occupy Doorstop/Boundver territory.

## Keep freshness and assurance as separate layers

Treat these as two composable layers.

### Layer 1: identity, dependency, and freshness

This layer answers questions such as:

- What stable object is this?
- Which source or artifact currently resolves to it?
- What bytes or declared contract identity were previously observed?
- Which declared relationships depend on it?
- Which relationships or consumers may be affected after a change?
- Is the target missing or unavailable?

Doorstop, Boundver, build graphs, requirements tools, and source resolvers can supply parts of this layer. Upheld may implement the minimum needed for standalone use, but should not grow a second general dependency engine merely because it can.

### Layer 2: justified reliance

This is Upheld's core responsibility. It answers different questions:

- What falsifiable promise are we trying to uphold?
- What mechanism is asserted to defend it?
- Why is that mechanism appropriate for this promise and scope?
- What bypass paths or failure modes remain?
- What fault model and oracle can challenge the defense itself?
- What did an actual run observe?
- What exact grounds did that observation depend on?
- Which evidence, if any, did a person explicitly choose to rely upon?
- Have the grounds of that accepted evidence changed?

A fresh trace can still point to a bad defense. A stale trace can point to a defense that remains semantically adequate. Upheld must not collapse those states.

## A changed fingerprint invalidates reuse, not truth

The recurring mistake in traceability systems is to give a change event more semantic meaning than it has.

A changed ground means:

> The previous evidence or review decision cannot be reused without reassessment under the stated policy.

It does not mean:

> The promise is false.

It does not necessarily mean:

> The defense is inadequate.

And an unchanged fingerprint means only that the tracked grounds are unchanged under the selected profile. It does not re-prove the defense, authenticate the producer, establish complete coverage, or establish that the promise is true.

Upheld's result vocabulary and reports should preserve these distinctions. Imported Doorstop `suspect` state or Boundver `affected` state is change context. It is never an evidence verdict.

## Regeneration and bulk review must not manufacture acceptance

Doorstop demonstrates a useful workflow but also exposes a dangerous convenience: review and suspect-link stamps can be refreshed or cleared in bulk. An explicit bulk review can be a legitimate human decision, but mechanically refreshing hashes must never silently become acceptance.

Upheld therefore keeps these invariants:

1. Regenerating hashes, indexes, locators, manifests, or a lock never advances an evidence record's grounds.
2. Re-resolving a moved artifact may repair identity; it does not create a new observation.
3. Clearing an imported suspect flag does not create an Upheld binding.
4. A batch acceptance, if supported later, is an explicit human action over named findings or evidence records and remains auditable as such.
5. No importer or producer writes human bindings.

This is why the disposable-lock and immutable-evidence split is architectural rather than cosmetic.

## Stable identity is not a path, hash, or review stamp

Doorstop and requirements-management tools repeatedly encounter UID, rename, and link-maintenance problems. Boundver similarly separates component names and declared identities from the current source snapshot.

Upheld should preserve four distinct concepts:

- stable record identity;
- current locator or resolver result;
- current fingerprint or basis;
- human review or evidence decision.

A rename may preserve identity. A byte-identical replacement may still have different provenance. A guessed rename must not preserve validity merely to reduce the review queue. S15-S17 should make this separation explicit for component and cross-project records.

## Recommended enforcement is a proposal, not an existing defense

The same boundary applies to defense selection.

A tool may infer that a numeric invariant is better defended by a type restriction, property check, or boundary-focused test. That inference can be valuable, but it is not the same thing as discovering an implemented defense.

Future schemas should preserve at least these conceptual states:

- **recommended defense pattern** — a proposal with rationale, intended scope, bypass paths, proposed fault challenge, cost, and residual uncertainty;
- **candidate or asserted defense** — a mechanism that actually exists and is claimed to uphold the promise;
- **observed defense evidence** — a run that challenged that mechanism with a justified oracle;
- **accepted evidence** — a person's explicit choice to rely on one compatible supporting record.

A recommendation must never appear in the machine-readable register as though the mechanism already exists. Conversely, discovering an existing test must not imply that it is the best or adequate enforcement.

This makes S06 more important: classification is not just naming `test`, `property`, `checker`, `type`, `ratchet`, or `runtime_invariant`; it is producing reviewable advice about why one mechanism is appropriate and how it could fail.

## Integrate existing trace systems instead of requiring migration

Upheld should support an adoption bypass for projects that already maintain requirements or dependency graphs.

Potential imports include:

- Doorstop or StrictDoc requirements as candidate promises and source locators;
- Doorstop parent links and suspect state as trace/freshness context;
- Boundver components, contract facets, and affected-consumer output as component and change context;
- build-system affected-target output as scheduling context;
- external ALM or ReqIF records as candidate obligation sources.

The importer boundary is strict. Imported review status, passing tests, affected state, or link hashes do not become Upheld evidence or bindings. They reduce duplicate authoring and help select what to inspect.

The preferred adoption path for an existing project is therefore:

1. reuse its existing requirement and dependency identities where stable enough;
2. import or resolve candidate promises and relationships;
3. add Upheld defense assertions only where the project wants assurance beyond traceability;
4. challenge those defenses and create evidence;
5. bind only after explicit review;
6. use existing change-impact systems to narrow future reassessment where possible.

A team should not have to replace Doorstop, StrictDoc, Boundver, or its build graph in order to use Upheld.

## Component work must not recreate a generic dependency graph

S15-S17 need a sharper boundary.

A component membership edge means that something belongs to a component. A dependency or consumer edge means that a change may affect another component. A support edge means that one claim, mechanism, or argument is offered as grounds for another claim. These are not interchangeable.

Boundver can supply component topology and change impact. Upheld should own semantic support only when it can record the conditions, scope, reason, and defenses that make the relationship meaningful.

A generated system view may combine both. It should be able to say, for example:

- Boundver reports that component B consumes A's changed public contract;
- Upheld records that B relies on exported guarantee G from A under conditions C;
- the evidence supporting G was observed against versions V and W;
- the changed contract touches one of that evidence record's grounds;
- reassessment is required.

That is stronger than either system alone without pretending that consumer impact proves incompatibility or that an assurance link discovers every dependency.

## Evaluation must compare against the simpler baseline

Upheld should not validate itself only against manual work or no tool. The relevant baseline is now clearer.

For maintenance trials, include a simple fingerprinted-trace baseline that can:

- store obligation-to-artifact or dependency links;
- fingerprint reviewed state;
- flag changed or missing grounds;
- report affected relationships.

Then measure whether Upheld's additional semantics earn their cost. Useful gains include:

- catching defenses that exist but do not discriminate the promised fault;
- avoiding false conclusions from a passing suite;
- preserving the difference between changed grounds and actual failure;
- reducing unnecessary reassessment through validated scope;
- producing better enforcement recommendations;
- preserving explicit human choices across regeneration;
- giving more useful next actions per unit of review time.

If Upheld cannot outperform or materially complement that simpler baseline, the extra ontology is not justified.

## Product claims must reflect the boundary

Do not claim novelty for:

- requirements as code;
- machine-readable traceability;
- requirement-to-test or requirement-to-code links;
- fingerprinted reviewed state;
- suspect-link detection;
- generic change-impact traversal.

The value Upheld must demonstrate is the combination around **reasons to rely on a defense**: explicit defense semantics, adversarial defense checks, immutable scoped observations, explicit human acceptance, and changed-ground invalidation that does not overclaim semantic failure.

The [prior-art review](PRIOR_ART.md) records the sources. The [component design](COMPONENT_REGISTER_DESIGN.md) applies this boundary to S15-S17. The [decisions](DECISIONS.md) make it a product rule rather than a comparison note.
