"""Check the README's explicit status claims against committed artifacts.

This narrow documentation defense cannot judge arbitrary prose or grade itself.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT, readme=None):
    readme = (root / 'README.md').read_text() if readme is None else readme
    register = json.loads((root / 'examples/heldtospec-contracts/obligations.register.json').read_text())
    ps = register['promises']
    bindings = json.loads((root / 'examples/heldtospec-contracts/obligations.bindings.json').read_text())['bindings']
    expected = {'Promises': len(ps), 'Candidate defenses': sum(len(p['defenses']) for p in ps),
                'Promises awaiting a defense or gap decision': sum(not p['defenses'] and 'gap' not in p for p in ps),
                'Accepted gaps': sum('gap' in p for p in ps), 'Bound evidence records': len(set(bindings.values()))}
    observations = json.loads((root / 'examples/heldtospec-contracts/observations.json').read_text())
    runs = [x for x in observations['observations'] if x['id'] == 'RUN-002']
    if len(runs) != 1:
        raise ValueError('Expected exactly one historical RUN-002 observation')
    expected['Library tests reported passing'] = runs[0]['result']['passed']
    findings = []
    for label, number in expected.items():
        match = re.search(r'^\| ' + re.escape(label) + r' \| (\d+) \|', readme, re.M)
        if not match or int(match.group(1)) != number:
            findings.append({'code': 'status_count_mismatch', 'subject': label, 'expected': number})

    collapsed = ' '.join(readme.lower().split())
    stale = ['nothing has been measured from a real register',
             'heldtospec has no register', 'neither is here yet']
    for claim in stale:
        if claim in collapsed:
            findings.append({'code': 'obsolete_status_claim', 'subject': claim})

    if 'full upheld cli remains unbuilt' not in collapsed:
        findings.append({'code': 'cli_status_requires_review', 'subject': 'README.md'})
    if any((root / p).exists() for p in ('src/upheld', 'upheld/__main__.py', 'pyproject.toml')):
        findings.append({'code': 'cli_status_requires_review', 'subject': 'package added; inspect actual command state'})

    required_02 = (
        'schemas/0.2/register.schema.json',
        'schemas/0.2/evidence.schema.json',
        'schemas/0.2/bindings.schema.json',
        'schemas/0.2/assurance-report.schema.json',
        'tools/assurance_report.py',
    )
    if 'schema 0.2 now represents that product model' not in collapsed:
        findings.append({'code': 'schema_02_status_requires_review', 'subject': 'README.md'})
    missing = [path for path in required_02 if not (root / path).is_file()]
    if missing:
        findings.append({'code': 'schema_02_status_requires_review', 'subject': ', '.join(missing)})

    return findings


if __name__ == '__main__':
    try:
        findings = check()
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({'result': 'could_not_look', 'error': str(exc)}))
        raise SystemExit(2)
    print(json.dumps({'result': 'violated' if findings else 'clean', 'findings': findings}, indent=2))
    raise SystemExit(1 if findings else 0)
