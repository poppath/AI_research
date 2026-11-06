# Research Notes — 2026-11-06

> โน้ตดิบจากการวิจัย (ไม่ผ่านการเกลาเหมือน docs/) เก็บไว้เพื่อให้เห็น *ที่มา* ของข้อสรุป, *ความไม่แน่ใจ*, และ *สิ่งที่ต้องอัปเดตครั้งหน้า*
> **ห้ามลบไฟล์นี้** — เป็น timeline ให้ AI รู้ว่าโลกเปลี่ยนตอนไหน

---

## 1. คำถามวิจัย

1. Meta เปลี่ยนกลไกโฆษณาอย่างไรในช่วง 2024–2026 และมีผลต่อการตั้ง targeting/audience อย่างไร?
2. เครื่องมือ AI ทั้งหมดของ Meta มีอะไร ใช้ตอนไหน และมีข้อจำกัดอะไร?
3. Placement ทุกตัว (FB, IG, Reels, Stories, Threads, Messenger, WhatsApp, AN) ต้องใช้ครีเอทีฟต่างกันอย่างไร?
4. ระบบวัดผลแบบไหนที่แยก "เครดิต" ออกจาก "สาเหตุ" ได้?
5.playbook ที่ AI อ่านแล้วนำไปใช้ต่อได้ควรมีโครงอย่างไร?

## 2. วิธีการ

- ค้นเว็บ (พ.ย. 2026) เน้นแหล่งที่อ้างถึง Meta Business Help Center / Marketing API changelog / DataReportal
- ตรวจ cross-source สำหรับตัวเลขที่สำคัญ (เช่น safe zone, EMQ, lift threshold)
- แยกข้อมูลเป็น 3 ชั้น: **ยืนยันได้** / **vendor-reported** / **ยังไม่ชัด**
- สังเคราะห์เป็น playbook + rules + prompts (ไม่ได้คัดลอกเนื้อหา)

---

## 3. Timeline ที่ต้องจำ

| เวลา | เหตุการณ์ | ผลต่อ advertiser |
|---|---|---|
| ปลาย 2024 | เปิดใช้ **Andromeda** (retrieval engine, ความจุโมเดลเพิ่มมาก) | ครีเอทีฟมีผลต่อการจับคู่ผู้ชมมากขึ้น |
| 2025 | ถอด **detailed targeting exclusions** | ต้องใช้ custom audience exclusion แทน |
| 2025 | ขยาย **Advantage+ Leads** | ใช้ AI กับ lead gen ได้ |
| มิ.ย. 2025 | Cannes Lions: 11 เครื่องมือ gen-AI (brand kit, image-to-video, video highlights, Business AI, sticker CTA, virtual try-on, dubbing) | ผลิตครีเอทีฟเร็วขึ้นมาก |
| 2025 | ประกาศ **GEM** (generative ad model) | สร้าง/ประกอบ creative element ใน Ads Manager |
| 15 ม.ค. 2026 | interest ที่ถูกยุบ/เลิกใช้ **หยุด delivering** | ต้องตรวจ ad set เก่า |
| 26 ม.ค. 2026 | **Threads ads** เปิดให้ผู้ใช้ทั้งหมดทั่วโลก | placement ใหม่ |
| 2026 | **Muse / Muse Image** ขับเคลื่อนการสร้างภาพ | คุณภาพภาพ AI ดีขึ้น |
| ส.ค. 2026 | **placement exclusions ถูกถอด** สำหรับ objective หลัก → ใช้ value rule | คุม placement ได้จำกัดลง |
| 29 ก.ย. 2026 | **Muse for Small Business** (approval-gated AI agent) | automation สำหรับ SME |
| 26 ต.ค. 2026 | **Threads เป็น default placement** ทุกแคมเปญ | งบไหลเข้า Threads อัตโนมัติ |
| 27 ต.ค. 2026 | Marketing API v26 changes; Messenger Stories + IG Explore ถูกถอดจาก API | ตรวจ integration |
| 4 พ.ย. 2026 | DataReportal *Digital 2027: Thailand* | อัปเดตตัวเลข reach ไทย |

---

## 4. ตัวเลขที่เก็บได้ (พร้อมระดับความมั่นใจ)

| ตัวเลข | ค่า | แหล่ง | ความมั่นใจ |
|---|---|---|---|
| Facebook ad reach ไทย | ~50.7M (ต.ค. 2026) | DataReportal Digital 2027 | สูง |
| Instagram ad reach ไทย | ~21.3M | DataReportal Digital 2027 | สูง |
| TikTok ad reach ไทย | ~70.3M (มีบัญชีซ้ำ) | DataReportal Digital 2027 | กลาง (ตัวเลขเกินจริง) |
| LINE MAU ไทย | ~56.3M | DataReportal Digital 2027 | สูง |
| Safe zone 9:16 | บน 14% / ล่าง 35% / ข้าง 6% | Meta Ads Guide (อ้างผ่านหลายแหล่ง) | สูง |
| Reels ความยาวแนะนำ | 5–15 วิ | หลายแหล่ง | กลาง–สูง |
| EMQ เป้าหมาย | ≥ 6.0, ดี 7.5–9.0 | ผู้ให้บริการ tracking + Meta docs | สูง |
| CAPI recovery | 15–25% (บางกรณี 30%) | ผู้ให้บริการ tracking | กลาง |
| 50 conversions/สัปดาห์/ad set | มาตรฐาน learning phase | Meta (long-standing) | สูง |
| Advantage+ ROAS +22% | vendor-reported | Meta | ต่ำ–กลาง (ใช้เป็นทิศทาง) |
| GEM conversion +5% | vendor-reported | Meta | ต่ำ–กลาง |
| Threads CPM ต่ำกว่า IG feed 20–40% | รายงานอุตสาหกรรม | several blogs | กลาง |
| Lift: >15% strong, 8–15% healthy, 3–8% weak, <3% negligible | แนวปฏิบัติ | agencies | กลาง |

