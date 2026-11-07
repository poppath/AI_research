# TikTok Performance Marketing Playbook 2026
### Playbook สำหรับ AI — สร้าง Performance ที่ดีบน TikTok (Paid + Shop + Affiliate + LIVE)

> **เวอร์ชัน:** 1.0 · **อัปเดต:** 6 พ.ย. 2026 · **ตลาดหลัก:** ประเทศไทย (เทียบ global/US)
> **สถานะข้อมูล:** ทุกตัวเลขมีวันที่กำกับ — ตัวเลขที่เก่ากว่า 90 วันต้อง re-verify ก่อนใช้ตัดสินใจงบ

---

## 🎯 TL;DR — 10 ข้อที่ต้องรู้ก่อนอ่านอะไรทั้งหมด

1. **TikTok 2026 = automation-first.** Smart+ (web/app/lead) และ GMV Max (Shop) คือ default. ของที่คุณ "คุม" ได้จริงเหลือ 4 อย่าง: **creative, product feed, offer, target ROAS/CPA** — targeting ที่เหลือปล่อย AI [1][6][7]
2. **Creative คือคันเร่ง ไม่ใช่ targeting.** เวลา performance ตก ลำดับการ diagnose คือ creative fatigue → offer → tracking → bid → audience (กลับลำดับนี้คือการเผาเงิน) [2][6]
3. **Hook 3 วินาทีแรกตัดสิน 80% ของผลลัพธ์.** TikTok ตัดสินใจเร็วกว่า Meta — Meta ให้ 2–3 วิ, TikTok ให้ ~1–3 วิ. เอา 90% ของแรง creative ไปลงที่ hook [6-rig][creative]
4. **อย่าตัดสินแคมเปญก่อนมี signal.** conversion campaign ต้องการ ~50 conversions/7 วัน ต่อ ad group และงบ ≈10× CPA. ต่ำกว่านั้น "มันไม่เวิร์ก" ยังไม่ใช่ข้อสรุปที่ถูก [1][cost]
5. **Scale แบบมีกฎ:** +20–30% ทุก 3–5 วัน (post-learning), ไม่เกิน +40% ต่อครั้งตอนยัง learning, ห่างกันอย่างน้อย 2 วัน [scale]
6. **ยอด ROAS บน dashboard ไม่ใช่ความจริง.** platform over-credit 30–60%; native default = 7-day click / 1-day view. ต้องมี Events API + blended ROAS + incrementality [meas]
7. **Shop ชนะด้วย creator volume ไม่ใช่ ad budget.** ลำดับที่ถูก: **catalog → creator/affiliate volume → GMV Max → LIVE**. เริ่มจาก ads ก่อน = GMV Max อดตาย [shop][gmv]
8. **ไทยคือตลาดที่ TikTok Shop โตแรงติด top ของโลก** — GMV ครึ่งปี 2025 ~$5.9B ติดอันดับ 3 ของโลก; ผู้ใช้ ~44–46M/เดือน. TikTok แซง YouTube เป็นสื่อดิจิทัลอันดับ 2 ของไทย (งบ 6,776 ลบ., +63% YoY, DAAT 2025) [th]
9. **CPM ไทยยังถูกกว่า Meta อย่างมีนัยสำคัญ** — ฿50–200 (in-feed), CPC ฿1–5. แต่ conversion rate ต่ำกว่า → ต้องคิดถึง **CPA และ margin** ไม่ใช่ CPM [th-cost]
10. **Compliance เป็นเรื่องของ performance ไม่ใช่แค่ legal.** TikTok 2026: ปิด Custom Identity (ต้องผูก verified business account), แบน AI endorsement, เข้ม health claims; ไทย: Thai FDA sweep มี.ค. 2026 ยิงตรง supplement/influencer [policy]

---

## 🗺️ แผนที่ playbook (อ่านตามลำดับ)

