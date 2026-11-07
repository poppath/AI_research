# 03 · Google Ads สำหรับบริการ: lead quality และ offline outcomes

## ออกแบบ conversion ก่อนซื้อ traffic
| Stage | คำจำกัดความตัวอย่าง | ใช้เมื่อ |
|---|---|---|
| form submit | ระบบรับข้อมูลสำเร็จ | สัญญาณขั้นต้น; อาจเป็น secondary |
| qualified | ผ่าน criteria พื้นที่/บริการ/ความต้องการ | เมื่อ sales มีนิยามและส่งข้อมูลสม่ำเสมอ |
| appointment held | ลูกค้ามาตามนัดจริง | เมื่อ no-show สูงและ tracking น่าเชื่อถือ |
| won / paid | ปิดสัญญา / รับเงินตามนิยาม | มูลค่าจริงแต่ล่าช้าและ volume อาจต่ำ |

Google Ads primary/secondary มีผลต่อ standard goal bidding; **custom goal สามารถใช้ secondary เพื่อ bidding ได้ด้วย** จึงต้องตรวจ campaign goal configuration จริง [S4]. อย่าใช้ form-submit และ won ของคนเดียวกันเป็น primary พร้อมกันโดยไม่ตั้งใจ เพราะอาจนับหลาย milestone เป็นผลลัพธ์เดียว

## CRM → Ads แบบปลอดภัย
1. ระบุ lead ID, stage, event time/timezone, dedup key, source/consent status, conversion action และ value basis ใน CRM; แยก stage มี owner
2. ตรวจ lawful basis, notice, ความจำเป็น, ข้อกำหนด Google และ data processing/cross-border; hashing ไม่ใช่ anonymization. ไม่ส่ง health data หรือข้อมูลอ่อนไหวไป ads โดยไม่มีการประเมินและสิทธิที่เหมาะสม [S5]
3. เมื่อ eligible ใช้ Google Ads Data Manager / ช่องทางที่ Google รองรับเพื่อนำเข้า offline conversions หรือ enhanced conversions for leads; ตรวจ tag, click identifiers, user-provided data และ matching ตามเอกสารปัจจุบัน [S6]. Google แจ้งการเปลี่ยน API ในปี 2026 และรายละเอียดอาจเปลี่ยน ควรตรวจบัญชีและเอกสารก่อน implement
4. ทดสอบ records ปลอดภัย/มีสิทธิ; ตรวจ diagnostics, timestamps, upload errors, match coverage, dedup และ lag; reconcile aggregate กับ CRM โดยไม่คาดหวัง match 100%
5. เริ่มใช้ stage ที่เชื่อถือได้และ volume เพียงพอ; เมื่อใช้ qualified/won ที่ล่าช้า ต้องติดตาม conversion lag และเปลี่ยน primary goal อย่างมีแผน ไม่ตัดสินจากข้อมูลล่าสุดที่ยังไม่ mature

## Call / LINE
Click-to-call คือ click ไม่ใช่โทรเชื่อมต่อหรือ qualified; call conversion อาจอาศัย forwarding numbers ที่มีเฉพาะประเทศ/บัญชีที่รองรับ [S7]. LINE click ไม่ใช่ lead จนระบบหรือทีมยืนยัน; เก็บ aggregate/CRM ตามความเหมาะสมและสิทธิ ไม่แต่ง attribution ที่เชื่อมไม่ได้

## ตัวอย่างบริการสมมติ
Spend ฿20,000 / 100 leads = CPL ฿200; 40 qualified → ฿500/qualified; 10 won → ฿2,000/won (cohort เดียวกัน mature แล้ว). ถ้า contribution ก่อน media ฿2,500/won เหลือ ฿500 ก่อน fixed costs; ผลเหล่านี้เป็น observed ไม่ใช่ incremental. ตรวจ capacity และความเสี่ยง cancellation ก่อนเพิ่มงบ

หยุด imports เมื่อผิด stage, duplicate หรือไม่มีสิทธิประมวลผล; หยุดการขยายงบเมื่อ tracking/CRM quality ไม่ผ่านหรือ capacity เต็ม
