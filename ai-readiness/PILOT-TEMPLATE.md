# Pilot card · กรอกก่อนทดสอบกับบัญชีจริง

**สถานะ:** template ว่าง; ไม่ใช่ approval. อย่าใส่ข้อมูลลูกค้าหรือ token ลง repo.

## 1. Scope และ owner
- ธุรกิจ/offer/บทบาท (merchant, affiliate, agency): ____
- Market, channel, account ID ที่ระบบอนุญาต (เก็บใน secure system): ____
- Owner ธุรกิจ / reviewer / ผู้อนุมัติ / incident contact: ____
- เริ่ม–สิ้นสุด / เวลาทบทวน / timezone: ____
- สิ่งที่ agent ทำได้ / ห้ามทำ / ใครเป็นผู้ execute: ____

## 2. Baseline และข้อมูลที่ต้องมี
- Revenue basis, currency, COGS, fulfilment, platform fees, returns, commission settlement, tracking window: ____
- Baseline source / account / timestamp / reliability: ____ (ไม่ทราบ = UNKNOWN, ไม่ใช่ 0)
- Evidence URL/claim ID, rights, privacy, program eligibility และวันที่ตรวจ: ____
- หากข้อมูลสำคัญไม่ครบ: **NEEDS_INFO/HOLD** ไม่เริ่ม spend หรือ publish.

## 3. Experiment card
- Hypothesis / alternative / segment / channel / creative version: ____
- Primary KPI พร้อม numerator, denominator และ window: ____
- Guardrail 1 (cash/CM): ____; Guardrail 2 (safety, returns หรือ service): ____
- Cap งบรวม + รายวัน, currency, owner-approved threshold และ decision date: ____
- Comparison design / sample limitations / confounders / ไม่สรุป causal จาก correlation: ____
- Consent, platform permissions, draft approval digest และ expiry: ____

## 4. เริ่ม–หยุด–กู้คืน
- Preflight: rights และ claim approved, measurement tested, cap enforced, inventory/service ready, stop owner reachable.
- Stop immediately หาก evidence/rights ไม่ครบ, platform restriction, data/measurement incident, spend exceeds approved cap หรือ safety incident; owner ตัดสินสถานการณ์อื่นตาม thresholds ที่อนุมัติ.
- Timeout/unknown outcome → query/reconcile ก่อน retry; ไม่บันทึก success ที่ยังไม่ยืนยัน.
- Record outcome, spending, pending/approved/paid commission แยกกัน, refund/reversal, incident, owner decision และ next review; rollback plan: ____

## 5. Exit / report
- ผลลัพธ์และ denominator + uncertainty: ____; สิ่งที่เรียนรู้ / ไม่สามารถสรุป: ____
- Evidence/log references แบบ redacted: ____; reviewer sign-off: ____; next decision: ____
