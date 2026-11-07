# 02 · Google Ads สำหรับสินค้า: Search → Merchant Center → economics

## Business inputs
SKU, net sale price, fee base, stock/fulfilment, refund, CM2/order, allowed claims, budget cap และข้อจำกัด geography. คำค้น brand/non-brand และ product category ให้ map ไปยัง landing ที่ตรงเจตนา; brand search ได้อิทธิพลจากกิจกรรมอื่น จึงไม่ถือทุก conversion เป็นผลเพิ่มของ search

## Product feed readiness
1. Link Merchant Center, Google Ads และ source of product data ที่มีสิทธิใช้งาน; ตรวจ eligibility ประเทศ/สินค้าในบัญชี
2. ตรวจ ID/variant, title, image, price/currency, availability, shipping, landing และ structured data; ต้องตรง feed และหน้าเว็บ/checkout ตามข้อกำหนด [S3]
3. มี owner สำหรับ feed refresh, diagnostics/disapproval, promotion start/end และ stock; ไม่โฆษณาสินค้าหมดด้วยการแสดงว่ายังมี
4. Purchase และ refund มี transaction ID ไม่ใช่ PII; QA กับ OMS และ settlement; duplicate ใช้การตรวจจริง ไม่สมมติว่า tag ทำงาน

## Campaign choices
- Search: เก็บ intent ที่หน้า landing ตอบได้; ตรวจ search terms, relevance, negatives ที่ไม่ตัดคนซื้อสำคัญ
- Shopping หรือ Performance Max: เมื่อ product feed ถูกต้องและ account รองรับ; PMax ครอบคลุมหลาย surfaces ไม่ใช่ channel เดียว [S1]
- แยก campaign ตาม objective/สินค้าที่คุม margin หรือ supply ต่างกันเมื่อมีเหตุผลและข้อมูลเพียงพอ ไม่กำหนดจำนวนตายตัว

## Economics ตัวอย่างสมมติ
ราคา net ฿1,000; CM2 หลัง costs ก่อน media ฿300 → break-even ad cost/order ฿300 และ break-even revenue/ad spend ≈ 3.33× หาก revenue และ CM2 ใช้ฐานเดียวกัน ไม่มี fixed costs/return นอกสมมติฐาน; target จริงต้องเผื่อความเสี่ยงและกำไร. Platform ROAS ไม่ใช่ incremental ROAS

## QA และ stop
ตรวจ primary goals, duplicate conversions, cap, feed/landing mismatch, sold-out และ refund/lag; หยุด SKU ที่ข้อมูลเท็จหรือ stock/cap ผิดก่อนแก้. ห้าม scale จาก click/ROAS อย่างเดียว
