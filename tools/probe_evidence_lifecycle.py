"""Exercise one development evidence lifecycle; all acceptance is simulated."""
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

import fastjsonschema

ROOT = Path(__file__).resolve().parents[1]
PROFILE = 'development/readme-byte-snapshot/v1'
CHECKER = 'tools/check_readme_status.py'
RUNNER = 'tools/probe_evidence_lifecycle.py'
SUBJECT = 'README.md'
INPUTS = tuple('examples/heldtospec-contracts/' + name for name in (
    'obligations.register.json', 'obligations.bindings.json', 'observations.json'))


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def digest(data):
    return 'sha256:' + hashlib.sha256(data).hexdigest()


def validate(name, value):
    schema = json.loads((ROOT / f'schemas/0.1/{name}.schema.json').read_text())
    fastjsonschema.compile(schema)(value)


def file_hash(root, name):
    path = root / name
    if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != root.parent):
        raise ValueError('Snapshot paths cannot contain symlinks')
    return digest(path.read_bytes())


def basis(root, register):
    """A closed fixture profile, not Upheld's deferred product hash profile."""
    validate('register', register)
    if len(register['promises']) != 1:
        raise ValueError('Demo requires exactly one promise')
    promise = copy.deepcopy(register['promises'][0])
    defenses = promise.pop('defenses')
    if len(defenses) != 1:
        raise ValueError('Demo requires exactly one defense')
    defense = defenses[0]
    if (defense['guarded_by'] != 'checker' or promise['subject_scope'] != SUBJECT
            or defense['subject_scope'] != SUBJECT
            or defense['artifact_locator'] != CHECKER + '::check'):
        raise ValueError('Unsupported demo mechanism or scope')
    paths = []
    for path in root.rglob('*'):
        if path.is_symlink():
            raise ValueError('Snapshot cannot contain symlinks')
        paths.append(path.relative_to(root).as_posix() + ('/' if path.is_dir() else ''))
    return {'hashing_profile': PROFILE, 'promise': digest(encoded(promise)),
            'defense_assertion': digest(encoded(defense)),
            'artifacts': {name: file_hash(root, name) for name in (CHECKER, RUNNER)},
            'subject_scope': {'scope': SUBJECT, 'hash': file_hash(root, SUBJECT)},
            'environment': {**{name: file_hash(root, name) for name in INPUTS},
                            'demo-tree-paths': digest(encoded(sorted(paths)))}}


def evidence_id(record):
    payload = {k: v for k, v in record.items() if k != 'evidence_id'}
    return 'development:' + digest(encoded(payload))


def inspect(root, register, record, bindings):
    """Read-only, deliberately bounded comparison used by the demo scenarios."""
    try:
        validate('register', register)
        validate('bindings', bindings)
        if record is None:
            return {'state': 'unresolvable', 'changed_grounds': ['evidence_missing']}
        validate('evidence', record)
        defense = register['promises'][0]['defenses'][0]
        if record['evidence_id'] != evidence_id(record):
            raise ValueError('Evidence bytes changed')
        if (record['defense_id'] != defense['id'] or record['oracle'] != 'seeded_violation'
                or record['verdict'] != 'supports' or record['oracle_result'] != 'fired'
                or record['validated_subject_scope'] != SUBJECT
                or record['basis']['hashing_profile'] != PROFILE
                or record['execution']['status'] != 'recorded'):
            raise ValueError('Incompatible evidence')
        if not bindings['bindings']:
            return {'state': 'open', 'changed_grounds': []}
        if bindings['bindings'] != {defense['id']: record['evidence_id']}:
            raise ValueError('Binding does not select this defense and evidence')
        for name in (CHECKER, RUNNER):
            if not (root / name).exists():
                return {'state': 'invalid', 'changed_grounds': ['artifact_missing:' + name]}
        current = basis(root, register)
        changed = []
        for key in ('promise', 'defense_assertion', 'subject_scope'):
            if record['basis'][key] != current[key]:
                changed.append(key)
        for key in ('artifacts', 'environment'):
            old, new = record['basis'][key], current[key]
            changed.extend(key + ':' + name for name in sorted(old.keys() | new.keys())
                           if old.get(name) != new.get(name))
        return {'state': 'review_required' if changed else 'still_valid', 'changed_grounds': changed}
    except OSError as exc:
        return {'state': 'unresolvable', 'changed_grounds': ['input_unavailable'], 'error': str(exc)}
    except (ValueError, KeyError, TypeError, IndexError, fastjsonschema.JsonSchemaException) as exc:
        return {'state': 'invalid', 'changed_grounds': ['invalid_input'], 'error': str(exc)}


