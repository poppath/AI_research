#!/usr/bin/env python3
"""Offline structural checks; does not verify facts or external URLs."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
for path in files:
    rel = path.relative_to(ROOT)
    if path.suffix == '.json':
        try:
            json.loads(path.read_text(encoding='utf-8'))
        except (ValueError, UnicodeError) as exc:
            errors.append(f'{rel}: invalid JSON: {exc}')
    if path.suffix == '.md':
        for dest in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            dest = dest.split()[0].split('#')[0].split('?')[0]
            if not dest or '://' in dest or dest.startswith(('mailto:', '/')):
                continue
            if not (path.parent / unquote(dest)).exists():
                errors.append(f'{rel}: missing link {dest}')
groups = json.loads((ROOT / 'playbooks/sector-business-2026/gics-drilldown/groups.json').read_text())['groups']
if len(groups) != 25 or len({g['group_code'] for g in groups}) != 25 or len({g['sector_code'] for g in groups}) != 11:
    errors.append('GICS: expected 11 sectors and 25 distinct groups')
for error in errors:
    print(error, file=sys.stderr)
print(f'Checked {len(files)} files, JSON syntax, relative markdown links, GICS counts; {len(errors)} error(s).')
sys.exit(bool(errors))
