# Upheld's README contradicted its committed example

Readers can reproduce a narrow documentation check from this case. The original README claimed that no real register had been measured after a hand survey already existed.

This case concerns Upheld on 6 September 2026. It establishes a specific documentation failure and a checked repair. It does not establish a general prose verifier.

## The source history shows both states

| State | Source | Claim or artifact |
|---|---|---|
| Before | [README at 3cc993e](https://github.com/yzm1/upheld/blob/3cc993edf7810901ce285b013e18fc670e18919a/README.md) | “Nothing has been measured from a real register.” |
| Same tree | [Example introduced at 7dfa532](https://github.com/yzm1/upheld/commit/7dfa532) | 44 promises and 78 candidate defenses |
| After | Current README | States that the hand example exists and the CLI remains unbuilt |

The corrected table links its counts to the committed records. The trade is that readers must distinguish a hand survey from the product CLI.

## One checker detects the known stale claim and count drift

Run from the repository root:

```bash
python tools/check_readme_status.py
python -m unittest discover -s tests -p 'test_*.py'
```

The tests reintroduce the historical absence claim, change a reported count, and make an input unreadable. The checker reports a violation for stale claims and exits 2 when it cannot inspect inputs. It also requests review when package files appear.

The [register](obligations.register.json) records promise `UPH-001` and its checker. It has no accepted evidence binding. The script checks explicit table rows and known wording; a human must still review other claims. The fixture tests establish those limits and never create a product evidence record.
