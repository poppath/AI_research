# Executive Summary — Meta Ads × AI (สถานะ พ.ย. 2026)

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

## 1. สิ่งที่เปลี่ยนไปแล้ว (และเปลี่ยนถาวร)

### 1.1 จาก "เลือกคน" → "ป้อนครีเอทีฟให้อัลกอริทึมหาคน"
ระบบ retrieval ของ Meta (**Andromeda**, เปิดใช้ปลายปี 2024) เพิ่มความจุของโมเดลขึ้นหลายเท่าตัว (Meta กล่าวว่า ~10,000×) ทำให้การดึงแอดที่ relevancy สูงสุดจาก inventory มหาศาลทำได้ละเอียดขึ้นมาก

ผลเชิงปฏิบัติ:
- **Detailed targeting กลายเป็น "คำใบ้" ไม่ใช่ "กำแพง"** เมื่อเปิด Advantage+ Audience
- **Detailed targeting exclusions ถูกถอดออก (2025)** → ต้องใช้ custom audience exclusion แทน
- **Interest ที่ Meta ยุบ/เลิกใช้ หยุด delivering 15 ม.ค. 2026** → ad set เก่าที่ค้างค่าเหล่านี้ต้องตรวจ
- ครีเอทีฟที่แตกต่างกันจริง (คนละ persona/angle) ให้ผลดีกว่าการยิง interest ละเอียด 4–5 ชั้นในเกือบทุก vertical

### 1.2 Advantage+ กลายเป็น "ค่าเริ่มต้น" ไม่ใช่ "ตัวเลือก"
- **Advantage+ Sales / Shopping (ASC)**: 1 แคมเปญ, สูงสุด ~150 creative combinations, มี existing-customer budget cap
- **Advantage+ Leads**: ขยายมาแนว lead gen (2025) ใช้ได้ทั้ง Instant Form และ landing page
- **Advantage+ Audience / Creative / Placements**: เปิดเป็น default ในหลาย objective
- **Advantage+ Catalog (ASC+)**: แทน Dynamic Product Ads

### 1.3 Generative AI เข้ามาอยู่ใน Ads Manager
- **GEM (Generative Ad Model)**: สร้าง/ประกอบชิ้นส่วนครีเอทีฟและปรับการRecommendation (Meta อ้าง conversion ดีขึ้นถึง ~5%)
- **Muse / Muse Image**: โมเดลภาพรุ่นใหม่ที่ขับเคลื่อนการสร้างภาพใน Advantage+ Creative
- **11 เครื่องมือจาก Cannes Lions 2025**: brand kit (โลโก้/ฟอนต์/สี), image-to-video (stitch รูปสินค้าได้ถึง 20 รูปเป็นคลิปหลายฉาก), video highlights, AI dubbing/แปลเสียง, Creative Sticker CTA, virtual try-on, Business AI agents ใน Messenger/WhatsApp/IG/FB
- **17 AI enhancements** ใน Advantage+ Creative (image expansion, background generation, text generation, 3D animation, music ฯลฯ) — หลายตัวเปิด default
- **Muse for Small Business** (29 ก.ย. 2026): AI agent แบบ approval-gated ที่เชื่อมต่อ ad account ได้

### 1.4 Placement landscape เปลี่ยน
- **Threads**: ads GA ทั่วโลก (2026) → เป็น **default placement ของทุกแคมเปญ** ตั้งแต่สัปดาห์ 26 ต.ค. 2026
- **Placement exclusions ถูกถอด (ส.ค. 2026)** สำหรับ objective หลัก → ใช้ **placement value rule** (ลด bid ได้ถึง 90%) แทนการปิด
- **WhatsApp ads**: Status ads + Promoted Channels เฉพาะแท็บ Updates (ไม่แตะแชทส่วนตัว)
- **Messenger Stories / IG Explore** ถูกถอดออกจาก API (ต.ค. 2026)
- **Reels** กลายเป็นสัดส่วน impression หลัก (ครึ่งหนึ่งหรือมากกว่าในหลายบัญชี)

## 2. สิ่งที่ยังใช้ได้ (แต่วิธีใช้เปลี่ยน)

| เดิม | ใหม่ |
|---|---|
| Interest stacking เพื่อจำกัดกลุ่ม | 3–5 interest กว้างเป็น suggestion หรือ broad ล้วน |
| Lookalike เป็นพาหนะหลัก | Lookalike เป็น "ตั๋วเข้าคิว" ให้อัลกอริทึมชี้นำ |
| Retargeting ROAS สูง = ดี | ต้องหักด้วย lift test เพราะ retargeting มัก incrementality ต่ำ |
| แยก ad set ละ audience | รวม ad set, ให้ creative diversity ทำหน้าที่แบ่งกลุ่ม |
| ปิด placement ที่ไม่อยากได้ | ใช้ value rule + ตรวจ placement report รายสัปดาห์ |
| รายงาน ROAS อย่างเดียว | MER / blended CAC / iROAS / cohort LTV |

