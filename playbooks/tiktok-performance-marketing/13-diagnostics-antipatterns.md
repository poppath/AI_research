# 13 · Diagnostics & Anti-patterns

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> **TL;DR** — เวลา performance ตก อย่าเริ่มจาก "ปรับ targeting" หรือ "ลด bid". ไล่ตามลำดับ: **tracking → creative → offer/หน้าเว็บ → structure/bid → audience**. 9 ใน 10 ครั้ง ปัญหาอยู่ใน 3 อย่างแรก

---

## 1. Diagnostic ladder (ไล่จากบนลงล่าง เสมอ)

```
STEP 0  TRACKING  → event ยังยิงครบไหม? EMQ ปกติไหม? ตัวเลขใน Ads Manager กับร้านตรงกันไหม?
STEP 1  CREATIVE  → hook rate ตกไหม? frequency สูงไหม? มี creative ใหม่ใน 14 วันไหม?
STEP 2  OFFER/LP  → ราคาเปลี่ยนไหม? coupon หมดอายุ? หน้าเว็บช้า/พัง? stock?
STEP 3  STRUCTURE → มี campaign learning limited? งบ < 10× CPA? งบกระจายเกิน?
STEP 4  BID       → cost cap ต่ำเกิน? bid cap?
STEP 5  AUDIENCE  → อิ่มตัวจริงหรือเปล่า? (ต้องพิสูจน์ด้วย frequency + reach)
```

> **99% ของ "TikTok ไม่ work" จบที่ STEP 0–2**

---

## 2. ตาราง diagnose: อาการ → สาเหตุ → สั่งการ

### 2.1 ไม่มี spend / spend น้อย

| อาการ | สาเหตุ | ทำอะไร (ตามลำดับ) |
|---|---|---|
| ไม่มี spend เลย | bid cap/cost cap ต่ำ, งบ < 10× CPA, audience เล็กเกิน, ad rejected | ตรวจสถานะ ad → เปลี่ยน Lowest Cost → เพิ่มงบ → ขยาย audience |
| spend ไม่เต็มงบ | ใช้ view-through attribution แล้วติดข้อจำกัด, cost cap เข้ม | ปิด view-through tracking / ผ่อน cap |
| spend กระตุก | การแก้ไขบ่อย, งบเปลี่ยนทุวัน | หยุดแตะ 3–5 วัน |
| spend ได้แต่เฉพาะบางชั่วโมง | การแข่งขัน/audience | ปล่อย หรือ daypart ถ้ามีข้อมูล |

### 2.2 CPA แพง

| อาการ | สาเหตุ | ทำอะไร |
|---|---|---|
| CPA แพงตั้งแต่ต้น | creative อ่อน หรือ offer ไม่แข่ง | เพิ่ม creative 5–8 ชิ้นใหม่ → ทบทวน offer |
| CPA ดี 3 วันแรก แล้วแย่ | learning จบ, audience อิ่มตัว | เพิ่ม creative + horizontal expand |
| CPA แพงขึ้นหลังเพิ่มงบ | pool คุณภาพต่ำลง | ยอมรับ +10–20% หรือ scale แบบ horizontal |
| CPA แพงขึ้นหลังเปลี่ยน bid | หลุด learning | กลับค่าเดิม, รอ 5–7 วัน |
| CPA แพงทุก campaign พร้อมกัน | ตลาด (seasonality/competitor) หรือ tracking | ตรวจ event ก่อน → เทียบ YoY |

### 2.3 CTR ดี แต่ conversion ต่ำ

| สาเหตุ | ตรวจ | แก้ |
|---|---|---|
| หน้าเว็บ/product page | load time, ราคาตรง, รูป, รีวิว, ค่าส่ง | แก้ LP — **อย่าโทษ creative** |
| CTA ไม่ตรงปลายทาง | "ซื้อเลย" เด้งไปหน้าแรก | ทำ landing ให้ตรง |
| ราคาในแอด ≠ ราคาจริง | โปรโมชันหมดอายุ | sync ราคา/คูปอง |
| ความคาดหวังผิด | แอดบอกอย่าง หน้าเว็บบอกอีกอย่าง | align message |

