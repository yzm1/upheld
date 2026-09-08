"""Challenge the bounded demo; these tests grant no human acceptance."""
from contextlib import contextmanager
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import probe_evidence_lifecycle as lifecycle


class EvidenceLifecycleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = lifecycle.run_demo(ROOT)

    @contextmanager
    def fixture(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name in (lifecycle.SUBJECT, lifecycle.CHECKER, lifecycle.RUNNER, *lifecycle.INPUTS):
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, root / name)
            self.assertEqual(lifecycle.inspect(root, self.record['register'], self.record['evidence'],
                                              self.record['simulated_binding'])['state'], 'still_valid')
            yield root

    def test_real_checker_and_weakened_checker_discriminate_the_seeded_fault(self):
        record = self.record['evidence']
        lifecycle.validate('evidence', record)
        runs = record['metadata']['observed_runs']
        self.assertEqual(runs['clean']['exit_code'], 0)
        self.assertEqual(runs['count_fault']['exit_code'], 1)
        self.assertEqual(runs['weakened_checker']['exit_code'], 0)
        self.assertEqual(runs['missing_input']['exit_code'], 2)
        self.assertEqual(record['evidence_id'], lifecycle.evidence_id(record))
        self.assertEqual(self.record['accepted_human_bindings_created'], 0)

    def test_changed_grounds_and_regeneration_preserve_review_required(self):
        rows = {r['case']: r for r in self.record['scenarios']}
        self.assertTrue(all(row['matched'] for row in rows.values()))
        for case, ground in (('subject_changed', 'subject_scope'),
                            ('promise_changed', 'promise'),
                            ('defense_weakened', 'artifacts:' + lifecycle.CHECKER)):
            self.assertEqual(rows[case]['actual']['state'], 'review_required')
            self.assertIn(ground, rows[case]['actual']['changed_grounds'])
        self.assertEqual(rows['regenerated_view_keeps_review']['actual'], rows['subject_changed']['actual'])
        self.assertEqual(rows['candidate_without_acceptance']['actual']['state'], 'open')
        self.assertEqual(rows['artifact_relocated']['actual']['state'], 'invalid')
        self.assertEqual(rows['input_unavailable']['actual']['state'], 'unresolvable')

    def test_simulated_acceptance_rejects_wrong_scope_profile_and_verdict(self):
        for key, value in (('defense_id', 'unrelated:d0'), ('verdict', 'could_not_establish'),
                           ('verdict', 'contradicts'), ('oracle', 'unrelated'),
                           ('validated_subject_scope', 'other.py')):
            with self.subTest(key=key, value=value):
                record = copy.deepcopy(self.record['evidence'])
                record[key] = value
                record['evidence_id'] = lifecycle.evidence_id(record)
                with self.fixture() as root, self.assertRaises(ValueError):
                    lifecycle.simulate_accept(root, self.record['register'], record)
        record = copy.deepcopy(self.record['evidence'])
        record['basis']['hashing_profile'] = 'unsupported'
        record['evidence_id'] = lifecycle.evidence_id(record)
        with self.fixture() as root, self.assertRaises(ValueError):
            lifecycle.simulate_accept(root, self.record['register'], record)

    def test_added_files_and_stale_bindings_cannot_be_accepted(self):
        with self.fixture() as root:
            (root / 'pyproject.toml').write_text('# New package declaration\n')
            with self.assertRaises(ValueError):
                lifecycle.simulate_accept(root, self.record['register'], self.record['evidence'])
            result = lifecycle.inspect(root, self.record['register'], self.record['evidence'],
                                       self.record['simulated_binding'])
            self.assertIn('environment:demo-tree-paths', result['changed_grounds'])
        with self.fixture() as root:
            binding = copy.deepcopy(self.record['simulated_binding'])
            binding['bindings'] = {'unrelated:d0': self.record['evidence']['evidence_id']}
            result = lifecycle.inspect(root, self.record['register'], self.record['evidence'], binding)
            self.assertEqual(result['state'], 'invalid')

    def test_changed_record_cannot_reuse_its_old_identity(self):
        record = copy.deepcopy(self.record['evidence'])
        record['metadata']['observed_runs']['count_fault']['exit_code'] = 0
        result = lifecycle.inspect(ROOT, self.record['register'], record, self.record['simulated_binding'])
        self.assertEqual(result['state'], 'invalid')
        self.assertIn('Evidence bytes changed', result['error'])

    def test_cli_refuses_to_replace_a_record_or_follow_an_output_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'record.json'
            path.write_text('Keep prior observation')
            for target in (path, Path(d) / 'link.json'):
                if target != path:
                    target.symlink_to(path)
                run = subprocess.run([sys.executable, str(ROOT / lifecycle.RUNNER), '--output', str(target)],
                                     capture_output=True, timeout=10)
                self.assertNotEqual(run.returncode, 0)
                self.assertEqual(path.read_text(), 'Keep prior observation')

    def test_snapshot_rejects_symlinks_and_unsupported_scope(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'README.md').symlink_to(ROOT / 'README.md')
            with self.assertRaises(ValueError):
                lifecycle.basis(root, self.record['register'])
        changed = copy.deepcopy(self.record['register'])
        changed['promises'][0]['subject_scope'] = 'other.md'
        with self.assertRaisesRegex(ValueError, 'Unsupported'):
            lifecycle.basis(ROOT, changed)

    def test_recorded_report_cannot_claim_human_acceptance_or_hide_a_failed_case(self):
        lifecycle.check_recorded_demo(self.record)
        for mutation in (lambda r: r.update(accepted_human_bindings_created=1),
                         lambda r: r['simulated_binding'].update(note='A person accepted this'),
                         lambda r: r['scenarios'][0]['actual'].update(state='invalid'),
                         lambda r: r['evidence']['metadata']['observed_runs']['count_fault'].update(exit_code=0)):
            record = copy.deepcopy(self.record)
            mutation(record)
            with self.assertRaises(ValueError):
                lifecycle.check_recorded_demo(record)
