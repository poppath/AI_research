# Customer Experience, Service & Reviews · คู่มือปฏิบัติ

## 1. ตั้ง service journey
แผนที่ตั้งแต่คำถามก่อนซื้อ → order confirmation → tracking → issue → refund/exchange → follow-up; กำหนด owner, escalation, เวลาเป้าหมายที่ร้านรับไหว, ช่องทางเข้าถึง และวิธีส่งต่องาน; แยกคำสัญญากับลูกค้าออกจากเป้าภายใน

## 2. จัดการ case
ใช้ case ID, timestamp, reason, SKU, order status, owner, next action, resolution และ customer contact preference; ออกแบบ taxonomy เช่น product mismatch, late delivery, damage, payment และ return; เข้าถึงข้อมูลเท่าที่จำเป็น ไม่ใส่ข้อมูลส่วนบุคคลลง public repo หรือ AI ที่ไม่อนุมัติ

## 3. Recovery และ reviews
รับฟังและยืนยันปัญหา เสนอทางเลือกที่ทำได้จริง แจ้งระยะเวลาและติดตามจนปิด; วิเคราะห์ root cause แยกอาการกับสาเหตุ ส่งต่อ ops/creative/offer; ขอรีวิวจากประสบการณ์จริงอย่างเป็นกลาง ไม่สร้างรีวิวหรือกดทับรีวิวลบ ตรวจสิทธิการนำคำพูดไปใช้ซ้ำและ disclosure ในตลาด/แพลตฟอร์มนั้น FTC เป็นกฎหมายสหรัฐไม่ใช่หลักกฎหมายไทย [S1]

## 4. วัดและหยุด
first response time และ resolution time ระบุ business hours และ median/percentile; complaint rate = cases / orders ใน cohort เดียวกัน (ต้องระวังหนึ่ง order มีหลาย case); refund rate และ repeat แยก cohort; หยุด campaign/claim เมื่อพบ product harm หรือคำโฆษณาไม่ตรง พร้อม escalation และบันทึกการแก้ไข

เชื่อม LINE CRM โดยไม่ส่งข้อความการตลาดเกินสิทธิที่มี; ประสานผู้รับผิดชอบ PDPA เรื่อง notice, basis, retention และสิทธิผู้ใช้
