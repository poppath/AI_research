# 05 · การวัดผล & Incrementality — วัดอย่างไรไม่ให้หลอกตัวเอง

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> คำเตือนสำคัญ: **ROAS ใน Ads Manager คือ "เครดิต" ไม่ใช่ "กำไร"** เอกสารนี้จะวางระบบวัดผลที่แยกได้ว่า *อะไรเกิดเพราะโฆษณา* และ *อะไรจะเกิดอยู่แล้ว*

---

## 1. ชั้นฐาน: Signal ที่สะอาด (ทำก่อนทุกอย่าง)

### 1.1 Pixel + Conversions API (CAPI)

| องค์ประกอบ | บทบาท |
|---|---|
| **Pixel** (browser) | เก็บ event ฝั่ง client, มี `fbp`/`fbc` |
| **CAPI** (server) | ส่ง event จาก server/bypass ad blocker + iOS |
| **`event_id` ร่วม** | dedup ไม่ให้ purchase ถูกนับซ้ำ |
| **hashed PII** (SHA-256, lowercase+trim) | เพิ่ม match rate: email (+~4 คะแนน), phone (+~3) |
| **`fbp` / `fbc`** | ผูก server event กับ session/click |

**ผลที่คาดหวัง**: match rate จาก ~60–70% (Pixel เดียว) → **85–95%**; EMQ จาก ~3.5–5.0 → **7.5–9.0**
**Recovery**: CAPI กู้ conversion ที่หายได้ราว **15–25%** (บางกรณีถึง 30%) และ Meta อ้างว่า CAPI เพิ่ม attributed conversions ได้ 13–19%

### 1.2 Event Match Quality (EMQ) — KPI อันดับ 1

| คะแนน | ความหมาย | การกระทำ |
|---|---|---|
| 0–4 | แย่ — matching ล้มเหลว | หยุดสเกล, แก้ทันที |
| 4–6 | พอใช้ | เพิ่ม email/phone/fbp/fbc |
| 6–8 | ดี | เป้าหมายขั้นต่ำของทุกบัญชี |
| 8–10 | ดีเยี่ยม | เป้าสำหรับ ecom/lead |

**ตรวจที่**: Events Manager → Data Sources → Overview → Event Match Quality (อัปเดตทุก ~48 ชม.)
**ตรวจทุกสัปดาห์** และ alert ถ้าตกลง > 1.0 คะแนน

### 1.3 Aggregated Event Measurement (AEM)

- ตั้ง **8 events ต่อโดเมน** เรียงความสำคัญ: Purchase → Lead → ATC → InitiateCheckout → ViewContent → …
- ถ้าตั้งผิด ลำดับ event จะถูก prioritize ผิด → optimization เพี้ยน

---

## 2. Event Taxonomy (มาตรฐานที่ควรใช้)

| ขั้น | Event มาตรฐาน | Event เสริม (custom) | ใช้ optimize |
|---|---|---|---|
| เห็น | Impression | — | Reach |
| สนใจ | ViewContent | VideoView75, Save | Traffic |
| พิจารณา | AddToCart | CompareTableOpen | Consideration |
| ตั้งใจ | InitiateCheckout | AddPaymentInfo | Conversion |
| ซื้อ | Purchase (+ value, currency) | FirstPurchase, SubscriptionStart | Sales |
| Lead | Lead | QualifiedLead (CAPI จาก CRM) | Leads |
| แชท | Contact / ConversationStarted | QualifiedConversation | Messaging |

**กติกา**: ชื่อ event ต้องเป็นมาตรฐานเดียวกันทั้งบัญชี (`Purchase` ไม่ใช่ `purchase`, `Buy`, `Order`)
**สำหรับ lead gen**: ส่ง **QualifiedLead** กลับผ่าน CAPI/Offline Conversions จาก CRM — นี่คือการเปลี่ยนเกมคุณภาพ lead

---

## 3. Attribution: อ่านให้ถูก

### 3.1 ค่าเริ่มต้นที่ควรใช้

| ประเภท | Window | ใช้เมื่อ |
|---|---|---|
| Click-through | 7 วัน | ค่าเริ่มต้นสำหรับ ecom/lead |
| View-through | 1 วัน | ค่าเริ่มต้น; อย่าขยายเกิน 1 วัน |
| Value optimization | เปิดเมื่อมีมูลค่าคำสั่งซื้อเพียงพอ | ecom ที่มี AOV ต่างกันมาก |

