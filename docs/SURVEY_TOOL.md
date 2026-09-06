# The survey tool

The piece that produces the value, and the least designed. This is a sketch and
not a specification: it carries no numbered requirements, because nothing here
has been tried, and the method's rule is that a MUST is earned by a defect.

## What it does

Four steps, the last of which is the checker.

1. **Scan** a component for candidate promises.
2. **Raise** the odd, the ambiguous and the missing for a decision.
3. **Ask** what kind of thing defends each confirmed promise, and emit the
   register.
4. **Track** whether each defense's evidence still holds -- `CHECKER.md`.

It is a register producer in the checker's sense: it declares itself and its
inputs, the checker fingerprints those inputs and never reruns it, and bindings
live in a file it does not write.

## What the evidence says about each step

**Scan.** The richest sources are mostly language-agnostic: published
documentation, specification files, configuration schemas, CLI help, contract
formats. That is S1 in the method, and it is how ConnectLang's obligation table
and heldtospec's contract module were found. Code-level scanning -- exception
paths, signatures, error strings -- needs an adapter per language, the same
cost the mutation runner carries. Existing tests are an under-used source:
every test asserts a promise, so mining tests for what they assert yields
promises that arrive with a candidate defense attached.

**Raise.** The queue will be large. Roughly a third of a generated rule's first
output in A did not survive reading. What worked was an adversarial second
pass: B's skeptic refuted 73 of 418 gap claims and was told to default to
"covered" when unsure, which makes a surviving gap stronger evidence and a
refutation weaker. Triage should be built skeptical by default, not as a
confirmation click. "Missing" is the hard case, since nobody can scan for a
promise nobody wrote; what can be detected are proxies -- a public surface with
no promise, a specification clause with no implementation, a configuration
field nothing validates. heldtospec's `references` field is exactly that shape;
see `../reference/heldtospec.md`.

**Ask.** This step has one known failure mode and it is the largest finding of
the whole exercise: **a recommender will say "test."** Four repositories, four
times. So the tool presents no default and no pre-selected answer. Better than
a recommendation is a question that derives the kind:

- Must this hold across the whole tree, or on chosen inputs? -- checker, or test
- Can the type system make the violation unrepresentable? -- type
- Can it be seen only where it runs? -- runtime invariant
- Is the decision to leave it undefended? -- a gap, with its reason

There is an evaluation set nobody has used. A holds 1,578 obligations
classified by a person as 803 test, 620 checker, 155 type; B holds 620 with a
blind five-value re-classification. A classifier that cannot reproduce A's
distribution from promise text is biased, and measurably so.

**Track.** The checker.

## What to build first

Not a specification. The scanner, against heldtospec, which has no register --
its method document's own self-score marks every register requirement
unreachable for that reason. Sources in order of expected yield: the contract
format, CLI help text, docstrings on the public surface, and the 5,127 test
functions. Emit candidates. Look at the queue. Its size says whether the
skeptic pass or the question-driven classifier is the second thing to build.

## Open questions

- Whether the scanner is a script per repository sharing a candidate format, or
  one tool with adapters. The mutation runner chose adapters; the same
  reasoning applies and the same cost.
- Whether triage is a file, a command, or a review surface. An agent is the
  usual reader, which argues for a file.
- Whether the classifier is rules, a model, or the questions above put to a
  person. The evaluation set can settle it.
- How a scanned candidate becomes a `DefenseAssertion` with a `subject_scope`
  when the scanner found it in a document rather than in code. The containment
  check in T5 assumes the promise has one.
