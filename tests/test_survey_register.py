"""Challenge the canonical output's source, scope, and preservation boundaries."""
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import survey
import survey_register


class RegisterExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'source'
        self.root.mkdir()
        source = b'Only positive values pass.\nZero needs a decision.\n'
        (self.root / 'guide.md').write_bytes(source)
        manifest = {'repository': 'fixture/repo', 'revision': 'declared-only',
                    'boundary': 'guide only', 'files': [
                        {'path': 'guide.md', 'sha256': survey.digest(source)},
                        {'path': 'missing.md', 'sha256': '0' * 64},
                        {'path': 'excluded.md', 'exclude_reason': 'Outside survey'}]}
        spec = self.base / 'manifest.json'
        survey.write_new(spec, manifest)
        self.run = self.base / 'run'
        self.packet = survey.prepare(self.root, spec, self.run)
        self.sid = self.packet['payload']['sources'][0]['id']
        self.output = self.base / 'obligations.register.json'

    def reply(self):
        return {'packet_id': self.packet['packet_id'], 'reviewer': 'fixture reviewer',
                'assessments': [{'source_id': self.sid, 'note': 'Read first line only',
                                 'coverage': 'partial', 'uninspected': 'Second line remains unread'}],
                'candidates': [{'claim': 'Positive values pass.', 'subject': 'numeric input',
                                'kind': 'behavior', 'qualifiers': 'Only positive values.',
                                'rationale': 'Inputs outside the allowed range could pass.',
                                'uncertainty': 'No code inspection or execution',
                                'next_question': 'What rejects zero?',
                                'faithfulness_review': 'The only qualifier must remain visible.',
                                'references': [{'source_id': self.sid, 'start_line': 1,
                                                'end_line': 1, 'quote': 'Only positive values pass.'}]}]}

    def submit(self, reply):
        path = self.base / 'reply.json'
        path.write_text(json.dumps(reply))
        return survey.record_attempt(self.run, self.packet, path, {'backend': 'test'})

    def test_cli_exports_real_schema_with_qualifiers_and_unknown_defenses(self):
        self.submit(self.reply())
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = survey.main(['register', '--run', str(self.run), '--out', str(self.output)])
        self.assertEqual(result, 0)
        self.assertEqual(json.loads(stdout.getvalue())['promises'], 1)
        register = json.loads(self.output.read_text())
        survey_register.validate_register(register)
        promise = register['promises'][0]
        self.assertIn('Only positive values.', promise['text'])
        self.assertEqual(promise['confidence'], 'suspected')
        self.assertEqual(promise['reachability'], 'unknown')
        self.assertEqual(promise['defenses'], [])
        self.assertNotIn('gap', promise)
        self.assertNotIn('bindings', register)
        self.assertIn('Unknown', promise['the_test_that_would_catch_it'])
        trace = promise['metadata']['survey']
        self.assertEqual(trace['references'][0]['quote'], 'Only positive values pass.')
        self.assertEqual(trace['candidate']['uncertainty'], self.reply()['candidates'][0]['uncertainty'])
        self.assertEqual(register['producer']['source_rev'], 'declared-only')

    def test_partial_unavailable_and_excluded_sources_survive_export(self):
        self.submit(self.reply())
        result = survey_register.build_register(self.run)['metadata']['survey']
        self.assertEqual(result['coverage'], 'not_established')
        self.assertEqual([x['status'] for x in result['inventory']], ['ready', 'unavailable', 'excluded'])
        note = result['submissions'][0]['assessments'][0]
        self.assertEqual(note['coverage'], 'partial')
        self.assertEqual(note['uninspected'], 'Second line remains unread')

    def test_ambiguity_stays_a_question_and_inference_stays_suspected(self):
        reply = self.reply()
        question = copy.deepcopy(reply['candidates'][0])
        question.update(kind='ambiguity', claim='Is zero allowed?')
        reply['candidates'][0]['kind'] = 'inferred'
        reply['candidates'].append(question)
        self.submit(reply)
        result = survey_register.build_register(self.run)
        self.assertEqual(len(result['promises']), 1)
        self.assertEqual(result['promises'][0]['confidence'], 'suspected')
        questions = result['metadata']['survey']['questions']
        self.assertEqual(questions[0]['candidate'], question)
        self.assertEqual(result['metadata']['survey']['counts'],
                         {'candidates': 2, 'promises': 1, 'questions': 1, 'defenses': 0})

    def test_no_submission_fails_but_reviewed_zero_candidates_remains_explicit(self):
        with self.assertRaisesRegex(ValueError, 'valid submission'):
            survey_register.export_register(self.run, self.output)
        self.assertFalse(self.output.exists())
        reply = self.reply()
        reply['candidates'] = []
        self.submit(reply)
        result = survey_register.build_register(self.run)
        self.assertEqual(result['promises'], [])
        self.assertEqual(result['metadata']['survey']['coverage'], 'not_established')
        self.assertEqual(len(result['metadata']['survey']['submissions']), 1)

    def test_exact_duplicates_keep_all_reviewers_and_conflicts_stay_separate(self):
        first = self.reply()
        self.submit(first)
        self.submit(first)
        second = copy.deepcopy(first)
        second['reviewer'] = 'second reviewer'
        self.submit(second)
        result = survey_register.build_register(self.run)
        self.assertEqual(len(result['promises']), 1)
        self.assertEqual(len(result['promises'][0]['metadata']['survey']['submission_ids']), 2)
        second['candidates'][0]['claim'] = 'Zero also passes.'
        self.submit(second)
        result = survey_register.build_register(self.run)
        self.assertEqual(len(result['promises']), 2)
        self.assertTrue(all(p['confidence'] == 'suspected' for p in result['promises']))

    def test_rerun_is_repeatable_and_existing_decisions_are_untouched(self):
        self.submit(self.reply())
        survey_register.export_register(self.run, self.output)
        first = self.output.read_bytes()
        another = self.base / 'another.json'
        survey_register.export_register(self.run, another)
        self.assertEqual(first, another.read_bytes())
        self.output.write_text('Human-edited register; keep this exact text.')
        bindings = self.base / 'obligations.bindings.json'
        bindings.write_text('Accepted binding sentinel')
        with self.assertRaises(FileExistsError):
            survey_register.export_register(self.run, self.output)
        self.assertEqual(self.output.read_text(), 'Human-edited register; keep this exact text.')
        self.assertEqual(bindings.read_text(), 'Accepted binding sentinel')
        self.assertEqual(list(self.base.glob('.survey-register-*')), [])

    def test_output_inside_run_or_dangling_symlink_is_rejected(self):
        self.submit(self.reply())
        with self.assertRaisesRegex(ValueError, 'outside the input run'):
            survey_register.export_register(self.run, self.run / 'new.json')
        target = self.base / 'absent.json'
        self.output.symlink_to(target)
        with self.assertRaises(FileExistsError):
            survey_register.export_register(self.run, self.output)
        self.assertFalse(target.exists())
        self.assertTrue(self.output.is_symlink())

    def test_tampered_reply_or_wrong_packet_never_produces_a_register(self):
        self.submit(self.reply())
        path = next((self.run / 'attempts').glob('*.json'))
        original = json.loads(path.read_text())
        mutations = [lambda a: a['reply']['candidates'][0].update(claim='Invented'),
                     lambda a: a.update(response_sha256='0' * 64),
                     lambda a: a.update(packet_id='foreign'),
                     lambda a: a.update(status='accepted')]
        for mutate in mutations:
            attempt = copy.deepcopy(original)
            mutate(attempt)
            path.write_text(json.dumps(attempt))
            with self.assertRaises(ValueError):
                survey_register.export_register(self.run, self.output)
            self.assertFalse(self.output.exists())

    def test_rejected_attempts_do_not_become_promises(self):
        self.submit({'invalid': True})
        self.submit(self.reply())
        result = survey_register.build_register(self.run)
        self.assertEqual(len(result['promises']), 1)
        self.assertEqual(result['metadata']['survey']['rejected_attempts'], 1)

    def test_changed_candidate_gets_a_new_proposal_id_without_modifying_old_output(self):
        first = self.reply()
        self.submit(first)
        survey_register.export_register(self.run, self.output)
        original = self.output.read_bytes()
        old_id = json.loads(original)['promises'][0]['id']
        first['candidates'][0]['qualifiers'] = 'Only positive integers.'
        self.submit(first)
        proposal = survey_register.build_register(self.run)
        self.assertEqual(len({p['id'] for p in proposal['promises']}), 2)
        self.assertIn(old_id, [p['id'] for p in proposal['promises']])
        self.assertEqual(self.output.read_bytes(), original)

    def test_size_or_publish_failure_leaves_no_partial_output(self):
        self.submit(self.reply())
        with patch.object(survey_register, 'MAX_REGISTER', 1):
            with self.assertRaises(ValueError):
                survey_register.export_register(self.run, self.output)
        self.assertFalse(self.output.exists())
        with patch.object(os, 'link', side_effect=OSError('publish failed')):
            with self.assertRaisesRegex(OSError, 'publish failed'):
                survey_register.export_register(self.run, self.output)
        self.assertFalse(self.output.exists())
        self.assertEqual(list(self.base.glob('.survey-register-*')), [])


if __name__ == '__main__':
    unittest.main()
