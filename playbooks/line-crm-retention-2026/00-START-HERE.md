# LINE OA × CRM × Retention/LTV Playbook 2026 (TH)

> **ฉบับสำหรับคนและสำหรับ AI** — อ่านจบแล้วตัดสินใจได้ ไม่ใช่แค่เข้าใจ
> ขอบเขต: LINE Official Account · LINE Ads · MyShop / chat commerce · MyCustomer CRM · loyalty · lifecycle flows · LTV/cohort measurement · PDPA
> ตลาด: ไทยเป็นหลัก (THB) · ข้อมูล ณ 2026-11-06

---

## TL;DR 10 ข้อ

1. **TikTok/Meta คือที่หาคน — LINE คือที่ทำกำไร** ถ้า CM ต่อออเดอร์แรกเหลือ 15–20% (ดู TikTok playbook บท 04) คุณจะอยู่ไม่ได้ถ้าไม่มีออเดอร์ที่ 2
2. **ตัวเลขที่ต้องรู้ก่อนทำอะไรทั้งสิ้น: 90-day repeat purchase rate แยกตาม source** ไม่ใช่ blended LTV — เพราะ blended LTV ซ่อน cohort ที่แย่ไว้
3. **LINE ไม่ใช่ช่องโฆษณา มันคือช่องความสัมพันธ์** ตัววัดหลักคือ block rate (<5%) และต้นทุนต่อออเดอร์ที่ 2 ไม่ใช่ reach
4. **ต้นทุนจริงของ LINE ถูกมากเมื่อเทียบกับ paid media** — Pro ฿1,780/เดือน = ฿21,360/ปี ซึ่งน้อยกว่างบ TikTok 2–3 วัน แต่ทำงานได้เฉพาะเมื่อมี segmentation
5. **ถ้าไม่มี tag standard = ไม่มี CRM** LINE OA ที่ไม่มี tag มาตรฐานคือกล่องข้อความ ไม่ใช่ระบบลูกค้า
6. **อย่าส่งให้ทุกคน** ทุกครั้งที่ broadcast ทั้งฐาน = จ่ายเงินเพื่อรบกวนคนที่ไม่สนใจ → block rate พุ่ง
7. **Broadcast 2–4 ครั้ง/เดือนคือค่าตั้งต้น** ไม่ใช่ 2–4 ครั้ง/สัปดาห์ (นั่นคือของ SME บางประเภทที่ยอมรับ block rate สูงได้)
8. **RFM ทำได้ด้วย SQL query เดียว** ไม่ต้อง ML — NTILE(5) สามครั้ง แล้ว map เป็น 11 segment พร้อม action
9. **PDPA: consent ต้องแยกจาก consent ของบริการ, ห้าม pre-tick, ต้องถอนได้ง่ายเท่าที่ให้** และมี พ.ร.บ.ขายตรง/การตลาดตรง อีกชั้นที่หลายคนลืม
10. **ตัวเลข "chat commerce ปิดยอด 85–98%" เป็น vendor claim** อย่าเอาไปใส่ deck โดยไม่ระบุที่มา — ใช้เป็นทิศทาง ไม่ใช่เป้า

---

## แก่นของ playbook นี้ (ประโยคเดียว)

> **Acquisition buys the first order; retention buys the company.**

TikTok playbook บอกว่า "creative คือคันเร่ง" — playbook นี้บอกว่า **"cohort คือเข็มทิศ"** เพราะทุกครั้งที่คุณตัดสินใจเพิ่มงบหาแขกใหม่ คุณกำลังเดิมพันว่า cohort นั้นจะกลับมาซื้อซ้ำใน 45–90 วัน ถ้าไม่กลับ คุณไม่ได้ scale คุณกำลังจ่ายเงินซื้อการขาดทุนซ้ำ ๆ

**ลำดับการวินิจฉัยเมื่อธุรกิจ "ขายดีแต่ไม่เหลือกำไร":**
```
(1) unit economics ต่อออเดอร์แรก → (2) 90-day repeat by source → (3) time to 2nd order
→ (4) flow coverage → (5) segmentation quality → (6) broadcast discipline → (7) acquisition
```

กลับกับสัญชาตญาณของคนส่วนใหญ่ที่เริ่มจาก (7)

