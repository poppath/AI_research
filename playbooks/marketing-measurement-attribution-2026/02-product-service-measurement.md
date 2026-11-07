# 02 · Measurement architecture: สินค้า vs บริการ

## ตัดสินใจด้วยข้อมูลที่สอดคล้องกับธุรกิจ
| | สินค้า: direct store / marketplace | บริการ: นัดหมาย / โครงการ / subscription |
|---|---|---|
| หน่วยวิเคราะห์ | unique order + item และ order cohort | unique lead → opportunity → contract → service/invoice |
| milestone ที่นับได้ | order accepted, paid/COD delivered, return, refund | lead รับแล้ว, qualified, appointment held, won, delivered, paid |
| สิ่งลวงที่พบบ่อย | กดจ่ายไม่ใช่ paid; COD สั่งแล้วไม่ใช่ส่งสำเร็จ; GMV ไม่ใช่รายได้สุทธิ | submit ซ้ำ, lead ไม่มีคุณภาพ, นัดแต่ no-show, signed ไม่ใช่เงินรับ |
| source of truth | OMS/payment/settlement; marketplace export เมื่อเข้าถึงได้ | CRM + booking + invoices; ระบบ account/contract สำหรับ B2B |
| ระยะรอ | payment, delivery, return window | qualification, sales cycle, service delivery, cancellations |

ทั้งสองต้องกำหนด primary outcome ก่อนเปิดแคมเปญ; ทำให้บัญชีโฆษณาและ ledger ตรงกันโดยไม่สมมติว่า attribution ครอบคลุมทั้งหมด. Marketplace ที่ไม่ส่ง order ID ระดับบุคคลใช้ aggregate reconciliation, ระบุ coverage และห้ามอนุมาน identity จากข้อมูลไม่พอ

## Event contract — product
| Event / source | เกิดขึ้นเมื่อ | key และข้อควรตรวจ |
|---|---|---|
| `view_item`, `add_to_cart`, `begin_checkout` | ผู้ใช้ทำ action สำเร็จจริง | timestamp, SKU, currency; ไม่ใช้เป็น revenue |
| `purchase` | ธุรกิจนิยามว่า order ผ่านเงื่อนไขสำเร็จ เช่น confirmation หลัง payment หรือ COD accepted | transaction ID เฉพาะออเดอร์ ไม่มีข้อมูลระบุตัวตน; value, currency และ items [S3,S4] |
| delivered / cancelled | OMS หรือ marketplace settlement ยืนยัน | เก็บใน ledger; ไม่จำเป็นต้องเป็น GA event |
| `refund` | อนุมัติคืนเงินเต็ม/บางส่วน | transaction ID เดิม + สินค้า/จำนวนที่คืน; ไม่ลบทั้ง order หากคืนเพียงบางชิ้น [S3] |

กำหนดให้ชัดว่า `purchase` คือ accepted order หรือ paid order หาก COD accepted ให้รายงาน delivered/collected แยก การหัก refund ใน analytics และบัญชีต้องไม่ซ้ำ. GA4 dedup ด้วย transaction ID ที่เอกสารอธิบายเป็น **web streams เท่านั้น**; ไม่ส่ง ID ว่างหรือใช้ ID ซ้ำข้าม order [S4]. ใช้ backend confirmation ไม่ใช่ button click เป็นหลักฐานจ่ายสำเร็จ แม้ตัวอย่าง setup ของ Google บางหน้าจะแสดง button click เพื่อสาธิต tag

## Event contract — service
| Stage | Entry criteria ตัวอย่าง | Timestamp / owner | ไม่เท่ากับ |
|---|---|---|---|
| Lead | ส่งแบบฟอร์มสำเร็จหรือทีมบันทึกการติดต่อ | created_at / CRM | lead คุณภาพ |
| Qualified | ผ่านเกณฑ์ที่ตกลง เช่น พื้นที่/ความต้องการ/บริการที่รับ | qualified_at / sales | นัดจริง |
| Appointment held | มีการนัดและได้รับบริการปรึกษาจริง | held_at / operations | ปิดสัญญา |
| Won | สัญญามีผลตามนิยาม | won_at / sales | รับเงินหรือกำไร |
| Paid / delivered | ชำระหรือให้บริการสำเร็จตามระบบ | paid_at / finance | attribution ที่ถูกต้องทั้งหมด |

เก็บ unique lead ID แยกจาก customer ID และ opportunity ID; หนึ่ง lead อาจมีหลาย opportunity และหนึ่งบริษัทมีหลาย contacts จึงต้องระบุ attribution unit ก่อนนับ; เอกสาร event taxonomy ไม่มีข้อมูลส่วนบุคคล; match กับ CRM ผ่านระบบควบคุมสิทธิ

## Cohort และการ reconcile
1. เลือก lead-created cohort แล้วติดตามทุก stage ใน window ที่กำหนด เช่น 60 วัน (ตัวอย่าง ไม่ใช่ benchmark); ตัด cohort ล่าสุดที่ยังไม่ mature ออกหรือแสดง separately
2. อัตรา qualified = unique qualified leads / eligible unique leads ใน cohort เดียวกัน; win rate อาจใช้ won opportunities / qualified opportunities โดยระบุ unit และ time window ไม่เอา lead หาร opportunity
3. ตรวจ coverage แยก source (website, LINE, โทร, walk-in) และ matching; unknown source คือ unknown ไม่ใช่ organic อัตโนมัติ
4. บัญชี reconcile กับรายได้ paid/recognized ตามนโยบายบัญชี; bookings/contract value อย่าเรียก cash collected และอย่าบันทึกเงินมัดจำซ้ำกับยอดสัญญา

## Privacy และ quality
ก่อนส่ง identifiers ไป third-party ตรวจ purpose, lawful basis, notice, contract, security, retention และ cross-border transfer กับผู้เชี่ยวชาญ; hashing ไม่ทำให้ข้อมูลกลายเป็น anonymous หรือแทนฐานกฎหมาย [S5]. หลีกเลี่ยงข้อมูลสุขภาพ/ข้อมูลอ่อนไหวใน URL, events และ ads; กำหนด test records, access log และวิธีลบ. Analytics ≠ accounting truth และ modeled data ต้องระบุแยก
