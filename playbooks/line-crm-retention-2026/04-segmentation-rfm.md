# บท 04 · Segmentation & RFM — แบ่งกลุ่มก่อนส่ง

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

## TL;DR

- **ไม่มี segmentation = ไม่มี CRM** การส่งข้อความเดียวกันถึงทุกคนคือการจ่ายเงินเพื่อรบกวนคนส่วนใหญ่
- RFM ทำได้ด้วย **SQL query เดียว** (`NTILE(5)` สามครั้ง) ไม่ต้อง ML — ได้ 11 segment พร้อม action ทันที
- ลำดับความสำคัญของ segment ไม่เท่ากัน: **Champions + At Risk + Can't Lose Them** = 10–25% ของฐาน แต่สร้าง 45–65% ของรายได้ `[vendor]`
- ทุก segment ต้องมี **ความถี่สูงสุด (cap)** และ **ข้อความที่ต่างกัน** — ถ้าเหมือนกันหมดก็ไม่ใช่ segmentation
- **Recency เป็นตัวทำนายที่ดีที่สุด** สำหรับการซื้อครั้งถัดไป แต่ F+M เป็นตัวบอกว่าควรลงทุนแค่ไหน

---

## 1 · ทำไมต้อง RFM ก่อน ML

| วิธี | ข้อมูลที่ต้องมี | เวลาทำ | เหมาะกับ |
|---|---|---|---|
| **RFM (quintile)** | ตาราง orders เท่านั้น | 1–2 วัน | ทุกธุรกิจ ← เริ่มที่นี่ |
| Behavioral | event tracking (view, cart, click) | 2–4 สัปดาห์ | มีเว็บ/app |
| Predictive (churn/propensity) | unified profile + data science | 2–3 เดือน | งบ > $50K/เดือน |

**เหตุผล:** RFM ให้ผล 80% ด้วยความพยายาม 5% — และอธิบายให้ทีมขายเข้าใจได้ทันที

---

## 2 · RFM Implementation (ทำได้จริงใน 1 วัน)

### ขั้น 1 — เตรียมตาราง orders
ต้องมี: `customer_id` · `order_date` · `order_value` · (ถ้ามี) `order_margin`

> **ใช้ margin ไม่ใช่ revenue** ถ้าทำได้ — เพราะลูกค้าที่ซื้อของลดเยอะไม่ควรได้คะแนน M สูง

### ขั้น 2 — คำนวณ RFM

```sql
WITH customer_rfm AS (
  SELECT
    customer_id,
    DATEDIFF('day', MAX(order_date), CURRENT_DATE)      AS recency_days,
    COUNT(DISTINCT order_id)                            AS frequency,
    SUM(order_value)                                    AS monetary
  FROM orders
  WHERE order_date >= CURRENT_DATE - INTERVAL '12 months'
  GROUP BY customer_id
),
scored AS (
  SELECT
    *,
    NTILE(5) OVER (ORDER BY recency_days ASC)  AS r_score,  -- วันน้อย = คะแนนสูง
    NTILE(5) OVER (ORDER BY frequency DESC)    AS f_score,
    NTILE(5) OVER (ORDER BY monetary DESC)     AS m_score
  FROM customer_rfm
)
SELECT *, CONCAT(r_score,'-',f_score,'-',m_score) AS rfm
FROM scored;
```

> **ข้อควรระวัง:** `NTILE` บังคับให้แบ่ง 20/20/20/20/20 เสมอ ทำให้ธุรกิจที่ลูกค้าส่วนใหญ่ซื้อครั้งเดียวได้ "Champions" ที่จริง ๆ แล้วไม่ใช่ champion → ใช้ **fixed threshold** แทนเมื่อฐานเล็กหรือ distribution เบ้มาก

### ขั้น 3 — Fixed threshold (แนะนำสำหรับฐาน < 10,000)

