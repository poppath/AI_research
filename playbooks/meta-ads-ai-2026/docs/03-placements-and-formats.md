# 03 · Placements & Formats — ทุกช่องทางของ Meta และวิธีใช้ให้ต่างกัน

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> หลักเดียวของบทนี้: **audience แชร์กันข้าม placement แต่ "บริบท" ไม่เหมือนกัน** — ดังนั้นสิ่งที่ต้องปรับคือ *ครีเอทีฟ*, *ความยาว*, *ข้อความ*, และ *bid value* ไม่ใช่การสร้าง audience แยกทุก placement

---

## 1. แผนที่ Placement ทั้งหมด (พ.ย. 2026)

| Placement | ที่อยู่ | รูปแบบที่รองรับ | อัตราส่วนหลัก | บทบาทใน funnel |
|---|---|---|---|---|
| **Facebook Feed** | ฟีด FB | image, video, carousel, collection | 4:5 / 1:1 | Mid–low funnel, intent ปานกลาง |
| **Facebook Reels** | full-screen Reels | video (9:16) | 9:16 | Top funnel, discovery |
| **Facebook Stories** | สตอรี่ | image, video | 9:16 | Top–mid, offer |
| **Facebook In-stream** | ก่อน/กลางวิดีโอ | video | 16:9 / 1:1 | Awareness |
| **Facebook Profile/Feed video** | วิดีโอในฟีด | video | 4:5 / 1:1 | Engagement |
| **Instagram Feed** | ฟีด IG | image, video, carousel | 4:5 / 1:1 | Mid funnel, aesthetic |
| **Instagram Reels** | full-screen | video (9:16) | 9:16 | Top funnel, discovery |
| **Instagram Stories** | สตอรี่ | image, video | 9:16 | Top–mid, CTA sticker |
| **Instagram Explore** | หน้า explore | image, video | 1:1 / 4:5 | *(ถูกถอดจาก API ต.ค. 2026 — ตรวจใน Ads Manager)* |
| **Threads** | ฟีด Threads | image, video, carousel (4:5) | 4:5 | Top–mid, text-first |
| **Messenger** | กล่องข้อความ/ฟีด | image, video, carousel | 1:1 | Conversational |
| **WhatsApp** | แท็บ Updates (Status/Channels) | image, video แนวตั้ง | 9:16 | Conversational, reach |
| **Audience Network** | แอป/เว็บพาร์ตเนอร์ | image, video, native, rewarded | 1:1 / 9:16 | Reach ราคาถูก, คุณภาพต่ำ |

> **สิ่งที่ถูกถอด/เปลี่ยน**: Messenger Stories และ IG Explore ถูกถอดจาก Marketing API (ต.ค. 2026) · placement exclusions ถูกแทนด้วย value rules (ส.ค. 2026) · Threads เป็น default placement (26 ต.ค. 2026)

---

## 2. สเปกครีเอทีฟ (ตัวเลขที่ใช้จริง)

### 2.1 วิดีโอ / Reels / Stories

| รายการ | ค่า |
|---|---|
| อัตราส่วน | **9:16** (แนวตั้งเท่านั้น) |
| ความละเอียดแนะนำ | 1080 × 1920 px |
| ความละเอียดคุณภาพสูง | 1440 × 2560 px |
| ขั้นต่ำ | 500 × 889 px |
| ไฟล์ | MP4 (แนะนำ), MOV, GIF |
| Codec | H.264, progressive, fixed frame rate |
| Frame rate | ≤ 30 fps |
| เสียง | AAC stereo ≥ 128 kbps |
| ขนาดไฟล์สูงสุด | 4 GB |
| ความยาว | 1 วิ – 90 วิ (Reels), แนะนำ **5–15 วิ** |
| Safe zone | บน 14% (≈269 px) · ล่าง 35% (≈672 px) · ข้าง 6% (≈65 px) |
| Bottom-right corner | เว้น 40% (ไอคอน like/comment/share) |
| Primary text ที่แสดง | ~40 ตัวอักษร (FB Reels), ~44 (IG Reels) |
| Headline | ~55 ตัวอักษร |

### 2.2 ภาพ / Feed

| Placement | อัตราส่วน | ขนาด | หมายเหตุ |
|---|---|---|---|
| Feed (แนะนำ) | 4:5 | 1080 × 1350 | กินพื้นที่แนวตั้งมากกว่า 1:1 |
| Feed (ทางเลือก) | 1:1 | 1080 × 1080 | ปลอดภัยทุก placement |
| Stories/Reels (ภาพ) | 9:16 | 1080 × 1920 | ภาพนิ่งแสดง 5 วิ |
| Carousel | 1:1 | 1080 × 1080 (การ์ดละ) | 2–10 การ์ด |
| ไฟล์ภาพ | JPG/PNG | ≤ 30 MB | หลีกเลี่ยงข้อความเกิน 20% ของภาพ |

