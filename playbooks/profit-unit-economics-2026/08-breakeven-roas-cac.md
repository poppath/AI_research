# 08 · Breakeven ROAS / MER / CAC — สูตรและตารางตัดสินใจ

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> as_of: 2026-11 · market: TH + global · source_type: vendor (eightx, jetfuel, northbeam) + est

บทนี้ตอบคำถามที่ถูกถามบ่อยที่สุดและตอบผิดบ่อยที่สุด: **"ROAS เท่าไหร่ถึงเรียกว่าคุ้ม"**

---

## 1. ทำไม ROAS ที่แพลตฟอร์มรายงานไม่ใช่คำตอบ

| ตัวชี้วัด | สูตร | บอกอะไร | พลาดอะไร |
|---|---|---|---|
| Platform ROAS | platform revenue ÷ platform spend | ประสิทธิภาพ **ภายใน** แพลตฟอร์มเดียว | margin, organic lift, double-counting |
| Blended ROAS | total revenue ÷ total ad spend | ประสิทธิภาพข้ามช่อง | margin |
| **MER** | total revenue ÷ **total marketing spend** (รวม influencer, agency, tool) | ประสิทธิภาพระดับธุรกิจ | margin (ยังเป็น revenue-based) |
| **Breakeven MER** | **1 ÷ CM2% (ก่อนการตลาด)** | เส้นตายที่แท้จริง | ไม่มี — นี่คือพื้น |
| Breakeven ROAS | **net revenue ÷ CM2 (บาท)** | เส้นตายต่อออเดอร์ | ไม่คิด repeat |

**หลักการ:** platform ROAS ใช้ตัดสินใจ **ภายใน** แพลตฟอร์ม (creative A vs B) แต่ใช้ตัดสินใจ **เรื่องงบ** ไม่ได้

---

## 2. Breakeven ROAS และ MER — สูตรและตาราง

### สูตร

```
Breakeven ROAS = Net revenue ต่อออเดอร์ ÷ CM2 ต่อออเดอร์ (บาท)
Breakeven MER  = 1 ÷ CM2% (ก่อนการตลาด)
```

### ตารางตัดสินใจ

| CM2% | Breakeven MER | ตีความ |
|---|---|---|
| 50% | 2.00× | margin หนามาก — scale ได้เต็มที่ |
| 45% | 2.22× | ดี |
| 40% | 2.50× | ดี |
| 35% | 2.86× | ปกติ |
| 30% | 3.33× | เริ่มต้องระวัง |
| 25% | 4.00× | แคบ |
| 20% | 5.00× | แคบมาก — ต้องพึ่ง repeat |
| 15% | 6.67× | อันตราย |
| 10% | 10.00× | เป็นไปไม่ได้ในทางปฏิบัติ |

`[vendor: eightx 2026, jetfuel 2026]`

**Benchmark MER ที่ healthy (DTC global):** 3.0×–5.0× `[vendor: Shopify/Eightx 2026]`
**Triple Whale 2025 median:** marketing spend 41% ของ revenue = MER 2.4× — คือ **ต่ำกว่า breakeven ของหลายธุรกิจ** แปลว่าอุตสาหกรรมโดยรวมกำลังซื้อ revenue มากกว่าทำกำไร

### MER ตามขนาดธุรกิจ (global DTC benchmark)

| Revenue | MER ปกติ | หมายเหตุ |
|---|---|---|
| $1M–$5M | 1.5×–2.5× | ขาดทุนได้ถ้า unit economics ดี |
| $5M–$10M | 2.5×–3.5× | |
| $10M–$25M | 3.0×–4.5× | |
| $25M–$100M | 3.5×–6.0× | |

`[vendor: Eightx 2026 via jetfuel]`

**⚠️ ตัวเลขนี้เป็นของ DTC ตะวันตก** — สำหรับตลาดไทยที่ CM2 ต่ำกว่า (GP สูง, COD, return) MER ที่ต้องการจะ **สูงกว่า** 0.3–0.7×

---

## 3. Breakeven CAC — สูตรที่ใช้จริง

### กรณีขายครั้งเดียว (ไม่มี repeat)

```
Max CAC = CM2 ต่อออเดอร์
```
ตัวอย่าง CM2 = ฿204 → จ่ายค่าแอดได้สูงสุด ฿204/ลูกค้าใหม่

### กรณีมี repeat (สูตรที่ถูกต้อง)

```
Max CAC = CM2 ออเดอร์แรก + (repeat% × CM2 ออเดอร์ 2) + (repeat2% × CM2 ออเดอร์ 3) + ...

หรือแบบย่อ (ใช้บ่อย):
Max CAC = CM2₁ × [1 + (repeat% × (CM2₂/CM2₁))]

นิยมเขียนเป็น:
Max CAC = CM2₁ + (90-day repeat% × CM2₂)
```

