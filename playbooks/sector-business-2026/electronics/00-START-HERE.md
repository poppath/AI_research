# เทคโนโลยีและอุปกรณ์อิเล็กทรอนิกส์ · Sector Playbook

**ขอบเขต:** โทรศัพท์ คอมพิวเตอร์ แกดเจ็ตและอุปกรณ์ต่อพ่วง. **ตลาด:** TH; research 7 พ.ย. 2026; starter guide ไม่ใช่คำแนะนำกฎหมายหรือผลทดลอง. อ่าน [กติกากลาง](../COMMON.md), [แหล่ง](../SOURCES.md), [rules](playbook.json), [benchmarks](benchmarks.json). AI: ห้ามเดา KPI, สิทธิ, claims หรือข้อมูลธุรกิจ; ขอข้อมูลที่ขาดก่อน launch.

## 1. Baseline / Market
- กลุ่มและ pain: ผู้ซื้อเปรียบเทียบ compatibility warranty และประสิทธิภาพ. ระบุ persona จากหลักฐานจริง ไม่สมมติว่าเป็นตลาดทั้งหมด.
- Offer: model compatibility, warranty และวิธีทดสอบ. กรอกชื่อผู้ขาย/ผู้ให้บริการ, พื้นที่, channel, งบ, เวลา, pricing, eligibility, target และ baseline จากบัญชี; **ไม่มีข้อมูล — ต้องวัดเอง**.
- Evidence ก่อนสร้าง: manufacturer specs, device models, documented test conditions. ตรวจ source/date และ rights; ข้อมูลไม่ชัด = HOLD.

## 2. Money และ delivery
- วิธีคิดเฉพาะ: margin หลัง warranty, defective returns, platform fees และ freight. รายได้ affiliate นับ approved commission ไม่ใช่ GMV; merchant และบริการใช้ฐานรายได้ต่างกัน ดู [COMMON](../COMMON.md).
- บันทึกต้นทุนจริงตาม order/job/cohort รวมค่าแรง แพลตฟอร์ม โฆษณา ผลคืน และค่าใช้จ่ายเฉพาะธุรกิจ; แยก cash, ภาษีและค่าเสื่อม. ห้ามใช้ตัวเลขค่าคอม/ROAS จาก sector อื่นโดยไม่ตรวจ.
- Operational failure: compatibility ผิด, warranty ไม่ครอบคลุม, benchmark ลวง. ตั้ง owner และ capacity ก่อนรับ demand.

## 3. Man / Material / Machine
- Owner รับผิดชอบ product/service, claims/rights, creative, publishing, operations และเงิน; คนเดียวทำหลายหน้าที่ได้ แต่ต้องระบุผู้อนุมัติจริง.
- คลัง material: manufacturer specs, device models, documented test conditions; เก็บแหล่ง ภาพ/เสียง license, เวอร์ชัน, วันที่หมดอายุ และการอนุมัติ; ข้อมูลส่วนบุคคลเท่าที่จำเป็น [S13].
- AI: AI สรุป spec จากแหล่ง; ห้ามสร้าง benchmark ปลอม. งาน publish ใช้เฉพาะ flow ที่ platform อนุญาต; แยกสิทธิ agent และเก็บ audit, cap, stop switch; ไม่อ้าง automation 24h ได้ทุกแพลตฟอร์ม.

## 4. Method · ขั้นตอนทดลอง
1. ตรวจ suitability และ eligibility ของโปรแกรม/ผลิตภัณฑ์/บริการ รวม disclaimer/affiliate disclosure และสิทธิ assets; ตรวจ มอก./กสทช. และใบอนุญาตตามชนิดสินค้า.
2. ตั้ง hypothesis สำหรับกลุ่มจริง เลือก offer ที่ deliver ได้; เลือกช่องทางและ budget cap จาก capacity ไม่ซื้อ traffic ถ้า fulfillment หรือสิทธิไม่พร้อม.
3. ทำ original content: ทดสอบการใช้งานจริงพร้อมวิธีและข้อจำกัด. AI ทำ draft; คนตรวจ source, claim, ราคา/สถานะ, disclosure และ preview ก่อนเผยแพร่ [S1,S14].
4. ส่งผู้สนใจผ่านช่องทางที่อนุญาต พร้อมข้อจำกัดและวิธีติดต่อ; ห้ามสร้างรีวิว/ประสบการณ์เท็จ. บันทึก source, campaign, content version และ conversion แบบ aggregate เมื่อเข้าถึงได้.
5. รายงาน cohort, เงินจริงและต้นทุน; เปรียบเทียบกับเกณฑ์ที่กำหนดไว้ก่อน pilot; รายงาน pending และข้อมูลที่ไม่รู้แยก. หลีกเลี่ยงสรุป causal จากยอด attribution.

## 5. Measurement / gates
- Primary และ guardrails: contribution ต่อ order; guardrail DOA และ compatibility returns. ระบุสูตร denominator, window, owner และ threshold ตามธุรกิจจริงก่อนเริ่ม; ไม่มี benchmark ในเอกสารนี้.
- **Stop:** หยุดเมื่อ compatibility หรือ safety certification ตรวจไม่ได้; หยุดทันทีเมื่อ token รั่ว, claim ไม่มีหลักฐาน, ผิด ToS, งบเกิน cap หรือ safety/privacy incident. บันทึกปัญหา แก้ และให้ owner อนุมัติก่อนเริ่มใหม่.
- **Test card:** สมมติฐาน / กลุ่ม / concept / channel / KPI / window / cap / risk / stop threshold / owner / decision. การเทียบโพสต์ไม่สุ่มเป็น exploratory ไม่ใช่ข้อสรุปเหตุและผล.

## 6. คำถามและช่องว่างก่อน launch
สินค้าหรือบริการจริงคืออะไร? ใบอนุญาตหรือข้อบังคับใดใช้? ใครอนุมัติ claim? รายได้และต้นทุนต่อ unit เท่าใด? ลูกค้าจะได้รับสินค้าหรือบริการอย่างไร? มีข้อมูล measurement/returns หรือยัง? หากตอบไม่ได้ให้ HOLD และตรวจ regulator, program, platform และผู้เชี่ยวชาญตามบริบท; เอกสารรวมนี้ไม่ได้ยืนยันกฎทุก subsector.
