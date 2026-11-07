# 02 · Product CRO: จากโฆษณาถึงการซื้อและคืนสินค้า

## Funnel และ scope
วิเคราะห์ product/variant + device + source + ใหม่/เดิม: landing → view_item → add_to_cart → checkout → accepted/paid → delivered → retained after return; ใช้ unique users หรือ sessions ให้คงที่; การดู event count อย่างเดียวอาจนับซ้ำ. marketplace จำกัดการแก้ checkout ให้โฟกัส listing, product info, ราคา, fulfillment promise และ chat ที่ร้านควบคุม

## Research → friction → change
| หลักฐาน | hypothesis | สิ่งที่ทดลอง |
|---|---|---|
| ผู้ร่วมทดสอบไม่เข้าใจขนาด | size uncertainty ขัดขวางซื้อ | size chart + วิธีวัดที่ตรวจสอบได้ |
| ค่าส่งเห็นช้า | total cost surprise | แจ้งค่าจัดส่งหรือเงื่อนไขประมาณการแต่ต้น |
| สินค้าไม่ตรงภาพ | expectation mismatch ทำให้คืน | รูปสินค้า/สี/รายละเอียดจริงจาก asset ที่ได้รับสิทธิ |
| checkout error | form validation ใช้งานยาก | error message ใกล้ field และรักษาข้อมูลที่ไม่อ่อนไหว |

Baymard ศึกษา checkout ต่างประเทศ ไม่ใช่ค่า benchmark ไทย [S1]. usability interview ใช้หาเหตุ ไม่ยืนยัน uplift; ทำ A/B เมื่อออกแบบได้และ sample เพียงพอ

## ตัวอย่าง A/B (สมมติ)
A = PDP เดิม, B = ขนาดชัดขึ้น โดยราคา/ส่ง/CTA ไม่เปลี่ยน; randomize user และคง variant ตลอดการทดลอง; primary = paid orders / randomized eligible users; guardrails = return rate ใน cohort, contribution/order, complaint. กำหนด MDE/power/sample และช่วง refund ก่อนเริ่ม; ถ้าจบก่อน return mature รายงานเป็น preliminary. Sample ต่ำหรือ variant leakage → inconclusive ไม่บอกว่าขนาดเป็นสาเหตุ

## QA ก่อนปล่อย
- สินค้าตรงภาพ variant, ราคา + ค่าส่ง + ระยะส่ง + return policy ชัดและไม่บิดเบือน
- ตรวจ mobile/desktop, keyboard/screen reader, payment, error และ stock จริง
- Tag: event fired once หลัง action จริง, unique non-PII order ID, refund mapping; ตรวจ data กับ OMS
- หยุดทันทีถ้า checkout fail, ราคา/stock ผิด, privacy รั่ว หรือถึง risk cap; บันทึก rollback owner
