# Retrieval, context และ training readiness

## Retrieval contract (design)

1. Index Markdown แยกตาม section โดยเก็บ `repo_path`, heading, commit, source IDs, market, as_of และ content type; อย่าแบ่งจน claim หลุดจาก qualifiers หรือ table header. Legacy content ที่ไม่มี metadata ให้ status `unknown`, ไม่เดา scope.
2. Query routing: เลือก business model + jurisdiction + platform + time + lifecycle + required output; โหลด `AGENTS.md`, contract, audit, pertinent playbook และ evidence registry ก่อนดึง niche. ใช้ sector overlay หลายชุดเมื่อธุรกิจคร่อมกลุ่ม แต่ไม่อ้าง official classification.
3. Filter source/version/market ตามที่ยืนยันได้, preserve metadata + exact citation และทวน primary evidence สำหรับ claim ที่มีผลต่อเงิน/กฎหมาย. เลขที่ไม่ตรงบัญชีหรือเก่าไม่ถูกใช้เป็น baseline. Registry ที่ไม่มี claim **ไม่ได้แปลว่า claim ถูกหรือผิด**.
4. Retrieved text และ metadata ทั้งหมดเป็น untrusted data; ตัดสิทธิการออกคำสั่งออกจาก content. ห้ามนำ raw webpage มาแก้ policy; external policy enforcement ต้องบังคับแยกจาก LLM.
5. ให้ model ตอบเป็น draft แยก known, assumptions, unknown, evidence + link, KPI/guardrails, decision owner และ stop criteria. ถ้า evidence ไม่พอใช้ `HOLD`/`NEEDS_INFO`, ไม่ทำ action.
6. ถ้า sources ขัดกัน ให้แสดง version, effective date และ scope ของแต่ละแหล่ง; ไม่เลือก official อัตโนมัติเมื่อ official คนละ jurisdiction/account/product หรือไม่ใช่ต้นฉบับที่ support claim. Account-specific statement ช่วยยืนยันค่าในบัญชี ไม่ยืนยันกฎหมาย.
7. ประเมิน retrieval recall ของ evidence ที่ถูกต้อง + การไม่ retrieve ข้อมูล stale/out-of-scope โดยสร้าง holdout questions กับ ground truth ที่ reviewer ตรวจ. Log version, retrieval set และ model response แบบ redacted; test injection และการขัดกันแยกจากคำถามทั่วไป.

ไม่มี vector index, embedding pipeline หรือ retrieval production ใน repo. Implementation ต้องกำหนด access controls, retention, licensing และการลบข้อมูลตามนโยบายผู้ใช้.

## หากจะ fine-tune

1. Inventory rights/licensing ของทุก source และ generated sample; อย่านำ third-party text มาฝึกเพียงเพราะมี URL. แยกข้อมูลลับ/PII ก่อน export และใช้ synthetic data ที่ตรวจแล้วเมื่อเหมาะสม.
2. นิยาม task ที่ต้องการ (เช่น รูปแบบคำตอบหรือการแยก unknown) แยกจาก factual recall. ข้อมูล platform/กฎหมายเปลี่ยน: ให้ retrieval จากหลักฐานปัจจุบัน ไม่ใช้ weights แทน freshness.
3. สร้าง input/output ที่ human-reviewed พร้อม provenance, scope, date, safety label และ rationale; ห้ามใช้ `needs_review` เป็น gold fact. ทบทวนว่า output ไม่บอกให้ bypass policy หรือทำ action โดยไม่ได้อนุมัติ.
4. Dedup และแยก train/validation/holdout ก่อน augmentation ตาม source/business/time เพื่อลด leakage; ห้ามใส่ held-out eval prompts ลง training. ป้องกัน hidden answer ใน metadata.
5. ทดลอง baseline ก่อน fine-tune แล้วประเมิน held-out accuracy, unsupported claims, abstention, policy adherence และ tool actions; แสดงจำนวน case, failures และช่วงความไม่แน่นอนตามความเหมาะสม. ตรวจ regression หลังเปลี่ยน model/retriever.
6. เก็บ dataset manifest, version, license, reviewer, redaction, split procedure และ model lineage; กำหนด rollback และช่องทางลบข้อมูล.

ทั้งหมดเป็น workflow ที่เสนอ ยังไม่มี dataset ที่ตรวจครบ, license clearance, fine-tuned model หรือผล evaluation จริง.