### 3.2 กับดักที่พบบ่อย

| กับดัก | อาการ | วิธีแก้ |
|---|---|---|
| **Retargeting over-credit** | ROAS 8–15 แต่ lift ~0 | วัดด้วย lift/geo holdout; ลดงบ retargeting |
| **Double counting** | Purchase สูงกว่ายอดจริง | ตรวจ dedup `event_id` + เทียบกับ backend |
| **Modeled conversions** | ตัวเลขเปลี่ยนแม้ไม่แก้อะไร | ดู trend 7 วัน ไม่ใช่วันเดียว |
| **Cross-channel** | Google/Meta เคลมยอดเดียวกัน | ใช้ MER + MMM/geo test |
| **Chat conversions** | click-to-message ดูดี แต่ปิดการขายไม่ได้ | วัด qualified conversation + ปิดการขายจริง |
| **iOS/ATT** | conversion ต่ำลงหลัง opt-out | CAPI + AEM + value events |

---

## 4. Incrementality: คำถามที่ต้องตอบทุกไตรมาส

### 4.1 เครื่องมือและความเหมาะ

| วิธี | ตอบคำถาม | ข้อจำกัด |
|---|---|---|
| **Conversion Lift** (ในตัว Meta) | โฆษณาเพิ่มยอดจริงแค่ไหน | Meta เป็นผู้วัด; ต้องมี volume/EMQ |
| **Geo holdout** | เปิด/ปิดพื้นที่แล้วยอดต่างไหม | ต้องมีพื้นที่พอและตลาดนิ่ง |
| **Pause test** | หยุดแคมเปญ 7–14 วันแล้วยอดหายไหม | รบกวนธุรกิจ; เหมาะแคมเปญเล็ก |
| **Incremental attribution column** | จัดอันดับแคมเปญภายใน Meta | เทียบข้ามแพลตฟอร์มไม่ได้ |
| **MMM** | ภาพรวมทุกช่อง | ต้องมีข้อมูล 1–2 ปี |
| **MER / blended CAC** | ประสิทธิภาพรวม | ไม่แยกชิ้น |

### 4.2 ออกแบบ Lift Test ที่อ่านผลได้

| องค์ประกอบ | ค่าแนะนำ |
|---|---|
| CAPI + EMQ | ≥ 6.0 (เข้มกว่านี้ดี) |
| Conversion ขั้นต่ำ | ~100–500 conversions ในช่วงทดสอบ (ยิ่งมากยิ่งอ่านละเอียด) |
| ระยะเวลา | 2–4 สัปดาห์ |
| Holdout | 10–20% ของ audience |
| งบ | บางกรณี ≥ 50,000 USD สำหรับ user-level study; ถ้าน้อยกว่านั้นใช้ geo-lift |
| เงื่อนไข | อย่าเปลี่ยนครีเอทีฟ/งบกลางการทดสอบ, หลีกเลี่ยงช่วงโปรใหญ่ |

### 4.3 อ่านผลลัพธ์

| Lift | แปลว่า | ทำอะไร |
|---|---|---|
| > 15% | มีผลเชิงสาเหตุชัด | สเกลได้อย่างมั่นใจ |
| 8–15% | สัญญาณดี | คงไว้ + ปรับครีเอทีฟ |
| 3–8% | อ่อน/กำกวม | ตรวจ targeting/offer |
| < 3% หรือลบ | แทบไม่มี incremental | พิจารณาโครงสร้างใหม่/หยุด |

> จำไว้: lift ที่ต่ำใน retargeting เป็นเรื่องปกติ — เพราะคนกลุ่มนั้นมักจะซื้ออยู่แล้ว

---

## 5. ตัวชี้วัดทางธุรกิจ (ไม่ใช่แค่ platform metrics)

### 5.1 สูตรที่ต้องมีใน dashboard

