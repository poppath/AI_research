# 07 · Bidding, Budget & Scaling

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> **TL;DR** — งบไม่ใช่แค่ "เงินที่มี" แต่คือ **ตัวกำหนดว่า AI มีข้อมูลพอหรือไม่**. กฎหลัก: งบต่อ ad group ≥10× CPA, conversion campaign ต้องได้ ~50 conversions/7 วัน, scale +20–30% ทุก 3–5 วัน, และ **อย่าลด bid เพื่อแก้ CPA ที่แพง — ให้แก้ creative ก่อน**

---

## 1. งบขั้นต่ำ vs งบที่พอจะเรียนรู้

| ระดับ | platform minimum | งบที่ "พอเรียน" |
|---|---|---|
| Campaign | $50/วัน (ตรวจขั้นต่ำและสกุลเงินในบัญชี) | — |
| Ad group | $20/วัน (ตรวจขั้นต่ำและสกุลเงินในบัญชี) | **≥10× CPA** (practical ≈ $50/วันขึ้นไป) |
| Smart+ Web | ไม่มีขั้นต่ำเฉพาะ | ≥10× historical CPA (ideal 30× ถ้าใช้ target CPA/min ROAS) |
| Smart+ App (Cost Cap) | — | ≥30× target CPA |
| GMV Max | ไม่มีขั้นต่ำ | 2 × historical non-LIVE GMV ÷ ROI target |
| LIVE Shopping (legacy) | — | 40× CPA เป็นงบทั้ง campaign |

**ตัวอย่างคำนวณ:**
```
CPA เป้าหมาย ฿350
→ ad group งบขั้นต่ำที่ควรใช้ = 350 × 10 = ฿3,500/วัน
→ 3 ad groups = ฿10,500/วัน ≈ ฿315,000/เดือน
```
ถ้างบมีแค่ ฿100,000/เดือน → **อย่าแยก 3 ad group** ให้ใช้ 1–2 group ที่งบพอ ไม่งั้นทุก group จะ "learning limited" ตลอด

---

## 2. Bidding strategies — เลือกให้ตรงสถานะ

| Strategy | ทำงานยังไง | ใช้เมื่อ | ห้ามใช้เมื่อ |
|---|---|---|---|
| **Lowest Cost** (Maximum Delivery) | ใช้งบให้ได้ผลมากสุดในราคาที่ถูกที่สุด | ช่วงทดสอบ, ยังไม่รู้ CPA floor | ต้องการคุม CPA แน่นอน |
| **Cost Cap** | พยายามรักษา CPA เฉลี่ย ≤ target | หลังมี data 7+ วัน และรู้ CPA จริง | ตอน learning (จะ under-deliver) |
| **Bid Cap** | จำกัด bid ต่อ auction | CPM-sensitive, top-of-funnel, มี data 30+ วัน | ช่วง learning (จำกัด exploration) |
| **Minimum/Target ROAS** | optimize มูลค่า | margin ต่างกันมาก, มี value parameter ครบ | value ส่งไม่ครบ |
| **Value-Based (VBO)** | optimize ตาม value ของ conversion | e-commerce หลาย SKU | ไม่มี value |

### ลำดับการใช้ที่แนะนำ
```
1. Lowest Cost       → หา CPA floor ตามธรรมชาติ (7-14 วัน)
2. Cost Cap = CPA ที่พบ +10-20%   → เริ่มคุม
3. ค่อย ๆ ลด cap ลง 5-10% ทุก 1-2 สัปดาห์จนถึงเป้า  ← "downward pressure"
4. (ถ้ามีข้อมูลพอ) Minimum ROAS สำหรับ VBO
```

> **กับดัก:** ตั้ง Cost Cap ต่ำกว่าความจริงตั้งแต่วันแรก = ไม่มี spend = ไม่มี data = ไม่มีทางรู้ว่าต่ำไปหรือไม่

---

## 3. Scaling — กฎที่ต้องท่อง

| สถานะ | เงื่อนไขก่อน scale | ขนาดการเพิ่ม | ความถี่ |
|---|---|---|---|
| ยัง learning | ยังไม่ครบ 50 conversions | ≤ +40% ต่อครั้ง | ห่าง ≥2 วัน |
| หลัง learning | ครบ 50 conv/7 วัน + CPA ตามเป้า | +20–30% ต่อครั้ง | ทุก 3–5 วัน |
| Smart+ | stable หลัง day 14 | +20–30% | ทุก 3–5 วัน |
| GMV Max | ROI ตามเป้า 3 วันติด | ~+30% | เมื่อ budget consumption >80% |
| Non-conversion | spend 90-100% ของงบ + cost ≤ target | +20–30% | ทุก 2–3 วัน |

### Vertical vs Horizontal scaling
| วิธี | ทำอะไร | ข้อดี | ข้อเสีย |
|---|---|---|---|
| **Vertical** | เพิ่มงบใน campaign เดิม | ง่าย, รักษา learning | CPA จะค่อย ๆ แพงขึ้นเมื่ออิ่มตัว |
| **Horizontal** | เพิ่ม ad group/campaign ใหม่ (audience ใหม่, creative cluster ใหม่, ภูมิภาคใหม่) | หา pool ใหม่ | fragment, ต้องมีงบพอ |
| **Creative** | เพิ่ม creative ใน group เดิม | ถูกที่สุด, ได้ผลเร็ว | ต้องมี pipeline |
| **Geo** | ขยายต่างจังหวัด/ประเทศ | หา pool ใหม่ | ต้อง localise creative |

**ลำดับที่ถูกเมื่อชนเพดาน:** `creative → horizontal (audience) → geo → vertical`

---

## 4. ตารางตัดสินใจ: งบเท่านี้ ทำอะไรได้