def simulate_accept(root, register, record):
    """Create only a labeled test decision; never claim a person accepted evidence."""
    bindings = {'schema_version': '0.1',
                'bindings': {record['defense_id']: record['evidence_id']},
                'note': 'SIMULATED acceptance for a development probe; no human acceptance.'}
    if inspect(root, register, record, bindings)['state'] != 'still_valid':
        raise ValueError('Cannot simulate accepting incompatible or stale evidence')
    return bindings


def execute(root):
    start = time.monotonic()
    command = [sys.executable, str(root / CHECKER)]
    run = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=10)
    return {'command': command, 'exit_code': run.returncode, 'stdout': run.stdout,
            'stderr': run.stderr, 'duration_seconds': time.monotonic() - start}


def run_demo(source=ROOT):
    source = Path(source).resolve()
    register = json.loads((source / 'examples/upheld-status/obligations.register.json').read_text())
    # Copy an existing promise and checker; seeded faults are explicit test data.
    started = datetime.now(timezone.utc).isoformat()
    begin = time.monotonic()
    source_rev = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
    rows, runs = [], {}
    with tempfile.TemporaryDirectory(prefix='upheld-lifecycle-') as directory:
        root = Path(directory)
        for name in (SUBJECT, CHECKER, *INPUTS):
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, root / name)
        shutil.copyfile(Path(__file__), root / RUNNER)
        original = {name: (root / name).read_bytes() for name in (SUBJECT, CHECKER, RUNNER, *INPUTS)}
        captured = basis(root, register)
        expected = {'clean': 0, 'count_fault': 1, 'historical_claim': 1,
                    'missing_input': 2, 'weakened_checker': 0}
        runs['clean'] = execute(root)
        text = original[SUBJECT].decode()
        if text.count('| Promises | 44 |') != 1:
            raise ValueError('The declared count-fault target changed; review this probe')
        (root / SUBJECT).write_text(text.replace('| Promises | 44 |', '| Promises | 45 |'))
        runs['count_fault'] = execute(root)
        broken = (root / CHECKER).read_text()
        if broken.count('    return findings') != 1:
            raise ValueError('The declared checker mutation target changed; review this probe')
        (root / CHECKER).write_text(broken.replace('    return findings', '    return []'))
        runs['weakened_checker'] = execute(root)
        (root / CHECKER).write_bytes(original[CHECKER])
        (root / SUBJECT).write_text(text + '\nNothing has been measured from a real register.\n')
        runs['historical_claim'] = execute(root)
        (root / SUBJECT).write_bytes(original[SUBJECT])
        (root / INPUTS[0]).unlink()
        runs['missing_input'] = execute(root)
        (root / INPUTS[0]).write_bytes(original[INPUTS[0]])
        outputs = {name: json.loads(run['stdout']) for name, run in runs.items()}
        matched = all(runs[name]['exit_code'] == code for name, code in expected.items())
        matched &= any(x['code'] == 'status_count_mismatch' for x in outputs['count_fault'].get('findings', []))
        matched &= any(x['code'] == 'obsolete_status_claim' for x in outputs['historical_claim'].get('findings', []))
        matched &= outputs['missing_input'].get('result') == 'could_not_look'
        if not matched or basis(root, register) != captured:
            raise ValueError('Fault challenge failed or did not restore its input snapshot')
        record = {'schema_version': '0.1', 'evidence_id': 'pending',
                  'defense_id': register['promises'][0]['defenses'][0]['id'],
                  'oracle': 'seeded_violation', 'oracle_result': 'fired', 'verdict': 'supports',
                  'validated_subject_scope': SUBJECT, 'basis': captured,
                  'source_rev': source_rev, 'producer': 'development-readme-lifecycle',
                  'supersedes': None, 'execution': {'status': 'recorded',
                      'command': [sys.executable, *sys.argv],
                      'started_at': started, 'duration_seconds': time.monotonic() - begin,
                      'toolchain': {'python': platform.python_version(), 'platform': platform.platform()},
                      'target': 'Disposable snapshot of Upheld README status checks',
                      'configuration': {'profile': PROFILE},
                      'dirty_tree': {'state': 'dirty', 'snapshot': digest(encoded(captured))},
                      'omissions': ['Arbitrary prose, concurrency, other platforms, and external state were not assessed.']},
                  'metadata': {'development_only': True, 'expected_exits': expected, 'observed_runs': runs,
                               'source_identity': 'source_rev names checkout HEAD; basis hashes the copied working files.'}}
        record['evidence_id'] = evidence_id(record)
        validate('evidence', record)
        no_binding = {'schema_version': '0.1', 'bindings': {}}
        rows.append({'case': 'candidate_without_acceptance', 'expected': 'open',
                     'actual': inspect(root, register, record, no_binding)})
        binding = simulate_accept(root, register, record)
        protected = encoded({'register': register, 'evidence': record, 'bindings': binding})
        def observe(case, expected_state, changed_register=register, changed_record=record):
            rows.append({'case': case, 'expected': expected_state,
                         'actual': inspect(root, changed_register, changed_record, binding)})
        observe('accepted_fixture_unchanged', 'still_valid')
        (root / SUBJECT).write_bytes(original[SUBJECT] + b'\n')
        observe('subject_changed', 'review_required')
        # Recomputing a disposable view cannot update the record or the binding.
        first = encoded(basis(root, register))
        if first != encoded(basis(root, register)):
            raise ValueError('Snapshot regeneration is not deterministic')
        observe('regenerated_view_keeps_review', 'review_required')
        (root / SUBJECT).write_bytes(original[SUBJECT])
        (root / CHECKER).write_text(broken.replace('    return findings', '    return []'))
        observe('defense_weakened', 'review_required')
        (root / CHECKER).write_bytes(original[CHECKER])
        (root / INPUTS[2]).write_bytes(original[INPUTS[2]] + b'\n')
        observe('declared_input_changed', 'review_required')
        (root / INPUTS[2]).write_bytes(original[INPUTS[2]])
        revised = copy.deepcopy(register)
        revised['promises'][0]['text'] += ' An additional condition.'
        observe('promise_changed', 'review_required', changed_register=revised)
        (root / CHECKER).rename(root / 'tools/relocated.py')
        observe('artifact_relocated', 'invalid')
        (root / 'tools/relocated.py').rename(root / CHECKER)
        (root / INPUTS[0]).unlink()
        observe('input_unavailable', 'unresolvable')
        (root / INPUTS[0]).write_bytes(original[INPUTS[0]])
        observe('evidence_missing', 'unresolvable', changed_record=None)
        altered = copy.deepcopy(record)
        altered['verdict'] = 'contradicts'
        observe('evidence_bytes_changed', 'invalid', changed_record=altered)
        if protected != encoded({'register': register, 'evidence': record, 'bindings': binding}):
            raise ValueError('Inspection or regeneration edited a protected record')
    for row in rows:
        row['matched'] = row['expected'] == row['actual']['state']
    if not all(row['matched'] for row in rows):
        raise ValueError('Lifecycle result differs from its declared expectation')
    return {'kind': 'development_evidence_lifecycle', 'started_at': started,
            'finished_at': datetime.now(timezone.utc).isoformat(), 'register': register,
            'evidence': record, 'simulated_binding': binding, 'scenarios': rows,
            'accepted_human_bindings_created': 0,
            'limits': ['This is a closed fixture demonstration, not a product checker or hashing profile.',
                       'Acceptance is simulated and does not change any project bindings.',
                       'Lineage, arbitrary scopes, multi-component graphs, cycles, and review cost remain untested.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        parser.error('Use a new output path; prior observations cannot be replaced')
    result = run_demo(args.root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'scenarios': len(result['scenarios']), 'matched': sum(r['matched'] for r in result['scenarios']),
                      'accepted_human_bindings_created': 0}))


if __name__ == '__main__':
    main()
