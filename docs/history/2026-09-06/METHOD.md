<!--
Snapshot of docs/OBLIGATION_SURVEY.md from heldtospec (https://github.com/yzm1/heldtospec), taken 2026-09-06.
Source sha256 prefix 138f5f6bd081669f, 1256 lines. That file may be revised there; this is the
version the rest of this repository was written against. In this document
"this repository" means heldtospec, and paths such as tools/, tests/ and
src/heldtospec/ are heldtospec paths. Relative links have been redirected.
-->

# Obligation survey

**Version 1.0 — 6 September 2026.**

A method for deciding what to test, and in what order, when the honest
starting position is "the suite is large and nobody knows what it holds."

[TESTING_STRATEGY.md](https://github.com/yzm1/heldtospec/blob/main/docs/TESTING_STRATEGY.md) is what this method produced when
run against this repository. This file is the method itself, written so it can
be run against a different one. Where the two disagree about this project,
TESTING_STRATEGY.md is right: it has been checked against the code.

**This document is normative.** It states requirements a survey either meets or
does not, numbered so they can be cited, each paired with the observation that
produced it and with the condition under which a reader can tell it has been
violated. [Conformance](#conformance) collects all of them. The prose around each
requirement is the evidence for it, not decoration: a rule whose defect nobody
can name is a rule nobody should adopt.

## The claim

The unit of work is the **obligation** -- a promise the code makes that
something outside it depends on -- and not the test, the module, or the
technique. Everything else here serves that unit.

The two obvious alternatives fail in the same way. "Improve the tests" has no
termination condition and no way to detect progress. "Apply the testing
taxonomy" produces output invariant to the codebase: the first version of
TESTING_STRATEGY.md was written that way, and its opening records the result --
it "would have read almost identically for any Python data tool, and it
mis-ranked its own priorities." It ranked config fuzzing second on general
grounds. Twenty-five malformed configs later produced twenty-five clean exits
and no defect.

An obligation cannot be domain-invariant. It either names something this code
promises or it does not exist.

## Versioning, and why this document needs it

Requirement identifiers are an interface. Three repositories replied to the
unversioned draft of this file and all three cited requirements by number; one
structured its entire compliance report around them. Between that draft and this
version, two requirements changed meaning, one changed strength, one had its
detection condition reversed, and two were added. **Those replies now report
against wording that no longer exists, and nothing said so** — which is `O7` and
`O8`, versioned linking, failing between four repositories inside the document
that requires it and marks it never built.

This section is the fix, and it is the first implementation of that requirement
anywhere in the set.

**The compatibility rule.**

- An identifier is never reused and never renumbered. `V5` means what `V5` has
  always pointed at, whatever its strength.
- Strength moves in both directions and is not a version-breaking change. It is
  the whole point of tying strength to evidence.
- Wording may be narrowed or corrected. A change that alters what conformance
  *means* is listed in the changelog against its identifier.
- A withdrawn requirement keeps its number and is marked withdrawn. It is not
  deleted, because somebody's report cites it.
- A claim that turns out to be false is struck through and kept, for the same
  reason.

### Changelog

**1.0** — first versioned release. Everything below moved after A, B and C
replied to the unversioned draft, and mostly because they did. A report written
against that draft can be re-checked from this table alone.

| | Change | Source |
|---|---|---|
| `O2` | The five values were a closed set; they are now seven, and the set is explicitly open. A mechanism fitting none is recorded as itself | C, and B's two extra cells |
| `O9` | **Added.** Environment unavailability is its own field, never an `answered_by` value | B |
| `O10` | **Added.** Deployment reachability is its own field, with the condition that arms it | A |
| `V2` | Detection condition **reversed**. Look for a failure indistinguishable from a real violation, not one indistinguishable from a clean tree | A |
| `V4` | Was "until mutation has graded that test"; now "until a fault under a stated model has been shown to be discriminated". Mutation is the default instrument, not the definition | C |
| `V5` | **SHOULD → MUST**, and the wording gained the three-state clause: red is not caught | A, B, and this repository, each running it |
| `X2` | Was "cheaper than regeneration"; now about the ratio. Where regeneration is cheap, regenerating *is* the guard | B and C, independently |
| `H1` | Unchanged, but its justification was wrong: the open count does not measure movement | C |
| `Rp3` | Unchanged, now explicitly named as the one requirement with no mechanical check | A |
| — | Three claims struck: the untested floor, the ranking formula as a governing rule, and the `type` oracle's attribution | C |
| — | A's checker inventory is forty, not thirty-nine | A |

## The repositories behind the numbers

Every figure in this document comes from one of four repositories. They are
lettered so a reader can tell which, because provenance is the first thing this
method asks of a claim and the last thing a document usually supplies about its
own.

| | Shape | What was run | Contributes |
|---|---|---|---|
| **A** | A service monorepo | A survey of 1,586 obligations, classified by artifact; forty checkers executed | The only three-value distribution; the first half of V5 |
| **B** | A versioning library | A survey of 620 obligations, re-classified blind under a pre-registration | A second classified register; a seeded-violation run; the pre-registration protocol |
| **C** | A compiler for a dependently-typed language | No survey. A pre-registered measurement of its own obligation table | The artifact column, committed February 2026; the only measured `type` share; the counterexample that traced a promise through three layers |
| **this repository** | A data-quality library | A survey, thirty-eight modules measured by mutation, and a ten-dataset seeded-violation run against its contract compiler | [TESTING_STRATEGY.md](https://github.com/yzm1/heldtospec/blob/main/docs/TESTING_STRATEGY.md), and the third V5 result |

A, B and C were worked independently, none with access to the others' results.
All three have since read this document and replied to it, and those replies are
the source of most of what follows. Where a reply corrected this document, the
correction is recorded in place rather than folded in silently.

Figures for this repository are as of commit `830a1ea`, September 2026. A's are
as of `cb2c13cd`, B's as of `849f79e` on 6 September 2026, and C's as of
`6586e09f1` and `5c858debd`. None has been re-taken since, which is a limitation
this document elsewhere warns about and demonstrates once, below.

## How to read a requirement

Requirement strength records **how much evidence stands behind the rule**, not
how strongly anyone feels about it.

| Keyword | Means | Earned by |
|---|---|---|
| **MUST** | Violating it produced an observed defect in at least one of the four repositories, and the defect is described where the requirement appears | Something broke |
| **SHOULD** | Argued from a single instance, or proposed and not yet run anywhere. Adopt it, and expect it to move | One observation, or none |
| **MAY** | Genuinely optional. Recorded so that omitting it reads as a decision rather than an oversight | Nothing yet |

A **SHOULD** whose evidence is "proposed and not yet run" is marked as such in
place. Three requirements below carry that mark: one oracle never exercised, and
the two halves of versioned linking, which no survey in this set has built.

Movement runs both ways and has run both ways. Eight requirements were demoted
from MUST when this section was written, because arguing for a rule is not the
same as having been bitten by its absence. **V5 has since been promoted the other
way** -- it was the most-argued-from and least-run rule here, three repositories
ran it, and each returned a defect. That is the only route up: a defect, not a
further argument.

No requirement below is a MAY. That is a finding rather than an oversight: every
rule this method has produced so far is one it claims is necessary, which is a
shape worth distrusting in any list of twenty-seven, and the first thing a reader
adopting this should push back on.

Each requirement also states **how a reader detects that it has been violated**.
That is not a formality. This document's own central claim about artifacts is
that a rule which nothing can check is a description wearing a rule's grammar,
and a normative document exempting itself from that would be the clearest
possible instance of the failure it describes.

## Two passes, and the oracle that decides whether they can fuse

Run the reading pass to completion before writing a single test.

The reason is contamination. Choosing what to test while writing tests silently
selects for obligations that are convenient to satisfy, and the selection is
invisible because it happens one decision at a time. Separated, the survey is
free to record an obligation it has no idea how to discharge.

Separation is the remedy rather than the principle. The principle is that a pass
needs **an oracle that is not the author's judgment**, and separating discovery
from writing is how a pass gets one when nothing else supplies it. Where an
independent oracle already exists, the passes can safely fuse: mutation
contradicts the author regardless of what the author chose to write, so a pass
driven by it discovers real and inconvenient things while building. The same
holds for enumerable obligations, whose oracle is the artifact list itself.

What has no such oracle is reading for promises, which is most of a survey and
the part that produces the cross-file obligations. There, separate.

The split is checkable after the fact. Read the hand-found obligations and ask
which of them anyone would have started with if the goal had been to finish a
test that day. If the answer is "none of them", the split worked. Compatibility
of a stored row against a later model version, a security policy that degrades
to a default role when its input is unset, two code paths in one file handling
the same condition in opposite directions: each is a poor place to start
writing and a good place to start reading.

> **P1 (SHOULD)** -- The reading pass completes before any test is written, unless
> the pass is driven by an oracle that is not the author's judgment. Mutation and
> artifact enumeration qualify; reading for promises does not.
> *Detected by:* every obligation in the register being one a reader would have
> been willing to start writing that day.

## What an obligation records

| Field | Holds |
|---|---|
| `name` | The promise, stated so it can be false |
| `source` | File and line of the code that creates it |
| `confidence` | `verified` means the code creating it has been read and quoted. `suspected` means the shape is present and the failing case is not demonstrated |
| `evidence_tier` | How much of the claim rests on behaviour outside the text read. See below |
| `why` | What is lost when it breaks, as consequence rather than category |
| `detail` | The mechanism, with the quoted code |
| `answered_by` | The kind of artifact that discharges it. Five values; see below |
| `the_test_that_would_catch_it` | Prose. What evidence would falsify the promise |
| `satisfied_by` | Which artifact discharged it, **at which commit** |
| `next_step` | Present whenever the obligation is not yet answerable |
| `status` | Open, answered, or carrying an unresolved `next_step` |

`the_test_that_would_catch_it` outranks any technique tag whenever the two
disagree, and they disagree often. In A's twenty-two hand-found obligation
kinds, four had free text reading "not a test -- a template assertion" or
"not a test first: a baseline, then a checker" while carrying technique tags of
`example` and `negative_auth`. The prose was right every time. A tag is applied
afterwards; the prose is the judgment.

> **O1 (SHOULD)** -- `name` states the promise so that it can be false. A noun
> phrase naming a component is not an obligation.
> *Detected by:* reading the name and asking what observation would contradict
> it. If none exists, the row is a label.
>
> **O2 (MUST)** -- `answered_by` is present on every obligation and names the
> mechanism that discharges it. The seven values below are the groupings in use;
> a mechanism fitting none of them is recorded as itself and reported, never
> forced into `test`.
> *Detected by:* a count of obligations missing the field, which is the first
> number a register should be able to produce about itself. A register in which
> every obligation fits the vocabulary exactly has probably been rounded to it.
>
> **O3 (MUST)** -- `the_test_that_would_catch_it` is present as prose, and
> outranks any technique tag it disagrees with.
> *Detected by:* rows where the prose says "not a test" while the tag names one.
> Four such rows existed in A, and the prose was right in all four.
>
> **O4 (SHOULD)** -- `confidence` distinguishes `verified`, meaning the code
> creating the obligation has been read and quoted, from `suspected`, meaning the
> shape is present and the failing case is not demonstrated.
> *Detected by:* a `verified` row whose `detail` quotes nothing.
>
> **O5 (SHOULD)** -- `next_step` is present whenever the obligation is not yet
> answerable, and carries the question that would resolve it rather than a
> restatement of the gap.
> *Detected by:* an obligation with `status: open` and no `next_step`, which is
> an item nobody can pick up.
>
> **O6 (SHOULD)** -- `evidence_tier` records how much of the claim rests on
> behaviour outside the text that was read.
> *Detected by:* comparing correction history against the tier. This is a
> SHOULD because the axis has been through one revision already and may go
> through another.
>
> **O9 (MUST)** -- Whether a mechanism needs an environment unavailable where the
> survey runs is recorded in **its own field**, never as a value of
> `answered_by`.
> *Detected by:* a classification whose justification names a missing shell,
> absent service or unbuilt adapter rather than a mechanism.
>
> This is B's finding and it is the best-controlled result in this document.
> Fourteen of sixteen obligations B classified as `review` turned on an
> environment the repository cannot construct -- the clearest being an obligation
> requiring three shells to parse a script, filed as needing human review because
> two of the shells are absent on that host, while the checker that parses all
> three exists and runs where they are present. The field was carrying two
> orthogonal facts and the second silently ate the first, in the direction that
> hides work which is actually doable. B tested the repair rather than asserting
> it: all sixteen moved on re-classification, control tests held at 88%, and
> **none of sixteen control tests moved to `checker`**, so the fix does not
> manufacture the category it was written to rescue.
>
> **O10 (MUST)** -- Whether the deployment as it stands can reach the defect is
> recorded in its own field -- `live`, `latent`, or `impossible` -- and a latent
> obligation names the condition that arms it. A latent entry without an
> `armed_by` is worse than no entry: it reads as dormant forever and nothing
> fires when the precondition changes.
> *Detected by:* a mechanical tell A found rather than argued. Every confirmed
> finding in A's register ships as a strict xfail that fails today. A dormant one
> cannot: it passes, and strict mode reports that as a failure. An obligation
> whose demonstration cannot be written is either latent or misfiled, and the
> register will say which the moment the field exists.
>
> The rule that follows carries the weight: **a latent obligation's artifact
> guards the arming condition, because the obligation itself has nothing to guard
> until the condition holds.** That gives a second pin shape. A scope pin fails
> when a live defect spreads; an *arming* pin passes today and goes red on the
> change that wakes a dormant one -- and it watches a different file from the one
> carrying the defect. A's example: a sign-up path reachable only by federated
> identity, with no client declaring a third-party provider, armed by a one-line
> configuration change in a template the handler knows nothing about.
>
> Enforcing it produced two results in a register of 38. It refused an obligation
> holding one live claim and one latent one, because marking the pair latent
> contradicted its own strict xfail -- split, both were clearer. And it grouped
> two billing defects in different obligation kinds with different `answered_by`
> values, because both were armed by the same unanswered question: which of two
> stacks is deployed. No other field in that register connects them.

## Unread dependence

Reliability falls as more of a claim rests on **behaviour outside the text being
read**. That is the axis, and it is not the same as how many artifacts the check
spans.

The obvious version of this axis was linking distance -- one file, then an exact
join, then a fuzzy name match -- and it has a counter-example. Three errors made
in one session were all single-file reads with zero joins and zero name
matching, and all three were wrong for the same reason: the claim rested on a
library's semantics that had not been read. The sharpest was a numeric guard
with a `try/except` below it returning `None` on any failure, which made a
mutant look equivalent. It is not equivalent: the underlying library returns a
real coefficient for Boolean, Date, Datetime and Duration, and the guard is what
declines them.

Linking distance survives as a consequence rather than as the axis. A fuzzy
obligation-to-test link is the extreme case of unread dependence: the entire
claim rests on someone else's naming, and none of that naming has been read.

| Tier | What the claim rests on | Correction history |
|---|---|---|
| **Read** | Only the text in front of the reader | Correct first time |
| **Unread dependence** | A library's or a service's behaviour, inferred rather than run | Wrong repeatedly, and silently |
| **Structural** | An exact join inside one artifact type, names resolving exactly | One correction, and it stayed fixed |
| **Fuzzy** | Someone else's naming, unread by construction | Cannot be corrected, only bounded |

The tiers differ in a second dimension that matters more for planning: **what it
costs to check them.**

An unread-dependence claim is falsifiable for almost nothing. Calling the
library on a Boolean column is one line, and it settles the question outright.
A fuzzy link is not falsifiable at any price, because there is no ground truth
to compare against. So the two unreliable tiers call for opposite responses:
probe the first, bound the second.

This is one failure wearing two costumes. Ranking config fuzzing second on
general grounds, and calling a mutant equivalent by reading the code beneath it,
are both a confident deduction standing where a cheap probe was available.
Twenty-five malformed configs settled the first. One library call settles the
second. **Where a probe exists, a deduction is not evidence.**

> **P3 (MUST)** -- Where a probe costing minutes would settle a claim, the claim
> is not recorded as evidence until the probe is run. This applies to the
> document reporting the survey as much as to the survey.
> *Detected by:* any claim in the register whose `detail` reasons about a
> library's, service's or tool's behaviour without quoting a run of it.

### What fuzzy linking does to a verdict

Matching obligations to tests by name over-matches badly. An obligation about
service registration drew forty covering tests including a websocket smoke test
and a classifier end-to-end test, on shared words.

The asymmetry is what makes it dangerous. A false `untested` costs one look and
self-corrects. A false `adequate` is silent and removes the item from the
worklist permanently. So treat `adequate` as "not yet read" rather than "held",
and spend the reading budget there rather than on the untested list.

**An earlier revision went one step further and called the untested count a
floor. It is not, and C's counter-example is decisive:** a hundred protected
obligations whose tests are named unlike them produce a hundred false untested
while the true unprotected count is zero. Cost asymmetry justifies triaging the
two lists differently. It licenses no numerical bound in either direction.
Report **no link found** as its own state, distinct from confirmed absence, and
give the count no floor until something has executed rather than matched.

That distinction is what separates a name-matched verdict from a graded one. A
survey that runs the artifact against a seeded violation can claim a floor,
because nothing was inferred. A survey that matched words cannot.

> **P2 (MUST)** -- A verdict produced by matching obligations to artifacts on
> shared words is recorded as `not yet read`, never as `adequate` or `covered`.
> *Detected by:* sampling ten `adequate` verdicts and reading the artifacts. If
> any of the ten does not hold the property, the field was reporting the join.

## Versioned linking

A link recorded without a commit is unfalsifiable.

If the obligation outlives the test -- and it does, which is the reason to keep
obligations at all -- then a test can be deleted, or refactored into something
vacuous, and the obligation will silently re-link to some other keyword match.
Nothing reports that anything changed. That is the same defect the survey
exists to find, reproduced inside the survey.

Record `satisfied_by` as artifact plus commit. When that artifact stops
existing, or its content hash moves without the obligation being re-read, the
obligation re-opens. A survey without this looks identical on the day it is
written, which is why it is the easiest component to leave out.

**It catches disappearance and not vacation.** A test can remain in place, stay
correctly linked, keep passing, and still hold nothing for the property it
appears to cover. One test here was written for three duration-parsing branches
that could never be reached, and it fixed them. It checks five frequency strings
against a single two-row frame five hours apart and asserts one gap, so `5ms`,
`250ns`, `30s` and `1w` all pass whatever they were parsed as. It proves the
strings no longer raise. It cannot see `5ms` read as five nanoseconds. No
deletion, no re-link, no commit boundary crossed, and versioning reports nothing.

Only mutation found it. Which means `answered_by: test` and a *measured*
`answered_by: test` are different claims about an obligation's health, and the
survey needs to distinguish them.

> **O7 (SHOULD -- proposed, never built)** -- `satisfied_by` records the artifact
> **and** the commit at which it discharged the obligation. An artifact name
> alone is not a link. No survey in this set has built this; it is argued from a
> defect the method would reproduce, not from one it has observed.
> *Detected by:* grepping the register for `satisfied_by` values carrying no
> revision. A survey that omits this looks identical to one that does not, on
> the day it is written, which is why it is the easiest field to skip.
>
> **O8 (SHOULD -- proposed, never built)** -- An obligation re-opens when its
> `satisfied_by` artifact stops existing, or when that artifact's content hash
> moves without the obligation being re-read.
>
> C's reply is right that a hash is not enough: an unchanged test can stop being
> adequate when the implementation, specification, dependencies, target or build
> flags move, and a recent run may have tested an old revision. Its list --
> source revision *and dirty-tree state*, command, toolchain, target,
> configuration, exercised scope, result, omissions, run time -- is what evidence
> needs to carry. And **invalidation means reassessment is required, not that a
> regression has occurred**, which is a third state again.
>
> Building the grader here found the constraint that bounds it. A baseline
> reporting a diff on every regeneration cannot be used as a baseline, so a
> timestamp cannot live in the ratcheted artifact. Provenance and baseline are
> two files, not two fields: one records how the evidence was obtained and is
> allowed to churn, the other records what was concluded and must be stable
> enough to compare. Putting C's list in the ratchet would destroy the ratchet.
> *Detected by:* running the check over a commit range and confirming it reports
> at least one re-opening on a range where an artifact is known to have changed.
> A re-opening rule that has never fired has not been shown to work.

## What answers an obligation

The most consequential design error in this method is treating "which technique"
as the open question when the open question is **which kind of artifact**.

The symptom is a vocabulary that reports the *location* of an artifact it has no
*name* for. A field meaning "runs in a workflow" gets attached to obligations
whose real answer is a repository-wide checker, because the taxonomy has entries
for kinds of test and no entry for a checker at all. The fix is not a further
technique. It is an `answered_by` axis. Three values are the minimum; A's
independent derivation settled on five:

- **type** -- makes the violation unrepresentable, so nothing needs to run.
- **checker** -- a rule over a surface, failing on the next new instance.
- **ratchet** -- a rule over *time*: this must still match what a previous
  release produced. No checker over the current tree answers one.
- **test** -- exercises behaviour on chosen cases and asserts an outcome.
- **property** -- exercises a generated space against an oracle, and chooses no
  cases.
- **runtime invariant** -- asserts or alarms in production, and therefore sees
  nothing before it happens.
- **accepted** -- decided, by someone entitled to decide, to be undefended.

Seven, and the last two additions came from B's reply rather than from anyone's
design. **`property` is 28.5% of B's register** -- 177 obligations. A
differential against the platform's own matcher over a generated space does not
choose cases, and it fails differently from an example test: a property with a
weak oracle survives mutants exactly as an example with a weak assertion does,
and the repair is not the same one. Folding those 177 into `test` puts B's test
share at 83% and is the instrument reporting itself.

**`ratchet` was in use here and had no cell.** X1 requires one for the exit
criterion, V2 makes ratcheting a checker clause, and the decay section says an
exit criterion without one is a milestone rather than a gate -- while the
vocabulary folded it into `checker` as a parenthetical. B found five obligations
whose load-bearing clause is closure over time. Five is small enough to ignore
and still a named artifact the vocabulary could describe and not classify.

**Twice now, `answered_by` has been found absorbing a fact that is not a
mechanism.** B discovered that environment unavailability was eating its
classifications; A discovered that deployment reachability had nowhere to go and
was being spread across `confidence`, `accepted` and `status`, all wrongly. The
two repositories did not know about each other's finding, the facts they
recovered are unrelated, and the structural error is identical: a single-valued
field naming the answer attracts every orthogonal fact that has no field of its
own, and absorbs it in the direction that flatters the register. B's ate work
that was actually doable; A's ate the distinction between a defect nobody can
reach and a defect nobody decided about.

That is a property of the axis rather than of either repository, and it predicts
more of the same. When a value in `answered_by` is hard to assign, the first
question is whether a second field is missing, not which value is closest.

**The list is open, and C's reply is why that has to be said.** O2 requires one
value from this set while the failure modes section warns that a taxonomy is a
list of what has been named so far. Both cannot be requirements. The set is a
descriptive grouping: it went three to five to seven in three revisions, twice
because somebody classifying a real register ran out of cells. A mechanism that
fits none of them is a finding about the axis, not an obligation to be forced
into `test`.

The last is what a three-value axis loses. Without it, "no artifact exists" and
"we decided not to build one" occupy the same cell, and the second re-enters the
worklist on every pass.

This repository supplies a worked instance of that cell, in shipping code rather
than in a test suite. Its data-contract compiler turns a published contract into
checks, and the function's own docstring concedes a boundary by naming what it
handles: the *enforceable* promises. Reading the whole function, there are three
tiers and only one of them has a name.

| Tier | What happens to the promise | Instances |
|---|---|---|
| Enforced | Compiles to a check | Nullability, uniqueness, allowed values, ranges, regex, schema, freshness, row counts, null-percentage SLAs |
| Known unenforceable | A `logger.warning` | A validity SLA with no metric behind it; a check naming a metric with no expected value, "so it cannot fail"; a check with neither |
| Silently dropped | Nothing at all | A declared foreign key, which parses under a strict model, lints clean, verifies clean, and is read by no code anywhere in the package |

Neither of the lower tiers is `accepted`, and an earlier revision said the middle
one was. C's reply corrects it: **`accepted` is a decision about a promise, taken
by somebody with the authority to take it. A warning is not acceptance, and a
silent omission is not acceptance.** Both lower tiers are undefended promises;
what separates them is only whether anything says so, and neither has been
decided about by anyone.

That correction sharpens the requirement rather than weakening it. `accepted` is
the one value in the axis that cannot be computed from the artifacts, because it
records an authority rather than a mechanism. It must be declared, with a reason
and by someone entitled to declare it, and an undefended promise carrying no such
declaration is a finding and not a cell.

The middle tier also holds a vacuity detector that nobody called one. "Names a
metric with no expected value, so it cannot fail" is precisely the property
mutation is run to find, applied to a promise rather than to a test, and it
already works. The distinction this axis draws is not academic: the same
codebase implements it, one branch of one `if` at a time, without a name for
what it is doing.

On A, 803 obligations needed a test, 620 a checker and 155 a type. A test
answers barely half, in a repository holding forty checkers with
twenty-one of them wired to nothing.

Those three numbers sum to A's entire obligation count, which is the tell that
the classification producing them was the three-value one. `runtime invariant`
and `accepted` hold zero there by construction rather than by measurement: they
were not available to be chosen. The five-value axis is argued for below on
other grounds, and no distribution has yet been taken with it anywhere.

**The strongest evidence for this axis is not a distribution, it is a repeated
failure.** Three surveys, run independently from one shared taxonomy, each began
by classifying every obligation as a test. Two later found the defect and named
it the same way: a vocabulary reporting the *location* of an artifact it cannot
name. B has not, and its own method statement shows why -- its assessment pass
reads only the test files, so it cannot report a checker even where one is the
answer, in a repository whose shipped product is a checker.

C exhibits the same failure from the other side, and it is the sharpest instance
because nobody had asked it to survey anything. Its testing methodology runs to
nine audit categories, eight of which are kinds of test. Its targets are test
files per crate, test-to-code ratio and assertion density; it schedules itself
quarterly; and it has no category for a checker, a type, a runtime invariant or
an accepted decision -- in a compiler whose README promises that "the compiler
fences every choice, so no guarantee is ever silently lost". In the same
repository, its normative specification carries a table of compiler obligations
with a **"Delivered via"** column naming, per row, the pass or the type-system
extension that discharges each one.

That column is not `answered_by`. It records what *implements* an obligation
rather than what would *catch it breaking*, and that difference is what the
oracle table below exists to draw. But it is one column away, it was committed in
February 2026 -- seven months before the earliest survey here -- and it sits
alongside an audit framework, written later, that cannot express what it
records.

Four for four on the failure; two for four on catching it. The repository that
came closest to the answer before anyone posed the question is the one that then
wrote the most test-centric audit of the four. Whatever produces this bias, it
is not ignorance of the alternative.

**Each branch has its own validity oracle**, and this is what the axis is really
for. Classifying the answer is only useful if it names the evidence that proves
the answer works:

| `answered_by` | What proves it discriminates | Cost |
|---|---|---|
| `type` | **Unsourced.** Not the compiler: C's reply establishes that the compiler is part of the system under test and its own acceptance is not an independent oracle. An external authority -- a database's DDL, a checked proof artifact, a differential against a reference implementation -- is the shape, and none is exercised here | Unknown |
| `checker` | A seeded violation it must catch, kept as a fixture | Minutes, once |
| `test` | Mutation. Nothing else grades an assertion | Hours per module |
| `runtime invariant` | A fault injected where it runs | Hours, plus somewhere to inject |
| `accepted` | Nothing. The record is the artifact | The only honest zero |

**Two of those rows have been exercised, two are unsourced, and the fifth has
nothing to exercise.** Mutation runs on this repository and on B. The seeded
violation has now run in three repositories, which is what promoted V5.

The `type` row is the correction this section most needed. An earlier revision
gave it "the compiler, free", sourced to C. C's reply removed both halves. The
description was wrong on the facts -- the website component it cited reads a
saved golden and does not execute the compiler, and the collector it cited is not
the production router. And the principle was wrong: *the compiler is part of the
system under test, and its own acceptance is not an independent soundness
oracle.* What grades a type-discharged obligation is an authority outside the
thing being graded. No survey here has exercised one.

`runtime invariant` remains a proposal. `accepted` is not unexercised -- its
oracle is deliberately nothing, which is what makes it the honest cell rather
than an empty one.

> **V4 (MUST)** -- An obligation is not reported as answered by a test until
> some fault has been introduced under a stated fault model and the test has been
> observed to discriminate. `answered_by: test` and a measured `answered_by:
> test` are different claims.
> *Detected by:* an obligation whose `status` is answered, whose `answered_by` is
> `test`, and for which no fault was ever introduced.
>
> An earlier revision required mutation specifically, on the grounds that nothing
> else grades an assertion. C's reply narrowed that correctly: mutation is a
> powerful instrument for sensitivity to a *selected* fault set, and killing the
> selected mutants still does not establish that the intended property was
> observed or that the operator set models the relevant failures. A replayed
> historical defect, a deliberately corrupted artifact, or an injected fault
> demonstrates the same sensitivity. Mutation remains the default because it is
> automatic and adversarial; the requirement is a justified fault model and an
> observed discriminating outcome. Timeouts and build failures are not kills.
>
> **V5 (MUST)** -- An obligation is not reported as answered by a checker until
> a violation has been seeded and the checker has been observed to **distinguish
> it from a clean tree and from a failure to look**. Red is not caught. An audit
> counting a non-zero exit as a catch scores a missing environment variable as a
> pass, which is A's finding from running it.
> *Detected by:* the absence of a stored violation fixture per checker, and by
> any audit whose result column has two states rather than three.
>
> This was a SHOULD marked *proposed, never run* through four revisions of this
> document, which argued from it in four places. Three repositories then ran it
> and each returned a finding: A executed forty checkers and found three that
> could not look and seven red and unread; B seeded three violations against one
> checker, caught all three, and found that a deleted input reports byte-
> identically to a stale one; this repository generated one witness and nine
> counterexamples against its contract compiler and found a published guarantee
> defended by nothing. It is the only requirement here promoted by being run.
>
> **V6 (SHOULD -- proposed, never run)** -- An obligation is not reported as
> answered by a runtime invariant until a fault has been injected where it runs.
> *Detected by:* no survey in this set has classified a single obligation into
> this branch, so the requirement has never been reached, let alone tested.

This is where a "the check is proven able to fail" entry belongs. It is not a
kind of test sitting unused in a technique list; it is the checker branch's
mutation. A technique list that carries it and requires it of nothing has
misfiled it, and the consequence is that a repository can hold forty
checkers with no seeded violation between them while the survey reports on
assertion quality in tests only. Ungraded checkers and vacuous tests are the
same defect on two branches, and an instrument built for one branch counts one.

**Classify by mechanism, not by file location.** A ratcheted sweep over the tree
is a checker whatever directory it lives in. Two in this repository sit in
`tests/` and carry a self-marking exemption token so the sweep can contain the
string it forbids -- mechanically checkers, filed as tests. Reading
`answered_by` off the path overstates the test share.

> **V1 (MUST)** -- `answered_by` is assigned from what the artifact does, not
> from the directory it sits in.
> *Detected by:* any obligation whose `answered_by` was derived from a path.
> Two artifacts in this repository are ratcheted sweeps living under `tests/`;
> a path-derived classification files both as tests.

**Whether the distribution varies by domain is not known, and an earlier version
of this document claimed it did.** That claim read: a service tree comes out 803
test to 620 checker, while two library repositories "measured the same way" both
come out tests-dominant. They were not measured the same way. B's assessment
reads only test files, so its test-dominance is its instrument reporting itself
rather than a finding about libraries. This repository has never been classified
by artifact at all -- the axis postdates its survey and was never applied back,
and its strategy document contains no occurrence of the word. The real state is
one classified repository, one that cannot see past tests, and one that was never
measured. Three sources, one measurement.

The claim is worth reporting as a wrong one because of how it survived. It was
false in the way this method exists to catch: a verdict resting on a name-match
rather than a look, in the section arguing that a false `covered` is the
expensive direction because it removes the item from the worklist permanently.
Four passes over the document did not find it. Reading the file whole did.

What survives is narrower. A field that reported the same mix everywhere would be
describing the instrument rather than the repository, and A's mix is not what a
general prior predicts: a test answers barely half. That is enough to make the
axis worth taking. It is not enough to say what drives the variance, and nothing
here yet does.

Settling it needs classifications run with an instrument capable of reporting a
checker. Two now exist and they do not settle it.

B re-classified its 620 obligations blind, against a falsifier committed before
the classifier was written, and returned 338 test, 177 property, 100 checker, 5
ratchet. Folded onto A's three values that reads roughly 515 test to 105 checker
-- 83% against A's 51%, which is the direction a domain claim predicts. B
declines to call it a comparison, and is right to: A was classified three-value
from the start and B five-value blind, and two measurements on unmatched
instruments are the shape the `adequate`-verdict section above warns about. The
state is **two measurements, partially reconcilable, differing in the predicted
direction, instruments still unmatched.**

An earlier revision said a dependently-typed compiler would "obviously" return a
high `type` share, so measuring C would confirm nothing in doubt. C measured it,
against a prediction recorded first, and found **one explicitly type-delivered
row in seven -- 14.29%**. The obvious answer was wrong, and the sentence
asserting it was the reason nobody had checked.

**A checker is worth building only if it does four things.** It fails on the tree
as it stands, or ratchets against a recorded baseline. It enumerates rather than
returning a boolean. It separates "found nothing" from "could not look". And it
runs somewhere that fires. Every clause of that comes from a defect found in
checkers that were already shipping.

> **V2 (MUST)** -- A checker fails on the tree as it stands or ratchets against a
> recorded baseline; enumerates rather than returning a boolean; distinguishes
> "found nothing" from "could not look"; and runs somewhere that fires. A rule
> meeting three of the four is not a checker.
> *Detected by:* each clause separately. The third is the one that hides, and an
> earlier revision looked for it in the wrong direction. It said: check whether
> the failure is distinguishable from a clean tree. A's run found the opposite
> shape -- the failures were distinguishable from a clean tree and
> **indistinguishable from a real violation**, because "could not look" and
> "found a violation" shared an exit code. B found the same thing from the other
> side: a deleted input reporting byte-identically to a stale one. Look for three
> states a caller can tell apart -- found nothing, found a violation, could not
> look -- not two.
>
> A third instance, from building the grader in this repository, shows the clause
> biting one level deeper. Its pipeline stops scheduling after a task raises, so
> a check later in the list never runs -- and its absence from the results reads
> at a glance exactly like having run and stayed quiet. Taking that silence as
> "did not fire" reports a working check as vacuous. The run now tracks `absent`
> as its own state. Three repositories, three artifacts, one clause.

## Location is not execution

A boolean meaning "declared in a workflow" is wrong in both directions, and
both have been observed.

It **under-reports** when the artifact's real answer is a checker the vocabulary
cannot name, so the field describes where a file sits rather than whether
anything runs it. It **over-reports** when the workflow exists, is correctly
configured, and has not fired. This repository is 424 commits ahead of
`origin/main` with nothing behind, on a workflow that triggers on push and pull
request, and its pre-commit hooks are configured but not installed in
`.git/hooks`. Every checker here would score "wired" and none of them has
evaluated those commits.

That figure read 410 when this paragraph was first written, and 424 when the
document was next read whole. Nothing happened in between except ordinary work.
The sentence arguing that a declaration proves nothing was itself a photograph
of a number that had already moved, which is the shortest available
demonstration of the paragraph it appears in.

Record `last_actually_ran` as a timestamp rather than `wired` as a boolean.
Declaration is cheap and proves nothing.

> **V3 (MUST)** -- Execution is recorded as `last_actually_ran`, a timestamp
> taken from the run, never as a boolean meaning "declared somewhere".
> *Detected by:* comparing the newest timestamp in the register against the
> repository's most recent commit. If nothing has run over the last hundred
> commits, the survey is describing a plan.

## Ranking

A survey that ends with a thousand items and no order is not a work queue.

Rank by **the size of the failure mode times the absence of any technique that
addresses it**. Size comes from counting how often the mode has already occurred
here, which most repositories can supply from test docstrings and commit
messages. Absence comes from the survey.

That product, and not severity alone, is why mutation ranks first in
TESTING_STRATEGY.md: the mode it addresses is the largest and no other technique
touches it at all.

**It cannot be the governing rule, and C's objection is the reason.** A first
catastrophic memory-safety failure has a historical count of zero, and a
technique that is present but ineffective suppresses the second factor while
protecting nothing. Both errors run the same way: toward what has already gone
wrong and away from what has not gone wrong yet. Prior attention shapes the
counts as much as risk does. Use consequence, exposure, and the cost of resolving
the uncertainty, and treat historical frequency as evidence inside that judgment
rather than as the judgment.

## Health is open threads, not item count

A survey's size measures how much has been noticed. Its health measures how much
is still moving.

The mechanism is `next_step`, and it is more general than a to-do marker. It
lets an obligation ship **unfinished**: recorded as suspected, with the question
that would resolve it written down. One such entry shipped as "determine which
deployment template is live"; following that step later resolved the obligation
and turned up an unrelated three-way configuration divergence nobody was looking
for.

A test-writing pass has no equivalent state. An item is written or skipped.
Unfinished-but-recorded needs a pass that is not trying to close anything, which
is what separation buys and what an independent oracle buys without it. That is
where the compounding happens, because a wrong-but-concrete artifact recruits
its reader as a collaborator. Criticism is cheaper than construction.

> **H1 (SHOULD)** -- A survey reports its count of unresolved `next_step` entries
> alongside, and with equal prominence to, its obligation count. The obligation
> count alone measures how much has been noticed.
> *Detected by:* a survey summary quoting a total and no open-thread count.
> B reports 413 of 620 obligations carrying a non-empty residual gap and had
> never published that number, which is the asymmetry this requirement exists to
> catch.
>
> An earlier revision claimed the open count measures whether anything is moving.
> C's reply refutes it: an abandoned register retains its open entries
> indefinitely. The count identifies unresolved work. Movement needs two counts
> taken at different times, and this requirement does not deliver it.

So count unresolved `next_step` entries and report that number. A survey
carrying open threads is working. A survey with none is either finished or
abandoned, and those look the same from the item count alone.

This repository runs the mechanism without the name: TESTING_STRATEGY.md ends
with "Open decisions this work surfaced", carrying four threads. Two of the four
were produced by the mutation pass rather than by the survey, which is the
argument for treating measurement as a permanent source of obligations rather
than as a phase that ends.

## The exit criterion is a measurement, and measurements decay

Checkboxes finish. That is their defect: a completed checklist reports
completion whether or not the risk moved, and under fuzzy linking it can be
completed by naming files well.

Pick a criterion generated from the code rather than from the survey. The one
used here is a mutation score on the modules that decide a verdict, with every
survivor killed or recorded as equivalent with its reason. Mutants come from the
source, so no amount of survey bookkeeping satisfies them. And the score is not
the goal: **a score is evidence; the goal is that every survivor has been read
and has an answer.** Forcing a number by killing survivors that hold nothing is
the same error one level up.

The failure mode is decay. A measurement is a photograph, and a checklist at
least stays where it was left. This repository's mutation table records
thirty-eight modules, and the driver that produces it is the one tool in
`tools/` referenced by no workflow and no hook. There is no machine-readable
baseline for a ratchet to compare against, and the declared `[tool.mutmut]`
scope is still one module while the table holds thirty-eight -- the config and
the evidence disagree about what is even in range. Every number is true as of
the day it was taken, and nothing re-takes it.

The obligation "these modules stay at their measured score" is real, and by the
axis above it is `answered_by: checker` -- a ratchet on recorded scores, not a
test. An exit criterion with no ratchet is a milestone, not a gate.

> **X1 (MUST)** -- The exit criterion is generated from the code rather than from
> the survey, and is ratcheted against a machine-readable baseline that something
> re-evaluates.
> *Detected by:* two checks. Whether a baseline file exists in a format a program
> can compare, and whether any workflow or hook names the tool that produces it.
> This repository fails the second, and says so below.
>
> **X2 (MUST)** -- The survey's own generated state is guarded by a check that
> runs at every occasion it is meant to guard. Where regeneration is expensive
> the guard must cost materially less; where regeneration is cheap, regenerating
> and comparing *is* the guard and no second mechanism is warranted.
> *Detected by:* timing the generator first. B and C objected to this
> independently and both were right: B's generator is sub-second, so
> regenerate-and-compare costs nothing there, and a cached freshness check would
> add an invalidation problem in exchange for no saving. The rule is about the
> ratio, and an earlier revision stated it as an absolute.

A, B and this repository each found their own instrument undefended. Two have
since closed it, in different shapes worth telling apart. One regenerates its
register under a `--check` mode that fails when the generated view disagrees
with the source, and runs its mutation catalog as its own job. The other hashes
the generator's inputs and diffs a commit range instead of regenerating --
milliseconds against a seven-minute generator, which is the property that makes
it viable on a commit hook rather than in a workflow. That cost asymmetry is the
design decision: a freshness check that costs as much as the generation it
guards will be run exactly as often as the generation, which is to say when
someone remembers.

The occasion for the second one is the sharpest instance of decay this method
has produced. A survey documenting that generated state goes stale silently was
staged for commit while its own regeneration was still running, so the committed
copy predated a finding the fresh copy contained. The document about silent
staleness went silently stale inside the hour, and surfaced only because a
`git diff` happened to be open. Nothing in the artifact detected it, because
describing a failure mode provides no detection of it -- which is the whole
distinction between a description and a checker, arriving as a demonstration
rather than an argument.

This repository is now the one of the three that has not closed it. C is not
counted here because it ran no survey to leave undefended -- though its own audit
is scheduled quarterly rather than gated, which is the same failure with a
calendar in place of a ratchet.

## Teeth-checking

Every new check is proven able to fail before it is believed. Break the thing it
claims to hold and watch it go red.

It is the checker branch's oracle, and the counterpart to mutation rather than
a substitute for it. A cross-format equivalence sweep was teeth-checked by
casting one loader's columns to text; a model-based store test by removing a
field from the identity key.

**Two operations wear this one name, and only one of them has ever been done.**
Teeth-checking at authoring time proves a *new* check can fail, on the day it is
written, by the person writing it -- that is the practice above, and it works.
Seeding a violation against an *existing* inventory of checkers is the
retrospective audit: take A's forty that already ship, break what each one
claims to hold, and count how many notice. Nobody in this set has done the
second. The first is a habit; only the second is a measurement, and it is the
one this document argues from.

Reading is not a substitute. A test asserting `pytest.raises(ConfigError,
match="column_range")` here passed, looked correct, and discriminated nothing:
a second error further down the same path also said "column_range". Only
mutation showed that it held nothing. So `confidence: verified` on an obligation
says the hazard was read; it says nothing about whether the covering test
discriminates.

The habit matters more than any tag. A taxonomy may contain an entry for "the
check is proven able to fail" and still have it required by zero obligations,
which is what happens when it is filed as a kind of test rather than as a
condition on every artifact -- and especially on every checker.

## Measurement discovers obligations too

The method as described runs discovery, then building. There is a third pass,
and it runs backwards: measurement finds obligations that no amount of reading
produces.

A cluster of surviving mutants inside one function is not ten weak assertions.
It is an entry point no test called. One such cluster here was a remote
streaming loader that returned an empty frame for every input, so a config
pointing at a remote source produced a green verdict over zero rows. Another
showed that three of the commonest failures from a cloud SDK matched no branch,
because the tests had been written against invented message strings rather than
real ones.

None of those was reachable by reading for promises. Feed them back into the
survey as obligations rather than fixing them in place, or the next reader
re-derives them.

The sharpest instance available came from running this method over the tool
built to implement it. The clause grader here exported a verdict called
`inverted`, counted it among its actionable findings, and documented it -- and no
branch anywhere in the grader could emit it. Reading the code had not found that
in three passes. Surveying the package's own tests for what each obligation was
answered by found it immediately, because the obligation "a reversed comparison
is reported" had no artifact that could produce the reported value. A test now
asserts every verdict in the actionable set is emitted by some test, so the gap
cannot reopen.

This also bounds a claim the method makes elsewhere: absence of a technique is
not evidence of absence of coverage. Config fuzzing was ranked second here on
exactly that inference and was wrong. A cheap probe beats a confident deduction.

## Reconciling the specification against the implementation

C carries one mechanism none of the others has, from a document otherwise
superseded by everything above. Its audit reconciles three lists rather than two:
what the specification requires, what the implementation provides, and what the
tests exercise. Comparing all three pairs finds a class this method cannot.

An obligation survey reads code for promises, so every obligation it finds is one
the code already makes. **A promise the specification makes and the code never
implements is invisible to it.** There is no source line to read, nothing to
quote into `detail`, and no artifact for a link to attach to. It fails as an
absence, and absences are precisely what the rest of this method is built to
surface. The survey will report the specification's other clauses in confident
detail and say nothing at all about the missing one.

Where a written specification exists, run the third comparison. Where one does
not, its stand-in is whatever the project publishes: documented behaviour, a
contract format, CLI help text, a README's promises. Each is a promise made
somewhere other than the code that is supposed to keep it, and each can be
enumerated independently of the code and then joined to it.

> **S1 (SHOULD)** -- Where the project publishes promises somewhere other than
> its source -- a specification, a contract format, documented behaviour, CLI
> help -- those promises are enumerated independently and joined to the code,
> and clauses with no implementation are recorded as obligations.
> *Detected by:* a published clause that appears in no obligation. This is a
> SHOULD because it is adopted from C on its argument, with one instance run
> here: a foreign-key clause in this repository's contract format that parses,
> lints, verifies, and is read by no code.

This repository has such a stand-in and the join is short: its contract model
enumerates every clause a published contract may contain, and reading the
compiler that consumes them, clause by clause, is what produced the three-tier
table above -- including the foreign-key clause that no code reads. That took
one reading of one function. Nothing in the obligation survey had surfaced it,
because there was no code to read for a promise nobody implemented.

## Targeting the expensive tier

Mutation is the only oracle that grades assertions and it costs hours per
module, so it cannot be run everywhere. It needs a targeting function, and a
cheap static screen is the right one.

The screen is a **read-queue, not a verdict**, which is the honest use of a
heuristic instrument: it says where to spend the expensive measurement, and it
is allowed to over-match because nothing is concluded from a hit.

The shape worth screening for has already been named here, in the docstring of
a test written to replace one that could not fail: *the control flow is held and
the amounts are free.* Assertions that check a call did not raise, or that a
count is one, or that two numbers stand in some relation, hold the path and say
nothing about magnitude or unit. Four separate modules here failed that way --
memory figures that held whatever the unit, a rate limiter whose throttle count
held while its arithmetic was free, a statistics module, and a duration parser
whose five frequency strings all produced the same answer.

This has been done once already and it worked. Sweeping for short-probe
substring assertions put most of the weak ones in one area; measuring the module
they covered returned 54.8%, among the lowest baselines recorded here. The weak
assertions and the unheld code were the same finding from two directions.
Run the screen first, and let it choose the modules.

## Predict the oracle before measuring it

When a sweep needs an expected answer for each subject, write the expectations
first, from the contract. Deriving them by running the code asserts whatever the
code currently does, which is a snapshot and not an oracle.

The same rule applies to models: write the model from the stated contract, so
that when model and implementation disagree the model wins until someone decides
otherwise.

## Deliberately absent

Record the empty cells and why they are empty, with the condition that would
change each answer. Without this section a later reader cannot distinguish a
decision from an oversight, and re-derives it.

The "what would change it" column is the part that earns the table. An absence
with no falsification condition is an opinion. And the table must be revisable
in both directions: one row here was removed after it turned out the codebase
already carried the behaviour the row dismissed as irrelevant.

> **D1 (SHOULD)** -- Every deliberately-absent entry carries the condition that
> would change the answer. An absence with no falsification condition is an
> opinion.
> *Detected by:* a row in the table with an empty "what would change it" cell.

## What this rests on, and what would falsify it

This document was written from A and this repository. B arrived afterwards,
surveyed independently from the same starting taxonomy by someone who had not
read this; it corrected two claims below and confirmed several others, which is
the only reason those rows carry more than one source. C arrived last and was
never surveyed at all. It contributes by having produced the central idea before
anyone posed the question, and by supplying the one oracle here that is observed
rather than proposed. It did not produce the struck row below; that was found by
re-reading this document.

Read the middle column before the claim. Several entries rest on a single
observation, two are proposals that have never been run, and one row records a
claim this document previously made and no longer supports.

> **Rp1 (MUST)** -- Every quantitative claim states which repository it came from
> and when it was taken.
> *Detected by:* a number in the report with no attribution. This document
> violated the requirement in its own first four drafts, and the correction is
> the lettering above.
>
> **Rp2 (MUST)** -- A claim resting on a single observation, or on none, is
> marked as such where it is used and not only where it is catalogued.
> *Detected by:* a confident sentence in the body whose provenance row says one
> instance. The struck row below is what this requirement exists to prevent.
>
> **Rp3 (MUST)** -- A survey report is read whole before it is shared, not as a
> diff against its previous state.
> *Detected by:* asking the reader what the document says in a section they did
> not edit. **This is the one requirement here with no mechanical check, and it
> is named as the exception rather than left for a reader to notice**, because A's
> reply pointed out that P2 and V2 both say a rule nothing can check is a
> description wearing a rule's grammar -- and that leaving Rp3 unmarked puts that
> exact object inside a normative document. The reason it stays: every defect
> this document has corrected in itself, eight in one pass and eleven in the pass
> after it, was found by reading the file end to end and none by reading the
> changes to it. A rule with no checker is worth stating when the evidence for it
> is that strong, provided it says so.

| Claim | Derived from | What would falsify it |
|---|---|---|
| The unit of work is the obligation | A, B, this repository | A taxonomy-first survey that ranks its own priorities as well |
| Surveys classify everything as a test unless told otherwise | All four exhibited it; two found it. B's reply confirms it did not find it -- `answered_by` was handed to B in review, so its later adoption is not evidence about discovery | A survey or audit framework that classifies by artifact from the start without being prompted |
| `answered_by` is load-bearing, not decorative | A, B and this repository. B re-classified 620 obligations blind and returned four populated values plus two it had to invent | A repository where every obligation genuinely is answered by a test, classified with an instrument that could have said otherwise |
| ~~The distribution varies by domain~~ | **Struck, and not restored.** B's blind re-classification reads ~83% test against A's 51%, the direction a domain claim predicts -- but A was classified three-value from the start and B five-value, and two measurements on unmatched instruments are what the `adequate` section warns about | Two registers classified on the *same* instrument, differing repositories, agreeing |
| A fuzzy `adequate` verdict is an unknown mixture | A. Grading the join cut a pass rate from 751 to 234, leaving 517 too loosely linked to trust | Grading the join on another repository and finding the pass rate holds |
| ~~The untested count is a trustworthy floor~~ | **Struck.** C's counter-example: a hundred protected obligations with dissimilarly named tests give a hundred false untested against a true count of zero. Cost asymmetry licenses different triage, not a bound | -- |
| Unread dependence, not linking distance, predicts error | This repository, three errors in one session. A's reply confirms it against its own axis: its clearest single error was one file, zero joins, and wrong, which its linking-distance axis rates most reliable. A also reproduced the failure while writing that reply, flagging three checkers from exit codes and finding on reading that two were already correct | A repository whose error pattern tracks linking distance instead |
| A fault under a stated model is the oracle for `answered_by: test` | This repository and B both run mutation. **C narrowed the claim**: killing selected mutants does not establish that the intended property was observed or that the operator set models the relevant failures | A test that discriminates every seeded fault and still misses the defect the obligation names |
| An external authority is the `type` branch's oracle | **Unsourced, and one revision worse than that.** An earlier version credited "the compiler, free" to C. C's reply removed it: the compiler is part of the system under test, and its acceptance is not an independent oracle | An independent authority -- DDL, a checked proof artifact, a reference differential -- exercised anywhere in this set |
| A seeded violation is the `checker` branch's oracle | **Run three times, three findings.** A executed forty checkers: 3 could not look, 7 red and unread. B seeded three against one checker: 3 caught, and a clause-three failure. This repository ran one witness and nine counterexamples: 8 sound, 1 published guarantee defended by nothing | An inventory audited with three-state grading where every violation is already caught |
| An injected fault is the `runtime invariant` branch's oracle | **Proposed. Never run anywhere in this set, and no survey here has classified an obligation into that branch** | An invariant that survives fault injection while still being worth its cost |
| `property` is a distinct kind, not a flavour of `test` | B, 177 obligations at 28.5%, from a blind re-classification against a pre-committed falsifier | A register where folding `property` into `test` changes no repair and no oracle |
| `ratchet` is a distinct kind, not a clause of `checker` | B, 5 obligations whose load-bearing clause is closure over time. Used unnamed throughout this document in X1, V2 and the decay section | Those five answered by a checker over the current tree |
| Environment unavailability is orthogonal to mechanism | B, controlled: 14 of 16 `review` classifications turned on it; on repair all 16 moved, controls held at 88%, and 0 of 16 control tests moved to `checker` | A register where the two facts co-vary |
| Deployment reachability is orthogonal to mechanism, and needs an arming condition | A, 3 of 38. Enforcement refused a conflated obligation and grouped two billing defects sharing one precondition that no other field connects. The tell is mechanical: a dormant finding cannot carry a strict xfail | A latent obligation whose arming pin never fires and whose defect wakes anyway |
| `answered_by` attracts orthogonal facts | A and B independently, on unrelated facts, neither aware of the other. The generalisation is available to neither alone | A third missing field found that does *not* fit the pattern -- one whose absence distorts something other than `answered_by` |
| Reconciling specification against implementation finds a class surveying misses | C's method. Two instances now: a contract clause no code reads here, and B's six `proposed-behaviour` obligations, which B reports it had held all along without recognising them as a category | Running it on a repository with a written specification and finding every gap already had a source line to read |
| ~~Rank by size of mode times absence of technique~~ | **Struck as a governing rule.** C: a first catastrophic failure has historical count zero, and an ineffective-but-present technique suppresses the second factor. Retained as evidence inside a judgment | -- |
| A static screen can target mutation | One instance | Screen hits that fail to predict low mutation scores |
| Measurement discovers obligations reading cannot | A and this repository. C's traced counterexample is the strongest instance in the set: a specification named the right artifacts, those artifacts had tests, and the composition still failed | A reading pass that independently finds what measurement found |

**Three rows are struck and one was promoted, and the ratio is the finding.**

The struck rows are the method applied to itself and losing. Domain variance read
as a three-way measurement and rested on one. The untested floor was a bound
asserted from an asymmetry that does not imply one. The ranking formula was a
product of two factors that both run toward what has already gone wrong. Two of
the three were caught by reading this file whole; the third came from C, which
had no reason to be gentle about it.

The promotion ran the other way and is the more useful result. The seeded
violation was the most-argued-from and least-run rule in the document -- bolded
twice as the cheapest unrun measurement available. Three repositories ran it,
independently, in three languages, on three kinds of artifact. **Each returned a
defect on the first attempt**: checkers that could not look, a diagnostic that
could not distinguish deleted from stale, a published foreign-key guarantee
defended by nothing. Nothing in the argument for it was worth what running it
once was worth, in any of the three.

One row remains proposed and never run anywhere: the runtime-invariant oracle.
No survey in this set has classified an obligation into that branch, so the
requirement has not been reached, let alone tested. It is now the weakest claim
here, and it is weak in a quieter way than the checker row was -- that one was
argued from constantly, this one is not argued from at all.

A generated finding is a hypothesis, and A and B put numbers on it from
different angles. Roughly a third of a new rule's first output does not
survive reading. Of 418 gap claims put to a reader instructed to refute them,
73 were refuted -- and that reader was told to default to "covered" when
uncertain, which makes a surviving gap stronger evidence and a refutation
weaker. Both point the same way: be reluctant to write "covered", because a
false absence costs one look while a false presence deletes the item from the
worklist permanently.

## Conformance

Twenty-seven requirements, collected. Each restates a rule made where the evidence
for it appears; the wording there governs if the two ever drift.

| | Requirement | Strength |
|---|---|---|
| **P1** | The reading pass completes before writing, unless the pass has an oracle that is not the author's judgment | SHOULD |
| **P2** | Name-matched verdicts are recorded as `not yet read`, never as `adequate` | MUST |
| **P3** | Where a probe costing minutes would settle a claim, the claim is not evidence until the probe runs | MUST |
| **O1** | `name` states the promise so it can be false | SHOULD |
| **O2** | `answered_by` is present and names the mechanism; the seven values are groupings, not a closed set | MUST |
| **O3** | `the_test_that_would_catch_it` is present as prose and outranks any technique tag | MUST |
| **O4** | `confidence` distinguishes read-and-quoted from shape-present | SHOULD |
| **O5** | `next_step` is present whenever the obligation is not yet answerable | SHOULD |
| **O6** | `evidence_tier` records unread dependence | SHOULD |
| **O9** | Environment unavailability is its own field, never an `answered_by` value | MUST |
| **O10** | Deployment reachability is its own field, and a latent obligation names what arms it | MUST |
| **O7** | `satisfied_by` records the artifact **and** the commit | SHOULD -- proposed, never built |
| **O8** | An obligation re-opens when its artifact disappears or its hash moves unread | SHOULD -- proposed, never built |
| **V1** | `answered_by` is assigned from mechanism, never from file location | MUST |
| **V2** | A checker ratchets, enumerates, separates "found nothing" from "could not look", and runs somewhere that fires | MUST |
| **V3** | Execution is recorded as `last_actually_ran`, never as a boolean | MUST |
| **V4** | No obligation is answered by a test until a fault under a stated model has been shown to be discriminated | MUST |
| **V5** | No obligation is answered by a checker until a seeded violation has been distinguished from both a clean tree and a failure to look | MUST |
| **V6** | No obligation is answered by a runtime invariant until a fault has been injected | SHOULD -- never run |
| **H1** | Open `next_step` count is reported with equal prominence to obligation count | SHOULD |
| **X1** | The exit criterion is generated from the code and ratcheted against a machine-readable baseline | MUST |
| **X2** | Generated survey state is guarded at every occasion it is meant to guard, by regeneration where that is cheap and by a cheaper check where it is not | MUST |
| **S1** | Promises published outside the source are enumerated and joined to it | SHOULD |
| **D1** | Every deliberately-absent entry carries its falsification condition | SHOULD |
| **Rp1** | Every quantitative claim states its repository and its date | MUST |
| **Rp2** | Single-observation and unrun claims are marked where used, not only where catalogued | MUST |
| **Rp3** | The report is read whole before sharing, not as a diff | MUST |

### This is not a checklist, and the difference is load-bearing

Elsewhere this document argues that a completed checklist reports completion
whether or not the risk moved. That argument stands, and it does not apply here,
for a reason worth stating rather than assuming.

These requirements are over **the survey's own artifacts** -- does the register
carry this field, has this oracle been run, does this baseline exist. They are
not over the code under survey, and they say nothing about whether it is safe.
Full conformance means the instrument is built correctly and is running. It does
not mean the risk moved.

The distinction has a sharp edge. Twenty-seven of twenty-seven is reachable by a
survey that has enumerated every obligation, graded every test, ratcheted every
score -- and found the code to be in exactly the state it was already believed to
be in. That survey conforms completely and has discovered nothing. Conformance
is a claim about the instrument's construction; the findings are a separate
report, and a survey that leads with its conformance score is doing what this
document warns a mutation score does when it becomes the goal.

### This repository's conformance

Stated because a normative document whose own repository has never been scored
against it is making a recommendation, not a requirement. Every requirement gets
a row, including the ones that cannot be reached here -- a report that lists only
its failures cannot be distinguished from one that stopped looking.

| | Status | Why |
|---|---|---|
| **P1** | Met | The survey ran to completion before any test was written |
| **P2** | Not applicable | No register, so no name-matched verdict exists to mis-report |
| **P3** | Met | The config-fuzzing ranking was corrected by twenty-five probes rather than argued down |
| **O1--O10** | Unreachable | This repository has no register. Its survey output is [TESTING_STRATEGY.md](https://github.com/yzm1/heldtospec/blob/main/docs/TESTING_STRATEGY.md), which is prose, and prose carries no fields. This is the largest gap between what this document asks for and what the repository holding it has done |
| **V1** | Unreachable | Nothing here has been classified by artifact at all |
| **V2** | **Unassessed** | Eight tools sit in `tools/`. Whether each ratchets, enumerates, and separates "found nothing" from "could not look" has never been checked. This cell is the requirement's own third clause, turned on the report |
| **V3** | Not met | Nothing records `last_actually_ran`. The stand-in figure moved by fourteen between two readings of this file |
| **V4** | Partially met | Mutation has graded thirty-eight modules. With no register, no obligation is marked answered by anything, so the rule is met in substance and unreachable in form |
| **V5** | Met | One witness and nine counterexamples were run against the contract compiler. Eight defended clauses each fired one check on exactly the mutated column; the ninth, a published foreign key, fired nothing. Fired and errored were distinguished throughout, which is the clause A's run showed most audits drop. This is one of the three runs that promoted the requirement |
| **V6** | Unreachable | No obligation anywhere in this set has been classified into that branch |
| **H1** | Partially met | Four open threads are reported under "Open decisions this work surfaced". There is no obligation count to report them against |
| **X1** | Not met | `tools/mutate.py` produces the mutation table and is named by no workflow and no hook. There is no machine-readable baseline for a ratchet to compare against |
| **X2** | Not met | Nothing generated here is guarded, because nothing here is generated. A and B have both closed this; this repository has not |
| **S1** | Partially met | Run once, against the contract format, which is what surfaced the foreign-key clause no code reads. Not run against the CLI surface or the documented behaviour |
| **D1** | Met | The "Deliberately absent" table carries a "What would change it" column |
| **Rp1--Rp3** | Met | Only as of this revision, and only because reading the file whole found all three violated |

Sixteen requirements are MUST: P2, P3, O2, O3, O9, O10, V1, V2, V3, V4, V5, X1,
X2, Rp1, Rp2, Rp3. This repository meets five (P3, V5, Rp1, Rp2, Rp3), fails
three (V3, X1, X2), meets one in substance but not in form (V4), cannot reach six
for want of a register (P2, O2, O3, O9, O10, V1), and has never assessed one
(V2).

The score improved by one this revision, and it is worth naming how. V5 was met
by running the measurement the document had been arguing from and never taking --
ten datasets, one afternoon. Nothing was built, no requirement was relaxed, and
the run found a published guarantee this repository defends with nothing. The
cheapest available measurement moved both the score and the code, which is the
argument the rest of this document makes at greater length.

## Failure modes of this method

Stated plainly, because each has occurred.

**The survey becomes the artefact.** Producing obligations is more pleasant than
discharging them, and a growing file feels like progress. Counting open
`next_step` entries rather than obligations is the guard.

**Proxies get trusted past their range.** Counting test files that import a
surface looked informative until measurement contradicted it: two of the
lowest-reach modules here scored 8 of 8 and 18 of 19 under mutation. Reach
counts files, not rigour. Record every proxy with the case that showed its
limit, and retire it out loud.

**Generated rules are believed before they are checked.** Every generated rule
needs a hand-found answer to check against, and the structural tier is where
that check pays: it is the tier where a bug is both likely and fixable.

**The taxonomy is treated as complete.** It is a list of what has been named so
far, and the artifacts it cannot name are invisible rather than unscored. C is
the sharpest instance available: its audit framework enumerates nine kinds of
test among nine audit categories, while its own normative specification, in the
same repository, tabulates obligations discharged by artifacts that none of the
eight can express.

**Nothing fires.** A survey describing a repository whose checks are wired but
untriggered measures the map rather than the territory. If the checks have not
run, that is the first obligation, and the rest of the file is a plan rather
than a status.

**Every promotion becomes a description.** In A, nine detectors were promoted
from findings. All nine shipped as entries in a report and none of them fails a
build; the three that do gate there were built only after somebody explicitly
asked for checkers. The reason is legible rather than lazy.
A test is self-contained and finishes. A checker is a standing commitment
needing a baseline format, ratchet semantics, wiring, and acceptance that it
runs red on its first day -- four decisions, every one of them avoidable by
reaching for the familiar artifact. This is the method's largest risk: it
produces description at exactly the rate nobody stops it.

The counter-example is instructive about what actually stops it. In A a checker
was later built unprompted -- and the trigger was not the finding, which had
been written down and changed nothing for nine detectors. It was being bitten
once, concretely, by the failure the survey described. Naming a
failure mode is apparently not sufficient to change what gets built; a
first-person instance of it is. Which is an argument for probing early, since a
probe is the cheapest way to be bitten on purpose.
