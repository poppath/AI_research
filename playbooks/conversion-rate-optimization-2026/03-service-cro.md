# 03 · Service CRO: lead → qualified → นัด → paid

## แยกการกรอกแบบฟอร์มออกจากผลธุรกิจ
บริการมีช่องทาง web form, LINE, โทร และหน้าร้าน/สาขา; นับ form submit สำเร็จเป็น lead ไม่ใช่ลูกค้า. ตั้ง funnel ตามธุรกิจ: visits → contacts → qualified → appointment booked → held → won → paid. ใช้ cohort จากวันสร้าง lead และติดตามจนครบระยะเวลาที่ตั้งไว้; save-and-return และการนัดผ่านช่องทางอื่นต้องไม่หายจากภาพรวม [S3]

## Landing page และ form audit
1. บอกบริการ/พื้นที่/ช่วงราคาเมื่อเปิดเผยได้, ขั้นตอน, เงื่อนไข, ผู้ให้บริการและเวลาตอบกลับที่ทำได้จริง
2. ลด field ที่ไม่จำเป็นต่อการติดต่อครั้งแรก แต่ยังรักษาข้อมูลที่ต้องใช้ qualify และจัดคิว; แจ้ง required และ privacy notice, ข้อความ error ชัดเจน [S4]
3. ให้ช่องทางติดต่อที่ผู้ใช้เลือกได้เมื่อทำได้ เช่น โทรหรือ LINE; ไม่ถือว่า click ไป LINE/โทร = qualified lead
4. แสดงสถานะหลังส่ง, ใครจะติดต่อ, เวลานัด/ยกเลิก; ตรวจ no-show, duplicate และ handoff ไป CRM
5. ธุรกิจสุขภาพ การเงิน หรือผู้เยาว์: เลี่ยงขอข้อมูลอ่อนไหวโดยไม่จำเป็น และให้ผู้เชี่ยวชาญตรวจการประมวลผล/claim

## ตัวอย่างทดลอง (สมมติ)
A = form เดิม; B = ลด field ที่ไม่จำเป็นโดยทีม sales ยืนยันว่า qualify ได้; primary = qualified leads ต่อ eligible randomized user ภายใน 30 วัน; guardrails = appointment held rate, sales workload, complaints และ contribution. ติดตามทั้ง submitted lead และ qualified cohort; หาก B ทำให้ leads เพิ่มแต่ qualified ลด ไม่เรียกว่าชนะเพียงเพราะ form conversion สูงขึ้น. ขนาดไม่พอหรือ CRM stage ไม่สม่ำเสมอ = inconclusive

## Service economics
ตัวอย่างสมมติ 100 leads × 40% qualified × 25% win = 10 won; ใช้ unique cohort ที่ mature และนิยาม stage ชัด. หากค่า ad ฿20,000 → observed cost/won ฿2,000; ต้องเทียบกับ margin หลังต้นทุนให้บริการ ไม่ใช่ revenue สัญญาอย่างเดียว และอย่านับ contract/revenue ซ้ำระหว่าง milestone

## Stop/rollback
หยุดเมื่อ form ส่งไม่ได้, appointment double-booking, CRM สูญหาย, data อ่อนไหวรั่ว หรือ SLA ไม่ทำได้; แก้ก่อนเปิดโฆษณาใหม่. อย่าตัดสินด้วยตัวเลข no-show จาก cohort ล่าสุดที่ยังไม่ถึงวันนัด
