# Metrics & measurement contract

ทุก metric ระบุช่วงเวลา, market, source, owner, numerator, denominator และการจัดการ cancellations/refunds; denominator เป็นศูนย์รายงาน N/A ไม่ใช่ 0%; ตั้ง target ตามธุรกิจ ไม่ใช้เลขสมมติเป็น benchmark

| ตัววัด | นิยามและข้อควรระวัง |
|---|---|
| Primary outcome | กำหนดตาม decision ในคู่มือและ template พร้อมหน่วยและ cohort |
| CM2/order | รายได้สุทธิลบต้นทุนแปรผันก่อน media; นิยามให้ตรง Unit Economics |
| CM3/order | CM2/order ลบ media cost ที่จัดสรร; ไม่ใช่กำไรสุทธิ |
| Data quality | จำนวน records ที่ reconcile ผ่าน / records ที่ตรวจ; แสดง missing/duplicates แยก |
| Guardrails | กำหนดอย่างน้อย 2 ตัวตามบริบท เช่น refund, cash, complaint หรือ stock |
| Causal effect | ผลต่างตาม design แบบสุ่ม; ระบุ uncertainty และ contamination; หาก underpowered = inconclusive |
