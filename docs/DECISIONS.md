# Decisions

Recorded so that a later reader can tell a decision from an oversight, with the
condition that would change each one where there is one.

## Where the method lives

The question, as asked:

> should the methodology (once it is shareable) be:
> a. hand rolled per repo?
> b. put in a dedicated tool?
> c. be part of boundver's offerings?
> d. be part of heldtospec's offerings?
> e. other

**Decision: its own repository, holding the method and the tools.** Reached in
three steps, kept because each corrected the last.

The first answer was (e): the document now, a versioned register schema next,
extract only what had been built twice. It collapsed under one question -- a
schema nothing enforces is a document with braces -- so (e) was (a) with a
reading order.

The second answer was (a), read as "nothing shared but the idea," which the
evidence supports: three repositories derived compatible taxonomies from prose
alone. But (a) as phrased was "hand rolled per repo," set against (b) "a
dedicated tool." That contrast is each-builds-its-own versus one-shared-tool,
and a shared document is compatible with (a).

The third answer followed from an observation: every finding in the exercise
came from the survey, and the checker only stops findings from rotting. The
survey is the tool worth building, and all four surveys were already performed
by a tool -- an agent with a shared taxonomy prompt -- that nobody had
packaged. That is (b), and it needs a home that is neither of the two
repositories it grew out of.

**Not (c).** boundver ratchets declared contracts; this ratchets the defense of
declared contracts. It is the same architecture one level down, and widening
boundver's subject from "did the contract move" to "is the contract defended"
would cost it its focus. The architecture is copied instead; see
`reference/boundver.md`.

**Not (d).** heldtospec's translation of the idea into its own domain is real
and is a different product: a contract clause can be given the oracle a test
gets from mutation -- a datum that must pass and one that must fail -- and that
belongs in heldtospec. This tool checks registers; heldtospec validates data.

Would change it: a second repository wanting the checker and finding this one
harder to adopt than copying the design.

## What was earned by duplication

The rule applied throughout: a shared mechanism is extracted when it has been
built independently more than once, never when it is anticipated.

- **Mutant catalogue running.** Built by B as a catalogue with
  `expected: survives`; run by A as an audit that counted red as caught; run by
  heldtospec through a driver over mutmut. Three repositories, three shapes,
  one job. Extracted, as the companion runner.
- **Freshness checking.** Built by A for a seven-minute generator. B's
  generator is sub-second and regenerates instead. Earned once, and folded into
  the checker as a register-provenance finding rather than a command.
- **The register format.** Built compatibly nowhere. Not extracted; specified.

## The name

`upheld`. A promise is upheld; the register records what upholds each one; the
checker asks whether it still is. Free on GitHub and PyPI when chosen.
Rejected: `stillheld`, too close to a word nobody wants near a tool;
`steelhead`, a long-standing Riverbed product.

## The license

Apache-2.0, matching heldtospec, from which `docs/METHOD.md` and
`docs/CHECKER.md` were copied. The patent grant matters for a tool meant to
gate CI in repositories the author does not own. One license for code and
documents; no separate documentation license.

## Language

Python, unless a reason appears. Three of the four source repositories are
Python, boundver is Python 3.10+, and the checker reads JSON and git.

## Deliberately not here yet

- **No package scaffold.** "Nothing is built" is meant literally.
- **No hashing profile.** It is the first artifact, and writing it before an
  implementation exists to test it against would be the confident deduction
  the method warns about.
- **No register for this repository.** It will be the first thing the survey
  tool is run against, after heldtospec.
- **No move of `METHOD.md` out of heldtospec.** The copy here is a snapshot;
  the original is mid-revision there. Once that lands, this repository becomes
  the home and heldtospec keeps a pointer.
