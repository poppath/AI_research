# 01 · แผนที่เครื่องมือ AI ของ Meta (สถานะ พ.ย. 2026)

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

เอกสารนี้ตอบคำถาม: **"Meta มีเครื่องมือ AI อะไรบ้าง และแต่ละตัวควรใช้ตอนไหน"**
เรียงจากชั้นล่าง (โครงสร้าง/จัดอันดับ) → ชั้นบน (หน้าจอที่คนใช้)

---

## 1. ชั้นโครงสร้าง (Infrastructure Layer)

### 1.1 Andromeda — ระบบ retrieval
- **คืออะไร**: ระบบดึง candidate ads ที่มีความเป็นไปได้สูงสุดต่อผู้ใช้แต่ละคน ก่อนเข้าสู่ชั้น auction
- **ผลต่อ advertiser**:
  - ความจุโมเดลเพิ่มขึ้นมาก (Meta อ้าง ~10,000×) → ระบบ "อ่าน" ครีเอทีฟได้ละเอียดขึ้น
  - การแข่งขันอยู่ที่ **relevance ของครีเอทีฟต่อคน** ไม่ใช่ขนาดของ audience ที่ตั้งไว้
  - ครีเอทีฟที่หยุดผู้ชมได้จริง (hook 3 วินาทีแรก) มีผลต่อ CPM มากกว่าการปรับ bid เล็กน้อย
- **ข้อควรระวัง**: ระบบยิ่งเก่ง → ครีเอทีฟที่คล้ายกันมากจะถูกมองเป็น "ชิ้นเดียว" (creative homogenization) ทำให้ไม่มีอะไรใหม่ให้ระบบเรียนรู้

### 1.2 GEM (Generative Ad Model)
- **คืออะไร**: โมเดล generative ที่ช่วยสร้าง/ประกอบชิ้นส่วนโฆษณา (ภาพ, ข้อความ, พื้นหลัง) และปรับ recommendation
- **ใช้เมื่อ**: ต้องการ variation ของ concept ที่ชนะแล้ว (ไม่ใช่หาคอนเซ็ปต์ใหม่)
- **ข้อจำกัด**: GEM ผลิต "variation" ได้ดี แต่ "คิดแง่มุมใหม่" ไม่ได้ → มนุษย์ต้องป้อน strategic angle

### 1.3 Lattice / โมเดลจัดอันดับรุ่นใหม่
- โครงสร้างโมเดลแบบ multi-stage (retrieval → ranking → auction) ที่ทำให้แอดที่ "ตรง" ถูกพบได้แม้ budget ต่ำ
- ผลเชิงกลยุทธ์: **แคมเปญเล็กก็แข่งขันได้** ถ้าครีเอทีฟคมและ signal สะอาด

### 1.4 Muse / Muse Image
- โมเดลภาพรุ่นใหม่ที่ขับเคลื่อน image generation ใน Advantage+ Creative
- ใช้กับ: background generation, product scene, image expansion
- ข้อควรระวัง: ภาพสินค้าที่มีเงื่อนไขแบรนด์เข้ม (สี, โลโก้, วัสดุ) ต้อง preview ทุกครั้ง

---

## 2. Advantage+ Suite — หัวใจของการทำงาน

### 2.1 ตารางสรุป

| เครื่องมือ | ทำอะไร | ควรเปิดเมื่อ | ควรระวัง |
|---|---|---|---|
| **Advantage+ Sales (ASC)** | รวมแคมเปญขายเป็น 1, จัดสรร budget/audience/placement อัตโนมัติ, สูงสุด ~150 creative combos | E-commerce ที่มี conversion ≥ 50/สัปดาห์ และมี catalog | ต้องตั้ง existing-customer cap (แนะนำ 25–30%) ไม่งั้นงบไหลไป retargeting |
| **Advantage+ Leads** | ใช้ AI หาคนที่มีโอกาสกรอกฟอร์ม/สมัคร | Lead gen ที่ปริมาณ lead เพียงพอ | คุณภาพ lead อาจต่ำลง → ต้องมี qualified-event ป้อนกลับ |
| **Advantage+ Audience** | ให้ AI ขยายจาก "คำใบ้" ของคุณ | เกือบทุกแคมเปญ ยกเว้นมีข้อจำกัดทางกฎหมาย/พื้นที่ | location/อายุขั้นต่ำ/ภาษา/exclusion = hard control; ที่เหลือเป็น suggestion |
| **Advantage+ Creative** | แต่ง/ต่อ/สร้าง variation ของ asset | ต้องการ scale ครีเอทีฟเร็ว | เปิดเฉพาะ enhancement ที่ปลอดภัย (ดู §4) |
| **Advantage+ Placements** | กระจาย placement อัตโนมัติ | ค่าเริ่มต้น | ต้องใช้ value rule คุม placement ที่ intent ต่ำ |
| **Advantage+ Catalog (ASC+)** | เลือกสินค้าที่จะโชว์ต่อคน + automation | ร้านที่มี feed สมบูรณ์ | feed quality = ผลลัพธ์; ปัญหา title/price ทำ ROI พังทั้งแคมเปญ |

