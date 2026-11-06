# 06 · Audience, Targeting & Search Ads

> **TL;DR** — ในยุค automation การตั้ง targeting ที่ดีคือ **"ทำให้ AI มีทางเลือกที่ถูกต้อง"** ไม่ใช่ "เลือกคนให้ AI". ใช้ broad เป็นฐาน, ใส่ signal ที่ดี (custom audience, VBO, exclusions) เป็นกรอบ, และใช้ **search** เป็น surface ที่ให้ intent สูงสุดในราคาถูก

---

## 1. หลักคิด 2026: Broad-first แล้วค่อยใส่กรอบ

```
Broad (age + geo เท่านั้น)
   + exclusion ที่จำเป็น (ลูกค้าเดิม, recent purchasers)
   + creative ที่พูดกับ segment เฉพาะ
   ↓
AI หาคนที่ใช่เอง  ← นี่คือวิธีที่ TikTok ออกแบบมาให้ใช้
```

**ทำไม interest targeting ได้ผลน้อยลง:**
- TikTok ย้ายน้ำหนักไปที่ creative + engagement signal มากกว่า declared interest
- interest audiences บน TikTok เล็กและทับซ้อนกันสูง เมื่อเทียบกับ Meta
- ใน Smart+/GMV Max interest ไม่มีให้ใช้เลยในหลาย objective

**เมื่อไหร่ยังควรใช้ interest:** เมื่อ audience แคบมากและต้องการ isolate เพื่อ **ทดสอบ** (ไม่ใช่เพื่อ scale) หรือเมื่อเป็น regulated category ที่ต้องคุมการเข้าถึง

---

## 2. Custom Audiences & Exclusions — lever ที่ยังคุมได้จริง

| ประเภท | ใช้ทำอะไร | ข้อควรระวัง |
|---|---|---|
| Customer file (email/phone) | สร้าง lookalike, exclusion ลูกค้าเดิม | ต้องมี consent ตาม PDPA (บท 10) |
| Engagement audience | คนที่ดูวิดีโอ ≥X%, ไลก์, คอมเมนต์ | ระวังขนาดเล็กเกินไป |
| Website visitor (Pixel) | retargeting ตามหน้า | ต้องมี consent banner ที่ถูกต้อง |
| Add-to-cart / initiate checkout | retargeting ที่ intent สูง | ต้องมี volume พอ ไม่งั้นเล็กเกิน |
| App activity | retarget ในแอป | ต้องมี SDK |

**Exclusions ที่ควรใส่เสมอ:**
- ลูกค้าที่ซื้อใน X วัน (ตามรอบซื้อจริง เช่น 30/60/180)
- พนักงาน/ครีเอเตอร์ของตัวเอง (กัน attribution เพี้ยน)
- กลุ่มที่กฎหมายห้าม (เช่นอายุ <20 สำหรับสินค้าบางหมวดในไทย)

> **2026 policy:** TikTok เข้มขึ้นเรื่อง **first-party data สำหรับ retargeting** — third-party segments ถูกจำกัด ลง [vendor]

---

## 3. Value-Based Optimization (VBO) — ทางลัดสู่กำไร

แทนที่จะ optimize "จำนวน purchase" ให้ optimize "**มูลค่า** ของ purchase"

**ต้องทำ:**
1. ส่ง `value` + `currency` ใน Purchase event ทั้ง Pixel และ Events API
2. ตรวจว่า value ส่งครบทุก SKU (ไม่ใช่ 0 หรือค่าคงที่)
3. ตั้ง Minimum ROAS แทน Target CPA

**เหมาะเมื่อ:** margin ต่างกันมากระหว่าง SKU หรือมี bundle/up-sell ที่ทำให้ order value ต่างกัน 3–5 เท่า

> ถ้า `value` ไม่ครบ → VBO จะ optimize ผิด (มักไปหาสินค้าถูกที่ margin ต่ำ)

---

## 4. TikTok Search — surface ที่คนมองข้าม

### 4.1 ทำไมต้องสน
- ผู้ใช้ที่ค้นหา = **intent สูง** (เทียบเท่า search commerce)
- Search Ads ราคาถูกกว่า in-feed ในหลายหมวด เพราะ competition ต่ำกว่า
- Q3 2026 TikTok เปิด **Smart+ Search Ads** → ใช้ automation ใน search ได้
- คลิปที่ติด search แบบ organic ทำงานต่อเนื่องหลายเดือน (compounding) ต่างจาก FYP ที่จบใน 48 ชม.

### 4.2 Ranking signals ของ TikTok search (2026)

