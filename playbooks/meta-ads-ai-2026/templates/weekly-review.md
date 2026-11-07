# Weekly Review — วาระ 45 นาที (Meta Ads × AI)

> ใช้ทุกวันจันทร์ · เตรียมข้อมูลก่อนประชุม 15 นาที · ห้ามประชุมโดยไม่มีตัวเลข

---

## 0. ข้อมูลที่ต้องเตรียม (ก่อนประชุม)

- [ ] Export Ads Manager ระดับ ad: 7 วัน + 28 วัน (`spend, impressions, clicks, conversions, revenue, frequency`)
- [ ] EMQ + event volume จาก Events Manager
- [ ] Placement report (spend %, CPA)
- [ ] ตาราง `templates/experiment-log.csv` ที่อัปเดตแล้ว
- [ ] ตัวเลขธุรกิจ: orders, revenue, new customers, refunds (จาก backend)
- [ ] MER / breakeven ROAS ของเดือน

---

## 1. Signal Health (5 นาที)

| ตัวชี้วัด | สัปดาห์ก่อน | สัปดาห์นี้ | สถานะ |
|---|---|---|---|
| EMQ (Purchase/Lead) | | | 🟢 ≥7 / 🟡 6–7 / 🔴 <6 |
| Event volume (7d) | | | |
| Dedup rate | | | |
| Purchase events last 24h | | | |

**คำถาม**: มีอะไรที่ทำให้ตัวเลข performance "ดูดี/แย่" เพราะ tracking ไม่ใช่เพราะแคมเปญ?

---

## 2. Delivery & Structure (10 นาที)

| แคมเปญ | Spend | % งบ | CPA | vs เป้า | Learning phase | Frequency |
|---|---|---|---|---|---|---|
| 01 Sales | | | | | | |
| 02 Leads | | | | | | |
| 03 Retarget | | | | | | |
| 04 Test | | | | | | |

**ตรวจ**:
- มี ad set ไหนติด learning นาน > 7 วัน?
- มี ad set ที่ถูกแก้จน reset?
- งบกระจายเกิน 5 ad set/แคมเปญหรือไม่?

---

## 3. Creative Performance (10 นาที)

### Top 5

| Creative | Persona | Angle | Hook | CPA | CTR | Spend | สถานะ |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### Bottom 5

| Creative | CPA | CTR | สาเหตุที่สงสัย | Action |
|---|---|---|---|---|
| | | | | |

**คำถาม**:
1. มี pattern อะไรในผู้ชนะ? (persona/angle/hook/format)
2. มีชิ้นไหน fatigue? (frequency > 3 หรือ CTR ลด > 25%)
3. ต้องผลิต concept ใหม่กี่ชิ้นสัปดาห์หน้า?

---

## 4. Placement Mix (5 นาที)

| Placement | Spend % | CPA | vs เฉลี่ย | Action (value rule) |
|---|---|---|---|---|
| FB Feed | | | | |
| FB Reels | | | | |
| IG Feed | | | | |
| IG Reels | | | | |
| IG Stories | | | | |
| Threads | | | | |
| Audience Network | | | | |

---

## 5. Business Outcome (5 นาที)

| ตัวชี้วัด | เดือนก่อน | เดือนนี้ | เป้า |
|---|---|---|---|
| MER | | | |
| Blended CAC | | | |
| Contribution | | | |
| LTV:CAC | | | |
| Payback (เดือน) | | | |

**คำถาม**: ถ้า MER แย่ลง แต่ ROAS ดีขึ้น → เกิดอะไรขึ้น? (มักแปลว่า attribution over-credit)

---

## 6. Experiments (5 นาที)

| ID | สมมติฐาน | ผล | Verdict | บทเรียน |
|---|---|---|---|---|
| | | | win/lose/inconclusive | |

**คำถาม**: บทเรียนไหนควรกลายเป็น rule ถาวร? (ส่งเข้า `agent-rules.yaml`)

---

## 7. Decisions & Next Week (5 นาที)

### ตัดสินใจวันนี้
| Action | Owner | Deadline |
|---|---|---|
| Scale: | | |
| Hold: | | |
| Kill: | | |
| Refresh creative: | | |

### การทดลองสัปดาห์หน้า (เลือก 1 อย่าง)
- สมมติฐาน:
- ตัวแปร:
- เกณฑ์ชนะ:
- งบ:
- ระยะเวลา:

---

## 8. บันทึก 3 บรรทัด (บังคับ)

```
เรียนรู้อะไร: ______________________________________
จะทำอะไร: _________________________________________
ต้องรออะไร: _______________________________________
```

> ถ้าตอบสามข้อนี้ไม่ได้ แปลว่าประชุมไม่เกิดการเรียนรู้ — ให้กลับไปดูข้อ 1 และ 6 อีกครั้ง
