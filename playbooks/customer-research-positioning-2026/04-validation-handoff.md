# 04 · Validate → ส่งต่อ creative

## Validation ladder
| ขั้น | วิธี | ผลที่นำไปใช้ได้ | สิ่งที่ห้ามสรุป |
|---|---|---|---|
| Discovery | neutral interview | สร้างสมมติฐานและคำลูกค้า | คนทั้งตลาดมีปัญหาเท่านี้ |
| Message comprehension | ให้กลุ่มเป้าหมายอธิบายข้อความด้วยคำตัวเอง | แก้ความเข้าใจผิด | เกิดยอดขายจริง |
| Behavioral test | randomized A/B หรือ landing test เมื่อมีทรัพยากร | ผลเปรียบเทียบภายใต้ design | สาเหตุหากหลายตัวแปรเปลี่ยนหรือ traffic เลือกเอง |
| Economics & repeat | กำไร + cohort | ขยายภายใต้ข้อจำกัดที่วัดได้ | ยอดคลิกเท่ากับกำไร |

กำหนด hypothesis, unit of randomization, primary KPI, guardrails, baseline, minimum detectable effect (MDE), ขนาดตัวอย่าง, ช่วง attribution, ระยะเวลา, budget cap และ stop rules **ก่อน** ทดสอบ หาก sample/งบไม่พอให้ระบุ inconclusive ไม่เรียกผู้ชนะ [S5]. ผลใน ad set เดียวกันที่ระบบจัดสรร impression ไม่เท่ากันเป็นการสำรวจ ไม่ใช่ randomized causal result

## ตัวอย่าง Handoff (ตัวเลขสมมติ ไม่ใช่ผลวิจัย)
H-01: ผู้ซื้อใหม่ที่กังวลเรื่องเวลาอาจตอบสนองต่อ demo มากกว่า feature list; evidence E-01/E-02 **ยังต้องเก็บจริง**; test A=demo, B=feature list, offer/landing/objective คงที่; primary = cost per qualified purchase; guardrails = CM3/order และ complaint rate; ก่อนเริ่มใส่ target, cap, sample และ date จากธุรกิจจริง; stop ถ้าข้ออ้างไม่ผ่าน QA หรือ tracking เสีย; ข้อมูลไม่พอ = inconclusive

ส่ง [creative brief](../ai-creative-production-2026/templates.md) พร้อม segment, context, evidence IDs, claim/proof, offer, objections, constraints และ test spec ปิดวงโดยนำผลกลับมาแก้สมมติฐาน ไม่ตีความ ad delivery เป็นหลักฐานว่าทุกคนใน segment คิดเหมือนกัน
