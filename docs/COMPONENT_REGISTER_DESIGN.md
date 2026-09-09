# Components own claims; shared contracts need their own records

Readers are engineers planning Upheld's next schema. **Keep a component's promises near its code, and give shared contracts an explicit owner.** Combine those files into a generated system view. This is agreed design work for S15–S17; the current exporter uses schema 0.1.

## Boundver supplies component names and change impact

Boundver declares component paths, contract inputs, and downstream consumers. Its named groups can include explicit members or every downstream component. Its current schema keeps those declarations in one central file. Separate authored files would be an Upheld choice. [Boundver schema at the reviewed commit](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/boundary.config.schema.json).

The payments demo traces an API change through a client library and checkout app to an external mobile consumer. External labels end traversal; they do not identify a verified remote contract. [Runnable demo](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/scripts/demo_consumer_impact.py), [graph code](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/src/boundver/_consumer_graph.py).

Doorstop supplies the same lower-level pattern in a requirements setting: a parent-link stamp records the upstream item's fingerprint, and a changed fingerprint makes the link suspect until reviewed. [Reviewed Doorstop item implementation](https://github.com/doorstop-dev/doorstop/blob/1f5756390bdeeff58fc22e30d5c5a56bb1a81c16/doorstop/core/item.py).

[The trace-freshness boundary](TRACE_FRESHNESS_BOUNDARY.md) therefore treats generic identity, fingerprint drift, and affected-relationship propagation as an established lower layer. S15–S17 must not recreate a second general dependency engine unless measured needs require semantics that the available tools cannot provide.

## Membership, dependency, and support are different relations

The next schema must not overload one edge type.

| Relation | Meaning | Evidence implication |
|---|---|---|
| Membership | A claim or artifact belongs to a component or authored register. | None. It organizes ownership and scope. |
| Dependency / consumer | A change in one component may affect another. | None. It selects possible review work. |
| Trace / source relation | An obligation is derived from, published in, or linked to another record or artifact. | None by itself. It may become stale. |
| Support | One claim, mechanism, or argument is offered as grounds for another claim under stated conditions. | Requires an explicit reason, scope, and compatible defenses/evidence before reliance. |

Boundver can supply dependency topology. Doorstop or StrictDoc can supply requirement/source traceability. Upheld owns the support semantics only when it can say why the relationship matters and what grounds justify relying on it.

A generated view may combine these relation types, but it must label their provenance and never promote a dependency or fresh trace into evidence.

## A shared claim needs more than a link

The Object Management Group's assurance standard lets a package expose selected claims. A separate package records the argument connecting claims from other packages. This gives us a place to explain why one guarantee meets another requirement. It does not prescribe our JSON layout or prove the claims. [Structured Assurance Case Metamodel 2.3, October 2023, sections 11.4–11.6](https://www.omg.org/spec/SACM/2.3/PDF).

| Proposed record | What belongs there |
|---|---|
| Component register | Owned promises, assumptions, implemented defenses, and separately labeled recommendations |
| Exported contract | Claims that other components may rely on |
| Shared-contract register | Participating claims, support mapping, conditions, owner, and its own defenses |
| Manifest | Included files, exported names, external references, and optional topology providers |
| Generated view | Resolved sources, open questions, relation types, cycles, and change-impact context |

These names describe planned roles. S15 will define the fields and a schema version. Upheld already uses binding for a person's evidence choice; shared contracts need a distinct name.

Recommendations about how best to enforce a promise remain proposals. They need rationale, scope, bypass paths, fault challenge, cost, and residual uncertainty, and they must not appear as though the recommended mechanism already exists.

## Existing trace systems provide an adoption bypass

A project should not need to migrate its entire requirements or dependency model before using Upheld.

S15 should define provenance for imported records and references. S16 should be able to assemble a view using optional external context such as:

- Boundver component IDs, contract facets, and affected consumers;
- Doorstop or StrictDoc requirement IDs and source links;
- build-system affected-target output;
- ReqIF or requirements-management records as candidate obligation sources.

Imported `suspect`, `affected`, `reviewed`, passing-test, or link-hash state is context only. It never becomes an Upheld evidence verdict or binding. The importer should minimize duplicate authoring without inheriting the source tool's acceptance semantics.

For standalone use, Upheld may keep minimal locators, fingerprints, and relations required to verify its own evidence basis. That fallback must remain smaller than a general dependency-management subsystem unless evaluation shows a real unmet need.

## Cycles stay visible and need a justified argument

Requiring A, B, and C together does not create a dependency cycle. Mutual conditions can both hold while their desired outcomes remain false. Formal assume-guarantee rules permit some circular reasoning under added premises. Upheld must record the rule and grounds before claiming a cycle has support. [Abadi and Lamport, Conjoining Specifications, 1995, sections 4.3 and 5](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Conjoining-Specifications.pdf).

A group of mutually dependent claims can define a review scope. Merely visiting every node supplies no evidence. Full promise-level grading remains deferred in [the checker rules](CHECKER.md).

## Cross-project checks bind the participating versions

Pact's matrix associates consumer and provider versions through contracts and test results. Upheld should likewise record which versions and conditions support a shared claim. A version label alone does not establish compatible behavior. [Pact's version-based check](https://docs.pact.io/pact_broker/can_i_deploy).

Keep stable claim IDs separate from source paths and inspected revisions. Missing remote sources remain unknown. Review deleted links using both the old and new graph. Boundver's range review uses that approach so removed consumers remain visible. [Range-review rules](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/docs/reference.md).

A cross-project consumer edge only says where change may matter. The shared-contract record must separately explain why an exported guarantee from one component is sufficient for a consumer obligation, under which versions and conditions, and what evidence defends that support relationship.

## The next work must preserve local choices

S15 defines the schema and migration. It must distinguish membership, dependency, trace, support, and recommendation state. S16 loads component files and builds views; it should consume existing topology providers where available instead of reproducing their graph semantics. S17 adds cross-project mappings and real shared-contract cases. Their gates must cover moved files, missing sources, changed assumptions, conflicting versions, unsupported cycles, imported suspect/affected states, and source-tool drift. Regeneration must preserve reviewed claims and evidence choices.

Small projects may keep one authored file. Splitting files adds reference and review work; its maintenance benefit remains unmeasured. An optional Boundver import can supply component context without requiring every Upheld user to adopt it. A Doorstop or StrictDoc import can likewise reduce duplicate obligation authoring without treating source-tool review status as accepted evidence.

The research reviewed Boundver commit `b8c8861` on 8 September 2026 and Doorstop commit `1f57563` on 9 September 2026. Boundver's 23 graph tests and disposable Git demo passed in the recorded review. A historical-edge test was inspected but could not run because pytest was unavailable. These are focused checks. Large-project trials and a working cross-project resolver remain open.
