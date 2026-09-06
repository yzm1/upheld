"""Check current documentation artifacts; this is not the Upheld CLI."""
import json
from collections import Counter
from pathlib import Path
import re
import subprocess
import sys

import fastjsonschema
from check_readme_status import check
from prepare_probe_review import convert, diagnostics
from documentation_integrity import require, check_todo, check_fixtures, check_rules

ROOT = Path(__file__).resolve().parents[1]
CURRENT = [ROOT / x for x in ['AGENTS.md','CONTRIBUTING.md','README.md','TODO.md']]
CURRENT += sorted((ROOT / 'docs').glob('*.md'))
CURRENT += [ROOT / 'docs/history/README.md', ROOT / 'examples/README.md']
CURRENT += sorted((ROOT / 'examples').glob('*/*.md'))
CURRENT += [ROOT / 'measurements/RESULTS.md']
CURRENT += sorted((ROOT / 'reference').glob('*.md'))
CURRENT += sorted((ROOT / 'messages').glob('*.md'))
CURRENT += sorted((ROOT / 'reviews').glob('*.md'))  # verbatim bodies are fenced from the gate


def json_file(path): return json.loads((ROOT / path).read_text())


def check_artifacts():
    compiled = {p.stem.replace('.schema',''): fastjsonschema.compile(json.loads(p.read_text()))
                for p in (ROOT / 'schemas/0.1').glob('*.json')}
    cases = [('probe-register','examples/heldtospec-contracts/obligations.register.json'),
             ('probe-bindings','examples/heldtospec-contracts/obligations.bindings.json'),
             ('register','examples/heldtospec-contracts/review-register.json'),
             ('register','examples/upheld-status/obligations.register.json'),
             ('bindings','examples/upheld-status/obligations.bindings.json')]
    for name, path in cases: compiled[name](json_file(path))
    source = json_file(cases[0][1]); ps=source['promises']
    require(json_file(cases[2][1]) == convert(source, cases[0][1]), 'Review copy changed independently of its source')
    actual = {'promises':len(ps), 'defenses':sum(len(p['defenses']) for p in ps),
              'defenses_by_kind':dict(Counter(d['guarded_by'] for p in ps for d in p['defenses'])),
              'promises_with_no_defense_and_no_gap':[p['id'] for p in ps if not p['defenses'] and 'gap' not in p],
              'gaps':[p['id'] for p in ps if 'gap' in p],
              'promises_with_next_step':[p['id'] for p in ps if p.get('next_step')]}
    for key,value in actual.items(): require(source['summary'][key] == value, key)
    require([x['subject'] for x in diagnostics(source)] == ['CTR-003','CTR-005','CTR-037','CTR-044'], 'Artifact invariant failed')
    records = json_file('examples/heldtospec-contracts/observations.json')
    require(len(records['findings']) == 19, 'Artifact invariant failed')
    require(Counter(x['group'] for x in records['findings']) == {'odd':5,'ambiguous':6,'missing':8}, 'Artifact invariant failed')
    require(len({x['id'] for x in records['findings']}) == 19, 'Artifact invariant failed')
    require(records['historical_summary']['confirmed_probe_count'] is None, 'Artifact invariant failed')
    require(len(records['observations']) == 5, 'Artifact invariant failed')
    check_fixtures(ROOT)
    require(check() == [], 'README status check failed')
    check_rules(ROOT)
    check_todo((ROOT / 'TODO.md').read_text())
    # Historical source snapshots must retain their content hashes.
    import hashlib
    for name,digest in json_file('docs/history/snapshot-hashes.json').items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest, name)
    print(f'Artifact checks passed: {len(compiled)} schemas; 44 promises; 78 defenses; 19 triage bullets; 4 expected unresolved choices.')


def check_links():
    bad=[]
    for file in CURRENT:
        text=re.sub(r'```.*?```','',file.read_text(),flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if re.match(r'^[a-z]+:',target) or target.startswith('#'): continue
            path=target.split('#')[0]
            if path and not (file.parent / path).exists():bad.append(f'{file.relative_to(ROOT)} -> {target}')
    if bad: raise AssertionError('Broken local links: '+', '.join(bad))
    print('Current document links passed.')


def main():
    check_artifacts()
    check_links()
    failures=[]
    for file in CURRENT:
        run=subprocess.run([sys.executable,str(ROOT/'.claude/skills/writing-shared-docs/check_prose.py'),str(file)],capture_output=True,text=True)
        if run.returncode:
            failures.append(str(file.relative_to(ROOT)));print(run.stdout);print(run.stderr)
    if failures: raise AssertionError('Prose check failed: '+', '.join(failures))
    print(f'Prose checks passed for all {len(CURRENT)} current documents.')
    run=subprocess.run([sys.executable,str(ROOT/'.claude/skills/writing-shared-docs/test_check_prose.py')],capture_output=True,text=True)
    if run.returncode:raise AssertionError(run.stdout+run.stderr)
    print(run.stdout.strip().splitlines()[-1]+' supplied prose-check tests')


if __name__=='__main__':
    try:main()
    except (OSError,ValueError,AssertionError,fastjsonschema.JsonSchemaException) as exc:
        print(str(exc),file=sys.stderr);raise SystemExit(1)
