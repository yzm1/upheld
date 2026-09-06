"""Exercise trust boundaries and recovery of the S02 prototype."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import survey


class SurveyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'source'
        self.root.mkdir()
        self.text = '# Bounds\n\nOnly positive values pass.\n<table>unsafe</table>\n'
        (self.root / 'guide.md').write_text(self.text)
        self.manifest = self.base / 'manifest.json'
        self.spec = {'repository': 'fixture', 'revision': 'fixture-v1', 'boundary': 'guide only',
                     'files': [{'path': 'guide.md', 'sha256': hashlib.sha256(self.text.encode()).hexdigest()}]}
        self.save_manifest()
        self.run = self.base / 'run'

    def save_manifest(self):
        self.manifest.write_text(json.dumps(self.spec))

    def prepare(self):
        self.packet = survey.prepare(self.root, self.manifest, self.run)
        return self.packet

    def reply(self):
        sid = self.packet['payload']['sources'][0]['id']
        return {'packet_id': self.packet['packet_id'], 'reviewer': 'test fixture',
                'assessments': [{'source_id': sid, 'note': 'Synthetic fixture inspected'}],
                'candidates': [{'claim': 'Positive values pass', 'subject': 'values', 'kind': 'behavior',
                                'qualifiers': 'Only positive values', 'rationale': 'Boundary needs checking',
                                'uncertainty': 'Not executed', 'next_question': 'What happens at zero?',
                                'faithfulness_review': 'Preserves positive condition',
                                'references': [{'source_id': sid, 'start_line': 3, 'end_line': 3,
                                                'quote': 'Only positive values pass.'}]}]}

    def submit(self, reply):
        p = self.base / 'reply.json'
        p.write_text(json.dumps(reply))
        return survey.record_attempt(self.run, self.packet, p, {'backend': 'test'})

    def test_inventory_marks_missing_hash_mismatch_and_excluded(self):
        self.spec['files'] += [{'path': 'missing.md', 'sha256': '0' * 64},
                               {'path': 'excluded.md', 'exclude_reason': 'Outside component'}]
        (self.root / 'guide.md').write_text('Changed')
        self.save_manifest()
        packet = self.prepare()
        self.assertEqual([x['status'] for x in packet['payload']['inventory']],
                         ['unavailable', 'unavailable', 'excluded'])
        self.assertEqual(packet['payload']['sources'], [])

    def test_source_escape_and_duplicate_rejected_before_output(self):
        for files in [[{'path': '../escape.md', 'sha256': 'x'}], self.spec['files'] * 2]:
            self.spec['files'] = files
            self.save_manifest()
            with self.assertRaises(ValueError):
                self.prepare()
            self.assertFalse(self.run.exists())

    def test_symlink_not_followed(self):
        target = self.base / 'outside.md'
        target.write_text('Private source')
        (self.root / 'guide.md').unlink()
        (self.root / 'guide.md').symlink_to(target)
        with self.assertRaises(ValueError):
            self.prepare()

    def test_repeatable_packet_and_existing_run_protected(self):
        first = self.prepare()
        second = survey.prepare(self.root, self.manifest, self.base / 'again')
        self.assertEqual(first, second)
        with self.assertRaises(FileExistsError):
            self.prepare()

    def test_fabricated_quote_bad_range_unknown_source_and_acceptance_rejected(self):
        self.prepare()
        changes = [lambda r: r['candidates'][0]['references'][0].update(quote='All values pass.'),
                   lambda r: r['candidates'][0]['references'][0].update(start_line=True),
                   lambda r: r['candidates'][0]['references'][0].update(source_id='invented'),
                   lambda r: r['candidates'][0].update(accepted=True),
                   lambda r: r.update(packet_id='other')]
        for change in changes:
            reply = self.reply()
            change(reply)
            result = self.submit(reply)
            self.assertEqual(result['status'], 'rejected')
        self.assertEqual(survey.render(self.run)['inspection_reported'], 0)

    def test_recovery_and_duplicate_grouping_keep_prior_submissions(self):
        self.prepare()
        self.submit({'bad': 'shape'})
        self.submit(self.reply())
        self.submit(self.reply())
        self.assertEqual(survey.render(self.run), {'candidates': 1, 'inspection_reported': 1,
                                                  'ready_sources': 1, 'attempts': 3})
        self.assertEqual(len(list((self.run / 'attempts').glob('*.json'))), 3)

    def test_report_escapes_source_and_generated_text(self):
        self.prepare()
        reply = self.reply()
        reply['candidates'][0]['claim'] = '<script>alert(1)</script>'
        self.submit(reply)
        report = (self.run / 'review.html').read_text()
        self.assertNotIn('<script>', report)
        self.assertNotIn('<table>unsafe', report)
        self.assertIn('&lt;script&gt;', report)

    def test_zero_candidates_requires_inspection_note(self):
        self.prepare()
        reply = self.reply()
        reply['candidates'] = []
        reply['assessments'][0]['note'] = ''
        self.assertEqual(self.submit(reply)['status'], 'rejected')
        reply['assessments'][0]['note'] = 'No consequential claim found by this reviewer'
        self.assertEqual(self.submit(reply)['status'], 'valid_candidate_submission')

    def test_packet_tampering_blocks_resume(self):
        packet = self.prepare()
        packet['payload']['sources'][0]['text'] = 'Replaced source'
        (self.run / 'packet.json').write_text(json.dumps(packet))
        with self.assertRaisesRegex(ValueError, 'Packet content changed'):
            survey.render(self.run)

    def test_compare_exposes_changed_source_without_rewriting_old_run(self):
        self.prepare()
        self.submit(self.reply())
        (self.root / 'guide.md').write_text('Changed scope\n')
        self.spec['files'][0]['sha256'] = hashlib.sha256(b'Changed scope\n').hexdigest()
        self.save_manifest()
        second = self.base / 'second'
        survey.prepare(self.root, self.manifest, second)
        change = survey.compare(self.run, second)
        self.assertFalse(change['same_packet'])
        self.assertEqual(change['source_changes'], ['guide.md'])
        self.assertEqual(len(change['removed_candidate_ids']), 1)
        self.assertEqual(survey.render(self.run)['candidates'], 1)

    def test_oversized_source_is_visible_and_not_truncated(self):
        (self.root / 'guide.md').write_bytes(b'x' * (survey.MAX_SOURCE + 1))
        packet = self.prepare()
        self.assertEqual(packet['payload']['sources'], [])
        self.assertIn('exceeds', packet['payload']['inventory'][0]['reason'])

    def test_committed_example_remains_replayable_after_collector_changes(self):
        example = Path(__file__).resolve().parents[1] / 'examples/survey-heldtospec'
        packet = survey.prepare(example / 'sources', example / 'manifest.json', self.base / 'example')
        recorded = survey.load_packet(example / 'run')
        self.assertEqual(packet['packet_id'], recorded['packet_id'])
        survey.validate_reply(survey.read_json(example / 'response.json'), packet)

    def test_missing_cli_preserves_queue_and_records_failure(self):
        self.prepare()
        config = self.base / 'codex.json'
        config.write_text(json.dumps({'executable': str(self.base / 'absent'), 'model': 'fixture', 'timeout_seconds': 1}))
        result = survey.run_codex(self.run, config)
        self.assertEqual(result['status'], 'rejected')
        self.assertEqual(survey.render(self.run)['inspection_reported'], 0)

    def test_subprocess_adapter_uses_stdin_and_recovers_from_timeout(self):
        self.prepare()
        executable = self.base / 'fake-codex'
        executable.write_text('''#!/usr/bin/env python3
import json, sys, time
from pathlib import Path
if '--version' in sys.argv:
    print('test-double 1'); sys.exit(0)
p=json.load(sys.stdin)
if '--sandbox' not in sys.argv or sys.argv[sys.argv.index('--sandbox')+1]!='read-only': sys.exit(4)
reply={'packet_id':p['packet_id'], 'reviewer':'CLI test double', 'assessments':[], 'candidates':[]}
Path(sys.argv[sys.argv.index('-o')+1]).write_text(json.dumps(reply))
''')
        executable.chmod(0o700)
        config = self.base / 'codex.json'
        settings = {'executable': str(executable), 'model': 'fixture', 'timeout_seconds': 2}
        config.write_text(json.dumps(settings))
        result = survey.run_codex(self.run, config)
        self.assertEqual(result['status'], 'valid_candidate_submission')
        self.assertEqual(result['provenance']['version'], 'test-double 1')
        executable.write_text(executable.read_text().replace('p=json.load(sys.stdin)', 'time.sleep(5)\np=json.load(sys.stdin)'))
        settings['timeout_seconds'] = 0.1
        config.write_text(json.dumps(settings))
        result = survey.run_codex(self.run, config)
        self.assertEqual(result['status'], 'rejected')
        self.assertIn('timed out', result['error'])
        self.assertEqual(survey.render(self.run)['attempts'], 2)


if __name__ == '__main__':
    unittest.main()