| งบ/เดือน (THB) | ทำอะไรได้จริง | ห้ามทำ |
|---|---|---|
| < ฿50k | 1 campaign, 1–2 ad group, ทดสอบ creative + tracking | อย่าหวัง purchase optimization ถ้า CPA สูง |
| ฿50k–150k | 1–2 campaign, creative testing + early conversion | อย่าแยก 5 ad group |
| ฿150k–500k | creative matrix, Spark Ads, Smart+ เริ่มได้, Shop เริ่มได้ | อย่าเปิดหลาย platform พร้อมกัน |
| ฿500k–1.5M | always-on testing + Smart+ + affiliate + LIVE | อย่าปล่อยให้ creative refresh ขาดคน |
| > ฿1.5M | full funnel, multi-market, incrementality testing | อย่าวัดด้วย platform ROAS |

---

## 5. การจัดสรรงบ (allocation framework)

**สำหรับ D2C / performance ทั่วไป:**
```
70%  proven     — campaign ที่ ROAS ตามเป้าแล้ว
20%  testing    — creative/audience ใหม่
10%  experimental — search, LIVE, ใหม่ ๆ, ภูมิภาคใหม่
```

**สำหรับ Shop (มี LIVE):**
| สถานการณ์ | Product GMV Max | LIVE GMV Max |
|---|---|---|
| ไม่มีไลฟ์ | 100% | 0% |
| ไลฟ์สัปดาห์ละครั้ง | 70–80% | 20–30% |
| ไลฟ์ทุกวัน | 50–60% | 40–50% |

**สำหรับมีทั้ง Shop และเว็บ:**
- แยกบัญชี/แยก campaign ให้ชัด อย่าให้ attribution ชนกัน
- ถ้าเว็บกับ Shop ขายสินค้าเดียวกัน → ต้องทำ **halo measurement** (บท 08) ก่อนตัดสินใจย้ายงบ

---

## 6. Dayparting & flighting

- TikTok ไทย peak: **07:00–09:00, 12:00–13:00, 18:00–20:00, 21:00–23:00** [vendor]
- อย่า daypart ซอยละเอียดเกินไปตอนงบน้อย — จะทำให้ learning ไม่ครบ
- ใช้ dayparting เฉพาะเมื่อ (ก) งบใหญ่พอ (ข) มีข้อมูล hourly conversion ชัด (ค) เป็น LIVE ที่มีเวลาตายตัว
- **Mega sale ไทย**: 6.6 / 7.7 / 8.8 / 9.9 / 10.10 / 11.11 / 12.12 → เพิ่มงบ 1.5–3× ในช่วง 3 วันรอบ event และเตรียม creative + stock ล่วงหน้า 2–3 สัปดาห์

---

## 7. อาการ → สาเหตุ → การสั่งการ (budget/bid)

| อาการ | สาเหตุที่เป็นไปได้ | ทำอะไร (ตามลำดับ) |
|---|---|---|
| ไม่มี spend เลย | bid cap/cost cap ต่ำ, งบต่ำกว่า 10× CPA, audience เล็ก | เปลี่ยน Lowest Cost ชั่วคราว → เพิ่มงบ → ขยาย audience |
| Spend 90-100% แต่ CPA แพง | creative อ่อน หรือเพดาน audience | เพิ่ม creative → ตรวจ frequency → ขยาย pool |
| CPA ดีช่วง 3 วันแรก แล้วแย่ลง | learning จบ, audience อิ่มตัว | เพิ่ม creative + horizontal expansion |
| CPA ขึ้นหลังเพิ่มงบ | ขยายไป pool ที่คุณภาพต่ำลง | ยอมรับ CPA ที่สูงขึ้น 10–20% หรือ scale แบบ horizontal |
| CTR ดี CVR ตก | หน้าเว็บ/product page | อย่าแตะ bid — แก้ LP |
| ROAS ดีแต่กำไรขาดทุน | CM ติดลบ (commission/return/discount) | แก้ offer/margin ไม่ใช่ ads |

---

## 8. กฎ "ห้ามทำ" ด้านงบ

1. ❌ เปลี่ยน bid ทุกวัน
2. ❌ ลดงบเพื่อ "แก้" CPA (มักทำให้แย่ลงเพราะหลุด learning)
3. ❌ เปิด campaign ใหม่ทุกครั้งที่ของเดิมเริ่มแย่ (ให้ refresh creative ก่อน)
4. ❌ ใช้ CBO ตั้งแต่ยังไม่มีข้อมูล
5. ❌ ตั้ง target ROAS สูงกว่าที่ unit economics รับได้ แล้วโทษ TikTok
6. ❌ scale พร้อมกันหลาย campaign ในวันเดียว (อ่านไม่ออกว่าอะไรทำให้เกิดอะไร)

---

## 9. Scaling checklist (ก่อนเพิ่มงบทุกครั้ง)

- [ ] campaign ผ่าน learning แล้ว (≥50 conversions, ≥7 วัน)
- [ ] CPA/ROAS ตามเป้า **3 วันติด**
- [ ] frequency < 2.5–3
- [ ] มี creative ใหม่ ≥5 ชิ้นพร้อมป้อน
- [ ] stock เพียงพอ (สำคัญมาก — ads ดีแต่ของหมด = เผาเงิน)
- [ ] tracking ปกติ (ไม่มี event ตก)
- [ ] เพิ่มทีละ campaign, ทีละ ≤30%
- [ ] บันทึกวันที่และตัวเลขก่อน/หลัง เพื่อวัดผลการ scale

---

## อ้างอิงบทนี้
กลุ่ม `budget`, `bidding`, `scaling`, `thailand` ใน [`SOURCES.md`](SOURCES.md)