**ตัวอย่าง:**

| | ค่า |
|---|---|
| CM2 ออเดอร์แรก | ฿204 |
| CM2 ออเดอร์ที่ 2 (ไม่ต้องจ่าย take rate เท่าเดิม ถ้าย้ายไป LINE) | ฿232 |
| 90-day repeat rate | 22% |
| **Max CAC** | ฿204 + (0.22 × ฿232) = **฿255** |

→ จ่ายค่าแอดได้ถึง ฿255/ลูกค้าใหม่ (ไม่ใช่ ฿204) **ถ้า** repeat rate เป็น 22% จริง

**กับดัก:** ถ้าใช้ตัวเลขนี้แล้ว repeat rate จริงเป็น 10% (ไม่ใช่ 22%) → จ่ายเกินไป ฿26/ลูกค้า → ขาดทุน ฿26 × จำนวนลูกค้าใหม่

### Payback window

ถ้าธุรกิจต้องการคืนทุนภายใน 90 วัน แต่ repeat cycle คือ 120 วัน → **ใช้แค่ CM2₁** ในการตัดสินใจ

| Payback window | ใช้สูตร |
|---|---|
| 0 วัน (ต้องการกำไรทันที) | Max CAC = CM2₁ |
| 30 วัน | Max CAC = CM2₁ + (30-day repeat% × CM2₂) |
| 90 วัน | Max CAC = CM2₁ + (90-day repeat% × CM2₂) |
| 12 เดือน | ใช้ LTV₁₂ (ดูบท 09) |

**ข้อกำหนดขั้นต่ำ:** payback < 90 วันคือมาตรฐานที่ดี `[vendor]` — ถ้าเกิน 120 วัน ต้องมีเหตุผลชัดเจนเรื่องกระแสเงินสด

---

## 4. Target CPA ที่ควรตั้ง (ไม่ใช่ breakeven)

**Breakeven ≠ เป้าหมาย** — ถ้าตั้งเป้าที่ breakeven คุณจะไม่มีกำไรเลย

```
Target CPA = Breakeven CPA × (1 − target profit margin)

ตัวอย่าง:
Breakeven CPA = ฿255
ต้องการกำไร 25% ของ CM2
Target CPA = ฿255 × 0.75 = ฿191
```

**หรือคิดจาก MER:**

```
Target MER = Breakeven MER × 1.20 ถึง 1.35
(คือมี cushion 20–35% เหนือเส้นตาย)
```

ถ้า CM2 = 30% → breakeven MER 3.33 → target MER 4.0–4.5

---

## 5. ตารางตัดสินใจ: ควรเพิ่ม/ลดงบหรือไม่

| สถานการณ์ | ทำอะไร |
|---|---|
| MER > target MER + 25% | เพิ่มงบ 20–30% ต่อสัปดาห์ (รอ ≥7 วันก่อนเพิ่มอีก) |
| MER อยู่ในช่วง target | คงงบ ปรับ creative |
| MER = breakeven | ห้ามเพิ่มงบ — แก้ CM2 หรือ CPA ก่อน |
| MER < breakeven | ลดงบ 30–50% ทันที และวินิจฉัยตามบท 13 |
| MER ดี แต่ CM3 ต่ำ | ปัญหาอยู่ที่ overhead ไม่ใช่การตลาด |
| MER แย่ แต่ platform ROAS ดี | double-counting / organic cannibalization |

**กฎการ scale:** เพิ่มงบไม่เกิน **20–30% ต่อครั้ง** และรออย่างน้อย **7 วัน** ก่อนวัด — การเพิ่มแรงเกินทำให้ CPA พุ่งและระบบ learning เสีย

---

## 6. MER vs Platform ROAS: ทำไมตัวเลขต่างกัน

**สาเหตุที่ platform ROAS สูงกว่า MER จริงเสมอ:**

| สาเหตุ | ผล |
|---|---|
| Double-counting (Meta + TikTok + Shopee claim ออเดอร์เดียวกัน) | platform รวม > จริง 20–40% |
| View-through / engaged-view attribution | ให้เครดิตกับ impression ที่ไม่ได้ทำให้เกิด |
| Organic cannibalization (ลูกค้าซื้ออยู่แล้ว) | attribution ให้ ad ทั้งที่ไม่ได้ทำอะไร |
| Revenue ที่ platform ไม่เห็น (LINE, direct) | MER สูงขึ้น แต่ platform ROAS ไม่รวม |

**วิธีตรวจ:** ถ้า `sum(platform attributed revenue) > actual total revenue` → มี double-counting แน่นอน