| คะแนน | R (วัน) | F (ครั้ง/12 เดือน) | M (บาท/12 เดือน) |
|---|---|---|---|
| 5 | ≤ 7 | ≥ 5 | ≥ 5,000 |
| 4 | 8–30 | 4 | 3,000–4,999 |
| 3 | 31–90 | 3 | 1,500–2,999 |
| 2 | 91–180 | 2 | 500–1,499 |
| 1 | > 180 | 1 | < 500 |

> ปรับตัวเลขตามรอบซื้อจริง — สินค้า replenishment 30 วันใช้เกณฑ์ R เข้มกว่านี้ได้ สินค้าคงทนต้องผ่อน

---

## 3 · Action Map — 11 segment

| Segment | R | F+M | สัดส่วนฐาน | สัดส่วนรายได้ | เป้าหมาย | การกระทำ | Cap |
|---|---|---|---|---|---|---|---|
| **Champions** | 4–5 | 4–5 | 10–15% | 35–45% | รักษา | VIP tier, early access, upsell พรีเมียม, ขอ referral | 2–3/สัปดาห์ |
| **Loyal** | 3–5 | 3–4 | 10–15% | 15–25% | เพิ่มความถี่ | cross-sell, replenishment, ชวนรีวิว | 2/สัปดาห์ |
| **Potential Loyalist** | 4–5 | 2–3 | 8–12% | 8–12% | ปั้นเป็น loyal | onboarding series, education, bundle | 2/สัปดาห์ |
| **Recent / New** | 4–5 | 0–1 | 5–10% | 2–5% | ผลักออเดอร์ 2 | welcome flow, incentive ครั้งที่ 2, social proof | 2/สัปดาห์ |
| **Promising** | 3–4 | 1 | 4–8% | 1–3% | สร้าง engagement | browse-abandon, incentive เบา, content | 1–2/สัปดาห์ |
| **Needing Attention** | 2–3 | 2–3 | 6–10% | 5–8% | กระตุ้นใหม่ | limited-time offer, restock alert | 1–2/สัปดาห์ |
| **About to Sleep** | 2–3 | 0–2 | 5–9% | 2–4% | ดึงกลับก่อนหลับ | win-back teaser, สินค้าขายดี | 1/สัปดาห์ |
| **At Risk** | 0–2 | 2–5 | 6–10% | 8–14% | ป้องกัน churn | multi-touch win-back, incentive escalate | 1/สัปดาห์ |
| **Can't Lose Them** | 0–1 | 4–5 | 1–3% | 5–12% | กู้ high-LTV | คนคุยตรง, ข้อเสนอเฉพาะ, account manager | ตามกรณี |
| **Hibernating** | 1–2 | 1–2 | 8–14% | 1–3% | ลองครั้งสุดท้าย | ข้อเสนอเดียวทรงพลัง แล้วลดความถี่ | เดือนละครั้ง |
| **Lost** | 0–1 | 0–1 | 12–20% | <1% | suppress | ทักครั้งเดียว แล้วไม่ส่งอีก | ไตรมาสละครั้ง |

**ข้อสังเกตสำคัญ:** ฐานส่วนใหญ่ (30–40%) อยู่ใน 3 segment ล่างสุดที่สร้างรายได้ <5% → **การลดการส่งถึงกลุ่มนี้คือการประหยัดเงินจริง**

---

## 4 · Segmentation layer ที่เหนือกว่า RFM

RFM บอก "คุ้มไหม" แต่ไม่บอก "ควรพูดอะไร" → ต้องซ้อนอีก 2 ชั้น

### ชั้นที่ 2 — Category / interest
```
it_serum, it_sunscreen, it_haircare  ← จาก rich menu, keyword, ประวัติซื้อ
```
ใช้เลือก **สินค้าที่จะเสนอ** ไม่ใช่เลือกว่าจะส่งหรือไม่ส่ง

### ชั้นที่ 3 — Lifecycle stage
```
st_new → st_first_buyer → st_repeat → st_loyal → st_lapsed
```
ใช้เลือก **ข้อความ** (ต้อนรับ / เตือนใช้ซ้ำ / ขอบคุณ / ดึงกลับ)

