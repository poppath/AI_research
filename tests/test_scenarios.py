import copy
import itertools
import json
import unittest
from jsonschema import Draft202012Validator
from scripts.simulate_decisions import DATA, decision, run_case


class ScenarioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding='utf-8'))
        cls.schema = json.loads((DATA.parent / 'schema.json').read_text(encoding='utf-8'))

    def test_schema_ids_and_expected_steps(self):
        Draft202012Validator(self.schema).validate(self.data)
        scenarios = self.data['scenarios']
        self.assertEqual(len(scenarios), len({x['id'] for x in scenarios}))
        for scenario in scenarios:
            outputs = run_case(scenario)
            for step, result in zip(scenario['steps'], outputs):
                with self.subTest(case=scenario['id'], step=step['name']):
                    self.assertEqual(result['stage'], step['expected']['stage'])
                    self.assertEqual(result['decision'], step['expected']['decision'])
                    self.assertTrue(result['trace'])

    def test_all_required_gates_fail_closed(self):
        state = self.data['scenarios'][0]['initial']
        for key in ['prohibited', 'incident', 'budget_breach', 'rights', 'eligibility', 'measurement', 'approval_matches', 'consent']:
            changed = copy.deepcopy(state)
            changed[key] = None
            with self.subTest(gate=key):
                self.assertNotEqual(decision(changed)['decision'], 'SIMULATE_RUN')
        changed = copy.deepcopy(state)
        changed.update(regulated=True, specialist_review=None)
        self.assertEqual(decision(changed)['decision'], 'HOLD')

    def test_all_economics_combinations(self):
        state = self.data['scenarios'][0]['initial']
        for revenue, cost, floor in itertools.product([0, 100, 200], repeat=3):
            s = dict(state, revenue_minor=revenue, cost_minor=cost, floor_minor=floor)
            self.assertEqual(decision(s)['decision'], 'SIMULATE_RUN' if revenue-cost >= floor else 'REWORK')

    def test_no_scale_on_inconclusive_and_timeout(self):
        state = self.data['scenarios'][0]['initial']
        self.assertEqual(decision(dict(state, execution='timeout'))['decision'], 'RECONCILE_FIRST')
        self.assertEqual(decision(dict(state, execution='success', settlement='matched', outcome='inconclusive'))['decision'], 'LEARN_MORE')
        self.assertEqual(decision(dict(state, execution='success', settlement='pending', outcome='positive'))['decision'], 'RECONCILE_FIRST')

    def test_reject_negative_or_typo(self):
        data = copy.deepcopy(self.data)
        data['scenarios'][0]['initial']['cost_minor'] = -1
        self.assertTrue(list(Draft202012Validator(self.schema).iter_errors(data)))
        data = copy.deepcopy(self.data)
        data['scenarios'][0]['steps'][0]['changes']['approvla_matches'] = True
        self.assertTrue(list(Draft202012Validator(self.schema).iter_errors(data)))


class PromptExportTest(unittest.TestCase):
    def test_export_never_includes_expectations(self):
        from scripts.export_scenario_prompts import model_case
        case = json.loads(DATA.read_text(encoding='utf-8'))['scenarios'][0]
        exported = model_case(case)
        self.assertFalse(any('expected' in step for step in exported['steps']))
        self.assertEqual(len(case['steps']), len(exported['steps']))
        self.assertEqual(exported['initial'], case['initial'])


if __name__ == '__main__':
    unittest.main()