---

## 5. สิ่งที่แหล่งข้อมูลขัดกัน (ต้องระวัง)

1. **Safe zone ล่าง**: บางแหล่งบอก 20% (Stories), บางแหล่ง 35% (Reels) → เลือก **35%** เป็นค่าที่ปลอดภัยที่สุด (ครอบทุก placement)
2. **ความละเอียดแนะนำ**: 1080×1920 vs 1440×2560 → Meta spec page บางหน้าบอก 1440×2560; 1080×1920 ยังใช้ได้
3. **จำนวน AI enhancements**: 17 ตัว (นับตาม Meta) vs 9 ตัว (นับเฉพาะที่ใช้บ่อย) → ใช้ 17 ตาม Meta
4. **ตัวเลข reach TikTok**: เกิน 100% ของผู้ใหญ่ → แสดงว่ามีบัญชีซ้ำ/การวัดไม่ตรง อย่าใช้เป็นตัวตั้งงบ
5. **"Advantage+ เพิ่ม ROAS 22%"**: เป็นค่าเฉลี่ยจากบัญชีที่ Meta คัดเลือก → อย่าสัญญากับลูกค้า

---

## 6. ข้อสังเกตเชิงกลยุทธ์ (ความเห็นของผู้วิจัย)

1. **ช่องว่างของ AI คือ "บริบท"** — Meta รู้ว่าคนไหนคลิก แต่ไม่รู้ว่าสินค้านี้แก้ปัญหาอะไรให้ใคร; LLM ช่วยเติมชั้นนี้ได้
2. **Creative homogenization เป็นความเสี่ยงใหม่** — เมื่อทุกคนใช้ AI ผลิต variant คล้ายกัน ความได้เปรียบจะย้ายไปที่ *insight จากลูกค้าจริง* และ *ความกล้าที่จะทดสอบสิ่งที่ต่าง*
3. **การวัดผลกำลังกลายเป็น competitive advantage** — คนที่รู้ iROAS จะกล้า scale ในขณะที่คนอื่นกลัว
4. **ตลาดไทยยังมีช่องว่างเรื่องแชท + AI** — click-to-LINE/WhatsApp ที่มี AI คัดกรอง จะลดต้นทุน lead ได้มาก แต่ยังมีน้อยรายที่ทำจริงจัง
5. **Threads เป็น arbitrage ที่มีวันหมดอายุ** — CPM ต่ำเพราะ ad load ต่ำ; เมื่อ ad load เพิ่มขึ้น (ซึ่งจะเกิด) ข้อได้เปรียบจะหายไป

---

## 7. สิ่งที่ยังไม่ชัด / ต้องตรวจรอบหน้า

- [ ] Threads ads effectiveness สำหรับ conversion ในตลาดไทย (ยังไม่มีข้อมูลเยอะ)
- [ ] ผลของ Muse Image ต่อคุณภาพภาพสินค้า (ยัง rollout ไม่ทั่ว)
- [ ] นโยบาย AI disclosure ของ Meta ในไทย (ข้อกำหนดทางกฎหมายยังไม่ชัด)
- [ ] ผลของ "AI-enabled audience discovery in Detailed Targeting" (ประกาศว่าภายในสิ้นปี 2026)
- [ ] Direct checkout ใน Meta AI / Business Agent (อยู่ในช่วงทดสอบ)
- [ ] ราคา CPM ไทยปี 2026 แยกตาม placement (ยังไม่มีข้อมูลเปิด)
- [ ] ผลของ Marketing API v26 ต่อเครื่องมือ third-party ที่ใช้อยู่

---

## 8. แหล่งที่ใช้อ่าน (สรุป)

- Meta Ads Guide / Business Help Center (ผ่านการอ้างในบทความหลายแหล่ง)
- DataReportal: Digital 2026 / Digital 2027 Thailand
- บทความ agency/analytics: adsuploader, adadvisor, commonthread, adplay, adquisition, optimyzee, growthmarketer, lionelz, jem.social, yosefk, mbadv, marketertools, perroly, redclawey, everydaymarketing, relevantaudience
- รายงานตลาดไทย: DAAT data cited in local reports, Priceza/The Nation, TikTok live commerce data

> รายละเอียด URL ดูที่ `sources.md`

---

## 9. หมายเหตุการอัปเดต

- **รอบถัดไป**: 2027-02-06 (หรือเมื่อ Meta ประกาศ การเปลี่ยนแปลงครั้งใหญ่)
- **สิ่งที่ต้องทำทุกรอบ**: ตรวจ changelog Marketing API, ตรวจ placement ใหม่, ตรวจตัวเลข reach, ทบทวน thresholds ใน `agent-rules.yaml`
