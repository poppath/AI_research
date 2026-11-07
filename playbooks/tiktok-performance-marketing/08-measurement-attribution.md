# 08 · Measurement & Attribution

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> **TL;DR** — platform-reported ROAS บน TikTok **over-credit 30–60%**. Pixel อย่างเดียวจับ conversion ได้ ~65%; Pixel + Events API ได้ ~95%. ถ้าคุณตัดสินใจงบจากตัวเลขใน Ads Manager คุณกำลัง optimise ให้ TikTok ชนะ ไม่ใช่ให้ธุรกิจชนะ

---

## 1. โครงสร้าง 5 ชั้นของ measurement stack

| ชั้น | เครื่องมือ | ตัดสินใจอะไร | ใส่เมื่อไหร่ |
|---|---|---|---|
| 1 | **TikTok Events API (+Pixel)** | ข้อมูล optimization ทั้งหมด | **ทันที — ไม่มีข้อยกเว้น** |
| 2 | **Multi-touch attribution** (Triple Whale / Northbeam / Cometly) | จัดสรรงบระหว่าง channel | งบ ≥ ~$50k/เดือน |
| 3 | **Post-purchase survey** (KnoCommerce / Enquire) | ความจริงจากปากลูกค้า | AOV สูง หรือ subscription |
| 4 | **MMM** (Meridian / Recast) | contribution ระยะยาว | งบ TikTok > ~$100k/เดือน |
| 5 | **Geo incrementality test** | lift ที่แท้จริง | งบ > ~$500k/เดือน, ทำ 2 ครั้ง/ไตรมาส |

---

## 2. ชั้น 1: Pixel + Events API — ทำให้ถูกตั้งแต่ต้น

### 2.1 ทำไมต้องสองชั้น
| Metric | Pixel only | Pixel + Events API |
|---|---|---|
| Conversion capture | ~65% | ~95% |
| EMQ score ceiling | ~6.5 | 8.0+ |
| Attributed conversions (index) | 100 | 120–130 |
| Events ที่ถูก browser block | ~35% | เกือบ 0 |

> **EMQ (Event Match Quality)** ต่ำกว่า 5.0 → **ใช้ value-based bidding ไม่ได้**. นี่คือเหตุผลว่าทำไมบางบัญชีตั้ง Min ROAS แล้วระบบไม่ทำงาน

### 2.2 Checklist การติดตั้ง
- [ ] Pixel ติดทุกหน้า + Purchase/InitiateCheckout/AddToCart/ViewContent/Lead ครบ
- [ ] Events API ส่งจาก server (Shopify → ใช้ Elevar/Littledata หรือ native integration)
- [ ] **dedup ด้วย `event_id` ร่วมกัน** (ถ้าไม่ dedup → นับซ้ำ 2 เท่า, ROAS เพี้ยน)
- [ ] ส่ง identifier ครบ: hashed email, phone, external_id, ttclid, `_ttp`
- [ ] ส่ง `content_id`, `value`, `currency` ครบทุก event
- [ ] เก็บ `ttclid` ก่อน checkout (จำเป็นสำหรับ server-side attribution)
- [ ] ตรวจ EMQ ≥8.0 ใน Events Manager
- [ ] ทดสอบด้วย Test Events + ซื้อจริง 1 ครั้ง ก่อนยิงงบ

### 2.3 Attribution window
| Window | ค่า default | ตัวเลือก click | ตัวเลือก view |
|---|---|---|---|
| TikTok | **7-day click / 1-day view** | 1, 7, 14, 28 วัน | off, 1, 7 วัน |

- **ใช้ default ในการ optimize** (ให้ algorithm ทำงานตามที่ออกแบบ)
- **audit ด้วย 28-day window เดือนละครั้ง** เพื่อดูว่าอะไรถูก under-credit (กู้คืนได้ 63–79% ของ conversion ที่ 7 วันมองไม่เห็น)
- **ห้ามเปลี่ยน window แล้วเทียบตัวเลขข้ามเวลา** — ตัวเลขทั้งหมดเปลี่ยน

---

## 3. ตัวเลขที่ต้องรายงาน (และตัวที่ไม่ควร)

| ✅ รายงาน | ❌ อย่ารายงานเดี่ยว |
|---|---|
| Blended ROAS (revenue รวม / spend รวม) | Platform ROAS |
| MER (marketing efficiency ratio) | ROAS ของ campaign เดียว |
| New-customer CPA | CPA รวม (ปนลูกค้าเก่า) |
| Contribution margin after ads | GMV |
| Incremental lift (geo test) | Conversion ที่ platform อ้าง |
| Repeat purchase rate 60d | ยอดขายวันแรก |

### สูตรที่ต้องใช้
```
Blended ROAS     = Total revenue ÷ (paid spend + creator/affiliate spend + tool cost)
MER              = Total revenue ÷ Total marketing spend
New-customer CPA = paid spend ÷ new customers acquired
CM after ads     = revenue − COGS − fees − commission − shipping − returns − ad spend
Payback (days)   = CAC ÷ (daily gross profit per customer)
```

> **กฎ:** ถ้า blended ROAS ดีแต่ CM ติดลบ → คุณกำลัง scale การขาดทุนอย่างมีประสิทธิภาพ

---

## 4. Incrementality — วิธีเดียวที่ตอบว่า "TikTok ทำให้เกิดยอดจริงไหม"

