# 11 · AI Stack & Automation Workflows

> **TL;DR** — AI ไม่ได้แทน strategist; มันแทน **งานที่ทำซ้ำ** (variation, research, reporting, tagging). ผลลัพธ์ที่ดีที่สุดเกิดเมื่อ: AI ผลิต 20 ตัวเลือก → มนุษย์เลือก 3 → AI ทำ variation ของ 3 → ระบบทดสอบ. จุดที่ AI ยังแพ้มนุษย์ชัด ๆ คือ **creative direction** และ **judgment เรื่อง claim/ความเสี่ยง**

---

## 1. แผนที่ว่า AI ใช้ตรงไหนของงาน

| งาน | AI ทำได้ดี | AI ทำได้แต่ต้อง review | AI ยังไม่ควรทำ |
|---|---|---|---|
| Research hook/trend | ✅ Creative Center + Keyword Insights + Symphony Assistant | | |
| Ideation hook | ✅ 20 hook จาก 5 angle | | |
| Script | ✅ draft | ✅ ต้องเกลาสำนวนให้เป็นภาษาคน | |
| Production | ✅ variation, resize, dubbing, avatar | ✅ hero content ควรถ่ายจริง | |
| Media buying | ✅ Smart+/GMV Max | | ✅ ตัดสินใจหยุด/สเกลเอง |
| Reporting | ✅ อ่านตาราง, สรุป, หา anomaly | ✅ ต้องตรวจตัวเลข | |
| Compliance check | ✅ ตรวจ claim เบื้องต้น | ✅ ต้องมีคนเซ็น | |
| Strategy / positioning | | ✅ AI ช่วยโครง | ✅ เลือก positioning แทน |

---

## 2. เครื่องมือ TikTok-native (ฟรี) — ใช้ก่อนซื้ออะไร

| เครื่องมือ | ทำอะไร | ราคา |
|---|---|---|
| **TikTok Creative Center** | Top Ads, Keyword Insights, Trends, Commercial Music Library | ฟรี |
| **Symphony Creative Studio** | สร้างวิดีโอจาก prompt/URL, avatar, dubbing | ฟรี (avatar มีค่าใช้จ่ายตามใช้) |
| **Symphony Assistant** | research assistant ที่ตอบจากข้อมูล Creative Center สด | ฟรี |
| **Symphony Automation** | refresh/resize creative อัตโนมัติ | ฟรี |
| **Symphony Agent** (Q3 2026) | สร้างวิดีโอ 12 วิ ใน ~3 นาที | ฟรี/ตาม package |
| **AI Dubbing** | พากย์หลายภาษา | ฟรี |
| **AI Symphony (Ads Manager)** | ปรับ creative ภายใน Ads Manager | ฟรี |
| **Creator Search Insights** (ในแอป) | keyword + content gap | ฟรี |

> **สำหรับงบ < $10k/เดือน: ใช้แค่ Symphony + Creative Center พอ** เครื่องมือเสียเงินยังไม่คุ้ม

---

## 3. เครื่องมือเสริม (เลือกตามคอขวด)

| คอขวด | เครื่องมือ | ราคาเริ่ม |
|---|---|---|
| ผลิตคลิปไม่ทัน | Creatify / Pippit / CapCut for Business | $24–99/เดือน |
| อยากได้ AI actor | Arcads / HeyGen | $29+/เดือน |
| อยากรู้ว่าองค์ประกอบไหนขับ ROAS | Segwise / Superads / VidMob | $125–499+/เดือน |
| ต้องส่งรายงานให้ลูกค้า | Motion | ~$750/เดือน |
| static/carousel | AdCreative.ai / Predis.ai | $19–39/เดือน |
| attribution | Triple Whale / Northbeam / Cometly / Elevar | varies |

**กฎการเลือก:** ซื้อ tool เมื่อ **คอขวดชัดเจน** ไม่ใช่เมื่อ tool ดูดี
- ถ้าผลิต <3 concept/สัปดาห์ → ซื้อ production tool
- ถ้าผลิต 3–10/สัปดาห์ → เพิ่ม fatigue tracking
- ถ้า >10/สัปดาห์ หรือมี >50 live creative → **ต้องมี element-level tagging**