---

## แผนที่บท

| บท | เนื้อหา | ใช้เมื่อ |
|---|---|---|
| [01](01-market-2026.md) | ตลาด LINE ไทย 2026 · 5 สิ่งที่เปลี่ยน · ทำไม retention ถึงเป็นวาระเร่งด่วน | ตั้งสมมติฐานก่อนวางแผน |
| [02](02-line-oa-foundation.md) | ตั้ง OA ให้ถูกตั้งแต่ต้น · เลือกแพ็กเกจด้วยคณิตศาสตร์ · rich menu · chat tag | เริ่มใหม่หรือรื้อของเดิม |
| [03](03-acquisition-friend-growth.md) | หา friend ให้คุ้ม · QR · LINE Ads · CPF campaign · source tagging | ต้องการฐานที่โต |
| [04](04-segmentation-rfm.md) | tag standard · RFM 11 segment · action map · cap ความถี่ | มีข้อมูลพอจะแบ่งกลุ่ม |
| [05](05-lifecycle-flows.md) | welcome · 2nd purchase · replenishment · win-back · flow benchmarks | อยากได้รายได้ที่ไม่ต้องจ่ายค่า ads |
| [06](06-broadcast-playbook.md) | จังหวะ · quota math · โครง 3 bubble · เวลาไทย · คุม block rate | ส่งข้อความทุกเดือน |
| [07](07-chat-commerce-myshop.md) | ขายผ่าน 1:1 · MyShop · สคริปต์ปิดการขาย · LINE Shopping | อยากปิดยอดในแชท |
| [08](08-loyalty-membership.md) | Reward Card vs MyCustomer CRM · point/tier · referral · LINE GIFT | มีลูกค้าซื้อซ้ำแล้ว |
| [09](09-measurement-ltv.md) | LTV ที่ไม่โกหก · cohort · payback · attribution · MER | ต้องตัดสินใจงบ |
| [10](10-compliance-pdpa.md) | PDPA · พ.ร.บ.ขายตรง · consent design · opt-out · sensitive data | ก่อนเก็บข้อมูลใด ๆ |
| [11](11-tools-stack.md) | native vs third-party · ราคา · build vs buy · ข้อจำกัด webhook | กำลังเลือกเครื่องมือ |
| [12](12-operating-cadence.md) | จังหวะรายวัน/สัปดาห์/เดือน · KPI tree · ทีมขั้นต่ำ · ปฏิทินไทย | วาง ops |
| [13](13-diagnostics-antipatterns.md) | diagnostic ladder · symptom→cause→action · 20 anti-patterns · recovery | มีปัญหา ต้องแก้เร็ว |

**ไฟล์ประกอบ**
- [`METRICS.md`](METRICS.md) — นิยาม + สูตร + threshold ของทุกตัวชี้วัด
- [`SOURCES.md`](SOURCES.md) — แหล่งอ้างอิงพร้อมระดับความน่าเชื่อถือ
- [`playbook.json`](playbook.json) — กฎที่เครื่องอ่านได้ (rule ID + stage routing)
- [`benchmarks.json`](benchmarks.json) — ตัวเลขพร้อม `as_of` + `source_type`

---

## 4-week starter plan

```
สัปดาห์ 1  ตรวจสถานะ: 90-day repeat by source, time to 2nd order, block rate, plan/overage
           ติดตั้ง tag standard (source / stage / value) — ห้ามข้ามข้อนี้
สัปดาห์ 2  Welcome flow (3 ข้อความ) + greeting + rich menu 4 ปุ่ม
           เปิด source tagging ทุกจุดที่แจก QR
สัปดาห์ 3  2nd-purchase flow (trigger: วันที่ 7 หลังออเดอร์แรก, ตามรอบใช้สินค้า)
           broadcast แรกแบบ segmented (ไม่ใช่ all-friends)
สัปดาห์ 4  รัน RFM รอบแรก → 11 segment → ตั้ง cap ความถี่
           ตั้ง dashboard 12 ตัวเลข (ดู METRICS.md)
```

---

## วิธีใช้กับ AI

