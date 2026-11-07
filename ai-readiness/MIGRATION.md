# Data contract & legacy migration

## v1 documents

- `schemas/claims.schema.json`: registry ของ claims มี source, scope, status, reviewer/date/limitations, `null` หมายถึงไม่ทราบ ไม่ใช่ 0. Reviewed calculation ไม่ทำให้ source หรือข้อมูลบัญชีกลายเป็น verified.
- `schemas/agent-evals.schema.json`: กรณีทดสอบสำหรับ agent พร้อม outcome และข้อกำหนดที่ human reviewer ต้องตรวจ.
- `schemas/decision-record.schema.json`: decision record/plan ใหม่ พร้อม provenance, assumptions, missing, KPI, guardrails และสิทธิ; ตัวอย่าง [draft](examples/decision-record.json). ไม่ได้เป็น authorization object และไม่ใช้แทน policy gateway.
- `schemas/playbook-envelope.schema.json`: metadata envelope แบบ opt-in สำหรับ playbook ใหม่หรือ migrated. ไฟล์ legacy ยังคงเป็นต้นฉบับ; ห้ามถือว่า legacy JSON ผ่าน schema นี้.

Schemas ใช้ JSON Schema Draft 2020-12 และ validator มี network off; format checker สำหรับวันที่และ URI. Strict `additionalProperties: false` ช่วยจับ typo แต่ไม่พิสูจน์เนื้อหาจริง.

## การย้ายโดยไม่สร้างความเชื่อมั่นเทียม

1. เก็บไฟล์เดิมไว้และระบุ path + version ใน envelope; ทดสอบ parse ก่อน migrate. Meta ใช้ YAML, ไม่แปลงด้วยการเดาว่าเป็น JSON; sector ใช้ sources ส่วนกลาง.
2. แยก claims ที่มีผลต่องบ/ความปลอดภัยก่อน ให้ stable ID และ exact repo location. ลง `needs_review` ถ้ายังไม่ได้ตรวจแหล่งตรง + scope; กรอก source type ตาม publisher ไม่ใช่แค่ label เดิม.
3. แยก `official` (platform/regulator) กับ `account_primary` (first-party account); `vendor`, `press`, `calculation`, `unknown`. คำ `primary` legacy ไม่ map อัตโนมัติ.
4. benchmark ต้องมีค่า/unit, as_of, market, source และ confidence; ยังไม่มีข้อมูลให้ใช้ `null`/unavailable ไม่ใช่ `0`. ต้องตรวจ currency, denominator, per-unit และ context ก่อนย้าย.
5. สูตรและตัวเลขสมมติให้ใส่ assumption, input units, formula และ test; reviewed calculation ไม่ใช่ benchmark. เลี่ยงทำ claims ที่แหล่งไม่รองรับให้ดู verified.
6. ให้ reviewer ตรวจ evidence จริง บันทึกวันที่/owner และ version; ใช้ 90-day freshness gate สำหรับ budget เป็นอย่างต่ำ ไม่รับรองว่าอายุน้อยกว่า 90 วันถูกต้อง. Policy เปลี่ยนได้เร็วกว่า.
7. Review machine rules ทีละตัว: trigger, scope, action, safety override, evidence, owner. อย่า execute legacy rules; ต้องมี simulator/evals และ approval ก่อนเชื่อม tool.

## Completeness

Current registry เป็น representative starter เท่านั้น ไม่มีการสแกนหรือรับรองว่าครอบคลุมทุก numerical claim. JSON schema/CI ตรวจชนิดและโครงสร้าง ไม่ตรวจ truth, licensed use หรือ external URL. อย่าฝึกโมเดลด้วยเนื้อหา `needs_review` แล้วสรุปว่าเป็นข้อเท็จจริง.
