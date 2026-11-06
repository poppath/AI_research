# 04 · TikTok Shop, GMV Max & Affiliate

> **TL;DR** — Shop ไม่ใช่แค่ "ยิงแอดขายของ" แต่เป็นระบบ 3 ชั้นที่ต้องเรียงลำดับ: **ของพร้อม (catalog+offer) → คนพูดถึง (creator/affiliate volume) → AI ขยาย (GMV Max)**. ถ้าเริ่มจาก GMV Max ก่อน = เอาเงินไปเลี้ยง AI ที่ไม่มีวัตถุดิบ

---

## 1. ลำดับที่ถูกต้อง (ห้ามสลับ)

```
┌─ ชั้น 0 · CATALOG & OFFER ─────────────────────────────┐
│  title ถูก, รูปชัด, variant ครบ, ราคา/coupon/bundle, │
│  inventory, fulfillment, return policy                 │
└────────────────────────────────────────────────────────┘
                        ↓
┌─ ชั้น 1 · CREATOR / AFFILIATE VOLUME ──────────────────┐
│  Open Plan (ใครก็สมัครได้) + Target Plan (ดีลตัวต่อตัว)│
│  เป้า: 15–25 ครีเอเตอร์ช่วง cold start                 │
│  เป้า content: 3–5 คลิป/ครีเอเตอร์ ใน 30 วันแรก        │
└────────────────────────────────────────────────────────┘
                        ↓
┌─ ชั้น 2 · PROOF OF LIFE ───────────────────────────────┐
│  20–50 ออร์เดอร์/สัปดาห์ ติดกัน 2–4 สัปดาห์            │
│  + creative per SKU ≥10–15 ชิ้นที่ authorize แล้ว       │
└────────────────────────────────────────────────────────┘
                        ↓
┌─ ชั้น 3 · GMV MAX ─────────────────────────────────────┐
│  Target ROI 2–3x (learning) → 3–4x (day 30+)          │
└────────────────────────────────────────────────────────┘
                        ↓
┌─ ชั้น 4 · LIVE + Spark multiplier ─────────────────────┐
│  หลังมี GMV ฐาน ~$50k/เดือนขึ้นไป                     │
└────────────────────────────────────────────────────────┘
```

---

## 2. GMV Max คืออะไร และต่างจาก Smart+ อย่างไร

| มิติ | Smart+ | GMV Max |
|---|---|---|
| ขอบเขต | objective ทั่วไป (traffic/lead/app) | Shop เท่านั้น |
| Attribution | ad-driven conversions | **ทุกออร์เดอร์ของสินค้าที่อยู่ใน campaign** รวมออร์แกนิก + affiliate |
| Targeting | automation (เปิด/ปิดได้บางส่วน) | automation เต็ม ≈ ไม่มี age/gender/interest |
| Creative | asset group ที่คุณป้อน | ดึงจากทุกวิดีโอที่ผูกสินค้าและ authorize แล้ว (auto-select ไม่จำกัด) |
| Levers ที่คุณคุม | creative, target CPA/ROAS, exclusions | creative volume, feed, offer, target ROI |
| ประเภท | Web / App / Lead | **Product GMV Max** / **LIVE GMV Max** |

**ทำไม attribution แบบนี้สำคัญมาก:** GMV Max จะได้เครดิตจากยอดที่เกิดขึ้นแม้มาจากออร์แกนิก → **ตัวเลข ROI จะดูดีเกินจริงเมื่อเทียบกับ incremental**. ต้องอ่านคู่กับ blended และทำ incrementality test (บท 08)

---

## 3. ตั้งค่า GMV Max ให้ถูกตั้งแต่ launch

| พารามิเตอร์ | ค่าแนะนำ | เหตุผล |
|---|---|---|
| Target ROI (day 1–14) | **2.0–3.0×** | 5× = ไม่มี spend; 1× = เผาเงิน |
| Target ROI (day 30+) | 3.0–4.0× (ถ้า margin รองรับ) | ค่อย ๆ  tighten เมื่อ AI เรียนรู้แล้ว |
| งบต่อ SKU/วัน | $50–150 (≈฿1,800–5,400) ที่ launch | พอให้เกิด learning |
| สูตรงบ TikTok | **2 × historical non-LIVE GMV ÷ ROI target** | [tiktok] Product GMV Max best practices |
| Budget consumption | ให้ต่ำกว่า ~80% | ถ้าใช้ 90%+ ให้เพิ่มงบทีละ ~30% |
| จำนวน creative | ≥15–20 เพื่อ launch, 50+ เพื่อ scale | GMV Max ต้องการความหลากหลายจริง |
| ระยะเวลาก่อนประเมิน | ≥7 วัน | pause วันที่ 3 = reset learning |
| การ hold target | 3 วันเต็มต่อ 1 target | อย่าขยับทุกวัน |
| Authorize affiliate content | **ก่อน** launch ≥48 ชม. | เพิ่มทีหลัง = บังคับให้ระบบ re-learn |