| # | บท | ตอบคำถามอะไร | ใช้ตอนไหน |
|---|---|---|---|
| 01 | [ภาพรวมตลาด & สิ่งที่เปลี่ยนใน 2026](01-market-2026.md) | TikTok 2026 ต่างจาก 2024 ยังไง, ไทยอยู่ตรงไหน | ก่อนวางแผน |
| 02 | [โครงสร้างแคมเปญ & Smart+](02-campaign-structure-smartplus.md) | จะตั้ง campaign/ad group ยังไง, automation แค่ไหน | ตอน setup |
| 03 | [Creative System & Hook Engineering](03-creative-system.md) | จะผลิต hook/creative ยังไงให้ไม่ตาย, refresh เมื่อไหร่ | ตลอดเวลา (สำคัญสุด) |
| 04 | [TikTok Shop, GMV Max & Affiliate](04-shop-gmvmax-affiliate.md) | จะโตยอดขาย Shop ยังไงให้กำไร | ถ้าขาย Shop |
| 05 | [LIVE Commerce](05-live-commerce.md) | ไลฟ์ให้คุ้ม, LIVE GMV Max, 30/60/90 | ถ้ามีไลฟ์ |
| 06 | [Audience, Targeting & Search Ads](06-audience-targeting-search.md) | broad vs interest, TikTok SEO, search ads | ตอนตั้ง targeting + SEO |
| 07 | [Bidding, Budget & Scaling](07-bidding-budget-scaling.md) | งบเท่าไหร่, bid อะไร, scale ยังไงไม่พัง CPA | ตอน launch + scale |
| 08 | [Measurement & Attribution](08-measurement-attribution.md) | จะรู้ได้ยังไงว่าคุ้มจริง, blended ROAS, incrementality | ก่อนยิงเงิน |
| 09 | [Organic × Paid Flywheel](09-organic-paid-flywheel.md) | ออร์แกนิกช่วย paid ยังไง, Spark Ads, posting cadence | วาง content engine |
| 10 | [Compliance ไทย + TikTok Policy](10-compliance-th.md) | พูดอะไรไม่ได้, PDPA, Thai FDA | ก่อนเขียน copy |
| 11 | [AI Stack & Automation Workflow](11-ai-stack-workflows.md) | ใช้ AI ตรงไหนของงาน, tool อะไรคุ้ม | เพิ่ม productivity |
| 12 | [Operating Cadence & KPI Dashboard](12-operating-cadence.md) | ทำอะไรทุกวัน/สัปดาห์/เดือน, KPI ไหน | หลัง launch |
| 13 | [Diagnostics & Anti-patterns](13-diagnostics-antipatterns.md) | อาการ → สาเหตุ → สั่งการ | เวลา performance ตก |
| — | [Metrics & Benchmarks](METRICS.md) | นิยาม metric + สูตร | อ้างอิง |
| — | [SOURCES.md](SOURCES.md) | แหล่งอ้างอิงทั้งหมด | ตรวจสอบ |
| — | [playbook.json](playbook.json) | กฎที่เครื่องอ่านได้ | AI execute |
| — | [benchmarks.json](benchmarks.json) | ตัวเลข + วันที่ + source_type | AI อ้างอิง |

---

## ⚡ 30 วินาที: ถ้าต้องเริ่มวันนี้ ด้วยงบจำกัด

```
สัปดาห์ 1   →  ตรวจ tracking (Pixel + Events API + EMQ) · ตั้ง verified business account · นิยาม CPA/ROAS เป้าหมายจาก margin
สัปดาห์ 1-2 →  ผลิต 8-12 creative (4 concepts × 2-3 hooks) · 9:16 1080×1920 · 9-15 วิ · hook ใน 1-3 วิแรก
สัปดาห์ 2   →  ABO testing campaign: 1 campaign / 2-3 ad group / งบ ≥10× CPA ต่อ group / Lowest Cost
สัปดาห์ 2-3 →  ห้ามแตะ 7 วัน · อ่าน creative-level report · kill ตัวที่ต่ำกว่า ROAS floor
สัปดาห์ 3-4 →  ย้าย winner เข้า Smart+ (≥6 creative, ≥30× CPA ถ้าใช้ target CPA/ROAS) · เก็บ manual ไว้ 1 campaign
สัปดาห์ 4+  →  +20-30% ทุก 3-5 วัน · refresh 2-3 creative/สัปดาห์ · รายงาน blended ROAS ไม่ใช่ platform ROAS
```

---

## 🧠 วิธีใช้กับ AI (สำหรับ agent)

