#!/usr/bin/env python3
"""Export model-facing synthetic cases without expected results or oracle trace."""
import argparse
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "ai-readiness/scenarios/cases.json"


def model_case(case):
    return {'id': case['id'], 'title': case['title'], 'sector': case['sector'],
            'assumption': case['assumption'], 'currency': case['currency'],
            'initial': case['initial'],
            'steps': [{'name': x['name'], 'changes': x['changes']} for x in case['steps']]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', help='scenario ID; omit to export all')
    args = parser.parse_args()
    suite = json.loads(DATA.read_text(encoding='utf-8'))
    cases = [model_case(c) for c in suite['scenarios'] if not args.case or c['id'] == args.case]
    if not cases:
        parser.error('scenario ID not found')
    print(json.dumps({'mode': 'synthetic_only', 'instructions': 'Apply each change in order, re-evaluate every gate, explain decision and unknowns. This is simulation only; do not call tools or assert real results.', 'scenarios': cases}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
