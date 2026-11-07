# Conversion Rate Optimization & Landing Pages · คู่มือปฏิบัติ

## 1. เริ่มจาก funnel ไม่ใช่ความชอบของทีม
แยกตาม device, channel, landing และสินค้า: landing sessions → product views → add to cart → begin checkout → paid order; ใช้ session หรือ user เป็นหน่วยให้คงที่ และเช็ก event ที่หาย/ซ้ำก่อนตีความ Marketplace ที่แก้ checkout เองไม่ได้ให้วิเคราะห์หน้าสินค้า ราคา แชต และข้อจำกัดของแพลตฟอร์มแทน

## 2. หา friction ด้วยหลักฐาน
ทำ usability test ให้ผู้เข้าร่วมทำภารกิจจริงโดยไม่ชี้นำ; ตรวจ mobile, ความเร็วที่วัดจากผู้ใช้จริง, ราคา/ค่าส่ง/ระยะส่ง, ทางเลือกชำระ, ความน่าเชื่อถือ, size และ return policy บนหน้าสินค้า ตรวจ error recovery และแสดงยอดรวมก่อนตัดสินใจ [S1,S2]. ไม่ใช่ทุก cart abandonment เป็นปัญหา checkout: บางคนยังแค่เปรียบเทียบ [S1]

## 3. เลือก hypothesis และทำ test
ตัวอย่างสมมติ: “แสดงยอดรวมและค่าจัดส่งก่อน checkout ช่วยลดความไม่แน่ใจ”; A ปัจจุบัน B เปลี่ยนข้อความ/ตำแหน่งเดียวกัน; primary = paid orders / eligible randomized users; guardrails = CM3 ต่อ order และ refunds; ตั้ง MDE, sample size, duration, exposure integrity และ cap ก่อนเริ่ม หาก traffic ไม่พอ ใช้ qualitative test เพื่อหาข้อบกพร่องและระบุว่าไม่ใช่การพิสูจน์ uplift

## 4. Launch + stop
QA checkout หลายอุปกรณ์และ payment ที่เกี่ยวข้อง; หยุดทันทีเมื่อ payment ผิด, สินค้า/ราคาไม่ตรง, privacy หรือ tracking ล้มเหลว; รายงานผลพร้อม interval และการเปลี่ยนแปลงระหว่างทดลอง; ไม่เทียบ click กับ purchase คนละ denominator. ส่งเหตุผลที่ลูกค้าติดขัดกลับ research/creative และส่ง order มูลค่าสุทธิไป measurement
