# E-commerce Operations & Fulfillment · คู่มือปฏิบัติ

## 1. Order-to-delivery map
กำหนด owner ของ order capture → stock reservation → pick/pack → ship → delivery → settlement → return/refund; บันทึก SLA ที่สัญญากับลูกค้า, cut-off, tracking, exception code และต้นทุนราย SKU/ช่องทาง ระบุความแตกต่าง prepaid/COD และอย่าหัก return ทั้งใน net revenue และ provision ซ้ำโดยไม่ reconcile

## 2. Stock และ replenishment
คำนวณ inventory position = on-hand + confirmed inbound − allocated/backorders โดยระบุว่าแต่ละ bucket หมายถึงอะไร; reorder point = demand ต่อวัน × lead time วัน + safety stock [S1] ใช้ข้อมูล demand ที่ไม่ถูก stockout กดต่ำและพิจารณา seasonality, variability, MOQ, expiry และ cash; safety stock ตั้งจากระดับความเสี่ยงของร้าน ไม่ใช้เลขตายตัว

ตัวอย่างสมมติ: demand 10 ชิ้น/วัน, lead time 7 วัน, safety stock 20 ชิ้น → reorder point 90 ชิ้น; หาก inventory position ≤ 90 ให้เสนอ PO ไม่ได้แปลว่าต้องสั่ง 90 ชิ้น ปริมาณสั่งต้องคิดจาก target stock และเงินสด

## 3. Exceptions และ COD
แยก missing/damaged/late/refused/returned; สร้างเหตุผลและขั้นตอนแจ้งลูกค้า; ทำ reconciliation ระหว่าง carrier, settlement และ order status ตรวจ claim-window ในสัญญาจริง; ทดสอบการยืนยัน COD อย่างเคารพข้อมูลและสิทธิ ไม่ถือว่า refusal ทุกกรณีเป็นความผิดลูกค้า

## 4. จังหวะและ stop
รายวันตรวจ inventory position, overdue orders และ carrier exceptions; รายสัปดาห์ forecast + PO + cash; ก่อนโปรโมชันตรวจ stock และ capacity ทั้งระบบ; หยุดแคมเปญหรือแก้ landing เมื่อ stock ไม่พร้อม/คำสัญญาส่งทำไม่ได้ ส่งต้นทุนจริงกลับ Unit Economics และ feedback กลับ CX
