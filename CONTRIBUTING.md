# Check the documents before submitting a change

Readers are engineers evaluating or building Upheld. They know Git, tests, CI, and JSON. Each current document defines its project terms.

Install the documentation tools in a virtual environment:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-docs.txt
.venv/bin/python tools/check_docs.py
.venv/bin/python -m unittest discover -s tests -p 'test_*.py'
```

Use the [supplied writing skill](.claude/skills/writing-shared-docs/SKILL.md) for shared prose. Its thresholds guide review; the script cannot assess factual truth.

## Preserve the source of each claim

Link counts to a dated record. Keep historical reports unchanged and explain corrections in current pages. Label synthetic test inputs as test data. Record a completed task in [the todo list](TODO.md) with its check result.

The workflow runs on pushes and pull requests. A configured workflow alone establishes no execution history. Local checks and GitHub runs have separate records.
