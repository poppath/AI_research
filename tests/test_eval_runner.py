import sys
import unittest
from scripts.run_agent_evals import run_case


class EvalRunnerTest(unittest.TestCase):
    def setUp(self):
        self.case = {'id': 'E-001', 'prompt': 'สวัสดี', 'expected_disposition': 'HOLD', 'must_include': ['SECRET_RUBRIC']}

    def test_adapter_sees_prompt_not_rubric(self):
        code = "import sys,json; x=json.load(sys.stdin); print(json.dumps({'response': json.dumps(x)}))"
        result = run_case([sys.executable, '-c', code], self.case, 5)
        self.assertEqual(result['status'], 'completed')
        self.assertNotIn('SECRET_RUBRIC', result['response'])
        self.assertNotIn('expected_disposition', result['response'])

    def test_invalid_and_failure(self):
        self.assertEqual(run_case([sys.executable, '-c', 'print("bad")'], self.case, 5)['status'], 'invalid_json')
        self.assertEqual(run_case([sys.executable, '-c', 'raise SystemExit(1)'], self.case, 5)['status'], 'adapter_error')

    def test_timeout(self):
        self.assertEqual(run_case([sys.executable, '-c', 'import time; time.sleep(2)'], self.case, .1)['status'], 'timeout')


if __name__ == '__main__':
    unittest.main()
