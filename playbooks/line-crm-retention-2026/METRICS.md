# METRICS — นิยาม สูตร และ threshold

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

ทุกตัวเลขในไฟล์นี้มี `as_of: 2026-11` และมี `source_type` กำกับ
`[tiktok]` = เอกสารแพลตฟอร์ม · `[vendor]` = รายงาน agency/blog · `[est]` = ประมาณจาก triangulation

> ⚠️ line: ตัวเลขบน LINE ได้รับอิทธิพลจากต้นทุนข้อความและ block rate ซึ่งไม่ปรากฏในรายงาน vendor ส่วนใหญ่ → ใช้เป็นกรอบ ไม่ใช่เป้า

---

## 1 · Acquisition

| ตัวชี้วัด | สูตร | ค่าเฉลี่ย | ดี | แหล่ง |
|---|---|---|---|---|
| CPF (cost per friend) | ค่าใช้จ่าย ÷ เพื่อนใหม่ | ฿30–80 | < ฿30 | `[est]` |
| Add → first purchase (30d) | ซื้อ ÷ เพื่อนใหม่ | 10–15% | > 20% | `[est]` |
| Friend block rate (30d) | block ÷ ส่งถึง | 3–5% | < 3% | `[est]` |
| Net friend growth | เพื่อนใหม่ − เพื่อนหาย | — | > 0 | — |

---

## 2 · Engagement (LINE)

| ตัวชี้วัด | สูตร | ค่าเฉลี่ย | ดี | แหล่ง |
|---|---|---|---|---|
| Open rate | เปิด ÷ ส่งถึง | ~60% | > 70% | `[vendor]` |
| CTR | คลิก ÷ เปิด | 5–10% | > 12% | `[est]` |
| Block rate | block ÷ ส่งถึง | 3–5% | < 3% | `[est]` |
| RPM (revenue per message) | revenue ÷ messages | ฿1–3 | > ฿5 | `[est]` |
| First response time | เวลาตอบครั้งแรก | < 1 ชม. | < 5 นาที | `[est]` |

---

## 3 · Retention

| ตัวชี้วัด | สูตร | ค่าเฉลี่ย | ดีมาก | แหล่ง |
|---|---|---|---|---|
| Repeat purchase rate (12 เดือน, ทุกหมวด) | ลูกค้า ≥2 ออเดอร์ ÷ ลูกค้าทั้งหมด | ~19–30% | 40%+ | `[vendor]` |
| RPR — consumables | — | 25–40% | 40–55% | `[vendor]` |
| RPR — apparel | — | 12–17% | 20%+ | `[vendor]` |
| RPR — durable | — | 7–15% | 20%+ | `[vendor]` |
| 90-day repeat | ซื้อซ้ำภายใน 90 วัน ÷ cohort | 15–25% | 30%+ | `[vendor]` |
| Time to 2nd order | ค่าเฉลี่ยวัน | 45–90 | < 45 | `[vendor]` |
| m1 repeat (non-cumulative) | — | 35–42% (healthy DTC) | 45%+ | `[vendor]` |
| m3 repeat (non-cumulative) | — | 22–25% | 30%+ | `[vendor]` |

---

## 4 · Lifecycle flows

| Flow | Open rate | Conversion | RPR | แหล่ง |
|---|---|---|---|---|
| Welcome (email ref) | 35–60% | 2.1–4.4% | $2.5–6 | `[vendor]` |
| Welcome (top quartile) | 75–90% | 8–12% | $8+ | `[vendor]` |
| Cart / checkout recovery | 50–65% | 3.3–7.7% | สูงสุด | `[vendor]` |
| Post-purchase | 50–65% | 3–6% cross-sell | $0.8–2.5 | `[vendor]` |
| Replenishment | 40–55% | 4–10% | ปานกลาง | `[est]` |
| Win-back | 20–35% | 1–4% | ต่ำสุด | `[vendor]` |

**ตัวเลขที่ควรจำ:** flows = **~41% ของ email revenue จาก 5.3% ของ sends** `[vendor]` (Klaviyo 2026)
→ ใช้เป็น argument ว่าทำไม flow คุ้มกว่า broadcast

---

## 5 · Unit economics

```
CM₁        = AOV − COGS − fee − shipping − affiliate − return provision
ROAS floor = AOV ÷ CM₁
LTV₁₂      = AOV × frequency₁₂ × CM% × (1 − return_rate)
CAC        = (media + คน + tools) ÷ ลูกค้าใหม่
LTV:CAC    = LTV₁₂ ÷ CAC
Payback    = CAC ÷ (CM₁ × frequency ต่อเดือน)
MER        = revenue รวม ÷ media รวม
```

**ตัวอย่างที่ใช้ทั้ง playbook**
```
AOV ฿890 · COGS ฿400 · fee 7% ฿62 · affiliate 20% ฿178 · ship ฿60 · return 5% ฿45
→ CM₁ = ฿145 (16.3%)  · ROAS floor = 6.1×

ถ้า CAC = ฿250  → ขาด ฿105 ที่ออเดอร์แรก
Breakeven repeat = (250 − 145) ÷ 160 = 66%
```