**Sequence การแก้เมื่อแย่:**
```
1. เพิ่ม creative (ก่อนเสมอ)
2. ปรับ offer/coupon (ราคาคือ lever ที่ AI แก้ให้ไม่ได้)
3. ตรวจ feed (ชื่อ/รูป/category/stock)
4. ปรับ target ROI ±10–15%
5. ลด SKU ที่ margin ไม่ไหวออก
```

---

## 4. Affiliate engine — หัวใจของ Shop

### 4.1 โครงสร้างโปรแกรม
| ชั้น | คืออะไร | เป้า |
|---|---|---|
| **Open Plan** | ใครก็รับได้ (ครีเอเตอร์ ≥5,000 followers) | volume + long tail |
| **Target Plan (TAP)** | ดีล 1:1 อัตราพิเศษ | ครีเอเตอร์ที่พิสูจน์แล้ว |
| **Managed roster** | ทีมดูแล brief + sample + ติดตาม | 15–75 คน |

**commission ที่ตลาดใช้:**
- beauty / supplement: ~20% (median)
- fashion: 15–18%
- ตัวเลขนี้ต้องบวกเข้า unit economics — ดูข้อ 6

### 4.2 Cold start 30 วัน
```
สัปดาห์ 1:  คัด 15-25 ครีเอเตอร์ (ในหมวด, มี engagement จริง, ไม่ใช่ยอดปลอม)
           → ส่ง sample ภายใน 48 ชม. หลังเซ็น brief
สัปดาห์ 2:  ตั้งเป้า 3-5 คลิป/คน ใน 30 วัน
           → ให้ hook + talking points (ไม่ใช่ script เต็ม)
สัปดาห์ 3:  เก็บข้อมูล: GMV/ครีเอเตอร์, view, CVR, return
           → authorize คลิปที่ work เข้า GMV Max
สัปดาห์ 4:  คัด top 20% → ขึ้น TAP อัตราพิเศษ + retainer
           → ตัด bottom quartile
```

### 4.3 สิ่งที่ทำให้โปรแกรมตาย
| ปัญหา | ทางแก้ |
|---|---|
| ส่ง sample มือเปล่า → ครีเอเตอร์ไม่โพสต์ | สัญญาเป็นลายลักษณ์ + เป้าคลิป + ค่าตอบแทนขั้นต่ำ |
| brief ปล่อยอิสระ → claim ผิดกฎ | brief template ที่ระบุ "ห้ามพูด" ชัดเจน (บท 10) |
| ไม่มีระบบติดตาม → ไม่รู้ใครทำเงิน | ต้องมีตาราง GMV/ครีเอเตอร์ อัปเดตรายสัปดาห์ |
| commission สูงแต่ return rate สูง | คิด **net commission หลัง return** ไม่ใช่ gross GMV |
| ครีเอเตอร์เก่งคนเดียว = concentration risk | กระจาย ไม่ให้ 1 คน >30% ของ GMV |

---

## 5. ตัวเลข KPI ของ Shop ที่ต้องดู (ไม่ใช่แค่ GMV)

| KPI | ความหมาย | Benchmark 2026 (global) |
|---|---|---|
| GMV by source | split video / shop tab / live / affiliate | video 50–60%, shop 25–35%, live 10–15% |
| Video-to-purchase rate | ซื้อต่อ 10k views | 10–30 purchases / 10k views |
| Cart-to-purchase | add-to-cart ที่จ่ายจริง | 35–55% |
| Repeat purchase (60d) | % ซื้อซ้ำใน 60 วัน | top quartile 35–45% |
| Return rate | by category | fashion 12–18%, beauty 3–6% |
| Effective take rate | ค่าธรรมเนียมรวม/GMV (referral+payment+FBT+ads+return) | ~25–30% (US) — **ตัวเลขไทยต่าง, ต้องวัดเอง** |
| Creator affiliate ROI | net GMV หลัง commission | target 3.5×+ |
| Blended ROAS | revenue รวม / (paid + creator spend) | 2.5–4× ตามหมวด |
| Live session CVR | ซื้อต่อผู้ชมไลฟ์ | 1.5–3% (ดี), 8–12% (ยอดเยี่ยม) |