### 2.4 ROAS ดี แต่กำไรขาดทุน

| สาเหตุ | ตรวจ |
|---|---|
| commission/affiliate สูง | CM ต่อ SKU |
| return rate สูง | return by SKU |
| discount/coupon กิน margin | coupon cost ใน CM |
| platform fee + fulfillment | effective take rate |
| ขาย SKU ที่ margin ต่ำ | GMV mix |

**แก้:** bundle, up-sell, เปลี่ยน SKU ที่ margin ดี, ลด commission, เพิ่มราคา (ถ้าตลาดรับได้), ย้ายไป D2C web

### 2.5 Learning limited ตลอด

| สาเหตุ | แก้ |
|---|---|
| งบ < 10× CPA | รวม ad group / เพิ่มงบ |
| event เกิด < 20/สัปดาห์ | เปลี่ยนเป็น event ที่ถี่ขึ้นชั่วคราว |
| pause/เปิดซ้ำ | ปล่อยให้รันต่อเนื่อง |
| bid cap ต่ำ | เอา cap ออกชั่วคราว |

### 2.6 Creative fatigue

| สัญญาณ | Threshold | แก้ |
|---|---|---|
| Hook rate ลด | >20% จาก baseline | เปลี่ยน 3 วินาทีแรก |
| Frequency | >2.5–3 (7 วัน) | เพิ่ม creative / ขยาย pool |
| CPA เพิ่ม | >25% 3 วันติด | creative ใหม่ 3–5 ชิ้น |
| Age ของ concept | >10–14 วัน | refresh ตามปฏิทิน |

### 2.7 Shop / GMV Max เฉพาะ

| อาการ | สาเหตุ | แก้ |
|---|---|---|
| GMV Max ไม่ spend | target ROI สูงเกิน, ไม่มี creative authorize | ลด ROI เป็น 2×, authorize คลิปก่อน launch |
| ROI ต่ำกว่าเป้า | feed สกปรก, creative ซ้ำ, SKU margin ต่ำ | ทำ feed hygiene, เพิ่ม creative, คัด SKU |
| GMV ขึ้นแต่กำไรลง | attribution กว้าง + return สูง | วัด CM, ตรวจ return by SKU |
| LIVE GMV Max ไม่ work | ไลฟ์ไม่สม่ำเสมอ (learning reset ทุกครั้ง) | ไลฟ์เวลาเดิมสม่ำเสมอ, เปิด campaign ล่วงหน้า 3 วัน |

### 2.8 Tracking / measurement

| อาการ | สาเหตุ | แก้ |
|---|---|---|
| conversion ใน Ads Manager > ร้านจริง มาก | attribution window กว้าง + view-through | ใช้ blended เป็นหลัก |
| conversion < จริง | pixel ถูก block, ไม่มี Events API | ติด Events API + dedup |
| EMQ < 5 | ไม่ส่ง identifier | ส่ง hashed email/phone/external_id |
| ROAS เปลี่ยนทันทีหลังเปลี่ยน setting | เปลี่ยน attribution window | อย่าเปลี่ยนพร้อมกันอย่างอื่น |
| ตัวเลข TikTok ≠ GA4 10–30% | methodology ต่าง | กำหนด single source of truth |

---

## 3. 20 Anti-patterns ที่พบบ่อยที่สุด

