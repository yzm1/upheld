---
name: writing-shared-docs
description: How to write a document other people will actually read - an internal note, an audit or research report, a shared artifact, a README, a memo. Use when writing or revising any prose deliverable for other people, and before publishing an Artifact that is a document rather than an app. Ships a measurement script; run it before publishing.
---

# Writing shared docs

Readers scan. In Nielsen Norman Group's usability tests, **79% of users scanned any
new page and 16% read word by word**. Rewriting the same content to be concise,
scannable and objective measured **124% better usability** than the original -
58% from concision alone, 47% from scannable layout, 27% from dropping promotional
language. Write for the scanner and the reader still gets everything. Write for the
reader and the scanner gets nothing.

## 1. Name your reader, then use only words they own

Before the first sentence, write down who reads this and what they already know.
Everything else follows from that line.

The strongest finding in any documentation audit is the opening test: **name a
category the reader already has.** `A standalone disaster recovery tool for SQLite`
works because the reader owns "disaster recovery tool". `Classifies declared
contract drift across polyglot repositories` fails, because the reader owns none
of it.

Apply the test to every noun, not just the first one. A colleague two teams away
does not know your table names, your branch names, your internal shorthand, or the
nickname your team gave a subsystem. Each one stops them, and they stop for good
after the third.

**The test runs in both directions.** Explaining a word your readers already own
insults them and pads the draft. Colleagues one team away usually own the product
vocabulary and none of the repository vocabulary, so keep the first and translate
the second. Write down which is which before you start, and declare it to the gate
with `--owns` so it stops flagging the words that are fine.

**Three ways out, in order of preference:**

1. **Replace it.** "The foreign key a contract declares was never checked, because
   no code read the field" beats "the `references` clause compiled to nothing".
2. **Define it in six words at first use**, if the term is load-bearing and
   recurs.
3. **Delete the sentence.** If a point cannot survive translation, the reader
   could not have used it.

**Say what the thing is before you say what is wrong with it.** A verdict is
useless to a reader who does not know what was judged. One sentence of context
first: what this system does, who wrote the thing you are responding to, what
they were asked to look at.

## 2. Answer first

**Put the conclusion in the first screen.** Journalists call it the inverted
pyramid, the army calls it bottom line up front, and Barbara Minto's pyramid
principle says the same: main point at the top, support beneath it, evidence at
the base. Nobody has to
earn your conclusion by reading to the end.

Minto orients the reader in four sentences before the answer arrives: a
**situation** they already agree with, a **complication** that disrupts it, the
**question** it raises, then the **answer**. Use it when the reader needs context; skip
straight to the answer when they don't.

**Every section repeats the shape.** Lead each one with its own conclusion, then
the evidence. A reader who stops anywhere still leaves with the point.

## 3. Cut it in half

NN/g's guidance is **half the word count of conventional writing, or less**. Apply
it to the draft you think is already tight.

Delete any section that does not change what the reader does. Interesting is not
the bar, and neither is how hard it was to produce.

**No sentence whose only job is to announce the next one.**

**Cut what the verb already implies.** "The branch carries all thirty-two and the
code that reads them" spells out what "carries" already meant, and by spelling it
out invites the reader to wonder what the bare verb would have meant instead.
Choose the verb that settles it - implements, ships, enforces - and stop.

**Cut the run-up and start at the verb.** "It enumerates every structural defect
it finds and exits 1 if there are any, rather than stopping at the first" is
"It lists every structural defect, then exits 1". The clause before the verb
narrates the writer deciding to act. Delete it and the sentence loses nothing
but its throat-clearing.

## 4. Headings are claims

Write `The published example contract cannot pass its own witness`, and never
`Findings`.
NN/g's rule is meaningful sub-headings rather than clever ones; front-load the
words that carry meaning. A label forces the scanner to read the section to find
out whether they care. A claim lets them skip it and still know what it said.

The table of contents made of claims _is_ the executive summary. If it isn't,
the headings are wrong.

## 5. Give the load-bearing sentences their own weight

One or two sentences in a document carry the argument. A scanner moving through
headings and tables will pass straight over them if they sit in the middle of a
paragraph at body size.

Lift them out: their own line, slightly larger, a rule down the side. Two or three
per document, never more, or the emphasis stops meaning anything. Pick the
sentence a reader would quote back to you.

**Inside a sentence, bold the answer and leave the setup plain.** "The guide
says exit code 4 covers a clause that could not be graded. **It exits 0.**" The
setup reads light, the answer carries the weight, and a scanner who reads only
the bold halves still gets the document.

## 6. Bullets for lists, prose for reasoning

