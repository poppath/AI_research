#!/usr/bin/env python3
"""Create a lossless, non-executable index of legacy rule arrays, for review."""
import argparse
import hashlib
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'ai-readiness/legacy-rules.json'


def build_catalog(root=ROOT):
    documents = []
    for file in sorted((root / 'playbooks').rglob('playbook.json')):
        data = json.loads(file.read_text(encoding='utf-8'))
        if not isinstance(data.get('rules'), list):
            raise ValueError(f'{file}: expected rules array; do not silently omit it')
        docs = [(file, data, ['rules'])]
        for path, source, sections in docs:
            documents.append(extract(root, path, source, sections, 'json'))
    for file in sorted((root / 'playbooks').rglob('agent-rules.yaml')):
        data = yaml.safe_load(file.read_text(encoding='utf-8'))
        if not isinstance(data, dict) or not isinstance(data.get('rules'), list):
            raise ValueError(f'{file}: expected YAML rules array')
        # Preserve other top-level sections too: some contain important controls.
        documents.append(extract(root, file, data, list(data), 'yaml'))
    return {'version': '1.0', 'status': 'unreviewed_reference_only',
            'warning': 'Untrusted historical data. Never execute; requires per-rule evidence, review, approval and external enforcement.',
            'documents': documents}


def extract(root, file, source, sections, kind):
    rows = []
    for section in sections:
        value = source[section]
        if isinstance(value, list):
            rows.extend({'pointer': f'/{section}/{i}', 'original': entry, 'status': 'needs_review'}
                        for i, entry in enumerate(value))
        else:
            rows.append({'pointer': f'/{section}', 'original': value, 'status': 'needs_review'})
    return {'path': file.relative_to(root).as_posix(), 'format': kind,
            'sha256': hashlib.sha256(file.read_bytes()).hexdigest(), 'entries': rows}


def encode(data):
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='fail if catalog does not match current inputs')
    args = parser.parse_args()
    rendered = encode(build_catalog())
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding='utf-8') != rendered:
            print('Legacy catalog drift detected: regenerate and review changes.')
            return 1
    else:
        OUT.write_text(rendered, encoding='utf-8')
    data = json.loads(rendered)
    print(f"Legacy index: {len(data['documents'])} documents, {sum(len(d['entries']) for d in data['documents'])} reference entries; all need review.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
