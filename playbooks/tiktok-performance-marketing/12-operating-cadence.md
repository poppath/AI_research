# 12 · Operating Cadence & KPI Dashboard

> **TL;DR** — performance ที่ดีไม่ใช่ผลจากการตัดสินใจครั้งใหญ่ครั้งเดียว แต่มาจาก **จังหวะงานที่สม่ำเสมอ**: ดูทุกวัน 5 นาที (แค่เช็คว่าระบบไม่พัง), ตัดสินใจทุกสัปดาห์, ทบทวนเชิงกลยุทธ์ทุกเดือน. คนที่แพ้คือคนที่ "ดูทุกวันแล้วแตะทุกวัน"

---

## 1. ตารางจังหวะงาน (Operating Rhythm)

| ความถี่ | เวลา | ทำอะไร | ผลลัพธ์ที่ต้องได้ |
|---|---|---|---|
| **ทุกวัน** | 5 นาที | spend pacing, campaign ที่ไม่ spend, event ตก, ของหมด stock | "ระบบปกติ / มี 1 เรื่องต้องแก้" |
| **ทุกสัปดาห์ (จ.)** | 60–90 นาที | creative-level review, kill/scale ตามเกณฑ์, วาง creative sprint | creative tracker อัปเดต + 3 การตัดสินใจ |
| **ทุกสัปดาห์ (พฤ.)** | 60 นาที | creative sprint (ผลิตตามบท 11) | 8–12 ไฟล์พร้อม launch |
| **ทุกเดือน** | 2 ชม. | blended ROAS, new-customer CPA, 28-day audit, reconcile, ตรวจ compliance | monthly report + 1 การทดลองใหม่ |
| **ทุกไตรมาส** | ครึ่งวัน | MMM refresh, attribution reassessment, EMQ audit, incrementality test, ทบทวน playbook | ไตรมาส plan + update playbook |

---

## 2. Weekly review — agenda 60 นาที

```
00-10  ตัวเลขสัปดาห์นี้ vs สัปดาห์ก่อน (spend, revenue, blended ROAS, CPA, orders, CM)
       ← ข้อเท็จจริงเท่านั้น ยังไม่ตีความ

10-30  Creative-level report
       → kill: ตัวที่ CPA > 1.3× target ต่อเนื่อง 2 สัปดาห์ (และมี impression พอ)
       → scale: ตัวที่ CPA ≤ 0.85× target 3 วันติด
       → pattern: hook type ไหนชนะ/แพ้

30-40  Funnel breakdown
       impression → 3s → click → PDP → ATC → purchase
       หา step ที่ drop ผิดปกติ (เทียบ benchmark บท METRICS)

40-50  Stock / operation
       → สินค้าที่จะหมด, สินค้าที่ return สูง, สินค้าที่ margin เปลี่ยน

50-60  ตัดสินใจ 3 ข้อสำหรับสัปดาห์หน้า (ไม่เกิน 3)
       เขียนเป็น: [การกระทำ] [ตัวชี้วัด] [วันตัดสิน]
```

**กติกา:** ห้ามประชุมเกิน 90 นาที. ห้ามตัดสินใจเกิน 3 ข้อ. ถ้าต้องการมากกว่านั้น แสดงว่ายังไม่ได้จัดลำดับ

---

## 3. KPI tree — จากบนลงล่าง

```
                        ┌─────────────────┐
                        │  Contribution    │  ← KPI สูงสุด (เงินจริง)
                        │  Margin after ads│
                        └────────┬─────────┘
                 ┌───────────────┼───────────────┐
        ┌────────▼──────┐ ┌──────▼──────┐ ┌──────▼───────┐
        │ Blended ROAS  │ │ New-cust CPA│ │ Return rate  │
        └────────┬──────┘ └──────┬──────┘ └──────┬───────┘
          ┌──────┴──────┐  ┌─────┴──────┐  ┌─────┴──────┐
     ┌────▼───┐ ┌───────▼┐ │  CVR      │  │  AOV       │
     │  CPM   │ │  CTR   │ │ (LP/Shop) │  │  bundle    │
     └────┬───┘ └────┬───┘ └─────┬─────┘  └────────────┘
     ┌────▼──────────▼───────────▼─────┐
     │ Hook rate · Completion · Freq   │
     │ Creative volume · Offer strength│
     └─────────────────────────────────┘
```

**อ่านจากล่างขึ้นบน:** ถ้า CM ติดลบ ให้ไล่ขึ้นมาดูว่าไปพังที่ชั้นไหน

---

## 4. Dashboard: 12 ตัวเลขที่ต้องเห็นบนหน้าเดียว