---

## 4. Workflow: 1 สัปดาห์ creative sprint (ใช้ AI ทั้งหมด)

```
วันจันทร์ (60 นาที) — RESEARCH
  Creative Center → Top Ads (industry=ของฉัน, region=TH, objective=Sales)
  → บันทึก 10 hook ที่ work + 5 format
  → Keyword Insights: ดึง 15 คำที่แอดที่ work ใช้
  → Creator Search Insights: หา content gap 3 เรื่อง
  OUTPUT: research sheet (Hook bank, Format bank, Keyword bank)

วันอังคาร (90 นาที) — IDEATE
  LLM prompt: "จาก hook bank นี้ + สินค้า [X] + กลุ่ม [Y]
               ขอ 20 hook ใหม่ แบ่งเป็น 5 angle × 4 hook
               ภาษาพูดเหมือนคนจริง ไม่ใช่โฆษณา
               ห้ามใช้คำ: ดีที่สุด, การันตี, รักษา"
  → มนุษย์คัดเหลือ 6 hook (เลือกที่ 'พูดได้จริง' และไม่เสี่ยง claim)
  OUTPUT: 6 hook × 3 concept = 18 สคริปต์สั้น

วันพุธ (120 นาที) — PRODUCE
  ถ่ายจริง: 3 concept × 2 hook (hero) — มือถือ, 9:16
  Symphony/Pippit: variation ของ hook ที่เหลือ
  OUTPUT: 12-15 ไฟล์ raw

วันพฤหัส (60 นาที) — REVIEW
  ตรวจ checklist บท 03 §10 + compliance บท 10 §7
  ตั้งชื่อตาม convention (C07_H02_UGC_15s_v3)
  OUTPUT: 8-12 ไฟล์พร้อม launch

วันศุกร์ — LAUNCH & TRACK
  อัปเดต creative test ad group, ตั้ง kill criteria
  อัปเดต creative tracker sheet

สัปดาห์ถัดไป — LEARN
  อ่าน hook rate, completion, CPA ต่อ creative
  → ป้อนกลับเข้า Hook bank (ทั้งตัวที่ชนะและแพ้)
```

---

## 5. Prompt templates ที่ใช้ได้ผล

### 5.1 Hook ideation
```
สินค้า: [ชื่อ + 1 บรรทัดว่าคืออะไร + ราคา]
กลุ่มเป้าหมาย: [อายุ, ปัญหา, คำที่เขาใช้พูดถึงปัญหา]
แพลตฟอร์ม: TikTok (hook ต้องจบใน 1-3 วินาที)

ขอ hook 20 อัน แบ่งเป็น:
- 4 แบบ bold claim
- 4 แบบ direct call-out
- 4 แบบ problem-first
- 4 แบบ curiosity gap
- 4 แบบ social proof

ข้อกำหนด:
- แต่ละ hook ≤ 10 คำ (ภาษาไทย)
- ภาษาพูด ไม่ใช่ภาษาโฆษณา
- ห้ามใช้: ดีที่สุด, การันตี, รักษา, หายขาด, 100%
- ระบุว่าแต่ละ hook เหมาะกับใคร (1 บรรทัด)
```

### 5.2 Creative diagnosis
```
นี่คือข้อมูล creative 12 ตัวในแคมเปญ:
[ตาราง: ID, hook type, spend, impressions, 3s view rate, completion, CTR, CPA, ROAS]

วิเคราะห์:
1. hook type ไหนให้ 3s view rate ดีสุด — และดีกว่าเฉลี่ยกี่ %
2. ตัวไหนควร kill ทันที (ระบุเกณฑ์ที่ใช้)
3. ตัวไหนควรได้งบเพิ่ม (ระบุเกณฑ์)
4. pattern ที่ควรผลิตซ้ำ (ระบุให้ชัดว่า pattern อะไร)
5. สมมติฐาน 3 ข้อที่ยังต้องทดสอบสัปดาห์หน้า

ข้อกำหนด: อย่าสรุปเกินข้อมูล — ถ้าตัวอย่างน้อยกว่า 1,000 impressions ให้บอกว่าไม่พอ
```

