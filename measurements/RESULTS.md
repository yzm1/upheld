# Measurements

Two exist. Both are about the tool's own mechanics; neither is about a real
register. Every number the design would consume from a repository is unknown.

## Synthetic register load and index

`synthetic_register.py`. 10,000 promises, 21,650 defenses, 12.2 MB.

| Operation | Run 1 (2026-09-05) | Run 2 (2026-09-06) |
|---|---|---|
| JSON load | 108 ms | 481 ms |
| Build reverse index, artifact to defenses | 11 ms | 21 ms |
| Diff-first query, 12 changed files | 0.07 ms, 469 defenses | 0.08 ms, 500 defenses |

Both in the same Linux container under unknown concurrent load; the spread on
the load is the container, not the register. The defense count differs because
the second run samples the changed files with a fixed seed of its own. The
conclusion holds at either figure. `docs/CHECKER.md` quotes the first run.

Consequence: `docs/CHECKER.md` does not require a materialised reverse index.

## Walking history for one range

`git log -L74,90:tests/metrics/test_what_a_temporal_setting_actually_means.py`
on heldtospec at 1,262 commits did not complete within 120 seconds. Run to
completion in the background it returned one commit, because the file is new;
the cost is in the walk, not in the result.

Consequence: reconstructing fine-grained identity from history cannot be in the
hot path. The checker compares recorded grounds against recomputed ones, and
`why` is the one command permitted to walk history, degrading to "history
unavailable" on a shallow checkout.

## What deploying would measure

Per repository: promise and defense counts; degree distributions in both
directions; churn of linked artifacts; invalidations per commit and per week by
event kind; the fraction auto-resolved and the fraction needing semantic
review; queue age and time to clear. None of these exists.