| # | Metric | คำถามที่มันตอบ | เกณฑ์เฝ้าระวัง |
|---|---|---|---|
| 1 | Spend (วัน/เดือน) | ใช้เงินตามแผนไหม | ±20% ของ plan |
| 2 | Revenue (blended) | ยอดรวมเป็นเท่าไร | — |
| 3 | **Blended ROAS** | โดยรวมคุ้มไหม | < target = แดง |
| 4 | **CM after ads** | กำไรจริงหลังโฆษณา | < 0 = แดงทันที |
| 5 | **New-customer CPA** | ได้ลูกค้าใหม่ราคาเท่าไร | > 1.2× target |
| 6 | AOV | มูลค่าออเดอร์ | ลด >10% = ตรวจ promo |
| 7 | CVR | หน้าเว็บ/shop แปลงดีไหม | ลด >20% = ตรวจ LP |
| 8 | Return rate | คุณภาพยอด | > benchmark หมวด |
| 9 | **Hook rate** | creative ดีไหม | <20% = เปลี่ยน hook |
| 10 | Completion rate | เนื้อหาดีไหม | <70% (ถ้าต้องการ viral) |
| 11 | Frequency (7d) | อิ่มตัวไหม | >2.5–3 |
| 12 | Creative launched (7d) | เครื่องจักรยังเดินไหม | <2 = แดง |

---

## 5. ตาราง escalation — เมื่อไหร่ต้องยกระดับ

| ระดับ | อาการ | ใครจัดการ | SLA |
|---|---|---|---|
| L1 | CPA แพงขึ้น <20%, 1–2 วัน | media buyer | ตรวจ creative ก่อน, ไม่แตะ bid |
| L2 | CPA แพงขึ้น >25% 3 วันติด | media buyer + creative | เพิ่ม creative ใหม่ 5 ชิ้น + ตรวจ frequency |
| L3 | Blended ROAS ต่ำกว่า target 2 สัปดาห์ | หัวหน้าทีม | ทบทวน offer, structure, target ROAS |
| L4 | CM ติดลบ | business owner | หยุด scale, ทบทวน unit economics ทั้งระบบ |
| L5 | tracking/event ตก | dev | **หยุดใช้งบประมาณตัดสินใจ** จนแก้เสร็จ |

---

## 6. เอกสารที่ต้องมี (และคนมักไม่มี)

1. **Unit economics sheet** — AOV, COGS, fee, commission, return, CM, target ROAS/CPA
2. **Creative tracker** — ConceptID, HookID, format, launch date, spend, hook rate, CPA, status
3. **Hook bank** — hook ที่ work/ไม่ work, ใช้ซ้ำได้
4. **Test log** — สมมติฐาน, ช่วงเวลา, ผล, ข้อสรุป (กันการทดลองซ้ำ)
5. **Kill criteria log** — เกณฑ์ที่ตั้งไว้ก่อน launch + ผลจริง
6. **Compliance record** — claim ที่อนุมัติ + เอกสารอ้างอิง
7. **Change log** — วันที่เปลี่ยนอะไร ในแคมเปญไหน (สำคัญมากเวลา performance เปลี่ยน)

> ถ้าไม่มี test log และ change log คุณจะเรียนรู้ช้ากว่าคนที่มี 2–3 เท่า เพราะไม่รู้ว่าอะไรทำให้เกิดอะไร

---

## 7. บทบาทในทีมขั้นต่ำ (หรือ 1 คนทำทั้งหมด)

| บทบาท | งานหลัก | ถ้ามี 1 คน |
|---|---|---|
| Media buyer | โครงสร้าง, งบ, bid, scale | ✔ |
| Creative strategist | hook, brief, direction | ✔ |
| Creator/producer | ถ่าย, ตัด | ใช้ UGC/creator |
| Analyst | dashboard, measurement | ✔ (อัตโนมัติด้วย sheet) |
| Compliance reviewer | ตรวจ claim | ใช้ checklist + outsider check |

**ถ้าเป็นทีม 1 คน:** ทำตามจังหวะงานในข้อ 1 อย่างเคร่งครัด และใช้ AI ตามบท 11 — งานที่ต้อง "ตัดสินใจ" มีแค่ 3 ข้อ/สัปดาห์

---

## 8. ปฏิทินรายปี (ไทย)

| เดือน | event / สิ่งที่ต้องเตรียม |
|---|---|
| ม.ค. | ปีใหม่, ตั้งระบบปีใหม่, ตรวจ tracking |
| ก.พ.–มี.ค. | Valentine, Summer เริ่ม, เตรียม 3.3 |
| เม.ย. | Songkran (ยอดอาจตกช่วง 13–15) |
| พ.ค.–มิ.ย. | เตรียม 6.6, mid-year sale |
| ก.ค.–ส.ค. | 7.7, 8.8, back-to-school |
| ก.ย. | 9.9 (ใหญ่) |
| ต.ค. | 10.10, เตรียม 11.11 |
| พ.ย. | **11.11** (ใหญ่สุด), เตรียม 12.12 |
| ธ.ค. | **12.12**, year-end, Christmas |

**กฎ:** เตรียม creative + stock ล่วงหน้า **2–3 สัปดาห์** ก่อน event; เพิ่มงบ 1.5–3× ในช่วง 3 วันรอบ event; อย่าเปลี่ยนโครงสร้าง campaign กลาง event

---

## อ้างอิงบทนี้
กลุ่ม `benchmarks`, `shop` ใน [`SOURCES.md`](SOURCES.md)