1. โหลด `AGENTS.md` ที่ root ของ repo — กฎ epistemic ใช้ร่วมกันทุก playbook
2. โหลด `playbook.json` — 27 rules (R-101…R-180) + stage routing: `foundation` / `grow` / `segment` / `automate` / `sell` / `loyalty` / `fix`
3. โหลด `benchmarks.json` — ห้ามแต่งตัวเลขใหม่ ตัวเลขทุกตัวมี `as_of` + `source_type`
4. Output ที่ต้องมีเสมอ: **assumptions · primary KPI · guardrails · segment plan · flow plan · broadcast calendar · measurement plan · kill criteria**

**ตัวอย่าง prompt**
```
ใช้ playbook LINE OA × CRM ใน repo นี้ วางแผน 90 วันให้แบรนด์สกินแคร์
(AOV ฿890, CM 16%, มี TikTok Shop, LINE friends 6,000, ยังไม่มี CRM)
พร้อมระบุ: segment ที่จะโฟกัส, flow 3 ตัวแรก, ปฏิทิน broadcast 8 สัปดาห์,
ตัวเลขที่ต้องวัดทุกสัปดาห์ และเกณฑ์ที่จะบอกว่า "หยุด" (kill criteria)
```

---

## ข้อจำกัดของ playbook นี้

- ตัวเลขหลายตัวเป็น **vendor-reported** (โดยเฉพาะ chat commerce conversion 85–98% และ CPM ฿15) — ใช้เป็นกรอบ ไม่ใช่เป้า
- LINE เปลี่ยน pricing และฟีเจอร์บ่อย (ปรับแพ็กเกจ ส.ค. 2567, เพิ่ม MyCustomer, Target Reach) → **re-verify ทุกไตรมาส**
- Benchmark retention ส่วนใหญ่มาจาก DTC ตะวันตก — โครงสร้างตลาดไทยต่าง (marketplace สัดส่วนสูง, COD สูง, return rate สูงใน fashion) → ปรับก่อนใช้
- playbook นี้ไม่ใช่ที่ปรึกษากฎหมาย ส่วน PDPA/พ.ร.บ.ขายตรงต้องให้ที่ปรึกษาตรวจอีกครั้ง

---

## 🗂️ ที่เก็บสำเนา

| ที่ | ลิงก์ | เนื้อหา |
|---|---|---|
| Git (source of truth) | `github.com/poppath/AI_research` → `playbooks/line-crm-retention-2026/` | ครบทุกบท + JSON |
| Notion | [LINE OA × CRM × Retention/LTV Playbook 2026 (TH)](https://app.notion.com/p/LINE-OA-CRM-Retention-LTV-Playbook-2026-TH-41176ada348881399a95e49da3842858) | สรุปทุกบท + ตาราง decision + flow + anti-patterns |
| Google Docs | [ฉบับอ่าน/แชร์](https://docs.google.com/document/d/1NcTC3CIYyDC_i9hnhBKgu9jMX4FHBxfKk1pqAd4VnuM/edit) | สรุป 14 หัวข้อ ภาษาไทย อ่านบนมือถือได้ |


---

## 🔗 เล่มที่ใช้คู่กัน

- **ก่อนเล่มนี้:** [`../profit-unit-economics-2026/`](../profit-unit-economics-2026/00-START-HERE.md) · **Profit & Unit Economics 2026 (TH)** — นิยาม CM2, take rate ของแต่ละช่องทาง, breakeven CAC/LTV และ price floor
  → สูตรในบท 08–09 ของเล่มนี้ (LTV₉₀:CAC, breakeven repeat) ต้องใช้ CM ที่คำนวณจากเล่มนั้น
- **เล่มก่อนหน้า:** [`../tiktok-performance-marketing/`](../tiktok-performance-marketing/00-START-HERE.md) — TikTok หาแขก, LINE เก็บแขก
- **ข้อควรระวังเรื่องสัญกรณ์:** เล่มนี้ใช้ `CM₁`/`CM₂` = CM ของ**ออเดอร์ที่ 1/2** · profit playbook ใช้ `CM1`/`CM2` = **ลำดับการหักต้นทุน** (ก่อน platform fee / ก่อนการตลาด) — ห้ามปนกัน

อัปเดตล่าสุด: 2026-11-07
