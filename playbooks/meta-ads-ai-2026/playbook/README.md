# Meta Ads × AI Playbook — คู่มือปฏิบัติการ 90 วัน

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> เอกสารนี้คือ "คู่มือใช้งาน" ไม่ใช่ทฤษฎี — ทุกหัวข้อมีสิ่งที่ต้องทำ, เกณฑ์ตัดสิน, และสิ่งที่ต้องบันทึก
> ใช้คู่กับ: `docs/02` (audience) · `docs/03` (placement) · `docs/04` (creative) · `docs/05` (measurement) · `prompt-library.md` · `agent-rules.yaml`

---

## 0. หลัก 6 ข้อของ playbook นี้

1. **Signal ก่อน Scale** — ไม่มี CAPI/EMQ ที่ดี ไม่มีสิทธิ์เพิ่มงบ
2. **คุมขอบ ปล่อยกลาง** — คุมพื้นที่/อายุ/ภาษา/exclusion; ปล่อย interest/placement ให้ AI
3. **ครีเอทีฟคือ targeting** — วัดที่ creative diversity ไม่ใช่จำนวน interest
4. **หนึ่งการเปลี่ยนแปลงต่อหนึ่งรอบ** — ไม่งั้นอ่านผลไม่ได้
5. **ทุกการทดลองมีสมุดบันทึก** — ไม่มี log = ไม่มีบทเรียน = AI ไม่เรียนรู้
6. **คนอนุมัติ AI ลงมือ** — automation ต้องมีเพดานและจุดหยุด

---

## 1. โครงสร้างบัญชีที่แนะนำ (Account Architecture)

### 1.1 โครงหลัก 4 แคมเปญ

```
01_SALES_ASC_TH_Broad
   └─ AS01_Broad_TH_Age25+_ExBuyer180        (Advantage+ Sales)
   └─ AS02_Signal_LAL1%_Purchaser            (Advantage+ Sales, suggestion)

02_CONSIDER_Leads_TH
   └─ AS01_AdvPlus_Leads_Broad               (Advantage+ Leads)
   └─ AS02_Interest_Cluster_3to5             (manual + Adv+ audience)

03_RETARGET_30D
   └─ AS01_Web30D_ExBuyer30
   └─ AS02_Engage365_ExLead90

04_TEST_SANDBOX
   └─ AS01_Test_<hypothesis>                 (1 แคมเปญ/1 การทดลอง)
```

### 1.2 ตัวอย่างการจัดสรรงบ 100,000 THB/เดือน

| แคมเปญ | งบ/วัน | % | KPI หลัก |
|---|---|---|---|
| 01 Sales (ASC) | 2,300 | 70% | CPA ≤ เป้า, MER |
| 02 Leads/Consideration | 500 | 15% | cost per qualified lead |
| 03 Retargeting | 330 | 10% | incremental CPA, frequency |
| 04 Test | 170 | 5% | learning (ไม่ตัดสินจาก ROAS) |

> ปรับได้ แต่หลักคือ **อย่าให้ retargeting เกิน 15%** และ **อย่าให้ test ถูกตัดงบจนอ่านผลไม่ได้** (ต้องมีอย่างน้อย ~3× CPA ต่อการทดลอง)

### 1.3 กติกาโครงสร้าง
- 1 objective = 1 แคมเปญ
- อย่าเกิน 3–5 ad set ต่อแคมเปญ (งบกระจายเกินไป → ไม่ผ่าน learning phase)
- อย่าเปลี่ยนชื่อ/โครงสร้างระหว่างการทดสอบ
- ใช้ naming convention จาก `templates/campaign-naming.md` ทุกครั้ง

---

## 2. แผน 90 วัน

### สัปดาห์ 0 (ก่อนเริ่ม) — Audit
| งาน | ผลลัพธ์ |
|---|---|
| ตรวจ Pixel/CAPI/EMQ/AEM | รายงานช่องโหว่ signal |
| Export ข้อมูล 90 วัน (ad level) | baseline: CPA, ROAS, CPM, CTR, CVR |
| ตรวจ ad set ที่ใช้ interest ถูกยกเลิก | รายการที่ต้องแก้ |
| คำนวณ breakeven ROAS + MER | เป้าหมายทางธุรกิจ |
| ตั้ง experiment log + naming | โครงข้อมูลพร้อม |

