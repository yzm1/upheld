"""Package integrity checks; these are not language-model outcome tests."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import package_upheld_skill as skill


class SkillPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def source_copy(self):
        root = self.root / 'source'
        shutil.copytree(skill.ROOT / 'skills', root / 'skills')
        (root / 'docs').mkdir()
        for name in ('METHOD.md', 'rule-review.json'):
            shutil.copyfile(skill.ROOT / 'docs' / name, root / 'docs' / name)
        shutil.copyfile(skill.ROOT / 'LICENSE', root / 'LICENSE')
        shutil.copyfile(skill.ROOT / 'NOTICE', root / 'NOTICE')
        return root

    def test_each_client_exports_detachable_package(self):
        for client in skill.CLIENTS:
            with self.subTest(client=client):
                out = self.root / client / 'upheld'
                manifest = skill.build(client, out)
                relocated = self.root / (client + '-copy') / 'upheld'
                relocated.parent.mkdir()
                shutil.move(out, relocated)
                self.assertEqual(skill.verify_package(relocated), manifest)
                text = (relocated / 'SKILL.md').read_text()
                self.assertNotIn('allowed-tools:', text)
                if client == 'codex':
                    self.assertIn('disable-model-invocation: true', text)
                    self.assertIn('allow_implicit_invocation: false',
                                  (relocated / 'agents/openai.yaml').read_text())
                else:
                    self.assertIn('disable-model-invocation: true', text)
                    self.assertFalse((relocated / 'agents/openai.yaml').exists())
                # Every declared local reference survives relocation.
                for file in relocated.rglob('*.md'):
                    for target in skill.re.findall(r'\]\(([^)]+)\)', file.read_text()):
                        if not skill.re.match(r'^[a-z]+:', target) and not target.startswith('#'):
                            self.assertTrue((file.parent / target.split('#')[0]).is_file())

    def test_existing_output_is_untouched(self):
        out = self.root / 'upheld'
        out.mkdir()
        (out / 'local-work').write_text('keep me')
        with self.assertRaisesRegex(ValueError, 'already exists'):
            skill.build('codex', out)
        self.assertEqual(list(out.iterdir()), [out / 'local-work'])
        self.assertEqual((out / 'local-work').read_text(), 'keep me')

    def test_reference_tamper_blocks_export_before_writes(self):
        root = self.source_copy()
        p = root / 'skills/upheld/references/method.md'
        p.write_text(p.read_text().replace('| P2 | MUST |', '| P2 | SHOULD |'))
        out = self.root / 'upheld'
        with self.assertRaisesRegex(ValueError, 'drifted'):
            skill.build('codex', out, root)
        self.assertFalse(out.exists())

    def test_changed_reviewed_source_requires_new_source_pin(self):
        root = self.source_copy()
        source = root / 'docs/METHOD.md'
        source.write_text(source.read_text().replace('No supporting run', 'No recorded run'))
        path = root / 'docs/rule-review.json'
        data = json.loads(path.read_text())
        data['docs/METHOD.md']['sha256'] = skill.digest(source.read_bytes())
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'rule review'):
            skill.method_reference(root)

    def test_missing_and_escaping_references_fail(self):
        root = self.source_copy()
        core = root / 'skills/upheld/SKILL.md'
        for target in ('references/absent.md', '../../docs/METHOD.md'):
            original = core.read_text()
            core.write_text(original + f'\n[extra]({target})\n')
            with self.assertRaisesRegex(ValueError, 'Broken or escaping'):
                skill.check_bundle(root)
            core.write_text(original)

    def test_symlink_source_is_rejected(self):
        root = self.source_copy()
        path = root / 'skills/upheld/references/connectlang.md'
        path.unlink()
        path.symlink_to(root / 'docs/METHOD.md')
        with self.assertRaisesRegex(ValueError, 'unsafe source'):
            skill.check_bundle(root)

    def test_manifest_detects_changed_missing_and_extra_files(self):
        out = self.root / 'upheld'
        skill.build('codex', out)
        path = out / 'references/method.md'
        original = path.read_bytes()
        path.write_bytes(original + b'changed')
        with self.assertRaisesRegex(ValueError, 'digest mismatch'):
            skill.verify_package(out)
        path.unlink()
        with self.assertRaisesRegex(ValueError, 'files differ'):
            skill.verify_package(out)
        path.write_bytes(original)
        (out / 'references/manifest.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'files differ'):
            skill.verify_package(out)

    def test_same_sources_produce_same_bytes(self):
        left = self.root / 'left/upheld'
        right = self.root / 'right/upheld'
        self.assertEqual(skill.build('claude', left), skill.build('claude', right))
        self.assertEqual({p.relative_to(left): p.read_bytes() for p in left.rglob('*') if p.is_file()},
                         {p.relative_to(right): p.read_bytes() for p in right.rglob('*') if p.is_file()})


if __name__ == '__main__':
    unittest.main()
