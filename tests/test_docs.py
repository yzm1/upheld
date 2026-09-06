"""Check observable document/schema failures with explicit synthetic test records."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from check_readme_status import check
from prepare_probe_review import convert, diagnostics
import fastjsonschema


def validator(name):
    return fastjsonschema.compile(json.loads((ROOT / f'schemas/0.1/{name}.schema.json').read_text()))


class DocumentationChecks(unittest.TestCase):
    def test_current_readme_matches_real_records(self):
        self.assertEqual(check(), [])

    def test_historical_absence_claim_is_detected(self):
        text = (ROOT / 'README.md').read_text() + '\nNothing has been measured from a real register.\n'
        self.assertTrue(any(x['code'] == 'obsolete_status_claim' for x in check(readme=text)))

    def test_changed_count_is_detected(self):
        text = (ROOT / 'README.md').read_text().replace('| Promises | 44 |', '| Promises | 45 |')
        self.assertTrue(any(x['code'] == 'status_count_mismatch' for x in check(readme=text)))

    def test_unreadable_input_does_not_report_clean(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'tools').mkdir()
            (root / 'tools/check_readme_status.py').write_text((ROOT / 'tools/check_readme_status.py').read_text())
            (root / 'README.md').write_text('Unrelated document')
            run = subprocess.run([sys.executable, str(root / 'tools/check_readme_status.py')], capture_output=True, text=True)
            self.assertEqual(run.returncode, 2)
            self.assertEqual(json.loads(run.stdout)['result'], 'could_not_look')

    def test_probe_copy_preserves_original_and_diagnostics(self):
        src = json.loads((ROOT / 'examples/heldtospec-contracts/obligations.register.json').read_text())
        before = copy.deepcopy(src)
        converted = convert(src, 'examples/heldtospec-contracts/obligations.register.json')
        self.assertEqual(src, before)
        validator('register')(converted)
        self.assertEqual([x['subject'] for x in diagnostics(converted)], ['CTR-003','CTR-005','CTR-037','CTR-044'])
        self.assertEqual([p['id'] for p in src['promises']], [p['id'] for p in converted['promises']])

    def test_missing_kind_and_stored_promise_status_fail(self):
        doc = json.loads((ROOT / 'examples/upheld-status/obligations.register.json').read_text())
        for broken in ('kind', 'status'):
            changed = copy.deepcopy(doc)
            if broken == 'kind': del changed['promises'][0]['defenses'][0]['guarded_by']
            else: changed['promises'][0]['status'] = 'answered'
            with self.assertRaises(fastjsonschema.JsonSchemaException): validator('register')(changed)

    def test_extension_needs_mechanism_and_latent_needs_trigger(self):
        doc = json.loads((ROOT / 'examples/upheld-status/obligations.register.json').read_text())
        p = doc['promises'][0]; d = p['defenses'][0]
        d['guarded_by'] = 'x-manual-inspection'
        with self.assertRaises(fastjsonschema.JsonSchemaException): validator('register')(doc)
        d['mechanism'] = 'A person inspects the stated surface.'
        validator('register')(doc)
        p['reachability'] = 'latent'
        with self.assertRaises(fastjsonschema.JsonSchemaException): validator('register')(doc)
        p['armed_by'] = 'Public release'
        validator('register')(doc)

    def test_unresolvable_cannot_be_removed_from_config_gates(self):
        doc = {'schema_version':'0.1','hashing_profile':'test-only-profile','resolver_versions':{},'gated_facets':['link']}
        with self.assertRaises(fastjsonschema.JsonSchemaException): validator('config')(doc)
        doc['gated_facets'].append('unresolvable')
        validator('config')(doc)

    def test_synthetic_evidence_needs_basis_and_explicit_execution_context(self):
        # Deliberately synthetic schema fixture: never written to an evidence file.
        h = 'sha256:' + '0'*64
        doc = {'schema_version':'0.1','evidence_id':'test-only','defense_id':'test-only:d0',
               'oracle':'seeded_violation','oracle_result':'fired','verdict':'supports',
               'validated_subject_scope':'README.md','source_rev':'test-fixture','producer':'test-only',
               'supersedes':None,'basis':{'hashing_profile':'test-only','promise':h,'defense_assertion':h,
               'artifacts':{'check.py':h},'subject_scope':{'scope':'README.md','hash':h},'environment':{}},
               'execution':{'status':'unknown','reason':'Synthetic shape test only'}}
        validator('evidence')(doc)
        for key in ('basis','execution'):
            changed=copy.deepcopy(doc); del changed[key]
            with self.assertRaises(fastjsonschema.JsonSchemaException): validator('evidence')(changed)

    def test_first_command_outputs_accept_supported_shapes(self):
        validator('validate-output')({'schema_version':'0.1','command':'validate','exit_code':1,'diagnostics':[{'code':'missing','subject':'test-only','message':'Synthetic diagnostic'}]})
        validator('basis-output')({'schema_version':'0.1','command':'basis','exit_code':2,'diagnostics':[]})
        validator('verify-output')({'schema_version':'0.1','command':'verify','exit_code':0,'findings':[],'diagnostics':[],
                                  'counts':{k:0 for k in ['promises','open_defenses','gaps','still_valid','review_required','invalid','unresolvable']}})


if __name__ == '__main__': unittest.main()