### 2.3 Safe zone — กติกาเดียวที่ต้องจำ

```
┌─────────────────────────┐  ← 0%
│   เว้นบน 14%            │
├─────────────────────────┤  ← 14%  (≈269 px)
│                         │
│   พื้นที่ปลอดภัย        │
│   ≈ 950 × 979 px        │
│   (ใส่ hook/สินค้า/โลโก้)│
│                         │
├─────────────────────────┤  ← 65%  (≈1248 px)
│   เว้นล่าง 35%          │  ← CTA, caption, ปุ่ม
│   (เว้นขวาล่าง 40%)     │
└─────────────────────────┘  ← 100%
      ↑ เว้นข้าง 6% ทั้งสองด้าน ↑
```

**ใช้ได้กับ**: FB Reels, IG Reels, FB Stories, IG Stories, IG Feed (วิดีโอ 9:16)
**ถ้ามี disclaimer**: เว้นล่างเพิ่มเป็น **40%**

---

## 3. แต่ละ Placement ต้องใช้ครีเอทีฟต่างกันอย่างไร

### 3.1 Reels (FB + IG) — เครื่องยนต์ Reach หลัก

**ทำไมสำคัญ**: short-form video กินสัดส่วน impression มากกว่าครึ่งในหลายบัญชี และเป็นที่ที่ Andromeda ทำงานหนักที่สุด

**สูตร 15 วินาที**:

| วินาที | องค์ประกอบ | ตัวอย่าง |
|---|---|---|
| 0–2 | Hook (ภาพ + ข้อความ + เสียง) | "อย่าซื้อ___ก่อนดูคลิปนี้" / ภาพก่อน-หลัง |
| 2–5 | ปัญหา / ความเชื่อเดิม | "ส่วนใหญ่คิดว่า___ แต่จริง ๆ ___" |
| 5–10 | หลักฐาน / สาธิต | demo, รีวิว, ตัวเลข, before/after |
| 10–13 | ข้อเสนอ | ราคา, โปร, การรับประกัน |
| 13–15 | CTA | "กดดูรายละเอียด" + โลโก้ |

**กติกา Reels**:
- ออกแบบ **sound-off ได้ความหมาย** (ใส่ caption ทุกคลิป) แต่ก็ต้อง **sound-on ได้อารมณ์**
- ห้ามใส่ข้อความสำคัญในโซนล่าง 35%
- อย่าใช้ภาพนิ่งเดียว 15 วิ — ใช้ 3–5 ฉากสั้น
- หลีกเลี่ยง intro แบบโลโก้ 3 วิ (คนเลื่อนหนี)
- ใช้ native look (มือถือถือกล้อง) ดีกว่าผลิตโฆษณาเป๊ะ ๆ ในหลายตลาด

### 3.2 Stories

- 9:16 + **Sticker CTA** (ทดลอง)
- 1 ข้อความ/1 ไอเดีย ต่อเฟรม
- ใช้ "swipe up"/"กดลิงก์" ให้ชัดใน 3 วิแรก
- ภาพนิ่ง 5 วิ auto-advance → ต้องอ่านรู้เรื่องใน 2 วิ

### 3.3 Feed (FB + IG)

- **4:5** ชนะ 1:1 ในแง่พื้นที่ แต่ 1:1 ปลอดภัยกว่าในการใช้ asset เดียว
- Primary text แสดง ~125 ตัวอักษร → **ประโยคแรกต้องมี offer/hook**
- Carousel เหมาะกับ: หลาย SKU, ขั้นตอน, before/after, testimonial
- ใช้ Dynamic Creative (DCO) เมื่อมี asset หลายชิ้น (≤10 ภาพ/วิดีโอ, ≤5 headline, ≤5 copy)

### 3.4 Threads

- **Text-first**: คนอ่านข้อความมากกว่าดูภาพ → เขียน copy เหมือนโพสต์จริง ไม่ใช่โฆษณา
- 4:5 image/video, carousel ได้
- CPM ต่ำกว่า IG feed 20–40% (ตามรายงานอุตสาหกรรม) แต่ **intent ต่ำ**
- เหมาะ: awareness, content distribution, แบรนด์ที่อยากดู "มนุษย์"
- ไม่เหมาะ: hard-sell / discount ที่ต้องการ conversion ทันที (แต่ทดสอบได้)
- ใช้ placement value rule ลด bid ถ้า CPA แย่

### 3.5 Messenger / WhatsApp (Conversational)