1. อ่าน `AGENTS.md` (กฎ epistemic)
2. โหลด `playbook.json` → ใช้ `rules[]` เป็น decision table
3. โหลด `benchmarks.json` → ใช้เป็นตัวเลขอ้างอิง (ห้ามแต่งเลขใหม่)
4. เปิดบทที่ตรงกับ `context.stage` (launch / scale / fix / shop / live)
5. ตอบกลับตาม **Output rules** ใน `AGENTS.md` §4 (ต้องมี kill criteria เสมอ)

**ตัวอย่าง prompt ที่ให้ผลดี:**
> "ใช้ playbook TikTok ใน repo นี้ วางแผน 60 วัน ให้แบรนด์ X (AOV ฿890, gross margin 55%, งบ ฿300k/เดือน, สินค้า beauty, มี TikTok Shop). ระบุ assumption, KPI, structure, creative plan, measurement plan, kill criteria"

---

## ⚠️ ข้อจำกัดของ playbook นี้

- ตัวเลขส่วนใหญ่เป็น **vendor-reported ranges** ไม่ใช่ controlled test — ใช้เป็น "กรอบ" ไม่ใช่ "เป้า"
- TikTok เปลี่ยน product บ่อยมาก (2026 มี Smart+ upgraded, 50 asset groups, Symphony Agent, GMV Max Pro) → **re-verify ทุกไตรมาส**
- performance ขึ้นกับ margin/offer/ logistics มากกว่าตัวเลข ads — playbook นี้ไม่ใช่ silver bullet

---

## 🗂️ ที่เก็บสำเนา

| ที่ | ลิงก์ | เนื้อหา |
|---|---|---|
| Git (source of truth) | [github.com/poppath/AI_research](https://github.com/poppath/AI_research) → `playbooks/tiktok-performance-marketing/` | ครบทุกบท + `playbook.json` + `benchmarks.json` |
| Notion | [TikTok Performance Playbook 2026 (TH) — Paid × Shop × GMV Max × Affiliate × LIVE](https://app.notion.com/p/TikTok-Performance-Playbook-2026-TH-Paid-Shop-GMV-Max-Affiliate-LIVE-41076ada3488811082f3ff29bc2a1dd5) | สรุปทุกบท + ตาราง decision 2 ตาราง + anti-patterns |
| Google Docs | [TikTok Performance Playbook 2026 — Notes (TH)](https://docs.google.com/document/d/1c3ZzV3mA-6XtgLSJuB-pL_5MFIjMkKzfFzI2Po4GoPo) | ฉบับอ่าน/แชร์ 17 หัวข้อ (notes) |

อัปเดตล่าสุด: 2026-11-06 · ตัวเลขทั้งหมดอ้างอิง ณ วันนี้ (ดู freshness rule ใน `benchmarks.json`)

---

## เล่มถัดไป (อ่านต่อ)

TikTok playbook ตอบว่า "หาแขกยังไงให้ถูก" — แต่ CM ต่อออเดอร์แรกเหลือ ~16% แปลว่ากำไรจริงอยู่ที่ออเดอร์ที่ 2
→ [`../line-crm-retention-2026/`](../line-crm-retention-2026/00-START-HERE.md) · **LINE OA × CRM × Retention/LTV 2026 (TH)**
ต่อกันตรง: TikTok (บท 04 unit economics + บท 08 measurement) → LINE (บท 05 lifecycle flows + บท 09 LTV)

**ฐานของทั้งสองเล่ม:** [`../profit-unit-economics-2026/`](../profit-unit-economics-2026/00-START-HERE.md) · **Profit & Unit Economics 2026 (TH)**
เล่มนั้นนิยาม CM1/CM2/CM3, take rate จริงของแต่ละ marketplace, breakeven ROAS/MER/CAC และ price floor — ตัวเลข "CM ~16%" ที่ TikTok playbook อ้างถึง คำนวณและอธิบายที่มาที่นั่น
อัปเดตสำคัญที่กระทบเล่มนี้: **GP cut window 1 ธ.ค. 2026 – 31 พ.ค. 2027** ทำให้ breakeven ROAS บน Shopee/Lazada/TikTok Shop ลดลง ~19% ชั่วคราว แล้วเด้งกลับ มิ.ย. 2027 (ดู profit playbook บท 04 §5)
