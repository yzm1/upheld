"""Check maintained examples and reviewed rule text, without requiring task closure."""
import hashlib
import json
import re


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_todo(text):
    ids = []
    for line in text.splitlines():
        cells = [x.strip() for x in line.strip('|').split('|')]
        if not line.startswith('|') or not re.fullmatch(r'[DSPCEHL]\d{2,}', cells[0]):
            continue
        task, status = cells[:2]
        require(task not in ids, f'Duplicate task: {task}')
        ids.append(task)
        allowed = {'Complete', 'Open', 'Reopened', 'In progress', 'Deferred',
                   'P0', 'P1', 'P2', 'P0 release gate', 'Later', 'Later decision'}
        require(status in allowed, f'Unknown task status: {task}: {status}')
        if status == 'Complete':
            require(len(cells) >= 4 and re.search(r'\[[^]]+\]\([^)]+\)', cells[-1]),
                    f'Complete task needs closure evidence: {task}')
    require(bool(ids), 'Task list contains no recognized task IDs')


def check_fixtures(root):
    # These examples are explicitly unbound. Future examples may carry evidence.
    for name in ('heldtospec-contracts', 'upheld-status', 'upheld-self-audit',
                 'upheld-self-assurance'):
        folder = root / 'examples' / name
        evidence = folder / 'obligations.evidence.jsonl'
        require(evidence.is_file(), f'Missing evidence fixture: {evidence}')
        require(evidence.read_text() == '', f'Expected unbound example: {name}')
        bindings = json.loads((folder / 'obligations.bindings.json').read_text())
        require(bindings['bindings'] == {}, f'Unexpected binding in unbound example: {name}')


def check_rules(root):
    manifest = json.loads((root / 'docs/rule-review.json').read_text())
    for path, expected in manifest.items():
        text = (root / path).read_text()
        rows = re.findall(r'^\| (\w+) \| (MUST|SHOULD) \|.*$', text, re.M)
        require(len(rows) == len(dict(rows)), f'Duplicate normative rule in {path}')
        require(dict(rows) == expected['strengths'], f'Rule strengths changed: {path}')
        actual = hashlib.sha256(text.encode()).hexdigest()
        require(actual == expected['sha256'],
                f'Rule document changed: review semantics and update docs/rule-review.json: {path}')
