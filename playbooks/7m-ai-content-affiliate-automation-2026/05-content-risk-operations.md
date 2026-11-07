# Content trust, incident และ 24h operations

ตลาด TH · research 7 พ.ย. 2026 · [แหล่ง](SOURCES.md). เป็น risk-control ไม่ใช่คำปรึกษากฎหมาย หรือระบบที่ทดสอบแล้ว.

## Content provenance และ claims
ก่อนสร้าง video ให้ content record เชื่อม version ของ brief/script/asset, license/consent, evidence claim, reviewer, disclosure, platform และวันหมดสิทธิ. NIST แนะนำกำหนดเจ้าของ content provenance, monitoring และ incident response [S17]; metadata หรือ AI watermark ไม่ได้พิสูจน์ว่า asset มีสิทธิ. เก็บหลักฐานการใช้จริงถ้าจะบอกว่าใช้เอง; AI ห้ามสร้าง testimonial หรือรีวิวของคนไม่มีตัวตน [S18 เป็นกฎ US ไม่ใช่ข้อสรุปกฎหมายไทย]. ใช้ข้อความเปิดเผยที่คนเข้าใจ เช่น “ลิงก์นี้เป็น affiliate หากซื้อผ่านลิงก์เราอาจได้รับค่าคอมมิชชัน” พร้อมตรวจรูปแบบของ platform/กฎหมายที่เกี่ยวข้อง; แนวทาง FTC สำหรับสหรัฐแนะนำ disclosure ใน video และใกล้ลิงก์ [S19].

## แผนปฏิบัติการและ incident
| เหตุ | ผลกระทบ | การตอบสนอง |
|---|---|---|
| claim หรือ license ไม่ชัด/หมดอายุ | ความเสี่ยงต่อผู้ชมและ IP | quarantine draft/หยุด publish; owner ตรวจหลักฐานและแก้/นำออกตามขั้นตอน |
| API ตอบ spam risk หรือบัญชีถูกจำกัด | เสี่ยงฝ่าฝืน | หยุด automation, บันทึกรหัส, ทบทวนกับ platform; TikTok ระบุ spam_risk ไม่ให้ retry [S20] |
| publish timeout | อาจซ้ำ | สถานะ unknown; เช็ค publish ID/status หรือหน้า platform ก่อน retry; อาจมี moderation delay [S20] |
| token รั่ว | สิทธิถูกใช้โดยผู้อื่น | pause, revoke/rotate, จำกัดสิทธิ, ตรวจ logs และแจ้งตามกฎหมาย/ข้อกำหนด |
| model/provider ล่ม หรือ cap เกิน | backlog/ต้นทุน | หยุดงานที่เสียเงินและ publish; แจ้งเจ้าของ, กลับไป manual เมื่อปลอดภัย |

TikTok Upload API เป็น flow ส่ง draft ให้ creator ดำเนินต่อผ่าน inbox ไม่ใช่ publish อัตโนมัติ; Direct Post ต่างหากและอยู่ภายใต้ intended use, scope, audit และ consent [S4,S5,S21]. เมื่อไม่มี owner ตอบ alert อย่าเปิดระบบ publish unattended. เวลาทบทวนและ cap กำหนดตามทีมจริง; log incident, owner, impact, timeline, corrective action และ approval ก่อน restart.

## Test ก่อนเปิดจริง
จำลอง (1) claim ไม่มีแหล่ง (2) license หมด (3) cap ถึง (4) timeout ที่เกิดหลัง platform รับโพสต์ (5) credential ถูกถอน (6) moderation pending (7) payout ถูก reverse. ผลที่ต้องการคือ stop/reconcile/alert ไม่ใช่ retry อย่างไม่จำกัด. ทดสอบเฉพาะบัญชีและ API ที่ได้รับอนุญาต; ไม่มีการทดลองจริงใน research นี้.