### วันที่ 1–30: Foundation (วางราก)
| สัปดาห์ | ทำอะไร | Definition of done |
|---|---|---|
| 1 | แก้ signal: CAPI dedup, EMQ, AEM, event taxonomy, QualifiedLead | EMQ ≥ 6.0, event ครบ |
| 2 | Restructure: 4 แคมเปญตาม §1, ย้ายงบ, ตั้ง exclusion, existing-customer cap | โครงสร้างใหม่ live, ไม่มี ad set ซ้อน |
| 3 | ผลิตครีเอทีฟชุดแรก 10–15 ชิ้น (3 persona × 3 angle × format) | ผ่าน QA checklist 100% |
| 4 | เปิด placement value rule + เริ่มทดลองแรก (creative concept) | value rule live, log อัปเดต |

**KPI วันที่ 30**: EMQ ≥ 6.5 · ≥ 70% spend ในแคมเปญที่ผ่าน learning · ครีเอทีฟ ≥ 10 ชิ้น · มี 2 การทดลองที่บันทึก

### วันที่ 31–60: Build (หาจุดชนะ)
| สัปดาห์ | ทำอะไร | Definition of done |
|---|---|---|
| 5 | วิเคราะห์ creative win rate, ตัดตัวแพ้, ขยายตัวชนะ | ผู้ชนะ 2–3 concept |
| 6 | ทดลอง placement (Threads value rule 0.3 vs 1.0) | ผล +/- ชัดเจน |
| 7 | ทดลอง audience (broad vs LAL1%) | ผล +/- ชัดเจน |
| 8 | ปรับ offer/copy ตาม objection ที่เจอ + เริ่ม looking at MER | MER stable, CPA ลด |

**KPI วันที่ 60**: CPA ลด 10% · creative win rate ≥ 20% · มี 4–6 การทดลอง · frequency < 3

### วันที่ 61–90: Scale (ขยายอย่างมีวินัย)
| สัปดาห์ | ทำอะไร | Definition of done |
|---|---|---|
| 9 | เพิ่มงบผู้ชนะ 20%/รอบ (ทุก 2–3 วัน) + เฝ้า CPA | CPA ไม่เพิ่ม > 15% |
| 10 | เปิดช่องทางใหม่ (Threads/WhatsApp/IG Reels) + ครีเอทีฟเฉพาะช่อง | มีข้อมูล comparison |
| 11 | รัน lift test หรือ geo holdout | ผล lift + confidence |
| 12 | Post-mortem + เขียน playbook v2 + อัปเดต agent rules | เอกสาร + rules อัปเดต |

**KPI วันที่ 90**: MER ไม่ลดขณะ scale 20% · มี lift result 1 ครั้ง · ระบบ log ครบ 100% · playbook v2

---

## 3. Decision Rules (เกณฑ์ตัดสิน)

> ตัวเลขเหล่านี้คือ **จุดเริ่มต้น** ให้ calibrate กับบัญชีจริงหลัง 60 วัน

### 3.1 Scale
```
ถ้า CPA ≤ เป้า × 0.9 ต่อเนื่อง 3 วัน
และ spend ≥ 2 × CPA
และ ad set ผ่าน learning phase (≥ 50 conv/สัปดาห์)
→ เพิ่มงบ 20% ทุก 2 วัน จนถึงเพดานที่กำหนด
→ หยุดเพิ่มถ้า CPA เพิ่ม > 15% จาก baseline
```

### 3.2 Hold
```
ถ้า CPA อยู่ระหว่าง 0.9–1.2 × เป้า
→ ไม่แตะ 3 วัน (อย่าแก้อะไรเพราะระบบยังเรียนรู้)
```

### 3.3 Kill
```
ถ้า CPA > 1.5 × เป้า ต่อเนื่อง 5 วัน และ spend ≥ 3 × CPA
→ ปิด ad set/ad
ถ้า CTR < 0.5% และ frequency > 2.5 → ปัญหาครีเอทีฟ ไม่ใช่ audience
```

### 3.4 Refresh Creative
```
ถ้า frequency > 3 (7 วัน) หรือ CTR ลด > 25% สัปดาห์ต่อสัปดาห์
→ เปลี่ยน hook ก่อน (ถูกสุด) → แล้วจึงเปลี่ยน angle
```

### 3.5 Placement
```
ถ้า placement spend > 15% และ CPA > 1.3 × เฉลี่ย
→ ตั้ง value rule 0.3× (Threads/AN) แล้วรอ 7 วัน
ถ้า CPA < 0.8 × เฉลี่ย → เพิ่ม value 1.2–1.5×
```

