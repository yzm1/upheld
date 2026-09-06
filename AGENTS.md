# Documentation changes use the supplied writing skill

Readers are software engineers evaluating or building Upheld. They know Git, tests, CI, and JSON. Define Upheld's terms at first use.

Read `.claude/skills/writing-shared-docs/SKILL.md` before writing shared prose. Use its supplied checker and reader vocabulary. Keep the supplied files unchanged unless a task calls for editing the skill.

Run `python tools/check_docs.py` before committing documentation. It checks current prose, schemas, recorded counts, local links, and the README status defense. Run `python -m unittest discover -s tests -p 'test_*.py'` when their behavior changes.

Keep dated source snapshots and historical observations intact. Link a correction from current documents. Record unknown facts as unknown. A passing documentation check does not grade an Upheld defense.

Current rules are in `docs/METHOD.md`, `docs/CHECKER.md`, and `docs/SCHEMA.md`. Track work in `TODO.md`. Complete tasks with links to artifacts and observed checks.