NN/g recommends bulleted lists; Amazon banned slide bullets for six-page
narratives because "writing forces precision that bullet points allow you to
skip." Both are right, in different places.

- **A list** is for parallel items the reader scans and does not need connected:
  four surfaces, six thresholds, the steps of a plan.
- **Prose** is for anything with a _because_ in it. A bulleted argument hides the
  connective step, and the writer stops noticing it is missing.

Never bullet a causal chain.

## 7. State the fact, never your search for it

<!-- prose-gate:ignore -->

"I found no production release" reports the writer's effort. "Nothing has shipped"
reports the world. The second is shorter, checkable, and does not rest on how hard
the writer looked.

When you genuinely do not know, say what is unknown and who can settle it. Do not
dress a gap as a finding.

**And say why.** A fact with its cause attached ends the question. "No CI run
has evaluated the last 468 commits, because the workflow triggers on a push and
the remote has received none since 27 August" saves the reader from assuming
the workflow is broken.

## 8. One voice, and it is not yours

A note circulated inside a team is written by the team. First-person singular puts
a narrator between the reader and the facts, and it invites the question of who is
speaking. Use "we" for what the team did and a plain subject for everything else.
Sign it at the top if authorship matters.

<!-- /prose-gate:ignore -->

## 9. Do the work the document would recommend

If a section ends with "we should check X", check X before you publish and report
what came back. A recommendation is the writer handing the work to the reader, and
the reader is worse placed to do it.

This applies hardest to anything you can run. When a source names a test, run the
test. When a claim is checkable against the code, check it. The finding you get is
worth more than the suggestion, and it is usually the strongest thing in the
document.

## 10. Claim, evidence, consequence

Every claim carries a number, a quote or a table, then what it costs. A claim with
no evidence is an opinion. Evidence with no consequence is trivia.

**Measure outcomes, never effort.** Commit counts, hours spent, files touched,
tickets closed: these say how busy the writer was, and no reader acts differently
because of them. State what changed and when. "Nothing has shipped, because the
branch is still under test work" is the whole fact; the commit count adds nothing
to it.

**Never invent an example.** An illustration you made up is a claim with no
evidence, wearing the costume of evidence. Search for a real one; if none is
findable, state the claim plainly without an illustration and say what would
prove it. A reader who checks an invented example and finds it hollow discards
the argument it was supporting.

**When you claim a change, show both states.** Before and after, close enough
together that the reader can judge whether it is an improvement rather than
taking your word. **Then name the trade it makes.** Almost every real change
costs something, and the colleague who owns the affected work needs that
sentence more than they need the good news.

**Every number carries its provenance and its date.** The first reader to check one
and find it wrong stops trusting the rest of the document.

**Group rows by the reader's question, not by their history.** A fault that is
fixed belongs under fixed, whatever branch it sits on; where it lives belongs in a column. If a row needs a sentence explaining why it is in this table rather
than that one, it is in the wrong one.

**Data goes in tables.** A row beats a sentence saying the same thing, and prose
that recites what a table already shows is the commonest padding in a report.

## 11. State the limits, before the findings

Say what your numbers do not establish, which thresholds are yours rather than a
standard, and what you did not check.

**A caveat the reader cannot decode is worse than no caveat.** "Our fault list is
out of date, so this came from the code" assumes they know which list, why it
matters, and what the alternative was. Name the thing, say what is wrong with it,
say what you used instead. Placed early it reads as rigour. Placed late,
or omitted, the first reader to find the gap themselves treats it as a discovery.

## 12. Objective language

NN/g found promotional language "imposes a cognitive burden" - users have to filter
hyperbole to reach fact, and they **detested** it. That finding is why the banned list
exists. It is a measured effect, and taste never entered it.

<!-- prose-gate:ignore -->

**Banned:** drive, unlock, deep dive, robust, hub, portal, landscape, ecosystem,
going forward, leverage, seamless, comprehensive, holistic, utilise. And the
announcer phrases: it is worth noting, importantly, it should be said, as
mentioned above.

<!-- /prose-gate:ignore -->

## 13. Cut the machine tells

Generated prose has a house style, and readers now recognise it. Every tell below
swaps a rhythm in for a fact, so cutting them shortens the draft and sharpens it
at the same time.

<!-- prose-gate:ignore -->

- **The antithesis reflex.** "X, not Y." "Not just X, but Y." "This isn't a bug,
  it's a feature." State what is true and stop. The contrast almost always carries
  no information.
- **Tic words:** delve, tapestry, testament to, underscore, pivotal, crucial,
  realm, multifaceted.
- **Hedged intensifiers:** truly, genuinely, remarkably, incredibly, undeniably,
  arguably. Each one weakens the claim it decorates.
