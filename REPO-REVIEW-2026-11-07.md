# Repo review และ gap register · 7 พ.ย. 2026

## ขอบเขตและความเชื่อมั่น

ตรวจ inventory ทั้ง repo (ก่อนแก้: 254 files, 183 Markdown, 69 JSON, 1 YAML, 1 CSV; 16 playbook directories), syntax JSON, relative Markdown links และจำนวน GICS; ตรวจเนื้อหาเชิงลึกแบบ **risk-based sampling** ใน repo rules, README, profit calculations/sources/JSON, TikTok budgets, short guides และ GICS. ไม่ใช่การ fact-check ทีละ claim, ทดสอบ API, ตรวจทุก external link หรือ legal audit. การผ่าน structural check ไม่ใช่การรับรองความจริงหรือความครบถ้วนของเนื้อหา.

**สถานะโดยรวม: ยังไม่ครบถ้วน/ไม่พร้อมใช้เป็น autonomous decision engine.** บางส่วนเป็น starter guide, บางส่วนเป็น research snapshot ที่ตัวเลขและข้ออ้างเสี่ยงล้าสมัยหรือยังยืนยันไม่ได้. ใช้ GitHub เป็น source of truth; Docs/Notion เป็น snapshot ไม่ sync และอาจไม่มี correction รายบรรทัด.

## Findings และการดำเนินการ

| Priority | Gap / หลักฐาน | สิ่งที่ทำรอบนี้ | ค้าง / เงื่อนไขก่อนใช้ |
|---|---|---|---|
| P0 | สูตร discount ใน profit บท 07 และ JSON หัก margin เปอร์เซ็นต์ตรง ๆ ทั้งที่ denominator เปลี่ยน; 30% → 18% ไม่ได้แปลว่า cap 12% | แก้สูตรพร้อม assumptions, numerical examples, JSON, METRICS และ regression tests | ค่าธรรมเนียมหลายฐาน/ขั้นบันได, VAT, subsidy และ returns ต้องคำนวณจากสัญญาจริง |
| P0 | Quick start profit เรียก CM1 หลังหัก fees ขัดบท 03 ซึ่งเรียก CM2; สูตร CAC ซ้ำหน่วย และ COD ปน revenue กับ cost | แก้ quick start ให้ตรงนิยามและระบุ contribution/window | ตรวจสูตรและตัวอย่าง profit อื่นทีละรายการก่อนใช้จริง; ค่าใน JSON อื่นยังมี heuristic เก่า |
| P0 | `AGENTS.md` บังคับ 18% floor, refusal 8–12%, attribution overlap 20–40%, GP cut, 50 conversions และ freeze edits เป็นกฎทั่วไป | ปรับเป็น account-specific, sourced, stop-on-incident; precedence ชัดเหนือ heuristic เก่า; ใส่ warning ใน prose และ JSON ของ playbook เสี่ยง | legacy prose/JSON ยังมีตัวเลขเดิม: ต้อง re-verify รายข้อก่อนนำไปใช้ ไม่ใช้เป็น decision threshold อัตโนมัติ |
| P0 | รายงาน GP cut source [11] เป็น vendor แต่ METRICS เรียก primary; ยังไม่ได้ตรวจคำประกาศต้นฉบับ | แก้ label ที่พบใน METRICS และ benchmarks JSON (รวม source [3]) และเตือนทั้งชุด | ยืนยันจากผู้มีอำนาจและ rate card ที่ตรงบัญชี/หมวด/ช่วงเวลาจริง ก่อนใช้งบหรือกำหนดราคา |
| P1 | TikTok chapter แสดง $50 = ฿500 และ $20 = ฿50 ซึ่งไม่ใช่อัตราแปลงที่มีหลักฐาน | เอา THB ที่ชวนเข้าใจว่าแปลงสกุลเงินออก | ตรวจ minimum ตาม account, currency, objective และเวลา; ค่าที่แสดงไม่ได้ตรวจปัจจุบัน |
| P1 | README ไม่แสดง 7M, ตารางขาดตอน และคำว่า every chapter/sources/JSON สื่อว่าเหมือนกันทั้งหมด | เพิ่มลิงก์ 7M, จัดตาราง และปรับคำอธิบายความหลากหลาย | Meta ใช้ YAML ไม่ใช่ playbook.json; sector ใช้ common source ร่วม; parser ต้องรู้รูปแบบ |
| P1 | ตรวจซ้ำด้วยมืออย่างเดียว; ไม่มี structural checks/discount tests | เพิ่ม `scripts/check_repo.py` และ `tests/test_discount_math.py` ใช้ stdlib | ยังไม่ตรวจ anchors, external availability, YAML schema, source-claim entailment, platform policy หรือ clinical/legal correctness |
| P1 | GICS ระดับ 25 groups มีตัวอย่างย่อย ไม่ใช่ inventory 74 industries/163 sub-industries; ใช้ generic 7M ซ้ำ | คงขอบเขตและป้ายตัวอย่างอย่างชัดเจน | ทำ taxonomy ลึกกว่า group จาก methodology ที่ใช้อยู่ ตรวจสิทธิการใช้งาน, version/codes และ review ทีละรายการ; ทำ niche-specific operating economics และ evidence |
| P1 | 20 sector guides และบาง horizontal guides เป็น starter ไม่ใช่ detailed operating manual; บาง benchmark ว่างโดยเจตนา | บันทึก coverage และลำดับทำงานด้านล่าง; ไม่เติมตัวเลขที่ไม่มีแหล่ง | สัมภาษณ์ผู้ประกอบการ, source research, ตัวอย่างและ validation แยกแต่ละ niche/ประเทศ |
| P1 | source label ไม่สม่ำเสมอ: AGENTS เรียก primary เป็น account measurement แต่ profit sources ใช้ official; แหล่งบางรายการเป็น landing page/vendor ไม่ใช่หลักฐานตรง | ระบุ mapping ข้างล่างและขั้นตอน verification | ตรวจ source_ref/ทุก claim ทุกไฟล์และ record วันที่เข้าถึง, URL ตรง, quote, scope, effective date |
| P2 | ไม่มี schema รวมข้าม playbooks; YAML/JSON มีโครงสร้างต่างกัน; benchmark ว่างจำนวนมาก | checker ตรวจ syntax ไม่บังคับ schema ผิดกับข้อมูลเดิม | นิยาม versioned schema + migration และ ownership; ห้ามมอง empty benchmark เป็นศูนย์ |
| P2 | หลาย guides ยังไม่มีหลักฐานการทดลองในบัญชี, incident drill, third-party integration tests หรือ owner | ระบุ readiness gate ด้านล่าง | ต้องทดสอบในบัญชีจริงโดยเจ้าของอนุมัติ ไม่กล่าวอ้างว่าได้รันทดสอบแล้ว |