### 3.6 Budget reallocation
```
ทุกวันจันทร์: ย้ายงบจากแคมเปญที่ CPA > 1.3× เป้า ไปยังแคมเปญที่ CPA < 0.9× เป้า
ขนาดการย้าย ≤ 20% ของงบแคมเปญ/ครั้ง
```

### 3.7 Stop / Escalate
```
ถ้า spend วันนี้ > เพดานรายวัน × 1.2 → หยุด automation + แจ้งคน
ถ้า EMQ ลด > 1.0 → แช่แข็งการสเกลจนแก้ signal
ถ้า conversion volume ลด > 40% โดยไม่อธิบายได้ → ตรวจ event/tracking ก่อนสรุปว่า performance ตก
```

---

## 4. Operating Cadence (จังหวะการทำงาน)

| รอบ | เวลา | ผู้เข้าร่วม | วาระ |
|---|---|---|---|
| **Daily check** | 10 นาที | คนดูแลแอด | spend vs cap, error, CPA anomaly, event ไหลปกติ |
| **Weekly review** | 45 นาที | media buyer + creative + analytics | §5 (ใช้ `templates/weekly-review.md`) |
| **Bi-weekly creative** | 60 นาที | creative + strategist | concept ใหม่ 3–5 ชิ้น, ตรวจ fatigue |
| **Monthly business** | 60 นาที | marketing + finance | MER, CAC, contribution, LTV:CAC |
| **Quarterly truth** | 90 นาที | ทุกฝ่าย | lift/geo/MMM, recalibrate rules, playbook update |

### 4.1 Weekly review — 7 คำถาม
1. สัปดาห์นี้เราเรียนรู้อะไรที่ไม่รู้เมื่อสัปดาห์ก่อน?
2. อะไรชนะ/แพ้ และเพราะอะไร (ไม่ใช่แค่ตัวเลข)?
3. มี ad set ไหนออก/เข้า learning phase?
4. ครีเอทีฟไหนต้อง refresh?
5. Placement mix เปลี่ยนไหม?
6. MER ขยับอย่างไร?
7. สัปดาห์หน้าจะทดลองอะไร (1 อย่าง)?

---

## 5. Creative Operating System (สรุป)

```
INPUT: รีวิวลูกค้า, คอมเมนต์, แชท, คำถามจาก sales, เสิร์ชเทอม
   ↓ (LLM สรุป insight + objection)
CONCEPT: 3 persona × 3 awareness × 3 angle = 27 → เลือก 12–15
   ↓
PRODUCTION: Reels 9:16 (3–5 ชิ้น), Feed 4:5 (3–5), Carousel (2), Threads copy (2)
   ↓
QA: safe zone + subtitle + ราคา + แบรนด์ + กฎหมาย
   ↓
LAUNCH: 10–15 ชิ้น/ad set (ห้ามน้อยกว่า 6)
   ↓
LEARN: 7–14 วัน → win rate → concept ใหม่
```

**กติกา creative test**:
- ทดสอบ *hook* ก่อน *visual* ก่อน *offer*
- อย่าทดสอบพร้อมกันเกิน 1 ตัวแปรต่อ 1 การทดลอง
- เก็บ "ผู้ชนะ" ไว้เป็น asset ต้นแบบ (evergreen) แล้วผลิต variant จากมัน
- อย่าลบครีเอทีฟที่แพ้ทันที — เก็บไว้เป็นหลักฐานว่าอะไรไม่ทำงาน

---

## 6. AI Automation & Agent Design

### 6.1 ระดับ autonomy 4 ขั้น

| ระดับ | AI ทำอะไร | ตัวอย่าง | ต้องอนุมัติ |
|---|---|---|---|
| L0 Manual | ไม่มี automation | คนกดเองทั้งหมด | — |
| L1 Assist | วิเคราะห์/เสนอ | รายงาน weekly, เสนอ scale/kill | คนอนุมัติทุก action |
| L2 Supervised | ลงมือในกรอบแคบ | ปรับ bid ภายใน ±10%, ตั้ง value rule | แจ้งเตือนหลังทำ |
| L3 Autonomous | ลงมือข้ามแคมเปญ | reallocate งบ, pause, launch | ต้องมีเพดาน + audit log |

**คำแนะนำ**: เริ่มที่ L1 → 2 เดือน → L2 เฉพาะ rule ที่ผ่านการทดสอบแล้ว → L3 เฉพาะธุรกิจที่มีทีม data และเพดานชัดเจน

### 6.2 สถาปัตยกรรมขั้นต่ำสำหรับ agent

