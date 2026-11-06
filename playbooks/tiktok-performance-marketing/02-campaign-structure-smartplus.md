# 02 · โครงสร้างแคมเปญ & Smart+

> **TL;DR** — ใช้ **สองเลนคู่กันเสมอ**: (1) **Smart+** สำหรับ scale และ (2) **manual/ABO** สำหรับอ่านสัญญาณ creative แบบสะอาด. ถ้าใช้แต่ Smart+ คุณจะ scale ได้แต่จะไม่รู้ว่าอะไรทำให้ work; ถ้าใช้แต่ manual คุณจะไม่มีวันชนะ auction ระยะยาว

---

## 1. โครงสร้าง 3 ชั้นของ TikTok

```
Campaign   → objective + งบ (CBO) + ชื่อที่ parse ได้
  Ad Group → audience + placement + optimization event + bid strategy + งบ
    Ad     → creative + caption + CTA + destination
```

**กฎที่ห้ามละเมิด:**
- 1 campaign = 1 objective (ห้ามผสม)
- 1 ad group = 1 ประเภท audience (ห้าม stack interest 5 อย่าง)
- 1 optimization event ต่อ ad group — และ event นั้นต้องมี ≥20 conversions/สัปดาห์ ไม่งั้น "Learning limited"

---

## 2. Smart+ คืออะไร และเหมาะกับใคร

**นิยาม:** campaign type ที่ AI รวม creative selection + audience + bidding + placement แล้ว optimize ไปที่ KPI ที่คุณตั้ง (Traffic / Sales / Lead Gen / App Promotion)

**สถานะ 2026:**
- รองรับ **สูงสุด 50 asset groups** (Help page ส.ค. 2026 — ก่อนหน้านี้ 30) [vendor: socialscalehub]
- เปิด/ปิด automation รายโมดูลได้ (targeting / budget / catalog ads / placements) — พ.ค. 2026
- **Smart+ Search Ads** เพิ่ม Q3 2026
- มี **Bid Protection** (โปรโมชันจำกัดเวลา): refund overspend เป็น ad credit ถ้าใช้ Cost Cap / Min ROAS / Target ROAS, รัน ≥3 วันติด, ได้ ≥15 conversions, และอยู่ใน edit limit [vendor: soku]

**ตัวเลขที่ TikTok อ้าง (ใช้เป็น marketing claim ไม่ใช่ forecast):**

| Claim | ค่า | ที่มา |
|---|---|---|
| CPA ดีขึ้น vs manual | 29% | TikTok blog 13 พ.ค. 2026 [tiktok via vendor] |
| ROAS ดีขึ้น | สูงสุด 52% / 53% / 64% | หลายแหล่ง ไม่ตรงกัน → **เชื่อทิศทาง ไม่เชื่อตัวเลข** |
| CPA ลด | ~32–36% | [vendor] |
| Case: PHLUR | +28% ROAS, −14% CPA | [vendor] |
| Case: Dr. Squatch | 1.6× ROAS | [vendor] |
| Case: Fabletics | −11% CAC | [vendor] |

> **อ่านอย่างไร:** ตัวเลขพวกนี้มาจาก advertiser ที่มี creative library หนาและ tracking สะอาด. ถ้าคุณยังไม่มีสองอย่างนั้น Smart+ จะ *แย่กว่า* manual เพราะมัน amplify สัญญาณที่ผิด

---

## 3. Smart+ vs Manual — decision table

| สถานการณ์ | เลือก | เหตุผล |
|---|---|---|
| เพิ่งเริ่ม, ยังไม่รู้ CPA | **Manual ABO + Lowest Cost** | ต้องอ่านสัญญาณก่อน ยังไม่รู้ว่า target ควรเป็นเท่าไหร่ |
| มี CPA/ROAS ที่นิ่งแล้ว, ต้องการ scale | **Smart+ (Target CPA / Min ROAS)** | AI หา incremental audience ได้ถูกกว่า |
| ต้อง isolate creative test | **Manual ABO** | Smart+ จะ blend ทำให้อ่านผลไม่ได้ |
| ขาย TikTok Shop | **GMV Max** (ไม่ใช่ Smart+) | GMV Max ผูกกับ Shop catalog + attribution ทั้งShop |
| Regulated (health/finance) | **Smart+ แต่ปิด placement automation** | ต้องคุม ad placement ที่ต้อง review |
| Multi-market เดียวกัน creative | **แยก campaign ตามประเทศ** | อย่าใส่หลายประเทศใน ad group เดียว |
| Launch สินค้าใหม่ที่ต้องการคุม message | **Manual + Spark Ads** | คุม narrative ได้ |