## Coverage map

- **Deep chapters แต่เสี่ยงตัวเลขเก่า:** TikTok, LINE, profit, Meta — สัญญาณ detail ไม่เท่ากับ fact-checked; ใช้ source และ dates ตรวจทุกตัวเลขก่อนตัดสินใจ.
- **หลายบทเชิงวิธี:** 7M affiliate/automation, AI creative, customer research, measurement, CRO, Google Ads — มีขั้นตอนและ risk gates แต่ยังไม่มีผลลัพธ์จากบัญชีจริง.
- **Starter ความละเอียดจำกัด:** brand/organic, customer experience, fulfillment, offers, marketing planning — ให้ framework ไม่ใช่ production SOP เฉพาะธุรกิจ; ต้องเติม role, input/output, data source, scenario และ acceptance criteria ตามบริบท.
- **Taxonomy + starter:** 20 sector guides, 11 GICS sector pages/25 groups; ตัวอย่าง business และ crosswalk ไม่ใช่ official company assignments หรือ S&P 500 constituents. ไม่ครบทุก niche หรือ GICS sub-industry.

## Source และ freshness gate

1. แยก `account_primary` = first-party account measurement, `official` = regulator/platform ระบุ scope, `vendor`/`press` = secondary, `est` = สมมติฐาน/คำนวณ. ชื่อ `primary` เดิมมีสองความหมาย **ห้ามรวมสองแบบโดยอัตโนมัติ**.
2. ก่อนใช้: claim → URL ตรงและวันที่มีผล → platform/product/ประเทศ/บัญชี → เอกสารต้นฉบับ → owner ตรวจ → วันทบทวน. หากเจอ vendor อย่างเดียว ให้ระบุว่ายังไม่ยืนยัน ไม่ยกระดับเป็น official.
3. ตัวเลขเกิน 90 วันให้ตรวจใหม่ก่อน budget decision; ตัวเลขอายุน้อยกว่านั้นก็ยังไม่รับประกันว่าถูกหรือใช้กับบัญชีนี้ได้. ไม่พบข้อมูลให้ใช้ “ไม่มีข้อมูล — ต้องวัดเอง”.
4. Legal/health/finance ต้องให้ผู้เชี่ยวชาญใน jurisdiction ตรวจ; platform permission, IP, consent และ disclosure เป็น hard gates.

## ลำดับปิด gap ที่ยังค้าง

1. **Safety first:** ตรวจ profit/LINE/TikTok/Meta ทั้ง prose และ machine rules รายข้อ โดยเริ่มสูตร, fees, finance/health/legal และ platform permissions; ระบุ verified/unverified/obsolete พร้อมแหล่งตรง ไม่คง universal thresholds.
2. **Evidence ledger:** แยก claim ID, source URL, publisher, effective/access date, account/market, confidence, reviewer และ next review; ทำ reconciliation กับ JSON source references.
3. **Coverage expansion:** เลือก niches ตาม impact; ลงระดับ 74/163 เฉพาะเมื่อ mapping กับ methodology รุ่นล่าสุดและตรวจ licensing ได้; ทำ business-model playbook ที่มีตัวอย่าง input → calculation → output → exception → owner.
4. **Machine readiness:** schema version, CI ตรวจ links/JSON/schema/citation/date และ unit tests สูตร; human approval, permissions, least privilege, logging, rollback และ incident drill ก่อนเชื่อมเครื่องมือจริง.
5. **Reality validation:** ทดลอง pilot แบบจำกัด cash/เวลา/สิทธิ พร้อม owner, baseline, primary KPI, 2 guardrails, stop rule และ reconciliation; แล้วบันทึกผลจริงแยกจากสมมติฐาน.

## ตรวจซ้ำในเครื่อง

```
python scripts/check_repo.py
python -m unittest discover -s tests -v
git diff --check
```

การตรวจนี้เป็น automated structural/math smoke test เท่านั้น ไม่มี network และไม่ตรวจความจริงของ claims.
