# 04 · เลือกทดลองอย่างไรเมื่อทรัพยากรจำกัด

## Prioritization
ทำ backlog: problem, evidence, potential effect, implementation effort, risk, dependencies, owner และ expected decision; จัดลำดับแบบทีมตกลง ไม่แปลงคะแนนเป็นความน่าจะเป็นโดยไม่มีข้อมูล. งานที่เป็น defect ร้ายแรง เช่น payment ไม่ทำงาน / นัดไม่ได้ / privacy leak ให้แก้ก่อนทดลองเพื่อหาค่า uplift

## Pre-registration
- ปัญหาและ evidence IDs; target: product หรือ service และ eligible population
- hypothesis, randomization unit, variant, isolation, exclusions และ analysis plan
- primary outcome ต่อ eligible randomized unit, MDE ที่มีความหมาย, power, confidence interval, sample calculation, duration, expected lag และ budget cap
- guardrails: product = returns + CM3; service = qualified/held, capacity + contribution; ระบุผู้มีอำนาจหยุดและ safety stop
- planned end date และวิธี repeated looks ที่กำหนดไว้ล่วงหน้า; หลีกเลี่ยงการเลือกเฉพาะ metric ที่ดูดีหลังจบ

## ถ้าทราฟฟิกน้อย
ทดสอบความเข้าใจและ usability แบบคุณภาพ; prioritize functional fixes; หรือทำ feasibility/power calculation และรวมเวลาที่เหมาะสม; อย่าใช้ before-after เพียงอย่างเดียวเพื่อเคลมผลเชิงเหตุ เพราะโปรโมชัน seasonality และแหล่ง traffic เปลี่ยนพร้อมกัน

## อ่านผล
ตรวจ sample-ratio mismatch, bot/internal users, duplicate/late events, variant delivery และ outcome maturity; รายงาน effect, interval, guardrail และข้อจำกัด. หาก tracking เสียหรือ test underpowered = inconclusive; เมื่อพบผลเสียร้ายแรงให้ rollback และตรวจผลเสียกับลูกค้า
