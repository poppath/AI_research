# Experiment design: เรียนรู้โดยไม่หลงผล

TH · 7 พ.ย. 2026 · ไม่พบ baseline ของบัญชีผู้ใช้; ตัวอย่างไม่ใช่ benchmark. Audience metrics เป็นของแต่ละ platform ไม่เทียบตรงโดยไม่ normalize นิยาม.

## เริ่มจากการตัดสินใจ
ระบุ hypothesis, population/placement, intervention, comparison, primary metric, guardrails, unit, window, minimum useful effect, budget cap, stopping rule และเจ้าของ **ก่อน** เผยแพร่. เช่น “intro ที่เริ่มด้วยปัญหาจะช่วย engagement มากกว่า intro ที่เริ่มด้วยสเปก” การเปลี่ยน hook พร้อมสินค้า/ความยาว/เวลาโพสต์ทำให้แยกเหตุไม่ได้. กำหนด capacity และ reporting cadence; ตัวเลขขั้นต่ำต้องคำนวณจาก baseline, effect, power, variance และแผนที่เหมาะกับการสุ่ม ไม่คิดตัวเลขตายตัว.

## ลำดับคุณภาพหลักฐาน
1. **Smoke test:** ตรวจลิงก์ disclosure และ event; ยังไม่วัดผลเชิงสาเหตุ.
2. **Exploratory:** เปรียบเทียบ posts ในช่วงเวลาใกล้กัน ใช้ทำ hypothesis ไม่เรียก A/B causal หากไม่มีการสุ่ม; control audience, เวลา, format, product และ distribution ไม่ได้.
3. **Randomized test เมื่อทำได้:** ใช้ native experiment หรือ randomize หน่วยที่ platform อนุญาต กำหนด outcome/window และไม่ปรับเป้าระหว่างทาง; ป้องกัน contamination. ไม่มีสิทธิ randomize หรือมี sample น้อย = รายงาน inconclusive, ไม่สรุปว่าไม่มีผล.
4. **Business impact:** content engagement ไม่เท่ากับ incremental approved commission; ทดลอง holdout ตามความเหมาะสมเมื่อวัดได้และมี data เพียงพอ. รายงาน contribution หลัง matured cohort และ costs แยกจากผล engagement.

YouTube Studio รองรับทดสอบ title/thumbnail ของวิดีโอที่ eligible โดยดู watch time; เอกสารระบุ Shorts ไม่รองรับฟีเจอร์นี้ ณ วันที่ตรวจ [S25]. Native test เป็นตัวเลือก ไม่การันตี eligibility, power หรือยอดขาย. ผลไม่พบ winner อาจเกิดจากข้อมูลไม่พอ [S25].

## อ่านผลอย่างซื่อสัตย์
ดู denominator, ช่วงเวลา, sample, วิธีสุ่ม, effect ขนาดจริง, uncertainty และความสามารถนำไปใช้. อย่าเลือก winner จากยอดวิวอย่างเดียว หรือยุติเมื่อบังเอิญขึ้นโดยไม่มีกฎหยุดล่วงหน้า. Retention dip อาจเป็นสัญญาณจุดที่คน skip/เลิกดู ส่วน spike อาจหมายถึงทั้งความชอบและความไม่เข้าใจ ต้องดูเนื้อหาและหลักฐานอื่นร่วม [S26]. ค่า p ไม่ใช่โอกาสที่สมมติฐานจริงหรือโอกาสที่ผลเกิดจาก randomness โดยตรง.

## ตัวอย่างแผนจำลอง
ประชากร: ผู้ชมวิดีโอ long-form ที่ eligible บน YouTube; ตัวแปร: thumbnail A/B ใช้ native tool ถ้ามี; primary: watch-time outcome ตามรายงาน native; guardrails: claim accuracy และ budget; วันเริ่ม/จบ/cap/owner ให้กรอกก่อนทดลอง. Outcome inconclusive = เก็บเป็นบทเรียน ไม่ประกาศว่าเท่ากัน. Affiliate clicks และ approved commissions ใช้วัดธุรกิจแยก โดยยอมรับ attribution และเวลา payout; ไม่มีข้อมูลพอไม่คำนวณ ROI ที่แน่นอน.

## Test card
ID / คำถาม / เหตุผล / ช่องทางและ eligibility / หน่วยและวิธีจัดกลุ่ม / A-B / metric และสูตร / cutoff, mature window / baseline และ minimum useful effect / sample feasibility / budget cap / safety stop / decision / limitations / owner.
