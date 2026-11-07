# 02 · Target Audience & การเข้าถึง (Audience Architecture 2026)

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> เป้าหมายของบทนี้: ทำให้คุณ **ตั้งค่า audience ได้อย่างมีเหตุผลภายใต้ระบบที่ AI เป็นคนตัดสิน**, รู้ว่าอะไรคุมได้ อะไรคุมไม่ได้, และมีตาราง audience 12 แบบที่เอาไปใส่ Ads Manager ได้เลย

---

## 1. หลักคิด: "คุมขอบ ปล่อยกลาง"

Meta แบ่งสิ่งที่คุณตั้งใน Advantage+ Audience เป็น 2 ชนิด

| ชนิด | รายการ | พฤติกรรม |
|---|---|---|
| **Control (คุมจริง)** | ประเทศ/พื้นที่, อายุขั้นต่ำ, ภาษา, **exclusion ของ custom audience** | ระบบเคารพเสมอ |
| **Suggestion (คำใบ้)** | ช่วงอายุ/เพศ, detailed targeting (interest/behavior), การใส่ custom audience/lookalike | ระบบใช้เป็นจุดเริ่ม แล้วขยายออกได้ |

ถ้าต้องการให้ suggestion กลายเป็นกำแพงจริง ต้องใช้ตัวเลือก **"Further limit the reach of your ads"** (แล้วปิด "use as suggestion") — แต่ผลข้างเคียงคือ Advantage+ อาจแสดงเป็น "off" และระบบจะเรียนรู้น้อยลง

> **หลักที่ใช้ได้บ่อยที่สุด**: ปล่อย positive targeting ให้กว้าง แล้วใช้ **negative targeting (exclusion)** เป็นเครื่องมือหลักของคุณ

---

## 2. สิ่งที่เปลี่ยนและต้องตรวจในบัญชีเก่า

| เปลี่ยนแปลง | ผลกระทบ | สิ่งที่ต้องทำ |
|---|---|---|
| Detailed targeting **exclusions** ถูกถอด (2025) | ตั้ง "excluding interest X" ไม่ได้แล้ว | ใช้ custom audience exclusion หรือแยก ad set ด้วย original audience options (ถ้าจำเป็นจริง) |
| Interest ที่ถูกยุบ/เลิกใช้ หยุด delivering **15 ม.ค. 2026** | ad set เก่าอาจส่งไม่ได้/ส่งแย่ | ตรวจ ad set ที่ error, เปลี่ยนเป็น兴趣 ใหม่หรือ broad |
| Advantage+ Audience เป็นค่าเริ่มต้น | แม้ตั้ง interest ก็ไม่ใช่กำแพง | อย่าจ่ายเงินเพื่อตั้ง interest 5 ชั้น |
| Threads เป็น default placement (26 ต.ค. 2026) | งบไหลไป Threads อัตโนมัติ | ใช้ placement value rule + ตรวจ report รายสัปดาห์ |
| Placement exclusions ถูกถอด (ส.ค. 2026) | ปิด Threads/AN ไม่ได้เต็มรูปแบบ | ลด bid ได้ถึง 90% ด้วย value rule |

---

## 3. Audience Architecture — 4 ชั้นที่แนะนำ

```
ชั้น A: ACQUISITION BROAD      → 70–80% ของงบ (แคมเปญ Advantage+ / Sales / Leads)
ชั้น B: SIGNAL-SEEDED          → 10–15% (LAL คุณภาพ + interest cluster แบบ suggestion)
ชั้น C: RETARGETING            → 10–15% (แคบ, มี exclusion กันซ้อน)
ชั้น D: TEST SANDBOX           → 5–10% (ทดลอง persona/angle/placement ใหม่)
```

เหตุผล: ชั้น A ให้ระบบเรียนรู้เร็ว (volume สูง) ชั้น B ให้ "ไกด์" เมื่อระบบยังไม่รู้จักสินค้า ชั้น C เก็บคนที่ใกล้ซื้อ ชั้น D กันไม่ให้การทดลองไปรบกวนแคมเปญหลัก

