"""Regression probes from the 6 September 2026 documentation review."""
import copy
import fastjsonschema
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from documentation_integrity import check_todo, check_rules, check_fixtures
from check_readme_status import check
from prepare_probe_review import convert
from test_docs import validator


class RedTeamChecks(unittest.TestCase):
    def test_reopened_and_new_tasks_are_allowed(self):
        text = (ROOT / 'TODO.md').read_text()
        check_todo(text.replace('| D06 | Complete |', '| D06 | Reopened |'))
        check_todo(text + '\n| D09 | Open | New work | Pending |\n')

    def test_duplicate_status_and_missing_closure_fail(self):
        for text in ('| D01 | Open | Work | |\n| D01 | Open | Work | |',
                     '| D01 | Fiction | Work | |', '| D01 | Complete | Work | |'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                check_todo(text)

    def test_every_status_count_is_guarded(self):
        text = (ROOT / 'README.md').read_text()
        labels = ['Promises', 'Candidate defenses', 'Promises awaiting a defense or gap decision',
                  'Accepted gaps', 'Bound evidence records', 'Library tests reported passing']
        import re
        for label in labels:
            changed, n = re.subn(r'(\| ' + re.escape(label) + r' \| )\d+( \|)', r'\g<1>999\2', text)
            self.assertEqual(n, 1)
            self.assertTrue(any(x['subject'] == label for x in check(readme=changed)), label)

    def test_converter_rejects_unsupported_and_malformed_sources(self):
        src = json.loads((ROOT / 'examples/heldtospec-contracts/obligations.register.json').read_text())
        bad = copy.deepcopy(src); bad['schema_version'] = '99-unsupported'
        with self.assertRaises(ValueError): convert(bad, 'synthetic/source.json')
        bad = copy.deepcopy(src); del bad['promises']
        with self.assertRaises(fastjsonschema.JsonSchemaException): convert(bad, 'synthetic/source.json')
        converted = convert(src, 'other/source.json')
        self.assertEqual(converted['producer']['inputs'][0], 'other/source.json')

    def test_cli_rejects_before_creating_output(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / 'source.json'; out = Path(d) / 'review.json'
            src.write_text('{"schema_version":"99-unsupported"}')
            run = subprocess.run([sys.executable, str(ROOT / 'tools/prepare_probe_review.py'), str(src), str(out)], capture_output=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertFalse(out.exists())

    def test_rule_changes_require_review(self):
        for old, new in (('| T2 | MUST |', '| T2 | SHOULD |'),
                         ('Regeneration never advances it.', 'Regeneration always advances it.')):
            with tempfile.TemporaryDirectory() as d:
                root = Path(d); shutil.copytree(ROOT / 'docs', root / 'docs')
                path = root / 'docs/CHECKER.md'
                self.assertIn(old, path.read_text())
                path.write_text(path.read_text().replace(old, new))
                with self.assertRaises(ValueError): check_rules(root)

    def test_missing_evidence_and_dangling_bindings_fail(self):
        for mode in ('missing', 'binding'):
            with tempfile.TemporaryDirectory() as d:
                root = Path(d); shutil.copytree(ROOT / 'examples', root / 'examples')
                folder = root / 'examples/upheld-status'
                if mode == 'missing': (folder / 'obligations.evidence.jsonl').unlink()
                else:
                    path = folder / 'obligations.bindings.json'
                    doc = json.loads(path.read_text()); doc['bindings'] = {'UPH-001:d0': 'nonexistent-record'}
                    path.write_text(json.dumps(doc))
                with self.assertRaises(ValueError): check_fixtures(root)

    def test_future_evidence_is_not_globally_forbidden(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); shutil.copytree(ROOT / 'examples', root / 'examples')
            future = root / 'examples/future'; future.mkdir()
            (future / 'obligations.evidence.jsonl').write_text('synthetic placeholder\n')
            check_fixtures(root)

    def test_timestamp_format(self):
        doc = json.loads((ROOT / 'examples/upheld-status/obligations.register.json').read_text())
        defense = doc['promises'][0]['defenses'][0]
        for value in (None, '2026-09-06T12:00:00Z'):
            defense['last_actually_ran'] = value; validator('register')(doc)
        defense['last_actually_ran'] = 'not-a-timestamp'
        with self.assertRaises(fastjsonschema.JsonSchemaException): validator('register')(doc)

    def test_unresolvable_never_has_clean_exit(self):
        doc = {'schema_version':'0.1','command':'verify','exit_code':0,'findings':[], 'diagnostics':[],
               'counts':{k:0 for k in ['promises','open_defenses','gaps','still_valid','review_required','invalid','unresolvable']}}
        finding = {'subject':'defense:test:d0', 'facet':'unresolvable', 'consequence':'unresolvable',
                   'acknowledgement':'acknowledged', 'message':'Synthetic unreadable target', 'fingerprint':'test'}
        for mode in ('finding', 'count'):
            bad = copy.deepcopy(doc)
            if mode == 'finding': bad['findings'] = [finding]
            else: bad['counts']['unresolvable'] = 1
            with self.assertRaises(fastjsonschema.JsonSchemaException): validator('verify-output')(bad)
            bad['exit_code'] = 5; validator('verify-output')(bad)

    def test_optimized_gate_still_rejects_false_count(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d) / 'repo'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            path = root / 'README.md'
            path.write_text(path.read_text().replace('| Promises | 44 |', '| Promises | 45 |'))
            run = subprocess.run([sys.executable, '-O', str(root / 'tools/check_docs.py')], capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('README status check failed', run.stderr)


if __name__ == '__main__': unittest.main()
