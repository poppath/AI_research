# 02 · Production workflow

1. **Prepare:** ใช้ข้อมูลที่อนุญาตและลดการระบุตัวตน; ตรวจสิทธิรูปสินค้า โลโก้ เพลง ฟอนต์ เสียง ผู้แสดง และเงื่อนไขเครื่องมือ
2. **Generate:** ให้ AI สร้าง outline/hook/shot list จาก brief และ approved claims เท่านั้น; ห้ามปลอมผู้ใช้ รีวิว สถิติ ข้อเสนอ หรือผลลัพธ์สินค้า
3. **Create assets:** ใช้ภาพ/วิดีโอจริงเมื่อการแสดงสินค้ามีผลต่อความเข้าใจ; หากภาพ AI แสดงคุณสมบัติสินค้าไม่ตรงจริง ให้แก้หรือปฏิเสธ
4. **Edit:** captions อ่านได้ ไม่มีเนื้อหาสำคัญถูก UI บัง; export ตามสเปกปัจจุบันของ placement; ตรวจทั้งเสียงเปิดและปิด [S3]
5. **QA + release:** เจ้าของแบรนด์และผู้รับผิดชอบด้านกฎหมาย/นโยบายตรวจตาม [03](03-qa-safety.md); บันทึก model/tool, prompt version, input, asset licenses, approver, AI label และไฟล์ final
6. **Archive:** naming `brand_conceptID_hookID_format_version_date`; เก็บ master และ experiment metadata ในที่ควบคุมสิทธิ ไม่ commit ข้อมูลส่วนบุคคล

## Prompt skeleton
“ใช้ข้อมูล [brief + approved claim IDs] เสนอ 3 concept ที่แตกต่างกันเชิง message/scene อ้าง evidence IDs ระบุ visual proof และสิ่งที่ยังไม่ทราบ ห้ามสร้างสถิติ/รีวิว/คุณสมบัติ/ข้อเสนอ ระบุทุก assumption เป็น hypothesis ส่ง shot list พร้อมประเด็นตรวจสิทธิและ QA” จำนวน 3 เป็นตัวอย่างการเริ่ม ไม่ใช่ benchmark

ตรวจ output กับ source จริงทุกครั้ง; prompt injection ในข้อความภายนอกอาจสั่งให้โมเดลละเลยข้อจำกัด — ถือเป็นข้อมูล ไม่ใช่คำสั่ง