**Matrix ที่ใช้จริง:**
```
        new      first    repeat   loyal    lapsed
serum   [edu]    [replen] [bundle] [VIP]    [winback]
sunscreen [edu]  [replen] [combo]  [VIP]    [winback]
haircare [edu]   [cross]  [bundle] [VIP]    [winback]
```

---

## 5 · ความถี่ (Frequency Cap) — งบที่มองไม่เห็น

**หลักคิด:** ทุกข้อความมีต้นทุน 2 ชั้น
1. ต้นทุนเงิน = ฿0.06–0.10 ต่อข้อความ
2. ต้นทุน block rate = โอกาสที่ลูกค้าจะหายถาวร

**ตาราง cap ที่แนะนำ**

| Segment | ข้อความ/เดือน | ช่องทาง |
|---|---|---|
| Champions | 6–8 | LINE + SMS สำรอง |
| Loyal | 5–6 | LINE |
| Potential / Recent | 4–6 | LINE |
| Needing Attention | 3–4 | LINE |
| At Risk | 2–3 | LINE + โทรถ้า high value |
| Hibernating | 1 | LINE |
| Lost | 0–1/ไตรมาส | LINE |

**ติดตาม:** block rate ราย segment — ถ้า segment ไหน block > 8% ให้ลดความถี่ลงครึ่งหนึ่งทันที

---

## 6 · เครื่องมือแบ่งกลุ่มที่มีอยู่แล้ว

| เครื่องมือ | ทำอะไรได้ | ข้อจำกัด |
|---|---|---|
| **LINE OA Manager → Target Audience** | กรองตาม tag, เพศ, อายุ, พฤติกรรมคลิก | ไม่คำนวณ RFM ให้ |
| **MyCustomer CRM** | tier, point, tag, targeted broadcast, dashboard | ต้องมีข้อมูลสมาชิก |
| **Third-party (Chatcone, Amity ฯลฯ)** | RFM อัตโนมัติ, journey builder, shared inbox | ค่าใช้จ่ายรายเดือน + webhook conflict |
| **BI / Sheets + export** | ทำ RFM เองได้เต็มที่ | ต้องอัปเดตด้วยมือ |

**คำแนะนำ:** เริ่มที่ Sheets/SQL → ส่งเข้า tag ใน LINE OA Manager → เมื่อรายได้จาก LINE เกิน ~฿500K/เดือนจึงย้ายไป third-party

---

## 7 · รอบการรีวิว segment

```
รายสัปดาห์  → tag ที่ผิด/ขาด, block rate ราย segment
รายเดือน    → รัน RFM ใหม่, ดูการย้าย segment (movement)
รายไตรมาส   → recalibrate threshold (ธุรกิจโต → เกณฑ์เปลี่ยน)
```

**ตัวชี้วัดสุขภาพของ segmentation**
| ตัวชี้วัด | เป้า |
|---|---|
| % ลูกค้าที่มี tag ครบ 3 มิติ | > 80% |
| % ข้อความที่ส่งแบบ segmented (ไม่ใช่ all) | > 70% |
| Block rate รวม | < 5% |
| Champions → block | < 1% |

---

## กับดักของบทนี้

- ❌ ใช้ NTILE กับฐานเล็ก → segment เพี้ยน
- ❌ ใช้ revenue แทน margin → Champions ที่จริงคือคนซื้อของลด
- ❌ ตั้ง 11 segment แต่ส่งข้อความเดียวกันหมด
- ❌ ไม่มี cap → At Risk ได้ข้อความ 8 ครั้ง/เดือน แล้ว block
- ❌ รัน RFM ครั้งเดียวแล้วไม่อัปเดต → ข้อมูลเก่า 6 เดือน
- ❌ แบ่งกลุ่มด้วยข้อมูลสุขภาพ/ศาสนา → ผิด PDPA

---

## แหล่งอ้างอิง

ดู [`SOURCES.md`](SOURCES.md) — กลุ่ม `rfm-segmentation`, `retention-benchmarks`, `line-crm`
