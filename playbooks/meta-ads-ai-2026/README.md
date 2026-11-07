# Meta Ads × AI Playbook 2026

> งานวิจัย + เพลย์บุ๊กปฏิบัติการ สำหรับทำโฆษณา Facebook/Meta ให้มีประสิทธิภาพด้วย AI
> ครอบคลุม: การเข้าถึง (Reach) · Target Audience · ทุก placement (Facebook, Instagram, Reels, Stories, Threads, Messenger, WhatsApp) · เครื่องมือ AI ของ Meta · ระบบสร้างครีเอทีฟด้วย AI · การวัดผลแบบเพิ่มส่วน (incrementality)
> อัปเดตล่าสุด: 2026-11-06 · ตลาดอ้างอิงหลัก: ประเทศไทย

---

## ทำไมต้องอ่านชุดนี้

ตั้งแต่ปลายปี 2024 Meta เปลี่ยนแกนของระบบโฆษณาจาก "คนเลือกกลุ่มเป้าหมาย" เป็น "อัลกอริทึมหาคนให้จากครีเอทีฟ" (retrieval engine **Andromeda** + โมเดล generative อย่าง **GEM/Muse**) ผลคือ

1. **ครีเอทีฟกลายเป็นตัวกำหนด targeting** — อัลกอริทึ่อ่านภาพ/เสียง/ข้อความในแอด แล้วจับคู่กับคนที่ relevancy สูงสุด
2. **การตั้งค่าแบบ manual ถูกยุบ** — detailed targeting exclusions ถูกถอด, placement exclusions ถูกแทนด้วย placement value rule, Threads กลายเป็น default placement
3. **ช่องว่างใหม่คือ "ระบบ" ไม่ใช่ "ปุ่ม"** — คนที่ชนะคือคนที่ป้อน *signal ที่สะอาด* + *ครีเอทีฟที่หลากหลายเชิงกลยุทธ์* + *การอ่านผลที่แยก causation ได้*
4. **AI ทำงาน 4 ชั้น** — วิจัย → ผลิตครีเอทีฟ → ยิงแอด/จัดสรรงบ → เรียนรู้และปรับ (นี่คือโครงของ playbook ทั้งเล่ม)

ดังนั้นเอกสารชุดนี้ไม่ได้บอกว่า "เปิด Advantage+ แล้วจบ" แต่บอกว่า **อะไรควรปล่อยให้ AI, อะไรต้องคุมด้วยมือ, และวัดอย่างไรไม่ให้หลอกตัวเอง**

---

## TL;DR — 10 หลักการที่ใช้ได้ทันที

| # | หลักการ | ความหมายปฏิบัติ |
|---|---|---|
| 1 | **Creative is targeting** | ผลิตครีเอทีฟให้ต่างกันเชิง *persona × awareness × angle* อย่างน้อย 10–15 ชิ้นต่อ ad set แล้วให้ AI จับคู่คน |
| 2 | **คุมแค่ "ขอบ" ปล่อย "กลาง" ให้ AI** | Hard control = ประเทศ/พื้นที่, อายุขั้นต่ำ, ภาษา, exclusion ของ custom audience |
| 3 | **ยิงกว้างก่อน แล้วอ่านสัญญาณ** | อย่าซอย interest 4–5 ชั้น; ใช้ 3–5 interest กว้างเป็น "suggestion" หรือไม่ใส่เลย |
| 4 | **Signal ก่อน Scale** | Pixel + Conversions API (dedup ด้วย `event_id`) และ EMQ ≥ 6.0 (เป้า 7.5–9.0) ก่อนเพิ่มงบ |
| 5 | **50 conversions/สัปดาห์/ad set** | ต่ำกว่านี้ = รวม ad set/แคมเปญให้ใหญ่ขึ้น หรือเปลี่ยน optimization event ให้สูงขึ้นใน funnel |
| 6 | **9:16 คือภาษากลาง** | 1080×1920 (หรือ 1440×2560) + safe zone บน 14% / ล่าง 35% / ข้าง 6% ใช้ได้ทั้ง Reels, Stories, Feed แนวตั้ง |
| 7 | **Threads/WhatsApp = ช่องว่างราคา** | CPM ต่ำกว่า feed 20–40% แต่ conversion intent ต่ำ → ใช้ creative ที่ "อ่านแล้วหยุด" ไม่ใช่ creative ขายตรง |
| 8 | **ทดลองทีละตัวแปร** | โครงสร้าง = A/B test tool; ครีเอทีฟ = หลาย asset ใน ad set เดียว; อย่าทำพร้อมกันทั้งสองชั้น |
| 9 | **ROAS ในAds Manager ≠ กำไร** | ตรวจด้วย conversion lift / geo holdout และเทียบกับ MER หรือ blended CAC ทุกไตรมาส |
| 10 | **ทุกการทดลองต้องถูกบันทึกเป็นข้อมูล** | ใช้ `templates/experiment-log.csv` + `playbook/agent-rules.yaml` เพื่อให้ AI เรียนรู้จากผลจริง ไม่ใช่จากความรู้สึก |

