#!/usr/bin/env python3
"""Synthetic, side-effect-free decision tree; no accounts, calls, money or LLM."""
import argparse
import copy
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'ai-readiness/scenarios/cases.json'


def decision(s):
    """Evaluate one synthetic state; input must already pass the schema."""
    trace = []

    def gate(stage, ok, failure, why):
        trace.append({'stage': stage, 'result': 'pass' if ok else 'blocked', 'reason': why})
        return None if ok else {'stage': stage, 'decision': failure, 'reason': why, 'trace': trace}

    checks = [
        ('prohibited', s['prohibited'] is False, 'REJECT' if s['prohibited'] is True else 'HOLD', 'ห้ามละเมิดสิทธิ bypass หรือปลอมหลักฐาน'),
        ('incident', s['incident'] is False, 'STOP' if s['incident'] is True else 'HOLD', 'ตรวจ safety, platform และ security incident'),
        ('budget_breach', s['budget_breach'] is False, 'STOP' if s['budget_breach'] is True else 'HOLD', 'ตรวจ budget cap ที่อนุมัติ'),
        ('baseline', all(s[k] is not None for k in ('business', 'role', 'market', 'channel')), 'NEEDS_INFO', 'ระบุธุรกิจ บทบาท ตลาด และช่องทาง'),
        ('rights', s['rights'] is True, 'HOLD', 'สิทธิ asset และการใช้เนื้อหาต้องชัดเจน'),
        ('evidence', s['evidence'] == 'verified', 'HOLD', 'ตรวจหลักฐาน claim, scope และความใหม่'),
        ('regulated', s['regulated'] is False or (s['regulated'] is True and s['specialist_review'] is True), 'HOLD', 'กรณีกำกับต้องตรวจโดยผู้เชี่ยวชาญ'),
        ('eligibility', s['eligibility'] is True, 'HOLD', 'ตรวจ platform/program eligibility และสิทธิ'),
        ('economics_inputs', all(s[k] is not None for k in ('revenue_minor', 'cost_minor', 'floor_minor')), 'NEEDS_INFO', 'กำหนดรายได้ ต้นทุน และ floor ต่อหน่วย'),
    ]
    for args in checks:
        failure = gate(*args)
        if failure:
            return failure
    contribution = s['revenue_minor'] - s['cost_minor']
    failed = gate('economics', contribution >= s['floor_minor'], 'REWORK', 'contribution ต่อหน่วยเทียบ floor ที่กำหนด')
    if failed:
        failed['contribution_minor'] = contribution
        return failed
    checks = [
        ('measurement', s['measurement'] is True, 'HOLD', 'ต้องมี KPI, window และ tracking ที่จำลองไว้'),
        ('approval', s['approval_matches'] is True, 'HOLD', 'approval ต้องตรง payload/target/version'),
        ('consent', s['consent'] is True, 'HOLD', 'platform consent และ permission ต้องชัดเจน'),
    ]
    for args in checks:
        failure = gate(*args)
        if failure:
            failure['contribution_minor'] = contribution
            return failure
    result = s['execution']
    if result == 'not_started':
        status, why = 'SIMULATE_RUN', 'ผ่าน gate สมมติเท่านั้น; เริ่มจำลอง ไม่ใช่อนุญาตทำจริง'
    elif result == 'timeout':
        status, why = 'RECONCILE_FIRST', 'ไม่ retry ก่อนตรวจผลปลายทางหรือ idempotency ที่รองรับ'
    elif result == 'failed':
        status, why = 'STOP', 'จำลอง failure: หยุด ตรวจเหตุ และส่งต่อ owner'
    elif s['settlement'] != 'matched':
        status, why = 'RECONCILE_FIRST', 'แยก pending, approved, paid และตรวจ discrepancy'
    elif s['outcome'] in ('unknown', 'inconclusive'):
        status, why = 'LEARN_MORE', 'ข้อมูลไม่พอ ไม่สรุปว่าได้ผลหรือไม่ได้ผล'
    elif s['outcome'] == 'negative':
        status, why = 'REWORK', 'ผลจำลองไม่ผ่าน ให้ปรับหรือหยุดตามเกณฑ์ที่กำหนด'
    else:
        status, why = 'PROPOSE_NEXT_TEST', 'ผลจำลองบวก ให้เสนอทดสอบต่อ ไม่สรุป causal หรือ scale อัตโนมัติ'
    trace.append({'stage': 'outcome', 'result': 'decision', 'reason': why})
    return {'stage': 'outcome', 'decision': status, 'reason': why, 'contribution_minor': contribution, 'trace': trace}


def run_case(case):
    state = copy.deepcopy(case['initial'])
    result = []
    for step in case['steps']:
        state.update(step['changes'])
        output = decision(state)
        result.append({'step': step['name'], **output})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', help='scenario ID; omit to run all')
    args = parser.parse_args()
    suite = json.loads(DATA.read_text(encoding='utf-8'))
    schema = json.loads((DATA.parent / 'schema.json').read_text(encoding='utf-8'))
    Draft202012Validator(schema).validate(suite)
    cases = [c for c in suite['scenarios'] if not args.case or c['id'] == args.case]
    if not cases:
        parser.error('scenario ID not found')
    print(json.dumps({'mode': 'synthetic_only', 'warning': 'NOT authorization, real-account validation, platform permission, measured outcome or LLM evaluation.',
                      'scenarios': [{'id': c['id'], 'title': c['title'], 'steps': run_case(c)} for c in cases]}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
