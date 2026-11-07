# 24-hour operations, pilot และ decision gates

## ระบบทำงานข้ามวัน
- Scheduler รับงานที่มี owner, version และ cap; worker สร้าง draft เป็น default ไม่เผยแพร่; เก็บ state queued/running/review/approved/published/failed.
- Alert เมื่อ queue ค้าง, credential หมดอายุ, budget ใกล้เกิน, สิทธิ asset หมดอายุ, API rejection หรือโพสต์ซ้ำ. ไม่มี owner รับ alert ให้หยุด publishing ไม่ปล่อย retry ต่อเนื่อง.
- สำรองข้อมูลเท่าที่จำเป็นและทดสอบกู้คืน; ป้องกัน token, ลด PII, ลบตาม retention policy; ตรวจไฟฟ้า อุณหภูมิ เครื่องดับ และ network outage. Budget ต้องรวมค่าแรงคนและ hardware ด้วย.
- Incident: pause/kill switch → บันทึกหลักฐานและ status → revoke credential ถ้ารั่ว → แจ้ง owner/platform ตามความจำเป็น → ลบหรือแก้โพสต์ตามขั้นตอนแพลตฟอร์ม → root cause และ approval ก่อน restart. ไม่แก้ด้วยการสมัครบัญชีใหม่เพื่อหลบ restriction.

## Pilot 4 สัปดาห์ (ตัวอย่างแผน ไม่ใช่ benchmark)
| สัปดาห์ | งาน | gate |
|---|---|---|
| 1 | เลือก 1 niche/ช่องทาง, ตรวจสิทธิและ payout, กำหนด budget cap, KPI/guardrails และ owner | ไม่ทราบสิทธิหรือไม่มี owner = no launch |
| 2 | สร้างคลังสิทธิและ evidence, ทำ draft ต้นฉบับและ dry run | claim/asset/disclosure ไม่ผ่าน = แก้ก่อน |
| 3 | คนอนุมัติและโพสต์ผ่าน flow ที่อนุญาต, ตรวจลิงก์และ event | ลิงก์หรือ attribution ผิด, โพสต์ซ้ำ = หยุด |
| 4 | reconcile order status, reversal, cost และ feedback; ตัดสินใจ | หากยัง pending รายงานแยกและรอ payout window; ห้ามอ้างว่ากำไรจริง |

ก่อนเริ่มกำหนดเป้าหมาย contribution, budget สูงสุด, ระยะเวลา, จำนวน sample ที่ทำได้ และ stop-loss เป็นตัวเลขตามบัญชีจริง. Guardrails อย่างน้อย 2: compliance incidents และ spend cap. Review ทุกสัปดาห์; หยุดทันทีเมื่อสิทธิ/claim/consent ไม่ชัด, มี account restriction, เงินเกิน cap หรือ tracking ผิด. ไม่มี benchmark จำนวนวิว ยอดขาย หรือรายได้ที่รับรองผล; ใช้ข้อมูลบัญชีจริง.

## ทางเลือกการลงทุน
Manual-first → เครื่องมือช่วย draft → queue/report → approved platform-specific integration ตาม eligibility. อย่าซื้อเครื่องหรือจ่าย API ยาวก่อนรู้ unit economics. เครื่องเปิด 24h ต้องมีความคุ้มทุนเทียบ cloud/manual และแผนเมื่อคนไม่พร้อม; ไม่ถือว่า local machine = free.