### 3.1 สัดส่วนงบตามระดับรายจ่าย

| งบ/เดือน (THB) | A Broad | B Signal | C Retarget | D Test | หมายเหตุ |
|---|---|---|---|---|---|
| < 30,000 | 70% | 15% | 15% | 0% | ยังไม่ควรมี sandbox แยก — ทดลองใน A |
| 30,000–100,000 | 70% | 15% | 10% | 5% | จุดที่คุ้มที่สุดในการเริ่มระบบ |
| 100,000–300,000 | 75% | 10% | 10% | 5% | เริ่มแยก creative testing cell |
| > 300,000 | 75% | 10% | 10% | 5% | พิจารณา geo-split สำหรับ holdout |

> กติกา: **อย่าให้ชั้น C กินงบเกิน 15%** เว้นแต่ธุรกิจเป็น repeat purchase สูง (เช่น F&B, subscription)

---

## 4. ตาราง Target Audience 12 แบบ (ใช้ได้จริง)

| # | Audience | วิธีสร้าง | ใช้กับ objective | Indication ว่าดี | ข้อควรระวัง |
|---|---|---|---|---|---|
| 1 | **Broad National** | ประเทศ + อายุขั้นต่ำ + ภาษา, ไม่ใส่ interest | Sales, Leads, Traffic | CPM ต่ำ, เรียนรู้เร็ว | ต้องมี creative หลากหลาย ไม่งั้นระบบวนหาคนเดิม |
| 2 | **Broad + Exclusions** | Broad + exclude ผู้ซื้อ 180 วัน + lead 90 วัน | Acquisition | ลดการจ่ายซ้ำ | อย่า exclude ถี่เกินจน reach หด |
| 3 | **Interest Cluster (กว้าง)** | 3–5 interest หมวดเดียวกัน (เช่น ธุรกิจ/เทคโนโลยี) เป็น suggestion | Sales, Leads | ช่วยตอนระบบยังไม่รู้จักสินค้า | ห้ามซ้อน 10+ interest |
| 4 | **Lookalike 1–3% (ยอดขาย)** | source = purchaser 180 วัน (อย่างน้อย 1,000 คน) | Acquisition | CPA ต่ำกว่า broad ในช่วงแรก | source ต้องสะอาด; อัปเดตทุก 90 วัน |
| 5 | **Lookalike 1–3% (LTV สูง)** | source = ลูกค้าซื้อซ้ำ/มูลค่าสูง | Sales (value optimization) | ROAS ดีขึ้น | ต้องมี CRM match |
| 6 | **Video Viewers 75%** | people who watched 75% ของวิดีโอ 30 วัน | Retargeting / Consideration | ถูกและได้คนสนใจจริง | อย่าใช้เป็น acquisition เดี่ยว |
| 7 | **Engagers 365 วัน** | IG/FB engage, save, share | Retargeting | ใช้กับ offer เฉพาะกลุ่ม | frequency ง่ายเกิน |
| 8 | **Website Visitors 30/180 วัน** | Pixel/CAPI | Retargeting | intent สูง | ต้องแยกตาม page depth |
| 9 | **ATC / Initiate Checkout 14 วัน** | event audience | Retargeting ล่าง funnel | conversion สูงสุด | อย่าหวัง incrementality สูง |
| 10 | **Lead Form Openers / Leads** | Instant Form audience | Leads retargeting | ปิดการขายเร็ว | exclude เมื่อปิดแล้ว |
| 11 | **Messenger/WhatsApp Conversationalists** | people who messaged 90 วัน | Click-to-message | ปิดการขายในแชท | ต้องมี SLA ตอบกลับ |
| 12 | **CRM / Offline Matched** | อัปโหลดเบอร์/อีเมล (hashed) | Exclusion + LAL source | แม่นที่สุด | ต้องปฏิบัติตาม PDPA |

### 4.1 ตัวอย่างการตั้งใน Ads Manager (Broad + Exclusions)

