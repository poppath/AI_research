#!/usr/bin/env python3
"""Identify numeric lines for human review; heuristic candidates, not factual claims."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'ai-readiness/numeric-candidates.json'
PATTERN = re.compile(r'(?:฿|\$)\s*\d|\d[\d,.]*\s*(?:%|บาท|THB|USD|เท่า|conversions?|orders?|วัน|สัปดาห์|เดือน|hours?|days?)|(?:≥|≤|>=|<=)\s*\d', re.I)


def build(root=ROOT):
    docs = []
    for path in sorted((root / 'playbooks').rglob('*.md')):
        raw = path.read_bytes()
        text = raw.decode('utf-8')
        matches = [{'line': n, 'text': line.strip(), 'status': 'candidate_unreviewed'}
                   for n, line in enumerate(text.splitlines(), 1)
                   if not line.lstrip().startswith('#') and PATTERN.search(line)]
        if matches:
            docs.append({'path': path.relative_to(root).as_posix(),
                         'sha256': hashlib.sha256(raw).hexdigest(), 'candidates': matches})
    return {'version': '1.0', 'method': 'regex numeric lines; false positives and false negatives; not a complete claim extraction',
            'documents': docs}


def encode(data):
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = build()
    content = encode(data)
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding='utf-8') != content:
            print('Numeric candidate index drift: regenerate and review.')
            return 1
    else:
        OUT.write_text(content, encoding='utf-8')
    print(f"Numeric candidates: {sum(len(x['candidates']) for x in data['documents'])} lines across {len(data['documents'])} files; no factual verification.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