### 5.3 Compliance pre-check
```
ตรวจ creative นี้กับกฎ TikTok Ads Policy + กฎหมายไทย:
[สคริปต์/แคปชัน]

ระบุ:
1. คำ/ประโยคที่เสี่ยง (ยกมาทั้งประโยค)
2. ความเสี่ยงระดับ: สูง / กลาง / ต่ำ และอ้างอิงกฎอะไร
3. ข้อความทดแทนที่ปลอดภัยกว่า (ยังคงสาระการขาย)
4. เอกสารที่ต้องเตรียมถ้าจะใช้ claim นี้

ข้อกำหนด: ถ้าไม่แน่ใจ ให้บอกว่าไม่แน่ใจ ห้ามเดาว่าผ่าน
```

### 5.4 Weekly report
```
นี่คือข้อมูลสัปดาห์นี้ vs สัปดาห์ก่อน:
[ตาราง]

สรุปเป็น 3 ส่วน:
1. สิ่งที่เกิดขึ้น (ข้อเท็จจริงจากตัวเลขเท่านั้น)
2. ทำไมน่าจะเกิด (สมมติฐาน + ระดับความมั่นใจ)
3. สิ่งที่ต้องทำสัปดาห์หน้า (ไม่เกิน 3 ข้อ เรียงตามผลกระทบ)

ข้อกำหนด: ห้ามสรุปจากตัวเลขที่ sample เล็ก; ระบุถ้าตัวเลขยังไม่ significant
```

---

## 6. Automation ที่ควรทำอัตโนมัติ vs ไม่ควร

| ✅ ควรอัตโนมัติ | ❌ ไม่ควร |
|---|---|
| ดึงข้อมูลรายวันเข้า sheet | เปลี่ยน bid อัตโนมัติ |
| แจ้งเตือนเมื่อ CPA เกินเกณฑ์ | ปิด campaign อัตโนมัติ |
| tag creative ตาม hook/format | เปลี่ยน target ROAS อัตโนมัติ |
| resize/caption อัตโนมัติ | อนุมัติ creative ขึ้นแพลตฟอร์ม |
| รายงานสรุปรายสัปดาห์ | ตัดสินใจ compliance |
| A/B assign creative ใน test | ย้ายงบข้ามแพลตฟอร์ม |

**หลัก:** automate **การรับรู้** (sensing), manual **การตัดสินใจ** (judgment) — จนกว่าคุณจะมีข้อมูลมากพอจะพิสูจน์ว่า guardrail ปลอดภัยจริง

---

## 7. AI content: กติกาที่ต้องยึด

1. **Disclose AI content** ตามที่ TikTok กำหนด
2. **ห้ามใช้ likeness/เสียงของคนจริง** โดยไม่มี consent
3. **ห้ามใช้ AI สร้างรีวิว/endorsement ปลอม** (ผิดทั้ง policy และกฎหมายคุ้มครองผู้บริโภค)
4. **AI avatar เหมาะกับ volume ไม่เหมาะกับ trust-sensitive** (health, finance)
5. **AI-generated hero creative ยังแพ้ของจริง** ในหมวดที่ต้องการความน่าเชื่อถือ
6. เก็บ **prompt/source log** ไว้ เพื่อ audit ได้

---

## 8. ROI ของ AI stack — คิดแบบนี้

```
เวลาที่ประหยัด/สัปดาห์ (ชม.) × ต้นทุนเวลาต่อชม.  >  ค่าเครื่องมือ/เดือน ÷ 4.3
```
ตัวอย่าง: ทีม 1 คน ฿40,000/เดือน (~฿230/ชม.), ประหยัด 6 ชม./สัปดาห์ = ฿5,520/เดือน → คุ้มถ้า tool < ฿5,500/เดือน

**แต่ตัวคูณจริงไม่ใชเวลา — คือจำนวน creative ที่ทดสอบได้ต่อเดือน** เพราะนั่นคือสิ่งที่ขับ CPA ลง

---

## อ้างอิงบทนี้
กลุ่ม `ai-tools` ใน [`SOURCES.md`](SOURCES.md)