### 2.2 หลักการตั้ง Advantage+
1. **1 objective = 1 แคมเปญหลัก** (อย่าแตกเป็น 5 แคมเปญตาม product line ตั้งแต่แรก)
2. **ให้ระบบมีอะไรให้เรียนรู้**: อย่างน้อย 10–15 creative, 3+ format, 2+ hook family
3. **ตั้งเพดานลูกค้าเดิม** (existing customer cap) และตรวจทุกเดือน
4. **อย่าแก้ ad set บ่อย** — ทุกครั้งที่แก้ significant edit ระบบอาจ reset learning
5. **ถ้า conversion < 50/สัปดาห์**: ลดจำนวน ad set, ใช้ optimization event ที่สูงขึ้นใน funnel (เช่น Lead แทน Purchase) หรือยอมรับว่า advantage+ จะเรียนรู้ช้า

---

## 3. Generative AI ใน Ads Manager (ชุดจาก Cannes Lions 2025)

| เครื่องมือ | ทำอะไร | สถานะ/หมายเหตุ |
|---|---|---|
| **Brand kit / brand consistency** | ดึงโลโก้ สี ฟอนต์จากเว็บ/ร้าน เพื่อคงอัตลักษณ์ในงาน AI | ควรตั้งก่อนเปิด creative automation |
| **Image-to-video / Video Generation 2.0** | ประกอบภาพสินค้า (สูงสุด ~20 ภาพ) เป็นคลิปหลายฉาก พร้อมข้อความ/เพลง | เหมาะทำ variant เร็ว; ตรวจคุณภาพทุกคลิป |
| **Video highlights** | ตัดช่วงสำคัญจากวิดีโอยาวเป็นคลิปสั้น | ใช้กับ content ที่มีอยู่แล้ว |
| **AI dubbing / voice / แปล** | พากย์และแปลหลายภาษา (รวมเสียง) | เหมาะกับตลาดหลายภาษาในไทย/อาเซียน |
| **Text generation / translations** | สร้าง headline, primary text, แปลข้อความบนภาพ | ปิดถ้ามีข้อความที่ต้องเป๊ะ (ราคา, เงื่อนไข, ข้อกฎหมาย) |
| **Creative Sticker CTA** | สติกเกอร์ CTA แบบกดได้ (FB ก่อน, IG ตาม) | ทดลองกับ Reels/Stories |
| **Virtual try-on** | ลองเสื้อผ้าบนนางแบบ virtual | Fashion/apparel เท่านั้น |
| **Business AI agents** | ตอบ FAQ, แนะนำสินค้าใน Messenger/WhatsApp/IG/FB | ต้องต่อ knowledge base ที่ถูกต้อง + มี fallback to human |
| **Muse for Small Business** | AI agent (approval-gated) เชื่อม ad account | ต้องอนุมัติสิทธิ์; เหมาะธุรกิจเล็กที่ไม่มีทีม |

**หลักปฏิบัติ**: ใช้ generative AI เพื่อ *เพิ่มจำนวน variant* และ *ลดต้นทุนการผลิต* — ไม่ใช่เพื่อ *คิดกลยุทธ์* เพราะ AI ไม่รู้ว่าลูกค้าซื้อเพราะอะไรจริง ๆ

---

## 4. Advantage+ Creative Enhancements — เปิด/ปิดอะไร

มี 17 enhancement ที่ Meta จัดว่าเป็น AI ตารางนี้คือค่าเริ่มต้นที่แนะนำ (ปรับได้ตามแบรนด์)

### 4.1 เปิดไว้ (ความเสี่ยงต่ำ)

| Enhancement | ทำอะไร | ทำไมเปิด |
|---|---|---|
| Visual touch-ups (image/video) | ปรับความสว่าง คอนทราสต์ คมชัด | แทบไม่เปลี่ยนความหมาย |
| Image expansion | ขยายขอบภาพให้เต็ม 9:16/4:5 | ได้ inventory เพิ่มโดยไม่ต้องผลิตใหม่ |
| Adjust brightness/contrast | มาตรฐาน | ปลอดภัย |
| Dynamic description (carousel/catalog) | เลือกคำอธิบายที่ตรงกับคนดู | เพิ่ม relevancy |
| Dynamic media (catalog) | เลือกสื่อจาก feed ตามคน | ใช้ได้ถ้า feed ดี |
| Video subtitles | คำบรรยาย | คนดูแบบปิดเสียงจำนวนมาก |
| Relevant comments | โชว์คอมเมนต์เชิงบวก | social proof — แต่ต้องมีคอมเมนต์ดีจริง |
| Catalog overlays (ราคา/โปร) | ป้ายราคาจาก feed | ข้อเท็จจริงจาก feed |

### 4.2 เปิดแบบทดสอบ (ความเสี่ยงกลาง)

