# บท 09 · Measurement — LTV ที่ไม่โกหก

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

## TL;DR

- **LTV แบบ blended คือตัวเลขที่ทำให้ตัดสินใจผิดมากที่สุดในธุรกิจ DTC** — เพราะมันเฉลี่ย cohort ที่ดีกับ cohort ที่ขาดทุนเข้าด้วยกัน
- ใช้ **90-day repeat purchase rate แยกตาม acquisition source** เป็นตัวชี้ขาดว่าจะเพิ่มงบช่องทางไหน
- LTV:CAC ที่ healthy = **2.5:1 ถึง 4:1 บน basis ของ contribution margin 12 เดือน** (ไม่ใช่ revenue และไม่ใช่ "ตลอดชีพ")
- **CAC payback < 90 วัน** คือเงื่อนไขการอยู่รอดของ SME ที่มีเงินทุนจำกัด
- ทุกตัวเลขต้อง reconcile กับ **bank statement** ไม่ใช่ platform dashboard

---

## 1 · นิยามที่ต้องตกลงกันก่อน

| คำ | นิยามที่ใช้ใน playbook นี้ |
|---|---|
| **CM (contribution margin)** | รายได้ − COGS − ค่าธรรมเนียม − ค่าขนส่ง − affiliate − ประมาณการคืนสินค้า |
| **LTV** | CM สะสมต่อลูกค้า 1 คนใน 12 เดือน (ไม่ใช่ตลอดชีพ) |
| **CAC** | (ค่า media + ค่าคน + ค่าเครื่องมือ) ÷ จำนวนลูกค้าใหม่ |
| **Payback** | จำนวนเดือนที่ CM สะสม ≥ CAC |
| **Repeat rate** | % ลูกค้าที่ซื้อ ≥2 ครั้งในกรอบเวลาที่กำหนด |
| **MER** | รายได้รวม ÷ ค่า media รวม |

> **ข้อผิดพลาดคลาสสิก:** ใช้ revenue แทน CM → LTV สูงเกินจริง 2–4 เท่า

---

## 2 · สูตร LTV ที่ใช้ได้จริง

### แบบง่าย (ใช้ได้เมื่อมีข้อมูล ≥ 6 เดือน)
```
LTV₁₂ = AOV × purchase_frequency₁₂ × CM% × (1 − return_rate)
```

### แบบ cohort (แม่นกว่า)
```
LTV₁₂ ของ cohort = ผลรวม CM ของ cohort ÷ จำนวนลูกค้าใน cohort
```

### แบบ predictive (ใช้เมื่อมี 12 เดือนขึ้นไป)
```
predictive LTV = (AOV × frequency × CM%) ÷ churn_rate
```

**ตัวอย่างจริง**
```
AOV            ฿890
frequency/12  1.8 ครั้ง
CM%           16.3%
return rate   5%
→ LTV₁₂ = 890 × 1.8 × 0.163 × 0.95 = ฿248
ถ้า CAC = ฿250 → LTV:CAC = 0.99:1  ← ขาดทุน
```
**แปลว่า:** ธุรกิจนี้ต้องเพิ่ม repeat จาก 1.8 → 3.0 ครั้ง หรือลด CAC ลง 40% หรือเพิ่ม CM%

---

## 3 · CAC payback — ตัวเลขที่ทำให้ธุรกิจรอด

```
payback (เดือน) = CAC ÷ (CM ต่อออเดอร์ × ความถี่ต่อเดือน)
ตัวอย่าง: 250 ÷ (145 × 0.15) = 11.5 เดือน   ← ยาวเกินไป
```

| Payback | ตีความ |
|---|---|
| < 30 วัน | ดีมาก — scale ได้ทันที |
| 30–90 วัน | healthy สำหรับ SME |
| 90–180 วัน | ต้องมีเงินทุนหมุนเวียน |
| > 180 วัน | เสี่ยง — ต้องแก้ unit economics ก่อน scale |

---

## 4 · ชุดตัวเลข 12 ตัวที่ต้องดูทุกเดือน

| # | ตัวชี้วัด | สูตร | ทำไมต้องดู |
|---|---|---|---|
| 1 | เพื่อนใหม่ | net new friends | การเติบโตของฐาน |
| 2 | Block rate | block ÷ ส่งถึง | สุขภาพของความสัมพันธ์ |
| 3 | Open rate | เปิด ÷ ส่งถึง | คุณภาพข้อความ |
| 4 | CTR | คลิก ÷ เปิด | ความน่าสนใจของ offer |
| 5 | Revenue จาก LINE | ยอดขายที่ track ได้ | ขนาดของช่องทาง |
| 6 | Revenue แยก flow/broadcast/chat | — | รู้ว่าอะไรทำเงิน |
| 7 | 90-day repeat by source | — | **ตัวชี้ขาดงบ** |
| 8 | Time to 2nd order | ค่าเฉลี่ยวัน | ความเร็วในการคืนทุน |
| 9 | CAC | — | ต้นทุน acquisition |
| 10 | LTV₁₂ : CAC | — | ความยั่งยืน |
| 11 | CM after ads | — | กำไรจริง |
| 12 | MER | รายได้รวม ÷ media | สุขภาพรวม |