- **Openers that stall:** "Let's dive in", "Here's the thing", "At its core",
  "In essence", "The result?"
- **The rhetorical fragment.** A one-word question followed by its own answer.
- **Em-dash overuse.** More than about five per thousand words reads as generated,
  and a ` -- ` typed for one counts as one. Most are a comma or a full stop.
- **The triad.** Three parallel adjectives where one would do.
<!-- /prose-gate:ignore -->

## 14. No figures of speech in a factual document

<!-- prose-gate:ignore -->

A run cannot "speak for" a technology. A view does not "want" anything, a service
does not "care", and a branch does not "know best". Giving a system intentions
makes the reader translate before they learn anything, and the translation is
always longer than the fact would have been.

Write the mechanism. "A run holding no assessments could be picked as a
technology's current answer" says what happens. "A run chosen to speak for a
technology" makes the reader work out that you meant the same thing.

The same goes for any decorative metaphor. If a phrase pleased you as you wrote
it, check whether it carries a fact. Conventional usage is fine and not a figure
of speech: documents say things, code reads values, a screen shows a number.

<!-- /prose-gate:ignore -->

## 15. Sentences

Google's developer style guide, in its own words: **"Use active voice: make clear
who's performing the action."** **"Use second person: 'you' rather than 'we.'"**
Present tense. Sentence case for titles and headings. Descriptive link text.

The "you" is the reader you are instructing. The "we" in section 8 is the team
that did the work. A report has both and an "I" in neither.

**Abstraction is what makes prose dense, not length.** `classification`,
`verification`, `implementation` each bury a verb inside a noun, and the reader
unpacks it before the sentence means anything. Short sentences built from buried
verbs still read as dense. Write `we classify`, not `classification is performed`.

| Rule                    | Target                                                 | Source                          |
| ----------------------- | ------------------------------------------------------ | ------------------------------- |
| Passive voice           | under 10% of sentences                                 | Google, GOV.UK                  |
| Mean sentence length    | 20 words or fewer                                      | GOV.UK                          |
| Sentences over 25 words | under 15%                                              | GOV.UK                          |
| Abstraction density     | under 45 `-ion/-ment/-ance/-ity` nouns per 1,000 words | local threshold, not a standard |
| Banned words            | zero                                                   | NN/g objective-language finding |

The last two rows are calibration, not authority. Say so if you publish them.

## 16. Don't mix documentation modes

Diátaxis sorts writing by two questions: does it inform **action or cognition**,
and does it serve **acquiring** a skill or **applying** one. Tutorial, how-to,
reference, explanation. A page that mixes them serves none of them, and a reference
section with explanation woven through returns the explanation too when someone -
or something - searches it.

Most shared notes are explanation plus a plan. Keep the reference in a table.

## Before you publish

```bash
python3 .claude/skills/writing-shared-docs/check_prose.py <file.html|file.md>
```

Nine checks: passive rate, sentence length, long sentences, abstraction density,
banned words, insider terms, machine tells, figures of speech, em-dash rate. Every
failure names the lines that caused it.

Declare the words your readers already own with `--owns TERM,TERM`, or add them to
`reader-vocabulary.txt` beside the script. A declared word stops counting as insider
jargon and stops counting as a banned word, so `dbt` passes the gate and
`leverage` still fails it.

**It still over-counts passive voice.** It matches a `to be` form followed by a past
participle, so an adjective with a participle ending reads as passive. `is different`,
`is present` and `is consistent` are excluded by name, and that list is not
exhaustive. Read the flagged lines; don't rewrite on the number.

The regexes have their own tests. Run them after changing one:

```bash
python3 -m pytest .claude/skills/writing-shared-docs/test_check_prose.py -q
```

Then check by hand:

- Is there an "I" anywhere? Take it out.
- Read it aloud. Every sentence you would not say aloud is a tell.
- Hand it to someone outside the project. Which word stops them first?
- Does sentence one carry news, or does it recap what the reader already knows?
- Is anything here a recommendation you could have carried out yourself?
- Is any status here copied from a tracker rather than checked at the source?
- Does every caveat make sense to someone reading it cold?
- Does the first screen carry the answer?
- Is every heading a claim?
- Does the contents list read as the summary?
- Does every claim have a number, a quote or a table under it?
- Are the limits before the findings?
- Does the plan tag back to the findings?
- Which section would you cut if forced to cut one? Cut it.

## Sources

Nielsen Norman Group, _How Users Read on the Web_ and _Concise, Scannable, and
Objective_ · Barbara Minto, _The Pyramid Principle_ · Google developer
documentation style guide · GOV.UK content design · Diátaxis · Amazon's six-page
narrative practice.