**คำแนะนำจาก practitioners ที่สอดคล้องกันหลายแหล่ง:** *"default ให้ Smart+ สำหรับ objective performance ส่วนใหญ่ แต่เก็บ manual/DR campaign ไว้ 1 ตัวแบบขนาน เมื่อต้องการ creative-test data ที่แยกได้ หรือต้องคุม audience สำหรับ launch"* [vendor: adfirm]

---

## 4. สามโครงสร้างที่ใช้ได้จริง

### โครงสร้าง A — Cold start / ยังไม่มีข้อมูล (งบ ≤ ฿150k/เดือน)

```
[ABO] Conversions — Test
├── AG1: Broad (อายุ+geo เท่านั้น)           งบ = 10× CPA ประมาณการ
│    ├── Concept A · Hook 1
│    ├── Concept A · Hook 2
│    └── Concept B · Hook 1
└── AG2: Interest / Lookalike 1% (ถ้ามี data)  งบ = 10× CPA
     ├── Concept B · Hook 2
     ├── Concept C · Hook 1
     └── Concept C · Hook 2
```
- Bid: Lowest Cost (ไม่มี cap) — ปล่อยให้ AI หา CPA ตามธรรมชาติ ก่อน
- ห้ามแตะ 7 วัน
- เป้าอ่านผล: **creative-level**, ไม่ใช่ ad-group-level

### โครงสร้าง B — Scale (มี CPA/ROAS นิ่งแล้ว)

```
[Smart+] Sales — Target CPA / Min ROAS
├── Asset group 1: hook "problem"     (6-10 creative)
├── Asset group 2: hook "social proof" (6-10 creative)
└── Asset group 3: hook "demo/result"  (6-10 creative)

[Manual] Conversions — Control (10-15% ของงบ)
└── AG1: Broad + proven creatives  →  ใช้เป็น benchmark/cannibalization check
```

### โครงสร้าง C — Shop (TikTok Shop)

```
[GMV Max] Product — Target ROI 2.0-3.0x (ช่วงเรียน)
   ↑ ใช้ creative ที่ authorize แล้ว ≥15-20 ชิ้น/SKU

[Manual/Spark] Brand + Affiliate boost (ถ้าต้องการคุม narrative)
[LIVE GMV Max] เฉพาะวันที่มีไลฟ์ (แยก campaign)
```

---

## 5. Optimization event — เลือกให้ถูกตั้งแต่แรก

| Event | ใช้เมื่อ | ข้อควรระวัง |
|---|---|---|
| **Complete Payment / Purchase** | e-commerce ที่มี volume พอ | ดีที่สุดเพื่อหาก "คนซื้อ" ไม่ใช่ "คนกด" |
| **Initiate Checkout** | Purchase เกิดน้อยกว่า ~20/สัปดาห์ | ระวังได้คนที่ทิ้งตะกร้า |
| **Add to Cart** | ใช้ชั่วคราวเพื่อออกจาก learning limited | อย่าอยู่นาน — จะ optimize ผิดเป้า |
| **Lead (form)** | service/B2B | ต้องมี CRM feedback เพื่อวัด qualified lead |
| **Complete Registration** | app/SaaS | ระวังคุณภาพหลังบ้าน |
| **Value-based (VBO)** | margin ต่างกันมากระหว่าง SKU | ต้องส่ง `value` + `currency` ให้ครบ ไม่งั้น VBO ไม่ทำงาน |

> **กฎ:** optimize ที่ event ที่ใกล้รายได้ที่สุด *ที่ยังมี volume พอ*. ถ้า Purchase น้อยเกินไป ให้ขยับขึ้นไป 1 ขั้น **ชั่วคราว** พร้อมแผนกลับลงมาเมื่อ volume พอ

