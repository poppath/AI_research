# Marketing Measurement & Attribution · คู่มือปฏิบัติ

## 1. ตั้ง measurement contract
กำหนด decision, owner, ช่องทาง, market, SKU, ช่วงเวลา, timezone, currency, gross/net และ conversion lag ให้ตรงกันก่อนเปรียบเทียบ; บันทึก objective และ attribution window ของแต่ละ platform ระบุแยก new/repeat และยกเลิก/คืนสินค้า; ห้ามนำ platform-attributed conversions มาบวกเป็นยอดลูกค้าจริงเพราะอาจนับซ้ำ

## 2. สร้าง single order ledger
ใช้ order ID ที่ไม่ใช่ข้อมูลส่วนบุคคลเป็น key; เก็บ order date, channel, SKU, gross, seller discount, net revenue, fees, fulfilment, returns, status และ ad spend ในช่วงที่กำหนด; ตรวจ duplicates, late events และการ reconcile กับบัญชี/settlement ทุกสัปดาห์ โดยแยก provisional กับ finalized ห้ามแชร์ identifier ตรงโดยไม่จำเป็น ตรวจ PDPA และเงื่อนไขการส่งข้อมูลกับผู้เชี่ยวชาญ

## 3. แยก 3 มุมมอง
- **Platform attribution:** ใช้ optimize ภายในแพลตฟอร์ม ภายใต้ attribution window ของมัน ไม่ใช่ causal effect
- **Blended:** MER = net revenue / total ad spend ในช่วงที่กำหนด; บันทึกว่ารายได้รวมช่องทางใดและคืนสินค้าปรับเมื่อไร; MER ไม่ได้บอกว่าโฆษณาก่อรายได้ทั้งหมด
- **Incrementality:** randomized holdout หรือ geo test หากเป็นไปได้; ระบุ treatment/control, หน่วยสุ่ม, outcome และช่วงติดตาม กรณีขนาดกลุ่มไม่เท่ากันต้องเทียบอัตราแล้วปรับขนาด ไม่ลบยอดดิบตรง ๆ [S1,S2]

## 4. ตัวอย่างทดลอง (สมมติ)
กลุ่มสุ่ม A และ B ขนาดเท่ากัน; A ได้รับสิทธิ์เห็นโฆษณา B เป็น holdout; กำหนด primary outcome ยอดซื้อสุทธิต่อ eligible user, guardrail contribution และ complaint, วันที่ปิด, sample/power/MDE และ cap ก่อนเริ่ม รายงาน effect พร้อม confidence interval; หาก contamination, stockout หรือ sample ไม่พอให้รายงาน inconclusive ไม่ใช่ zero effect. Lift tool ของ Google อาจไม่พร้อมให้ทุกบัญชี [S1]; geo test ต้องคุม spillover และความต่างพื้นที่ [S2]

## 5. ตัดสินใจ
หาก tracking เสีย → หยุด test; หากผลไม่ชัด → เก็บเพิ่มหรือปรับ design แทนการประกาศ winner; หาก incremental contribution คุ้มและ supply รองรับ → เสนอเพิ่มงบแบบมี cap และ review; หากข้อมูลไม่พอใช้ decision ภายใต้ uncertainty พร้อม owner
