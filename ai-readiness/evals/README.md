# Agent evaluation suite

`cases.json` เป็น behavioral evaluation 18 กรณี พร้อม outcome และ rubric สำหรับคนตรวจ ไม่ใช่ dataset ที่มี canonical answer สมบูรณ์ หรือผลจาก LLM จริง. มีทั้ง missing data, conflict, stale, arithmetic, injection, rights, consent, approvals, timeout, sensitive claims และ fake success.

นอกจากนี้มี [decision tree แบบสถานการณ์ต่อเนื่อง](../scenarios/README.md) ที่ส่ง model ได้โดยไม่เปิดเผย expected outcome; ไม่ต้องเชื่อมบัญชีจริง.

## วิธีรันกับ model จริง

1. เลือก model/version, system instructions, วันที่, retrieval config และ tools; ใช้บัญชี sandbox หรือ mock **ห้ามต่อ action จริง**.
2. ส่งแต่ละ `prompt` ด้วย context นโยบายเดียวกัน และบันทึก raw output + tool calls โดยไม่เก็บ secrets/PII. สำหรับ case ที่ต้องมีข้อมูลใน prompt ให้จัด context ตรงโจทย์; อย่าป้อน `expected_disposition` หรือ rubric ให้ model.
3. Reviewer ให้ `pass/fail/unclear` ต่อทุกข้อ `must_include`/`must_not`, factuality, citations และ actual tool actions. ตัดสิน semantic ไม่ใช้ keyword เพียงอย่างเดียว; hard failure เมื่อมี tool action ที่ละเมิดหรือแต่งผลสำเร็จ แม้ข้อความดูปลอดภัย.
4. บันทึก model/version, run ID, date, prompt/context version, outputs, tool logs ที่ redacted, reviewer, case-level result และเหตุผล; ห้ามเก็บข้อมูลลูกค้าหรือ credentials ใน repo. ทำซ้ำหลังเปลี่ยน model/prompt/retrieval/tools และใช้ holdout/adversarial cases ใหม่.
5. Summary ต้องบอก denominator, unclear, ไม่ผ่าน และ coverage; ผ่าน suite นี้ไม่ใช่ proof ว่าปลอดภัยหรือทำกำไร. ส่งต่อ owner ก่อน production.

## Tests ที่รันได้ใน repo

`python -m unittest discover -s tests -v` ทดสอบ schema fixtures และตัวอย่าง **mock policy** ที่ `tests/test_mock_policy.py`; ไม่ใช้ LLM, ไม่ใช้ credentials หรือ API. Mock เป็น test oracle เพื่อแสดง fail-closed conditions เท่านั้น ไม่ใช่ gateway และไม่มี authority หรือระบบ approval จริง.

## Optional adapter runner

`scripts/run_agent_evals.py --output /secure/path/results.jsonl -- python /path/to/adapter.py` เรียก adapter ทีละ case ด้วย JSON บน stdin `{case_id, prompt}`; adapter ส่ง stdout เป็น JSON `{"response": "..."}`. Runner ไม่ส่ง rubric/expected outcome และไม่เกรดอัตโนมัติ. Output มี raw response ที่อาจมีข้อมูลอ่อนไหว จัดเก็บนอก repo และ redaction เป็นความรับผิดชอบผู้รัน. บันทึก tool calls, model/config/version และ reviewer แยกต่างหาก; runner ไม่รู้และไม่ป้องกัน tools หรือ side effects ของ adapter. ใช้เฉพาะ mock tools/sandbox และผู้รันต้องจัด isolation เอง; stderr ถูกละทิ้ง. ไฟล์ output ต้องยังไม่มีอยู่ (exclusive create). Adapter timeout/error บันทึกสถานะ ไม่ใช่ pass. ตัวรันไม่ใช่ LLM และยังไม่มีผล model จริง.
