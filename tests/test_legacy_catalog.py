import json
import unittest
from pathlib import Path
from scripts.build_legacy_catalog import ROOT, OUT, build_catalog, encode


class CatalogTest(unittest.TestCase):
    def test_matches_sources_and_includes_all_files(self):
        catalog = build_catalog()
        self.assertEqual(OUT.read_text(encoding='utf-8'), encode(catalog))
        paths = {d['path'] for d in catalog['documents']}
        expected = {p.relative_to(ROOT).as_posix() for p in ROOT.glob('playbooks/**/playbook.json')}
        expected |= {p.relative_to(ROOT).as_posix() for p in ROOT.glob('playbooks/**/agent-rules.yaml')}
        self.assertEqual(paths, expected)
        self.assertTrue(all(e['status'] == 'needs_review' for d in catalog['documents'] for e in d['entries']))

    def test_json_rules_roundtrip(self):
        for doc in build_catalog()['documents']:
            if doc['format'] != 'json':
                continue
            source = json.loads((ROOT / doc['path']).read_text())
            self.assertEqual([x['original'] for x in doc['entries']], source['rules'])


if __name__ == '__main__':
    unittest.main()