---

## 5 · Attribution — ทำอย่างไรให้ไม่หลอกตัวเอง

**ปัญหาพื้นฐาน**
- Platform (TikTok/Meta/LINE) over-credit 30–60%
- LINE conversion ส่วนใหญ่เกิดในแชท → ไม่มี pixel
- ลูกค้าเห็น 4–6 touchpoint ก่อนซื้อ

**วิธีที่ใช้ได้ตามระดับ**
| ระดับงบ | วิธี |
|---|---|
| < ฿300K/เดือน | ใช้ **code/UTM + ถามลูกค้าตอนปิดการขาย** ("รู้จักเราจากไหน") |
| ฿300K–1M | เพิ่ม **source-level cohort** (repeat แยกช่องทาง) |
| > ฿1M | **geo holdout** (ปิด ads บางจังหวัด 2–4 สัปดาห์ เทียบยอด) |

**กฎที่ห้ามละเมิด**
1. ประกาศ window ที่ใช้อ่าน (เช่น 7-day click) แล้วอย่าเปลี่ยนกลางเดือน
2. ตัวเลขที่ใช้ตัดสินงบ = **blended + bank statement** ไม่ใช่ platform ROAS
3. ทุกครั้งที่เพิ่มงบ ตรวจว่า CM after ads ยังบวก

---

## 6 · Dashboard ที่ควรมี (ทำใน Sheets ก็พอ)

```
[สรุปรายเดือน]
spend / revenue / CM / MER / CAC / LTV:CAC / payback

[LINE]
friends · net growth · block rate · open rate · CTR
revenue by: flow · broadcast · chat
RPM ต่อ broadcast

[Segments]
จำนวนต่อ segment · revenue ต่อ segment · block rate ต่อ segment

[Cohort]
ตาราง cohort รายเดือน × เดือนที่ 0–12 (repeat % และ CM สะสม)
```

**ความถี่:** อัปเดตรายสัปดาห์สำหรับ 4 ตัวแรก, รายเดือนสำหรับที่เหลือ

---

## 7 · วิธีตัดสินใจด้วยตัวเลข (ไม่ใช่ความรู้สึก)

**คำถาม:** ควรเพิ่มงบ TikTok หรือเพิ่มงบ LINE?

```
ขั้น 1   CAC ของแต่ละช่อง
ขั้น 2   90-day repeat ของแต่ละช่อง
ขั้น 3   LTV₉₀ = CM₁ + (repeat% × CM₂)
ขั้น 4   เปรียบ LTV₉₀ : CAC
```
ช่องที่ LTV₉₀:CAC สูงกว่า **ควรได้งบมากกว่า** แม้ CPA แพงกว่า

**ตัวอย่าง**
| ช่อง | CAC | repeat 90d | LTV₉₀ | ratio |
|---|---|---|---|---|
| TikTok | ฿250 | 12% | 145 + 0.12×160 = ฿164 | 0.66 ← ขาดทุน |
| LINE (จาก creator) | ฿180 | 34% | 145 + 0.34×160 = ฿199 | 1.11 |
| ลูกค้าเก่า (LINE broadcast) | ฿20 | 55% | 145 + 0.55×160 = ฿233 | **11.6** |

→ คำตอบคือ **ลงทุนใน retention และ creator ที่พา cohort คุณภาพ** ไม่ใช่เพิ่มงบ cold traffic

---

## 8 · ข้อผิดพลาดในการวัดที่พบบ่อย

| ผิด | ถูก |
|---|---|
| ใช้ platform ROAS ตัดสินงบ | ใช้ MER + CM after ads |
| LTV จาก revenue | LTV จาก contribution margin |
| repeat rate ทั้งฐาน | repeat rate แยก source |
| นับยอดขาย LINE ทั้งหมดเป็นผลของ Line Ads | แยก flow / broadcast / chat |
| ไม่หักค่าข้อความ | หักค่าข้อความ + ค่าคน |
| วัด 30 วันแล้วสรุป | ใช้ 90 วันเป็นอย่างน้อย |

---

## กับดักของบทนี้

- ❌ ใช้ blended LTV ที่ถูกปนด้วยลูกค้าเก่า 3 ปี
- ❌ คำนวณ CAC โดยไม่รวมค่าคนและค่าเครื่องมือ
- ❌ ไม่มี cohort table → ไม่เห็นปัญหาจนสาย
- ❌ เปลี่ยน attribution window กลางเดือน
- ❌ ใช้ "LTV ตลอดชีพ" เพื่อ justify CAC สูง
- ❌ วัดเฉพาะรายได้ ไม่วัด block rate

---

## แหล่งอ้างอิง

ดู [`SOURCES.md`](SOURCES.md) — กลุ่ม `retention-benchmarks`, `ltv-metrics`, `attribution`
