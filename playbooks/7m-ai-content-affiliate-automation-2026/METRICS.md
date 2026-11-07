# Metrics และการตีความ

| metric | นิยาม/ข้อควรระวัง |
|---|---|
| qualified click | คลิกที่รายงานโดย affiliate/platform; dedupe เท่าที่ทำได้ |
| order conversion | attributed orders / qualified clicks ใน cohort และ attribution window เดียวกัน; ไม่ใช่ผลเพิ่มเชิงเหตุและผล |
| approval rate | approved orders / eligible resolved orders; แยก pending ที่ยังไม่ถึงรอบ |
| realized commission | คอม approved แยก paid และ reversals; เทียบ statement ของโปรแกรม |
| contribution | approved commission หักต้นทุนที่เกี่ยวข้อง; ระบุค่าแรง, ads, AI, ไฟ และค่าเสื่อม/ภาษีที่ยังไม่รวม |
| compliance | จำนวน incidents แยก severity, time-to-resolution; เป้าหมายไม่มีการละเมิดที่ทราบ |

ข้อมูลไม่ครบให้รายงาน unknown ไม่แทนด้วยศูนย์; ระบุเวลา, เขตตลาด, cohort, currency, attribution window, source, return cut-off และ revision. ใช้ contribution เป็น primary KPI ส่วน compliance และ budget เป็น guardrails; กำหนดตัวเลข kill criterion จากงบและความเสี่ยงก่อนเริ่ม.
