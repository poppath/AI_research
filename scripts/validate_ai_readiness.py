#!/usr/bin/env python3
"""Validate opted-in v1 fixtures; no network, no semantic truth validation."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'ai-readiness'
PAIRS = [
    ('schemas/claims.schema.json', 'claims.json'),
    ('schemas/agent-evals.schema.json', 'evals/cases.json'),
    ('schemas/decision-record.schema.json', 'examples/decision-record.json'),
    ('schemas/playbook-envelope.schema.json', 'examples/playbook-envelope.json'),
    ('scenarios/schema.json', 'scenarios/cases.json'),
]


def validate_all():
    errors = []
    for schema_file, data_file in PAIRS:
        schema = json.loads((BASE / schema_file).read_text(encoding='utf-8'))
        data = json.loads((BASE / data_file).read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for e in validator.iter_errors(data):
            errors.append(f'{data_file}:{"/".join(map(str, e.absolute_path))}: {e.message}')
    claims = json.loads((BASE / 'claims.json').read_text(encoding='utf-8'))['claims']
    ids = [c['id'] for c in claims]
    if len(ids) != len(set(ids)):
        errors.append('claims.json: duplicate claim IDs')
    for claim in claims:
        if not (ROOT / claim['repo_path']).is_file():
            errors.append(f'{claim["id"]}: missing repo_path {claim["repo_path"]}')
    cases = json.loads((BASE / 'evals/cases.json').read_text(encoding='utf-8'))['cases']
    if len({c['id'] for c in cases}) != len(cases):
        errors.append('evals/cases.json: duplicate case IDs')
    envelope = json.loads((BASE / 'examples/playbook-envelope.json').read_text(encoding='utf-8'))
    for path in [envelope['legacy_path'], *envelope['source_paths']]:
        if not (ROOT / path).is_file():
            errors.append(f'envelope: missing path {path}')
    for claim_id in envelope['claim_ids']:
        if claim_id not in ids:
            errors.append(f'envelope: unknown claim {claim_id}')
    record = json.loads((BASE / 'examples/decision-record.json').read_text(encoding='utf-8'))
    for ref in record['evidence']:
        if ref['claim_id'] is not None and ref['claim_id'] not in ids:
            errors.append(f'decision: unknown claim {ref["claim_id"]}')
    return errors


if __name__ == '__main__':
    errors = validate_all()
    for err in errors:
        print(err)
    print(f'AI readiness structural validation: {len(errors)} error(s); semantic claims unverified.')
    raise SystemExit(bool(errors))
