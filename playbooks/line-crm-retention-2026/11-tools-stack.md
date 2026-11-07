# บท 11 · Tools Stack — เลือกเครื่องมือให้คุ้ม

## TL;DR

- **เริ่มจาก native ก่อนเสมอ**: LINE OA Manager + MyCustomer CRM ครอบคลุม 80% ของ use case SME ไทย
- **ข้อจำกัดที่สำคัญที่สุด: 1 channel = 1 webhook URL** → เลือกแพลตฟอร์มบอทได้เจ้าหลักเจ้าหนึ่งเท่านั้น (ซื้อซ้อน = ระบบพัง)
- ลำดับการใช้จ่ายที่คุ้ม: แพ็กเกจข้อความ → CRM native → third-party CRM → custom build
- **อย่าจ่ายเพื่อฟีเจอร์ที่ยังไม่มีคนใช้** — ซื้อเครื่องมือเมื่อมี bottleneck ชัด ไม่ใช่เพราะน่าสนใจ
- ค่าใช้จ่ายที่คนลืมคิด: ค่าคน, ค่าออกแบบ asset, ค่าดูแลรายเดือน, ค่า migration

---

## 1 · Native stack (แนะนำเริ่มต้น)

| องค์ประกอบ | ราคา | ได้อะไร |
|---|---|---|
| LINE OA Free | ฿0 | 300 messages/เดือน, rich menu, greeting, auto-reply, step message |
| LINE OA Basic | ฿1,280/เดือน | 15,000 messages + ฿0.10 เกิน |
| LINE OA Pro | ฿1,780/เดือน | 35,000 messages + ฿0.06 เกิน + **MyCustomer CRM ฟรี** |
| MyCustomer CRM | ฿369/เดือน (ฟรีบน Pro) | membership, point, tier, targeted broadcast, dashboard |
| OA Chat Package | ฿555/เดือน | chat history 5 ปี, tag ≤300, note, **AI Chatbot (Beta)** |
| Verified badge | ฿888 ครั้งเดียว | blue badge, ค้นหาเจอ |
| Premium ID | ~฿444–459/ปี | @yourbrand |

**ชุดที่แนะนำสำหรับ SME ที่จริงจัง:** Pro (฿1,780) + OA Chat Package (฿555) = **฿2,335/เดือน** ≈ ฿28,000/ปี
เทียบกับงบ TikTok 2–3 วัน — คุ้มที่สุดใน stack ทั้งหมด

---

## 2 · Third-party ที่นิยมในไทย

| ประเภท | ตัวอย่าง | จุดแข็ง | ข้อควรระวัง |
|---|---|---|---|
| CRM + chatbot | Chatcone, Amity, Mautic (self-host) | journey builder, shared inbox, RFM อัตโนมัติ | ค่าใช้จ่ายรายเดือน, webhook conflict |
| Automation | Make / Zapier / n8n | ต่อระบบเองได้ | ต้องมีคนดูแล |
| E-commerce | MyShop (native), Shopee/Lazada integration | ครบวงจร | ข้อมูลกระจายหลายระบบ |
| Analytics | Sheets + Looker Studio | ฟรี, ยืดหยุ่น | ต้องดูแลเอง |
| AI assistant | ChatGPT/Claude + API | เขียนข้อความ, สรุปแชท | ต้องมี guardrail + PDPA |

**เกณฑ์เลือก third-party**
1. รองรับภาษาไทยจริง (ไม่ใช่แค่แปล UI)
2. มี webhook/migration ออกได้ (อย่าล็อกข้อมูล)
3. ราคาต่อ active contact ไม่ใช่ต่อ message อย่างเดียว
4. มี DPA (สัญญาประมวลผลข้อมูล) ให้ลงนาม
5. ทดลอง 30 วันก่อนผูกสัญญาปี

---

## 3 · Build vs Buy

```
ถ้าใช้ < 3 use case ที่ native ทำไม่ได้  → BUY (หรือไม่ต้องซื้อ)
ถ้าใช้ 3–5 use case + ทีมมี dev      → BUY + ต่อ API
ถ้าใช้ > 5 use case + ข้อมูลเป็นสินทรัพย์หลัก → BUILD (หรือ hybrid)
```

**ต้นทุนที่คนลืม**
| รายการ | ตัวอย่าง |
|---|---|
| Implementation | ฿30,000–150,000 (chatbot custom) |
| ค่าออกแบบ rich menu / asset | ฿1,500–5,000 ต่อชุด |
| ค่าดูแลรายเดือน | 15–30% ของค่า implement |
| ค่าคนดูแลระบบ | 0.3–1 FTE |
| ค่า migration ออก | มักแพงกว่าตอนเข้า |

