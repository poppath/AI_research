#!/usr/bin/env python3
"""Run cases against a user-provided sandboxed adapter. Never runs a model itself."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_case(command, case, timeout):
    # No expected answer, disposition or scoring rubric is given to the adapter.
    request = json.dumps({'case_id': case['id'], 'prompt': case['prompt']}, ensure_ascii=False)
    try:
        result = subprocess.run(command, input=request, text=True, capture_output=True,
                                timeout=timeout, check=False)
    except subprocess.TimeoutExpired:
        return {'case_id': case['id'], 'status': 'timeout', 'response': None}
    if result.returncode != 0:
        # Do not persist stderr; it may contain secrets.
        return {'case_id': case['id'], 'status': 'adapter_error', 'response': None}
    try:
        output = json.loads(result.stdout)
    except json.JSONDecodeError:
        return {'case_id': case['id'], 'status': 'invalid_json', 'response': None}
    if not isinstance(output, dict) or not isinstance(output.get('response'), str):
        return {'case_id': case['id'], 'status': 'invalid_response', 'response': None}
    return {'case_id': case['id'], 'status': 'completed', 'response': output['response']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, help='JSONL results path; use a secure location outside the repo')
    parser.add_argument('--timeout', type=float, default=60)
    parser.add_argument('adapter', nargs=argparse.REMAINDER, help='command after --; reads one JSON object from stdin')
    args = parser.parse_args()
    command = args.adapter[1:] if args.adapter[:1] == ['--'] else args.adapter
    if not command or args.timeout <= 0:
        parser.error('provide adapter command after -- and a positive timeout')
    cases = json.loads((ROOT / 'ai-readiness/evals/cases.json').read_text(encoding='utf-8'))['cases']
    # Exclusive creation prevents silently overwriting previous experiment evidence.
    with open(args.output, 'x', encoding='utf-8') as out:
        for case in cases:
            try:
                item = run_case(command, case, args.timeout)
            except OSError as exc:
                print(f'Adapter could not start: {exc}', file=sys.stderr)
                return 1
            out.write(json.dumps(item, ensure_ascii=False) + '\n')
            out.flush()
    print(f'Wrote {len(cases)} ungraded results; human review is required.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