```
MER            = Revenue ทั้งหมด ÷ Ad spend ทั้งหมด
Blended CAC    = (Ad spend + ค่าใช้จ่ายการตลาดอื่น) ÷ จำนวนลูกค้าใหม่
Breakeven ROAS = 1 ÷ Gross margin
iROAS          = Incremental revenue ÷ Ad spend
Contribution   = Revenue − COGS − ค่าใช้จ่ายผันแปร − Ad spend
LTV:CAC        = (AOV × จำนวนซื้อเฉลี่ย × margin) ÷ CAC
Payback period = CAC ÷ (กำไรต่อออเดอร์ × จำนวนออเดอร์/เดือน)
```

**ตัวอย่าง**: margin 40% → breakeven ROAS = 1/0.4 = **2.5**
ถ้า Ads Manager รายงาน ROAS 3.0 แต่ lift บอก incremental จริงแค่ 40% → iROAS = 1.2 → **ขาดทุน**

### 5.2 Dashboard 3 ระดับ

| ระดับ | ตัวชี้วัด | ความถี่ |
|---|---|---|
| **Signal** | EMQ, match rate, dedup rate, event volume | รายวัน (alert) |
| **Delivery** | spend, CPM, CTR, CVR, frequency, learning phase | รายวัน/รายสัปดาห์ |
| **Business** | MER, blended CAC, contribution, LTV:CAC, payback | รายสัปดาห์/รายเดือน |
| **Truth** | lift %, geo result, MMM | รายไตรมาส |

---

## 6. ระบบเก็บข้อมูลเพื่อให้ AI เรียนรู้

AI จะเก่งได้ก็ต่อเมื่อมีข้อมูลที่ **มีโครงสร้าง + มีบริบท + มีผลลัพธ์**

### 6.1 ตารางขั้นต่ำที่ต้องมี

| ตาราง | คอลัมน์หลัก |
|---|---|
| `experiment_log` | id, date, hypothesis, variable, variant, audience, budget, result, decision, owner |
| `creative_registry` | creative_id, concept, persona, awareness, angle, format, hook, launch_date, status |
| `campaign_daily` | date, campaign, adset, ad, spend, impr, clicks, conversions, revenue, freq |
| `business_daily` | date, orders, revenue, new_customers, refunds, COGS |

> `templates/experiment-log.csv` คือจุดเริ่มต้น — อย่าลบ, อย่าเขียนทับ ให้ append เท่านั้น

### 6.2 Data hygiene
- ใช้ naming convention เดียว (`templates/campaign-naming.md`)
- เก็บ UTM ให้ตรงกับชื่อแคมเปญ (เพื่อ join กับ analytics)
- เก็บ currency และ timezone ให้ตรงกัน (THB, Asia/Bangkok)
- ระบุ "data source" ทุกครั้ง (Ads Manager vs backend) เพื่อไม่ให้ AI สับสน

---

## 7. วาระตรวจวัดผลรายสัปดาห์ (15 นาที)

1. **Signal**: EMQ เปลี่ยนไหม? event หยุดไหลไหม?
2. **Delivery**: มี ad set ไหนออกจาก learning phase? frequency เกิน 3 ไหม?
3. **Efficiency**: CPA/ROAS เทียบ 7 วันก่อน + เทียบเป้า
4. **Placement**: Threads/AN กินงบเกิน 15% ไหม?
5. **Creative**: ชิ้นไหน fatigue? ต้อง refresh กี่ชิ้น?
6. **Business**: MER ขยับอย่างไร? เทียบกับเป้ากำไร
7. **บันทึก**: เขียน 3 บรรทัด "เรียนรู้อะไร / จะทำอะไร / ต้องรออะไร"

---

## 8. Checklist ความพร้อมในการวัดผล

- [ ] Pixel + CAPI ทำงาน และ dedup ถูก (ทดสอบด้วย Test Events)
- [ ] EMQ ≥ 6.0 (เป้า 7.5+)
- [ ] AEM ตั้ง 8 events ถูกลำดับ
- [ ] Event taxonomy เป็นมาตรฐานเดียวกันทั้งบัญชี
- [ ] มี QualifiedLead/QualifiedConversation ส่งกลับจาก CRM (ถ้าเป็น lead gen)
- [ ] มี dashboard 3 ระดับ (§5.2)
- [ ] มี experiment log ที่อัปเดตทุกสัปดาห์
- [ ] มี lift หรือ geo test อย่างน้อยไตรมาสละ 1 ครั้ง
- [ ] คำนวณ breakeven ROAS และเตือนทีมเมื่อ ROAS ต่ำกว่านั้น
