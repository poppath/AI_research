# 7M AI Content & Affiliate Automation · คู่มือปฏิบัติ

**สถานะ:** research + แผนทดลอง ไม่ใช่ระบบที่สร้างหรือพิสูจน์รายได้แล้ว · ตลาดไทย · ตรวจข้อมูล 7 พ.ย. 2026 · [แหล่ง](SOURCES.md) · [สรุป Docs](https://docs.google.com/document/d/16rr9MfA1V-fCwAvJ0VapX26NLmEVfqFAWr4DziTRHQs/edit) · [Notion](https://app.notion.com/p/7M-AI-Content-Affiliate-Automation-Playbook-2026-TH-41176ada348881a38616dcf86a87e722)

7M ในที่นี้เป็น **กรอบที่เสนอขึ้นสำหรับโจทย์นี้ ไม่ใช่มาตรฐานสากล**: Market, Money, Man, Material, Machine, Method, Measurement โดย governance คร่อมทุก M. GitHub คือฉบับหลัก; Docs/Notion เป็น snapshot สรุป ไม่มี sync อัตโนมัติ

## ข้อสรุปผู้บริหาร
AI ช่วยวิจัย ทำ script ผลิต draft ตรวจ checklist จัดคิว และรายงานได้ แต่คอมเปิด 24 ชม. ไม่ได้หมายถึง passive income: งานสิทธิ ความจริง คุณภาพ การอนุมัติ และการจัดการเหตุขัดข้องต้องมีคนรับผิดชอบ API แต่ละแพลตฟอร์มมีข้อกำหนดเฉพาะ เริ่ม 1 niche, 1 ช่องทาง, 1 รายการต้นทุน แล้วพิสูจน์กำไรหลัง reversal ก่อนขยาย

| แนวคิด | สถานะและวิธีเริ่ม | ข้อจำกัดสำคัญ |
|---|---|---|
| Shopee Video + Affiliate | ทดลอง original video และติดสินค้าผ่าน native flow; AI ช่วยเตรียม draft | ตรวจคุณสมบัติ affiliate และ AI-generated Inform ตาม FAQ; ไม่ยืนยัน API อัปโหลด/ติดสินค้าในบัญชีนี้ [S1,S2] |
| Shopee Affiliate → Facebook | สร้างโพสต์ต้นฉบับพร้อมลิงก์ที่โปรแกรมอนุญาต; Page API อาจใช้ได้เมื่อมีสิทธิ | ตรวจ program, Page token, permissions, app review, disclosure และปลายทางลิงก์ [S1,S6] |
| AI creator หนัง/ซีรีส์/เรื่องเล่า | เรื่องแต่งต้นฉบับหรือใช้เนื้อหาที่ licensed ครบทุกองค์ประกอบและแพลตฟอร์ม | หนัง/เพลง/ภาพนักแสดงต้องมีสิทธิ; เครดิตหรือเปลี่ยนคลิปไม่ให้สิทธิ; การอนุญาตไม่รับประกัน YouTube monetization [S8,S9] |
| TikTok Affiliate | สร้าง draft; คน preview ตรวจและโพสต์/ปักสินค้าผ่าน native flow ที่อนุญาต | Direct Post ต้อง scope, authorization, audit และ explicit consent; guideline ไม่รองรับ internal-only uploader สำหรับบัญชีที่ตนหรือทีมจัดการ; API ปักตะกร้ายังไม่ยืนยัน [S4,S5] |
| ดูดคลิปปั่นช่องขาย | **ไม่แนะนำ**; เปลี่ยนเป็นช่อง original/licensed ที่มีคุณค่า | เสี่ยงละเมิด IP, reused/inauthentic content; การโอน/ขายบัญชีต้องตรวจ ToS และสิทธิแพลตฟอร์มก่อน ไม่สมมติว่าทำได้ [S8,S9] |
| YouTube | upload API มีเอกสาร แต่ต้องตรวจ OAuth/quota/eligibility ก่อนใช้ | ไม่มีหลักฐานรับประกัน monetization; realistic altered content ต้องตรวจ disclosure [S7,S8,S10] |

**ขอบเขตหลักฐาน:** Shopee Original Creator เป็นโปรแกรมเฉพาะ ไม่ใช่กฎเดียวสำหรับครีเอเตอร์ทุกคน [S3]. ข้ออ้างว่า AI label ทำให้เสียคอมทุกประเภทในไทยยังไม่ยืนยัน; ขอคำตอบจาก support พร้อมบันทึกวันที่และบัญชี ก่อนคาดการณ์รายได้. API และเงื่อนไขเปลี่ยนได้ ตรวจใหม่ก่อนใช้งาน.

อ่านต่อ: [7M & workflow](01-7m-workflow.md) · [ปฏิบัติการและ pilot](02-operations-pilot.md) · [แบบฟอร์มและ AI](templates.md) · [metrics](METRICS.md) · [sources](SOURCES.md) · [rules JSON](playbook.json)

## Research ต่อเนื่อง
- [คัดสินค้าและโปรแกรม Affiliate](03-product-program-selection.md): eligibility gate, scorecard และ sensitivity
- [วัดผลและกระทบยอด](04-measurement-reconciliation.md): tracking, pending/approved/paid และ reversal
- [ความน่าเชื่อถือของเนื้อหาและ incident](05-content-risk-operations.md): provenance, disclosure และแผนรับมือ 24 ชั่วโมง

## ภาพรวมกว้างและหัวข้อเจาะลึกเพิ่มเติม
[แผนที่ 12 ด้านและลำดับความสำคัญ](06-broad-research-map.md) → [ผู้ชมและคอนเทนต์](07-content-audience-strategy.md) → [การทดลอง](08-testing-and-learning.md) → [business models และกฎหมายไทย](09-operations-business-model.md) → [agent security](10-agent-security.md)