---

## 6. การตั้งชื่อ (naming convention) — สำคัญกว่าที่คิด

AI และทีมอ่านรายงานจากชื่อ. ถ้าชื่อไม่ parse ได้ คุณจะรายงานไม่ได้

```
{CampaignType}_{Objective}_{Audience}_{Market}_{YYYYMM}_{Owner}
เช่น:  SP_Sales_Broad_TH_202611_POP
       ABO_Conv_LAL1_TH_202611_POP
       GMV_Product_SKU123_TH_202611_POP

Ad name: {ConceptID}_{HookID}_{Format}_{Length}_{Version}
เช่น:  C07_H02_UGC_15s_v3
```

**ทำไมต้องมี ConceptID/HookID:** เพราะจะเอาไป join กับ creative-level report และกับตารางในบท 03 ได้ทันที

---

## 7. Learning phase — กติกาที่คนมักฝ่าฝืน

| เงื่อนไขออกจาก learning | ค่า |
|---|---|
| จำนวน optimization events | ~50 conversions ภายใน 7 วัน (ต่อ ad group) |
| งบขั้นต่ำ | ≥ $50/วันต่อ ad group (practical), platform min $20 |
| ระยะเวลาไม่แตะ | 7 วัน (Smart+), 3–5 วัน (manual) |
| งบแนะนำ | 10× CPA (max delivery), 30× CPA (target CPA/min ROAS), ไม่น้อยกว่า 10× |

**สาเหตุ "Learning limited" ที่พบบ่อย:**
1. งบต่ำกว่า 10× CPA
2. optimization event เกิด <20 ครั้ง/สัปดาห์ → เปลี่ยน event ให้ถี่ขึ้นชั่วคราว
3. pause/เปิด ad group ซ้ำ ๆ
4. bid cap ต่ำเกิน

---

## 8. กับดักโครงสร้าง (anti-patterns)

| ❌ ทำ | ทำไมพัง | ✅ ทำแทน |
|---|---|---|
| 15 ad groups × งบ ฿500 | ไม่มี group ไหนถึง 50 conversions | 2–3 groups × งบมากพอ |
| แยก campaign ตาม creative | fragmented, ทุกกลุ่มเรียนไม่จบ | รวม creative ใน group เดียว, แยกด้วยชื่อ |
| ใส่ 5 ประเทศใน 1 ad group | auction คนละราคา, อ่านผลไม่ได้ | แยก campaign ตามประเทศ |
| ใช้ CBO ตั้งแต่ยังไม่มีข้อมูล | งบไหลไป group ที่ฟลุ๊ก | ABO ก่อน, CBO เมื่อมี 2–3 group ที่พิสูจน์แล้ว |
| ปิด campaign วันที่ 3 | ยังไม่ถึง 50 conversions = สุ่ม | ตั้ง kill criteria ล่วงหน้าเป็นวัน ไม่ใช่อารมณ์ |
| เปิด auto-select creative ทั้งหมดใน Smart+ ทันที | ไม่รู้ว่าอะไรชนะ | เริ่ม 8–12 asset group ที่เป็น hypothesis ต่างกันจริง |

---

## 9. Checklist ก่อนกด Publish

- [ ] tracking ยิง event ที่จะ optimize ถูกต้อง + dedup แล้ว
- [ ] objective ตรงกับ KPI ที่จะรายงาน
- [ ] งบ ≥ 10× CPA ประมาณการ ต่อ ad group
- [ ] creative ≥ 3–6 ชิ้น (manual) / ≥ 6 (Smart+) — และเป็น 9:16
- [ ] ชื่อ campaign parse ได้ตาม convention
- [ ] มี exclusion: recent purchasers (30/60/90 วันตามรอบซื้อ)
- [ ] ตั้ง kill criteria + วันตัดสิน ไว้ในเอกสารแล้ว
- [ ] ผ่าน compliance checklist บท 10

---

## อ้างอิงบทนี้
กลุ่ม `smartplus`, `structure`, `budget` ใน [`SOURCES.md`](SOURCES.md)
