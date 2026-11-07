import unittest
from scripts.build_numeric_candidates import OUT, build, encode


class CandidateTest(unittest.TestCase):
    def test_index_matches_sources(self):
        current = build()
        self.assertEqual(OUT.read_text(encoding='utf-8'), encode(current))
        self.assertTrue(current['documents'])
        self.assertTrue(all(c['status'] == 'candidate_unreviewed' for d in current['documents'] for c in d['candidates']))


if __name__ == '__main__':
    unittest.main()