---

## โครงเอกสาร

### วิจัย (ทำความเข้าใจระบบ)
| ไฟล์ | เนื้อหา |
|---|---|
| [`docs/00-executive-summary.md`](docs/00-executive-summary.md) | สรุปผู้บริหาร 1 หน้า: อะไรเปลี่ยน อะไรใช้ต่อ อะไรเลิกใช้ |
| [`docs/01-meta-ai-stack-2026.md`](docs/01-meta-ai-stack-2026.md) | แผนที่เครื่องมือ AI ทั้งหมดของ Meta: Andromeda, GEM, Muse, Advantage+ (Sales/Leads/Audience/Creative/Placements), Business AI, Creative enhancements 17 ตัว |
| [`docs/02-audience-and-targeting.md`](docs/02-audience-and-targeting.md) | กลไก Advantage+ Audience, control vs suggestion, audience architecture, exclusion logic, ตาราง target audience 12 แบบ |
| [`docs/03-placements-and-formats.md`](docs/03-placements-and-formats.md) | ทุก placement + สเปก + safe zone + วิธีใช้ Reels/Stories/Threads/Messenger/WhatsApp ต่างกัน |
| [`docs/04-creative-ai-production.md`](docs/04-creative-ai-production.md) | ระบบผลิตครีเอทีฟด้วย AI: concept matrix, hook, สคริปต์, asset, QA, เครื่องมือและข้อจำกัด |
| [`docs/05-measurement-and-incrementality.md`](docs/05-measurement-and-incrementality.md) | CAPI/EMQ/AEM, attribution, lift test, geo holdout, MER, dashboard ที่ควรมี |
| [`docs/06-thailand-market-context.md`](docs/06-thailand-market-context.md) | บริบทตลาดไทย: ขนาด Reach, พฤติกรรม, ภาษา, การจ่ายเงิน, LINE/chat commerce |

### เพลย์บุ๊ก (เอาไปใช้)
| ไฟล์ | เนื้อหา |
|---|---|
| [`playbook/README.md`](playbook/README.md) | เพลย์บุ๊ก 90 วัน + operating cadence รายสัปดาห์ + decision rules + guardrails |
| [`playbook/prompt-library.md`](playbook/prompt-library.md) | คลัง prompt ภาษาไทย 14 ชุด (วิจัย, persona, hook, สคริปต์ Reels, copy, วิเคราะห์ผล, post-mortem) |
| [`playbook/agent-rules.yaml`](playbook/agent-rules.yaml) | กติกาที่เครื่องอ่านได้ สำหรับ AI agent/automation (scale/kill/refresh/alert) |

### เทมเพลต
| ไฟล์ | ใช้ทำอะไร |
|---|---|
| [`templates/campaign-naming.md`](templates/campaign-naming.md) | โครงชื่อแคมเปญ/ad set/ad + UTM ให้ query ได้ด้วย AI |
| [`templates/creative-brief.md`](templates/creative-brief.md) | บรีฟครีเอทีฟ 1 หน้า ที่ส่งให้ AI หรือทีมผลิต ได้เลย |
| [`templates/weekly-review.md`](templates/weekly-review.md) | วาระประชุมรีวิวรายสัปดาห์ + คำถามที่ต้องตอบ |
| [`templates/experiment-log.csv`](templates/experiment-log.csv) | สมุดบันทึกการทดลอง (ห้ามลบ — เป็นหน่วยความจำของ AI) |

