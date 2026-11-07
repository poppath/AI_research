# Numeric triage · index เพื่อทบทวน ไม่ใช่ fact check

`numeric-candidates.json` สร้างจาก `scripts/build_numeric_candidates.py`: ตรวจ Markdown ทุกไฟล์ภายใต้ playbooks หา line ที่อาจมีเงิน เปอร์เซ็นต์ ระยะเวลา หรือเกณฑ์. Snapshot นี้มี 1,677 lines ใน 87 files; ทุก candidate เป็น `candidate_unreviewed` **รวมทั้งตัวอย่างสมมติ วันที่ ข้อห้าม และบรรทัดที่อาจเคยตรวจแล้ว**. ไฟล์ระบุ path, line และ SHA-256 เพื่อเปิดแหล่งเดิม.

Regex พลาดตัวเลข/ข้ออ้างได้มาก เช่น ตัวเลขเขียนเป็นคำ ตารางที่ไม่มี unit, การอ้างเชิงคุณภาพ, JSON/YAML, ข้อกำหนดที่อ้างเป็นภาษาอื่น หรือความผิดพลาดด้านสูตรที่ไม่มีตัวเลข. จำนวนนี้จึงไม่ใช่จำนวน claims ทั้งหมด และ status ไม่บอกว่าเป็นจริงหรือเท็จ. การ review ต้องเปิดบริบทรอบบรรทัด + แหล่งตรง แยก scenario, benchmark, date, unit, market, effective date และ account scope; ถ้าไม่พอให้คง unknown. ใช้คู่ [source verification](SOURCE-VERIFICATION.md) และ [audit](../REPO-REVIEW-2026-11-07.md).

รีเฟรชด้วย `python scripts/build_numeric_candidates.py` และตรวจ drift ด้วย `--check`; การ regenerate ไม่ได้ยืนยันเนื้อหา. ห้าม LLM นำ candidate ไปใช้เป็น benchmark โดยไม่ตรวจ.
