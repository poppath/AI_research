# 7M และ workflow

## 1 Market
เลือก niche ที่เข้าใจและมี buyer intent; ระบุ persona, pain, สินค้าหรือบริการ, เหตุผลเชื่อ, ข้อจำกัด claims, ช่องทาง, eligibility และกลุ่มเปรียบเทียบ. สินค้าดู demonstrations/returns; บริการตรวจคุณสมบัติผู้ให้บริการ availability และข้อจำกัดผลลัพธ์. เก็บหลักฐานราคาปัจจุบัน ไม่สร้างประสบการณ์ใช้เองปลอม.

## 2 Money
ตั้งงบเพดานและ owner ก่อนเริ่ม. รายได้ affiliate = commission **approved** หลัง reversal; paid เป็น cash ไม่ใช่ pending. Contribution = approved commission − ค่าแรง − AI/software − ค่าไฟ/เน็ต − ค่าโฆษณา − ค่าใช้จ่ายผันแปรอื่น; คิดค่าเสื่อมและภาษีแยก. ไม่สับสนกับ GMV.

ตัวอย่างสมมติ TH, พ.ย. 2026 ไม่ใช่ benchmark: 100 approved orders × ฿25 = ฿2,500; แรงงาน ฿1,200 + เครื่องมือ ฿500 + ไฟ ฿200 + ads ฿400 = ฿2,300; contribution ฿200 ก่อนค่าเสื่อม/ภาษี. หากคอมต่อออเดอร์เหลือ ฿20 รายได้ ฿2,000 และขาดทุน ฿300. จุดคุ้มทุน = ฿2,300 / ฿25 = 92 approved orders (สมมติคอมและต้นทุนคงที่). ค่าไฟ = kW เฉลี่ย × ชั่วโมง × ค่าไฟจริง; วัด watt meter และบิล ไม่ใช้ตัวอย่างเป็นราคาไฟ.

## 3 Man
มอบหมาย owner สำหรับ research, creative, rights/claims, publisher, finance/measurement, incident และ backup. คนเดียวถือหลายบทบาทได้ แต่ต้องมี named approver; AI ไม่ใช่ผู้รับผิดชอบตามกฎหมาย. กำหนดเวลาตอบ alert และ on-call ไม่สัญญาว่ามนุษย์พร้อม 24 ชม.

## 4 Material
บันทึก asset ID, ที่มา, ผู้ให้สิทธิ, ขอบเขต commercial use, derivative, platforms, territory, duration, proof และ expiry. ตรวจภาพ เพลง voice ลิขสิทธิ์บุคคลและเครื่องหมายการค้า. Claims มีแหล่ง หลักฐาน วันที่ ข้อจำกัด และ reviewer; ไม่สร้าง review ปลอมหรือสรรพคุณเกินจริง. เปิดเผย affiliate ให้เด่นใกล้คำแนะนำและในวิดีโอเมื่อเหมาะสม ตรวจเครื่องมือ branded/commercial disclosure ตาม platform [S11,S12]; FTC เป็นแหล่ง US ไม่ใช่กฎหมายไทย. ตรวจ PDPA ตามบริบทและลด PII [S13].

## 5 Machine
สถาปัตยกรรม: scheduler → queue → research/script → asset/license check → render draft → human review/preview → platform-specific adapter หรือ manual native publish → log/reconcile → metrics. AI ใช้ sandbox และ least privilege; credentials ผ่าน secret store ไม่อยู่ใน Git/log. ใช้ job idempotency key = campaign + content version + target; append-only audit, timeout, capped backoff, dead-letter queue, budget cap, backup และ kill switch. หาก publish timeout สถานะไม่ทราบ ให้ query/reconcile กับ platform ก่อน retry; ห้ามเดา success หรือส่งซ้ำ. ห้าม browser automation ที่ฝ่าฝืน ToS หรือ bypass captcha/rate limits. งาน 24 ชม. คือ queue/render/monitor เท่านั้น ไม่ใช่สิทธิ post unattended ทุก platform.

## 6 Method
1. Intake: niche, audience, market, cap, approved platform และ owner.
2. Eligibility: ตรวจ ToS, affiliate rates, API scopes/audit, consent, tags/labels และวิธีปักสินค้าในบัญชีจริง.
3. Evidence: verify product, claim และสิทธิทุก asset; เก็บวันที่/หลักฐาน.
4. Draft: 2–3 concepts ตาม capacity, script, captions, disclosure, evidence references และ cost estimate; AI ห้ามแต่งหลักฐาน.
5. QA: คนตรวจภาพ/เสียง/claim/link/สิทธิ/AI label, ดู preview และอนุมัติ version ที่แน่นอน. TikTok ให้ creator ยินยอมตาม flow ที่แพลตฟอร์มกำหนด ไม่ใช่ blanket approval แทนการยืนยัน.
6. Publish: native หรือ API ที่อนุญาตจริง; บันทึก post ID และ approval. ห้ามตั้ง scheduled Direct Post โดยสมมติว่าผ่านนโยบาย.
7. Reconcile: ตรวจโพสต์, status, orders, reversals, payout, costs, incidents; รายงานตาม cohort และ window.
8. Learn: ทบทวนคุณภาพ กำไร และความเสี่ยงก่อนขยาย; เก็บ decision log.

## 7 Measurement
ดู [METRICS](METRICS.md). ติดตาม post ID → link/product → clicks → orders → pending → approved → paid พร้อม refunds, cost และเวลา. นับ conversion ตาม attribution ของโปรแกรม ไม่อ้าง causal incrementality จาก last-click. ข้อมูล affiliate ไม่เปิด event ระดับผู้ใช้ก็วัด aggregate และระบุข้อจำกัด.