> ⚠️ ตัวเลขในตารางนี้เป็น **global/US** — อย่าเอาไปใช้เป็นเป้าในไทยตรง ๆ. ใช้เป็น "กรอบเทียบ" แล้ววัดของจริง

---

## 6. Unit economics — สมการที่ต้องทำก่อนตั้ง Target ROI

```
ราคาขาย (AOV)                          ฿890
− ต้นทุนสินค้า (COGS)                   ฿400
− platform commission + payment (~5-8%) ฿62
− affiliate commission (20%)            ฿178
− fulfillment + shipping                ฿60
− return/refund provision (~5%)         ฿45  (คิดจากอัตราคืนจริง)
─────────────────────────────────────────────
= Contribution margin ก่อน ad spend     ฿145  (16.3%)

Target ROAS ขั้นต่ำที่ยังไม่ขาดทุน = AOV / CM = 890 / 145 = 6.1x
```
**นี่คือเหตุผลที่ "ROAS 3x ก็พอ" มักไม่จริงใน Shop** เมื่อบวก commission + return + fee เข้าไป

**ถ้าคำนวณแล้ว Target ROAS ที่ต้องการสูงกว่าที่ TikTok รับได้ → ปัญหาอยู่ที่ offer/margin ไม่ใช่ ads** ทางแก้: bundle, up-sell, ลด commission, เปลี่ยน SKU ที่ margin ดีขึ้น, หรือย้ายไป D2C web

---

## 7. Product feed hygiene (ทำครั้งเดียว ใช้ได้ตลอด)

GMV Max optimize จาก feed — feed สกปรก = AI เลือกคนผิด

- [ ] ชื่อสินค้า: `[แบรนด์] + [สินค้า] + [คุณสมบัติหลัก] + [ขนาด]` (ไม่ยัด keyword)
- [ ] รูป: ≥5 รูป, พื้นขาว 1 + ใช้งานจริง 1 + scale/size 1 + ส่วนผสม 1 + before/after (ถ้า allowed)
- [ ] variant ครบ (สี/ไซซ์) และ stock ตรง
- [ ] category ถูก (ผิด category = AI หาคนผิด)
- [ ] ราคา + coupon ตรงกับที่โฆษณา
- [ ] return policy ชัด (ลด return rate)
- [ ] ไม่มี claim ผิดกฎในชื่อ/รูป

---

## 8. Anti-patterns ยอดฮิต

| ❌ | ทำไมพัง | ✅ |
|---|---|---|
| เปิด GMV Max วันแรกที่เปิดร้าน | ไม่มี purchase signal ให้เรียน | สร้าง affiliate + ads awareness ก่อน |
| Target ROI 5× ตั้งแต่วันแรก | ไม่มี spend เลย → ไม่มี data | 2–3× ก่อน 14 วัน |
| เปลี่ยน creative ทุกวัน | learning reset | เพิ่ม ไม่ใช่เปลี่ยน |
| วัดผลด้วย GMV อย่างเดียว | GMV สูงแต่ขาดทุน | CM after all costs |
| เอาคลิปที่ยังไม่อนุญาตมาใช้ | ระบบไม่ดึง, หรือผิดสิทธิ์ | authorize ก่อน launch |
| ไลฟ์ทุกวันตั้งแต่ต้น | burn out + GMV ไม่คุ้ม | เริ่ม 1–2 ครั้ง/สัปดาห์ 2–4 ชม. |
| โยนสินค้าทุก SKU เข้า GMV Max | งบกระจาย, ไม่มี SKU ไหนพอ | 3–5 SKU ที่ margin ดีสุดก่อน |

---

## 9. 90-day plan (Shop)

| ช่วง | เป้าหมาย | ตัวชี้วัด |
|---|---|---|
| Day 1–30 | catalog + affiliate cold start + ads awareness | 15–25 ครีเอเตอร์, ≥40 คลิป, 20–50 ออร์เดอร์/สัปดาห์ |
| Day 31–60 | GMV Max บน 3–5 SKU + คัด top creator | ROI ≥2.5×, CM positive, return <เป้า |
| Day 61–90 | LIVE + scale GMV Max + TAP | GMV +50–100%, concentration <30%/คน |

---

## อ้างอิงบทนี้
กลุ่ม `shop`, `gmv-max`, `affiliate` ใน [`SOURCES.md`](SOURCES.md)