## 3. สิ่งที่ควรเลิกทำทันที

1. **ยิง interest 5–10 ชั้น** ในบัญชีที่ conversions > 50/สัปดาห์ — จำกัดการเรียนรู้ของอัลกอริทึม
2. **ปิด Advantage+ Creative ทั้งหมด** เพราะกลัวภาพเพี้ยน — ให้ปิดเฉพาะตัวที่เสี่ยง (text generation, background generation) และเก็บ image expansion ไว้
3. **วัดผลด้วย ROAS ใน platform เดียว** โดยไม่เคยทำ lift/geo test — เสี่ยง scale สิ่งที่ไม่มีส่วนเพิ่มจริง
4. **ใช้ครีเอทีฟชุดเดียวกับทุก placement** โดยไม่มี 9:16 — จะเสีย inventory Reels/Stories ทั้งหมด
5. **ปล่อยให้ AI เอเจนต์เพิ่มงบเองโดยไม่มีเพดาน** — ต้องมี spend cap + approval
6. **ถือว่า Meta lift report = ความจริงสุดท้าย** — Meta เป็นผู้วัดผล自己的工作; ต้องมี geo holdout หรือ MMM เป็นตัวถ่วง

## 4. โครง 4 ชั้นของระบบ AI ที่แนะนำ

```
[1] INSIGHT        → วิจัยลูกค้า/ตลาด/คู่แข่ง ด้วย LLM + data จริง
        ↓
[2] PRODUCTION     → แปลง insight เป็น concept → hook → สคริปต์ → asset (image/video/voice)
        ↓
[3] ACTIVATION     → โครงสร้างแคมเปญ + audience + placement + bidding (คนคุมขอบ, AI คุมกลาง)
        ↓
[4] LEARNING       → วัดผล → แยก causation → บันทึก experiment log → ปรับ rules
        ↓  (feedback loop กลับไป [1])
```

ชั้นที่ 4 คือชั้นที่คนส่วนใหญ่ข้าม — และเป็นชั้นที่ทำให้ "AI เรียนรู้" ได้จริง

## 5. 80/20 ของงานนี้

ถ้าทำได้แค่ 5 อย่าง ให้ทำสิ่งนี้:

1. **ติด CAPI + ตรวจ EMQ ≥ 6.0** (ถ้าไม่ทำ ที่เหลือเชื่อถือไม่ได้)
2. **ย้ายโครงสร้างเป็น 3 แคมเปญ**: Sales (Advantage+), Consideration/Leads, Retargeting (แคบ)
3. **ผลิตครีเอทีฟ 9:16 อย่างน้อย 10 ชิ้น/ad set** จาก 3 persona × 3 angle
4. **เปิด Advantage+ Audience + broad** และใส่ interest แค่เป็น suggestion 3–5 ตัว
5. **รีวิวสัปดาห์ละครั้งด้วยวาระตายตัว** (ดู `templates/weekly-review.md`) และบันทึกทุกการทดลอง

## 6. ตัวชี้วัดความสำเร็จของ playbook นี้ (90 วัน)

| มิติ | KPI | เป้า |
|---|---|---|
| Signal | EMQ (Purchase/Lead) | ≥ 7.0 |
| โครงสร้าง | % spend ที่อยู่ในแคมเปญที่ผ่าน learning phase | ≥ 70% |
| ครีเอทีฟ | จำนวน concept ใหม่/เดือน | ≥ 12 |
| ครีเอทีฟ | Creative win rate (ชิ้นที่ชนะ benchmark) | ≥ 20% |
| ประสิทธิภาพ | CPA / cost per qualified lead | ลด 10–20% จาก baseline |
| ประสิทธิภาพ | Blended MER | ไม่ลดลงขณะ scale 20% |
| กระบวนการ | % การทดลองที่บันทึกใน log | 100% |
| ความจริง | มี lift/geo test อย่างน้อย | 1 ครั้ง/ไตรมาส |

> หมายเหตุ: ตัวเลขทั้งหมดในเอกสารนี้เป็นกรอบวางแผน ไม่ใช่การรับประกัน ผลจริงขึ้นกับอุตสาหกรรม ราคาประมูล และคุณภาพข้อมูลของแต่ละบัญชี