```
[Data]  Ads Insights API + backend orders + experiment log
    ↓
[Brain] LLM + agent-rules.yaml (กติกา) + brand guide
    ↓
[Action] Marketing API (read-only ก่อน → write ภายหลัง)
    ↓
[Guard] spend cap, whitelist actions, approval queue, audit log
    ↓
[Memory] experiment_log + creative_registry + post-mortems
```

**เริ่มจาก read-only 30 วัน** — ให้ agent "อ่านและอธิบาย" ก่อน "ลงมือ"

### 6.3 สิ่งที่ agent ควรทำได้ (และไม่ควร)
| ควร | ไม่ควร |
|---|---|
| สรุปรายงานรายสัปดาห์ | เปลี่ยนข้อความที่มีผลทางกฎหมาย |
| ตรวจจับ anomaly | เพิ่มงบเกินเพดาน |
| เสนอ scale/kill | ลบข้อมูลการทดลอง |
| สร้าง creative brief | สร้างรีวิว/ใบรับรองปลอม |
| ตั้ง value rule ตามสูตร | เปลี่ยน special ad category |
| จัดกลุ่มข้อความลูกค้าเป็น insight | ส่งข้อมูลส่วนบุคคลออกนอกระบบ |

---

## 7. Guardrails (ต้องมีก่อนเปิด automation ใด ๆ)

| Guardrail | ค่าเริ่มต้น |
|---|---|
| Daily spend cap | 100–110% ของงบประมาณ |
| Max single budget change | 20% |
| Freeze window | ห้ามแก้ 24 ชม. หลัง launch / ระหว่างทดสอบ |
| Human approval | action ที่เพิ่มงบ > 20% หรือปิดแคมเปญ |
| Brand safety | banned words, banned claims list |
| PII | ไม่ส่งข้อมูลดิบออก; hash เท่านั้น |
| AI disclosure | เนื้อหา AI ต้อง label ตามนโยบาย |
| Audit log | ทุก action: ใคร/อะไร/เมื่อไหร่/เพราะอะไร |
| Rollback | เก็บ snapshot การตั้งค่าก่อนแก้ |
| Kill switch | ปุ่มหยุด automation ทั้งหมด |

**กฎเหล็ก**: ถ้า agent ทำงานผิด ให้ปิดที่ kill switch ก่อน แล้วค่อยหาสาเหตุ — อย่าแก้กลางระบบที่กำลังรัน

---

## 8. Roles & RACI (ทีมเล็ก)

| งาน | Media buyer | Creative | Analyst | AI/Agent | Owner |
|---|---|---|---|---|---|
| โครงสร้างแคมเปญ | A | C | C | R (เสนอ) | **A** |
| ผลิตครีเอทีฟ | C | **A** | I | R (variant) | **A** |
| ตั้ง audience/exclusion | **A** | I | C | R (ตรวจ) | **A** |
| วัดผล/รายงาน | C | I | **A** | R (สรุป) | **A** |
| ตัดสิน scale/kill | **A** | I | C | R (เสนอ) | **A** |
| Guardrail/เพดาน | **A** | I | C | R (บังคับใช้) | **A** |

> A = Accountable, R = Responsible, C = Consulted, I = Informed

---

## 9. Playbook Maintenance

- **ทุกสัปดาห์**: อัปเดต `experiment_log.csv`
- **ทุกเดือน**: ทบทวน decision rules (ตัวเลขจริง vs เกณฑ์)
- **ทุกไตรมาส**: อัปเดต `docs/` ตามการเปลี่ยนแปลงของ Meta (placement/นโยบาย/เครื่องมือ)
- **ทุกครั้งที่ Meta อัปเดต**: เพิ่มบรรทัดใน `notes/` พร้อมวันที่ เพื่อให้ AI อ่าน timeline ได้

---

## 10. Definition of Done (ใช้ตรวจก่อนถือว่างานเสร็จ)

- [ ] โครงสร้าง ≤ 4 แคมเปญ, ≤ 3–5 ad set/แคมเปญ
- [ ] ทุก ad set มี exclusion + hard controls
- [ ] EMQ ≥ 6.0 และ AEM ตั้งถูก
- [ ] มี 9:16 + 4:5 + copy สำหรับ Threads
- [ ] placement value rule ตั้งแล้ว
- [ ] creative ≥ 10 ชิ้น/ad set หลัก, ผ่าน QA
- [ ] experiment log มีรายการของการเปลี่ยนแปลงทั้งหมด
- [ ] dashboard 3 ระดับอัปเดต
- [ ] มีเจ้าของ (owner) และวันทบทวนถัดไปชัดเจน
