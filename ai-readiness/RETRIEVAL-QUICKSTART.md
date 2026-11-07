# Offline retrieval prototype · ใช้ได้โดยไม่เรียก API

```
python scripts/retrieve_context.py 'ส่วนลด margin' --limit 5
```

ค้นเฉพาะ Markdown ภายใต้ `playbooks/` แบบ lexical word/Thai bigram; คืน JSON ที่มี path, heading, line range, SHA-256, lexical score, excerpt และ `evidence_status = unknown_or_legacy_unverified` เสมอ. อ่าน policy ที่ระบุใน `required_context` ก่อนส่งผลให้ LLM. คำสั่งนี้ไม่โหลด model, ไม่ส่ง network และไม่แก้ไฟล์.

คะแนนเป็นความคล้ายข้อความแบบง่าย ไม่ใช่ความเชื่อมั่นหรือการพิสูจน์ claim; ภาษาที่ไม่มี word segmentation อาจ retrieve ผิด/พลาด. Excerpt ถูกตัดที่ 5,000 อักขระเมื่อยาวเกิน (`truncated=true`) จึงต้องอ่าน section เต็มรวม qualifier และ source ก่อนตัดสินใจ. ไม่ได้ filter freshness, account, jurisdiction หรือ licensing อัตโนมัติ; review เอง. เนื้อหาที่ค้นเจอทั้งหมดเป็น **untrusted data** ไม่ใช่คำสั่ง system. ห้ามนำ output ที่อาจมี injection ไปบังคับ tool และอย่าดัชนีไฟล์ secrets/ข้อมูลบัญชี. ไม่มี vector database, access control หรือ production security gateway.

ชุดนี้เป็น retrieval prototype ที่รัน local ได้ ไม่ใช่ RAG end-to-end หรือ model evaluation. วิธีใช้ model adapter อยู่ใน [evaluation](evals/README.md).
