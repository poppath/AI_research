# สถานะการปิด AI-readiness gaps · 7 พ.ย. 2026

| Gap | ทำแล้วใน repo | ยังไม่เสร็จ / ต้องทำต่อ |
|---|---|---|
| Evidence | Claim ledger เริ่มต้น; ทวน source-level 4 claims, log และ numeric triage 1,677 candidate lines (ไม่ใช่ expert/account verification) | regex มี false positives/negatives และยังไม่ extract/verify ทุก claim, ยังไม่มี independent claim-by-claim verification และระบบ refresh |
| Machine contract | Draft 2020-12 schemas, fixtures, validator/CI; catalog read-only ครบ rules arrays 35 documents (279 entries) | Legacy JSON/YAML ยังไม่ migrated เป็น reviewed executable rules หรือ verified; schema ไม่ตรวจเนื้อหาจริง |
| Agent authority | operating contract และ mock deterministic policy tests | ไม่ใช่ enforcement gateway, IAM, consent หรือ audit ที่ deploy จริง; ต้องบังคับที่ tool/backend |
| Evaluation | adversarial/gap scenarios และ human rubric; test mock policy; template สำหรับผลจาก model จริง | ยังไม่ได้รันกับ LLM, ไม่ใช่ score หรือ benchmark; ต้องทดสอบ model/provider/retrieval/tool จริงและ review โดยคน |
| Coverage | มี taxonomy/source/gate เดิม; ติดป้ายขอบเขต | ยังไม่ได้ทำครบ GICS 74/163, niche SOP และ verified rates ราย sector |
| Retrieval | Offline lexical prototype คืน path/lines/hash และสถานะ unknown | ไม่ใช่ RAG production, ไม่มี model, account filters หรือ security boundary; ต้อง review แหล่ง |
| Pilot/data | pilot card มี baseline, stop/approval/reconciliation | ไม่มี account, approval, financial data หรือระบบจริง; ยังไม่มี pilot results |
| Fine-tuning | มี retrieval/fine-tune readiness guide และข้อจำกัด rights | ยังไม่มี training data licenses, dedup, PII scrubbing, train/test split หรือ model-evaluation; ไม่พร้อมฝึก |

จุดเสี่ยง legacy ตาม [audit](../REPO-REVIEW-2026-11-07.md) ยังมีผล. จำนวน records หรือ test cases ที่เพิ่มไม่เท่ากับความครอบคลุมของทั้ง repo. จัด priority ต่อ: claim verification (fees/math/health/finance/platform) → rule migration → evaluation กับ model จริง → pilot ที่ได้รับอนุมัติ → niche expansion.
