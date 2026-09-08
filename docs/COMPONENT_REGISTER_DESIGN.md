# Components own claims; shared contracts need their own records

Readers are engineers planning Upheld's next schema. **Keep a component's promises near its code, and give shared contracts an explicit owner.** Combine those files into a generated system view. This is agreed design work for S15–S17; the current exporter uses schema 0.1.

## Boundver supplies component names and change impact

Boundver declares component paths, contract inputs, and downstream consumers. Its named groups can include explicit members or every downstream component. Its current schema keeps those declarations in one central file. Separate authored files would be an Upheld choice. [Boundver schema at the reviewed commit](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/boundary.config.schema.json).

The payments demo traces an API change through a client library and checkout app to an external mobile consumer. External labels end traversal; they do not identify a verified remote contract. [Runnable demo](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/scripts/demo_consumer_impact.py), [graph code](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/src/boundver/_consumer_graph.py).

## A shared claim needs more than a link

The Object Management Group's assurance standard lets a package expose selected claims. A separate package records the argument connecting claims from other packages. This gives us a place to explain why one guarantee meets another requirement. It does not prescribe our JSON layout or prove the claims. [Structured Assurance Case Metamodel 2.3, October 2023, sections 11.4–11.6](https://www.omg.org/spec/SACM/2.3/PDF).

| Proposed record | What belongs there |
|---|---|
| Component register | Owned promises, assumptions, and defenses |
| Exported contract | Claims that other components may rely on |
| Shared-contract register | Participating claims, mapping, conditions, owner, and its own defenses |
| Manifest | Included files, exported names, and external references |
| Generated view | Resolved sources, open questions, cycles, and change impact |

These names describe planned roles. S15 will define the fields and a schema version. Upheld already uses binding for a person's evidence choice; shared contracts need a distinct name.

## Cycles stay visible and need a justified argument

Requiring A, B, and C together does not create a dependency cycle. Mutual conditions can both hold while their desired outcomes remain false. Formal assume-guarantee rules permit some circular reasoning under added premises. Upheld must record the rule and grounds before claiming a cycle has support. [Abadi and Lamport, Conjoining Specifications, 1995, sections 4.3 and 5](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Conjoining-Specifications.pdf).

A group of mutually dependent claims can define a review scope. Merely visiting every node supplies no evidence. Full promise-level grading remains deferred in [the checker rules](CHECKER.md).

## Cross-project checks bind the participating versions

Pact's matrix associates consumer and provider versions through contracts and test results. Upheld should likewise record which versions and conditions support a shared claim. A version label alone does not establish compatible behavior. [Pact's version-based check](https://docs.pact.io/pact_broker/can_i_deploy).

Keep stable claim IDs separate from source paths and inspected revisions. Missing remote sources remain unknown. Review deleted links using both the old and new graph. Boundver's range review uses that approach so removed consumers remain visible. [Range-review rules](https://github.com/yzm1/boundver/blob/b8c886100694a0b9f9d45502d072876f07c43444/docs/reference.md).

## The next work must preserve local choices

S15 defines the schema and migration. S16 loads component files and builds views. S17 adds cross-project mappings and real shared-contract cases. Their gates must cover moved files, missing sources, changed assumptions, conflicting versions, and unsupported cycles. Regeneration must preserve reviewed claims and evidence choices.

Small projects may keep one authored file. Splitting files adds reference and review work; its maintenance benefit remains unmeasured. An optional Boundver import can supply component context without requiring every Upheld user to adopt it.

The research reviewed Boundver commit `b8c8861` on 8 September 2026. Its 23 graph tests and disposable Git demo passed. A historical-edge test was inspected but could not run because pytest was unavailable. These are focused checks. Large-project trials and a working cross-project resolver remain open.
