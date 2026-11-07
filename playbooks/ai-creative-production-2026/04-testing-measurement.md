# 04 · Testing, statistics และ measurement

## สองโหมด ไม่ปะปน
| | Exploration ใน campaign | Randomized experiment |
|---|---|---|
| เป้าหมาย | หา concept ที่ควรศึกษาต่อ | ประมาณผลต่างระหว่างทางเลือก |
| การจัดสรร | algorithm อาจให้งบ/impression ไม่เท่า | randomize unit และป้องกัน overlap ตามเครื่องมือ |
| ข้อสรุป | hypothesis / directional | เปรียบเทียบภายใต้ design และ uncertainty |

Meta อธิบาย A/B test ว่าแบ่ง audience ไม่ให้เห็นทั้งสองเวอร์ชัน [S8]; availability และ implementation ต้องตรวจใน account ห้ามใช้จำนวน impression เท่ากันเป็นหลักฐานสุ่มเอง

## Pre-register
- สมมติฐาน, A/B, ตัวแปรเดียวที่ต้องการแยก และสิ่งที่คงที่: offer, landing, objective, audience definition, measurement window
- unit randomization, exclusions, baseline, outcome, MDE ที่คุ้มค่า, confidence/power, sample size calculator และ expected duration จาก traffic จริง; วิธีจัดการ multiple comparisons และ repeated peeking
- primary KPI: cost per qualified purchase หรือ contribution ที่กำหนดให้ตรงโจทย์; guardrails: CM3/order และ complaints/refunds; ระบุแหล่งข้อมูลและ attribution window
- cap งบและวันปิด รวมถึงหยุดทันทีถ้า tracking เสีย, claim ไม่ผ่าน, สิทธิไม่ชัด หรือถึง risk cap; อย่าหยุดเพียงเพราะ early noise ดูดี
- underpowered, delivery ไม่พอ, contamination หรือ tracking เสีย = **inconclusive**; บันทึก interval และข้อจำกัด ไม่ถือว่าไม่มี effect

## ตัวอย่างสมมติ
A และ B ต่างแค่ hook; offer + body + CTA + landing เดียวกัน; กำหนด primary cost/qualified purchase, guardrails และ cap จาก CM2 จริงก่อนเริ่ม หากปรับ offer พร้อม hook ทดสอบ “แพ็กเกจ” ได้ แต่ห้ามสรุปว่า hook เป็นสาเหตุ เมื่อไม่พอสำหรับ A/B ให้ explore อย่างโปร่งใส แล้วนำผลไปวางการทดลองถัดไป