```
Campaign: 01_SALES_ASC_TH_Broad_2026Q4
Ad set:  AS01_Broad_TH_Age25+_All_ExBuyer180
  Location:        Thailand (ทั้งหมด)
  Minimum age:     25
  Languages:       Thai (optional — ถ้าสินค้าไทยล้วน)
  Advantage+ audience: ON
  Suggestions:     ไม่ใส่ (หรือ LAL 1% purchaser)
  Exclusions:      CA_Purchaser_180D, CA_Lead_90D
  Placements:      Advantage+ placements + value rule Threads (0.3x)
  Optimize for:    Purchase (value optimization ถ้ามีข้อมูลพอ)
  Budget:          ≥ 50 × target CPA ต่อสัปดาห์
```

---

## 5. Objective → Optimization Event → โครงสร้าง

| Objective | Optimization event ที่แนะนำ | โครงสร้าง | งบขั้นต่ำ/ad set/วัน |
|---|---|---|---|
| Awareness | Reach / Impression | 1 แคมเปญ, 1–2 ad set | 500–1,000 THB |
| Traffic | Landing Page View | 1 แคมเปญ, broad 1 ad set | 500 THB |
| Engagement | Conversation / Post engagement | 1 แคมเปญ + retargeting | 500 THB |
| Leads | Lead (Instant Form) หรือ Qualified Lead (CAPI) | Advantage+ Leads + retargeting | 700–1,500 THB |
| Sales (ecom) | Purchase / Value | Advantage+ Sales + retargeting | 1,500–3,000 THB |
| Sales (high-ticket) | Lead → CRM qualified | Manual + Advantage+ Audience | 1,000–2,000 THB |
| App | App Install / In-app event | Advantage+ App | 700 THB |
| Messaging | Conversation started | Click-to-WhatsApp/Messenger | 500–1,000 THB |

**สูตรงบขั้นต่ำ**: `งบ/วัน ≈ (CPA เป้าหมาย × 50) / 7`
ตัวอย่าง: CPA เป้า 300 THB → 300×50/7 ≈ **2,143 THB/วัน/ad set**
ถ้าทำไม่ได้ → รวม ad set หรือใช้ optimization event ที่ถูกลง (ATC/Lead) เพื่อให้ระบบมี event ให้เรียนรู้

---

## 6. Exclusion Logic (สำคัญที่สุดในปี 2026)

Positive targeting เป็นของ AI — **negative targeting ยังเป็นของมนุษย์**

### 6.1 กติกา exclusion 5 ข้อ

1. **Acquisition ต้อง exclude ผู้ซื้อล่าสุด** (180 วันสำหรับ ecom, 90 วันสำหรับ lead) — ไม่งั้นระบบจะไป retarget คนที่ซื้อแล้วเพราะ conversion ง่าย
2. **Retargeting ต้อง exclude ผู้ซื้อล่าสุด** (30–90 วัน) — กันการจ่ายซ้ำ
3. **Acquisition กับ Retargeting ต้องไม่ทับกัน** — ถ้าทับ ให้ exclude retargeting pool ใน acquisition
4. **อย่า exclude ตาม "ความรู้สึก"** (เช่น ผู้ชาย/ผู้หญิง) — ทุก constraint ที่ไม่จำเป็นคือการตัด signal
5. **ทุก exclusion ต้องมีเหตุผลทางธุรกิจ/กฎหมาย/พื้นที่** ไม่ใช่ "เพื่อความปลอดภัย"

### 6.2 ตาราง exclusion มาตรฐาน

| แคมเปญ | Exclude | เหตุผล |
|---|---|---|
| Acquisition (ecom) | Purchaser 180D | กันจ่ายซ้ำ |
| Acquisition (lead) | Lead 90D, Customer list | กัน lead ซ้ำ |
| Retargeting | Purchaser 30D | กันจ่ายซ้ำ |
| Retargeting | Lead 30D (สำหรับ lead) | กันซ้ำ |
| ทุกแคมเปญ | พื้นที่นอกเขตให้บริการ | ลดการคืนสินค้า/ยกเลิก |
| ทุกแคมเปญ | อายุต่ำกว่าที่กฎหมายกำหนด | ข้อกำหนด Compliance |

---