---

## 4 · Webhook Constraint — กับดักที่ทำให้ระบบพัง

**ข้อเท็จจริง:** LINE OA channel หนึ่งชี้ webhook ได้ **URL เดียว**
→ ถ้าติดตั้ง chatbot platform A แล้วภายหลังซื้อ B → ต้องเลือก หรือทำ proxy

**ทางแก้**
1. **เลือกเจ้าเดียว** (แนะนำสำหรับ SME)
2. ทำ **middleware proxy** (n8n/Make/Cloud Function) ที่รับ webhook แล้วกระจายต่อ → ยืดหยุ่นแต่ต้องมีคนดูแล
3. ใช้ **LIFF + Messaging API** เฉพาะจุดที่ต้อง custom แทนการเปลี่ยนแพลตฟอร์มทั้งระบบ

---

## 5 · Stack ตามระดับงบ

### ระดับ 1 — งบ < ฿5,000/เดือน
```
LINE OA Free/Basic + Reward Card + Sheets/Excel + Canva
ทำ: rich menu, greeting, auto-reply, broadcast 1–2/เดือน
```

### ระดับ 2 — งบ ฿5,000–20,000/เดือน
```
LINE OA Basic/Pro + MyCustomer CRM + OA Chat Package + Looker Studio
ทำ: segmentation, 3 flows, targeted broadcast, RFM ด้วยมือ
```

### ระดับ 3 — งบ ฿20,000–80,000/เดือน
```
Pro + CRM third-party + Make/n8n + LINE Ads + creative freelance
ทำ: journey builder, RFM อัตโนมัติ, A/B test, multi-channel
```

### ระดับ 4 — งบ > ฿80,000/เดือน
```
Pro + CRM enterprise + CDP + BI (Looker/PowerBI) + in-house dev
ทำ: predictive, next-best-action, attribution ขั้นสูง
```

---

## 6 · AI ใน Stack — ทำอะไรได้และไม่ได้

| งาน | AI ทำได้ | ต้องมีคนตรวจ |
|---|---|---|
| ร่างข้อความ broadcast | ✅ | ✅ (claim, โทน) |
| สรุปแชท / tag อัตโนมัติ | ✅ | ✅ (โดยเฉพาะข้อมูลสุขภาพ) |
| แนะนำสินค้า | ✅ | ✅ (ไม่ให้ตัดสิทธิ์ลูกค้า) |
| ตอบ FAQ | ✅ | ต้องมีทางออกไปหาคน |
| ปิดการขาย high-value | ❌ | ต้องเป็นคน |
| ตัดสินใจลด/หยุดส่งถึงลูกค้า | ❌ | ต้องเป็นคน + ตรวจ PDPA |

**Streamline ที่ได้ผลจริง (ROI ดี)**
1. AI ร่าง 5 ข้อความ broadcast จาก brief → คนเลือก/แก้
2. AI สรุปแชทลูกค้า VIP ก่อนโทร
3. AI จัดหมวดคำถามซ้ำ → ทำ auto-reply
4. AI ร่างรายงานรายสัปดาห์จาก export

---

## 7 · Checklist ก่อนเซ็นสัญญาเครื่องมือ

- [ ] ทดลองกับข้อมูลจริง ไม่ใช่ demo
- [ ] ส่งออกข้อมูลได้ (CSV + API)
- [ ] รองรับภาษาไทย + กัน spoofing
- [ ] มี DPA + ระบุที่เก็บข้อมูล (ใน/นอกไทย)
- [ ] ราคาชัด: ต่อ contact / ต่อ message / ต่อ seat
- [ ] ไม่มีเงื่อนไขผูก 24 เดือนโดยไม่มี exit
- [ ] migration plan ถ้าต้องย้ายออก
- [ ] ใครดูแลเมื่อมีปัญหา (SLA)
- [ ] ทำงานร่วมกับ LINE OA plan ที่ใช้อยู่ได้
- [ ] ไม่ชน webhook กับของเดิม

---

## กับดักของบทนี้

- ❌ ซื้อ CRM ก่อนมี tag standard
- ❌ ใช้ 2 chatbot platform พร้อมกัน
- ❌ จ่าย enterprise tool แต่ใช้ 20%
- ❌ ลืมค่าคนและค่าออกแบบในงบ
- ❌ ไม่ทดลองกับข้อมูลจริงก่อนเซ็นปี
- ❌ เก็บข้อมูลไว้ในเครื่องมือที่ export ไม่ได้

---

## แหล่งอ้างอิง

ดู [`SOURCES.md`](SOURCES.md) — กลุ่ม `line-pricing`, `tools-stack`, `line-crm`