**ค่าปกติ:** สัดส่วน platform-attributed revenue ต่อ actual revenue = **110%–145%** ในธุรกิจที่ยิงหลายช่อง

---

## 7. Incrementality: คำถามที่ MER ตอบไม่ได้

MER บอกว่า "การตลาดโดยรวมคุ้มไหม" แต่ไม่บอกว่า **"ถ้าหยุดช่องนี้จะเกิดอะไร"**

**วิธีทดสอบ incrementality ที่ทำได้จริงในไทย (เรียงตามความแม่น/ต้นทุน):**

| วิธี | ความแม่น | ต้นทุน | เวลาที่ใช้ |
|---|---|---|---|
| **Geo holdout** (ปิดแอดใน 3–5 จังหวัด 2–4 สัปดาห์) | สูง | กลาง | 4–6 สัปดาห์ |
| **Time-based holdout** (หยุด 7–14 วัน) | กลาง | ต่ำ | 2–3 สัปดาห์ |
| **Spend-elasticity** (ดู MER ที่ระดับงบต่าง ๆ) | กลาง–ต่ำ | ต่ำ | ต่อเนื่อง |
| **Platform conversion lift study** | กลาง | ต่ำ (แต่ต้องมี scale) | 2–4 สัปดาห์ |
| **Pre/post** (ไม่มี control) | ต่ำ | ต่ำ | — |

**เมื่อไหร่ต้องทำ incrementality test:**
- ก่อนเพิ่มงบเกิน 2 เท่าของปัจจุบัน
- ก่อน decide ว่าจะเลิกช่องทางหนึ่ง
- เมื่อ platform ROAS ดีขึ้นเรื่อย ๆ แต่ยอดรวมไม่โต

**ตัวอย่างผลลัพธ์ที่มักเจอ:** platform ROAS 4.2× แต่ incrementality จริง 1.8× → **เกินครึ่งของยอดที่ platform เคลม มาจาก organic/ลูกค้าเดิม**

---

## 8. Dashboard: 8 ตัวเลขการตลาดที่ต้องดูทุกสัปดาห์

| # | ตัวเลข | สูตร | เกณฑ์ |
|---|---|---|---|
| 1 | Blended MER | revenue ÷ total marketing spend | > breakeven MER + 20% |
| 2 | CM3 % | CM2 − ads, ÷ net revenue | ≥ 22% |
| 3 | CAC รวม | total spend ÷ new customers | < max CAC |
| 4 | CAC แยกช่อง | spend ช่อง ÷ new customers ช่อง | เทียบกันได้ |
| 5 | Payback days | CAC ÷ (CM2/30) | < 90 |
| 6 | New vs returning revenue mix | new rev ÷ total rev | ดู trend ไม่ใช่เป้า |
| 7 | Platform-attributed ÷ actual revenue | | < 130% |
| 8 | Ad spend % of revenue | | ตามหมวด (10–25%) |

---

## 9. Anti-pattern 7 ข้อ

1. **ตั้ง target ROAS จากคู่แข่ง/บทความ** โดยไม่คำนวณจาก CM2 ของตัวเอง
2. **ใช้ platform ROAS ตัดสินใจข้ามช่อง** (Meta vs TikTok vs Shopee) — ใช้ MER หรือ CAC ต่อช่อง
3. **ใช้ breakeven เป็น target** → ไม่มีกำไร
4. **ไม่คิด repeat ใน max CAC** → จ่ายน้อยเกินไป และ scale ไม่ขึ้น
5. **คิด repeat ใน max CAC แต่ repeat ไม่จริง** → จ่ายเกิน ขาดทุนเงียบ
6. **เพิ่มงบทีละ 2 เท่า** → CPA พุ่ง ระบบ learning เสีย
7. **ไม่เคยทดสอบ incrementality** → ไม่รู้ว่าครึ่งหนึ่งของยอดมาจาก organic

---

## 10. สรุป 1 หน้า

- Breakeven ROAS = net revenue ÷ CM2 (บาท) · Breakeven MER = 1 ÷ CM2%
- CM2 30% → breakeven MER 3.33× · CM2 20% → 5.0×
- Max CAC = CM2₁ + (repeat% × CM2₂) — แต่ต้องใช้ payback window ที่ธุรกิจรับได้
- Target CPA = breakeven × (1 − target profit) ไม่ใช่ breakeven
- scale 20–30% ต่อครั้ง รอ ≥7 วัน
- platform ROAS ใช้เลือก creative · MER ใช้ตัดสินงบ · incrementality ใช้ตัดสินว่าจะเลิก/เพิ่มช่อง
- ทำ incrementality test ก่อนเพิ่มงบเกิน 2 เท่า

**อ่านต่อ:** บท 09 — LTV บนฐาน contribution margin และ payback