| ตัวชี้วัด | สุขภาพ | อันตราย | แหล่ง |
|---|---|---|---|
| LTV:CAC (12 เดือน, CM basis) | 2.5:1–4:1 | < 2:1 | `[vendor]` |
| CAC payback | < 90 วัน | > 180 วัน | `[vendor]` |
| MER | 2.5–4× | < 2× | `[vendor]` |
| CM after ads | > 0 | ติดลบ | — |

---

## 6 · ต้นทุน LINE (ไทย, ต.ค. 2026, ไม่รวม VAT)

| แพ็กเกจ | ราคา/เดือน | messages | เกิน | CRM |
|---|---|---|---|---|
| Free | ฿0 | 300 | ส่งไม่ได้ | — |
| Basic | ฿1,280 | 15,000 | ฿0.10 | +฿369 |
| Pro | ฿1,780 | 35,000 | ฿0.06 | ฟรี |

**จุดตัด**
```
20,000 messages  → Pro = Basic+overage
16,310 messages  → Pro คุ้มกว่าถ้าจะซื้อ CRM อยู่แล้ว
```

**Add-ons:** OA Chat Package ฿555/เดือน · Verified badge ฿888 ครั้งเดียว · Premium ID ~฿444–459/ปี

---

## 7 · LINE Ads (ไทย)

| ตัวชี้วัด | ค่า | แหล่ง |
|---|---|---|
| CPM (mass) | ~฿15 | `[vendor]` |
| CPM (premium placement) | ฿50–200 | `[vendor]` |
| งบขั้นต่ำ/วัน | ~฿500 | `[vendor]` |
| งบขั้นต่ำที่อ่านผลได้ | ฿10,000–25,000/เดือน | `[vendor]` |
| CPF | ฿30–80 | `[est]` |

**รูปแบบการซื้อ:** CPM · CPC · **CPF** · CPV · CPA · CPI

---

## 8 · Chat commerce

| ตัวชี้วัด | ค่า | แหล่ง |
|---|---|---|
| Chat → close (ผู้ที่ทักเข้ามา) | 85–98% | `[vendor]` ⚠️ ไม่ใช่ funnel CR |
| Chat → order (ทั้งระบบ) | 15–25% | `[est]` |
| First response time (เป้า) | < 5 นาที | `[est]` |
| Resolution time | < 24 ชม. | `[est]` |

> ⚠️ 85–98% วัดจากคนที่ทักเข้ามาแล้วเท่านั้น อย่าเอาไปเทียบกับ CR ของ landing page

---

## 9 · Segmentation

| ตัวชี้วัด | เป้า |
|---|---|
| % ลูกค้าที่มี tag ครบ 3 มิติ | > 80% |
| % ข้อความแบบ segmented | > 70% |
| Tag completeness ของทีมแชท | ≥ 80% |
| Segment ที่ block > 8% | ต้องลดความถี่ทันที |

---

## 10 · TikTok vs LINE (ใช้เทียบเพื่อจัดสรรงบ)

| มิติ | TikTok (paid) | LINE (retention) |
|---|---|---|
| ต้นทุนหลัก | media spend | message quota + คน |
| ตัวชี้วัดหลัก | CPA / ROAS | RPM / repeat rate |
| ระยะเวลาคืนทุน | ทันที (ถ้า ROAS ดี) | 30–90 วัน |
| อัตราการรั่ว | สูง (ไม่มีการติดตาม) | ต่ำ (เป็นเจ้าของ audience) |
| สเกล | สูงมาก | จำกัดด้วยจำนวนคน |
| ความเสี่ยงหลัก | creative fatigue | block rate |

**สูตรจัดสรรงบที่แนะนำ (SME ไทย)**
```
70%  performance media (TikTok/Meta) — หาลูกค้าใหม่
20%  retention (LINE + flow + content) — ทำกำไร
10%  test (ช่องทาง/creators ใหม่)
```
ปรับเป็น 60/30/10 เมื่อ LTV:CAC ของ retention ชัดว่าดีกว่า

---

## 11 · Credibility caveat

- benchmark retention ส่วนใหญ่มาจาก **DTC ตะวันตก** — ตลาดไทยมี COD สูง, return สูง (fashion 20–30%), marketplace fee 5–8%
- ตัวเลข flow benchmarks มาจาก **email** ไม่ใช่ LINE — LINE มี open rate สูงกว่าแต่ conversion ขึ้นกับ offer
- ตัวเลข CPM/CPF ของ LINE Ads มี dispersion สูงมากตาม creative และ audience
- **กฎ 90 วัน:** ตัวเลขใดในไฟล์นี้อายุเกิน 90 วันต้อง re-verify ก่อนใช้ตัดสินใจงบ
