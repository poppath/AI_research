# 04 · Planning, tests และ diagnostics

## ก่อน launch — checklist
- ธุรกิจสินค้า: order economics, inventory และ feed/price/availability; บริการ: qualified definition, handoff, CRM, capacity และ revenue/cost ต่อบริการ
- เก็บ campaign objective, source, target geography/language, landing, privacy notice, required claims และผู้อนุมัติ
- ตรวจ primary/secondary + account/default/campaign/custom goals; ทดสอบ conversion events และ duplicate ใน production อย่างปลอดภัย
- ระบุ baseline, primary KPI, 2 guardrails, budget/day + total cap, owner, review date และ stop rules

## Test plan
เปรียบเทียบ ad/landing/strategy แบบ random ที่เครื่องมือรองรับ โดยคงสิ่งที่ไม่ใช่ตัวแปรเป้าหมายและลงทะเบียน MDE/power/sample, conversion lag, budget และ interval ก่อนเริ่ม; test PMax เป็น multi-surface intervention ไม่อนุมานผล Search ล้วน. Google Conversion Lift ไม่พร้อมทุกบัญชี [S8]; หากไม่ feasible ให้รายงาน exploratory และปัจจัยกวน

## Diagnostic table
| อาการ | ตรวจเป็นลำดับ | ห้ามสรุปเร็ว |
|---|---|---|
| clicks เยอะ แต่ product paid ต่ำ | query intent → landing → checkout → payment → inventory | โทษ keyword อย่างเดียว |
| lead เยอะ แต่ won น้อย | duplicate → qualification → sales follow-up → cohort maturity → service fit | CPL ต่ำ = คุ้ม |
| conversions หาย | tag/consent → data lag → goal configuration → imports → CRM | demand หายแน่ |
| ROAS ดีแต่ cash ตึง | refunds/fee, contribution, settlement lag, capacity | ROAS = กำไร |

## Review
รายวันตรวจ incident/cap; รายสัปดาห์ดู search terms, conversion health, feed/CRM and capacity; รายเดือน reconcile และวาง test. หาก action ต้องอาศัยข้อมูลที่ยังไม่มี ให้ระบุ owner และวิธีเก็บ ไม่ใช้ benchmark ทดแทน
