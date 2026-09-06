# boundver

<https://github.com/yzm1/boundver> -- read at v0.15.0 (`main` at `9119319` on
2026-09-05). "A Git-aware lockfile and CI check for contracts shared across
components." Python 3.10+, MIT.

It is the same tool one level down: it ratchets declared contracts; upheld
ratchets the defense of declared contracts. Its architecture is copied. None of
its code is.

## Taken

| From boundver | Into upheld |
|---|---|
| `boundary.config.json` / `boundary.lock.json`, both committed, schemas pinned by URL | the config / register / lock split; T6 |
| Four facets with distinct exit codes; `2` reserved for "could not complete the check reliably"; highest applicable code wins | facets, and exit codes ranked by consequence; T12 |
| Gate some facets, report the rest (`verify_facets`) | T13 |
| `spec/verify-baseline.schema.json`, acknowledged drift | `ack` and the baseline; T15. boundver's README already carries the warning that became T15: "With a verification baseline, acknowledged lock drift can still be present. It does not prove backward compatibility" |
| `spec/cli-output.*.schema.json`, one published schema per command | T14 |
| `spec/HASHING.md` -- tree versus working tree, CRLF/LF equivalence, ordering | T17, the first artifact upheld lacks |
| `--source working-tree` versus a git snapshot as an explicit flag | the index/worktree race behind A's staleness incident, modelled rather than hoped away |
| `init --discover`, `migrate-lock` | the adoption ramp; T19 |
| README section "What it will not tell you" | the non-goals section, and the positioning sentence: "does not replace a compiler, build graph, compatibility checker, or consumer test. It supplies the repository-level signal that connects them" |
| Distribution: PyPI, GitHub Action, GitLab Catalog, Docker | to copy when there is something to distribute |

## Not taken

Its subject. See `../docs/DECISIONS.md`.

## Its own obligation work

boundver also surveyed itself, on branch `audit/testing-obligations` (unpushed
at the time of writing): `spec/testing-obligations.json`, 620 obligations, and
`spec/mutants.json`, 119 mutants with `expected: survives`. That is B in the
method document. See `../examples/README.md`.