### 4.1 Geo holdout test (ถูกที่สุด, ทำได้เอง)
```
1. เลือก 2 กลุ่มภูมิภาคที่คล้ายกัน (ยอดขายต่อหัวใกล้กัน)
2. กลุ่ม A: ยิง TikTok ปกติ · กลุ่ม B: ปิด TikTok 100%
3. รัน 3-4 สัปดาห์ (อย่างน้อย 2 รอบการซื้อ)
4. Incremental lift = (ยอด A − ยอด B) ÷ ยอด B  (หลังหักแนวโน้ม)
5. iROAS = revenue ที่เพิ่ม ÷ ad spend
```
**ข้อควรระวัง:** อย่าเลือกจังหวัดที่ต่างกันมากเรื่องรายได้; ต้องมี baseline 2–4 สัปดาห์ก่อนเริ่ม; ระวัง spillover ระหว่างภูมิภาค (คนย้ายถิ่น, ส่งของข้ามจังหวัด)

### 4.2 อ่านผลอย่างไร
| ผลลัพธ์ | แปลว่า | ทำอะไร |
|---|---|---|
| iROAS > platform ROAS | TikTok under-credited | เพิ่มงบ |
| iROAS ≈ 60-80% ของ platform ROAS | ปกติ (นี่คือค่าเฉลี่ยของอุตสาหกรรม) | คงเดิม, ใช้ platform ROAS หารด้วยตัวคูณนี้ในการวางแผน |
| iROAS < 50% ของ platform ROAS | TikTok over-credited หนัก | ลดงบ, ตรวจ organic cannibalization |
| iROAS ≈ 0 | ไม่ incremental | ย้ายงบ (แต่มักเกิดจาก test ออกแบบผิด) |

---

## 5. ปัญหาเฉพาะของ TikTok ที่ต้องรู้

### 5.1 GMV Max attribution = ทั้ง Shop
GMV Max นับ **ทุกออร์เดอร์ของสินค้าที่อยู่ใน campaign** รวมออร์แกนิกและ affiliate → ROI ที่เห็นจะสูงกว่าความจริงเชิง incremental เสมอ
**แก้:** วัดด้วย (ก) Shop GMV เทียบช่วงก่อนเปิด campaign (ข) spillover report (ค) geo/time holdout

### 5.2 Shop vs เว็บ ชนกัน
ถ้าขายทั้งสองที่ด้วยสินค้าเดียวกัน:
- แยก measurement ตาม source ใน Seller Center
- join ข้อมูลด้วย `order_id` ใน warehouse
- ดู SKU × สัปดาห์ เพื่อหา cannibalization หรือ halo

### 5.3 iOS / ATT / ad blocker
- Events API คือคำตอบหลัก
- Advanced Matching (hashed email/phone)
- อย่าใช้ iOS conversion จำนวนน้อยไปตัดสินใจปิด campaign

### 5.4 ตัวเลขไม่ตรงกันระหว่างระบบ
คาดว่าจะต่างกัน **10–30%** ระหว่าง TikTok กับ MMP/GA4 — เป็นเรื่องปกติของ methodology ที่ต่างกัน
**แก้:** กำหนด **single source of truth** ตั้งแต่แรก (แนะนำ: warehouse/BI ของคุณเอง) แล้วใช้ platform report เพื่อ "optimize" เท่านั้น

---

## 6. Dashboard ขั้นต่ำที่ต้องมี (ทำใน Sheets/Looker ก็พอ)

**หน้า 1 · Daily pulse**
spend · revenue · blended ROAS · orders · CPA · new customers · CM after ads

**หน้า 2 · Creative**
creative ID · hook ID · hook rate · completion · CTR · CPA · spend · ROAS floor pass/fail

**หน้า 3 · Funnel**
impressions → 3s views → clicks → PDP views → ATC → IC → purchase (เทียบกับ benchmark)

**หน้า 4 · Channel**
TikTok paid / TikTok affiliate / LIVE / Shop organic / อื่น ๆ · spend · revenue · blended contribution

**หน้า 5 · Quality**
return rate · refund rate · repeat purchase 60d · AOV · coupon cost · effective take rate

---

## 7. รอบการตรวจ (cadence)

| ความถี่ | ทำอะไร |
|---|---|
| ทุกวัน (5 นาที) | spend pacing, มี event ตกไหม, มี campaign ไม่ spend ไหม — **ห้ามตัดสินใจจากวันเดียว** |
| ทุกสัปดาห์ | creative-level report, kill/scale ตามเกณฑ์, อัปเดต CM |
| ทุกเดือน | blended ROAS, new-customer CPA, 28-day audit, reconcile กับ GA4/MMP |
| ทุกไตรมาส | MMM refresh, attribution window reassessment, EMQ/CAPI audit, incrementality test |

---

## 8. Anti-patterns ด้าน measurement

| ❌ | ผล |
|---|---|
| ใช้ platform ROAS ตัดสินใจงบ | over-invest เพราะ over-credit |
| ไม่ dedup `event_id` | นับ conversion ซ้ำ, ROAS สูงปลอม |
| ดู CPA รวมโดยไม่แยก new vs returning | ได้ลูกค้าเก่ามาแทนลูกค้าใหม่ |
| วัด GMV เป็น KPI เดียว | scale การขาดทุน |
| เปลี่ยน attribution window แล้วเทียบกับเดือนก่อน | ข้อสรุปผิดทั้งหมด |
| ไม่มี single source of truth | ทุกทีมเถียงกันเรื่องตัวเลข |
| ไม่เคยทำ incrementality test | ไม่มีทางรู้ว่า paid สร้างยอดหรือแค่ไปเก็บยอดที่มีอยู่ |

---

## อ้างอิงบทนี้
กลุ่ม `measurement` ใน [`SOURCES.md`](SOURCES.md)