| Signal | น้ำหนัก | ทำอะไร |
|---|---|---|
| Spoken keyword ในวิดีโอ (TikTok ถอดเสียง) | สูง | **พูดคำที่คนค้น ออกเสียงชัด ๆ ใน 10 วิแรก** |
| Caption text ตรงกับ query | สูง | ใส่ phrase ใน caption ≤100 ตัวอักษร |
| On-screen text (OCR) | สูง | เขียน keyword บนจอ frame แรก |
| Hashtag relevance | กลาง | 1–3 hashtag ที่ตรง > ใส่ #fyp |
| Recency | กลาง | โพสต์สม่ำเสมอ |
| Watch % ของวิดีโอนั้น | สูง | เหมือน FYP |
| Creator authority ในหัวข้อ | กลาง | โพสต์เรื่องเดิมซ้ำ ๆ = topical authority |

### 4.3 Keyword research (ฟรีทั้งหมด)

| เครื่องมือ | ที่ไหน | ให้อะไร |
|---|---|---|
| **Creator Search Insights** | ในแอป TikTok (ค้นคำนี้ในช่อง search) | keyword ที่คนค้นจริง + **Content Gap** (ความต้องการสูง/ซัพพลายต่ำ) |
| **TikTok autocomplete** | ช่อง search | phrase จริงที่คนพิมพ์ |
| **Creative Center → Keyword Insights** | ads.tiktok.com (desktop, ต้อง login) | คำ/phrase ที่โฆษณาที่ work ใช้ + search-ads keyword data |
| **Comment mining** | คอมเมนต์คู่แข่ง/ของตัวเอง | คำถามที่ยังไม่มีใครตอบ = วิดีโอที่ validated by demand |

### 4.4 สูตรวาง keyword ต่อ 1 คลิป
```
1 คลิป = 1 search phrase หลัก
   พูด phrase นั้นใน 3 วิแรก (เสียง)
   เขียน phrase นั้นบนจอ frame แรก
   ใส่ phrase นั้นใน caption (ตำแหน่งต้น)
   + 2-3 hashtag ที่ตรง (broad 1 + niche 1-2)
```

### 4.5 Search Ads setup
- แยก campaign จาก prospecting (เพื่ออ่านผลได้)
- ใช้ keyword matching: broad ก่อน แล้วค่อยเพิ่ม exact เมื่อมี data
- ระวัง: search volume ไทยต่ำกว่าอังกฤษมาก → อย่าแยก ad group ละ keyword มากเกินไป
- ใช้ negative keywords กับคำที่ไม่มี intent ซื้อ (เช่น "ฟรี", "วิธีทำเอง" ถ้าไม่ใช่เป้า)

---

## 5. Placement

| Placement | ใช้เมื่อ | หมายเหตุ |
|---|---|---|
| TikTok in-feed (FYP) | default | ที่หลักของทุก campaign |
| **Search results** | มีสินค้าที่คนค้นหา | intent สูง, ราคาดี |
| **Shop tab** | Shop seller | ต้องมี GMV Max/Shop campaign |
| **Pangle / Audience Network** | ต้องการ reach ราคาถูก | คุณภาพต่ำกว่า, CVR ต่ำ — วัดแยก |
| TopView / Top Feed | awareness mass | ต้องจองล่วงหน้า, ราคาสูง |

**หลัก:** ใน Smart+ ให้เริ่มด้วย placement อัตโนมัติ; แต่ถ้าเป็น regulated หรือต้องการ brand safety → **ปิด placement automation** และเลือกเอง

---

## 6. Retargeting funnel ที่ไม่ cannibalize

```
[Prospecting · broad]  งบ 70-80%
        ↓
[Engagement 75%+ VV / profile visit]  งบ 10%    → creative: social proof, FAQ
        ↓
[A TC / IC 7-14 วัน]  งบ 10-15%                → creative: urgency, review, bundle
        ↓
[Purchasers]  → EXCLUDE จาก prospecting          → ใช้ upsell/cross-sell แยก campaign
```

**กติกา:**
- retargeting ควรเป็น **<20–25%** ของงบทั้งหมด มิฉะนั้นคุณกำลังจ่ายให้คนที่จะซื้ออยู่แล้ว
- ใส่ **frequency cap** ที่ระดับ ad group ถ้าเป็น reach campaign
- retargeting audience ต้อง refresh (window เลื่อน) ไม่ใช่ static

---

## 7. Checklist targeting ก่อน launch

- [ ] broad ad group อย่างน้อย 1 ตัว (เพื่อเป็น benchmark)
- [ ] exclusion: purchasers ใน X วัน + พนักงาน
- [ ] ถ้าใช้ lookalike → ระบุ % และ source ที่สะอาด
- [ ] optimization event มี volume ≥20/สัปดาห์
- [ ] ถ้าใช้ VBO → ตรวจ `value` ส่งครบ
- [ ] search campaign แยกออกมา (ถ้ามี)
- [ ] ตรวจ audience overlap ระหว่าง ad group < 30%
- [ ] regulated → ปิดการเข้าถึงกลุ่มอายุที่ห้าม

---

## อ้างอิงบทนี้
กลุ่ม `targeting`, `search-seo`, `measurement` ใน [`SOURCES.md`](SOURCES.md)
