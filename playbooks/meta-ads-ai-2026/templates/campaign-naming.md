# Campaign Naming Convention

> **Review 7 พ.ย. 2026:** เอกสารเดิมเป็น research snapshot มีตัวเลข/heuristic และข้ออ้างที่ยังต้องตรวจรายกรณี ไม่ใช่กฎสากลหรือ rate ปัจจุบัน; ก่อนใช้ให้ดู [ข้อจำกัดและรายการแก้ไข](../../../REPO-REVIEW-2026-11-07.md) และ `AGENTS.md` โดยเฉพาะก่อนตัดสินใจงบ กฎหมาย หรือ automation.

> จุดประสงค์: ให้ชื่อสื่อความหมาย, sort ได้, และ **AI query ได้** โดยไม่ต้องเดา
> ใช้ตัวพิมพ์ใหญ่ทั้งหมด, คั่นด้วย `_`, ห้ามเว้นวรรค, ห้ามอักขระพิเศษ (ยกเว้น `-`)

---

## 1. โครงสร้าง

```
{SEQ}_{FUNNEL}_{TYPE}_{MARKET}_{AUDIENCE}_{CREATIVE}_{YYYYMMDD}
```

| ส่วน | ค่า | ตัวอย่าง |
|---|---|---|
| SEQ | ลำดับ 2 หลัก | `01`, `02` |
| FUNNEL | `TOF` / `MOF` / `BOF` / `RET` / `TEST` | `MOF` |
| TYPE | `SALES` / `LEADS` / `TRAFFIC` / `ENGAGE` / `AWARE` / `APP` / `MSG` | `SALES` |
| MARKET | ISO-2 หรือกลุ่ม | `TH`, `TH-BKK`, `SEA` |
| AUDIENCE | ชื่อ audience แบบสั้น | `BROAD`, `LAL1P`, `INT3`, `WEB30D` |
| CREATIVE | concept/hook สั้น | `HOOKPRICE`, `UGCREVIEW`, `DEMO15S` |
| YYYYMMDD | วันที่เริ่ม | `20261106` |

### ตัวอย่าง

```
01_TOF_SALES_TH_BROAD_HOOKPRICE_20261106
02_MOF_LEADS_TH_INT3_UGCREVIEW_20261106
03_RET_SALES_TH_WEB30D_OFFER7D_20261110
04_TEST_SALES_TH_LAL1P_DEMO15S_20261112
```

**Ad set**
```
AS{NN}_{AUDIENCE}_{AGE}_{GEO}_{EXCLUSION}
AS01_BROAD_25PLUS_TH_EXBUYER180
AS02_LAL1P_25-44_BKK_EXLEAD90
```

**Ad**
```
AD{NN}_{FORMAT}_{HOOK}_{VERSION}
AD01_REELS9X16_PRICEHOOK_V1
AD02_FEED4X5_UGCPROOF_V2
```

---

## 2. โครงสร้าง UTM

```
utm_source   = facebook | instagram | threads        (ตาม placement หลัก)
utm_medium   = paid_social
utm_campaign = {campaign_name}                        (ตรงกับชื่อแคมเปญ 100%)
utm_content  = {ad_name}
utm_term     = {audience}
```

**ตัวอย่าง**
```
https://example.com/product?utm_source=facebook&utm_medium=paid_social
&utm_campaign=01_TOF_SALES_TH_BROAD_HOOKPRICE_20261106
&utm_content=AD01_REELS9X16_PRICEHOOK_V1
&utm_term=BROAD
```

> กติกา: UTM ต้อง **ตรงกับชื่อใน Ads Manager** เพื่อให้ join ข้อมูลได้อัตโนมัติ (ถ้าไม่ตรง AI จะจับคู่ผิด)

---

## 3. กติกาการเปลี่ยนชื่อ

| สถานการณ์ | ทำได้ | ห้าม |
|---|---|---|
| แก้ creative ใน ad เดิม | เปลี่ยน version ท้ายชื่อ (`_V2`) | เปลี่ยนทั้งชื่อ |
| ย้าย ad set | สร้างใหม่ + ใส่ `_MIG` | เปลี่ยนชื่อเดิม |
| ปิดแคมเปญ | ใส่ `_PAUSED` ต่อท้าย (ถ้าจำเป็น) | ลบ |
| ทดลองซ้ำ | ใช้ SEQ ใหม่ + `_R2` | ใช้ชื่อเดิม |

---

## 4. ตัวอย่างการอ่านชื่อด้วย AI

```
ให้ AI แยกฟิลด์จากชื่อนี้:
01_TOF_SALES_TH_BROAD_HOOKPRICE_20261106

ผลลัพธ์:
seq: 01
funnel: TOF
type: SALES
market: TH
audience: BROAD
creative: HOOKPRICE
start_date: 2026-11-06
```