| Enhancement | เงื่อนไขก่อนเปิด |
|---|---|
| Enhance CTA | ตรวจว่าข้อความ CTA ยังตรง offer |
| Add overlays | ตรวจว่าข้อความไม่ทับ safe zone |
| Flex media | ใช้เมื่อมีทั้งภาพและวิดีโอคุณภาพเท่ากัน |
| 3D / image animation | ใช้กับภาพ lifestyle; ห้ามกับภาพสินค้าที่ต้องเห็นรายละเอียด |
| Background generation | preview ทุกภาพ; ห้ามกับสินค้าที่สี/วัสดุเป็น selling point |
| Text generation | ใช้กับ copy ที่ไม่มีความเสี่ยงด้านราคา/กฎหมาย |
| Translations | ตรวจคำศัพท์เฉพาะอุตสาหกรรม |
| Music | เลือกเองเมื่อแบรนด์มี tone ชัด |

### 4.3 ปิด (ความเสี่ยงสูง)

| Enhancement | เหตุผล |
|---|---|
| Text improvements (เขียนทับ copy เดิม) | อาจเปลี่ยนราคา/เงื่อนไข/คำรับรอง |
| Enhance media text (แก้ข้อความบนภาพ) | เสี่ยงผิดเพี้ยน แบรนด์ |
| Show summaries | อาจตัดข้อมูลจำเป็นออก |
| Site links (ถ้าไม่ตรง) | ทำให้คนไปผิดหน้า |
| Auto music ในแบรนด์พรีเมียม | tone clash |

> **กฎ**: ทุกครั้งที่เปิด enhancement ใหม่ ให้รันเป็น "การทดลอง" ใน `templates/experiment-log.csv` และเปรียบเทียบกับกลุ่มควบคุม (ปิด enhancement) อย่างน้อย 7 วัน

---

## 5. การวัดและ signal tools

| เครื่องมือ | ใช้ทำอะไร | หมายเหตุ |
|---|---|---|
| **Pixel** | เก็บ event ฝั่ง browser | อย่างเดียวไม่พอ (สูญเสีย signal 20–40%) |
| **Conversions API (CAPI)** | ส่ง event จาก server | ต้อง dedup ด้วย `event_id` ร่วมกับ Pixel |
| **Event Match Quality (EMQ)** | คะแนน 0–10 คุณภาพ identifier | ≥ 6.0 คือขั้นต่ำ, เป้า 7.5–9.0 |
| **Aggregated Event Measurement (AEM)** | จัดลำดับ 8 event ต่อโดเมน | ต้องตั้ง Purchase/Lead เป็นอันดับแรก |
| **Conversion Lift / A/B test** | วัด causation | ต้องมี volume พอ (มัก ≥ 100–500 conversions) |
| **Incremental attribution** | คอลัมน์เทียบ relative incrementality | ใช้จัดอันดับแคมเปญภายใน Meta เท่านั้น |
| **Experiments (A/B)** | แยกทดสอบโครงสร้าง | 1 ตัวแปร/ครั้ง |

---

## 6. Decision Tree: ควรใช้เครื่องมือไหนเมื่อไหร่

```
มี conversion ≥ 50/สัปดาห์ หรือไม่?
├── ใช่ → ใช้ Advantage+ Sales/Leads เป็นแกน
│         + Advantage+ Audience (broad + suggestion)
│         + ครีเอทีฟ 10–15 ชิ้น
│         + placement value rule สำหรับ Threads/AN
│
└── ไม่ → ใช้แคมเปญ manual/Consideration
          + optimization event ที่สูงขึ้น (Lead, ATC, Landing Page View)
          + audience แคบลงเล็กน้อย (3–5 interest หรือ LAL 1–3%)
          + creative น้อยแต่คม (5–8 ชิ้น) แล้วค่อยขยับ

มี CAPI + EMQ ≥ 6 หรือไม่?
├── ไม่ → หยุดสเกล; แก้ signal ก่อน (งานด่วนอันดับ 1)
└── ใช่ → ตรวจ lift/geo test อย่างน้อยไตรมาสละครั้ง

มีทีมผลิตครีเอทีฟจำกัดหรือไม่?
├── ใช่ → ใช้ image-to-video + brand kit + AI avatar/UGC (มี disclosure)
└── ไม่ → ใช้ AI เป็นตัวเร่ง variant ไม่ใช่ตัวตั้งต้น concept
```

---

## 7. ข้อจำกัดที่ต้องรู้ (และบอกลูกค้า)

1. **Meta ไม่โปร่งใสเรื่อง attribution ภายใน** — รู้ว่าใครเห็นอะไรบ้างในระดับ aggregate เท่านั้น
2. **AI optimization ทำงานได้ดีกับสิ่งที่เคยเห็น** — สินค้าใหม่/หมวดใหม่ต้องมี "ไกด์" (interest/audience) มากขึ้น
3. **Creative homogenization** — ถ้าทุกคนใช้ AI เดียวกัน แอดจะคล้ายกัน; ความได้เปรียบอยู่ที่ insight ไม่ใช่เครื่องมือ
4. **ค่า CPM มีแนวโน้มสูงขึ้น** — ต้องชดเชยด้วย conversion rate และ creative quality ไม่ใช่ลด bid
5. **ข้อกำหนดการเปิดเผยเนื้อหา AI** — Meta ติด label เนื้อหาที่สร้างด้วย AI; แบรนด์ควรมีนโยบายภายในเรื่อง disclosure กับผู้บริโภค