- **Click-to-Message** = ทางลัดสำหรับธุรกิจไทย (ปิดการขายในแชท, ส่งสลิป, นัดหมาย)
- ใช้ **Business AI agent** ตอบ FAQ/คัดกรองเบื้องต้น → ส่งต่อคน
- WhatsApp ads อยู่เฉพาะแท็บ Updates (Status/Channels) — **ไม่แตะแชทส่วนตัว**
- ต้องมี SLA ตอบกลับ (< 15 นาทีในเวลาทำการ) ไม่งั้น CPA จะดูดีแต่ยอดจริงแย่
- วัดผลด้วย "conversation started" + "qualified conversation" (CAPI) ไม่ใช่แค่ click

### 3.6 Audience Network

- ราคาถูก แต่คุณภาพต่ำและ fraud เสี่ยง
- ใช้เฉพาะ awareness/reach หรือ remarketing ที่มีข้อเสนอชัด
- ตรวจ placement report รายสัปดาห์; ถ้า spend > 10% และ CPA แย่ → ลด bid ด้วย value rule

---

## 4. Placement Value Rule (ทดแทนการปิด placement)

ตั้งแต่ ส.ค. 2026 การปิด placement บาง objective ทำไม่ได้เต็มรูปแบบแล้ว ให้ใช้ **value rule** ที่ระดับ ad set:

```
Ad set → Placements → Advantage+ Placements → Placement value
  Threads:            0.3×  (bid ต่ำลง 70%)
  Audience Network:   0.2×
  Facebook In-stream: 0.5×
  IG Reels:           1.2×
  FB Feed:            1.0×
```

**วิธีคิด multiplier**:
1. ดึง report 30 วัน แยก placement: spend, CVR, CPA
2. คำนวณ `CPA_placement / CPA_เฉลี่ย` → ถ้า > 1.5 = ลด (0.3–0.5×), ถ้า < 0.8 = เพิ่ม (1.2–1.5×)
3. ตั้งแล้วรอ 7 วันก่อนปรับใหม่ (อย่าแก้วันละครั้ง)
4. บันทึกผลใน experiment log

> **ข้อจำกัด**: value rule ไม่ใช่การปิด; ยังมี delivery บ้าง แต่จำกัดลงมาก (ลดได้ถึง 90%)

---

## 5. Ad Format Matrix — เลือกฟอร์แมตตามเป้าหมาย

| เป้าหมาย | ฟอร์แมตที่ควรมี | ฟอร์แมตที่ควรทดลอง |
|---|---|---|
| Reach / Awareness | video 9:16 (6–15 วิ), image 4:5 | creator-style Reels |
| Consideration | carousel, video สาธิต, collection | Instant Experience |
| Lead | Instant Form + video testimonial | Click-to-WhatsApp + AI agent |
| Conversion | image 4:5 + video 9:16 + carousel | catalog overlay ใน Reels |
| Retention | video 9:16 (offer เฉพาะกลุ่ม) | Click-to-message |
| App | video 9:16 + playable | — |

---

## 6. การอ่าน Placement Report

**ทำทุกสัปดาห์** (15 นาที):

| คอลัมน์ | ดูอะไร | เกณฑ์ |
|---|---|---|
| Spend % | placement ไหนกินงบ | ถ้า > 15% และ CPA > 1.3× เฉลี่ย → ต้องแก้ |
| CPM | ราคาต่อการเห็น | ใช้เทียบ arbitrage (Threads/AN ถูกกว่า) |
| CTR (link) | คุณภาพ hook | ต่ำกว่า 0.8% ใน Reels = hook อ่อน |
| CVR | คุณภาพปลายทาง | ต่ำกว่า feed 30% = ไม่เหมาะ conversion |
| Frequency | ความถี่ | > 3 ใน 7 วัน = ครีเอทีฟเริ่ม Fatigue |
| ROAS/CPA | ผลลัพธ์ | เทียบกับเป้า |

**ข้อควรระวัง**: ตัวเลขใน Ads Manager เป็น *modeled* ไม่ใช่ *observed* ทั้งหมด — อย่าตัดสิน placement จากตัวเลขวันเดียว

---

## 7. Checklist ก่อน Launch (placement & format)

- [ ] มี asset 9:16 อย่างน้อย 1 ชุด (วิดีโอ) + 4:5 (ภาพ)
- [ ] ข้อความสำคัญอยู่ใน safe zone (ตรวจด้วย overlay guide)
- [ ] caption/subtitle ฝังในวิดีโอ (ไม่พึ่ง auto-caption อย่างเดียว)
- [ ] ตั้ง placement value rule ตาม §4
- [ ] ตรวจว่า Threads เปิดอยู่ และมี creative ที่ "text-first" อย่างน้อย 1 ชิ้น
- [ ] ถ้าใช้ click-to-message: ทดสอบลิงก์ + ตรวจว่า AI agent ตอบได้
- [ ] ตรวจ preview ทั้ง 6 placement หลัก (FB Feed, FB Reels, IG Feed, IG Reels, IG Stories, Threads)
- [ ] ตรวจว่า primary text ประโยคแรกมี hook (≤ 125 ตัวอักษร)
