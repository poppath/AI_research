# METRICS.md — นิยาม metric + สูตร + เกณฑ์

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> ใช้ไฟล์นี้เป็น reference เวลาอ่าน dashboard หรือเขียนรายงาน. **ทุกสูตรต้องใช้ค่าที่สอดคล้องกัน** (เช่น revenue ที่หัก refund แล้วหรือยัง — ต้องระบุให้ชัด)

---

## 1. Metric ระดับ creative

| Metric | สูตร | เกณฑ์ 2026 | หมายเหตุ |
|---|---|---|---|
| **Hook rate** (3s view rate) | 3-second video views ÷ impressions | <20% อ่อน · 20–30% พอใช้ · >30% ดี | metric สำคัญที่สุดของ creative |
| 6s view rate | 6s views ÷ impressions | Creative Center ใช้เป็น ranking | |
| **Completion rate** | video completions ÷ views | >70% = เกณฑ์ viral push | ยิ่งสั้นยิ่งง่ายถึงเกณฑ์ — อย่าเทียบข้ามความยาว |
| Rewatch rate | replays ÷ views | ยิ่งสูงยิ่งดี | บ่งชี้ density ของเนื้อหา |
| Share rate | shares ÷ views | สูงมากใน Wave 3+ | signal สำคัญสุดหลังผ่าน Wave 2 |
| Save rate | saves ÷ views | | บ่งชี้ utility |
| CTR | clicks ÷ impressions | 0.6–1.2% (e-comm median) · 1.5–3% = ดี (in-feed TH) | ต่างกันมากตามอุตสาหกรรม |
| CPC | spend ÷ clicks | ฿1–5 (TH in-feed) · $1–2 (global e-comm) | |
| CPM | spend ÷ impressions × 1000 | ฿50–200 (TH) · $4–14 (global) | ถูกที่สุดในบรรดาแพลตฟอร์มหลัก |
| Frequency (7d) | impressions ÷ reach | ควร <2.5–3 | เกิน = อิ่มตัว |
| Cost per 3s view | spend ÷ 3s views | — | ใช้เทียบคุณภาพ hook |

---

## 2. Metric ระดับ campaign

| Metric | สูตร | เกณฑ์ |
|---|---|---|
| CPA (cost per action) | spend ÷ conversions | ตาม unit economics |
| CVR | conversions ÷ clicks | 1.5–2.5% (LP นอกแอป) · 3–5% (Shop) · 10%+ (Shop บางหมวด) |
| ROAS (platform) | revenue (platform) ÷ spend | ≥2.5× (baseline e-comm) · 3.5–5× (top DTC หลัง 60 วัน) |
| ROAS floor | 1 ÷ CM% | เช่น CM 16.3% → 6.1× |
| Learning status | ≥50 conversions / 7 วัน + ≥7 วัน | ถ้าไม่ถึง = learning limited |

---

## 3. Metric ระดับธุรกิจ (สำคัญที่สุด)

| Metric | สูตร | ทำไม |
|---|---|---|
| **Blended ROAS** | total revenue ÷ (paid + creator + tool spend) | รอดจาก attribution loss |
| **MER** | total revenue ÷ total marketing spend | เทียบข้ามช่องทาง |
| **CM after ads** | revenue − COGS − fees − commission − shipping − returns − ad spend | KPI สูงสุด |
| **New-customer CPA** | paid spend ÷ new customers | แยกจาก returning |
| **Payback period** | CAC ÷ (daily gross profit/customer) | สำหรับ subscription/LTV |
| AOV | revenue ÷ orders | |
| Repeat purchase 60d | % buyers ที่ซื้อซ้ำใน 60 วัน | leading indicator ของ margin |
| Effective take rate | total fees ÷ GMV | Shop: ~25–30% (US) |
| Return rate | returns ÷ orders | fashion 12–18%, beauty 3–6% (global) |

---

## 4. Metric ระดับ Shop / LIVE

