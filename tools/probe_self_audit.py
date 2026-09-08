"""Run a bounded fault challenge of Upheld's package checker; creates no bindings."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.output.exists():
        parser.error('Output already exists; observations are append-only')
    script = root / 'tools/package_upheld_skill.py'
    spec = importlib.util.spec_from_file_location('audit_package', script)
    package = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(package)
    # Expectations come from the published file contract and METHOD V2/V5.
    expected = {'clean': 0, 'altered_file': 1, 'empty_manifest': 1, 'cannot_inspect': 2,
                'wrong_source_commit': 'ValueError', 'missing_source_commit': 'OSError'}
    started = datetime.now(timezone.utc).isoformat()
    rows = []
    with tempfile.TemporaryDirectory(prefix='upheld-self-audit-') as temp:
        temp = Path(temp)
        for name in ('clean', 'altered_file', 'empty_manifest', 'cannot_inspect'):
            out = temp / name / 'upheld'
            if name in ('clean', 'altered_file'):
                package.build('codex', out, root)
                if name == 'altered_file':
                    with (out / 'SKILL.md').open('a') as stream:
                        stream.write('\nseeded unexpected edit\n')
            elif name == 'empty_manifest':
                out.mkdir(parents=True)
                (out / 'manifest.json').write_text('{"files": {}}')
            run = subprocess.run([sys.executable, str(script), '--verify', str(out)], capture_output=True, text=True)
            rows.append({'case': name, 'expected_exit': expected[name], 'actual_exit': run.returncode,
                         'stdout': run.stdout, 'stderr': run.stderr,
                         'matches_expectation': run.returncode == expected[name]})
        fixture = temp / 'source'
        shutil.copytree(root / 'skills', fixture / 'skills')
        (fixture / 'docs').mkdir()
        for name in ('METHOD.md', 'rule-review.json'):
            shutil.copyfile(root / 'docs' / name, fixture / 'docs' / name)
        method = fixture / 'docs/METHOD.md'
        current = method.read_bytes()
        method.write_bytes(current + b'\nOlder source revision for the fault challenge.\n')
        def git(*argv):
            return subprocess.check_output(['git', '-C', str(fixture), *argv], stderr=subprocess.DEVNULL).decode().strip()
        git('init', '-q')
        git('add', 'docs/METHOD.md')
        git('-c', 'user.name=Upheld probe', '-c', 'user.email=probe@example.invalid', 'commit', '-qm', 'Seed older method')
        wrong_rev = git('rev-parse', 'HEAD')
        method.write_bytes(current)
        original_rev = package.SOURCE_REV
        for name, revision in [('wrong_source_commit', wrong_rev), ('missing_source_commit', '0' * 40)]:
            package.SOURCE_REV = revision
            try:
                package.method_reference(fixture)
                actual = 'returned'
            except OSError:
                actual = 'OSError'
            except ValueError:
                actual = 'ValueError'
            rows.append({'case': name, 'source_revision': revision, 'expected': expected[name], 'actual': actual,
                         'matches_expectation': actual == expected[name]})
        package.SOURCE_REV = original_rev
    git = lambda *argv: subprocess.check_output(['git', '-C', str(root), *argv]).decode().strip()
    record = {'kind': 'development_fault_challenge', 'repository': 'yzm1/upheld',
              'started_at': started, 'finished_at': datetime.now(timezone.utc).isoformat(),
              'source_commit': git('rev-parse', 'HEAD'), 'working_tree': git('status', '--porcelain'),
              'python': platform.python_version(), 'platform': platform.platform(),
              'invocation': [sys.executable, str(Path(__file__).resolve()), '--root', str(root),
                             '--output', str(args.output.absolute())],
              'runner': {'path': str(Path(__file__).resolve()),
                         'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'source_sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in [script, root / 'docs/METHOD.md', root / 'skills/upheld/SKILL.md']},
              'expected_results_declared_before_execution': expected,
              'cases': rows, 'accepted_bindings_created': 0,
              'limits': ['Single local development observation; not an independent agent trial.',
                         'No product basis, oracle producer, or accepted evidence record.',
                         'Operating-system denial, concurrent edits, and live client behavior not exercised.']}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(record, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'cases': len(rows), 'matched': sum(r['matches_expectation'] for r in rows)}))


if __name__ == '__main__':
    main()
