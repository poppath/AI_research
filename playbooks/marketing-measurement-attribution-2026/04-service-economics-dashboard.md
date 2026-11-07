# 04 · Dashboard และ unit economics ของบริการ

## KPI tree สำหรับสินค้า
Spend → visits → orders accepted → delivered orders → net revenue → CM2 → CM3; แยก SKU/channel, refund cohort และ COD; ใช้ definitions ใน [Unit Economics](../profit-unit-economics-2026/00-START-HERE.md). อย่านำ platform purchase รวมกันแทน unique order ledger

## KPI tree สำหรับบริการ
Spend → unique leads → qualified leads → appointments held → won → paid / delivered → contribution หลัง media. สำหรับ subscription ให้ติดตาม active cohort, churn, collections, onboarding และ capacity เพิ่ม; อย่าคิดยอดสัญญาทั้งปีเป็น cash วันนี้

| Metric | สูตร | เงื่อนไข |
|---|---|---|
| Cost per qualified lead | spend หาร unique qualified leads | matched cohort/window; เป็น observed ratio ไม่ใช่ incremental CAC |
| Lead-to-qualified | unique qualified / eligible unique leads | stage criteria/version และ mature horizon |
| Cost per won | spend หาร unique won customers หรือ won opportunities | บอกหน่วย; period/cohort alignment |
| Service contribution | paid/recognized revenue − incremental delivery labor − tools/contractor − payment/service fees − expected refunds | ไม่ใช่กำไรสุทธิ; ระบุ cost basis และช่วงเวลา |
| Capacity utilization | booked productive hours / available productive hours | กำหนด productive hours และ service capacity; อย่าสร้าง incentive ให้ขายเกินกำลัง |

### ตัวอย่างบริการสมมติ
100 eligible leads, 40 qualified, 10 won; spend ฿20,000 → cost/qualified = ฿500; cost/won = ฿2,000. แต่ละ won มีรายได้สุทธิ ฿5,000 และต้นทุนบริการแปรผัน ฿2,500 → CM ก่อน media ฿2,500; หลัง media จัดสรร ฿500 ต่อ won (ก่อน fixed costs/tax). ใช้ได้เมื่อ 100 leads และ spend เป็น cohort/attribution เดียวกัน และ 10 won mature แล้ว; หากยังไม่ mature ห้ามสรุปว่า rate คงที่

## Dashboard review
- รายวัน: event anomalies, spending cap, form/call availability และ service capacity
- รายสัปดาห์: source coverage, duplicate, cohort progression, open leads, revenue และ exceptions
- รายเดือน: reconciled sales vs ad/CRM, refund/returns, lag distributions, uncertainty และ decision log
- ตัดสินใจ: owner, KPI/guardrails, data freshness และ stop rule ต้องระบุ ก่อนขยายงบ