## 7. Special Ad Category (สำคัญสำหรับไทย)

ถ้าสินค้าเข้าข่าย **ที่อยู่อาศัย / การจ้างงาน / สินเชื่อ-การเงิน / ประเด็นสังคม-การเมือง** Meta จะบังคับ special ad category ซึ่ง:
- ตัดความสามารถในการใช้ อายุ/เพศ/พื้นที่ละเอียด
- จำกัด lookalike
- มีข้อกำหนดด้านข้อความ (ห้ามเลือกปฏิบัติ)
- Advantage+ Detailed Targeting ใช้ไม่ได้

**สิ่งที่ต้องทำ**: ตั้ง category ให้ถูกตั้งแต่สร้างแคมเปญ (เปลี่ยนภายหลังไม่ได้) และให้ทีม legal ตรวจข้อความ

---

## 8. Audience Sizing & Reach ในตลาดไทย (กรอบวางแผน)

จากข้อมูล DataReportal (พ.ย. 2026) — *ตัวเลข reach ของ platform ไม่ใช่ขนาด audience ที่คุณตั้งได้จริง*

| Platform | Ad reach ไทย | % ประชากร |
|---|---|---|
| Facebook | ~50.7 ล้าน | ~70.9% |
| Instagram | ~21.3 ล้าน | ~29.7% |
| TikTok (อ้างอิงเทียบ) | ~70.3 ล้าน (มีบัญชีซ้ำ) | — |
| LINE (MAU) | ~56.3 ล้าน | — |

**การอ่านตัวเลขนี้ให้ถูก**:
- Reach = คนที่ *เห็นแอดได้* ไม่ใช่คนที่ *จะซื้อ*
- Audience ที่ตั้งแคบ (เช่น interest 4 ชั้น + อายุ 30–35 + กรุงเทพ) อาจเหลือ < 200,000 คน → ระบบเรียนรู้น้อย
- กติกา: acquisition audience ควรมีขนาด ≥ 1–2 ล้านคนในไทย (หรือ ≥ 5–10× จำนวน conversion ที่ต้องการ/สัปดาห์)

---

## 9. Audience สำหรับ Reels / Threads / IG (ต่างจาก Feed)

| Placement | พฤติกรรมผู้ชม | วิธีตั้ง audience/creative |
|---|---|---|
| FB Reels | discovery, sound-on, scroll เร็ว | Broad, creative hook 1–2 วิ, 9:16 |
| IG Reels | younger, aesthetic, save/share | Broad + interest แนว lifestyle, creative UGC |
| IG Feed | intent สูงกว่า, อ่านแคปชัน | 4:5 + carousel, copy ละเอียด |
| IG Stories | swipe, sticker, CTA | 9:16 + sticker CTA, offer ชัด |
| Threads | text-first, คุย/แชร์ความเห็น | 4:5 + copy แบบโพสต์, ไม่ขายตรง |
| Messenger/WhatsApp | บทสนทนา | Click-to-message + Business AI |

**หมายเหตุ**: audience ใน Meta แชร์กันข้าม placement — สิ่งที่แตกต่างคือ **creative** และ **placement value rule**

---

## 10. Checklist ก่อนกด Publish (audience)

- [ ] ตั้ง objective ถูก และ optimization event ตรงกับ business outcome
- [ ] ตรวจว่า Advantage+ Audience เปิด/ปิดตามแผน
- [ ] ใส่ hard controls ครบ (พื้นที่, อายุขั้นต่ำ, ภาษา)
- [ ] ใส่ exclusion ตามตาราง §6.2
- [ ] ตรวจขนาด audience (ไม่เล็กกว่า 1–2 ล้าน สำหรับ acquisition)
- [ ] ตั้ง existing customer cap (ASC) = 25–30%
- [ ] ตั้ง placement value rule สำหรับ Threads/Audience Network
- [ ] ตรวจ special ad category
- [ ] บันทึกสมมติฐานลง `templates/experiment-log.csv`
- [ ] ตรวจว่า ad set ใหม่ไม่แย่ง budget กับ ad set เดิม (audience overlap)