| # | Anti-pattern | ทำไมพัง |
|---|---|---|
| 1 | ตั้ง target ROAS จากความหวัง ไม่ใช่จาก unit economics | ระบบไม่ spend หรือ spend แล้วขาดทุน |
| 2 | ตัดสินใจปิด campaign วันที่ 2–3 | ยังไม่ถึง 50 conversions = สุ่ม |
| 3 | แตะ bid/งบทุกวัน | learning reset ตลอด |
| 4 | แก้ audience ก่อนแก้ creative | แก้ผิดจุด |
| 5 | ผลิต creative 3 ชิ้นแล้วรอ "ให้มัน work" | fatigue ที่ 10–14 วัน |
| 6 | ใช้เพลง trending ในโฆษณา | ผิดลิขสิทธิ์ / แอด reject |
| 7 | ขึ้นโลโก้ใน 1 วินาทีแรก | คนปัดทิ้ง |
| 8 | วัดด้วย platform ROAS | over-credit 30–60% |
| 9 | ไม่มี Events API | สูญเสีย ~35% ของ signal |
| 10 | ไม่ dedup event_id | นับ conversion ซ้ำ |
| 11 | เปิด GMV Max ก่อนมี affiliate content | AI ไม่มีวัตถุดิบ |
| 12 | Target ROI 5× วันแรก | ไม่มี spend |
| 13 | วัด Shop ด้วย GMV | scale การขาดทุน |
| 14 | ใส่ 5 ประเทศใน 1 ad group | อ่านผลไม่ได้ |
| 15 | 15 ad group × งบน้อย | ทุกกลุ่ม learning limited |
| 16 | ใช้ interest targeting เพื่อ scale | แคบและทับซ้อน |
| 17 | ไม่ตรวจ claim กับกฎหมายไทย | Thai FDA sweep, แอดถูกแบน, ความเสี่ยง criminal |
| 18 | ใช้ AI avatar กับ health/finance | trust ต่ำ + policy เสี่ยง |
| 19 | ไม่มี change log | เรียนรู้ไม่ได้ |
| 20 | ไม่เคยทำ incrementality test | ไม่รู้ว่า paid สร้างยอดหรือแค่เก็บยอด |

---

## 4. Recovery playbook: แคมเปญที่ "ตายแล้ว" จะกู้อย่างไร

```
Day 0   ตรวจ STEP 0 (tracking) — ถ้าพัง หยุดทุกอย่างแล้วแก้
Day 0   ดึง creative-level report 14 วันย้อนหลัง
Day 1   Kill: ทุก creative ที่ CPA > 1.3× target และมี impression ≥5,000
Day 1   เพิ่ม creative ใหม่ 6–8 ชิ้น จาก hook ที่เคยชนะ + hook ใหม่ 2 แบบ
Day 1   ตรวจ offer: ราคา, coupon, shipping, stock
Day 2   ลด target ROAS/cap ลง 10–15% ชั่วคราว (ซื้อ data)
Day 3-7 ปล่อย ไม่แตะ
Day 7   อ่านผล: ถ้า CPA ยังแย่ → ปัญหาอยู่ที่ offer/margin/LP ไม่ใช่ ads
```

---

## 5. คำถาม 7 ข้อที่ต้องตอบได้ก่อนบอกว่า "TikTok ไม่ work"

1. tracking สมบูรณ์และ dedup แล้วหรือยัง? (EMQ ≥8?)
2. แต่ละ ad group ได้ ≥50 conversions หรือยัง?
3. งบต่อ ad group ≥10× CPA หรือยัง?
4. มี creative ใหม่ใน 14 วันล่าสุดกี่ชิ้น?
5. hook rate เท่าไร? (ต่ำกว่า 20% = ปัญหา creative)
6. unit economics รองรับ target ROAS ที่ตั้งไว้จริงไหม?
7. เคยทำ incrementality test หรือยัง?

ถ้าตอบ "ไม่" ข้อไหน → นั่นคือสาเหตุก่อนจะโทษแพลตฟอร์ม

---

## อ้างอิงบทนี้
ทุกกลุ่มใน [`SOURCES.md`](SOURCES.md) — บทนี้เป็นการสังเคราะห์