| Metric | เกณฑ์ |
|---|---|
| GMV by source | video 50–60% · shop tab 25–35% · live 10–15% |
| Video-to-purchase rate | 10–30 purchases / 10k views |
| Cart-to-purchase | 35–55% |
| Creator affiliate ROI (net) | ≥3.5× หลัง commission |
| Live avg watch time | 3–5 นาที = ดี · 8+ = ยอดเยี่ยม |
| Live CVR | 1.5–3% ดี · 8–12% ยอดเยี่ยม |
| Live engagement rate | 5–10% ดี · 15%+ ยอดเยี่ยม |
| GMV per session | $500–2,000 ปกติ · $5,000+ ดี |

---

## 5. Metric ระดับ measurement quality

| Metric | เป้า | ที่วัด |
|---|---|---|
| **EMQ (Event Match Quality)** | ≥8.0 | Ads Manager → Events → Overview (สเกล 0–10) |
| Conversion capture rate | ~95% | ประเมินจาก pixel-only ~65% |
| Attributed conversion index | 120–130 (vs pixel only = 100) | เปรียบเทียบก่อน/หลังเปิด Events API |
| Dedup error rate | 0 | ตรวจ event_id |
| TikTok vs GA4 discrepancy | ยอมรับ 10–30% | reconcile รายเดือน |

---

## 6. สูตร Unit Economics (ใช้ก่อนตั้ง target ROAS เสมอ)

```
CM (contribution margin) =
    AOV
  − COGS
  − platform fee (% ของ GMV)
  − payment fee (%)
  − affiliate commission (%)
  − fulfillment + shipping
  − return provision (return rate × (AOV + shipping))

ROAS floor (จุดคุ้มทุน ไม่รวมค่าการตลาดอื่น) = AOV ÷ CM

ตัวอย่าง:
AOV 890 · COGS 400 · fee 7% (62) · commission 20% (178)
shipping 60 · return 5% (45)
CM = 890 − 400 − 62 − 178 − 60 − 45 = 145  (16.3%)
ROAS floor = 890 ÷ 145 = 6.1×
```

> ถ้า ROAS floor สูงกว่าที่แพลตฟอร์มทำได้ในหมวดนั้น → **ต้องแก้ offer/margin ก่อน ไม่ใช่ ads**

---

## 7. เกณฑ์เปรียบเทียบ TikTok vs Meta (ใช้อย่างระวัง)

| | TikTok | Meta |
|---|---|---|
| CPM | ถูกกว่า ~40–50% [vendor, 2025] | แพงกว่า |
| CTR | ต่ำกว่าเล็กน้อย | สูงกว่า |
| CVR (LP) | ต่ำกว่า (คนอยู่โหมด discover) | สูงกว่า |
| CVR (Shop/in-app) | สูงกว่าชัด (checkout ในแอป) | ไม่มี |
| Hook timing | 1–3 วินาที | 2–3 วินาที |
| Creative fatigue | 10–14 วัน | 14–21 วัน |
| Aspect ratio | 9:16 เท่านั้น | หลายแบบ |

**สรุป:** TikTok ถูกกว่าในการ "เข้าถึง" แต่แพงกว่าในการ "ปิดการขาย" — TikTok ชนะเมื่อ (ก) มี TikTok Shop (ข) สินค้า demonstrative (ค) มี creative pipeline

---

## 8. หมายเหตุเรื่องความน่าเชื่อถือของตัวเลข

ทุกตัวเลขในไฟล์นี้เป็น **vendor-reported ranges** จากหลายแหล่ง (ดู SOURCES.md) ไม่ใช่ controlled benchmark ของคุณเอง

- ใช้เป็น **กรอบตัดสินใจ** ไม่ใช่ **เป้าที่ต้องชนะ**
- ตัวเลข global/US ห้ามใช้เป็นเป้าในไทยตรง ๆ
- ก่อนใช้กับลูกค้า/งบจริง → สร้าง **baseline ของตัวเอง** จาก 4 สัปดาห์แรก แล้วใช้ไฟล์นี้เป็น "ผิดปกติหรือเปล่า"
