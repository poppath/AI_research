import copy
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from scripts.validate_ai_readiness import validate_all

BASE = Path(__file__).resolve().parents[1] / 'ai-readiness'


class ReadinessSchemaTest(unittest.TestCase):
    def test_current_fixtures(self):
        self.assertEqual(validate_all(), [])

    def test_claim_missing_required_reviewer_is_rejected(self):
        schema = json.loads((BASE / 'schemas/claims.schema.json').read_text())
        data = json.loads((BASE / 'claims.json').read_text())
        data = copy.deepcopy(data)
        data['claims'][0]['status'] = 'verified'
        data['claims'][0]['reviewer'] = None
        self.assertTrue(list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data)))

    def test_invalid_date_and_extra_key(self):
        schema = json.loads((BASE / 'schemas/decision-record.schema.json').read_text())
        data = json.loads((BASE / 'examples/decision-record.json').read_text())
        data['next_review'] = '2026-02-31'
        data['surprise'] = True
        errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data))
        self.assertGreaterEqual(len(errors), 2)

    def test_cases_are_unique_and_cover_categories(self):
        cases = json.loads((BASE / 'evals/cases.json').read_text())['cases']
        categories = {c['category'] for c in cases}
        self.assertTrue({'prompt_injection', 'approval_mismatch', 'unknown_post_outcome', 'sensitive_claim', 'discount_denominator'} <= categories)
        self.assertEqual(len(cases), len({c['id'] for c in cases}))


if __name__ == '__main__':
    unittest.main()
