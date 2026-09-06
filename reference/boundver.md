# boundver

<https://github.com/yzm1/boundver>, read at v0.15.0 (`main` at `9119319`,
2026-09-05). Its README describes it as "a Git-aware lockfile and CI check for
contracts shared across components". It runs on Python 3.10 and later, under
the MIT licence.

boundver checks whether a declared contract moved. upheld checks whether the
defense of a declared contract still holds. The two share one architecture,
one level apart, so upheld copies boundver's architecture and none of its code.

## What upheld took, by file

| From boundver | Into upheld |
|---|---|
| `boundary.config.json` and `boundary.lock.json`, both committed, with schemas pinned by URL | The config, register and lock split; T6 |
| Four facets, each with an exit code; `2` reserved for "could not complete the check reliably"; the highest applicable code wins | Facets and consequence-ranked exit codes; T12 |
| `verify_facets`: gate some facets and report the rest | T13 |
| `spec/verify-baseline.schema.json`, the record of acknowledged drift | `ack` and the baseline; T15. boundver's README already carries the warning that became T15: "With a verification baseline, acknowledged lock drift can still be present. It does not prove backward compatibility." |
| `spec/cli-output.*.schema.json`, one published schema per command | T14 |
| `spec/HASHING.md`: tree against working tree, line-ending equivalence, ordering | T17, the first artifact upheld lacks |
| `--source working-tree` as an explicit flag, distinct from a git snapshot | The index-against-worktree race behind A's stale register, modelled rather than hoped away |
| `init --discover` and `migrate-lock` | The adoption ramp; T19 |
| The README section "What it will not tell you" | The non-goals section, and the sentence "does not replace a compiler, build graph, compatibility checker, or consumer test. It supplies the repository-level signal that connects them." |
| Distribution through PyPI, GitHub Action, GitLab Catalog and Docker | To copy when there is something to distribute |

## What upheld did not take

Its subject. `../docs/DECISIONS.md` says why.

## boundver also surveyed itself

Branch `audit/testing-obligations`, unpushed at the time of writing, holds
`spec/testing-obligations.json` with 620 obligations and `spec/mutants.json`
with 119 mutants marked `expected: survives`. That survey is B in the method.
`../examples/README.md` says where it stands.