### อ้างอิง
| ไฟล์ | เนื้อหา |
|---|---|
| [`notes/2026-11-06-research-notes.md`](notes/2026-11-06-research-notes.md) | โน้ตดิบจากการวิจัย (timeline, ข้อสังเกต, สิ่งที่ยังไม่ยืนยัน) |
| [`sources.md`](sources.md) | แหล่งอ้างอิงทั้งหมดพร้อมวันที่ |

---

## ลิงก์เวอร์ชันมือถือ/อ่านนอก repo

| ที่ | ลิงก์ |
|---|---|
| **Google Docs (Notes)** | [Meta Ads × AI Playbook 2026 — Notes (TH)](https://docs.google.com/document/d/1Gz2zKZZ5svZ0jjaVxYEZc9_Yb2AY22-HoFPxwm84A28/edit) |
| **Notion** | [Meta Ads × AI Playbook 2026](https://app.notion.com/p/Meta-Ads-AI-Playbook-2026-Facebook-IG-Reels-Threads-41076ada3488814c953eccd33af83ca3) |

> Google Docs เป็นฉบับย่อสำหรับอ่าน/แชร์ (13 ส่วน) ส่วน repo และ Notion มีตารางและไฟล์เทมเพลตครบที่สุด

---

## วิธีใช้กับ AI (สำคัญ)

1. **โหลดบริบท**: ให้ AI อ่าน `README.md` → `docs/02` → `docs/04` → `playbook/README.md` → `playbook/agent-rules.yaml`
2. **ให้ข้อมูลจริง**: export จาก Ads Manager (ระดับ ad) 30–90 วัน + ตาราง `templates/experiment-log.csv`
3. **สั่งงานเป็นรอบ**: ใช้ prompt ใน `playbook/prompt-library.md` ทีละชุด (ห้ามยัดทุกอย่างใน prompt เดียว)
4. **ปิดวง**: ทุกคำแนะนำของ AI ต้องกลายเป็นแถวใน experiment log → ผ่านไป 7–14 วัน บันทึกผล → ให้ AI อ่านซ้ำ
5. **牢记 guardrail**: AI ไม่มีสิทธิ์เพิ่มงบเกินกำหนด, ไม่มีสิทธิ์ลบข้อมูล, และทุกการเปลี่ยนแปลงต้องมีคนอนุมัติ (ดู `playbook/README.md` หัวข้อ Guardrails)

---

## สถานะความน่าเชื่อถือของตัวเลข

ตัวเลข performance ที่ Meta ประกาศ (เช่น Advantage+ เพิ่ม ROAS 22%, GEM เพิ่ม conversion 5%) เป็น **vendor-reported** — ใช้เป็นทิศทาง ไม่ใช่การรับประกัน ผลจริงขึ้นกับ signal quality, ราคาตลาด, และคุณภาพครีเอทีฟของแต่ละบัญชี

ตัวเลข Reach ตลาดไทยอ้างจาก DataReportal *Digital 2027: Thailand* (เผยแพร่ 4 พ.ย. 2026) และ *Digital 2026* — ดูรายละเอียดและ caveat ใน `sources.md`

---

## License / การนำไปใช้

เอกสารนี้เป็น research synthesis เขียนใหม่ทั้งหมด (ไม่ได้คัดลอกเนื้อหาจากแหล่งอ้างอิง) ใช้อ้างอิงภายในได้ตามสะดวก

> ต้นฉบับนำมาจาก [PR #1](https://github.com/poppath/AI_research/pull/1) (commit `6350f3842991b56b0b1439cbc81d6213e1919c23`); ข้อมูลและตัวเลขเป็นข้อมูล ณ พฤศจิกายน 2026 ควรตรวจสอบก่อนใช้งาน
