import tempfile
import unittest
from pathlib import Path
from scripts.retrieve_context import retrieve, sections


class RetrievalTest(unittest.TestCase):
    def test_empty_and_missing(self):
        self.assertEqual(retrieve(''), [])
        self.assertEqual(retrieve('zzzzunfindable'), [])

    def test_results_preserve_path_lines_hash_and_no_secret_files(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'playbooks').mkdir()
            (root / 'playbooks/a.md').write_text('# Title\n\n## Discount\nDiscount rate and margin\n', encoding='utf-8')
            (root / 'secret.md').write_text('discount secret', encoding='utf-8')
            result = retrieve('discount', root=root)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]['path'], 'playbooks/a.md')
            self.assertEqual(result[0]['start_line'], 3)
            self.assertEqual(result[0]['end_line'], 4)
            self.assertEqual(len(result[0]['sha256']), 64)
            self.assertEqual(result[0]['evidence_status'], 'unknown_or_legacy_unverified')

    def test_thai_search_and_limit(self):
        results = retrieve('ส่วนลด', limit=2)
        self.assertEqual(len(results), 2)
        self.assertTrue(all(r['lexical_score'] > 0 for r in results))


if __name__ == '__main__':
    unittest.main()
