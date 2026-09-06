# upheld

What a codebase promises, what upholds each promise, and whether it still does.

**Design stage. Nothing is built, and nothing has been measured from a real
register.** This repository holds the method, the design of the tool, the
reviews that shaped it, the reference material it draws on, and the two
measurements that exist. It exists so that implementation starts from a record
rather than from memory.

## What it is for

A register states what a codebase promises and what defends each promise -- a
test, a checker, a type, a runtime invariant, or a deliberate gap -- and points
at the evidence that the defense works. Three pieces keep such a register
honest:

| Piece | Does | State |
|---|---|---|
| Survey tool | Scans a codebase for candidate promises, raises the odd and the missing for a decision, asks what kind of thing defends each, emits the register | Sketched in `docs/SURVEY_TOOL.md` |
| Evidence producers | Grade a defense -- a mutation run, a seeded violation, a compiler pass -- and append what they observed | Mutation runner specified in `docs/CHECKER.md` |
| Checker | Compares the tree now against what the bound evidence observed, and reports which grades are no longer entitled | Specified in `docs/CHECKER.md` |

The method the register implements is `docs/METHOD.md`. It was derived across
four repositories that did not read each other's work and converged anyway.

## Reading order

1. `docs/METHOD.md` -- the method, normative. Read the requirements key first.
2. `docs/CHECKER.md` -- the checker design, normative. Read the open problems
   before the command surface.
3. `docs/SURVEY_TOOL.md` -- the piece that produces the value and is the least
   designed.
4. `docs/DECISIONS.md` -- why this is its own repository, and what else was
   decided on the way.
5. `reviews/` -- four external reviews, verbatim, each headed with what was
   accepted and what was pushed back on.
6. `reference/` -- what was taken from boundver, ConnectLang and heldtospec,
   by file.
7. `measurements/` -- the two numbers that exist.
8. `examples/` -- where the real registers are, and why they are not here yet.
9. `messages/` -- drafts to the agents working the other repositories.

## Status

- The hashing profile (`CHECKER.md`, T17) is unwritten and is the first
  artifact an implementation needs.
- `METHOD.md` and `CHECKER.md` disagree about the register schema. The
  checker's is the intended one; the method document is being revised in its
  home repository.
- Two real registers exist elsewhere, both in an older schema. Neither is here
  yet.
- The first target for the survey tool is heldtospec, which has no register.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
